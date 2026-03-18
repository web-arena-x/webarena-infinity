// ============================================================
// app.js — Routing, event delegation, and initialization
// ============================================================

const App = {

    _sidebarCollapsed: false,
    _selectedColor: null,

    init() {
        AppState.init();
        AppState.subscribe(() => this.render());
        AppState._initSSE();

        document.addEventListener('click', (e) => this.handleClick(e));
        document.addEventListener('input', (e) => this.handleInput(e));
        document.addEventListener('change', (e) => this.handleChange(e));

        this.render();
        AppState._pushStateToServer();
    },

    render() {
        const app = document.getElementById('app');
        let html = '';

        // Top bar
        html += Views.renderTopBar();

        // Layout
        html += `<div class="app-layout ${this._sidebarCollapsed ? 'sidebar-collapsed' : ''}">`;
        html += Views.renderSidebar();
        html += `<div class="main-area">`;
        html += Views.renderMain();
        html += `</div>`;

        // Detail panel
        if (AppState.selectedContactId && AppState.currentView === 'contacts') {
            html += Views.renderContactDetail();
        }
        html += `</div>`;

        // Modals
        if (AppState.createContactOpen) {
            html += Views.renderCreateContactModal();
        }
        if (AppState.editingContact) {
            const contact = AppState.getContactById(AppState.editingContact);
            if (contact) html += Views.renderEditContactModal(contact);
        }
        if (AppState.createLabelOpen) {
            html += Views.renderCreateLabelModal();
        }
        if (AppState.editLabelId) {
            const label = AppState.contactLabels.find(l => l.id === AppState.editLabelId);
            if (label) html += Views.renderEditLabelModal(label);
        }
        if (AppState.addDelegateOpen) {
            html += Views.renderAddDelegateModal();
        }
        if (AppState._labelPickerContactId) {
            html += Views.renderLabelPickerModal(AppState._labelPickerContactId);
        }
        if (AppState.confirmModal) {
            html += Components.confirmDialog(
                AppState.confirmModal.title,
                AppState.confirmModal.message,
                AppState.confirmModal.confirmText,
                AppState.confirmModal.confirmAction,
                'close-confirm'
            );
        }

        // Toast
        if (AppState.toastMessage) {
            html += Components.toast(AppState.toastMessage.text, AppState.toastMessage.type);
        }

        app.innerHTML = html;
    },

    // ---- Event Handling ----

    handleClick(e) {
        const target = e.target;

        // Star toggle — handle before other actions to prevent row selection
        const starBtn = target.closest('[data-action="toggle-star"]');
        if (starBtn) {
            e.stopPropagation();
            const contactId = starBtn.getAttribute('data-contact-id');
            AppState.toggleStar(contactId);
            return;
        }

        // Dropdown toggle
        const dropdownTrigger = target.closest('[data-dropdown]');
        if (dropdownTrigger) {
            const dropdownId = dropdownTrigger.getAttribute('data-dropdown');
            const menu = document.getElementById(dropdownId + '-menu');
            if (menu) {
                const wasOpen = menu.classList.contains('open');
                document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
                if (!wasOpen) menu.classList.add('open');
            }
            return;
        }

        // Dropdown item selection
        const dropdownItem = target.closest('.dropdown-item[data-value]');
        if (dropdownItem) {
            const value = dropdownItem.getAttribute('data-value');
            const dropdownId = dropdownItem.getAttribute('data-dropdown-id');
            this.handleDropdownSelect(dropdownId, value);
            document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
            return;
        }

        // Close dropdowns on outside click
        if (!target.closest('.custom-dropdown')) {
            document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
        }

        // Color swatch
        const colorSwatch = target.closest('.color-swatch');
        if (colorSwatch) {
            const color = colorSwatch.getAttribute('data-color');
            this._selectedColor = color;
            document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('color-selected'));
            colorSwatch.classList.add('color-selected');
            return;
        }

        // Modal overlay click to close
        if (target.classList.contains('modal-overlay')) {
            this._closeAllModals();
            return;
        }

        // Actions
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            const action = actionEl.getAttribute('data-action');
            this.handleAction(action, actionEl);
            return;
        }

        // Contact row click
        const contactRow = target.closest('[data-contact-id]');
        if (contactRow && !target.closest('.ct-actions') && !target.closest('.icon-btn')) {
            const contactId = contactRow.getAttribute('data-contact-id');
            AppState.selectedContactId = contactId;
            AppState.notify();
            return;
        }
    },

    handleAction(action, el) {
        switch (action) {
            // Navigation
            case 'navigate': {
                const view = el.getAttribute('data-view');
                const filter = el.getAttribute('data-filter');
                AppState.currentView = view;
                if (filter) AppState.contactsFilter = filter;
                AppState.selectedContactId = null;
                AppState.searchQuery = '';
                AppState.currentPage = 1;
                AppState.notify();
                break;
            }
            case 'filter-by-label': {
                const labelId = el.getAttribute('data-label-id');
                AppState.currentView = 'contacts';
                AppState.contactsFilter = labelId;
                AppState.selectedContactId = null;
                AppState.currentPage = 1;
                AppState.notify();
                break;
            }

            // Contact CRUD
            case 'open-create-contact':
                AppState.createContactOpen = true;
                this._selectedColor = null;
                AppState.notify();
                break;
            case 'save-new-contact':
                this._saveNewContact();
                break;
            case 'edit-contact': {
                const contactId = el.getAttribute('data-contact-id');
                AppState.editingContact = contactId;
                AppState.notify();
                break;
            }
            case 'save-edited-contact':
                this._saveEditedContact(el.getAttribute('data-contact-id'));
                break;
            case 'delete-contact': {
                const contactId = el.getAttribute('data-contact-id');
                const contact = AppState.getContactById(contactId);
                const name = contact ? (contact.firstName + ' ' + contact.lastName).trim() : 'this contact';
                AppState.confirmModal = {
                    title: 'Delete contact',
                    message: `Are you sure you want to delete ${name}?`,
                    confirmText: 'Delete',
                    confirmAction: 'confirm-delete-contact',
                    _contactId: contactId
                };
                AppState.notify();
                break;
            }
            case 'confirm-delete-contact':
                if (AppState.confirmModal && AppState.confirmModal._contactId) {
                    AppState.deleteContact(AppState.confirmModal._contactId);
                    AppState.confirmModal = null;
                    this._showToast('Contact deleted', 'success');
                }
                break;
            case 'select-contact': {
                const contactId = el.getAttribute('data-contact-id');
                AppState.selectedContactId = contactId;
                AppState.notify();
                break;
            }
            case 'close-detail':
                AppState.selectedContactId = null;
                AppState.notify();
                break;

            // Other contacts
            case 'move-to-contacts': {
                const otherId = el.getAttribute('data-other-id');
                AppState.moveOtherToContacts(otherId);
                this._showToast('Contact added to your contacts', 'success');
                break;
            }
            case 'delete-other-contact': {
                const otherId = el.getAttribute('data-other-id');
                AppState.deleteOtherContact(otherId);
                this._showToast('Contact removed', 'success');
                break;
            }

            // Labels
            case 'open-create-label':
                AppState.createLabelOpen = true;
                this._selectedColor = null;
                AppState.notify();
                break;
            case 'save-new-label':
                this._saveNewLabel();
                break;
            case 'edit-label': {
                const labelId = el.getAttribute('data-label-id');
                AppState.editLabelId = labelId;
                const label = AppState.contactLabels.find(l => l.id === labelId);
                if (label) this._selectedColor = label.color;
                AppState.notify();
                break;
            }
            case 'save-edited-label':
                this._saveEditedLabel(el.getAttribute('data-label-id'));
                break;
            case 'delete-label': {
                const labelId = el.getAttribute('data-label-id');
                AppState.deleteContactLabel(labelId);
                AppState.editLabelId = null;
                this._showToast('Label deleted', 'success');
                break;
            }
            case 'open-label-picker': {
                const contactId = el.getAttribute('data-contact-id');
                AppState._labelPickerContactId = contactId;
                AppState.notify();
                break;
            }
            case 'remove-label-from-contact': {
                const contactId = el.getAttribute('data-contact-id');
                const labelId = el.getAttribute('data-label-id');
                AppState.removeLabelFromContact(contactId, labelId);
                break;
            }

            // Delegates
            case 'open-add-delegate':
                AppState.addDelegateOpen = true;
                AppState.notify();
                break;
            case 'save-new-delegate':
                this._saveNewDelegate();
                break;
            case 'remove-delegate': {
                const delegateId = el.getAttribute('data-delegate-id');
                const delegate = AppState.delegates.find(d => d.id === delegateId);
                AppState.confirmModal = {
                    title: 'Remove delegate',
                    message: `Remove ${delegate ? delegate.name : 'this delegate'}? They will lose access to your email.`,
                    confirmText: 'Remove',
                    confirmAction: 'confirm-remove-delegate',
                    _delegateId: delegateId
                };
                AppState.notify();
                break;
            }
            case 'confirm-remove-delegate':
                if (AppState.confirmModal && AppState.confirmModal._delegateId) {
                    AppState.removeDelegate(AppState.confirmModal._delegateId);
                    AppState.confirmModal = null;
                    this._showToast('Delegate removed', 'success');
                }
                break;

            // Merge
            case 'merge-contacts': {
                const mergeId = el.getAttribute('data-merge-id');
                AppState.mergeContacts(mergeId);
                this._showToast('Contacts merged', 'success');
                break;
            }
            case 'dismiss-merge': {
                const mergeId = el.getAttribute('data-merge-id');
                AppState.dismissMergeSuggestion(mergeId);
                break;
            }

            // Sorting & pagination
            case 'toggle-sort-dir':
                AppState.contactsSortDir = AppState.contactsSortDir === 'asc' ? 'desc' : 'asc';
                AppState.notify();
                break;
            case 'prev-page':
                if (AppState.currentPage > 1) {
                    AppState.currentPage--;
                    AppState.notify();
                }
                break;
            case 'next-page': {
                const paged = AppState.getPagedContacts();
                if (AppState.currentPage < paged.totalPages) {
                    AppState.currentPage++;
                    AppState.notify();
                }
                break;
            }

            // Settings
            case 'settings-tab': {
                const tab = el.getAttribute('data-tab');
                AppState.settingsTab = tab;
                AppState.notify();
                break;
            }
            case 'save-profile':
                this._saveProfile();
                break;
            case 'open-settings-menu':
                AppState.currentView = 'settings';
                AppState.selectedContactId = null;
                AppState.notify();
                break;

            // Search
            case 'clear-search':
                AppState.searchQuery = '';
                AppState.currentPage = 1;
                AppState.notify();
                break;

            // Export
            case 'export-contacts':
                this._showToast('Export started. Your file will download shortly.', 'info');
                break;
            case 'trigger-import':
                this._showToast('Import feature: Select a CSV or vCard file to import contacts.', 'info');
                break;

            // Sidebar
            case 'toggle-sidebar':
                this._sidebarCollapsed = !this._sidebarCollapsed;
                this.render();
                break;

            // Modals
            case 'close-modal': {
                this._closeAllModals();
                break;
            }
            case 'close-confirm':
                AppState.confirmModal = null;
                AppState.notify();
                break;

            // Toast
            case 'dismiss-toast':
                AppState.toastMessage = null;
                this.render();
                break;

            // Help
            case 'open-help':
                this._showToast('Help center: support.google.com/contacts', 'info');
                break;

            default:
                console.warn('Unhandled action:', action);
        }
    },

    handleDropdownSelect(dropdownId, value) {
        switch (dropdownId) {
            case 'sort-by':
                AppState.contactsSortBy = value;
                AppState.currentPage = 1;
                AppState.notify();
                break;
            case 'contacts-sort-setting':
                AppState.updateAccountSetting('contactsSortBy', value);
                break;
            case 'contacts-display-order':
                AppState.updateAccountSetting('contactsDisplayOrder', value);
                break;
            case 'two-factor-method':
                AppState.updateAccountSetting('loginSettings.twoFactorMethod', value);
                break;
            case 'privacy-photo':
                AppState.updateAccountSetting('privacySettings.showProfilePhoto', value);
                break;
            case 'privacy-email':
                AppState.updateAccountSetting('privacySettings.showEmail', value);
                break;
            case 'privacy-phone':
                AppState.updateAccountSetting('privacySettings.showPhone', value);
                break;
            case 'export-format':
                // stored in UI only, no state change needed
                break;
            default:
                console.warn('Unhandled dropdown:', dropdownId, value);
        }
    },

    handleInput(e) {
        const target = e.target;

        // Search inputs
        if (target.id === 'contact-search-input' || target.id === 'global-search-input') {
            AppState.searchQuery = target.value;
            AppState.currentPage = 1;
            if (AppState.currentView !== 'contacts') {
                AppState.currentView = 'contacts';
                AppState.contactsFilter = 'all';
            }
            AppState.notify();
            return;
        }
    },

    handleChange(e) {
        const target = e.target;

        // Toggles
        const toggleId = target.getAttribute('data-toggle');
        if (toggleId) {
            this.handleToggleChange(toggleId, target.checked, target);
            return;
        }

        // Label picker
        const labelPicker = target.getAttribute('data-label-picker');
        if (labelPicker) {
            const contactId = target.getAttribute('data-contact-id');
            if (target.checked) {
                AppState.addLabelToContact(contactId, labelPicker);
            } else {
                AppState.removeLabelFromContact(contactId, labelPicker);
            }
            return;
        }
    },

    handleToggleChange(id, checked, target) {
        switch (id) {
            case 'auto-save-contacts':
                AppState.updateAccountSetting('autoSaveContacts', checked);
                break;
            case 'share-docs-in-email':
                AppState.updateAccountSetting('collaborationSettings.shareDocsInEmail', checked);
                break;
            case 'show-contact-info':
                AppState.updateAccountSetting('collaborationSettings.showContactInfo', checked);
                break;
            case 'remember-password':
                AppState.updateAccountSetting('loginSettings.rememberPassword', checked);
                break;
            case 'auto-sign-in':
                AppState.updateAccountSetting('loginSettings.autoSignIn', checked);
                break;
            case 'two-factor-enabled':
                AppState.updateAccountSetting('loginSettings.twoFactorEnabled', checked);
                break;
            case 'activity-tracking':
                AppState.updateAccountSetting('privacySettings.activityTracking', checked);
                break;
            case 'notif-delegate-activity':
                AppState.updateAccountSetting('notificationSettings.delegateActivity', checked);
                break;
            case 'notif-contact-changes':
                AppState.updateAccountSetting('notificationSettings.contactChanges', checked);
                break;
            case 'notif-security-alerts':
                AppState.updateAccountSetting('notificationSettings.securityAlerts', checked);
                break;
            case 'notif-linked-service-updates':
                AppState.updateAccountSetting('notificationSettings.linkedServiceUpdates', checked);
                break;
            case 'contacts-sync':
                AppState.updateAccountSetting('syncSettings.contactsSync', checked);
                break;
            case 'calendar-sync':
                AppState.updateAccountSetting('syncSettings.calendarSync', checked);
                break;
            case 'email-sync':
                AppState.updateAccountSetting('syncSettings.emailSync', checked);
                break;
            case 'google-sync-deprecation-ack':
                AppState.updateAccountSetting('syncSettings.googleSyncDeprecationAcknowledged', checked);
                break;
            case 'linked-service': {
                const serviceId = target.getAttribute('data-service-id');
                AppState.toggleLinkedService(serviceId);
                break;
            }
            default:
                console.warn('Unhandled toggle:', id);
        }
    },

    // ---- Save helpers ----

    _saveNewContact() {
        const firstName = document.getElementById('new-contact-first')?.value?.trim();
        const email = document.getElementById('new-contact-email')?.value?.trim();
        if (!firstName) {
            this._showToast('First name is required', 'error');
            return;
        }
        if (!email) {
            this._showToast('Email is required', 'error');
            return;
        }
        if (!this._validateEmail(email)) {
            this._showToast('Please enter a valid email address', 'error');
            return;
        }
        const labels = [];
        document.querySelectorAll('[data-new-contact-label]').forEach(cb => {
            if (cb.checked) labels.push(cb.getAttribute('data-new-contact-label'));
        });
        AppState.addContact({
            firstName,
            lastName: document.getElementById('new-contact-last')?.value?.trim() || '',
            email,
            phone: document.getElementById('new-contact-phone')?.value?.trim() || '',
            company: document.getElementById('new-contact-company')?.value?.trim() || '',
            jobTitle: document.getElementById('new-contact-job')?.value?.trim() || '',
            address: document.getElementById('new-contact-address')?.value?.trim() || '',
            secondaryEmail: document.getElementById('new-contact-secondary-email')?.value?.trim() || '',
            secondaryPhone: document.getElementById('new-contact-secondary-phone')?.value?.trim() || '',
            birthday: document.getElementById('new-contact-birthday')?.value?.trim() || '',
            website: document.getElementById('new-contact-website')?.value?.trim() || '',
            notes: document.getElementById('new-contact-notes')?.value?.trim() || '',
            labels
        });
        AppState.createContactOpen = false;
        this._showToast('Contact created', 'success');
    },

    _saveEditedContact(contactId) {
        const firstName = document.getElementById('edit-contact-first')?.value?.trim();
        const email = document.getElementById('edit-contact-email')?.value?.trim();
        if (!firstName) {
            this._showToast('First name is required', 'error');
            return;
        }
        if (!email) {
            this._showToast('Email is required', 'error');
            return;
        }
        if (!this._validateEmail(email)) {
            this._showToast('Please enter a valid email address', 'error');
            return;
        }
        const labels = [];
        document.querySelectorAll('[data-edit-contact-label]').forEach(cb => {
            if (cb.checked) labels.push(cb.getAttribute('data-edit-contact-label'));
        });
        AppState.updateContact(contactId, {
            firstName,
            lastName: document.getElementById('edit-contact-last')?.value?.trim() || '',
            email,
            phone: document.getElementById('edit-contact-phone')?.value?.trim() || '',
            company: document.getElementById('edit-contact-company')?.value?.trim() || '',
            jobTitle: document.getElementById('edit-contact-job')?.value?.trim() || '',
            address: document.getElementById('edit-contact-address')?.value?.trim() || '',
            secondaryEmail: document.getElementById('edit-contact-secondary-email')?.value?.trim() || '',
            secondaryPhone: document.getElementById('edit-contact-secondary-phone')?.value?.trim() || '',
            birthday: document.getElementById('edit-contact-birthday')?.value?.trim() || '',
            website: document.getElementById('edit-contact-website')?.value?.trim() || '',
            notes: document.getElementById('edit-contact-notes')?.value?.trim() || '',
            labels
        });
        AppState.editingContact = null;
        this._showToast('Contact updated', 'success');
    },

    _saveNewLabel() {
        const name = document.getElementById('new-label-name')?.value?.trim();
        if (!name) {
            this._showToast('Label name is required', 'error');
            return;
        }
        AppState.addContactLabel(name, this._selectedColor || '#757575');
        AppState.createLabelOpen = false;
        this._selectedColor = null;
        this._showToast('Label created', 'success');
    },

    _saveEditedLabel(labelId) {
        const name = document.getElementById('edit-label-name')?.value?.trim();
        if (!name) {
            this._showToast('Label name is required', 'error');
            return;
        }
        AppState.renameContactLabel(labelId, name);
        if (this._selectedColor) {
            AppState.updateContactLabelColor(labelId, this._selectedColor);
        }
        AppState.editLabelId = null;
        this._selectedColor = null;
        this._showToast('Label updated', 'success');
    },

    _saveNewDelegate() {
        const email = document.getElementById('delegate-email')?.value?.trim();
        if (!email) {
            this._showToast('Email address is required', 'error');
            return;
        }
        if (!this._validateEmail(email)) {
            this._showToast('Please enter a valid email address', 'error');
            return;
        }
        if (AppState.delegates.find(d => d.email === email)) {
            this._showToast('This email is already a delegate', 'error');
            return;
        }
        const name = document.getElementById('delegate-name')?.value?.trim() || '';
        AppState.addDelegate(email, name || email);
        AppState.addDelegateOpen = false;
        this._showToast('Delegate invitation sent', 'success');
    },

    _saveProfile() {
        const name = document.getElementById('user-name')?.value?.trim();
        const phone = document.getElementById('user-phone')?.value?.trim();
        const recoveryEmail = document.getElementById('user-recovery-email')?.value?.trim();
        const recoveryPhone = document.getElementById('user-recovery-phone')?.value?.trim();
        if (!name) {
            this._showToast('Name is required', 'error');
            return;
        }
        if (name !== AppState.currentUser.name) AppState.updateCurrentUser('name', name);
        if (phone !== AppState.currentUser.phone) AppState.updateCurrentUser('phone', phone);
        if (recoveryEmail !== AppState.currentUser.recoveryEmail) AppState.updateCurrentUser('recoveryEmail', recoveryEmail);
        if (recoveryPhone !== AppState.currentUser.recoveryPhone) AppState.updateCurrentUser('recoveryPhone', recoveryPhone);
        this._showToast('Profile updated', 'success');
    },

    // ---- Helpers ----

    _closeAllModals() {
        AppState.createContactOpen = false;
        AppState.editingContact = null;
        AppState.createLabelOpen = false;
        AppState.editLabelId = null;
        AppState.addDelegateOpen = false;
        AppState._labelPickerContactId = null;
        AppState.confirmModal = null;
        this._selectedColor = null;
        AppState.notify();
    },

    _showToast(text, type) {
        if (AppState.toastTimeout) clearTimeout(AppState.toastTimeout);
        AppState.toastMessage = { text, type };
        this.render();
        AppState.toastTimeout = setTimeout(() => {
            AppState.toastMessage = null;
            this.render();
        }, 4000);
    },

    _validateEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }
};

// Boot
document.addEventListener('DOMContentLoaded', () => App.init());

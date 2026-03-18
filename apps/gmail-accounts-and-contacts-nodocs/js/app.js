/* app.js — Router, event delegation & lifecycle for Gmail Accounts & Contacts */

const App = {

    init() {
        AppState.init();
        this._setupSSE();
        AppState.subscribe(() => this.render());
        this._parseRoute();
        this.render();

        window.addEventListener('hashchange', () => {
            this._parseRoute();
            this.render();
        });

        document.addEventListener('click', (e) => this._handleClick(e));
        document.addEventListener('input', (e) => this._handleInput(e));
        document.addEventListener('change', (e) => this._handleChange(e));
    },

    render() {
        const sidebar = document.getElementById('sidebarNav');
        const content = document.getElementById('contentWrapper');
        if (sidebar) sidebar.innerHTML = Views.renderSidebar();
        if (content) content.innerHTML = Views.renderContent();
    },

    navigate(route, params) {
        if (params) {
            window.location.hash = '#/' + route + '/' + params;
        } else {
            window.location.hash = '#/' + route;
        }
    },

    _parseRoute() {
        const hash = window.location.hash.replace('#/', '') || 'contacts';
        const parts = hash.split('/');
        const route = parts[0];
        const param = parts[1] || null;

        switch (route) {
            case 'contacts':
                AppState.currentView = 'contacts';
                AppState.currentContactId = null;
                break;
            case 'contact':
                AppState.currentView = 'contact-detail';
                AppState.currentContactId = param;
                break;
            case 'new-contact':
                AppState.currentView = 'new-contact';
                AppState.currentContactId = null;
                break;
            case 'edit-contact':
                AppState.currentView = 'edit-contact';
                AppState.currentContactId = param;
                break;
            case 'group':
                AppState.currentView = 'group-detail';
                AppState.currentGroupId = param;
                break;
            case 'other-contacts':
                AppState.currentView = 'other-contacts';
                break;
            case 'directory':
                AppState.currentView = 'directory';
                break;
            case 'account':
                AppState.currentView = 'account';
                break;
            case 'send-mail-as':
                AppState.currentView = 'send-mail-as';
                break;
            case 'delegation':
                AppState.currentView = 'delegation';
                break;
            case 'import-export':
                AppState.currentView = 'import-export';
                break;
            case 'merge-duplicates':
                AppState.currentView = 'merge-duplicates';
                break;
            default:
                AppState.currentView = 'contacts';
        }
    },

    _setupSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = (e) => {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
                window.location.hash = '#/contacts';
            }
        };
    },

    // ─── Event Handling ───
    _handleClick(e) {
        const target = e.target;

        // Dropdown trigger
        const ddTrigger = target.closest('[data-dropdown-trigger]');
        if (ddTrigger) {
            e.preventDefault();
            e.stopPropagation();
            const menuId = ddTrigger.dataset.dropdownTrigger + '-menu';
            this._toggleDropdown(menuId);
            return;
        }

        // Dropdown item
        const ddItem = target.closest('[data-dropdown-item]');
        if (ddItem) {
            e.preventDefault();
            this._handleDropdownSelect(ddItem);
            return;
        }

        // Route navigation
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            e.preventDefault();
            const route = routeEl.dataset.route;
            const filter = routeEl.dataset.filter;
            const id = routeEl.dataset.id;

            if (route === 'contacts' && filter) {
                if (filter !== 'all' && filter !== 'starred' && filter.startsWith('grp_')) {
                    AppState.contactFilter = filter;
                    AppState.currentView = 'contacts';
                    AppState.currentContactId = null;
                    AppState.currentPage = 1;
                    AppState.selectedContactIds = [];
                    this.navigate('contacts');
                    return;
                }
                AppState.contactFilter = filter;
                AppState.currentView = 'contacts';
                AppState.currentContactId = null;
                AppState.currentPage = 1;
                AppState.selectedContactIds = [];
                this.navigate('contacts');
                return;
            }
            if (route === 'contact-detail' && id) {
                this.navigate('contact', id);
                return;
            }
            this.navigate(route, id || undefined);
            return;
        }

        // Action dispatch
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            this._handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // Contact row click → detail
        const contactRow = target.closest('.contact-row[data-contact-id]');
        if (contactRow && !target.closest('input, button, .star-icon, [data-action]')) {
            this.navigate('contact', contactRow.dataset.contactId);
            return;
        }

        // Modal backdrop
        if (target.id === 'modalOverlay') {
            Components.closeModal();
            return;
        }

        // Close dropdowns on outside click
        this._closeAllDropdowns();
    },

    _handleInput(e) {
        const target = e.target;
        if (target.id === 'contactSearch') {
            AppState.setSearch(target.value);
        } else if (target.id === 'otherContactSearch') {
            AppState.setOtherContactSearch(target.value);
        } else if (target.id === 'directorySearch') {
            AppState.setDirectorySearch(target.value);
        }
    },

    _handleChange(e) {
        const target = e.target;

        // Radio: reply-from
        if (target.name === 'replyFrom') {
            AppState.setReplyFromSetting(target.value);
        }

        // Toggle
        if (target.dataset && target.dataset.toggle) {
            // Currently no generic toggles outside modals
        }
    },

    // ─── Action Dispatch ───
    _handleAction(action, el) {
        switch (action) {
            // Contact CRUD
            case 'new-contact':
                this.navigate('new-contact');
                break;
            case 'save-contact':
                this._saveContact(el.dataset.id);
                break;
            case 'edit-contact':
                this.navigate('edit-contact', el.dataset.id);
                break;
            case 'delete-contact':
                Components.confirmDanger('Are you sure you want to delete this contact?', () => {
                    AppState.deleteContact(el.dataset.id);
                    Components.showToast('Contact deleted', 'info');
                    this.navigate('contacts');
                });
                break;
            case 'cancel-form':
                window.history.back();
                break;
            case 'merge-duplicates':
                this.navigate('merge-duplicates');
                break;
            case 'merge-keep': {
                const keepId = el.dataset.keepId;
                const mergeId = el.dataset.mergeId;
                const result = AppState.mergeContacts(keepId, mergeId);
                if (result) {
                    Components.showToast('Contacts merged', 'success');
                } else {
                    Components.showToast('Could not merge contacts', 'error');
                }
                break;
            }
            case 'toggle-star':
                AppState.toggleContactStar(el.dataset.id);
                break;

            // Selection
            case 'toggle-select': {
                AppState.toggleContactSelection(el.dataset.id);
                break;
            }
            case 'select-all-page': {
                const contacts = AppState.getFilteredContacts();
                const page = AppState.currentPage;
                const pageSize = AppState.pageSize;
                const paged = contacts.slice((page - 1) * pageSize, page * pageSize);
                const ids = paged.map(c => c.id);
                const allSelected = ids.every(id => AppState.selectedContactIds.includes(id));
                if (allSelected) {
                    AppState.selectedContactIds = AppState.selectedContactIds.filter(id => !ids.includes(id));
                } else {
                    const newIds = ids.filter(id => !AppState.selectedContactIds.includes(id));
                    AppState.selectedContactIds = AppState.selectedContactIds.concat(newIds);
                }
                AppState.notify();
                break;
            }
            case 'clear-selection':
                AppState.clearSelection();
                break;

            // Bulk actions
            case 'bulk-delete':
                Components.confirmDanger(`Delete ${AppState.selectedContactIds.length} contacts?`, () => {
                    AppState.deleteContacts(AppState.selectedContactIds.slice());
                    Components.showToast('Contacts deleted', 'info');
                });
                break;
            case 'bulk-add-to-group':
                this._showBulkAddToGroupModal();
                break;

            // Groups
            case 'new-group':
                this._showNewGroupModal();
                break;
            case 'rename-group':
                this._showRenameGroupModal(el.dataset.id);
                break;
            case 'delete-group':
                Components.confirmDanger('Delete this label? Contacts in this label will not be deleted.', () => {
                    AppState.deleteGroup(el.dataset.id);
                    Components.showToast('Label deleted', 'info');
                    this.navigate('contacts');
                });
                break;
            case 'remove-from-group':
                AppState.removeContactFromGroup(el.dataset.contactId, el.dataset.groupId);
                Components.showToast('Contact removed from label', 'info');
                break;

            // Other contacts
            case 'promote-other':
                AppState.promoteOtherContact(el.dataset.id);
                Components.showToast('Contact added to your contacts', 'success');
                break;
            case 'delete-other':
                AppState.deleteOtherContact(el.dataset.id);
                Components.showToast('Other contact deleted', 'info');
                break;

            // Aliases
            case 'new-alias':
                this._showAliasForm();
                break;
            case 'edit-alias':
                this._showAliasForm(el.dataset.id);
                break;
            case 'delete-alias': {
                Components.confirmDanger('Remove this email address?', () => {
                    const result = AppState.deleteAlias(el.dataset.id);
                    if (result === false) {
                        Components.showToast('Cannot remove primary address', 'error');
                    } else {
                        Components.showToast('Address removed', 'info');
                    }
                });
                break;
            }
            case 'set-default-alias':
                AppState.setDefaultAlias(el.dataset.id);
                Components.showToast('Default address updated', 'success');
                break;
            case 'save-alias':
                this._saveAlias(el.dataset.id);
                break;

            // Delegates
            case 'add-delegate':
                this._showAddDelegateModal();
                break;
            case 'remove-delegate':
                Components.confirmDanger('Remove this delegate?', () => {
                    AppState.removeDelegate(el.dataset.id);
                    Components.showToast('Delegate removed', 'info');
                });
                break;
            case 'save-delegate':
                this._saveDelegate();
                break;

            // Import
            case 'add-import':
                this._showImportForm();
                break;
            case 'remove-import':
                Components.confirmDanger('Remove this mail account?', () => {
                    AppState.removeImportAccount(el.dataset.id);
                    Components.showToast('Mail account removed', 'info');
                });
                break;
            case 'save-import':
                this._saveImport();
                break;

            // Export
            case 'export-contacts':
                this._doExport();
                break;

            // Account settings
            case 'edit-name':
                this._showEditNameModal();
                break;
            case 'edit-recovery-email':
                this._showEditFieldModal('Recovery Email', 'recoveryEmail', AppState.currentUser.recoveryEmail, 'email@example.com');
                break;
            case 'edit-recovery-phone':
                this._showEditFieldModal('Recovery Phone', 'recoveryPhone', AppState.currentUser.recoveryPhone, '+1 (555) 123-4567');
                break;
            case 'change-password':
                this._showChangePasswordModal();
                break;
            case 'toggle-2sv':
                AppState.updateAccountInfo({ twoStepVerification: !AppState.currentUser.twoStepVerification });
                Components.showToast('2-Step Verification ' + (AppState.currentUser.twoStepVerification ? 'enabled' : 'disabled'), 'success');
                break;
            case 'new-app-password':
                this._showNewAppPasswordModal();
                break;
            case 'delete-app-password':
                Components.confirmDanger('Revoke this app password?', () => {
                    AppState.deleteAppPassword(el.dataset.id);
                    Components.showToast('App password revoked', 'info');
                });
                break;
            case 'save-field':
                this._saveField(el.dataset.field);
                break;
            case 'save-name':
                this._saveName();
                break;
            case 'save-password':
                this._savePassword();
                break;
            case 'save-app-password':
                this._saveAppPassword();
                break;

            // Pagination
            case 'prev-page':
                if (AppState.currentPage > 1) AppState.setPage(AppState.currentPage - 1);
                break;
            case 'next-page': {
                const totalPages = Math.ceil(AppState.getFilteredContacts().length / AppState.pageSize);
                if (AppState.currentPage < totalPages) AppState.setPage(AppState.currentPage + 1);
                break;
            }
            case 'goto-page':
                AppState.setPage(parseInt(el.dataset.page));
                break;

            // Modal
            case 'close-modal':
                Components.closeModal();
                break;
            case 'confirm-modal':
                if (Components._confirmCallback) {
                    Components._confirmCallback();
                    Components.closeModal();
                }
                break;
        }
    },

    // ─── Dropdown Management ───
    _toggleDropdown(menuId) {
        const menu = document.getElementById(menuId);
        if (!menu) return;
        const isOpen = menu.style.display !== 'none';
        this._closeAllDropdowns();
        if (!isOpen) menu.style.display = 'block';
    },

    _closeAllDropdowns() {
        document.querySelectorAll('.dropdown-menu').forEach(m => { m.style.display = 'none'; });
    },

    _handleDropdownSelect(item) {
        const ddId = item.dataset.dropdownId;
        const value = item.dataset.value;

        if (ddId === 'sortDropdown') {
            AppState.setContactSort(value);
        }

        this._closeAllDropdowns();
    },

    // ─── Save Contact ───
    _saveContact(existingId) {
        const firstName = (document.getElementById('firstName') || {}).value || '';
        const lastName = (document.getElementById('lastName') || {}).value || '';
        const email = (document.getElementById('contactEmail') || {}).value || '';
        const phone = (document.getElementById('contactPhone') || {}).value || '';
        const company = (document.getElementById('contactCompany') || {}).value || '';
        const jobTitle = (document.getElementById('contactJobTitle') || {}).value || '';
        const address = (document.getElementById('contactAddress') || {}).value || '';
        const birthday = (document.getElementById('contactBirthday') || {}).value || '';
        const notes = (document.getElementById('contactNotes') || {}).value || '';

        if (!email && !firstName && !lastName) {
            Components.showToast('Please provide at least a name or email', 'error');
            return;
        }

        // Collect groups from checkboxes
        const groups = [];
        AppState.contactGroups.forEach(g => {
            const cb = document.getElementById('group-' + g.id);
            if (cb && cb.checked) groups.push(g.id);
        });

        const data = { firstName, lastName, email, phone, company, jobTitle, address, birthday, notes, groups };

        if (existingId) {
            AppState.updateContact(existingId, data);
            Components.showToast('Contact updated', 'success');
            this.navigate('contact', existingId);
        } else {
            const c = AppState.createContact(data);
            Components.showToast('Contact created', 'success');
            this.navigate('contact', c.id);
        }
    },

    // ─── Modal Forms ───
    _showNewGroupModal() {
        Components.showModal('Create Label',
            '<div class="form-field">' + Components.textInput('newGroupName', '', 'Label name', 'Name') + '</div>',
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-new-group">Create</button>'
        );
        // Attach save handler
        const saveBtn = document.querySelector('[data-action="save-new-group"]');
        if (saveBtn) {
            saveBtn.addEventListener('click', () => {
                const name = document.getElementById('newGroupName').value.trim();
                if (!name) { Components.showToast('Name is required', 'error'); return; }
                const g = AppState.createGroup(name);
                Components.showToast('Label created', 'success');
                Components.closeModal();
            });
        }
    },

    _showRenameGroupModal(groupId) {
        const g = AppState.getGroupById(groupId);
        if (!g) return;
        Components.showModal('Rename Label',
            '<div class="form-field">' + Components.textInput('renameGroupName', g.name, 'Label name', 'Name') + '</div>',
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" id="saveRenameGroup">Rename</button>'
        );
        document.getElementById('saveRenameGroup').addEventListener('click', () => {
            const name = document.getElementById('renameGroupName').value.trim();
            if (!name) { Components.showToast('Name is required', 'error'); return; }
            AppState.renameGroup(groupId, name);
            Components.showToast('Label renamed', 'success');
            Components.closeModal();
        });
    },

    _showBulkAddToGroupModal() {
        let body = '<p>Add ' + AppState.selectedContactIds.length + ' contacts to a label:</p>';
        body += '<div class="modal-group-list">';
        AppState.contactGroups.forEach(g => {
            body += `<label class="checkbox-label"><input type="checkbox" value="${Components.escapeAttr(g.id)}" class="bulk-group-cb">${Components.escapeHtml(g.name)}</label>`;
        });
        body += '</div>';

        Components.showModal('Add to Label', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" id="saveBulkGroup">Add</button>'
        );
        document.getElementById('saveBulkGroup').addEventListener('click', () => {
            const checked = document.querySelectorAll('.bulk-group-cb:checked');
            checked.forEach(cb => {
                AppState.addContactsToGroup(AppState.selectedContactIds.slice(), cb.value);
            });
            AppState.clearSelection();
            Components.showToast('Contacts added to label(s)', 'success');
            Components.closeModal();
        });
    },

    // Alias form
    _showAliasForm(aliasId) {
        const a = aliasId ? AppState.aliases.find(al => al.id === aliasId) : null;
        const title = a ? 'Edit Email Address' : 'Add Email Address';
        let body = '<div class="form-grid">';
        body += '<div class="form-field">' + Components.textInput('aliasName', a ? a.name : '', 'Display name', 'Name') + '</div>';
        body += '<div class="form-field">' + Components.textInput('aliasEmail', a ? a.email : '', 'email@example.com', 'Email address *') + '</div>';
        body += '<div class="form-field">' + Components.textInput('aliasSmtp', a ? a.smtpServer : '', 'smtp.example.com', 'SMTP Server') + '</div>';
        body += '<div class="form-row two-col">';
        body += '<div class="form-field">' + Components.textInput('aliasPort', a ? a.smtpPort : '587', '587', 'Port') + '</div>';
        body += '<div class="form-field">' + Components.textInput('aliasUsername', a ? a.smtpUsername : '', 'username', 'Username') + '</div>';
        body += '</div>';
        body += Components.toggle('aliasSSL', a ? a.useSSL : true, 'Use SSL', 'Secure connection (recommended)');
        body += '</div>';

        Components.showModal(title, body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            `<button class="btn btn-primary" data-action="save-alias" data-id="${Components.escapeAttr(aliasId || '')}">Save</button>`
        );
    },

    _saveAlias(aliasId) {
        const name = (document.getElementById('aliasName') || {}).value || '';
        const email = (document.getElementById('aliasEmail') || {}).value || '';
        const smtpServer = (document.getElementById('aliasSmtp') || {}).value || '';
        const smtpPort = (document.getElementById('aliasPort') || {}).value || '';
        const smtpUsername = (document.getElementById('aliasUsername') || {}).value || '';
        const useSSL = document.getElementById('aliasSSL') ? document.getElementById('aliasSSL').checked : true;

        if (!email) { Components.showToast('Email is required', 'error'); return; }

        const data = { name, email, smtpServer, smtpPort, smtpUsername, useSSL };

        if (aliasId) {
            AppState.updateAlias(aliasId, data);
            Components.showToast('Address updated', 'success');
        } else {
            AppState.createAlias(data);
            Components.showToast('Address added', 'success');
        }
        Components.closeModal();
    },

    // Delegate
    _showAddDelegateModal() {
        let body = '<div class="form-grid">';
        body += '<div class="form-field">' + Components.textInput('delegateEmail', '', 'delegate@example.com', 'Email address *') + '</div>';
        body += '<div class="form-field">' + Components.textInput('delegateName', '', 'Display name', 'Name (optional)') + '</div>';
        body += '</div>';
        body += '<p class="text-muted" style="margin-top:8px">The delegate will receive an email to confirm access. Status will show as "pending" until confirmed.</p>';

        Components.showModal('Add Delegate', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-delegate">Add</button>'
        );
    },

    _saveDelegate() {
        const email = (document.getElementById('delegateEmail') || {}).value || '';
        const name = (document.getElementById('delegateName') || {}).value || '';
        if (!email) { Components.showToast('Email is required', 'error'); return; }
        AppState.addDelegate(email, name || email);
        Components.showToast('Delegate invitation sent', 'success');
        Components.closeModal();
    },

    // Import
    _showImportForm() {
        let body = '<div class="form-grid">';
        body += '<div class="form-field">' + Components.textInput('importEmail', '', 'email@example.com', 'Email address *') + '</div>';
        body += '<div class="form-field">' + Components.textInput('importServer', '', 'pop.example.com', 'POP3 Server *') + '</div>';
        body += '<div class="form-row two-col">';
        body += '<div class="form-field">' + Components.textInput('importPort', '995', '995', 'Port') + '</div>';
        body += '<div class="form-field">' + Components.textInput('importUsername', '', 'username', 'Username *') + '</div>';
        body += '</div>';
        body += '<div class="form-field">' + Components.textInput('importLabel', '', 'e.g. personal', 'Label for incoming messages') + '</div>';
        body += Components.toggle('importSSL', true, 'Use SSL', 'Secure connection');
        body += Components.toggle('importLeave', true, 'Leave a copy on the server', 'Keep messages on the original server');
        body += '</div>';

        Components.showModal('Add Mail Account', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-import">Add</button>'
        );
    },

    _saveImport() {
        const email = (document.getElementById('importEmail') || {}).value || '';
        const server = (document.getElementById('importServer') || {}).value || '';
        const port = (document.getElementById('importPort') || {}).value || '995';
        const username = (document.getElementById('importUsername') || {}).value || '';
        const labelIncoming = (document.getElementById('importLabel') || {}).value || '';
        const useSSL = document.getElementById('importSSL') ? document.getElementById('importSSL').checked : true;
        const leaveOnServer = document.getElementById('importLeave') ? document.getElementById('importLeave').checked : true;

        if (!email || !server || !username) {
            Components.showToast('Email, server, and username are required', 'error');
            return;
        }

        AppState.addImportAccount({ email, server, port, username, labelIncoming, useSSL, leaveOnServer });
        Components.showToast('Mail account added', 'success');
        Components.closeModal();
    },

    // Export
    _doExport() {
        const format = document.querySelector('input[name="exportFormat"]:checked');
        const scope = document.querySelector('input[name="exportScope"]:checked');
        if (!format || !scope) return;

        const contacts = scope.value === 'starred' ? AppState.getStarredContacts() : AppState.contacts;
        let content = '';
        let filename = '';
        let mimeType = '';

        if (format.value === 'vcard') {
            content = contacts.map(c => {
                return `BEGIN:VCARD\nVERSION:3.0\nN:${c.lastName || ''};${c.firstName || ''}\nFN:${(c.firstName + ' ' + c.lastName).trim()}\nEMAIL:${c.email || ''}\nTEL:${c.phone || ''}\nORG:${c.company || ''}\nTITLE:${c.jobTitle || ''}\nADR:;;${c.address || ''}\nNOTE:${c.notes || ''}\nEND:VCARD`;
            }).join('\n\n');
            filename = 'contacts.vcf';
            mimeType = 'text/vcard';
        } else {
            const headers = ['First Name', 'Last Name', 'Email', 'Phone', 'Company', 'Job Title', 'Address', 'Birthday', 'Notes'];
            const rows = contacts.map(c => [c.firstName, c.lastName, c.email, c.phone, c.company, c.jobTitle, c.address, c.birthday, c.notes].map(v => '"' + (v || '').replace(/"/g, '""') + '"').join(','));
            content = headers.join(',') + '\n' + rows.join('\n');
            filename = format.value === 'outlook-csv' ? 'contacts-outlook.csv' : 'contacts-google.csv';
            mimeType = 'text/csv';
        }

        const blob = new Blob([content], { type: mimeType });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = filename;
        a.click();
        Components.showToast(`Exported ${contacts.length} contacts`, 'success');
    },

    // Account settings modals
    _showEditNameModal() {
        const u = AppState.currentUser;
        let body = '<div class="form-row two-col">';
        body += '<div class="form-field">' + Components.textInput('editFirstName', u.firstName, 'First name', 'First name') + '</div>';
        body += '<div class="form-field">' + Components.textInput('editLastName', u.lastName, 'Last name', 'Last name') + '</div>';
        body += '</div>';
        Components.showModal('Edit Name', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-name">Save</button>'
        );
    },

    _saveName() {
        const firstName = (document.getElementById('editFirstName') || {}).value || '';
        const lastName = (document.getElementById('editLastName') || {}).value || '';
        if (!firstName) { Components.showToast('First name is required', 'error'); return; }
        AppState.updateAccountInfo({ firstName, lastName });
        Components.showToast('Name updated', 'success');
        Components.closeModal();
        // Update user initials in top bar
        const initialsEl = document.getElementById('userInitials');
        if (initialsEl) initialsEl.textContent = (firstName[0] || '') + (lastName[0] || '');
    },

    _showEditFieldModal(title, field, currentValue, placeholder) {
        let body = '<div class="form-field">' + Components.textInput('editFieldValue', currentValue || '', placeholder || '', title) + '</div>';
        Components.showModal('Edit ' + title, body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            `<button class="btn btn-primary" data-action="save-field" data-field="${Components.escapeAttr(field)}">Save</button>`
        );
    },

    _saveField(field) {
        const value = (document.getElementById('editFieldValue') || {}).value || '';
        const update = {};
        update[field] = value;
        AppState.updateAccountInfo(update);
        Components.showToast('Updated successfully', 'success');
        Components.closeModal();
    },

    _showChangePasswordModal() {
        let body = '<div class="form-grid">';
        body += '<div class="form-field">' + Components.textInput('currentPassword', '', 'Current password', 'Current password', 'password') + '</div>';
        body += '<div class="form-field">' + Components.textInput('newPassword', '', 'New password', 'New password', 'password') + '</div>';
        body += '<div class="form-field">' + Components.textInput('confirmPassword', '', 'Confirm password', 'Confirm new password', 'password') + '</div>';
        body += '</div>';
        Components.showModal('Change Password', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-password">Change password</button>'
        );
    },

    _savePassword() {
        const current = (document.getElementById('currentPassword') || {}).value || '';
        const newPw = (document.getElementById('newPassword') || {}).value || '';
        const confirm = (document.getElementById('confirmPassword') || {}).value || '';
        if (!current || !newPw) { Components.showToast('Please fill in all fields', 'error'); return; }
        if (newPw !== confirm) { Components.showToast('Passwords do not match', 'error'); return; }
        if (newPw.length < 8) { Components.showToast('Password must be at least 8 characters', 'error'); return; }
        AppState.updateAccountInfo({ lastPasswordChange: new Date().toISOString() });
        Components.showToast('Password changed successfully', 'success');
        Components.closeModal();
    },

    _showNewAppPasswordModal() {
        let body = '<div class="form-field">' + Components.textInput('appPasswordName', '', 'e.g., Mail on iPhone', 'App name *') + '</div>';
        body += '<p class="text-muted">This name helps you identify which app is using the password.</p>';
        Components.showModal('Generate App Password', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-app-password">Generate</button>'
        );
    },

    _saveAppPassword() {
        const name = (document.getElementById('appPasswordName') || {}).value || '';
        if (!name) { Components.showToast('App name is required', 'error'); return; }
        AppState.createAppPassword(name);
        Components.showToast('App password generated', 'success');
        Components.closeModal();
    }
};

// ─── Bootstrap ───
document.addEventListener('DOMContentLoaded', () => App.init());

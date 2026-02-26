// ============================================================
// app.js — Routing, event delegation, and initialization
// for the Gmail Organize & Manage web app
// ============================================================

const App = {
    _sseConnection: null,
    _keySequence: '',
    _keySequenceTimer: null,
    _openDropdownId: null,
    _contextMenuEmailId: null,
    _labelPickerEmailIds: [],

    // ============================================================
    // Router
    // ============================================================

    parseRoute() {
        const hash = window.location.hash || '#/inbox';
        const parts = hash.replace('#/', '').split('/');
        const view = parts[0] || 'inbox';

        // Reset transient UI state on navigation
        AppState.selectedEmailIds = new Set();
        AppState.currentPage = 1;
        AppState.searchResults = null;

        if (view === 'email' && parts[1]) {
            AppState.currentView = AppState.currentView || 'inbox';
            AppState.currentEmailId = parseInt(parts[1], 10);
        } else if (view === 'label' && parts[1]) {
            AppState.currentView = parts[1];
            AppState.currentEmailId = null;
        } else if (view === 'settings') {
            AppState.currentView = 'settings';
            AppState.settingsTab = parts[1] || 'general';
            AppState.currentEmailId = null;
        } else {
            const validViews = ['inbox', 'starred', 'snoozed', 'sent', 'drafts',
                                'important', 'allmail', 'spam', 'trash'];
            AppState.currentView = validViews.includes(view) ? view : 'inbox';
            AppState.currentEmailId = null;
        }
    },

    navigate(route) {
        window.location.hash = '#/' + route;
    },

    // ============================================================
    // Render
    // ============================================================

    render() {
        // Apply theme
        document.body.classList.remove('theme-dark', 'theme-default', 'theme-soft');
        if (AppState.settings.theme === 'dark') {
            document.body.classList.add('theme-dark');
        }

        // Apply density
        document.body.classList.remove('density-default', 'density-comfortable', 'density-compact');
        if (AppState.settings.density && AppState.settings.density !== 'default') {
            document.body.classList.add('density-' + AppState.settings.density);
        }

        // User avatar
        const avatarEl = document.getElementById('userAvatar');
        if (avatarEl && AppState.currentUser) {
            avatarEl.style.background = AppState.currentUser.avatarColor || '#1a73e8';
            const initialsEl = document.getElementById('userInitials');
            if (initialsEl) {
                initialsEl.textContent = AppState.currentUser.name
                    .split(' ').map(w => w[0]).join('').substring(0, 2).toUpperCase();
            }
        }

        // Sidebar
        const sidebarNav = document.getElementById('sidebarNav');
        if (sidebarNav && typeof Views !== 'undefined') {
            sidebarNav.innerHTML = Views.renderSidebar();
        }

        const toolbar = document.getElementById('toolbar');
        const contentWrapper = document.getElementById('contentWrapper');
        if (!contentWrapper || typeof Views === 'undefined') return;

        // Settings page — no toolbar, no email list
        if (AppState.currentView === 'settings') {
            if (toolbar) toolbar.innerHTML = '';
            contentWrapper.innerHTML = Views.renderSettings();
            return;
        }

        // Email detail view — no toolbar
        if (AppState.currentEmailId) {
            if (toolbar) toolbar.innerHTML = '';
            const email = AppState.getEmailById(AppState.currentEmailId);
            if (email) {
                if (!email.isRead) {
                    email.isRead = true;
                    AppState._recalculateLabelCounts();
                    AppState._persist();
                    AppState._pushStateToServer();
                }
                contentWrapper.innerHTML = Views.renderEmailDetail(email);
            } else {
                contentWrapper.innerHTML = Components.emptyState(
                    Components.navIcon('inbox'), 'Email not found',
                    'The email you are looking for does not exist or has been deleted.'
                );
            }
            return;
        }

        // Search results
        if (AppState.searchResults !== null) {
            if (toolbar) toolbar.innerHTML = Views.renderToolbar(AppState.currentView, AppState.searchResults);
            contentWrapper.innerHTML = Views.renderSearchResults(AppState.searchResults);
            return;
        }

        // Compute emails for the current view
        let emails;
        if (AppState.currentView === 'inbox' && AppState.settings.inboxType === 'default') {
            const catEnabled = AppState.settings.categoriesEnabled || {};
            const anyCategory = catEnabled.social || catEnabled.promotions ||
                                catEnabled.updates || catEnabled.forums;
            if (anyCategory) {
                emails = AppState.getInboxEmailsByCategory(AppState.currentCategory);
            } else {
                emails = AppState.getInboxEmails();
            }
        } else {
            emails = AppState.getEmailsForView(AppState.currentView);
        }

        const sorted = AppState.sortEmails(emails);
        const paged = AppState.getPagedEmails(sorted);

        // Toolbar (needs the full sorted list for pagination info)
        if (toolbar) {
            toolbar.innerHTML = Views.renderToolbar(AppState.currentView, sorted);
        }

        // Content
        let contentHtml = '';
        if (AppState.currentView === 'inbox' && AppState.settings.inboxType === 'default') {
            const catEnabled = AppState.settings.categoriesEnabled || {};
            const anyCategory = catEnabled.social || catEnabled.promotions ||
                                catEnabled.updates || catEnabled.forums;
            if (anyCategory) {
                contentHtml += App._renderCategoryTabs();
            }
        }
        contentHtml += Views.renderEmailList(paged.items);
        contentWrapper.innerHTML = contentHtml;
    },

    _renderCategoryTabs() {
        const catEnabled = AppState.settings.categoriesEnabled || {};
        const categories = [
            { id: 'primary', name: 'Primary', enabled: true },
            { id: 'social', name: 'Social', enabled: catEnabled.social },
            { id: 'promotions', name: 'Promotions', enabled: catEnabled.promotions },
            { id: 'updates', name: 'Updates', enabled: catEnabled.updates },
            { id: 'forums', name: 'Forums', enabled: catEnabled.forums },
        ];

        let html = '<div class="category-tabs">';
        for (const cat of categories) {
            if (!cat.enabled) continue;
            const active = AppState.currentCategory === cat.id ? ' active' : '';
            const unread = AppState.getInboxEmailsByCategory(cat.id)
                .filter(e => !e.isRead).length;
            html += `<button class="category-tab${active}" data-category="${cat.id}" data-testid="category-tab-${cat.id}">`;
            html += `<span class="category-tab-icon">${Components.categoryIcon(cat.id)}</span>`;
            html += `<span>${Components.escapeHtml(cat.name)}</span>`;
            if (unread > 0) {
                html += `<span class="category-tab-count">${unread}</span>`;
            }
            html += '</button>';
        }
        html += '</div>';
        return html;
    },

    // ============================================================
    // Event delegation — single click handler
    // ============================================================

    handleClick(e) {
        const target = e.target;

        // Close open dropdowns when clicking outside
        if (App._openDropdownId) {
            const ddMenu = document.getElementById(App._openDropdownId + '-menu');
            if (ddMenu && !ddMenu.contains(target) &&
                !target.closest(`[data-dropdown="${App._openDropdownId}"]`)) {
                ddMenu.classList.remove('open');
                App._openDropdownId = null;
            }
        }

        // Close context menu when clicking outside
        const contextMenu = document.getElementById('contextMenu');
        if (contextMenu && contextMenu.classList.contains('open') &&
            !contextMenu.contains(target)) {
            contextMenu.classList.remove('open');
        }

        // --- Checkbox on email item (before data-action to prevent interception) ---
        const emailCheckbox = target.closest('.email-checkbox');
        if (emailCheckbox) {
            const emailId = parseInt(emailCheckbox.dataset.emailId, 10);
            if (AppState.selectedEmailIds.has(emailId)) {
                AppState.selectedEmailIds.delete(emailId);
            } else {
                AppState.selectedEmailIds.add(emailId);
            }
            App.render();
            return;
        }

        // --- Star click (before data-action to prevent interception) ---
        const starEl = target.closest('.email-star');
        if (starEl) {
            e.preventDefault();
            e.stopPropagation();
            const emailId = parseInt(starEl.dataset.emailId, 10);
            if (emailId) {
                AppState.cycleStar(emailId);
            }
            return;
        }

        // --- Importance marker click (before data-action to prevent interception) ---
        const importanceEl = target.closest('.email-important');
        if (importanceEl) {
            e.preventDefault();
            e.stopPropagation();
            const emailId = parseInt(importanceEl.dataset.emailId, 10);
            if (emailId) {
                AppState.toggleImportant(emailId);
            }
            return;
        }

        // --- data-route: navigate ---
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            e.preventDefault();
            App.navigate(routeEl.dataset.route);
            return;
        }

        // --- data-action: execute action ---
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            App.handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // --- data-dropdown: toggle dropdown ---
        const dropdownEl = target.closest('[data-dropdown]');
        if (dropdownEl) {
            e.preventDefault();
            const ddId = dropdownEl.dataset.dropdown;
            App.toggleDropdown(ddId);
            return;
        }

        // --- data-category: switch inbox category ---
        const categoryEl = target.closest('[data-category]');
        if (categoryEl) {
            e.preventDefault();
            AppState.currentCategory = categoryEl.dataset.category;
            AppState.currentPage = 1;
            App.render();
            return;
        }

        // --- Dropdown item click ---
        const dropdownItem = target.closest('.dropdown-item[data-value]');
        if (dropdownItem) {
            e.preventDefault();
            const ddId = dropdownItem.dataset.dropdownId;
            const value = dropdownItem.dataset.value;
            App.handleDropdownSelect(ddId, value);
            return;
        }

        // --- Snooze option click ---
        const snoozeOption = target.closest('[data-snooze]');
        if (snoozeOption) {
            e.preventDefault();
            App.handleSnoozeSelect(snoozeOption);
            return;
        }

        // --- Color swatch click ---
        const colorSwatch = target.closest('.color-swatch');
        if (colorSwatch) {
            e.preventDefault();
            App.handleColorSelect(colorSwatch);
            return;
        }

        // --- data-email-id: open email ---
        const emailEl = target.closest('[data-email-id]');
        if (emailEl && !target.closest('.email-checkbox') && !target.closest('.email-star') &&
            !target.closest('.email-important') && !target.closest('.hover-action-btn')) {
            e.preventDefault();
            const emailId = parseInt(emailEl.dataset.emailId, 10);
            App.navigate('email/' + emailId);
            return;
        }

        // --- Settings tab click ---
        const settingsTab = target.closest('.settings-tab[data-settings-tab]');
        if (settingsTab) {
            e.preventDefault();
            AppState.settingsTab = settingsTab.dataset.settingsTab;
            App.render();
            return;
        }

        // --- Toggle switch in settings ---
        const toggleSwitch = target.closest('.toggle-switch input');
        if (toggleSwitch) {
            App.handleToggleChange(toggleSwitch);
            return;
        }

        // --- Radio button in settings ---
        const radioInput = target.closest('.radio-option input[type="radio"]');
        if (radioInput) {
            App.handleRadioChange(radioInput);
            return;
        }

        // --- Context menu item ---
        const contextItem = target.closest('.context-menu-item[data-context-action]');
        if (contextItem) {
            e.preventDefault();
            App.handleContextAction(contextItem.dataset.contextAction);
            return;
        }

        // --- Close modal ---
        const modalOverlay = target.closest('.modal-overlay');
        if (modalOverlay && target === modalOverlay) {
            Components.closeModal();
            return;
        }

        // --- Label picker checkbox ---
        const labelPickerItem = target.closest('.label-picker-item');
        if (labelPickerItem) {
            const checkbox = labelPickerItem.querySelector('input[type="checkbox"]');
            const labelId = labelPickerItem.dataset.labelId;
            if (checkbox && labelId) {
                // Toggle checkbox if the click was on the row, not the checkbox itself
                if (target !== checkbox) {
                    checkbox.checked = !checkbox.checked;
                }
                const isChecked = checkbox.checked;
                const emailIds = App._labelPickerEmailIds.length > 0
                    ? App._labelPickerEmailIds
                    : Array.from(AppState.selectedEmailIds);
                if (emailIds.length === 0 && AppState.currentEmailId) {
                    emailIds.push(AppState.currentEmailId);
                }
                if (isChecked) {
                    AppState.addLabel(emailIds, labelId);
                } else {
                    AppState.removeLabel(emailIds, labelId);
                }
            }
            return;
        }

        // --- Filter list item actions ---
        const filterAction = target.closest('[data-filter-action]');
        if (filterAction) {
            e.preventDefault();
            const action = filterAction.dataset.filterAction;
            const filterId = filterAction.dataset.filterId;
            if (action === 'edit') {
                App.showFilterDialog(filterId);
            } else if (action === 'delete') {
                Components.confirmDanger('Delete Filter', 'Are you sure you want to delete this filter?', 'Delete', () => {
                    AppState.deleteFilter(filterId);
                });
            }
            return;
        }
    },

    // ============================================================
    // Action handlers
    // ============================================================

    handleAction(action, el) {
        const selectedIds = Array.from(AppState.selectedEmailIds);
        const currentId = AppState.currentEmailId;

        switch (action) {
            // ---- Selection ----
            case 'select-all': {
                const emails = App._getVisibleEmails();
                for (const email of emails) {
                    AppState.selectedEmailIds.add(email.id);
                }
                App.render();
                break;
            }
            case 'deselect-all':
                AppState.selectedEmailIds = new Set();
                App.render();
                break;

            case 'select-all-checkbox': {
                const checkboxEl = el.querySelector('input') || el;
                if (AppState.selectedEmailIds.size > 0) {
                    AppState.selectedEmailIds = new Set();
                } else {
                    const emails = App._getVisibleEmails();
                    for (const email of emails) {
                        AppState.selectedEmailIds.add(email.id);
                    }
                }
                App.render();
                break;
            }

            // ---- Archive ----
            case 'archive-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.archiveEmails(ids);
                AppState.selectedEmailIds = new Set();
                if (currentId) {
                    App._advanceAfterAction();
                }
                Components.showToast(`${ids.length} conversation(s) archived`, 'Undo', () => {
                    AppState.moveToInbox(ids);
                });
                break;
            }

            // ---- Delete / Trash ----
            case 'delete-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.trashEmails(ids);
                AppState.selectedEmailIds = new Set();
                if (currentId) {
                    App._advanceAfterAction();
                }
                Components.showToast(`${ids.length} conversation(s) moved to Trash`, 'Undo', () => {
                    AppState.moveToInbox(ids);
                });
                break;
            }

            case 'delete-forever': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                Components.confirmDanger(
                    'Delete forever',
                    `Are you sure you want to permanently delete ${ids.length} conversation(s)? This action cannot be undone.`,
                    'Delete forever',
                    () => {
                        AppState.deleteForever(ids);
                        AppState.selectedEmailIds = new Set();
                        if (currentId) {
                            App._advanceAfterAction();
                        }
                        Components.showToast(`${ids.length} conversation(s) permanently deleted`);
                    }
                );
                break;
            }

            case 'empty-trash':
                Components.confirmDanger(
                    'Empty Trash',
                    'All messages in Trash will be permanently deleted. This action cannot be undone.',
                    'Empty Trash now',
                    () => {
                        AppState.emptyTrash();
                        Components.showToast('Trash has been emptied');
                    }
                );
                break;

            // ---- Mark read/unread ----
            case 'mark-read-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.markAsRead(ids);
                AppState.selectedEmailIds = new Set();
                Components.showToast(`${ids.length} conversation(s) marked as read`);
                break;
            }

            case 'mark-unread-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.markAsUnread(ids);
                AppState.selectedEmailIds = new Set();
                Components.showToast(`${ids.length} conversation(s) marked as unread`);
                break;
            }

            // ---- Spam ----
            case 'spam-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.markAsSpam(ids);
                AppState.selectedEmailIds = new Set();
                if (currentId) {
                    App._advanceAfterAction();
                }
                Components.showToast(`${ids.length} conversation(s) marked as spam`, 'Undo', () => {
                    AppState.unmarkSpam(ids);
                });
                break;
            }

            case 'not-spam-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.unmarkSpam(ids);
                AppState.selectedEmailIds = new Set();
                Components.showToast(`${ids.length} conversation(s) marked as not spam`);
                break;
            }

            // ---- Move to inbox ----
            case 'move-to-inbox-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.moveToInbox(ids);
                AppState.selectedEmailIds = new Set();
                Components.showToast(`${ids.length} conversation(s) moved to Inbox`);
                break;
            }

            // ---- Star ----
            case 'star-email': {
                const emailId = parseInt(el.dataset.emailId, 10);
                if (emailId) AppState.cycleStar(emailId);
                break;
            }

            // ---- Important ----
            case 'toggle-important': {
                const emailId = parseInt(el.dataset.emailId, 10) || currentId;
                if (emailId) AppState.toggleImportant(emailId);
                break;
            }

            // ---- Snooze / Unsnooze ----
            case 'unsnooze-email': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.unsnoozeEmails(ids);
                AppState.selectedEmailIds = new Set();
                if (AppState.currentEmailId) App._advanceAfterAction();
                Components.showToast('Conversation moved to Inbox');
                break;
            }

            case 'snooze-email': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                App._snoozeTargetIds = ids;
                const body = Components.snoozePicker();
                Components.showModal('Snooze', body, '');
                break;
            }

            // ---- Label ----
            case 'label-email': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                App.showLabelPicker(ids);
                break;
            }

            // ---- Move to ----
            case 'move-to': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                App.showMoveToPicker(ids);
                break;
            }

            // ---- Mute ----
            case 'mute-email': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length === 0) return;
                AppState.muteEmails(ids);
                AppState.selectedEmailIds = new Set();
                if (currentId) {
                    App._advanceAfterAction();
                }
                Components.showToast(`Conversation muted`, 'Undo', () => {
                    // Un-mute is essentially moving back to inbox
                    for (const id of ids) {
                        const email = AppState.getEmailById(id);
                        if (email) {
                            email.isMuted = false;
                            email.isArchived = false;
                            if (!email.labels.includes('INBOX')) email.labels.push('INBOX');
                        }
                    }
                    AppState._recalculateLabelCounts();
                    AppState.notify();
                });
                break;
            }

            // ---- Compose ----
            case 'compose':
                App.openCompose();
                break;

            case 'send-email':
                App.sendEmail();
                break;

            case 'close-compose': {
                const composeTo = document.getElementById('composeTo');
                const composeSubject = document.getElementById('composeSubject');
                const composeBody = document.getElementById('composeBody');
                const hasContent = (composeTo && composeTo.value.trim()) ||
                                   (composeSubject && composeSubject.value.trim()) ||
                                   (composeBody && composeBody.value.trim());
                if (hasContent) {
                    // Auto-save as draft
                    AppState.saveDraft(
                        composeTo ? composeTo.value : '',
                        '', '',
                        composeSubject ? composeSubject.value : '',
                        composeBody ? composeBody.value : ''
                    );
                    Components.showToast('Draft saved');
                }
                App.closeCompose();
                break;
            }

            case 'minimize-compose': {
                const composeModal = document.getElementById('composeModal');
                if (composeModal) {
                    const modalContent = composeModal.querySelector('.compose-modal');
                    if (modalContent) {
                        modalContent.classList.toggle('minimized');
                    }
                }
                break;
            }

            case 'show-cc': {
                const ccField = document.getElementById('composeCcField');
                if (ccField) ccField.style.display = 'flex';
                const ccBtn = document.getElementById('showCcBtn');
                if (ccBtn) ccBtn.style.display = 'none';
                break;
            }

            case 'show-bcc': {
                const bccField = document.getElementById('composeBccField');
                if (bccField) bccField.style.display = 'flex';
                const bccBtn = document.getElementById('showBccBtn');
                if (bccBtn) bccBtn.style.display = 'none';
                break;
            }

            case 'discard-draft': {
                App.closeCompose();
                Components.showToast('Draft discarded');
                break;
            }

            // ---- Reply / Forward ----
            case 'reply': {
                const email = currentId ? AppState.getEmailById(currentId) : null;
                if (email) {
                    App.openCompose({
                        to: email.from.email,
                        subject: 'Re: ' + email.subject.replace(/^Re:\s*/i, ''),
                        body: '\n\n--- Original Message ---\nFrom: ' + email.from.name +
                              ' <' + email.from.email + '>\nDate: ' +
                              Components.formatFullDate(email.date) + '\n\n' + (email.body || email.snippet)
                    });
                }
                break;
            }

            case 'reply-all': {
                const email = currentId ? AppState.getEmailById(currentId) : null;
                if (email) {
                    const allRecipients = [email.from.email];
                    if (email.to) {
                        for (const r of email.to) {
                            if (r.email !== AppState.currentUser.email) allRecipients.push(r.email);
                        }
                    }
                    if (email.cc) {
                        for (const r of email.cc) {
                            if (r.email !== AppState.currentUser.email) allRecipients.push(r.email);
                        }
                    }
                    App.openCompose({
                        to: allRecipients.join(', '),
                        subject: 'Re: ' + email.subject.replace(/^Re:\s*/i, ''),
                        body: '\n\n--- Original Message ---\nFrom: ' + email.from.name +
                              ' <' + email.from.email + '>\nDate: ' +
                              Components.formatFullDate(email.date) + '\n\n' + (email.body || email.snippet)
                    });
                }
                break;
            }

            case 'forward': {
                const email = currentId ? AppState.getEmailById(currentId) : null;
                if (email) {
                    App.openCompose({
                        to: '',
                        subject: 'Fwd: ' + email.subject.replace(/^Fwd:\s*/i, ''),
                        body: '\n\n--- Forwarded Message ---\nFrom: ' + email.from.name +
                              ' <' + email.from.email + '>\nDate: ' +
                              Components.formatFullDate(email.date) + '\nSubject: ' +
                              email.subject + '\n\n' + (email.body || email.snippet)
                    });
                }
                break;
            }

            // ---- Settings ----
            case 'open-settings':
                App.navigate('settings');
                break;

            case 'close-settings':
                App.navigate(AppState.currentView === 'settings' ? 'inbox' : AppState.currentView);
                break;

            // ---- Quick settings panel ----
            case 'open-quick-settings': {
                const settingsPanel = document.getElementById('settingsPanel');
                if (settingsPanel) {
                    if (settingsPanel.style.display === 'none') {
                        settingsPanel.style.display = 'block';
                        settingsPanel.innerHTML = Views.renderQuickSettings ? Views.renderQuickSettings() : '';
                    } else {
                        settingsPanel.style.display = 'none';
                    }
                }
                break;
            }

            case 'close-quick-settings': {
                const settingsPanel = document.getElementById('settingsPanel');
                if (settingsPanel) settingsPanel.style.display = 'none';
                break;
            }

            // ---- Labels ----
            case 'create-label':
                App.showCreateLabelDialog();
                break;

            case 'edit-label': {
                const labelId = el.dataset.labelId;
                if (labelId) App.showEditLabelDialog(labelId);
                break;
            }

            case 'delete-label': {
                const labelId = el.dataset.labelId;
                if (!labelId) return;
                const label = AppState.getLabelById(labelId);
                Components.confirmDanger(
                    'Delete Label',
                    `Are you sure you want to delete the label "${label ? label.name : labelId}"? Emails with this label will not be deleted.`,
                    'Delete',
                    () => {
                        AppState.deleteLabel(labelId);
                        Components.showToast('Label deleted');
                    }
                );
                break;
            }

            // ---- Filters ----
            case 'create-filter':
                App.showFilterDialog(null);
                break;

            case 'edit-filter': {
                const filterId = el.dataset.filterId;
                if (filterId) App.showFilterDialog(filterId);
                break;
            }

            case 'delete-filter': {
                const filterId = el.dataset.filterId;
                if (!filterId) return;
                Components.confirmDanger(
                    'Delete Filter',
                    'Are you sure you want to delete this filter?',
                    'Delete',
                    () => {
                        AppState.deleteFilter(filterId);
                        Components.showToast('Filter deleted');
                    }
                );
                break;
            }

            // ---- Block / Unblock ----
            case 'block-sender': {
                const senderEmail = el.dataset.senderEmail;
                if (senderEmail) {
                    AppState.blockSender(senderEmail);
                    Components.showToast(`Blocked ${senderEmail}`);
                }
                break;
            }

            case 'unblock-sender': {
                const senderEmail = el.dataset.senderEmail;
                if (senderEmail) {
                    AppState.unblockSender(senderEmail);
                    Components.showToast(`Unblocked ${senderEmail}`);
                }
                break;
            }

            // ---- Settings changes ----
            case 'set-theme': {
                const theme = el.dataset.value;
                AppState.updateSetting('theme', theme);
                break;
            }

            case 'set-inbox-type': {
                const inboxType = el.dataset.value;
                AppState.updateSetting('inboxType', inboxType);
                break;
            }

            case 'set-density': {
                const density = el.dataset.value;
                AppState.updateSetting('density', density);
                break;
            }

            case 'set-conversation-view': {
                const enabled = el.dataset.value === 'true';
                AppState.updateSetting('conversationView', enabled);
                break;
            }

            case 'set-preview-pane': {
                const pane = el.dataset.value;
                AppState.updateSetting('previewPane', pane);
                break;
            }

            case 'toggle-category': {
                const cat = el.dataset.category;
                const key = 'categoriesEnabled.' + cat;
                const current = AppState.settings.categoriesEnabled[cat];
                AppState.updateSetting(key, !current);
                break;
            }

            case 'set-undo-send-delay': {
                const delay = parseInt(el.dataset.value, 10);
                AppState.updateSetting('undoSendDelay', delay);
                break;
            }

            case 'set-default-reply-behavior': {
                const behavior = el.dataset.value;
                AppState.updateSetting('defaultReplyBehavior', behavior);
                break;
            }

            case 'set-send-and-archive': {
                const enabled = el.dataset.value === 'true';
                AppState.updateSetting('sendAndArchive', enabled);
                break;
            }

            case 'set-max-page-size': {
                const size = parseInt(el.dataset.value, 10);
                AppState.updateSetting('maxPageSize', size);
                break;
            }

            case 'set-auto-advance': {
                const mode = el.dataset.value;
                AppState.updateSetting('autoAdvance', mode);
                break;
            }

            case 'set-button-labels': {
                const mode = el.dataset.value;
                AppState.updateSetting('buttonLabels', mode);
                break;
            }

            case 'toggle-keyboard-shortcuts': {
                const enabled = !AppState.settings.keyboardShortcutsEnabled;
                AppState.updateSetting('keyboardShortcutsEnabled', enabled);
                break;
            }

            case 'toggle-importance-markers': {
                const enabled = !AppState.settings.importanceMarkers;
                AppState.updateSetting('importanceMarkers', enabled);
                break;
            }

            case 'toggle-hover-actions': {
                const enabled = !AppState.settings.hoverActions;
                AppState.updateSetting('hoverActions', enabled);
                break;
            }

            case 'toggle-nudges-reply': {
                const enabled = !AppState.settings.nudges.suggestEmailsToReply;
                AppState.updateSetting('nudges.suggestEmailsToReply', enabled);
                break;
            }

            case 'toggle-nudges-followup': {
                const enabled = !AppState.settings.nudges.suggestEmailsToFollowUp;
                AppState.updateSetting('nudges.suggestEmailsToFollowUp', enabled);
                break;
            }

            case 'toggle-dynamic-email': {
                const enabled = !AppState.settings.dynamicEmail;
                AppState.updateSetting('dynamicEmail', enabled);
                break;
            }

            // ---- Pagination ----
            case 'prev-page':
                if (AppState.currentPage > 1) {
                    AppState.currentPage--;
                    App.render();
                }
                break;

            case 'next-page': {
                const emails = App._getVisibleEmails();
                const paged = AppState.getPagedEmails(emails);
                if (paged.hasNext) {
                    AppState.currentPage++;
                    App.render();
                }
                break;
            }

            // ---- Refresh ----
            case 'refresh':
                App.render();
                Components.showToast('Mail refreshed');
                break;

            // ---- More menu actions ----
            case 'more-menu': {
                App.showMoreMenu(el);
                break;
            }

            // ---- Search ----
            case 'search': {
                const input = document.getElementById('searchInput');
                if (input && input.value.trim()) {
                    AppState.searchQuery = input.value.trim();
                    AppState.searchResults = AppState.searchEmails(input.value.trim());
                    AppState.currentEmailId = null;
                    AppState.currentPage = 1;
                    App.render();
                }
                break;
            }

            case 'clear-search':
                AppState.searchQuery = '';
                AppState.searchResults = null;
                const searchInput = document.getElementById('searchInput');
                if (searchInput) searchInput.value = '';
                App.render();
                break;

            // ---- Toggle sidebar ----
            case 'toggle-sidebar':
                document.body.classList.toggle('sidebar-collapsed');
                break;

            // ---- Toggle labels section ----
            case 'toggle-labels':
                AppState.expandedLabels = !AppState.expandedLabels;
                App.render();
                break;

            // ---- Close modal ----
            case 'close-modal':
                Components.closeModal();
                break;

            // ---- Move to category ----
            case 'move-to-category': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                const category = el.dataset.category;
                if (ids.length > 0 && category) {
                    AppState.moveToCategory(ids, category);
                    AppState.selectedEmailIds = new Set();
                    Components.showToast(`Moved to ${category}`);
                }
                break;
            }

            // ---- Back to list from email detail ----
            case 'back-to-list':
                AppState.currentEmailId = null;
                App.navigate(AppState.currentView);
                break;

            // ---- Reset data ----
            case 'reset-data':
                Components.confirmDanger(
                    'Reset All Data',
                    'This will reset all emails, labels, filters, and settings to their original state. This cannot be undone.',
                    'Reset Everything',
                    () => {
                        AppState.resetToSeedData();
                        App.navigate('inbox');
                        Components.showToast('All data has been reset');
                    }
                );
                break;

            // ---- Save settings (full settings page) ----
            case 'save-settings':
                App.saveSettingsFromForm();
                Components.showToast('Settings saved');
                break;

            // ---- Cancel settings ----
            case 'cancel-settings':
                App.navigate('inbox');
                break;

            // ---- Empty spam ----
            case 'empty-spam':
                Components.confirmDanger(
                    'Empty Spam',
                    'All messages in Spam will be permanently deleted. This action cannot be undone.',
                    'Empty Spam now',
                    () => {
                        AppState.emptySpam();
                        Components.showToast('Spam has been emptied');
                    }
                );
                break;

            // ---- Single-email actions (hover buttons / email detail toolbar) ----
            case 'archive-email': {
                const emailId = parseInt(el.dataset.emailId, 10) || currentId;
                if (emailId) {
                    AppState.archiveEmails([emailId]);
                    App._advanceAfterAction();
                    Components.showToast('Conversation archived', 'Undo', () => {
                        AppState.moveToInbox([emailId]);
                    });
                }
                break;
            }

            case 'delete-email': {
                const emailId = parseInt(el.dataset.emailId, 10) || currentId;
                if (emailId) {
                    AppState.trashEmails([emailId]);
                    App._advanceAfterAction();
                    Components.showToast('Conversation moved to Trash', 'Undo', () => {
                        AppState.moveToInbox([emailId]);
                    });
                }
                break;
            }

            case 'spam-email': {
                const emailId = parseInt(el.dataset.emailId, 10) || currentId;
                if (emailId) {
                    AppState.markAsSpam([emailId]);
                    App._advanceAfterAction();
                    Components.showToast('Conversation marked as spam', 'Undo', () => {
                        AppState.unmarkSpam([emailId]);
                    });
                }
                break;
            }

            case 'mark-read-email': {
                const emailId = parseInt(el.dataset.emailId, 10) || currentId;
                if (emailId) {
                    AppState.markAsRead([emailId]);
                    Components.showToast('Conversation marked as read');
                }
                break;
            }

            case 'mark-unread-email': {
                const emailId = parseInt(el.dataset.emailId, 10) || currentId;
                if (emailId) {
                    AppState.markAsUnread([emailId]);
                    Components.showToast('Conversation marked as unread');
                }
                break;
            }

            // ---- Toolbar aliases ----
            case 'label-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length > 0) App.showLabelPicker(ids);
                break;
            }

            case 'move-to-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length > 0) App.showMoveToPicker(ids);
                break;
            }

            case 'more-actions': {
                App.showMoreMenu(el);
                break;
            }

            // ---- Context menu / More menu items ----
            case 'mark-important-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                for (const id of ids) {
                    const email = AppState.getEmailById(id);
                    if (email && !email.isImportant) AppState.toggleImportant(id);
                }
                break;
            }

            case 'mark-not-important-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                for (const id of ids) {
                    const email = AppState.getEmailById(id);
                    if (email && email.isImportant) AppState.toggleImportant(id);
                }
                break;
            }

            case 'mute-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                if (ids.length > 0) {
                    AppState.muteEmails(ids);
                    AppState.selectedEmailIds = new Set();
                    Components.showToast('Conversation muted');
                }
                break;
            }

            case 'unmute-selected': {
                const ids = selectedIds.length > 0 ? selectedIds : (currentId ? [currentId] : []);
                for (const id of ids) {
                    const email = AppState.getEmailById(id);
                    if (email) {
                        email.isMuted = false;
                        email.isArchived = false;
                        if (!email.labels.includes('INBOX')) email.labels.push('INBOX');
                    }
                }
                AppState._recalculateLabelCounts();
                AppState.selectedEmailIds = new Set();
                AppState.notify();
                Components.showToast('Conversation unmuted');
                break;
            }

            // ---- Expand message ----
            case 'expand-message': {
                const msgCard = el.closest('.message-card');
                if (msgCard) {
                    msgCard.classList.toggle('collapsed');
                }
                break;
            }

            default:
                console.warn('Unknown action:', action);
        }
    },

    // ============================================================
    // Dropdown handling
    // ============================================================

    toggleDropdown(id) {
        // Close previously open dropdown
        if (App._openDropdownId && App._openDropdownId !== id) {
            const prevMenu = document.getElementById(App._openDropdownId + '-menu');
            if (prevMenu) prevMenu.classList.remove('open');
        }

        const menu = document.getElementById(id + '-menu');
        if (menu) {
            const isOpen = menu.classList.contains('open');
            menu.classList.toggle('open');
            App._openDropdownId = isOpen ? null : id;
        }
    },

    handleDropdownSelect(ddId, value) {
        const menu = document.getElementById(ddId + '-menu');
        if (menu) menu.classList.remove('open');
        App._openDropdownId = null;

        // Map dropdown IDs to settings
        const settingsMap = {
            'theme-dropdown': 'theme',
            'density-dropdown': 'density',
            'inbox-type-dropdown': 'inboxType',
            'preview-pane-dropdown': 'previewPane',
            'undo-send-dropdown': 'undoSendDelay',
            'page-size-dropdown': 'maxPageSize',
            'auto-advance-dropdown': 'autoAdvance',
            'button-labels-dropdown': 'buttonLabels',
            'reply-behavior-dropdown': 'defaultReplyBehavior',
            'language-dropdown': 'language',
            'desktop-notifications-dropdown': 'desktopNotifications',
        };

        const settingKey = settingsMap[ddId];
        if (settingKey) {
            let parsedValue = value;
            if (settingKey === 'undoSendDelay' || settingKey === 'maxPageSize') {
                parsedValue = parseInt(value, 10);
            }
            AppState.updateSetting(settingKey, parsedValue);
            return;
        }

        // Selection dropdown in toolbar
        if (ddId === 'select-dropdown') {
            const emails = App._getVisibleEmails();
            switch (value) {
                case 'all':
                    for (const e of emails) AppState.selectedEmailIds.add(e.id);
                    break;
                case 'none':
                    AppState.selectedEmailIds = new Set();
                    break;
                case 'read':
                    AppState.selectedEmailIds = new Set();
                    for (const e of emails) { if (e.isRead) AppState.selectedEmailIds.add(e.id); }
                    break;
                case 'unread':
                    AppState.selectedEmailIds = new Set();
                    for (const e of emails) { if (!e.isRead) AppState.selectedEmailIds.add(e.id); }
                    break;
                case 'starred':
                    AppState.selectedEmailIds = new Set();
                    for (const e of emails) { if (e.isStarred) AppState.selectedEmailIds.add(e.id); }
                    break;
                case 'unstarred':
                    AppState.selectedEmailIds = new Set();
                    for (const e of emails) { if (!e.isStarred) AppState.selectedEmailIds.add(e.id); }
                    break;
            }
            App.render();
            return;
        }

        // Multiple inbox section editing
        if (ddId && ddId.startsWith('multi-inbox-position')) {
            AppState.updateSetting('multipleInboxPosition', value);
            return;
        }
    },

    // ============================================================
    // Snooze handling
    // ============================================================

    handleSnoozeSelect(el) {
        const snoozeType = el.dataset.snooze;
        const ids = App._snoozeTargetIds || [];

        if (snoozeType === 'pick_date') {
            // Show custom date picker in modal
            const body = `
                <div class="form-group">
                    <label class="form-label">Date</label>
                    <input type="date" class="form-input" id="snoozeDateInput">
                </div>
                <div class="form-group">
                    <label class="form-label">Time</label>
                    <input type="time" class="form-input" id="snoozeTimeInput" value="08:00">
                </div>
            `;
            const footer = `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" id="snoozeConfirmBtn">Snooze</button>
            `;
            Components.showModal('Pick date & time', body, footer);
            document.getElementById('snoozeConfirmBtn').onclick = () => {
                const dateVal = document.getElementById('snoozeDateInput').value;
                const timeVal = document.getElementById('snoozeTimeInput').value;
                if (dateVal) {
                    const snoozeDate = new Date(dateVal + 'T' + (timeVal || '08:00') + ':00');
                    AppState.snoozeEmails(ids, snoozeDate.toISOString());
                    AppState.selectedEmailIds = new Set();
                    if (AppState.currentEmailId) App._advanceAfterAction();
                    Components.closeModal();
                    Components.showToast('Snoozed until ' + Components.formatDateTime(snoozeDate.toISOString()));
                }
            };
            return;
        }

        const snoozeDate = el.dataset.snoozeDate;
        if (snoozeDate && ids.length > 0) {
            AppState.snoozeEmails(ids, snoozeDate);
            AppState.selectedEmailIds = new Set();
            if (AppState.currentEmailId) App._advanceAfterAction();
            Components.closeModal();
            Components.showToast('Snoozed until ' + Components.formatDateTime(snoozeDate), 'Undo', () => {
                AppState.unsnoozeEmails(ids);
            });
        }
    },

    // ============================================================
    // Color select handling
    // ============================================================

    handleColorSelect(swatch) {
        const bg = swatch.dataset.colorBg;
        const fg = swatch.dataset.colorFg;

        // Store selected color for later use by label dialog
        App._selectedColor = bg ? { background: bg, text: fg } : null;

        // Update UI to show selection
        const allSwatches = swatch.parentElement.querySelectorAll('.color-swatch');
        for (const s of allSwatches) {
            s.style.border = '';
        }
        if (bg) {
            swatch.style.border = '2px solid var(--color-primary)';
        }
    },

    // ============================================================
    // Toggle / Radio handlers for settings forms
    // ============================================================

    handleToggleChange(input) {
        const id = input.id;
        const checked = input.checked;

        const toggleMap = {
            'setting-keyboard-shortcuts': 'keyboardShortcutsEnabled',
            'setting-importance-markers': 'importanceMarkers',
            'setting-hover-actions': 'hoverActions',
            'setting-dynamic-email': 'dynamicEmail',
            'setting-send-archive': 'sendAndArchive',
            'setting-nudge-reply': 'nudges.suggestEmailsToReply',
            'setting-nudge-followup': 'nudges.suggestEmailsToFollowUp',
            'setting-conversation-view': 'conversationView',
            'setting-cat-social': 'categoriesEnabled.social',
            'setting-cat-promotions': 'categoriesEnabled.promotions',
            'setting-cat-updates': 'categoriesEnabled.updates',
            'setting-cat-forums': 'categoriesEnabled.forums',
        };

        const settingKey = toggleMap[id];
        if (settingKey) {
            AppState.updateSetting(settingKey, checked);
        }
    },

    handleRadioChange(input) {
        const name = input.name;
        const value = input.value;

        const radioMap = {
            'theme': 'theme',
            'density': 'density',
            'inbox-type': 'inboxType',
            'preview-pane': 'previewPane',
            'undo-send-delay': 'undoSendDelay',
            'auto-advance': 'autoAdvance',
            'button-labels': 'buttonLabels',
            'reply-behavior': 'defaultReplyBehavior',
            'desktop-notifications': 'desktopNotifications',
            'conversationView': 'conversationView',
            'sendAndArchive': 'sendAndArchive',
            'hoverActions': 'hoverActions',
            'multipleInboxPosition': 'multipleInboxPosition',
        };

        const booleanRadios = ['conversationView', 'sendAndArchive', 'hoverActions'];

        const settingKey = radioMap[name];
        if (settingKey) {
            let parsedValue = value;
            if (settingKey === 'undoSendDelay') parsedValue = parseInt(value, 10);
            if (booleanRadios.includes(settingKey)) parsedValue = (value === 'on');
            AppState.updateSetting(settingKey, parsedValue);
        }
    },

    // ============================================================
    // Compose
    // ============================================================

    openCompose(prefill) {
        const modal = document.getElementById('composeModal');
        if (!modal) return;
        modal.style.display = 'block';

        // Reset fields
        const toEl = document.getElementById('composeTo');
        const ccEl = document.getElementById('composeCc');
        const bccEl = document.getElementById('composeBcc');
        const subjectEl = document.getElementById('composeSubject');
        const bodyEl = document.getElementById('composeBody');
        const ccField = document.getElementById('composeCcField');
        const bccField = document.getElementById('composeBccField');
        const ccBtn = document.getElementById('showCcBtn');
        const bccBtn = document.getElementById('showBccBtn');

        if (toEl) toEl.value = prefill ? (prefill.to || '') : '';
        if (ccEl) ccEl.value = prefill ? (prefill.cc || '') : '';
        if (bccEl) bccEl.value = prefill ? (prefill.bcc || '') : '';
        if (subjectEl) subjectEl.value = prefill ? (prefill.subject || '') : '';
        if (bodyEl) bodyEl.value = prefill ? (prefill.body || '') : '';
        if (ccField) ccField.style.display = (prefill && prefill.cc) ? 'flex' : 'none';
        if (bccField) bccField.style.display = (prefill && prefill.bcc) ? 'flex' : 'none';
        if (ccBtn) ccBtn.style.display = (prefill && prefill.cc) ? 'none' : '';
        if (bccBtn) bccBtn.style.display = (prefill && prefill.bcc) ? 'none' : '';

        // Focus the To field
        if (toEl) setTimeout(() => toEl.focus(), 100);
    },

    closeCompose() {
        const modal = document.getElementById('composeModal');
        if (modal) modal.style.display = 'none';
    },

    sendEmail() {
        const to = (document.getElementById('composeTo')?.value || '').trim();
        const cc = (document.getElementById('composeCc')?.value || '').trim();
        const bcc = (document.getElementById('composeBcc')?.value || '').trim();
        const subject = (document.getElementById('composeSubject')?.value || '').trim();
        const body = (document.getElementById('composeBody')?.value || '').trim();

        if (!to) {
            Components.showToast('Please specify at least one recipient');
            return;
        }

        AppState.sendEmail(to, cc, bcc, subject, body);
        App.closeCompose();
        Components.showToast('Message sent', 'Undo', () => {
            // Remove the last sent email
            const sent = AppState.emails.find(e => e.isSent && !e.isTrashed);
            if (sent) {
                AppState.emails = AppState.emails.filter(e => e.id !== sent.id);
                AppState._recalculateLabelCounts();
                AppState.notify();
            }
        });
    },

    // ============================================================
    // Label picker
    // ============================================================

    showLabelPicker(emailIds) {
        App._labelPickerEmailIds = emailIds;
        const userLabels = AppState.getUserLabels();

        // Determine which labels are currently applied to all selected emails
        const appliedToAll = {};
        for (const label of userLabels) {
            appliedToAll[label.id] = emailIds.every(id => {
                const email = AppState.getEmailById(id);
                return email && email.labels.includes(label.id);
            });
        }

        let body = '<div class="label-picker-search"><input type="text" class="form-input" id="labelPickerSearch" placeholder="Search labels"></div>';
        body += '<div class="label-picker-list">';
        for (const label of userLabels) {
            const checked = appliedToAll[label.id] ? 'checked' : '';
            const colorDot = label.color
                ? `<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:${Components.escapeAttr(label.color.background)};margin-right:4px"></span>`
                : '';
            body += `<div class="label-picker-item" data-label-id="${Components.escapeAttr(label.id)}">
                <input type="checkbox" ${checked} data-label-id="${Components.escapeAttr(label.id)}">
                ${colorDot}
                <span>${Components.escapeHtml(label.name)}</span>
            </div>`;
        }
        body += '</div>';
        body += '<div class="label-picker-footer"><a href="#" data-action="create-label" style="font-size:13px;color:var(--color-primary)">Create new label</a></div>';

        const footer = `<button class="btn btn-primary" data-action="close-modal">Apply</button>`;
        Components.showModal('Label as', body, footer);

        // Wire up search
        setTimeout(() => {
            const searchInput = document.getElementById('labelPickerSearch');
            if (searchInput) {
                searchInput.addEventListener('input', () => {
                    const q = searchInput.value.toLowerCase();
                    const items = document.querySelectorAll('.label-picker-item');
                    for (const item of items) {
                        const name = item.textContent.toLowerCase();
                        item.style.display = name.includes(q) ? '' : 'none';
                    }
                });
            }
        }, 50);
    },

    // ============================================================
    // Move-to picker
    // ============================================================

    showMoveToPicker(emailIds) {
        const destinations = [
            { id: 'inbox', name: 'Inbox' },
            { id: 'archive', name: 'Archive' },
            { id: 'trash', name: 'Trash' },
            { id: 'spam', name: 'Spam' },
        ];
        const userLabels = AppState.getUserLabels();

        let body = '<div style="max-height:300px;overflow-y:auto">';
        body += '<div style="padding:4px 0;font-size:12px;color:var(--text-secondary);font-weight:600;text-transform:uppercase">Move to</div>';
        for (const dest of destinations) {
            body += `<div class="dropdown-item" data-moveto-dest="${dest.id}" style="cursor:pointer">
                <span class="nav-item-icon">${Components.navIcon(dest.id === 'archive' ? 'allmail' : dest.id)}</span>
                <span>${Components.escapeHtml(dest.name)}</span>
            </div>`;
        }
        if (userLabels.length > 0) {
            body += '<div class="dropdown-divider"></div>';
            body += '<div style="padding:4px 0;font-size:12px;color:var(--text-secondary);font-weight:600;text-transform:uppercase">Labels</div>';
            for (const label of userLabels) {
                const colorDot = label.color
                    ? `<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:${Components.escapeAttr(label.color.background)};margin-right:4px"></span>`
                    : '';
                body += `<div class="dropdown-item" data-moveto-label="${Components.escapeAttr(label.id)}" style="cursor:pointer">
                    ${colorDot}
                    <span>${Components.escapeHtml(label.name)}</span>
                </div>`;
            }
        }
        body += '</div>';

        Components.showModal('Move to', body, '');

        // Handle clicks on move-to items
        setTimeout(() => {
            const modalBody = document.getElementById('modalBody');
            if (!modalBody) return;
            modalBody.addEventListener('click', function handler(evt) {
                const destEl = evt.target.closest('[data-moveto-dest]');
                const labelEl = evt.target.closest('[data-moveto-label]');

                if (destEl) {
                    const dest = destEl.dataset.movetoDest;
                    if (dest === 'inbox') AppState.moveToInbox(emailIds);
                    else if (dest === 'archive') AppState.archiveEmails(emailIds);
                    else if (dest === 'trash') AppState.trashEmails(emailIds);
                    else if (dest === 'spam') AppState.markAsSpam(emailIds);
                    AppState.selectedEmailIds = new Set();
                    Components.closeModal();
                    Components.showToast(`Moved to ${dest}`);
                    modalBody.removeEventListener('click', handler);
                } else if (labelEl) {
                    const labelId = labelEl.dataset.movetoLabel;
                    // Move = remove from inbox + add label
                    for (const id of emailIds) {
                        const email = AppState.getEmailById(id);
                        if (email) {
                            email.labels = email.labels.filter(l => l !== 'INBOX');
                            if (!email.labels.includes(labelId)) email.labels.push(labelId);
                            email.isArchived = true;
                        }
                    }
                    AppState._recalculateLabelCounts();
                    AppState.selectedEmailIds = new Set();
                    AppState.notify();
                    Components.closeModal();
                    const label = AppState.getLabelById(labelId);
                    Components.showToast(`Moved to ${label ? label.name : 'label'}`);
                    modalBody.removeEventListener('click', handler);
                }
            });
        }, 50);
    },

    // ============================================================
    // More menu (toolbar overflow)
    // ============================================================

    showMoreMenu(anchorEl) {
        const ids = Array.from(AppState.selectedEmailIds);
        const currentId = AppState.currentEmailId;
        const targetIds = ids.length > 0 ? ids : (currentId ? [currentId] : []);

        let items = [];
        items.push({ label: 'Mark as read', action: 'mark-read-selected' });
        items.push({ label: 'Mark as unread', action: 'mark-unread-selected' });
        items.push({ divider: true });
        // Show Unsnooze if the first target email is snoozed
        const _firstEmail = targetIds.length > 0 ? AppState.getEmailById(targetIds[0]) : null;
        if (_firstEmail && _firstEmail.isSnoozed) {
            items.push({ label: 'Unsnooze', action: 'unsnooze-email' });
        } else {
            items.push({ label: 'Snooze', action: 'snooze-email' });
        }
        items.push({ label: 'Add label', action: 'label-email' });
        items.push({ label: 'Move to', action: 'move-to' });
        items.push({ divider: true });
        items.push({ label: 'Mute', action: 'mute-email' });

        // Block sender — resolve sender from the first target email
        if (targetIds.length > 0) {
            const targetEmail = AppState.getEmailById(targetIds[0]);
            if (targetEmail && targetEmail.from && targetEmail.from.email) {
                items.push({ divider: true });
                items.push({ label: `Block "${targetEmail.from.name || targetEmail.from.email}"`, action: 'block-sender', senderEmail: targetEmail.from.email });
            }
        }

        if (AppState.currentView === 'spam') {
            items.push({ label: 'Not spam', action: 'not-spam-selected' });
        }

        if (AppState.currentView === 'trash') {
            items.push({ label: 'Delete forever', action: 'delete-forever' });
        }

        let body = '<div style="min-width:180px">';
        for (const item of items) {
            if (item.divider) {
                body += '<div class="dropdown-divider"></div>';
            } else {
                const extra = item.senderEmail ? ` data-sender-email="${Components.escapeAttr(item.senderEmail)}"` : '';
                body += `<div class="dropdown-item" data-action="${item.action}"${extra} style="cursor:pointer">${Components.escapeHtml(item.label)}</div>`;
            }
        }
        body += '</div>';

        Components.showModal('', body, '');
    },

    // ============================================================
    // Create / Edit label dialogs
    // ============================================================

    showCreateLabelDialog() {
        App._selectedColor = null;
        const parentOptions = AppState.getTopLevelUserLabels();
        let parentHtml = '<option value="">None (top-level)</option>';
        for (const p of parentOptions) {
            parentHtml += `<option value="${Components.escapeAttr(p.id)}">${Components.escapeHtml(p.name)}</option>`;
        }

        const body = `
            <div class="form-group">
                <label class="form-label">Label name</label>
                <input type="text" class="form-input" id="labelNameInput" placeholder="Enter label name" data-testid="label-name-input">
            </div>
            <div class="form-group">
                <label class="form-label">Nest under</label>
                <select class="form-input" id="labelParentSelect" data-testid="label-parent-select">
                    ${parentHtml}
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Color</label>
                ${Components.labelColorPicker(null)}
            </div>
        `;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" id="createLabelBtn">Create</button>
        `;
        Components.showModal('Create Label', body, footer);

        document.getElementById('createLabelBtn').onclick = () => {
            const name = document.getElementById('labelNameInput').value.trim();
            if (!name) {
                Components.showToast('Please enter a label name');
                return;
            }
            const parentId = document.getElementById('labelParentSelect').value || null;
            AppState.createLabel(name, App._selectedColor, parentId);
            Components.closeModal();
            Components.showToast(`Label "${name}" created`);
        };
    },

    showEditLabelDialog(labelId) {
        const label = AppState.getLabelById(labelId);
        if (!label) return;
        App._selectedColor = label.color;

        const parentOptions = AppState.getTopLevelUserLabels().filter(l => l.id !== labelId);
        let parentHtml = '<option value="">None (top-level)</option>';
        for (const p of parentOptions) {
            const selected = label.parentId === p.id ? ' selected' : '';
            parentHtml += `<option value="${Components.escapeAttr(p.id)}"${selected}>${Components.escapeHtml(p.name)}</option>`;
        }

        const body = `
            <div class="form-group">
                <label class="form-label">Label name</label>
                <input type="text" class="form-input" id="labelNameInput" value="${Components.escapeAttr(label.name)}" data-testid="label-name-input">
            </div>
            <div class="form-group">
                <label class="form-label">Nest under</label>
                <select class="form-input" id="labelParentSelect" data-testid="label-parent-select">
                    ${parentHtml}
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Color</label>
                ${Components.labelColorPicker(label.color)}
            </div>
        `;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-danger" id="deleteLabelBtn" style="margin-right:auto">Delete</button>
            <button class="btn btn-primary" id="saveLabelBtn">Save</button>
        `;
        Components.showModal('Edit Label', body, footer);

        document.getElementById('saveLabelBtn').onclick = () => {
            const name = document.getElementById('labelNameInput').value.trim();
            if (!name) {
                Components.showToast('Please enter a label name');
                return;
            }
            const parentId = document.getElementById('labelParentSelect').value || null;
            AppState.updateLabel(labelId, { name, color: App._selectedColor, parentId });
            Components.closeModal();
            Components.showToast(`Label "${name}" updated`);
        };

        document.getElementById('deleteLabelBtn').onclick = () => {
            Components.closeModal();
            Components.confirmDanger('Delete Label',
                `Are you sure you want to delete "${label.name}"?`, 'Delete', () => {
                    AppState.deleteLabel(labelId);
                    Components.showToast('Label deleted');
                });
        };
    },

    // ============================================================
    // Filter dialog
    // ============================================================

    showFilterDialog(filterId) {
        const existing = filterId ? AppState.filters.find(f => f.id === filterId) : null;
        const c = existing ? existing.criteria : { from: '', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' };
        const a = existing ? existing.actions : { label: null, archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: null };

        const userLabels = AppState.getUserLabels();
        let labelOptions = '<option value="">None</option>';
        for (const l of userLabels) {
            const selected = a.label === l.id ? ' selected' : '';
            labelOptions += `<option value="${Components.escapeAttr(l.id)}"${selected}>${Components.escapeHtml(l.name)}</option>`;
        }

        const body = `
            <div style="font-size:13px;color:var(--text-secondary);margin-bottom:16px">Criteria</div>
            <div class="filter-row">
                <label>From</label>
                <input type="text" class="form-input" id="filterFrom" value="${Components.escapeAttr(c.from)}" data-testid="filter-from">
            </div>
            <div class="filter-row">
                <label>To</label>
                <input type="text" class="form-input" id="filterTo" value="${Components.escapeAttr(c.to)}" data-testid="filter-to">
            </div>
            <div class="filter-row">
                <label>Subject</label>
                <input type="text" class="form-input" id="filterSubject" value="${Components.escapeAttr(c.subject)}" data-testid="filter-subject">
            </div>
            <div class="filter-row">
                <label>Has the words</label>
                <input type="text" class="form-input" id="filterHasWords" value="${Components.escapeAttr(c.hasWords)}" data-testid="filter-has-words">
            </div>
            <div class="filter-row">
                <label>Doesn't have</label>
                <input type="text" class="form-input" id="filterDoesntHave" value="${Components.escapeAttr(c.doesntHave)}" data-testid="filter-doesnt-have">
            </div>
            <div class="filter-row">
                <label>Has attachment</label>
                <input type="checkbox" id="filterHasAttachment" ${c.hasAttachment ? 'checked' : ''} data-testid="filter-has-attachment" style="accent-color:var(--color-primary)">
            </div>
            <div class="dropdown-divider" style="margin:16px 0"></div>
            <div style="font-size:13px;color:var(--text-secondary);margin-bottom:16px">Actions</div>
            <div class="filter-row">
                <label>Apply label</label>
                <select class="form-input" id="filterLabel" data-testid="filter-label">${labelOptions}</select>
            </div>
            <div class="filter-action-item"><input type="checkbox" id="filterArchive" ${a.archive ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterArchive">Skip the Inbox (Archive it)</label></div>
            <div class="filter-action-item"><input type="checkbox" id="filterMarkRead" ${a.markRead ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterMarkRead">Mark as read</label></div>
            <div class="filter-action-item"><input type="checkbox" id="filterStar" ${a.star ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterStar">Star it</label></div>
            <div class="filter-action-item"><input type="checkbox" id="filterDelete" ${a.delete ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterDelete">Delete it</label></div>
            <div class="filter-action-item"><input type="checkbox" id="filterNeverSpam" ${a.neverSpam ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterNeverSpam">Never send it to Spam</label></div>
            <div class="filter-action-item"><input type="checkbox" id="filterAlwaysImportant" ${a.alwaysImportant ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterAlwaysImportant">Always mark as important</label></div>
            <div class="filter-action-item"><input type="checkbox" id="filterNeverImportant" ${a.neverImportant ? 'checked' : ''} style="accent-color:var(--color-primary)"><label for="filterNeverImportant">Never mark as important</label></div>
            <div class="filter-row">
                <label>Forward to</label>
                <input type="text" class="form-input" id="filterForward" value="${Components.escapeAttr(a.forward || '')}" data-testid="filter-forward" placeholder="email@example.com">
            </div>
        `;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" id="saveFilterBtn">${existing ? 'Update' : 'Create'} Filter</button>
        `;
        Components.showModal(existing ? 'Edit Filter' : 'Create Filter', body, footer);

        document.getElementById('saveFilterBtn').onclick = () => {
            const criteria = {
                from: document.getElementById('filterFrom').value.trim(),
                to: document.getElementById('filterTo').value.trim(),
                subject: document.getElementById('filterSubject').value.trim(),
                hasWords: document.getElementById('filterHasWords').value.trim(),
                doesntHave: document.getElementById('filterDoesntHave').value.trim(),
                hasAttachment: document.getElementById('filterHasAttachment').checked,
                size: null,
                sizeUnit: 'MB',
                sizeComparison: 'greater',
            };
            const actions = {
                label: document.getElementById('filterLabel').value || null,
                archive: document.getElementById('filterArchive').checked,
                markRead: document.getElementById('filterMarkRead').checked,
                star: document.getElementById('filterStar').checked,
                forward: document.getElementById('filterForward').value.trim() || null,
                delete: document.getElementById('filterDelete').checked,
                neverSpam: document.getElementById('filterNeverSpam').checked,
                alwaysImportant: document.getElementById('filterAlwaysImportant').checked,
                neverImportant: document.getElementById('filterNeverImportant').checked,
                category: null,
            };

            if (existing) {
                AppState.updateFilter(filterId, criteria, actions);
                Components.showToast('Filter updated');
            } else {
                AppState.createFilter(criteria, actions);
                Components.showToast('Filter created');
            }
            Components.closeModal();
        };
    },

    // ============================================================
    // Save settings from full settings form
    // ============================================================

    saveSettingsFromForm() {
        // Collect values from any form elements with data-setting attributes
        const settingInputs = document.querySelectorAll('[data-setting]');
        for (const input of settingInputs) {
            const key = input.dataset.setting;
            let value;
            if (input.type === 'checkbox') {
                value = input.checked;
            } else if (input.type === 'number') {
                value = parseInt(input.value, 10);
            } else {
                value = input.value;
            }
            AppState.updateSetting(key, value);
        }

        // Save multiple inbox sections
        const sections = [];
        let i = 0;
        while (true) {
            const queryInput = document.querySelector(`[data-field="multi-inbox-query-${i}"]`);
            const nameInput = document.querySelector(`[data-field="multi-inbox-name-${i}"]`);
            if (!queryInput) break;
            sections.push({ query: queryInput.value, name: nameInput ? nameInput.value : '' });
            i++;
        }
        if (sections.length > 0) {
            AppState.updateSetting('multipleInboxSections', sections);
        }
    },

    // ============================================================
    // Context menu (right-click)
    // ============================================================

    handleContextMenu(e) {
        const emailEl = e.target.closest('[data-email-id]');
        if (!emailEl) return;

        e.preventDefault();
        const emailId = parseInt(emailEl.dataset.emailId, 10);
        App._contextMenuEmailId = emailId;
        const email = AppState.getEmailById(emailId);
        if (!email) return;

        let contextMenu = document.getElementById('contextMenu');
        if (!contextMenu) {
            contextMenu = document.createElement('div');
            contextMenu.id = 'contextMenu';
            contextMenu.className = 'context-menu';
            document.body.appendChild(contextMenu);
        }

        const isRead = email.isRead;

        contextMenu.innerHTML = `
            <div class="context-menu-item" data-context-action="reply">
                <span class="context-menu-item-icon">${Components.toolbarIcon('reply')}</span>
                <span>Reply</span>
            </div>
            <div class="context-menu-item" data-context-action="reply-all">
                <span class="context-menu-item-icon">${Components.toolbarIcon('replyAll')}</span>
                <span>Reply all</span>
            </div>
            <div class="context-menu-item" data-context-action="forward">
                <span class="context-menu-item-icon">${Components.toolbarIcon('forward')}</span>
                <span>Forward</span>
            </div>
            <div class="context-menu-divider"></div>
            <div class="context-menu-item" data-context-action="archive">
                <span class="context-menu-item-icon">${Components.toolbarIcon('archive')}</span>
                <span>Archive</span>
            </div>
            <div class="context-menu-item" data-context-action="delete">
                <span class="context-menu-item-icon">${Components.toolbarIcon('delete')}</span>
                <span>Delete</span>
            </div>
            <div class="context-menu-item" data-context-action="${isRead ? 'mark-unread' : 'mark-read'}">
                <span class="context-menu-item-icon">${Components.toolbarIcon(isRead ? 'markUnread' : 'markRead')}</span>
                <span>Mark as ${isRead ? 'unread' : 'read'}</span>
            </div>
            <div class="context-menu-divider"></div>
            ${email.isSnoozed
                ? `<div class="context-menu-item" data-context-action="unsnooze">
                <span class="context-menu-item-icon">${Components.toolbarIcon('snooze')}</span>
                <span>Unsnooze</span>
            </div>`
                : `<div class="context-menu-item" data-context-action="snooze">
                <span class="context-menu-item-icon">${Components.toolbarIcon('snooze')}</span>
                <span>Snooze</span>
            </div>`}
            <div class="context-menu-item" data-context-action="label">
                <span class="context-menu-item-icon">${Components.toolbarIcon('label')}</span>
                <span>Label as</span>
            </div>
            <div class="context-menu-item" data-context-action="move-to">
                <span class="context-menu-item-icon">${Components.toolbarIcon('moveTo')}</span>
                <span>Move to</span>
            </div>
            <div class="context-menu-item" data-context-action="mute">
                <span class="context-menu-item-icon">${Components.toolbarIcon('archive')}</span>
                <span>Mute</span>
            </div>
            <div class="context-menu-divider"></div>
            <div class="context-menu-item" data-context-action="block-sender">
                <span class="context-menu-item-icon">${Components.toolbarIcon('spam')}</span>
                <span>Block "${Components.escapeHtml(email.from.name || email.from.email)}"</span>
            </div>
        `;

        // Position the menu
        contextMenu.style.left = e.clientX + 'px';
        contextMenu.style.top = e.clientY + 'px';
        contextMenu.classList.add('open');

        // Ensure menu stays within viewport
        const rect = contextMenu.getBoundingClientRect();
        if (rect.right > window.innerWidth) {
            contextMenu.style.left = (window.innerWidth - rect.width - 8) + 'px';
        }
        if (rect.bottom > window.innerHeight) {
            contextMenu.style.top = (window.innerHeight - rect.height - 8) + 'px';
        }
    },

    handleContextAction(action) {
        const emailId = App._contextMenuEmailId;
        if (!emailId) return;

        const contextMenu = document.getElementById('contextMenu');
        if (contextMenu) contextMenu.classList.remove('open');

        switch (action) {
            case 'reply':
            case 'reply-all':
            case 'forward': {
                const email = AppState.getEmailById(emailId);
                if (!email) return;
                if (action === 'reply') {
                    App.openCompose({
                        to: email.from.email,
                        subject: 'Re: ' + email.subject.replace(/^Re:\s*/i, ''),
                        body: '\n\n--- Original Message ---\nFrom: ' + email.from.name +
                              ' <' + email.from.email + '>\n\n' + (email.body || email.snippet)
                    });
                } else if (action === 'reply-all') {
                    const allRecipients = [email.from.email];
                    if (email.to) {
                        for (const r of email.to) {
                            if (r.email !== AppState.currentUser.email) allRecipients.push(r.email);
                        }
                    }
                    App.openCompose({
                        to: allRecipients.join(', '),
                        subject: 'Re: ' + email.subject.replace(/^Re:\s*/i, ''),
                        body: '\n\n--- Original Message ---\nFrom: ' + email.from.name +
                              ' <' + email.from.email + '>\n\n' + (email.body || email.snippet)
                    });
                } else {
                    App.openCompose({
                        to: '',
                        subject: 'Fwd: ' + email.subject.replace(/^Fwd:\s*/i, ''),
                        body: '\n\n--- Forwarded Message ---\nFrom: ' + email.from.name +
                              ' <' + email.from.email + '>\nSubject: ' +
                              email.subject + '\n\n' + (email.body || email.snippet)
                    });
                }
                break;
            }
            case 'archive':
                AppState.archiveEmails([emailId]);
                Components.showToast('Conversation archived', 'Undo', () => AppState.moveToInbox([emailId]));
                break;
            case 'delete':
                AppState.trashEmails([emailId]);
                Components.showToast('Conversation moved to Trash', 'Undo', () => AppState.moveToInbox([emailId]));
                break;
            case 'mark-read':
                AppState.markAsRead([emailId]);
                break;
            case 'mark-unread':
                AppState.markAsUnread([emailId]);
                break;
            case 'snooze':
                App._snoozeTargetIds = [emailId];
                Components.showModal('Snooze', Components.snoozePicker(), '');
                break;
            case 'unsnooze':
                AppState.unsnoozeEmails([emailId]);
                Components.showToast('Conversation moved to Inbox');
                break;
            case 'label':
                App.showLabelPicker([emailId]);
                break;
            case 'move-to':
                App.showMoveToPicker([emailId]);
                break;
            case 'mute':
                AppState.muteEmails([emailId]);
                Components.showToast('Conversation muted');
                break;
            case 'block-sender': {
                const ctxEmail = AppState.getEmailById(emailId);
                if (ctxEmail && ctxEmail.from && ctxEmail.from.email) {
                    AppState.blockSender(ctxEmail.from.email);
                    Components.showToast(`Blocked ${ctxEmail.from.email}`);
                }
                break;
            }
        }
    },

    // ============================================================
    // Keyboard shortcuts
    // ============================================================

    handleKeydown(e) {
        // Don't handle if typing in an input
        const tag = e.target.tagName;
        if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') {
            // Allow Enter in search input
            if (tag === 'INPUT' && e.target.id === 'searchInput' && e.key === 'Enter') {
                e.preventDefault();
                const val = e.target.value.trim();
                if (val) {
                    AppState.searchQuery = val;
                    AppState.searchResults = AppState.searchEmails(val);
                    AppState.currentEmailId = null;
                    AppState.currentPage = 1;
                    App.render();
                }
            }
            // Allow Escape to blur inputs and close compose
            if (e.key === 'Escape') {
                e.target.blur();
                const composeModal = document.getElementById('composeModal');
                if (composeModal && composeModal.style.display !== 'none') {
                    App.closeCompose();
                }
                const modalOverlay = document.getElementById('modalOverlay');
                if (modalOverlay && modalOverlay.style.display !== 'none') {
                    Components.closeModal();
                }
            }
            return;
        }

        // Escape closes menus/modals
        if (e.key === 'Escape') {
            const contextMenu = document.getElementById('contextMenu');
            if (contextMenu && contextMenu.classList.contains('open')) {
                contextMenu.classList.remove('open');
                return;
            }
            const composeModal = document.getElementById('composeModal');
            if (composeModal && composeModal.style.display !== 'none') {
                App.closeCompose();
                return;
            }
            const modalOverlay = document.getElementById('modalOverlay');
            if (modalOverlay && modalOverlay.style.display !== 'none') {
                Components.closeModal();
                return;
            }
            // If in email detail, go back
            if (AppState.currentEmailId) {
                AppState.currentEmailId = null;
                App.navigate(AppState.currentView);
                return;
            }
            return;
        }

        // Keyboard shortcuts only if enabled
        if (!AppState.settings.keyboardShortcutsEnabled) return;

        const key = e.key;

        // Handle * sequences (select all/none)
        if (App._keySequence === '*') {
            clearTimeout(App._keySequenceTimer);
            App._keySequence = '';
            if (key === 'a') {
                e.preventDefault();
                App.handleAction('select-all');
                return;
            }
            if (key === 'n') {
                e.preventDefault();
                App.handleAction('deselect-all');
                return;
            }
        }

        if (key === '*') {
            App._keySequence = '*';
            App._keySequenceTimer = setTimeout(() => { App._keySequence = ''; }, 1000);
            return;
        }

        // Single-key shortcuts
        switch (key) {
            case 'e':
                e.preventDefault();
                App.handleAction('archive-selected');
                break;
            case '#':
                e.preventDefault();
                App.handleAction('delete-selected');
                break;
            case 'r':
                e.preventDefault();
                if (AppState.currentEmailId) {
                    App.handleAction('reply', document.body);
                }
                break;
            case 'a':
                e.preventDefault();
                if (AppState.currentEmailId) {
                    App.handleAction('reply-all', document.body);
                }
                break;
            case 'f':
                e.preventDefault();
                if (AppState.currentEmailId) {
                    App.handleAction('forward', document.body);
                }
                break;
            case 'j': // next email in list
                e.preventDefault();
                App._navigateEmailList(1);
                break;
            case 'k': // previous email in list
                e.preventDefault();
                App._navigateEmailList(-1);
                break;
            case 'o':
            case 'Enter':
                e.preventDefault();
                if (!AppState.currentEmailId) {
                    // Open first selected or first email
                    const selectedIds = Array.from(AppState.selectedEmailIds);
                    if (selectedIds.length > 0) {
                        App.navigate('email/' + selectedIds[0]);
                    } else {
                        const emails = App._getVisibleEmails();
                        const sorted = AppState.sortEmails(emails);
                        if (sorted.length > 0) {
                            App.navigate('email/' + sorted[0].id);
                        }
                    }
                }
                break;
            case 'u':
                e.preventDefault();
                if (AppState.currentEmailId) {
                    AppState.currentEmailId = null;
                    App.navigate(AppState.currentView);
                }
                break;
            case 's':
                e.preventDefault();
                if (AppState.currentEmailId) {
                    AppState.cycleStar(AppState.currentEmailId);
                } else {
                    const selectedIds = Array.from(AppState.selectedEmailIds);
                    if (selectedIds.length > 0) {
                        for (const id of selectedIds) AppState.toggleStar(id);
                    }
                }
                break;
            case 'l':
                e.preventDefault();
                App.handleAction('label-email');
                break;
            case 'v':
                e.preventDefault();
                App.handleAction('move-to');
                break;
            case 'b':
                e.preventDefault();
                App.handleAction('snooze-email');
                break;
            case 'I': // Shift+i
                if (e.shiftKey) {
                    e.preventDefault();
                    App.handleAction('mark-read-selected');
                }
                break;
            case 'U': // Shift+u
                if (e.shiftKey) {
                    e.preventDefault();
                    App.handleAction('mark-unread-selected');
                }
                break;
            case 'm':
                e.preventDefault();
                App.handleAction('mute-email');
                break;
            case '/':
                e.preventDefault();
                const searchInput = document.getElementById('searchInput');
                if (searchInput) searchInput.focus();
                break;
            case 'c':
                e.preventDefault();
                App.openCompose();
                break;
        }
    },

    _navigateEmailList(direction) {
        const emails = App._getVisibleEmails();
        const sorted = AppState.sortEmails(emails);
        if (sorted.length === 0) return;

        if (AppState.currentEmailId) {
            // Navigate within email detail
            const idx = sorted.findIndex(e => e.id === AppState.currentEmailId);
            const nextIdx = idx + direction;
            if (nextIdx >= 0 && nextIdx < sorted.length) {
                App.navigate('email/' + sorted[nextIdx].id);
            }
        } else {
            // Move selection in the list
            const selectedIds = Array.from(AppState.selectedEmailIds);
            if (selectedIds.length === 0) {
                // Select first email
                AppState.selectedEmailIds = new Set([sorted[0].id]);
            } else {
                const lastSelected = selectedIds[selectedIds.length - 1];
                const idx = sorted.findIndex(e => e.id === lastSelected);
                const nextIdx = idx + direction;
                if (nextIdx >= 0 && nextIdx < sorted.length) {
                    AppState.selectedEmailIds = new Set([sorted[nextIdx].id]);
                }
            }
            App.render();
        }
    },

    // ============================================================
    // SSE connection for reset events
    // ============================================================

    setupSSE() {
        if (App._sseConnection) {
            App._sseConnection.close();
        }

        try {
            const evtSource = new EventSource('/api/events');
            App._sseConnection = evtSource;

            evtSource.onmessage = (event) => {
                if (event.data === 'reset') {
                    AppState.resetToSeedData();
                    App.navigate('inbox');
                }
            };

            evtSource.onerror = () => {
                // Reconnect after a delay
                setTimeout(() => {
                    if (App._sseConnection === evtSource) {
                        App.setupSSE();
                    }
                }, 5000);
            };
        } catch (e) {
            console.warn('SSE not available:', e);
        }
    },

    // ============================================================
    // Helper: get visible emails for current view
    // ============================================================

    _getVisibleEmails() {
        if (AppState.searchResults !== null) {
            return AppState.searchResults;
        }
        if (AppState.currentView === 'inbox' && AppState.settings.inboxType === 'default') {
            const catEnabled = AppState.settings.categoriesEnabled || {};
            const anyCategory = catEnabled.social || catEnabled.promotions ||
                                catEnabled.updates || catEnabled.forums;
            if (anyCategory) {
                return AppState.getInboxEmailsByCategory(AppState.currentCategory);
            }
        }
        return AppState.getEmailsForView(AppState.currentView);
    },

    // ============================================================
    // Helper: advance to next/previous email after action
    // ============================================================

    _advanceAfterAction() {
        const autoAdvance = AppState.settings.autoAdvance || 'newer';
        const emails = AppState.sortEmails(App._getVisibleEmails());
        const idx = emails.findIndex(e => e.id === AppState.currentEmailId);

        AppState.currentEmailId = null;

        if (autoAdvance === 'newer' && idx > 0) {
            AppState.currentEmailId = emails[idx - 1].id;
            App.navigate('email/' + AppState.currentEmailId);
        } else if (autoAdvance === 'older' && idx < emails.length - 1) {
            AppState.currentEmailId = emails[idx + 1].id;
            App.navigate('email/' + AppState.currentEmailId);
        } else {
            // Back to list
            App.navigate(AppState.currentView);
        }
    },

    // ============================================================
    // Initialization
    // ============================================================

    initApp() {
        // Initialize state
        AppState.init();

        // Set up router
        App.parseRoute();
        window.addEventListener('hashchange', () => {
            App.parseRoute();
            App.render();
        });

        // Set up SSE connection
        App.setupSSE();

        // Set up event delegation
        document.addEventListener('click', App.handleClick);
        document.addEventListener('contextmenu', App.handleContextMenu);
        document.addEventListener('keydown', App.handleKeydown);

        // Menu toggle for sidebar
        const menuToggle = document.getElementById('menuToggle');
        if (menuToggle) {
            menuToggle.addEventListener('click', () => {
                document.body.classList.toggle('sidebar-collapsed');
            });
        }

        // Search input enter key
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    const val = searchInput.value.trim();
                    if (val) {
                        AppState.searchQuery = val;
                        AppState.searchResults = AppState.searchEmails(val);
                        AppState.currentEmailId = null;
                        AppState.currentPage = 1;
                        App.render();
                    }
                }
            });
        }

        // Search options toggle
        const searchOptionsBtn = document.getElementById('searchOptionsBtn');
        if (searchOptionsBtn) {
            searchOptionsBtn.addEventListener('click', () => {
                const panel = document.getElementById('searchOptionsPanel');
                if (panel) {
                    if (panel.style.display === 'none') {
                        panel.style.display = 'block';
                        panel.innerHTML = App._renderSearchOptionsPanel();
                    } else {
                        panel.style.display = 'none';
                    }
                }
            });
        }

        // Click outside search options to close
        document.addEventListener('click', (e) => {
            const panel = document.getElementById('searchOptionsPanel');
            if (panel && panel.style.display !== 'none') {
                if (!panel.contains(e.target) && !e.target.closest('#searchOptionsBtn')) {
                    panel.style.display = 'none';
                }
            }
        });

        // Subscribe to state changes
        AppState.subscribe(() => App.render());

        // Initial render
        App.render();

        // Push initial state to server
        AppState._pushStateToServer();
    },

    // ============================================================
    // Search options panel
    // ============================================================

    _renderSearchOptionsPanel() {
        return `
            <div class="search-options-row">
                <label>From</label>
                <input type="text" class="form-input" id="searchFrom" placeholder="" data-testid="search-from">
            </div>
            <div class="search-options-row">
                <label>To</label>
                <input type="text" class="form-input" id="searchTo" placeholder="" data-testid="search-to">
            </div>
            <div class="search-options-row">
                <label>Subject</label>
                <input type="text" class="form-input" id="searchSubject" placeholder="" data-testid="search-subject">
            </div>
            <div class="search-options-row">
                <label>Has words</label>
                <input type="text" class="form-input" id="searchHasWords" placeholder="" data-testid="search-has-words">
            </div>
            <div class="search-options-actions">
                <button class="btn btn-text" onclick="document.getElementById('searchOptionsPanel').style.display='none'">Close</button>
                <button class="btn btn-primary" id="searchOptionsSearchBtn">Search</button>
            </div>
        `;
    },
};

// ============================================================
// Bootstrap
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    App.initApp();

    // Wire up search options search button (after panel rendered)
    document.addEventListener('click', (e) => {
        if (e.target.id === 'searchOptionsSearchBtn') {
            const from = document.getElementById('searchFrom')?.value.trim();
            const to = document.getElementById('searchTo')?.value.trim();
            const subject = document.getElementById('searchSubject')?.value.trim();
            const hasWords = document.getElementById('searchHasWords')?.value.trim();

            let query = '';
            if (from) query += 'from:' + from + ' ';
            if (to) query += 'to:' + to + ' ';
            if (subject) query += 'subject:' + subject + ' ';
            if (hasWords) query += hasWords;
            query = query.trim();

            if (query) {
                const searchInput = document.getElementById('searchInput');
                if (searchInput) searchInput.value = query;
                AppState.searchQuery = query;
                AppState.searchResults = AppState.searchEmails(query);
                AppState.currentEmailId = null;
                AppState.currentPage = 1;
                document.getElementById('searchOptionsPanel').style.display = 'none';
                App.render();
            }
        }
    });
});

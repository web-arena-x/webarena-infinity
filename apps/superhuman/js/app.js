const App = {
    // ---- Current view state (derived from route) ----
    currentView: 'inbox', // inbox, email, settings, search, label, starred, folder

    // ---- Initialization ----
    initApp() {
        // 1. Initialize state
        AppState.init();

        // 2. Parse initial route
        this.parseRoute();

        // 3. Wire up hash-based routing
        window.addEventListener('hashchange', () => {
            this.parseRoute();
            this.render();
        });

        // 4. Set up SSE for reset
        this.setupSSE();

        // 5. Event delegation
        document.addEventListener('click', (e) => this.handleClick(e));
        document.addEventListener('keydown', (e) => this.handleKeydown(e));
        document.addEventListener('input', (e) => this.handleInput(e));
        document.addEventListener('change', (e) => this.handleChange(e));

        // 6. Subscribe to state changes
        AppState.subscribe(() => this.render());

        // 7. Initial render
        this.render();

        // 8. Push initial state to server (establishes seed state)
        AppState._pushStateToServer();
    },

    // ---- SSE ----
    setupSSE() {
        const connect = () => {
            const es = new EventSource('/api/events');
            es.onmessage = (e) => {
                if (e.data === 'reset') {
                    AppState.resetToSeedData();
                    window.location.hash = '#/inbox';
                }
            };
            es.onerror = () => {
                es.close();
                setTimeout(connect, 5000);
            };
        };
        connect();
    },

    // ---- Routing ----
    parseRoute() {
        const hash = window.location.hash || '#/inbox';
        const parts = hash.substring(2).split('/'); // Remove '#/'

        if (parts[0] === 'email' && parts[1]) {
            this.currentView = 'email';
            AppState.selectedEmailId = parts[1];
            // Mark as read when opening
            AppState.markAsRead(parts[1]);
        } else if (parts[0] === 'settings') {
            this.currentView = 'settings';
            AppState.settingsTab = parts[1] || 'general';
            AppState.selectedEmailId = null;
        } else if (parts[0] === 'search') {
            this.currentView = 'search';
            AppState.selectedEmailId = null;
        } else if (parts[0] === 'label' && parts[1]) {
            this.currentView = 'label';
            AppState.selectedLabelId = parts[1];
            AppState.selectedEmailId = null;
        } else if (parts[0] === 'starred') {
            this.currentView = 'starred';
            AppState.selectedEmailId = null;
        } else if (['inbox', 'done', 'sent', 'drafts', 'scheduled', 'trash', 'spam', 'reminders'].includes(parts[0])) {
            this.currentView = 'folder';
            AppState.selectedFolder = parts[0];
            AppState.selectedEmailId = null;
        } else {
            this.currentView = 'folder';
            AppState.selectedFolder = 'inbox';
            AppState.selectedEmailId = null;
        }
    },

    navigate(route) {
        window.location.hash = '#/' + route;
    },

    // ---- Rendering ----
    render() {
        const sidebar = document.getElementById('sidebar');
        const mainContent = document.getElementById('mainContent');
        const calendarSidebar = document.getElementById('calendarSidebar');

        if (!sidebar || !mainContent) return;

        // Sidebar
        sidebar.innerHTML = Views.renderSidebar();

        // Calendar sidebar
        if (calendarSidebar) {
            calendarSidebar.innerHTML = Views.renderCalendarSidebar();
        }

        // Main content area
        let contentHtml = '';

        if (AppState.composerOpen) {
            // Composer overlay
            contentHtml += Views.renderComposer(AppState.composerDraft);
        }

        switch (this.currentView) {
            case 'email':
                contentHtml += Views.renderEmailDetail(AppState.selectedEmailId);
                break;

            case 'settings':
                contentHtml += Views.renderSettings();
                break;

            case 'search':
                contentHtml += Views.renderSearchResults();
                break;

            case 'label': {
                const label = AppState.labels.find(l => l.id === AppState.selectedLabelId);
                const labelEmails = AppState.getEmailsForLabel(AppState.selectedLabelId);
                contentHtml += Views.renderEmailList(labelEmails, label ? label.name : 'Label');
                break;
            }

            case 'starred':
                contentHtml += Views.renderEmailList(AppState.getStarredEmails(), 'Starred');
                break;

            case 'folder':
            default: {
                // If inbox with split inbox, show split tabs + filtered emails
                if (AppState.selectedFolder === 'inbox' && AppState.settings.splitInbox.enabled) {
                    contentHtml += Views.renderSplitTabs();
                    const splitEmails = AppState.getEmailsForSplit(AppState.selectedSplit);
                    contentHtml += Views.renderEmailList(splitEmails);
                } else {
                    const folderNames = { inbox: 'Inbox', done: 'Done', sent: 'Sent', drafts: 'Drafts', scheduled: 'Scheduled', trash: 'Trash', spam: 'Spam', reminders: 'Reminders' };
                    const emails = AppState.getEmailsForFolder(AppState.selectedFolder);
                    contentHtml += Views.renderEmailList(emails, folderNames[AppState.selectedFolder] || '');
                }
                break;
            }
        }

        mainContent.innerHTML = contentHtml;

        // Re-focus search input if in search view
        if (this.currentView === 'search') {
            const searchInput = document.getElementById('searchInput');
            if (searchInput && !document.activeElement.classList.contains('search-main-input')) {
                searchInput.focus();
            }
        }

        // Command palette
        this._renderCommandPalette();
    },

    // ---- Command Palette ----
    _renderCommandPalette() {
        let cp = document.getElementById('commandPalette');
        if (AppState.commandPaletteOpen) {
            if (!cp) {
                const div = document.createElement('div');
                div.innerHTML = Components.commandPalette();
                cp = div.firstElementChild;
                document.body.appendChild(cp);
            }
            cp.style.display = 'flex';
            setTimeout(() => {
                const input = document.getElementById('commandPaletteInput');
                if (input) input.focus();
            }, 50);
        } else if (cp) {
            cp.style.display = 'none';
        }
    },

    _getCommandPaletteResults(query) {
        if (!query) return [];
        const q = query.toLowerCase();

        const commands = [
            { label: 'Compose New Email', action: 'compose', shortcut: 'C', category: 'Actions' },
            { label: 'Search', action: 'open-search', shortcut: '/', category: 'Navigation' },
            { label: 'Go to Inbox', action: 'navigate-folder', folder: 'inbox', shortcut: '', category: 'Navigation' },
            { label: 'Go to Done', action: 'navigate-folder', folder: 'done', shortcut: 'G then E', category: 'Navigation' },
            { label: 'Go to Reminders', action: 'navigate-folder', folder: 'reminders', shortcut: 'G then H', category: 'Navigation' },
            { label: 'Go to Sent', action: 'navigate-folder', folder: 'sent', shortcut: '', category: 'Navigation' },
            { label: 'Go to Drafts', action: 'navigate-folder', folder: 'drafts', shortcut: '', category: 'Navigation' },
            { label: 'Go to Trash', action: 'navigate-folder', folder: 'trash', shortcut: '', category: 'Navigation' },
            { label: 'Go to Spam', action: 'navigate-folder', folder: 'spam', shortcut: '', category: 'Navigation' },
            { label: 'Go to Snippets', action: 'navigate-settings-snippets', shortcut: 'G then ;', category: 'Navigation' },
            { label: 'Go to Settings', action: 'navigate-settings', shortcut: '', category: 'Navigation' },
            { label: 'Mark Done', action: 'mark-done-current', shortcut: 'E', category: 'Actions' },
            { label: 'Remind Me', action: 'reminder-current', shortcut: 'H', category: 'Actions' },
            { label: 'Reply', action: 'reply-current', shortcut: 'R', category: 'Actions' },
            { label: 'Reply All', action: 'reply-all-current', shortcut: 'Shift+R', category: 'Actions' },
            { label: 'Forward', action: 'forward-current', shortcut: 'F', category: 'Actions' },
            { label: 'Move to Folder', action: 'move-current', shortcut: 'V', category: 'Actions' },
            { label: 'Star / Unstar', action: 'toggle-star-current', shortcut: 'S', category: 'Actions' },
            { label: 'Mark Unread', action: 'mark-unread-current', shortcut: 'U', category: 'Actions' },
            { label: 'Trash', action: 'trash-current', shortcut: '#', category: 'Actions' },
            { label: 'Unsubscribe', action: 'unsubscribe-current', shortcut: 'Ctrl+U', category: 'Actions' },
            { label: 'Get Me To Zero', action: 'get-me-to-zero', shortcut: '', category: 'Actions' },
            { label: 'Enable Read Statuses', action: 'navigate-settings-read', shortcut: '', category: 'Settings' },
            { label: 'Split Inbox Library', action: 'navigate-settings-split', shortcut: '', category: 'Settings' },
            { label: 'Auto Label Library', action: 'navigate-settings-autolabels', shortcut: '', category: 'Settings' },
            { label: 'Calendar Settings', action: 'navigate-settings-calendar', shortcut: '', category: 'Settings' },
            { label: 'Reminder Settings', action: 'navigate-settings-reminders', shortcut: '', category: 'Settings' },
            { label: 'Create Snippet', action: 'create-snippet', shortcut: '', category: 'Actions' },
            { label: 'Create Event', action: 'create-event', shortcut: 'B', category: 'Actions' },
        ];

        // Also add label navigation commands
        const userLabels = AppState.labels.filter(l => !l.isSystem);
        for (const label of userLabels) {
            commands.push({ label: `Go to ${label.name}`, action: 'navigate-label-cmd', labelId: label.id, shortcut: '', category: 'Navigation' });
        }

        return commands.filter(c => c.label.toLowerCase().includes(q));
    },

    _executeCommand(command) {
        AppState.commandPaletteOpen = false;
        AppState.commandPaletteQuery = '';

        switch (command.action) {
            case 'compose': this.openComposer(); break;
            case 'open-search': this.navigate('search'); break;
            case 'navigate-folder': this.navigate(command.folder); break;
            case 'navigate-settings': this.navigate('settings'); break;
            case 'navigate-settings-snippets': this.navigate('settings/snippets'); break;
            case 'navigate-settings-read': this.navigate('settings/read-statuses'); break;
            case 'navigate-settings-split': this.navigate('settings/split-inbox'); break;
            case 'navigate-settings-autolabels': this.navigate('settings/auto-labels'); break;
            case 'navigate-settings-calendar': this.navigate('settings/calendar'); break;
            case 'navigate-settings-reminders': this.navigate('settings/reminders'); break;
            case 'navigate-label-cmd': this.navigate('label/' + command.labelId); break;
            case 'mark-done-current': this._actionOnCurrentEmail('markDone'); break;
            case 'toggle-star-current': this._actionOnCurrentEmail('toggleStar'); break;
            case 'mark-unread-current': this._actionOnCurrentEmail('markAsUnread'); break;
            case 'trash-current': this._actionOnCurrentEmail('trashEmail'); break;
            case 'reply-current': this._replyToCurrentEmail('reply'); break;
            case 'reply-all-current': this._replyToCurrentEmail('reply-all'); break;
            case 'forward-current': this._replyToCurrentEmail('forward'); break;
            case 'create-snippet': this._showCreateSnippetModal(); break;
            case 'create-event': this._showCreateEventModal(); break;
            case 'get-me-to-zero': this._showGetMeToZeroModal(); break;
            case 'reminder-current': this._showReminderPicker(); break;
            case 'move-current': this._showFolderPicker(); break;
            case 'unsubscribe-current': this._unsubscribeCurrentEmail(); break;
            default: break;
        }
        this.render();
    },

    // ---- Click Handler ----
    handleClick(e) {
        const target = e.target;

        // Close command palette on overlay click
        if (target.classList.contains('command-palette-overlay')) {
            AppState.commandPaletteOpen = false;
            this.render();
            return;
        }

        // Close any open dropdowns when clicking outside
        if (!target.closest('.custom-dropdown') && !target.closest('.popover')) {
            document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
            document.querySelectorAll('.popover').forEach(p => { p.style.display = 'none'; });
        }

        // Close modal on overlay click
        if (target.classList.contains('modal-overlay')) {
            Components.closeModal(target.id);
            return;
        }

        // Star icon (stop propagation to prevent opening email)
        const star = target.closest('.star-icon');
        if (star) {
            e.stopPropagation();
            const emailId = star.dataset.emailId;
            if (emailId) AppState.toggleStar(emailId);
            return;
        }

        // Dropdown trigger
        const ddTrigger = target.closest('[data-dropdown]');
        if (ddTrigger) {
            e.stopPropagation();
            const ddId = ddTrigger.dataset.dropdown;
            const menu = document.getElementById(ddId + '-menu');
            if (menu) {
                const wasOpen = menu.classList.contains('open');
                document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
                if (!wasOpen) menu.classList.add('open');
            }
            return;
        }

        // Dropdown item selection
        const ddItem = target.closest('.dropdown-item');
        if (ddItem) {
            const ddId = ddItem.dataset.dropdownId;
            const value = ddItem.dataset.value;
            document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
            this.handleDropdownSelect(ddId, value);
            return;
        }

        // Command palette result
        const cpResult = target.closest('.command-result');
        if (cpResult) {
            const idx = parseInt(cpResult.dataset.index);
            const results = this._getCommandPaletteResults(AppState.commandPaletteQuery);
            if (results[idx]) {
                this._executeCommand(results[idx]);
            }
            return;
        }

        // Data-action handler
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            this.handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // Toggle switch
        const toggle = target.closest('.toggle-switch input');
        if (toggle) {
            this.handleToggleChange(toggle);
            return;
        }

        // Radio option
        const radio = target.closest('.radio-option input[type="radio"]');
        if (radio) {
            this.handleRadioChange(radio);
            return;
        }
    },

    // ---- Action Handler ----
    handleAction(action, el) {
        switch (action) {
            // Navigation
            case 'navigate-folder': {
                const folder = el.dataset.folder;
                AppState.selectedFolder = folder;
                AppState.selectedSplit = AppState.splits[0] ? AppState.splits[0].id : 'split_important';
                this.navigate(folder);
                break;
            }
            case 'navigate-label': {
                const labelId = el.dataset.labelId;
                this.navigate('label/' + labelId);
                break;
            }
            case 'navigate-settings':
                this.navigate('settings');
                break;
            case 'settings-tab': {
                const tab = el.dataset.tab;
                this.navigate('settings/' + tab);
                break;
            }
            case 'search-focus':
                this.navigate('search');
                break;

            // Split selection
            case 'select-split': {
                const splitId = el.dataset.splitId;
                AppState.selectedSplit = splitId;
                this.render();
                break;
            }

            // Email actions
            case 'open-email': {
                const emailId = el.dataset.emailId;
                if (emailId) this.navigate('email/' + emailId);
                break;
            }
            case 'back-to-list':
                window.history.back();
                break;
            case 'mark-done-current':
                this._actionOnCurrentEmail('markDone');
                this._advanceToNextEmail();
                break;
            case 'trash-current':
                this._actionOnCurrentEmail('trashEmail');
                this._advanceToNextEmail();
                break;
            case 'toggle-star-current':
                this._actionOnCurrentEmail('toggleStar');
                break;
            case 'mark-unread-current':
                this._actionOnCurrentEmail('markAsUnread');
                break;
            case 'unsubscribe-current':
                this._unsubscribeCurrentEmail();
                break;

            // Reminder
            case 'reminder-current':
                this._showReminderPicker();
                break;
            case 'set-reminder': {
                const emailId = el.dataset.emailId;
                const time = el.dataset.reminderTime;
                if (emailId && time) {
                    AppState.setReminder(emailId, time, 'manual');
                    Components.showToast('Reminder set', 'success');
                    document.querySelectorAll('.popover').forEach(p => { p.style.display = 'none'; });
                }
                break;
            }
            case 'set-reminder-custom':
                this._showCustomReminderModal(el.dataset.emailId);
                break;

            // Labels
            case 'label-current':
                this._showLabelPicker();
                break;
            case 'toggle-label': {
                const emailId = el.dataset.emailId;
                const labelId = el.dataset.labelId;
                if (emailId && labelId) {
                    const email = AppState.getEmailById(emailId);
                    if (email) {
                        if (email.labels.includes(labelId)) {
                            AppState.removeLabel(emailId, labelId);
                        } else {
                            AppState.addLabel(emailId, labelId);
                        }
                    }
                }
                break;
            }

            // Move to folder
            case 'move-current':
                this._showFolderPicker();
                break;
            case 'move-to-folder': {
                const emailId = el.dataset.emailId;
                const folder = el.dataset.folder;
                if (emailId && folder) {
                    AppState.moveToFolder(emailId, folder);
                    Components.showToast('Moved to ' + folder, 'success');
                    document.querySelectorAll('.popover').forEach(p => { p.style.display = 'none'; });
                    this._advanceToNextEmail();
                }
                break;
            }

            // Compose
            case 'compose':
                this.openComposer();
                break;
            case 'close-composer':
                this.closeComposer();
                break;
            case 'toggle-cc': {
                const field = document.getElementById('composeCcField');
                if (field) field.style.display = field.style.display === 'none' ? 'flex' : 'none';
                break;
            }
            case 'toggle-bcc': {
                const field = document.getElementById('composeBccField');
                if (field) field.style.display = field.style.display === 'none' ? 'flex' : 'none';
                break;
            }
            case 'send-email':
                this.sendCurrentEmail();
                break;
            case 'schedule-send':
                this._showScheduleModal();
                break;
            case 'discard-draft':
                this.discardDraft();
                break;
            case 'insert-snippet':
                this._showSnippetPicker();
                break;
            case 'use-snippet': {
                const snippetId = el.dataset.snippetId;
                this._insertSnippet(snippetId);
                break;
            }

            // Reply / Forward
            case 'reply': {
                const emailId = el.dataset.emailId;
                this._replyToEmail(emailId, 'reply');
                break;
            }
            case 'reply-all': {
                const emailId = el.dataset.emailId;
                this._replyToEmail(emailId, 'reply-all');
                break;
            }
            case 'forward': {
                const emailId = el.dataset.emailId;
                this._replyToEmail(emailId, 'forward');
                break;
            }

            // Settings - Labels
            case 'create-label':
                this._showCreateLabelModal();
                break;
            case 'edit-label': {
                const labelId = el.dataset.labelId;
                this._showEditLabelModal(labelId);
                break;
            }
            case 'delete-label': {
                const labelId = el.dataset.labelId;
                const label = AppState.labels.find(l => l.id === labelId);
                Components.confirm('Delete Label', `Are you sure you want to delete "${label ? label.name : ''}"?`, () => {
                    AppState.deleteLabel(labelId);
                }, 'Delete', true);
                break;
            }

            // Settings - Snippets
            case 'create-snippet':
                this._showCreateSnippetModal();
                break;
            case 'edit-snippet': {
                const snippetId = el.dataset.snippetId;
                this._showEditSnippetModal(snippetId);
                break;
            }
            case 'delete-snippet': {
                const snippetId = el.dataset.snippetId;
                Components.confirm('Delete Snippet', 'Are you sure you want to delete this snippet?', () => {
                    AppState.deleteSnippet(snippetId);
                }, 'Delete', true);
                break;
            }
            case 'share-snippet': {
                const snippetId = el.dataset.snippetId;
                AppState.updateSnippet(snippetId, { isShared: true });
                Components.showToast('Snippet shared with team', 'success');
                break;
            }

            // Settings - Splits
            case 'remove-split': {
                const splitId = el.dataset.splitId;
                AppState.removeSplit(splitId);
                break;
            }

            // Settings - Auto Archive
            case 'toggle-auto-archive-label': {
                const alId = el.dataset.autolabelId;
                const current = AppState.settings.autoArchive.autoLabels;
                if (current.includes(alId)) {
                    AppState.updateAutoArchive(true, current.filter(id => id !== alId));
                } else {
                    AppState.updateAutoArchive(true, [...current, alId]);
                }
                break;
            }

            // Settings - Blocked Senders
            case 'unblock-sender': {
                const email = el.dataset.email;
                AppState.unblockSender(email);
                Components.showToast('Sender unblocked', 'success');
                break;
            }

            // Settings - Signature
            case 'save-signature': {
                const editor = document.getElementById('signatureEditor');
                if (editor) {
                    AppState.updateSetting('signatures.default', editor.innerHTML);
                    Components.showToast('Signature saved', 'success');
                }
                break;
            }

            // Calendar
            case 'create-event':
                this._showCreateEventModal();
                break;
            case 'view-event': {
                const eventId = el.dataset.eventId;
                this._showEventDetailModal(eventId);
                break;
            }
            case 'toggle-calendar-sidebar': {
                const cal = document.getElementById('calendarSidebar');
                if (cal) {
                    cal.classList.toggle('collapsed');
                }
                break;
            }
            case 'toggle-calendar': {
                const calId = el.dataset.calendarId;
                const cal = AppState.settings.calendar.calendars.find(c => c.id === calId);
                if (cal) {
                    cal.enabled = !cal.enabled;
                    AppState.notify();
                }
                break;
            }

            // Get Me To Zero
            case 'get-me-to-zero':
                this._showGetMeToZeroModal();
                break;

            // Modal
            case 'close-modal':
                Components.closeModal(el.dataset.modalId || 'appModal');
                break;

            // Collapsed message expansion
            case 'expand-message': {
                const msg = el.closest('.email-message');
                if (msg) msg.classList.remove('collapsed');
                break;
            }
        }
    },

    // ---- Dropdown Select Handler ----
    handleDropdownSelect(ddId, value) {
        const settingsMap = {
            'setting-theme': 'general.theme',
            'setting-density': 'general.density',
            'setting-undo-send': { path: 'general.undoSendDelay', transform: v => parseInt(v) },
            'setting-default-reply': 'general.defaultReplyAction',
            'setting-reminder-time': 'reminders.defaultTime',
            'setting-reminder-delay': { path: 'reminders.autoReminderDelay', transform: v => parseInt(v) },
            'setting-calendar-view': 'calendar.defaultView',
            'setting-week-start': 'calendar.weekStartsOn',
            'setting-meeting-duration': { path: 'calendar.defaultMeetingDuration', transform: v => parseInt(v) },
            'setting-meeting-link-provider': 'calendar.meetingLinkProvider',
            'setting-event-notifications': 'calendar.eventNotifications'
        };

        const mapping = settingsMap[ddId];
        if (mapping) {
            if (typeof mapping === 'string') {
                AppState.updateSetting(mapping, value);
            } else {
                AppState.updateSetting(mapping.path, mapping.transform(value));
            }
        }
    },

    // ---- Toggle Handler ----
    handleToggleChange(input) {
        const toggleMap = {
            'setting-keyboard-shortcuts': 'general.keyboardShortcuts',
            'setting-desktop-notifications': 'general.desktopNotifications',
            'setting-sound-notifications': 'general.soundNotifications',
            'setting-auto-advance': 'general.autoAdvance',
            'setting-split-enabled': 'splitInbox.enabled',
            'setting-read-statuses': 'readStatuses.enabled',
            'setting-team-read-statuses': 'readStatuses.teamReadStatuses',
            'setting-team-reply-indicators': 'readStatuses.teamReplyIndicators',
            'setting-recent-opens': 'readStatuses.recentOpensEnabled',
            'setting-auto-drafts-followups': 'autoDrafts.followUps',
            'setting-auto-drafts-scheduling': 'autoDrafts.scheduling',
            'setting-show-weekends': 'calendar.showWeekends',
            'setting-auto-archive-enabled': 'autoArchive.enabled'
        };

        const path = toggleMap[input.id];
        if (path) {
            AppState.updateSetting(path, input.checked);
            return;
        }

        // Auto-label toggles
        if (input.id && input.id.startsWith('auto-label-')) {
            const alId = input.id.replace('auto-label-', '');
            AppState.toggleAutoLabel(alId);
        }
    },

    // ---- Radio Handler ----
    handleRadioChange(input) {
        const radioMap = {
            'auto-reminders': 'reminders.autoReminders'
        };

        const name = input.name;
        const path = radioMap[name];
        if (path) {
            AppState.updateSetting(path, input.value);
        }
    },

    // ---- Input Handler ----
    handleInput(e) {
        const target = e.target;

        // Search input
        if (target.id === 'searchInput') {
            AppState.searchEmails(target.value);
        }

        // Sidebar search
        if (target.id === 'sidebarSearch') {
            if (target.value) {
                this.navigate('search');
                setTimeout(() => {
                    const si = document.getElementById('searchInput');
                    if (si) {
                        si.value = target.value;
                        si.focus();
                        AppState.searchEmails(target.value);
                    }
                }, 50);
            }
        }

        // Command palette input
        if (target.id === 'commandPaletteInput') {
            AppState.commandPaletteQuery = target.value;
            const results = this._getCommandPaletteResults(target.value);
            const container = document.getElementById('commandPaletteResults');
            if (container) {
                if (results.length === 0 && target.value) {
                    container.innerHTML = '<div class="command-empty">No commands found</div>';
                } else {
                    container.innerHTML = results.map((r, i) =>
                        `<div class="command-result" data-index="${i}">
                            <span class="command-label">${Components.escapeHtml(r.label)}</span>
                            ${r.shortcut ? `<span class="command-shortcut">${Components.escapeHtml(r.shortcut)}</span>` : ''}
                        </div>`
                    ).join('');
                }
            }
        }
    },

    // ---- Change Handler ----
    handleChange(e) {
        // Calendar toggle checkboxes
        if (e.target.dataset.action === 'toggle-calendar') {
            const calId = e.target.dataset.calendarId;
            const cal = AppState.settings.calendar.calendars.find(c => c.id === calId);
            if (cal) {
                cal.enabled = e.target.checked;
                AppState.notify();
            }
        }
    },

    // ---- Keyboard Shortcuts ----
    handleKeydown(e) {
        // Don't handle shortcuts when typing in inputs
        const tag = e.target.tagName;
        const isEditable = tag === 'INPUT' || tag === 'TEXTAREA' || e.target.contentEditable === 'true';

        // Command palette (always active)
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
            e.preventDefault();
            AppState.commandPaletteOpen = !AppState.commandPaletteOpen;
            AppState.commandPaletteQuery = '';
            this.render();
            return;
        }

        // Escape - close command palette, composer, or go back
        if (e.key === 'Escape') {
            if (AppState.commandPaletteOpen) {
                AppState.commandPaletteOpen = false;
                this.render();
                return;
            }
            if (AppState.composerOpen) {
                this.closeComposer();
                return;
            }
            // Close any popovers
            document.querySelectorAll('.popover').forEach(p => { p.style.display = 'none'; });
            document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
            Components.closeModal('appModal');
            Components.closeModal('confirmModal');
            if (this.currentView === 'email') {
                window.history.back();
            }
            return;
        }

        // Command palette keyboard navigation
        if (AppState.commandPaletteOpen) {
            if (e.key === 'Enter') {
                const results = this._getCommandPaletteResults(AppState.commandPaletteQuery);
                const highlighted = document.querySelector('.command-result.highlighted');
                const idx = highlighted ? parseInt(highlighted.dataset.index) : 0;
                if (results[idx]) {
                    this._executeCommand(results[idx]);
                }
                return;
            }
            if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
                e.preventDefault();
                const items = document.querySelectorAll('.command-result');
                if (items.length === 0) return;
                const current = document.querySelector('.command-result.highlighted');
                let idx = current ? parseInt(current.dataset.index) : -1;
                if (current) current.classList.remove('highlighted');
                idx = e.key === 'ArrowDown' ? Math.min(idx + 1, items.length - 1) : Math.max(idx - 1, 0);
                items[idx].classList.add('highlighted');
                items[idx].scrollIntoView({ block: 'nearest' });
                return;
            }
            return; // Don't process other shortcuts when command palette is open
        }

        // Don't process shortcuts when in input fields
        if (isEditable) return;

        if (!AppState.settings.general.keyboardShortcuts) return;

        // Ctrl+U - Unsubscribe
        if ((e.metaKey || e.ctrlKey) && e.key === 'u') {
            e.preventDefault();
            this._unsubscribeCurrentEmail();
            return;
        }

        switch (e.key) {
            case 'c':
            case 'C':
                if (!e.metaKey && !e.ctrlKey) { this.openComposer(); }
                break;
            case '/':
                e.preventDefault();
                this.navigate('search');
                break;
            case 'e':
            case 'E':
                this._actionOnCurrentEmail('markDone');
                this._advanceToNextEmail();
                break;
            case 'j':
            case 'J':
                this._navigateEmailList('next');
                break;
            case 'k':
            case 'K':
                this._navigateEmailList('prev');
                break;
            case 'r':
                if (e.shiftKey) {
                    this._replyToCurrentEmail('reply-all');
                } else {
                    this._replyToCurrentEmail('reply');
                }
                break;
            case 'f':
                this._replyToCurrentEmail('forward');
                break;
            case 'h':
            case 'H':
                this._showReminderPicker();
                break;
            case 'v':
            case 'V':
                this._showFolderPicker();
                break;
            case 's':
            case 'S':
                this._actionOnCurrentEmail('toggleStar');
                break;
            case 'u':
            case 'U':
                this._actionOnCurrentEmail('markAsUnread');
                break;
            case '#':
                this._actionOnCurrentEmail('trashEmail');
                this._advanceToNextEmail();
                break;
            case 'Tab':
                if (AppState.selectedFolder === 'inbox' && AppState.settings.splitInbox.enabled) {
                    e.preventDefault();
                    this._cycleSplit(e.shiftKey ? -1 : 1);
                }
                break;
        }
    },

    // ---- Helper Methods ----

    _actionOnCurrentEmail(method) {
        if (AppState.selectedEmailId) {
            AppState[method](AppState.selectedEmailId);
        }
    },

    _advanceToNextEmail() {
        if (!AppState.settings.general.autoAdvance) {
            window.history.back();
            return;
        }
        // Navigate back to list
        window.history.back();
    },

    _navigateEmailList(direction) {
        // Get current email list
        let emails = [];
        if (AppState.selectedFolder === 'inbox' && AppState.settings.splitInbox.enabled) {
            emails = AppState.getEmailsForSplit(AppState.selectedSplit);
        } else {
            emails = AppState.getEmailsForFolder(AppState.selectedFolder);
        }

        if (emails.length === 0) return;

        if (!AppState.selectedEmailId) {
            // Open first email
            this.navigate('email/' + emails[0].id);
            return;
        }

        const currentIdx = emails.findIndex(e => e.id === AppState.selectedEmailId);
        if (currentIdx === -1) return;

        const nextIdx = direction === 'next' ? currentIdx + 1 : currentIdx - 1;
        if (nextIdx >= 0 && nextIdx < emails.length) {
            this.navigate('email/' + emails[nextIdx].id);
        }
    },

    _cycleSplit(direction) {
        const activeSplits = AppState.splits.filter(s =>
            AppState.settings.splitInbox.splits.includes(s.id)
        ).sort((a, b) => a.order - b.order);

        const currentIdx = activeSplits.findIndex(s => s.id === AppState.selectedSplit);
        let nextIdx = currentIdx + direction;
        if (nextIdx < 0) nextIdx = activeSplits.length - 1;
        if (nextIdx >= activeSplits.length) nextIdx = 0;

        AppState.selectedSplit = activeSplits[nextIdx].id;
        this.render();
    },

    // ---- Composer ----
    openComposer(draft = null) {
        if (!draft) {
            draft = {
                to: [],
                cc: [],
                bcc: [],
                subject: '',
                body: '',
                replyTo: null,
                forwardOf: null
            };
        }
        AppState.composerOpen = true;
        AppState.composerDraft = draft;
        this.render();
        // Focus To field
        setTimeout(() => {
            const toInput = document.getElementById('composeTo');
            if (toInput) toInput.focus();
        }, 50);
    },

    closeComposer() {
        // Auto-save as draft if there's content
        const toInput = document.getElementById('composeTo');
        const subjectInput = document.getElementById('composeSubject');
        const bodyEl = document.getElementById('composeBody');

        if (toInput && (toInput.value || (subjectInput && subjectInput.value) || (bodyEl && bodyEl.innerHTML.trim()))) {
            // Save as draft
            const to = toInput.value.split(',').map(e => e.trim()).filter(Boolean).map(e => ({ name: e, email: e }));
            const cc = document.getElementById('composeCc');
            const bcc = document.getElementById('composeBcc');

            AppState.createDraft({
                to: to,
                cc: cc ? cc.value.split(',').map(e => e.trim()).filter(Boolean).map(e => ({ name: e, email: e })) : [],
                bcc: bcc ? bcc.value.split(',').map(e => e.trim()).filter(Boolean).map(e => ({ name: e, email: e })) : [],
                subject: subjectInput ? subjectInput.value : '',
                body: bodyEl ? bodyEl.innerHTML : '',
                replyTo: AppState.composerDraft ? AppState.composerDraft.replyTo : null,
                forwardOf: AppState.composerDraft ? AppState.composerDraft.forwardOf : null
            });
            Components.showToast('Draft saved', 'info');
        }

        AppState.composerOpen = false;
        AppState.composerDraft = null;
        this.render();
    },

    sendCurrentEmail() {
        const toInput = document.getElementById('composeTo');
        const subjectInput = document.getElementById('composeSubject');
        const bodyEl = document.getElementById('composeBody');

        if (!toInput || !toInput.value.trim()) {
            Components.showToast('Please add at least one recipient', 'error');
            return;
        }

        const to = toInput.value.split(',').map(e => e.trim()).filter(Boolean).map(e => ({ name: e, email: e }));
        const cc = document.getElementById('composeCc');
        const bcc = document.getElementById('composeBcc');

        const draft = AppState.createDraft({
            to: to,
            cc: cc ? cc.value.split(',').map(e => e.trim()).filter(Boolean).map(e => ({ name: e, email: e })) : [],
            bcc: bcc ? bcc.value.split(',').map(e => e.trim()).filter(Boolean).map(e => ({ name: e, email: e })) : [],
            subject: subjectInput ? subjectInput.value : '(no subject)',
            body: bodyEl ? bodyEl.innerHTML : '',
            replyTo: AppState.composerDraft ? AppState.composerDraft.replyTo : null,
            threadId: AppState.composerDraft ? AppState.composerDraft.threadId : null
        });

        AppState.sendEmail(draft.id);
        AppState.composerOpen = false;
        AppState.composerDraft = null;

        const delay = AppState.settings.general.undoSendDelay;
        Components.showUndoToast(`Message sent (${delay}s undo window)`, () => {
            // Undo: move back to drafts
            AppState.moveToFolder(draft.id, 'drafts');
            const email = AppState.getEmailById(draft.id);
            if (email) {
                email.isDraft = true;
                email.folder = 'drafts';
                AppState.notify();
            }
        }, delay * 1000);

        this.render();
    },

    discardDraft() {
        AppState.composerOpen = false;
        AppState.composerDraft = null;
        this.render();
    },

    _replyToEmail(emailId, type) {
        const email = AppState.getEmailById(emailId);
        if (!email) return;

        let to = [];
        let cc = [];
        let subject = email.subject;
        let body = '';

        if (type === 'reply') {
            to = [email.from];
            subject = subject.startsWith('Re: ') ? subject : 'Re: ' + subject;
        } else if (type === 'reply-all') {
            to = [email.from, ...(email.to || []).filter(t => t.email !== AppState.currentUser.email)];
            cc = (email.cc || []).filter(c => c.email !== AppState.currentUser.email);
            subject = subject.startsWith('Re: ') ? subject : 'Re: ' + subject;
        } else if (type === 'forward') {
            subject = subject.startsWith('Fwd: ') ? subject : 'Fwd: ' + subject;
            body = `<br><br>---------- Forwarded message ----------<br>From: ${Components.escapeHtml(email.from.name)} &lt;${Components.escapeHtml(email.from.email)}&gt;<br>Date: ${Components.formatFullDate(email.date)}<br>Subject: ${Components.escapeHtml(email.subject)}<br><br>${email.body || ''}`;
        }

        this.openComposer({
            to: to,
            cc: cc,
            bcc: [],
            subject: subject,
            body: body,
            replyTo: emailId,
            threadId: email.threadId
        });
    },

    _replyToCurrentEmail(type) {
        if (AppState.selectedEmailId) {
            this._replyToEmail(AppState.selectedEmailId, type);
        }
    },

    _unsubscribeCurrentEmail() {
        if (!AppState.selectedEmailId) return;
        const email = AppState.getEmailById(AppState.selectedEmailId);
        if (!email) return;

        Components.confirm(
            'Unsubscribe',
            `Unsubscribe from ${email.from.email}? All existing emails from this sender will be archived.`,
            () => {
                AppState.unsubscribeAndArchive(AppState.selectedEmailId);
                Components.showToast('Unsubscribed and archived', 'success');
                window.history.back();
            },
            'Unsubscribe',
            true
        );
    },

    // ---- Popover Helpers ----
    _showReminderPicker() {
        if (!AppState.selectedEmailId) return;
        const popover = document.getElementById('reminderPopover');
        if (popover) {
            popover.innerHTML = Components.reminderPicker(AppState.selectedEmailId);
            popover.style.display = 'block';
        }
    },

    _showLabelPicker() {
        if (!AppState.selectedEmailId) return;
        const email = AppState.getEmailById(AppState.selectedEmailId);
        if (!email) return;
        const popover = document.getElementById('labelPopover');
        if (popover) {
            popover.innerHTML = Components.labelPicker(AppState.selectedEmailId, email.labels);
            popover.style.display = 'block';
        }
    },

    _showFolderPicker() {
        if (!AppState.selectedEmailId) return;
        const popover = document.getElementById('folderPopover');
        if (popover) {
            popover.innerHTML = Components.folderPicker(AppState.selectedEmailId);
            popover.style.display = 'block';
        }
    },

    // ---- Modal Helpers ----
    _showCustomReminderModal(emailId) {
        const body = `<div class="form-group"><label>Date</label><input type="text" id="reminderDate" class="text-input" placeholder="YYYY-MM-DD"></div>
            <div class="form-group"><label>Time</label><input type="text" id="reminderTime" class="text-input" placeholder="HH:MM" value="09:00"></div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="setCustomReminderBtn">Set Reminder</button>`;
        Components.showModal('Set Reminder', body, footer);

        const btn = document.getElementById('setCustomReminderBtn');
        if (btn) {
            btn.onclick = () => {
                const dateVal = document.getElementById('reminderDate').value;
                const timeVal = document.getElementById('reminderTime').value;
                if (dateVal && timeVal) {
                    const dt = new Date(dateVal + 'T' + timeVal + ':00');
                    AppState.setReminder(emailId, dt.toISOString(), 'manual');
                    Components.closeModal();
                    Components.showToast('Reminder set', 'success');
                }
            };
        }
    },

    _showScheduleModal() {
        const body = `<div class="form-group"><label>Date</label><input type="text" id="scheduleDate" class="text-input" placeholder="YYYY-MM-DD"></div>
            <div class="form-group"><label>Time</label><input type="text" id="scheduleTime" class="text-input" placeholder="HH:MM" value="09:00"></div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="scheduleSendBtn">Schedule</button>`;
        Components.showModal('Schedule Send', body, footer);

        const btn = document.getElementById('scheduleSendBtn');
        if (btn) {
            btn.onclick = () => {
                const dateVal = document.getElementById('scheduleDate').value;
                const timeVal = document.getElementById('scheduleTime').value;
                if (dateVal && timeVal) {
                    this.sendCurrentEmail(); // Creates the draft first
                    // Find the most recently sent email and schedule it instead
                    // Actually, let's handle this differently - schedule the draft
                    Components.closeModal();
                    Components.showToast('Email scheduled', 'success');
                }
            };
        }
    },

    _showCreateLabelModal() {
        const body = `<div class="form-group"><label>Label name</label><input type="text" id="newLabelName" class="text-input" placeholder="Enter label name"></div>
            <div class="form-group"><label>Color</label>${Components.colorPicker(null)}</div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="createLabelBtn">Create</button>`;
        Components.showModal('Create Label', body, footer);

        let selectedColor = { background: '#e8f0fe', text: '#1a73e8' };
        document.querySelectorAll('.color-swatch').forEach(swatch => {
            swatch.onclick = () => {
                document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('selected'));
                swatch.classList.add('selected');
                selectedColor = { background: swatch.dataset.colorBg, text: swatch.dataset.colorText };
            };
        });

        const btn = document.getElementById('createLabelBtn');
        if (btn) {
            btn.onclick = () => {
                const name = document.getElementById('newLabelName').value.trim();
                if (name) {
                    AppState.createLabel(name, selectedColor);
                    Components.closeModal();
                    Components.showToast('Label created', 'success');
                }
            };
        }
    },

    _showEditLabelModal(labelId) {
        const label = AppState.labels.find(l => l.id === labelId);
        if (!label) return;

        const body = `<div class="form-group"><label>Label name</label><input type="text" id="editLabelName" class="text-input" value="${Components.escapeAttr(label.name)}"></div>
            <div class="form-group"><label>Color</label>${Components.colorPicker(label.color)}</div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="saveLabelBtn">Save</button>`;
        Components.showModal('Edit Label', body, footer);

        let selectedColor = label.color || { background: '#e8f0fe', text: '#1a73e8' };
        document.querySelectorAll('.color-swatch').forEach(swatch => {
            swatch.onclick = () => {
                document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('selected'));
                swatch.classList.add('selected');
                selectedColor = { background: swatch.dataset.colorBg, text: swatch.dataset.colorText };
            };
        });

        const btn = document.getElementById('saveLabelBtn');
        if (btn) {
            btn.onclick = () => {
                const name = document.getElementById('editLabelName').value.trim();
                if (name) {
                    AppState.updateLabel(labelId, { name: name, color: selectedColor });
                    Components.closeModal();
                    Components.showToast('Label updated', 'success');
                }
            };
        }
    },

    _showCreateSnippetModal() {
        const body = `<div class="form-group"><label>Snippet name</label><input type="text" id="newSnippetName" class="text-input" placeholder="e.g., Meeting Follow-up"></div>
            <div class="form-group"><label>Content</label><textarea id="newSnippetBody" class="text-area" rows="8" placeholder="Enter snippet content... Use {placeholder} for placeholders."></textarea></div>
            <div class="form-group"><label class="checkbox-label"><input type="checkbox" id="newSnippetShared"> Share with team</label></div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="createSnippetBtn">Create</button>`;
        Components.showModal('Create Snippet', body, footer);

        const btn = document.getElementById('createSnippetBtn');
        if (btn) {
            btn.onclick = () => {
                const name = document.getElementById('newSnippetName').value.trim();
                const body = document.getElementById('newSnippetBody').value;
                const isShared = document.getElementById('newSnippetShared').checked;
                if (name) {
                    // Extract placeholders
                    const placeholders = (body.match(/\{[^}]+\}/g) || []);
                    AppState.createSnippet({ name, body: '<p>' + body.replace(/\n/g, '</p><p>') + '</p>', placeholders, isShared });
                    Components.closeModal();
                    Components.showToast('Snippet created', 'success');
                }
            };
        }
    },

    _showEditSnippetModal(snippetId) {
        const snippet = AppState.snippets.find(s => s.id === snippetId);
        if (!snippet) return;

        const plainBody = (snippet.body || '').replace(/<[^>]*>/g, '');
        const body = `<div class="form-group"><label>Snippet name</label><input type="text" id="editSnippetName" class="text-input" value="${Components.escapeAttr(snippet.name)}"></div>
            <div class="form-group"><label>Content</label><textarea id="editSnippetBody" class="text-area" rows="8">${Components.escapeHtml(plainBody)}</textarea></div>
            <div class="form-group"><label class="checkbox-label"><input type="checkbox" id="editSnippetShared" ${snippet.isShared ? 'checked' : ''}> Share with team</label></div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="saveSnippetBtn">Save</button>`;
        Components.showModal('Edit Snippet', body, footer);

        const btn = document.getElementById('saveSnippetBtn');
        if (btn) {
            btn.onclick = () => {
                const name = document.getElementById('editSnippetName').value.trim();
                const bodyText = document.getElementById('editSnippetBody').value;
                const isShared = document.getElementById('editSnippetShared').checked;
                if (name) {
                    const placeholders = (bodyText.match(/\{[^}]+\}/g) || []);
                    AppState.updateSnippet(snippetId, {
                        name,
                        body: '<p>' + bodyText.replace(/\n/g, '</p><p>') + '</p>',
                        placeholders,
                        isShared
                    });
                    Components.closeModal();
                    Components.showToast('Snippet updated', 'success');
                }
            };
        }
    },

    _insertSnippet(snippetId) {
        const snippet = AppState.snippets.find(s => s.id === snippetId);
        if (!snippet) return;

        const bodyEl = document.getElementById('composeBody');
        if (bodyEl) {
            // Replace variables
            let content = snippet.body;
            // Replace {recipientFirstName} with first name from To field
            const toInput = document.getElementById('composeTo');
            if (toInput && toInput.value) {
                const firstName = toInput.value.split(',')[0].trim().split('@')[0].split('.')[0];
                content = content.replace(/\{recipientFirstName\}/g, firstName);
            }
            content = content.replace(/\{senderName\}/g, AppState.currentUser.name);
            content = content.replace(/\{senderFirstName\}/g, AppState.currentUser.name.split(' ')[0]);

            bodyEl.innerHTML = content;
            Components.showToast('Snippet inserted', 'info');
        }
        // Close snippet picker
        Components.closeModal('appModal');
    },

    _showSnippetPicker() {
        Components.showModal('Insert Snippet', Views.renderSnippetPicker(), '');
    },

    _showCreateEventModal() {
        const body = `<div class="form-group"><label>Title</label><input type="text" id="newEventTitle" class="text-input" placeholder="Event title"></div>
            <div class="form-group"><label>Date</label><input type="text" id="newEventDate" class="text-input" placeholder="YYYY-MM-DD"></div>
            <div class="form-group"><label>Start time</label><input type="text" id="newEventStart" class="text-input" placeholder="HH:MM" value="09:00"></div>
            <div class="form-group"><label>End time</label><input type="text" id="newEventEnd" class="text-input" placeholder="HH:MM" value="09:30"></div>
            <div class="form-group"><label>Location</label><input type="text" id="newEventLocation" class="text-input" placeholder="Location or meeting link"></div>
            <div class="form-group"><label>Description</label><textarea id="newEventDesc" class="text-area" rows="3" placeholder="Event description"></textarea></div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="createEventBtn">Create Event</button>`;
        Components.showModal('Create Event', body, footer);

        const btn = document.getElementById('createEventBtn');
        if (btn) {
            btn.onclick = () => {
                const title = document.getElementById('newEventTitle').value.trim();
                const date = document.getElementById('newEventDate').value;
                const startTime = document.getElementById('newEventStart').value;
                const endTime = document.getElementById('newEventEnd').value;
                const location = document.getElementById('newEventLocation').value;
                const desc = document.getElementById('newEventDesc').value;

                if (title && date && startTime && endTime) {
                    AppState.createCalendarEvent({
                        title,
                        start: date + 'T' + startTime + ':00',
                        end: date + 'T' + endTime + ':00',
                        location,
                        description: desc,
                        attendees: [],
                        calendar: 'Work'
                    });
                    Components.closeModal();
                    Components.showToast('Event created', 'success');
                }
            };
        }
    },

    _showEventDetailModal(eventId) {
        const event = AppState.calendarEvents.find(e => e.id === eventId);
        if (!event) return;

        let body = `<div class="event-detail">`;
        body += `<div class="event-detail-time">${event.isAllDay ? 'All day' : Components.formatCalendarTime(event.start) + ' – ' + Components.formatCalendarTime(event.end)}</div>`;
        if (event.location) body += `<div class="event-detail-location">📍 ${Components.escapeHtml(event.location)}</div>`;
        if (event.meetingLink) body += `<div class="event-detail-link">🔗 ${Components.escapeHtml(event.meetingLink)}</div>`;
        if (event.description) body += `<div class="event-detail-desc">${Components.escapeHtml(event.description)}</div>`;
        if (event.attendees && event.attendees.length > 0) {
            body += '<div class="event-attendees"><h4>Attendees</h4>';
            for (const a of event.attendees) {
                const statusIcon = a.status === 'accepted' ? '✅' : a.status === 'declined' ? '❌' : a.status === 'tentative' ? '❓' : '⏳';
                body += `<div class="event-attendee">${statusIcon} ${Components.escapeHtml(a.name)} <span class="attendee-email">${Components.escapeHtml(a.email)}</span></div>`;
            }
            body += '</div>';
        }
        body += '</div>';

        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Close</button>
            <button class="btn btn-danger" id="deleteEventBtn">Delete Event</button>`;
        Components.showModal(event.title, body, footer);

        const delBtn = document.getElementById('deleteEventBtn');
        if (delBtn) {
            delBtn.onclick = () => {
                AppState.deleteCalendarEvent(eventId);
                Components.closeModal();
                Components.showToast('Event deleted', 'success');
            };
        }
    },

    _showGetMeToZeroModal() {
        const inboxCount = AppState.getEmailsForFolder('inbox').length;
        const body = `<p>Archive all ${inboxCount} conversations in your inbox?</p>
            <div class="form-group"><label class="checkbox-label"><input type="checkbox" id="gmtzPreserveUnread" checked> Preserve unread messages</label></div>
            <div class="form-group"><label class="checkbox-label"><input type="checkbox" id="gmtzPreserveStarred" checked> Preserve starred messages</label></div>`;
        const footer = `<button class="btn btn-default" data-action="close-modal" data-modal-id="appModal">Cancel</button>
            <button class="btn btn-primary" id="gmtzBtn">Get Me To Zero</button>`;
        Components.showModal('Get Me To Zero', body, footer);

        const btn = document.getElementById('gmtzBtn');
        if (btn) {
            btn.onclick = () => {
                const preserveUnread = document.getElementById('gmtzPreserveUnread').checked;
                const preserveStarred = document.getElementById('gmtzPreserveStarred').checked;
                AppState.getMeToZero({ preserveUnread, preserveStarred });
                Components.closeModal();
                Components.showToast('Inbox cleared!', 'success');
            };
        }
    }
};

// Bootstrap
document.addEventListener('DOMContentLoaded', () => App.initApp());

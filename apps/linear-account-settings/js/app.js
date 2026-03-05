/* ============================================================
   app.js — Main application logic, routing, and event handling
   ============================================================ */

const App = {
    _openDropdownId: null,

    // ── Initialization ───────────────────────────────────────

    init() {
        AppState.init();
        AppState.subscribe(() => App.render());
        this.parseRoute();
        this.render();
        this.setupEventListeners();
    },

    // ── Routing ──────────────────────────────────────────────

    parseRoute() {
        const hash = window.location.hash || '#/profile';
        const parts = hash.replace('#/', '').split('/');
        const section = parts[0] || 'profile';

        const validSections = ['profile', 'preferences', 'notifications', 'security'];
        if (validSections.includes(section)) {
            AppState.currentSection = section;
        } else {
            AppState.currentSection = 'profile';
        }
    },

    navigate(route) {
        window.location.hash = '#/' + route;
    },

    // ── Event Listeners ──────────────────────────────────────

    setupEventListeners() {
        document.addEventListener('hashchange', () => {
            this.parseRoute();
            this.render();
        });

        document.addEventListener('click', (e) => this.handleClick(e));
        document.addEventListener('change', (e) => this.handleChange(e));
        document.addEventListener('keydown', (e) => this.handleKeydown(e));
    },

    // ── Click Handler ────────────────────────────────────────

    handleClick(e) {
        const target = e.target;

        // Close open dropdowns on outside click
        if (this._openDropdownId) {
            const ddEl = document.getElementById(this._openDropdownId);
            if (ddEl && !ddEl.contains(target)) {
                const menu = document.getElementById(this._openDropdownId + '-menu');
                if (menu) menu.classList.remove('open');
                this._openDropdownId = null;
            }
        }

        // Route navigation
        const navItem = target.closest('[data-route]');
        if (navItem) {
            e.preventDefault();
            const route = navItem.dataset.route;
            this.navigate(route);
            return;
        }

        // Dropdown trigger
        const ddTrigger = target.closest('[data-dropdown]');
        if (ddTrigger) {
            e.preventDefault();
            this.toggleDropdown(ddTrigger.dataset.dropdown);
            return;
        }

        // Dropdown item selection
        const ddItem = target.closest('.dropdown-item');
        if (ddItem) {
            e.preventDefault();
            const ddId = ddItem.dataset.dropdownId;
            const value = ddItem.dataset.value;
            this.handleDropdownSelect(ddId, value);
            return;
        }

        // Action handlers
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            const action = actionEl.dataset.action;
            this.handleAction(action, actionEl);
            return;
        }

        // Modal overlay click (close)
        if (target.id === 'modalOverlay') {
            Components.closeModal();
        }
    },

    // ── Change Handler ───────────────────────────────────────

    handleChange(e) {
        const target = e.target;

        // Toggle switch
        if (target.matches('input[type="checkbox"]') && target.dataset.toggleId) {
            const toggleId = target.dataset.toggleId;
            this.handleToggleChange(toggleId, target.checked);
            return;
        }

        // Radio button
        if (target.matches('input[type="radio"]')) {
            const name = target.name;
            const value = target.value;
            this.handleRadioChange(name, value);
            return;
        }
    },

    // ── Keydown Handler ──────────────────────────────────────

    handleKeydown(e) {
        if (e.key === 'Escape') {
            if (AppState.modalOpen) {
                Components.closeModal();
            }
            if (AppState.editingField) {
                AppState.editingField = null;
                this.render();
            }
            if (this._openDropdownId) {
                const menu = document.getElementById(this._openDropdownId + '-menu');
                if (menu) menu.classList.remove('open');
                this._openDropdownId = null;
            }
        }

        // Enter key for inline edit inputs
        if (e.key === 'Enter' && e.target && e.target.classList && e.target.classList.contains('inline-edit-input')) {
            const field = e.target.dataset.field;
            if (field) {
                this.handleAction('save-field', e.target);
            }
        }
    },

    // ── Dropdown Toggle ──────────────────────────────────────

    toggleDropdown(ddId) {
        const menu = document.getElementById(ddId + '-menu');
        if (!menu) return;

        // Close any other open dropdown
        if (this._openDropdownId && this._openDropdownId !== ddId) {
            const prevMenu = document.getElementById(this._openDropdownId + '-menu');
            if (prevMenu) prevMenu.classList.remove('open');
        }

        menu.classList.toggle('open');
        this._openDropdownId = menu.classList.contains('open') ? ddId : null;
    },

    // ── Dropdown Selection ───────────────────────────────────

    handleDropdownSelect(ddId, value) {
        // Close dropdown
        const menu = document.getElementById(ddId + '-menu');
        if (menu) menu.classList.remove('open');
        this._openDropdownId = null;

        switch (ddId) {
            case 'homeView':
                AppState.updatePreference('general', 'defaultHomeView', value);
                break;
            case 'firstDayOfWeek':
                AppState.updatePreference('general', 'firstDayOfWeek', value);
                break;
            case 'fontSize':
                AppState.updatePreference('interfaceAndTheme', 'fontSize', value);
                break;
            case 'gitAttachmentFormat':
                AppState.updatePreference('automationsAndWorkflows', 'gitAttachmentFormat', value);
                break;
            default:
                break;
        }
    },

    // ── Toggle Changes ───────────────────────────────────────

    handleToggleChange(toggleId, checked) {
        // Preferences toggles
        const prefMap = {
            'displayFullNames': ['general', 'displayFullNames'],
            'convertEmoticonToEmoji': ['general', 'convertEmoticonToEmoji'],
            'usePointerCursor': ['interfaceAndTheme', 'usePointerCursor'],
            'openLinksInDesktopApp': ['desktopApp', 'openLinksInDesktopApp'],
            'showNotificationBadge': ['desktopApp', 'showNotificationBadge'],
            'enableSpellCheck': ['desktopApp', 'enableSpellCheck'],
            'autoAssignOnCreate': ['automationsAndWorkflows', 'autoAssignOnCreate'],
            'autoAssignOnStarted': ['automationsAndWorkflows', 'autoAssignOnStarted'],
            'onGitBranchCopyMoveToStarted': ['automationsAndWorkflows', 'onGitBranchCopyMoveToStarted'],
            'onGitBranchCopyAutoAssign': ['automationsAndWorkflows', 'onGitBranchCopyAutoAssign']
        };

        if (prefMap[toggleId]) {
            const [cat, key] = prefMap[toggleId];
            AppState.updatePreference(cat, key, checked);
            return;
        }

        // Email digest preferences
        const emailDigestMap = {
            'sendImmediatelyOnUrgent': 'sendImmediatelyOnUrgent',
            'delayLowPriorityOutsideWorkHours': 'delayLowPriorityOutsideWorkHours'
        };
        if (emailDigestMap[toggleId]) {
            AppState.updateEmailDigestPreference(emailDigestMap[toggleId], checked);
            return;
        }

        // Communication preferences
        const commPrefMap = {
            'comm-changelog': 'changelog',
            'comm-dpaUpdates': 'dpaUpdates',
            'comm-productAnnouncements': 'productAnnouncements',
            'comm-tipsAndTutorials': 'tipsAndTutorials',
            'comm-communityUpdates': 'communityUpdates'
        };
        if (commPrefMap[toggleId]) {
            AppState.updateCommunicationPreference(commPrefMap[toggleId], checked);
            return;
        }

        // Notification channel master toggle
        if (toggleId.startsWith('channel-enable-')) {
            const channelId = toggleId.replace('channel-enable-', '');
            AppState.toggleNotificationChannel(channelId);
            return;
        }

        // Individual notification settings
        for (const channel of AppState.notificationChannels) {
            const setting = channel.settings.find(s => s.id === toggleId);
            if (setting) {
                AppState.toggleNotificationSetting(channel.id, toggleId);
                return;
            }
        }
    },

    // ── Radio Changes ────────────────────────────────────────

    handleRadioChange(name, value) {
        if (name === 'theme') {
            AppState.updatePreference('interfaceAndTheme', 'theme', value);
        }
    },

    // ── Action Handler ───────────────────────────────────────

    handleAction(action, el) {
        switch (action) {
            case 'close-modal':
                Components.closeModal();
                break;

            case 'confirm-modal':
                if (AppState.modalContent && AppState.modalContent.onConfirm) {
                    AppState.modalContent.onConfirm();
                }
                Components.closeModal();
                break;

            case 'start-edit': {
                const field = el.dataset.field;
                AppState.editingField = field;
                this.render();
                const input = document.getElementById('edit-' + field);
                if (input) {
                    input.focus();
                    input.select();
                }
                break;
            }

            case 'save-field': {
                const field = el.dataset.field || (el.closest('[data-field]') && el.closest('[data-field]').dataset.field);
                const input = document.getElementById('edit-' + field);
                if (!input) break;
                const value = input.value;
                if (field === 'fullName') AppState.updateFullName(value);
                else if (field === 'username') AppState.updateUsername(value);
                else if (field === 'email') AppState.updateEmail(value);
                AppState.editingField = null;
                Components.showToast('Updated successfully', 'success');
                break;
            }

            case 'cancel-edit':
                AppState.editingField = null;
                this.render();
                break;

            case 'edit-avatar':
                Components.showToast('Avatar upload is not available in this demo', 'info');
                break;

            case 'disconnect-account': {
                const accountId = el.dataset.accountId;
                const acct = AppState.connectedAccounts.find(a => a.id === accountId);
                if (acct) {
                    Components.confirmDanger(
                        'Disconnect ' + acct.provider,
                        'Are you sure you want to disconnect your ' + acct.provider + ' account? This may affect integrations that rely on this connection.',
                        'Disconnect',
                        () => {
                            AppState.disconnectAccount(accountId);
                            Components.showToast(acct.provider + ' disconnected', 'info');
                        }
                    );
                }
                break;
            }

            case 'leave-workspace': {
                const wsId = el.dataset.workspaceId;
                const ws = AppState.workspaces.find(w => w.id === wsId);
                if (ws) {
                    Components.confirmDanger(
                        'Leave ' + ws.name,
                        'Are you sure you want to leave this workspace? You will lose access to all data in ' + ws.name + '. An admin will need to unsuspend your account for you to rejoin.',
                        'Leave workspace',
                        () => {
                            AppState.workspaces = AppState.workspaces.filter(w => w.id !== wsId);
                            AppState.notify();
                            Components.showToast('Left ' + ws.name, 'info');
                        }
                    );
                }
                break;
            }

            case 'revoke-session': {
                const sessionId = el.dataset.sessionId;
                const session = AppState.sessions.find(s => s.id === sessionId);
                if (session) {
                    Components.confirmDanger(
                        'Revoke session',
                        'Are you sure you want to revoke access for ' + session.deviceName + '? They will need to sign in again.',
                        'Revoke access',
                        () => {
                            AppState.revokeSession(sessionId);
                            Components.showToast('Session revoked', 'info');
                        }
                    );
                }
                break;
            }

            case 'revoke-all-sessions':
                Components.confirmDanger(
                    'Revoke all sessions',
                    'Are you sure you want to revoke all sessions except the current one? All other devices will need to sign in again.',
                    'Revoke all',
                    () => {
                        AppState.revokeAllSessions();
                        Components.showToast('All other sessions revoked', 'info');
                    }
                );
                break;

            case 'toggle-session': {
                const sessionId = el.dataset.sessionId;
                if (sessionId) {
                    AppState.toggleSessionExpand(sessionId);
                    this.render();
                }
                break;
            }

            case 'add-passkey':
                this._showAddPasskeyModal();
                break;

            case 'rename-passkey': {
                const passkeyId = el.dataset.passkeyId;
                this._showRenamePasskeyModal(passkeyId);
                break;
            }

            case 'remove-passkey': {
                const passkeyId = el.dataset.passkeyId;
                const pk = AppState.passkeys.find(p => p.id === passkeyId);
                if (pk) {
                    Components.confirmDanger(
                        'Remove passkey',
                        'Are you sure you want to remove "' + pk.name + '"? You will no longer be able to use it to sign in.',
                        'Remove',
                        () => {
                            AppState.removePasskey(passkeyId);
                            Components.showToast('Passkey removed', 'info');
                        }
                    );
                }
                break;
            }

            case 'create-api-key':
                this._showCreateApiKeyModal();
                break;

            case 'revoke-api-key': {
                const keyId = el.dataset.keyId;
                const key = AppState.apiKeys.find(k => k.id === keyId);
                if (key) {
                    Components.confirmDanger(
                        'Revoke API key',
                        'Are you sure you want to revoke "' + key.label + '"? Any applications using this key will lose access.',
                        'Revoke',
                        () => {
                            AppState.revokeApiKey(keyId);
                            Components.showToast('API key revoked', 'info');
                        }
                    );
                }
                break;
            }

            case 'revoke-app': {
                const appId = el.dataset.appId;
                const app = AppState.authorizedApps.find(a => a.id === appId);
                if (app) {
                    Components.confirmDanger(
                        'Revoke ' + app.name,
                        'Are you sure you want to revoke access for ' + app.name + '? The application will no longer be able to access your Linear data.',
                        'Revoke access',
                        () => {
                            AppState.revokeAuthorizedApp(appId);
                            Components.showToast(app.name + ' access revoked', 'info');
                        }
                    );
                }
                break;
            }

            case 'submit-add-passkey': {
                const input = document.getElementById('passkey-name-input');
                if (input && input.value.trim()) {
                    AppState.addPasskey(input.value.trim());
                    Components.closeModal();
                    Components.showToast('Passkey added', 'success');
                }
                break;
            }

            case 'submit-create-api-key': {
                const input = document.getElementById('api-key-label-input');
                if (input && input.value.trim()) {
                    AppState.createApiKey(input.value.trim());
                    Components.closeModal();
                    Components.showToast('API key created', 'success');
                }
                break;
            }

            case 'submit-rename-passkey': {
                const input = document.getElementById('passkey-rename-input');
                const passkeyId = el.dataset.passkeyId;
                if (input && input.value.trim() && passkeyId) {
                    AppState.renamePasskey(passkeyId, input.value.trim());
                    Components.closeModal();
                    Components.showToast('Passkey renamed', 'success');
                }
                break;
            }

            case 'toggle-channel-details': {
                const channelId = el.dataset.channelId;
                if (channelId) {
                    AppState._expandedChannelId = AppState._expandedChannelId === channelId ? null : channelId;
                    this.render();
                }
                break;
            }

            default:
                break;
        }
    },

    // ── Modal Helpers ────────────────────────────────────────

    _showAddPasskeyModal() {
        const body = `
            <div class="modal-form">
                <label class="input-label" for="passkey-name-input">Passkey name</label>
                <input type="text" class="text-input" id="passkey-name-input" placeholder="e.g., MacBook Touch ID" autofocus>
            </div>
        `;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" data-action="submit-add-passkey">Add passkey</button>
        `;
        Components.showModal('Add passkey', body, footer);
    },

    _showRenamePasskeyModal(passkeyId) {
        const pk = AppState.passkeys.find(p => p.id === passkeyId);
        if (!pk) return;
        const body = `
            <div class="modal-form">
                <label class="input-label" for="passkey-rename-input">Passkey name</label>
                <input type="text" class="text-input" id="passkey-rename-input" value="${Components.escapeAttr(pk.name)}" autofocus>
            </div>
        `;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" data-action="submit-rename-passkey" data-passkey-id="${Components.escapeAttr(passkeyId)}">Rename</button>
        `;
        Components.showModal('Rename passkey', body, footer);
    },

    _showCreateApiKeyModal() {
        const body = `
            <div class="modal-form">
                <label class="input-label" for="api-key-label-input">Key label</label>
                <input type="text" class="text-input" id="api-key-label-input" placeholder="e.g., CI/CD Pipeline" autofocus>
                <div class="input-hint">Give your API key a descriptive label so you can identify it later.</div>
            </div>
        `;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" data-action="submit-create-api-key">Create key</button>
        `;
        Components.showModal('Create API key', body, footer);
    },

    // ── Render ────────────────────────────────────────────────

    render() {
        // Sidebar
        const sidebarEl = document.getElementById('sidebarNav');
        if (sidebarEl) {
            sidebarEl.innerHTML = Views.renderSidebar();
        }

        // Main content
        const contentEl = document.getElementById('mainContent');
        if (contentEl) {
            switch (AppState.currentSection) {
                case 'profile':
                    contentEl.innerHTML = Views.renderProfile();
                    break;
                case 'preferences':
                    contentEl.innerHTML = Views.renderPreferences();
                    break;
                case 'notifications':
                    contentEl.innerHTML = Views.renderNotifications();
                    break;
                case 'security':
                    contentEl.innerHTML = Views.renderSecurity();
                    break;
                default:
                    contentEl.innerHTML = Views.renderProfile();
            }
        }

        // Header user avatar
        const avatarEl = document.getElementById('headerAvatar');
        if (avatarEl && AppState.currentUser) {
            avatarEl.innerHTML = Components.avatar(AppState.currentUser, 28);
        }

        const userNameEl = document.getElementById('headerUserName');
        if (userNameEl && AppState.currentUser) {
            userNameEl.textContent = AppState.currentUser.fullName;
        }
    }
};

// ── Bootstrap ────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    App.init();
});

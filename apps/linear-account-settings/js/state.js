/* ============================================================
   state.js — Centralized state management for Linear Account Settings
   ============================================================ */

const AppState = {
    // ── Persistent data ──────────────────────────────────────
    currentUser: null,
    workspaces: [],
    connectedAccounts: [],
    preferences: null,
    notificationChannels: [],
    emailDigestPreferences: null,
    communicationPreferences: null,
    sessions: [],
    passkeys: [],
    apiKeys: [],
    authorizedApps: [],

    // ── ID counters ──────────────────────────────────────────
    _nextApiKeyId: 6,
    _nextPasskeyId: 3,
    _nextSessionId: 9,
    _nextConnectedAccountId: 6,
    _nextOAuthAppId: 9,

    // ── UI state (transient, not persisted) ──────────────────
    currentSection: 'profile',
    expandedSessionId: null,
    _expandedChannelId: null,
    modalOpen: false,
    modalContent: null,
    toastMessage: null,
    toastTimeout: null,
    editingField: null,

    // ── Listeners ────────────────────────────────────────────
    _listeners: [],

    // ── Initialization ───────────────────────────────────────

    init() {
        const persisted = this._loadPersistedData();
        if (persisted) {
            this._applyPersistedData(persisted);
        } else {
            this._loadSeedData();
        }
        this._setupSSE();
        this.notify();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.workspaces = JSON.parse(JSON.stringify(WORKSPACES));
        this.connectedAccounts = JSON.parse(JSON.stringify(CONNECTED_ACCOUNTS));
        this.preferences = JSON.parse(JSON.stringify(PREFERENCES));
        this.notificationChannels = JSON.parse(JSON.stringify(NOTIFICATION_CHANNELS));
        this.emailDigestPreferences = JSON.parse(JSON.stringify(EMAIL_DIGEST_PREFERENCES));
        this.communicationPreferences = JSON.parse(JSON.stringify(COMMUNICATION_PREFERENCES));
        this.sessions = JSON.parse(JSON.stringify(SESSIONS));
        this.passkeys = JSON.parse(JSON.stringify(PASSKEYS));
        this.apiKeys = JSON.parse(JSON.stringify(API_KEYS));
        this.authorizedApps = JSON.parse(JSON.stringify(AUTHORIZED_APPS));

        Object.assign(this, JSON.parse(JSON.stringify(INITIAL_NEXT_IDS)));
    },

    _loadPersistedData() {
        try {
            const saved = localStorage.getItem('linearAccountSettings');
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('linearAccountSettings');
                return null;
            }
            return parsed;
        } catch (e) {
            localStorage.removeItem('linearAccountSettings');
            return null;
        }
    },

    _applyPersistedData(data) {
        this.currentUser = data.currentUser;
        this.workspaces = data.workspaces;
        this.connectedAccounts = data.connectedAccounts;
        this.preferences = data.preferences;
        this.notificationChannels = data.notificationChannels;
        this.emailDigestPreferences = data.emailDigestPreferences;
        this.communicationPreferences = data.communicationPreferences;
        this.sessions = data.sessions;
        this.passkeys = data.passkeys;
        this.apiKeys = data.apiKeys;
        this.authorizedApps = data.authorizedApps;
        this._nextApiKeyId = data._nextApiKeyId || 6;
        this._nextPasskeyId = data._nextPasskeyId || 3;
        this._nextSessionId = data._nextSessionId || 9;
        this._nextConnectedAccountId = data._nextConnectedAccountId || 6;
        this._nextOAuthAppId = data._nextOAuthAppId || 9;
    },

    // ── Persistence ──────────────────────────────────────────

    _persist() {
        const persistable = {
            currentUser: this.currentUser,
            workspaces: this.workspaces,
            connectedAccounts: this.connectedAccounts,
            preferences: this.preferences,
            notificationChannels: this.notificationChannels,
            emailDigestPreferences: this.emailDigestPreferences,
            communicationPreferences: this.communicationPreferences,
            sessions: this.sessions,
            passkeys: this.passkeys,
            apiKeys: this.apiKeys,
            authorizedApps: this.authorizedApps,
            _nextApiKeyId: this._nextApiKeyId,
            _nextPasskeyId: this._nextPasskeyId,
            _nextSessionId: this._nextSessionId,
            _nextConnectedAccountId: this._nextConnectedAccountId,
            _nextOAuthAppId: this._nextOAuthAppId,
            _seedVersion: SEED_DATA_VERSION
        };
        localStorage.setItem('linearAccountSettings', JSON.stringify(persistable));
    },

    _pushStateToServer() {
        const state = this.getSerializableState();
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(state)
        }).catch(() => {});
    },

    getSerializableState() {
        return {
            currentUser: this.currentUser,
            workspaces: this.workspaces,
            connectedAccounts: this.connectedAccounts,
            preferences: this.preferences,
            notificationChannels: this.notificationChannels,
            emailDigestPreferences: this.emailDigestPreferences,
            communicationPreferences: this.communicationPreferences,
            sessions: this.sessions,
            passkeys: this.passkeys,
            apiKeys: this.apiKeys,
            authorizedApps: this.authorizedApps,
            _nextApiKeyId: this._nextApiKeyId,
            _nextPasskeyId: this._nextPasskeyId,
            _nextSessionId: this._nextSessionId,
            _nextConnectedAccountId: this._nextConnectedAccountId,
            _nextOAuthAppId: this._nextOAuthAppId,
            _seedVersion: SEED_DATA_VERSION
        };
    },

    // ── Observer pattern ─────────────────────────────────────

    subscribe(fn) {
        this._listeners.push(fn);
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        for (const fn of this._listeners) {
            fn();
        }
    },

    // ── SSE ──────────────────────────────────────────────────

    _setupSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = (e) => {
            if (e.data === 'reset') {
                this.resetToSeedData();
            }
        };
    },

    resetToSeedData() {
        localStorage.removeItem('linearAccountSettings');
        this._loadSeedData();
        this.currentSection = 'profile';
        this.expandedSessionId = null;
        this._expandedChannelId = null;
        this.modalOpen = false;
        this.editingField = null;
        this.notify();
    },

    // ── Profile mutations ────────────────────────────────────

    updateFullName(name) {
        if (!name || !name.trim()) return;
        this.currentUser.fullName = name.trim();
        this.currentUser.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateUsername(username) {
        if (!username || !username.trim()) return;
        this.currentUser.username = username.trim();
        this.currentUser.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateEmail(email) {
        if (!email || !email.trim()) return;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.trim())) return;
        this.currentUser.email = email.trim();
        this.currentUser.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateTimezone(tz) {
        this.currentUser.timezone = tz;
        this.currentUser.updatedAt = new Date().toISOString();
        this.notify();
    },

    // ── Connected Accounts ───────────────────────────────────

    disconnectAccount(accountId) {
        this.connectedAccounts = this.connectedAccounts.filter(a => a.id !== accountId);
        this.notify();
    },

    // ── Preferences mutations ────────────────────────────────

    updatePreference(category, key, value) {
        if (this.preferences[category]) {
            this.preferences[category][key] = value;
            this.notify();
        }
    },

    // ── Notification mutations ───────────────────────────────

    toggleNotificationChannel(channelId) {
        const channel = this.notificationChannels.find(c => c.id === channelId);
        if (channel) {
            channel.enabled = !channel.enabled;
            if (!channel.enabled) {
                channel.settings.forEach(s => { s.enabled = false; });
            }
            this.notify();
        }
    },

    toggleNotificationSetting(channelId, settingId) {
        const channel = this.notificationChannels.find(c => c.id === channelId);
        if (!channel) return;
        const setting = channel.settings.find(s => s.id === settingId);
        if (!setting) return;
        setting.enabled = !setting.enabled;
        if (setting.enabled && !channel.enabled) {
            channel.enabled = true;
        }
        this.notify();
    },

    updateEmailDigestPreference(key, value) {
        this.emailDigestPreferences[key] = value;
        this.notify();
    },

    updateCommunicationPreference(key, value) {
        this.communicationPreferences[key] = value;
        this.notify();
    },

    // ── Sessions mutations ───────────────────────────────────

    revokeSession(sessionId) {
        this.sessions = this.sessions.filter(s => s.id !== sessionId);
        if (this.expandedSessionId === sessionId) {
            this.expandedSessionId = null;
        }
        this.notify();
    },

    revokeAllSessions() {
        this.sessions = this.sessions.filter(s => s.isCurrent);
        this.expandedSessionId = null;
        this.notify();
    },

    toggleSessionExpand(sessionId) {
        this.expandedSessionId = this.expandedSessionId === sessionId ? null : sessionId;
    },

    // ── Passkeys mutations ───────────────────────────────────

    addPasskey(name) {
        if (!name || !name.trim()) return;
        const newPasskey = {
            id: 'pk_' + String(this._nextPasskeyId).padStart(3, '0'),
            name: name.trim(),
            createdAt: new Date().toISOString(),
            lastUsedAt: null,
            deviceType: 'cross-platform'
        };
        this._nextPasskeyId++;
        this.passkeys.push(newPasskey);
        this.notify();
    },

    removePasskey(passkeyId) {
        this.passkeys = this.passkeys.filter(p => p.id !== passkeyId);
        this.notify();
    },

    renamePasskey(passkeyId, newName) {
        const passkey = this.passkeys.find(p => p.id === passkeyId);
        if (passkey && newName && newName.trim()) {
            passkey.name = newName.trim();
            this.notify();
        }
    },

    // ── API Keys mutations ───────────────────────────────────

    createApiKey(label) {
        if (!label || !label.trim()) return;
        const chars = 'abcdef0123456789';
        let prefix = 'lin_api_';
        for (let i = 0; i < 4; i++) {
            prefix += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        const newKey = {
            id: 'apikey_' + String(this._nextApiKeyId).padStart(3, '0'),
            label: label.trim(),
            prefix: prefix,
            createdAt: new Date().toISOString(),
            lastUsedAt: null,
            expiresAt: null
        };
        this._nextApiKeyId++;
        this.apiKeys.push(newKey);
        this.notify();
        return newKey;
    },

    revokeApiKey(keyId) {
        this.apiKeys = this.apiKeys.filter(k => k.id !== keyId);
        this.notify();
    },

    updateApiKeyLabel(keyId, newLabel) {
        const key = this.apiKeys.find(k => k.id === keyId);
        if (key && newLabel && newLabel.trim()) {
            key.label = newLabel.trim();
            this.notify();
        }
    },

    // ── Authorized Apps mutations ────────────────────────────

    revokeAuthorizedApp(appId) {
        this.authorizedApps = this.authorizedApps.filter(a => a.id !== appId);
        this.notify();
    },

    // ── Navigation ───────────────────────────────────────────

    navigateTo(section) {
        this.currentSection = section;
        this.expandedSessionId = null;
        this.editingField = null;
    }
};

// ============================================================
// state.js — Centralized state management with localStorage persistence
// ============================================================

const STORAGE_KEY = 'linearAccountSettingsState';

function _loadSeedData() {
    return {
        _seedVersion: SEED_DATA_VERSION,
        currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
        workspaceMembers: JSON.parse(JSON.stringify(WORKSPACE_MEMBERS)),
        workspace: JSON.parse(JSON.stringify(WORKSPACE)),
        preferences: JSON.parse(JSON.stringify(PREFERENCES)),
        notificationChannels: JSON.parse(JSON.stringify(NOTIFICATION_CHANNELS)),
        notificationGroups: JSON.parse(JSON.stringify(NOTIFICATION_GROUPS)),
        emailDigestSettings: JSON.parse(JSON.stringify(EMAIL_DIGEST_SETTINGS)),
        communicationPreferences: JSON.parse(JSON.stringify(COMMUNICATION_PREFERENCES)),
        sessions: JSON.parse(JSON.stringify(SESSIONS)),
        passkeys: JSON.parse(JSON.stringify(PASSKEYS)),
        apiKeys: JSON.parse(JSON.stringify(API_KEYS)),
        authorizedApps: JSON.parse(JSON.stringify(AUTHORIZED_APPS)),
        connectedAccounts: JSON.parse(JSON.stringify(CONNECTED_ACCOUNTS)),
        issueSubscriptions: JSON.parse(JSON.stringify(ISSUE_SUBSCRIPTIONS)),
        _nextSessionId: 8,
        _nextPasskeyId: 3,
        _nextApiKeyId: 4,
        _nextSubscriptionId: 9,
        _nextConnectedAccountId: 6
    };
}

function _loadPersistedData() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) {
            console.log('[AppState] No persisted data found, using seed data');
            return null;
        }
        const parsed = JSON.parse(raw);
        if (parsed._seedVersion !== SEED_DATA_VERSION) {
            console.log('[AppState] Seed data version changed, discarding stale localStorage');
            localStorage.removeItem(STORAGE_KEY);
            return null;
        }
        console.log('[AppState] Loaded persisted data');
        return parsed;
    } catch (e) {
        console.error('[AppState] Failed to load persisted data:', e);
        return null;
    }
}

const _initial = _loadPersistedData() || _loadSeedData();

const AppState = {
    // Persistent data
    currentUser: _initial.currentUser,
    workspaceMembers: _initial.workspaceMembers,
    workspace: _initial.workspace,
    preferences: _initial.preferences,
    notificationChannels: _initial.notificationChannels,
    notificationGroups: _initial.notificationGroups,
    emailDigestSettings: _initial.emailDigestSettings,
    communicationPreferences: _initial.communicationPreferences,
    sessions: _initial.sessions,
    passkeys: _initial.passkeys,
    apiKeys: _initial.apiKeys,
    authorizedApps: _initial.authorizedApps,
    connectedAccounts: _initial.connectedAccounts,
    issueSubscriptions: _initial.issueSubscriptions,

    _seedVersion: _initial._seedVersion,

    // Counters
    _nextSessionId: _initial._nextSessionId,
    _nextPasskeyId: _initial._nextPasskeyId,
    _nextApiKeyId: _initial._nextApiKeyId,
    _nextSubscriptionId: _initial._nextSubscriptionId,
    _nextConnectedAccountId: _initial._nextConnectedAccountId,

    // UI state (transient)
    currentRoute: '/profile',
    routeParams: {},
    modalOpen: false,
    validationErrors: {},
    toasts: [],

    // Listeners
    _listeners: [],

    subscribe(fn) {
        this._listeners.push(fn);
        return () => {
            this._listeners = this._listeners.filter(l => l !== fn);
        };
    },

    notify() {
        this._listeners.forEach(fn => fn(this));
        this._persist();
    },

    // ---- Persistence ----

    _getPersistable() {
        return {
            _seedVersion: this._seedVersion,
            currentUser: this.currentUser,
            workspaceMembers: this.workspaceMembers,
            workspace: this.workspace,
            preferences: this.preferences,
            notificationChannels: this.notificationChannels,
            notificationGroups: this.notificationGroups,
            emailDigestSettings: this.emailDigestSettings,
            communicationPreferences: this.communicationPreferences,
            sessions: this.sessions,
            passkeys: this.passkeys,
            apiKeys: this.apiKeys,
            authorizedApps: this.authorizedApps,
            connectedAccounts: this.connectedAccounts,
            issueSubscriptions: this.issueSubscriptions,
            _nextSessionId: this._nextSessionId,
            _nextPasskeyId: this._nextPasskeyId,
            _nextApiKeyId: this._nextApiKeyId,
            _nextSubscriptionId: this._nextSubscriptionId,
            _nextConnectedAccountId: this._nextConnectedAccountId
        };
    },

    _persist() {
        try {
            const persistable = this._getPersistable();
            const json = JSON.stringify(persistable);
            localStorage.setItem(STORAGE_KEY, json);
            fetch('/api/state', {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: json
            }).catch(() => {});
        } catch (e) {
            console.error('[AppState] Failed to persist state:', e);
        }
    },

    resetToSeedData() {
        localStorage.removeItem(STORAGE_KEY);
        const seed = _loadSeedData();
        Object.keys(seed).forEach(key => {
            this[key] = seed[key];
        });
        this._listeners.forEach(fn => fn(this));
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this._getPersistable())
        }).catch(() => {});
    },

    // ---- Helper Methods ----

    getUserById(id) {
        return this.workspaceMembers.find(u => u.id === id);
    },

    getUserByUsername(username) {
        return this.workspaceMembers.find(u => u.username === username);
    },

    getSessionById(id) {
        return this.sessions.find(s => s.id === id);
    },

    getApiKeyById(id) {
        return this.apiKeys.find(k => k.id === id);
    },

    getPasskeyById(id) {
        return this.passkeys.find(p => p.id === id);
    },

    getAuthorizedAppById(id) {
        return this.authorizedApps.find(a => a.id === id);
    },

    getConnectedAccountById(id) {
        return this.connectedAccounts.find(c => c.id === id);
    },

    getConnectedAccountByProvider(provider) {
        return this.connectedAccounts.find(c => c.provider === provider);
    },

    // ---- Mutation Methods ----

    // Profile mutations
    updateProfile(data) {
        Object.assign(this.currentUser, data);
        // Sync to workspaceMembers
        const idx = this.workspaceMembers.findIndex(u => u.id === this.currentUser.id);
        if (idx !== -1) {
            this.workspaceMembers[idx] = JSON.parse(JSON.stringify(this.currentUser));
        }
        this.notify();
    },

    updateEmail(newEmail) {
        this.currentUser.email = newEmail;
        const idx = this.workspaceMembers.findIndex(u => u.id === this.currentUser.id);
        if (idx !== -1) {
            this.workspaceMembers[idx].email = newEmail;
        }
        this.notify();
    },

    // Preferences mutations
    updatePreference(key, value) {
        this.preferences[key] = value;
        this.notify();
    },

    updatePreferences(data) {
        Object.assign(this.preferences, data);
        this.notify();
    },

    // Notification mutations
    toggleNotificationChannel(channelId, enabled) {
        if (this.notificationChannels[channelId]) {
            this.notificationChannels[channelId].enabled = enabled;
            this.notify();
        }
    },

    updateNotificationGroup(groupId, channelId, enabled) {
        const group = this.notificationGroups.find(g => g.id === groupId);
        if (group && group.channels[channelId] !== undefined) {
            group.channels[channelId] = enabled;
            this.notify();
        }
    },

    updateEmailDigestSetting(key, value) {
        this.emailDigestSettings[key] = value;
        this.notify();
    },

    updateCommunicationPreference(key, value) {
        this.communicationPreferences[key] = value;
        this.notify();
    },

    // Subscription mutations
    addSubscription(data) {
        const id = 'sub-' + String(this._nextSubscriptionId++).padStart(3, '0');
        this.issueSubscriptions.push({
            id,
            issueId: data.issueId,
            issueTitle: data.issueTitle,
            teamName: data.teamName,
            reason: data.reason || 'manual',
            subscribedAt: new Date().toISOString()
        });
        this.notify();
    },

    removeSubscription(subscriptionId) {
        this.issueSubscriptions = this.issueSubscriptions.filter(s => s.id !== subscriptionId);
        this.notify();
    },

    // Session mutations
    revokeSession(sessionId) {
        this.sessions = this.sessions.filter(s => s.id !== sessionId);
        this.notify();
    },

    revokeAllSessionsExceptCurrent() {
        this.sessions = this.sessions.filter(s => s.isCurrent);
        this.notify();
    },

    // Passkey mutations
    addPasskey(data) {
        const id = 'pk-' + String(this._nextPasskeyId++).padStart(4, '0');
        this.passkeys.push({
            id,
            name: data.name,
            createdAt: new Date().toISOString(),
            lastUsedAt: null,
            deviceType: data.deviceType || 'cross-platform'
        });
        this.notify();
        return id;
    },

    removePasskey(passkeyId) {
        this.passkeys = this.passkeys.filter(p => p.id !== passkeyId);
        this.notify();
    },

    renamePasskey(passkeyId, newName) {
        const pk = this.getPasskeyById(passkeyId);
        if (pk) {
            pk.name = newName;
            this.notify();
        }
    },

    // API Key mutations
    createApiKey(label) {
        const id = 'key-' + Math.random().toString(36).substring(2, 8);
        const prefix = 'lin_api_' + Math.random().toString(36).substring(2, 6) + '...' + Math.random().toString(36).substring(2, 4);
        this.apiKeys.push({
            id,
            label,
            prefix,
            createdAt: new Date().toISOString(),
            lastUsedAt: null
        });
        this.notify();
        return id;
    },

    revokeApiKey(keyId) {
        this.apiKeys = this.apiKeys.filter(k => k.id !== keyId);
        this.notify();
    },

    renameApiKey(keyId, newLabel) {
        const key = this.getApiKeyById(keyId);
        if (key) {
            key.label = newLabel;
            this.notify();
        }
    },

    // Authorized Apps mutations
    revokeAuthorizedApp(appId) {
        this.authorizedApps = this.authorizedApps.filter(a => a.id !== appId);
        this.notify();
    },

    // Connected Accounts mutations
    disconnectAccount(accountId) {
        this.connectedAccounts = this.connectedAccounts.filter(c => c.id !== accountId);
        this.notify();
    },

    addConnectedAccount(data) {
        const id = 'conn-' + Math.random().toString(36).substring(2, 6);
        this.connectedAccounts.push({
            id,
            provider: data.provider,
            username: data.username,
            email: data.email,
            connectedAt: new Date().toISOString(),
            status: 'active'
        });
        this._nextConnectedAccountId++;
        this.notify();
        return id;
    }
};

// Push initial state to server on page load
fetch('/api/state', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(AppState._getPersistable())
}).catch(() => {});

// ============================================================
// state.js — Centralized state management for Gmail Accounts & Contacts
// ============================================================

const AppState = {
    // ---- Persistent State ----
    contacts: [],
    otherContacts: [],
    contactLabels: [],
    delegates: [],
    linkedServices: [],
    alwaysLinkedServices: [],
    accountSettings: {},
    currentUser: null,
    contactHistory: [],
    importExportHistory: [],
    mergeSuggestions: [],

    // ---- ID Counters ----
    _nextContactId: 50,
    _nextOtherContactId: 30,
    _nextLabelId: 20,
    _nextDelegateId: 10,
    _nextHistoryId: 20,

    // ---- UI State (not persisted) ----
    currentView: 'contacts',
    contactsFilter: 'all',
    selectedContactId: null,
    searchQuery: '',
    searchResults: null,
    editingContact: null,
    createContactOpen: false,
    createLabelOpen: false,
    editLabelId: null,
    addDelegateOpen: false,
    confirmModal: null,
    toastMessage: null,
    toastTimeout: null,
    contactsSortBy: 'firstName',
    contactsSortDir: 'asc',
    currentPage: 1,
    pageSize: 25,
    settingsTab: 'general',

    // ---- Listeners ----
    _listeners: [],

    subscribe(fn) {
        this._listeners.push(fn);
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        for (const fn of this._listeners) {
            try { fn(); } catch (e) { console.error('Listener error:', e); }
        }
    },

    // ---- Initialization ----

    init() {
        const persisted = this._loadPersistedData();
        if (persisted) {
            this.contacts = persisted.contacts || [];
            this.otherContacts = persisted.otherContacts || [];
            this.contactLabels = persisted.contactLabels || [];
            this.delegates = persisted.delegates || [];
            this.linkedServices = persisted.linkedServices || [];
            this.alwaysLinkedServices = persisted.alwaysLinkedServices || [];
            this.accountSettings = persisted.accountSettings || {};
            this.currentUser = persisted.currentUser || null;
            this.contactHistory = persisted.contactHistory || [];
            this.importExportHistory = persisted.importExportHistory || [];
            this.mergeSuggestions = persisted.mergeSuggestions || [];
            this._nextContactId = persisted._nextContactId || 50;
            this._nextOtherContactId = persisted._nextOtherContactId || 30;
            this._nextLabelId = persisted._nextLabelId || 20;
            this._nextDelegateId = persisted._nextDelegateId || 10;
            this._nextHistoryId = persisted._nextHistoryId || 20;
        } else {
            this._loadSeedData();
        }
        this._recalculateLabelCounts();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.contacts = JSON.parse(JSON.stringify(CONTACTS));
        this.otherContacts = JSON.parse(JSON.stringify(OTHER_CONTACTS));
        this.contactLabels = JSON.parse(JSON.stringify(CONTACT_LABELS));
        this.delegates = JSON.parse(JSON.stringify(DELEGATES));
        this.linkedServices = JSON.parse(JSON.stringify(LINKED_SERVICES));
        this.alwaysLinkedServices = JSON.parse(JSON.stringify(ALWAYS_LINKED_SERVICES));
        this.accountSettings = JSON.parse(JSON.stringify(ACCOUNT_SETTINGS));
        this.contactHistory = JSON.parse(JSON.stringify(CONTACT_HISTORY));
        this.importExportHistory = JSON.parse(JSON.stringify(IMPORT_EXPORT_HISTORY));
        this.mergeSuggestions = JSON.parse(JSON.stringify(MERGE_SUGGESTIONS));
        this._nextContactId = 50;
        this._nextOtherContactId = 30;
        this._nextLabelId = 20;
        this._nextDelegateId = 10;
        this._nextHistoryId = 20;
    },

    _loadPersistedData() {
        try {
            const saved = localStorage.getItem('gmailAccountsContactsState');
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('gmailAccountsContactsState');
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    },

    // ---- Persistence ----

    _persist() {
        const persistable = {
            contacts: this.contacts,
            otherContacts: this.otherContacts,
            contactLabels: this.contactLabels,
            delegates: this.delegates,
            linkedServices: this.linkedServices,
            alwaysLinkedServices: this.alwaysLinkedServices,
            accountSettings: this.accountSettings,
            currentUser: this.currentUser,
            contactHistory: this.contactHistory,
            importExportHistory: this.importExportHistory,
            mergeSuggestions: this.mergeSuggestions,
            _nextContactId: this._nextContactId,
            _nextOtherContactId: this._nextOtherContactId,
            _nextLabelId: this._nextLabelId,
            _nextDelegateId: this._nextDelegateId,
            _nextHistoryId: this._nextHistoryId,
            _seedVersion: SEED_DATA_VERSION
        };
        localStorage.setItem('gmailAccountsContactsState', JSON.stringify(persistable));
    },

    _pushStateToServer() {
        const state = {
            contacts: this.contacts,
            otherContacts: this.otherContacts,
            contactLabels: this.contactLabels,
            delegates: this.delegates,
            linkedServices: this.linkedServices,
            alwaysLinkedServices: this.alwaysLinkedServices,
            accountSettings: this.accountSettings,
            currentUser: this.currentUser,
            contactHistory: this.contactHistory,
            importExportHistory: this.importExportHistory,
            mergeSuggestions: this.mergeSuggestions,
            _nextContactId: this._nextContactId,
            _nextOtherContactId: this._nextOtherContactId,
            _nextLabelId: this._nextLabelId,
            _nextDelegateId: this._nextDelegateId,
            _nextHistoryId: this._nextHistoryId
        };
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(state)
        }).catch(() => {});
    },

    // ---- SSE listener ----

    _initSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = (e) => {
            if (e.data === 'reset') {
                this._loadSeedData();
                this._recalculateLabelCounts();
                this.currentView = 'contacts';
                this.selectedContactId = null;
                this.searchQuery = '';
                this.searchResults = null;
                this.editingContact = null;
                this.createContactOpen = false;
                this.notify();
            }
        };
    },

    // ---- Label Counts ----

    _recalculateLabelCounts() {
        for (const label of this.contactLabels) {
            label.contactCount = this.contacts.filter(c => c.labels && c.labels.includes(label.id)).length;
        }
    },

    // ---- Contact CRUD ----

    getContactById(id) {
        return this.contacts.find(c => c.id === id) || null;
    },

    getFilteredContacts() {
        let list = [...this.contacts];

        if (this.contactsFilter === 'starred') {
            list = list.filter(c => c.isStarred);
        } else if (this.contactsFilter === 'frequently') {
            list = list.filter(c => c.isStarred || ['contact_01', 'contact_02', 'contact_03', 'contact_05', 'contact_14', 'contact_21', 'contact_30'].includes(c.id));
        } else if (this.contactsFilter.startsWith('clabel_')) {
            list = list.filter(c => c.labels && c.labels.includes(this.contactsFilter));
        }

        if (this.searchQuery) {
            const q = this.searchQuery.toLowerCase();
            list = list.filter(c =>
                (c.firstName + ' ' + c.lastName).toLowerCase().includes(q) ||
                c.email.toLowerCase().includes(q) ||
                (c.company || '').toLowerCase().includes(q) ||
                (c.phone || '').includes(q) ||
                (c.jobTitle || '').toLowerCase().includes(q)
            );
        }

        const sortKey = this.contactsSortBy;
        const dir = this.contactsSortDir === 'asc' ? 1 : -1;
        list.sort((a, b) => {
            let va = (a[sortKey] || '').toLowerCase();
            let vb = (b[sortKey] || '').toLowerCase();
            if (va < vb) return -1 * dir;
            if (va > vb) return 1 * dir;
            return 0;
        });

        return list;
    },

    getPagedContacts() {
        const filtered = this.getFilteredContacts();
        const start = (this.currentPage - 1) * this.pageSize;
        return {
            contacts: filtered.slice(start, start + this.pageSize),
            total: filtered.length,
            page: this.currentPage,
            totalPages: Math.ceil(filtered.length / this.pageSize)
        };
    },

    addContact(data) {
        const id = 'contact_' + String(this._nextContactId++).padStart(2, '0');
        const now = new Date().toISOString();
        const contact = {
            id,
            firstName: data.firstName || '',
            lastName: data.lastName || '',
            email: data.email || '',
            phone: data.phone || '',
            company: data.company || '',
            jobTitle: data.jobTitle || '',
            address: data.address || '',
            secondaryEmail: data.secondaryEmail || '',
            secondaryPhone: data.secondaryPhone || '',
            birthday: data.birthday || '',
            website: data.website || '',
            notes: data.notes || '',
            labels: data.labels || [],
            isStarred: false,
            avatarColor: this._randomColor(),
            createdAt: now,
            updatedAt: now,
            source: 'manual'
        };
        this.contacts.push(contact);
        this._addHistory(id, 'created', null, null, null);
        this._recalculateLabelCounts();
        this.notify();
        return contact;
    },

    updateContact(id, data) {
        const contact = this.getContactById(id);
        if (!contact) return;
        const now = new Date().toISOString();
        for (const [key, val] of Object.entries(data)) {
            if (key === 'id' || key === 'createdAt' || key === 'source' || key === 'avatarColor') continue;
            if (contact[key] !== val) {
                this._addHistory(id, 'edited', key, contact[key], val);
                contact[key] = val;
            }
        }
        contact.updatedAt = now;
        this._recalculateLabelCounts();
        this.notify();
    },

    deleteContact(id) {
        const idx = this.contacts.findIndex(c => c.id === id);
        if (idx !== -1) {
            this.contacts.splice(idx, 1);
            if (this.selectedContactId === id) this.selectedContactId = null;
            this._recalculateLabelCounts();
            this.notify();
        }
    },

    deleteMultipleContacts(ids) {
        this.contacts = this.contacts.filter(c => !ids.includes(c.id));
        if (ids.includes(this.selectedContactId)) this.selectedContactId = null;
        this._recalculateLabelCounts();
        this.notify();
    },

    toggleStar(id) {
        const contact = this.getContactById(id);
        if (contact) {
            contact.isStarred = !contact.isStarred;
            contact.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    addLabelToContact(contactId, labelId) {
        const contact = this.getContactById(contactId);
        if (contact && !contact.labels.includes(labelId)) {
            contact.labels.push(labelId);
            contact.updatedAt = new Date().toISOString();
            const label = this.contactLabels.find(l => l.id === labelId);
            this._addHistory(contactId, 'label_added', 'labels', null, label ? label.name : labelId);
            this._recalculateLabelCounts();
            this.notify();
        }
    },

    removeLabelFromContact(contactId, labelId) {
        const contact = this.getContactById(contactId);
        if (contact) {
            contact.labels = contact.labels.filter(l => l !== labelId);
            contact.updatedAt = new Date().toISOString();
            const label = this.contactLabels.find(l => l.id === labelId);
            this._addHistory(contactId, 'label_removed', 'labels', label ? label.name : labelId, null);
            this._recalculateLabelCounts();
            this.notify();
        }
    },

    moveOtherToContacts(otherId) {
        const idx = this.otherContacts.findIndex(c => c.id === otherId);
        if (idx === -1) return;
        const other = this.otherContacts[idx];
        const newContact = {
            id: 'contact_' + String(this._nextContactId++).padStart(2, '0'),
            firstName: other.firstName || '',
            lastName: other.lastName || '',
            email: other.email,
            phone: '',
            company: '',
            jobTitle: '',
            address: '',
            secondaryEmail: '',
            secondaryPhone: '',
            birthday: '',
            website: '',
            notes: 'Auto-saved contact moved to main contacts.',
            labels: [],
            isStarred: false,
            avatarColor: this._randomColor(),
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString(),
            source: 'auto-promoted'
        };
        this.contacts.push(newContact);
        this.otherContacts.splice(idx, 1);
        this._addHistory(newContact.id, 'created', null, null, null);
        this.notify();
        return newContact;
    },

    deleteOtherContact(id) {
        const idx = this.otherContacts.findIndex(c => c.id === id);
        if (idx !== -1) {
            this.otherContacts.splice(idx, 1);
            this.notify();
        }
    },

    // ---- Contact Labels ----

    addContactLabel(name, color) {
        const id = 'clabel_' + this._nextLabelId++;
        this.contactLabels.push({ id, name, color: color || '#757575', contactCount: 0 });
        this.notify();
        return id;
    },

    renameContactLabel(id, newName) {
        const label = this.contactLabels.find(l => l.id === id);
        if (label) {
            label.name = newName;
            this.notify();
        }
    },

    deleteContactLabel(id) {
        this.contactLabels = this.contactLabels.filter(l => l.id !== id);
        for (const c of this.contacts) {
            c.labels = c.labels.filter(l => l !== id);
        }
        if (this.contactsFilter === id) this.contactsFilter = 'all';
        this.notify();
    },

    updateContactLabelColor(id, color) {
        const label = this.contactLabels.find(l => l.id === id);
        if (label) {
            label.color = color;
            this.notify();
        }
    },

    // ---- Delegates ----

    addDelegate(email, name) {
        const id = 'delegate_' + this._nextDelegateId++;
        const delegate = {
            id, email, name: name || email,
            status: 'pending',
            addedAt: new Date().toISOString(),
            activatedAt: null,
            permissions: { readEmail: true, sendEmail: true, deleteEmail: true, manageChat: false, changePassword: false }
        };
        this.delegates.push(delegate);
        this.notify();
        return delegate;
    },

    removeDelegate(id) {
        this.delegates = this.delegates.filter(d => d.id !== id);
        this.notify();
    },

    // ---- Linked Services ----

    toggleLinkedService(id) {
        const svc = this.linkedServices.find(s => s.id === id);
        if (svc) {
            svc.isLinked = !svc.isLinked;
            this.notify();
        }
    },

    // ---- Account Settings ----

    updateAccountSetting(path, value) {
        const parts = path.split('.');
        let obj = this.accountSettings;
        for (let i = 0; i < parts.length - 1; i++) {
            obj = obj[parts[i]];
        }
        obj[parts[parts.length - 1]] = value;
        this.notify();
    },

    updateCurrentUser(field, value) {
        this.currentUser[field] = value;
        this.notify();
    },

    // ---- Merge suggestions ----

    dismissMergeSuggestion(id) {
        const suggestion = this.mergeSuggestions.find(s => s.id === id);
        if (suggestion) {
            suggestion.dismissed = true;
            this.notify();
        }
    },

    mergeContacts(suggestionId) {
        const suggestion = this.mergeSuggestions.find(s => s.id === suggestionId);
        if (!suggestion) return;
        const [primaryId, ...others] = suggestion.contacts;
        const primary = this.getContactById(primaryId);
        if (!primary) return;
        for (const otherId of others) {
            const other = this.getContactById(otherId);
            if (!other) continue;
            if (!primary.secondaryEmail && other.email) primary.secondaryEmail = other.email;
            if (!primary.secondaryPhone && other.phone) primary.secondaryPhone = other.phone;
            for (const lbl of other.labels) {
                if (!primary.labels.includes(lbl)) primary.labels.push(lbl);
            }
            if (other.notes && !primary.notes.includes(other.notes)) {
                primary.notes = primary.notes ? primary.notes + '\n' + other.notes : other.notes;
            }
            this.contacts = this.contacts.filter(c => c.id !== otherId);
        }
        primary.updatedAt = new Date().toISOString();
        suggestion.dismissed = true;
        this._recalculateLabelCounts();
        this.notify();
    },

    // ---- History ----

    _addHistory(contactId, action, field, oldValue, newValue) {
        this.contactHistory.push({
            id: 'hist_' + this._nextHistoryId++,
            contactId,
            action,
            field,
            oldValue: oldValue !== undefined ? oldValue : null,
            newValue: newValue !== undefined ? newValue : null,
            timestamp: new Date().toISOString(),
            actor: this.currentUser ? this.currentUser.email : 'unknown'
        });
    },

    getHistoryForContact(contactId) {
        return this.contactHistory
            .filter(h => h.contactId === contactId)
            .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
    },

    // ---- Helpers ----

    _randomColor() {
        const colors = ['#EA4335', '#34A853', '#FBBC04', '#4285F4', '#9C27B0', '#FF5722',
            '#009688', '#795548', '#E91E63', '#3F51B5', '#FF9800', '#607D8B',
            '#00BCD4', '#673AB7', '#2196F3', '#F44336', '#8BC34A', '#CDDC39'];
        return colors[Math.floor(Math.random() * colors.length)];
    },

    searchContacts(query) {
        if (!query) return [];
        const q = query.toLowerCase();
        const results = [];
        for (const c of this.contacts) {
            const fullName = (c.firstName + ' ' + c.lastName).toLowerCase();
            if (fullName.includes(q) || c.email.toLowerCase().includes(q) ||
                (c.company || '').toLowerCase().includes(q) ||
                (c.phone || '').includes(q)) {
                results.push(c);
            }
        }
        for (const c of this.otherContacts) {
            if ((c.name || '').toLowerCase().includes(q) || c.email.toLowerCase().includes(q)) {
                results.push({ ...c, _isOther: true });
            }
        }
        return results;
    }
};

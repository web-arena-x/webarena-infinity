/* state.js — Centralized state management for Gmail Accounts & Contacts */

const AppState = {

    // ─── Persistent data ───
    currentUser: null,
    aliases: [],
    delegates: [],
    importAccounts: [],
    contacts: [],
    contactGroups: [],
    otherContacts: [],
    directory: [],
    appPasswords: [],
    replyFromSetting: 'default',
    _seedVersion: null,

    // ─── ID counters ───
    _nextContactId: 121,
    _nextGroupId: 11,
    _nextAliasId: 5,
    _nextDelegateId: 4,
    _nextImportId: 3,
    _nextAppPasswordId: 4,
    _nextOtherContactId: 26,

    // ─── UI state (ephemeral) ───
    currentView: 'contacts',
    currentContactId: null,
    currentGroupId: null,
    searchQuery: '',
    contactSort: 'firstName',
    contactFilter: 'all',
    directorySearch: '',
    otherContactSearch: '',
    currentPage: 1,
    pageSize: 25,
    selectedContactIds: [],

    // ─── Listeners ───
    _listeners: [],

    // ─── Initialization ───
    init() {
        const stored = localStorage.getItem('gmailAccountsContactsState');
        if (stored) {
            try {
                const parsed = JSON.parse(stored);
                if (parsed._seedVersion === SEED_DATA_VERSION) {
                    this._loadPersistedData(parsed);
                } else {
                    localStorage.removeItem('gmailAccountsContactsState');
                    this._loadSeedData();
                }
            } catch (e) {
                this._loadSeedData();
            }
        } else {
            this._loadSeedData();
        }
        this._pushStateToServer();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.aliases = JSON.parse(JSON.stringify(ALIASES));
        this.delegates = JSON.parse(JSON.stringify(DELEGATES));
        this.importAccounts = JSON.parse(JSON.stringify(IMPORT_ACCOUNTS));
        this.contacts = JSON.parse(JSON.stringify(CONTACTS));
        this.contactGroups = JSON.parse(JSON.stringify(CONTACT_GROUPS));
        this.otherContacts = JSON.parse(JSON.stringify(OTHER_CONTACTS));
        this.directory = JSON.parse(JSON.stringify(DIRECTORY));
        this.appPasswords = JSON.parse(JSON.stringify(APP_PASSWORDS));
        this.replyFromSetting = REPLY_FROM_SETTING;
        this._seedVersion = SEED_DATA_VERSION;
        this._nextContactId = 121;
        this._nextGroupId = 11;
        this._nextAliasId = 5;
        this._nextDelegateId = 4;
        this._nextImportId = 3;
        this._nextAppPasswordId = 4;
        this._nextOtherContactId = 26;
    },

    _loadPersistedData(parsed) {
        this.currentUser = parsed.currentUser;
        this.aliases = parsed.aliases || [];
        this.delegates = parsed.delegates || [];
        this.importAccounts = parsed.importAccounts || [];
        this.contacts = parsed.contacts || [];
        this.contactGroups = parsed.contactGroups || [];
        this.otherContacts = parsed.otherContacts || [];
        this.directory = parsed.directory || [];
        this.appPasswords = parsed.appPasswords || [];
        this.replyFromSetting = parsed.replyFromSetting || 'default';
        this._seedVersion = parsed._seedVersion;
        this._nextContactId = parsed._nextContactId || 121;
        this._nextGroupId = parsed._nextGroupId || 11;
        this._nextAliasId = parsed._nextAliasId || 5;
        this._nextDelegateId = parsed._nextDelegateId || 4;
        this._nextImportId = parsed._nextImportId || 3;
        this._nextAppPasswordId = parsed._nextAppPasswordId || 4;
        this._nextOtherContactId = parsed._nextOtherContactId || 26;
    },

    resetToSeedData() {
        this._loadSeedData();
        this.currentView = 'contacts';
        this.currentContactId = null;
        this.currentGroupId = null;
        this.searchQuery = '';
        this.contactSort = 'firstName';
        this.contactFilter = 'all';
        this.directorySearch = '';
        this.otherContactSearch = '';
        this.currentPage = 1;
        this.selectedContactIds = [];
        this.notify();
    },

    // ─── Persistence & sync ───
    _persist() {
        const data = {
            currentUser: this.currentUser,
            aliases: this.aliases,
            delegates: this.delegates,
            importAccounts: this.importAccounts,
            contacts: this.contacts,
            contactGroups: this.contactGroups,
            otherContacts: this.otherContacts,
            directory: this.directory,
            appPasswords: this.appPasswords,
            replyFromSetting: this.replyFromSetting,
            _seedVersion: this._seedVersion,
            _nextContactId: this._nextContactId,
            _nextGroupId: this._nextGroupId,
            _nextAliasId: this._nextAliasId,
            _nextDelegateId: this._nextDelegateId,
            _nextImportId: this._nextImportId,
            _nextAppPasswordId: this._nextAppPasswordId,
            _nextOtherContactId: this._nextOtherContactId
        };
        localStorage.setItem('gmailAccountsContactsState', JSON.stringify(data));
    },

    _pushStateToServer() {
        const data = {
            currentUser: this.currentUser,
            aliases: this.aliases,
            delegates: this.delegates,
            importAccounts: this.importAccounts,
            contacts: this.contacts,
            contactGroups: this.contactGroups,
            otherContacts: this.otherContacts,
            directory: this.directory,
            appPasswords: this.appPasswords,
            replyFromSetting: this.replyFromSetting,
            _seedVersion: this._seedVersion,
            _nextContactId: this._nextContactId,
            _nextGroupId: this._nextGroupId,
            _nextAliasId: this._nextAliasId,
            _nextDelegateId: this._nextDelegateId,
            _nextImportId: this._nextImportId,
            _nextAppPasswordId: this._nextAppPasswordId,
            _nextOtherContactId: this._nextOtherContactId
        };
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        }).catch(() => {});
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        this._listeners.forEach(fn => fn());
    },

    subscribe(fn) {
        this._listeners.push(fn);
    },

    // ─── Query helpers: Contacts ───
    getContactById(id) {
        return this.contacts.find(c => c.id === id) || null;
    },

    getFilteredContacts() {
        let list = this.contacts.slice();

        // Filter by group
        if (this.contactFilter && this.contactFilter !== 'all' && this.contactFilter !== 'starred') {
            list = list.filter(c => c.groups && c.groups.includes(this.contactFilter));
        }
        if (this.contactFilter === 'starred') {
            list = list.filter(c => c.starred);
        }

        // Search
        if (this.searchQuery) {
            const q = this.searchQuery.toLowerCase();
            list = list.filter(c => {
                const full = (c.firstName + ' ' + c.lastName).toLowerCase();
                return full.includes(q) ||
                       (c.email && c.email.toLowerCase().includes(q)) ||
                       (c.company && c.company.toLowerCase().includes(q)) ||
                       (c.phone && c.phone.includes(q)) ||
                       (c.jobTitle && c.jobTitle.toLowerCase().includes(q));
            });
        }

        // Sort
        list.sort((a, b) => {
            if (this.contactSort === 'firstName') {
                return (a.firstName || '').localeCompare(b.firstName || '');
            } else if (this.contactSort === 'lastName') {
                return (a.lastName || '').localeCompare(b.lastName || '');
            } else if (this.contactSort === 'email') {
                return (a.email || '').localeCompare(b.email || '');
            } else if (this.contactSort === 'recentlyAdded') {
                return (b.createdAt || '').localeCompare(a.createdAt || '');
            }
            return 0;
        });

        return list;
    },

    getContactsForGroup(groupId) {
        return this.contacts.filter(c => c.groups && c.groups.includes(groupId));
    },

    getGroupById(id) {
        return this.contactGroups.find(g => g.id === id) || null;
    },

    getStarredContacts() {
        return this.contacts.filter(c => c.starred);
    },

    getFilteredOtherContacts() {
        let list = this.otherContacts.slice();
        if (this.otherContactSearch) {
            const q = this.otherContactSearch.toLowerCase();
            list = list.filter(c => {
                const name = ((c.firstName || '') + ' ' + (c.lastName || '')).toLowerCase().trim();
                return name.includes(q) || (c.email && c.email.toLowerCase().includes(q));
            });
        }
        list.sort((a, b) => (b.lastInteraction || '').localeCompare(a.lastInteraction || ''));
        return list;
    },

    getFilteredDirectory() {
        let list = this.directory.slice();
        if (this.directorySearch) {
            const q = this.directorySearch.toLowerCase();
            list = list.filter(d => {
                return d.name.toLowerCase().includes(q) ||
                       d.email.toLowerCase().includes(q) ||
                       d.department.toLowerCase().includes(q) ||
                       d.title.toLowerCase().includes(q);
            });
        }
        list.sort((a, b) => a.name.localeCompare(b.name));
        return list;
    },

    // ─── Mutations: Contacts ───
    createContact(data) {
        const id = 'ct_' + this._nextContactId++;
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
            birthday: data.birthday || '',
            notes: data.notes || '',
            starred: false,
            groups: data.groups || [],
            createdAt: now,
            updatedAt: now
        };
        this.contacts.push(contact);
        this.notify();
        return contact;
    },

    updateContact(id, data) {
        const c = this.getContactById(id);
        if (!c) return null;
        Object.keys(data).forEach(key => {
            if (key !== 'id' && key !== 'createdAt') {
                c[key] = data[key];
            }
        });
        c.updatedAt = new Date().toISOString();
        this.notify();
        return c;
    },

    deleteContact(id) {
        this.contacts = this.contacts.filter(c => c.id !== id);
        this.selectedContactIds = this.selectedContactIds.filter(sid => sid !== id);
        this.notify();
    },

    deleteContacts(ids) {
        this.contacts = this.contacts.filter(c => !ids.includes(c.id));
        this.selectedContactIds = [];
        this.notify();
    },

    toggleContactStar(id) {
        const c = this.getContactById(id);
        if (c) {
            c.starred = !c.starred;
            c.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    addContactToGroup(contactId, groupId) {
        const c = this.getContactById(contactId);
        if (c && !c.groups.includes(groupId)) {
            c.groups.push(groupId);
            c.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    removeContactFromGroup(contactId, groupId) {
        const c = this.getContactById(contactId);
        if (c) {
            c.groups = c.groups.filter(g => g !== groupId);
            c.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    addContactsToGroup(contactIds, groupId) {
        contactIds.forEach(cid => {
            const c = this.getContactById(cid);
            if (c && !c.groups.includes(groupId)) {
                c.groups.push(groupId);
                c.updatedAt = new Date().toISOString();
            }
        });
        this.notify();
    },

    removeContactsFromGroup(contactIds, groupId) {
        contactIds.forEach(cid => {
            const c = this.getContactById(cid);
            if (c) {
                c.groups = c.groups.filter(g => g !== groupId);
                c.updatedAt = new Date().toISOString();
            }
        });
        this.notify();
    },

    // ─── Mutations: Contact Groups ───
    createGroup(name) {
        const id = 'grp_' + this._nextGroupId++;
        const now = new Date().toISOString();
        const group = { id, name, system: false, createdAt: now, updatedAt: now };
        this.contactGroups.push(group);
        this.notify();
        return group;
    },

    renameGroup(id, name) {
        const g = this.getGroupById(id);
        if (g) {
            g.name = name;
            g.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    deleteGroup(id) {
        this.contactGroups = this.contactGroups.filter(g => g.id !== id);
        // Remove group from all contacts
        this.contacts.forEach(c => {
            c.groups = c.groups.filter(g => g !== id);
        });
        if (this.contactFilter === id) {
            this.contactFilter = 'all';
        }
        this.notify();
    },

    // ─── Mutations: Other Contacts ───
    promoteOtherContact(id) {
        const oc = this.otherContacts.find(c => c.id === id);
        if (!oc) return null;
        const contact = this.createContact({
            firstName: oc.firstName || '',
            lastName: oc.lastName || '',
            email: oc.email
        });
        this.otherContacts = this.otherContacts.filter(c => c.id !== id);
        this.notify();
        return contact;
    },

    deleteOtherContact(id) {
        this.otherContacts = this.otherContacts.filter(c => c.id !== id);
        this.notify();
    },

    // ─── Mutations: Aliases ───
    createAlias(data) {
        const id = 'alias_' + this._nextAliasId++;
        const alias = {
            id,
            name: data.name || '',
            email: data.email || '',
            isPrimary: false,
            isDefault: false,
            replyFrom: data.replyFrom || 'default',
            smtpServer: data.smtpServer || '',
            smtpPort: data.smtpPort || '',
            smtpUsername: data.smtpUsername || '',
            useSSL: data.useSSL !== false,
            createdAt: new Date().toISOString()
        };
        this.aliases.push(alias);
        this.notify();
        return alias;
    },

    updateAlias(id, data) {
        const a = this.aliases.find(al => al.id === id);
        if (!a) return null;
        Object.keys(data).forEach(key => {
            if (key !== 'id' && key !== 'isPrimary' && key !== 'createdAt') {
                a[key] = data[key];
            }
        });
        this.notify();
        return a;
    },

    deleteAlias(id) {
        const a = this.aliases.find(al => al.id === id);
        if (a && a.isPrimary) return false;
        if (a && a.isDefault) {
            // Set primary as default
            const primary = this.aliases.find(al => al.isPrimary);
            if (primary) primary.isDefault = true;
        }
        this.aliases = this.aliases.filter(al => al.id !== id);
        this.notify();
        return true;
    },

    setDefaultAlias(id) {
        this.aliases.forEach(a => { a.isDefault = (a.id === id); });
        this.notify();
    },

    setReplyFromSetting(value) {
        this.replyFromSetting = value;
        this.notify();
    },

    // ─── Mutations: Delegates ───
    addDelegate(email, name) {
        const id = 'del_' + this._nextDelegateId++;
        const del = {
            id,
            email,
            name: name || email,
            status: 'pending',
            addedAt: new Date().toISOString()
        };
        this.delegates.push(del);
        this.notify();
        return del;
    },

    removeDelegate(id) {
        this.delegates = this.delegates.filter(d => d.id !== id);
        this.notify();
    },

    // ─── Mutations: Import Accounts ───
    addImportAccount(data) {
        const id = 'imp_' + this._nextImportId++;
        const imp = {
            id,
            email: data.email || '',
            server: data.server || '',
            port: data.port || '995',
            username: data.username || '',
            useSSL: data.useSSL !== false,
            leaveOnServer: data.leaveOnServer !== false,
            labelIncoming: data.labelIncoming || '',
            status: 'active',
            lastChecked: new Date().toISOString(),
            addedAt: new Date().toISOString()
        };
        this.importAccounts.push(imp);
        this.notify();
        return imp;
    },

    removeImportAccount(id) {
        this.importAccounts = this.importAccounts.filter(i => i.id !== id);
        this.notify();
    },

    // ─── Mutations: Account Settings ───
    updateAccountInfo(data) {
        Object.keys(data).forEach(key => {
            this.currentUser[key] = data[key];
        });
        this.notify();
    },

    // ─── Mutations: App Passwords ───
    createAppPassword(name) {
        const id = 'ap_' + this._nextAppPasswordId++;
        const ap = {
            id,
            name,
            createdAt: new Date().toISOString(),
            lastUsed: null
        };
        this.appPasswords.push(ap);
        this.notify();
        return ap;
    },

    deleteAppPassword(id) {
        this.appPasswords = this.appPasswords.filter(a => a.id !== id);
        this.notify();
    },

    // ─── Mutations: Merge contacts ───
    mergeContacts(keepId, mergeId) {
        const keep = this.getContactById(keepId);
        const merge = this.getContactById(mergeId);
        if (!keep || !merge) return null;

        // Merge empty fields from merge into keep
        if (!keep.phone && merge.phone) keep.phone = merge.phone;
        if (!keep.company && merge.company) keep.company = merge.company;
        if (!keep.jobTitle && merge.jobTitle) keep.jobTitle = merge.jobTitle;
        if (!keep.address && merge.address) keep.address = merge.address;
        if (!keep.birthday && merge.birthday) keep.birthday = merge.birthday;
        if (!keep.notes && merge.notes) keep.notes = merge.notes;
        // Merge groups
        merge.groups.forEach(g => {
            if (!keep.groups.includes(g)) keep.groups.push(g);
        });
        keep.updatedAt = new Date().toISOString();

        // Remove the merged contact
        this.contacts = this.contacts.filter(c => c.id !== mergeId);
        this.notify();
        return keep;
    },

    // ─── Find Duplicate Contacts ───
    findDuplicates() {
        const pairs = [];
        const seen = new Set();
        for (let i = 0; i < this.contacts.length; i++) {
            for (let j = i + 1; j < this.contacts.length; j++) {
                const a = this.contacts[i];
                const b = this.contacts[j];
                const key = [a.id, b.id].sort().join(':');
                if (seen.has(key)) continue;

                // Match on email
                if (a.email && b.email && a.email.toLowerCase() === b.email.toLowerCase()) {
                    seen.add(key);
                    pairs.push({ a, b, reason: 'Same email address' });
                    continue;
                }
                // Match on full name (both first + last must match, case-insensitive)
                const nameA = ((a.firstName || '') + ' ' + (a.lastName || '')).trim().toLowerCase();
                const nameB = ((b.firstName || '') + ' ' + (b.lastName || '')).trim().toLowerCase();
                if (nameA && nameB && nameA === nameB) {
                    seen.add(key);
                    pairs.push({ a, b, reason: 'Same name' });
                    continue;
                }
                // Match on last name + same company
                if (a.lastName && b.lastName && a.company && b.company &&
                    a.lastName.toLowerCase() === b.lastName.toLowerCase() &&
                    a.company.toLowerCase() === b.company.toLowerCase()) {
                    seen.add(key);
                    pairs.push({ a, b, reason: 'Same last name & company' });
                }
            }
        }
        return pairs;
    },

    // ─── Selection ───
    toggleContactSelection(id) {
        const idx = this.selectedContactIds.indexOf(id);
        if (idx >= 0) {
            this.selectedContactIds.splice(idx, 1);
        } else {
            this.selectedContactIds.push(id);
        }
        this.notify();
    },

    selectAllContacts(ids) {
        this.selectedContactIds = ids.slice();
        this.notify();
    },

    clearSelection() {
        this.selectedContactIds = [];
        this.notify();
    },

    // ─── Navigation ───
    setView(view, itemId) {
        this.currentView = view;
        this.currentContactId = null;
        this.currentGroupId = null;
        if (view === 'contact-detail' || view === 'edit-contact') {
            this.currentContactId = itemId || null;
        }
        if (view === 'group-detail') {
            this.currentGroupId = itemId || null;
        }
        this.currentPage = 1;
        this._listeners.forEach(fn => fn());
    },

    setSearch(query) {
        this.searchQuery = query;
        this.currentPage = 1;
        this._listeners.forEach(fn => fn());
    },

    setDirectorySearch(query) {
        this.directorySearch = query;
        this._listeners.forEach(fn => fn());
    },

    setOtherContactSearch(query) {
        this.otherContactSearch = query;
        this._listeners.forEach(fn => fn());
    },

    setContactSort(sort) {
        this.contactSort = sort;
        this.currentPage = 1;
        this._listeners.forEach(fn => fn());
    },

    setContactFilter(filter) {
        this.contactFilter = filter;
        this.currentPage = 1;
        this.selectedContactIds = [];
        this._listeners.forEach(fn => fn());
    },

    setPage(page) {
        this.currentPage = page;
        this._listeners.forEach(fn => fn());
    }
};

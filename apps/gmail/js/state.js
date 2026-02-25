// ============================================================
// state.js — Centralized state management for Gmail app
// ============================================================

const AppState = {
    // ---- Persistent State ----
    emails: [],
    labels: [],
    filters: [],
    settings: {},
    contacts: [],
    blockedSenders: [],
    currentUser: null,

    // ---- ID Counters ----
    _nextEmailId: 200,
    _nextLabelId: 30,
    _nextFilterId: 20,

    // ---- UI State (not persisted) ----
    currentView: 'inbox',
    currentCategory: 'primary',
    currentEmailId: null,
    selectedEmailIds: new Set(),
    searchQuery: '',
    searchResults: null,
    settingsOpen: false,
    settingsTab: 'general',
    composeOpen: false,
    composeDraft: null,
    contextMenuOpen: false,
    labelPickerOpen: false,
    currentPage: 1,
    expandedLabels: true,

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
            this.emails = persisted.emails || [];
            this.labels = persisted.labels || [];
            this.filters = persisted.filters || [];
            this.settings = persisted.settings || {};
            this.contacts = persisted.contacts || [];
            this.blockedSenders = persisted.blockedSenders || [];
            this.currentUser = persisted.currentUser || null;
            this._nextEmailId = persisted._nextEmailId || 200;
            this._nextLabelId = persisted._nextLabelId || 30;
            this._nextFilterId = persisted._nextFilterId || 20;
        } else {
            this._loadSeedData();
        }
        this._recalculateLabelCounts();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.emails = JSON.parse(JSON.stringify(EMAILS));
        this.labels = JSON.parse(JSON.stringify(LABELS));
        this.filters = JSON.parse(JSON.stringify(FILTERS));
        this.settings = JSON.parse(JSON.stringify(SETTINGS));
        this.contacts = JSON.parse(JSON.stringify(CONTACTS));
        this.blockedSenders = JSON.parse(JSON.stringify(BLOCKED_SENDERS));
        this._nextEmailId = EMAILS.length > 0 ? Math.max(...EMAILS.map(e => e.id)) + 1 : 200;
        this._nextLabelId = 30;
        this._nextFilterId = 20;
    },

    _loadPersistedData() {
        try {
            const saved = localStorage.getItem('gmailAppState');
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('gmailAppState');
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    },

    // ---- Persistence ----

    _persist() {
        const state = this.getSerializableState();
        localStorage.setItem('gmailAppState', JSON.stringify(state));
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
            _seedVersion: SEED_DATA_VERSION,
            emails: this.emails,
            labels: this.labels,
            filters: this.filters,
            settings: this.settings,
            contacts: this.contacts,
            blockedSenders: this.blockedSenders,
            currentUser: this.currentUser,
            _nextEmailId: this._nextEmailId,
            _nextLabelId: this._nextLabelId,
            _nextFilterId: this._nextFilterId,
        };
    },

    resetToSeedData() {
        localStorage.removeItem('gmailAppState');
        this._loadSeedData();
        this._recalculateLabelCounts();
        this.currentView = 'inbox';
        this.currentCategory = 'primary';
        this.currentEmailId = null;
        this.selectedEmailIds = new Set();
        this.searchQuery = '';
        this.searchResults = null;
        this.currentPage = 1;
        this.notify();
    },

    // ---- Email Queries ----

    getEmailById(id) {
        return this.emails.find(e => e.id === id);
    },

    getEmailsByThread(threadId) {
        return this.emails.filter(e => e.threadId === threadId).sort((a, b) => new Date(a.date) - new Date(b.date));
    },

    getInboxEmails() {
        return this.emails.filter(e =>
            e.labels.includes('INBOX') && !e.isTrashed && !e.isSpam && !e.isDraft && !e.isSnoozed
        );
    },

    getInboxEmailsByCategory(category) {
        return this.getInboxEmails().filter(e => e.category === category);
    },

    getStarredEmails() {
        return this.emails.filter(e => e.isStarred && !e.isTrashed && !e.isSpam);
    },

    getSnoozedEmails() {
        return this.emails.filter(e => e.isSnoozed && !e.isTrashed);
    },

    getSentEmails() {
        return this.emails.filter(e => e.isSent && !e.isTrashed);
    },

    getDraftEmails() {
        return this.emails.filter(e => e.isDraft && !e.isTrashed);
    },

    getTrashEmails() {
        return this.emails.filter(e => e.isTrashed);
    },

    getSpamEmails() {
        return this.emails.filter(e => e.isSpam && !e.isTrashed);
    },

    getImportantEmails() {
        return this.emails.filter(e => e.isImportant && !e.isTrashed && !e.isSpam);
    },

    getAllMailEmails() {
        return this.emails.filter(e => !e.isTrashed && !e.isSpam);
    },

    getArchivedEmails() {
        return this.emails.filter(e => e.isArchived && !e.isTrashed && !e.isSpam && !e.labels.includes('INBOX'));
    },

    getEmailsByLabel(labelId) {
        return this.emails.filter(e => e.labels.includes(labelId) && !e.isTrashed && !e.isSpam);
    },

    getEmailsForView(view) {
        switch (view) {
            case 'inbox': return this.getInboxEmails();
            case 'starred': return this.getStarredEmails();
            case 'snoozed': return this.getSnoozedEmails();
            case 'sent': return this.getSentEmails();
            case 'drafts': return this.getDraftEmails();
            case 'trash': return this.getTrashEmails();
            case 'spam': return this.getSpamEmails();
            case 'important': return this.getImportantEmails();
            case 'allmail': return this.getAllMailEmails();
            default:
                if (view.startsWith('label_')) return this.getEmailsByLabel(view);
                return this.getInboxEmails();
        }
    },

    searchEmails(query) {
        if (!query) return null;
        const q = query.toLowerCase().trim();
        const results = this.emails.filter(e => {
            if (e.isTrashed || e.isSpam) return false;
            // Parse search operators
            if (q.startsWith('from:')) {
                const val = q.slice(5).trim();
                return e.from.email.toLowerCase().includes(val) || e.from.name.toLowerCase().includes(val);
            }
            if (q.startsWith('to:')) {
                const val = q.slice(3).trim();
                return e.to.some(t => t.email.toLowerCase().includes(val) || t.name.toLowerCase().includes(val));
            }
            if (q.startsWith('subject:')) {
                const val = q.slice(8).trim();
                return e.subject.toLowerCase().includes(val);
            }
            if (q.startsWith('label:')) {
                const val = q.slice(6).trim();
                const label = this.labels.find(l => l.name.toLowerCase() === val);
                return label && e.labels.includes(label.id);
            }
            if (q.startsWith('has:attachment') || q.startsWith('has:attachments')) {
                return e.hasAttachments;
            }
            if (q === 'is:unread') return !e.isRead;
            if (q === 'is:read') return e.isRead;
            if (q === 'is:starred') return e.isStarred;
            if (q === 'is:important') return e.isImportant;
            if (q === 'is:snoozed') return e.isSnoozed;
            if (q === 'is:muted') return e.isMuted;
            if (q === 'in:archive' || q === 'in:archived') return e.isArchived;
            if (q.startsWith('category:')) {
                const cat = q.slice(9).trim();
                return e.category === cat;
            }
            // General text search
            return e.subject.toLowerCase().includes(q) ||
                   e.snippet.toLowerCase().includes(q) ||
                   e.from.name.toLowerCase().includes(q) ||
                   e.from.email.toLowerCase().includes(q) ||
                   (e.body && e.body.toLowerCase().includes(q));
        });
        return results;
    },

    // ---- Email Mutations ----

    markAsRead(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) email.isRead = true;
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    markAsUnread(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) email.isRead = false;
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    toggleStar(emailId) {
        const email = this.getEmailById(emailId);
        if (!email) return;
        if (email.isStarred) {
            email.isStarred = false;
            email.starType = null;
        } else {
            email.isStarred = true;
            email.starType = this.settings.enabledStars[0] || 'yellow-star';
        }
        this.notify();
    },

    cycleStar(emailId) {
        const email = this.getEmailById(emailId);
        if (!email) return;
        const stars = this.settings.enabledStars || ['yellow-star'];
        if (!email.isStarred) {
            email.isStarred = true;
            email.starType = stars[0];
        } else {
            const idx = stars.indexOf(email.starType);
            if (idx < stars.length - 1) {
                email.starType = stars[idx + 1];
            } else {
                email.isStarred = false;
                email.starType = null;
            }
        }
        this.notify();
    },

    toggleImportant(emailId) {
        const email = this.getEmailById(emailId);
        if (!email) return;
        email.isImportant = !email.isImportant;
        if (email.isImportant && !email.labels.includes('IMPORTANT')) {
            email.labels.push('IMPORTANT');
        } else if (!email.isImportant) {
            email.labels = email.labels.filter(l => l !== 'IMPORTANT');
        }
        this.notify();
    },

    archiveEmails(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.labels = email.labels.filter(l => l !== 'INBOX');
                email.isArchived = true;
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    moveToInbox(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                if (!email.labels.includes('INBOX')) email.labels.push('INBOX');
                email.isArchived = false;
                email.isTrashed = false;
                email.isSpam = false;
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    trashEmails(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.isTrashed = true;
                email.labels = email.labels.filter(l => l !== 'INBOX');
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    deleteForever(emailIds) {
        this.emails = this.emails.filter(e => !emailIds.includes(e.id));
        this._recalculateLabelCounts();
        this.notify();
    },

    emptyTrash() {
        this.emails = this.emails.filter(e => !e.isTrashed);
        this._recalculateLabelCounts();
        this.notify();
    },

    emptySpam() {
        this.emails = this.emails.filter(e => !e.isSpam);
        this._recalculateLabelCounts();
        this.notify();
    },

    markAsSpam(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.isSpam = true;
                email.labels = email.labels.filter(l => l !== 'INBOX');
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    unmarkSpam(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.isSpam = false;
                if (!email.labels.includes('INBOX')) email.labels.push('INBOX');
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    snoozeEmails(emailIds, snoozeUntil) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.isSnoozed = true;
                email.snoozeUntil = snoozeUntil;
                email.labels = email.labels.filter(l => l !== 'INBOX');
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    unsnoozeEmails(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.isSnoozed = false;
                email.snoozeUntil = null;
                if (!email.labels.includes('INBOX')) email.labels.push('INBOX');
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    muteEmails(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.isMuted = true;
                email.labels = email.labels.filter(l => l !== 'INBOX');
                email.isArchived = true;
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    addLabel(emailIds, labelId) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email && !email.labels.includes(labelId)) {
                email.labels.push(labelId);
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    removeLabel(emailIds, labelId) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.labels = email.labels.filter(l => l !== labelId);
            }
        }
        this._recalculateLabelCounts();
        this.notify();
    },

    moveToCategory(emailIds, category) {
        const catLabel = 'CATEGORY_' + category.toUpperCase();
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.labels = email.labels.filter(l => !l.startsWith('CATEGORY_'));
                email.labels.push(catLabel);
                email.category = category;
            }
        }
        this.notify();
    },

    // ---- Compose / Send ----

    sendEmail(to, cc, bcc, subject, body) {
        const id = this._nextEmailId++;
        const email = {
            id,
            threadId: 'thread_' + id,
            from: { name: this.currentUser.name, email: this.currentUser.email },
            to: to.split(',').map(e => e.trim()).filter(Boolean).map(e => {
                const contact = this.contacts.find(c => c.email === e || c.name === e);
                return { name: contact ? contact.name : e, email: contact ? contact.email : e };
            }),
            cc: cc ? cc.split(',').map(e => ({ name: e.trim(), email: e.trim() })) : [],
            bcc: bcc ? bcc.split(',').map(e => ({ name: e.trim(), email: e.trim() })) : [],
            subject: subject || '(no subject)',
            snippet: (body || '').substring(0, 100),
            body: body || '',
            date: new Date().toISOString(),
            isRead: true,
            isStarred: false,
            starType: null,
            isImportant: false,
            labels: ['SENT'],
            category: 'primary',
            hasAttachments: false,
            attachments: [],
            isSnoozed: false,
            snoozeUntil: null,
            isTrashed: false,
            isSpam: false,
            isArchived: false,
            isDraft: false,
            isSent: true,
            isMuted: false,
        };
        this.emails.unshift(email);
        this._recalculateLabelCounts();
        this.notify();
        return email;
    },

    saveDraft(to, cc, bcc, subject, body) {
        const id = this._nextEmailId++;
        const draft = {
            id,
            threadId: 'thread_' + id,
            from: { name: this.currentUser.name, email: this.currentUser.email },
            to: to ? to.split(',').map(e => ({ name: e.trim(), email: e.trim() })) : [],
            cc: cc ? cc.split(',').map(e => ({ name: e.trim(), email: e.trim() })) : [],
            bcc: bcc ? bcc.split(',').map(e => ({ name: e.trim(), email: e.trim() })) : [],
            subject: subject || '(no subject)',
            snippet: (body || '').substring(0, 100),
            body: body || '',
            date: new Date().toISOString(),
            isRead: true,
            isStarred: false,
            starType: null,
            isImportant: false,
            labels: ['DRAFT'],
            category: 'primary',
            hasAttachments: false,
            attachments: [],
            isSnoozed: false,
            snoozeUntil: null,
            isTrashed: false,
            isSpam: false,
            isArchived: false,
            isDraft: true,
            isSent: false,
            isMuted: false,
        };
        this.emails.unshift(draft);
        this._recalculateLabelCounts();
        this.notify();
        return draft;
    },

    // ---- Label Mutations ----

    createLabel(name, color = null, parentId = null) {
        const id = 'label_' + this._nextLabelId++;
        const label = {
            id,
            name,
            type: 'user',
            color,
            visible: true,
            parentId,
            messageCount: 0,
            unreadCount: 0,
        };
        this.labels.push(label);
        this.notify();
        return label;
    },

    updateLabel(labelId, updates) {
        const label = this.labels.find(l => l.id === labelId);
        if (!label) return;
        if (updates.name !== undefined) label.name = updates.name;
        if (updates.color !== undefined) label.color = updates.color;
        if (updates.visible !== undefined) label.visible = updates.visible;
        if (updates.parentId !== undefined) label.parentId = updates.parentId;
        this.notify();
    },

    deleteLabel(labelId) {
        // Remove label from all emails
        for (const email of this.emails) {
            email.labels = email.labels.filter(l => l !== labelId);
        }
        // Remove child labels
        const children = this.labels.filter(l => l.parentId === labelId);
        for (const child of children) {
            this.deleteLabel(child.id);
        }
        this.labels = this.labels.filter(l => l.id !== labelId);
        this._recalculateLabelCounts();
        this.notify();
    },

    getLabelById(id) {
        return this.labels.find(l => l.id === id);
    },

    getUserLabels() {
        return this.labels.filter(l => l.type === 'user');
    },

    getTopLevelUserLabels() {
        return this.labels.filter(l => l.type === 'user' && !l.parentId);
    },

    getChildLabels(parentId) {
        return this.labels.filter(l => l.parentId === parentId);
    },

    // ---- Filter Mutations ----

    createFilter(criteria, actions) {
        const id = 'filter_' + this._nextFilterId++;
        const filter = {
            id,
            criteria,
            actions,
            enabled: true,
            createdAt: new Date().toISOString(),
        };
        this.filters.push(filter);
        this.notify();
        return filter;
    },

    updateFilter(filterId, criteria, actions) {
        const filter = this.filters.find(f => f.id === filterId);
        if (!filter) return;
        if (criteria) filter.criteria = criteria;
        if (actions) filter.actions = actions;
        this.notify();
    },

    deleteFilter(filterId) {
        this.filters = this.filters.filter(f => f.id !== filterId);
        this.notify();
    },

    // ---- Settings Mutations ----

    updateSetting(key, value) {
        if (key.includes('.')) {
            const parts = key.split('.');
            let obj = this.settings;
            for (let i = 0; i < parts.length - 1; i++) {
                obj = obj[parts[i]];
            }
            obj[parts[parts.length - 1]] = value;
        } else {
            this.settings[key] = value;
        }
        this.notify();
    },

    updateSettings(updates) {
        Object.assign(this.settings, updates);
        this.notify();
    },

    // ---- Blocked Senders ----

    blockSender(email) {
        if (!this.blockedSenders.find(b => b.email === email)) {
            this.blockedSenders.push({
                email,
                blockedAt: new Date().toISOString(),
            });
            this.notify();
        }
    },

    unblockSender(email) {
        this.blockedSenders = this.blockedSenders.filter(b => b.email !== email);
        this.notify();
    },

    // ---- Label Count Recalculation ----

    _recalculateLabelCounts() {
        for (const label of this.labels) {
            const emails = this.emails.filter(e => {
                if (label.id === 'INBOX') return e.labels.includes('INBOX') && !e.isTrashed && !e.isSpam && !e.isSnoozed;
                if (label.id === 'STARRED') return e.isStarred && !e.isTrashed && !e.isSpam;
                if (label.id === 'SNOOZED') return e.isSnoozed && !e.isTrashed;
                if (label.id === 'SENT') return e.isSent && !e.isTrashed;
                if (label.id === 'DRAFT') return e.isDraft && !e.isTrashed;
                if (label.id === 'TRASH') return e.isTrashed;
                if (label.id === 'SPAM') return e.isSpam && !e.isTrashed;
                if (label.id === 'IMPORTANT') return e.isImportant && !e.isTrashed && !e.isSpam;
                if (label.id === 'ALL_MAIL') return !e.isTrashed && !e.isSpam;
                return e.labels.includes(label.id) && !e.isTrashed && !e.isSpam;
            });
            label.messageCount = emails.length;
            label.unreadCount = emails.filter(e => !e.isRead).length;
        }
    },

    // ---- Pagination ----

    getPagedEmails(emails) {
        const pageSize = this.settings.maxPageSize || 50;
        const start = (this.currentPage - 1) * pageSize;
        const end = start + pageSize;
        return {
            items: emails.slice(start, end),
            total: emails.length,
            start: start + 1,
            end: Math.min(end, emails.length),
            hasNext: end < emails.length,
            hasPrev: this.currentPage > 1,
        };
    },

    // ---- Sort ----

    sortEmails(emails) {
        return [...emails].sort((a, b) => new Date(b.date) - new Date(a.date));
    },
};

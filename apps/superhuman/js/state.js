const AppState = {
    // ---- Core state ----
    // All properties from INITIAL_STATE are spread onto AppState during init()

    // ---- Internal ----
    _listeners: [],
    _nextEmailId: 200,
    _nextLabelId: 30,
    _nextSnippetId: 20,
    _nextEventId: 30,

    // ---- Lifecycle ----

    init() {
        const saved = localStorage.getItem('superhuman_state');
        let source = null;
        if (saved) {
            try {
                const parsed = JSON.parse(saved);
                if (parsed.version === SEED_DATA_VERSION) {
                    source = parsed;
                } else {
                    localStorage.removeItem('superhuman_state');
                }
            } catch(e) {
                localStorage.removeItem('superhuman_state');
            }
        }
        if (!source) {
            source = JSON.parse(JSON.stringify(INITIAL_STATE));
        }
        // Spread all state properties onto AppState
        Object.assign(this, source);
        // Reset transient UI state
        this.selectedEmailId = null;
        this.selectedFolder = 'inbox';
        this.selectedSplit = 'split_important';
        this.composerOpen = false;
        this.composerDraft = null;
        this.searchQuery = '';
        this.searchResults = [];
        this.commandPaletteOpen = false;
        this.commandPaletteQuery = '';
        // Recalculate folder counts
        this._recalculateFolderCounts();
    },

    resetToSeedData() {
        localStorage.removeItem('superhuman_state');
        const fresh = JSON.parse(JSON.stringify(INITIAL_STATE));
        // Remove old data keys
        const keysToKeep = ['_listeners', '_nextEmailId', '_nextLabelId', '_nextSnippetId', '_nextEventId'];
        for (const key of Object.keys(this)) {
            if (!keysToKeep.includes(key) && typeof this[key] !== 'function') {
                delete this[key];
            }
        }
        Object.assign(this, fresh);
        this.selectedEmailId = null;
        this.selectedFolder = 'inbox';
        this.selectedSplit = 'split_important';
        this.composerOpen = false;
        this.composerDraft = null;
        this.searchQuery = '';
        this.searchResults = [];
        this.commandPaletteOpen = false;
        this.commandPaletteQuery = '';
        this._recalculateFolderCounts();
        this.notify();
    },

    // ---- Observer ----

    subscribe(fn) {
        this._listeners.push(fn);
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        for (const fn of this._listeners) {
            try { fn(); } catch(e) { console.error('Listener error:', e); }
        }
    },

    _persist() {
        const state = this.getSerializableState();
        localStorage.setItem('superhuman_state', JSON.stringify(state));
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
            version: this.version,
            currentUser: this.currentUser,
            contacts: this.contacts,
            labels: this.labels,
            autoLabels: this.autoLabels,
            splits: this.splits,
            folders: this.folders,
            snippets: this.snippets,
            calendarEvents: this.calendarEvents,
            emails: this.emails,
            settings: this.settings,
            blockedSenders: this.blockedSenders,
            recentOpens: this.recentOpens,
            folderCounts: this.folderCounts,
            _nextEmailId: this._nextEmailId,
            _nextLabelId: this._nextLabelId,
            _nextSnippetId: this._nextSnippetId,
            _nextEventId: this._nextEventId
        };
    },

    // ---- Folder Counts ----

    _recalculateFolderCounts() {
        const counts = {};
        for (const f of FOLDERS) {
            counts[f.id] = 0;
        }
        for (const email of this.emails) {
            if (email.isDraft) {
                counts['drafts'] = (counts['drafts'] || 0) + 1;
            } else if (email.isScheduled) {
                counts['scheduled'] = (counts['scheduled'] || 0) + 1;
            } else if (email.folder && counts.hasOwnProperty(email.folder)) {
                counts[email.folder]++;
            }
            if (email.reminder) {
                counts['reminders'] = (counts['reminders'] || 0) + 1;
            }
        }
        this.folderCounts = counts;
    },

    // ---- Email Queries ----

    getEmailsForFolder(folderId) {
        if (folderId === 'drafts') {
            return this.emails.filter(e => e.isDraft).sort((a, b) => new Date(b.date) - new Date(a.date));
        }
        if (folderId === 'scheduled') {
            return this.emails.filter(e => e.isScheduled).sort((a, b) => new Date(a.scheduledTime) - new Date(b.scheduledTime));
        }
        if (folderId === 'reminders') {
            return this.emails.filter(e => e.reminder !== null).sort((a, b) => new Date(a.reminder.date) - new Date(b.reminder.date));
        }
        return this.emails.filter(e => e.folder === folderId && !e.isDraft && !e.isScheduled)
            .sort((a, b) => new Date(b.date) - new Date(a.date));
    },

    getEmailsForSplit(splitId) {
        const inboxEmails = this.getEmailsForFolder('inbox');
        const split = this.splits.find(s => s.id === splitId);
        if (!split) return inboxEmails;

        if (split.criteria.type === 'important') {
            return inboxEmails.filter(e => e.split === 'important');
        }
        if (split.criteria.type === 'other') {
            return inboxEmails.filter(e => e.split === 'other');
        }
        if (split.criteria.type === 'calendar') {
            return inboxEmails.filter(e => e.split === 'calendar');
        }
        if (split.criteria.autoLabels) {
            return inboxEmails.filter(e =>
                e.autoLabels && e.autoLabels.some(al => split.criteria.autoLabels.includes(al))
            );
        }
        return inboxEmails;
    },

    getSplitCounts() {
        const inboxEmails = this.getEmailsForFolder('inbox');
        const counts = {};
        for (const split of this.splits) {
            if (split.criteria.type === 'important') {
                counts[split.id] = inboxEmails.filter(e => e.split === 'important').length;
            } else if (split.criteria.type === 'other') {
                counts[split.id] = inboxEmails.filter(e => e.split === 'other').length;
            } else if (split.criteria.type === 'calendar') {
                counts[split.id] = inboxEmails.filter(e => e.split === 'calendar').length;
            } else if (split.criteria.autoLabels) {
                counts[split.id] = inboxEmails.filter(e =>
                    e.autoLabels && e.autoLabels.some(al => split.criteria.autoLabels.includes(al))
                ).length;
            }
        }
        return counts;
    },

    getEmailById(id) {
        return this.emails.find(e => e.id === id) || null;
    },

    getThreadEmails(threadId) {
        return this.emails.filter(e => e.threadId === threadId)
            .sort((a, b) => new Date(a.date) - new Date(b.date));
    },

    getStarredEmails() {
        return this.emails.filter(e => e.isStarred && e.folder !== 'trash' && e.folder !== 'spam')
            .sort((a, b) => new Date(b.date) - new Date(a.date));
    },

    getUnreadCount(folderId) {
        if (folderId) {
            return this.emails.filter(e => e.folder === folderId && !e.isRead && !e.isDraft && !e.isScheduled).length;
        }
        return this.emails.filter(e => e.folder === 'inbox' && !e.isRead).length;
    },

    // ---- Email Mutations ----

    markAsRead(emailId) {
        const email = this.getEmailById(emailId);
        if (email && !email.isRead) {
            email.isRead = true;
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    markAsUnread(emailId) {
        const email = this.getEmailById(emailId);
        if (email && email.isRead) {
            email.isRead = false;
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    toggleStar(emailId) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.isStarred = !email.isStarred;
            this.notify();
        }
    },

    markDone(emailId) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.folder = 'done';
            email.isRead = true;
            email.reminder = null;
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    markDoneMultiple(emailIds) {
        for (const id of emailIds) {
            const email = this.getEmailById(id);
            if (email) {
                email.folder = 'done';
                email.isRead = true;
                email.reminder = null;
            }
        }
        this._recalculateFolderCounts();
        this.notify();
    },

    moveToFolder(emailId, folderId) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.folder = folderId;
            if (folderId === 'trash' || folderId === 'spam') {
                email.reminder = null;
            }
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    moveToInbox(emailId) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.folder = 'inbox';
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    trashEmail(emailId) {
        this.moveToFolder(emailId, 'trash');
    },

    spamEmail(emailId) {
        this.moveToFolder(emailId, 'spam');
    },

    deleteEmail(emailId) {
        this.emails = this.emails.filter(e => e.id !== emailId);
        this._recalculateFolderCounts();
        this.notify();
    },

    setReminder(emailId, reminderDate, type = 'manual') {
        const email = this.getEmailById(emailId);
        if (email) {
            email.reminder = { date: reminderDate, type: type };
            email.folder = 'inbox'; // Keep in inbox but with reminder
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    clearReminder(emailId) {
        const email = this.getEmailById(emailId);
        if (email && email.reminder) {
            email.reminder = null;
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    addLabel(emailId, labelId) {
        const email = this.getEmailById(emailId);
        if (email && !email.labels.includes(labelId)) {
            email.labels.push(labelId);
            this.notify();
        }
    },

    removeLabel(emailId, labelId) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.labels = email.labels.filter(l => l !== labelId);
            this.notify();
        }
    },

    // ---- Compose / Draft ----

    createDraft(draft) {
        const id = 'email_' + String(this._nextEmailId++).padStart(3, '0');
        const newDraft = {
            id: id,
            threadId: draft.threadId || id,
            subject: draft.subject || '',
            from: { name: this.currentUser.name, email: this.currentUser.email },
            to: draft.to || [],
            cc: draft.cc || [],
            bcc: draft.bcc || [],
            body: draft.body || '',
            snippet: (draft.body || '').replace(/<[^>]*>/g, '').substring(0, 100),
            date: new Date().toISOString(),
            isRead: true,
            isStarred: false,
            folder: 'drafts',
            split: 'important',
            labels: [],
            autoLabels: [],
            hasAttachments: false,
            attachments: [],
            readStatus: { enabled: false, opens: [] },
            reminder: null,
            isDraft: true,
            isScheduled: false,
            scheduledTime: null,
            threadMessages: [],
            replyTo: draft.replyTo || null,
            forwardOf: draft.forwardOf || null
        };
        this.emails.push(newDraft);
        this._recalculateFolderCounts();
        this.notify();
        return newDraft;
    },

    updateDraft(emailId, updates) {
        const email = this.getEmailById(emailId);
        if (email && email.isDraft) {
            Object.assign(email, updates);
            email.snippet = (email.body || '').replace(/<[^>]*>/g, '').substring(0, 100);
            email.date = new Date().toISOString();
            this.notify();
        }
    },

    sendEmail(emailId) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.isDraft = false;
            email.isScheduled = false;
            email.folder = 'sent';
            email.date = new Date().toISOString();
            email.readStatus = { enabled: this.settings.readStatuses.enabled, opens: [] };
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    scheduleEmail(emailId, scheduledTime) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.isDraft = false;
            email.isScheduled = true;
            email.scheduledTime = scheduledTime;
            email.folder = 'scheduled';
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    cancelScheduledEmail(emailId) {
        const email = this.getEmailById(emailId);
        if (email && email.isScheduled) {
            email.isScheduled = false;
            email.isDraft = true;
            email.scheduledTime = null;
            email.folder = 'drafts';
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    // ---- Search ----

    searchEmails(query) {
        if (!query || !query.trim()) {
            this.searchResults = [];
            this.searchQuery = '';
            this.notify();
            return [];
        }
        this.searchQuery = query;
        const q = query.toLowerCase();
        const results = this.emails.filter(email => {
            // Check for search operators
            if (q.startsWith('from:')) {
                const val = q.substring(5).trim();
                return email.from.email.toLowerCase().includes(val) || email.from.name.toLowerCase().includes(val);
            }
            if (q.startsWith('to:')) {
                const val = q.substring(3).trim();
                return email.to.some(t => t.email.toLowerCase().includes(val) || t.name.toLowerCase().includes(val));
            }
            if (q.startsWith('subject:')) {
                const val = q.substring(8).trim();
                return email.subject.toLowerCase().includes(val);
            }
            if (q.startsWith('has:attachment')) {
                return email.hasAttachments;
            }
            if (q.startsWith('is:unread')) {
                return !email.isRead;
            }
            if (q.startsWith('is:starred')) {
                return email.isStarred;
            }
            if (q.startsWith('label:')) {
                const val = q.substring(6).trim();
                const label = this.labels.find(l => l.name.toLowerCase() === val);
                return label && email.labels.includes(label.id);
            }
            if (q.startsWith('in:')) {
                const val = q.substring(3).trim();
                return email.folder === val;
            }
            // General text search across subject, from, snippet, body
            return email.subject.toLowerCase().includes(q) ||
                email.from.name.toLowerCase().includes(q) ||
                email.from.email.toLowerCase().includes(q) ||
                email.snippet.toLowerCase().includes(q) ||
                (email.body && email.body.toLowerCase().includes(q));
        }).sort((a, b) => new Date(b.date) - new Date(a.date));

        this.searchResults = results;
        this.notify();
        return results;
    },

    // ---- Label Mutations ----

    createLabel(name, color) {
        const id = 'label_' + this._nextLabelId++;
        const label = {
            id: id,
            name: name,
            color: color || { background: '#e8eaed', text: '#5f6368' },
            isSystem: false,
            isAutoLabel: false
        };
        this.labels.push(label);
        this.notify();
        return label;
    },

    updateLabel(labelId, updates) {
        const label = this.labels.find(l => l.id === labelId);
        if (label && !label.isSystem) {
            Object.assign(label, updates);
            this.notify();
        }
    },

    deleteLabel(labelId) {
        this.labels = this.labels.filter(l => l.id !== labelId);
        // Remove label from all emails
        for (const email of this.emails) {
            email.labels = email.labels.filter(l => l !== labelId);
        }
        this.notify();
    },

    getEmailsForLabel(labelId) {
        return this.emails.filter(e => e.labels.includes(labelId))
            .sort((a, b) => new Date(b.date) - new Date(a.date));
    },

    // ---- Snippet Mutations ----

    createSnippet(snippet) {
        const id = 'snippet_' + String(this._nextSnippetId++).padStart(2, '0');
        const newSnippet = {
            id: id,
            name: snippet.name,
            body: snippet.body || '',
            variables: snippet.variables || [],
            placeholders: snippet.placeholders || [],
            isShared: snippet.isShared || false,
            author: this.currentUser.name,
            metrics: { sends: 0, openRate: 0, responseRate: 0 },
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        this.snippets.push(newSnippet);
        this.notify();
        return newSnippet;
    },

    updateSnippet(snippetId, updates) {
        const snippet = this.snippets.find(s => s.id === snippetId);
        if (snippet) {
            Object.assign(snippet, updates);
            snippet.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    deleteSnippet(snippetId) {
        this.snippets = this.snippets.filter(s => s.id !== snippetId);
        this.notify();
    },

    // ---- Calendar Event Mutations ----

    createCalendarEvent(event) {
        const id = 'event_' + String(this._nextEventId++).padStart(2, '0');
        const newEvent = {
            id: id,
            title: event.title || 'New Event',
            start: event.start,
            end: event.end,
            location: event.location || '',
            description: event.description || '',
            attendees: event.attendees || [],
            meetingLink: event.meetingLink || this.settings.calendar.meetingLink || '',
            calendar: event.calendar || 'Work',
            color: event.color || '#4285f4',
            isAllDay: event.isAllDay || false,
            recurrence: event.recurrence || null
        };
        this.calendarEvents.push(newEvent);
        this.notify();
        return newEvent;
    },

    updateCalendarEvent(eventId, updates) {
        const event = this.calendarEvents.find(e => e.id === eventId);
        if (event) {
            Object.assign(event, updates);
            this.notify();
        }
    },

    deleteCalendarEvent(eventId) {
        this.calendarEvents = this.calendarEvents.filter(e => e.id !== eventId);
        this.notify();
    },

    // ---- Settings Mutations ----

    updateSetting(path, value) {
        // path is like 'general.theme' or 'reminders.autoReminders'
        const parts = path.split('.');
        let obj = this.settings;
        for (let i = 0; i < parts.length - 1; i++) {
            obj = obj[parts[i]];
            if (!obj) return;
        }
        obj[parts[parts.length - 1]] = value;
        this.notify();
    },

    getSetting(path) {
        const parts = path.split('.');
        let obj = this.settings;
        for (const part of parts) {
            obj = obj[part];
            if (obj === undefined) return undefined;
        }
        return obj;
    },

    // ---- Split Mutations ----

    addSplit(split) {
        this.splits.push(split);
        if (this.settings.splitInbox.splits.indexOf(split.id) === -1) {
            this.settings.splitInbox.splits.push(split.id);
        }
        this.notify();
    },

    updateSplit(splitId, updates) {
        const split = this.splits.find(s => s.id === splitId);
        if (split) {
            Object.assign(split, updates);
            this.notify();
        }
    },

    removeSplit(splitId) {
        this.splits = this.splits.filter(s => s.id !== splitId);
        this.settings.splitInbox.splits = this.settings.splitInbox.splits.filter(id => id !== splitId);
        this.notify();
    },

    moveEmailToSplit(emailId, splitType) {
        const email = this.getEmailById(emailId);
        if (email) {
            email.split = splitType;
            this.notify();
        }
    },

    // ---- Auto Label Mutations ----

    toggleAutoLabel(autoLabelId) {
        const al = this.autoLabels.find(a => a.id === autoLabelId);
        if (al) {
            al.isEnabled = !al.isEnabled;
            this.notify();
        }
    },

    // ---- Auto Archive ----

    updateAutoArchive(enabled, autoLabelIds) {
        this.settings.autoArchive.enabled = enabled;
        this.settings.autoArchive.autoLabels = autoLabelIds || [];
        this.notify();
    },

    // ---- Blocked Senders ----

    blockSender(email) {
        if (!this.blockedSenders.find(b => b.email === email)) {
            this.blockedSenders.push({ email: email, blockedAt: new Date().toISOString() });
            this.notify();
        }
    },

    unblockSender(email) {
        this.blockedSenders = this.blockedSenders.filter(b => b.email !== email);
        this.notify();
    },

    // ---- Unsubscribe ----

    unsubscribeAndArchive(emailId) {
        const email = this.getEmailById(emailId);
        if (email) {
            // Block the sender
            this.blockSender(email.from.email);
            // Archive all emails from this sender
            const senderEmail = email.from.email;
            for (const e of this.emails) {
                if (e.from.email === senderEmail && e.folder === 'inbox') {
                    e.folder = 'done';
                }
            }
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    unsubscribeAndTrash(emailId) {
        const email = this.getEmailById(emailId);
        if (email) {
            this.blockSender(email.from.email);
            const senderEmail = email.from.email;
            for (const e of this.emails) {
                if (e.from.email === senderEmail) {
                    e.folder = 'trash';
                }
            }
            this._recalculateFolderCounts();
            this.notify();
        }
    },

    // ---- Get Me To Zero ----

    getMeToZero(options = {}) {
        // Archive all inbox emails, optionally preserving unread/starred
        const inbox = this.getEmailsForFolder('inbox');
        for (const email of inbox) {
            if (options.preserveUnread && !email.isRead) continue;
            if (options.preserveStarred && email.isStarred) continue;
            email.folder = 'done';
            email.isRead = true;
        }
        this._recalculateFolderCounts();
        this.notify();
    }
};

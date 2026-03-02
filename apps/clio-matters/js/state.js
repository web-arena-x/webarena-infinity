/* state.js — Centralized state management for Clio Matters */
/* eslint-disable */

const AppState = {
    // Persistent data (synced to server + localStorage)
    currentUser: null,
    users: [],
    groups: [],
    contacts: [],
    practiceAreas: [],
    customFieldDefinitions: [],
    matterTemplates: [],
    numberingScheme: {},
    matters: [],
    damages: [],
    medicalProviders: [],
    medicalRecords: [],
    medicalBills: [],
    settlements: {},
    timeEntries: [],
    expenses: [],
    activityLog: [],
    notificationSettings: {},
    firmSettings: {},
    deletedMatters: [],
    expenseCategories: [],
    currencies: [],
    relationshipTypes: [],

    // ID counters
    _nextMatterId: 121,
    _nextContactId: 61,
    _nextDamageId: 31,
    _nextMedicalProviderId: 9,
    _nextMedicalRecordId: 16,
    _nextMedicalBillId: 16,
    _nextTimeEntryId: 201,
    _nextExpenseId: 81,
    _nextLogId: 151,
    _nextFolderId: 500,
    _seedVersion: null,

    // UI-only state (not persisted)
    currentView: 'matters-list',
    currentMatterId: null,
    currentSubTab: 'overview',
    searchQuery: '',
    statusFilter: 'all',
    filters: {},
    selectedMatterIds: [],
    currentPage: 1,
    pageSize: 25,
    sortField: 'number',
    sortDirection: 'asc',
    stagesSelectedPracticeAreaId: null,
    settingsTab: 'practice-areas',
    modalData: null,

    // Listeners
    _listeners: [],

    // ========================================================================
    // Lifecycle
    // ========================================================================

    init() {
        const stored = localStorage.getItem('clioMattersState');
        if (stored) {
            try {
                const parsed = JSON.parse(stored);
                if (parsed._seedVersion === SEED_DATA_VERSION) {
                    this._loadPersistedData(parsed);
                    this._pushStateToServer();
                    this._setupSSE();
                    return;
                }
            } catch (e) { /* fall through to seed */ }
        }
        this._loadSeedData();
        this._pushStateToServer();
        this._setupSSE();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.users = JSON.parse(JSON.stringify(USERS));
        this.groups = JSON.parse(JSON.stringify(GROUPS));
        this.contacts = JSON.parse(JSON.stringify(CONTACTS));
        this.practiceAreas = JSON.parse(JSON.stringify(PRACTICE_AREAS));
        this.customFieldDefinitions = JSON.parse(JSON.stringify(CUSTOM_FIELD_DEFINITIONS));
        this.matterTemplates = JSON.parse(JSON.stringify(MATTER_TEMPLATES));
        this.numberingScheme = JSON.parse(JSON.stringify(NUMBERING_SCHEME));
        this.matters = JSON.parse(JSON.stringify(MATTERS));
        this.damages = JSON.parse(JSON.stringify(DAMAGES));
        this.medicalProviders = JSON.parse(JSON.stringify(MEDICAL_PROVIDERS));
        this.medicalRecords = JSON.parse(JSON.stringify(MEDICAL_RECORDS));
        this.medicalBills = JSON.parse(JSON.stringify(MEDICAL_BILLS));
        this.settlements = JSON.parse(JSON.stringify(SETTLEMENTS));
        this.timeEntries = JSON.parse(JSON.stringify(TIME_ENTRIES));
        this.expenses = JSON.parse(JSON.stringify(EXPENSES));
        this.activityLog = JSON.parse(JSON.stringify(ACTIVITY_LOG));
        this.notificationSettings = JSON.parse(JSON.stringify(NOTIFICATION_SETTINGS));
        this.firmSettings = JSON.parse(JSON.stringify(FIRM_SETTINGS));
        this.deletedMatters = JSON.parse(JSON.stringify(DELETED_MATTERS));
        this.expenseCategories = JSON.parse(JSON.stringify(EXPENSE_CATEGORIES));
        this.currencies = JSON.parse(JSON.stringify(CURRENCIES));
        this.relationshipTypes = JSON.parse(JSON.stringify(RELATIONSHIP_TYPES));
        this._seedVersion = SEED_DATA_VERSION;

        // Helper: extract numeric suffix from string IDs like 'matter_120', 'dmg_38', etc.
        function _maxIdNum(items) {
            return Math.max(...items.map(item => {
                const parts = String(item.id).split('_');
                return parseInt(parts[parts.length - 1], 10);
            }).filter(n => !isNaN(n)));
        }

        // Recalculate next IDs from data
        if (this.matters.length > 0) {
            this._nextMatterId = _maxIdNum(this.matters) + 1;
        }
        if (this.contacts.length > 0) {
            this._nextContactId = _maxIdNum(this.contacts) + 1;
        }
        if (this.damages.length > 0) {
            this._nextDamageId = _maxIdNum(this.damages) + 1;
        }
        if (this.medicalProviders.length > 0) {
            this._nextMedicalProviderId = _maxIdNum(this.medicalProviders) + 1;
        }
        if (this.medicalRecords.length > 0) {
            this._nextMedicalRecordId = _maxIdNum(this.medicalRecords) + 1;
        }
        if (this.medicalBills.length > 0) {
            this._nextMedicalBillId = _maxIdNum(this.medicalBills) + 1;
        }
        if (this.timeEntries.length > 0) {
            this._nextTimeEntryId = _maxIdNum(this.timeEntries) + 1;
        }
        if (this.expenses.length > 0) {
            this._nextExpenseId = _maxIdNum(this.expenses) + 1;
        }
        if (this.activityLog.length > 0) {
            this._nextLogId = _maxIdNum(this.activityLog) + 1;
        }
    },

    _loadPersistedData(parsed) {
        this.currentUser = parsed.currentUser || JSON.parse(JSON.stringify(CURRENT_USER));
        this.users = parsed.users || [];
        this.groups = parsed.groups || [];
        this.contacts = parsed.contacts || [];
        this.practiceAreas = parsed.practiceAreas || [];
        this.customFieldDefinitions = parsed.customFieldDefinitions || [];
        this.matterTemplates = parsed.matterTemplates || [];
        this.numberingScheme = parsed.numberingScheme || {};
        this.matters = parsed.matters || [];
        this.damages = parsed.damages || [];
        this.medicalProviders = parsed.medicalProviders || [];
        this.medicalRecords = parsed.medicalRecords || [];
        this.medicalBills = parsed.medicalBills || [];
        this.settlements = parsed.settlements || {};
        this.timeEntries = parsed.timeEntries || [];
        this.expenses = parsed.expenses || [];
        this.activityLog = parsed.activityLog || [];
        this.notificationSettings = parsed.notificationSettings || {};
        this.firmSettings = parsed.firmSettings || {};
        this.deletedMatters = parsed.deletedMatters || [];
        this.expenseCategories = parsed.expenseCategories || [];
        this.currencies = parsed.currencies || [];
        this.relationshipTypes = parsed.relationshipTypes || [];
        this._seedVersion = parsed._seedVersion;
        this._nextMatterId = parsed._nextMatterId || 121;
        this._nextContactId = parsed._nextContactId || 61;
        this._nextDamageId = parsed._nextDamageId || 31;
        this._nextMedicalProviderId = parsed._nextMedicalProviderId || 9;
        this._nextMedicalRecordId = parsed._nextMedicalRecordId || 16;
        this._nextMedicalBillId = parsed._nextMedicalBillId || 16;
        this._nextTimeEntryId = parsed._nextTimeEntryId || 201;
        this._nextExpenseId = parsed._nextExpenseId || 81;
        this._nextLogId = parsed._nextLogId || 151;
        this._nextFolderId = parsed._nextFolderId || 500;
    },

    resetToSeedData() {
        localStorage.removeItem('clioMattersState');
        this._loadSeedData();
        // Reset UI state
        this.currentView = 'matters-list';
        this.currentMatterId = null;
        this.currentSubTab = 'overview';
        this.searchQuery = '';
        this.statusFilter = 'all';
        this.filters = {};
        this.selectedMatterIds = [];
        this.currentPage = 1;
        this.sortField = 'number';
        this.sortDirection = 'asc';
        this.stagesSelectedPracticeAreaId = null;
        this.settingsTab = 'practice-areas';
        this.modalData = null;
        this.notify();
    },

    _setupSSE() {
        const evtSource = new EventSource('/api/events');
        evtSource.addEventListener('reset', () => {
            this.resetToSeedData();
        });
    },

    subscribe(fn) {
        this._listeners.push(fn);
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        this._listeners.forEach(fn => fn());
    },

    // ========================================================================
    // Serialization
    // ========================================================================

    getSerializableState() {
        return {
            currentUser: this.currentUser,
            users: this.users,
            groups: this.groups,
            contacts: this.contacts,
            practiceAreas: this.practiceAreas,
            customFieldDefinitions: this.customFieldDefinitions,
            matterTemplates: this.matterTemplates,
            numberingScheme: this.numberingScheme,
            matters: this.matters,
            damages: this.damages,
            medicalProviders: this.medicalProviders,
            medicalRecords: this.medicalRecords,
            medicalBills: this.medicalBills,
            settlements: this.settlements,
            timeEntries: this.timeEntries,
            expenses: this.expenses,
            activityLog: this.activityLog,
            notificationSettings: this.notificationSettings,
            firmSettings: this.firmSettings,
            deletedMatters: this.deletedMatters,
            expenseCategories: this.expenseCategories,
            currencies: this.currencies,
            relationshipTypes: this.relationshipTypes,
            _seedVersion: this._seedVersion,
            _nextMatterId: this._nextMatterId,
            _nextContactId: this._nextContactId,
            _nextDamageId: this._nextDamageId,
            _nextMedicalProviderId: this._nextMedicalProviderId,
            _nextMedicalRecordId: this._nextMedicalRecordId,
            _nextMedicalBillId: this._nextMedicalBillId,
            _nextTimeEntryId: this._nextTimeEntryId,
            _nextExpenseId: this._nextExpenseId,
            _nextLogId: this._nextLogId,
            _nextFolderId: this._nextFolderId
        };
    },

    _persist() {
        localStorage.setItem('clioMattersState', JSON.stringify(this.getSerializableState()));
    },

    _pushStateToServer() {
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.getSerializableState())
        }).catch(() => {});
    },

    // ========================================================================
    // Helper / Lookup Methods
    // ========================================================================

    getUserById(id) {
        return this.users.find(u => u.id === id);
    },

    getContactById(id) {
        return this.contacts.find(c => c.id === id);
    },

    getPracticeAreaById(id) {
        return this.practiceAreas.find(pa => pa.id === id);
    },

    getTemplateById(id) {
        return this.matterTemplates.find(t => t.id === id);
    },

    getMatterById(id) {
        return this.matters.find(m => m.id === id);
    },

    // ========================================================================
    // Matter CRUD
    // ========================================================================

    createMatter(data) {
        const id = 'matter_' + this._nextMatterId++;
        const now = new Date().toISOString();
        const number = this.getNextMatterNumber();

        const matter = {
            id: id,
            number: number,
            description: data.description || '',
            status: data.status || 'open',
            clientId: data.clientId || null,
            practiceAreaId: data.practiceAreaId || null,
            stageId: data.stageId || null,
            responsibleAttorneyId: data.responsibleAttorneyId || this.currentUser.id,
            originatingAttorneyId: data.originatingAttorneyId || null,
            billingMethod: data.billingMethod || 'hourly',
            openDate: data.openDate || now.split('T')[0],
            closedDate: null,
            pendingDate: null,
            statuteOfLimitations: data.statuteOfLimitations || null,
            customFields: data.customFields || {},
            relationships: data.relationships || [],
            notes: data.notes || '',
            tags: data.tags || [],
            createdDate: now,
            updatedDate: now
        };

        this.matters.push(matter);
        this.addActivityLog(id, 'created', 'matter', id, { description: matter.description });
        this.notify();
        return matter;
    },

    updateMatter(id, data) {
        const matter = this.getMatterById(id);
        if (!matter) return;
        const changes = {};
        for (const key of Object.keys(data)) {
            if (JSON.stringify(matter[key]) !== JSON.stringify(data[key])) {
                changes[key] = { from: matter[key], to: data[key] };
            }
        }
        Object.assign(matter, data, { updatedDate: new Date().toISOString() });
        this.addActivityLog(id, 'updated', 'matter', id, changes);
        this.notify();
    },

    deleteMatter(id) {
        const idx = this.matters.findIndex(m => m.id === id);
        if (idx === -1) return;
        const matter = this.matters.splice(idx, 1)[0];
        matter.deletedDate = new Date().toISOString();
        this.deletedMatters.push(matter);
        this.selectedMatterIds = this.selectedMatterIds.filter(mid => mid !== id);
        this.addActivityLog(id, 'deleted', 'matter', id, { description: matter.description });
        this.notify();
    },

    recoverMatter(id) {
        const idx = this.deletedMatters.findIndex(m => m.id === id);
        if (idx === -1) return;
        const matter = this.deletedMatters.splice(idx, 1)[0];
        delete matter.deletedDate;
        matter.status = 'open';
        matter.updatedDate = new Date().toISOString();
        this.matters.push(matter);
        this.addActivityLog(id, 'recovered', 'matter', id, { description: matter.description });
        this.notify();
    },

    duplicateMatter(id) {
        const source = this.getMatterById(id);
        if (!source) return null;
        const newData = {
            description: source.description + ' (Copy)',
            clientId: source.clientId,
            practiceAreaId: source.practiceAreaId,
            stageId: source.stageId,
            responsibleAttorneyId: source.responsibleAttorneyId,
            originatingAttorneyId: source.originatingAttorneyId,
            billingMethod: source.billingMethod,
            statuteOfLimitations: source.statuteOfLimitations,
            customFields: JSON.parse(JSON.stringify(source.customFields || {})),
            tags: [...(source.tags || [])],
            notes: source.notes || ''
        };
        return this.createMatter(newData);
    },

    closeMatter(id) {
        const matter = this.getMatterById(id);
        if (!matter) return;
        matter.status = 'closed';
        matter.closedDate = new Date().toISOString().split('T')[0];
        matter.updatedDate = new Date().toISOString();
        this.addActivityLog(id, 'closed', 'matter', id, {});
        this.notify();
    },

    reopenMatter(id) {
        const matter = this.getMatterById(id);
        if (!matter) return;
        matter.status = 'open';
        matter.closedDate = null;
        matter.updatedDate = new Date().toISOString();
        this.addActivityLog(id, 'reopened', 'matter', id, {});
        this.notify();
    },

    bulkUpdateStatus(ids, status) {
        ids.forEach(id => {
            const matter = this.getMatterById(id);
            if (!matter) return;
            matter.status = status;
            matter.updatedDate = new Date().toISOString();
            if (status === 'closed') {
                matter.closedDate = new Date().toISOString().split('T')[0];
            } else if (status === 'open') {
                matter.closedDate = null;
            }
            this.addActivityLog(id, 'status_changed', 'matter', id, { status: status });
        });
        this.selectedMatterIds = [];
        this.notify();
    },

    bulkDeleteMatters(ids) {
        ids.forEach(id => {
            const idx = this.matters.findIndex(m => m.id === id);
            if (idx === -1) return;
            const matter = this.matters.splice(idx, 1)[0];
            matter.deletedDate = new Date().toISOString();
            this.deletedMatters.push(matter);
            this.addActivityLog(id, 'deleted', 'matter', id, { description: matter.description });
        });
        this.selectedMatterIds = [];
        this.notify();
    },

    // ========================================================================
    // Matter Queries
    // ========================================================================

    getFilteredMatters() {
        let result = [...this.matters];

        // Status filter
        if (this.statusFilter && this.statusFilter !== 'all') {
            result = result.filter(m => m.status === this.statusFilter);
        }

        // Search query (matches number, description, client name)
        if (this.searchQuery) {
            const q = this.searchQuery.toLowerCase();
            result = result.filter(m => {
                if (String(m.number).toLowerCase().includes(q)) return true;
                if (m.description && m.description.toLowerCase().includes(q)) return true;
                if (m.clientId) {
                    const client = this.getContactById(m.clientId);
                    if (client) {
                        const clientName = (client.name || ((client.firstName || '') + ' ' + (client.lastName || '')).trim()).toLowerCase();
                        if (clientName.includes(q)) return true;
                    }
                }
                return false;
            });
        }

        // Additional filters
        if (this.filters.practiceAreaId) {
            result = result.filter(m => m.practiceAreaId === this.filters.practiceAreaId);
        }
        if (this.filters.responsibleAttorneyId) {
            result = result.filter(m => m.responsibleAttorneyId === this.filters.responsibleAttorneyId);
        }
        if (this.filters.originatingAttorneyId) {
            result = result.filter(m => m.originatingAttorneyId === this.filters.originatingAttorneyId);
        }
        if (this.filters.billingMethod) {
            result = result.filter(m => m.billingMethod === this.filters.billingMethod);
        }

        // Sort
        const field = this.sortField;
        const dir = this.sortDirection;
        result.sort((a, b) => {
            let va = a[field];
            let vb = b[field];
            if (va == null) va = '';
            if (vb == null) vb = '';
            if (typeof va === 'string') { va = va.toLowerCase(); vb = (vb || '').toLowerCase(); }
            if (typeof va === 'number' && typeof vb === 'number') {
                return dir === 'asc' ? va - vb : vb - va;
            }
            if (va < vb) return dir === 'asc' ? -1 : 1;
            if (va > vb) return dir === 'asc' ? 1 : -1;
            return 0;
        });

        // Pagination
        const totalCount = result.length;
        const totalPages = Math.max(1, Math.ceil(totalCount / this.pageSize));
        const start = (this.currentPage - 1) * this.pageSize;
        const paged = result.slice(start, start + this.pageSize);

        return {
            matters: paged,
            totalCount: totalCount,
            totalPages: totalPages
        };
    },

    getMattersByStatus(status) {
        return this.matters.filter(m => m.status === status);
    },

    getMattersForPracticeArea(paId) {
        return this.matters.filter(m => m.practiceAreaId === paId);
    },

    getMattersForStage(stageId) {
        return this.matters.filter(m => m.stageId === stageId);
    },

    getMatterClient(matterId) {
        const matter = this.getMatterById(matterId);
        if (!matter || !matter.clientId) return null;
        return this.getContactById(matter.clientId);
    },

    getMatterResponsibleAttorney(matterId) {
        const matter = this.getMatterById(matterId);
        if (!matter || !matter.responsibleAttorneyId) return null;
        return this.getUserById(matter.responsibleAttorneyId);
    },

    getMatterFinancials(matterId) {
        const entries = this.getTimeEntriesForMatter(matterId);
        const matterExpenses = this.getExpensesForMatter(matterId);

        let workInProgress = 0;
        let outstandingBalance = 0;
        let totalTime = 0;

        entries.forEach(entry => {
            const hours = entry.hours || 0;
            const rate = entry.rate || 0;
            totalTime += hours;
            if (entry.status === 'approved' || entry.status === 'unbilled') {
                workInProgress += hours * rate;
            }
            if (entry.status === 'billed') {
                outstandingBalance += hours * rate;
            }
        });

        let totalExpenses = 0;
        matterExpenses.forEach(exp => {
            totalExpenses += exp.amount || 0;
        });

        return {
            workInProgress: workInProgress,
            outstandingBalance: outstandingBalance,
            totalTime: totalTime,
            totalExpenses: totalExpenses
        };
    },

    // ========================================================================
    // Contact CRUD
    // ========================================================================

    createContact(data) {
        const id = 'contact_' + this._nextContactId++;
        const now = new Date().toISOString();
        const contact = {
            id: id,
            type: data.type || 'person',
            firstName: data.firstName || '',
            lastName: data.lastName || '',
            name: data.name || ((data.firstName || '') + ' ' + (data.lastName || '')).trim(),
            company: data.company || '',
            email: data.email || '',
            phone: data.phone || '',
            address: data.address || '',
            city: data.city || '',
            state: data.state || '',
            zip: data.zip || '',
            notes: data.notes || '',
            createdDate: now,
            updatedDate: now
        };
        this.contacts.push(contact);
        this.notify();
        return contact;
    },

    updateContact(id, data) {
        const contact = this.getContactById(id);
        if (!contact) return;
        Object.assign(contact, data, { updatedDate: new Date().toISOString() });
        // Keep name in sync
        if (data.firstName !== undefined || data.lastName !== undefined) {
            contact.name = ((contact.firstName || '') + ' ' + (contact.lastName || '')).trim();
        }
        this.notify();
    },

    // ========================================================================
    // Practice Area CRUD
    // ========================================================================

    createPracticeArea(data) {
        const maxNum = this.practiceAreas.length > 0
            ? Math.max(...this.practiceAreas.map(pa => parseInt(String(pa.id).split('_').pop(), 10)).filter(n => !isNaN(n)))
            : 0;
        const id = 'pa_' + (maxNum + 1);
        const pa = {
            id: id,
            name: data.name,
            description: data.description || '',
            stages: data.stages || [],
            color: data.color || '#6366f1',
            createdDate: new Date().toISOString()
        };
        this.practiceAreas.push(pa);
        this.notify();
        return pa;
    },

    updatePracticeArea(id, data) {
        const pa = this.getPracticeAreaById(id);
        if (!pa) return;
        Object.assign(pa, data);
        this.notify();
    },

    deletePracticeArea(id) {
        const mattersUsing = this.getMattersForPracticeArea(id);
        if (mattersUsing.length > 0) return false;
        this.practiceAreas = this.practiceAreas.filter(pa => pa.id !== id);
        this.notify();
        return true;
    },

    createStage(practiceAreaId, name) {
        const pa = this.getPracticeAreaById(practiceAreaId);
        if (!pa) return null;
        if (!pa.stages) pa.stages = [];
        if (pa.stages.length >= 15) return null;
        const maxStageNum = pa.stages.length > 0
            ? Math.max(...pa.stages.map(s => parseInt(String(s.id).split('_').pop(), 10)).filter(n => !isNaN(n)))
            : 0;
        const paNum = String(practiceAreaId).split('_').pop();
        const stage = {
            id: 'stage_' + paNum + '_' + (maxStageNum + 1),
            name: name,
            order: pa.stages.length
        };
        pa.stages.push(stage);
        this.notify();
        return stage;
    },

    updateStage(practiceAreaId, stageId, name) {
        const pa = this.getPracticeAreaById(practiceAreaId);
        if (!pa || !pa.stages) return;
        const stage = pa.stages.find(s => s.id === stageId);
        if (!stage) return;
        stage.name = name;
        this.notify();
    },

    deleteStage(practiceAreaId, stageId) {
        const pa = this.getPracticeAreaById(practiceAreaId);
        if (!pa || !pa.stages) return;
        pa.stages = pa.stages.filter(s => s.id !== stageId);
        // Reorder remaining stages
        pa.stages.forEach((s, i) => s.order = i);
        // Clear stageId from matters that used this stage
        this.matters.forEach(m => {
            if (m.practiceAreaId === practiceAreaId && m.stageId === stageId) {
                m.stageId = null;
            }
        });
        this.notify();
    },

    reorderStages(practiceAreaId, stageIds) {
        const pa = this.getPracticeAreaById(practiceAreaId);
        if (!pa || !pa.stages) return;
        const reordered = [];
        stageIds.forEach((sid, idx) => {
            const stage = pa.stages.find(s => s.id === sid);
            if (stage) {
                stage.order = idx;
                reordered.push(stage);
            }
        });
        pa.stages = reordered;
        this.notify();
    },

    moveMatterToStage(matterId, stageId) {
        const matter = this.getMatterById(matterId);
        if (!matter) return;
        matter.stageId = stageId;
        matter.updatedDate = new Date().toISOString();
        this.addActivityLog(matterId, 'stage_changed', 'matter', matterId, { stageId: stageId });
        this.notify();
    },

    // ========================================================================
    // Template CRUD
    // ========================================================================

    createTemplate(data) {
        const maxNum = this.matterTemplates.length > 0
            ? Math.max(...this.matterTemplates.map(t => parseInt(String(t.id).split('_').pop(), 10)).filter(n => !isNaN(n)))
            : 0;
        const id = 'template_' + (maxNum + 1);
        const template = {
            id: id,
            name: data.name,
            description: data.description || '',
            practiceAreaId: data.practiceAreaId || null,
            billingMethod: data.billingMethod || 'hourly',
            taskLists: data.taskLists || [],
            customFields: data.customFields || {},
            isDefault: false,
            createdDate: new Date().toISOString()
        };
        this.matterTemplates.push(template);
        this.notify();
        return template;
    },

    updateTemplate(id, data) {
        const template = this.getTemplateById(id);
        if (!template) return;
        Object.assign(template, data);
        this.notify();
    },

    deleteTemplate(id) {
        this.matterTemplates = this.matterTemplates.filter(t => t.id !== id);
        this.notify();
    },

    setDefaultTemplate(id) {
        this.matterTemplates.forEach(t => {
            t.isDefault = (t.id === id);
        });
        this.notify();
    },

    // ========================================================================
    // Numbering Scheme
    // ========================================================================

    updateNumberingScheme(data) {
        Object.assign(this.numberingScheme, data);
        this.notify();
    },

    formatMatterNumber(matter) {
        const scheme = this.numberingScheme;
        const prefix = scheme.prefix || '';
        const padLength = scheme.padLength || 5;
        const separator = scheme.separator || '-';
        const padded = String(matter.number).padStart(padLength, '0');

        let formatted = prefix ? prefix + separator + padded : padded;

        // Append client name if configured
        if (scheme.appendClientName && matter.clientId) {
            const client = this.getContactById(matter.clientId);
            if (client) {
                const clientName = client.name || ((client.firstName || '') + ' ' + (client.lastName || '')).trim();
                if (clientName) {
                    formatted += separator + clientName;
                }
            }
        }

        return formatted;
    },

    getNextMatterNumber() {
        const allNumbers = [
            ...this.matters.map(m => m.number),
            ...this.deletedMatters.map(m => m.number)
        ].map(n => parseInt(n, 10)).filter(n => !isNaN(n));
        if (allNumbers.length === 0) return '00001';
        const next = Math.max(...allNumbers) + 1;
        return String(next).padStart(5, '0');
    },

    // ========================================================================
    // Damages CRUD
    // ========================================================================

    createDamage(data) {
        const id = 'dmg_' + this._nextDamageId++;
        const now = new Date().toISOString();
        const damage = {
            id: id,
            matterId: data.matterId,
            type: data.type || 'general',
            description: data.description || '',
            amount: data.amount || 0,
            date: data.date || null,
            notes: data.notes || '',
            createdDate: now,
            updatedDate: now
        };
        this.damages.push(damage);
        this.addActivityLog(data.matterId, 'created', 'damage', id, { type: damage.type, amount: damage.amount });
        this.notify();
        return damage;
    },

    updateDamage(id, data) {
        const damage = this.damages.find(d => d.id === id);
        if (!damage) return;
        Object.assign(damage, data, { updatedDate: new Date().toISOString() });
        this.addActivityLog(damage.matterId, 'updated', 'damage', id, data);
        this.notify();
    },

    deleteDamage(id) {
        const damage = this.damages.find(d => d.id === id);
        if (!damage) return;
        const matterId = damage.matterId;
        this.damages = this.damages.filter(d => d.id !== id);
        this.addActivityLog(matterId, 'deleted', 'damage', id, {});
        this.notify();
    },

    getDamagesForMatter(matterId) {
        return this.damages.filter(d => d.matterId === matterId);
    },

    getDamageSummary(matterId) {
        const damages = this.getDamagesForMatter(matterId);
        const summary = {};
        let total = 0;
        damages.forEach(d => {
            const type = d.type || 'general';
            if (!summary[type]) summary[type] = 0;
            summary[type] += d.amount || 0;
            total += d.amount || 0;
        });
        summary._total = total;
        return summary;
    },

    // ========================================================================
    // Medical Records CRUD
    // ========================================================================

    createMedicalProvider(data) {
        const id = 'mp_' + this._nextMedicalProviderId++;
        const now = new Date().toISOString();
        const provider = {
            id: id,
            matterId: data.matterId,
            name: data.name || '',
            specialty: data.specialty || '',
            phone: data.phone || '',
            fax: data.fax || '',
            address: data.address || '',
            notes: data.notes || '',
            createdDate: now,
            updatedDate: now
        };
        this.medicalProviders.push(provider);
        this.addActivityLog(data.matterId, 'created', 'medical_provider', id, { name: provider.name });
        this.notify();
        return provider;
    },

    updateMedicalProvider(id, data) {
        const provider = this.medicalProviders.find(p => p.id === id);
        if (!provider) return;
        Object.assign(provider, data, { updatedDate: new Date().toISOString() });
        this.notify();
    },

    deleteMedicalProvider(id) {
        const provider = this.medicalProviders.find(p => p.id === id);
        if (!provider) return;
        const matterId = provider.matterId;
        this.medicalProviders = this.medicalProviders.filter(p => p.id !== id);
        // Delete related records and bills
        this.medicalRecords = this.medicalRecords.filter(r => r.providerId !== id);
        this.medicalBills = this.medicalBills.filter(b => b.providerId !== id);
        this.addActivityLog(matterId, 'deleted', 'medical_provider', id, { name: provider.name });
        this.notify();
    },

    getMedicalProvidersForMatter(matterId) {
        return this.medicalProviders.filter(p => p.matterId === matterId);
    },

    createMedicalRecord(data) {
        const id = 'mr_' + this._nextMedicalRecordId++;
        const now = new Date().toISOString();
        const record = {
            id: id,
            providerId: data.providerId,
            matterId: data.matterId,
            type: data.type || 'office_visit',
            date: data.date || null,
            description: data.description || '',
            status: data.status || 'requested',
            requestedDate: data.requestedDate || null,
            receivedDate: data.receivedDate || null,
            notes: data.notes || '',
            createdDate: now,
            updatedDate: now
        };
        this.medicalRecords.push(record);
        this.notify();
        return record;
    },

    updateMedicalRecord(id, data) {
        const record = this.medicalRecords.find(r => r.id === id);
        if (!record) return;
        Object.assign(record, data, { updatedDate: new Date().toISOString() });
        this.notify();
    },

    deleteMedicalRecord(id) {
        this.medicalRecords = this.medicalRecords.filter(r => r.id !== id);
        this.notify();
    },

    createMedicalBill(data) {
        const id = 'mb_' + this._nextMedicalBillId++;
        const now = new Date().toISOString();
        const bill = {
            id: id,
            providerId: data.providerId,
            matterId: data.matterId,
            date: data.date || null,
            amount: data.amount || 0,
            adjustments: data.adjustments || 0,
            insurancePaid: data.insurancePaid || 0,
            balance: data.balance || 0,
            status: data.status || 'outstanding',
            description: data.description || '',
            notes: data.notes || '',
            createdDate: now,
            updatedDate: now
        };
        this.medicalBills.push(bill);
        this.notify();
        return bill;
    },

    updateMedicalBill(id, data) {
        const bill = this.medicalBills.find(b => b.id === id);
        if (!bill) return;
        Object.assign(bill, data, { updatedDate: new Date().toISOString() });
        this.notify();
    },

    deleteMedicalBill(id) {
        this.medicalBills = this.medicalBills.filter(b => b.id !== id);
        this.notify();
    },

    // ========================================================================
    // Settlement CRUD
    // ========================================================================

    getSettlement(matterId) {
        if (!this.settlements[matterId]) {
            this.settlements[matterId] = {
                matterId: matterId,
                grossSettlement: 0,
                deductionOrder: 'fees_first',
                recoveries: [],
                legalFees: [],
                nonMedicalLiens: [],
                outstandingBalances: [],
                notes: '',
                _nextRecoveryId: 1,
                _nextLegalFeeId: 1,
                _nextLienId: 1,
                _nextBalanceId: 1
            };
        }
        return this.settlements[matterId];
    },

    addRecovery(matterId, data) {
        const settlement = this.getSettlement(matterId);
        const id = settlement._nextRecoveryId++;
        const recovery = {
            id: id,
            type: data.type || 'settlement',
            amount: data.amount || 0,
            date: data.date || null,
            source: data.source || '',
            notes: data.notes || ''
        };
        settlement.recoveries.push(recovery);
        this.notify();
        return recovery;
    },

    updateRecovery(matterId, id, data) {
        const settlement = this.getSettlement(matterId);
        const recovery = settlement.recoveries.find(r => r.id === id);
        if (!recovery) return;
        Object.assign(recovery, data);
        this.notify();
    },

    deleteRecovery(matterId, id) {
        const settlement = this.getSettlement(matterId);
        settlement.recoveries = settlement.recoveries.filter(r => r.id !== id);
        this.notify();
    },

    addLegalFee(matterId, data) {
        const settlement = this.getSettlement(matterId);
        const id = settlement._nextLegalFeeId++;
        const fee = {
            id: id,
            type: data.type || 'contingency',
            description: data.description || '',
            percentage: data.percentage || 0,
            flatAmount: data.flatAmount || 0,
            notes: data.notes || ''
        };
        settlement.legalFees.push(fee);
        this.notify();
        return fee;
    },

    updateLegalFee(matterId, id, data) {
        const settlement = this.getSettlement(matterId);
        const fee = settlement.legalFees.find(f => f.id === id);
        if (!fee) return;
        Object.assign(fee, data);
        this.notify();
    },

    deleteLegalFee(matterId, id) {
        const settlement = this.getSettlement(matterId);
        settlement.legalFees = settlement.legalFees.filter(f => f.id !== id);
        this.notify();
    },

    addNonMedicalLien(matterId, data) {
        const settlement = this.getSettlement(matterId);
        const id = settlement._nextLienId++;
        const lien = {
            id: id,
            lienholder: data.lienholder || '',
            type: data.type || 'other',
            amount: data.amount || 0,
            negotiatedAmount: data.negotiatedAmount || null,
            status: data.status || 'pending',
            notes: data.notes || ''
        };
        settlement.nonMedicalLiens.push(lien);
        this.notify();
        return lien;
    },

    updateNonMedicalLien(matterId, id, data) {
        const settlement = this.getSettlement(matterId);
        const lien = settlement.nonMedicalLiens.find(l => l.id === id);
        if (!lien) return;
        Object.assign(lien, data);
        this.notify();
    },

    deleteNonMedicalLien(matterId, id) {
        const settlement = this.getSettlement(matterId);
        settlement.nonMedicalLiens = settlement.nonMedicalLiens.filter(l => l.id !== id);
        this.notify();
    },

    addOutstandingBalance(matterId, data) {
        const settlement = this.getSettlement(matterId);
        const id = settlement._nextBalanceId++;
        const balance = {
            id: id,
            creditor: data.creditor || '',
            type: data.type || 'medical',
            originalAmount: data.originalAmount || 0,
            negotiatedAmount: data.negotiatedAmount || null,
            status: data.status || 'outstanding',
            notes: data.notes || ''
        };
        settlement.outstandingBalances.push(balance);
        this.notify();
        return balance;
    },

    updateOutstandingBalance(matterId, id, data) {
        const settlement = this.getSettlement(matterId);
        const balance = settlement.outstandingBalances.find(b => b.id === id);
        if (!balance) return;
        Object.assign(balance, data);
        this.notify();
    },

    deleteOutstandingBalance(matterId, id) {
        const settlement = this.getSettlement(matterId);
        settlement.outstandingBalances = settlement.outstandingBalances.filter(b => b.id !== id);
        this.notify();
    },

    getSettlementSummary(matterId) {
        const settlement = this.getSettlement(matterId);

        // Total gross recovery
        const grossRecovery = settlement.recoveries.reduce((sum, r) => sum + (r.amount || 0), 0);

        // Legal fees calculation
        let totalLegalFees = 0;
        settlement.legalFees.forEach(fee => {
            if (fee.percentage > 0) {
                totalLegalFees += grossRecovery * (fee.percentage / 100);
            }
            if (fee.flatAmount > 0) {
                totalLegalFees += fee.flatAmount;
            }
        });

        // Medical bill liens (from medical bills with outstanding balance)
        const matterBills = this.medicalBills.filter(b => b.matterId === matterId);
        const totalMedicalBillLiens = matterBills.reduce((sum, b) => sum + (b.balance || 0), 0);

        // Non-medical liens
        const totalNonMedicalLiens = settlement.nonMedicalLiens.reduce((sum, l) => {
            return sum + (l.negotiatedAmount != null ? l.negotiatedAmount : (l.amount || 0));
        }, 0);

        // Outstanding balances
        const totalOutstandingBalances = settlement.outstandingBalances.reduce((sum, b) => {
            return sum + (b.negotiatedAmount != null ? b.negotiatedAmount : (b.originalAmount || 0));
        }, 0);

        // Total case expenses (from expenses table)
        const matterExpenses = this.getExpensesForMatter(matterId);
        const totalCaseExpenses = matterExpenses.reduce((sum, e) => sum + (e.amount || 0), 0);

        // Deduction order determines what gets subtracted first
        let netClientCompensation = grossRecovery;
        const totalLiens = totalMedicalBillLiens + totalNonMedicalLiens + totalOutstandingBalances;

        if (settlement.deductionOrder === 'fees_first') {
            // Deduct fees first, then expenses, then liens
            netClientCompensation -= totalLegalFees;
            netClientCompensation -= totalCaseExpenses;
            netClientCompensation -= totalLiens;
        } else {
            // Deduct expenses first, then fees (calculated on remainder), then liens
            netClientCompensation -= totalCaseExpenses;
            // Recalculate fees on post-expense amount
            let feesOnRemainder = 0;
            settlement.legalFees.forEach(fee => {
                if (fee.percentage > 0) {
                    feesOnRemainder += netClientCompensation * (fee.percentage / 100);
                }
                if (fee.flatAmount > 0) {
                    feesOnRemainder += fee.flatAmount;
                }
            });
            netClientCompensation -= feesOnRemainder;
            totalLegalFees = feesOnRemainder;
            netClientCompensation -= totalLiens;
        }

        return {
            grossRecovery: grossRecovery,
            totalLegalFees: totalLegalFees,
            totalMedicalBillLiens: totalMedicalBillLiens,
            totalNonMedicalLiens: totalNonMedicalLiens,
            totalOutstandingBalances: totalOutstandingBalances,
            totalCaseExpenses: totalCaseExpenses,
            totalLiens: totalLiens,
            netClientCompensation: netClientCompensation,
            deductionOrder: settlement.deductionOrder
        };
    },

    // ========================================================================
    // Time & Expense
    // ========================================================================

    getTimeEntriesForMatter(matterId) {
        return this.timeEntries.filter(t => t.matterId === matterId);
    },

    getExpensesForMatter(matterId) {
        return this.expenses.filter(e => e.matterId === matterId);
    },

    getExpenseSummaryForMatter(matterId) {
        const matterExpenses = this.getExpensesForMatter(matterId);
        const byCategory = {};
        let total = 0;
        matterExpenses.forEach(exp => {
            const cat = exp.category || 'Uncategorized';
            if (!byCategory[cat]) byCategory[cat] = 0;
            byCategory[cat] += exp.amount || 0;
            total += exp.amount || 0;
        });
        return { byCategory: byCategory, total: total };
    },

    // ========================================================================
    // Activity Log
    // ========================================================================

    addActivityLog(matterId, action, entityType, entityId, details) {
        const id = 'log_' + this._nextLogId++;
        const entry = {
            id: id,
            matterId: matterId,
            userId: this.currentUser ? this.currentUser.id : null,
            action: action,
            entityType: entityType,
            entityId: entityId,
            details: details || {},
            timestamp: new Date().toISOString()
        };
        this.activityLog.push(entry);
        return entry;
    },

    getActivityLogForMatter(matterId) {
        return this.activityLog
            .filter(l => l.matterId === matterId)
            .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
    },

    // ========================================================================
    // Settings
    // ========================================================================

    updateFirmSettings(data) {
        Object.assign(this.firmSettings, data);
        this.notify();
    },

    updateNotificationSettings(data) {
        Object.assign(this.notificationSettings, data);
        this.notify();
    },

    // ========================================================================
    // Filter / Search / Sort / Pagination
    // ========================================================================

    setStatusFilter(status) {
        this.statusFilter = status;
        this.currentPage = 1;
        this.notify();
    },

    setSearchQuery(query) {
        this.searchQuery = query;
        this.currentPage = 1;
        this.notify();
    },

    setFilter(key, value) {
        if (value === null || value === undefined || value === '') {
            delete this.filters[key];
        } else {
            this.filters[key] = value;
        }
        this.currentPage = 1;
        this.notify();
    },

    clearFilters() {
        this.filters = {};
        this.searchQuery = '';
        this.statusFilter = 'all';
        this.currentPage = 1;
        this.notify();
    },

    setSort(field, direction) {
        this.sortField = field;
        this.sortDirection = direction || 'asc';
        this.notify();
    },

    setPage(page) {
        this.currentPage = page;
        this.notify();
    }
};

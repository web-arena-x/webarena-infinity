/* state.js — Centralized state management for GitLab Plan & Track */
/* eslint-disable */

const AppState = {
    // Persistent data
    users: [],
    issues: [],
    labels: [],
    milestones: [],
    iterations: [],
    iterationCadences: [],
    epics: [],
    boards: [],
    todos: [],
    timelogs: [],
    currentUser: null,

    // ID counters
    _nextIssueIid: 100,
    _nextEpicIid: 20,
    _nextLabelId: 50,
    _nextMilestoneId: 20,
    _nextIterationId: 20,
    _nextCadenceId: 10,
    _nextBoardId: 10,
    _nextTodoId: 20,
    _nextTimelogId: 30,
    _seedVersion: null,

    // UI state (not persisted)
    currentView: 'issues',
    currentItemId: null,
    selectedIssueIds: new Set(),
    searchQuery: '',
    filters: { status: 'open', labels: [], assignee: null, milestone: null, iteration: null, epic: null, author: null, search: '' },
    issueSort: { field: 'createdAt', direction: 'desc' },
    currentBoardId: 'board_1',
    todoTab: 'pending',
    settingsOpen: false,
    currentPage: 1,
    pageSize: 20,
    expandedEpicIds: new Set(),

    // Listeners
    _listeners: [],

    init() {
        const stored = localStorage.getItem('gitlabPlanTrackState');
        if (stored) {
            try {
                const parsed = JSON.parse(stored);
                if (parsed._seedVersion === SEED_DATA_VERSION) {
                    this._loadPersistedData(parsed);
                    this._pushStateToServer();
                    return;
                }
            } catch (e) { /* fall through to seed */ }
        }
        this._loadSeedData();
        this._pushStateToServer();
    },

    _loadSeedData() {
        this.users = JSON.parse(JSON.stringify(USERS));
        this.issues = JSON.parse(JSON.stringify(ISSUES));
        this.labels = JSON.parse(JSON.stringify(LABELS));
        this.milestones = JSON.parse(JSON.stringify(MILESTONES));
        this.iterations = JSON.parse(JSON.stringify(ITERATIONS));
        this.iterationCadences = JSON.parse(JSON.stringify(ITERATION_CADENCES));
        this.epics = JSON.parse(JSON.stringify(EPICS));
        this.boards = JSON.parse(JSON.stringify(BOARDS));
        this.todos = JSON.parse(JSON.stringify(TODOS));
        this.timelogs = JSON.parse(JSON.stringify(TIMELOGS));
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this._seedVersion = SEED_DATA_VERSION;

        // Calculate next IDs from data
        this._nextIssueIid = Math.max(...this.issues.map(i => i.iid)) + 1;
        this._nextEpicIid = Math.max(...this.epics.map(e => e.iid)) + 1;
    },

    _loadPersistedData(parsed) {
        this.users = parsed.users || [];
        this.issues = parsed.issues || [];
        this.labels = parsed.labels || [];
        this.milestones = parsed.milestones || [];
        this.iterations = parsed.iterations || [];
        this.iterationCadences = parsed.iterationCadences || [];
        this.epics = parsed.epics || [];
        this.boards = parsed.boards || [];
        this.todos = parsed.todos || [];
        this.timelogs = parsed.timelogs || [];
        this.currentUser = parsed.currentUser || JSON.parse(JSON.stringify(CURRENT_USER));
        this._seedVersion = parsed._seedVersion;
        this._nextIssueIid = parsed._nextIssueIid || 100;
        this._nextEpicIid = parsed._nextEpicIid || 20;
        this._nextLabelId = parsed._nextLabelId || 50;
        this._nextMilestoneId = parsed._nextMilestoneId || 20;
        this._nextIterationId = parsed._nextIterationId || 20;
        this._nextCadenceId = parsed._nextCadenceId || 10;
        this._nextBoardId = parsed._nextBoardId || 10;
        this._nextTodoId = parsed._nextTodoId || 20;
        this._nextTimelogId = parsed._nextTimelogId || 30;
    },

    resetToSeedData() {
        localStorage.removeItem('gitlabPlanTrackState');
        this._loadSeedData();
        this.currentView = 'issues';
        this.currentItemId = null;
        this.selectedIssueIds = new Set();
        this.searchQuery = '';
        this.filters = { status: 'open', labels: [], assignee: null, milestone: null, iteration: null, epic: null, author: null, search: '' };
        this.issueSort = { field: 'createdAt', direction: 'desc' };
        this.currentBoardId = 'board_1';
        this.todoTab = 'pending';
        this.currentPage = 1;
        this.expandedEpicIds = new Set();
        this.notify();
    },

    getSerializableState() {
        return {
            users: this.users,
            issues: this.issues,
            labels: this.labels,
            milestones: this.milestones,
            iterations: this.iterations,
            iterationCadences: this.iterationCadences,
            epics: this.epics,
            boards: this.boards,
            todos: this.todos,
            timelogs: this.timelogs,
            currentUser: this.currentUser,
            _seedVersion: this._seedVersion,
            _nextIssueIid: this._nextIssueIid,
            _nextEpicIid: this._nextEpicIid,
            _nextLabelId: this._nextLabelId,
            _nextMilestoneId: this._nextMilestoneId,
            _nextIterationId: this._nextIterationId,
            _nextCadenceId: this._nextCadenceId,
            _nextBoardId: this._nextBoardId,
            _nextTodoId: this._nextTodoId,
            _nextTimelogId: this._nextTimelogId
        };
    },

    _persist() {
        localStorage.setItem('gitlabPlanTrackState', JSON.stringify(this.getSerializableState()));
    },

    _pushStateToServer() {
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.getSerializableState())
        }).catch(() => {});
    },

    subscribe(fn) {
        this._listeners.push(fn);
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        this._listeners.forEach(fn => fn());
    },

    // ---- Query helpers ----

    getUserById(id) { return this.users.find(u => u.id === id); },
    getIssueById(id) { return this.issues.find(i => i.id === id); },
    getIssueByIid(iid) { return this.issues.find(i => i.iid === iid); },
    getLabelById(id) { return this.labels.find(l => l.id === id); },
    getMilestoneById(id) { return this.milestones.find(m => m.id === id); },
    getIterationById(id) { return this.iterations.find(i => i.id === id); },
    getCadenceById(id) { return this.iterationCadences.find(c => c.id === id); },
    getEpicById(id) { return this.epics.find(e => e.id === id); },
    getBoardById(id) { return this.boards.find(b => b.id === id); },

    getFilteredIssues() {
        let result = this.issues;
        const f = this.filters;
        if (f.status === 'open') result = result.filter(i => i.status === 'open');
        else if (f.status === 'closed') result = result.filter(i => i.status === 'closed');
        if (f.labels && f.labels.length > 0) result = result.filter(i => f.labels.every(l => i.labels.includes(l)));
        if (f.assignee) result = result.filter(i => i.assignees.includes(f.assignee));
        if (f.milestone) result = result.filter(i => i.milestoneId === f.milestone);
        if (f.iteration) result = result.filter(i => i.iterationId === f.iteration);
        if (f.epic) result = result.filter(i => i.epicId === f.epic);
        if (f.author) result = result.filter(i => i.authorId === f.author);
        if (f.search) {
            const q = f.search.toLowerCase();
            result = result.filter(i => i.title.toLowerCase().includes(q) || (i.description && i.description.toLowerCase().includes(q)) || ('#' + i.iid).includes(q));
        }
        // Sort
        const { field, direction } = this.issueSort;
        result = [...result].sort((a, b) => {
            let va = a[field], vb = b[field];
            if (va == null) va = '';
            if (vb == null) vb = '';
            if (typeof va === 'string') { va = va.toLowerCase(); vb = (vb || '').toLowerCase(); }
            if (va < vb) return direction === 'asc' ? -1 : 1;
            if (va > vb) return direction === 'asc' ? 1 : -1;
            return 0;
        });
        return result;
    },

    getIssuesForMilestone(msId) {
        return this.issues.filter(i => i.milestoneId === msId);
    },

    getIssuesForIteration(iterId) {
        return this.issues.filter(i => i.iterationId === iterId);
    },

    getIssuesForEpic(epicId) {
        return this.issues.filter(i => i.epicId === epicId);
    },

    getChildEpics(epicId) {
        return this.epics.filter(e => e.parentEpicId === epicId);
    },

    getIssuesForLabel(labelId) {
        return this.issues.filter(i => i.labels.includes(labelId));
    },

    getIssuesForBoard(boardId) {
        const board = this.getBoardById(boardId);
        if (!board) return {};
        const result = { _open: [] };
        const openIssues = this.issues.filter(i => i.status === 'open');
        board.lists.forEach(list => {
            if (list.type === 'label') {
                result[list.id] = openIssues.filter(i => i.labels.includes(list.labelId));
            } else if (list.type === 'milestone') {
                result[list.id] = openIssues.filter(i => i.milestoneId === list.milestoneId);
            }
        });
        // Open issues not in any list
        const assignedIds = new Set();
        Object.keys(result).forEach(k => {
            if (k !== '_open') result[k].forEach(i => assignedIds.add(i.id));
        });
        result._open = openIssues.filter(i => !assignedIds.has(i.id));
        // Closed issues
        result._closed = this.issues.filter(i => i.status === 'closed');
        return result;
    },

    getTodos(tab) {
        if (tab === 'pending') return this.todos.filter(t => t.status === 'pending');
        if (tab === 'snoozed') return this.todos.filter(t => t.status === 'snoozed');
        if (tab === 'done') return this.todos.filter(t => t.status === 'done');
        return this.todos;
    },

    // ---- Mutations ----

    createIssue(data) {
        const iid = this._nextIssueIid++;
        const now = new Date().toISOString();
        const issue = {
            id: 'issue_' + iid,
            iid,
            title: data.title,
            description: data.description || '',
            status: 'open',
            assignees: data.assignees || [],
            labels: data.labels || [],
            milestoneId: data.milestoneId || null,
            iterationId: data.iterationId || null,
            epicId: data.epicId || null,
            weight: data.weight || null,
            dueDate: data.dueDate || null,
            startDate: data.startDate || null,
            healthStatus: null,
            timeEstimate: 0,
            timeSpent: 0,
            confidential: data.confidential || false,
            authorId: this.currentUser.id,
            createdAt: now,
            updatedAt: now,
            closedAt: null,
            taskIds: [],
            linkedIssueIds: []
        };
        this.issues.push(issue);
        this.notify();
        return issue;
    },

    updateIssue(id, updates) {
        const issue = this.getIssueById(id);
        if (!issue) return;
        Object.assign(issue, updates, { updatedAt: new Date().toISOString() });
        if (updates.status === 'closed' && !issue.closedAt) issue.closedAt = new Date().toISOString();
        if (updates.status === 'open') issue.closedAt = null;
        this.notify();
    },

    deleteIssue(id) {
        this.issues = this.issues.filter(i => i.id !== id);
        this.todos = this.todos.filter(t => !(t.targetType === 'issue' && t.targetId === id));
        this.timelogs = this.timelogs.filter(t => t.issueId !== id);
        this.notify();
    },

    toggleIssueStatus(id) {
        const issue = this.getIssueById(id);
        if (!issue) return;
        if (issue.status === 'open') {
            issue.status = 'closed';
            issue.closedAt = new Date().toISOString();
        } else {
            issue.status = 'open';
            issue.closedAt = null;
        }
        issue.updatedAt = new Date().toISOString();
        this.notify();
    },

    // Label mutations
    createLabel(data) {
        const id = 'lbl_' + this._nextLabelId++;
        const label = {
            id,
            title: data.title,
            description: data.description || '',
            color: data.color || '#6c757d',
            textColor: data.textColor || '#fff',
            type: data.type || 'project',
            scoped: data.title.includes('::')
        };
        this.labels.push(label);
        this.notify();
        return label;
    },

    updateLabel(id, updates) {
        const label = this.getLabelById(id);
        if (!label) return;
        Object.assign(label, updates);
        if (updates.title !== undefined) label.scoped = updates.title.includes('::');
        this.notify();
    },

    deleteLabel(id) {
        this.labels = this.labels.filter(l => l.id !== id);
        this.issues.forEach(issue => {
            issue.labels = issue.labels.filter(l => l !== id);
        });
        this.epics.forEach(epic => {
            epic.labels = epic.labels.filter(l => l !== id);
        });
        this.notify();
    },

    // Milestone mutations
    createMilestone(data) {
        const id = 'ms_' + this._nextMilestoneId++;
        const ms = {
            id,
            title: data.title,
            description: data.description || '',
            startDate: data.startDate || null,
            dueDate: data.dueDate || null,
            status: 'active',
            createdAt: new Date().toISOString()
        };
        this.milestones.push(ms);
        this.notify();
        return ms;
    },

    updateMilestone(id, updates) {
        const ms = this.getMilestoneById(id);
        if (!ms) return;
        Object.assign(ms, updates);
        this.notify();
    },

    deleteMilestone(id) {
        this.milestones = this.milestones.filter(m => m.id !== id);
        this.issues.forEach(i => { if (i.milestoneId === id) i.milestoneId = null; });
        this.notify();
    },

    toggleMilestoneStatus(id) {
        const ms = this.getMilestoneById(id);
        if (!ms) return;
        ms.status = ms.status === 'active' ? 'closed' : 'active';
        this.notify();
    },

    // Iteration mutations
    createIteration(data) {
        const id = 'iter_' + this._nextIterationId++;
        const iter = {
            id,
            title: data.title,
            cadenceId: data.cadenceId,
            startDate: data.startDate,
            dueDate: data.dueDate,
            status: data.status || 'upcoming',
            createdAt: new Date().toISOString()
        };
        this.iterations.push(iter);
        this.notify();
        return iter;
    },

    updateIteration(id, updates) {
        const iter = this.getIterationById(id);
        if (!iter) return;
        Object.assign(iter, updates);
        this.notify();
    },

    deleteIteration(id) {
        this.iterations = this.iterations.filter(i => i.id !== id);
        this.issues.forEach(i => { if (i.iterationId === id) i.iterationId = null; });
        this.notify();
    },

    // Cadence mutations
    createCadence(data) {
        const id = 'cad_' + this._nextCadenceId++;
        const cad = {
            id,
            title: data.title,
            description: data.description || '',
            automatic: data.automatic || false,
            startDate: data.startDate || null,
            durationWeeks: data.durationWeeks || null,
            upcomingIterations: data.upcomingIterations || null,
            rollOver: data.rollOver || false,
            active: true
        };
        this.iterationCadences.push(cad);
        this.notify();
        return cad;
    },

    updateCadence(id, updates) {
        const cad = this.getCadenceById(id);
        if (!cad) return;
        Object.assign(cad, updates);
        this.notify();
    },

    deleteCadence(id) {
        this.iterationCadences = this.iterationCadences.filter(c => c.id !== id);
        const iterIds = this.iterations.filter(i => i.cadenceId === id).map(i => i.id);
        this.iterations = this.iterations.filter(i => i.cadenceId !== id);
        this.issues.forEach(i => { if (iterIds.includes(i.iterationId)) i.iterationId = null; });
        this.notify();
    },

    // Epic mutations
    createEpic(data) {
        const iid = this._nextEpicIid++;
        const now = new Date().toISOString();
        const epic = {
            id: 'epic_' + iid,
            iid,
            title: data.title,
            description: data.description || '',
            status: 'open',
            startDate: data.startDate || null,
            dueDate: data.dueDate || null,
            labels: data.labels || [],
            healthStatus: null,
            authorId: this.currentUser.id,
            confidential: data.confidential || false,
            parentEpicId: data.parentEpicId || null,
            createdAt: now,
            updatedAt: now
        };
        this.epics.push(epic);
        this.notify();
        return epic;
    },

    updateEpic(id, updates) {
        const epic = this.getEpicById(id);
        if (!epic) return;
        Object.assign(epic, updates, { updatedAt: new Date().toISOString() });
        this.notify();
    },

    deleteEpic(id) {
        this.epics = this.epics.filter(e => e.id !== id);
        this.issues.forEach(i => { if (i.epicId === id) i.epicId = null; });
        this.epics.forEach(e => { if (e.parentEpicId === id) e.parentEpicId = null; });
        this.todos = this.todos.filter(t => !(t.targetType === 'epic' && t.targetId === id));
        this.notify();
    },

    toggleEpicStatus(id) {
        const epic = this.getEpicById(id);
        if (!epic) return;
        epic.status = epic.status === 'open' ? 'closed' : 'open';
        epic.updatedAt = new Date().toISOString();
        this.notify();
    },

    // Board mutations
    createBoard(data) {
        const id = 'board_' + this._nextBoardId++;
        const board = { id, name: data.name, lists: data.lists || [] };
        this.boards.push(board);
        this.notify();
        return board;
    },

    updateBoard(id, updates) {
        const board = this.getBoardById(id);
        if (!board) return;
        Object.assign(board, updates);
        this.notify();
    },

    deleteBoard(id) {
        this.boards = this.boards.filter(b => b.id !== id);
        if (this.currentBoardId === id && this.boards.length > 0) this.currentBoardId = this.boards[0].id;
        this.notify();
    },

    addBoardList(boardId, listData) {
        const board = this.getBoardById(boardId);
        if (!board) return;
        const listId = 'list_' + Date.now();
        const newList = { id: listId, ...listData, position: board.lists.length };
        board.lists.push(newList);
        this.notify();
    },

    removeBoardList(boardId, listId) {
        const board = this.getBoardById(boardId);
        if (!board) return;
        board.lists = board.lists.filter(l => l.id !== listId);
        board.lists.forEach((l, i) => l.position = i);
        this.notify();
    },

    moveIssueBetweenLists(issueId, fromListId, toListId, boardId) {
        const board = this.getBoardById(boardId);
        if (!board) return;
        const issue = this.getIssueById(issueId);
        if (!issue) return;

        const fromList = board.lists.find(l => l.id === fromListId);
        const toList = board.lists.find(l => l.id === toListId);

        // Handle special lists
        if (toListId === '_closed') {
            issue.status = 'closed';
            issue.closedAt = new Date().toISOString();
        } else if (fromListId === '_closed') {
            issue.status = 'open';
            issue.closedAt = null;
        }

        if (fromList && fromList.type === 'label') {
            issue.labels = issue.labels.filter(l => l !== fromList.labelId);
        }
        if (toList && toList.type === 'label') {
            // For scoped labels, remove existing same-scope label
            const toLabel = this.getLabelById(toList.labelId);
            if (toLabel && toLabel.scoped) {
                const scope = toLabel.title.split('::')[0];
                issue.labels = issue.labels.filter(lid => {
                    const lbl = this.getLabelById(lid);
                    return !(lbl && lbl.scoped && lbl.title.startsWith(scope + '::'));
                });
            }
            if (!issue.labels.includes(toList.labelId)) {
                issue.labels.push(toList.labelId);
            }
        }
        if (fromList && fromList.type === 'milestone') {
            issue.milestoneId = null;
        }
        if (toList && toList.type === 'milestone') {
            issue.milestoneId = toList.milestoneId;
        }

        issue.updatedAt = new Date().toISOString();
        this.notify();
    },

    // Todo mutations
    markTodoDone(id) {
        const todo = this.todos.find(t => t.id === id);
        if (!todo) return;
        todo.status = 'done';
        this.notify();
    },

    markTodoPending(id) {
        const todo = this.todos.find(t => t.id === id);
        if (!todo) return;
        todo.status = 'pending';
        todo.snoozedUntil = null;
        this.notify();
    },

    snoozeTodo(id, until) {
        const todo = this.todos.find(t => t.id === id);
        if (!todo) return;
        todo.status = 'snoozed';
        todo.snoozedUntil = until;
        this.notify();
    },

    markAllTodosDone() {
        this.todos.filter(t => t.status === 'pending').forEach(t => t.status = 'done');
        this.notify();
    },

    restoreTodo(id) {
        const todo = this.todos.find(t => t.id === id);
        if (!todo) return;
        todo.status = 'pending';
        todo.snoozedUntil = null;
        this.notify();
    },

    // Time tracking
    addTimelog(issueId, data) {
        const id = 'tl_' + this._nextTimelogId++;
        const tl = {
            id,
            issueId,
            userId: this.currentUser.id,
            timeSpent: data.timeSpent,
            summary: data.summary || '',
            spentAt: data.spentAt || new Date().toISOString()
        };
        this.timelogs.push(tl);
        const issue = this.getIssueById(issueId);
        if (issue) {
            issue.timeSpent = (issue.timeSpent || 0) + data.timeSpent;
            issue.updatedAt = new Date().toISOString();
        }
        this.notify();
        return tl;
    },

    deleteTimelog(id) {
        const tl = this.timelogs.find(t => t.id === id);
        if (!tl) return;
        const issue = this.getIssueById(tl.issueId);
        if (issue) {
            issue.timeSpent = Math.max(0, (issue.timeSpent || 0) - tl.timeSpent);
        }
        this.timelogs = this.timelogs.filter(t => t.id !== id);
        this.notify();
    },

    setTimeEstimate(issueId, seconds) {
        const issue = this.getIssueById(issueId);
        if (!issue) return;
        issue.timeEstimate = seconds;
        issue.updatedAt = new Date().toISOString();
        this.notify();
    },

    // Issue label management with scoped label handling
    addLabelToIssue(issueId, labelId) {
        const issue = this.getIssueById(issueId);
        if (!issue) return;
        const label = this.getLabelById(labelId);
        if (label && label.scoped) {
            const scope = label.title.split('::')[0];
            issue.labels = issue.labels.filter(lid => {
                const l = this.getLabelById(lid);
                return !(l && l.scoped && l.title.startsWith(scope + '::'));
            });
        }
        if (!issue.labels.includes(labelId)) {
            issue.labels.push(labelId);
        }
        issue.updatedAt = new Date().toISOString();
        this.notify();
    },

    removeLabelFromIssue(issueId, labelId) {
        const issue = this.getIssueById(issueId);
        if (!issue) return;
        issue.labels = issue.labels.filter(l => l !== labelId);
        issue.updatedAt = new Date().toISOString();
        this.notify();
    },

    // Epic label management
    addLabelToEpic(epicId, labelId) {
        const epic = this.getEpicById(epicId);
        if (!epic) return;
        const label = this.getLabelById(labelId);
        if (label && label.scoped) {
            const scope = label.title.split('::')[0];
            epic.labels = epic.labels.filter(lid => {
                const l = this.getLabelById(lid);
                return !(l && l.scoped && l.title.startsWith(scope + '::'));
            });
        }
        if (!epic.labels.includes(labelId)) {
            epic.labels.push(labelId);
        }
        epic.updatedAt = new Date().toISOString();
        this.notify();
    },

    removeLabelFromEpic(epicId, labelId) {
        const epic = this.getEpicById(epicId);
        if (!epic) return;
        epic.labels = epic.labels.filter(l => l !== labelId);
        epic.updatedAt = new Date().toISOString();
        this.notify();
    }
};

// GitLab Plan & Track — State Management
const AppState = (() => {
    const STORAGE_KEY = 'gitlab-plan-track-state';

    // The live application state
    let state = {};

    // UI-only state (not persisted)
    let ui = {
        currentView: 'issues',
        currentIssueId: null,
        currentMilestoneId: null,
        currentEpicId: null,
        currentIterationId: null,
        currentBoardId: 1,
        modalOpen: null,
        toastMessage: null,
        toastType: null,
        issueFilters: {
            status: 'open',
            search: '',
            authorId: null,
            assigneeId: null,
            labelIds: [],
            milestoneId: null,
            iterationId: null,
            weight: null,
            confidential: null,
            sort: 'created_desc',
        },
        issueListPage: 1,
        issueListPageSize: 20,
        boardFilters: {
            assigneeId: null,
            labelIds: [],
            milestoneId: null,
            iterationId: null,
        },
        epicFilters: {
            status: 'open',
            search: '',
        },
        roadmapZoom: 'months',
        sidebarCollapsed: false,
        editingIssueTitle: false,
        editingIssueDescription: false,
    };

    function init() {
        const persisted = _loadPersisted();
        if (persisted) {
            state = persisted;
        } else {
            _loadSeedData();
        }
        _setupSSE();
    }

    function _loadSeedData() {
        const seed = SeedData;
        state = {
            _seedVersion: seed.SEED_DATA_VERSION,
            users: JSON.parse(JSON.stringify(seed.users)),
            currentUserId: seed.currentUserId,
            labels: JSON.parse(JSON.stringify(seed.labels)),
            milestones: JSON.parse(JSON.stringify(seed.milestones)),
            iterationCadences: JSON.parse(JSON.stringify(seed.iterationCadences)),
            iterations: JSON.parse(JSON.stringify(seed.iterations)),
            epics: JSON.parse(JSON.stringify(seed.epics)),
            issueTemplates: JSON.parse(JSON.stringify(seed.issueTemplates)),
            issues: JSON.parse(JSON.stringify(seed.issues)),
            comments: JSON.parse(JSON.stringify(seed.comments)),
            activityLog: JSON.parse(JSON.stringify(seed.activityLog)),
            boards: JSON.parse(JSON.stringify(seed.boards)),
            notifications: JSON.parse(JSON.stringify(seed.notifications)),
            notificationSettings: JSON.parse(JSON.stringify(seed.notificationSettings)),
            project: JSON.parse(JSON.stringify(seed.project)),
            _nextId: JSON.parse(JSON.stringify(seed._nextId)),
        };
    }

    function _loadPersisted() {
        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SeedData.SEED_DATA_VERSION) {
                localStorage.removeItem(STORAGE_KEY);
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    }

    function _persist() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
        } catch (e) {
            console.warn('Failed to persist state:', e);
        }
    }

    function _pushStateToServer() {
        try {
            fetch('/api/state', {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(state),
            }).catch(() => {});
        } catch (e) {}
    }

    function notify() {
        _persist();
        _pushStateToServer();
    }

    function resetToSeed() {
        localStorage.removeItem(STORAGE_KEY);
        _loadSeedData();
        notify();
    }

    function _setupSSE() {
        try {
            const es = new EventSource('/api/events');
            es.onmessage = (e) => {
                if (e.data === 'reset') {
                    localStorage.removeItem(STORAGE_KEY);
                    _loadSeedData();
                    ui.currentView = 'issues';
                    ui.currentIssueId = null;
                    if (typeof App !== 'undefined' && App.render) {
                        App.render();
                    }
                }
            };
        } catch (e) {}
    }

    // ─── Getters ──────────────────────────────────────────────────
    function getState() { return state; }
    function getUI() { return ui; }
    function getUser(id) { return state.users.find(u => u.id === id); }
    function getCurrentUser() { return getUser(state.currentUserId); }
    function getIssue(id) { return state.issues.find(i => i.id === id); }
    function getLabel(id) { return state.labels.find(l => l.id === id); }
    function getMilestone(id) { return state.milestones.find(m => m.id === id); }
    function getIteration(id) { return state.iterations.find(i => i.id === id); }
    function getEpic(id) { return state.epics.find(e => e.id === id); }
    function getBoard(id) { return state.boards.find(b => b.id === id); }
    function getComments(issueId) { return state.comments.filter(c => c.issueId === issueId); }
    function getActivity(issueId) { return state.activityLog.filter(a => a.issueId === issueId); }

    function getNextId(entity) {
        const id = state._nextId[entity];
        state._nextId[entity] = id + 1;
        return id;
    }

    // ─── Filtered/sorted issues ───────────────────────────────────
    function getFilteredIssues() {
        const f = ui.issueFilters;
        let result = state.issues.slice();

        if (f.status === 'open') result = result.filter(i => i.status === 'open');
        else if (f.status === 'closed') result = result.filter(i => i.status === 'closed');

        if (f.search) {
            const s = f.search.toLowerCase();
            result = result.filter(i =>
                i.title.toLowerCase().includes(s) ||
                (i.description && i.description.toLowerCase().includes(s)) ||
                ('#' + i.id).includes(s)
            );
        }

        if (f.authorId) result = result.filter(i => i.authorId === f.authorId);
        if (f.assigneeId) result = result.filter(i => i.assigneeIds.includes(f.assigneeId));
        if (f.labelIds.length > 0) result = result.filter(i => f.labelIds.every(lid => i.labelIds.includes(lid)));
        if (f.milestoneId) result = result.filter(i => i.milestoneId === f.milestoneId);
        if (f.iterationId) result = result.filter(i => i.iterationId === f.iterationId);
        if (f.weight !== null && f.weight !== undefined) result = result.filter(i => i.weight === f.weight);
        if (f.confidential !== null && f.confidential !== undefined) result = result.filter(i => i.confidential === f.confidential);

        // Sort
        const sortMap = {
            created_desc: (a, b) => b.createdAt.localeCompare(a.createdAt),
            created_asc: (a, b) => a.createdAt.localeCompare(b.createdAt),
            updated_desc: (a, b) => b.updatedAt.localeCompare(a.updatedAt),
            updated_asc: (a, b) => a.updatedAt.localeCompare(b.updatedAt),
            due_date_asc: (a, b) => {
                if (!a.dueDate && !b.dueDate) return 0;
                if (!a.dueDate) return 1;
                if (!b.dueDate) return -1;
                return a.dueDate.localeCompare(b.dueDate);
            },
            due_date_desc: (a, b) => {
                if (!a.dueDate && !b.dueDate) return 0;
                if (!a.dueDate) return 1;
                if (!b.dueDate) return -1;
                return b.dueDate.localeCompare(a.dueDate);
            },
            weight_desc: (a, b) => (b.weight || 0) - (a.weight || 0),
            weight_asc: (a, b) => (a.weight || 0) - (b.weight || 0),
            priority_desc: (a, b) => _getPriority(b) - _getPriority(a),
            priority_asc: (a, b) => _getPriority(a) - _getPriority(b),
        };
        const sortFn = sortMap[f.sort] || sortMap.created_desc;
        result.sort(sortFn);

        return result;
    }

    function _getPriority(issue) {
        if (issue.labelIds.includes(11)) return 4; // critical
        if (issue.labelIds.includes(12)) return 3; // high
        if (issue.labelIds.includes(13)) return 2; // medium
        if (issue.labelIds.includes(14)) return 1; // low
        return 0;
    }

    function getPagedIssues() {
        const all = getFilteredIssues();
        const start = (ui.issueListPage - 1) * ui.issueListPageSize;
        return {
            issues: all.slice(start, start + ui.issueListPageSize),
            total: all.length,
            page: ui.issueListPage,
            totalPages: Math.ceil(all.length / ui.issueListPageSize),
        };
    }

    // ─── Milestone stats ──────────────────────────────────────────
    function getMilestoneStats(milestoneId) {
        const issues = state.issues.filter(i => i.milestoneId === milestoneId);
        const open = issues.filter(i => i.status === 'open').length;
        const closed = issues.filter(i => i.status === 'closed').length;
        const total = issues.length;
        return { open, closed, total, percent: total > 0 ? Math.round((closed / total) * 100) : 0 };
    }

    // ─── Epic stats ───────────────────────────────────────────────
    function getEpicStats(epicId) {
        const epic = getEpic(epicId);
        if (!epic) return { open: 0, closed: 0, total: 0, percent: 0 };
        const issues = epic.childIssueIds.map(id => getIssue(id)).filter(Boolean);
        const open = issues.filter(i => i.status === 'open').length;
        const closed = issues.filter(i => i.status === 'closed').length;
        const total = issues.length;
        return { open, closed, total, percent: total > 0 ? Math.round((closed / total) * 100) : 0 };
    }

    // ─── Iteration stats ──────────────────────────────────────────
    function getIterationStats(iterationId) {
        const issues = state.issues.filter(i => i.iterationId === iterationId);
        const open = issues.filter(i => i.status === 'open').length;
        const closed = issues.filter(i => i.status === 'closed').length;
        const total = issues.length;
        const totalWeight = issues.reduce((s, i) => s + (i.weight || 0), 0);
        const closedWeight = issues.filter(i => i.status === 'closed').reduce((s, i) => s + (i.weight || 0), 0);
        return { open, closed, total, totalWeight, closedWeight, percent: total > 0 ? Math.round((closed / total) * 100) : 0 };
    }

    // ─── Board helpers ────────────────────────────────────────────
    function getBoardIssues(boardId) {
        const board = getBoard(boardId);
        if (!board) return {};
        const f = ui.boardFilters;
        let issues = state.issues.slice();

        if (f.assigneeId) issues = issues.filter(i => i.assigneeIds.includes(f.assigneeId));
        if (f.labelIds.length > 0) issues = issues.filter(i => f.labelIds.every(lid => i.labelIds.includes(lid)));
        if (f.milestoneId) issues = issues.filter(i => i.milestoneId === f.milestoneId);
        if (f.iterationId) issues = issues.filter(i => i.iterationId === f.iterationId);

        const result = {};
        board.lists.forEach(list => {
            if (list.type === 'backlog') {
                // Open issues not matching any label-based list
                const labelListIds = board.lists.filter(l => l.type === 'label').map(l => l.labelId);
                result[list.id] = issues.filter(i =>
                    i.status === 'open' && !labelListIds.some(lid => i.labelIds.includes(lid))
                );
            } else if (list.type === 'label') {
                result[list.id] = issues.filter(i =>
                    i.status === 'open' && i.labelIds.includes(list.labelId)
                );
            } else if (list.type === 'closed') {
                result[list.id] = issues.filter(i => i.status === 'closed');
            }
        });
        return result;
    }

    // ─── Mutations ────────────────────────────────────────────────
    function createIssue(data) {
        const id = getNextId('issues');
        const now = new Date().toISOString();
        const issue = {
            id,
            title: data.title,
            description: data.description || '',
            type: data.type || 'issue',
            status: 'open',
            authorId: state.currentUserId,
            assigneeIds: data.assigneeIds || [],
            labelIds: data.labelIds || [],
            milestoneId: data.milestoneId || null,
            iterationId: data.iterationId || null,
            weight: data.weight || null,
            dueDate: data.dueDate || null,
            confidential: data.confidential || false,
            timeEstimate: data.timeEstimate || 0,
            timeSpent: 0,
            createdAt: now,
            updatedAt: now,
            closedAt: null,
            relatedIssues: [],
        };
        state.issues.push(issue);
        _addActivity(id, 'created_issue', null);
        notify();
        return issue;
    }

    function updateIssue(id, updates) {
        const issue = getIssue(id);
        if (!issue) return;
        const now = new Date().toISOString();

        Object.keys(updates).forEach(key => {
            if (key === 'labelIds') {
                const added = updates.labelIds.filter(l => !issue.labelIds.includes(l));
                const removed = issue.labelIds.filter(l => !updates.labelIds.includes(l));
                added.forEach(lid => _addActivity(id, 'added_label', { labelId: lid }));
                removed.forEach(lid => _addActivity(id, 'removed_label', { labelId: lid }));
            }
            if (key === 'assigneeIds') {
                const added = updates.assigneeIds.filter(a => !issue.assigneeIds.includes(a));
                const removed = issue.assigneeIds.filter(a => !updates.assigneeIds.includes(a));
                added.forEach(aid => _addActivity(id, 'assigned', { assigneeId: aid }));
                removed.forEach(aid => _addActivity(id, 'unassigned', { assigneeId: aid }));
            }
            if (key === 'milestoneId' && updates.milestoneId !== issue.milestoneId) {
                _addActivity(id, 'changed_milestone', { from: issue.milestoneId, to: updates.milestoneId });
            }
            if (key === 'iterationId' && updates.iterationId !== issue.iterationId) {
                _addActivity(id, 'changed_iteration', { from: issue.iterationId, to: updates.iterationId });
            }
            issue[key] = updates[key];
        });
        issue.updatedAt = now;
        notify();
    }

    function closeIssue(id) {
        const issue = getIssue(id);
        if (!issue) return;
        issue.status = 'closed';
        issue.closedAt = new Date().toISOString();
        issue.updatedAt = issue.closedAt;
        _addActivity(id, 'closed_issue', null);
        notify();
    }

    function reopenIssue(id) {
        const issue = getIssue(id);
        if (!issue) return;
        issue.status = 'open';
        issue.closedAt = null;
        issue.updatedAt = new Date().toISOString();
        _addActivity(id, 'reopened_issue', null);
        notify();
    }

    function addComment(issueId, body) {
        const id = getNextId('comments');
        const now = new Date().toISOString();
        const comment = {
            id, issueId, authorId: state.currentUserId,
            body, createdAt: now, updatedAt: now, type: 'comment'
        };
        state.comments.push(comment);
        const issue = getIssue(issueId);
        if (issue) issue.updatedAt = now;
        _processQuickActions(issueId, body);
        notify();
        return comment;
    }

    function updateComment(commentId, body) {
        const comment = state.comments.find(c => c.id === commentId);
        if (!comment) return;
        comment.body = body;
        comment.updatedAt = new Date().toISOString();
        notify();
    }

    function deleteComment(commentId) {
        const idx = state.comments.findIndex(c => c.id === commentId);
        if (idx !== -1) state.comments.splice(idx, 1);
        notify();
    }

    function _processQuickActions(issueId, body) {
        const issue = getIssue(issueId);
        if (!issue) return;
        const lines = body.split('\n');
        lines.forEach(line => {
            const trimmed = line.trim();
            // /close
            if (trimmed === '/close') { closeIssue(issueId); }
            // /reopen
            if (trimmed === '/reopen') { reopenIssue(issueId); }
            // /assign @username
            const assignMatch = trimmed.match(/^\/assign\s+@(\S+)/);
            if (assignMatch) {
                const user = state.users.find(u => u.username === assignMatch[1]);
                if (user && !issue.assigneeIds.includes(user.id)) {
                    issue.assigneeIds.push(user.id);
                    _addActivity(issueId, 'assigned', { assigneeId: user.id });
                }
            }
            // /unassign @username
            const unassignMatch = trimmed.match(/^\/unassign\s+@(\S+)/);
            if (unassignMatch) {
                const user = state.users.find(u => u.username === unassignMatch[1]);
                if (user) {
                    issue.assigneeIds = issue.assigneeIds.filter(id => id !== user.id);
                    _addActivity(issueId, 'unassigned', { assigneeId: user.id });
                }
            }
            // /label ~labelname
            const labelMatch = trimmed.match(/^\/label\s+~(.+)/);
            if (labelMatch) {
                const labelName = labelMatch[1].trim();
                const label = state.labels.find(l => l.name === labelName);
                if (label && !issue.labelIds.includes(label.id)) {
                    // Handle scoped labels (remove existing in same scope)
                    if (label.scoped) {
                        const scope = label.name.split('::')[0];
                        issue.labelIds = issue.labelIds.filter(lid => {
                            const existing = getLabel(lid);
                            return !(existing && existing.scoped && existing.name.startsWith(scope + '::'));
                        });
                    }
                    issue.labelIds.push(label.id);
                    _addActivity(issueId, 'added_label', { labelId: label.id });
                }
            }
            // /unlabel ~labelname
            const unlabelMatch = trimmed.match(/^\/unlabel\s+~(.+)/);
            if (unlabelMatch) {
                const labelName = unlabelMatch[1].trim();
                const label = state.labels.find(l => l.name === labelName);
                if (label) {
                    issue.labelIds = issue.labelIds.filter(lid => lid !== label.id);
                    _addActivity(issueId, 'removed_label', { labelId: label.id });
                }
            }
            // /milestone %title
            const milestoneMatch = trimmed.match(/^\/milestone\s+%(.+)/);
            if (milestoneMatch) {
                const msTitle = milestoneMatch[1].trim();
                const ms = state.milestones.find(m => m.title.includes(msTitle));
                if (ms) {
                    _addActivity(issueId, 'changed_milestone', { from: issue.milestoneId, to: ms.id });
                    issue.milestoneId = ms.id;
                }
            }
            // /weight N
            const weightMatch = trimmed.match(/^\/weight\s+(\d+)/);
            if (weightMatch) {
                issue.weight = parseInt(weightMatch[1]);
            }
            // /due YYYY-MM-DD
            const dueMatch = trimmed.match(/^\/due\s+(\d{4}-\d{2}-\d{2})/);
            if (dueMatch) {
                issue.dueDate = dueMatch[1];
            }
            // /estimate Xh or XhYm
            const estimateMatch = trimmed.match(/^\/estimate\s+(\d+)h(?:(\d+)m)?/);
            if (estimateMatch) {
                const hours = parseInt(estimateMatch[1]);
                const minutes = parseInt(estimateMatch[2] || '0');
                issue.timeEstimate = (hours * 3600) + (minutes * 60);
            }
            // /spend Xh or XhYm
            const spendMatch = trimmed.match(/^\/spend\s+(\d+)h(?:(\d+)m)?/);
            if (spendMatch) {
                const hours = parseInt(spendMatch[1]);
                const minutes = parseInt(spendMatch[2] || '0');
                issue.timeSpent += (hours * 3600) + (minutes * 60);
            }
        });
    }

    function _addActivity(issueId, action, detail) {
        const id = getNextId('activityLog');
        state.activityLog.push({
            id, issueId, userId: state.currentUserId,
            action, detail, createdAt: new Date().toISOString()
        });
    }

    // ─── Label CRUD ───────────────────────────────────────────────
    function createLabel(data) {
        const id = getNextId('labels');
        const label = {
            id,
            name: data.name,
            description: data.description || '',
            color: data.color,
            textColor: _getTextColor(data.color),
            scoped: data.name.includes('::'),
        };
        state.labels.push(label);
        notify();
        return label;
    }

    function updateLabel(id, updates) {
        const label = getLabel(id);
        if (!label) return;
        Object.assign(label, updates);
        if (updates.color) label.textColor = _getTextColor(updates.color);
        if (updates.name !== undefined) label.scoped = updates.name.includes('::');
        notify();
    }

    function deleteLabel(id) {
        const idx = state.labels.findIndex(l => l.id === id);
        if (idx === -1) return;
        state.labels.splice(idx, 1);
        // Remove from all issues
        state.issues.forEach(issue => {
            issue.labelIds = issue.labelIds.filter(lid => lid !== id);
        });
        // Remove from epics
        state.epics.forEach(epic => {
            epic.labels = epic.labels.filter(lid => lid !== id);
        });
        // Remove from board lists
        state.boards.forEach(board => {
            board.lists = board.lists.filter(l => l.labelId !== id);
        });
        notify();
    }

    function _getTextColor(bgColor) {
        const hex = bgColor.replace('#', '');
        const r = parseInt(hex.substr(0, 2), 16);
        const g = parseInt(hex.substr(2, 2), 16);
        const b = parseInt(hex.substr(4, 2), 16);
        const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
        return luminance > 0.5 ? '#333' : '#fff';
    }

    // ─── Milestone CRUD ───────────────────────────────────────────
    function createMilestone(data) {
        const id = getNextId('milestones');
        const ms = {
            id,
            title: data.title,
            description: data.description || '',
            startDate: data.startDate || null,
            dueDate: data.dueDate || null,
            status: 'active',
        };
        state.milestones.push(ms);
        notify();
        return ms;
    }

    function updateMilestone(id, updates) {
        const ms = getMilestone(id);
        if (!ms) return;
        Object.assign(ms, updates);
        notify();
    }

    function closeMilestone(id) {
        const ms = getMilestone(id);
        if (!ms) return;
        ms.status = 'closed';
        notify();
    }

    function reopenMilestone(id) {
        const ms = getMilestone(id);
        if (!ms) return;
        ms.status = 'active';
        notify();
    }

    function deleteMilestone(id) {
        const idx = state.milestones.findIndex(m => m.id === id);
        if (idx === -1) return;
        state.milestones.splice(idx, 1);
        state.issues.forEach(issue => {
            if (issue.milestoneId === id) issue.milestoneId = null;
        });
        notify();
    }

    // ─── Iteration CRUD ───────────────────────────────────────────
    function createIteration(data) {
        const id = getNextId('iterations');
        const iter = {
            id,
            cadenceId: data.cadenceId,
            title: data.title,
            startDate: data.startDate,
            endDate: data.endDate,
            status: data.status || 'upcoming',
        };
        state.iterations.push(iter);
        notify();
        return iter;
    }

    function updateIteration(id, updates) {
        const iter = getIteration(id);
        if (!iter) return;
        Object.assign(iter, updates);
        notify();
    }

    function deleteIteration(id) {
        const idx = state.iterations.findIndex(i => i.id === id);
        if (idx === -1) return;
        state.iterations.splice(idx, 1);
        state.issues.forEach(issue => {
            if (issue.iterationId === id) issue.iterationId = null;
        });
        notify();
    }

    // ─── Epic CRUD ────────────────────────────────────────────────
    function createEpic(data) {
        const id = getNextId('epics');
        const now = new Date().toISOString();
        const epic = {
            id,
            title: data.title,
            description: data.description || '',
            status: 'open',
            startDate: data.startDate || null,
            dueDate: data.dueDate || null,
            labels: data.labels || [],
            authorId: state.currentUserId,
            confidential: data.confidential || false,
            childIssueIds: [],
            childEpicIds: [],
            createdAt: now,
            updatedAt: now,
        };
        state.epics.push(epic);
        notify();
        return epic;
    }

    function updateEpic(id, updates) {
        const epic = getEpic(id);
        if (!epic) return;
        Object.assign(epic, updates);
        epic.updatedAt = new Date().toISOString();
        notify();
    }

    function closeEpic(id) {
        const epic = getEpic(id);
        if (!epic) return;
        epic.status = 'closed';
        epic.updatedAt = new Date().toISOString();
        notify();
    }

    function reopenEpic(id) {
        const epic = getEpic(id);
        if (!epic) return;
        epic.status = 'open';
        epic.updatedAt = new Date().toISOString();
        notify();
    }

    function addChildIssueToEpic(epicId, issueId) {
        const epic = getEpic(epicId);
        if (!epic) return;
        if (!epic.childIssueIds.includes(issueId)) {
            epic.childIssueIds.push(issueId);
            epic.updatedAt = new Date().toISOString();
            notify();
        }
    }

    function removeChildIssueFromEpic(epicId, issueId) {
        const epic = getEpic(epicId);
        if (!epic) return;
        epic.childIssueIds = epic.childIssueIds.filter(id => id !== issueId);
        epic.updatedAt = new Date().toISOString();
        notify();
    }

    // ─── Board mutations ──────────────────────────────────────────
    function addBoardList(boardId, labelId) {
        const board = getBoard(boardId);
        if (!board) return;
        const listId = getNextId('boardLists');
        const label = getLabel(labelId);
        const closedIdx = board.lists.findIndex(l => l.type === 'closed');
        const position = closedIdx > -1 ? closedIdx : board.lists.length;
        board.lists.splice(position, 0, {
            id: listId,
            type: 'label',
            title: label ? label.name : 'List',
            position,
            labelId,
        });
        // Re-index positions
        board.lists.forEach((l, i) => l.position = i);
        notify();
    }

    function removeBoardList(boardId, listId) {
        const board = getBoard(boardId);
        if (!board) return;
        board.lists = board.lists.filter(l => l.id !== listId);
        board.lists.forEach((l, i) => l.position = i);
        notify();
    }

    function moveIssueOnBoard(issueId, fromListId, toListId, boardId) {
        const board = getBoard(boardId);
        if (!board) return;
        const issue = getIssue(issueId);
        if (!issue) return;

        const fromList = board.lists.find(l => l.id === fromListId);
        const toList = board.lists.find(l => l.id === toListId);
        if (!fromList || !toList) return;

        // Remove old label if from a label list
        if (fromList.type === 'label' && fromList.labelId) {
            issue.labelIds = issue.labelIds.filter(lid => lid !== fromList.labelId);
        }

        // Add new label or change status
        if (toList.type === 'label' && toList.labelId) {
            if (!issue.labelIds.includes(toList.labelId)) {
                // Handle scoped labels
                const newLabel = getLabel(toList.labelId);
                if (newLabel && newLabel.scoped) {
                    const scope = newLabel.name.split('::')[0];
                    issue.labelIds = issue.labelIds.filter(lid => {
                        const existing = getLabel(lid);
                        return !(existing && existing.scoped && existing.name.startsWith(scope + '::'));
                    });
                }
                issue.labelIds.push(toList.labelId);
            }
            if (issue.status === 'closed') {
                issue.status = 'open';
                issue.closedAt = null;
            }
        } else if (toList.type === 'closed') {
            closeIssue(issueId);
            return;
        } else if (toList.type === 'backlog') {
            if (issue.status === 'closed') {
                issue.status = 'open';
                issue.closedAt = null;
            }
        }

        issue.updatedAt = new Date().toISOString();
        notify();
    }

    // ─── Notification mutations ───────────────────────────────────
    function markNotificationRead(id) {
        const n = state.notifications.find(n => n.id === id);
        if (n) { n.read = true; notify(); }
    }

    function markAllNotificationsRead() {
        state.notifications.forEach(n => { n.read = true; });
        notify();
    }

    function updateNotificationSettings(updates) {
        Object.assign(state.notificationSettings, updates);
        notify();
    }

    // ─── Issue bulk actions ───────────────────────────────────────
    function bulkCloseIssues(ids) {
        ids.forEach(id => closeIssue(id));
    }

    function bulkAssignIssues(ids, assigneeId) {
        ids.forEach(id => {
            const issue = getIssue(id);
            if (issue && !issue.assigneeIds.includes(assigneeId)) {
                issue.assigneeIds.push(assigneeId);
                issue.updatedAt = new Date().toISOString();
                _addActivity(id, 'assigned', { assigneeId });
            }
        });
        notify();
    }

    function bulkLabelIssues(ids, labelId) {
        ids.forEach(id => {
            const issue = getIssue(id);
            if (issue && !issue.labelIds.includes(labelId)) {
                issue.labelIds.push(labelId);
                issue.updatedAt = new Date().toISOString();
                _addActivity(id, 'added_label', { labelId });
            }
        });
        notify();
    }

    function bulkSetMilestone(ids, milestoneId) {
        ids.forEach(id => {
            const issue = getIssue(id);
            if (issue) {
                _addActivity(id, 'changed_milestone', { from: issue.milestoneId, to: milestoneId });
                issue.milestoneId = milestoneId;
                issue.updatedAt = new Date().toISOString();
            }
        });
        notify();
    }

    // ─── Related issues ───────────────────────────────────────────
    function addRelatedIssue(issueId, relatedId, type) {
        const issue = getIssue(issueId);
        const related = getIssue(relatedId);
        if (!issue || !related) return;

        if (!issue.relatedIssues.find(r => r.issueId === relatedId)) {
            issue.relatedIssues.push({ issueId: relatedId, type });
        }

        const reverseType = type === 'blocks' ? 'is_blocked_by' : type === 'is_blocked_by' ? 'blocks' : 'related_to';
        if (!related.relatedIssues.find(r => r.issueId === issueId)) {
            related.relatedIssues.push({ issueId, type: reverseType });
        }
        notify();
    }

    function removeRelatedIssue(issueId, relatedId) {
        const issue = getIssue(issueId);
        const related = getIssue(relatedId);
        if (issue) issue.relatedIssues = issue.relatedIssues.filter(r => r.issueId !== relatedId);
        if (related) related.relatedIssues = related.relatedIssues.filter(r => r.issueId !== issueId);
        notify();
    }

    // ─── Time tracking helpers ────────────────────────────────────
    function formatTime(seconds) {
        if (!seconds || seconds <= 0) return '0h';
        const h = Math.floor(seconds / 3600);
        const m = Math.floor((seconds % 3600) / 60);
        if (h > 0 && m > 0) return `${h}h ${m}m`;
        if (h > 0) return `${h}h`;
        return `${m}m`;
    }

    function addTimeSpent(issueId, seconds) {
        const issue = getIssue(issueId);
        if (!issue) return;
        issue.timeSpent = (issue.timeSpent || 0) + seconds;
        issue.updatedAt = new Date().toISOString();
        notify();
    }

    function setTimeEstimate(issueId, seconds) {
        const issue = getIssue(issueId);
        if (!issue) return;
        issue.timeEstimate = seconds;
        issue.updatedAt = new Date().toISOString();
        notify();
    }

    // ─── Subscribe/unsubscribe ────────────────────────────────────
    // Track subscriptions as an array in state
    function toggleSubscription(issueId) {
        if (!state.subscriptions) state.subscriptions = [];
        const idx = state.subscriptions.indexOf(issueId);
        if (idx === -1) {
            state.subscriptions.push(issueId);
        } else {
            state.subscriptions.splice(idx, 1);
        }
        notify();
        return idx === -1; // returns true if now subscribed
    }

    function isSubscribed(issueId) {
        if (!state.subscriptions) state.subscriptions = [];
        return state.subscriptions.includes(issueId);
    }

    // ─── Toast ────────────────────────────────────────────────────
    function showToast(message, type = 'info') {
        ui.toastMessage = message;
        ui.toastType = type;
        setTimeout(() => {
            ui.toastMessage = null;
            ui.toastType = null;
            if (typeof App !== 'undefined' && App.renderToast) App.renderToast();
        }, 3000);
    }

    return {
        init, notify, resetToSeed,
        getState, getUI, getUser, getCurrentUser,
        getIssue, getLabel, getMilestone, getIteration, getEpic, getBoard,
        getComments, getActivity, getNextId,
        getFilteredIssues, getPagedIssues,
        getMilestoneStats, getEpicStats, getIterationStats,
        getBoardIssues,
        createIssue, updateIssue, closeIssue, reopenIssue,
        addComment, updateComment, deleteComment,
        createLabel, updateLabel, deleteLabel,
        createMilestone, updateMilestone, closeMilestone, reopenMilestone, deleteMilestone,
        createIteration, updateIteration, deleteIteration,
        createEpic, updateEpic, closeEpic, reopenEpic, addChildIssueToEpic, removeChildIssueFromEpic,
        addBoardList, removeBoardList, moveIssueOnBoard,
        markNotificationRead, markAllNotificationsRead, updateNotificationSettings,
        bulkCloseIssues, bulkAssignIssues, bulkLabelIssues, bulkSetMilestone,
        addRelatedIssue, removeRelatedIssue,
        formatTime, addTimeSpent, setTimeEstimate,
        toggleSubscription, isSubscribed,
        showToast,
        _getTextColor,
    };
})();

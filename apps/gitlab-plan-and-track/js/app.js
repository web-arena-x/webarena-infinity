/* app.js — Router, event delegation, and lifecycle for GitLab Plan & Track */
/* eslint-disable */

const App = {
    _openDropdown: null,
    _selectedLabelColor: '#6c757d',
    _dragIssueId: null,
    _dragFromList: null,

    init() {
        AppState.init();
        this._setupSSE();
        AppState.subscribe(() => this.render());
        this._parseRoute();
        this.render();
        window.addEventListener('hashchange', () => { this._parseRoute(); this.render(); });
        document.addEventListener('click', (e) => this._handleClick(e));
        document.addEventListener('input', (e) => this._handleInput(e));
        document.addEventListener('change', (e) => this._handleChange(e));
        document.addEventListener('dragstart', (e) => this._handleDragStart(e));
        document.addEventListener('dragover', (e) => this._handleDragOver(e));
        document.addEventListener('drop', (e) => this._handleDrop(e));
        document.addEventListener('dragend', (e) => this._handleDragEnd(e));
    },

    _setupSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = (e) => {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
                window.location.hash = '#/issues';
            }
        };
    },

    _parseRoute() {
        const hash = window.location.hash.replace('#/', '') || 'issues';
        const parts = hash.split('/');
        const view = parts[0];
        const id = parts[1] || null;

        if (['issues', 'boards', 'epics', 'milestones', 'iterations', 'labels', 'todos'].includes(view)) {
            AppState.currentView = view;
            AppState.currentItemId = id;
        } else if (view === 'new-issue') {
            AppState.currentView = 'new-issue';
            AppState.currentItemId = null;
        } else if (view === 'edit-issue') {
            AppState.currentView = 'edit-issue';
            AppState.currentItemId = id;
        } else if (view === 'new-epic') {
            AppState.currentView = 'new-epic';
            AppState.currentItemId = null;
        } else if (view === 'edit-epic') {
            AppState.currentView = 'edit-epic';
            AppState.currentItemId = id;
        } else if (view === 'new-milestone') {
            AppState.currentView = 'new-milestone';
            AppState.currentItemId = null;
        } else if (view === 'edit-milestone') {
            AppState.currentView = 'edit-milestone';
            AppState.currentItemId = id;
        } else if (view === 'new-label') {
            AppState.currentView = 'new-label';
            AppState.currentItemId = null;
        } else if (view === 'edit-label') {
            AppState.currentView = 'edit-label';
            AppState.currentItemId = id;
            const editLabel = AppState.getLabelById(id);
            if (editLabel) this._selectedLabelColor = editLabel.color;
        } else if (view === 'new-cadence') {
            AppState.currentView = 'new-cadence';
            AppState.currentItemId = null;
        } else if (view === 'edit-cadence') {
            AppState.currentView = 'edit-cadence';
            AppState.currentItemId = id;
        } else if (view === 'new-iteration') {
            AppState.currentView = 'new-iteration';
            AppState.currentItemId = null;
        } else {
            AppState.currentView = 'issues';
            AppState.currentItemId = null;
        }
        AppState.selectedIssueIds = new Set();
    },

    navigate(route) {
        window.location.hash = '#/' + route;
    },

    render() {
        const sidebar = document.getElementById('sidebarNav');
        const content = document.getElementById('contentWrapper');
        if (sidebar) sidebar.innerHTML = Views.renderSidebar();
        if (content) content.innerHTML = Views.renderContent();
        // Close any open filter dropdowns
        this._openDropdown = null;
        // Update todo badge
        const todoBadge = document.getElementById('todoBadge');
        const pendingCount = AppState.todos.filter(t => t.status === 'pending').length;
        if (todoBadge) todoBadge.textContent = pendingCount > 0 ? pendingCount : '';
    },

    // ---- Event Handling ----
    _handleClick(e) {
        const target = e.target;

        // Close open dropdowns on outside click
        if (this._openDropdown) {
            const dd = document.getElementById(this._openDropdown);
            if (dd && !dd.contains(target) && !target.closest('[data-dropdown-trigger]') && !target.closest('[data-action="toggle-filter-dropdown"]')) {
                dd.style.display = 'none';
                this._openDropdown = null;
            }
        }

        // Route links
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            e.preventDefault();
            this.navigate(routeEl.dataset.route);
            return;
        }

        // Actions
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            this._handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // Dropdown triggers
        const triggerEl = target.closest('[data-dropdown-trigger]');
        if (triggerEl) {
            e.preventDefault();
            const ddId = triggerEl.dataset.dropdownTrigger + '-menu';
            this._toggleDropdown(ddId);
            return;
        }

        // Dropdown items
        const ddItemEl = target.closest('[data-dropdown-item]');
        if (ddItemEl) {
            e.preventDefault();
            this._handleDropdownSelect(ddItemEl);
            return;
        }

        // Color swatch
        const swatchEl = target.closest('[data-color]');
        if (swatchEl) {
            e.preventDefault();
            this._handleColorSelect(swatchEl);
            return;
        }

        // Issue row click (navigate to detail)
        const issueRow = target.closest('.issue-row');
        if (issueRow && !target.closest('a') && !target.closest('button') && !target.closest('.label-badge')) {
            const issueId = issueRow.dataset.issueId;
            if (issueId) this.navigate('issues/' + issueId);
            return;
        }

        // Modal overlay click to close
        if (target.id === 'modalOverlay') {
            Components.closeModal();
            return;
        }
    },

    _handleAction(action, el) {
        switch (action) {
            // Issue actions
            case 'new-issue':
                this.navigate('new-issue');
                break;
            case 'save-issue':
                this._saveIssue();
                break;
            case 'edit-issue':
                this.navigate('edit-issue/' + el.dataset.id);
                break;
            case 'toggle-issue-status':
                AppState.toggleIssueStatus(el.dataset.id);
                break;
            case 'delete-issue':
                Components.confirmDanger('Are you sure you want to delete this issue?', () => {
                    AppState.deleteIssue(el.dataset.id);
                    this.navigate('issues');
                    Components.showToast('Issue deleted');
                });
                break;

            // Epic actions
            case 'new-epic':
                this.navigate('new-epic');
                break;
            case 'save-epic':
                this._saveEpic();
                break;
            case 'edit-epic':
                this.navigate('edit-epic/' + el.dataset.id);
                break;
            case 'toggle-epic-status':
                AppState.toggleEpicStatus(el.dataset.id);
                break;

            // Milestone actions
            case 'new-milestone':
                this.navigate('new-milestone');
                break;
            case 'save-milestone':
                this._saveMilestone();
                break;
            case 'edit-milestone':
                this.navigate('edit-milestone/' + el.dataset.id);
                break;
            case 'toggle-milestone-status':
                AppState.toggleMilestoneStatus(el.dataset.id);
                break;

            // Label actions
            case 'new-label':
                this.navigate('new-label');
                break;
            case 'save-label':
                this._saveLabel();
                break;
            case 'apply-custom-color': {
                const inp = document.getElementById('custom-color-input');
                if (inp) {
                    const hex = inp.value.trim();
                    if (/^#[0-9a-fA-F]{6}$/.test(hex)) {
                        this._selectedLabelColor = hex;
                        document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('selected'));
                        const preview = document.getElementById('colorPreview');
                        if (preview) {
                            const title = document.getElementById('label-title');
                            const titleVal = title ? title.value : 'Preview';
                            const isScoped = titleVal.includes('::');
                            preview.innerHTML = Components.labelBadge({ id: 'preview', title: titleVal || 'Preview', color: hex, textColor: '#fff', scoped: isScoped });
                        }
                    } else {
                        Components.showToast('Enter a valid hex color (e.g. #ff5733)');
                    }
                }
                break;
            }
            case 'edit-label':
                this.navigate('edit-label/' + el.dataset.id);
                break;
            case 'delete-label':
                Components.confirmDanger('Delete this label? It will be removed from all issues.', () => {
                    AppState.deleteLabel(el.dataset.id);
                    Components.showToast('Label deleted');
                });
                break;

            // Cadence & iteration actions
            case 'new-cadence':
                this.navigate('new-cadence');
                break;
            case 'save-cadence':
                this._saveCadence();
                break;
            case 'edit-cadence':
                this.navigate('edit-cadence/' + el.dataset.id);
                break;
            case 'new-iteration':
                AppState._tempCadenceId = el.dataset.cadenceId || null;
                this.navigate('new-iteration');
                break;
            case 'save-iteration':
                this._saveIteration();
                break;

            // Board actions
            case 'switch-board':
                AppState.currentBoardId = el.dataset.id;
                this.render();
                break;

            // Todo actions
            case 'switch-todo-tab':
                AppState.todoTab = el.dataset.tab;
                this.render();
                break;
            case 'done-todo':
                AppState.markTodoDone(el.dataset.id);
                Components.showToast('To-do marked as done');
                break;
            case 'snooze-todo':
                this._showSnoozePicker(el.dataset.id);
                break;
            case 'unsnooze-todo':
                AppState.restoreTodo(el.dataset.id);
                Components.showToast('Snooze removed');
                break;
            case 'restore-todo':
                AppState.restoreTodo(el.dataset.id);
                Components.showToast('To-do restored');
                break;
            case 'mark-all-todos-done':
                AppState.markAllTodosDone();
                Components.showToast('All to-dos marked as done');
                break;

            // Filter actions
            case 'filter-status':
                AppState.filters.status = el.dataset.value;
                AppState.currentPage = 1;
                this.render();
                break;
            case 'toggle-filter-dropdown': {
                const filterId = 'filter-' + el.dataset.filter;
                this._toggleDropdown(filterId);
                break;
            }
            case 'set-filter': {
                const filter = el.dataset.filter;
                const value = el.dataset.value || null;
                if (filter === 'assignee') AppState.filters.assignee = value;
                else if (filter === 'milestone') AppState.filters.milestone = value;
                AppState.currentPage = 1;
                this.render();
                break;
            }
            case 'toggle-label-filter': {
                const labelId = el.dataset.value;
                const idx = AppState.filters.labels.indexOf(labelId);
                if (idx >= 0) AppState.filters.labels.splice(idx, 1);
                else AppState.filters.labels.push(labelId);
                AppState.currentPage = 1;
                this.render();
                break;
            }
            case 'set-sort': {
                AppState.issueSort.field = el.dataset.field;
                AppState.issueSort.direction = el.dataset.direction;
                AppState.currentPage = 1;
                this.render();
                break;
            }

            // Pagination
            case 'prev-page':
                if (AppState.currentPage > 1) { AppState.currentPage--; this.render(); }
                break;
            case 'next-page':
                AppState.currentPage++;
                this.render();
                break;
            case 'goto-page':
                AppState.currentPage = parseInt(el.dataset.page);
                this.render();
                break;

            // Sidebar edit actions
            case 'edit-assignees':
                this._showAssigneeEditor(el.dataset.id);
                break;
            case 'edit-labels':
                this._showLabelEditor(el.dataset.id, el.dataset.type);
                break;
            case 'edit-milestone':
                if (!el.closest('.detail-sidebar')) {
                    this.navigate('edit-milestone/' + el.dataset.id);
                } else {
                    this._showMilestoneEditor(el.dataset.id);
                }
                break;
            case 'edit-iteration':
                this._showIterationEditor(el.dataset.id);
                break;
            case 'edit-epic-assignment':
                this._showEpicEditor(el.dataset.id);
                break;
            case 'edit-health':
                this._showHealthEditor(el.dataset.id);
                break;
            case 'edit-due-date':
                this._showDueDateEditor(el.dataset.id);
                break;
            case 'edit-weight':
                this._showWeightEditor(el.dataset.id);
                break;
            case 'edit-time-estimate':
                this._showTimeEstimateEditor(el.dataset.id);
                break;
            case 'add-timelog':
                this._showTimelogEditor(el.dataset.issueId);
                break;
            case 'delete-timelog':
                AppState.deleteTimelog(el.dataset.id);
                Components.showToast('Time entry deleted');
                break;

            // Modal actions
            case 'close-modal':
                Components.closeModal();
                break;
            case 'confirm-modal':
                if (Components._confirmCallback) {
                    Components._confirmCallback();
                    Components._confirmCallback = null;
                }
                Components.closeModal();
                break;

            // Cancel form
            case 'cancel-form':
                this.navigate(el.dataset.route || 'issues');
                break;

            default:
                break;
        }
    },

    _handleInput(e) {
        if (e.target.id === 'issueSearchInput') {
            AppState.filters.search = e.target.value;
            AppState.currentPage = 1;
            // Debounce render
            clearTimeout(this._searchTimer);
            this._searchTimer = setTimeout(() => this.render(), 200);
        }
    },

    _handleChange(e) {
        // Handle checkbox changes in filter dropdowns
        const toggleFilter = e.target.closest('[data-action="toggle-label-filter"]');
        if (toggleFilter) {
            const labelId = toggleFilter.dataset.value;
            const idx = AppState.filters.labels.indexOf(labelId);
            if (idx >= 0) AppState.filters.labels.splice(idx, 1);
            else AppState.filters.labels.push(labelId);
            AppState.currentPage = 1;
            this.render();
        }
    },

    // ---- Dropdown management ----
    _toggleDropdown(ddId) {
        const dd = document.getElementById(ddId);
        if (!dd) return;
        if (this._openDropdown && this._openDropdown !== ddId) {
            const prev = document.getElementById(this._openDropdown);
            if (prev) prev.style.display = 'none';
        }
        const isOpen = dd.style.display !== 'none';
        dd.style.display = isOpen ? 'none' : 'block';
        this._openDropdown = isOpen ? null : ddId;
    },

    _handleDropdownSelect(el) {
        const ddId = el.dataset.dropdownItem;
        const value = el.dataset.value;

        // Update display
        const dropdown = document.getElementById(ddId);
        if (dropdown) {
            const trigger = dropdown.querySelector('.dropdown-text');
            if (trigger) trigger.textContent = value ? el.textContent : dropdown.closest('.custom-dropdown').querySelector('.dropdown-trigger').dataset.placeholder || 'Select...';
            const items = dropdown.querySelectorAll('.dropdown-item');
            items.forEach(item => item.classList.toggle('selected', item === el));
        }

        // Close dropdown
        const menu = document.getElementById(ddId + '-menu');
        if (menu) menu.style.display = 'none';
        this._openDropdown = null;
    },

    _handleColorSelect(el) {
        const color = el.dataset.color;
        this._selectedLabelColor = color;
        const customInput = document.getElementById('custom-color-input');
        if (customInput) customInput.value = color;
        // Update preview
        document.querySelectorAll('.color-swatch').forEach(s => s.classList.toggle('selected', s.dataset.color === color));
        const preview = document.getElementById('colorPreview');
        if (preview) {
            const title = document.getElementById('label-title');
            const titleVal = title ? title.value : 'Preview';
            const isScoped = titleVal.includes('::');
            preview.innerHTML = Components.labelBadge({ id: 'preview', title: titleVal || 'Preview', color: color, textColor: '#fff', scoped: isScoped });
        }
    },

    // ---- Drag and drop for boards ----
    _handleDragStart(e) {
        const card = e.target.closest('.board-card');
        if (!card) return;
        this._dragIssueId = card.dataset.issueId;
        this._dragFromList = card.dataset.listId;
        card.classList.add('dragging');
        e.dataTransfer.effectAllowed = 'move';
    },

    _handleDragOver(e) {
        const listBody = e.target.closest('.board-list-body');
        if (listBody) {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            listBody.classList.add('drag-over');
        }
    },

    _handleDrop(e) {
        e.preventDefault();
        const listBody = e.target.closest('.board-list-body');
        if (!listBody || !this._dragIssueId) return;
        const toListId = listBody.dataset.listId;
        const boardId = listBody.closest('.board-list').dataset.boardId;
        if (this._dragFromList !== toListId) {
            AppState.moveIssueBetweenLists(this._dragIssueId, this._dragFromList, toListId, boardId);
        }
        listBody.classList.remove('drag-over');
    },

    _handleDragEnd(e) {
        this._dragIssueId = null;
        this._dragFromList = null;
        document.querySelectorAll('.dragging').forEach(el => el.classList.remove('dragging'));
        document.querySelectorAll('.drag-over').forEach(el => el.classList.remove('drag-over'));
    },

    // ---- Save functions ----
    _saveIssue() {
        const title = document.getElementById('issue-title');
        if (!title || !title.value.trim()) {
            Components.showToast('Title is required');
            return;
        }
        const data = {
            title: title.value.trim(),
            description: (document.getElementById('issue-description') || {}).value || '',
            assignees: Array.from(document.querySelectorAll('input[name="assignees"]:checked')).map(c => c.value),
            labels: Array.from(document.querySelectorAll('input[name="labels"]:checked')).map(c => c.value),
            milestoneId: this._getDropdownValue('issue-milestone'),
            iterationId: this._getDropdownValue('issue-iteration'),
            epicId: this._getDropdownValue('issue-epic'),
            startDate: (document.getElementById('issue-start-date') || {}).value || null,
            dueDate: (document.getElementById('issue-due-date') || {}).value || null,
            weight: parseInt((document.getElementById('issue-weight') || {}).value) || null,
            confidential: (document.getElementById('issue-confidential') || {}).checked || false
        };
        if (AppState.currentView === 'edit-issue' && AppState.currentItemId) {
            AppState.updateIssue(AppState.currentItemId, data);
            Components.showToast('Issue updated');
            this.navigate('issues/' + AppState.currentItemId);
        } else {
            const issue = AppState.createIssue(data);
            Components.showToast('Issue created');
            this.navigate('issues/' + issue.id);
        }
    },

    _saveEpic() {
        const title = document.getElementById('epic-title');
        if (!title || !title.value.trim()) {
            Components.showToast('Title is required');
            return;
        }
        const data = {
            title: title.value.trim(),
            description: (document.getElementById('epic-description') || {}).value || '',
            labels: Array.from(document.querySelectorAll('input[name="epic-labels"]:checked')).map(c => c.value),
            parentEpicId: this._getDropdownValue('epic-parent'),
            startDate: (document.getElementById('epic-start-date') || {}).value || null,
            dueDate: (document.getElementById('epic-due-date') || {}).value || null,
            confidential: (document.getElementById('epic-confidential') || {}).checked || false
        };
        if (AppState.currentView === 'edit-epic' && AppState.currentItemId) {
            AppState.updateEpic(AppState.currentItemId, data);
            Components.showToast('Epic updated');
            this.navigate('epics/' + AppState.currentItemId);
        } else {
            const epic = AppState.createEpic(data);
            Components.showToast('Epic created');
            this.navigate('epics/' + epic.id);
        }
    },

    _saveMilestone() {
        const title = document.getElementById('ms-title');
        if (!title || !title.value.trim()) {
            Components.showToast('Title is required');
            return;
        }
        const data = {
            title: title.value.trim(),
            description: (document.getElementById('ms-description') || {}).value || '',
            startDate: (document.getElementById('ms-start-date') || {}).value || null,
            dueDate: (document.getElementById('ms-due-date') || {}).value || null
        };
        if (AppState.currentView === 'edit-milestone' && AppState.currentItemId) {
            AppState.updateMilestone(AppState.currentItemId, data);
            Components.showToast('Milestone updated');
            this.navigate('milestones/' + AppState.currentItemId);
        } else {
            const ms = AppState.createMilestone(data);
            Components.showToast('Milestone created');
            this.navigate('milestones/' + ms.id);
        }
    },

    _saveLabel() {
        const title = document.getElementById('label-title');
        if (!title || !title.value.trim()) {
            Components.showToast('Title is required');
            return;
        }
        const typeEl = document.getElementById('label-type');
        const selectedType = typeEl ? (typeEl.querySelector('.dropdown-item.selected') || {}) : {};
        const typeVal = (selectedType.dataset || {}).value || 'project';

        const data = {
            title: title.value.trim(),
            description: (document.getElementById('label-description') || {}).value || '',
            color: this._selectedLabelColor,
            textColor: this._isLightColor(this._selectedLabelColor) ? '#333' : '#fff',
            type: typeVal
        };
        if (AppState.currentView === 'edit-label' && AppState.currentItemId) {
            AppState.updateLabel(AppState.currentItemId, data);
            Components.showToast('Label updated');
            this.navigate('labels');
        } else {
            AppState.createLabel(data);
            Components.showToast('Label created');
            this.navigate('labels');
        }
    },

    _saveCadence() {
        const title = document.getElementById('cad-title');
        if (!title || !title.value.trim()) {
            Components.showToast('Title is required');
            return;
        }
        const data = {
            title: title.value.trim(),
            description: (document.getElementById('cad-description') || {}).value || '',
            automatic: (document.getElementById('cad-automatic') || {}).checked || false,
            startDate: (document.getElementById('cad-start-date') || {}).value || null,
            durationWeeks: parseInt((document.getElementById('cad-duration') || {}).value) || null,
            upcomingIterations: parseInt((document.getElementById('cad-upcoming') || {}).value) || null,
            rollOver: (document.getElementById('cad-rollover') || {}).checked || false
        };
        if (AppState.currentView === 'edit-cadence' && AppState.currentItemId) {
            AppState.updateCadence(AppState.currentItemId, data);
            Components.showToast('Cadence updated');
        } else {
            AppState.createCadence(data);
            Components.showToast('Cadence created');
        }
        this.navigate('iterations');
    },

    _saveIteration() {
        const title = document.getElementById('iter-title');
        if (!title || !title.value.trim()) {
            Components.showToast('Title is required');
            return;
        }
        const cadenceId = this._getDropdownValue('iter-cadence');
        if (!cadenceId) {
            Components.showToast('Please select a cadence');
            return;
        }
        const data = {
            title: title.value.trim(),
            cadenceId: cadenceId,
            startDate: (document.getElementById('iter-start-date') || {}).value || null,
            dueDate: (document.getElementById('iter-due-date') || {}).value || null
        };
        AppState.createIteration(data);
        Components.showToast('Iteration created');
        this.navigate('iterations');
    },

    // ---- Sidebar editors (modals) ----
    _showAssigneeEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        let body = '<div class="modal-checkbox-list">';
        AppState.users.forEach(u => {
            const checked = issue.assignees.includes(u.id);
            body += '<label class="checkbox-item"><input type="checkbox" class="modal-assignee-cb" value="'+u.id+'"'+(checked ? ' checked' : '')+'> '+Components.avatar(u, 20)+' '+Components.escapeHtml(u.name)+'</label>';
        });
        body += '</div>';
        Components.showModal('Edit assignees', body, '<button class="btn btn-primary" id="saveAssigneesBtn">Save</button>');
        document.getElementById('saveAssigneesBtn').addEventListener('click', () => {
            const assignees = Array.from(document.querySelectorAll('.modal-assignee-cb:checked')).map(c => c.value);
            AppState.updateIssue(issueId, { assignees });
            Components.closeModal();
        });
    },

    _showLabelEditor(id, type) {
        const entity = type === 'epic' ? AppState.getEpicById(id) : AppState.getIssueById(id);
        if (!entity) return;
        let body = '<div class="modal-checkbox-list">';
        AppState.labels.forEach(l => {
            const checked = entity.labels.includes(l.id);
            body += '<label class="checkbox-item"><input type="checkbox" class="modal-label-cb" value="'+l.id+'"'+(checked ? ' checked' : '')+'> '+Components.labelBadge(l)+'</label>';
        });
        body += '</div>';
        Components.showModal('Edit labels', body, '<button class="btn btn-primary" id="saveLabelsBtn">Save</button>');
        document.getElementById('saveLabelsBtn').addEventListener('click', () => {
            const labels = Array.from(document.querySelectorAll('.modal-label-cb:checked')).map(c => c.value);
            if (type === 'epic') AppState.updateEpic(id, { labels });
            else AppState.updateIssue(id, { labels });
            Components.closeModal();
        });
    },

    _showMilestoneEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        let body = '<div class="modal-radio-list">';
        body += '<label class="radio-item"><input type="radio" name="modal-ms" value="" '+(issue.milestoneId ? '' : 'checked')+'> None</label>';
        AppState.milestones.filter(m => m.status === 'active').forEach(m => {
            body += '<label class="radio-item"><input type="radio" name="modal-ms" value="'+m.id+'"'+(issue.milestoneId === m.id ? ' checked' : '')+'> '+Components.escapeHtml(m.title)+'</label>';
        });
        body += '</div>';
        Components.showModal('Set milestone', body, '<button class="btn btn-primary" id="saveMsBtn">Save</button>');
        document.getElementById('saveMsBtn').addEventListener('click', () => {
            const selected = document.querySelector('input[name="modal-ms"]:checked');
            AppState.updateIssue(issueId, { milestoneId: selected && selected.value ? selected.value : null });
            Components.closeModal();
        });
    },

    _showIterationEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        let body = '<div class="modal-radio-list">';
        body += '<label class="radio-item"><input type="radio" name="modal-iter" value="" '+(issue.iterationId ? '' : 'checked')+'> None</label>';
        AppState.iterations.filter(i => i.status !== 'closed').forEach(i => {
            body += '<label class="radio-item"><input type="radio" name="modal-iter" value="'+i.id+'"'+(issue.iterationId === i.id ? ' checked' : '')+'> '+Components.escapeHtml(i.title)+'</label>';
        });
        body += '</div>';
        Components.showModal('Set iteration', body, '<button class="btn btn-primary" id="saveIterBtn">Save</button>');
        document.getElementById('saveIterBtn').addEventListener('click', () => {
            const selected = document.querySelector('input[name="modal-iter"]:checked');
            AppState.updateIssue(issueId, { iterationId: selected && selected.value ? selected.value : null });
            Components.closeModal();
        });
    },

    _showEpicEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        let body = '<div class="modal-radio-list">';
        body += '<label class="radio-item"><input type="radio" name="modal-epic" value="" '+(issue.epicId ? '' : 'checked')+'> None</label>';
        AppState.epics.filter(e => e.status === 'open').forEach(e => {
            body += '<label class="radio-item"><input type="radio" name="modal-epic" value="'+e.id+'"'+(issue.epicId === e.id ? ' checked' : '')+'> '+Components.escapeHtml(e.title)+'</label>';
        });
        body += '</div>';
        Components.showModal('Set epic', body, '<button class="btn btn-primary" id="saveEpicBtn">Save</button>');
        document.getElementById('saveEpicBtn').addEventListener('click', () => {
            const selected = document.querySelector('input[name="modal-epic"]:checked');
            AppState.updateIssue(issueId, { epicId: selected && selected.value ? selected.value : null });
            Components.closeModal();
        });
    },

    _showHealthEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        let body = '<div class="modal-radio-list">';
        body += '<label class="radio-item"><input type="radio" name="modal-health" value="" '+(issue.healthStatus ? '' : 'checked')+'> None</label>';
        ['on_track', 'needs_attention', 'at_risk'].forEach(h => {
            body += '<label class="radio-item"><input type="radio" name="modal-health" value="'+h+'"'+(issue.healthStatus === h ? ' checked' : '')+'> '+Components.healthBadge(h)+'</label>';
        });
        body += '</div>';
        Components.showModal('Set health status', body, '<button class="btn btn-primary" id="saveHealthBtn">Save</button>');
        document.getElementById('saveHealthBtn').addEventListener('click', () => {
            const selected = document.querySelector('input[name="modal-health"]:checked');
            AppState.updateIssue(issueId, { healthStatus: selected && selected.value ? selected.value : null });
            Components.closeModal();
        });
    },

    _showDueDateEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        const body = '<div class="form-group"><label class="form-label">Due date</label><input type="text" class="form-input" id="modal-due-date" value="'+Components.escapeAttr(issue.dueDate || '')+'" placeholder="YYYY-MM-DD"></div>';
        Components.showModal('Set due date', body, '<button class="btn btn-secondary" id="clearDueBtn">Clear</button><button class="btn btn-primary" id="saveDueBtn">Save</button>');
        document.getElementById('saveDueBtn').addEventListener('click', () => {
            AppState.updateIssue(issueId, { dueDate: document.getElementById('modal-due-date').value || null });
            Components.closeModal();
        });
        document.getElementById('clearDueBtn').addEventListener('click', () => {
            AppState.updateIssue(issueId, { dueDate: null });
            Components.closeModal();
        });
    },

    _showWeightEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        const body = '<div class="form-group"><label class="form-label">Weight</label><input type="number" class="form-input" id="modal-weight" value="'+(issue.weight != null ? issue.weight : '')+'" min="0"></div>';
        Components.showModal('Set weight', body, '<button class="btn btn-secondary" id="clearWeightBtn">Clear</button><button class="btn btn-primary" id="saveWeightBtn">Save</button>');
        document.getElementById('saveWeightBtn').addEventListener('click', () => {
            const val = document.getElementById('modal-weight').value;
            AppState.updateIssue(issueId, { weight: val !== '' ? parseInt(val) : null });
            Components.closeModal();
        });
        document.getElementById('clearWeightBtn').addEventListener('click', () => {
            AppState.updateIssue(issueId, { weight: null });
            Components.closeModal();
        });
    },

    _showTimeEstimateEditor(issueId) {
        const issue = AppState.getIssueById(issueId);
        if (!issue) return;
        const body = '<div class="form-group"><label class="form-label">Time estimate (e.g., 2h 30m, 1d, 3w)</label><input type="text" class="form-input" id="modal-estimate" value="'+Components.formatDuration(issue.timeEstimate)+'" placeholder="e.g., 2h 30m"></div>';
        Components.showModal('Set time estimate', body, '<button class="btn btn-secondary" id="clearEstBtn">Remove</button><button class="btn btn-primary" id="saveEstBtn">Save</button>');
        document.getElementById('saveEstBtn').addEventListener('click', () => {
            const val = document.getElementById('modal-estimate').value;
            AppState.setTimeEstimate(issueId, Components.parseDuration(val));
            Components.closeModal();
        });
        document.getElementById('clearEstBtn').addEventListener('click', () => {
            AppState.setTimeEstimate(issueId, 0);
            Components.closeModal();
        });
    },

    _showTimelogEditor(issueId) {
        const body = '<div class="form-group"><label class="form-label">Time spent (e.g., 2h 30m)</label><input type="text" class="form-input" id="modal-timespent" placeholder="e.g., 1h 30m"></div>'
            + '<div class="form-group"><label class="form-label">Date</label><input type="text" class="form-input" id="modal-timedate" value="'+new Date().toISOString().split('T')[0]+'" placeholder="YYYY-MM-DD"></div>'
            + '<div class="form-group"><label class="form-label">Summary</label><input type="text" class="form-input" id="modal-timesummary" placeholder="What did you work on?"></div>';
        Components.showModal('Add time entry', body, '<button class="btn btn-secondary" data-action="close-modal">Cancel</button><button class="btn btn-primary" id="saveTimelogBtn">Add</button>');
        document.getElementById('saveTimelogBtn').addEventListener('click', () => {
            const spent = Components.parseDuration(document.getElementById('modal-timespent').value);
            if (spent <= 0) { Components.showToast('Please enter valid time'); return; }
            AppState.addTimelog(issueId, {
                timeSpent: spent,
                summary: document.getElementById('modal-timesummary').value || '',
                spentAt: (document.getElementById('modal-timedate').value || new Date().toISOString().split('T')[0]) + 'T12:00:00Z'
            });
            Components.closeModal();
            Components.showToast('Time entry added');
        });
    },

    _showSnoozePicker(todoId) {
        const now = new Date();
        const oneHour = new Date(now.getTime() + 3600000).toISOString();
        const fourHours = new Date(now.getTime() + 14400000).toISOString();
        const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 8, 0, 0).toISOString();
        const nextWeek = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 7, 8, 0, 0).toISOString();

        const body = '<div class="snooze-options">'
            + '<button class="snooze-option" data-until="'+oneHour+'">1 hour</button>'
            + '<button class="snooze-option" data-until="'+fourHours+'">Later today (4 hours)</button>'
            + '<button class="snooze-option" data-until="'+tomorrow+'">Tomorrow (8:00 AM)</button>'
            + '<button class="snooze-option" data-until="'+nextWeek+'">Next week</button>'
            + '</div>';
        Components.showModal('Snooze until', body, '');
        document.querySelectorAll('.snooze-option').forEach(btn => {
            btn.addEventListener('click', () => {
                AppState.snoozeTodo(todoId, btn.dataset.until);
                Components.closeModal();
                Components.showToast('To-do snoozed');
            });
        });
    },

    // ---- Helpers ----
    _getDropdownValue(ddId) {
        const dd = document.getElementById(ddId);
        if (!dd) return null;
        const selected = dd.querySelector('.dropdown-item.selected');
        if (!selected) return null;
        return selected.dataset.value || null;
    },

    _isLightColor(hex) {
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        return (r * 299 + g * 587 + b * 114) / 1000 > 150;
    }
};

// Boot
document.addEventListener('DOMContentLoaded', () => App.init());

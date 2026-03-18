// GitLab Plan & Track — Application Controller
const App = (() => {
    const C = Components;

    // ─── Selected issue IDs for bulk actions ──────────────────────
    let selectedIssueIds = new Set();

    // ─── Dropdown state tracking ──────────────────────────────────
    let _dropdownValues = {};

    function init() {
        AppState.init();
        render();
        AppState.notify(); // Push initial state to server
        _setupGlobalListeners();
    }

    function render() {
        const ui = AppState.getUI();

        // Sidebar
        document.getElementById('sidebar').innerHTML = Views.sidebar();

        // Main content
        const main = document.getElementById('main-content');
        switch (ui.currentView) {
            case 'issues': main.innerHTML = Views.issuesList(); break;
            case 'issue-detail': main.innerHTML = Views.issueDetail(); break;
            case 'new-issue': main.innerHTML = Views.newIssueForm(); break;
            case 'labels': main.innerHTML = Views.labelsView(); break;
            case 'milestones': main.innerHTML = Views.milestonesView(); break;
            case 'milestone-detail': main.innerHTML = Views.milestoneDetail(); break;
            case 'boards': main.innerHTML = Views.boardsView(); _setupBoardDragDrop(); break;
            case 'iterations': main.innerHTML = Views.iterationsView(); break;
            case 'iteration-detail': main.innerHTML = Views.iterationDetail(); break;
            case 'epics': main.innerHTML = Views.epicsView(); break;
            case 'epic-detail': main.innerHTML = Views.epicDetail(); break;
            case 'roadmap': main.innerHTML = Views.roadmapView(); break;
            case 'notifications': main.innerHTML = Views.notificationsView(); break;
            case 'time-tracking': main.innerHTML = Views.timeTrackingView(); break;
            default: main.innerHTML = Views.issuesList();
        }

        // Modals
        const modalContainer = document.getElementById('modal-container');
        if (ui.modalOpen) {
            modalContainer.innerHTML = ui.modalOpen;
            modalContainer.style.display = 'block';
        } else {
            modalContainer.innerHTML = '';
            modalContainer.style.display = 'none';
        }

        renderToast();
    }

    function renderToast() {
        const ui = AppState.getUI();
        const toastContainer = document.getElementById('toast-container');
        if (toastContainer) {
            toastContainer.innerHTML = ui.toastMessage ? C.toast(ui.toastMessage, ui.toastType) : '';
        }
    }

    // ─── Global Event Delegation ──────────────────────────────────
    function _setupGlobalListeners() {
        document.addEventListener('click', _handleClick);
        document.addEventListener('input', _handleInput);
        document.addEventListener('change', _handleChange);
        document.addEventListener('keydown', _handleKeydown);

        // Close dropdowns when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.custom-dropdown')) {
                document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.remove('open'));
            }
        }, true);
    }

    function _handleClick(e) {
        const target = e.target.closest('[data-action]');
        if (!target) return;

        const action = target.dataset.action;

        switch (action) {
            // ─── Navigation ───────────────────────────────────────
            case 'navigate': _navigate(target.dataset.view); break;

            // ─── Issue List ───────────────────────────────────────
            case 'view-issue': {
                const id = parseInt(target.dataset.issueId || target.closest('[data-issue-id]')?.dataset.issueId);
                if (id) { _navigate('issue-detail', { issueId: id }); }
                break;
            }
            case 'new-issue': _navigate('new-issue'); break;
            case 'filter-status': {
                AppState.getUI().issueFilters.status = target.dataset.status;
                AppState.getUI().issueListPage = 1;
                render();
                break;
            }
            case 'page': {
                const p = parseInt(target.dataset.page);
                if (p >= 1) { AppState.getUI().issueListPage = p; render(); }
                break;
            }
            case 'select-all-issues': {
                const checked = target.checked;
                document.querySelectorAll('.issue-checkbox').forEach(cb => { cb.checked = checked; });
                _updateBulkSelection();
                break;
            }

            // ─── Bulk actions ─────────────────────────────────────
            case 'bulk-close': {
                if (selectedIssueIds.size > 0) {
                    AppState.bulkCloseIssues([...selectedIssueIds]);
                    selectedIssueIds.clear();
                    AppState.showToast(`Closed ${selectedIssueIds.size || 'selected'} issues`, 'success');
                    render();
                }
                break;
            }
            case 'bulk-assign': _showBulkModal('assign'); break;
            case 'bulk-label': _showBulkModal('label'); break;
            case 'bulk-milestone': _showBulkModal('milestone'); break;
            case 'confirm-bulk-assign': {
                const assigneeId = _dropdownValues['bulk-assignee'];
                if (assigneeId) {
                    AppState.bulkAssignIssues([...selectedIssueIds], assigneeId);
                    _closeModal();
                    selectedIssueIds.clear();
                    AppState.showToast('Issues assigned', 'success');
                    render();
                }
                break;
            }
            case 'confirm-bulk-label': {
                const labelId = _dropdownValues['bulk-label'];
                if (labelId) {
                    AppState.bulkLabelIssues([...selectedIssueIds], labelId);
                    _closeModal();
                    selectedIssueIds.clear();
                    AppState.showToast('Label applied', 'success');
                    render();
                }
                break;
            }
            case 'confirm-bulk-milestone': {
                const milestoneId = _dropdownValues['bulk-milestone'];
                AppState.bulkSetMilestone([...selectedIssueIds], milestoneId);
                _closeModal();
                selectedIssueIds.clear();
                AppState.showToast('Milestone set', 'success');
                render();
                break;
            }

            // ─── Issue Detail ─────────────────────────────────────
            case 'edit-issue-title':
                AppState.getUI().editingIssueTitle = true;
                render();
                document.getElementById('issue-title-input')?.focus();
                break;
            case 'confirm-issue-title': {
                const input = document.getElementById('issue-title-input');
                if (input && input.value.trim()) {
                    AppState.updateIssue(AppState.getUI().currentIssueId, { title: input.value.trim() });
                    AppState.getUI().editingIssueTitle = false;
                    render();
                }
                break;
            }
            case 'cancel-issue-title':
                AppState.getUI().editingIssueTitle = false;
                render();
                break;
            case 'edit-issue-description':
                AppState.getUI().editingIssueDescription = true;
                render();
                break;
            case 'save-issue-description': {
                const editor = document.getElementById('description-editor');
                if (editor) {
                    AppState.updateIssue(AppState.getUI().currentIssueId, { description: editor.value });
                    AppState.getUI().editingIssueDescription = false;
                    render();
                }
                break;
            }
            case 'cancel-issue-description':
                AppState.getUI().editingIssueDescription = false;
                render();
                break;
            case 'close-issue': {
                const id = parseInt(target.dataset.issueId);
                AppState.closeIssue(id);
                AppState.showToast('Issue closed', 'success');
                render();
                break;
            }
            case 'reopen-issue': {
                const id = parseInt(target.dataset.issueId);
                AppState.reopenIssue(id);
                AppState.showToast('Issue reopened', 'success');
                render();
                break;
            }
            case 'submit-comment': {
                const editor = document.getElementById('comment-editor');
                if (editor && editor.value.trim()) {
                    AppState.addComment(parseInt(target.dataset.issueId), editor.value.trim());
                    AppState.showToast('Comment added', 'success');
                    render();
                }
                break;
            }
            case 'toggle-subscription': {
                const issueId = parseInt(target.dataset.issueId);
                const now = AppState.toggleSubscription(issueId);
                AppState.showToast(now ? 'Subscribed to notifications' : 'Unsubscribed from notifications', 'info');
                render();
                break;
            }
            case 'remove-related-issue': {
                AppState.removeRelatedIssue(parseInt(target.dataset.issueId), parseInt(target.dataset.relatedId));
                render();
                break;
            }
            case 'add-related-issue': {
                AppState.getUI().modalOpen = Views.relatedIssueModal(AppState.getUI().currentIssueId);
                render();
                break;
            }
            case 'confirm-add-related': {
                const type = _dropdownValues['related-type'] || 'related_to';
                const relatedId = _dropdownValues['related-issue'];
                if (relatedId) {
                    AppState.addRelatedIssue(parseInt(target.dataset.issueId), relatedId, type);
                    _closeModal();
                    AppState.showToast('Related issue added', 'success');
                    render();
                }
                break;
            }

            // ─── Issue Sidebar ────────────────────────────────────
            case 'remove-label': {
                const labelId = parseInt(target.dataset.labelId);
                const issue = AppState.getIssue(AppState.getUI().currentIssueId);
                if (issue) {
                    AppState.updateIssue(issue.id, { labelIds: issue.labelIds.filter(id => id !== labelId) });
                    render();
                }
                e.stopPropagation();
                break;
            }

            // ─── Create Issue ─────────────────────────────────────
            case 'create-issue': _createIssue(); break;

            // ─── Dropdowns ────────────────────────────────────────
            case 'toggle-dropdown': _toggleDropdown(target.dataset.dropdown); e.stopPropagation(); break;
            case 'select-dropdown-item': _selectDropdownItem(target); e.stopPropagation(); break;
            case 'clear-date': {
                const picker = target.dataset.picker;
                const input = document.getElementById(picker + '-input');
                if (input) input.value = '';
                _handleDateChange(picker, '');
                break;
            }

            // ─── Labels ──────────────────────────────────────────
            case 'new-label':
                AppState.getUI().modalOpen = Views.labelFormModal();
                render();
                break;
            case 'edit-label': {
                const label = AppState.getLabel(parseInt(target.dataset.labelId));
                AppState.getUI().modalOpen = Views.labelFormModal(label);
                render();
                break;
            }
            case 'delete-label': {
                if (confirm('Delete this label?')) {
                    AppState.deleteLabel(parseInt(target.dataset.labelId));
                    AppState.showToast('Label deleted', 'success');
                    render();
                }
                break;
            }
            case 'create-label-confirm': _createLabel(); break;
            case 'save-label': _saveLabel(parseInt(target.dataset.labelId)); break;
            case 'select-color': {
                const color = target.dataset.color;
                const picker = target.dataset.picker;
                document.querySelectorAll(`#${picker} .color-swatch-btn`).forEach(b => b.classList.remove('selected'));
                target.classList.add('selected');
                const colorInput = document.getElementById(picker + '-input');
                if (colorInput) colorInput.value = color;
                break;
            }

            // ─── Milestones ───────────────────────────────────────
            case 'new-milestone':
                AppState.getUI().modalOpen = Views.milestoneFormModal();
                render();
                break;
            case 'view-milestone':
                _navigate('milestone-detail', { milestoneId: parseInt(target.dataset.milestoneId) });
                break;
            case 'edit-milestone': {
                const ms = AppState.getMilestone(parseInt(target.dataset.milestoneId));
                AppState.getUI().modalOpen = Views.milestoneFormModal(ms);
                render();
                break;
            }
            case 'close-milestone':
                AppState.closeMilestone(parseInt(target.dataset.milestoneId));
                AppState.showToast('Milestone closed', 'success');
                render();
                break;
            case 'reopen-milestone':
                AppState.reopenMilestone(parseInt(target.dataset.milestoneId));
                AppState.showToast('Milestone reopened', 'success');
                render();
                break;
            case 'delete-milestone':
                AppState.deleteMilestone(parseInt(target.dataset.milestoneId));
                AppState.showToast('Milestone deleted', 'success');
                _navigate('milestones');
                break;
            case 'create-milestone-confirm': _createMilestone(); break;
            case 'save-milestone': _saveMilestone(parseInt(target.dataset.milestoneId)); break;
            case 'switch-tab': {
                AppState.getUI()._milestonesTab = target.dataset.tab;
                render();
                break;
            }

            // ─── Boards ──────────────────────────────────────────
            case 'add-board-list': {
                AppState.getUI().modalOpen = Views.addBoardListModal(parseInt(target.dataset.boardId));
                render();
                break;
            }
            case 'confirm-add-board-list': {
                const labelId = _dropdownValues['board-list-label'];
                if (labelId) {
                    AppState.addBoardList(parseInt(target.dataset.boardId), labelId);
                    _closeModal();
                    render();
                }
                break;
            }
            case 'remove-board-list': {
                AppState.removeBoardList(parseInt(target.dataset.boardId), parseInt(target.dataset.listId));
                render();
                e.stopPropagation();
                break;
            }
            case 'board-new-issue': {
                _navigate('new-issue');
                break;
            }

            // ─── Iterations ───────────────────────────────────────
            case 'new-iteration':
                AppState.getUI().modalOpen = Views.iterationFormModal();
                render();
                break;
            case 'view-iteration':
                _navigate('iteration-detail', { iterationId: parseInt(target.dataset.iterationId) });
                break;
            case 'create-iteration-confirm': _createIteration(); break;

            // ─── Epics ────────────────────────────────────────────
            case 'new-epic':
                AppState.getUI().modalOpen = Views.epicFormModal();
                render();
                break;
            case 'view-epic':
                _navigate('epic-detail', { epicId: parseInt(target.dataset.epicId) });
                break;
            case 'close-epic':
                AppState.closeEpic(parseInt(target.dataset.epicId));
                AppState.showToast('Epic closed', 'success');
                render();
                break;
            case 'reopen-epic':
                AppState.reopenEpic(parseInt(target.dataset.epicId));
                AppState.showToast('Epic reopened', 'success');
                render();
                break;
            case 'create-epic-confirm': _createEpic(); break;
            case 'filter-epics-status': {
                AppState.getUI().epicFilters.status = target.dataset.status;
                render();
                break;
            }

            // ─── Notifications ────────────────────────────────────
            case 'mark-read':
                AppState.markNotificationRead(parseInt(target.dataset.notificationId));
                render();
                e.stopPropagation();
                break;
            case 'mark-all-read':
                AppState.markAllNotificationsRead();
                render();
                break;
            case 'notification-click': {
                const notifId = parseInt(target.dataset.notificationId);
                const issueId = parseInt(target.dataset.issueId);
                AppState.markNotificationRead(notifId);
                if (issueId) _navigate('issue-detail', { issueId });
                break;
            }

            // ─── Modal ───────────────────────────────────────────
            case 'close-modal':
            case 'close-modal-overlay':
                if (action === 'close-modal-overlay' && e.target !== target) break;
                _closeModal();
                break;
        }
    }

    function _handleInput(e) {
        const target = e.target;

        // Search issues
        if (target.id === 'issue-search') {
            AppState.getUI().issueFilters.search = target.value;
            AppState.getUI().issueListPage = 1;
            _debounceRender();
            return;
        }

        // Search epics
        if (target.id === 'epic-search') {
            AppState.getUI().epicFilters.search = target.value;
            _debounceRender();
            return;
        }

        // Dropdown search filter
        if (target.classList.contains('dropdown-search-input')) {
            const dropdownId = target.dataset.dropdown;
            const menu = document.getElementById(dropdownId + '-menu');
            if (!menu) return;
            const searchVal = target.value.toLowerCase();
            menu.querySelectorAll('.dropdown-item').forEach(item => {
                const label = (item.dataset.label || '').toLowerCase();
                item.style.display = label.includes(searchVal) ? '' : 'none';
            });
            return;
        }

        // Color input
        if (target.classList.contains('color-input')) {
            const color = target.value;
            if (/^#[0-9a-fA-F]{6}$/.test(color)) {
                const picker = target.dataset.picker;
                document.querySelectorAll(`#${picker} .color-swatch-btn`).forEach(b => b.classList.remove('selected'));
            }
        }
    }

    function _handleChange(e) {
        const target = e.target;

        // Issue checkbox
        if (target.classList.contains('issue-checkbox')) {
            _updateBulkSelection();
            return;
        }

        // Weight input
        if (target.id === 'sidebar-weight') {
            const issueId = parseInt(target.dataset.issueId);
            const weight = target.value ? parseInt(target.value) : null;
            AppState.updateIssue(issueId, { weight });
            return;
        }

        // Confidential toggle
        if (target.id === 'sidebar-confidential') {
            const issueId = parseInt(target.dataset.issueId);
            AppState.updateIssue(issueId, { confidential: target.checked });
            return;
        }

        // Date input
        if (target.classList.contains('date-input')) {
            const picker = target.dataset.picker;
            _handleDateChange(picker, target.value);
            return;
        }
    }

    function _handleKeydown(e) {
        // Save issue title on Enter
        if (e.key === 'Enter' && e.target.id === 'issue-title-input') {
            e.preventDefault();
            document.querySelector('[data-action="confirm-issue-title"]')?.click();
        }

        // Submit comment on Ctrl+Enter
        if (e.key === 'Enter' && e.ctrlKey && e.target.id === 'comment-editor') {
            document.querySelector('[data-action="submit-comment"]')?.click();
        }

        // Time input enter handlers
        if (e.key === 'Enter' && e.target.id === 'sidebar-estimate') {
            _handleTimeEstimate(e.target);
        }
        if (e.key === 'Enter' && e.target.id === 'sidebar-spend') {
            _handleTimeSpend(e.target);
        }

        // Escape to close modal
        if (e.key === 'Escape' && AppState.getUI().modalOpen) {
            _closeModal();
        }
    }

    // ─── Date change handler ──────────────────────────────────────
    function _handleDateChange(picker, value) {
        const ui = AppState.getUI();
        if (picker === 'sidebar-due-date') {
            AppState.updateIssue(ui.currentIssueId, { dueDate: value || null });
        }
    }

    // ─── Time tracking handlers ───────────────────────────────────
    function _handleTimeEstimate(input) {
        const seconds = _parseTimeInput(input.value);
        if (seconds !== null) {
            AppState.setTimeEstimate(AppState.getUI().currentIssueId, seconds);
            input.value = '';
            AppState.showToast('Time estimate updated', 'success');
            render();
        }
    }

    function _handleTimeSpend(input) {
        const seconds = _parseTimeInput(input.value);
        if (seconds !== null && seconds > 0) {
            AppState.addTimeSpent(AppState.getUI().currentIssueId, seconds);
            input.value = '';
            AppState.showToast('Time logged', 'success');
            render();
        }
    }

    function _parseTimeInput(value) {
        if (!value) return null;
        const match = value.match(/^(\d+)h(?:\s*(\d+)m)?$/);
        if (match) {
            return parseInt(match[1]) * 3600 + (parseInt(match[2] || '0')) * 60;
        }
        const matchM = value.match(/^(\d+)m$/);
        if (matchM) return parseInt(matchM[1]) * 60;
        return null;
    }

    // ─── Dropdown Logic ───────────────────────────────────────────
    function _toggleDropdown(dropdownId) {
        const menu = document.getElementById(dropdownId + '-menu');
        if (!menu) return;

        // Close all other dropdowns first
        document.querySelectorAll('.dropdown-menu.open').forEach(m => {
            if (m.id !== dropdownId + '-menu') m.classList.remove('open');
        });

        menu.classList.toggle('open');

        // Focus search input if present
        if (menu.classList.contains('open')) {
            const searchInput = menu.querySelector('.dropdown-search-input');
            if (searchInput) setTimeout(() => searchInput.focus(), 0);
        }
    }

    function _selectDropdownItem(target) {
        const dropdownId = target.dataset.dropdown;
        const value = target.dataset.value;
        const el = document.getElementById(dropdownId);
        const isMulti = el?.dataset.multi === 'true';

        // Parse value
        let parsedValue = value;
        if (value === 'null' || value === '') parsedValue = null;
        else if (!isNaN(value)) parsedValue = parseInt(value);

        if (isMulti) {
            if (!_dropdownValues[dropdownId]) _dropdownValues[dropdownId] = [];
            const arr = _dropdownValues[dropdownId];
            const idx = arr.indexOf(parsedValue);
            if (idx > -1) {
                arr.splice(idx, 1);
                target.classList.remove('selected');
                target.querySelector('.dropdown-check').innerHTML = '';
            } else {
                arr.push(parsedValue);
                target.classList.add('selected');
                target.querySelector('.dropdown-check').innerHTML = '&#10003;';
            }
            // Update trigger display
            const trigger = document.querySelector(`#${dropdownId} .dropdown-value`);
            if (trigger) {
                const labels = arr.map(v => {
                    const item = document.querySelector(`#${dropdownId}-menu [data-value="${v}"]`);
                    return item ? item.dataset.label : v;
                });
                trigger.textContent = labels.length > 0 ? labels.join(', ') : el.querySelector('.dropdown-trigger')?.textContent || 'Select...';
            }
        } else {
            _dropdownValues[dropdownId] = parsedValue;
            // Update selected state
            const menu = document.getElementById(dropdownId + '-menu');
            menu.querySelectorAll('.dropdown-item').forEach(item => {
                item.classList.remove('selected');
                item.querySelector('.dropdown-check').innerHTML = '';
            });
            target.classList.add('selected');
            target.querySelector('.dropdown-check').innerHTML = '&#10003;';
            // Update trigger
            const trigger = document.querySelector(`#${dropdownId} .dropdown-value`);
            if (trigger) trigger.textContent = target.dataset.label;
            // Close dropdown
            menu.classList.remove('open');
        }

        // Handle specific dropdown side effects
        _handleDropdownChange(dropdownId, isMulti ? _dropdownValues[dropdownId] : parsedValue);
    }

    function _handleDropdownChange(dropdownId, value) {
        const ui = AppState.getUI();

        switch (dropdownId) {
            // Issue list filters
            case 'filter-author':
                ui.issueFilters.authorId = value;
                ui.issueListPage = 1;
                render();
                break;
            case 'filter-assignee':
                ui.issueFilters.assigneeId = value;
                ui.issueListPage = 1;
                render();
                break;
            case 'filter-label':
                ui.issueFilters.labelIds = value || [];
                ui.issueListPage = 1;
                render();
                break;
            case 'filter-milestone':
                ui.issueFilters.milestoneId = value;
                ui.issueListPage = 1;
                render();
                break;
            case 'filter-sort':
                ui.issueFilters.sort = value;
                ui.issueListPage = 1;
                render();
                break;

            // Issue detail sidebar
            case 'sidebar-assignees':
                AppState.updateIssue(ui.currentIssueId, { assigneeIds: value || [] });
                render();
                break;
            case 'sidebar-labels': {
                // Handle scoped labels
                let newLabels = value || [];
                const scopedGroups = {};
                newLabels.forEach(lid => {
                    const label = AppState.getLabel(lid);
                    if (label && label.scoped) {
                        const scope = label.name.split('::')[0];
                        if (!scopedGroups[scope]) scopedGroups[scope] = [];
                        scopedGroups[scope].push(lid);
                    }
                });
                // Keep only last of each scoped group
                Object.values(scopedGroups).forEach(group => {
                    if (group.length > 1) {
                        const keep = group[group.length - 1];
                        newLabels = newLabels.filter(lid => !group.includes(lid) || lid === keep);
                    }
                });
                AppState.updateIssue(ui.currentIssueId, { labelIds: newLabels });
                render();
                break;
            }
            case 'sidebar-milestone':
                AppState.updateIssue(ui.currentIssueId, { milestoneId: value });
                render();
                break;
            case 'sidebar-iteration':
                AppState.updateIssue(ui.currentIssueId, { iterationId: value });
                render();
                break;

            // Board filters
            case 'board-filter-assignee':
                ui.boardFilters.assigneeId = value;
                render();
                break;
            case 'board-filter-milestone':
                ui.boardFilters.milestoneId = value;
                render();
                break;

            // Notification settings
            case 'notification-level':
                AppState.updateNotificationSettings({ level: value });
                break;

            // Roadmap zoom
            case 'roadmap-zoom':
                ui.roadmapZoom = value;
                render();
                break;

            // Issue template
            case 'issue-template': {
                if (value) {
                    const template = AppState.getState().issueTemplates.find(t => t.id === value);
                    if (template) {
                        const desc = document.getElementById('new-issue-description');
                        if (desc) desc.value = template.content;
                    }
                }
                break;
            }

            // Add child issue to epic
            case 'add-child-issue': {
                if (value && ui.currentEpicId) {
                    AppState.addChildIssueToEpic(ui.currentEpicId, value);
                    AppState.showToast('Child issue added', 'success');
                    render();
                }
                break;
            }
        }
    }

    // ─── Navigation ───────────────────────────────────────────────
    function _navigate(view, params = {}) {
        const ui = AppState.getUI();
        ui.currentView = view;
        ui.editingIssueTitle = false;
        ui.editingIssueDescription = false;
        selectedIssueIds.clear();
        _dropdownValues = {};

        if (params.issueId) ui.currentIssueId = params.issueId;
        if (params.milestoneId) ui.currentMilestoneId = params.milestoneId;
        if (params.epicId) ui.currentEpicId = params.epicId;
        if (params.iterationId) ui.currentIterationId = params.iterationId;

        window.scrollTo(0, 0);
        render();
    }

    // ─── Create Issue ─────────────────────────────────────────────
    function _createIssue() {
        const title = document.getElementById('new-issue-title')?.value?.trim();
        if (!title) {
            document.getElementById('title-error').style.display = 'block';
            document.getElementById('new-issue-title').classList.add('field-error');
            return;
        }

        const description = document.getElementById('new-issue-description')?.value || '';
        const type = _dropdownValues['issue-type'] || 'issue';
        const assigneeIds = _dropdownValues['new-issue-assignees'] || [];
        const labelIds = _dropdownValues['new-issue-labels'] || [];
        const milestoneId = _dropdownValues['new-issue-milestone'] || null;
        const iterationId = _dropdownValues['new-issue-iteration'] || null;
        const weight = parseInt(document.getElementById('new-issue-weight')?.value) || null;
        const dueDate = document.getElementById('new-issue-due-date-input')?.value || null;
        const confidential = document.getElementById('new-issue-confidential')?.checked || false;

        const issue = AppState.createIssue({
            title, description, type, assigneeIds, labelIds,
            milestoneId, iterationId, weight, dueDate, confidential
        });

        AppState.showToast(`Issue #${issue.id} created`, 'success');
        _navigate('issue-detail', { issueId: issue.id });
    }

    // ─── Create Label ─────────────────────────────────────────────
    function _createLabel() {
        const name = document.getElementById('label-name')?.value?.trim();
        const description = document.getElementById('label-description')?.value?.trim() || '';
        const colorInput = document.getElementById('label-color-input');
        const selectedBtn = document.querySelector('#label-color .color-swatch-btn.selected');
        const color = selectedBtn ? selectedBtn.dataset.color : (colorInput?.value || '#428bca');

        if (!name) return;
        AppState.createLabel({ name, description, color });
        _closeModal();
        AppState.showToast('Label created', 'success');
        render();
    }

    function _saveLabel(id) {
        const name = document.getElementById('label-name')?.value?.trim();
        const description = document.getElementById('label-description')?.value?.trim() || '';
        const colorInput = document.getElementById('label-color-input');
        const selectedBtn = document.querySelector('#label-color .color-swatch-btn.selected');
        const color = selectedBtn ? selectedBtn.dataset.color : (colorInput?.value || '#428bca');

        if (!name) return;
        AppState.updateLabel(id, { name, description, color });
        _closeModal();
        AppState.showToast('Label updated', 'success');
        render();
    }

    // ─── Create Milestone ─────────────────────────────────────────
    function _createMilestone() {
        const title = document.getElementById('milestone-title')?.value?.trim();
        if (!title) return;
        const description = document.getElementById('milestone-description')?.value?.trim() || '';
        const startDate = document.getElementById('milestone-start-date-input')?.value || null;
        const dueDate = document.getElementById('milestone-due-date-input')?.value || null;

        AppState.createMilestone({ title, description, startDate, dueDate });
        _closeModal();
        AppState.showToast('Milestone created', 'success');
        render();
    }

    function _saveMilestone(id) {
        const title = document.getElementById('milestone-title')?.value?.trim();
        if (!title) return;
        const description = document.getElementById('milestone-description')?.value?.trim() || '';
        const startDate = document.getElementById('milestone-start-date-input')?.value || null;
        const dueDate = document.getElementById('milestone-due-date-input')?.value || null;

        AppState.updateMilestone(id, { title, description, startDate, dueDate });
        _closeModal();
        AppState.showToast('Milestone updated', 'success');
        render();
    }

    // ─── Create Iteration ─────────────────────────────────────────
    function _createIteration() {
        const cadenceId = _dropdownValues['iteration-cadence'];
        const title = document.getElementById('iteration-title')?.value?.trim();
        const startDate = document.getElementById('iteration-start-date-input')?.value;
        const endDate = document.getElementById('iteration-end-date-input')?.value;

        if (!title || !startDate || !endDate) return;

        AppState.createIteration({ cadenceId, title, startDate, endDate });
        _closeModal();
        AppState.showToast('Iteration created', 'success');
        render();
    }

    // ─── Create Epic ──────────────────────────────────────────────
    function _createEpic() {
        const title = document.getElementById('epic-title')?.value?.trim();
        if (!title) return;
        const description = document.getElementById('epic-description')?.value || '';
        const startDate = document.getElementById('epic-start-date-input')?.value || null;
        const dueDate = document.getElementById('epic-due-date-input')?.value || null;
        const labels = _dropdownValues['epic-labels'] || [];
        const confidential = document.getElementById('epic-confidential')?.checked || false;

        const epic = AppState.createEpic({ title, description, startDate, dueDate, labels, confidential });
        _closeModal();
        AppState.showToast(`Epic created`, 'success');
        _navigate('epic-detail', { epicId: epic.id });
    }

    // ─── Board Drag & Drop ────────────────────────────────────────
    function _setupBoardDragDrop() {
        const columns = document.querySelectorAll('.board-column-body');
        const cards = document.querySelectorAll('.board-card');

        cards.forEach(card => {
            card.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', card.dataset.issueId);
                card.classList.add('dragging');
                e.dataTransfer.effectAllowed = 'move';
            });
            card.addEventListener('dragend', () => {
                card.classList.remove('dragging');
            });
        });

        columns.forEach(col => {
            col.addEventListener('dragover', (e) => {
                e.preventDefault();
                e.dataTransfer.dropEffect = 'move';
                col.classList.add('drag-over');
            });
            col.addEventListener('dragleave', () => {
                col.classList.remove('drag-over');
            });
            col.addEventListener('drop', (e) => {
                e.preventDefault();
                col.classList.remove('drag-over');
                const issueId = parseInt(e.dataTransfer.getData('text/plain'));
                const toListId = parseInt(col.dataset.listId);
                const boardId = parseInt(col.dataset.boardId);

                // Find the source list
                const issue = AppState.getIssue(issueId);
                if (!issue) return;
                const board = AppState.getBoard(boardId);
                if (!board) return;

                // Determine source list
                let fromListId = null;
                const boardIssues = AppState.getBoardIssues(boardId);
                for (const [listId, issues] of Object.entries(boardIssues)) {
                    if (issues.find(i => i.id === issueId)) {
                        fromListId = parseInt(listId);
                        break;
                    }
                }

                if (fromListId !== null && fromListId !== toListId) {
                    AppState.moveIssueOnBoard(issueId, fromListId, toListId, boardId);
                    render();
                }
            });
        });
    }

    // ─── Bulk Selection ───────────────────────────────────────────
    function _updateBulkSelection() {
        selectedIssueIds.clear();
        document.querySelectorAll('.issue-checkbox:checked').forEach(cb => {
            selectedIssueIds.add(parseInt(cb.dataset.issueId));
        });
        const bar = document.getElementById('bulk-actions-bar');
        const count = document.getElementById('bulk-count');
        if (bar) {
            bar.style.display = selectedIssueIds.size > 0 ? 'flex' : 'none';
        }
        if (count) {
            count.textContent = `${selectedIssueIds.size} selected`;
        }
    }

    function _showBulkModal(type) {
        AppState.getUI().modalOpen = Views.bulkActionModal(type);
        render();
    }

    // ─── Modal helpers ────────────────────────────────────────────
    function _closeModal() {
        AppState.getUI().modalOpen = null;
        render();
    }

    // ─── Debounce ─────────────────────────────────────────────────
    let _renderTimer = null;
    function _debounceRender() {
        clearTimeout(_renderTimer);
        _renderTimer = setTimeout(render, 200);
    }

    return { init, render, renderToast };
})();

// ─── Boot ─────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', App.init);

/* views.js — View renderers for GitLab Plan & Track */
/* eslint-disable */

const Views = {
    renderSidebar() {
        const view = AppState.currentView;
        const openCount = AppState.issues.filter(i => i.status === 'open').length;
        const todoCount = AppState.todos.filter(t => t.status === 'pending').length;

        return '<div class="sidebar-section">'
            + '<div class="sidebar-header">Plan</div>'
            + this._navItem('issues', 'Issues', '<svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>', openCount, view)
            + this._navItem('boards', 'Boards', '<svg width="16" height="16" viewBox="0 0 16 16"><rect x="1" y="3" width="4" height="10" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><rect x="6" y="1" width="4" height="14" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><rect x="11" y="5" width="4" height="8" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>', null, view)
            + this._navItem('epics', 'Epics', '<svg width="16" height="16" viewBox="0 0 16 16"><rect x="1" y="2" width="14" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="4" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="1.5"/><line x1="4" y1="10" x2="9" y2="10" stroke="currentColor" stroke-width="1.5"/></svg>', null, view)
            + this._navItem('milestones', 'Milestones', '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M3 2v12M3 4h7l3 3-3 3H3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>', null, view)
            + this._navItem('iterations', 'Iterations', '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M13 8A5 5 0 113 8" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13 8l2-2M13 8l2 2" stroke="currentColor" stroke-width="1.5"/></svg>', null, view)
            + this._navItem('labels', 'Labels', '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M2 7.5V2h5.5L14 8.5 8.5 14z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="5.5" cy="5.5" r="1" fill="currentColor"/></svg>', null, view)
            + '</div>'
            + '<div class="sidebar-section">'
            + '<div class="sidebar-header">Personal</div>'
            + this._navItem('todos', 'To-Do List', '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M3 8l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>', todoCount, view)
            + '</div>';
    },

    _navItem(route, label, icon, count, currentView) {
        const active = currentView === route ? ' active' : '';
        const countHtml = count ? '<span class="nav-count">'+count+'</span>' : '';
        return '<a class="nav-item'+active+'" data-route="'+Components.escapeAttr(route)+'" data-testid="nav-'+Components.escapeAttr(route)+'">'
            + '<span class="nav-icon">'+icon+'</span>'
            + '<span class="nav-label">'+Components.escapeHtml(label)+'</span>'
            + countHtml + '</a>';
    },

    renderContent() {
        switch (AppState.currentView) {
            case 'issues': return AppState.currentItemId ? this.renderIssueDetail() : this.renderIssueList();
            case 'boards': return this.renderBoardView();
            case 'epics': return AppState.currentItemId ? this.renderEpicDetail() : this.renderEpicList();
            case 'milestones': return AppState.currentItemId ? this.renderMilestoneDetail() : this.renderMilestoneList();
            case 'iterations': return AppState.currentItemId ? this.renderIterationDetail() : this.renderIterationList();
            case 'labels': return this.renderLabelList();
            case 'todos': return this.renderTodoList();
            case 'new-issue': return this.renderIssueForm();
            case 'edit-issue': return this.renderIssueForm(AppState.currentItemId);
            case 'new-epic': return this.renderEpicForm();
            case 'edit-epic': return this.renderEpicForm(AppState.currentItemId);
            case 'new-milestone': return this.renderMilestoneForm();
            case 'edit-milestone': return this.renderMilestoneForm(AppState.currentItemId);
            case 'new-label': return this.renderLabelForm();
            case 'edit-label': return this.renderLabelForm(AppState.currentItemId);
            case 'new-cadence': return this.renderCadenceForm();
            case 'edit-cadence': return this.renderCadenceForm(AppState.currentItemId);
            case 'new-iteration': return this.renderIterationForm();
            default: return this.renderIssueList();
        }
    },

    // ---- Issues ----
    renderIssueList() {
        const issues = AppState.getFilteredIssues();
        const total = issues.length;
        const pageSize = AppState.pageSize;
        const page = AppState.currentPage;
        const paged = issues.slice((page - 1) * pageSize, page * pageSize);
        const openCount = AppState.issues.filter(i => i.status === 'open').length;
        const closedCount = AppState.issues.filter(i => i.status === 'closed').length;

        let html = '<div class="page-header"><div class="page-header-left"><h1>Issues</h1></div>';
        html += '<div class="page-header-right"><button class="btn btn-primary" data-action="new-issue" data-testid="new-issue-btn">New issue</button></div></div>';
        // Filter bar
        html += '<div class="filter-bar" data-testid="issue-filters">';
        html += '<div class="filter-tabs"><button class="filter-tab'+(AppState.filters.status === 'open' ? ' active' : '')+'" data-action="filter-status" data-value="open" data-testid="filter-open">Open <span class="count">'+openCount+'</span></button>';
        html += '<button class="filter-tab'+(AppState.filters.status === 'closed' ? ' active' : '')+'" data-action="filter-status" data-value="closed" data-testid="filter-closed">Closed <span class="count">'+closedCount+'</span></button>';
        html += '<button class="filter-tab'+(AppState.filters.status === 'all' ? ' active' : '')+'" data-action="filter-status" data-value="all" data-testid="filter-all">All</button></div>';
        html += '<div class="filter-controls">';
        html += '<input type="text" class="filter-search" id="issueSearchInput" placeholder="Search issues..." value="'+Components.escapeAttr(AppState.filters.search)+'" data-testid="issue-search">';
        // Assignee filter dropdown
        html += '<div class="filter-dropdown-wrap">'
            + '<button class="btn btn-sm btn-outline filter-btn" data-action="toggle-filter-dropdown" data-filter="assignee">Assignee'+(AppState.filters.assignee ? ' ✓' : '')+'</button>'
            + '<div class="filter-dropdown" id="filter-assignee" style="display:none">'
            + '<div class="filter-dropdown-item'+(AppState.filters.assignee === null ? ' selected' : '')+'" data-action="set-filter" data-filter="assignee" data-value="">Any</div>';
        AppState.users.forEach(u => {
            html += '<div class="filter-dropdown-item'+(AppState.filters.assignee === u.id ? ' selected' : '')+'" data-action="set-filter" data-filter="assignee" data-value="'+u.id+'">'+Components.escapeHtml(u.name)+'</div>';
        });
        html += '</div></div>';
        // Milestone filter
        html += '<div class="filter-dropdown-wrap">'
            + '<button class="btn btn-sm btn-outline filter-btn" data-action="toggle-filter-dropdown" data-filter="milestone">Milestone'+(AppState.filters.milestone ? ' ✓' : '')+'</button>'
            + '<div class="filter-dropdown" id="filter-milestone" style="display:none">'
            + '<div class="filter-dropdown-item'+(AppState.filters.milestone === null ? ' selected' : '')+'" data-action="set-filter" data-filter="milestone" data-value="">Any</div>';
        AppState.milestones.filter(m => m.status === 'active').forEach(m => {
            html += '<div class="filter-dropdown-item'+(AppState.filters.milestone === m.id ? ' selected' : '')+'" data-action="set-filter" data-filter="milestone" data-value="'+m.id+'">'+Components.escapeHtml(m.title)+'</div>';
        });
        html += '</div></div>';
        // Label filter
        html += '<div class="filter-dropdown-wrap">'
            + '<button class="btn btn-sm btn-outline filter-btn" data-action="toggle-filter-dropdown" data-filter="labels">Label'+(AppState.filters.labels.length > 0 ? ' ✓' : '')+'</button>'
            + '<div class="filter-dropdown" id="filter-labels" style="display:none">';
        AppState.labels.forEach(l => {
            const checked = AppState.filters.labels.includes(l.id);
            html += '<label class="filter-dropdown-item filter-checkbox"><input type="checkbox" data-action="toggle-label-filter" data-value="'+l.id+'"'+(checked ? ' checked' : '')+'> '+Components.labelBadge(l)+'</label>';
        });
        html += '</div></div>';
        // Sort
        html += '<div class="filter-dropdown-wrap">'
            + '<button class="btn btn-sm btn-outline filter-btn" data-action="toggle-filter-dropdown" data-filter="sort">Sort</button>'
            + '<div class="filter-dropdown" id="filter-sort" style="display:none">';
        ['createdAt','updatedAt','dueDate','title','weight'].forEach(f => {
            const label = { createdAt:'Created date', updatedAt:'Updated date', dueDate:'Due date', title:'Title', weight:'Weight' }[f];
            const active = AppState.issueSort.field === f;
            const dir = active ? AppState.issueSort.direction : 'desc';
            html += '<div class="filter-dropdown-item'+(active ? ' selected' : '')+'" data-action="set-sort" data-field="'+f+'" data-direction="'+(active && dir === 'desc' ? 'asc' : 'desc')+'">'+label+(active ? (dir === 'desc' ? ' ↓' : ' ↑') : '')+'</div>';
        });
        html += '</div></div>';
        html += '</div></div>';

        // Issue table
        if (paged.length === 0) {
            html += Components.emptyState('<svg width="48" height="48" viewBox="0 0 16 16"><circle cx="8" cy="8" r="7" fill="none" stroke="#ccc" stroke-width="1.5"/></svg>', 'No issues found', 'Try adjusting your filters or create a new issue.', '<button class="btn btn-primary" data-action="new-issue">New issue</button>');
        } else {
            html += '<div class="issue-table" data-testid="issue-list">';
            paged.forEach(issue => { html += this._renderIssueRow(issue); });
            html += '</div>';
            html += Components.pagination(page, total, pageSize);
        }
        return html;
    },

    _renderIssueRow(issue) {
        const assignees = issue.assignees.map(id => AppState.getUserById(id)).filter(Boolean);
        const milestone = issue.milestoneId ? AppState.getMilestoneById(issue.milestoneId) : null;
        const labels = issue.labels.map(id => AppState.getLabelById(id)).filter(Boolean);

        let html = '<div class="issue-row" data-issue-id="'+issue.id+'" data-testid="issue-row-'+issue.id+'">';
        html += '<div class="issue-row-left">';
        html += '<div class="issue-status-icon">' + (issue.status === 'open'
            ? '<svg width="16" height="16" viewBox="0 0 16 16" class="icon-open"><circle cx="8" cy="8" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
            : '<svg width="16" height="16" viewBox="0 0 16 16" class="icon-closed"><path d="M8 16A8 8 0 108 0a8 8 0 000 16zm3.78-9.72a.75.75 0 00-1.06-1.06L7 8.94 5.28 7.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.06 0l4.25-4.25z"/></svg>') + '</div>';
        html += '<div class="issue-row-content">';
        html += '<div class="issue-row-title">';
        if (issue.confidential) html += '<svg width="14" height="14" viewBox="0 0 16 16" class="icon-confidential" title="Confidential"><path fill="currentColor" d="M8 0a4 4 0 00-4 4v2H2v8h12V6h-2V4a4 4 0 00-4-4zm2 6H6V4a2 2 0 114 0v2z"/></svg> ';
        html += '<a class="issue-link" data-route="issues/'+issue.id+'" data-testid="issue-title-'+issue.id+'">'+Components.escapeHtml(issue.title)+'</a>';
        html += ' <span class="issue-ref">#'+issue.iid+'</span>';
        html += '</div>';
        html += '<div class="issue-row-meta">';
        if (labels.length > 0) { labels.slice(0, 4).forEach(l => { html += Components.labelBadge(l); }); if (labels.length > 4) html += '<span class="label-more">+' + (labels.length - 4) + '</span>'; }
        if (milestone) html += '<span class="issue-milestone" title="'+Components.escapeAttr(milestone.title)+'"><svg width="12" height="12" viewBox="0 0 16 16"><path d="M3 2v12M3 4h7l3 3-3 3H3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg> '+Components.escapeHtml(milestone.title)+'</span>';
        if (issue.dueDate) { const overdue = new Date(issue.dueDate) < new Date() && issue.status === 'open'; html += '<span class="issue-due'+(overdue ? ' overdue' : '')+'" title="Due date">'+Components.formatDateShort(issue.dueDate)+'</span>'; }
        if (issue.weight) html += '<span class="issue-weight" title="Weight">'+issue.weight+'</span>';
        html += '</div>';
        html += '</div></div>';
        html += '<div class="issue-row-right">';
        if (issue.healthStatus) html += Components.healthBadge(issue.healthStatus);
        if (assignees.length > 0) {
            html += '<div class="issue-assignees">';
            assignees.slice(0, 3).forEach(u => { html += Components.avatar(u, 24); });
            if (assignees.length > 3) html += '<span class="assignee-more">+' + (assignees.length - 3) + '</span>';
            html += '</div>';
        }
        html += '<span class="issue-updated" title="Updated '+Components.formatDateTime(issue.updatedAt)+'">'+Components.timeAgo(issue.updatedAt)+'</span>';
        html += '</div></div>';
        return html;
    },

    renderIssueDetail() {
        const issue = AppState.getIssueById(AppState.currentItemId);
        if (!issue) return Components.emptyState('', 'Issue not found', 'This issue may have been deleted.');
        const author = AppState.getUserById(issue.authorId);
        const assignees = issue.assignees.map(id => AppState.getUserById(id)).filter(Boolean);
        const labels = issue.labels.map(id => AppState.getLabelById(id)).filter(Boolean);
        const milestone = issue.milestoneId ? AppState.getMilestoneById(issue.milestoneId) : null;
        const iteration = issue.iterationId ? AppState.getIterationById(issue.iterationId) : null;
        const epic = issue.epicId ? AppState.getEpicById(issue.epicId) : null;
        const timelogs = AppState.timelogs.filter(t => t.issueId === issue.id);

        let html = '<div class="detail-page">';
        // Breadcrumb
        html += '<div class="breadcrumb"><a data-route="issues" class="breadcrumb-link">Issues</a> <span class="breadcrumb-sep">/</span> <span>#'+issue.iid+'</span></div>';
        // Header
        html += '<div class="detail-header">';
        html += '<div class="detail-title-row"><h1 class="detail-title">'+Components.escapeHtml(issue.title)+'</h1>';
        if (issue.confidential) html += '<span class="confidential-badge" title="Confidential"><svg width="16" height="16" viewBox="0 0 16 16"><path fill="currentColor" d="M8 0a4 4 0 00-4 4v2H2v8h12V6h-2V4a4 4 0 00-4-4zm2 6H6V4a2 2 0 114 0v2z"/></svg></span>';
        html += '</div>';
        html += '<div class="detail-actions">';
        html += '<button class="btn btn-outline" data-action="edit-issue" data-id="'+issue.id+'" data-testid="edit-issue-btn">Edit</button>';
        html += '<button class="btn '+(issue.status === 'open' ? 'btn-secondary' : 'btn-primary')+'" data-action="toggle-issue-status" data-id="'+issue.id+'" data-testid="toggle-status-btn">'+(issue.status === 'open' ? 'Close issue' : 'Reopen issue')+'</button>';
        html += '</div></div>';

        html += '<div class="detail-layout">';
        // Main content
        html += '<div class="detail-main">';
        html += '<div class="detail-description">';
        html += '<div class="detail-meta-line">'+Components.statusBadge(issue.status)+' &middot; Opened '+Components.timeAgo(issue.createdAt)+' by '+(author ? Components.escapeHtml(author.name) : 'Unknown')+'</div>';
        if (issue.description) {
            html += '<div class="description-body" data-testid="issue-description">'+Components.escapeHtml(issue.description).replace(/\n/g, '<br>')+'</div>';
        } else {
            html += '<div class="description-empty">No description provided.</div>';
        }
        // Time tracking section
        if (issue.timeEstimate > 0 || issue.timeSpent > 0 || timelogs.length > 0) {
            html += '<div class="detail-section"><h3>Time tracking</h3>';
            html += '<div class="time-tracking-summary">';
            html += '<div class="time-stat"><span class="time-label">Estimated</span><span class="time-value" data-testid="time-estimate">'+Components.formatDuration(issue.timeEstimate)+'</span></div>';
            html += '<div class="time-stat"><span class="time-label">Spent</span><span class="time-value" data-testid="time-spent">'+Components.formatDuration(issue.timeSpent)+'</span></div>';
            if (issue.timeEstimate > 0) {
                const remaining = Math.max(0, issue.timeEstimate - issue.timeSpent);
                html += '<div class="time-stat"><span class="time-label">Remaining</span><span class="time-value">'+Components.formatDuration(remaining)+'</span></div>';
            }
            html += '</div>';
            if (timelogs.length > 0) {
                html += '<div class="timelogs-list" data-testid="timelogs">';
                timelogs.forEach(tl => {
                    const user = AppState.getUserById(tl.userId);
                    html += '<div class="timelog-entry" data-testid="timelog-'+tl.id+'">'
                        + '<span class="timelog-user">'+(user ? Components.escapeHtml(user.name) : 'Unknown')+'</span>'
                        + '<span class="timelog-duration">'+Components.formatDuration(tl.timeSpent)+'</span>'
                        + '<span class="timelog-summary">'+Components.escapeHtml(tl.summary)+'</span>'
                        + '<span class="timelog-date">'+Components.formatDateShort(tl.spentAt)+'</span>'
                        + '<button class="timelog-delete" data-action="delete-timelog" data-id="'+tl.id+'" title="Delete">&times;</button>'
                        + '</div>';
                });
                html += '</div>';
            }
            html += '<button class="btn btn-sm btn-outline" data-action="add-timelog" data-issue-id="'+issue.id+'" data-testid="add-timelog-btn">Add time entry</button>';
            html += '</div>';
        }
        html += '</div>';

        // Sidebar
        html += '<div class="detail-sidebar">';
        // Assignees
        html += '<div class="sidebar-field" data-testid="sidebar-assignees"><div class="sidebar-field-label">Assignees <button class="sidebar-edit-btn" data-action="edit-assignees" data-id="'+issue.id+'">Edit</button></div>';
        if (assignees.length > 0) {
            assignees.forEach(u => { html += '<div class="sidebar-assignee">'+Components.avatar(u, 24)+'<span>'+Components.escapeHtml(u.name)+'</span></div>'; });
        } else { html += '<div class="sidebar-none">None</div>'; }
        html += '</div>';
        // Labels
        html += '<div class="sidebar-field" data-testid="sidebar-labels"><div class="sidebar-field-label">Labels <button class="sidebar-edit-btn" data-action="edit-labels" data-id="'+issue.id+'" data-type="issue">Edit</button></div>';
        if (labels.length > 0) {
            html += '<div class="sidebar-labels">';
            labels.forEach(l => { html += Components.labelBadge(l); });
            html += '</div>';
        } else { html += '<div class="sidebar-none">None</div>'; }
        html += '</div>';
        // Milestone
        html += '<div class="sidebar-field" data-testid="sidebar-milestone"><div class="sidebar-field-label">Milestone <button class="sidebar-edit-btn" data-action="edit-milestone" data-id="'+issue.id+'">Edit</button></div>';
        html += milestone ? '<a data-route="milestones/'+milestone.id+'" class="sidebar-link">'+Components.escapeHtml(milestone.title)+'</a>' : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Iteration
        html += '<div class="sidebar-field" data-testid="sidebar-iteration"><div class="sidebar-field-label">Iteration <button class="sidebar-edit-btn" data-action="edit-iteration" data-id="'+issue.id+'">Edit</button></div>';
        html += iteration ? '<a data-route="iterations/'+iteration.id+'" class="sidebar-link">'+Components.escapeHtml(iteration.title)+'</a>' : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Epic
        html += '<div class="sidebar-field" data-testid="sidebar-epic"><div class="sidebar-field-label">Epic <button class="sidebar-edit-btn" data-action="edit-epic-assignment" data-id="'+issue.id+'">Edit</button></div>';
        html += epic ? '<a data-route="epics/'+epic.id+'" class="sidebar-link">'+Components.escapeHtml(epic.title)+'</a>' : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Health status
        html += '<div class="sidebar-field" data-testid="sidebar-health"><div class="sidebar-field-label">Health status <button class="sidebar-edit-btn" data-action="edit-health" data-id="'+issue.id+'">Edit</button></div>';
        html += issue.healthStatus ? Components.healthBadge(issue.healthStatus) : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Due date
        html += '<div class="sidebar-field" data-testid="sidebar-due-date"><div class="sidebar-field-label">Due date <button class="sidebar-edit-btn" data-action="edit-due-date" data-id="'+issue.id+'">Edit</button></div>';
        html += issue.dueDate ? '<span>'+Components.formatDate(issue.dueDate)+'</span>' : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Weight
        html += '<div class="sidebar-field" data-testid="sidebar-weight"><div class="sidebar-field-label">Weight <button class="sidebar-edit-btn" data-action="edit-weight" data-id="'+issue.id+'">Edit</button></div>';
        html += issue.weight != null ? '<span data-testid="weight-value">'+issue.weight+'</span>' : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Confidential
        html += '<div class="sidebar-field" data-testid="sidebar-confidential"><div class="sidebar-field-label">Confidential</div>';
        html += '<span>'+(issue.confidential ? 'Yes' : 'No')+'</span>';
        html += '</div>';
        // Time tracking compact
        html += '<div class="sidebar-field" data-testid="sidebar-time"><div class="sidebar-field-label">Time tracking <button class="sidebar-edit-btn" data-action="edit-time-estimate" data-id="'+issue.id+'">Edit</button></div>';
        html += '<div class="sidebar-time">'+(issue.timeEstimate > 0 ? Components.formatDuration(issue.timeSpent)+' / '+Components.formatDuration(issue.timeEstimate) : (issue.timeSpent > 0 ? Components.formatDuration(issue.timeSpent)+' spent' : 'No estimate'))+'</div>';
        html += '</div>';

        html += '</div>'; // detail-sidebar
        html += '</div>'; // detail-layout
        html += '</div>'; // detail-page
        return html;
    },

    renderIssueForm(issueId) {
        const issue = issueId ? AppState.getIssueById(issueId) : null;
        const isEdit = !!issue;
        const title = isEdit ? 'Edit issue' : 'New issue';

        let html = '<div class="form-page">';
        html += '<div class="breadcrumb"><a data-route="issues" class="breadcrumb-link">Issues</a> <span class="breadcrumb-sep">/</span> <span>'+title+'</span></div>';
        html += '<h1>'+title+'</h1>';
        html += '<form class="entity-form" id="issueForm" data-testid="issue-form">';
        html += Components.textInput('issue-title', issue ? issue.title : '', 'Title', 'Title *');
        html += Components.textarea('issue-description', issue ? issue.description : '', 'Describe the issue...', 'Description');

        // Assignees as checkboxes
        html += '<div class="form-group"><label class="form-label">Assignees</label><div class="checkbox-grid" id="assignee-checkboxes">';
        AppState.users.forEach(u => {
            const checked = issue && issue.assignees.includes(u.id);
            html += '<label class="checkbox-item"><input type="checkbox" name="assignees" value="'+u.id+'"'+(checked ? ' checked' : '')+'> '+Components.escapeHtml(u.name)+'</label>';
        });
        html += '</div></div>';

        // Labels as checkboxes
        html += '<div class="form-group"><label class="form-label">Labels</label><div class="checkbox-grid" id="label-checkboxes">';
        AppState.labels.forEach(l => {
            const checked = issue && issue.labels.includes(l.id);
            html += '<label class="checkbox-item"><input type="checkbox" name="labels" value="'+l.id+'"'+(checked ? ' checked' : '')+'> '+Components.labelBadge(l)+'</label>';
        });
        html += '</div></div>';

        // Milestone dropdown
        const msOptions = AppState.milestones.filter(m => m.status === 'active').map(m => ({ value: m.id, label: m.title }));
        html += '<div class="form-group"><label class="form-label">Milestone</label>' + Components.dropdown('issue-milestone', msOptions, issue ? issue.milestoneId : null, 'Select milestone...') + '</div>';

        // Iteration dropdown
        const iterOptions = AppState.iterations.filter(i => i.status !== 'closed').map(i => ({ value: i.id, label: i.title }));
        html += '<div class="form-group"><label class="form-label">Iteration</label>' + Components.dropdown('issue-iteration', iterOptions, issue ? issue.iterationId : null, 'Select iteration...') + '</div>';

        // Epic dropdown
        const epicOptions = AppState.epics.filter(e => e.status === 'open').map(e => ({ value: e.id, label: e.title }));
        html += '<div class="form-group"><label class="form-label">Epic</label>' + Components.dropdown('issue-epic', epicOptions, issue ? issue.epicId : null, 'Select epic...') + '</div>';

        html += '<div class="form-row">';
        html += Components.dateInput('issue-start-date', issue ? issue.startDate : '', 'Start date');
        html += Components.dateInput('issue-due-date', issue ? issue.dueDate : '', 'Due date');
        html += '</div>';
        html += '<div class="form-row">';
        html += Components.numberInput('issue-weight', issue ? issue.weight : '', 'Weight', 0);
        html += '</div>';
        html += '<div class="form-group"><label class="checkbox-item"><input type="checkbox" id="issue-confidential"'+(issue && issue.confidential ? ' checked' : '')+'> This issue is confidential</label></div>';

        html += '<div class="form-actions">';
        html += '<button type="button" class="btn btn-primary" data-action="save-issue" data-testid="save-issue-btn">'+(isEdit ? 'Save changes' : 'Create issue')+'</button>';
        html += '<button type="button" class="btn btn-secondary" data-action="cancel-form" data-route="issues">Cancel</button>';
        html += '</div></form></div>';
        return html;
    },

    // ---- Epics ----
    renderEpicList() {
        const openEpics = AppState.epics.filter(e => e.status === 'open');
        const closedEpics = AppState.epics.filter(e => e.status === 'closed');

        let html = '<div class="page-header"><div class="page-header-left"><h1>Epics</h1></div>';
        html += '<div class="page-header-right"><button class="btn btn-primary" data-action="new-epic" data-testid="new-epic-btn">New epic</button></div></div>';

        html += '<div class="epic-section"><h2>Open <span class="count">'+openEpics.length+'</span></h2>';
        if (openEpics.length === 0) {
            html += '<p class="text-secondary">No open epics.</p>';
        } else {
            openEpics.forEach(epic => { html += this._renderEpicRow(epic); });
        }
        html += '</div>';

        html += '<div class="epic-section"><h2>Closed <span class="count">'+closedEpics.length+'</span></h2>';
        if (closedEpics.length === 0) {
            html += '<p class="text-secondary">No closed epics.</p>';
        } else {
            closedEpics.forEach(epic => { html += this._renderEpicRow(epic); });
        }
        html += '</div>';
        return html;
    },

    _renderEpicRow(epic) {
        const author = AppState.getUserById(epic.authorId);
        const labels = epic.labels.map(id => AppState.getLabelById(id)).filter(Boolean);
        const childIssues = AppState.getIssuesForEpic(epic.id);
        const closedIssues = childIssues.filter(i => i.status === 'closed').length;
        const childEpics = AppState.getChildEpics(epic.id);

        let html = '<div class="epic-row" data-epic-id="'+epic.id+'" data-testid="epic-row-'+epic.id+'">';
        html += '<div class="epic-row-left">';
        html += Components.statusBadge(epic.status);
        html += '<div class="epic-row-content">';
        html += '<a class="epic-link" data-route="epics/'+epic.id+'" data-testid="epic-title-'+epic.id+'">'+Components.escapeHtml(epic.title)+'</a>';
        html += ' <span class="epic-ref">&'+epic.iid+'</span>';
        if (epic.confidential) html += ' <svg width="14" height="14" viewBox="0 0 16 16" class="icon-confidential"><path fill="currentColor" d="M8 0a4 4 0 00-4 4v2H2v8h12V6h-2V4a4 4 0 00-4-4zm2 6H6V4a2 2 0 114 0v2z"/></svg>';
        html += '<div class="epic-row-meta">';
        labels.forEach(l => { html += Components.labelBadge(l); });
        if (epic.startDate || epic.dueDate) html += '<span class="epic-dates">'+Components.formatDateShort(epic.startDate)+' – '+Components.formatDateShort(epic.dueDate)+'</span>';
        html += '</div></div></div>';
        html += '<div class="epic-row-right">';
        if (epic.healthStatus) html += Components.healthBadge(epic.healthStatus);
        if (childIssues.length > 0) {
            html += '<div class="epic-progress">'+Components.progressBar(closedIssues, childIssues.length)+'</div>';
        }
        if (childEpics.length > 0) html += '<span class="epic-children" title="'+childEpics.length+' child epic(s)">'+childEpics.length+' child</span>';
        html += '</div></div>';
        return html;
    },

    renderEpicDetail() {
        const epic = AppState.getEpicById(AppState.currentItemId);
        if (!epic) return Components.emptyState('', 'Epic not found', 'This epic may have been deleted.');
        const author = AppState.getUserById(epic.authorId);
        const labels = epic.labels.map(id => AppState.getLabelById(id)).filter(Boolean);
        const childIssues = AppState.getIssuesForEpic(epic.id);
        const childEpics = AppState.getChildEpics(epic.id);
        const parentEpic = epic.parentEpicId ? AppState.getEpicById(epic.parentEpicId) : null;
        const closedIssues = childIssues.filter(i => i.status === 'closed').length;

        let html = '<div class="detail-page">';
        html += '<div class="breadcrumb"><a data-route="epics" class="breadcrumb-link">Epics</a> <span class="breadcrumb-sep">/</span> <span>&'+epic.iid+'</span></div>';
        html += '<div class="detail-header"><div class="detail-title-row"><h1 class="detail-title">'+Components.escapeHtml(epic.title)+'</h1></div>';
        html += '<div class="detail-actions">';
        html += '<button class="btn btn-outline" data-action="edit-epic" data-id="'+epic.id+'" data-testid="edit-epic-btn">Edit</button>';
        html += '<button class="btn '+(epic.status === 'open' ? 'btn-secondary' : 'btn-primary')+'" data-action="toggle-epic-status" data-id="'+epic.id+'" data-testid="toggle-epic-status-btn">'+(epic.status === 'open' ? 'Close epic' : 'Reopen epic')+'</button>';
        html += '</div></div>';

        html += '<div class="detail-layout"><div class="detail-main">';
        html += '<div class="detail-meta-line">'+Components.statusBadge(epic.status)+' &middot; Opened '+Components.timeAgo(epic.createdAt)+' by '+(author ? Components.escapeHtml(author.name) : 'Unknown')+'</div>';
        if (epic.description) {
            html += '<div class="description-body" data-testid="epic-description">'+Components.escapeHtml(epic.description).replace(/\n/g, '<br>')+'</div>';
        }

        // Child epics
        if (childEpics.length > 0) {
            html += '<div class="detail-section"><h3>Child epics <span class="count">'+childEpics.length+'</span></h3>';
            childEpics.forEach(ce => { html += this._renderEpicRow(ce); });
            html += '</div>';
        }

        // Child issues
        html += '<div class="detail-section"><h3>Issues <span class="count">'+childIssues.length+'</span></h3>';
        if (childIssues.length > 0) {
            html += '<div class="detail-progress-bar">'+Components.progressBar(closedIssues, childIssues.length)+'</div>';
            html += '<div class="issue-table">';
            childIssues.forEach(issue => { html += this._renderIssueRow(issue); });
            html += '</div>';
        } else {
            html += '<p class="text-secondary">No issues assigned to this epic.</p>';
        }
        html += '</div>';

        html += '</div><div class="detail-sidebar">';
        // Parent epic
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Parent epic</div>';
        html += parentEpic ? '<a data-route="epics/'+parentEpic.id+'" class="sidebar-link">'+Components.escapeHtml(parentEpic.title)+'</a>' : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Labels
        html += '<div class="sidebar-field" data-testid="epic-sidebar-labels"><div class="sidebar-field-label">Labels <button class="sidebar-edit-btn" data-action="edit-labels" data-id="'+epic.id+'" data-type="epic">Edit</button></div>';
        if (labels.length > 0) { html += '<div class="sidebar-labels">'; labels.forEach(l => { html += Components.labelBadge(l); }); html += '</div>'; }
        else { html += '<div class="sidebar-none">None</div>'; }
        html += '</div>';
        // Health
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Health status</div>';
        html += epic.healthStatus ? Components.healthBadge(epic.healthStatus) : '<div class="sidebar-none">None</div>';
        html += '</div>';
        // Dates
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Start date</div><span>'+Components.formatDate(epic.startDate)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Due date</div><span>'+Components.formatDate(epic.dueDate)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Confidential</div><span>'+(epic.confidential ? 'Yes' : 'No')+'</span></div>';

        html += '</div></div></div>';
        return html;
    },

    renderEpicForm(epicId) {
        const epic = epicId ? AppState.getEpicById(epicId) : null;
        const isEdit = !!epic;

        let html = '<div class="form-page">';
        html += '<div class="breadcrumb"><a data-route="epics" class="breadcrumb-link">Epics</a> <span class="breadcrumb-sep">/</span> <span>'+(isEdit ? 'Edit' : 'New epic')+'</span></div>';
        html += '<h1>'+(isEdit ? 'Edit epic' : 'New epic')+'</h1>';
        html += '<form class="entity-form" id="epicForm" data-testid="epic-form">';
        html += Components.textInput('epic-title', epic ? epic.title : '', 'Title', 'Title *');
        html += Components.textarea('epic-description', epic ? epic.description : '', 'Describe the epic...', 'Description');
        // Labels
        html += '<div class="form-group"><label class="form-label">Labels</label><div class="checkbox-grid">';
        AppState.labels.filter(l => l.type === 'group').forEach(l => {
            const checked = epic && epic.labels.includes(l.id);
            html += '<label class="checkbox-item"><input type="checkbox" name="epic-labels" value="'+l.id+'"'+(checked ? ' checked' : '')+'> '+Components.labelBadge(l)+'</label>';
        });
        html += '</div></div>';
        // Parent epic
        const parentOptions = AppState.epics.filter(e => e.id !== epicId && e.status === 'open').map(e => ({ value: e.id, label: e.title }));
        html += '<div class="form-group"><label class="form-label">Parent epic</label>' + Components.dropdown('epic-parent', parentOptions, epic ? epic.parentEpicId : null, 'None') + '</div>';
        html += '<div class="form-row">';
        html += Components.dateInput('epic-start-date', epic ? epic.startDate : '', 'Start date');
        html += Components.dateInput('epic-due-date', epic ? epic.dueDate : '', 'Due date');
        html += '</div>';
        html += '<div class="form-group"><label class="checkbox-item"><input type="checkbox" id="epic-confidential"'+(epic && epic.confidential ? ' checked' : '')+'> Confidential epic</label></div>';
        html += '<div class="form-actions">';
        html += '<button type="button" class="btn btn-primary" data-action="save-epic" data-testid="save-epic-btn">'+(isEdit ? 'Save changes' : 'Create epic')+'</button>';
        html += '<button type="button" class="btn btn-secondary" data-action="cancel-form" data-route="epics">Cancel</button>';
        html += '</div></form></div>';
        return html;
    },

    // ---- Milestones ----
    renderMilestoneList() {
        const active = AppState.milestones.filter(m => m.status === 'active');
        const closed = AppState.milestones.filter(m => m.status === 'closed');

        let html = '<div class="page-header"><div class="page-header-left"><h1>Milestones</h1></div>';
        html += '<div class="page-header-right"><button class="btn btn-primary" data-action="new-milestone" data-testid="new-milestone-btn">New milestone</button></div></div>';

        html += '<div class="milestone-section"><h2>Active <span class="count">'+active.length+'</span></h2>';
        active.forEach(ms => { html += this._renderMilestoneRow(ms); });
        if (active.length === 0) html += '<p class="text-secondary">No active milestones.</p>';
        html += '</div>';

        html += '<div class="milestone-section"><h2>Closed <span class="count">'+closed.length+'</span></h2>';
        closed.forEach(ms => { html += this._renderMilestoneRow(ms); });
        if (closed.length === 0) html += '<p class="text-secondary">No closed milestones.</p>';
        html += '</div>';
        return html;
    },

    _renderMilestoneRow(ms) {
        const issues = AppState.getIssuesForMilestone(ms.id);
        const closed = issues.filter(i => i.status === 'closed').length;
        const total = issues.length;

        let html = '<div class="milestone-row" data-testid="milestone-row-'+ms.id+'">';
        html += '<div class="milestone-row-left">';
        html += '<a class="milestone-link" data-route="milestones/'+ms.id+'" data-testid="milestone-title-'+ms.id+'">'+Components.escapeHtml(ms.title)+'</a>';
        if (ms.startDate || ms.dueDate) html += '<span class="milestone-dates">'+Components.formatDateShort(ms.startDate)+' – '+Components.formatDateShort(ms.dueDate)+'</span>';
        html += '</div>';
        html += '<div class="milestone-row-right">';
        html += '<div class="milestone-progress">'+Components.progressBar(closed, total)+'</div>';
        html += '<span class="milestone-issue-count">'+total+' issues</span>';
        html += '</div></div>';
        return html;
    },

    renderMilestoneDetail() {
        const ms = AppState.getMilestoneById(AppState.currentItemId);
        if (!ms) return Components.emptyState('', 'Milestone not found', '');
        const issues = AppState.getIssuesForMilestone(ms.id);
        const open = issues.filter(i => i.status === 'open');
        const closed = issues.filter(i => i.status === 'closed');
        const totalWeight = issues.reduce((s, i) => s + (i.weight || 0), 0);
        const closedWeight = closed.reduce((s, i) => s + (i.weight || 0), 0);
        const totalTime = issues.reduce((s, i) => s + (i.timeSpent || 0), 0);

        let html = '<div class="detail-page">';
        html += '<div class="breadcrumb"><a data-route="milestones" class="breadcrumb-link">Milestones</a> <span class="breadcrumb-sep">/</span> <span>'+Components.escapeHtml(ms.title)+'</span></div>';
        html += '<div class="detail-header"><div class="detail-title-row"><h1 class="detail-title">'+Components.escapeHtml(ms.title)+'</h1></div>';
        html += '<div class="detail-actions">';
        html += '<button class="btn btn-outline" data-action="edit-milestone" data-id="'+ms.id+'" data-testid="edit-milestone-btn">Edit</button>';
        html += '<button class="btn '+(ms.status === 'active' ? 'btn-secondary' : 'btn-primary')+'" data-action="toggle-milestone-status" data-id="'+ms.id+'" data-testid="toggle-ms-status-btn">'+(ms.status === 'active' ? 'Close' : 'Reopen')+'</button>';
        html += '</div></div>';

        html += '<div class="detail-layout"><div class="detail-main">';
        if (ms.description) html += '<div class="description-body">'+Components.escapeHtml(ms.description).replace(/\n/g,'<br>')+'</div>';
        // Stats
        html += '<div class="milestone-stats">';
        html += '<div class="stat-card"><span class="stat-value" data-testid="ms-open-count">'+open.length+'</span><span class="stat-label">Open</span></div>';
        html += '<div class="stat-card"><span class="stat-value" data-testid="ms-closed-count">'+closed.length+'</span><span class="stat-label">Closed</span></div>';
        html += '<div class="stat-card"><span class="stat-value">'+totalWeight+'</span><span class="stat-label">Total weight</span></div>';
        html += '<div class="stat-card"><span class="stat-value">'+Components.formatDuration(totalTime)+'</span><span class="stat-label">Time spent</span></div>';
        html += '</div>';
        html += '<div class="detail-progress-bar">'+Components.progressBar(closed.length, issues.length)+'</div>';

        // Issues list
        html += '<div class="detail-section"><h3>Issues</h3>';
        if (open.length > 0) { html += '<h4 class="sub-heading">Open</h4><div class="issue-table">'; open.forEach(i => { html += this._renderIssueRow(i); }); html += '</div>'; }
        if (closed.length > 0) { html += '<h4 class="sub-heading">Closed</h4><div class="issue-table">'; closed.forEach(i => { html += this._renderIssueRow(i); }); html += '</div>'; }
        if (issues.length === 0) html += '<p class="text-secondary">No issues in this milestone.</p>';
        html += '</div>';

        html += '</div><div class="detail-sidebar">';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Status</div><span class="status-badge status-'+ms.status+'">'+ms.status.charAt(0).toUpperCase()+ms.status.slice(1)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Start date</div><span>'+Components.formatDate(ms.startDate)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Due date</div><span>'+Components.formatDate(ms.dueDate)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Completion</div>'+Components.progressBar(closed.length, issues.length)+'</div>';
        html += '</div></div></div>';
        return html;
    },

    renderMilestoneForm(msId) {
        const ms = msId ? AppState.getMilestoneById(msId) : null;
        const isEdit = !!ms;
        let html = '<div class="form-page">';
        html += '<div class="breadcrumb"><a data-route="milestones" class="breadcrumb-link">Milestones</a> <span class="breadcrumb-sep">/</span> <span>'+(isEdit ? 'Edit' : 'New milestone')+'</span></div>';
        html += '<h1>'+(isEdit ? 'Edit milestone' : 'New milestone')+'</h1>';
        html += '<form class="entity-form" id="milestoneForm" data-testid="milestone-form">';
        html += Components.textInput('ms-title', ms ? ms.title : '', 'Title', 'Title *');
        html += Components.textarea('ms-description', ms ? ms.description : '', 'Describe the milestone...', 'Description');
        html += '<div class="form-row">';
        html += Components.dateInput('ms-start-date', ms ? ms.startDate : '', 'Start date');
        html += Components.dateInput('ms-due-date', ms ? ms.dueDate : '', 'Due date');
        html += '</div>';
        html += '<div class="form-actions">';
        html += '<button type="button" class="btn btn-primary" data-action="save-milestone" data-testid="save-milestone-btn">'+(isEdit ? 'Save changes' : 'Create milestone')+'</button>';
        html += '<button type="button" class="btn btn-secondary" data-action="cancel-form" data-route="milestones">Cancel</button>';
        html += '</div></form></div>';
        return html;
    },

    // ---- Iterations ----
    renderIterationList() {
        let html = '<div class="page-header"><div class="page-header-left"><h1>Iterations</h1></div>';
        html += '<div class="page-header-right"><button class="btn btn-primary" data-action="new-cadence" data-testid="new-cadence-btn">New cadence</button></div></div>';

        AppState.iterationCadences.forEach(cad => {
            const iters = AppState.iterations.filter(i => i.cadenceId === cad.id);
            const current = iters.filter(i => i.status === 'current');
            const upcoming = iters.filter(i => i.status === 'upcoming');
            const closed = iters.filter(i => i.status === 'closed');

            html += '<div class="cadence-section" data-testid="cadence-'+cad.id+'">';
            html += '<div class="cadence-header">';
            html += '<div class="cadence-header-left"><h2>'+Components.escapeHtml(cad.title)+'</h2>';
            if (cad.automatic) html += '<span class="cadence-badge auto">Automatic</span>';
            if (cad.rollOver) html += '<span class="cadence-badge rollover">Roll over</span>';
            html += '<span class="cadence-info">'+(cad.durationWeeks ? cad.durationWeeks+'-week' : 'Manual')+' cadence</span>';
            html += '</div>';
            html += '<div class="cadence-header-right">';
            html += '<button class="btn btn-sm btn-outline" data-action="edit-cadence" data-id="'+cad.id+'" data-testid="edit-cadence-'+cad.id+'">Edit</button>';
            if (!cad.automatic) html += '<button class="btn btn-sm btn-outline" data-action="new-iteration" data-cadence-id="'+cad.id+'" data-testid="new-iter-'+cad.id+'">Add iteration</button>';
            html += '</div></div>';

            if (cad.description) html += '<p class="cadence-desc">'+Components.escapeHtml(cad.description)+'</p>';

            if (current.length > 0) { html += '<h4 class="sub-heading">Current</h4>'; current.forEach(i => { html += this._renderIterationRow(i); }); }
            if (upcoming.length > 0) { html += '<h4 class="sub-heading">Upcoming</h4>'; upcoming.forEach(i => { html += this._renderIterationRow(i); }); }
            if (closed.length > 0) { html += '<h4 class="sub-heading">Completed</h4>'; closed.forEach(i => { html += this._renderIterationRow(i); }); }
            html += '</div>';
        });
        return html;
    },

    _renderIterationRow(iter) {
        const issues = AppState.getIssuesForIteration(iter.id);
        const closed = issues.filter(i => i.status === 'closed').length;
        const statusCls = { current: 'iter-current', upcoming: 'iter-upcoming', closed: 'iter-closed' }[iter.status] || '';

        let html = '<div class="iteration-row '+statusCls+'" data-testid="iteration-row-'+iter.id+'">';
        html += '<div class="iteration-row-left">';
        html += '<a class="iteration-link" data-route="iterations/'+iter.id+'" data-testid="iteration-title-'+iter.id+'">'+Components.escapeHtml(iter.title)+'</a>';
        html += '<span class="iteration-dates">'+Components.formatDateShort(iter.startDate)+' – '+Components.formatDateShort(iter.dueDate)+'</span>';
        html += '<span class="iteration-status-badge '+statusCls+'">'+iter.status.charAt(0).toUpperCase()+iter.status.slice(1)+'</span>';
        html += '</div>';
        html += '<div class="iteration-row-right">';
        html += '<div class="iteration-progress">'+Components.progressBar(closed, issues.length)+'</div>';
        html += '<span class="iteration-issue-count">'+issues.length+' issues</span>';
        html += '</div></div>';
        return html;
    },

    renderIterationDetail() {
        const iter = AppState.getIterationById(AppState.currentItemId);
        if (!iter) return Components.emptyState('', 'Iteration not found', '');
        const cadence = AppState.getCadenceById(iter.cadenceId);
        const issues = AppState.getIssuesForIteration(iter.id);
        const open = issues.filter(i => i.status === 'open');
        const closed = issues.filter(i => i.status === 'closed');
        const totalWeight = issues.reduce((s, i) => s + (i.weight || 0), 0);
        const closedWeight = closed.reduce((s, i) => s + (i.weight || 0), 0);

        let html = '<div class="detail-page">';
        html += '<div class="breadcrumb"><a data-route="iterations" class="breadcrumb-link">Iterations</a> <span class="breadcrumb-sep">/</span> <span>'+Components.escapeHtml(iter.title)+'</span></div>';
        html += '<div class="detail-header"><div class="detail-title-row"><h1 class="detail-title">'+Components.escapeHtml(iter.title)+'</h1>';
        html += '<span class="iteration-status-badge iter-'+iter.status+'">'+iter.status.charAt(0).toUpperCase()+iter.status.slice(1)+'</span>';
        html += '</div></div>';

        html += '<div class="detail-layout"><div class="detail-main">';
        if (cadence) html += '<div class="detail-meta-line">Cadence: <strong>'+Components.escapeHtml(cadence.title)+'</strong></div>';
        html += '<div class="milestone-stats">';
        html += '<div class="stat-card"><span class="stat-value" data-testid="iter-open-count">'+open.length+'</span><span class="stat-label">Open</span></div>';
        html += '<div class="stat-card"><span class="stat-value" data-testid="iter-closed-count">'+closed.length+'</span><span class="stat-label">Closed</span></div>';
        html += '<div class="stat-card"><span class="stat-value">'+totalWeight+'</span><span class="stat-label">Total weight</span></div>';
        html += '<div class="stat-card"><span class="stat-value">'+closedWeight+'</span><span class="stat-label">Closed weight</span></div>';
        html += '</div>';
        html += '<div class="detail-progress-bar">'+Components.progressBar(closed.length, issues.length)+'</div>';

        html += '<div class="detail-section"><h3>Issues</h3>';
        if (open.length > 0) { html += '<h4 class="sub-heading">Open</h4><div class="issue-table">'; open.forEach(i => { html += this._renderIssueRow(i); }); html += '</div>'; }
        if (closed.length > 0) { html += '<h4 class="sub-heading">Closed</h4><div class="issue-table">'; closed.forEach(i => { html += this._renderIssueRow(i); }); html += '</div>'; }
        if (issues.length === 0) html += '<p class="text-secondary">No issues in this iteration.</p>';
        html += '</div>';

        html += '</div><div class="detail-sidebar">';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Status</div><span class="iteration-status-badge iter-'+iter.status+'">'+iter.status+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Start date</div><span>'+Components.formatDate(iter.startDate)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Due date</div><span>'+Components.formatDate(iter.dueDate)+'</span></div>';
        html += '<div class="sidebar-field"><div class="sidebar-field-label">Completion</div>'+Components.progressBar(closed.length, issues.length)+'</div>';
        html += '</div></div></div>';
        return html;
    },

    renderCadenceForm(cadId) {
        const cad = cadId ? AppState.getCadenceById(cadId) : null;
        const isEdit = !!cad;
        let html = '<div class="form-page">';
        html += '<div class="breadcrumb"><a data-route="iterations" class="breadcrumb-link">Iterations</a> <span class="breadcrumb-sep">/</span> <span>'+(isEdit ? 'Edit cadence' : 'New cadence')+'</span></div>';
        html += '<h1>'+(isEdit ? 'Edit cadence' : 'New iteration cadence')+'</h1>';
        html += '<form class="entity-form" id="cadenceForm" data-testid="cadence-form">';
        html += Components.textInput('cad-title', cad ? cad.title : '', 'Title', 'Title *');
        html += Components.textarea('cad-description', cad ? cad.description : '', 'Describe the cadence...', 'Description');
        html += '<div class="form-group"><label class="checkbox-item"><input type="checkbox" id="cad-automatic"'+(cad && cad.automatic ? ' checked' : '')+'> Enable automatic scheduling</label></div>';
        html += '<div class="form-row">';
        html += Components.dateInput('cad-start-date', cad ? cad.startDate : '', 'Start date');
        html += Components.numberInput('cad-duration', cad ? cad.durationWeeks : '', 'Duration (weeks)', 1, 52);
        html += '</div>';
        html += '<div class="form-row">';
        html += Components.numberInput('cad-upcoming', cad ? cad.upcomingIterations : '', 'Upcoming iterations', 1, 10);
        html += '</div>';
        html += '<div class="form-group"><label class="checkbox-item"><input type="checkbox" id="cad-rollover"'+(cad && cad.rollOver ? ' checked' : '')+'> Roll over incomplete issues to next iteration</label></div>';
        html += '<div class="form-actions">';
        html += '<button type="button" class="btn btn-primary" data-action="save-cadence" data-testid="save-cadence-btn">'+(isEdit ? 'Save changes' : 'Create cadence')+'</button>';
        html += '<button type="button" class="btn btn-secondary" data-action="cancel-form" data-route="iterations">Cancel</button>';
        html += '</div></form></div>';
        return html;
    },

    renderIterationForm() {
        let html = '<div class="form-page">';
        html += '<div class="breadcrumb"><a data-route="iterations" class="breadcrumb-link">Iterations</a> <span class="breadcrumb-sep">/</span> <span>New iteration</span></div>';
        html += '<h1>New iteration</h1>';
        html += '<form class="entity-form" id="iterationForm" data-testid="iteration-form">';
        html += Components.textInput('iter-title', '', 'Title', 'Title *');
        const cadOptions = AppState.iterationCadences.filter(c => !c.automatic).map(c => ({ value: c.id, label: c.title }));
        html += '<div class="form-group"><label class="form-label">Cadence</label>'+Components.dropdown('iter-cadence', cadOptions, AppState._tempCadenceId || null, 'Select cadence...')+'</div>';
        html += '<div class="form-row">';
        html += Components.dateInput('iter-start-date', '', 'Start date *');
        html += Components.dateInput('iter-due-date', '', 'Due date *');
        html += '</div>';
        html += '<div class="form-actions">';
        html += '<button type="button" class="btn btn-primary" data-action="save-iteration" data-testid="save-iteration-btn">Create iteration</button>';
        html += '<button type="button" class="btn btn-secondary" data-action="cancel-form" data-route="iterations">Cancel</button>';
        html += '</div></form></div>';
        return html;
    },

    // ---- Labels ----
    renderLabelList() {
        const grouped = {};
        AppState.labels.forEach(l => {
            const scope = l.scoped ? l.title.split('::')[0] : '_unscoped';
            if (!grouped[scope]) grouped[scope] = [];
            grouped[scope].push(l);
        });

        let html = '<div class="page-header"><div class="page-header-left"><h1>Labels</h1></div>';
        html += '<div class="page-header-right"><button class="btn btn-primary" data-action="new-label" data-testid="new-label-btn">New label</button></div></div>';

        // Scoped labels first
        Object.keys(grouped).sort().forEach(scope => {
            if (scope === '_unscoped') return;
            html += '<div class="label-group"><h3 class="label-group-title">'+Components.escapeHtml(scope)+'::</h3>';
            grouped[scope].forEach(l => { html += this._renderLabelRow(l); });
            html += '</div>';
        });

        // Unscoped
        if (grouped._unscoped) {
            html += '<div class="label-group"><h3 class="label-group-title">Other labels</h3>';
            grouped._unscoped.forEach(l => { html += this._renderLabelRow(l); });
            html += '</div>';
        }
        return html;
    },

    _renderLabelRow(label) {
        const issueCount = AppState.getIssuesForLabel(label.id).length;
        let html = '<div class="label-row" data-testid="label-row-'+label.id+'">';
        html += '<div class="label-row-left">'+Components.labelBadge(label);
        if (label.description) html += '<span class="label-row-desc">'+Components.escapeHtml(label.description)+'</span>';
        html += '</div>';
        html += '<div class="label-row-right">';
        html += '<span class="label-issue-count">'+issueCount+' issues</span>';
        html += '<span class="label-type-badge">'+label.type+'</span>';
        html += '<button class="btn btn-sm btn-outline" data-action="edit-label" data-id="'+label.id+'" data-testid="edit-label-'+label.id+'">Edit</button>';
        html += '<button class="btn btn-sm btn-danger-outline" data-action="delete-label" data-id="'+label.id+'" data-testid="delete-label-'+label.id+'">Delete</button>';
        html += '</div></div>';
        return html;
    },

    renderLabelForm(labelId) {
        const label = labelId ? AppState.getLabelById(labelId) : null;
        const isEdit = !!label;
        let html = '<div class="form-page">';
        html += '<div class="breadcrumb"><a data-route="labels" class="breadcrumb-link">Labels</a> <span class="breadcrumb-sep">/</span> <span>'+(isEdit ? 'Edit' : 'New label')+'</span></div>';
        html += '<h1>'+(isEdit ? 'Edit label' : 'New label')+'</h1>';
        html += '<form class="entity-form" id="labelForm" data-testid="label-form">';
        html += Components.textInput('label-title', label ? label.title : '', 'Title (use :: for scoped labels)', 'Title *');
        html += Components.textarea('label-description', label ? label.description : '', 'Describe the label...', 'Description', 2);
        // Type dropdown
        html += '<div class="form-group"><label class="form-label">Type</label>';
        html += Components.dropdown('label-type', [{value:'project',label:'Project'},{value:'group',label:'Group'}], label ? label.type : 'project', 'Select type');
        html += '</div>';
        // Color picker
        html += '<div class="form-group"><label class="form-label">Color</label>';
        html += '<div class="color-picker" id="colorPicker">';
        Components.labelColors.forEach(c => {
            html += Components.colorSwatch(c, label && label.color === c);
        });
        html += '</div>';
        html += '<div class="color-preview" id="colorPreview" style="margin-top:8px">';
        html += Components.labelBadge({ id: 'preview', title: label ? label.title : 'Preview', color: label ? label.color : '#6c757d', textColor: label ? label.textColor : '#fff', scoped: label ? label.scoped : false });
        html += '</div></div>';
        html += '<div class="form-actions">';
        html += '<button type="button" class="btn btn-primary" data-action="save-label" data-testid="save-label-btn">'+(isEdit ? 'Save changes' : 'Create label')+'</button>';
        html += '<button type="button" class="btn btn-secondary" data-action="cancel-form" data-route="labels">Cancel</button>';
        html += '</div></form></div>';
        return html;
    },

    // ---- Boards ----
    renderBoardView() {
        const board = AppState.getBoardById(AppState.currentBoardId);
        if (!board && AppState.boards.length > 0) {
            AppState.currentBoardId = AppState.boards[0].id;
            return this.renderBoardView();
        }

        let html = '<div class="page-header"><div class="page-header-left"><h1>Boards</h1>';
        // Board selector
        html += '<div class="board-selector">';
        AppState.boards.forEach(b => {
            html += '<button class="board-tab'+(b.id === AppState.currentBoardId ? ' active' : '')+'" data-action="switch-board" data-id="'+b.id+'" data-testid="board-tab-'+b.id+'">'+Components.escapeHtml(b.name)+'</button>';
        });
        html += '</div></div></div>';

        if (!board) {
            html += Components.emptyState('', 'No boards', 'Create a board to get started.');
            return html;
        }

        const boardIssues = AppState.getIssuesForBoard(board.id);

        html += '<div class="board-container" data-testid="board-'+board.id+'">';
        // Open (backlog) list
        html += this._renderBoardList('_open', 'Open', boardIssues._open || [], board.id);
        // Label/milestone lists
        board.lists.forEach(list => {
            let title = '';
            if (list.type === 'label') {
                const l = AppState.getLabelById(list.labelId);
                title = l ? l.title : 'Unknown';
            } else if (list.type === 'milestone') {
                const m = AppState.getMilestoneById(list.milestoneId);
                title = m ? m.title : 'Unknown';
            }
            html += this._renderBoardList(list.id, title, boardIssues[list.id] || [], board.id);
        });
        // Closed list
        html += this._renderBoardList('_closed', 'Closed', boardIssues._closed || [], board.id);
        html += '</div>';
        return html;
    },

    _renderBoardList(listId, title, issues, boardId) {
        let html = '<div class="board-list" data-list-id="'+listId+'" data-board-id="'+boardId+'" data-testid="board-list-'+listId+'">';
        html += '<div class="board-list-header"><span class="board-list-title">'+Components.escapeHtml(title)+'</span><span class="board-list-count">'+issues.length+'</span></div>';
        html += '<div class="board-list-body" data-list-id="'+listId+'">';
        issues.slice(0, 20).forEach(issue => {
            const labels = issue.labels.map(id => AppState.getLabelById(id)).filter(Boolean);
            const assignees = issue.assignees.map(id => AppState.getUserById(id)).filter(Boolean);
            html += '<div class="board-card" draggable="true" data-issue-id="'+issue.id+'" data-list-id="'+listId+'" data-testid="board-card-'+issue.id+'">';
            html += '<div class="board-card-title"><a data-route="issues/'+issue.id+'">'+Components.escapeHtml(issue.title)+'</a> <span class="issue-ref">#'+issue.iid+'</span></div>';
            if (labels.length > 0) { html += '<div class="board-card-labels">'; labels.slice(0, 3).forEach(l => { html += Components.labelBadge(l); }); html += '</div>'; }
            html += '<div class="board-card-footer">';
            if (assignees.length > 0) { html += '<div class="board-card-assignees">'; assignees.slice(0, 2).forEach(u => { html += Components.avatar(u, 20); }); html += '</div>'; }
            if (issue.dueDate) html += '<span class="board-card-due">'+Components.formatDateShort(issue.dueDate)+'</span>';
            if (issue.weight) html += '<span class="board-card-weight">'+issue.weight+'</span>';
            html += '</div></div>';
        });
        if (issues.length > 20) html += '<div class="board-list-more">+'+(issues.length - 20)+' more</div>';
        html += '</div></div>';
        return html;
    },

    // ---- Todos ----
    renderTodoList() {
        const tab = AppState.todoTab;
        const todos = AppState.getTodos(tab);
        const pendingCount = AppState.todos.filter(t => t.status === 'pending').length;
        const snoozedCount = AppState.todos.filter(t => t.status === 'snoozed').length;
        const doneCount = AppState.todos.filter(t => t.status === 'done').length;

        let html = '<div class="page-header"><div class="page-header-left"><h1>To-Do List</h1></div>';
        if (tab === 'pending' && pendingCount > 0) html += '<div class="page-header-right"><button class="btn btn-outline" data-action="mark-all-todos-done" data-testid="mark-all-done-btn">Mark all as done</button></div>';
        html += '</div>';

        html += '<div class="todo-tabs">';
        html += '<button class="todo-tab'+(tab === 'pending' ? ' active' : '')+'" data-action="switch-todo-tab" data-tab="pending" data-testid="todo-tab-pending">To Do <span class="count">'+pendingCount+'</span></button>';
        html += '<button class="todo-tab'+(tab === 'snoozed' ? ' active' : '')+'" data-action="switch-todo-tab" data-tab="snoozed" data-testid="todo-tab-snoozed">Snoozed <span class="count">'+snoozedCount+'</span></button>';
        html += '<button class="todo-tab'+(tab === 'done' ? ' active' : '')+'" data-action="switch-todo-tab" data-tab="done" data-testid="todo-tab-done">Done <span class="count">'+doneCount+'</span></button>';
        html += '</div>';

        if (todos.length === 0) {
            const msg = tab === 'pending' ? 'You\'re all caught up!' : (tab === 'snoozed' ? 'No snoozed items.' : 'No completed items.');
            html += Components.emptyState('<svg width="48" height="48" viewBox="0 0 16 16"><path d="M3 8l3 3 7-7" fill="none" stroke="#ccc" stroke-width="2" stroke-linecap="round"/></svg>', msg, '');
        } else {
            html += '<div class="todo-list" data-testid="todo-list">';
            todos.forEach(todo => { html += this._renderTodoRow(todo); });
            html += '</div>';
        }
        return html;
    },

    _renderTodoRow(todo) {
        let targetTitle = '';
        let targetRoute = '';
        if (todo.targetType === 'issue') {
            const issue = AppState.getIssueById(todo.targetId);
            targetTitle = issue ? issue.title + ' #' + issue.iid : 'Unknown issue';
            targetRoute = 'issues/' + todo.targetId;
        } else if (todo.targetType === 'epic') {
            const epic = AppState.getEpicById(todo.targetId);
            targetTitle = epic ? epic.title + ' &' + epic.iid : 'Unknown epic';
            targetRoute = 'epics/' + todo.targetId;
        }
        const author = AppState.getUserById(todo.authorId);
        const actionText = { assigned: 'assigned', mentioned: 'mentioned you on', review_requested: 'requested review on' }[todo.action] || todo.action;

        let html = '<div class="todo-row" data-testid="todo-row-'+todo.id+'">';
        html += '<div class="todo-row-left">';
        html += Components.avatar(author, 32);
        html += '<div class="todo-row-content">';
        html += '<div class="todo-row-text">'+(author ? '<strong>'+Components.escapeHtml(author.name)+'</strong>' : 'Someone')+' '+actionText+'</div>';
        html += '<a class="todo-target" data-route="'+Components.escapeAttr(targetRoute)+'">'+Components.escapeHtml(targetTitle)+'</a>';
        html += '<span class="todo-time">'+Components.timeAgo(todo.createdAt)+'</span>';
        if (todo.snoozedUntil) html += '<span class="todo-snooze-info">Snoozed until '+Components.formatDateTime(todo.snoozedUntil)+'</span>';
        html += '</div></div>';
        html += '<div class="todo-row-right">';
        if (todo.status === 'pending') {
            html += '<button class="btn btn-sm btn-outline" data-action="snooze-todo" data-id="'+todo.id+'" data-testid="snooze-todo-'+todo.id+'">Snooze</button>';
            html += '<button class="btn btn-sm btn-primary" data-action="done-todo" data-id="'+todo.id+'" data-testid="done-todo-'+todo.id+'">Done</button>';
        } else if (todo.status === 'snoozed') {
            html += '<button class="btn btn-sm btn-outline" data-action="unsnooze-todo" data-id="'+todo.id+'" data-testid="unsnooze-todo-'+todo.id+'">Remove snooze</button>';
            html += '<button class="btn btn-sm btn-primary" data-action="done-todo" data-id="'+todo.id+'" data-testid="done-todo-'+todo.id+'">Done</button>';
        } else {
            html += '<button class="btn btn-sm btn-outline" data-action="restore-todo" data-id="'+todo.id+'" data-testid="restore-todo-'+todo.id+'">Restore</button>';
        }
        html += '</div></div>';
        return html;
    }
};

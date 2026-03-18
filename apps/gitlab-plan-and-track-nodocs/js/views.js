// GitLab Plan & Track — View Renderers
const Views = (() => {
    const C = Components;

    // ─── Issues List View ─────────────────────────────────────────
    function issuesList() {
        const ui = AppState.getUI();
        const { issues, total, page, totalPages } = AppState.getPagedIssues();
        const state = AppState.getState();

        // Counts
        const openCount = state.issues.filter(i => i.status === 'open').length;
        const closedCount = state.issues.filter(i => i.status === 'closed').length;

        let html = `<div class="view-header">
            <h1>Issues</h1>
            <button class="btn btn-primary" data-action="new-issue">New issue</button>
        </div>`;

        // Filter bar
        html += `<div class="filter-bar">
            <div class="filter-status-tabs">
                <button class="filter-tab${ui.issueFilters.status === 'open' ? ' active' : ''}" data-action="filter-status" data-status="open">\u25CB Open <span class="count">${openCount}</span></button>
                <button class="filter-tab${ui.issueFilters.status === 'closed' ? ' active' : ''}" data-action="filter-status" data-status="closed">\u25CF Closed <span class="count">${closedCount}</span></button>
                <button class="filter-tab${ui.issueFilters.status === 'all' ? ' active' : ''}" data-action="filter-status" data-status="all">All <span class="count">${state.issues.length}</span></button>
            </div>
            <div class="filter-search">
                <input type="text" class="search-input" id="issue-search" placeholder="Search issues..." value="${C._esc(ui.issueFilters.search)}" data-action="search-issues" />
            </div>
        </div>`;

        // Advanced filters row
        html += `<div class="filter-row">`;
        html += C.dropdown({
            id: 'filter-author', label: null, value: ui.issueFilters.authorId,
            options: [{ value: null, label: 'Any author' }, ...state.users.map(u => ({ value: u.id, label: u.name, avatar: u }))],
            placeholder: 'Author', searchable: true, className: 'filter-dropdown'
        });
        html += C.dropdown({
            id: 'filter-assignee', label: null, value: ui.issueFilters.assigneeId,
            options: [{ value: null, label: 'Any assignee' }, ...state.users.map(u => ({ value: u.id, label: u.name, avatar: u }))],
            placeholder: 'Assignee', searchable: true, className: 'filter-dropdown'
        });
        html += C.dropdown({
            id: 'filter-label', label: null, value: ui.issueFilters.labelIds,
            options: state.labels.map(l => ({ value: l.id, label: l.name, color: l.color })),
            placeholder: 'Label', searchable: true, multi: true, className: 'filter-dropdown'
        });
        html += C.dropdown({
            id: 'filter-milestone', label: null, value: ui.issueFilters.milestoneId,
            options: [{ value: null, label: 'Any milestone' }, ...state.milestones.map(m => ({ value: m.id, label: m.title }))],
            placeholder: 'Milestone', searchable: true, className: 'filter-dropdown'
        });
        html += C.dropdown({
            id: 'filter-sort', label: null, value: ui.issueFilters.sort,
            options: [
                { value: 'created_desc', label: 'Newest' },
                { value: 'created_asc', label: 'Oldest' },
                { value: 'updated_desc', label: 'Recently updated' },
                { value: 'updated_asc', label: 'Least recently updated' },
                { value: 'due_date_asc', label: 'Due date (earliest)' },
                { value: 'due_date_desc', label: 'Due date (latest)' },
                { value: 'priority_desc', label: 'Priority (highest)' },
                { value: 'priority_asc', label: 'Priority (lowest)' },
                { value: 'weight_desc', label: 'Weight (highest)' },
                { value: 'weight_asc', label: 'Weight (lowest)' },
            ],
            placeholder: 'Sort', className: 'filter-dropdown'
        });
        html += `</div>`;

        // Bulk actions bar (hidden by default, shown when checkboxes selected)
        html += `<div class="bulk-actions-bar" id="bulk-actions-bar" style="display:none">
            <span class="bulk-selected-count" id="bulk-count">0 selected</span>
            <button class="btn btn-sm" data-action="bulk-close">Close</button>
            <button class="btn btn-sm" data-action="bulk-assign">Assign</button>
            <button class="btn btn-sm" data-action="bulk-label">Label</button>
            <button class="btn btn-sm" data-action="bulk-milestone">Milestone</button>
        </div>`;

        if (issues.length === 0) {
            html += C.emptyState('No issues match your filters.', 'New issue', 'data-action="new-issue"');
        } else {
            html += `<table class="issues-table">
                <thead>
                    <tr>
                        <th class="th-checkbox"><input type="checkbox" id="select-all-issues" data-action="select-all-issues" /></th>
                        <th>Title</th>
                        <th>Status</th>
                        <th>Assignee</th>
                        <th>Milestone</th>
                        <th>Weight</th>
                        <th>Due date</th>
                        <th>Created</th>
                    </tr>
                </thead>
                <tbody>`;
            issues.forEach(issue => { html += C.issueRow(issue); });
            html += `</tbody></table>`;
            html += C.pagination(page, totalPages, total);
        }

        return html;
    }

    // ─── Issue Detail View ────────────────────────────────────────
    function issueDetail() {
        const ui = AppState.getUI();
        const issue = AppState.getIssue(ui.currentIssueId);
        if (!issue) return `<div class="error-box">Issue not found</div>`;

        const state = AppState.getState();
        const author = AppState.getUser(issue.authorId);
        const milestone = issue.milestoneId ? AppState.getMilestone(issue.milestoneId) : null;
        const iteration = issue.iterationId ? AppState.getIteration(issue.iterationId) : null;
        const comments = AppState.getComments(issue.id);
        const activities = AppState.getActivity(issue.id);
        const isSubscribed = AppState.isSubscribed(issue.id);

        let html = `<div class="issue-detail">`;

        // Breadcrumb
        html += `<div class="breadcrumb">
            <a data-action="navigate" data-view="issues">Issues</a> &raquo;
            <span>#${issue.id}</span>
        </div>`;

        // Header
        html += `<div class="issue-detail-header">
            <div class="issue-detail-title-row">
                ${C.issueTypeBadge(issue.type)}
                ${issue.confidential ? '<span class="confidential-icon" title="Confidential">&#128274;</span>' : ''}`;

        if (ui.editingIssueTitle) {
            html += `<input type="text" class="issue-title-edit" id="issue-title-input" value="${C._esc(issue.title)}" data-action="save-issue-title" />
                     <button class="btn btn-sm btn-primary" data-action="confirm-issue-title">Save</button>
                     <button class="btn btn-sm" data-action="cancel-issue-title">Cancel</button>`;
        } else {
            html += `<h1 class="issue-detail-title" data-action="edit-issue-title">${C._esc(issue.title)} <span class="issue-id-lg">#${issue.id}</span></h1>`;
        }
        html += `</div>`;
        html += `<div class="issue-detail-meta">
            ${C.statusBadge(issue.status)}
            <span>Opened ${C._timeAgo(issue.createdAt)} by ${author ? C._esc(author.name) : 'Unknown'}</span>
            ${issue.closedAt ? `<span> \u2022 Closed ${C._timeAgo(issue.closedAt)}</span>` : ''}
        </div>`;
        html += `</div>`;

        // Main content + sidebar layout
        html += `<div class="issue-detail-layout">`;

        // Main content
        html += `<div class="issue-detail-main">`;

        // Description
        html += `<div class="issue-description-section">
            <h3>Description</h3>`;
        if (ui.editingIssueDescription) {
            html += `<textarea class="description-editor" id="description-editor" rows="10">${C._esc(issue.description)}</textarea>
                     <div class="editor-actions">
                         <button class="btn btn-primary btn-sm" data-action="save-issue-description">Save</button>
                         <button class="btn btn-sm" data-action="cancel-issue-description">Cancel</button>
                     </div>`;
        } else {
            html += `<div class="issue-description" data-action="edit-issue-description">${issue.description ? C.renderMarkdown(issue.description) : '<span class="text-muted">No description provided. Click to add one.</span>'}</div>`;
        }
        html += `</div>`;

        // Related issues
        if (issue.relatedIssues.length > 0) {
            html += `<div class="related-issues-section">
                <h3>Related issues</h3>
                <div class="related-issues-list">`;
            issue.relatedIssues.forEach(rel => {
                const related = AppState.getIssue(rel.issueId);
                if (!related) return;
                const typeLabel = rel.type === 'blocks' ? 'blocks' : rel.type === 'is_blocked_by' ? 'is blocked by' : 'related to';
                html += `<div class="related-issue-item">
                    <span class="related-type">${typeLabel}</span>
                    <span class="related-issue-link" data-action="view-issue" data-issue-id="${related.id}">
                        ${C.statusBadge(related.status)} #${related.id} ${C._esc(related.title)}
                    </span>
                    <button class="btn-icon" data-action="remove-related-issue" data-issue-id="${issue.id}" data-related-id="${related.id}" title="Remove">&times;</button>
                </div>`;
            });
            html += `</div></div>`;
        }

        // Activity / Comments
        html += `<div class="activity-section">
            <h3>Activity</h3>
            <div class="activity-list">`;

        // Merge comments and activity, sort by date
        const allActivity = [];
        comments.forEach(c => allActivity.push({ ...c, _type: 'comment', _date: c.createdAt }));
        activities.forEach(a => allActivity.push({ ...a, _type: 'activity', _date: a.createdAt }));
        allActivity.sort((a, b) => a._date.localeCompare(b._date));

        allActivity.forEach(item => {
            if (item._type === 'comment') {
                const commentAuthor = AppState.getUser(item.authorId);
                html += `<div class="comment-item" id="comment-${item.id}">
                    <div class="comment-header">
                        ${C.avatar(commentAuthor, 28)}
                        <span class="comment-author">${commentAuthor ? C._esc(commentAuthor.name) : 'Unknown'}</span>
                        <span class="comment-date">${C._timeAgo(item.createdAt)}</span>
                        ${item.updatedAt !== item.createdAt ? '<span class="comment-edited">(edited)</span>' : ''}
                    </div>
                    <div class="comment-body">${C.renderMarkdown(item.body)}</div>
                </div>`;
            } else {
                html += _renderActivityItem(item);
            }
        });

        html += `</div>`;

        // Comment form
        html += `<div class="comment-form">
            <h4>Add a comment</h4>
            <textarea class="comment-editor" id="comment-editor" rows="4" placeholder="Write a comment... Use /assign, /label, /close, /weight, /estimate, /spend for quick actions"></textarea>
            <div class="comment-form-actions">
                <button class="btn btn-primary" data-action="submit-comment" data-issue-id="${issue.id}">Comment</button>
                ${issue.status === 'open'
                    ? `<button class="btn btn-danger" data-action="close-issue" data-issue-id="${issue.id}">Close issue</button>`
                    : `<button class="btn btn-success" data-action="reopen-issue" data-issue-id="${issue.id}">Reopen issue</button>`}
            </div>
        </div>`;

        html += `</div>`; // end main

        // Sidebar
        html += `<div class="issue-detail-sidebar">`;

        // Assignees
        html += C.sidebarSection('Assignees',
            C.dropdown({
                id: 'sidebar-assignees', value: issue.assigneeIds,
                options: state.users.map(u => ({ value: u.id, label: u.name, avatar: u })),
                placeholder: 'Select assignees', searchable: true, multi: true, className: 'sidebar-dropdown'
            })
        );

        // Labels
        html += C.sidebarSection('Labels',
            `<div class="sidebar-labels">${C.labelBadges(issue.labelIds, true, 'issue-detail')}</div>` +
            C.dropdown({
                id: 'sidebar-labels', value: issue.labelIds,
                options: state.labels.map(l => ({ value: l.id, label: l.name, color: l.color })),
                placeholder: 'Select labels', searchable: true, multi: true, className: 'sidebar-dropdown'
            })
        );

        // Milestone
        html += C.sidebarSection('Milestone',
            C.dropdown({
                id: 'sidebar-milestone', value: issue.milestoneId,
                options: [{ value: null, label: 'No milestone' }, ...state.milestones.filter(m => m.status === 'active').map(m => ({ value: m.id, label: m.title }))],
                placeholder: 'Select milestone', className: 'sidebar-dropdown'
            })
        );

        // Iteration
        html += C.sidebarSection('Iteration',
            C.dropdown({
                id: 'sidebar-iteration', value: issue.iterationId,
                options: [{ value: null, label: 'No iteration' }, ...state.iterations.filter(i => i.status === 'current' || i.status === 'upcoming').map(i => ({ value: i.id, label: i.title }))],
                placeholder: 'Select iteration', className: 'sidebar-dropdown'
            })
        );

        // Weight
        html += C.sidebarSection('Weight',
            `<input type="number" class="weight-input" id="sidebar-weight" value="${issue.weight || ''}" min="0" max="99" placeholder="Enter weight" data-action="change-weight" data-issue-id="${issue.id}" />`
        );

        // Due date
        html += C.sidebarSection('Due date',
            C.datePicker({ id: 'sidebar-due-date', value: issue.dueDate, placeholder: 'YYYY-MM-DD' })
        );

        // Confidential
        html += C.sidebarSection('Confidential',
            `<label class="toggle-label">
                <input type="checkbox" class="toggle-input" id="sidebar-confidential" ${issue.confidential ? 'checked' : ''} data-action="toggle-confidential" data-issue-id="${issue.id}" />
                <span class="toggle-switch"></span>
                <span>This issue is confidential</span>
            </label>`
        );

        // Time tracking
        html += C.sidebarSection('Time tracking',
            C.timeTrackingBar(issue.timeEstimate, issue.timeSpent) +
            `<div class="time-tracking-inputs">
                <div class="time-input-group">
                    <label>Estimate</label>
                    <input type="text" class="time-input" id="sidebar-estimate" placeholder="e.g. 4h 30m" data-action="set-estimate" data-issue-id="${issue.id}" />
                </div>
                <div class="time-input-group">
                    <label>Spend</label>
                    <input type="text" class="time-input" id="sidebar-spend" placeholder="e.g. 2h" data-action="add-spent" data-issue-id="${issue.id}" />
                </div>
            </div>`
        );

        // Subscription
        html += C.sidebarSection('Notifications',
            `<button class="btn btn-sm btn-block" data-action="toggle-subscription" data-issue-id="${issue.id}">
                ${isSubscribed ? '\u2713 Subscribed' : 'Subscribe'}
            </button>`
        );

        html += `</div>`; // end sidebar
        html += `</div>`; // end layout
        html += `</div>`; // end issue-detail

        return html;
    }

    function _renderActivityItem(item) {
        const user = AppState.getUser(item.userId);
        const userName = user ? C._esc(user.name) : 'Unknown';
        let description = '';

        switch (item.action) {
            case 'created_issue': description = 'created this issue'; break;
            case 'closed_issue': description = 'closed this issue'; break;
            case 'reopened_issue': description = 'reopened this issue'; break;
            case 'assigned': {
                const assignee = AppState.getUser(item.detail?.assigneeId);
                description = `assigned ${assignee ? C._esc(assignee.name) : 'someone'}`;
                break;
            }
            case 'unassigned': {
                const assignee = AppState.getUser(item.detail?.assigneeId);
                description = `unassigned ${assignee ? C._esc(assignee.name) : 'someone'}`;
                break;
            }
            case 'added_label': {
                const label = AppState.getLabel(item.detail?.labelId);
                description = `added label ${label ? C.labelBadge(label) : 'unknown'}`;
                break;
            }
            case 'removed_label': {
                const label = AppState.getLabel(item.detail?.labelId);
                description = `removed label ${label ? C.labelBadge(label) : 'unknown'}`;
                break;
            }
            case 'changed_label': {
                const added = AppState.getLabel(item.detail?.added);
                const removed = AppState.getLabel(item.detail?.removed);
                description = `changed label from ${removed ? C.labelBadge(removed) : '?'} to ${added ? C.labelBadge(added) : '?'}`;
                break;
            }
            case 'changed_milestone': {
                const from = item.detail?.from ? AppState.getMilestone(item.detail.from) : null;
                const to = item.detail?.to ? AppState.getMilestone(item.detail.to) : null;
                description = `changed milestone from ${from ? C._esc(from.title) : 'none'} to ${to ? C._esc(to.title) : 'none'}`;
                break;
            }
            case 'changed_iteration': {
                const from = item.detail?.from ? AppState.getIteration(item.detail.from) : null;
                const to = item.detail?.to ? AppState.getIteration(item.detail.to) : null;
                description = `changed iteration from ${from ? C._esc(from.title) : 'none'} to ${to ? C._esc(to.title) : 'none'}`;
                break;
            }
            default: description = item.action.replace(/_/g, ' ');
        }

        return `<div class="activity-item">
            <span class="activity-dot"></span>
            <span class="activity-text">${userName} ${description}</span>
            <span class="activity-date">${C._timeAgo(item.createdAt)}</span>
        </div>`;
    }

    // ─── New Issue Form ───────────────────────────────────────────
    function newIssueForm() {
        const state = AppState.getState();

        let html = `<div class="view-header">
            <h1>New issue</h1>
        </div>`;

        html += `<div class="new-issue-layout">`;
        html += `<div class="new-issue-main">`;

        // Template selection
        html += `<div class="form-group">
            <label class="field-label">Template</label>`;
        html += C.dropdown({
            id: 'issue-template', value: null,
            options: [{ value: null, label: 'No template' }, ...state.issueTemplates.map(t => ({ value: t.id, label: t.name }))],
            placeholder: 'Select template', className: 'form-dropdown'
        });
        html += `</div>`;

        // Type
        html += `<div class="form-group">
            <label class="field-label">Type</label>`;
        html += C.dropdown({
            id: 'issue-type', value: 'issue',
            options: [
                { value: 'issue', label: 'Issue' },
                { value: 'incident', label: 'Incident' },
                { value: 'task', label: 'Task' },
            ],
            placeholder: 'Select type', className: 'form-dropdown'
        });
        html += `</div>`;

        // Title
        html += `<div class="form-group">
            <label class="field-label required">Title</label>
            <input type="text" class="form-input" id="new-issue-title" placeholder="Enter issue title" required />
            <div class="field-error" id="title-error" style="display:none">Title is required</div>
        </div>`;

        // Description
        html += `<div class="form-group">
            <label class="field-label">Description</label>
            <textarea class="form-textarea" id="new-issue-description" rows="10" placeholder="Describe the issue... Supports Markdown"></textarea>
        </div>`;

        html += `</div>`; // end main

        // Sidebar fields
        html += `<div class="new-issue-sidebar">`;

        html += `<div class="form-group">
            <label class="field-label">Assignees</label>`;
        html += C.dropdown({
            id: 'new-issue-assignees', value: [],
            options: state.users.map(u => ({ value: u.id, label: u.name, avatar: u })),
            placeholder: 'Select assignees', searchable: true, multi: true, className: 'form-dropdown'
        });
        html += `</div>`;

        html += `<div class="form-group">
            <label class="field-label">Labels</label>`;
        html += C.dropdown({
            id: 'new-issue-labels', value: [],
            options: state.labels.map(l => ({ value: l.id, label: l.name, color: l.color })),
            placeholder: 'Select labels', searchable: true, multi: true, className: 'form-dropdown'
        });
        html += `</div>`;

        html += `<div class="form-group">
            <label class="field-label">Milestone</label>`;
        html += C.dropdown({
            id: 'new-issue-milestone', value: null,
            options: [{ value: null, label: 'No milestone' }, ...state.milestones.filter(m => m.status === 'active').map(m => ({ value: m.id, label: m.title }))],
            placeholder: 'Select milestone', className: 'form-dropdown'
        });
        html += `</div>`;

        html += `<div class="form-group">
            <label class="field-label">Iteration</label>`;
        html += C.dropdown({
            id: 'new-issue-iteration', value: null,
            options: [{ value: null, label: 'No iteration' }, ...state.iterations.filter(i => i.status === 'current' || i.status === 'upcoming').map(i => ({ value: i.id, label: i.title }))],
            placeholder: 'Select iteration', className: 'form-dropdown'
        });
        html += `</div>`;

        html += `<div class="form-group">
            <label class="field-label">Weight</label>
            <input type="number" class="form-input" id="new-issue-weight" min="0" max="99" placeholder="Issue weight" />
        </div>`;

        html += `<div class="form-group">
            <label class="field-label">Due date</label>`;
        html += C.datePicker({ id: 'new-issue-due-date', placeholder: 'YYYY-MM-DD' });
        html += `</div>`;

        html += `<div class="form-group">
            <label class="toggle-label">
                <input type="checkbox" class="toggle-input" id="new-issue-confidential" />
                <span class="toggle-switch"></span>
                <span>Confidential</span>
            </label>
        </div>`;

        html += `</div>`; // end sidebar

        html += `</div>`; // end layout

        // Submit buttons
        html += `<div class="form-actions">
            <button class="btn" data-action="navigate" data-view="issues">Cancel</button>
            <button class="btn btn-primary" data-action="create-issue" id="create-issue-btn">Create issue</button>
        </div>`;

        return html;
    }

    // ─── Labels Management View ───────────────────────────────────
    function labelsView() {
        const state = AppState.getState();
        const scopedLabels = state.labels.filter(l => l.scoped);
        const regularLabels = state.labels.filter(l => !l.scoped);

        let html = `<div class="view-header">
            <h1>Labels</h1>
            <button class="btn btn-primary" data-action="new-label">New label</button>
        </div>`;

        // Scoped labels section
        if (scopedLabels.length > 0) {
            html += `<h3 class="section-heading">Scoped labels</h3>`;
            html += `<div class="labels-list">`;
            scopedLabels.forEach(label => {
                const issueCount = state.issues.filter(i => i.labelIds.includes(label.id)).length;
                html += _labelRow(label, issueCount);
            });
            html += `</div>`;
        }

        // Regular labels section
        html += `<h3 class="section-heading">Labels</h3>`;
        html += `<div class="labels-list">`;
        regularLabels.forEach(label => {
            const issueCount = state.issues.filter(i => i.labelIds.includes(label.id)).length;
            html += _labelRow(label, issueCount);
        });
        html += `</div>`;

        return html;
    }

    function _labelRow(label, issueCount) {
        return `<div class="label-row" data-label-id="${label.id}">
            <div class="label-row-info">
                ${C.labelBadge(label)}
                <span class="label-description">${C._esc(label.description)}</span>
            </div>
            <div class="label-row-meta">
                <span class="label-issue-count">${issueCount} issue${issueCount !== 1 ? 's' : ''}</span>
                <button class="btn btn-sm" data-action="edit-label" data-label-id="${label.id}">Edit</button>
                <button class="btn btn-sm btn-danger" data-action="delete-label" data-label-id="${label.id}">Delete</button>
            </div>
        </div>`;
    }

    // ─── Milestones View ──────────────────────────────────────────
    function milestonesView() {
        const state = AppState.getState();
        const activeMilestones = state.milestones.filter(m => m.status === 'active');
        const closedMilestones = state.milestones.filter(m => m.status === 'closed');

        let html = `<div class="view-header">
            <h1>Milestones</h1>
            <button class="btn btn-primary" data-action="new-milestone">New milestone</button>
        </div>`;

        html += C.tabs([
            { id: 'active', label: 'Active', count: activeMilestones.length },
            { id: 'closed', label: 'Closed', count: closedMilestones.length },
        ], AppState.getUI()._milestonesTab || 'active');

        const milestones = (AppState.getUI()._milestonesTab || 'active') === 'active' ? activeMilestones : closedMilestones;

        if (milestones.length === 0) {
            html += C.emptyState('No milestones found.', 'New milestone', 'data-action="new-milestone"');
        } else {
            milestones.forEach(ms => {
                const stats = AppState.getMilestoneStats(ms.id);
                html += `<div class="milestone-card" data-action="view-milestone" data-milestone-id="${ms.id}">
                    <div class="milestone-card-header">
                        <h3>${C._esc(ms.title)}</h3>
                        <span class="milestone-dates">${ms.startDate ? C._formatDate(ms.startDate) : ''} ${ms.startDate || ms.dueDate ? '\u2013' : ''} ${ms.dueDate ? C._formatDate(ms.dueDate) : 'No due date'}</span>
                    </div>
                    <p class="milestone-description">${C._esc(ms.description)}</p>
                    ${C.progressBar(stats.percent)}
                    <div class="milestone-stats">
                        <span class="text-success">${stats.closed} closed</span>
                        <span class="text-muted">${stats.open} open</span>
                    </div>
                </div>`;
            });
        }

        return html;
    }

    // ─── Milestone Detail View ────────────────────────────────────
    function milestoneDetail() {
        const ui = AppState.getUI();
        const ms = AppState.getMilestone(ui.currentMilestoneId);
        if (!ms) return '<div class="error-box">Milestone not found</div>';

        const stats = AppState.getMilestoneStats(ms.id);
        const issues = AppState.getState().issues.filter(i => i.milestoneId === ms.id);
        const openIssues = issues.filter(i => i.status === 'open');
        const closedIssues = issues.filter(i => i.status === 'closed');

        let html = `<div class="breadcrumb">
            <a data-action="navigate" data-view="milestones">Milestones</a> &raquo;
            <span>${C._esc(ms.title)}</span>
        </div>`;

        html += `<div class="view-header">
            <h1>${C._esc(ms.title)}</h1>
            <div class="header-actions">
                <button class="btn btn-sm" data-action="edit-milestone" data-milestone-id="${ms.id}">Edit</button>
                ${ms.status === 'active'
                    ? `<button class="btn btn-sm btn-warning" data-action="close-milestone" data-milestone-id="${ms.id}">Close milestone</button>`
                    : `<button class="btn btn-sm btn-success" data-action="reopen-milestone" data-milestone-id="${ms.id}">Reopen milestone</button>`}
                <button class="btn btn-sm btn-danger" data-action="delete-milestone" data-milestone-id="${ms.id}">Delete</button>
            </div>
        </div>`;

        if (ms.description) html += `<p class="milestone-description-detail">${C._esc(ms.description)}</p>`;

        html += `<div class="milestone-meta">
            <span>Start: ${ms.startDate ? C._formatDate(ms.startDate) : 'N/A'}</span>
            <span>Due: ${ms.dueDate ? C._formatDate(ms.dueDate) : 'N/A'}</span>
        </div>`;

        html += C.progressBar(stats.percent);
        html += `<div class="milestone-stats"><span class="text-success">${stats.closed} closed</span> \u2022 <span class="text-muted">${stats.open} open</span> \u2022 <span>${stats.total} total</span></div>`;

        // Time tracking summary
        const totalEstimate = issues.reduce((s, i) => s + (i.timeEstimate || 0), 0);
        const totalSpent = issues.reduce((s, i) => s + (i.timeSpent || 0), 0);
        if (totalEstimate > 0 || totalSpent > 0) {
            html += `<div class="milestone-time-summary">
                <h3>Time tracking</h3>
                ${C.timeTrackingBar(totalEstimate, totalSpent)}
            </div>`;
        }

        // Issues list
        html += `<h3 class="section-heading">Open issues (${openIssues.length})</h3>`;
        if (openIssues.length > 0) {
            html += `<table class="issues-table"><tbody>`;
            openIssues.forEach(i => { html += C.issueRow(i); });
            html += `</tbody></table>`;
        }

        html += `<h3 class="section-heading">Closed issues (${closedIssues.length})</h3>`;
        if (closedIssues.length > 0) {
            html += `<table class="issues-table"><tbody>`;
            closedIssues.forEach(i => { html += C.issueRow(i); });
            html += `</tbody></table>`;
        }

        return html;
    }

    // ─── Boards View ──────────────────────────────────────────────
    function boardsView() {
        const ui = AppState.getUI();
        const board = AppState.getBoard(ui.currentBoardId);
        if (!board) return '<div class="error-box">Board not found</div>';

        const boardIssues = AppState.getBoardIssues(board.id);
        const state = AppState.getState();

        let html = `<div class="view-header board-header">
            <h1>${C._esc(board.name)}</h1>
            <div class="board-filters">`;
        html += C.dropdown({
            id: 'board-filter-assignee', value: ui.boardFilters.assigneeId,
            options: [{ value: null, label: 'Any assignee' }, ...state.users.map(u => ({ value: u.id, label: u.name, avatar: u }))],
            placeholder: 'Assignee', searchable: true, className: 'filter-dropdown'
        });
        html += C.dropdown({
            id: 'board-filter-milestone', value: ui.boardFilters.milestoneId,
            options: [{ value: null, label: 'Any milestone' }, ...state.milestones.map(m => ({ value: m.id, label: m.title }))],
            placeholder: 'Milestone', className: 'filter-dropdown'
        });
        html += `</div></div>`;

        html += `<div class="board-container">`;
        board.lists.forEach(list => {
            const issues = boardIssues[list.id] || [];
            html += `<div class="board-column" data-list-id="${list.id}" data-board-id="${board.id}">
                <div class="board-column-header">
                    <span class="board-column-title">${C._esc(list.title)}</span>
                    <span class="board-column-count">${issues.length}</span>
                    ${list.type === 'label' ? `<button class="btn-icon board-column-remove" data-action="remove-board-list" data-board-id="${board.id}" data-list-id="${list.id}" title="Remove list">&times;</button>` : ''}
                </div>
                <div class="board-column-body" data-list-id="${list.id}" data-board-id="${board.id}">`;
            issues.slice(0, 20).forEach(issue => {
                html += C.issueCard(issue);
            });
            if (issues.length > 20) {
                html += `<div class="board-more">+ ${issues.length - 20} more</div>`;
            }
            if (list.type !== 'closed') {
                html += `<button class="board-add-issue" data-action="board-new-issue" data-list-id="${list.id}" data-board-id="${board.id}">+ New issue</button>`;
            }
            html += `</div></div>`;
        });

        // Add list button
        html += `<div class="board-column board-add-column">
            <button class="btn board-add-list-btn" data-action="add-board-list" data-board-id="${board.id}">+ Add list</button>
        </div>`;

        html += `</div>`;

        return html;
    }

    // ─── Iterations View ──────────────────────────────────────────
    function iterationsView() {
        const state = AppState.getState();
        const cadences = state.iterationCadences;

        let html = `<div class="view-header">
            <h1>Iterations</h1>
            <button class="btn btn-primary" data-action="new-iteration">New iteration</button>
        </div>`;

        cadences.forEach(cadence => {
            const iters = state.iterations.filter(i => i.cadenceId === cadence.id);
            html += `<div class="cadence-section">
                <h2 class="cadence-title">${C._esc(cadence.title)} <span class="text-muted">(${cadence.durationWeeks}-week${cadence.durationWeeks > 1 ? 's' : ''})</span></h2>
                <p class="cadence-description">${C._esc(cadence.description)}</p>`;

            const currentIter = iters.find(i => i.status === 'current');
            const upcomingIters = iters.filter(i => i.status === 'upcoming');
            const closedIters = iters.filter(i => i.status === 'closed');

            if (currentIter) {
                const stats = AppState.getIterationStats(currentIter.id);
                html += `<div class="iteration-card current" data-action="view-iteration" data-iteration-id="${currentIter.id}">
                    <div class="iteration-card-badge">Current</div>
                    <h3>${C._esc(currentIter.title)}</h3>
                    <div class="iteration-dates">${C._formatDate(currentIter.startDate)} \u2013 ${C._formatDate(currentIter.endDate)}</div>
                    ${C.progressBar(stats.percent)}
                    <div class="iteration-stats">${stats.closed}/${stats.total} issues \u2022 ${stats.closedWeight}/${stats.totalWeight} weight</div>
                </div>`;
            }

            if (upcomingIters.length > 0) {
                html += `<h4>Upcoming</h4>`;
                upcomingIters.forEach(iter => {
                    const stats = AppState.getIterationStats(iter.id);
                    html += `<div class="iteration-card upcoming" data-action="view-iteration" data-iteration-id="${iter.id}">
                        <h3>${C._esc(iter.title)}</h3>
                        <div class="iteration-dates">${C._formatDate(iter.startDate)} \u2013 ${C._formatDate(iter.endDate)}</div>
                        <div class="iteration-stats">${stats.total} issues \u2022 ${stats.totalWeight} weight</div>
                    </div>`;
                });
            }

            if (closedIters.length > 0) {
                html += `<h4>Closed (${closedIters.length})</h4>`;
                closedIters.forEach(iter => {
                    const stats = AppState.getIterationStats(iter.id);
                    html += `<div class="iteration-card closed" data-action="view-iteration" data-iteration-id="${iter.id}">
                        <h3>${C._esc(iter.title)}</h3>
                        <div class="iteration-dates">${C._formatDate(iter.startDate)} \u2013 ${C._formatDate(iter.endDate)}</div>
                        ${C.progressBar(stats.percent)}
                        <div class="iteration-stats">${stats.closed}/${stats.total} issues \u2022 ${stats.closedWeight}/${stats.totalWeight} weight</div>
                    </div>`;
                });
            }

            html += `</div>`;
        });

        return html;
    }

    // ─── Iteration Detail View ────────────────────────────────────
    function iterationDetail() {
        const ui = AppState.getUI();
        const iter = AppState.getIteration(ui.currentIterationId);
        if (!iter) return '<div class="error-box">Iteration not found</div>';

        const cadence = AppState.getState().iterationCadences.find(c => c.id === iter.cadenceId);
        const stats = AppState.getIterationStats(iter.id);
        const issues = AppState.getState().issues.filter(i => i.iterationId === iter.id);
        const openIssues = issues.filter(i => i.status === 'open');
        const closedIssues = issues.filter(i => i.status === 'closed');

        let html = `<div class="breadcrumb">
            <a data-action="navigate" data-view="iterations">Iterations</a> &raquo;
            <span>${C._esc(iter.title)}</span>
        </div>`;

        html += `<div class="view-header">
            <h1>${C._esc(iter.title)}</h1>
            <div class="header-actions">
                <span class="iteration-status-badge ${iter.status}">${iter.status}</span>
            </div>
        </div>`;

        if (cadence) html += `<p class="text-muted">Cadence: ${C._esc(cadence.title)}</p>`;
        html += `<div class="iteration-meta">
            <span>${C._formatDate(iter.startDate)} \u2013 ${C._formatDate(iter.endDate)}</span>
        </div>`;

        html += C.progressBar(stats.percent);
        html += `<div class="iteration-detail-stats">
            <div class="stat-box"><div class="stat-value">${stats.total}</div><div class="stat-label">Total issues</div></div>
            <div class="stat-box"><div class="stat-value">${stats.closed}</div><div class="stat-label">Completed</div></div>
            <div class="stat-box"><div class="stat-value">${stats.open}</div><div class="stat-label">Open</div></div>
            <div class="stat-box"><div class="stat-value">${stats.totalWeight}</div><div class="stat-label">Total weight</div></div>
            <div class="stat-box"><div class="stat-value">${stats.closedWeight}</div><div class="stat-label">Completed weight</div></div>
        </div>`;

        // Burndown placeholder
        html += `<div class="burndown-chart">
            <h3>Burndown</h3>
            <div class="burndown-placeholder">
                <div class="burndown-bar" style="width:${100 - stats.percent}%;background:#e24329"></div>
                <div class="burndown-bar" style="width:${stats.percent}%;background:#1aaa55"></div>
            </div>
            <div class="burndown-legend">
                <span class="legend-item"><span class="legend-dot" style="background:#e24329"></span> Remaining</span>
                <span class="legend-item"><span class="legend-dot" style="background:#1aaa55"></span> Completed</span>
            </div>
        </div>`;

        // Issues
        html += `<h3 class="section-heading">Open issues (${openIssues.length})</h3>`;
        if (openIssues.length > 0) {
            html += `<table class="issues-table"><tbody>`;
            openIssues.forEach(i => { html += C.issueRow(i); });
            html += `</tbody></table>`;
        }

        html += `<h3 class="section-heading">Closed issues (${closedIssues.length})</h3>`;
        if (closedIssues.length > 0) {
            html += `<table class="issues-table"><tbody>`;
            closedIssues.forEach(i => { html += C.issueRow(i); });
            html += `</tbody></table>`;
        }

        return html;
    }

    // ─── Epics View ───────────────────────────────────────────────
    function epicsView() {
        const state = AppState.getState();
        const ui = AppState.getUI();

        let filtered = state.epics.slice();
        if (ui.epicFilters.status === 'open') filtered = filtered.filter(e => e.status === 'open');
        else if (ui.epicFilters.status === 'closed') filtered = filtered.filter(e => e.status === 'closed');
        if (ui.epicFilters.search) {
            const s = ui.epicFilters.search.toLowerCase();
            filtered = filtered.filter(e => e.title.toLowerCase().includes(s));
        }

        const openCount = state.epics.filter(e => e.status === 'open').length;
        const closedCount = state.epics.filter(e => e.status === 'closed').length;

        let html = `<div class="view-header">
            <h1>Epics</h1>
            <button class="btn btn-primary" data-action="new-epic">New epic</button>
        </div>`;

        html += `<div class="filter-bar">
            <div class="filter-status-tabs">
                <button class="filter-tab${ui.epicFilters.status === 'open' ? ' active' : ''}" data-action="filter-epics-status" data-status="open">\u25CB Open <span class="count">${openCount}</span></button>
                <button class="filter-tab${ui.epicFilters.status === 'closed' ? ' active' : ''}" data-action="filter-epics-status" data-status="closed">\u25CF Closed <span class="count">${closedCount}</span></button>
                <button class="filter-tab${ui.epicFilters.status === 'all' ? ' active' : ''}" data-action="filter-epics-status" data-status="all">All <span class="count">${state.epics.length}</span></button>
            </div>
            <div class="filter-search">
                <input type="text" class="search-input" id="epic-search" placeholder="Search epics..." value="${C._esc(ui.epicFilters.search)}" data-action="search-epics" />
            </div>
        </div>`;

        if (filtered.length === 0) {
            html += C.emptyState('No epics found.', 'New epic', 'data-action="new-epic"');
        } else {
            filtered.forEach(epic => {
                const stats = AppState.getEpicStats(epic.id);
                const author = AppState.getUser(epic.authorId);
                html += `<div class="epic-card" data-action="view-epic" data-epic-id="${epic.id}">
                    <div class="epic-card-header">
                        ${epic.confidential ? '<span class="confidential-icon">&#128274;</span>' : ''}
                        <h3>${C._esc(epic.title)}</h3>
                        ${C.statusBadge(epic.status)}
                    </div>
                    <p class="epic-card-description">${C._esc((epic.description || '').substring(0, 200))}${(epic.description || '').length > 200 ? '...' : ''}</p>
                    <div class="epic-card-meta">
                        ${C.progressBar(stats.percent)}
                        <span>${stats.closed}/${stats.total} issues</span>
                        <span>${epic.startDate ? C._formatDate(epic.startDate) : ''} ${epic.startDate || epic.dueDate ? '\u2013' : ''} ${epic.dueDate ? C._formatDate(epic.dueDate) : ''}</span>
                        <span>by ${author ? C._esc(author.name) : 'Unknown'}</span>
                    </div>
                    <div class="epic-card-labels">${C.labelBadges(epic.labels || [])}</div>
                </div>`;
            });
        }

        return html;
    }

    // ─── Epic Detail View ─────────────────────────────────────────
    function epicDetail() {
        const ui = AppState.getUI();
        const epic = AppState.getEpic(ui.currentEpicId);
        if (!epic) return '<div class="error-box">Epic not found</div>';

        const stats = AppState.getEpicStats(epic.id);
        const author = AppState.getUser(epic.authorId);
        const childIssues = epic.childIssueIds.map(id => AppState.getIssue(id)).filter(Boolean);
        const state = AppState.getState();

        let html = `<div class="breadcrumb">
            <a data-action="navigate" data-view="epics">Epics</a> &raquo;
            <span>${C._esc(epic.title)}</span>
        </div>`;

        html += `<div class="view-header">
            <div>
                <h1>${epic.confidential ? '<span class="confidential-icon">&#128274;</span>' : ''} ${C._esc(epic.title)}</h1>
                <div class="issue-detail-meta">
                    ${C.statusBadge(epic.status)}
                    <span>Created ${C._timeAgo(epic.createdAt)} by ${author ? C._esc(author.name) : 'Unknown'}</span>
                </div>
            </div>
            <div class="header-actions">
                ${epic.status === 'open'
                    ? `<button class="btn btn-warning" data-action="close-epic" data-epic-id="${epic.id}">Close epic</button>`
                    : `<button class="btn btn-success" data-action="reopen-epic" data-epic-id="${epic.id}">Reopen epic</button>`}
            </div>
        </div>`;

        html += `<div class="epic-detail-layout">`;
        html += `<div class="epic-detail-main">`;

        // Description
        if (epic.description) {
            html += `<div class="epic-description-section">
                <h3>Description</h3>
                <div class="epic-description">${C.renderMarkdown(epic.description)}</div>
            </div>`;
        }

        // Progress
        html += `<div class="epic-progress-section">
            <h3>Progress</h3>
            ${C.progressBar(stats.percent)}
            <div class="epic-stats">${stats.closed} of ${stats.total} issues completed</div>
        </div>`;

        // Roadmap bar
        if (epic.startDate && epic.dueDate) {
            html += `<div class="epic-roadmap-bar">
                <h3>Timeline</h3>
                <div class="roadmap-single-bar">
                    <span class="roadmap-date">${C._formatDate(epic.startDate)}</span>
                    <div class="roadmap-bar-visual">
                        <div class="roadmap-bar-fill" style="width:${_epicTimelinePercent(epic)}%"></div>
                    </div>
                    <span class="roadmap-date">${C._formatDate(epic.dueDate)}</span>
                </div>
            </div>`;
        }

        // Child issues
        html += `<div class="epic-children-section">
            <h3>Child issues (${childIssues.length})</h3>`;
        if (childIssues.length > 0) {
            html += `<table class="issues-table"><tbody>`;
            childIssues.forEach(i => { html += C.issueRow(i); });
            html += `</tbody></table>`;
        } else {
            html += `<p class="text-muted">No child issues.</p>`;
        }

        // Add child issue
        html += `<div class="add-child-section">`;
        html += C.dropdown({
            id: 'add-child-issue', value: null,
            options: state.issues.filter(i => !epic.childIssueIds.includes(i.id) && i.status === 'open')
                .slice(0, 30).map(i => ({ value: i.id, label: `#${i.id} ${i.title}` })),
            placeholder: 'Add child issue...', searchable: true, className: 'inline-dropdown'
        });
        html += `</div>`;

        html += `</div>`;

        html += `</div>`; // end main

        // Sidebar
        html += `<div class="epic-detail-sidebar">`;
        html += C.sidebarSection('Labels',
            C.labelBadges(epic.labels || []) || '<span class="text-muted">None</span>'
        );
        html += C.sidebarSection('Start date',
            `<span>${epic.startDate ? C._formatDate(epic.startDate) : 'Not set'}</span>`
        );
        html += C.sidebarSection('Due date',
            `<span>${epic.dueDate ? C._formatDate(epic.dueDate) : 'Not set'}</span>`
        );
        html += C.sidebarSection('Confidential',
            `<span>${epic.confidential ? 'Yes' : 'No'}</span>`
        );
        html += `</div>`;

        html += `</div>`; // end layout

        return html;
    }

    function _epicTimelinePercent(epic) {
        const start = new Date(epic.startDate).getTime();
        const end = new Date(epic.dueDate).getTime();
        const now = Date.now();
        if (now <= start) return 0;
        if (now >= end) return 100;
        return Math.round(((now - start) / (end - start)) * 100);
    }

    // ─── Roadmap View ─────────────────────────────────────────────
    function roadmapView() {
        const state = AppState.getState();
        const ui = AppState.getUI();
        const epics = state.epics.filter(e => e.startDate && e.dueDate && e.status === 'open');

        let html = `<div class="view-header">
            <h1>Roadmap</h1>
            <div class="roadmap-controls">`;
        html += C.dropdown({
            id: 'roadmap-zoom', value: ui.roadmapZoom,
            options: [
                { value: 'weeks', label: 'Weeks' },
                { value: 'months', label: 'Months' },
                { value: 'quarters', label: 'Quarters' },
            ],
            placeholder: 'Zoom', className: 'filter-dropdown'
        });
        html += `</div></div>`;

        if (epics.length === 0) {
            html += C.emptyState('No epics with dates to display on the roadmap.');
            return html;
        }

        // Calculate timeline range
        const allDates = epics.flatMap(e => [new Date(e.startDate), new Date(e.dueDate)]);
        const minDate = new Date(Math.min(...allDates));
        const maxDate = new Date(Math.max(...allDates));
        // Add some padding
        minDate.setDate(minDate.getDate() - 14);
        maxDate.setDate(maxDate.getDate() + 14);

        const totalDays = Math.ceil((maxDate - minDate) / (1000 * 60 * 60 * 24));

        // Month headers
        html += `<div class="roadmap-timeline">`;
        html += `<div class="roadmap-header">`;
        html += `<div class="roadmap-label-col">Epic</div>`;
        html += `<div class="roadmap-bars-col">`;

        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        let current = new Date(minDate);
        while (current <= maxDate) {
            const daysInMonth = new Date(current.getFullYear(), current.getMonth() + 1, 0).getDate();
            const monthStart = new Date(current.getFullYear(), current.getMonth(), 1);
            const startOffset = Math.max(0, Math.ceil((monthStart - minDate) / (1000 * 60 * 60 * 24)));
            const width = (daysInMonth / totalDays) * 100;
            html += `<div class="roadmap-month" style="left:${(startOffset / totalDays) * 100}%;width:${width}%">${months[current.getMonth()]} ${current.getFullYear()}</div>`;
            current.setMonth(current.getMonth() + 1);
        }
        html += `</div></div>`;

        // Epic bars
        epics.forEach(epic => {
            const start = new Date(epic.startDate);
            const end = new Date(epic.dueDate);
            const startOffset = Math.max(0, (start - minDate) / (1000 * 60 * 60 * 24));
            const duration = Math.max(1, (end - start) / (1000 * 60 * 60 * 24));
            const left = (startOffset / totalDays) * 100;
            const width = (duration / totalDays) * 100;
            const stats = AppState.getEpicStats(epic.id);

            html += `<div class="roadmap-row">
                <div class="roadmap-label-col">
                    <span class="roadmap-epic-label" data-action="view-epic" data-epic-id="${epic.id}">${C._esc(epic.title)}</span>
                </div>
                <div class="roadmap-bars-col">
                    <div class="roadmap-bar" style="left:${left}%;width:${width}%" title="${C._esc(epic.title)}: ${C._formatDate(epic.startDate)} – ${C._formatDate(epic.dueDate)}">
                        <div class="roadmap-bar-progress" style="width:${stats.percent}%"></div>
                        <span class="roadmap-bar-label">${C._esc(epic.title)}</span>
                    </div>
                </div>
            </div>`;
        });

        // Today marker
        const todayOffset = (Date.now() - minDate.getTime()) / (1000 * 60 * 60 * 24);
        if (todayOffset >= 0 && todayOffset <= totalDays) {
            html += `<div class="roadmap-today" style="left:calc(200px + ${(todayOffset / totalDays) * (100)}% * (100% - 200px) / 100%)"></div>`;
        }

        html += `</div>`;
        return html;
    }

    // ─── Notifications View ───────────────────────────────────────
    function notificationsView() {
        const state = AppState.getState();
        const notifications = state.notifications.sort((a, b) => b.createdAt.localeCompare(a.createdAt));
        const unreadCount = notifications.filter(n => !n.read).length;

        let html = `<div class="view-header">
            <h1>Notifications</h1>
            <div class="header-actions">
                ${unreadCount > 0 ? `<button class="btn btn-sm" data-action="mark-all-read">Mark all as read</button>` : ''}
            </div>
        </div>`;

        // Settings
        html += `<div class="notification-settings">
            <h3>Notification preferences</h3>`;
        html += C.dropdown({
            id: 'notification-level', value: state.notificationSettings.level,
            options: [
                { value: 'global', label: 'Global' },
                { value: 'watch', label: 'Watch' },
                { value: 'on_mention', label: 'On mention' },
                { value: 'disabled', label: 'Disabled' },
            ],
            placeholder: 'Notification level', className: 'notification-dropdown'
        });
        html += `</div>`;

        if (notifications.length === 0) {
            html += C.emptyState('No notifications yet.');
        } else {
            html += `<div class="notifications-list">`;
            notifications.forEach(n => {
                const icon = _notificationIcon(n.type);
                html += `<div class="notification-item${n.read ? '' : ' unread'}" data-action="notification-click" data-notification-id="${n.id}" data-issue-id="${n.issueId}">
                    <span class="notification-icon">${icon}</span>
                    <div class="notification-content">
                        <span class="notification-message">${C._esc(n.message)}</span>
                        <span class="notification-time">${C._timeAgo(n.createdAt)}</span>
                    </div>
                    ${!n.read ? `<button class="btn-icon notification-mark-read" data-action="mark-read" data-notification-id="${n.id}" title="Mark as read">\u2713</button>` : ''}
                </div>`;
            });
            html += `</div>`;
        }

        return html;
    }

    function _notificationIcon(type) {
        const icons = {
            assigned: '\u2192',
            mentioned: '@',
            comment: '\u{1F4AC}',
            status_change: '\u25CB',
            label_change: '\u{1F3F7}',
            milestone_change: '\u{1F3AF}',
        };
        return icons[type] || '\u2022';
    }

    // ─── Time Tracking Report View ────────────────────────────────
    function timeTrackingView() {
        const state = AppState.getState();

        let html = `<div class="view-header">
            <h1>Time tracking</h1>
        </div>`;

        // Summary stats
        const totalEstimate = state.issues.reduce((s, i) => s + (i.timeEstimate || 0), 0);
        const totalSpent = state.issues.reduce((s, i) => s + (i.timeSpent || 0), 0);
        const remaining = Math.max(0, totalEstimate - totalSpent);

        html += `<div class="time-summary-cards">
            <div class="stat-box"><div class="stat-value">${AppState.formatTime(totalEstimate)}</div><div class="stat-label">Total estimated</div></div>
            <div class="stat-box"><div class="stat-value">${AppState.formatTime(totalSpent)}</div><div class="stat-label">Total spent</div></div>
            <div class="stat-box"><div class="stat-value">${AppState.formatTime(remaining)}</div><div class="stat-label">Remaining</div></div>
        </div>`;

        // Per milestone
        html += `<h3 class="section-heading">By milestone</h3>`;
        state.milestones.filter(m => m.status === 'active').forEach(ms => {
            const issues = state.issues.filter(i => i.milestoneId === ms.id);
            const est = issues.reduce((s, i) => s + (i.timeEstimate || 0), 0);
            const spent = issues.reduce((s, i) => s + (i.timeSpent || 0), 0);
            if (est > 0 || spent > 0) {
                html += `<div class="time-tracking-row">
                    <span class="time-tracking-label">${C._esc(ms.title)}</span>
                    ${C.timeTrackingBar(est, spent)}
                </div>`;
            }
        });

        // Per label (top 10 with time data)
        html += `<h3 class="section-heading">By label</h3>`;
        state.labels.filter(l => !l.scoped).forEach(label => {
            const issues = state.issues.filter(i => i.labelIds.includes(label.id));
            const est = issues.reduce((s, i) => s + (i.timeEstimate || 0), 0);
            const spent = issues.reduce((s, i) => s + (i.timeSpent || 0), 0);
            if (est > 0 || spent > 0) {
                html += `<div class="time-tracking-row">
                    <span class="time-tracking-label">${C.labelBadge(label)}</span>
                    ${C.timeTrackingBar(est, spent)}
                </div>`;
            }
        });

        return html;
    }

    // ─── Sidebar Navigation ───────────────────────────────────────
    function sidebar() {
        const ui = AppState.getUI();
        const state = AppState.getState();
        const openCount = state.issues.filter(i => i.status === 'open').length;
        const unreadNotifs = state.notifications.filter(n => !n.read).length;

        const items = [
            { id: 'issues', label: 'Issues', icon: '\u25CB', count: openCount },
            { id: 'boards', label: 'Boards', icon: '\u2630' },
            { id: 'labels', label: 'Labels', icon: '\u{1F3F7}' },
            { id: 'milestones', label: 'Milestones', icon: '\u{1F3AF}' },
            { id: 'iterations', label: 'Iterations', icon: '\u{1F504}' },
            { id: 'epics', label: 'Epics', icon: '\u{1F4DC}' },
            { id: 'roadmap', label: 'Roadmap', icon: '\u{1F5FA}' },
            { id: 'time-tracking', label: 'Time tracking', icon: '\u23F1' },
            { id: 'notifications', label: 'Notifications', icon: '\u{1F514}', count: unreadNotifs || null },
        ];

        let html = `<div class="sidebar-nav">`;
        html += `<div class="sidebar-header">
            <span class="sidebar-project-name">${C._esc(state.project.name)}</span>
            <span class="sidebar-project-path">${C._esc(state.project.path)}</span>
        </div>`;
        html += `<div class="sidebar-section-label">Plan</div>`;
        items.forEach(item => {
            const active = ui.currentView === item.id || (ui.currentView === 'issue-detail' && item.id === 'issues') ||
                (ui.currentView === 'new-issue' && item.id === 'issues') ||
                (ui.currentView === 'milestone-detail' && item.id === 'milestones') ||
                (ui.currentView === 'iteration-detail' && item.id === 'iterations') ||
                (ui.currentView === 'epic-detail' && item.id === 'epics');
            html += `<a class="sidebar-item${active ? ' active' : ''}" data-action="navigate" data-view="${item.id}">
                <span class="sidebar-icon">${item.icon}</span>
                <span class="sidebar-label">${item.label}</span>
                ${item.count ? `<span class="sidebar-count">${item.count}</span>` : ''}
            </a>`;
        });
        html += `</div>`;
        return html;
    }

    // ─── Modal Forms ──────────────────────────────────────────────
    function labelFormModal(label = null) {
        const title = label ? 'Edit label' : 'New label';
        const body = `<div class="form-group">
                <label class="field-label required">Name</label>
                <input type="text" class="form-input" id="label-name" value="${label ? C._esc(label.name) : ''}" placeholder="e.g. bug, priority::high" />
            </div>
            <div class="form-group">
                <label class="field-label">Description</label>
                <input type="text" class="form-input" id="label-description" value="${label ? C._esc(label.description) : ''}" placeholder="Label description" />
            </div>
            <div class="form-group">
                <label class="field-label">Color</label>
                ${C.colorPicker('label-color', label ? label.color : '#428bca')}
            </div>`;

        const actionLabel = label ? 'Save changes' : 'Create label';
        const action = label ? 'save-label' : 'create-label-confirm';
        const footer = `<button class="btn" data-action="close-modal" data-modal="label-form-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="${action}" ${label ? `data-label-id="${label.id}"` : ''} id="label-submit-btn">${actionLabel}</button>`;

        return C.modal({ id: 'label-form-modal', title, body, footer });
    }

    function milestoneFormModal(ms = null) {
        const title = ms ? 'Edit milestone' : 'New milestone';
        const body = `<div class="form-group">
                <label class="field-label required">Title</label>
                <input type="text" class="form-input" id="milestone-title" value="${ms ? C._esc(ms.title) : ''}" placeholder="e.g. v2.0" />
            </div>
            <div class="form-group">
                <label class="field-label">Description</label>
                <textarea class="form-textarea" id="milestone-description" rows="3" placeholder="Milestone description">${ms ? C._esc(ms.description) : ''}</textarea>
            </div>
            <div class="form-group-row">
                <div class="form-group">
                    <label class="field-label">Start date</label>
                    ${C.datePicker({ id: 'milestone-start-date', value: ms ? ms.startDate : '' })}
                </div>
                <div class="form-group">
                    <label class="field-label">Due date</label>
                    ${C.datePicker({ id: 'milestone-due-date', value: ms ? ms.dueDate : '' })}
                </div>
            </div>`;

        const actionLabel = ms ? 'Save changes' : 'Create milestone';
        const action = ms ? 'save-milestone' : 'create-milestone-confirm';
        const footer = `<button class="btn" data-action="close-modal" data-modal="milestone-form-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="${action}" ${ms ? `data-milestone-id="${ms.id}"` : ''} id="milestone-submit-btn">${actionLabel}</button>`;

        return C.modal({ id: 'milestone-form-modal', title, body, footer });
    }

    function iterationFormModal() {
        const state = AppState.getState();
        const body = `<div class="form-group">
                <label class="field-label required">Cadence</label>
                ${C.dropdown({
                    id: 'iteration-cadence', value: state.iterationCadences[0]?.id,
                    options: state.iterationCadences.map(c => ({ value: c.id, label: c.title })),
                    className: 'form-dropdown'
                })}
            </div>
            <div class="form-group">
                <label class="field-label required">Title</label>
                <input type="text" class="form-input" id="iteration-title" placeholder="e.g. Sprint 9" />
            </div>
            <div class="form-group-row">
                <div class="form-group">
                    <label class="field-label required">Start date</label>
                    ${C.datePicker({ id: 'iteration-start-date' })}
                </div>
                <div class="form-group">
                    <label class="field-label required">End date</label>
                    ${C.datePicker({ id: 'iteration-end-date' })}
                </div>
            </div>`;

        const footer = `<button class="btn" data-action="close-modal" data-modal="iteration-form-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="create-iteration-confirm" id="iteration-submit-btn">Create iteration</button>`;

        return C.modal({ id: 'iteration-form-modal', title: 'New iteration', body, footer });
    }

    function epicFormModal() {
        const state = AppState.getState();
        const body = `<div class="form-group">
                <label class="field-label required">Title</label>
                <input type="text" class="form-input" id="epic-title" placeholder="Epic title" />
            </div>
            <div class="form-group">
                <label class="field-label">Description</label>
                <textarea class="form-textarea" id="epic-description" rows="5" placeholder="Epic description... Supports Markdown"></textarea>
            </div>
            <div class="form-group-row">
                <div class="form-group">
                    <label class="field-label">Start date</label>
                    ${C.datePicker({ id: 'epic-start-date' })}
                </div>
                <div class="form-group">
                    <label class="field-label">Due date</label>
                    ${C.datePicker({ id: 'epic-due-date' })}
                </div>
            </div>
            <div class="form-group">
                <label class="field-label">Labels</label>
                ${C.dropdown({
                    id: 'epic-labels', value: [],
                    options: state.labels.map(l => ({ value: l.id, label: l.name, color: l.color })),
                    placeholder: 'Select labels', searchable: true, multi: true, className: 'form-dropdown'
                })}
            </div>
            <div class="form-group">
                <label class="toggle-label">
                    <input type="checkbox" class="toggle-input" id="epic-confidential" />
                    <span class="toggle-switch"></span>
                    <span>Confidential</span>
                </label>
            </div>`;

        const footer = `<button class="btn" data-action="close-modal" data-modal="epic-form-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="create-epic-confirm" id="epic-submit-btn">Create epic</button>`;

        return C.modal({ id: 'epic-form-modal', title: 'New epic', body, footer });
    }

    function addBoardListModal(boardId) {
        const state = AppState.getState();
        const board = AppState.getBoard(boardId);
        const usedLabelIds = board ? board.lists.filter(l => l.labelId).map(l => l.labelId) : [];
        const availableLabels = state.labels.filter(l => !usedLabelIds.includes(l.id));

        const body = `<div class="form-group">
            <label class="field-label">Select a label for the new list</label>
            ${C.dropdown({
                id: 'board-list-label', value: null,
                options: availableLabels.map(l => ({ value: l.id, label: l.name, color: l.color })),
                placeholder: 'Select label', searchable: true, className: 'form-dropdown'
            })}
        </div>`;

        const footer = `<button class="btn" data-action="close-modal" data-modal="add-board-list-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="confirm-add-board-list" data-board-id="${boardId}" id="board-list-submit-btn">Add list</button>`;

        return C.modal({ id: 'add-board-list-modal', title: 'Add list', body, footer });
    }

    function bulkActionModal(type) {
        const state = AppState.getState();
        let body = '';
        let title = '';
        let action = '';

        if (type === 'assign') {
            title = 'Assign issues';
            action = 'confirm-bulk-assign';
            body = C.dropdown({
                id: 'bulk-assignee', value: null,
                options: state.users.map(u => ({ value: u.id, label: u.name, avatar: u })),
                placeholder: 'Select assignee', searchable: true, className: 'form-dropdown'
            });
        } else if (type === 'label') {
            title = 'Add label';
            action = 'confirm-bulk-label';
            body = C.dropdown({
                id: 'bulk-label', value: null,
                options: state.labels.map(l => ({ value: l.id, label: l.name, color: l.color })),
                placeholder: 'Select label', searchable: true, className: 'form-dropdown'
            });
        } else if (type === 'milestone') {
            title = 'Set milestone';
            action = 'confirm-bulk-milestone';
            body = C.dropdown({
                id: 'bulk-milestone', value: null,
                options: [{ value: null, label: 'No milestone' }, ...state.milestones.filter(m => m.status === 'active').map(m => ({ value: m.id, label: m.title }))],
                placeholder: 'Select milestone', className: 'form-dropdown'
            });
        }

        const footer = `<button class="btn" data-action="close-modal" data-modal="bulk-action-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="${action}" id="bulk-action-submit">Apply</button>`;

        return C.modal({ id: 'bulk-action-modal', title, body, footer });
    }

    function relatedIssueModal(issueId) {
        const state = AppState.getState();
        const issue = AppState.getIssue(issueId);
        const existingRelated = issue ? issue.relatedIssues.map(r => r.issueId) : [];

        const body = `<div class="form-group">
            <label class="field-label">Relationship type</label>
            ${C.dropdown({
                id: 'related-type', value: 'related_to',
                options: [
                    { value: 'related_to', label: 'Related to' },
                    { value: 'blocks', label: 'Blocks' },
                    { value: 'is_blocked_by', label: 'Is blocked by' },
                ],
                className: 'form-dropdown'
            })}
        </div>
        <div class="form-group">
            <label class="field-label">Issue</label>
            ${C.dropdown({
                id: 'related-issue', value: null,
                options: state.issues.filter(i => i.id !== issueId && !existingRelated.includes(i.id))
                    .slice(0, 50).map(i => ({ value: i.id, label: `#${i.id} ${i.title}` })),
                placeholder: 'Select issue', searchable: true, className: 'form-dropdown'
            })}
        </div>`;

        const footer = `<button class="btn" data-action="close-modal" data-modal="related-issue-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="confirm-add-related" data-issue-id="${issueId}">Add relation</button>`;

        return C.modal({ id: 'related-issue-modal', title: 'Add related issue', body, footer });
    }

    return {
        issuesList, issueDetail, newIssueForm,
        labelsView, milestonesView, milestoneDetail,
        boardsView, iterationsView, iterationDetail,
        epicsView, epicDetail,
        roadmapView, notificationsView, timeTrackingView,
        sidebar,
        labelFormModal, milestoneFormModal, iterationFormModal,
        epicFormModal, addBoardListModal, bulkActionModal,
        relatedIssueModal,
    };
})();

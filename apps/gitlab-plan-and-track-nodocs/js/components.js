// GitLab Plan & Track — Reusable UI Components
const Components = (() => {

    // ─── Avatar ───────────────────────────────────────────────────
    function avatar(user, size = 24) {
        if (!user) return '';
        const initials = user.name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
        return `<span class="avatar" style="width:${size}px;height:${size}px;background:${user.avatar_color};font-size:${Math.floor(size * 0.45)}px" title="${_esc(user.name)}" data-user-id="${user.id}">${initials}</span>`;
    }

    function avatarStack(userIds, size = 24, max = 3) {
        const users = userIds.map(id => AppState.getUser(id)).filter(Boolean);
        if (users.length === 0) return '<span class="text-muted">Unassigned</span>';
        let html = '<span class="avatar-stack">';
        users.slice(0, max).forEach(u => { html += avatar(u, size); });
        if (users.length > max) {
            html += `<span class="avatar avatar-more" style="width:${size}px;height:${size}px;font-size:${Math.floor(size * 0.4)}px">+${users.length - max}</span>`;
        }
        html += '</span>';
        return html;
    }

    // ─── Label Badge ──────────────────────────────────────────────
    function labelBadge(label, removable = false, context = '') {
        if (!label) return '';
        const removeBtn = removable ? `<button class="label-remove" data-action="remove-label" data-label-id="${label.id}" data-context="${context}">&times;</button>` : '';
        return `<span class="label-badge" style="background:${label.color};color:${label.textColor}" data-label-id="${label.id}" title="${_esc(label.description || label.name)}">${_esc(label.name)}${removeBtn}</span>`;
    }

    function labelBadges(labelIds, removable = false, context = '') {
        return labelIds.map(id => labelBadge(AppState.getLabel(id), removable, context)).join('');
    }

    // ─── Custom Dropdown ──────────────────────────────────────────
    function dropdown(config) {
        const { id, label, value, options, placeholder, searchable, multi, className } = config;
        const displayValue = value
            ? (Array.isArray(value) ? value.map(v => {
                const opt = options.find(o => o.value === v);
                return opt ? opt.label : v;
            }).join(', ') : (() => { const opt = options.find(o => o.value === value); return opt ? opt.label : value; })())
            : (placeholder || 'Select...');

        let html = `<div class="dropdown-wrapper ${className || ''}" id="${id}-wrapper">`;
        if (label) html += `<label class="dropdown-label">${label}</label>`;
        html += `<div class="custom-dropdown" id="${id}" data-dropdown-id="${id}" data-multi="${!!multi}">`;
        html += `<div class="dropdown-trigger" data-action="toggle-dropdown" data-dropdown="${id}">`;
        html += `<span class="dropdown-value">${_esc(displayValue)}</span>`;
        html += `<span class="dropdown-arrow">&#9662;</span>`;
        html += `</div>`;
        html += `<div class="dropdown-menu" id="${id}-menu">`;
        if (searchable) {
            html += `<div class="dropdown-search"><input type="text" class="dropdown-search-input" data-dropdown="${id}" placeholder="Search..." /></div>`;
        }
        html += `<div class="dropdown-options">`;
        options.forEach(opt => {
            const selected = multi
                ? (Array.isArray(value) && value.includes(opt.value))
                : (value === opt.value);
            const checkMark = selected ? '<span class="dropdown-check">&#10003;</span>' : '<span class="dropdown-check"></span>';
            const colorSwatch = opt.color ? `<span class="color-swatch" style="background:${opt.color}"></span>` : '';
            const avatarHtml = opt.avatar ? avatar(opt.avatar, 20) : '';
            html += `<div class="dropdown-item${selected ? ' selected' : ''}" data-action="select-dropdown-item" data-dropdown="${id}" data-value="${opt.value}" data-label="${_esc(opt.label)}">${checkMark}${colorSwatch}${avatarHtml}<span class="dropdown-item-label">${_esc(opt.label)}</span></div>`;
        });
        if (options.length === 0) {
            html += `<div class="dropdown-empty">No options</div>`;
        }
        html += `</div></div></div>`;
        html += `</div>`;
        return html;
    }

    // ─── Custom Date Picker ───────────────────────────────────────
    function datePicker(config) {
        const { id, label, value, placeholder } = config;
        let html = `<div class="date-picker-wrapper" id="${id}-wrapper">`;
        if (label) html += `<label class="field-label">${label}</label>`;
        html += `<div class="date-picker" id="${id}">`;
        html += `<input type="text" class="date-input" id="${id}-input" value="${value || ''}" placeholder="${placeholder || 'YYYY-MM-DD'}" data-action="date-input" data-picker="${id}" />`;
        html += `<button class="date-clear" data-action="clear-date" data-picker="${id}" title="Clear date">&times;</button>`;
        html += `</div>`;
        html += `</div>`;
        return html;
    }

    // ─── Modal Dialog ─────────────────────────────────────────────
    function modal(config) {
        const { id, title, body, footer, size } = config;
        return `<div class="modal-overlay" id="${id}" data-action="close-modal-overlay" data-modal="${id}">
            <div class="modal ${size ? 'modal-' + size : ''}" onclick="event.stopPropagation()">
                <div class="modal-header">
                    <h3>${title}</h3>
                    <button class="modal-close" data-action="close-modal" data-modal="${id}">&times;</button>
                </div>
                <div class="modal-body">${body}</div>
                ${footer ? `<div class="modal-footer">${footer}</div>` : ''}
            </div>
        </div>`;
    }

    // ─── Toast ────────────────────────────────────────────────────
    function toast(message, type = 'info') {
        if (!message) return '';
        const icons = { info: 'i', success: '\u2713', warning: '!', error: '\u2717' };
        return `<div class="toast toast-${type}"><span class="toast-icon">${icons[type] || 'i'}</span><span class="toast-message">${_esc(message)}</span></div>`;
    }

    // ─── Progress Bar ─────────────────────────────────────────────
    function progressBar(percent, showLabel = true) {
        return `<div class="progress-bar">
            <div class="progress-fill" style="width:${percent}%"></div>
            ${showLabel ? `<span class="progress-label">${percent}%</span>` : ''}
        </div>`;
    }

    // ─── Time Tracking Bar ────────────────────────────────────────
    function timeTrackingBar(estimate, spent) {
        if (!estimate && !spent) return '<span class="text-muted">No time tracking</span>';
        const estimateStr = AppState.formatTime(estimate);
        const spentStr = AppState.formatTime(spent);
        const percent = estimate > 0 ? Math.min(100, Math.round((spent / estimate) * 100)) : (spent > 0 ? 100 : 0);
        const overBudget = spent > estimate && estimate > 0;
        return `<div class="time-tracking">
            <div class="time-tracking-bar">
                <div class="time-tracking-fill${overBudget ? ' over-budget' : ''}" style="width:${percent}%"></div>
            </div>
            <div class="time-tracking-labels">
                <span>Spent: ${spentStr}</span>
                <span>Est: ${estimateStr}</span>
            </div>
        </div>`;
    }

    // ─── Status Badge ─────────────────────────────────────────────
    function statusBadge(status) {
        const cls = status === 'open' ? 'status-open' : 'status-closed';
        const icon = status === 'open' ? '\u25CB' : '\u25CF';
        return `<span class="status-badge ${cls}">${icon} ${status.charAt(0).toUpperCase() + status.slice(1)}</span>`;
    }

    function issueTypeBadge(type) {
        const icons = { issue: '\u25CB', incident: '\u26A0', task: '\u2713' };
        return `<span class="issue-type-badge issue-type-${type}">${icons[type] || '\u25CB'} ${type}</span>`;
    }

    // ─── Pagination ───────────────────────────────────────────────
    function pagination(page, totalPages, total) {
        if (totalPages <= 1) return '';
        let html = `<div class="pagination">`;
        html += `<span class="pagination-info">Showing ${((page - 1) * 20) + 1}\u2013${Math.min(page * 20, total)} of ${total}</span>`;
        html += `<div class="pagination-controls">`;
        html += `<button class="btn btn-sm" data-action="page" data-page="${page - 1}" ${page <= 1 ? 'disabled' : ''}>&laquo; Prev</button>`;

        const range = _paginationRange(page, totalPages);
        range.forEach(p => {
            if (p === '...') {
                html += `<span class="pagination-ellipsis">...</span>`;
            } else {
                html += `<button class="btn btn-sm${p === page ? ' btn-active' : ''}" data-action="page" data-page="${p}">${p}</button>`;
            }
        });

        html += `<button class="btn btn-sm" data-action="page" data-page="${page + 1}" ${page >= totalPages ? 'disabled' : ''}>Next &raquo;</button>`;
        html += `</div></div>`;
        return html;
    }

    function _paginationRange(current, total) {
        if (total <= 7) return Array.from({ length: total }, (_, i) => i + 1);
        const range = [];
        range.push(1);
        if (current > 3) range.push('...');
        for (let i = Math.max(2, current - 1); i <= Math.min(total - 1, current + 1); i++) {
            range.push(i);
        }
        if (current < total - 2) range.push('...');
        range.push(total);
        return range;
    }

    // ─── Issue Row ────────────────────────────────────────────────
    function issueRow(issue) {
        const author = AppState.getUser(issue.authorId);
        const milestone = issue.milestoneId ? AppState.getMilestone(issue.milestoneId) : null;
        const dueDate = issue.dueDate ? _formatDate(issue.dueDate) : '';
        const isOverdue = issue.dueDate && issue.status === 'open' && new Date(issue.dueDate) < new Date();

        let html = `<tr class="issue-row" data-action="view-issue" data-issue-id="${issue.id}">`;
        html += `<td class="issue-checkbox-cell"><input type="checkbox" class="issue-checkbox" data-issue-id="${issue.id}" onclick="event.stopPropagation()" /></td>`;
        html += `<td class="issue-title-cell">
            <div class="issue-title-row">
                ${issue.confidential ? '<span class="confidential-icon" title="Confidential">&#128274;</span>' : ''}
                <span class="issue-title-text">${_esc(issue.title)}</span>
                <span class="issue-id">#${issue.id}</span>
            </div>
            <div class="issue-meta-row">
                ${labelBadges(issue.labelIds.slice(0, 5))}
                ${issue.labelIds.length > 5 ? `<span class="label-more">+${issue.labelIds.length - 5}</span>` : ''}
            </div>
        </td>`;
        html += `<td class="issue-status-cell">${statusBadge(issue.status)}</td>`;
        html += `<td class="issue-assignee-cell">${avatarStack(issue.assigneeIds, 22, 2)}</td>`;
        html += `<td class="issue-milestone-cell">${milestone ? _esc(milestone.title) : ''}</td>`;
        html += `<td class="issue-weight-cell">${issue.weight || ''}</td>`;
        html += `<td class="issue-due-cell${isOverdue ? ' overdue' : ''}">${dueDate}</td>`;
        html += `<td class="issue-created-cell">${_formatDate(issue.createdAt)}</td>`;
        html += `</tr>`;
        return html;
    }

    // ─── Issue Card (for boards) ──────────────────────────────────
    function issueCard(issue) {
        return `<div class="board-card" draggable="true" data-issue-id="${issue.id}" data-action="view-issue">
            <div class="board-card-header">
                ${issue.confidential ? '<span class="confidential-icon">&#128274;</span>' : ''}
                <span class="board-card-title">${_esc(issue.title)}</span>
            </div>
            <div class="board-card-labels">${labelBadges(issue.labelIds.filter(lid => {
                const l = AppState.getLabel(lid);
                return l && !l.name.startsWith('status::');
            }).slice(0, 3))}</div>
            <div class="board-card-footer">
                <span class="board-card-id">#${issue.id}</span>
                ${issue.weight ? `<span class="board-card-weight" title="Weight">\u2696 ${issue.weight}</span>` : ''}
                <span class="board-card-assignees">${avatarStack(issue.assigneeIds, 20, 2)}</span>
            </div>
        </div>`;
    }

    // ─── Color Picker ─────────────────────────────────────────────
    function colorPicker(id, selectedColor) {
        const colors = [
            '#d9534f', '#e24329', '#fc6d26', '#fca326', '#f0ad4e',
            '#5cb85c', '#1aaa55', '#2da160', '#1abc9c', '#428bca',
            '#1f75cb', '#6b4fbb', '#9b59b6', '#e44d2a', '#34495e',
            '#7f8c8d', '#95a5a6', '#c0392b', '#e67e22', '#3498db',
        ];
        let html = `<div class="color-picker" id="${id}">`;
        colors.forEach(c => {
            html += `<button class="color-swatch-btn${c === selectedColor ? ' selected' : ''}" data-action="select-color" data-color="${c}" data-picker="${id}" style="background:${c}"></button>`;
        });
        html += `<div class="color-custom"><input type="text" class="color-input" id="${id}-input" value="${selectedColor || '#428bca'}" placeholder="#hex" data-action="color-input" data-picker="${id}" /></div>`;
        html += `</div>`;
        return html;
    }

    // ─── Tabs ─────────────────────────────────────────────────────
    function tabs(items, activeId) {
        let html = `<div class="tabs">`;
        items.forEach(item => {
            html += `<button class="tab${item.id === activeId ? ' active' : ''}" data-action="switch-tab" data-tab="${item.id}">${item.label}${item.count !== undefined ? ` <span class="tab-count">${item.count}</span>` : ''}</button>`;
        });
        html += `</div>`;
        return html;
    }

    // ─── Empty State ──────────────────────────────────────────────
    function emptyState(message, actionLabel, actionData) {
        let html = `<div class="empty-state">`;
        html += `<div class="empty-state-icon">\u2690</div>`;
        html += `<p class="empty-state-message">${message}</p>`;
        if (actionLabel) {
            html += `<button class="btn btn-primary" ${actionData || ''}>${actionLabel}</button>`;
        }
        html += `</div>`;
        return html;
    }

    // ─── Confirm Dialog ───────────────────────────────────────────
    function confirmDialog(id, title, message, confirmLabel, confirmAction) {
        return modal({
            id,
            title,
            body: `<p>${message}</p>`,
            footer: `<button class="btn" data-action="close-modal" data-modal="${id}">Cancel</button>
                     <button class="btn btn-danger" data-action="${confirmAction}" data-modal="${id}">${confirmLabel}</button>`,
        });
    }

    // ─── Sidebar Section ──────────────────────────────────────────
    function sidebarSection(title, content, collapsible = false) {
        return `<div class="sidebar-section">
            <div class="sidebar-section-header">${title}</div>
            <div class="sidebar-section-content">${content}</div>
        </div>`;
    }

    // ─── Helpers ──────────────────────────────────────────────────
    function _esc(str) {
        if (str == null) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    function _formatDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return `${months[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;
    }

    function _formatDateTime(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const hours = d.getHours().toString().padStart(2, '0');
        const minutes = d.getMinutes().toString().padStart(2, '0');
        return `${months[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()} ${hours}:${minutes}`;
    }

    function _timeAgo(dateStr) {
        const now = new Date();
        const d = new Date(dateStr);
        const diff = Math.floor((now - d) / 1000);
        if (diff < 60) return 'just now';
        if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
        if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`;
        if (diff < 2592000) return `${Math.floor(diff / 86400)}d ago`;
        return _formatDate(dateStr);
    }

    function renderMarkdown(text) {
        if (!text) return '';
        let html = _esc(text);
        // Code blocks
        html = html.replace(/```(\w*)\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
        // Inline code
        html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
        // Bold
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        // Italic
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
        // Headings
        html = html.replace(/^### (.+)$/gm, '<h4>$1</h4>');
        html = html.replace(/^## (.+)$/gm, '<h3>$1</h3>');
        html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');
        // Checklists
        html = html.replace(/- \[x\] (.+)/g, '<div class="checklist-item checked"><span class="check-box">&#9745;</span> $1</div>');
        html = html.replace(/- \[ \] (.+)/g, '<div class="checklist-item"><span class="check-box">&#9744;</span> $1</div>');
        // Lists
        html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
        // Paragraphs
        html = html.replace(/\n\n/g, '</p><p>');
        html = html.replace(/\n/g, '<br>');
        // Mentions
        html = html.replace(/@(\w+)/g, '<span class="mention">@$1</span>');
        // Issue refs
        html = html.replace(/#(\d+)/g, '<span class="issue-ref" data-action="view-issue" data-issue-id="$1">#$1</span>');
        return `<p>${html}</p>`;
    }

    return {
        avatar, avatarStack,
        labelBadge, labelBadges,
        dropdown, datePicker,
        modal, toast, progressBar, timeTrackingBar,
        statusBadge, issueTypeBadge,
        pagination, issueRow, issueCard,
        colorPicker, tabs, emptyState,
        confirmDialog, sidebarSection,
        _esc, _formatDate, _formatDateTime, _timeAgo, renderMarkdown,
    };
})();

// ============================================================
// components.js — Reusable UI components for Clio Matters app
// All functions are pure: read from AppState, return HTML strings.
// No native OS UI elements (<select>, alert(), confirm()).
// ============================================================

/**
 * Escape HTML entities to prevent XSS in rendered content.
 */
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = String(text);
    return div.innerHTML;
}

const Components = {

    // ---- Custom Dropdown (single-select) ----
    // options: [{value, label}], selectedValue: current value, id: unique id
    renderDropdown(id, options, selectedValue, placeholder = 'Select...', searchable = false) {
        const selected = options.find(o => o.value === selectedValue);
        const displayText = selected ? selected.label : placeholder;
        return `
            <div class="custom-dropdown" id="${id}-dropdown" data-dropdown-id="${id}">
                <div class="dropdown-trigger" data-dropdown-trigger="${id}" tabindex="0">
                    <span class="dropdown-value">${escapeHtml(displayText)}</span>
                    <span class="dropdown-arrow">&#9662;</span>
                </div>
                <div class="dropdown-menu" id="${id}-menu">
                    ${searchable ? `<div class="dropdown-search-wrapper"><input type="text" class="dropdown-search" data-dropdown-search="${id}" placeholder="Search..." /></div>` : ''}
                    <div class="dropdown-options">
                        ${options.map(opt => `
                            <div class="dropdown-item ${opt.value === selectedValue ? 'selected' : ''}"
                                 data-dropdown-item="${id}" data-value="${escapeHtml(String(opt.value))}">
                                ${escapeHtml(opt.label)}
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    },

    // ---- Multi-Select Dropdown ----
    // options: [{value, label}], selectedValues: array of selected values
    renderMultiDropdown(id, options, selectedValues = [], placeholder = 'Select...') {
        const selectedLabels = options.filter(o => selectedValues.includes(o.value)).map(o => o.label);
        const displayText = selectedLabels.length > 0 ? selectedLabels.join(', ') : placeholder;
        return `
            <div class="custom-dropdown multi-dropdown" id="${id}-dropdown" data-dropdown-id="${id}">
                <div class="dropdown-trigger" data-dropdown-trigger="${id}" tabindex="0">
                    <span class="dropdown-value">${escapeHtml(displayText)}</span>
                    <span class="dropdown-arrow">&#9662;</span>
                </div>
                <div class="dropdown-menu" id="${id}-menu">
                    <div class="dropdown-options">
                        ${options.map(opt => `
                            <div class="dropdown-item ${selectedValues.includes(opt.value) ? 'selected' : ''}"
                                 data-multi-item="${id}" data-value="${escapeHtml(String(opt.value))}">
                                <span class="custom-checkbox">
                                    <span class="checkmark ${selectedValues.includes(opt.value) ? 'checked' : ''}"></span>
                                </span>
                                ${escapeHtml(opt.label)}
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    },

    // ---- Status Badge ----
    renderStatusBadge(status) {
        return `<span class="matter-status-badge ${escapeHtml(status)}">${escapeHtml(status.charAt(0).toUpperCase() + status.slice(1))}</span>`;
    },

    // ---- Custom Checkbox ----
    renderCheckbox(id, checked = false, label = '') {
        return `
            <label class="custom-checkbox" data-checkbox="${id}">
                <input type="checkbox" ${checked ? 'checked' : ''} style="display:none" />
                <span class="checkmark ${checked ? 'checked' : ''}"></span>
                ${label ? `<span class="checkbox-label">${escapeHtml(label)}</span>` : ''}
            </label>
        `;
    },

    // ---- Toggle Switch ----
    renderToggle(id, active = false, label = '') {
        return `
            <div class="toggle-wrapper">
                ${label ? `<span class="toggle-label">${escapeHtml(label)}</span>` : ''}
                <div class="toggle-switch ${active ? 'active' : ''}" data-toggle="${id}">
                    <div class="toggle-slider"></div>
                </div>
            </div>
        `;
    },

    // ---- Pagination ----
    renderPagination(currentPage, totalPages, totalCount) {
        if (totalPages <= 1) return '';
        const start = (currentPage - 1) * AppState.pageSize + 1;
        const end = Math.min(currentPage * AppState.pageSize, totalCount);

        let pages = [];
        for (let i = 1; i <= totalPages; i++) {
            if (i === 1 || i === totalPages || (i >= currentPage - 2 && i <= currentPage + 2)) {
                pages.push(i);
            } else if (pages[pages.length - 1] !== '...') {
                pages.push('...');
            }
        }

        return `
            <div class="pagination">
                <span class="pagination-info">Showing ${start}\u2013${end} of ${totalCount}</span>
                <div class="pagination-controls">
                    <button class="btn btn-sm btn-secondary" data-action="prev-page" ${currentPage === 1 ? 'disabled' : ''}>&#8249; Prev</button>
                    ${pages.map(p => p === '...'
                        ? '<span class="pagination-ellipsis">...</span>'
                        : `<button class="btn btn-sm ${p === currentPage ? 'btn-primary' : 'btn-secondary'}" data-action="goto-page" data-page="${p}">${p}</button>`
                    ).join('')}
                    <button class="btn btn-sm btn-secondary" data-action="next-page" ${currentPage === totalPages ? 'disabled' : ''}>Next &#8250;</button>
                </div>
            </div>
        `;
    },

    // ---- Toast Notification ----
    renderToast(message, type = 'info') {
        const id = 'toast_' + Date.now();
        return `
            <div class="toast ${escapeHtml(type)}" id="${id}">
                <span class="toast-message">${escapeHtml(message)}</span>
                <button class="toast-close" data-action="close-toast" data-toast-id="${id}">&times;</button>
            </div>
        `;
    },

    // ---- Search Input ----
    renderSearchInput(value = '', placeholder = 'Search matters...') {
        return `
            <div class="search-input-wrapper">
                <span class="search-icon">&#128269;</span>
                <input type="text" class="search-input" id="matters-search"
                    value="${escapeHtml(value)}" placeholder="${escapeHtml(placeholder)}"
                    data-action="search-input" />
                ${value ? '<button class="search-clear" data-action="clear-search">&times;</button>' : ''}
            </div>
        `;
    },

    // ---- User Avatar ----
    renderAvatar(user, size = 'md') {
        if (!user) return '<span class="avatar avatar-' + escapeHtml(size) + '" style="background:#ccc">?</span>';
        const initials = user.name.split(' ').map(n => n[0]).join('').substring(0, 2);
        return `<span class="avatar avatar-${escapeHtml(size)}" style="background:${escapeHtml(user.avatarColor || '#4A90D9')}" title="${escapeHtml(user.name)}">${escapeHtml(initials)}</span>`;
    },

    // ---- Breadcrumb Navigation ----
    renderBreadcrumb(items) {
        // items: [{label, route}] — last item has no route (current page)
        return `
            <nav class="breadcrumb">
                ${items.map((item, i) => {
                    if (i === items.length - 1) {
                        return `<span class="breadcrumb-item active">${escapeHtml(item.label)}</span>`;
                    }
                    return `<span class="breadcrumb-item"><a data-route="${escapeHtml(item.route)}">${escapeHtml(item.label)}</a></span>
                            <span class="breadcrumb-separator">/</span>`;
                }).join('')}
            </nav>
        `;
    },

    // ---- Info / Warning / Error / Success Boxes ----
    renderInfoBox(message) {
        return `<div class="info-box"><span class="box-icon">i</span> ${message}</div>`;
    },

    renderWarningBox(message) {
        return `<div class="warning-box"><span class="box-icon">!</span> ${message}</div>`;
    },

    renderErrorBox(message) {
        return `<div class="error-box"><span class="box-icon">x</span> ${message}</div>`;
    },

    renderSuccessBox(message) {
        return `<div class="success-box"><span class="box-icon">&#10003;</span> ${message}</div>`;
    },

    // ---- Empty State ----
    renderEmptyState(icon, title, description, actionLabel = '', actionRoute = '') {
        return `
            <div class="empty-state">
                <div class="empty-state-icon">${icon}</div>
                <div class="empty-state-title">${escapeHtml(title)}</div>
                <div class="empty-state-text">${escapeHtml(description)}</div>
                ${actionLabel ? `<button class="btn btn-primary" data-route="${escapeHtml(actionRoute)}">${escapeHtml(actionLabel)}</button>` : ''}
            </div>
        `;
    },

    // ---- Confirmation Modal ----
    // Returns an object {title, body, footer} for the modal renderer
    renderConfirmModal(title, message, confirmLabel = 'Confirm', confirmClass = 'btn-danger') {
        return {
            title: title,
            body: `<p>${escapeHtml(message)}</p>`,
            footer: `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn ${escapeHtml(confirmClass)}" data-action="confirm-modal">${escapeHtml(confirmLabel)}</button>
            `
        };
    },

    // ---- Collapsible Form Section ----
    renderFormSection(id, title, content, expanded = true) {
        return `
            <div class="form-section" id="section-${id}">
                <div class="form-section-header" data-action="toggle-section" data-section="${id}">
                    <span class="section-toggle">${expanded ? '&#9660;' : '&#9654;'}</span>
                    <h3>${escapeHtml(title)}</h3>
                </div>
                <div class="form-section-body" style="${expanded ? '' : 'display:none'}">
                    ${content}
                </div>
            </div>
        `;
    },

    // ---- Tag ----
    renderTag(text, removable = false, dataAttr = '') {
        return `
            <span class="tag ${removable ? 'removable' : ''}" ${dataAttr}>
                ${escapeHtml(text)}
                ${removable ? `<button class="tag-remove" ${dataAttr} data-action="remove-tag">&times;</button>` : ''}
            </span>
        `;
    },

    // ---- Currency Formatting ----
    renderCurrency(amount, currency = 'USD') {
        if (amount === null || amount === undefined) return '<span class="currency-amount">\u2014</span>';
        const formatted = new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(amount);
        const cls = amount < 0 ? 'negative' : (amount > 0 ? 'positive' : '');
        return `<span class="currency-amount ${cls}">${formatted}</span>`;
    },

    // ---- Progress / Budget Bar ----
    renderProgressBar(current, total, label = '') {
        if (!total) return '';
        const pct = Math.min(100, Math.round((current / total) * 100));
        const overBudget = pct >= 100;
        return `
            <div class="budget-bar-wrapper">
                ${label ? `<div class="budget-bar-label">${escapeHtml(label)}</div>` : ''}
                <div class="budget-bar">
                    <div class="budget-bar-fill ${overBudget ? 'over-budget' : ''}" style="width:${pct}%"></div>
                </div>
                <div class="budget-bar-text">${Components.renderCurrency(current)} / ${Components.renderCurrency(total)} (${pct}%)</div>
            </div>
        `;
    },

    // ---- Date Formatting ----
    formatDate(dateStr) {
        if (!dateStr) return '\u2014';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    },

    formatDateTime(dateStr) {
        if (!dateStr) return '\u2014';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' });
    },

    // ---- Data Table ----
    // columns: [{key, label, width?, sortable?, render?}], rows: array of objects
    // options: {selectable, selectedIds, emptyMessage, tableClass}
    renderTable(columns, rows, options = {}) {
        const { selectable, selectedIds, emptyMessage, tableClass } = {
            selectable: false,
            selectedIds: [],
            emptyMessage: 'No items found',
            tableClass: 'data-table',
            ...options
        };

        if (rows.length === 0) {
            return Components.renderEmptyState('&#128196;', emptyMessage, '');
        }

        return `
            <table class="${escapeHtml(tableClass)}">
                <thead>
                    <tr>
                        ${selectable ? `
                            <th class="checkbox-cell">
                                <label class="custom-checkbox select-all-checkbox" data-action="select-all">
                                    <input type="checkbox" style="display:none" />
                                    <span class="checkmark ${selectedIds.length === rows.length && rows.length > 0 ? 'checked' : ''}"></span>
                                </label>
                            </th>
                        ` : ''}
                        ${columns.map(col => `
                            <th ${col.width ? `style="width:${col.width}"` : ''}
                                ${col.sortable ? `class="sortable" data-action="sort" data-sort-field="${escapeHtml(col.key)}"` : ''}>
                                ${escapeHtml(col.label)}
                                ${col.sortable && AppState.sortField === col.key
                                    ? (AppState.sortDirection === 'asc' ? ' &#9650;' : ' &#9660;')
                                    : ''}
                            </th>
                        `).join('')}
                    </tr>
                </thead>
                <tbody>
                    ${rows.map(row => `
                        <tr class="${selectedIds.includes(row.id) ? 'selected' : ''}" data-row-id="${row.id}">
                            ${selectable ? `
                                <td class="checkbox-cell">
                                    <label class="custom-checkbox" data-action="select-row" data-id="${row.id}">
                                        <input type="checkbox" style="display:none" />
                                        <span class="checkmark ${selectedIds.includes(row.id) ? 'checked' : ''}"></span>
                                    </label>
                                </td>
                            ` : ''}
                            ${columns.map(col => `
                                <td>${col.render ? col.render(row) : escapeHtml(String(row[col.key] || ''))}</td>
                            `).join('')}
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    }
};

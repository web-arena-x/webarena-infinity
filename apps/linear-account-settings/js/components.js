// ============================================================
// components.js — Reusable UI components
// ============================================================

const Components = {

    // ---- Utility functions ----

    escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    },

    escapeAttr(str) {
        if (!str) return '';
        return String(str).replace(/"/g, '&quot;').replace(/'/g, '&#039;');
    },

    formatDate(isoStr) {
        if (!isoStr) return 'Never';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    },

    formatDateTime(isoStr) {
        if (!isoStr) return 'Never';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', {
            year: 'numeric', month: 'short', day: 'numeric',
            hour: '2-digit', minute: '2-digit'
        });
    },

    timeAgo(isoStr) {
        if (!isoStr) return 'Never';
        const now = new Date();
        const d = new Date(isoStr);
        const diffMs = now - d;
        const diffMins = Math.floor(diffMs / 60000);
        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins}m ago`;
        const diffHrs = Math.floor(diffMins / 60);
        if (diffHrs < 24) return `${diffHrs}h ago`;
        const diffDays = Math.floor(diffHrs / 24);
        if (diffDays < 30) return `${diffDays}d ago`;
        const diffMonths = Math.floor(diffDays / 30);
        if (diffMonths < 12) return `${diffMonths}mo ago`;
        return `${Math.floor(diffMonths / 12)}y ago`;
    },

    // ---- Avatar ----

    avatar(user, size = 32) {
        const initials = (user.name || user.username || '?').split(' ').map(w => w[0]).join('').substring(0, 2).toUpperCase();
        const color = user.avatarColor || '#5E6AD2';
        return `<div class="avatar" style="width:${size}px;height:${size}px;background:${color};font-size:${Math.floor(size * 0.4)}px" data-testid="avatar-${Components.escapeAttr(user.username || user.id)}">${initials}</div>`;
    },

    // ---- Custom Dropdown ----

    dropdown(id, options, selectedValue, opts = {}) {
        const label = opts.label || '';
        const placeholder = opts.placeholder || 'Select...';
        const selected = options.find(o => (o.id || o) === selectedValue);
        const displayText = selected ? (selected.name || selected) : placeholder;
        const disabled = opts.disabled || false;

        let html = '';
        if (label) {
            html += `<label class="form-label" for="${id}">${Components.escapeHtml(label)}</label>`;
        }
        html += `<div class="custom-dropdown ${disabled ? 'disabled' : ''}" id="${id}" data-testid="dropdown-${id}" data-value="${Components.escapeAttr(selectedValue || '')}">`;
        html += `<div class="dropdown-trigger" data-testid="dropdown-trigger-${id}">${Components.escapeHtml(displayText)}<span class="dropdown-arrow">&#9662;</span></div>`;
        html += `<div class="dropdown-menu" data-testid="dropdown-menu-${id}">`;
        for (const opt of options) {
            const val = opt.id || opt;
            const name = opt.name || opt;
            const isSelected = val === selectedValue;
            html += `<div class="dropdown-item ${isSelected ? 'selected' : ''}" data-value="${Components.escapeAttr(val)}" data-testid="dropdown-option-${Components.escapeAttr(val)}">${Components.escapeHtml(name)}</div>`;
        }
        html += '</div></div>';
        return html;
    },

    // ---- Toggle Switch ----

    toggle(id, checked, opts = {}) {
        const label = opts.label || '';
        const description = opts.description || '';
        const disabled = opts.disabled || false;
        let html = `<div class="toggle-row" data-testid="toggle-row-${id}">`;
        html += `<div class="toggle-info">`;
        if (label) html += `<div class="toggle-label">${Components.escapeHtml(label)}</div>`;
        if (description) html += `<div class="toggle-description">${Components.escapeHtml(description)}</div>`;
        html += `</div>`;
        html += `<div class="toggle-switch ${checked ? 'on' : 'off'} ${disabled ? 'disabled' : ''}" id="${id}" data-testid="toggle-${id}" data-checked="${checked}" role="switch" aria-checked="${checked}" tabindex="0">`;
        html += `<div class="toggle-knob"></div>`;
        html += `</div>`;
        html += `</div>`;
        return html;
    },

    // ---- Text Input ----

    textInput(id, value, opts = {}) {
        const label = opts.label || '';
        const placeholder = opts.placeholder || '';
        const type = opts.type || 'text';
        const error = opts.error || '';
        const readonly = opts.readonly || false;
        const maxlength = opts.maxlength || '';

        let html = `<div class="form-field" data-testid="field-${id}">`;
        if (label) html += `<label class="form-label" for="${id}">${Components.escapeHtml(label)}</label>`;
        html += `<input class="form-input ${error ? 'field-error' : ''}" type="${type}" id="${id}" data-testid="input-${id}" value="${Components.escapeAttr(value || '')}" placeholder="${Components.escapeAttr(placeholder)}" ${readonly ? 'readonly' : ''} ${maxlength ? `maxlength="${maxlength}"` : ''} />`;
        if (error) html += `<div class="error-message" data-testid="error-${id}">${Components.escapeHtml(error)}</div>`;
        html += `</div>`;
        return html;
    },

    // ---- Textarea ----

    textarea(id, value, opts = {}) {
        const label = opts.label || '';
        const placeholder = opts.placeholder || '';
        const rows = opts.rows || 3;
        const error = opts.error || '';

        let html = `<div class="form-field" data-testid="field-${id}">`;
        if (label) html += `<label class="form-label" for="${id}">${Components.escapeHtml(label)}</label>`;
        html += `<textarea class="form-textarea ${error ? 'field-error' : ''}" id="${id}" data-testid="textarea-${id}" placeholder="${Components.escapeAttr(placeholder)}" rows="${rows}">${Components.escapeHtml(value || '')}</textarea>`;
        if (error) html += `<div class="error-message" data-testid="error-${id}">${Components.escapeHtml(error)}</div>`;
        html += `</div>`;
        return html;
    },

    // ---- Modal ----

    showModal(title, bodyHtml, footerHtml) {
        const overlay = document.getElementById('modalOverlay');
        const titleEl = document.getElementById('modalTitle');
        const bodyEl = document.getElementById('modalBody');
        const footerEl = document.getElementById('modalFooter');

        titleEl.textContent = title;
        bodyEl.innerHTML = bodyHtml;
        footerEl.innerHTML = footerHtml || '';
        overlay.style.display = 'flex';
        AppState.modalOpen = true;
    },

    closeModal() {
        const overlay = document.getElementById('modalOverlay');
        overlay.style.display = 'none';
        AppState.modalOpen = false;
    },

    // ---- Confirm Dialog ----

    confirm(title, message, onConfirm, opts = {}) {
        const isDanger = opts.danger || false;
        const confirmText = opts.confirmText || 'Confirm';
        const cancelText = opts.cancelText || 'Cancel';

        const bodyHtml = `<p style="color:var(--color-text-secondary);margin:0">${Components.escapeHtml(message)}</p>`;
        const footerHtml = `
            <button class="btn btn-secondary" data-action="modal-cancel" data-testid="modal-cancel">${Components.escapeHtml(cancelText)}</button>
            <button class="btn ${isDanger ? 'btn-danger' : 'btn-primary'}" data-action="modal-confirm" data-testid="modal-confirm">${Components.escapeHtml(confirmText)}</button>
        `;

        Components.showModal(title, bodyHtml, footerHtml);

        // Attach handlers
        setTimeout(() => {
            const confirmBtn = document.querySelector('[data-action="modal-confirm"]');
            const cancelBtn = document.querySelector('[data-action="modal-cancel"]');
            if (confirmBtn) confirmBtn.onclick = () => { Components.closeModal(); onConfirm(); };
            if (cancelBtn) cancelBtn.onclick = () => Components.closeModal();
        }, 0);
    },

    // ---- Toast ----

    showToast(message, type = 'success', duration = 3000) {
        const container = document.getElementById('toastContainer');
        if (!container) return;
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        const icons = { success: '&#10003;', error: '&#10007;', warning: '&#9888;', info: '&#8505;' };
        toast.innerHTML = `<span class="toast-icon">${icons[type] || ''}</span><span class="toast-message">${Components.escapeHtml(message)}</span>`;
        container.appendChild(toast);
        setTimeout(() => { toast.classList.add('toast-fade'); }, duration - 300);
        setTimeout(() => { if (toast.parentNode) toast.parentNode.removeChild(toast); }, duration);
    },

    // ---- Status Badge ----

    statusBadge(status) {
        const colors = {
            enabled: 'var(--color-success)',
            disabled: 'var(--color-text-tertiary)',
            active: 'var(--color-success)',
            inactive: 'var(--color-text-tertiary)'
        };
        const color = colors[status] || 'var(--color-text-tertiary)';
        return `<span class="status-dot" style="background:${color}" data-testid="status-${status}"></span>`;
    },

    // ---- Permission Badge ----

    permissionBadge(permission) {
        return `<span class="permission-badge" data-testid="permission-${Components.escapeAttr(permission)}">${Components.escapeHtml(permission)}</span>`;
    },

    // ---- Section Header ----

    sectionHeader(title, opts = {}) {
        const description = opts.description || '';
        const action = opts.action || '';
        let html = `<div class="section-header" data-testid="section-${title.toLowerCase().replace(/[^a-z0-9]+/g, '-')}">`;
        html += `<div class="section-header-info">`;
        html += `<h2 class="section-title">${Components.escapeHtml(title)}</h2>`;
        if (description) html += `<p class="section-description">${Components.escapeHtml(description)}</p>`;
        html += `</div>`;
        if (action) html += `<div class="section-header-action">${action}</div>`;
        html += `</div>`;
        return html;
    },

    // ---- Info / Warning Box ----

    infoBox(message) {
        return `<div class="info-box" data-testid="info-box"><span class="box-icon">&#8505;</span> ${Components.escapeHtml(message)}</div>`;
    },

    warningBox(message) {
        return `<div class="warning-box" data-testid="warning-box"><span class="box-icon">&#9888;</span> ${Components.escapeHtml(message)}</div>`;
    },

    // ---- Empty State ----

    emptyState(message, opts = {}) {
        const icon = opts.icon || '';
        const action = opts.action || '';
        let html = `<div class="empty-state" data-testid="empty-state">`;
        if (icon) html += `<div class="empty-state-icon">${icon}</div>`;
        html += `<p>${Components.escapeHtml(message)}</p>`;
        if (action) html += action;
        html += `</div>`;
        return html;
    },

    // ---- Breadcrumb ----

    renderBreadcrumb(items) {
        let html = '';
        items.forEach((item, i) => {
            if (i > 0) html += '<span class="breadcrumb-sep">/</span>';
            if (item.route) {
                html += `<a class="breadcrumb-link" data-route="${Components.escapeAttr(item.route)}">${Components.escapeHtml(item.label)}</a>`;
            } else {
                html += `<span class="breadcrumb-current">${Components.escapeHtml(item.label)}</span>`;
            }
        });
        return html;
    }
};

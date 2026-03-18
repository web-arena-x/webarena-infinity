/* components.js — Reusable UI components for Gmail Accounts & Contacts */

const Components = {

    // ─── Escaping ───
    escapeHtml(str) {
        if (str == null) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    },

    escapeAttr(str) {
        return this.escapeHtml(str);
    },

    // ─── Formatting ───
    formatDate(iso) {
        if (!iso) return '';
        const d = new Date(iso);
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return `${months[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;
    },

    formatDateTime(iso) {
        if (!iso) return '';
        const d = new Date(iso);
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const h = d.getHours();
        const m = String(d.getMinutes()).padStart(2, '0');
        const ampm = h >= 12 ? 'PM' : 'AM';
        const h12 = h % 12 || 12;
        return `${months[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()} ${h12}:${m} ${ampm}`;
    },

    timeAgo(iso) {
        if (!iso) return '';
        const now = new Date();
        const d = new Date(iso);
        const diffMs = now - d;
        const diffSec = Math.floor(diffMs / 1000);
        const diffMin = Math.floor(diffSec / 60);
        const diffHr = Math.floor(diffMin / 60);
        const diffDay = Math.floor(diffHr / 24);
        if (diffDay > 30) return this.formatDate(iso);
        if (diffDay > 0) return diffDay + 'd ago';
        if (diffHr > 0) return diffHr + 'h ago';
        if (diffMin > 0) return diffMin + 'm ago';
        return 'just now';
    },

    // ─── Avatar ───
    avatar(name, size, color) {
        size = size || 32;
        color = color || '#1a73e8';
        const initials = (name || '?').split(' ').map(w => w[0] || '').join('').toUpperCase().slice(0, 2);
        return `<span class="avatar" style="width:${size}px;height:${size}px;line-height:${size}px;font-size:${Math.round(size * 0.4)}px;background:${color}">${this.escapeHtml(initials)}</span>`;
    },

    avatarColors: ['#1a73e8', '#ea4335', '#34a853', '#fbbc04', '#4285f4', '#e8710a', '#9334e6', '#f538a0', '#00897b', '#5f6368'],

    getAvatarColor(str) {
        let hash = 0;
        for (let i = 0; i < (str || '').length; i++) {
            hash = str.charCodeAt(i) + ((hash << 5) - hash);
        }
        return this.avatarColors[Math.abs(hash) % this.avatarColors.length];
    },

    // ─── Form Components ───
    textInput(id, value, placeholder, label, type) {
        type = type || 'text';
        let html = '';
        if (label) html += `<label class="form-label" for="${this.escapeAttr(id)}">${this.escapeHtml(label)}</label>`;
        html += `<input type="${type}" class="form-input" id="${this.escapeAttr(id)}" value="${this.escapeAttr(value || '')}" placeholder="${this.escapeAttr(placeholder || '')}" data-testid="${this.escapeAttr(id)}">`;
        return html;
    },

    textarea(id, value, placeholder, label, rows) {
        rows = rows || 3;
        let html = '';
        if (label) html += `<label class="form-label" for="${this.escapeAttr(id)}">${this.escapeHtml(label)}</label>`;
        html += `<textarea class="form-textarea" id="${this.escapeAttr(id)}" rows="${rows}" placeholder="${this.escapeAttr(placeholder || '')}" data-testid="${this.escapeAttr(id)}">${this.escapeHtml(value || '')}</textarea>`;
        return html;
    },

    dropdown(id, options, selectedValue, placeholder) {
        const selectedOpt = options.find(o => o.value === selectedValue);
        const displayText = selectedOpt ? selectedOpt.label : (placeholder || 'Select...');
        let html = `<div class="custom-dropdown" id="${this.escapeAttr(id)}" data-testid="${this.escapeAttr(id)}">`;
        html += `<div class="dropdown-trigger" data-dropdown-trigger="${this.escapeAttr(id)}">${this.escapeHtml(displayText)}<span class="dropdown-arrow">&#9662;</span></div>`;
        html += `<div class="dropdown-menu" id="${this.escapeAttr(id)}-menu" style="display:none">`;
        options.forEach(opt => {
            const sel = opt.value === selectedValue ? ' selected' : '';
            html += `<div class="dropdown-item${sel}" data-dropdown-item data-dropdown-id="${this.escapeAttr(id)}" data-value="${this.escapeAttr(opt.value)}">${this.escapeHtml(opt.label)}</div>`;
        });
        html += '</div></div>';
        return html;
    },

    toggle(id, checked, label, description) {
        let html = `<div class="toggle-row" data-testid="${this.escapeAttr(id)}-toggle">`;
        html += '<div class="toggle-info">';
        if (label) html += `<span class="toggle-label">${this.escapeHtml(label)}</span>`;
        if (description) html += `<span class="toggle-description">${this.escapeHtml(description)}</span>`;
        html += '</div>';
        html += `<label class="toggle-switch"><input type="checkbox" id="${this.escapeAttr(id)}" ${checked ? 'checked' : ''} data-toggle="${this.escapeAttr(id)}"><span class="toggle-slider"></span></label>`;
        html += '</div>';
        return html;
    },

    checkbox(id, checked, label) {
        let html = `<label class="checkbox-label" data-testid="${this.escapeAttr(id)}-checkbox">`;
        html += `<input type="checkbox" id="${this.escapeAttr(id)}" ${checked ? 'checked' : ''}>`;
        html += `<span class="checkbox-text">${this.escapeHtml(label)}</span></label>`;
        return html;
    },

    radioGroup(name, options, selectedValue) {
        let html = '<div class="radio-group">';
        options.forEach(opt => {
            const checked = opt.value === selectedValue ? ' checked' : '';
            html += `<label class="radio-label" data-testid="${this.escapeAttr(name)}-${this.escapeAttr(opt.value)}">`;
            html += `<input type="radio" name="${this.escapeAttr(name)}" value="${this.escapeAttr(opt.value)}"${checked}>`;
            html += `<span class="radio-text">${this.escapeHtml(opt.label)}</span>`;
            if (opt.description) html += `<span class="radio-description">${this.escapeHtml(opt.description)}</span>`;
            html += '</label>';
        });
        html += '</div>';
        return html;
    },

    // ─── Modal System ───
    showModal(title, bodyHtml, footerHtml) {
        document.getElementById('modalTitle').innerHTML = title;
        document.getElementById('modalBody').innerHTML = bodyHtml;
        document.getElementById('modalFooter').innerHTML = footerHtml || '';
        document.getElementById('modalOverlay').style.display = 'flex';
    },

    closeModal() {
        document.getElementById('modalOverlay').style.display = 'none';
        Components._confirmCallback = null;
    },

    _confirmCallback: null,

    confirm(message, onConfirm) {
        this._confirmCallback = onConfirm;
        this.showModal('Confirm', `<p>${this.escapeHtml(message)}</p>`,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="confirm-modal">Confirm</button>');
    },

    confirmDanger(message, onConfirm) {
        this._confirmCallback = onConfirm;
        this.showModal('Confirm', `<p>${this.escapeHtml(message)}</p>`,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-danger" data-action="confirm-modal">Delete</button>');
    },

    // ─── Toast Notifications ───
    showToast(message, type) {
        type = type || 'info';
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = 'toast toast-' + type;
        toast.textContent = message;
        container.appendChild(toast);
        setTimeout(() => {
            toast.classList.add('toast-fade');
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    },

    // ─── Empty State ───
    emptyState(icon, title, description, actionHtml) {
        let html = '<div class="empty-state">';
        if (icon) html += `<div class="empty-icon">${icon}</div>`;
        html += `<h3>${this.escapeHtml(title)}</h3>`;
        if (description) html += `<p>${this.escapeHtml(description)}</p>`;
        if (actionHtml) html += actionHtml;
        html += '</div>';
        return html;
    },

    // ─── Pagination ───
    pagination(currentPage, totalItems, pageSize) {
        const totalPages = Math.ceil(totalItems / pageSize);
        if (totalPages <= 1) return '';
        const start = (currentPage - 1) * pageSize + 1;
        const end = Math.min(currentPage * pageSize, totalItems);

        let html = '<div class="pagination">';
        html += `<span class="pagination-info">Showing ${start}\u2013${end} of ${totalItems}</span>`;
        html += '<div class="pagination-buttons">';
        html += `<button class="btn btn-sm" data-action="prev-page" ${currentPage <= 1 ? 'disabled' : ''}>Prev</button>`;

        const maxVisible = 5;
        let startPage = Math.max(1, currentPage - Math.floor(maxVisible / 2));
        let endPage = Math.min(totalPages, startPage + maxVisible - 1);
        if (endPage - startPage < maxVisible - 1) {
            startPage = Math.max(1, endPage - maxVisible + 1);
        }

        for (let i = startPage; i <= endPage; i++) {
            html += `<button class="btn btn-sm${i === currentPage ? ' btn-active' : ''}" data-action="goto-page" data-page="${i}">${i}</button>`;
        }

        html += `<button class="btn btn-sm" data-action="next-page" ${currentPage >= totalPages ? 'disabled' : ''}>Next</button>`;
        html += '</div></div>';
        return html;
    },

    // ─── Status Badge ───
    statusBadge(status) {
        const cls = status === 'active' ? 'badge-success' : status === 'pending' ? 'badge-warning' : status === 'error' ? 'badge-danger' : 'badge-default';
        return `<span class="badge ${cls}">${this.escapeHtml(status)}</span>`;
    },

    // ─── Group badge ───
    groupBadge(group) {
        if (!group) return '';
        return `<span class="group-badge">${this.escapeHtml(group.name)}</span>`;
    }
};

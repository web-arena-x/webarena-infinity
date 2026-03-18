/* components.js — Reusable UI components for Xero Invoicing */
/* eslint-disable */

const Components = {
    escapeHtml(str) {
        if (str == null) return '';
        return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    },

    escapeAttr(str) {
        return this.escapeHtml(str);
    },

    formatDate(iso) {
        if (!iso) return '\u2014';
        const d = new Date(iso + (iso.includes('T') ? '' : 'T00:00:00'));
        return d.toLocaleDateString('en-NZ', { day: 'numeric', month: 'short', year: 'numeric' });
    },

    formatDateTime(iso) {
        if (!iso) return '\u2014';
        const d = new Date(iso);
        return d.toLocaleDateString('en-NZ', { day: 'numeric', month: 'short', year: 'numeric' }) + ' ' +
            d.toLocaleTimeString('en-NZ', { hour: '2-digit', minute: '2-digit' });
    },

    timeAgo(iso) {
        if (!iso) return '';
        const now = new Date();
        const d = new Date(iso);
        const seconds = Math.floor((now - d) / 1000);
        if (seconds < 60) return 'just now';
        const minutes = Math.floor(seconds / 60);
        if (minutes < 60) return minutes + 'm ago';
        const hours = Math.floor(minutes / 60);
        if (hours < 24) return hours + 'h ago';
        const days = Math.floor(hours / 24);
        if (days < 30) return days + 'd ago';
        const months = Math.floor(days / 30);
        return months + 'mo ago';
    },

    formatCurrency(amount, currency) {
        if (amount == null) return '$0.00';
        const curr = AppState.getCurrencyByCode(currency || 'NZD');
        const sym = curr ? curr.symbol : '$';
        const neg = amount < 0;
        const abs = Math.abs(amount).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        return (neg ? '-' : '') + sym + abs;
    },

    formatNumber(n) {
        if (n == null) return '0';
        return Number(n).toLocaleString('en-NZ');
    },

    statusBadge(status) {
        const map = {
            draft: { label: 'Draft', cls: 'status-draft' },
            awaiting_approval: { label: 'Awaiting Approval', cls: 'status-awaiting-approval' },
            awaiting_payment: { label: 'Awaiting Payment', cls: 'status-awaiting-payment' },
            paid: { label: 'Paid', cls: 'status-paid' },
            overdue: { label: 'Overdue', cls: 'status-overdue' },
            voided: { label: 'Voided', cls: 'status-voided' },
        };
        const s = map[status] || { label: status, cls: '' };
        return '<span class="status-badge ' + s.cls + '" data-testid="status-' + this.escapeAttr(status) + '">' + this.escapeHtml(s.label) + '</span>';
    },

    contactAvatar(contact) {
        if (!contact) return '<span class="avatar avatar-sm" style="background:#ccc">?</span>';
        const initials = contact.name.split(' ').map(w => w[0]).join('').substring(0, 2).toUpperCase();
        const colors = ['#0078c8','#00b7e6','#13b5ea','#2e86de','#1abc9c','#27ae60','#8e44ad','#e67e22','#e74c3c','#34495e','#16a085','#c0392b','#7f8c8d','#f39c12'];
        const colorIdx = contact.name.charCodeAt(0) % colors.length;
        return '<span class="avatar avatar-sm" style="background:' + colors[colorIdx] + '" title="' + this.escapeAttr(contact.name) + '">' + this.escapeHtml(initials) + '</span>';
    },

    dropdown(id, options, selectedValue, placeholder) {
        placeholder = placeholder || 'Select...';
        const selected = options.find(o => String(o.value) === String(selectedValue));
        const displayText = selected ? selected.label : placeholder;
        let html = '<div class="custom-dropdown" id="' + this.escapeAttr(id) + '" data-dropdown="' + this.escapeAttr(id) + '" data-testid="dropdown-' + this.escapeAttr(id) + '">';
        html += '<div class="dropdown-trigger" data-dropdown-trigger="' + this.escapeAttr(id) + '"><span class="dropdown-text">' + this.escapeHtml(displayText) + '</span><svg class="dropdown-arrow" width="12" height="12" viewBox="0 0 16 16"><path fill="currentColor" d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"/></svg></div>';
        html += '<div class="dropdown-menu" id="' + this.escapeAttr(id) + '-menu" style="display:none">';
        if (placeholder) {
            html += '<div class="dropdown-item' + (selectedValue == null || selectedValue === '' ? ' selected' : '') + '" data-dropdown-item="' + this.escapeAttr(id) + '" data-value="">' + this.escapeHtml(placeholder) + '</div>';
        }
        options.forEach(opt => {
            html += '<div class="dropdown-item' + (String(opt.value) === String(selectedValue) ? ' selected' : '') + '" data-dropdown-item="' + this.escapeAttr(id) + '" data-value="' + this.escapeAttr(opt.value) + '">' + this.escapeHtml(opt.label) + '</div>';
        });
        html += '</div></div>';
        return html;
    },

    searchableDropdown(id, options, selectedValue, placeholder) {
        placeholder = placeholder || 'Search...';
        const selected = options.find(o => String(o.value) === String(selectedValue));
        const displayText = selected ? selected.label : '';
        let html = '<div class="custom-dropdown searchable-dropdown" id="' + this.escapeAttr(id) + '" data-dropdown="' + this.escapeAttr(id) + '" data-testid="dropdown-' + this.escapeAttr(id) + '">';
        html += '<div class="dropdown-trigger" data-dropdown-trigger="' + this.escapeAttr(id) + '">';
        html += '<input type="text" class="dropdown-search-input" id="' + this.escapeAttr(id) + '-search" data-dropdown-search="' + this.escapeAttr(id) + '" value="' + this.escapeAttr(displayText) + '" placeholder="' + this.escapeAttr(placeholder) + '" autocomplete="off">';
        html += '<svg class="dropdown-arrow" width="12" height="12" viewBox="0 0 16 16"><path fill="currentColor" d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"/></svg></div>';
        html += '<div class="dropdown-menu" id="' + this.escapeAttr(id) + '-menu" style="display:none">';
        options.forEach(opt => {
            html += '<div class="dropdown-item' + (String(opt.value) === String(selectedValue) ? ' selected' : '') + '" data-dropdown-item="' + this.escapeAttr(id) + '" data-value="' + this.escapeAttr(opt.value) + '">' + this.escapeHtml(opt.label) + '</div>';
        });
        html += '</div></div>';
        return html;
    },

    textInput(id, value, placeholder, label, required) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="' + this.escapeAttr(id) + '" class="form-label">' + this.escapeHtml(label) + (required ? ' <span class="required">*</span>' : '') + '</label>';
        html += '<input type="text" class="form-input" id="' + this.escapeAttr(id) + '" data-testid="input-' + this.escapeAttr(id) + '" value="' + this.escapeAttr(value || '') + '" placeholder="' + this.escapeAttr(placeholder || '') + '"' + (required ? ' required' : '') + '>';
        html += '</div>';
        return html;
    },

    textarea(id, value, placeholder, label, rows) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="' + this.escapeAttr(id) + '" class="form-label">' + this.escapeHtml(label) + '</label>';
        html += '<textarea class="form-textarea" id="' + this.escapeAttr(id) + '" data-testid="textarea-' + this.escapeAttr(id) + '" placeholder="' + this.escapeAttr(placeholder || '') + '" rows="' + (rows || 4) + '">' + this.escapeHtml(value || '') + '</textarea>';
        html += '</div>';
        return html;
    },

    numberInput(id, value, label, min, max, step) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="' + this.escapeAttr(id) + '" class="form-label">' + this.escapeHtml(label) + '</label>';
        html += '<input type="number" class="form-input" id="' + this.escapeAttr(id) + '" data-testid="input-' + this.escapeAttr(id) + '" value="' + this.escapeAttr(value != null ? value : '') + '"';
        if (min != null) html += ' min="' + min + '"';
        if (max != null) html += ' max="' + max + '"';
        if (step != null) html += ' step="' + step + '"';
        html += '></div>';
        return html;
    },

    showModal(title, bodyHtml, footerHtml, wide) {
        const overlay = document.getElementById('modalOverlay');
        const container = document.getElementById('modalContainer');
        document.getElementById('modalTitle').textContent = title;
        document.getElementById('modalBody').innerHTML = bodyHtml;
        document.getElementById('modalFooter').innerHTML = footerHtml || '';
        container.className = 'modal' + (wide ? ' modal-wide' : '');
        overlay.style.display = 'flex';
    },

    closeModal() {
        document.getElementById('modalOverlay').style.display = 'none';
    },

    confirm(message, onConfirm) {
        this.showModal('Confirm', '<p>' + this.escapeHtml(message) + '</p>',
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="confirm-modal">Confirm</button>');
        Components._confirmCallback = onConfirm;
    },

    confirmDanger(message, onConfirm) {
        this.showModal('Confirm', '<p>' + this.escapeHtml(message) + '</p>',
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-danger" data-action="confirm-modal">Delete</button>');
        Components._confirmCallback = onConfirm;
    },

    _confirmCallback: null,

    showToast(message, duration) {
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.innerHTML = '<span class="toast-message">' + this.escapeHtml(message) + '</span><button class="toast-close">&times;</button>';
        container.appendChild(toast);
        const remove = () => { toast.classList.add('toast-exit'); setTimeout(() => toast.remove(), 300); };
        toast.querySelector('.toast-close').addEventListener('click', remove);
        setTimeout(remove, duration || 4000);
        setTimeout(() => toast.classList.add('toast-enter'), 10);
    },

    pagination(currentPage, totalItems, pageSize) {
        const totalPages = Math.ceil(totalItems / pageSize);
        if (totalPages <= 1) return '';
        const start = (currentPage - 1) * pageSize + 1;
        const end = Math.min(currentPage * pageSize, totalItems);
        let html = '<div class="pagination" data-testid="pagination">';
        html += '<span class="pagination-info">Showing ' + start + '\u2013' + end + ' of ' + totalItems + '</span>';
        html += '<div class="pagination-buttons">';
        html += '<button class="btn btn-sm" data-action="prev-page"' + (currentPage <= 1 ? ' disabled' : '') + '>&laquo; Prev</button>';
        const maxPages = 5;
        let startPage = Math.max(1, currentPage - Math.floor(maxPages / 2));
        let endPage = Math.min(totalPages, startPage + maxPages - 1);
        if (endPage - startPage < maxPages - 1) startPage = Math.max(1, endPage - maxPages + 1);
        for (let p = startPage; p <= endPage; p++) {
            html += '<button class="btn btn-sm' + (p === currentPage ? ' btn-primary' : '') + '" data-action="goto-page" data-page="' + p + '">' + p + '</button>';
        }
        html += '<button class="btn btn-sm" data-action="next-page"' + (currentPage >= totalPages ? ' disabled' : '') + '>Next &raquo;</button>';
        html += '</div></div>';
        return html;
    },

    emptyState(icon, title, description, actionHtml) {
        return '<div class="empty-state"><div class="empty-icon">' + icon + '</div><h3>' + this.escapeHtml(title) + '</h3><p>' + this.escapeHtml(description) + '</p>' + (actionHtml || '') + '</div>';
    },

    activityIcon(type) {
        const icons = {
            created: '<svg width="16" height="16" viewBox="0 0 16 16" fill="#0078c8"><path d="M8 1a7 7 0 100 14A7 7 0 008 1zm1 10H7V7h2v4zm0-6H7V3h2v2z"/></svg>',
            approved: '<svg width="16" height="16" viewBox="0 0 16 16" fill="#27ae60"><path d="M8 1a7 7 0 100 14A7 7 0 008 1zm3.3 5.3l-4 4a.75.75 0 01-1.06 0l-2-2a.75.75 0 011.06-1.06L6.75 8.7l3.47-3.47a.75.75 0 011.06 1.06z"/></svg>',
            sent: '<svg width="16" height="16" viewBox="0 0 16 16" fill="#2e86de"><path d="M1 1l14 7-14 7V9l10-1L1 7V1z"/></svg>',
            marked_sent: '<svg width="16" height="16" viewBox="0 0 16 16" fill="#2e86de"><path d="M1 1l14 7-14 7V9l10-1L1 7V1z"/></svg>',
            payment: '<svg width="16" height="16" viewBox="0 0 16 16" fill="#27ae60"><path d="M8 1a7 7 0 100 14A7 7 0 008 1zm.75 3v1.25H10a.75.75 0 010 1.5H8.75V8h1.5a.75.75 0 010 1.5h-1.5v1.25H10a.75.75 0 010 1.5H8.75V13h-1.5v-.75H6a.75.75 0 010-1.5h1.25V9.5H6a.75.75 0 010-1.5h1.25V6.75H6a.75.75 0 010-1.5h1.25V4h1.5z"/></svg>',
            voided: '<svg width="16" height="16" viewBox="0 0 16 16" fill="#e74c3c"><path d="M8 1a7 7 0 100 14A7 7 0 008 1zm3 8.25H5a.75.75 0 010-1.5h6a.75.75 0 010 1.5z"/></svg>',
        };
        return icons[type] || icons.created;
    },
};

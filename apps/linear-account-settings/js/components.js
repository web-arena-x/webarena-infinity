/* ============================================================
   components.js — Reusable UI component generators
   ============================================================ */

const Components = {

    // ── Sanitization ─────────────────────────────────────────

    escapeHtml(str) {
        if (str == null) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    },

    escapeAttr(str) {
        if (str == null) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    },

    // ── Date formatting ──────────────────────────────────────

    formatDate(isoStr) {
        if (!isoStr) return 'Never';
        const d = new Date(isoStr);
        const now = new Date();
        const diffMs = now - d;
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffDays === 0) {
            return 'Today';
        } else if (diffDays === 1) {
            return 'Yesterday';
        } else if (diffDays < 7) {
            return d.toLocaleDateString('en-US', { weekday: 'long' });
        } else {
            return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
        }
    },

    formatDateTime(isoStr) {
        if (!isoStr) return 'Never';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
            hour: 'numeric',
            minute: '2-digit'
        });
    },

    formatFullDate(isoStr) {
        if (!isoStr) return 'Never';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', {
            weekday: 'long',
            month: 'long',
            day: 'numeric',
            year: 'numeric'
        }) + ' at ' + d.toLocaleTimeString('en-US', {
            hour: 'numeric',
            minute: '2-digit'
        });
    },

    timeAgo(isoStr) {
        if (!isoStr) return 'Never';
        const d = new Date(isoStr);
        const now = new Date();
        const diffMs = now - d;
        const diffMin = Math.floor(diffMs / 60000);
        const diffHr = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMin < 1) return 'Just now';
        if (diffMin < 60) return diffMin + 'm ago';
        if (diffHr < 24) return diffHr + 'h ago';
        if (diffDays < 30) return diffDays + 'd ago';
        return Components.formatDate(isoStr);
    },

    // ── Avatar ───────────────────────────────────────────────

    avatar(user, size) {
        size = size || 36;
        const initials = Components._getInitials(user.fullName || user.username || '?');
        const color = user.avatarColor || '#5E6AD2';
        return `<div class="avatar" style="width:${size}px;height:${size}px;background:${color};font-size:${Math.round(size * 0.4)}px" data-testid="user-avatar">${Components.escapeHtml(initials)}</div>`;
    },

    _getInitials(name) {
        const parts = name.trim().split(/\s+/);
        if (parts.length >= 2) {
            return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
        }
        return name.substring(0, 2).toUpperCase();
    },

    // ── Custom Dropdown ──────────────────────────────────────

    dropdown(id, options, selectedValue, placeholder) {
        placeholder = placeholder || 'Select...';
        const selectedOption = options.find(o => (typeof o === 'object' ? o.value : o) === selectedValue);
        const displayLabel = selectedOption
            ? (typeof selectedOption === 'object' ? selectedOption.label : selectedOption)
            : placeholder;

        let html = `<div class="custom-dropdown" id="${Components.escapeAttr(id)}">`;
        html += `<div class="dropdown-trigger" data-dropdown="${Components.escapeAttr(id)}" tabindex="0">`;
        html += `<span class="dropdown-value">${Components.escapeHtml(displayLabel)}</span>`;
        html += `<span class="dropdown-arrow">${Components.chevronDownIcon()}</span>`;
        html += `</div>`;
        html += `<div class="dropdown-menu" id="${Components.escapeAttr(id)}-menu">`;

        for (const opt of options) {
            const value = typeof opt === 'object' ? opt.value : opt;
            const label = typeof opt === 'object' ? opt.label : opt;
            const desc = typeof opt === 'object' ? opt.description : null;
            const isSelected = value === selectedValue;
            html += `<div class="dropdown-item${isSelected ? ' selected' : ''}" data-value="${Components.escapeAttr(value)}" data-dropdown-id="${Components.escapeAttr(id)}">`;
            html += `<span class="dropdown-item-label">${Components.escapeHtml(label)}</span>`;
            if (desc) {
                html += `<span class="dropdown-item-desc">${Components.escapeHtml(desc)}</span>`;
            }
            if (isSelected) {
                html += `<span class="dropdown-check">${Components.checkIcon()}</span>`;
            }
            html += `</div>`;
        }

        html += `</div></div>`;
        return html;
    },

    // ── Toggle Switch ────────────────────────────────────────

    toggle(id, checked, label, description) {
        let html = `<div class="toggle-row" data-testid="toggle-${Components.escapeAttr(id)}">`;
        html += `<div class="toggle-info">`;
        html += `<span class="toggle-label">${Components.escapeHtml(label)}</span>`;
        if (description) {
            html += `<span class="toggle-description">${Components.escapeHtml(description)}</span>`;
        }
        html += `</div>`;
        html += `<label class="toggle-switch">`;
        html += `<input type="checkbox" id="${Components.escapeAttr(id)}" ${checked ? 'checked' : ''} data-toggle-id="${Components.escapeAttr(id)}">`;
        html += `<span class="toggle-slider"></span>`;
        html += `</label>`;
        html += `</div>`;
        return html;
    },

    // ── Radio Group ──────────────────────────────────────────

    radioGroup(name, options, selectedValue) {
        let html = `<div class="radio-group" data-radio-name="${Components.escapeAttr(name)}">`;
        for (const opt of options) {
            const value = typeof opt === 'object' ? opt.value : opt;
            const label = typeof opt === 'object' ? opt.label : opt;
            const desc = typeof opt === 'object' ? opt.description : null;
            const isSelected = value === selectedValue;
            html += `<label class="radio-item${isSelected ? ' selected' : ''}">`;
            html += `<input type="radio" name="${Components.escapeAttr(name)}" value="${Components.escapeAttr(value)}" ${isSelected ? 'checked' : ''}>`;
            html += `<span class="radio-indicator"></span>`;
            html += `<span class="radio-content">`;
            html += `<span class="radio-label">${Components.escapeHtml(label)}</span>`;
            if (desc) {
                html += `<span class="radio-description">${Components.escapeHtml(desc)}</span>`;
            }
            html += `</span></label>`;
        }
        html += `</div>`;
        return html;
    },

    // ── Text Input ───────────────────────────────────────────

    textInput(id, value, placeholder, label) {
        let html = '';
        if (label) {
            html += `<label class="input-label" for="${Components.escapeAttr(id)}">${Components.escapeHtml(label)}</label>`;
        }
        html += `<input type="text" class="text-input" id="${Components.escapeAttr(id)}" value="${Components.escapeAttr(value || '')}" placeholder="${Components.escapeAttr(placeholder || '')}" data-testid="input-${Components.escapeAttr(id)}">`;
        return html;
    },

    // ── Modal ────────────────────────────────────────────────

    showModal(title, bodyHtml, footerHtml) {
        const overlay = document.getElementById('modalOverlay');
        document.getElementById('modalTitle').textContent = title;
        document.getElementById('modalBody').innerHTML = bodyHtml;
        document.getElementById('modalFooter').innerHTML = footerHtml || '';
        overlay.style.display = 'flex';
        AppState.modalOpen = true;
    },

    closeModal() {
        document.getElementById('modalOverlay').style.display = 'none';
        AppState.modalOpen = false;
        AppState.modalContent = null;
    },

    confirmDanger(title, message, confirmText, onConfirm) {
        const body = `<p class="modal-message">${Components.escapeHtml(message)}</p>`;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-danger" data-action="confirm-modal">${Components.escapeHtml(confirmText)}</button>
        `;
        Components.showModal(title, body, footer);
        AppState.modalContent = { onConfirm };
    },

    // ── Toast ────────────────────────────────────────────────

    showToast(message, type) {
        type = type || 'info';
        if (AppState.toastTimeout) {
            clearTimeout(AppState.toastTimeout);
        }
        AppState.toastMessage = { message, type };
        const container = document.getElementById('toastContainer');
        container.innerHTML = `<div class="toast toast-${type}">${Components.escapeHtml(message)}</div>`;
        container.style.display = 'block';

        AppState.toastTimeout = setTimeout(() => {
            container.style.display = 'none';
            container.innerHTML = '';
            AppState.toastMessage = null;
        }, 3000);
    },

    // ── Status Dot ───────────────────────────────────────────

    statusDot(enabled) {
        return `<span class="status-dot ${enabled ? 'status-enabled' : 'status-disabled'}"></span>`;
    },

    // ── Empty State ──────────────────────────────────────────

    emptyState(title, message) {
        return `<div class="empty-state"><div class="empty-state-title">${Components.escapeHtml(title)}</div><div class="empty-state-message">${Components.escapeHtml(message)}</div></div>`;
    },

    // ── Icons (inline SVG) ───────────────────────────────────

    chevronDownIcon() {
        return '<svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor"><path d="M2.5 4.5L6 8L9.5 4.5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    },

    chevronRightIcon() {
        return '<svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor"><path d="M4.5 2.5L8 6L4.5 9.5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    },

    checkIcon() {
        return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7L6 10L11 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    },

    pencilIcon() {
        return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M10 2L12 4L5 11H3V9L10 2Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    },

    trashIcon() {
        return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M2 4H12M5 4V3C5 2.45 5.45 2 6 2H8C8.55 2 9 2.45 9 3V4M4 4V12C4 12.55 4.45 13 5 13H9C9.55 13 10 12.55 10 12V4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    },

    plusIcon() {
        return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 2V12M2 7H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>';
    },

    closeIcon() {
        return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 3L11 11M11 3L3 11" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>';
    },

    keyIcon() {
        return '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 6C10 3.79 8.21 2 6 2C3.79 2 2 3.79 2 6C2 8.21 3.79 10 6 10C6.74 10 7.44 9.79 8.03 9.43L10 11.4V13H12V11H14V9L10.97 5.97C10.99 5.98 10.99 5.65 10 6Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="5.5" cy="5.5" r="1" fill="currentColor"/></svg>';
    },

    shieldIcon() {
        return '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 1L2 4V7.5C2 11.09 4.56 14.39 8 15C11.44 14.39 14 11.09 14 7.5V4L8 1Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    },

    deviceIcon(type) {
        if (type === 'Mobile') {
            return '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="4" y="1" width="8" height="14" rx="1.5" stroke="currentColor" stroke-width="1.2"/><line x1="7" y1="12.5" x2="9" y2="12.5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>';
        }
        if (type === 'Tablet') {
            return '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="2" width="12" height="12" rx="1.5" stroke="currentColor" stroke-width="1.2"/><line x1="7" y1="12" x2="9" y2="12" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>';
        }
        // Desktop
        return '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="1" y="2" width="14" height="10" rx="1" stroke="currentColor" stroke-width="1.2"/><line x1="5" y1="14" x2="11" y2="14" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><line x1="8" y1="12" x2="8" y2="14" stroke="currentColor" stroke-width="1.2"/></svg>';
    },

    providerIcon(provider) {
        const icons = {
            google: '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M15.5 8.2c0-.6-.1-1.2-.2-1.7H8v3.2h4.2c-.2 1-1 2.3-2.5 3.1v2.4h3.9c2.3-2.1 3.4-5.3 2.9-7z" fill="#4285F4"/><path d="M8 16c3.2 0 5.9-1.1 7.9-2.9l-3.9-2.4c-1.1.7-2.5 1.1-4 1.1-3.1 0-5.7-2.1-6.6-4.9H1.3v2.5C3.3 13.7 5.5 16 8 16z" fill="#34A853"/><path d="M1.4 6.9c-.5 1.4-.5 3 0 4.3v2.5H1.3C-.2 11.6-.2 8.4 1.3 6.3l.1.6z" fill="#FBBC05"/><path d="M8 3.2c1.7 0 3.3.6 4.5 1.8l3.4-3.4C14 .1 11.2-1 8-1 5.5-1 3.3 1.3 1.3 3.6l3.1 2.5C5.3 4.3 6.9 3.2 8 3.2z" fill="#EA4335"/></svg>',
            github: '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>',
            gitlab: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 14.5L10.5 7H5.5L8 14.5Z" fill="#E24329"/><path d="M8 14.5L5.5 7H1.5L8 14.5Z" fill="#FC6D26"/><path d="M1.5 7L.5 10C.4 10.3.5 10.7.8 10.9L8 14.5L1.5 7Z" fill="#FCA326"/><path d="M1.5 7H5.5L3.8 1.5C3.7 1.2 3.3 1.2 3.2 1.5L1.5 7Z" fill="#E24329"/><path d="M8 14.5L10.5 7H14.5L8 14.5Z" fill="#FC6D26"/><path d="M14.5 7L15.5 10C15.6 10.3 15.5 10.7 15.2 10.9L8 14.5L14.5 7Z" fill="#FCA326"/><path d="M14.5 7H10.5L12.2 1.5C12.3 1.2 12.7 1.2 12.8 1.5L14.5 7Z" fill="#E24329"/></svg>',
            slack: '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M3.4 10.1c0 .9-.7 1.6-1.6 1.6s-1.6-.7-1.6-1.6.7-1.6 1.6-1.6h1.6v1.6z" fill="#E01E5A"/><path d="M4.2 10.1c0-.9.7-1.6 1.6-1.6s1.6.7 1.6 1.6v4.1c0 .9-.7 1.6-1.6 1.6s-1.6-.7-1.6-1.6v-4.1z" fill="#E01E5A"/><path d="M5.8 3.4c-.9 0-1.6-.7-1.6-1.6S4.9.2 5.8.2s1.6.7 1.6 1.6v1.6H5.8z" fill="#36C5F0"/><path d="M5.8 4.2c.9 0 1.6.7 1.6 1.6s-.7 1.6-1.6 1.6H1.8c-.9 0-1.6-.7-1.6-1.6s.7-1.6 1.6-1.6h4z" fill="#36C5F0"/><path d="M12.6 5.8c0-.9.7-1.6 1.6-1.6s1.6.7 1.6 1.6-.7 1.6-1.6 1.6h-1.6V5.8z" fill="#2EB67D"/><path d="M11.8 5.8c0 .9-.7 1.6-1.6 1.6s-1.6-.7-1.6-1.6V1.8c0-.9.7-1.6 1.6-1.6s1.6.7 1.6 1.6v4z" fill="#2EB67D"/><path d="M10.2 12.6c.9 0 1.6.7 1.6 1.6s-.7 1.6-1.6 1.6-1.6-.7-1.6-1.6v-1.6h1.6z" fill="#ECB22E"/><path d="M10.2 11.8c-.9 0-1.6-.7-1.6-1.6s.7-1.6 1.6-1.6h4.1c.9 0 1.6.7 1.6 1.6s-.7 1.6-1.6 1.6h-4.1z" fill="#ECB22E"/></svg>',
            figma: '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M5.5 16A2.5 2.5 0 008 13.5V11H5.5A2.5 2.5 0 003 13.5 2.5 2.5 0 005.5 16z" fill="#0ACF83"/><path d="M3 8.5A2.5 2.5 0 015.5 6H8v5H5.5A2.5 2.5 0 013 8.5z" fill="#A259FF"/><path d="M3 3.5A2.5 2.5 0 015.5 1H8v5H5.5A2.5 2.5 0 013 3.5z" fill="#F24E1E"/><path d="M8 1h2.5A2.5 2.5 0 0113 3.5 2.5 2.5 0 0110.5 6H8V1z" fill="#FF7262"/><path d="M13 8.5A2.5 2.5 0 0110.5 11 2.5 2.5 0 018 8.5 2.5 2.5 0 0110.5 6 2.5 2.5 0 0113 8.5z" fill="#1ABCFE"/></svg>'
        };
        return icons[provider] || '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.2"/></svg>';
    },

    appIcon(name) {
        return `<div class="app-icon" title="${Components.escapeAttr(name)}">${Components.escapeHtml(name.substring(0, 2).toUpperCase())}</div>`;
    },

    navIcon(type) {
        const icons = {
            profile: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="5" r="3" stroke="currentColor" stroke-width="1.2"/><path d="M2 14c0-3.31 2.69-5 6-5s6 1.69 6 5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>',
            preferences: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6.5 2H2V6.5H6.5V2Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 2H9.5V6.5H14V2Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 9.5H9.5V14H14V9.5Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M6.5 9.5H2V14H6.5V9.5Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
            notifications: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 6C4 3.79 5.79 2 8 2C10.21 2 12 3.79 12 6V10L14 12H2L4 10V6Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M6.5 14C6.78 14.3 7.37 14.5 8 14.5C8.63 14.5 9.22 14.3 9.5 14" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>',
            security: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 1L2 4V7.5C2 11.09 4.56 14.39 8 15C11.44 14.39 14 11.09 14 7.5V4L8 1Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        };
        return icons[type] || '';
    }
};

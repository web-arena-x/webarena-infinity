// ============================================================
// components.js — Reusable UI components for Gmail app
// ============================================================

const Components = {

    // ---- Utility Functions ----

    escapeHtml(str) {
        if (str == null) return '';
        return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#039;');
    },

    escapeAttr(str) {
        if (str == null) return '';
        return String(str).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/'/g,'&#039;');
    },

    // ---- Date Formatting ----

    formatDate(isoStr) {
        if (!isoStr) return '';
        const d = new Date(isoStr);
        const now = new Date();
        const diffMs = now - d;
        const diffDays = Math.floor(diffMs / 86400000);
        if (diffDays === 0) {
            return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
        }
        if (diffDays === 1) return 'Yesterday';
        if (diffDays < 7) return d.toLocaleDateString('en-US', { weekday: 'short' });
        if (d.getFullYear() === now.getFullYear()) {
            return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        }
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    },

    formatDateTime(isoStr) {
        if (!isoStr) return '';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit', hour12: true });
    },

    formatFullDate(isoStr) {
        if (!isoStr) return '';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }) +
            ' at ' + d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
    },

    timeAgo(isoStr) {
        if (!isoStr) return '';
        const d = new Date(isoStr);
        const now = new Date();
        const diffS = Math.floor((now - d) / 1000);
        if (diffS < 60) return 'just now';
        if (diffS < 3600) return `${Math.floor(diffS/60)} min ago`;
        if (diffS < 86400) return `${Math.floor(diffS/3600)} hr ago`;
        if (diffS < 604800) return `${Math.floor(diffS/86400)} days ago`;
        return Components.formatDate(isoStr);
    },

    // ---- Avatar ----

    avatar(name, color, size = 32) {
        const initials = (name || '?').split(' ').map(w => w[0]).join('').substring(0,2).toUpperCase();
        return `<div class="email-message-avatar" style="width:${size}px;height:${size}px;background:${Components.escapeAttr(color || '#5f6368')};font-size:${Math.floor(size*0.4)}px">${Components.escapeHtml(initials)}</div>`;
    },

    // ---- Custom Dropdown ----

    dropdown(id, options, selectedValue, placeholder = 'Select...') {
        const selected = options.find(o => o.id === selectedValue || o.value === selectedValue);
        const displayText = selected ? Components.escapeHtml(selected.name || selected.label) : placeholder;
        let html = `<div class="custom-dropdown" id="${Components.escapeAttr(id)}" data-testid="${Components.escapeAttr(id)}">`;
        html += `<div class="dropdown-trigger" data-dropdown="${Components.escapeAttr(id)}">${displayText}<span class="arrow">&#9662;</span></div>`;
        html += `<div class="dropdown-menu" id="${Components.escapeAttr(id)}-menu">`;
        for (const opt of options) {
            const val = opt.id || opt.value;
            const isSelected = val === selectedValue;
            html += `<div class="dropdown-item${isSelected ? ' selected' : ''}" data-value="${Components.escapeAttr(val)}" data-dropdown-id="${Components.escapeAttr(id)}">`;
            if (isSelected) html += `<span class="check">&#10003;</span>`;
            else html += `<span class="check"></span>`;
            html += Components.escapeHtml(opt.name || opt.label);
            html += `</div>`;
        }
        html += `</div></div>`;
        return html;
    },

    // ---- Toggle Switch ----

    toggle(id, checked, label = '', description = '') {
        let html = `<div class="settings-item">`;
        html += `<div><div class="settings-item-label">${Components.escapeHtml(label)}</div>`;
        if (description) html += `<div class="settings-item-desc">${Components.escapeHtml(description)}</div>`;
        html += `</div>`;
        html += `<label class="toggle-switch" data-testid="${Components.escapeAttr(id)}">`;
        html += `<input type="checkbox" id="${Components.escapeAttr(id)}" ${checked ? 'checked' : ''}>`;
        html += `<span class="toggle-slider"></span></label></div>`;
        return html;
    },

    // ---- Radio Group ----

    radioGroup(name, options, selectedValue) {
        let html = `<div class="radio-group">`;
        for (const opt of options) {
            const val = opt.id || opt.value;
            html += `<label class="radio-option">`;
            html += `<input type="radio" name="${Components.escapeAttr(name)}" value="${Components.escapeAttr(val)}" ${val === selectedValue ? 'checked' : ''}>`;
            html += Components.escapeHtml(opt.name || opt.label);
            html += `</label>`;
        }
        html += `</div>`;
        return html;
    },

    // ---- Text Input ----

    textInput(id, value, placeholder = '', label = '') {
        let html = '';
        if (label) html += `<label class="form-label" for="${Components.escapeAttr(id)}">${Components.escapeHtml(label)}</label>`;
        html += `<input type="text" class="form-input" id="${Components.escapeAttr(id)}" data-testid="${Components.escapeAttr(id)}" value="${Components.escapeAttr(value || '')}" placeholder="${Components.escapeAttr(placeholder)}">`;
        return html;
    },

    // ---- Modal System ----

    showModal(title, bodyHtml, footerHtml) {
        const overlay = document.getElementById('modalOverlay');
        document.getElementById('modalTitle').textContent = title;
        document.getElementById('modalBody').innerHTML = bodyHtml;
        document.getElementById('modalFooter').innerHTML = footerHtml || '';
        overlay.style.display = 'flex';
    },

    closeModal() {
        document.getElementById('modalOverlay').style.display = 'none';
    },

    confirm(title, message, confirmText, onConfirm, cancelText = 'Cancel') {
        const bodyHtml = `<p style="font-size:14px;color:var(--text-primary)">${Components.escapeHtml(message)}</p>`;
        const footerHtml = `
            <button class="btn btn-secondary" data-action="close-modal">${Components.escapeHtml(cancelText)}</button>
            <button class="btn btn-primary" id="confirmActionBtn">${Components.escapeHtml(confirmText)}</button>
        `;
        Components.showModal(title, bodyHtml, footerHtml);
        document.getElementById('confirmActionBtn').onclick = () => {
            Components.closeModal();
            if (onConfirm) onConfirm();
        };
    },

    confirmDanger(title, message, confirmText, onConfirm) {
        const bodyHtml = `<p style="font-size:14px;color:var(--text-primary)">${Components.escapeHtml(message)}</p>`;
        const footerHtml = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-danger" id="confirmActionBtn">${Components.escapeHtml(confirmText)}</button>
        `;
        Components.showModal(title, bodyHtml, footerHtml);
        document.getElementById('confirmActionBtn').onclick = () => {
            Components.closeModal();
            if (onConfirm) onConfirm();
        };
    },

    // ---- Toast Notifications ----

    showToast(message, actionText = null, actionCallback = null, duration = 5000) {
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = 'toast';
        let html = `<span>${Components.escapeHtml(message)}</span>`;
        if (actionText) {
            html += `<button class="toast-action">${Components.escapeHtml(actionText)}</button>`;
        }
        toast.innerHTML = html;
        container.appendChild(toast);
        if (actionText && actionCallback) {
            toast.querySelector('.toast-action').onclick = () => {
                actionCallback();
                toast.remove();
            };
        }
        setTimeout(() => {
            toast.classList.add('removing');
            setTimeout(() => toast.remove(), 300);
        }, duration);
    },

    // ---- Star Icons ----

    starIcon(type, filled) {
        if (!filled) return '&#9734;'; // empty star
        switch (type) {
            case 'yellow-star': return '<span class="star-yellow">&#9733;</span>';
            case 'orange-star': return '<span class="star-orange">&#9733;</span>';
            case 'red-star': return '<span class="star-red">&#9733;</span>';
            case 'purple-star': return '<span class="star-purple">&#9733;</span>';
            case 'blue-star': return '<span class="star-blue">&#9733;</span>';
            case 'green-star': return '<span class="star-green">&#9733;</span>';
            case 'yellow-bang': return '<span class="star-yellow">!</span>';
            case 'red-bang': return '<span class="star-red">!</span>';
            case 'purple-question': return '<span class="star-purple">?</span>';
            case 'orange-guillemet': return '<span class="star-orange">&raquo;</span>';
            case 'blue-info': return '<span class="star-blue">&#9432;</span>';
            default: return '<span class="star-yellow">&#9733;</span>';
        }
    },

    // ---- Importance Marker ----

    importanceIcon(isImportant) {
        if (isImportant) {
            return '<span class="email-important marked" title="Important">&#9654;</span>';
        }
        return '<span class="email-important" title="Not important">&#9655;</span>';
    },

    // ---- Category Icons ----

    categoryIcon(category) {
        switch (category) {
            case 'primary': return '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>';
            case 'social': return '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>';
            case 'promotions': return '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg>';
            case 'updates': return '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>';
            case 'forums': return '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M21 6h-2v9H6v2c0 .55.45 1 1 1h11l4 4V7c0-.55-.45-1-1-1zm-4 6V3c0-.55-.45-1-1-1H3c-.55 0-1 .45-1 1v14l4-4h10c.55 0 1-.45 1-1z"/></svg>';
            default: return '';
        }
    },

    // ---- Sidebar Nav Icons ----

    navIcon(type) {
        const icons = {
            inbox: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M19 3H4.99c-1.11 0-1.98.89-1.98 2L3 19c0 1.1.88 2 1.99 2H19c1.1 0 2-.9 2-2V5c0-1.11-.9-2-2-2zm0 12h-4c0 1.66-1.35 3-3 3s-3-1.34-3-3H4.99V5H19v10z"/></svg>',
            starred: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>',
            snoozed: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>',
            sent: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>',
            drafts: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M21.99 8c0-.72-.37-1.35-.94-1.7L12 1 2.95 6.3C2.38 6.65 2 7.28 2 8v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2l-.01-10zm-10 1L3.74 4.84 12 1l8.26 3.84L12 9z"/></svg>',
            important: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg>',
            allmail: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M22 8.98V18c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V8.98l10 5.52 10-5.52zM20 4H4c-1.1 0-2 .9-2 2v.01L12 11.5 22 6V6c0-1.1-.9-2-2-2z"/></svg>',
            spam: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M15.73 3H8.27L3 8.27v7.46L8.27 21h7.46L21 15.73V8.27L15.73 3zM12 17.3c-.72 0-1.3-.58-1.3-1.3 0-.72.58-1.3 1.3-1.3.72 0 1.3.58 1.3 1.3 0 .72-.58 1.3-1.3 1.3zm1-4.3h-2V7h2v6z"/></svg>',
            trash: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>',
            label: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M17.63 5.84C17.27 5.33 16.67 5 16 5L5 5.01C3.9 5.01 3 5.9 3 7v10c0 1.1.9 1.99 2 1.99L16 19c.67 0 1.27-.33 1.63-.84L22 12l-4.37-6.16z"/></svg>',
            settings: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.07.62-.07.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>',
            createLabel: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>',
        };
        return icons[type] || icons.label;
    },

    // ---- Toolbar Icons ----

    toolbarIcon(type) {
        const icons = {
            archive: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M20.54 5.23l-1.39-1.68C18.88 3.21 18.47 3 18 3H6c-.47 0-.88.21-1.16.55L3.46 5.23C3.17 5.57 3 6.02 3 6.5V19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V6.5c0-.48-.17-.93-.46-1.27zM12 17.5L6.5 12H10v-2h4v2h3.5L12 17.5zM5.12 5l.81-1h12l.94 1H5.12z"/></svg>',
            delete: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>',
            markRead: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M22 8.98V18c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V8.98l10 5.52 10-5.52zM20 4H4c-1.1 0-2 .9-2 2v.01L12 11.5 22 6V6c0-1.1-.9-2-2-2z"/></svg>',
            markUnread: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
            spam: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M15.73 3H8.27L3 8.27v7.46L8.27 21h7.46L21 15.73V8.27L15.73 3zM12 17.3c-.72 0-1.3-.58-1.3-1.3 0-.72.58-1.3 1.3-1.3.72 0 1.3.58 1.3 1.3 0 .72-.58 1.3-1.3 1.3zm1-4.3h-2V7h2v6z"/></svg>',
            moveToInbox: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M19 3H4.99c-1.11 0-1.98.89-1.98 2L3 19c0 1.1.88 2 1.99 2H19c1.1 0 2-.9 2-2V5c0-1.11-.9-2-2-2zm0 12h-4c0 1.66-1.35 3-3 3s-3-1.34-3-3H4.99V5H19v10z"/></svg>',
            label: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M17.63 5.84C17.27 5.33 16.67 5 16 5L5 5.01C3.9 5.01 3 5.9 3 7v10c0 1.1.9 1.99 2 1.99L16 19c.67 0 1.27-.33 1.63-.84L22 12l-4.37-6.16z"/></svg>',
            snooze: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>',
            moveTo: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>',
            more: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>',
            refresh: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/></svg>',
            prevPage: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>',
            nextPage: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>',
            reply: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"/></svg>',
            replyAll: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M7 8V5l-7 7 7 7v-3l-4-4 4-4zm6 1V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"/></svg>',
            forward: '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 8V4l8 8-8 8v-4H4V8z"/></svg>',
        };
        return icons[type] || '';
    },

    // ---- Email Label Badge ----

    labelBadge(label) {
        if (!label || label.type === 'system') return '';
        const bg = label.color ? label.color.background : '#e0e0e0';
        const fg = label.color ? label.color.text : '#333';
        return `<span class="email-label-badge" style="background:${Components.escapeAttr(bg)};color:${Components.escapeAttr(fg)}">${Components.escapeHtml(label.name)}</span>`;
    },

    // ---- Empty State ----

    emptyState(icon, title, text) {
        return `<div class="empty-state">
            <div class="empty-state-icon">${icon}</div>
            <div class="empty-state-title">${Components.escapeHtml(title)}</div>
            <div class="empty-state-text">${Components.escapeHtml(text)}</div>
        </div>`;
    },

    // ---- Snooze Date Picker ----

    snoozePicker() {
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        tomorrow.setHours(8, 0, 0, 0);
        const weekend = new Date();
        weekend.setDate(weekend.getDate() + (6 - weekend.getDay()));
        weekend.setHours(8, 0, 0, 0);
        const nextWeek = new Date();
        nextWeek.setDate(nextWeek.getDate() + 7);
        nextWeek.setHours(8, 0, 0, 0);

        const fmt = d => d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' }) + ', 8:00 AM';

        return `<div class="snooze-options" data-testid="snooze-picker">
            <div class="dropdown-item" data-snooze="tomorrow" data-snooze-date="${tomorrow.toISOString()}">
                <span>Tomorrow</span><span style="color:var(--text-secondary);margin-left:auto;font-size:12px">${fmt(tomorrow)}</span>
            </div>
            <div class="dropdown-item" data-snooze="this_weekend" data-snooze-date="${weekend.toISOString()}">
                <span>This weekend</span><span style="color:var(--text-secondary);margin-left:auto;font-size:12px">${fmt(weekend)}</span>
            </div>
            <div class="dropdown-item" data-snooze="next_week" data-snooze-date="${nextWeek.toISOString()}">
                <span>Next week</span><span style="color:var(--text-secondary);margin-left:auto;font-size:12px">${fmt(nextWeek)}</span>
            </div>
            <div class="dropdown-divider"></div>
            <div class="dropdown-item" data-snooze="pick_date">
                <span>Pick date & time</span>
            </div>
        </div>`;
    },

    // ---- Label Color Picker ----

    labelColorPicker(selectedColor) {
        const colors = [
            { id: 'berry', bg: '#b3005e', fg: '#fff' },
            { id: 'red', bg: '#cc3333', fg: '#fff' },
            { id: 'orange', bg: '#e37400', fg: '#fff' },
            { id: 'yellow', bg: '#d5ae49', fg: '#000' },
            { id: 'green', bg: '#2a8547', fg: '#fff' },
            { id: 'teal', bg: '#13828b', fg: '#fff' },
            { id: 'blue', bg: '#2962ff', fg: '#fff' },
            { id: 'purple', bg: '#7e57c2', fg: '#fff' },
            { id: 'gray', bg: '#666', fg: '#fff' },
            { id: 'light-berry', bg: '#fce4ec', fg: '#880e4f' },
            { id: 'light-red', bg: '#ffcdd2', fg: '#c62828' },
            { id: 'light-orange', bg: '#ffe0b2', fg: '#e65100' },
            { id: 'light-yellow', bg: '#fff9c4', fg: '#f57f17' },
            { id: 'light-green', bg: '#c8e6c9', fg: '#2e7d32' },
            { id: 'light-teal', bg: '#b2dfdb', fg: '#00695c' },
            { id: 'light-blue', bg: '#bbdefb', fg: '#1565c0' },
            { id: 'light-purple', bg: '#e1bee7', fg: '#7b1fa2' },
            { id: 'light-gray', bg: '#e0e0e0', fg: '#424242' },
        ];
        let html = '<div class="color-grid" style="display:grid;grid-template-columns:repeat(9,1fr);gap:4px">';
        for (const c of colors) {
            const selected = selectedColor && selectedColor.background === c.bg ? 'border:2px solid var(--color-primary);' : '';
            html += `<div class="color-swatch" data-color-bg="${c.bg}" data-color-fg="${c.fg}" style="width:24px;height:24px;border-radius:50%;background:${c.bg};cursor:pointer;${selected}" title="${c.id}"></div>`;
        }
        html += `<div class="color-swatch" data-color-bg="" data-color-fg="" style="width:24px;height:24px;border-radius:50%;background:#f5f5f5;cursor:pointer;border:1px solid #ccc" title="Remove color">&#10005;</div>`;
        html += '</div>';
        return html;
    }
};

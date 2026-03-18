// ============================================================
// components.js — Reusable UI components for Gmail Accounts & Contacts
// ============================================================

const Components = {

    escapeHtml(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    },

    escapeAttr(str) {
        return this.escapeHtml(str);
    },

    formatDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const now = new Date();
        const diff = now - d;
        const days = Math.floor(diff / 86400000);
        if (days === 0) return 'Today';
        if (days === 1) return 'Yesterday';
        if (days < 7) return d.toLocaleDateString('en-US', { weekday: 'long' });
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    },

    formatDateTime(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) +
            ' ' + d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
    },

    timeAgo(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const now = new Date();
        const diff = Math.floor((now - d) / 1000);
        if (diff < 60) return 'just now';
        if (diff < 3600) return Math.floor(diff / 60) + 'm ago';
        if (diff < 86400) return Math.floor(diff / 3600) + 'h ago';
        if (diff < 2592000) return Math.floor(diff / 86400) + 'd ago';
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    },

    avatar(name, color, size) {
        size = size || 40;
        const initials = (name || '?').split(' ').map(w => w[0] || '').join('').toUpperCase().slice(0, 2);
        const fontSize = Math.round(size * 0.4);
        return `<div class="avatar" style="width:${size}px;height:${size}px;background:${color || '#757575'};font-size:${fontSize}px;line-height:${size}px;">${this.escapeHtml(initials)}</div>`;
    },

    icon(name, cls) {
        return `<span class="material-icons${cls ? ' ' + cls : ''}">${name}</span>`;
    },

    badge(count, cls) {
        if (!count) return '';
        return `<span class="badge ${cls || ''}">${count}</span>`;
    },

    dropdown(id, options, selected, placeholder) {
        const selectedOpt = options.find(o => o.value === selected);
        const displayText = selectedOpt ? selectedOpt.label : (placeholder || 'Select...');
        let html = `<div class="custom-dropdown" id="${id}" data-dropdown="${id}">`;
        html += `<div class="dropdown-trigger" data-dropdown="${id}">`;
        html += `<span class="dropdown-text">${this.escapeHtml(displayText)}</span>`;
        html += `<span class="material-icons dropdown-arrow">expand_more</span>`;
        html += `</div>`;
        html += `<div class="dropdown-menu" id="${id}-menu">`;
        for (const opt of options) {
            const isSelected = opt.value === selected ? ' selected' : '';
            html += `<div class="dropdown-item${isSelected}" data-value="${this.escapeAttr(opt.value)}" data-dropdown-id="${id}">`;
            if (opt.icon) html += `<span class="material-icons dropdown-item-icon">${opt.icon}</span>`;
            html += `<span>${this.escapeHtml(opt.label)}</span>`;
            if (opt.value === selected) html += `<span class="material-icons checkmark">check</span>`;
            html += `</div>`;
        }
        html += `</div></div>`;
        return html;
    },

    toggle(id, label, checked, description) {
        return `<div class="toggle-row" id="${id}-row">
            <div class="toggle-info">
                <label class="toggle-label" for="${id}">${this.escapeHtml(label)}</label>
                ${description ? `<div class="toggle-description">${this.escapeHtml(description)}</div>` : ''}
            </div>
            <label class="toggle-switch">
                <input type="checkbox" id="${id}" data-toggle="${id}" ${checked ? 'checked' : ''}>
                <span class="toggle-slider"></span>
            </label>
        </div>`;
    },

    textInput(id, label, value, placeholder, required, type) {
        type = type || 'text';
        return `<div class="form-field">
            <label class="form-label" for="${id}">${this.escapeHtml(label)}${required ? ' <span class="required">*</span>' : ''}</label>
            <input type="${type}" class="form-input" id="${id}" value="${this.escapeAttr(value || '')}"
                placeholder="${this.escapeAttr(placeholder || '')}" ${required ? 'required' : ''}>
        </div>`;
    },

    textarea(id, label, value, placeholder, rows) {
        return `<div class="form-field">
            <label class="form-label" for="${id}">${this.escapeHtml(label)}</label>
            <textarea class="form-textarea" id="${id}" rows="${rows || 3}"
                placeholder="${this.escapeAttr(placeholder || '')}">${this.escapeHtml(value || '')}</textarea>
        </div>`;
    },

    button(text, action, cls, icon) {
        return `<button class="btn ${cls || 'btn-secondary'}" data-action="${action}">
            ${icon ? `<span class="material-icons btn-icon">${icon}</span>` : ''}
            ${this.escapeHtml(text)}
        </button>`;
    },

    modal(id, title, bodyHtml, footerHtml) {
        return `<div class="modal-overlay" id="${id}">
            <div class="modal">
                <div class="modal-header">
                    <h2 class="modal-title">${this.escapeHtml(title)}</h2>
                    <button class="modal-close" data-action="close-modal" data-modal="${id}">
                        <span class="material-icons">close</span>
                    </button>
                </div>
                <div class="modal-body">${bodyHtml}</div>
                ${footerHtml ? `<div class="modal-footer">${footerHtml}</div>` : ''}
            </div>
        </div>`;
    },

    toast(message, type) {
        type = type || 'info';
        const iconMap = { success: 'check_circle', error: 'error', warning: 'warning', info: 'info' };
        return `<div class="toast toast-${type}">
            <span class="material-icons toast-icon">${iconMap[type] || 'info'}</span>
            <span class="toast-message">${this.escapeHtml(message)}</span>
            <button class="toast-close" data-action="dismiss-toast">
                <span class="material-icons">close</span>
            </button>
        </div>`;
    },

    emptyState(icon, title, description, actionText, action) {
        let html = `<div class="empty-state">`;
        html += `<span class="material-icons empty-state-icon">${icon}</span>`;
        html += `<h3 class="empty-state-title">${this.escapeHtml(title)}</h3>`;
        html += `<p class="empty-state-description">${this.escapeHtml(description)}</p>`;
        if (actionText && action) {
            html += `<button class="btn btn-primary" data-action="${action}">${this.escapeHtml(actionText)}</button>`;
        }
        html += `</div>`;
        return html;
    },

    searchBar(id, value, placeholder) {
        return `<div class="search-bar" id="${id}">
            <span class="material-icons search-icon">search</span>
            <input type="text" class="search-input" id="${id}-input"
                value="${this.escapeAttr(value || '')}"
                placeholder="${this.escapeAttr(placeholder || 'Search...')}">
            ${value ? `<button class="search-clear" data-action="clear-search"><span class="material-icons">close</span></button>` : ''}
        </div>`;
    },

    pagination(page, totalPages, total) {
        if (totalPages <= 1) return '';
        const start = (page - 1) * AppState.pageSize + 1;
        const end = Math.min(page * AppState.pageSize, total);
        let html = `<div class="pagination">`;
        html += `<span class="pagination-info">${start}-${end} of ${total}</span>`;
        html += `<button class="pagination-btn" data-action="prev-page" ${page <= 1 ? 'disabled' : ''}>`;
        html += `<span class="material-icons">chevron_left</span></button>`;
        html += `<button class="pagination-btn" data-action="next-page" ${page >= totalPages ? 'disabled' : ''}>`;
        html += `<span class="material-icons">chevron_right</span></button>`;
        html += `</div>`;
        return html;
    },

    statusBadge(status) {
        const colors = {
            active: 'badge-success',
            pending: 'badge-warning',
            expired: 'badge-error',
            linked: 'badge-success',
            unlinked: 'badge-neutral'
        };
        return `<span class="status-badge ${colors[status] || 'badge-neutral'}">${this.escapeHtml(status)}</span>`;
    },

    contactCard(contact, selected) {
        const name = contact.firstName + ' ' + contact.lastName;
        const isSelected = selected ? ' contact-selected' : '';
        return `<div class="contact-card${isSelected}" data-contact-id="${contact.id}" data-action="select-contact">
            <div class="contact-card-avatar">
                ${this.avatar(name, contact.avatarColor, 36)}
            </div>
            <div class="contact-card-info">
                <div class="contact-card-name">${this.escapeHtml(name.trim() || contact.email)}</div>
                <div class="contact-card-email">${this.escapeHtml(contact.email)}</div>
            </div>
            <div class="contact-card-actions">
                <button class="icon-btn contact-star ${contact.isStarred ? 'starred' : ''}"
                    data-action="toggle-star" data-contact-id="${contact.id}" title="${contact.isStarred ? 'Unstar' : 'Star'}">
                    <span class="material-icons">${contact.isStarred ? 'star' : 'star_border'}</span>
                </button>
            </div>
        </div>`;
    },

    otherContactCard(contact) {
        return `<div class="contact-card other-contact-card" data-other-id="${contact.id}">
            <div class="contact-card-avatar">
                ${this.avatar(contact.name || contact.email, '#9E9E9E', 36)}
            </div>
            <div class="contact-card-info">
                <div class="contact-card-name">${this.escapeHtml(contact.name || contact.email)}</div>
                <div class="contact-card-email">${this.escapeHtml(contact.email)}</div>
                <div class="contact-card-meta">${this.escapeHtml(contact.interactionCount + ' interactions')}</div>
            </div>
            <div class="contact-card-actions">
                <button class="icon-btn" data-action="move-to-contacts" data-other-id="${contact.id}" title="Add to contacts">
                    <span class="material-icons">person_add</span>
                </button>
                <button class="icon-btn" data-action="delete-other-contact" data-other-id="${contact.id}" title="Delete">
                    <span class="material-icons">delete</span>
                </button>
            </div>
        </div>`;
    },

    labelChip(label) {
        return `<span class="label-chip" style="background:${label.color}20;color:${label.color};border:1px solid ${label.color}40;">
            ${this.escapeHtml(label.name)}
        </span>`;
    },

    confirmDialog(title, message, confirmText, confirmAction, cancelAction) {
        const body = `<p class="confirm-message">${this.escapeHtml(message)}</p>`;
        const footer = `
            <button class="btn btn-secondary" data-action="${cancelAction || 'close-confirm'}"  >Cancel</button>
            <button class="btn btn-danger" data-action="${confirmAction}">${this.escapeHtml(confirmText || 'Confirm')}</button>
        `;
        return this.modal('confirm-modal', title, body, footer);
    }
};

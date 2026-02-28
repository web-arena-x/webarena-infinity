/* components.js — Reusable UI components for GitLab Plan & Track */
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
        if (!iso) return '—';
        const d = new Date(iso);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    },

    formatDateShort(iso) {
        if (!iso) return '—';
        const d = new Date(iso);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    },

    formatDateTime(iso) {
        if (!iso) return '—';
        const d = new Date(iso);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) + ' ' + d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
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

    formatDuration(seconds) {
        if (!seconds || seconds <= 0) return '0m';
        const h = Math.floor(seconds / 3600);
        const m = Math.floor((seconds % 3600) / 60);
        if (h > 0 && m > 0) return h + 'h ' + m + 'm';
        if (h > 0) return h + 'h';
        return m + 'm';
    },

    parseDuration(str) {
        if (!str) return 0;
        let total = 0;
        const mo = str.match(/(\d+)\s*mo/); if (mo) total += parseInt(mo[1]) * 576000;
        const w = str.match(/(\d+)\s*w/); if (w) total += parseInt(w[1]) * 144000;
        const d = str.match(/(\d+)\s*d/); if (d) total += parseInt(d[1]) * 28800;
        const h = str.match(/(\d+)\s*h/); if (h) total += parseInt(h[1]) * 3600;
        const m = str.match(/(\d+)\s*m(?!o)/); if (m) total += parseInt(m[1]) * 60;
        return total;
    },

    avatar(user, size) {
        size = size || 32;
        if (!user) return '<span class="avatar" style="width:'+size+'px;height:'+size+'px;background:#ccc"></span>';
        const initials = user.name.split(' ').map(n => n[0]).join('').substring(0, 2);
        return '<span class="avatar" style="width:'+size+'px;height:'+size+'px;font-size:'+(size*0.4)+'px;background:'+this.escapeAttr(user.avatarColor || '#6b4fbb')+'" title="'+this.escapeAttr(user.name)+'" data-testid="avatar-'+this.escapeAttr(user.id)+'">'+this.escapeHtml(initials)+'</span>';
    },

    labelBadge(label) {
        if (!label) return '';
        const scopedClass = label.scoped ? ' label-badge-scoped' : '';
        if (label.scoped) {
            const parts = label.title.split('::');
            return '<span class="label-badge'+scopedClass+'" style="--label-bg:'+this.escapeAttr(label.color)+';--label-text:'+this.escapeAttr(label.textColor)+'" data-testid="label-'+this.escapeAttr(label.id)+'" data-label-id="'+this.escapeAttr(label.id)+'">'
                + '<span class="label-scope">'+this.escapeHtml(parts[0])+'</span>'
                + '<span class="label-value">'+this.escapeHtml(parts.slice(1).join('::'))+'</span>'
                + '</span>';
        }
        return '<span class="label-badge" style="--label-bg:'+this.escapeAttr(label.color)+';--label-text:'+this.escapeAttr(label.textColor)+'" data-testid="label-'+this.escapeAttr(label.id)+'" data-label-id="'+this.escapeAttr(label.id)+'">'+this.escapeHtml(label.title)+'</span>';
    },

    healthBadge(status) {
        if (!status) return '';
        const map = { on_track: { text: 'On track', cls: 'health-on-track' }, needs_attention: { text: 'Needs attention', cls: 'health-needs-attention' }, at_risk: { text: 'At risk', cls: 'health-at-risk' } };
        const h = map[status];
        if (!h) return '';
        return '<span class="health-badge '+h.cls+'" data-testid="health-'+status+'">'+h.text+'</span>';
    },

    statusBadge(status) {
        const cls = status === 'open' ? 'status-open' : 'status-closed';
        const icon = status === 'open' ? '<svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><circle cx="8" cy="8" r="7" fill="none" stroke="currentColor" stroke-width="2"/></svg>' : '<svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 16A8 8 0 108 0a8 8 0 000 16zm3.78-9.72a.75.75 0 00-1.06-1.06L7 8.94 5.28 7.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.06 0l4.25-4.25z"/></svg>';
        return '<span class="status-badge '+cls+'">'+icon+' '+this.escapeHtml(status.charAt(0).toUpperCase() + status.slice(1))+'</span>';
    },

    progressBar(completed, total) {
        if (total === 0) return '<div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><span class="progress-text">0%</span>';
        const pct = Math.round((completed / total) * 100);
        return '<div class="progress-bar"><div class="progress-fill" style="width:'+pct+'%"></div></div><span class="progress-text">'+pct+'%</span>';
    },

    dropdown(id, options, selectedValue, placeholder) {
        placeholder = placeholder || 'Select...';
        const selected = options.find(o => o.value === selectedValue);
        const displayText = selected ? selected.label : placeholder;
        let html = '<div class="custom-dropdown" id="'+this.escapeAttr(id)+'" data-dropdown="'+this.escapeAttr(id)+'" data-testid="dropdown-'+this.escapeAttr(id)+'">';
        html += '<div class="dropdown-trigger" data-dropdown-trigger="'+this.escapeAttr(id)+'"><span class="dropdown-text">'+this.escapeHtml(displayText)+'</span><svg class="dropdown-arrow" width="12" height="12" viewBox="0 0 16 16"><path fill="currentColor" d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"/></svg></div>';
        html += '<div class="dropdown-menu" id="'+this.escapeAttr(id)+'-menu" style="display:none">';
        if (placeholder) {
            html += '<div class="dropdown-item'+(selectedValue == null ? ' selected' : '')+'" data-dropdown-item="'+this.escapeAttr(id)+'" data-value="">'+this.escapeHtml(placeholder)+'</div>';
        }
        options.forEach(opt => {
            html += '<div class="dropdown-item'+(opt.value === selectedValue ? ' selected' : '')+'" data-dropdown-item="'+this.escapeAttr(id)+'" data-value="'+this.escapeAttr(opt.value)+'">'+this.escapeHtml(opt.label)+'</div>';
        });
        html += '</div></div>';
        return html;
    },

    toggle(id, checked, label, description) {
        let html = '<div class="toggle-row" data-testid="toggle-'+this.escapeAttr(id)+'">';
        html += '<label class="toggle-switch"><input type="checkbox" id="'+this.escapeAttr(id)+'" data-toggle="'+this.escapeAttr(id)+'"'+(checked ? ' checked' : '')+'><span class="toggle-slider"></span></label>';
        html += '<div class="toggle-label-wrap"><span class="toggle-label">'+this.escapeHtml(label)+'</span>';
        if (description) html += '<span class="toggle-desc">'+this.escapeHtml(description)+'</span>';
        html += '</div></div>';
        return html;
    },

    textInput(id, value, placeholder, label) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="'+this.escapeAttr(id)+'" class="form-label">'+this.escapeHtml(label)+'</label>';
        html += '<input type="text" class="form-input" id="'+this.escapeAttr(id)+'" data-testid="input-'+this.escapeAttr(id)+'" value="'+this.escapeAttr(value || '')+'" placeholder="'+this.escapeAttr(placeholder || '')+'">';
        html += '</div>';
        return html;
    },

    textarea(id, value, placeholder, label, rows) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="'+this.escapeAttr(id)+'" class="form-label">'+this.escapeHtml(label)+'</label>';
        html += '<textarea class="form-textarea" id="'+this.escapeAttr(id)+'" data-testid="textarea-'+this.escapeAttr(id)+'" placeholder="'+this.escapeAttr(placeholder || '')+'" rows="'+(rows||4)+'">'+this.escapeHtml(value || '')+'</textarea>';
        html += '</div>';
        return html;
    },

    dateInput(id, value, label) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="'+this.escapeAttr(id)+'" class="form-label">'+this.escapeHtml(label)+'</label>';
        html += '<input type="text" class="form-input date-input" id="'+this.escapeAttr(id)+'" data-testid="date-'+this.escapeAttr(id)+'" value="'+this.escapeAttr(value || '')+'" placeholder="YYYY-MM-DD">';
        html += '</div>';
        return html;
    },

    numberInput(id, value, label, min, max) {
        let html = '<div class="form-group">';
        if (label) html += '<label for="'+this.escapeAttr(id)+'" class="form-label">'+this.escapeHtml(label)+'</label>';
        html += '<input type="number" class="form-input" id="'+this.escapeAttr(id)+'" data-testid="number-'+this.escapeAttr(id)+'" value="'+this.escapeAttr(value != null ? value : '')+'"';
        if (min != null) html += ' min="'+min+'"';
        if (max != null) html += ' max="'+max+'"';
        html += '></div>';
        return html;
    },

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

    confirm(message, onConfirm) {
        this.showModal('Confirm', '<p>' + this.escapeHtml(message) + '</p>', '<button class="btn btn-secondary" data-action="close-modal">Cancel</button><button class="btn btn-primary" data-action="confirm-modal">Confirm</button>');
        Components._confirmCallback = onConfirm;
    },

    confirmDanger(message, onConfirm) {
        this.showModal('Confirm', '<p>' + this.escapeHtml(message) + '</p>', '<button class="btn btn-secondary" data-action="close-modal">Cancel</button><button class="btn btn-danger" data-action="confirm-modal">Delete</button>');
        Components._confirmCallback = onConfirm;
    },

    _confirmCallback: null,

    showToast(message, actionText, actionCallback, duration) {
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.innerHTML = '<span class="toast-message">' + this.escapeHtml(message) + '</span>' + (actionText ? '<button class="toast-action">' + this.escapeHtml(actionText) + '</button>' : '') + '<button class="toast-close">&times;</button>';
        container.appendChild(toast);
        const remove = () => { toast.classList.add('toast-exit'); setTimeout(() => toast.remove(), 300); };
        toast.querySelector('.toast-close').addEventListener('click', remove);
        if (actionText && actionCallback) {
            toast.querySelector('.toast-action').addEventListener('click', () => { actionCallback(); remove(); });
        }
        setTimeout(remove, duration || 5000);
        setTimeout(() => toast.classList.add('toast-enter'), 10);
    },

    colorSwatch(color, selected) {
        return '<button class="color-swatch'+(selected ? ' selected' : '')+'" data-color="'+this.escapeAttr(color)+'" style="background:'+this.escapeAttr(color)+'" data-testid="swatch-'+this.escapeAttr(color)+'"></button>';
    },

    emptyState(icon, title, description, actionHtml) {
        return '<div class="empty-state"><div class="empty-icon">'+icon+'</div><h3>'+this.escapeHtml(title)+'</h3><p>'+this.escapeHtml(description)+'</p>'+(actionHtml || '')+'</div>';
    },

    pagination(currentPage, totalItems, pageSize) {
        const totalPages = Math.ceil(totalItems / pageSize);
        if (totalPages <= 1) return '';
        const start = (currentPage - 1) * pageSize + 1;
        const end = Math.min(currentPage * pageSize, totalItems);
        let html = '<div class="pagination" data-testid="pagination">';
        html += '<span class="pagination-info">Showing '+start+'–'+end+' of '+totalItems+'</span>';
        html += '<div class="pagination-buttons">';
        html += '<button class="btn btn-sm" data-action="prev-page"'+(currentPage <= 1 ? ' disabled' : '')+'>&laquo; Prev</button>';
        // Show page numbers
        const maxPages = 5;
        let startPage = Math.max(1, currentPage - Math.floor(maxPages/2));
        let endPage = Math.min(totalPages, startPage + maxPages - 1);
        if (endPage - startPage < maxPages - 1) startPage = Math.max(1, endPage - maxPages + 1);
        for (let p = startPage; p <= endPage; p++) {
            html += '<button class="btn btn-sm'+(p === currentPage ? ' btn-primary' : '')+'" data-action="goto-page" data-page="'+p+'">'+p+'</button>';
        }
        html += '<button class="btn btn-sm" data-action="next-page"'+(currentPage >= totalPages ? ' disabled' : '')+'>Next &raquo;</button>';
        html += '</div></div>';
        return html;
    },

    // Standard color palette for labels
    labelColors: ['#cc0000','#d9534f','#f0ad4e','#5bc0de','#69d100','#428bca','#7b68ee','#1aaa55','#dc3545','#6f42c1','#20c997','#17a2b8','#6c757d','#61dafb','#68a063','#ff6f61','#336791','#ff9900','#fbca04','#7057ff','#ee0701','#0e8a16','#d876e3','#b60205','#e11d48','#795548','#b91c1c','#ec4899','#0284c7','#84cc16']
};

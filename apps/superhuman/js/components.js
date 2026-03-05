const Components = {

    // ---- Utilities ----

    escapeHtml(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    },

    escapeAttr(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    },

    formatDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const now = new Date();
        const diff = now - d;
        const sameDay = d.toDateString() === now.toDateString();
        if (sameDay) {
            return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
        }
        const yesterday = new Date(now);
        yesterday.setDate(yesterday.getDate() - 1);
        if (d.toDateString() === yesterday.toDateString()) {
            return 'Yesterday';
        }
        if (diff < 7 * 24 * 60 * 60 * 1000) {
            return d.toLocaleDateString('en-US', { weekday: 'short' });
        }
        if (d.getFullYear() === now.getFullYear()) {
            return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        }
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    },

    formatFullDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }) +
            ' at ' + d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
    },

    formatTime(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
    },

    formatCalendarTime(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true }).toLowerCase();
    },

    timeAgo(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const now = new Date();
        const seconds = Math.floor((now - d) / 1000);
        if (seconds < 60) return 'just now';
        const minutes = Math.floor(seconds / 60);
        if (minutes < 60) return minutes + 'm ago';
        const hours = Math.floor(minutes / 60);
        if (hours < 24) return hours + 'h ago';
        const days = Math.floor(hours / 24);
        if (days < 7) return days + 'd ago';
        return Components.formatDate(dateStr);
    },

    // ---- Avatars ----

    avatar(name, size = 32) {
        const initials = (name || '?').split(' ').map(w => w[0]).join('').toUpperCase().substring(0, 2);
        const colors = ['#4285f4', '#ea4335', '#fbbc04', '#34a853', '#ff6d01', '#46bdc6', '#7baaf7', '#ee675c', '#f9ab00', '#5bb974'];
        const hash = (name || '').split('').reduce((acc, c) => acc + c.charCodeAt(0), 0);
        const color = colors[hash % colors.length];
        return `<div class="avatar" style="width:${size}px;height:${size}px;background:${color};border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:${Math.floor(size * 0.4)}px;color:#fff;font-weight:500;flex-shrink:0;" data-name="${Components.escapeAttr(name)}">${initials}</div>`;
    },

    // ---- Custom Dropdown ----

    dropdown(id, label, options, selectedValue, attrs = '') {
        const selectedOption = options.find(o => o.value === selectedValue);
        const displayLabel = selectedOption ? selectedOption.label : label;
        let html = `<div class="custom-dropdown" id="${Components.escapeAttr(id)}" ${attrs}>`;
        html += `<div class="dropdown-trigger" data-dropdown="${Components.escapeAttr(id)}">${Components.escapeHtml(displayLabel)}<span class="dropdown-arrow">▾</span></div>`;
        html += `<div class="dropdown-menu" id="${Components.escapeAttr(id)}-menu">`;
        for (const opt of options) {
            const selected = opt.value === selectedValue ? ' selected' : '';
            html += `<div class="dropdown-item${selected}" data-value="${Components.escapeAttr(opt.value)}" data-dropdown-id="${Components.escapeAttr(id)}">${Components.escapeHtml(opt.label)}</div>`;
        }
        html += '</div></div>';
        return html;
    },

    // ---- Toggle Switch ----

    toggle(id, label, checked, description = '') {
        return `<div class="toggle-row" id="${Components.escapeAttr(id)}-row">
            <div class="toggle-info">
                <span class="toggle-label">${Components.escapeHtml(label)}</span>
                ${description ? `<span class="toggle-description">${Components.escapeHtml(description)}</span>` : ''}
            </div>
            <label class="toggle-switch">
                <input type="checkbox" id="${Components.escapeAttr(id)}" ${checked ? 'checked' : ''}>
                <span class="toggle-slider"></span>
            </label>
        </div>`;
    },

    // ---- Radio Group ----

    radioGroup(name, options, selectedValue) {
        let html = `<div class="radio-group" data-radio-group="${Components.escapeAttr(name)}">`;
        for (const opt of options) {
            const checked = opt.value === selectedValue ? ' checked' : '';
            html += `<label class="radio-option">
                <input type="radio" name="${Components.escapeAttr(name)}" value="${Components.escapeAttr(opt.value)}"${checked}>
                <span class="radio-indicator"></span>
                <span class="radio-label">${Components.escapeHtml(opt.label)}</span>
                ${opt.description ? `<span class="radio-description">${Components.escapeHtml(opt.description)}</span>` : ''}
            </label>`;
        }
        html += '</div>';
        return html;
    },

    // ---- Text Input ----

    textInput(id, value, placeholder = '', type = 'text') {
        return `<input type="${type}" id="${Components.escapeAttr(id)}" class="text-input" value="${Components.escapeAttr(value || '')}" placeholder="${Components.escapeAttr(placeholder)}">`;
    },

    // ---- Text Area ----

    textArea(id, value, placeholder = '', rows = 4) {
        return `<textarea id="${Components.escapeAttr(id)}" class="text-area" placeholder="${Components.escapeAttr(placeholder)}" rows="${rows}">${Components.escapeHtml(value || '')}</textarea>`;
    },

    // ---- Buttons ----

    button(label, action, type = 'default', attrs = '') {
        return `<button class="btn btn-${type}" data-action="${Components.escapeAttr(action)}" ${attrs}>${Components.escapeHtml(label)}</button>`;
    },

    iconButton(icon, action, title = '', attrs = '') {
        return `<button class="btn-icon" data-action="${Components.escapeAttr(action)}" title="${Components.escapeAttr(title)}" ${attrs}>${icon}</button>`;
    },

    // ---- Badges / Counts ----

    badge(count, type = 'default') {
        if (!count || count <= 0) return '';
        return `<span class="badge badge-${type}">${count > 99 ? '99+' : count}</span>`;
    },

    // ---- Star Icon ----

    starIcon(isStarred, emailId) {
        const cls = isStarred ? 'star-icon starred' : 'star-icon';
        return `<span class="${cls}" data-action="toggle-star" data-email-id="${Components.escapeAttr(emailId)}">★</span>`;
    },

    // ---- Attachment Badge ----

    attachmentBadge(attachments) {
        if (!attachments || attachments.length === 0) return '';
        return `<span class="attachment-badge" title="${attachments.map(a => Components.escapeAttr(a.name)).join(', ')}">📎 ${attachments.length}</span>`;
    },

    // ---- Read Status Indicator ----

    readStatusIndicator(readStatus) {
        if (!readStatus || !readStatus.enabled) return '';
        if (readStatus.opens && readStatus.opens.length > 0) {
            const lastOpen = readStatus.opens[readStatus.opens.length - 1];
            return `<span class="read-status read-status-opened" title="Opened ${Components.timeAgo(lastOpen.timestamp)} on ${lastOpen.device}">✓✓</span>`;
        }
        return `<span class="read-status read-status-sent" title="Sent, not opened">✓</span>`;
    },

    // ---- Reminder Badge ----

    reminderBadge(reminder) {
        if (!reminder) return '';
        const d = new Date(reminder.date);
        const label = Components.formatDate(reminder.date);
        const typeIcon = reminder.type === 'auto' ? '🤖' : '⏰';
        return `<span class="reminder-badge" title="Reminder: ${Components.escapeAttr(Components.formatFullDate(reminder.date))}">${typeIcon} ${label}</span>`;
    },

    // ---- Label Tags ----

    labelTag(label) {
        if (!label) return '';
        const bg = label.color ? label.color.background : '#e8eaed';
        const fg = label.color ? label.color.text : '#5f6368';
        return `<span class="label-tag" style="background:${bg};color:${fg}" data-label-id="${Components.escapeAttr(label.id)}">${Components.escapeHtml(label.name)}</span>`;
    },

    // ---- Empty State ----

    emptyState(title, message, icon = '📭') {
        return `<div class="empty-state">
            <div class="empty-state-icon">${icon}</div>
            <div class="empty-state-title">${Components.escapeHtml(title)}</div>
            <div class="empty-state-message">${Components.escapeHtml(message)}</div>
        </div>`;
    },

    // ---- Snooze / Reminder Picker ----

    reminderPicker(emailId) {
        const now = new Date();
        const later = new Date(now); later.setHours(now.getHours() + 3);
        const tomorrow9am = new Date(now); tomorrow9am.setDate(now.getDate() + 1); tomorrow9am.setHours(9, 0, 0, 0);
        const nextWeek = new Date(now); nextWeek.setDate(now.getDate() + (8 - now.getDay()) % 7); nextWeek.setHours(9, 0, 0, 0);

        return `<div class="reminder-picker" data-email-id="${Components.escapeAttr(emailId)}">
            <div class="reminder-picker-title">Remind me</div>
            <div class="reminder-option" data-action="set-reminder" data-reminder-time="${later.toISOString()}" data-email-id="${Components.escapeAttr(emailId)}">
                <span class="reminder-option-icon">🕐</span>
                <span>Later today</span>
                <span class="reminder-option-time">${Components.formatCalendarTime(later.toISOString())}</span>
            </div>
            <div class="reminder-option" data-action="set-reminder" data-reminder-time="${tomorrow9am.toISOString()}" data-email-id="${Components.escapeAttr(emailId)}">
                <span class="reminder-option-icon">☀️</span>
                <span>Tomorrow</span>
                <span class="reminder-option-time">9:00 am</span>
            </div>
            <div class="reminder-option" data-action="set-reminder" data-reminder-time="${nextWeek.toISOString()}" data-email-id="${Components.escapeAttr(emailId)}">
                <span class="reminder-option-icon">📅</span>
                <span>Next week</span>
                <span class="reminder-option-time">Mon, 9:00 am</span>
            </div>
            <div class="reminder-option reminder-option-custom" data-action="set-reminder-custom" data-email-id="${Components.escapeAttr(emailId)}">
                <span class="reminder-option-icon">⚙️</span>
                <span>Pick date & time</span>
            </div>
        </div>`;
    },

    // ---- Label Picker (for applying labels to emails) ----

    labelPicker(emailId, currentLabels) {
        const userLabels = AppState.labels.filter(l => !l.isSystem);
        let html = `<div class="label-picker" data-email-id="${Components.escapeAttr(emailId)}">
            <div class="label-picker-title">Apply labels</div>`;
        for (const label of userLabels) {
            const checked = currentLabels.includes(label.id) ? ' checked' : '';
            const bg = label.color ? label.color.background : '#e8eaed';
            const fg = label.color ? label.color.text : '#5f6368';
            html += `<label class="label-picker-item" data-label-id="${Components.escapeAttr(label.id)}" data-email-id="${Components.escapeAttr(emailId)}">
                <input type="checkbox" ${checked} data-action="toggle-label" data-label-id="${Components.escapeAttr(label.id)}" data-email-id="${Components.escapeAttr(emailId)}">
                <span class="label-swatch" style="background:${bg};color:${fg}"></span>
                <span>${Components.escapeHtml(label.name)}</span>
            </label>`;
        }
        html += '</div>';
        return html;
    },

    // ---- Folder Picker (for moving emails) ----

    folderPicker(emailId) {
        const folders = ['inbox', 'done', 'trash', 'spam'];
        const folderLabels = { inbox: 'Inbox', done: 'Done', trash: 'Trash', spam: 'Spam' };
        const folderIcons = { inbox: '📥', done: '✅', trash: '🗑️', spam: '⚠️' };
        let html = `<div class="folder-picker" data-email-id="${Components.escapeAttr(emailId)}">
            <div class="folder-picker-title">Move to</div>`;
        for (const f of folders) {
            html += `<div class="folder-picker-item" data-action="move-to-folder" data-folder="${f}" data-email-id="${Components.escapeAttr(emailId)}">
                <span class="folder-picker-icon">${folderIcons[f]}</span>
                <span>${folderLabels[f]}</span>
            </div>`;
        }
        html += '</div>';
        return html;
    },

    // ---- Command Palette ----

    commandPalette() {
        return `<div class="command-palette-overlay" id="commandPalette">
            <div class="command-palette">
                <div class="command-palette-input-row">
                    <span class="command-palette-icon">⌘</span>
                    <input type="text" id="commandPaletteInput" class="command-palette-input" placeholder="Type a command..." autocomplete="off">
                </div>
                <div class="command-palette-results" id="commandPaletteResults"></div>
            </div>
        </div>`;
    },

    // ---- Modal ----

    showModal(title, bodyHtml, footerHtml = '', id = 'appModal') {
        let modal = document.getElementById(id);
        if (!modal) {
            modal = document.createElement('div');
            modal.id = id;
            modal.className = 'modal-overlay';
            document.body.appendChild(modal);
        }
        modal.innerHTML = `<div class="modal">
            <div class="modal-header">
                <h3>${title}</h3>
                <button class="modal-close" data-action="close-modal" data-modal-id="${id}">✕</button>
            </div>
            <div class="modal-body">${bodyHtml}</div>
            ${footerHtml ? `<div class="modal-footer">${footerHtml}</div>` : ''}
        </div>`;
        modal.style.display = 'flex';
        return modal;
    },

    closeModal(id = 'appModal') {
        const modal = document.getElementById(id);
        if (modal) {
            modal.style.display = 'none';
        }
    },

    // ---- Confirmation Dialog ----

    confirm(title, message, onConfirm, confirmLabel = 'Confirm', isDanger = false) {
        const btnClass = isDanger ? 'btn-danger' : 'btn-primary';
        const bodyHtml = `<p>${Components.escapeHtml(message)}</p>`;
        const footerHtml = `
            <button class="btn btn-default" data-action="close-modal" data-modal-id="confirmModal">Cancel</button>
            <button class="btn ${btnClass}" id="confirmModalBtn">${Components.escapeHtml(confirmLabel)}</button>`;
        const modal = Components.showModal(title, bodyHtml, footerHtml, 'confirmModal');
        const btn = document.getElementById('confirmModalBtn');
        if (btn) {
            btn.onclick = () => {
                Components.closeModal('confirmModal');
                if (onConfirm) onConfirm();
            };
        }
    },

    // ---- Toast Notification ----

    showToast(message, type = 'info', duration = 3000) {
        let container = document.getElementById('toastContainer');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toastContainer';
            container.className = 'toast-container';
            document.body.appendChild(container);
        }
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `<span class="toast-message">${Components.escapeHtml(message)}</span>
            <button class="toast-dismiss" onclick="this.parentElement.remove()">✕</button>`;
        container.appendChild(toast);
        setTimeout(() => { toast.classList.add('toast-show'); }, 10);
        if (duration > 0) {
            setTimeout(() => {
                toast.classList.remove('toast-show');
                setTimeout(() => toast.remove(), 300);
            }, duration);
        }
        return toast;
    },

    // ---- Undo Toast ----

    showUndoToast(message, onUndo, duration = 5000) {
        let container = document.getElementById('toastContainer');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toastContainer';
            container.className = 'toast-container';
            document.body.appendChild(container);
        }
        const toast = document.createElement('div');
        toast.className = 'toast toast-info';
        toast.innerHTML = `<span class="toast-message">${Components.escapeHtml(message)}</span>
            <button class="toast-undo" id="undoBtn">Undo</button>
            <button class="toast-dismiss" onclick="this.parentElement.remove()">✕</button>`;
        container.appendChild(toast);
        setTimeout(() => { toast.classList.add('toast-show'); }, 10);
        const undoBtn = toast.querySelector('#undoBtn');
        if (undoBtn && onUndo) {
            undoBtn.onclick = () => {
                onUndo();
                toast.remove();
            };
        }
        if (duration > 0) {
            setTimeout(() => {
                toast.classList.remove('toast-show');
                setTimeout(() => toast.remove(), 300);
            }, duration);
        }
    },

    // ---- Color Picker (for labels) ----

    colorPicker(selectedColor) {
        const colors = [
            { background: '#e8f0fe', text: '#1a73e8' },
            { background: '#fce8e6', text: '#d93025' },
            { background: '#fef7e0', text: '#f9ab00' },
            { background: '#e6f4ea', text: '#1e8e3e' },
            { background: '#f3e8fd', text: '#8430ce' },
            { background: '#e8f7fc', text: '#0d7377' },
            { background: '#fde7e0', text: '#e8710a' },
            { background: '#e8eaed', text: '#5f6368' },
            { background: '#fce4ec', text: '#c2185b' },
            { background: '#e0f2f1', text: '#00897b' }
        ];
        let html = '<div class="color-picker">';
        for (const c of colors) {
            const selected = selectedColor && selectedColor.background === c.background ? ' selected' : '';
            html += `<div class="color-swatch${selected}" style="background:${c.background};border:2px solid ${c.text}" data-color-bg="${c.background}" data-color-text="${c.text}"></div>`;
        }
        html += '</div>';
        return html;
    }
};

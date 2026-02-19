// ============================================================
// components.js — Reusable UI components
// ============================================================

const Components = {

    // ---- Escape Helpers ----
    escapeHtml(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;')
            .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#x27;');
    },

    escapeAttr(str) {
        return this.escapeHtml(str);
    },

    // ---- Format Helpers ----
    formatDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    },

    timeAgo(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const now = new Date();
        const diff = now - d;
        const mins = Math.floor(diff / 60000);
        if (mins < 1) return 'just now';
        if (mins < 60) return mins + 'm ago';
        const hours = Math.floor(mins / 60);
        if (hours < 24) return hours + 'h ago';
        const days = Math.floor(hours / 24);
        if (days < 30) return days + 'd ago';
        return this.formatDate(dateStr);
    },

    // ---- Custom Dropdown ----
    dropdown(id, options, selectedValue, opts = {}) {
        const placeholder = opts.placeholder || 'Select...';
        const searchable = opts.searchable || false;
        const selected = options.find(o => o.value === selectedValue);
        const displayText = selected ? this.escapeHtml(selected.label) : placeholder;

        let searchHtml = '';
        if (searchable) {
            searchHtml = `<div class="dropdown-search-wrap">
                <input type="text" class="dropdown-search" data-dropdown-id="${id}" placeholder="Search..." />
            </div>`;
        }

        let itemsHtml = options.map(o =>
            `<div class="dropdown-item ${o.value === selectedValue ? 'selected' : ''}"
                  data-value="${this.escapeAttr(o.value)}"
                  data-dropdown-id="${id}">
                ${this.escapeHtml(o.label)}
                ${o.description ? `<span class="dropdown-item-desc">${this.escapeHtml(o.description)}</span>` : ''}
            </div>`
        ).join('');

        return `<div class="custom-dropdown" id="${id}" data-value="${this.escapeAttr(selectedValue || '')}">
            <div class="dropdown-trigger" data-dropdown-id="${id}">
                <span class="dropdown-label">${displayText}</span>
                <span class="dropdown-arrow">&#9662;</span>
            </div>
            <div class="dropdown-menu">
                ${searchHtml}
                <div class="dropdown-items">${itemsHtml}</div>
            </div>
        </div>`;
    },

    // ---- Modal ----
    showModal(title, bodyHtml, footerHtml, opts = {}) {
        const modal = document.getElementById('appModal');
        if (!modal) return;

        const titleEl = modal.querySelector('.modal-title');
        const bodyEl = modal.querySelector('.modal-body');
        const footerEl = modal.querySelector('.modal-footer');

        titleEl.textContent = title;
        bodyEl.innerHTML = bodyHtml;
        footerEl.innerHTML = footerHtml;

        if (opts.wide) modal.querySelector('.modal-content').classList.add('wide');
        else modal.querySelector('.modal-content').classList.remove('wide');

        modal.classList.add('active');
        AppState.modalOpen = true;
    },

    closeModal() {
        const modal = document.getElementById('appModal');
        if (modal) {
            modal.classList.remove('active');
            AppState.modalOpen = false;
        }
    },

    confirm(title, message, onConfirm, opts = {}) {
        const isDanger = opts.danger || false;
        const confirmText = opts.confirmText || 'Confirm';
        const cancelText = opts.cancelText || 'Cancel';

        this.showModal(title,
            `<p style="margin: 0;">${this.escapeHtml(message)}</p>`,
            `<button class="btn btn-secondary" onclick="Components.closeModal()">${cancelText}</button>
             <button class="btn ${isDanger ? 'btn-danger' : 'btn-primary'}" id="modalConfirmBtn">${confirmText}</button>`
        );

        setTimeout(() => {
            const btn = document.getElementById('modalConfirmBtn');
            if (btn) {
                btn.addEventListener('click', () => {
                    onConfirm();
                    this.closeModal();
                });
            }
        }, 50);
    },

    // ---- Toast ----
    showToast(message, type = 'info', duration = 4000) {
        const container = document.getElementById('toastContainer');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        const icons = { info: 'i', success: '\u2713', warning: '\u26A0', error: '\u2717' };
        toast.innerHTML = `<span class="toast-icon">${icons[type] || 'i'}</span>
            <span class="toast-message">${this.escapeHtml(message)}</span>
            <button class="toast-close" onclick="this.parentElement.remove()">\u00D7</button>`;
        container.appendChild(toast);

        setTimeout(() => { if (toast.parentElement) toast.remove(); }, duration);
    },

    // ---- Form Components ----
    formField(label, inputHtml, opts = {}) {
        const required = opts.required ? '<span class="required">*</span>' : '';
        const error = opts.error ? `<div class="field-error-msg">${this.escapeHtml(opts.error)}</div>` : '';
        const hint = opts.hint ? `<div class="field-hint">${this.escapeHtml(opts.hint)}</div>` : '';
        return `<div class="form-field ${opts.error ? 'has-error' : ''}">
            <label class="form-label">${this.escapeHtml(label)}${required}</label>
            ${inputHtml}
            ${hint}
            ${error}
        </div>`;
    },

    textInput(id, value, opts = {}) {
        const placeholder = opts.placeholder || '';
        const maxLength = opts.maxLength ? `maxlength="${opts.maxLength}"` : '';
        const disabled = opts.disabled ? 'disabled' : '';
        return `<input type="text" id="${id}" class="form-input" value="${this.escapeAttr(value || '')}"
                    placeholder="${this.escapeAttr(placeholder)}" ${maxLength} ${disabled}
                    data-testid="${id}" />`;
    },

    textarea(id, value, opts = {}) {
        const rows = opts.rows || 3;
        const maxLength = opts.maxLength ? `maxlength="${opts.maxLength}"` : '';
        return `<textarea id="${id}" class="form-textarea" rows="${rows}" ${maxLength}
                    data-testid="${id}">${this.escapeHtml(value || '')}</textarea>`;
    },

    numberInput(id, value, opts = {}) {
        const min = opts.min !== undefined ? `min="${opts.min}"` : '';
        const max = opts.max !== undefined ? `max="${opts.max}"` : '';
        const step = opts.step ? `step="${opts.step}"` : '';
        return `<input type="number" id="${id}" class="form-input form-input-number" value="${value || 0}"
                    ${min} ${max} ${step} data-testid="${id}" />`;
    },

    rangeInput(id, value, min, max, opts = {}) {
        const step = opts.step || 1;
        const unit = opts.unit || '';
        return `<div class="range-input-wrap">
            <input type="range" id="${id}" class="form-range" value="${value}" min="${min}" max="${max}" step="${step}"
                data-testid="${id}" />
            <span class="range-value" id="${id}Value">${value}${unit}</span>
        </div>`;
    },

    checkbox(id, checked, label, opts = {}) {
        return `<label class="checkbox-label" for="${id}">
            <input type="checkbox" id="${id}" ${checked ? 'checked' : ''} data-testid="${id}" />
            <span class="checkbox-text">${this.escapeHtml(label)}</span>
        </label>`;
    },

    colorInput(id, value) {
        return `<div class="color-input-wrap">
            <div class="color-swatch" id="${id}Swatch" style="background:${value}" data-color="${this.escapeAttr(value)}" data-input-id="${id}"></div>
            <input type="text" id="${id}" class="form-input color-hex-input" value="${this.escapeAttr(value || '#000000')}"
                maxlength="7" pattern="^#[0-9A-Fa-f]{6}$" data-testid="${id}" />
        </div>`;
    },

    // ---- Status Badge ----
    statusBadge(status) {
        const colors = { live: 'green', draft: 'gray', trial: 'orange' };
        const labels = { live: 'Live', draft: 'Draft', trial: 'Trial' };
        return `<span class="badge badge-${colors[status] || 'gray'}">${labels[status] || status}</span>`;
    },

    // ---- Theme Card ----
    themeCard(theme) {
        const isLive = theme.status === 'live';
        return `<div class="theme-card ${isLive ? 'theme-card-live' : ''}" data-theme-id="${theme.id}" data-testid="theme-card-${theme.id}">
            <div class="theme-card-preview">
                <div class="theme-preview-placeholder">
                    <span class="theme-preview-name">${this.escapeHtml(theme.name)}</span>
                    <span class="theme-preview-version">v${this.escapeHtml(theme.version)}</span>
                </div>
            </div>
            <div class="theme-card-info">
                <div class="theme-card-header">
                    <h3 class="theme-card-title">${this.escapeHtml(theme.name)}</h3>
                    ${this.statusBadge(theme.status)}
                </div>
                <div class="theme-card-meta">
                    <span>Last saved: ${this.timeAgo(theme.lastSaved)}</span>
                    ${theme.updateAvailable ? '<span class="update-available">Update available (v' + this.escapeHtml(theme.updateVersion) + ')</span>' : ''}
                </div>
                <div class="theme-card-actions">
                    ${isLive
                        ? `<button class="btn btn-primary btn-sm" data-action="customize" data-theme-id="${theme.id}">Customize</button>`
                        : `<button class="btn btn-primary btn-sm" data-action="customize" data-theme-id="${theme.id}">Customize</button>
                           <button class="btn btn-secondary btn-sm" data-action="publish" data-theme-id="${theme.id}">Publish</button>`
                    }
                    <div class="theme-card-more">
                        <button class="btn btn-icon btn-sm theme-more-btn" data-action="theme-menu" data-theme-id="${theme.id}">&#8942;</button>
                        <div class="theme-menu" id="themeMenu${theme.id}">
                            <div class="theme-menu-item" data-action="rename" data-theme-id="${theme.id}">Rename</div>
                            <div class="theme-menu-item" data-action="duplicate" data-theme-id="${theme.id}">Duplicate</div>
                            <div class="theme-menu-item" data-action="preview" data-theme-id="${theme.id}">Preview</div>
                            ${!isLive ? `<div class="theme-menu-item theme-menu-item-danger" data-action="delete" data-theme-id="${theme.id}">Delete</div>` : ''}
                        </div>
                    </div>
                </div>
            </div>
        </div>`;
    },

    // ---- Section Tree Item ----
    sectionTreeItem(section, blocks) {
        const blockItems = blocks.map(b =>
            `<div class="tree-block ${b.hidden ? 'tree-hidden' : ''} ${AppState.selectedBlockId === b.id ? 'tree-selected' : ''}"
                  data-block-id="${b.id}" data-testid="block-${b.id}">
                <span class="tree-icon">&#9632;</span>
                <span class="tree-label">${this.escapeHtml(b.name)}</span>
                ${b.hidden ? '<span class="tree-hidden-icon" title="Hidden">&#128065;</span>' : ''}
            </div>`
        ).join('');

        return `<div class="tree-section ${section.hidden ? 'tree-hidden' : ''}" data-section-id="${section.id}" data-testid="section-${section.id}">
            <div class="tree-section-header ${AppState.selectedSectionId === section.id ? 'tree-selected' : ''}">
                <span class="tree-expand" data-section-id="${section.id}">&#9654;</span>
                <span class="tree-label" data-section-id="${section.id}">${this.escapeHtml(section.name)}</span>
                ${section.hidden ? '<span class="tree-hidden-icon" title="Hidden">&#128065;</span>' : ''}
            </div>
            <div class="tree-section-blocks" id="sectionBlocks${section.id}">
                ${blockItems}
            </div>
        </div>`;
    },

    // ---- Info / Warning / Error boxes ----
    infoBox(message) {
        return `<div class="msg-box msg-info"><span class="msg-icon">i</span> ${this.escapeHtml(message)}</div>`;
    },

    warningBox(message) {
        return `<div class="msg-box msg-warning"><span class="msg-icon">\u26A0</span> ${this.escapeHtml(message)}</div>`;
    },

    errorBox(message) {
        return `<div class="msg-box msg-error"><span class="msg-icon">\u2717</span> ${this.escapeHtml(message)}</div>`;
    },

    successBox(message) {
        return `<div class="msg-box msg-success"><span class="msg-icon">\u2713</span> ${this.escapeHtml(message)}</div>`;
    },

    // ---- Tabs ----
    tabs(tabList, activeTab) {
        return `<div class="tabs">
            ${tabList.map(t =>
                `<div class="tab-item ${t.id === activeTab ? 'tab-active' : ''}" data-tab="${t.id}" data-testid="tab-${t.id}">
                    ${this.escapeHtml(t.label)}
                </div>`
            ).join('')}
        </div>`;
    },

    // ---- Color Scheme Preview ----
    colorSchemePreview(scheme, isSelected) {
        return `<div class="color-scheme-card ${isSelected ? 'color-scheme-selected' : ''}" data-scheme-id="${scheme.id}" data-testid="color-scheme-${scheme.id}">
            <div class="color-scheme-preview" style="background:${scheme.background}; color:${scheme.text};">
                <div class="color-scheme-sample-text">Aa</div>
                <div class="color-scheme-buttons">
                    <span class="color-scheme-btn-solid" style="background:${scheme.solidButtonBg}; color:${scheme.solidButtonText};">Btn</span>
                    <span class="color-scheme-btn-outline" style="border-color:${scheme.outlineButton}; color:${scheme.outlineButton};">Btn</span>
                </div>
            </div>
            <div class="color-scheme-name">${this.escapeHtml(scheme.name)}</div>
        </div>`;
    }
};

// ---- Global event delegation for dropdowns ----
document.addEventListener('click', function(e) {
    // Dropdown trigger
    const trigger = e.target.closest('.dropdown-trigger');
    if (trigger) {
        const dropdown = trigger.closest('.custom-dropdown');
        if (dropdown) {
            // Close all other dropdowns
            document.querySelectorAll('.custom-dropdown.open').forEach(d => {
                if (d !== dropdown) d.classList.remove('open');
            });
            dropdown.classList.toggle('open');
            const searchInput = dropdown.querySelector('.dropdown-search');
            if (searchInput) setTimeout(() => searchInput.focus(), 50);
            e.stopPropagation();
            return;
        }
    }

    // Dropdown item selection
    const item = e.target.closest('.dropdown-item');
    if (item) {
        const dropdownId = item.dataset.dropdownId;
        const dropdown = document.getElementById(dropdownId);
        if (dropdown) {
            const value = item.dataset.value;
            dropdown.dataset.value = value;
            const label = dropdown.querySelector('.dropdown-label');
            if (label) label.textContent = item.textContent.trim();
            dropdown.querySelectorAll('.dropdown-item').forEach(i => i.classList.remove('selected'));
            item.classList.add('selected');
            dropdown.classList.remove('open');

            // Fire custom change event
            dropdown.dispatchEvent(new CustomEvent('change', { detail: { value: value } }));
        }
        e.stopPropagation();
        return;
    }

    // Close dropdowns on outside click
    document.querySelectorAll('.custom-dropdown.open').forEach(d => d.classList.remove('open'));

    // Close theme menus
    document.querySelectorAll('.theme-menu.active').forEach(m => m.classList.remove('active'));
});

// Dropdown search
document.addEventListener('input', function(e) {
    if (e.target.classList.contains('dropdown-search')) {
        const query = e.target.value.toLowerCase();
        const dropdownId = e.target.dataset.dropdownId;
        const dropdown = document.getElementById(dropdownId);
        if (dropdown) {
            dropdown.querySelectorAll('.dropdown-item').forEach(item => {
                const text = item.textContent.toLowerCase();
                item.style.display = text.includes(query) ? '' : 'none';
            });
        }
    }
});

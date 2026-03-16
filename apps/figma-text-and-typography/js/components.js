// Figma Text & Typography - Reusable UI Components
const Components = {

    // ---- Custom Dropdown ----
    dropdown(id, currentValue, options, extraClass = '') {
        const displayValue = currentValue || 'Select...';
        return `
            <div class="custom-dropdown ${extraClass}" id="${id}" data-value="${String(currentValue).replace(/"/g, '&quot;')}">
                <div class="dropdown-trigger" data-dropdown-id="${id}">
                    <span class="dropdown-value">${displayValue}</span>
                    <svg class="dropdown-arrow" width="10" height="6" viewBox="0 0 10 6"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
                </div>
                <div class="dropdown-menu">
                    ${options.map(opt => {
                        const val = typeof opt === 'object' ? opt.value : opt;
                        const label = typeof opt === 'object' ? opt.label : opt;
                        const selected = String(val) === String(currentValue);
                        return `
                            <div class="dropdown-item ${selected ? 'selected' : ''}"
                                 data-dropdown-id="${id}"
                                 data-value="${String(val).replace(/"/g, '&quot;')}">
                                ${label}
                                ${selected ? '<svg class="check-icon" width="12" height="10" viewBox="0 0 12 10"><path d="M1 5l3 3 7-7" stroke="currentColor" stroke-width="2" fill="none"/></svg>' : ''}
                            </div>`;
                    }).join('')}
                </div>
            </div>`;
    },

    // ---- Toggle Switch ----
    toggle(id, checked, label = '', description = '') {
        return `
            <div class="toggle-row">
                <div class="toggle-info">
                    ${label ? `<span class="toggle-label">${label}</span>` : ''}
                    ${description ? `<span class="toggle-description">${description}</span>` : ''}
                </div>
                <div class="toggle-switch ${checked ? 'active' : ''}" id="${id}" data-toggle-id="${id}">
                    <div class="toggle-knob"></div>
                </div>
            </div>`;
    },

    // ---- Number Input ----
    numberInput(id, value, min, max, step, unit, label) {
        const displayVal = value === 'auto' ? '' : value;
        return `
            <div class="number-input-group" id="${id}-group">
                ${label ? `<label class="number-label">${label}</label>` : ''}
                <div class="number-input-wrapper">
                    <input type="text" class="number-input" id="${id}"
                        value="${displayVal}"
                        data-min="${min}" data-max="${max}" data-step="${step || 1}"
                        placeholder="${value === 'auto' ? 'Auto' : ''}">
                    ${unit ? `<span class="number-unit">${unit}</span>` : ''}
                </div>
            </div>`;
    },

    // ---- Section Header ----
    sectionHeader(title, subtitle) {
        return `
            <div class="section-header">
                <h2 class="section-title">${title}</h2>
                ${subtitle ? `<p class="section-subtitle">${subtitle}</p>` : ''}
            </div>`;
    },

    // ---- Property Row ----
    propertyRow(label, controlHtml, id) {
        return `
            <div class="property-row" ${id ? `id="${id}"` : ''}>
                <label class="property-label">${label}</label>
                <div class="property-control">${controlHtml}</div>
            </div>`;
    },

    // ---- Icon Button ----
    iconButton(id, icon, tooltip, active, action, extraData) {
        const dataAttrs = extraData ? Object.entries(extraData).map(([k, v]) => `data-${k}="${String(v).replace(/"/g, '&quot;')}"`).join(' ') : '';
        return `<button class="icon-btn ${active ? 'active' : ''}" id="${id}"
            data-action="${action}" ${dataAttrs}
            title="${tooltip}">${icon}</button>`;
    },

    // ---- Button Group (segmented control) ----
    buttonGroup(id, options, currentValue) {
        return `
            <div class="button-group" id="${id}">
                ${options.map(opt => {
                    const val = typeof opt === 'object' ? opt.value : opt;
                    const label = typeof opt === 'object' ? opt.label : opt;
                    const icon = typeof opt === 'object' ? opt.icon : null;
                    const active = val === currentValue;
                    return `<button class="btn-group-item ${active ? 'active' : ''}"
                        data-group-id="${id}" data-value="${val}"
                        title="${label}">${icon || label}</button>`;
                }).join('')}
            </div>`;
    },

    // ---- Modal ----
    modal(id, title, bodyHtml, footerHtml, size) {
        return `
            <div class="modal-overlay" id="${id}">
                <div class="modal ${size || ''}">
                    <div class="modal-header">
                        <h3 class="modal-title">${title}</h3>
                        <button class="modal-close" data-action="closeModal">&times;</button>
                    </div>
                    <div class="modal-body">${bodyHtml}</div>
                    ${footerHtml ? `<div class="modal-footer">${footerHtml}</div>` : ''}
                </div>
            </div>`;
    },

    // ---- Toast ----
    toast(message) {
        if (!message) return '';
        return `<div class="toast visible">${message}</div>`;
    },

    // ---- Badge ----
    badge(text, type) {
        return `<span class="badge badge-${type || 'default'}">${text}</span>`;
    },

    // ---- Text Preview ----
    textPreview(layer) {
        const font = AppState.getFontFamily(layer.fontFamily);
        let style = `font-size: ${Math.min(layer.fontSize, 24)}px;`;

        if (layer.lineHeight && layer.lineHeight.value !== 'auto') {
            if (layer.lineHeight.unit === 'px') {
                style += `line-height: ${Math.min(layer.lineHeight.value, 32)}px;`;
            } else {
                style += `line-height: ${layer.lineHeight.value}%;`;
            }
        }

        if (layer.letterSpacing && layer.letterSpacing.value !== 0) {
            if (layer.letterSpacing.unit === 'em') {
                style += `letter-spacing: ${layer.letterSpacing.value}em;`;
            } else {
                style += `letter-spacing: ${layer.letterSpacing.value}px;`;
            }
        }

        style += `text-align: ${layer.horizontalAlign};`;

        if (layer.textDecoration === 'underline') style += 'text-decoration: underline;';
        if (layer.textDecoration === 'strikethrough') style += 'text-decoration: line-through;';

        if (layer.letterCase === 'uppercase') style += 'text-transform: uppercase;';
        else if (layer.letterCase === 'lowercase') style += 'text-transform: lowercase;';
        else if (layer.letterCase === 'capitalize') style += 'text-transform: capitalize;';
        else if (layer.letterCase === 'small-caps') style += 'font-variant: small-caps;';

        if (layer.textDirection === 'rtl') style += 'direction: rtl;';

        let truncStyle = '';
        if (layer.truncation && layer.truncation.enabled) {
            truncStyle = 'overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;';
            if (layer.truncation.maxLines) truncStyle += `-webkit-line-clamp:${layer.truncation.maxLines};`;
        }

        let content = this._escapeHtml(layer.content);
        if (layer.listStyle === 'bulleted') {
            content = content.split('\n').map(line => `<div class="preview-list-item"><span class="preview-bullet">&bull;</span> ${line}</div>`).join('');
        } else if (layer.listStyle === 'numbered') {
            const counters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
            content = content.split('\n').map((line, i) => `<div class="preview-list-item"><span class="preview-number">${counters[i] || i + 1}.</span> ${line}</div>`).join('');
        } else {
            content = content.replace(/\n/g, '<br>');
        }

        return `<div class="text-preview-box" style="${style}${truncStyle}"
            ${layer.width ? `style="max-width:${layer.width}px;"` : ''}>${content}</div>`;
    },

    // ---- Alignment icons ----
    alignIcon(type) {
        const icons = {
            left: '<svg width="16" height="14" viewBox="0 0 16 14"><line x1="0" y1="1" x2="16" y2="1" stroke="currentColor" stroke-width="2"/><line x1="0" y1="5" x2="10" y2="5" stroke="currentColor" stroke-width="2"/><line x1="0" y1="9" x2="14" y2="9" stroke="currentColor" stroke-width="2"/><line x1="0" y1="13" x2="8" y2="13" stroke="currentColor" stroke-width="2"/></svg>',
            center: '<svg width="16" height="14" viewBox="0 0 16 14"><line x1="0" y1="1" x2="16" y2="1" stroke="currentColor" stroke-width="2"/><line x1="3" y1="5" x2="13" y2="5" stroke="currentColor" stroke-width="2"/><line x1="1" y1="9" x2="15" y2="9" stroke="currentColor" stroke-width="2"/><line x1="4" y1="13" x2="12" y2="13" stroke="currentColor" stroke-width="2"/></svg>',
            right: '<svg width="16" height="14" viewBox="0 0 16 14"><line x1="0" y1="1" x2="16" y2="1" stroke="currentColor" stroke-width="2"/><line x1="6" y1="5" x2="16" y2="5" stroke="currentColor" stroke-width="2"/><line x1="2" y1="9" x2="16" y2="9" stroke="currentColor" stroke-width="2"/><line x1="8" y1="13" x2="16" y2="13" stroke="currentColor" stroke-width="2"/></svg>',
            justify: '<svg width="16" height="14" viewBox="0 0 16 14"><line x1="0" y1="1" x2="16" y2="1" stroke="currentColor" stroke-width="2"/><line x1="0" y1="5" x2="16" y2="5" stroke="currentColor" stroke-width="2"/><line x1="0" y1="9" x2="16" y2="9" stroke="currentColor" stroke-width="2"/><line x1="0" y1="13" x2="16" y2="13" stroke="currentColor" stroke-width="2"/></svg>'
        };
        return icons[type] || '';
    },

    vertAlignIcon(type) {
        const icons = {
            top: '<svg width="14" height="16" viewBox="0 0 14 16"><line x1="0" y1="0" x2="14" y2="0" stroke="currentColor" stroke-width="2"/><rect x="3" y="3" width="8" height="4" fill="currentColor" rx="1"/></svg>',
            middle: '<svg width="14" height="16" viewBox="0 0 14 16"><rect x="3" y="6" width="8" height="4" fill="currentColor" rx="1"/></svg>',
            bottom: '<svg width="14" height="16" viewBox="0 0 14 16"><line x1="0" y1="16" x2="14" y2="16" stroke="currentColor" stroke-width="2"/><rect x="3" y="9" width="8" height="4" fill="currentColor" rx="1"/></svg>'
        };
        return icons[type] || '';
    },

    resizingIcon(type) {
        const icons = {
            'auto-width': '<svg width="16" height="14" viewBox="0 0 16 14"><rect x="0" y="0" width="16" height="14" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/><line x1="2" y1="4" x2="14" y2="4" stroke="currentColor" stroke-width="2"/><line x1="2" y1="8" x2="10" y2="8" stroke="currentColor" stroke-width="2"/></svg>',
            'auto-height': '<svg width="16" height="14" viewBox="0 0 16 14"><rect x="0" y="0" width="16" height="14" fill="none" stroke="currentColor" stroke-width="1"/><line x1="2" y1="4" x2="14" y2="4" stroke="currentColor" stroke-width="2"/><line x1="2" y1="8" x2="10" y2="8" stroke="currentColor" stroke-width="2"/></svg>',
            'fixed': '<svg width="16" height="14" viewBox="0 0 16 14"><rect x="0" y="0" width="16" height="14" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="2" y1="4" x2="14" y2="4" stroke="currentColor" stroke-width="2"/><line x1="2" y1="8" x2="10" y2="8" stroke="currentColor" stroke-width="2"/></svg>'
        };
        return icons[type] || '';
    },

    // ---- Slider ----
    slider(id, value, min, max, step) {
        const pct = ((value - min) / (max - min)) * 100;
        return `
            <div class="slider-container" id="${id}-container">
                <input type="range" class="slider" id="${id}"
                    min="${min}" max="${max}" step="${step || 1}" value="${value}"
                    style="background: linear-gradient(to right, var(--accent) ${pct}%, var(--bg-tertiary) ${pct}%);">
                <input type="text" class="slider-value" id="${id}-value" value="${value}">
            </div>`;
    },

    // ---- Empty State ----
    emptyState(icon, title, description) {
        return `
            <div class="empty-state">
                <div class="empty-icon">${icon}</div>
                <h3 class="empty-title">${title}</h3>
                <p class="empty-description">${description}</p>
            </div>`;
    },

    // ---- Helpers ----
    _escapeHtml(str) {
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }
};

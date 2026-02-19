// ============================================================
// components.js — Reusable UI components
// ============================================================

const Components = {
    // ---- Utility ----
    escapeHtml(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#039;');
    },

    escapeAttr(str) {
        if (!str) return '';
        return String(str).replace(/"/g, '&quot;').replace(/'/g, '&#039;');
    },

    formatDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    },

    formatDateShort(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    },

    formatMetricValue(metric, value) {
        if (value === null || value === undefined) return '—';
        if (metric === 'cls') return value.toFixed(2);
        return Math.round(value).toLocaleString();
    },

    formatMetricUnit(metric) {
        if (metric === 'cls') return '';
        return 'ms';
    },

    // ---- Rating ----
    getRatingClass(rating) {
        if (rating === 'good') return 'rating-good';
        if (rating === 'moderate') return 'rating-moderate';
        if (rating === 'poor') return 'rating-poor';
        return '';
    },

    getRatingLabel(rating) {
        if (rating === 'good') return 'Good';
        if (rating === 'moderate') return 'Moderate';
        if (rating === 'poor') return 'Poor';
        return 'N/A';
    },

    ratingBadge(rating) {
        const cls = this.getRatingClass(rating);
        const label = this.getRatingLabel(rating);
        return `<span class="rating-badge ${cls}" data-testid="rating-badge">${label}</span>`;
    },

    // ---- Metric Card ----
    metricCard(metric, value, rating, opts = {}) {
        const metricInfo = METRICS[metric.toUpperCase()] || { shortName: metric, name: metric, unit: '' };
        const formattedValue = this.formatMetricValue(metric, value);
        const unit = this.formatMetricUnit(metric);
        const ratingClass = this.getRatingClass(rating);
        const clickAttr = opts.clickRoute ? `data-route="${opts.clickRoute}"` : '';
        const cursorClass = opts.clickRoute ? 'cursor-pointer' : '';

        return `
            <div class="metric-card ${cursorClass}" ${clickAttr} data-testid="metric-card-${metric}">
                <div class="metric-card-header">
                    <span class="metric-label">${metricInfo.shortName} P75 ${unit ? '(' + unit + ')' : ''}</span>
                    ${this.ratingBadge(rating)}
                </div>
                <div class="metric-card-body">
                    <span class="metric-value ${ratingClass}">${formattedValue}</span>
                    ${unit ? `<span class="metric-unit">${unit}</span>` : ''}
                </div>
                <div class="metric-card-footer text-muted text-small">
                    ${metricInfo.name}
                </div>
            </div>`;
    },

    // ---- Distribution Bar ----
    distributionBar(good, moderate, poor) {
        return `
            <div class="distribution-bar" data-testid="distribution-bar">
                <div class="distribution-segment distribution-segment-good" style="width:${good}%" title="Good: ${good}%"></div>
                <div class="distribution-segment distribution-segment-moderate" style="width:${moderate}%" title="Moderate: ${moderate}%"></div>
                <div class="distribution-segment distribution-segment-poor" style="width:${poor}%" title="Poor: ${poor}%"></div>
            </div>
            <div class="distribution-legend">
                <span class="legend-item"><span class="legend-dot distribution-segment-good"></span> Good ${good}%</span>
                <span class="legend-item"><span class="legend-dot distribution-segment-moderate"></span> Moderate ${moderate}%</span>
                <span class="legend-item"><span class="legend-dot distribution-segment-poor"></span> Poor ${poor}%</span>
            </div>`;
    },

    // ---- Custom Dropdown ----
    dropdown(id, options, selectedValue, opts = {}) {
        const placeholder = opts.placeholder || 'Select...';
        const searchable = opts.searchable || false;
        const selectedOpt = options.find(o => o.value === selectedValue);
        const displayText = selectedOpt ? selectedOpt.label : placeholder;

        let itemsHtml = '';
        options.forEach(opt => {
            const selected = opt.value === selectedValue ? 'selected' : '';
            itemsHtml += `<div class="dropdown-item ${selected}" data-value="${this.escapeAttr(opt.value)}">${this.escapeHtml(opt.label)}</div>`;
        });

        return `
            <div class="custom-dropdown" id="${id}" data-testid="${id}" data-value="${this.escapeAttr(selectedValue || '')}">
                <div class="dropdown-trigger">${this.escapeHtml(displayText)}<span class="dropdown-arrow">&#9662;</span></div>
                <div class="dropdown-menu">
                    ${searchable ? `<input type="text" class="dropdown-search" placeholder="Search..." data-testid="${id}-search">` : ''}
                    <div class="dropdown-items">${itemsHtml}</div>
                </div>
            </div>`;
    },

    // ---- Tabs ----
    tabs(id, items, activeTab) {
        let html = `<div class="tabs" id="${id}" data-testid="${id}">`;
        items.forEach(item => {
            const active = item.id === activeTab ? 'active' : '';
            html += `<div class="tab-item ${active}" data-tab="${item.id}" data-testid="tab-${item.id}">${this.escapeHtml(item.label)}</div>`;
        });
        html += '</div>';
        return html;
    },

    // ---- Badges ----
    badge(text, type) {
        return `<span class="badge badge-${type || 'default'}" data-testid="badge-${type}">${this.escapeHtml(text)}</span>`;
    },

    statusBadge(status) {
        const labels = { pending: 'Pending', in_progress: 'In Progress', completed: 'Completed', dismissed: 'Dismissed', active: 'Active', available: 'Available' };
        const types = { pending: 'warning', in_progress: 'info', completed: 'good', dismissed: 'muted', active: 'good', available: 'default' };
        return this.badge(labels[status] || status, types[status] || 'default');
    },

    priorityBadge(priority) {
        const types = { critical: 'poor', high: 'warning', medium: 'info', low: 'muted' };
        return this.badge(priority.charAt(0).toUpperCase() + priority.slice(1), types[priority] || 'default');
    },

    impactBadge(impact) {
        const types = { positive: 'good', negative: 'poor', neutral: 'muted' };
        const labels = { positive: 'Positive', negative: 'Negative', neutral: 'Neutral' };
        return this.badge(labels[impact] || impact, types[impact] || 'default');
    },

    // ---- Form Fields ----
    formField(id, label, inputHtml, opts = {}) {
        const required = opts.required ? '<span class="required">*</span>' : '';
        const hint = opts.hint ? `<div class="form-hint">${this.escapeHtml(opts.hint)}</div>` : '';
        const error = opts.error ? `<div class="form-error" data-testid="${id}-error">${this.escapeHtml(opts.error)}</div>` : '';
        return `
            <div class="form-group" data-testid="form-group-${id}">
                <label class="form-label" for="${id}">${label}${required}</label>
                ${inputHtml}
                ${hint}
                ${error}
            </div>`;
    },

    textInput(id, value, opts = {}) {
        const placeholder = opts.placeholder || '';
        const disabled = opts.disabled ? 'disabled' : '';
        const type = opts.type || 'text';
        const errorClass = opts.error ? 'field-error' : '';
        return `<input type="${type}" class="form-input ${errorClass}" id="${id}" data-testid="${id}" value="${this.escapeAttr(value || '')}" placeholder="${this.escapeAttr(placeholder)}" ${disabled}>`;
    },

    numberInput(id, value, opts = {}) {
        const min = opts.min !== undefined ? `min="${opts.min}"` : '';
        const max = opts.max !== undefined ? `max="${opts.max}"` : '';
        const step = opts.step !== undefined ? `step="${opts.step}"` : '';
        const disabled = opts.disabled ? 'disabled' : '';
        const errorClass = opts.error ? 'field-error' : '';
        return `<input type="number" class="form-input ${errorClass}" id="${id}" data-testid="${id}" value="${value !== undefined && value !== null ? value : ''}" ${min} ${max} ${step} ${disabled}>`;
    },

    textarea(id, value, opts = {}) {
        const placeholder = opts.placeholder || '';
        const rows = opts.rows || 3;
        return `<textarea class="form-textarea" id="${id}" data-testid="${id}" rows="${rows}" placeholder="${this.escapeAttr(placeholder)}">${this.escapeHtml(value || '')}</textarea>`;
    },

    checkbox(id, label, checked, opts = {}) {
        const checkedAttr = checked ? 'checked' : '';
        const disabled = opts.disabled ? 'disabled' : '';
        return `
            <div class="checkbox-wrapper">
                <label class="checkbox-label" for="${id}">
                    <input type="checkbox" id="${id}" data-testid="${id}" ${checkedAttr} ${disabled}>
                    <span class="checkbox-custom"></span>
                    ${this.escapeHtml(label)}
                </label>
            </div>`;
    },

    toggleSwitch(id, label, checked, opts = {}) {
        const checkedAttr = checked ? 'checked' : '';
        const disabled = opts.disabled ? 'disabled' : '';
        return `
            <div class="toggle-wrapper" data-testid="toggle-${id}">
                <label class="toggle-label">
                    <div class="toggle-switch">
                        <input type="checkbox" id="${id}" data-testid="${id}" ${checkedAttr} ${disabled}>
                        <span class="toggle-slider"></span>
                    </div>
                    <span class="toggle-text">${this.escapeHtml(label)}</span>
                </label>
            </div>`;
    },

    dateInput(id, value, opts = {}) {
        const placeholder = opts.placeholder || 'YYYY-MM-DD';
        const errorClass = opts.error ? 'field-error' : '';
        return `<input type="text" class="form-input date-input ${errorClass}" id="${id}" data-testid="${id}" value="${this.escapeAttr(value || '')}" placeholder="${this.escapeAttr(placeholder)}" pattern="\\d{4}-\\d{2}-\\d{2}">`;
    },

    // ---- Buttons ----
    button(text, opts = {}) {
        const type = opts.type || 'secondary';
        const size = opts.size ? `btn-${opts.size}` : '';
        const id = opts.id ? `id="${opts.id}"` : '';
        const testId = opts.testId ? `data-testid="${opts.testId}"` : '';
        const disabled = opts.disabled ? 'disabled' : '';
        const onClick = opts.onClick ? `onclick="${this.escapeAttr(opts.onClick)}"` : '';
        return `<button class="btn btn-${type} ${size}" ${id} ${testId} ${disabled} ${onClick}>${text}</button>`;
    },

    // ---- Modal ----
    showModal(title, body, footer) {
        const overlay = document.getElementById('modalOverlay');
        const container = document.getElementById('modalContainer');
        document.getElementById('modalTitle').textContent = title;
        document.getElementById('modalBody').innerHTML = body;
        document.getElementById('modalFooter').innerHTML = footer || '';
        overlay.classList.add('active');
        AppState.modalOpen = true;
    },

    closeModal() {
        const overlay = document.getElementById('modalOverlay');
        overlay.classList.remove('active');
        AppState.modalOpen = false;
    },

    confirm(title, message, onConfirm, opts = {}) {
        const type = opts.type || 'primary';
        const confirmText = opts.confirmText || 'Confirm';
        const cancelText = opts.cancelText || 'Cancel';

        const body = `<p>${message}</p>`;
        const footer = `
            <button class="btn btn-secondary" data-testid="modal-cancel" onclick="Components.closeModal()">${cancelText}</button>
            <button class="btn btn-${type}" data-testid="modal-confirm" id="modalConfirmBtn">${confirmText}</button>`;

        this.showModal(title, body, footer);

        document.getElementById('modalConfirmBtn').addEventListener('click', () => {
            onConfirm();
            this.closeModal();
        });
    },

    // ---- Toast ----
    showToast(message, type = 'success', duration = 3000) {
        const container = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.setAttribute('data-testid', 'toast');

        const icons = { success: '&#10003;', error: '&#10007;', warning: '&#9888;', info: '&#8505;' };
        toast.innerHTML = `<span class="toast-icon">${icons[type] || ''}</span><span class="toast-message">${this.escapeHtml(message)}</span>`;

        container.appendChild(toast);
        setTimeout(() => toast.classList.add('toast-visible'), 10);

        setTimeout(() => {
            toast.classList.remove('toast-visible');
            setTimeout(() => toast.remove(), 300);
        }, duration);
    },

    // ---- Info/Warning/Error/Success Boxes ----
    infoBox(message) {
        return `<div class="info-box" data-testid="info-box"><span class="box-icon">&#8505;</span> ${message}</div>`;
    },

    warningBox(message) {
        return `<div class="warning-box" data-testid="warning-box"><span class="box-icon">&#9888;</span> ${message}</div>`;
    },

    errorBox(message) {
        return `<div class="error-box" data-testid="error-box"><span class="box-icon">&#10007;</span> ${message}</div>`;
    },

    successBox(message) {
        return `<div class="success-box" data-testid="success-box"><span class="box-icon">&#10003;</span> ${message}</div>`;
    },

    // ---- Data Table ----
    dataTable(id, columns, rows, opts = {}) {
        let html = `<div class="table-wrapper"><table class="data-table" id="${id}" data-testid="${id}">`;
        html += '<thead><tr>';
        columns.forEach(col => {
            html += `<th class="${col.align === 'right' ? 'text-right' : ''}">${this.escapeHtml(col.label)}</th>`;
        });
        html += '</tr></thead><tbody>';

        if (rows.length === 0) {
            html += `<tr><td colspan="${columns.length}" class="text-center text-muted">No data available</td></tr>`;
        } else {
            rows.forEach(row => {
                html += '<tr>';
                columns.forEach(col => {
                    const value = col.render ? col.render(row) : (row[col.key] || '');
                    html += `<td class="${col.align === 'right' ? 'text-right' : ''}">${value}</td>`;
                });
                html += '</tr>';
            });
        }

        html += '</tbody></table></div>';
        return html;
    },

    // ---- Simple Bar Chart (CSS-based) ----
    barChart(id, data, opts = {}) {
        const maxValue = opts.maxValue || Math.max(...data.map(d => d.value), 1);
        const height = opts.height || 200;
        const metricKey = opts.metric || 'lcp';

        let html = `<div class="chart-container" id="${id}" data-testid="${id}" style="height:${height + 40}px">`;
        html += `<div class="bar-chart" style="height:${height}px">`;

        // Threshold lines
        const thresholds = METRIC_THRESHOLDS[metricKey.toUpperCase()];
        if (thresholds) {
            const goodLine = (thresholds.good / maxValue) * 100;
            const modLine = (thresholds.moderate / maxValue) * 100;
            if (goodLine <= 100) {
                html += `<div class="threshold-line threshold-good" style="bottom:${goodLine}%"><span class="threshold-label">Good: ${thresholds.good}${metricKey === 'cls' ? '' : 'ms'}</span></div>`;
            }
            if (modLine <= 100) {
                html += `<div class="threshold-line threshold-moderate" style="bottom:${modLine}%"><span class="threshold-label">Poor: ${thresholds.moderate}${metricKey === 'cls' ? '' : 'ms'}</span></div>`;
            }
        }

        const barWidth = Math.max(4, Math.min(20, Math.floor(600 / data.length)));
        data.forEach((d, i) => {
            const pct = Math.min((d.value / maxValue) * 100, 100);
            const rating = AppState.getRating(metricKey, d.value);
            html += `<div class="bar bar-${rating}" style="height:${pct}%;width:${barWidth}px" title="${d.label}: ${Components.formatMetricValue(metricKey, d.value)}${Components.formatMetricUnit(metricKey)}"></div>`;
        });

        html += '</div>';

        // X-axis labels (show every few)
        html += '<div class="chart-x-axis">';
        const step = Math.max(1, Math.floor(data.length / 8));
        data.forEach((d, i) => {
            if (i % step === 0 || i === data.length - 1) {
                html += `<span class="axis-label" style="left:${(i / Math.max(data.length - 1, 1)) * 100}%">${d.label}</span>`;
            }
        });
        html += '</div></div>';

        return html;
    },

    // ---- Event Timeline ----
    eventTimeline(events) {
        if (!events || events.length === 0) {
            return '<div class="text-muted text-center mt-md">No events recorded</div>';
        }

        let html = '<div class="event-timeline" data-testid="event-timeline">';
        events.sort((a, b) => new Date(b.date) - new Date(a.date)).forEach(event => {
            const impactClass = event.impact === 'positive' ? 'event-positive' : event.impact === 'negative' ? 'event-negative' : 'event-neutral';
            html += `
                <div class="event-item ${impactClass}" data-testid="event-item-${event.id}">
                    <div class="event-dot"></div>
                    <div class="event-content">
                        <div class="event-header">
                            <strong>${this.escapeHtml(event.title)}</strong>
                            <span class="text-muted text-small">${this.formatDate(event.date)}</span>
                        </div>
                        <div class="event-description text-muted">${this.escapeHtml(event.description)}</div>
                        <div class="event-tags">
                            ${this.impactBadge(event.impact)}
                            <span class="tag">${event.metric === 'all' ? 'All Metrics' : event.metric.toUpperCase()}</span>
                        </div>
                    </div>
                    <div class="event-actions">
                        <button class="btn btn-sm btn-secondary" data-testid="edit-event-${event.id}" data-action="edit-event" data-event-id="${event.id}">Edit</button>
                        <button class="btn btn-sm btn-danger" data-testid="remove-event-${event.id}" data-action="remove-event" data-event-id="${event.id}">Remove</button>
                    </div>
                </div>`;
        });
        html += '</div>';
        return html;
    },

    // ---- Empty State ----
    emptyState(message, actionHtml) {
        return `
            <div class="empty-state" data-testid="empty-state">
                <div class="empty-state-message">${this.escapeHtml(message)}</div>
                ${actionHtml || ''}
            </div>`;
    }
};

// ---- Global Dropdown Event Delegation ----
document.addEventListener('click', function(e) {
    // Toggle dropdown
    const trigger = e.target.closest('.dropdown-trigger');
    if (trigger) {
        const dropdown = trigger.closest('.custom-dropdown');
        const menu = dropdown.querySelector('.dropdown-menu');

        // Close all other dropdowns first
        document.querySelectorAll('.dropdown-menu.open').forEach(m => {
            if (m !== menu) m.classList.remove('open');
        });

        menu.classList.toggle('open');

        // Focus search input if exists
        const search = menu.querySelector('.dropdown-search');
        if (search && menu.classList.contains('open')) {
            setTimeout(() => search.focus(), 50);
        }

        e.stopPropagation();
        return;
    }

    // Select dropdown item
    const item = e.target.closest('.dropdown-item');
    if (item && item.closest('.dropdown-menu')) {
        const dropdown = item.closest('.custom-dropdown');
        const menu = dropdown.querySelector('.dropdown-menu');
        const triggerEl = dropdown.querySelector('.dropdown-trigger');
        const value = item.getAttribute('data-value');

        // Update selection
        dropdown.setAttribute('data-value', value);

        // Update trigger text (preserve arrow)
        const arrow = triggerEl.querySelector('.dropdown-arrow');
        triggerEl.textContent = item.textContent;
        if (arrow) triggerEl.appendChild(arrow.cloneNode(true));

        // Mark selected
        dropdown.querySelectorAll('.dropdown-item').forEach(di => di.classList.remove('selected'));
        item.classList.add('selected');

        // Close menu
        menu.classList.remove('open');

        // Fire custom event
        dropdown.dispatchEvent(new CustomEvent('change', { detail: { value }, bubbles: true }));

        e.stopPropagation();
        return;
    }

    // Click outside closes dropdowns
    if (!e.target.closest('.custom-dropdown')) {
        document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
    }
});

// Dropdown search filtering
document.addEventListener('input', function(e) {
    if (e.target.classList.contains('dropdown-search')) {
        const query = e.target.value.toLowerCase();
        const menu = e.target.closest('.dropdown-menu');
        menu.querySelectorAll('.dropdown-item').forEach(item => {
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? '' : 'none';
        });
    }
});

// Close modal on overlay click
document.addEventListener('click', function(e) {
    if (e.target.id === 'modalOverlay') {
        Components.closeModal();
    }
});

// Close modal on close button
document.addEventListener('click', function(e) {
    if (e.target.id === 'modalClose' || e.target.closest('#modalClose')) {
        Components.closeModal();
    }
});

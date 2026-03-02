/* ============================================================
   Shopify Dynamic Checkout – Reusable UI Components
   ============================================================ */

const Components = {

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
        return String(str).replace(/"/g, '&quot;').replace(/'/g, '&#039;');
    },

    formatDate(isoStr) {
        if (!isoStr) return '—';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    },

    formatDateTime(isoStr) {
        if (!isoStr) return '—';
        const d = new Date(isoStr);
        return d.toLocaleDateString('en-US', {
            year: 'numeric', month: 'short', day: 'numeric',
            hour: '2-digit', minute: '2-digit'
        });
    },

    timeAgo(isoStr) {
        if (!isoStr) return '';
        const now = new Date();
        const then = new Date(isoStr);
        const diffMs = now - then;
        const diffMin = Math.floor(diffMs / 60000);
        if (diffMin < 1) return 'just now';
        if (diffMin < 60) return `${diffMin}m ago`;
        const diffHr = Math.floor(diffMin / 60);
        if (diffHr < 24) return `${diffHr}h ago`;
        const diffDays = Math.floor(diffHr / 24);
        if (diffDays < 30) return `${diffDays}d ago`;
        const diffMonths = Math.floor(diffDays / 30);
        if (diffMonths < 12) return `${diffMonths}mo ago`;
        return `${Math.floor(diffMonths / 12)}y ago`;
    },

    formatPrice(price) {
        if (price == null) return '—';
        return '$' + parseFloat(price).toFixed(2);
    },

    // Status badge
    statusBadge(status) {
        const colors = {
            active: { bg: '#D1FAE5', text: '#065F46', label: 'Active' },
            draft: { bg: '#FEF3C7', text: '#92400E', label: 'Draft' },
            archived: { bg: '#F3F4F6', text: '#6B7280', label: 'Archived' },
            main: { bg: '#DBEAFE', text: '#1E40AF', label: 'Published' },
            unpublished: { bg: '#F3F4F6', text: '#6B7280', label: 'Unpublished' },
            demo: { bg: '#EDE9FE', text: '#5B21B6', label: 'Trial' }
        };
        const c = colors[status] || { bg: '#F3F4F6', text: '#6B7280', label: status };
        return `<span class="status-badge" style="background:${c.bg};color:${c.text}">${this.escapeHtml(c.label)}</span>`;
    },

    // Toggle switch
    toggle(id, checked, label, dataAttrs) {
        const attrs = dataAttrs ? Object.entries(dataAttrs).map(([k, v]) => `data-${k}="${this.escapeAttr(v)}"`).join(' ') : '';
        return `
            <label class="toggle-wrapper" for="${this.escapeAttr(id)}">
                <div class="toggle-switch ${checked ? 'active' : ''}" id="${this.escapeAttr(id)}" data-action="toggle" ${attrs} role="switch" aria-checked="${checked}" tabindex="0">
                    <div class="toggle-knob"></div>
                </div>
                <span class="toggle-label">${this.escapeHtml(label)}</span>
            </label>`;
    },

    // Checkbox
    checkbox(id, checked, label, dataAttrs) {
        const attrs = dataAttrs ? Object.entries(dataAttrs).map(([k, v]) => `data-${k}="${this.escapeAttr(v)}"`).join(' ') : '';
        return `
            <label class="checkbox-wrapper">
                <div class="custom-checkbox ${checked ? 'checked' : ''}" id="${this.escapeAttr(id)}" data-action="checkbox" ${attrs} role="checkbox" aria-checked="${checked}" tabindex="0">
                    ${checked ? '<svg viewBox="0 0 16 16" width="12" height="12"><polyline points="3.5 8 6.5 11 12.5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>' : ''}
                </div>
                <span>${this.escapeHtml(label)}</span>
            </label>`;
    },

    // Custom dropdown
    dropdown(id, options, selectedValue, placeholder, dataAttrs) {
        const attrs = dataAttrs ? Object.entries(dataAttrs).map(([k, v]) => `data-${k}="${this.escapeAttr(v)}"`).join(' ') : '';
        const selected = options.find(o => o.value === selectedValue);
        const displayText = selected ? selected.label : (placeholder || 'Select...');
        const optionsHtml = options.map(o =>
            `<div class="dropdown-item ${o.value === selectedValue ? 'selected' : ''}" data-action="dropdown-select" data-dropdown-id="${this.escapeAttr(id)}" data-value="${this.escapeAttr(o.value)}" ${attrs}>${this.escapeHtml(o.label)}</div>`
        ).join('');

        return `
            <div class="custom-dropdown" id="${this.escapeAttr(id)}" data-dropdown>
                <div class="dropdown-trigger" data-action="dropdown-toggle" data-dropdown-id="${this.escapeAttr(id)}">
                    <span class="dropdown-value">${this.escapeHtml(displayText)}</span>
                    <svg class="dropdown-arrow" viewBox="0 0 20 20" width="16" height="16"><path d="M5 7.5L10 12.5L15 7.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="dropdown-menu" style="display:none">
                    ${optionsHtml}
                </div>
            </div>`;
    },

    // Color swatch picker
    colorPicker(id, currentColor, label) {
        return `
            <div class="color-picker-field">
                <label class="field-label">${this.escapeHtml(label)}</label>
                <div class="color-picker-input" data-action="open-color-picker" data-picker-id="${this.escapeAttr(id)}">
                    <div class="color-swatch-preview" style="background:${this.escapeAttr(currentColor)}"></div>
                    <input type="text" class="color-text-input" id="${this.escapeAttr(id)}" value="${this.escapeAttr(currentColor)}" data-action="color-text-change" data-picker-id="${this.escapeAttr(id)}" maxlength="7" />
                </div>
            </div>`;
    },

    // Font dropdown
    fontDropdown(id, selectedFont, label) {
        const options = AppState.availableFonts.map(f => ({ value: f, label: f }));
        return `
            <div class="font-field">
                <label class="field-label">${this.escapeHtml(label)}</label>
                ${this.dropdown(id, options, selectedFont, 'Select font...')}
            </div>`;
    },

    // Toast notification
    toast(message, type) {
        const icons = {
            success: '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" fill="currentColor"/></svg>',
            error: '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" fill="currentColor"/></svg>',
            warning: '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 10-2 0 1 1 0 002 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" fill="currentColor"/></svg>',
            info: '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" fill="currentColor"/></svg>'
        };
        return `
            <div class="toast toast-${type}" data-testid="toast">
                <span class="toast-icon">${icons[type] || icons.info}</span>
                <span class="toast-message">${this.escapeHtml(message)}</span>
                <button class="toast-close" data-action="close-toast">&times;</button>
            </div>`;
    },

    // Modal
    modal(title, body, footer) {
        return `
            <div class="modal-overlay active" id="modalOverlay" data-action="close-modal-overlay">
                <div class="modal" data-testid="modal">
                    <div class="modal-header">
                        <h2>${this.escapeHtml(title)}</h2>
                        <button class="modal-close" data-action="close-modal">&times;</button>
                    </div>
                    <div class="modal-body">${body}</div>
                    ${footer ? `<div class="modal-footer">${footer}</div>` : ''}
                </div>
            </div>`;
    },

    // Confirm dialog
    confirmDialog(title, message, confirmLabel, confirmAction, destructive) {
        const btnClass = destructive ? 'btn-danger' : 'btn-primary';
        return this.modal(title, `<p>${this.escapeHtml(message)}</p>`,
            `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
             <button class="btn ${btnClass}" data-action="${this.escapeAttr(confirmAction)}">${this.escapeHtml(confirmLabel)}</button>`
        );
    },

    // Payment method logo/icon
    paymentLogo(method) {
        const logos = {
            shop_pay: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#5A31F4"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="8" font-weight="bold">Shop</text></svg>`,
            apple_pay: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#000"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="7" font-weight="bold">Apple</text></svg>`,
            google_pay: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#4285F4"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="7" font-weight="bold">GPay</text></svg>`,
            paypal: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#003087"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="7" font-weight="bold">PayPal</text></svg>`,
            amazon_pay: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#FF9900"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="7" font-weight="bold">Amazon</text></svg>`,
            venmo: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#3D95CE"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="8" font-weight="bold">Venmo</text></svg>`,
            shopify_payments: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#96BF48"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="6" font-weight="bold">Shopify</text></svg>`,
            manual: `<svg viewBox="0 0 40 24" width="40" height="24"><rect width="40" height="24" rx="4" fill="#6B7280"/><text x="20" y="15" text-anchor="middle" fill="white" font-size="7" font-weight="bold">Manual</text></svg>`
        };
        return logos[method.brand] || `<div class="payment-logo-placeholder" style="background:${this.escapeAttr(method.logoColor)}">${this.escapeHtml(method.name[0])}</div>`;
    },

    // Breadcrumb
    breadcrumb(items) {
        return `<nav class="breadcrumb" data-testid="breadcrumb">
            ${items.map((item, i) => {
                if (i === items.length - 1) {
                    return `<span class="breadcrumb-current">${this.escapeHtml(item.label)}</span>`;
                }
                return `<a class="breadcrumb-link" data-route="${this.escapeAttr(item.route)}">${this.escapeHtml(item.label)}</a><span class="breadcrumb-sep">/</span>`;
            }).join('')}
        </nav>`;
    },

    // Pagination
    pagination(page, totalPages, total) {
        if (totalPages <= 1) return '';
        const start = (page - 1) * AppState.pageSize + 1;
        const end = Math.min(page * AppState.pageSize, total);
        let pages = '';
        for (let i = 1; i <= totalPages; i++) {
            if (i === 1 || i === totalPages || Math.abs(i - page) <= 1) {
                pages += `<button class="pagination-page ${i === page ? 'active' : ''}" data-action="go-to-page" data-page="${i}">${i}</button>`;
            } else if (i === 2 && page > 3 || i === totalPages - 1 && page < totalPages - 2) {
                pages += '<span class="pagination-ellipsis">...</span>';
            }
        }
        return `
            <div class="pagination" data-testid="pagination">
                <span class="pagination-info">Showing ${start}-${end} of ${total}</span>
                <div class="pagination-controls">
                    <button class="pagination-prev ${page <= 1 ? 'disabled' : ''}" data-action="prev-page" ${page <= 1 ? 'disabled' : ''}>Previous</button>
                    ${pages}
                    <button class="pagination-next ${page >= totalPages ? 'disabled' : ''}" data-action="next-page" ${page >= totalPages ? 'disabled' : ''}>Next</button>
                </div>
            </div>`;
    },

    // Search input
    searchInput(value, placeholder) {
        return `
            <div class="search-input-wrapper">
                <svg class="search-icon" viewBox="0 0 20 20" width="16" height="16"><path d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" fill="currentColor"/></svg>
                <input type="text" class="search-input" value="${this.escapeAttr(value)}" placeholder="${this.escapeAttr(placeholder)}" data-action="search" />
                ${value ? '<button class="search-clear" data-action="clear-search">&times;</button>' : ''}
            </div>`;
    },

    // Empty state
    emptyState(icon, title, description) {
        return `
            <div class="empty-state" data-testid="empty-state">
                <div class="empty-state-icon">${icon}</div>
                <h3>${this.escapeHtml(title)}</h3>
                <p>${this.escapeHtml(description)}</p>
            </div>`;
    },

    // Info/Warning/Error box
    infoBox(message, type) {
        const icons = { info: 'i', warning: '!', error: 'x', success: '&#10003;' };
        return `<div class="info-box info-box-${type || 'info'}">
            <span class="info-box-icon">${icons[type] || icons.info}</span>
            <span>${this.escapeHtml(message)}</span>
        </div>`;
    },

    // Accelerated checkout button preview
    checkoutButtonPreview(theme, template, paymentMethods) {
        const activeMethods = paymentMethods.filter(pm => pm.type === 'accelerated' && pm.isActive);
        const colors = theme.settings.colors;
        const fonts = theme.settings.typography;

        let html = '<div class="checkout-preview" data-testid="checkout-preview">';

        // Add to cart button
        html += `<button class="preview-add-to-cart" style="background:${this.escapeAttr(colors.primaryText)};color:${this.escapeAttr(colors.primaryBg)};font-family:${this.escapeAttr(fonts.buttonFont)},sans-serif">${this.escapeHtml(template.buyButtonText)}</button>`;

        if (template.showAcceleratedCheckout) {
            // Unbranded button
            html += `<button class="preview-buy-now" style="background:${this.escapeAttr(colors.accentButtonBg)};color:${this.escapeAttr(colors.accentButtonText)};font-family:${this.escapeAttr(fonts.buttonFont)},sans-serif">Buy it now</button>`;

            // Branded buttons
            if (activeMethods.length > 0) {
                html += '<div class="preview-branded-buttons">';
                activeMethods.forEach(method => {
                    html += `<button class="preview-branded-btn" style="background:${this.escapeAttr(method.logoColor)};color:#fff">${this.escapeHtml(method.name)}</button>`;
                });
                html += '</div>';
            }
        }

        html += '</div>';
        return html;
    }
};

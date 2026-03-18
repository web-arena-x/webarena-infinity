/* views.js — All view renderers for Xero Invoicing */
/* eslint-disable */

const Views = {

    renderSidebar() {
        const items = [
            { route: 'dashboard', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="14" y="12" width="7" height="9" rx="1"/><rect x="3" y="16" width="7" height="5" rx="1"/></svg>', label: 'Dashboard' },
            { route: 'invoices', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>', label: 'Invoices' },
            { route: 'contacts', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>', label: 'Contacts' },
            { route: 'settings', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>', label: 'Settings' },
        ];
        const current = AppState.currentView;
        let html = '';
        items.forEach(item => {
            const active = (current === item.route || (item.route === 'invoices' && ['new-invoice','edit-invoice'].includes(current)));
            html += '<a class="sidebar-item' + (active ? ' active' : '') + '" data-route="' + item.route + '" data-testid="nav-' + item.route + '">';
            html += '<span class="sidebar-icon">' + item.icon + '</span>';
            html += '<span class="sidebar-label">' + item.label + '</span>';
            html += '</a>';
        });
        return html;
    },

    renderContent() {
        switch (AppState.currentView) {
            case 'dashboard': return this.renderDashboard();
            case 'invoices': return this.renderInvoiceList();
            case 'new-invoice': return this.renderInvoiceForm(null);
            case 'edit-invoice': return this.renderInvoiceForm(AppState.currentItemId);
            case 'invoice-detail': return this.renderInvoiceDetail(AppState.currentItemId);
            case 'contacts': return this.renderContacts();
            case 'contact-detail': return this.renderContactDetail(AppState.currentItemId);
            case 'settings': return this.renderSettings();
            default: return this.renderInvoiceList();
        }
    },

    // ==================== Dashboard ====================

    renderDashboard() {
        const stats = AppState.getDashboardStats();
        let html = '<div class="page-header"><h1>Dashboard</h1></div>';
        html += '<div class="dashboard-grid">';

        // Summary cards
        html += '<div class="stat-card"><div class="stat-label">Total Invoiced</div><div class="stat-value">' + Components.formatCurrency(stats.totalInvoiced) + '</div><div class="stat-sub">' + stats.invoiceCount + ' invoices</div></div>';
        html += '<div class="stat-card stat-outstanding"><div class="stat-label">Outstanding</div><div class="stat-value">' + Components.formatCurrency(stats.totalOutstanding) + '</div><div class="stat-sub">' + stats.outstandingCount + ' invoices</div></div>';
        html += '<div class="stat-card stat-overdue"><div class="stat-label">Overdue</div><div class="stat-value">' + Components.formatCurrency(stats.totalOverdue) + '</div><div class="stat-sub">' + stats.overdueCount + ' invoices</div></div>';
        html += '<div class="stat-card stat-paid"><div class="stat-label">Paid</div><div class="stat-value">' + Components.formatCurrency(stats.totalPaid) + '</div><div class="stat-sub">' + stats.paidCount + ' invoices</div></div>';

        html += '</div>';

        // Aging summary
        html += '<div class="section-card"><h2>Aging Summary</h2>';
        html += '<table class="data-table" data-testid="aging-table"><thead><tr>';
        html += '<th>Current</th><th>1\u201330 days</th><th>31\u201360 days</th><th>61\u201390 days</th><th>90+ days</th><th>Total</th>';
        html += '</tr></thead><tbody><tr>';
        html += '<td>' + Components.formatCurrency(stats.aging.current) + '</td>';
        html += '<td>' + Components.formatCurrency(stats.aging.days1_30) + '</td>';
        html += '<td>' + Components.formatCurrency(stats.aging.days31_60) + '</td>';
        html += '<td>' + Components.formatCurrency(stats.aging.days61_90) + '</td>';
        html += '<td>' + Components.formatCurrency(stats.aging.days90plus) + '</td>';
        html += '<td><strong>' + Components.formatCurrency(stats.totalOutstanding) + '</strong></td>';
        html += '</tr></tbody></table></div>';

        // Status breakdown
        html += '<div class="section-card"><h2>Invoice Status Breakdown</h2><div class="status-breakdown">';
        const statusCounts = {};
        AppState.invoices.forEach(inv => { statusCounts[inv.status] = (statusCounts[inv.status] || 0) + 1; });
        ['draft', 'awaiting_approval', 'awaiting_payment', 'paid', 'overdue', 'voided'].forEach(st => {
            const count = statusCounts[st] || 0;
            html += '<div class="status-row"><span>' + Components.statusBadge(st) + '</span><span class="status-count">' + count + '</span></div>';
        });
        html += '</div></div>';

        // Recent invoices
        html += '<div class="section-card"><h2>Recent Invoices</h2>';
        const recent = [...AppState.invoices].sort((a, b) => b.createdAt.localeCompare(a.createdAt)).slice(0, 10);
        html += '<table class="data-table" data-testid="recent-invoices-table"><thead><tr>';
        html += '<th>Invoice</th><th>Contact</th><th>Date</th><th>Total</th><th>Status</th>';
        html += '</tr></thead><tbody>';
        recent.forEach(inv => {
            html += '<tr class="clickable-row" data-route="invoices/' + inv.id + '">';
            html += '<td>' + Components.escapeHtml(inv.invoiceNumber) + '</td>';
            html += '<td>' + Components.escapeHtml(AppState.getContactName(inv.contactId)) + '</td>';
            html += '<td>' + Components.formatDate(inv.issueDate) + '</td>';
            html += '<td>' + Components.formatCurrency(inv.total, inv.currency) + '</td>';
            html += '<td>' + Components.statusBadge(inv.status) + '</td>';
            html += '</tr>';
        });
        html += '</tbody></table></div>';

        return html;
    },

    // ==================== Invoice List ====================

    renderInvoiceList() {
        const paged = AppState.getPagedInvoices();
        const f = AppState.invoiceFilters;

        let html = '<div class="page-header"><h1>Invoices</h1>';
        html += '<div class="page-actions">';
        html += '<button class="btn btn-primary" data-action="new-invoice" data-testid="new-invoice-btn">+ New Invoice</button>';
        html += '</div></div>';

        // Filters
        html += '<div class="filters-bar" data-testid="invoice-filters">';
        // Status filter
        const statusOpts = [
            { value: '', label: 'All Statuses' },
            { value: 'draft', label: 'Draft' },
            { value: 'awaiting_approval', label: 'Awaiting Approval' },
            { value: 'awaiting_payment', label: 'Awaiting Payment' },
            { value: 'paid', label: 'Paid' },
            { value: 'overdue', label: 'Overdue' },
            { value: 'voided', label: 'Voided' },
        ];
        html += Components.dropdown('filter-status', statusOpts.slice(1), f.status, 'All Statuses');

        // Contact filter
        const contactOpts = AppState.contacts.map(c => ({ value: c.id, label: c.name })).sort((a, b) => a.label.localeCompare(b.label));
        html += Components.dropdown('filter-contact', contactOpts, f.contact, 'All Contacts');

        // Date range
        html += '<div class="form-group form-group-inline"><input type="text" class="form-input form-input-sm" id="filter-date-from" placeholder="From (YYYY-MM-DD)" value="' + Components.escapeAttr(f.dateFrom) + '" data-testid="filter-date-from"></div>';
        html += '<div class="form-group form-group-inline"><input type="text" class="form-input form-input-sm" id="filter-date-to" placeholder="To (YYYY-MM-DD)" value="' + Components.escapeAttr(f.dateTo) + '" data-testid="filter-date-to"></div>';

        // Search
        html += '<div class="form-group form-group-inline search-group"><input type="text" class="form-input form-input-sm" id="filter-search" placeholder="Search invoices..." value="' + Components.escapeAttr(f.search) + '" data-testid="filter-search"><svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>';
        html += '</div>';

        // Bulk actions
        if (AppState.selectedInvoiceIds.length > 0) {
            html += '<div class="bulk-actions-bar" data-testid="bulk-actions">';
            html += '<span>' + AppState.selectedInvoiceIds.length + ' selected</span>';
            html += '<button class="btn btn-sm btn-secondary" data-action="bulk-approve">Approve</button>';
            html += '<button class="btn btn-sm btn-secondary" data-action="bulk-send">Send</button>';
            html += '<button class="btn btn-sm btn-danger" data-action="bulk-delete">Delete Drafts</button>';
            html += '<button class="btn btn-sm" data-action="clear-selection">Clear</button>';
            html += '</div>';
        }

        if (paged.items.length === 0) {
            html += Components.emptyState(
                '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
                'No invoices found',
                'Try adjusting your filters or create a new invoice.'
            );
            return html;
        }

        // Table
        html += '<div class="table-wrapper"><table class="data-table" data-testid="invoice-table"><thead><tr>';
        html += '<th class="checkbox-col"><input type="checkbox" id="select-all-invoices" data-action="toggle-select-all" ' + (AppState.selectedInvoiceIds.length === paged.items.length && paged.items.length > 0 ? 'checked' : '') + '></th>';

        const sortCols = [
            { field: 'invoiceNumber', label: 'Number' },
            { field: 'reference', label: 'Reference' },
            { field: 'contactName', label: 'To' },
            { field: 'issueDate', label: 'Date' },
            { field: 'dueDate', label: 'Due Date' },
            { field: 'total', label: 'Total' },
            { field: 'amountDue', label: 'Due' },
            { field: 'status', label: 'Status' },
        ];
        sortCols.forEach(col => {
            const isCurrent = AppState.invoiceSortField === col.field;
            const arrow = isCurrent ? (AppState.invoiceSortDir === 'asc' ? ' \u25b2' : ' \u25bc') : '';
            html += '<th class="sortable" data-action="sort-invoices" data-field="' + col.field + '" data-testid="sort-' + col.field + '">' + col.label + arrow + '</th>';
        });
        html += '</tr></thead><tbody>';

        paged.items.forEach(inv => {
            const contact = AppState.getContactById(inv.contactId);
            const isSelected = AppState.selectedInvoiceIds.includes(inv.id);
            html += '<tr class="invoice-row' + (isSelected ? ' selected-row' : '') + '" data-invoice-id="' + inv.id + '" data-testid="invoice-row-' + inv.id + '">';
            html += '<td class="checkbox-col"><input type="checkbox" data-action="toggle-select-invoice" data-id="' + inv.id + '" ' + (isSelected ? 'checked' : '') + '></td>';
            html += '<td><a class="link" data-route="invoices/' + inv.id + '">' + Components.escapeHtml(inv.invoiceNumber) + '</a></td>';
            html += '<td>' + Components.escapeHtml(inv.reference || '\u2014') + '</td>';
            html += '<td>' + (contact ? Components.escapeHtml(contact.name) : '\u2014') + '</td>';
            html += '<td>' + Components.formatDate(inv.issueDate) + '</td>';
            html += '<td>' + Components.formatDate(inv.dueDate) + '</td>';
            html += '<td class="text-right">' + Components.formatCurrency(inv.total, inv.currency) + '</td>';
            html += '<td class="text-right">' + Components.formatCurrency(inv.amountDue, inv.currency) + '</td>';
            html += '<td>' + Components.statusBadge(inv.status) + '</td>';
            html += '</tr>';
        });

        html += '</tbody></table></div>';
        html += Components.pagination(paged.page, paged.total, paged.pageSize);

        return html;
    },

    // ==================== Invoice Detail ====================

    renderInvoiceDetail(invoiceId) {
        const inv = AppState.getInvoiceById(invoiceId);
        if (!inv) return Components.emptyState('', 'Invoice not found', 'The requested invoice could not be found.');

        const contact = AppState.getContactById(inv.contactId);
        const payments = AppState.getPaymentsForInvoice(inv.id);
        const currency = AppState.getCurrencyByCode(inv.currency);

        let html = '<div class="page-header">';
        html += '<div class="page-header-left">';
        html += '<button class="btn btn-ghost" data-route="invoices" data-testid="back-to-invoices">&larr; Back to Invoices</button>';
        html += '<h1>' + Components.escapeHtml(inv.invoiceNumber) + ' ' + Components.statusBadge(inv.status) + '</h1>';
        html += '</div>';

        // Action buttons
        html += '<div class="page-actions" data-testid="invoice-actions">';
        if (inv.status === 'draft') {
            html += '<button class="btn btn-secondary" data-action="edit-invoice" data-id="' + inv.id + '" data-testid="edit-btn">Edit</button>';
            html += '<button class="btn btn-primary" data-action="approve-invoice" data-id="' + inv.id + '" data-testid="approve-btn">Approve</button>';
            html += '<button class="btn btn-secondary" data-action="send-invoice" data-id="' + inv.id + '" data-testid="send-btn">Approve & Send</button>';
            html += '<button class="btn btn-danger-outline" data-action="delete-invoice" data-id="' + inv.id + '" data-testid="delete-btn">Delete</button>';
        } else if (inv.status === 'awaiting_approval') {
            html += '<button class="btn btn-secondary" data-action="edit-invoice" data-id="' + inv.id + '" data-testid="edit-btn">Edit</button>';
            html += '<button class="btn btn-primary" data-action="approve-invoice" data-id="' + inv.id + '" data-testid="approve-btn">Approve</button>';
            html += '<button class="btn btn-secondary" data-action="send-invoice" data-id="' + inv.id + '" data-testid="send-btn">Approve & Send</button>';
        } else if (inv.status === 'awaiting_payment' || inv.status === 'overdue') {
            html += '<button class="btn btn-secondary" data-action="edit-invoice" data-id="' + inv.id + '" data-testid="edit-btn">Edit</button>';
            html += '<button class="btn btn-primary" data-action="add-payment" data-id="' + inv.id + '" data-testid="add-payment-btn">Add Payment</button>';
            html += '<button class="btn btn-secondary" data-action="send-invoice" data-id="' + inv.id + '" data-testid="send-btn">Resend</button>';
            html += '<button class="btn btn-secondary" data-action="mark-sent" data-id="' + inv.id + '" data-testid="mark-sent-btn">Mark as Sent</button>';
            html += '<button class="btn btn-secondary" data-action="copy-invoice" data-id="' + inv.id + '" data-testid="copy-btn">Copy</button>';
            html += '<button class="btn btn-danger-outline" data-action="void-invoice" data-id="' + inv.id + '" data-testid="void-btn">Void</button>';
        } else if (inv.status === 'paid') {
            html += '<button class="btn btn-secondary" data-action="copy-invoice" data-id="' + inv.id + '" data-testid="copy-btn">Copy to New</button>';
        }
        html += '</div></div>';

        // Invoice Preview
        html += '<div class="invoice-preview" data-testid="invoice-preview">';
        html += '<div class="invoice-preview-header">';
        html += '<div class="invoice-preview-company">';
        html += '<h2>' + Components.escapeHtml(AppState.settings.companyName) + '</h2>';
        html += '<p>' + Components.escapeHtml(AppState.settings.companyAddress) + '</p>';
        html += '<p>' + Components.escapeHtml(AppState.settings.companyEmail) + '</p>';
        html += '<p>GST: ' + Components.escapeHtml(AppState.settings.companyTaxId) + '</p>';
        html += '</div>';
        html += '<div class="invoice-preview-title">';
        html += '<h1>INVOICE</h1>';
        html += '<table class="invoice-meta">';
        html += '<tr><td>Invoice Number:</td><td>' + Components.escapeHtml(inv.invoiceNumber) + '</td></tr>';
        if (inv.reference) html += '<tr><td>Reference:</td><td>' + Components.escapeHtml(inv.reference) + '</td></tr>';
        html += '<tr><td>Date:</td><td>' + Components.formatDate(inv.issueDate) + '</td></tr>';
        html += '<tr><td>Due Date:</td><td>' + Components.formatDate(inv.dueDate) + '</td></tr>';
        if (inv.currency !== 'NZD') html += '<tr><td>Currency:</td><td>' + Components.escapeHtml(inv.currency) + '</td></tr>';
        html += '</table></div></div>';

        // Bill To
        html += '<div class="invoice-preview-billing">';
        html += '<h3>Bill To</h3>';
        if (contact) {
            html += '<p><strong>' + Components.escapeHtml(contact.name) + '</strong></p>';
            if (contact.billingAddress) {
                const addr = contact.billingAddress;
                if (addr.street) html += '<p>' + Components.escapeHtml(addr.street) + '</p>';
                html += '<p>' + [addr.city, addr.region, addr.postalCode].filter(Boolean).map(s => Components.escapeHtml(s)).join(', ') + '</p>';
                if (addr.country) html += '<p>' + Components.escapeHtml(addr.country) + '</p>';
            }
            if (contact.email) html += '<p>' + Components.escapeHtml(contact.email) + '</p>';
            if (contact.taxId) html += '<p>Tax ID: ' + Components.escapeHtml(contact.taxId) + '</p>';
        }
        html += '</div>';

        // Line items table
        html += '<table class="data-table invoice-lines-table" data-testid="line-items-table"><thead><tr>';
        html += '<th>Description</th><th class="text-right">Qty</th><th class="text-right">Unit Price</th><th>Tax</th><th>Account</th><th class="text-right">Amount</th>';
        html += '</tr></thead><tbody>';
        inv.lineItems.forEach(li => {
            const taxRate = AppState.getTaxRateById(li.taxRateId);
            const account = AppState.getAccountByCode(li.accountCode);
            html += '<tr>';
            html += '<td>' + Components.escapeHtml(li.description) + '</td>';
            html += '<td class="text-right">' + li.quantity + '</td>';
            html += '<td class="text-right">' + Components.formatCurrency(li.unitPrice, inv.currency) + '</td>';
            html += '<td>' + (taxRate ? Components.escapeHtml(taxRate.name) : '\u2014') + '</td>';
            html += '<td>' + (account ? Components.escapeHtml(account.code + ' - ' + account.name) : Components.escapeHtml(li.accountCode)) + '</td>';
            html += '<td class="text-right">' + Components.formatCurrency(li.lineTotal, inv.currency) + '</td>';
            html += '</tr>';
        });
        html += '</tbody></table>';

        // Totals
        html += '<div class="invoice-totals">';
        html += '<div class="totals-row"><span>Subtotal</span><span>' + Components.formatCurrency(inv.subtotal, inv.currency) + '</span></div>';
        html += '<div class="totals-row"><span>Tax (GST)</span><span>' + Components.formatCurrency(inv.taxTotal, inv.currency) + '</span></div>';
        html += '<div class="totals-row totals-total"><span>Total</span><span>' + Components.formatCurrency(inv.total, inv.currency) + '</span></div>';
        if (inv.amountPaid > 0) {
            html += '<div class="totals-row"><span>Paid</span><span>-' + Components.formatCurrency(inv.amountPaid, inv.currency) + '</span></div>';
        }
        html += '<div class="totals-row totals-due"><span>Amount Due</span><span>' + Components.formatCurrency(inv.amountDue, inv.currency) + '</span></div>';
        html += '</div>';

        // Notes
        if (inv.notes) {
            html += '<div class="invoice-notes"><h3>Notes</h3><p>' + Components.escapeHtml(inv.notes) + '</p></div>';
        }

        html += '</div>'; // end invoice-preview

        // Payments
        if (payments.length > 0) {
            html += '<div class="section-card" data-testid="payments-section"><h2>Payments</h2>';
            html += '<table class="data-table"><thead><tr>';
            html += '<th>Date</th><th>Amount</th><th>Bank Account</th><th>Reference</th><th></th>';
            html += '</tr></thead><tbody>';
            payments.forEach(p => {
                const bank = AppState.getBankAccountById(p.bankAccountId);
                html += '<tr data-testid="payment-row-' + p.id + '">';
                html += '<td>' + Components.formatDate(p.date) + '</td>';
                html += '<td>' + Components.formatCurrency(p.amount, inv.currency) + '</td>';
                html += '<td>' + (bank ? Components.escapeHtml(bank.name) : '\u2014') + '</td>';
                html += '<td>' + Components.escapeHtml(p.reference || '\u2014') + '</td>';
                html += '<td><button class="btn btn-sm btn-danger-outline" data-action="delete-payment" data-id="' + p.id + '">Remove</button></td>';
                html += '</tr>';
            });
            html += '</tbody></table></div>';
        }

        // Activity timeline
        html += '<div class="section-card" data-testid="activity-section"><h2>Activity</h2>';
        html += '<div class="activity-timeline">';
        [...inv.activity].reverse().forEach(act => {
            html += '<div class="activity-item">';
            html += '<div class="activity-icon">' + Components.activityIcon(act.type) + '</div>';
            html += '<div class="activity-content">';
            html += '<span class="activity-detail">' + Components.escapeHtml(act.detail) + '</span>';
            html += '<span class="activity-date">' + Components.formatDateTime(act.date) + '</span>';
            html += '</div></div>';
        });
        html += '</div></div>';

        return html;
    },

    // ==================== Invoice Form ====================

    renderInvoiceForm(invoiceId) {
        const isEdit = !!invoiceId;
        const inv = isEdit ? AppState.getInvoiceById(invoiceId) : null;
        if (isEdit && !inv) return Components.emptyState('', 'Invoice not found', '');

        const title = isEdit ? 'Edit Invoice ' + inv.invoiceNumber : 'New Invoice';
        const contactId = inv ? inv.contactId : '';
        const invoiceNumber = inv ? inv.invoiceNumber : AppState.getNextInvoiceNumber();
        const reference = inv ? inv.reference : '';
        const issueDate = inv ? inv.issueDate : new Date().toISOString().split('T')[0];
        const dueDate = inv ? inv.dueDate : '';
        const currency = inv ? inv.currency : 'NZD';
        const notes = inv ? inv.notes : '';
        const brandingThemeId = inv ? inv.brandingThemeId : AppState.settings.defaultBrandingThemeId;
        const lineItems = inv ? inv.lineItems : [{ id: 'new_1', description: '', quantity: 1, unitPrice: 0, taxRateId: AppState.settings.defaultTaxRateId, accountCode: '200', lineTotal: 0 }];

        let html = '<div class="page-header"><div class="page-header-left">';
        html += '<button class="btn btn-ghost" data-route="invoices">&larr; Back</button>';
        html += '<h1>' + Components.escapeHtml(title) + '</h1></div>';
        html += '<div class="page-actions">';
        html += '<button class="btn btn-secondary" data-action="save-invoice-draft" data-testid="save-draft-btn">Save as Draft</button>';
        html += '<button class="btn btn-primary" data-action="save-invoice-approve" data-testid="save-approve-btn">Approve</button>';
        html += '</div></div>';

        html += '<div class="invoice-form" data-testid="invoice-form">';

        // Contact selection
        const contactOpts = AppState.contacts.map(c => ({ value: c.id, label: c.name })).sort((a, b) => a.label.localeCompare(b.label));
        html += '<div class="form-row">';
        html += '<div class="form-col-2">';
        html += '<label class="form-label">To <span class="required">*</span></label>';
        html += Components.searchableDropdown('invoice-contact', contactOpts, contactId, 'Search contacts...');
        html += '<button class="btn btn-sm btn-link" data-action="quick-add-contact" data-testid="quick-add-contact-btn">+ Add new contact</button>';
        html += '</div>';
        html += '<div class="form-col">';
        html += Components.textInput('invoice-number', invoiceNumber, 'INV-0001', 'Invoice Number');
        html += '</div>';
        html += '<div class="form-col">';
        html += Components.textInput('invoice-reference', reference, 'e.g. PO-12345', 'Reference');
        html += '</div>';
        html += '</div>';

        // Dates and currency
        html += '<div class="form-row">';
        html += '<div class="form-col"><div class="form-group"><label class="form-label">Invoice Date <span class="required">*</span></label><input type="text" class="form-input" id="invoice-date" value="' + Components.escapeAttr(issueDate) + '" placeholder="YYYY-MM-DD" data-testid="input-invoice-date"></div></div>';
        html += '<div class="form-col"><div class="form-group"><label class="form-label">Due Date <span class="required">*</span></label><input type="text" class="form-input" id="invoice-due-date" value="' + Components.escapeAttr(dueDate) + '" placeholder="YYYY-MM-DD" data-testid="input-invoice-due-date"></div></div>';

        const currOpts = AppState.currencies.map(c => ({ value: c.code, label: c.code + ' - ' + c.name }));
        html += '<div class="form-col"><label class="form-label">Currency</label>';
        html += Components.dropdown('invoice-currency', currOpts, currency, 'Select currency');
        html += '</div>';

        const themeOpts = AppState.brandingThemes.map(t => ({ value: t.id, label: t.name }));
        html += '<div class="form-col"><label class="form-label">Branding Theme</label>';
        html += Components.dropdown('invoice-theme', themeOpts, brandingThemeId, 'Select theme');
        html += '</div>';
        html += '</div>';

        // Line items
        html += '<div class="line-items-section" data-testid="line-items-section">';
        html += '<h3>Line Items</h3>';
        html += '<table class="data-table line-items-edit-table" id="lineItemsTable"><thead><tr>';
        html += '<th>Description</th><th class="col-qty">Qty</th><th class="col-price">Unit Price</th><th class="col-tax">Tax Rate</th><th class="col-account">Account</th><th class="col-total">Amount</th><th class="col-action"></th>';
        html += '</tr></thead><tbody id="lineItemsBody">';

        const taxOpts = AppState.taxRates.map(t => ({ value: t.id, label: t.name }));
        const accOpts = AppState.accountCodes.filter(a => a.type === 'Revenue').map(a => ({ value: a.code, label: a.code + ' - ' + a.name }));

        lineItems.forEach((li, idx) => {
            html += this._renderLineItemRow(li, idx, taxOpts, accOpts);
        });

        html += '</tbody></table>';
        html += '<button class="btn btn-sm btn-secondary" data-action="add-line-item" data-testid="add-line-item-btn">+ Add Line Item</button>';
        html += '</div>';

        // Totals summary
        let subtotal = 0;
        let taxTotal = 0;
        lineItems.forEach(li => {
            subtotal += li.lineTotal || 0;
            const rate = AppState.getTaxRateById(li.taxRateId);
            if (rate) taxTotal += (li.lineTotal || 0) * (rate.rate / 100);
        });
        subtotal = Math.round(subtotal * 100) / 100;
        taxTotal = Math.round(taxTotal * 100) / 100;
        const total = Math.round((subtotal + taxTotal) * 100) / 100;

        html += '<div class="invoice-form-totals" id="invoiceFormTotals">';
        html += '<div class="totals-row"><span>Subtotal</span><span id="form-subtotal">' + Components.formatCurrency(subtotal, currency) + '</span></div>';
        html += '<div class="totals-row"><span>Tax (GST)</span><span id="form-tax">' + Components.formatCurrency(taxTotal, currency) + '</span></div>';
        html += '<div class="totals-row totals-total"><span>Total</span><span id="form-total">' + Components.formatCurrency(total, currency) + '</span></div>';
        html += '</div>';

        // Notes
        html += Components.textarea('invoice-notes', notes, 'Add any notes or payment terms...', 'Notes / Memo');

        html += '</div>'; // end invoice-form

        return html;
    },

    _renderLineItemRow(li, idx, taxOpts, accOpts) {
        let html = '<tr class="line-item-row" data-line-idx="' + idx + '" data-testid="line-item-' + idx + '">';
        html += '<td><input type="text" class="form-input" data-line-field="description" value="' + Components.escapeAttr(li.description) + '" placeholder="Enter description"></td>';
        html += '<td class="col-qty"><input type="number" class="form-input" data-line-field="quantity" value="' + (li.quantity || '') + '" step="any" min="0"></td>';
        html += '<td class="col-price"><input type="number" class="form-input" data-line-field="unitPrice" value="' + (li.unitPrice || '') + '" step="0.01" min="0"></td>';
        html += '<td class="col-tax">' + this._inlineDropdown('line-tax-' + idx, taxOpts, li.taxRateId, 'Tax') + '</td>';
        html += '<td class="col-account">' + this._inlineDropdown('line-acc-' + idx, accOpts, li.accountCode, 'Account') + '</td>';
        html += '<td class="col-total text-right"><span class="line-total">' + Components.formatCurrency(li.lineTotal || 0) + '</span></td>';
        html += '<td class="col-action"><button class="btn btn-sm btn-danger-outline" data-action="remove-line-item" data-idx="' + idx + '">&times;</button></td>';
        html += '</tr>';
        return html;
    },

    _inlineDropdown(id, options, selectedValue, placeholder) {
        const selected = options.find(o => String(o.value) === String(selectedValue));
        const displayText = selected ? selected.label : (placeholder || 'Select...');
        let html = '<div class="custom-dropdown inline-dropdown" id="' + Components.escapeAttr(id) + '" data-dropdown="' + Components.escapeAttr(id) + '">';
        html += '<div class="dropdown-trigger" data-dropdown-trigger="' + Components.escapeAttr(id) + '"><span class="dropdown-text">' + Components.escapeHtml(displayText) + '</span></div>';
        html += '<div class="dropdown-menu" id="' + Components.escapeAttr(id) + '-menu" style="display:none">';
        options.forEach(opt => {
            html += '<div class="dropdown-item' + (String(opt.value) === String(selectedValue) ? ' selected' : '') + '" data-dropdown-item="' + Components.escapeAttr(id) + '" data-value="' + Components.escapeAttr(opt.value) + '">' + Components.escapeHtml(opt.label) + '</div>';
        });
        html += '</div></div>';
        return html;
    },

    // ==================== Contacts ====================

    renderContacts() {
        const paged = AppState.getPagedContacts();

        let html = '<div class="page-header"><h1>Contacts</h1>';
        html += '<div class="page-actions"><button class="btn btn-primary" data-action="new-contact" data-testid="new-contact-btn">+ New Contact</button></div></div>';

        // Search
        html += '<div class="filters-bar">';
        html += '<div class="form-group form-group-inline search-group"><input type="text" class="form-input form-input-sm" id="contact-search" placeholder="Search contacts..." value="' + Components.escapeAttr(AppState.contactFilters.search) + '" data-testid="contact-search"><svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>';
        html += '</div>';

        if (paged.items.length === 0) {
            html += Components.emptyState('', 'No contacts found', 'Try adjusting your search or add a new contact.');
            return html;
        }

        html += '<div class="table-wrapper"><table class="data-table" data-testid="contacts-table"><thead><tr>';
        html += '<th>Name</th><th>Email</th><th>Phone</th><th>City</th><th class="text-right">Outstanding</th>';
        html += '</tr></thead><tbody>';

        paged.items.forEach(c => {
            const outstanding = AppState.getContactOutstandingBalance(c.id);
            html += '<tr class="clickable-row" data-route="contacts/' + c.id + '" data-testid="contact-row-' + c.id + '">';
            html += '<td><div class="contact-name-cell">' + Components.contactAvatar(c) + ' <span>' + Components.escapeHtml(c.name) + '</span></div></td>';
            html += '<td>' + Components.escapeHtml(c.email) + '</td>';
            html += '<td>' + Components.escapeHtml(c.phone || '\u2014') + '</td>';
            html += '<td>' + Components.escapeHtml(c.billingAddress ? c.billingAddress.city : '\u2014') + '</td>';
            html += '<td class="text-right">' + (outstanding > 0 ? '<span class="text-danger">' + Components.formatCurrency(outstanding) + '</span>' : Components.formatCurrency(0)) + '</td>';
            html += '</tr>';
        });

        html += '</tbody></table></div>';
        html += Components.pagination(paged.page, paged.total, paged.pageSize);

        return html;
    },

    // ==================== Contact Detail ====================

    renderContactDetail(contactId) {
        const contact = AppState.getContactById(contactId);
        if (!contact) return Components.emptyState('', 'Contact not found', '');

        const invoices = AppState.invoices.filter(inv => inv.contactId === contactId);
        const outstanding = AppState.getContactOutstandingBalance(contactId);

        let html = '<div class="page-header"><div class="page-header-left">';
        html += '<button class="btn btn-ghost" data-route="contacts">&larr; Back to Contacts</button>';
        html += '<h1>' + Components.escapeHtml(contact.name) + '</h1></div>';
        html += '<div class="page-actions">';
        html += '<button class="btn btn-secondary" data-action="edit-contact" data-id="' + contact.id + '" data-testid="edit-contact-btn">Edit</button>';
        if (invoices.length === 0) {
            html += '<button class="btn btn-danger-outline" data-action="delete-contact" data-id="' + contact.id + '" data-testid="delete-contact-btn">Delete</button>';
        }
        html += '</div></div>';

        // Contact details
        html += '<div class="detail-grid">';
        html += '<div class="section-card"><h2>Contact Details</h2>';
        html += '<div class="detail-row"><span class="detail-label">Email</span><span>' + Components.escapeHtml(contact.email) + '</span></div>';
        html += '<div class="detail-row"><span class="detail-label">Phone</span><span>' + Components.escapeHtml(contact.phone || '\u2014') + '</span></div>';
        html += '<div class="detail-row"><span class="detail-label">Tax ID</span><span>' + Components.escapeHtml(contact.taxId || '\u2014') + '</span></div>';
        html += '<div class="detail-row"><span class="detail-label">Type</span><span>' + Components.escapeHtml(contact.contactType) + '</span></div>';
        html += '<div class="detail-row"><span class="detail-label">Created</span><span>' + Components.formatDate(contact.createdAt) + '</span></div>';
        html += '</div>';

        html += '<div class="section-card"><h2>Billing Address</h2>';
        if (contact.billingAddress) {
            const addr = contact.billingAddress;
            if (addr.street) html += '<p>' + Components.escapeHtml(addr.street) + '</p>';
            html += '<p>' + [addr.city, addr.region, addr.postalCode].filter(Boolean).map(s => Components.escapeHtml(s)).join(', ') + '</p>';
            if (addr.country) html += '<p>' + Components.escapeHtml(addr.country) + '</p>';
        } else {
            html += '<p class="text-muted">No address on file</p>';
        }
        html += '</div></div>';

        // Outstanding balance
        html += '<div class="section-card"><h2>Financial Summary</h2>';
        html += '<div class="stat-row"><span>Outstanding Balance</span><span class="' + (outstanding > 0 ? 'text-danger' : '') + '">' + Components.formatCurrency(outstanding) + '</span></div>';
        html += '<div class="stat-row"><span>Total Invoices</span><span>' + invoices.length + '</span></div>';
        html += '</div>';

        // Invoice history
        html += '<div class="section-card"><h2>Invoices</h2>';
        if (invoices.length === 0) {
            html += '<p class="text-muted">No invoices for this contact.</p>';
        } else {
            html += '<table class="data-table"><thead><tr>';
            html += '<th>Number</th><th>Date</th><th>Due Date</th><th class="text-right">Total</th><th class="text-right">Due</th><th>Status</th>';
            html += '</tr></thead><tbody>';
            invoices.sort((a, b) => b.issueDate.localeCompare(a.issueDate)).forEach(inv => {
                html += '<tr class="clickable-row" data-route="invoices/' + inv.id + '">';
                html += '<td>' + Components.escapeHtml(inv.invoiceNumber) + '</td>';
                html += '<td>' + Components.formatDate(inv.issueDate) + '</td>';
                html += '<td>' + Components.formatDate(inv.dueDate) + '</td>';
                html += '<td class="text-right">' + Components.formatCurrency(inv.total, inv.currency) + '</td>';
                html += '<td class="text-right">' + Components.formatCurrency(inv.amountDue, inv.currency) + '</td>';
                html += '<td>' + Components.statusBadge(inv.status) + '</td>';
                html += '</tr>';
            });
            html += '</tbody></table>';
        }
        html += '</div>';

        return html;
    },

    // ==================== Settings ====================

    renderSettings() {
        const s = AppState.settings;

        let html = '<div class="page-header"><h1>Invoice Settings</h1></div>';

        // Due date terms
        html += '<div class="section-card" data-testid="due-date-settings"><h2>Default Due Date</h2>';
        const termOpts = [
            { value: '7', label: '7 days after invoice date' },
            { value: '14', label: '14 days after invoice date' },
            { value: '20', label: '20 days after invoice date' },
            { value: '30', label: '30 days after invoice date' },
            { value: '60', label: '60 days after invoice date' },
            { value: 'eom', label: 'End of month' },
            { value: 'eom_plus_7', label: 'End of month + 7 days' },
            { value: 'eom_plus_14', label: 'End of month + 14 days' },
            { value: 'eom_plus_30', label: 'End of month + 30 days' },
        ];
        html += '<label class="form-label">Due Date Terms</label>';
        html += Components.dropdown('settings-due-terms', termOpts, s.defaultDueDateTerms, 'Select terms');
        html += '</div>';

        // Tax settings
        html += '<div class="section-card" data-testid="tax-settings"><h2>Default Tax Rate</h2>';
        const taxOpts = AppState.taxRates.map(t => ({ value: t.id, label: t.name }));
        html += '<label class="form-label">Default Tax Rate for New Invoices</label>';
        html += Components.dropdown('settings-tax-rate', taxOpts, s.defaultTaxRateId, 'Select tax rate');
        html += '</div>';

        // Invoice number sequence
        html += '<div class="section-card" data-testid="number-settings"><h2>Invoice Number Sequence</h2>';
        html += '<div class="form-row">';
        html += '<div class="form-col">' + Components.textInput('settings-inv-prefix', s.invoiceNumberPrefix, 'INV-', 'Prefix') + '</div>';
        html += '<div class="form-col">' + Components.numberInput('settings-inv-next', s.invoiceNumberNextNumber, 'Next Number', 1) + '</div>';
        html += '<div class="form-col">' + Components.numberInput('settings-inv-padding', s.invoiceNumberPadding, 'Zero Padding', 1, 8) + '</div>';
        html += '</div>';
        html += '<p class="text-muted">Preview: ' + Components.escapeHtml(s.invoiceNumberPrefix + String(s.invoiceNumberNextNumber).padStart(s.invoiceNumberPadding, '0')) + '</p>';
        html += '</div>';

        // Branding theme
        html += '<div class="section-card" data-testid="branding-settings"><h2>Default Branding Theme</h2>';
        const themeOpts = AppState.brandingThemes.map(t => ({ value: t.id, label: t.name }));
        html += '<label class="form-label">Default Theme for New Invoices</label>';
        html += Components.dropdown('settings-branding-theme', themeOpts, s.defaultBrandingThemeId, 'Select theme');
        html += '</div>';

        // Email template
        html += '<div class="section-card" data-testid="email-settings"><h2>Default Email Template</h2>';
        html += Components.textInput('settings-email-subject', s.defaultEmailSubject, 'Email subject', 'Subject');
        html += Components.textarea('settings-email-body', s.defaultEmailBody, 'Email body', 'Body', 6);
        html += '<p class="text-muted">Available placeholders: {ContactName}, {InvoiceNumber}, {Total}, {DueDate}</p>';
        html += '</div>';

        // Late payment penalty
        html += '<div class="section-card" data-testid="penalty-settings"><h2>Late Payment Penalty</h2>';
        html += '<div class="toggle-row" data-testid="toggle-penalty">';
        html += '<label class="toggle-switch"><input type="checkbox" id="settings-penalty-enabled" data-toggle="settings-penalty-enabled"' + (s.latePenaltyEnabled ? ' checked' : '') + '><span class="toggle-slider"></span></label>';
        html += '<div class="toggle-label-wrap"><span class="toggle-label">Enable Late Payment Penalty</span></div></div>';

        html += '<div id="penalty-details" style="' + (s.latePenaltyEnabled ? '' : 'display:none') + '">';
        html += '<div class="form-row">';
        html += '<div class="form-col">' + Components.numberInput('settings-penalty-rate', s.latePenaltyRate, 'Penalty Rate (%)', 0, 100, 0.1) + '</div>';
        const freqOpts = [{ value: 'monthly', label: 'Monthly' }, { value: 'weekly', label: 'Weekly' }, { value: 'daily', label: 'Daily' }];
        html += '<div class="form-col"><label class="form-label">Frequency</label>' + Components.dropdown('settings-penalty-freq', freqOpts, s.latePenaltyFrequency, 'Frequency') + '</div>';
        html += '</div></div>';
        html += '</div>';

        // Company details
        html += '<div class="section-card" data-testid="company-settings"><h2>Company Details</h2>';
        html += Components.textInput('settings-company-name', s.companyName, 'Company name', 'Company Name');
        html += Components.textInput('settings-company-email', s.companyEmail, 'Email', 'Email');
        html += Components.textInput('settings-company-phone', s.companyPhone, 'Phone', 'Phone');
        html += Components.textInput('settings-company-address', s.companyAddress, 'Address', 'Address');
        html += Components.textInput('settings-company-taxid', s.companyTaxId, 'Tax ID', 'Tax ID / GST Number');
        html += '</div>';

        // Save button
        html += '<div class="form-actions"><button class="btn btn-primary" data-action="save-settings" data-testid="save-settings-btn">Save Settings</button></div>';

        return html;
    },

    // ==================== Modal Views ====================

    renderPaymentModal(invoiceId) {
        const inv = AppState.getInvoiceById(invoiceId);
        if (!inv) return '';

        const bankOpts = AppState.bankAccounts.map(b => ({ value: b.id, label: b.name }));
        const today = new Date().toISOString().split('T')[0];

        let html = '<div class="payment-form" data-testid="payment-form">';
        html += '<div class="form-group"><label class="form-label">Amount <span class="required">*</span></label>';
        html += '<input type="number" class="form-input" id="payment-amount" value="' + inv.amountDue.toFixed(2) + '" step="0.01" min="0.01" max="' + inv.amountDue.toFixed(2) + '" data-testid="input-payment-amount"></div>';
        html += '<div class="form-group"><label class="form-label">Date <span class="required">*</span></label>';
        html += '<input type="text" class="form-input" id="payment-date" value="' + today + '" placeholder="YYYY-MM-DD" data-testid="input-payment-date"></div>';
        html += '<label class="form-label">Bank Account</label>';
        html += Components.dropdown('payment-bank', bankOpts, 'bank_1', 'Select account');
        html += Components.textInput('payment-reference', '', 'e.g. CHQ-12345', 'Reference');
        html += Components.textInput('payment-note', '', 'Optional note', 'Note');

        if (inv.currency !== 'NZD') {
            html += Components.numberInput('payment-exchange-rate', inv.currency === 'AUD' ? 1.08 : 1.58, 'Exchange Rate', 0.0001, null, 0.0001);
        }

        html += '<p class="text-muted">Amount due: ' + Components.formatCurrency(inv.amountDue, inv.currency) + '</p>';
        html += '</div>';

        return html;
    },

    renderContactModal(contactId) {
        const isEdit = !!contactId;
        const contact = isEdit ? AppState.getContactById(contactId) : null;

        let html = '<div class="contact-form" data-testid="contact-form">';
        html += Components.textInput('contact-name', contact ? contact.name : '', 'Business or person name', 'Name *', true);
        html += Components.textInput('contact-email', contact ? contact.email : '', 'email@example.com', 'Email *', true);
        html += Components.textInput('contact-phone', contact ? contact.phone : '', '+64 9 555 0100', 'Phone');

        html += '<h3>Billing Address</h3>';
        const addr = contact ? contact.billingAddress : {};
        html += Components.textInput('contact-street', addr.street || '', 'Street address', 'Street');
        html += '<div class="form-row">';
        html += '<div class="form-col">' + Components.textInput('contact-city', addr.city || '', 'City', 'City') + '</div>';
        html += '<div class="form-col">' + Components.textInput('contact-region', addr.region || '', 'Region / State', 'Region') + '</div>';
        html += '</div>';
        html += '<div class="form-row">';
        html += '<div class="form-col">' + Components.textInput('contact-postal', addr.postalCode || '', 'Postal code', 'Postal Code') + '</div>';
        html += '<div class="form-col">' + Components.textInput('contact-country', addr.country || 'New Zealand', 'Country', 'Country') + '</div>';
        html += '</div>';

        html += Components.textInput('contact-taxid', contact ? contact.taxId : '', 'e.g. NZ-12-345-678', 'Tax ID');
        html += '</div>';

        return html;
    },
};

const Views = {

  renderSidebar() {
    const stats = AppState.getDashboardStats();
    let html = '<div class="sidebar-header">';
    html += '<div class="sidebar-logo">Xero</div>';
    html += '<div class="sidebar-org">' + Components.escapeHtml(AppState.currentUser.organization.name) + '</div>';
    html += '</div>';
    html += '<nav class="sidebar-nav">';
    html += this._navItem('dashboard', 'Dashboard', '&#9634;', '');
    html += '<div class="nav-section-title">Sales</div>';
    html += this._navItem('invoices', 'Invoices', '&#128196;', stats.awaitingPaymentCount > 0 ? stats.awaitingPaymentCount : '');
    html += this._navItem('quotes', 'Quotes', '&#128203;', '');
    html += this._navItem('credit-notes', 'Credit Notes', '&#128179;', '');
    html += this._navItem('repeating-invoices', 'Repeating Invoices', '&#128260;', '');
    html += '<div class="nav-section-title">Settings</div>';
    html += this._navItem('settings', 'Invoice Settings', '&#9881;', '');
    html += this._navItem('templates', 'Branding Themes', '&#127912;', '');
    html += this._navItem('reminders', 'Invoice Reminders', '&#128276;', '');
    html += '</nav>';
    return html;
  },

  _navItem(view, label, icon, badge) {
    const active = AppState.currentView === view ? ' active' : '';
    const badgeHtml = badge ? '<span class="nav-badge">' + badge + '</span>' : '';
    return '<a class="nav-item' + active + '" data-route="' + view + '"><span class="nav-icon">' + icon + '</span><span class="nav-label">' + Components.escapeHtml(label) + '</span>' + badgeHtml + '</a>';
  },

  // ---- Dashboard ----
  renderDashboard() {
    const stats = AppState.getDashboardStats();
    let html = '<div class="page-header"><h1>Sales Overview</h1>';
    html += '<div class="header-actions">';
    html += Components.button('New Invoice', 'new-invoice', 'primary');
    html += Components.button('New Quote', 'new-quote', 'secondary');
    html += '</div></div>';

    html += '<div class="dashboard-cards">';
    html += this._dashCard('Draft', stats.draftCount, stats.draftTotal, 'draft', 'invoices');
    html += this._dashCard('Awaiting Approval', stats.awaitingApprovalCount, stats.awaitingApprovalTotal, 'awaiting', 'invoices');
    html += this._dashCard('Awaiting Payment', stats.awaitingPaymentCount, stats.awaitingPaymentTotal, 'payment', 'invoices');
    html += this._dashCard('Overdue', stats.overdueCount, stats.overdueTotal, 'overdue', 'invoices');
    html += '</div>';

    html += '<div class="dashboard-summary">';
    html += '<div class="summary-card"><div class="summary-label">Total Outstanding</div><div class="summary-value">' + Components.formatCurrency(stats.totalOutstanding) + '</div></div>';
    html += '<div class="summary-card overdue"><div class="summary-label">Total Overdue</div><div class="summary-value">' + Components.formatCurrency(stats.totalOverdue) + '</div></div>';
    html += '</div>';

    // Recent invoices
    html += '<div class="section-header"><h2>Recent Invoices</h2></div>';
    const recent = AppState.invoices.filter(i => i.status !== 'deleted' && i.status !== 'voided').sort((a, b) => b.date.localeCompare(a.date)).slice(0, 8);
    if (recent.length) {
      html += this._invoiceTable(recent, false);
    } else {
      html += Components.emptyState('&#128196;', 'No invoices yet', 'Create your first invoice to get started.', 'New Invoice', 'new-invoice');
    }
    return html;
  },

  _dashCard(label, count, total, type, route) {
    return '<div class="dash-card dash-card-' + type + '" data-route="' + route + '" data-tab="' + (type === 'payment' ? 'awaiting_payment' : type === 'overdue' ? 'overdue' : type) + '">' +
      '<div class="dash-card-label">' + label + '</div>' +
      '<div class="dash-card-count">' + count + '</div>' +
      '<div class="dash-card-total">' + Components.formatCurrency(total) + '</div></div>';
  },

  // ---- Invoice List ----
  renderInvoiceList() {
    const tab = AppState.currentTab || 'all';
    const statuses = [
      { id: 'all', label: 'All' },
      { id: 'draft', label: 'Draft' },
      { id: 'awaiting_approval', label: 'Awaiting Approval' },
      { id: 'awaiting_payment', label: 'Awaiting Payment' },
      { id: 'overdue', label: 'Overdue' },
      { id: 'paid', label: 'Paid' }
    ];
    statuses.forEach(s => {
      s.count = AppState.getInvoicesByStatus(s.id).length;
    });

    let html = '<div class="page-header"><h1>Invoices</h1>';
    html += '<div class="header-actions">' + Components.button('New Invoice', 'new-invoice', 'primary') + '</div></div>';
    html += Components.tabs(statuses, tab);

    const invoices = AppState.getInvoicesByStatus(tab);
    const sorted = invoices.sort((a, b) => b.date.localeCompare(a.date));

    if (sorted.length === 0) {
      html += Components.emptyState('&#128196;', 'No invoices', 'No invoices match this filter.');
    } else {
      html += this._invoiceTable(sorted, true);
    }
    return html;
  },

  _invoiceTable(invoices, showCheckbox) {
    let html = '<div class="table-container"><table class="data-table" data-testid="invoice-table">';
    html += '<thead><tr>';
    if (showCheckbox) html += '<th class="col-check"><input type="checkbox" data-action="select-all" /></th>';
    html += '<th>Number</th><th>Reference</th><th>To</th><th>Date</th><th>Due Date</th><th class="text-right">Total</th><th class="text-right">Due</th><th>Status</th></tr></thead><tbody>';
    invoices.forEach(inv => {
      const contact = AppState.getContactById(inv.contactId);
      const selected = AppState.selectedIds.has(inv.id) ? ' selected' : '';
      html += '<tr class="table-row clickable' + selected + '" data-id="' + inv.id + '">';
      if (showCheckbox) html += '<td class="col-check"><input type="checkbox" class="row-checkbox" data-check-id="' + inv.id + '" ' + (AppState.selectedIds.has(inv.id) ? 'checked' : '') + ' /></td>';
      html += '<td><a class="link" data-action="view-invoice" data-id="' + inv.id + '">' + Components.escapeHtml(inv.number) + '</a></td>';
      html += '<td>' + Components.escapeHtml(inv.reference) + '</td>';
      html += '<td>' + Components.escapeHtml(contact ? contact.name : '') + '</td>';
      html += '<td>' + Components.formatDate(inv.date) + '</td>';
      html += '<td>' + Components.formatDate(inv.dueDate) + '</td>';
      html += '<td class="text-right">' + Components.formatCurrency(inv.total, inv.currency) + '</td>';
      html += '<td class="text-right">' + Components.formatCurrency(inv.amountDue, inv.currency) + '</td>';
      html += '<td>' + Components.statusBadge(inv.status) + '</td>';
      html += '</tr>';
    });
    html += '</tbody></table></div>';
    return html;
  },

  // ---- Invoice Detail ----
  renderInvoiceDetail(inv) {
    if (!inv) return '<div class="error">Invoice not found.</div>';
    const contact = AppState.getContactById(inv.contactId);
    const theme = AppState.getBrandingThemeById(inv.brandingThemeId);

    let html = '<div class="page-header">';
    html += '<div class="header-left"><button class="btn btn-back" data-action="back-to-invoices">&larr; Back</button>';
    html += '<h1>' + Components.escapeHtml(inv.number) + '</h1>' + Components.statusBadge(inv.status) + '</div>';
    html += '<div class="header-actions">';
    if (inv.status === 'draft') {
      html += Components.button('Edit', 'edit-invoice', 'secondary', ' data-id="' + inv.id + '"');
      html += Components.button('Submit for Approval', 'submit-for-approval', 'secondary', ' data-id="' + inv.id + '"');
      html += Components.button('Approve', 'approve-invoice', 'primary', ' data-id="' + inv.id + '"');
      html += Components.button('Delete', 'delete-invoice', 'danger', ' data-id="' + inv.id + '"');
    } else if (inv.status === 'awaiting_approval') {
      html += Components.button('Edit', 'edit-invoice', 'secondary', ' data-id="' + inv.id + '"');
      html += Components.button('Approve', 'approve-invoice', 'primary', ' data-id="' + inv.id + '"');
    } else if (inv.status === 'awaiting_payment') {
      html += Components.button('Add Payment', 'show-add-payment', 'primary', ' data-id="' + inv.id + '"');
      html += Components.button('Send', 'send-invoice', 'secondary', ' data-id="' + inv.id + '"');
      html += Components.button('Void', 'void-invoice', 'danger', ' data-id="' + inv.id + '"');
    }
    if (inv.status !== 'voided' && inv.status !== 'deleted') {
      html += Components.button('Copy', 'copy-invoice', 'secondary', ' data-id="' + inv.id + '"');
      html += Components.button('Credit Note', 'create-cn-from-invoice', 'secondary', ' data-id="' + inv.id + '"');
    }
    html += '</div></div>';

    // Invoice card
    html += '<div class="detail-card">';
    html += '<div class="detail-grid">';
    html += '<div class="detail-field"><label>To</label><div>' + Components.escapeHtml(contact ? contact.name : '') + '</div></div>';
    html += '<div class="detail-field"><label>Date</label><div>' + Components.formatDate(inv.date) + '</div></div>';
    html += '<div class="detail-field"><label>Due Date</label><div>' + Components.formatDate(inv.dueDate) + '</div></div>';
    html += '<div class="detail-field"><label>Invoice Number</label><div>' + Components.escapeHtml(inv.number) + '</div></div>';
    if (inv.reference) html += '<div class="detail-field"><label>Reference</label><div>' + Components.escapeHtml(inv.reference) + '</div></div>';
    html += '<div class="detail-field"><label>Currency</label><div>' + Components.escapeHtml(inv.currency) + '</div></div>';
    html += '<div class="detail-field"><label>Branding Theme</label><div>' + Components.escapeHtml(theme ? theme.name : '') + '</div></div>';
    html += '<div class="detail-field"><label>Tax</label><div>' + (inv.taxMode === 'inclusive' ? 'Tax Inclusive' : inv.taxMode === 'exclusive' ? 'Tax Exclusive' : 'No Tax') + '</div></div>';
    if (inv.title) html += '<div class="detail-field full-width"><label>Title</label><div>' + Components.escapeHtml(inv.title) + '</div></div>';
    if (inv.summary) html += '<div class="detail-field full-width"><label>Summary</label><div>' + Components.escapeHtml(inv.summary) + '</div></div>';
    html += '</div>';

    // Line items table
    html += '<h3>Line Items</h3>';
    html += this._lineItemsTable(inv.lineItems, inv.taxMode, inv.currency);

    // Totals
    html += '<div class="totals-section">';
    html += '<div class="total-row"><span>Subtotal</span><span>' + Components.formatCurrency(inv.subtotal, inv.currency) + '</span></div>';
    html += '<div class="total-row"><span>Tax</span><span>' + Components.formatCurrency(inv.taxTotal, inv.currency) + '</span></div>';
    html += '<div class="total-row total-main"><span>Total</span><span>' + Components.formatCurrency(inv.total, inv.currency) + '</span></div>';
    if (inv.amountPaid > 0) {
      html += '<div class="total-row"><span>Paid</span><span>-' + Components.formatCurrency(inv.amountPaid, inv.currency) + '</span></div>';
    }
    html += '<div class="total-row total-due"><span>Amount Due</span><span>' + Components.formatCurrency(inv.amountDue, inv.currency) + '</span></div>';
    html += '</div>';

    // Payments
    if (inv.payments.length > 0) {
      html += '<h3>Payments</h3>';
      html += '<table class="data-table compact"><thead><tr><th>Date</th><th>Reference</th><th class="text-right">Amount</th><th></th></tr></thead><tbody>';
      inv.payments.forEach(p => {
        html += '<tr><td>' + Components.formatDate(p.date) + '</td><td>' + Components.escapeHtml(p.reference) + '</td><td class="text-right">' + Components.formatCurrency(p.amount, inv.currency) + '</td>';
        html += '<td><button class="btn btn-sm btn-danger" data-action="remove-payment" data-invoice-id="' + inv.id + '" data-payment-id="' + p.id + '">Remove</button></td></tr>';
      });
      html += '</tbody></table>';
    }

    // History
    if (inv.notes.length > 0) {
      html += '<h3>History &amp; Notes</h3>';
      html += '<div class="history-list">';
      inv.notes.slice().reverse().forEach(n => {
        html += '<div class="history-item"><span class="history-date">' + Components.formatDateTime(n.date) + '</span> <span class="history-user">' + Components.escapeHtml(n.user) + '</span>: <span class="history-text">' + Components.escapeHtml(n.text) + '</span></div>';
      });
      html += '</div>';
    }

    html += '</div>';
    return html;
  },

  _lineItemsTable(lineItems, taxMode, currency) {
    let html = '<table class="data-table line-items-table"><thead><tr>';
    html += '<th>Item</th><th>Description</th><th class="text-right">Qty</th><th class="text-right">Unit Price</th><th class="text-right">Disc %</th><th>Account</th><th>Tax Rate</th><th class="text-right">Amount</th>';
    html += '</tr></thead><tbody>';
    lineItems.forEach(li => {
      const item = li.itemId ? AppState.getItemById(li.itemId) : null;
      const account = AppState.getAccountById(li.accountId);
      const tax = AppState.getTaxRateById(li.taxRateId);
      const lineAmt = li.quantity * li.unitPrice * (1 - (li.discountPercent || 0) / 100);
      html += '<tr>';
      html += '<td>' + Components.escapeHtml(item ? item.code : '') + '</td>';
      html += '<td>' + Components.escapeHtml(li.description) + '</td>';
      html += '<td class="text-right">' + li.quantity + '</td>';
      html += '<td class="text-right">' + Components.formatCurrency(li.unitPrice, currency) + '</td>';
      html += '<td class="text-right">' + (li.discountPercent || 0) + '%</td>';
      html += '<td>' + Components.escapeHtml(account ? account.code + ' - ' + account.name : '') + '</td>';
      html += '<td>' + Components.escapeHtml(tax ? tax.name : '') + '</td>';
      html += '<td class="text-right">' + Components.formatCurrency(lineAmt, currency) + '</td>';
      html += '</tr>';
    });
    html += '</tbody></table>';
    return html;
  },

  // ---- Invoice Form (Create/Edit) ----
  renderInvoiceForm(inv) {
    const isEdit = !!inv;
    const title = isEdit ? 'Edit Invoice ' + inv.number : 'New Invoice';
    const contactId = isEdit ? inv.contactId : '';
    const date = isEdit ? inv.date : Components.todayStr();
    const dueDate = isEdit ? inv.dueDate : AppState._calcDueDate(Components.todayStr());
    const reference = isEdit ? inv.reference : '';
    const currency = isEdit ? inv.currency : 'AUD';
    const themeId = isEdit ? inv.brandingThemeId : 'theme_standard';
    const taxMode = isEdit ? inv.taxMode : AppState.invoiceSettings.defaultTaxMode;
    const invTitle = isEdit ? (inv.title || '') : '';
    const invSummary = isEdit ? (inv.summary || '') : '';
    const lineItems = isEdit ? inv.lineItems : [{ id: AppState.generateLineItemId(), itemId: '', description: '', quantity: 1, unitPrice: 0, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }];

    let html = '<div class="page-header"><h1>' + Components.escapeHtml(title) + '</h1></div>';
    html += '<div class="form-card">';

    // Contact
    const contactOpts = AppState.contacts.filter(c => c.isCustomer).map(c => ({ value: c.id, label: c.name }));
    html += '<div class="form-row">';
    html += '<div class="form-group"><label>To <span class="required">*</span></label>' + Components.searchableDropdown('inv-contact', contactOpts, contactId, 'Search contacts...') + '</div>';
    html += '</div>';

    html += '<div class="form-row form-row-4">';
    html += '<div class="form-group"><label>Date</label>' + Components.dateInput('inv-date', date) + '</div>';
    html += '<div class="form-group"><label>Due Date</label>' + Components.dateInput('inv-due-date', dueDate) + '</div>';
    html += '<div class="form-group"><label>Reference</label>' + Components.textInput('inv-reference', reference) + '</div>';
    html += '<div class="form-group"><label>Currency</label>' + Components.dropdown('inv-currency', AppState.currencies.map(c => ({ value: c.code, label: c.code + ' - ' + c.name })), currency, 'Select currency') + '</div>';
    html += '</div>';

    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Branding Theme</label>' + Components.dropdown('inv-theme', AppState.brandingThemes.map(t => ({ value: t.id, label: t.name })), themeId, 'Select theme') + '</div>';
    html += '<div class="form-group"><label>Tax</label>' + Components.dropdown('inv-tax-mode', [
      { value: 'exclusive', label: 'Tax Exclusive' },
      { value: 'inclusive', label: 'Tax Inclusive' },
      { value: 'none', label: 'No Tax' }
    ], taxMode, 'Select tax mode') + '</div>';
    html += '<div class="form-group"></div>';
    html += '</div>';

    html += '<div class="form-row">';
    html += '<div class="form-group"><label>Title</label>' + Components.textInput('inv-title', invTitle, 'Optional title') + '</div>';
    html += '</div>';
    html += '<div class="form-row">';
    html += '<div class="form-group"><label>Summary</label>' + Components.textarea('inv-summary', invSummary, 'Optional summary', 2) + '</div>';
    html += '</div>';

    // Line items
    html += '<h3>Line Items</h3>';
    html += this._editableLineItems(lineItems, 'inv');

    // Totals (will be calculated dynamically)
    html += '<div class="totals-section" id="inv-totals"></div>';

    // Actions
    html += '<div class="form-actions">';
    if (isEdit) {
      html += Components.button('Save', 'save-invoice', 'primary', ' data-id="' + inv.id + '"');
    } else {
      html += Components.button('Save as Draft', 'save-invoice-draft', 'secondary');
      html += Components.button('Submit for Approval', 'save-invoice-submit', 'secondary');
      html += Components.button('Approve', 'save-invoice-approve', 'primary');
    }
    html += Components.button('Cancel', 'cancel-form', 'secondary');
    html += '</div></div>';
    return html;
  },

  _editableLineItems(lineItems, prefix) {
    const itemOpts = [{ value: '', label: '-- Select Item --' }].concat(AppState.items.filter(i => i.isSold).map(i => ({ value: i.id, label: i.code + ' - ' + i.description })));
    const accountOpts = AppState.getRevenueAccounts().map(a => ({ value: a.id, label: a.code + ' - ' + a.name }));
    const taxOpts = AppState.getOutputTaxRates().map(t => ({ value: t.id, label: t.name + ' (' + t.rate + '%)' }));
    const regionOpts = [{ value: '', label: 'None' }].concat(AppState.trackingCategories.find(tc => tc.id === 'track_region') ? AppState.trackingCategories.find(tc => tc.id === 'track_region').options.map(o => ({ value: o.id, label: o.name })) : []);
    const deptOpts = [{ value: '', label: 'None' }].concat(AppState.trackingCategories.find(tc => tc.id === 'track_dept') ? AppState.trackingCategories.find(tc => tc.id === 'track_dept').options.map(o => ({ value: o.id, label: o.name })) : []);

    let html = '<div class="line-items-edit" id="' + prefix + '-line-items">';
    html += '<table class="data-table editable-table"><thead><tr>';
    html += '<th>Item</th><th>Description</th><th class="col-narrow">Qty</th><th class="col-narrow">Price</th><th class="col-narrow">Disc %</th><th>Account</th><th>Tax</th><th>Region</th><th>Department</th><th class="col-narrow text-right">Amount</th><th></th>';
    html += '</tr></thead><tbody>';

    lineItems.forEach((li, idx) => {
      html += '<tr class="line-item-row" data-line-idx="' + idx + '">';
      html += '<td>' + Components.dropdown(prefix + '-item-' + idx, itemOpts, li.itemId || '', 'Item', 'compact-dropdown') + '</td>';
      html += '<td><input type="text" class="form-input compact" id="' + prefix + '-desc-' + idx + '" value="' + Components.escapeHtml(li.description) + '" placeholder="Description" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="' + prefix + '-qty-' + idx + '" value="' + li.quantity + '" min="0" step="0.01" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="' + prefix + '-price-' + idx + '" value="' + li.unitPrice + '" min="0" step="0.01" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="' + prefix + '-disc-' + idx + '" value="' + (li.discountPercent || 0) + '" min="0" max="100" step="0.01" /></td>';
      html += '<td>' + Components.dropdown(prefix + '-acc-' + idx, accountOpts, li.accountId, 'Account', 'compact-dropdown') + '</td>';
      html += '<td>' + Components.dropdown(prefix + '-tax-' + idx, taxOpts, li.taxRateId, 'Tax', 'compact-dropdown') + '</td>';
      html += '<td>' + Components.dropdown(prefix + '-region-' + idx, regionOpts, li.trackingRegion || '', 'Region', 'compact-dropdown') + '</td>';
      html += '<td>' + Components.dropdown(prefix + '-dept-' + idx, deptOpts, li.trackingDept || '', 'Dept', 'compact-dropdown') + '</td>';
      const amt = li.quantity * li.unitPrice * (1 - (li.discountPercent || 0) / 100);
      html += '<td class="text-right line-amount">' + Components.formatCurrency(amt) + '</td>';
      html += '<td><button class="btn-icon btn-remove-line" data-action="remove-line" data-prefix="' + prefix + '" data-line-idx="' + idx + '" title="Remove">&times;</button></td>';
      html += '</tr>';
    });

    html += '</tbody></table>';
    html += '<button class="btn btn-secondary btn-sm" data-action="add-line" data-prefix="' + prefix + '">+ Add Line</button>';
    html += '</div>';
    return html;
  },

  // ---- Quote List ----
  renderQuoteList() {
    const tab = AppState.currentTab || 'all';
    const statuses = [
      { id: 'all', label: 'All' },
      { id: 'draft', label: 'Draft' },
      { id: 'sent', label: 'Sent' },
      { id: 'accepted', label: 'Accepted' },
      { id: 'declined', label: 'Declined' }
    ];
    statuses.forEach(s => { s.count = AppState.getQuotesByStatus(s.id).length; });

    let html = '<div class="page-header"><h1>Quotes</h1>';
    html += '<div class="header-actions">' + Components.button('New Quote', 'new-quote', 'primary') + '</div></div>';
    html += Components.tabs(statuses, tab);

    const quotes = AppState.getQuotesByStatus(tab).sort((a, b) => b.date.localeCompare(a.date));
    if (quotes.length === 0) {
      html += Components.emptyState('&#128203;', 'No quotes', 'No quotes match this filter.', 'New Quote', 'new-quote');
    } else {
      html += '<div class="table-container"><table class="data-table" data-testid="quote-table"><thead><tr>';
      html += '<th>Number</th><th>Reference</th><th>To</th><th>Date</th><th>Expiry</th><th class="text-right">Total</th><th>Status</th></tr></thead><tbody>';
      quotes.forEach(q => {
        const contact = AppState.getContactById(q.contactId);
        html += '<tr class="table-row clickable">';
        html += '<td><a class="link" data-action="view-quote" data-id="' + q.id + '">' + Components.escapeHtml(q.number) + '</a></td>';
        html += '<td>' + Components.escapeHtml(q.reference) + '</td>';
        html += '<td>' + Components.escapeHtml(contact ? contact.name : '') + '</td>';
        html += '<td>' + Components.formatDate(q.date) + '</td>';
        html += '<td>' + Components.formatDate(q.expiryDate) + '</td>';
        html += '<td class="text-right">' + Components.formatCurrency(q.total, q.currency) + '</td>';
        html += '<td>' + Components.statusBadge(q.status) + (q.isInvoiced ? ' <span class="status-badge badge-paid">Invoiced</span>' : '') + '</td>';
        html += '</tr>';
      });
      html += '</tbody></table></div>';
    }
    return html;
  },

  // ---- Quote Detail ----
  renderQuoteDetail(quo) {
    if (!quo) return '<div class="error">Quote not found.</div>';
    const contact = AppState.getContactById(quo.contactId);

    let html = '<div class="page-header"><div class="header-left">';
    html += '<button class="btn btn-back" data-action="back-to-quotes">&larr; Back</button>';
    html += '<h1>' + Components.escapeHtml(quo.number) + '</h1>' + Components.statusBadge(quo.status);
    if (quo.isInvoiced) html += ' <span class="status-badge badge-paid">Invoiced</span>';
    html += '</div><div class="header-actions">';
    if (quo.status === 'draft') {
      html += Components.button('Edit', 'edit-quote', 'secondary', ' data-id="' + quo.id + '"');
      html += Components.button('Send', 'send-quote', 'primary', ' data-id="' + quo.id + '"');
      html += Components.button('Delete', 'delete-quote', 'danger', ' data-id="' + quo.id + '"');
    } else if (quo.status === 'sent') {
      html += Components.button('Edit', 'edit-quote', 'secondary', ' data-id="' + quo.id + '"');
      html += Components.button('Mark as Accepted', 'accept-quote', 'success', ' data-id="' + quo.id + '"');
      html += Components.button('Mark as Declined', 'decline-quote', 'danger', ' data-id="' + quo.id + '"');
    } else if (quo.status === 'accepted' && !quo.isInvoiced) {
      html += Components.button('Create Invoice', 'invoice-from-quote', 'primary', ' data-id="' + quo.id + '"');
    }
    if (quo.status !== 'deleted') {
      html += Components.button('Copy', 'copy-quote', 'secondary', ' data-id="' + quo.id + '"');
    }
    html += '</div></div>';

    html += '<div class="detail-card"><div class="detail-grid">';
    html += '<div class="detail-field"><label>To</label><div>' + Components.escapeHtml(contact ? contact.name : '') + '</div></div>';
    html += '<div class="detail-field"><label>Date</label><div>' + Components.formatDate(quo.date) + '</div></div>';
    html += '<div class="detail-field"><label>Expiry</label><div>' + Components.formatDate(quo.expiryDate) + '</div></div>';
    html += '<div class="detail-field"><label>Quote Number</label><div>' + Components.escapeHtml(quo.number) + '</div></div>';
    if (quo.reference) html += '<div class="detail-field"><label>Reference</label><div>' + Components.escapeHtml(quo.reference) + '</div></div>';
    html += '<div class="detail-field"><label>Currency</label><div>' + Components.escapeHtml(quo.currency) + '</div></div>';
    if (quo.title) html += '<div class="detail-field full-width"><label>Title</label><div>' + Components.escapeHtml(quo.title) + '</div></div>';
    if (quo.summary) html += '<div class="detail-field full-width"><label>Summary</label><div>' + Components.escapeHtml(quo.summary) + '</div></div>';
    if (quo.terms) html += '<div class="detail-field full-width"><label>Terms</label><div>' + Components.escapeHtml(quo.terms) + '</div></div>';
    html += '</div>';

    html += '<h3>Line Items</h3>';
    html += this._lineItemsTable(quo.lineItems, quo.taxMode, quo.currency);

    html += '<div class="totals-section">';
    html += '<div class="total-row"><span>Subtotal</span><span>' + Components.formatCurrency(quo.subtotal, quo.currency) + '</span></div>';
    html += '<div class="total-row"><span>Tax</span><span>' + Components.formatCurrency(quo.taxTotal, quo.currency) + '</span></div>';
    html += '<div class="total-row total-main"><span>Total</span><span>' + Components.formatCurrency(quo.total, quo.currency) + '</span></div>';
    html += '</div>';

    if (quo.notes.length > 0) {
      html += '<h3>History &amp; Notes</h3><div class="history-list">';
      quo.notes.slice().reverse().forEach(n => {
        html += '<div class="history-item"><span class="history-date">' + Components.formatDateTime(n.date) + '</span> <span class="history-user">' + Components.escapeHtml(n.user) + '</span>: ' + Components.escapeHtml(n.text) + '</div>';
      });
      html += '</div>';
    }
    html += '</div>';
    return html;
  },

  // ---- Quote Form ----
  renderQuoteForm(quo) {
    const isEdit = !!quo;
    const title = isEdit ? 'Edit Quote ' + quo.number : 'New Quote';
    const contactId = isEdit ? quo.contactId : '';
    const date = isEdit ? quo.date : Components.todayStr();
    const expiryDate = isEdit ? quo.expiryDate : (() => { const d = new Date(); d.setDate(d.getDate() + 30); return d.toISOString().split('T')[0]; })();
    const reference = isEdit ? quo.reference : '';
    const currency = isEdit ? quo.currency : 'AUD';
    const themeId = isEdit ? quo.brandingThemeId : 'theme_standard';
    const taxMode = isEdit ? quo.taxMode : AppState.invoiceSettings.defaultTaxMode;
    const quoTitle = isEdit ? (quo.title || '') : '';
    const quoSummary = isEdit ? (quo.summary || '') : '';
    const quoTerms = isEdit ? (quo.terms || '') : '';
    const lineItems = isEdit ? quo.lineItems : [{ id: AppState.generateLineItemId(), itemId: '', description: '', quantity: 1, unitPrice: 0, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }];

    let html = '<div class="page-header"><h1>' + Components.escapeHtml(title) + '</h1></div>';
    html += '<div class="form-card">';

    const contactOpts = AppState.contacts.filter(c => c.isCustomer).map(c => ({ value: c.id, label: c.name }));
    html += '<div class="form-row"><div class="form-group"><label>To <span class="required">*</span></label>' + Components.searchableDropdown('quo-contact', contactOpts, contactId, 'Search contacts...') + '</div></div>';

    html += '<div class="form-row form-row-4">';
    html += '<div class="form-group"><label>Date</label>' + Components.dateInput('quo-date', date) + '</div>';
    html += '<div class="form-group"><label>Expiry Date</label>' + Components.dateInput('quo-expiry-date', expiryDate) + '</div>';
    html += '<div class="form-group"><label>Reference</label>' + Components.textInput('quo-reference', reference) + '</div>';
    html += '<div class="form-group"><label>Currency</label>' + Components.dropdown('quo-currency', AppState.currencies.map(c => ({ value: c.code, label: c.code + ' - ' + c.name })), currency, 'Select currency') + '</div>';
    html += '</div>';

    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Branding Theme</label>' + Components.dropdown('quo-theme', AppState.brandingThemes.map(t => ({ value: t.id, label: t.name })), themeId, 'Select theme') + '</div>';
    html += '<div class="form-group"><label>Tax</label>' + Components.dropdown('quo-tax-mode', [{ value: 'exclusive', label: 'Tax Exclusive' }, { value: 'inclusive', label: 'Tax Inclusive' }, { value: 'none', label: 'No Tax' }], taxMode) + '</div>';
    html += '<div class="form-group"></div></div>';

    html += '<div class="form-row"><div class="form-group"><label>Title</label>' + Components.textInput('quo-title', quoTitle, 'Optional title') + '</div></div>';
    html += '<div class="form-row"><div class="form-group"><label>Summary</label>' + Components.textarea('quo-summary', quoSummary, 'Optional summary', 2) + '</div></div>';
    html += '<div class="form-row"><div class="form-group"><label>Terms</label>' + Components.textarea('quo-terms', quoTerms, 'Optional terms & conditions', 2) + '</div></div>';

    html += '<h3>Line Items</h3>';
    html += this._editableLineItems(lineItems, 'quo');
    html += '<div class="totals-section" id="quo-totals"></div>';

    html += '<div class="form-actions">';
    if (isEdit) {
      html += Components.button('Save', 'save-quote', 'primary', ' data-id="' + quo.id + '"');
    } else {
      html += Components.button('Save as Draft', 'save-quote-draft', 'secondary');
      html += Components.button('Save and Send', 'save-quote-send', 'primary');
    }
    html += Components.button('Cancel', 'cancel-form', 'secondary');
    html += '</div></div>';
    return html;
  },

  // ---- Credit Note List ----
  renderCreditNoteList() {
    const tab = AppState.currentTab || 'all';
    const statuses = [
      { id: 'all', label: 'All' },
      { id: 'draft', label: 'Draft' },
      { id: 'awaiting_payment', label: 'Open' },
      { id: 'paid', label: 'Allocated' }
    ];
    statuses.forEach(s => { s.count = AppState.getCreditNotesByStatus(s.id).length; });

    let html = '<div class="page-header"><h1>Credit Notes</h1>';
    html += '<div class="header-actions">' + Components.button('New Credit Note', 'new-credit-note', 'primary') + '</div></div>';
    html += Components.tabs(statuses, tab);

    const notes = AppState.getCreditNotesByStatus(tab).sort((a, b) => b.date.localeCompare(a.date));
    if (notes.length === 0) {
      html += Components.emptyState('&#128179;', 'No credit notes', 'No credit notes match this filter.');
    } else {
      html += '<div class="table-container"><table class="data-table" data-testid="cn-table"><thead><tr>';
      html += '<th>Number</th><th>Reference</th><th>To</th><th>Date</th><th class="text-right">Total</th><th class="text-right">Remaining</th><th>Status</th></tr></thead><tbody>';
      notes.forEach(cn => {
        const contact = AppState.getContactById(cn.contactId);
        html += '<tr class="table-row clickable">';
        html += '<td><a class="link" data-action="view-credit-note" data-id="' + cn.id + '">' + Components.escapeHtml(cn.number) + '</a></td>';
        html += '<td>' + Components.escapeHtml(cn.reference) + '</td>';
        html += '<td>' + Components.escapeHtml(contact ? contact.name : '') + '</td>';
        html += '<td>' + Components.formatDate(cn.date) + '</td>';
        html += '<td class="text-right">' + Components.formatCurrency(cn.total, cn.currency) + '</td>';
        html += '<td class="text-right">' + Components.formatCurrency(cn.remainingCredit, cn.currency) + '</td>';
        html += '<td>' + Components.statusBadge(cn.status) + '</td>';
        html += '</tr>';
      });
      html += '</tbody></table></div>';
    }
    return html;
  },

  // ---- Credit Note Detail ----
  renderCreditNoteDetail(cn) {
    if (!cn) return '<div class="error">Credit note not found.</div>';
    const contact = AppState.getContactById(cn.contactId);

    let html = '<div class="page-header"><div class="header-left">';
    html += '<button class="btn btn-back" data-action="back-to-credit-notes">&larr; Back</button>';
    html += '<h1>' + Components.escapeHtml(cn.number) + '</h1>' + Components.statusBadge(cn.status);
    html += '</div><div class="header-actions">';
    if (cn.status === 'draft') {
      html += Components.button('Edit', 'edit-credit-note', 'secondary', ' data-id="' + cn.id + '"');
      html += Components.button('Approve', 'approve-credit-note', 'primary', ' data-id="' + cn.id + '"');
      html += Components.button('Delete', 'delete-credit-note', 'danger', ' data-id="' + cn.id + '"');
    }
    if (cn.status === 'awaiting_payment' && cn.remainingCredit > 0) {
      html += Components.button('Allocate to Invoice', 'show-allocate-cn', 'primary', ' data-id="' + cn.id + '"');
    }
    html += '</div></div>';

    html += '<div class="detail-card"><div class="detail-grid">';
    html += '<div class="detail-field"><label>To</label><div>' + Components.escapeHtml(contact ? contact.name : '') + '</div></div>';
    html += '<div class="detail-field"><label>Date</label><div>' + Components.formatDate(cn.date) + '</div></div>';
    html += '<div class="detail-field"><label>Number</label><div>' + Components.escapeHtml(cn.number) + '</div></div>';
    if (cn.reference) html += '<div class="detail-field"><label>Reference</label><div>' + Components.escapeHtml(cn.reference) + '</div></div>';
    html += '</div>';

    html += '<h3>Line Items</h3>';
    html += this._lineItemsTable(cn.lineItems, cn.taxMode, cn.currency);

    html += '<div class="totals-section">';
    html += '<div class="total-row"><span>Subtotal</span><span>' + Components.formatCurrency(cn.subtotal, cn.currency) + '</span></div>';
    html += '<div class="total-row"><span>Tax</span><span>' + Components.formatCurrency(cn.taxTotal, cn.currency) + '</span></div>';
    html += '<div class="total-row total-main"><span>Total</span><span>' + Components.formatCurrency(cn.total, cn.currency) + '</span></div>';
    html += '<div class="total-row total-due"><span>Remaining Credit</span><span>' + Components.formatCurrency(cn.remainingCredit, cn.currency) + '</span></div>';
    html += '</div>';

    if (cn.allocations.length > 0) {
      html += '<h3>Allocations</h3>';
      html += '<table class="data-table compact"><thead><tr><th>Invoice</th><th>Date</th><th class="text-right">Amount</th></tr></thead><tbody>';
      cn.allocations.forEach(a => {
        html += '<tr><td><a class="link" data-action="view-invoice" data-id="' + a.invoiceId + '">' + Components.escapeHtml(a.invoiceNumber) + '</a></td>';
        html += '<td>' + Components.formatDate(a.date) + '</td>';
        html += '<td class="text-right">' + Components.formatCurrency(a.amount, cn.currency) + '</td></tr>';
      });
      html += '</tbody></table>';
    }

    if (cn.notes && cn.notes.length > 0) {
      html += '<h3>History &amp; Notes</h3><div class="history-list">';
      cn.notes.slice().reverse().forEach(n => {
        html += '<div class="history-item"><span class="history-date">' + Components.formatDateTime(n.date) + '</span> <span class="history-user">' + Components.escapeHtml(n.user) + '</span>: ' + Components.escapeHtml(n.text) + '</div>';
      });
      html += '</div>';
    }
    html += '</div>';
    return html;
  },

  // ---- Credit Note Form ----
  renderCreditNoteForm(cn) {
    const isEdit = !!cn;
    const title = isEdit ? 'Edit Credit Note ' + cn.number : 'New Credit Note';
    const contactId = isEdit ? cn.contactId : '';
    const date = isEdit ? cn.date : Components.todayStr();
    const reference = isEdit ? cn.reference : '';
    const taxMode = isEdit ? cn.taxMode : AppState.invoiceSettings.defaultTaxMode;
    const lineItems = isEdit ? cn.lineItems : [{ id: AppState.generateLineItemId(), itemId: '', description: '', quantity: 1, unitPrice: 0, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }];

    let html = '<div class="page-header"><h1>' + Components.escapeHtml(title) + '</h1></div>';
    html += '<div class="form-card">';

    const contactOpts = AppState.contacts.filter(c => c.isCustomer).map(c => ({ value: c.id, label: c.name }));
    html += '<div class="form-row"><div class="form-group"><label>To <span class="required">*</span></label>' + Components.searchableDropdown('cn-contact', contactOpts, contactId, 'Search contacts...') + '</div></div>';

    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Date</label>' + Components.dateInput('cn-date', date) + '</div>';
    html += '<div class="form-group"><label>Reference</label>' + Components.textInput('cn-reference', reference) + '</div>';
    html += '<div class="form-group"><label>Tax</label>' + Components.dropdown('cn-tax-mode', [{ value: 'exclusive', label: 'Tax Exclusive' }, { value: 'inclusive', label: 'Tax Inclusive' }, { value: 'none', label: 'No Tax' }], taxMode) + '</div>';
    html += '</div>';

    html += '<h3>Line Items</h3>';
    html += this._editableLineItems(lineItems, 'cn');
    html += '<div class="totals-section" id="cn-totals"></div>';

    html += '<div class="form-actions">';
    if (isEdit) {
      html += Components.button('Save', 'save-credit-note', 'primary', ' data-id="' + cn.id + '"');
    } else {
      html += Components.button('Save as Draft', 'save-cn-draft', 'secondary');
      html += Components.button('Approve', 'save-cn-approve', 'primary');
    }
    html += Components.button('Cancel', 'cancel-form', 'secondary');
    html += '</div></div>';
    return html;
  },

  // ---- Repeating Invoice List ----
  renderRepeatingInvoiceList() {
    let html = '<div class="page-header"><h1>Repeating Invoices</h1>';
    html += '<div class="header-actions">' + Components.button('New Repeating Invoice', 'new-repeating', 'primary') + '</div></div>';

    const repeating = AppState.repeatingInvoices;
    if (repeating.length === 0) {
      html += Components.emptyState('&#128260;', 'No repeating invoices', 'Set up recurring invoices to automate billing.', 'New Repeating Invoice', 'new-repeating');
    } else {
      html += '<div class="table-container"><table class="data-table" data-testid="repeating-table"><thead><tr>';
      html += '<th>Contact</th><th>Frequency</th><th>Next Invoice</th><th>End Date</th><th>Save As</th><th>Status</th><th></th></tr></thead><tbody>';
      repeating.forEach(r => {
        const contact = AppState.getContactById(r.contactId);
        const saveLabels = { draft: 'Draft', approved: 'Approved', approved_for_sending: 'Approved for Sending' };
        html += '<tr class="table-row clickable">';
        html += '<td><a class="link" data-action="view-repeating" data-id="' + r.id + '">' + Components.escapeHtml(contact ? contact.name : '') + '</a></td>';
        html += '<td>' + Components.escapeHtml(r.frequency.charAt(0).toUpperCase() + r.frequency.slice(1)) + '</td>';
        html += '<td>' + Components.formatDate(r.nextDate) + '</td>';
        html += '<td>' + (r.endDate ? Components.formatDate(r.endDate) : 'No end date') + '</td>';
        html += '<td>' + (saveLabels[r.saveAs] || r.saveAs) + '</td>';
        html += '<td>' + Components.statusBadge(r.status) + '</td>';
        html += '<td><button class="btn btn-sm btn-danger" data-action="delete-repeating" data-id="' + r.id + '">Delete</button></td>';
        html += '</tr>';
      });
      html += '</tbody></table></div>';
    }
    return html;
  },

  // ---- Repeating Invoice Form ----
  renderRepeatingInvoiceForm(ri) {
    const isEdit = !!ri;
    const title = isEdit ? 'Edit Repeating Invoice' : 'New Repeating Invoice';
    const contactId = isEdit ? ri.contactId : '';
    const frequency = isEdit ? ri.frequency : 'monthly';
    const startDate = isEdit ? ri.startDate : Components.todayStr();
    const nextDate = isEdit ? ri.nextDate : Components.todayStr();
    const endDate = isEdit ? ri.endDate : '';
    const saveAs = isEdit ? ri.saveAs : 'draft';
    const reference = isEdit ? ri.reference : '';
    const taxMode = isEdit ? ri.taxMode : AppState.invoiceSettings.defaultTaxMode;
    const themeId = isEdit ? ri.brandingThemeId : 'theme_standard';
    const lineItems = isEdit ? ri.lineItems : [{ id: AppState.generateLineItemId(), itemId: '', description: '', quantity: 1, unitPrice: 0, accountId: 'acc_200', taxRateId: 'tax_gst' }];

    let html = '<div class="page-header"><h1>' + Components.escapeHtml(title) + '</h1></div>';
    html += '<div class="form-card">';

    const contactOpts = AppState.contacts.filter(c => c.isCustomer).map(c => ({ value: c.id, label: c.name }));
    html += '<div class="form-row"><div class="form-group"><label>To <span class="required">*</span></label>' + Components.searchableDropdown('rep-contact', contactOpts, contactId, 'Search contacts...') + '</div></div>';

    html += '<div class="form-row form-row-4">';
    html += '<div class="form-group"><label>Frequency</label>' + Components.dropdown('rep-frequency', [{ value: 'weekly', label: 'Weekly' }, { value: 'fortnightly', label: 'Fortnightly' }, { value: 'monthly', label: 'Monthly' }, { value: 'bimonthly', label: 'Every 2 Months' }, { value: 'quarterly', label: 'Quarterly' }, { value: 'annually', label: 'Annually' }], frequency) + '</div>';
    html += '<div class="form-group"><label>Start Date</label>' + Components.dateInput('rep-start-date', startDate) + '</div>';
    html += '<div class="form-group"><label>Next Invoice Date</label>' + Components.dateInput('rep-next-date', nextDate) + '</div>';
    html += '<div class="form-group"><label>End Date</label>' + Components.dateInput('rep-end-date', endDate) + '</div>';
    html += '</div>';

    html += '<div class="form-row form-row-4">';
    html += '<div class="form-group"><label>Save As</label>' + Components.dropdown('rep-save-as', [{ value: 'draft', label: 'Draft' }, { value: 'approved', label: 'Approved' }, { value: 'approved_for_sending', label: 'Approved for Sending' }], saveAs) + '</div>';
    html += '<div class="form-group"><label>Branding Theme</label>' + Components.dropdown('rep-theme', AppState.brandingThemes.map(t => ({ value: t.id, label: t.name })), themeId) + '</div>';
    html += '<div class="form-group"><label>Tax</label>' + Components.dropdown('rep-tax-mode', [{ value: 'exclusive', label: 'Tax Exclusive' }, { value: 'inclusive', label: 'Tax Inclusive' }, { value: 'none', label: 'No Tax' }], taxMode) + '</div>';
    html += '<div class="form-group"><label>Reference</label>' + Components.textInput('rep-reference', reference) + '</div>';
    html += '</div>';

    html += '<h3>Line Items</h3>';
    const itemOpts = [{ value: '', label: '-- Select --' }].concat(AppState.items.filter(i => i.isSold).map(i => ({ value: i.id, label: i.code + ' - ' + i.description })));
    const accountOpts = AppState.getRevenueAccounts().map(a => ({ value: a.id, label: a.code + ' - ' + a.name }));
    const taxOpts = AppState.getOutputTaxRates().map(t => ({ value: t.id, label: t.name + ' (' + t.rate + '%)' }));

    html += '<div class="line-items-edit" id="rep-line-items"><table class="data-table editable-table"><thead><tr>';
    html += '<th>Item</th><th>Description</th><th class="col-narrow">Qty</th><th class="col-narrow">Price</th><th>Account</th><th>Tax</th><th></th></tr></thead><tbody>';
    lineItems.forEach((li, idx) => {
      html += '<tr class="line-item-row" data-line-idx="' + idx + '">';
      html += '<td>' + Components.dropdown('rep-item-' + idx, itemOpts, li.itemId || '', 'Item', 'compact-dropdown') + '</td>';
      html += '<td><input type="text" class="form-input compact" id="rep-desc-' + idx + '" value="' + Components.escapeHtml(li.description) + '" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="rep-qty-' + idx + '" value="' + li.quantity + '" min="0" step="0.01" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="rep-price-' + idx + '" value="' + li.unitPrice + '" min="0" step="0.01" /></td>';
      html += '<td>' + Components.dropdown('rep-acc-' + idx, accountOpts, li.accountId, 'Account', 'compact-dropdown') + '</td>';
      html += '<td>' + Components.dropdown('rep-tax-' + idx, taxOpts, li.taxRateId, 'Tax', 'compact-dropdown') + '</td>';
      html += '<td><button class="btn-icon btn-remove-line" data-action="remove-line" data-prefix="rep" data-line-idx="' + idx + '">&times;</button></td>';
      html += '</tr>';
    });
    html += '</tbody></table>';
    html += '<button class="btn btn-secondary btn-sm" data-action="add-line" data-prefix="rep">+ Add Line</button></div>';

    html += '<div class="form-actions">';
    if (isEdit) {
      html += Components.button('Save', 'save-repeating', 'primary', ' data-id="' + ri.id + '"');
    } else {
      html += Components.button('Save', 'save-repeating-new', 'primary');
    }
    html += Components.button('Cancel', 'cancel-form', 'secondary');
    html += '</div></div>';
    return html;
  },

  // ---- Settings ----
  renderSettings() {
    const s = AppState.invoiceSettings;
    let html = '<div class="page-header"><h1>Invoice Settings</h1></div>';
    html += '<div class="form-card">';

    html += '<h3>Invoice Numbering</h3>';
    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Invoice Prefix</label>' + Components.textInput('set-inv-prefix', s.invoicePrefix) + '</div>';
    html += '<div class="form-group"><label>Next Invoice Number</label>' + Components.textInput('set-inv-next', s.invoiceNextNumber, '', 'number') + '</div>';
    html += '<div class="form-group"></div></div>';

    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Credit Note Prefix</label>' + Components.textInput('set-cn-prefix', s.creditNotePrefix) + '</div>';
    html += '<div class="form-group"><label>Next Credit Note Number</label>' + Components.textInput('set-cn-next', s.creditNoteNextNumber, '', 'number') + '</div>';
    html += '<div class="form-group"></div></div>';

    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Quote Prefix</label>' + Components.textInput('set-quo-prefix', s.quotePrefix) + '</div>';
    html += '<div class="form-group"><label>Next Quote Number</label>' + Components.textInput('set-quo-next', s.quoteNextNumber, '', 'number') + '</div>';
    html += '<div class="form-group"></div></div>';

    html += '<h3>Default Due Date</h3>';
    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Due</label>' + Components.textInput('set-due-days', s.defaultDueDate.days, '', 'number') + '</div>';
    html += '<div class="form-group"><label>Type</label>' + Components.dropdown('set-due-type', DUE_DATE_OPTIONS.map(o => ({ value: o.value, label: o.label })), s.defaultDueDate.type) + '</div>';
    html += '<div class="form-group"></div></div>';

    html += '<h3>Default Tax Mode</h3>';
    html += '<div class="form-row">';
    html += '<div class="form-group">' + Components.dropdown('set-tax-mode', [{ value: 'exclusive', label: 'Tax Exclusive' }, { value: 'inclusive', label: 'Tax Inclusive' }, { value: 'none', label: 'No Tax' }], s.defaultTaxMode) + '</div></div>';

    html += '<h3>Display Options</h3>';
    html += Components.toggle('set-show-tax', s.showTaxColumn, 'Show tax column on invoices');
    html += Components.toggle('set-show-disc', s.showDiscountColumn, 'Show discount column on invoices');
    html += Components.toggle('set-show-code', s.showItemCode, 'Show item code on invoices');

    html += '<div class="form-actions">' + Components.button('Save Settings', 'save-settings', 'primary') + '</div>';
    html += '</div>';
    return html;
  },

  // ---- Branding Themes ----
  renderTemplates() {
    let html = '<div class="page-header"><h1>Branding Themes</h1>';
    html += '<div class="header-actions">' + Components.button('New Theme', 'new-theme', 'primary') + '</div></div>';

    html += '<div class="themes-grid">';
    AppState.brandingThemes.forEach(t => {
      html += '<div class="theme-card' + (t.isDefault ? ' theme-default' : '') + '">';
      html += '<div class="theme-name">' + Components.escapeHtml(t.name) + '</div>';
      if (t.isDefault) html += '<span class="status-badge badge-active">Default</span>';
      html += '<div class="theme-actions">';
      html += '<button class="btn btn-sm btn-secondary" data-action="edit-theme" data-id="' + t.id + '">Edit</button>';
      if (!t.isDefault) {
        html += '<button class="btn btn-sm btn-secondary" data-action="set-default-theme" data-id="' + t.id + '">Set Default</button>';
        html += '<button class="btn btn-sm btn-danger" data-action="delete-theme" data-id="' + t.id + '">Delete</button>';
      }
      html += '</div></div>';
    });
    html += '</div>';
    return html;
  },

  renderThemeForm(theme) {
    const isEdit = !!theme;
    const title = isEdit ? 'Edit Theme: ' + theme.name : 'New Branding Theme';
    const name = isEdit ? theme.name : '';
    const pt = isEdit ? theme.paymentTerms : '';
    const tc = isEdit ? theme.termsAndConditions : '';
    const showTax = isEdit ? theme.showTaxNumber : true;
    const showAdv = isEdit ? theme.showPaymentAdvice : true;

    let html = '<div class="page-header"><h1>' + Components.escapeHtml(title) + '</h1></div>';
    html += '<div class="form-card">';
    html += '<div class="form-row"><div class="form-group"><label>Theme Name <span class="required">*</span></label>' + Components.textInput('theme-name', name, 'Enter theme name') + '</div></div>';
    html += '<div class="form-row"><div class="form-group"><label>Payment Terms</label>' + Components.textarea('theme-payment-terms', pt, 'Payment instructions...', 3) + '</div></div>';
    html += '<div class="form-row"><div class="form-group"><label>Terms &amp; Conditions</label>' + Components.textarea('theme-terms', tc, 'Terms and conditions...', 3) + '</div></div>';
    html += Components.toggle('theme-show-tax', showTax, 'Show tax number on invoice');
    html += Components.toggle('theme-show-advice', showAdv, 'Show payment advice');
    html += '<div class="form-actions">';
    if (isEdit) {
      html += Components.button('Save', 'save-theme', 'primary', ' data-id="' + theme.id + '"');
    } else {
      html += Components.button('Create Theme', 'save-theme-new', 'primary');
    }
    html += Components.button('Cancel', 'cancel-form', 'secondary');
    html += '</div></div>';
    return html;
  },

  // ---- Invoice Reminders ----
  renderReminders() {
    let html = '<div class="page-header"><h1>Invoice Reminders</h1>';
    html += '<div class="header-actions">' + Components.button('Add Reminder', 'new-reminder', 'primary') + '</div></div>';

    html += '<div class="form-card">';
    if (AppState.invoiceReminders.length === 0) {
      html += Components.emptyState('&#128276;', 'No reminders', 'Set up reminders to automatically notify customers about upcoming or overdue invoices.');
    } else {
      html += '<div class="reminders-list">';
      AppState.invoiceReminders.forEach(r => {
        const timingLabel = r.timing === 'before' ? r.days + ' day(s) before due date' : r.days + ' day(s) after due date';
        html += '<div class="reminder-card' + (r.enabled ? '' : ' disabled') + '">';
        html += '<div class="reminder-header">';
        html += '<label class="toggle-row compact"><span class="toggle-switch"><input type="checkbox" id="toggle-rem-' + r.id + '" ' + (r.enabled ? 'checked' : '') + ' data-action="toggle-reminder" data-id="' + r.id + '" /><span class="toggle-slider"></span></span></label>';
        html += '<div class="reminder-timing">' + Components.escapeHtml(timingLabel) + '</div>';
        html += '<button class="btn btn-sm btn-secondary" data-action="edit-reminder" data-id="' + r.id + '">Edit</button>';
        html += '<button class="btn btn-sm btn-danger" data-action="delete-reminder" data-id="' + r.id + '">Delete</button>';
        html += '</div>';
        html += '<div class="reminder-subject">' + Components.escapeHtml(r.subject) + '</div>';
        html += '</div>';
      });
      html += '</div>';
    }
    html += '</div>';
    return html;
  },

  renderReminderForm(rem) {
    const isEdit = !!rem;
    const title = isEdit ? 'Edit Reminder' : 'New Reminder';
    const timing = isEdit ? rem.timing : 'before';
    const days = isEdit ? rem.days : 7;
    const subject = isEdit ? rem.subject : '';
    const body = isEdit ? rem.body : '';
    const inclPdf = isEdit ? rem.includeInvoicePdf : true;
    const inclSum = isEdit ? rem.includeSummary : true;

    let html = '<div class="page-header"><h1>' + Components.escapeHtml(title) + '</h1></div>';
    html += '<div class="form-card">';
    html += '<div class="form-row form-row-3">';
    html += '<div class="form-group"><label>Timing</label>' + Components.dropdown('rem-timing', [{ value: 'before', label: 'Before due date' }, { value: 'after', label: 'After due date (overdue)' }], timing) + '</div>';
    html += '<div class="form-group"><label>Days</label>' + Components.textInput('rem-days', days, '', 'number') + '</div>';
    html += '<div class="form-group"></div></div>';
    html += '<div class="form-row"><div class="form-group"><label>Subject</label>' + Components.textInput('rem-subject', subject, 'Email subject line') + '</div></div>';
    html += '<div class="form-row"><div class="form-group"><label>Email Body</label>' + Components.textarea('rem-body', body, 'Email body...', 6) + '</div></div>';
    html += Components.toggle('rem-incl-pdf', inclPdf, 'Include invoice PDF');
    html += Components.toggle('rem-incl-summary', inclSum, 'Include detail summary');
    html += '<div class="form-actions">';
    if (isEdit) {
      html += Components.button('Save', 'save-reminder', 'primary', ' data-id="' + rem.id + '"');
    } else {
      html += Components.button('Add Reminder', 'save-reminder-new', 'primary');
    }
    html += Components.button('Cancel', 'cancel-form', 'secondary');
    html += '</div></div>';
    return html;
  },

  // ---- Search Results ----
  renderSearchResults(results) {
    let html = '<div class="page-header"><h1>Search Results</h1></div>';
    if (results.length === 0) {
      html += Components.emptyState('&#128269;', 'No results', 'Try a different search term.');
    } else {
      html += '<div class="table-container"><table class="data-table"><thead><tr>';
      html += '<th>Type</th><th>Number</th><th>Contact</th><th>Date</th><th class="text-right">Total</th><th>Status</th></tr></thead><tbody>';
      results.forEach(r => {
        const typeLabels = { invoice: 'Invoice', quote: 'Quote', creditNote: 'Credit Note' };
        const viewAction = r.type === 'invoice' ? 'view-invoice' : r.type === 'quote' ? 'view-quote' : 'view-credit-note';
        html += '<tr class="table-row clickable">';
        html += '<td>' + (typeLabels[r.type] || r.type) + '</td>';
        html += '<td><a class="link" data-action="' + viewAction + '" data-id="' + r.id + '">' + Components.escapeHtml(r.number) + '</a></td>';
        html += '<td>' + Components.escapeHtml(r.contact) + '</td>';
        html += '<td>' + Components.formatDate(r.date) + '</td>';
        html += '<td class="text-right">' + Components.formatCurrency(r.total) + '</td>';
        html += '<td>' + Components.statusBadge(r.status) + '</td>';
        html += '</tr>';
      });
      html += '</tbody></table></div>';
    }
    return html;
  },

  // ---- Payment Modal ----
  renderPaymentModal(inv) {
    const body = '<div class="form-row form-row-3">' +
      '<div class="form-group"><label>Date</label>' + Components.dateInput('pay-date', Components.todayStr()) + '</div>' +
      '<div class="form-group"><label>Amount</label><input type="number" class="form-input" id="pay-amount" value="' + inv.amountDue.toFixed(2) + '" min="0.01" max="' + inv.amountDue.toFixed(2) + '" step="0.01" /></div>' +
      '<div class="form-group"><label>Reference</label>' + Components.textInput('pay-reference', '') + '</div></div>' +
      '<div class="form-row"><div class="form-group"><label>Account</label>' + Components.dropdown('pay-account', AppState.accounts.filter(a => a.type === 'Bank').map(a => ({ value: a.id, label: a.code + ' - ' + a.name })), 'acc_090') + '</div></div>';
    const footer = '<button class="btn btn-secondary" data-action="close-modal" data-modal-id="paymentModal">Cancel</button>' +
      '<button class="btn btn-primary" data-action="confirm-add-payment" data-invoice-id="' + inv.id + '">Record Payment</button>';
    return Components.modal('paymentModal', 'Record Payment for ' + inv.number, body, footer);
  },

  // ---- Allocate Credit Note Modal ----
  renderAllocateModal(cn) {
    const contact = AppState.getContactById(cn.contactId);
    const openInvoices = AppState.invoices.filter(i => i.contactId === cn.contactId && i.status === 'awaiting_payment' && i.amountDue > 0);
    let body = '<p>Remaining credit: <strong>' + Components.formatCurrency(cn.remainingCredit, cn.currency) + '</strong></p>';
    if (openInvoices.length === 0) {
      body += '<p>No open invoices for ' + Components.escapeHtml(contact ? contact.name : '') + '.</p>';
    } else {
      body += '<div class="form-group"><label>Invoice</label>' + Components.dropdown('alloc-invoice', openInvoices.map(i => ({ value: i.id, label: i.number + ' - Due: ' + Components.formatCurrency(i.amountDue) })), '', 'Select invoice') + '</div>';
      body += '<div class="form-group"><label>Amount</label><input type="number" class="form-input" id="alloc-amount" value="' + cn.remainingCredit.toFixed(2) + '" min="0.01" step="0.01" /></div>';
    }
    const footer = openInvoices.length > 0 ?
      '<button class="btn btn-secondary" data-action="close-modal" data-modal-id="allocateModal">Cancel</button><button class="btn btn-primary" data-action="confirm-allocate-cn" data-cn-id="' + cn.id + '">Allocate</button>' :
      '<button class="btn btn-secondary" data-action="close-modal" data-modal-id="allocateModal">Close</button>';
    return Components.modal('allocateModal', 'Allocate Credit Note ' + cn.number, body, footer);
  }
};

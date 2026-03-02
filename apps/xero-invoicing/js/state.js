const AppState = {
  // Persistent state (pushed to server)
  contacts: [],
  invoices: [],
  quotes: [],
  creditNotes: [],
  repeatingInvoices: [],
  items: [],
  taxRates: [],
  accounts: [],
  trackingCategories: [],
  currencies: [],
  brandingThemes: [],
  invoiceSettings: {},
  invoiceReminders: [],
  currentUser: null,

  // ID counters
  _nextInvoiceNum: 67,
  _nextQuoteNum: 30,
  _nextCreditNoteNum: 13,
  _nextContactId: 26,
  _nextItemId: 16,
  _nextReminderId: 5,
  _nextRepeatId: 6,
  _nextLineItemId: 1000,
  _nextPaymentId: 100,
  _nextThemeId: 5,

  // Transient UI state
  currentView: 'dashboard',
  currentSubView: '',
  currentId: null,
  currentTab: 'all',
  searchQuery: '',
  searchResults: null,
  selectedIds: new Set(),
  modalState: null,
  toastMessage: null,
  formDirty: false,

  _listeners: [],

  subscribe(fn) {
    this._listeners.push(fn);
  },

  notify() {
    this._persist();
    this._pushStateToServer();
    for (const fn of this._listeners) {
      try { fn(); } catch (e) { console.error('Listener error:', e); }
    }
  },

  init() {
    const persisted = this._loadPersistedData();
    if (persisted && persisted._seedVersion === SEED_DATA_VERSION) {
      this.contacts = persisted.contacts || [];
      this.invoices = persisted.invoices || [];
      this.quotes = persisted.quotes || [];
      this.creditNotes = persisted.creditNotes || [];
      this.repeatingInvoices = persisted.repeatingInvoices || [];
      this.items = persisted.items || [];
      this.taxRates = persisted.taxRates || [];
      this.accounts = persisted.accounts || [];
      this.trackingCategories = persisted.trackingCategories || [];
      this.currencies = persisted.currencies || [];
      this.brandingThemes = persisted.brandingThemes || [];
      this.invoiceSettings = persisted.invoiceSettings || {};
      this.invoiceReminders = persisted.invoiceReminders || [];
      this.currentUser = persisted.currentUser || null;
      this._nextInvoiceNum = persisted._nextInvoiceNum || 67;
      this._nextQuoteNum = persisted._nextQuoteNum || 30;
      this._nextCreditNoteNum = persisted._nextCreditNoteNum || 13;
      this._nextContactId = persisted._nextContactId || 26;
      this._nextItemId = persisted._nextItemId || 16;
      this._nextReminderId = persisted._nextReminderId || 5;
      this._nextRepeatId = persisted._nextRepeatId || 6;
      this._nextLineItemId = persisted._nextLineItemId || 1000;
      this._nextPaymentId = persisted._nextPaymentId || 100;
      this._nextThemeId = persisted._nextThemeId || 5;
    } else {
      this._loadSeedData();
    }
  },

  _loadSeedData() {
    this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
    this.contacts = JSON.parse(JSON.stringify(CONTACTS));
    this.invoices = JSON.parse(JSON.stringify(INVOICES));
    this.quotes = JSON.parse(JSON.stringify(QUOTES));
    this.creditNotes = JSON.parse(JSON.stringify(CREDIT_NOTES));
    this.repeatingInvoices = JSON.parse(JSON.stringify(REPEATING_INVOICES));
    this.items = JSON.parse(JSON.stringify(ITEMS));
    this.taxRates = JSON.parse(JSON.stringify(TAX_RATES));
    this.accounts = JSON.parse(JSON.stringify(ACCOUNTS));
    this.trackingCategories = JSON.parse(JSON.stringify(TRACKING_CATEGORIES));
    this.currencies = JSON.parse(JSON.stringify(CURRENCIES));
    this.brandingThemes = JSON.parse(JSON.stringify(BRANDING_THEMES));
    this.invoiceSettings = JSON.parse(JSON.stringify(INVOICE_SETTINGS));
    this.invoiceReminders = JSON.parse(JSON.stringify(INVOICE_REMINDERS));
    this._nextInvoiceNum = INVOICE_SETTINGS.invoiceNextNumber;
    this._nextQuoteNum = INVOICE_SETTINGS.quoteNextNumber;
    this._nextCreditNoteNum = INVOICE_SETTINGS.creditNoteNextNumber;
    this._nextContactId = 26;
    this._nextItemId = 16;
    this._nextReminderId = 5;
    this._nextRepeatId = 6;
    this._nextLineItemId = 1000;
    this._nextPaymentId = 100;
    this._nextThemeId = 5;
  },

  _loadPersistedData() {
    try {
      const raw = localStorage.getItem('xeroInvoicingState');
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  },

  _persist() {
    const state = this.getSerializableState();
    localStorage.setItem('xeroInvoicingState', JSON.stringify(state));
  },

  _pushStateToServer() {
    const state = this.getSerializableState();
    fetch('/api/state', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(state)
    }).catch(() => {});
  },

  getSerializableState() {
    return {
      _seedVersion: SEED_DATA_VERSION,
      contacts: this.contacts,
      invoices: this.invoices,
      quotes: this.quotes,
      creditNotes: this.creditNotes,
      repeatingInvoices: this.repeatingInvoices,
      items: this.items,
      taxRates: this.taxRates,
      accounts: this.accounts,
      trackingCategories: this.trackingCategories,
      currencies: this.currencies,
      brandingThemes: this.brandingThemes,
      invoiceSettings: this.invoiceSettings,
      invoiceReminders: this.invoiceReminders,
      currentUser: this.currentUser,
      _nextInvoiceNum: this._nextInvoiceNum,
      _nextQuoteNum: this._nextQuoteNum,
      _nextCreditNoteNum: this._nextCreditNoteNum,
      _nextContactId: this._nextContactId,
      _nextItemId: this._nextItemId,
      _nextReminderId: this._nextReminderId,
      _nextRepeatId: this._nextRepeatId,
      _nextLineItemId: this._nextLineItemId,
      _nextPaymentId: this._nextPaymentId,
      _nextThemeId: this._nextThemeId
    };
  },

  resetToSeedData() {
    localStorage.removeItem('xeroInvoicingState');
    this._loadSeedData();
    this.currentView = 'dashboard';
    this.currentSubView = '';
    this.currentId = null;
    this.currentTab = 'all';
    this.searchQuery = '';
    this.searchResults = null;
    this.selectedIds = new Set();
    this.modalState = null;
    this.formDirty = false;
    this.notify();
  },

  // ---- Query helpers ----

  getContactById(id) {
    return this.contacts.find(c => c.id === id) || null;
  },

  getContactName(id) {
    const c = this.getContactById(id);
    return c ? c.name : 'Unknown';
  },

  getInvoiceById(id) {
    return this.invoices.find(i => i.id === id) || null;
  },

  getQuoteById(id) {
    return this.quotes.find(q => q.id === id) || null;
  },

  getCreditNoteById(id) {
    return this.creditNotes.find(cn => cn.id === id) || null;
  },

  getRepeatingInvoiceById(id) {
    return this.repeatingInvoices.find(r => r.id === id) || null;
  },

  getItemById(id) {
    return this.items.find(i => i.id === id) || null;
  },

  getTaxRateById(id) {
    return this.taxRates.find(t => t.id === id) || null;
  },

  getAccountById(id) {
    return this.accounts.find(a => a.id === id) || null;
  },

  getBrandingThemeById(id) {
    return this.brandingThemes.find(t => t.id === id) || null;
  },

  getRevenueAccounts() {
    return this.accounts.filter(a => a.type === 'Revenue' || a.type === 'Direct Costs');
  },

  getOutputTaxRates() {
    return this.taxRates.filter(t => t.type === 'output' || t.type === 'none');
  },

  // Filtered invoice lists
  getInvoicesByStatus(status) {
    if (status === 'all') return this.invoices.filter(i => i.status !== 'deleted');
    if (status === 'overdue') {
      const today = new Date().toISOString().split('T')[0];
      return this.invoices.filter(i => i.status === 'awaiting_payment' && i.dueDate < today);
    }
    return this.invoices.filter(i => i.status === status);
  },

  getQuotesByStatus(status) {
    if (status === 'all') return this.quotes.filter(q => q.status !== 'deleted');
    return this.quotes.filter(q => q.status === status);
  },

  getCreditNotesByStatus(status) {
    if (status === 'all') return this.creditNotes.filter(cn => cn.status !== 'deleted');
    return this.creditNotes.filter(cn => cn.status === status);
  },

  // Dashboard stats
  getDashboardStats() {
    const today = new Date().toISOString().split('T')[0];
    const draft = this.invoices.filter(i => i.status === 'draft');
    const awaitingApproval = this.invoices.filter(i => i.status === 'awaiting_approval');
    const awaitingPayment = this.invoices.filter(i => i.status === 'awaiting_payment');
    const overdue = awaitingPayment.filter(i => i.dueDate < today);
    const paid = this.invoices.filter(i => i.status === 'paid');
    const paidLast30 = paid.filter(i => {
      const d = new Date(i.date);
      const ago = new Date();
      ago.setDate(ago.getDate() - 30);
      return d >= ago;
    });

    return {
      draftCount: draft.length,
      draftTotal: draft.reduce((s, i) => s + i.total, 0),
      awaitingApprovalCount: awaitingApproval.length,
      awaitingApprovalTotal: awaitingApproval.reduce((s, i) => s + i.total, 0),
      awaitingPaymentCount: awaitingPayment.length,
      awaitingPaymentTotal: awaitingPayment.reduce((s, i) => s + i.amountDue, 0),
      overdueCount: overdue.length,
      overdueTotal: overdue.reduce((s, i) => s + i.amountDue, 0),
      paidLast30Count: paidLast30.length,
      paidLast30Total: paidLast30.reduce((s, i) => s + i.total, 0),
      totalOutstanding: awaitingPayment.reduce((s, i) => s + i.amountDue, 0),
      totalOverdue: overdue.reduce((s, i) => s + i.amountDue, 0)
    };
  },

  // ---- Mutation methods ----

  generateNextNumber(type) {
    const settings = this.invoiceSettings;
    if (type === 'invoice') {
      const num = this._nextInvoiceNum;
      this._nextInvoiceNum++;
      return settings.invoicePrefix + String(num).padStart(4, '0');
    } else if (type === 'quote') {
      const num = this._nextQuoteNum;
      this._nextQuoteNum++;
      return settings.quotePrefix + String(num).padStart(4, '0');
    } else if (type === 'creditNote') {
      const num = this._nextCreditNoteNum;
      this._nextCreditNoteNum++;
      return settings.creditNotePrefix + String(num).padStart(4, '0');
    }
    return '';
  },

  generateLineItemId() {
    return 'li_' + (this._nextLineItemId++);
  },

  generatePaymentId() {
    return 'pay_' + (this._nextPaymentId++);
  },

  // Invoice mutations
  createInvoice(data) {
    const inv = {
      id: 'inv_' + String(this._nextInvoiceNum).padStart(3, '0'),
      number: this.generateNextNumber('invoice'),
      contactId: data.contactId,
      status: data.status || 'draft',
      date: data.date,
      dueDate: data.dueDate,
      reference: data.reference || '',
      currency: data.currency || 'AUD',
      brandingThemeId: data.brandingThemeId || 'theme_standard',
      taxMode: data.taxMode || this.invoiceSettings.defaultTaxMode,
      lineItems: data.lineItems || [],
      subtotal: data.subtotal || 0,
      taxTotal: data.taxTotal || 0,
      total: data.total || 0,
      amountDue: data.total || 0,
      amountPaid: 0,
      payments: [],
      notes: [{ date: new Date().toISOString(), text: 'Invoice created', user: this.currentUser.name }],
      sentAt: null,
      title: data.title || '',
      summary: data.summary || ''
    };
    this.invoices.push(inv);
    this.notify();
    return inv;
  },

  updateInvoice(id, data) {
    const inv = this.getInvoiceById(id);
    if (!inv) return null;
    Object.assign(inv, data);
    if (data.total !== undefined) {
      inv.amountDue = data.total - inv.amountPaid;
    }
    inv.notes.push({ date: new Date().toISOString(), text: 'Invoice updated', user: this.currentUser.name });
    this.notify();
    return inv;
  },

  approveInvoice(id) {
    const inv = this.getInvoiceById(id);
    if (!inv) return;
    if (inv.status === 'draft' || inv.status === 'awaiting_approval') {
      inv.status = 'awaiting_payment';
      inv.notes.push({ date: new Date().toISOString(), text: 'Invoice approved', user: this.currentUser.name });
      this.notify();
    }
  },

  submitForApproval(id) {
    const inv = this.getInvoiceById(id);
    if (!inv) return;
    if (inv.status === 'draft') {
      inv.status = 'awaiting_approval';
      inv.notes.push({ date: new Date().toISOString(), text: 'Submitted for approval', user: this.currentUser.name });
      this.notify();
    }
  },

  sendInvoice(id) {
    const inv = this.getInvoiceById(id);
    if (!inv) return;
    if (inv.status === 'draft' || inv.status === 'awaiting_approval') {
      inv.status = 'awaiting_payment';
    }
    inv.sentAt = new Date().toISOString();
    inv.notes.push({ date: new Date().toISOString(), text: 'Invoice sent to ' + this.getContactName(inv.contactId), user: this.currentUser.name });
    this.notify();
  },

  markInvoiceSent(id) {
    const inv = this.getInvoiceById(id);
    if (!inv) return;
    if (inv.status === 'draft' || inv.status === 'awaiting_approval') {
      inv.status = 'awaiting_payment';
    }
    inv.sentAt = new Date().toISOString();
    inv.notes.push({ date: new Date().toISOString(), text: 'Marked as sent', user: this.currentUser.name });
    this.notify();
  },

  voidInvoice(id) {
    const inv = this.getInvoiceById(id);
    if (!inv) return;
    inv.status = 'voided';
    inv.amountDue = 0;
    inv.notes.push({ date: new Date().toISOString(), text: 'Invoice voided', user: this.currentUser.name });
    this.notify();
  },

  deleteInvoice(id) {
    const inv = this.getInvoiceById(id);
    if (!inv) return;
    inv.status = 'deleted';
    inv.notes.push({ date: new Date().toISOString(), text: 'Invoice deleted', user: this.currentUser.name });
    this.notify();
  },

  addPayment(invoiceId, payment) {
    const inv = this.getInvoiceById(invoiceId);
    if (!inv) return;
    payment.id = this.generatePaymentId();
    inv.payments.push(payment);
    inv.amountPaid += payment.amount;
    inv.amountDue = inv.total - inv.amountPaid;
    if (inv.amountDue <= 0.005) {
      inv.status = 'paid';
      inv.amountDue = 0;
    }
    inv.notes.push({ date: new Date().toISOString(), text: 'Payment of $' + payment.amount.toFixed(2) + ' recorded', user: this.currentUser.name });
    this.notify();
  },

  removePayment(invoiceId, paymentId) {
    const inv = this.getInvoiceById(invoiceId);
    if (!inv) return;
    const idx = inv.payments.findIndex(p => p.id === paymentId);
    if (idx === -1) return;
    const removed = inv.payments.splice(idx, 1)[0];
    inv.amountPaid -= removed.amount;
    inv.amountDue = inv.total - inv.amountPaid;
    if (inv.status === 'paid') {
      inv.status = 'awaiting_payment';
    }
    inv.notes.push({ date: new Date().toISOString(), text: 'Payment of $' + removed.amount.toFixed(2) + ' removed', user: this.currentUser.name });
    this.notify();
  },

  copyInvoice(id) {
    const src = this.getInvoiceById(id);
    if (!src) return null;
    const copy = JSON.parse(JSON.stringify(src));
    copy.id = 'inv_' + String(this._nextInvoiceNum).padStart(3, '0');
    copy.number = this.generateNextNumber('invoice');
    copy.status = 'draft';
    copy.date = new Date().toISOString().split('T')[0];
    copy.payments = [];
    copy.amountPaid = 0;
    copy.amountDue = copy.total;
    copy.sentAt = null;
    copy.notes = [{ date: new Date().toISOString(), text: 'Copied from ' + src.number, user: this.currentUser.name }];
    copy.lineItems.forEach(li => { li.id = this.generateLineItemId(); });
    this.invoices.push(copy);
    this.notify();
    return copy;
  },

  // Quote mutations
  createQuote(data) {
    const quo = {
      id: 'quo_' + String(this._nextQuoteNum).padStart(3, '0'),
      number: this.generateNextNumber('quote'),
      contactId: data.contactId,
      status: data.status || 'draft',
      date: data.date,
      expiryDate: data.expiryDate,
      reference: data.reference || '',
      currency: data.currency || 'AUD',
      brandingThemeId: data.brandingThemeId || 'theme_standard',
      taxMode: data.taxMode || this.invoiceSettings.defaultTaxMode,
      lineItems: data.lineItems || [],
      subtotal: data.subtotal || 0,
      taxTotal: data.taxTotal || 0,
      total: data.total || 0,
      title: data.title || '',
      summary: data.summary || '',
      terms: data.terms || '',
      notes: [{ date: new Date().toISOString(), text: 'Quote created', user: this.currentUser.name }],
      sentAt: null,
      isInvoiced: false
    };
    this.quotes.push(quo);
    this.notify();
    return quo;
  },

  updateQuote(id, data) {
    const quo = this.getQuoteById(id);
    if (!quo) return null;
    Object.assign(quo, data);
    quo.notes.push({ date: new Date().toISOString(), text: 'Quote updated', user: this.currentUser.name });
    this.notify();
    return quo;
  },

  sendQuote(id) {
    const quo = this.getQuoteById(id);
    if (!quo) return;
    if (quo.status === 'draft') quo.status = 'sent';
    quo.sentAt = new Date().toISOString();
    quo.notes.push({ date: new Date().toISOString(), text: 'Quote sent to ' + this.getContactName(quo.contactId), user: this.currentUser.name });
    this.notify();
  },

  acceptQuote(id) {
    const quo = this.getQuoteById(id);
    if (!quo) return;
    quo.status = 'accepted';
    quo.notes.push({ date: new Date().toISOString(), text: 'Quote accepted', user: this.currentUser.name });
    this.notify();
  },

  declineQuote(id) {
    const quo = this.getQuoteById(id);
    if (!quo) return;
    quo.status = 'declined';
    quo.notes.push({ date: new Date().toISOString(), text: 'Quote declined', user: this.currentUser.name });
    this.notify();
  },

  markQuoteInvoiced(id) {
    const quo = this.getQuoteById(id);
    if (!quo) return;
    quo.isInvoiced = true;
    quo.notes.push({ date: new Date().toISOString(), text: 'Marked as invoiced', user: this.currentUser.name });
    this.notify();
  },

  deleteQuote(id) {
    const quo = this.getQuoteById(id);
    if (!quo) return;
    quo.status = 'deleted';
    quo.notes.push({ date: new Date().toISOString(), text: 'Quote deleted', user: this.currentUser.name });
    this.notify();
  },

  copyQuote(id) {
    const src = this.getQuoteById(id);
    if (!src) return null;
    const copy = JSON.parse(JSON.stringify(src));
    copy.id = 'quo_' + String(this._nextQuoteNum).padStart(3, '0');
    copy.number = this.generateNextNumber('quote');
    copy.status = 'draft';
    copy.date = new Date().toISOString().split('T')[0];
    copy.sentAt = null;
    copy.isInvoiced = false;
    copy.notes = [{ date: new Date().toISOString(), text: 'Copied from ' + src.number, user: this.currentUser.name }];
    copy.lineItems.forEach(li => { li.id = this.generateLineItemId(); });
    this.quotes.push(copy);
    this.notify();
    return copy;
  },

  createInvoiceFromQuote(quoteId) {
    const quo = this.getQuoteById(quoteId);
    if (!quo) return null;
    const invData = {
      contactId: quo.contactId,
      status: 'draft',
      date: new Date().toISOString().split('T')[0],
      dueDate: this._calcDueDate(new Date().toISOString().split('T')[0]),
      reference: quo.reference,
      currency: quo.currency,
      brandingThemeId: quo.brandingThemeId,
      taxMode: quo.taxMode,
      lineItems: JSON.parse(JSON.stringify(quo.lineItems)).map(li => {
        li.id = this.generateLineItemId();
        return li;
      }),
      subtotal: quo.subtotal,
      taxTotal: quo.taxTotal,
      total: quo.total,
      title: quo.title,
      summary: quo.summary
    };
    const inv = this.createInvoice(invData);
    inv.notes.push({ date: new Date().toISOString(), text: 'Created from quote ' + quo.number, user: this.currentUser.name });
    quo.isInvoiced = true;
    quo.notes.push({ date: new Date().toISOString(), text: 'Invoice ' + inv.number + ' created', user: this.currentUser.name });
    this.notify();
    return inv;
  },

  // Credit note mutations
  createCreditNote(data) {
    const cn = {
      id: 'cn_' + String(this._nextCreditNoteNum).padStart(3, '0'),
      number: this.generateNextNumber('creditNote'),
      contactId: data.contactId,
      status: data.status || 'draft',
      date: data.date,
      reference: data.reference || '',
      currency: data.currency || 'AUD',
      brandingThemeId: data.brandingThemeId || 'theme_standard',
      taxMode: data.taxMode || this.invoiceSettings.defaultTaxMode,
      lineItems: data.lineItems || [],
      subtotal: data.subtotal || 0,
      taxTotal: data.taxTotal || 0,
      total: data.total || 0,
      remainingCredit: data.total || 0,
      allocations: [],
      refunds: [],
      notes: [{ date: new Date().toISOString(), text: 'Credit note created', user: this.currentUser.name }]
    };
    this.creditNotes.push(cn);
    this.notify();
    return cn;
  },

  updateCreditNote(id, data) {
    const cn = this.getCreditNoteById(id);
    if (!cn) return null;
    Object.assign(cn, data);
    if (data.total !== undefined) {
      cn.remainingCredit = data.total - cn.allocations.reduce((s, a) => s + a.amount, 0) - cn.refunds.reduce((s, r) => s + r.amount, 0);
    }
    cn.notes.push({ date: new Date().toISOString(), text: 'Credit note updated', user: this.currentUser.name });
    this.notify();
    return cn;
  },

  approveCreditNote(id) {
    const cn = this.getCreditNoteById(id);
    if (!cn) return;
    cn.status = 'awaiting_payment';
    cn.notes.push({ date: new Date().toISOString(), text: 'Credit note approved', user: this.currentUser.name });
    this.notify();
  },

  allocateCreditNote(cnId, invoiceId, amount) {
    const cn = this.getCreditNoteById(cnId);
    const inv = this.getInvoiceById(invoiceId);
    if (!cn || !inv) return;
    cn.allocations.push({ invoiceId: inv.id, invoiceNumber: inv.number, amount: amount, date: new Date().toISOString().split('T')[0] });
    cn.remainingCredit -= amount;
    if (cn.remainingCredit <= 0.005) {
      cn.status = 'paid';
      cn.remainingCredit = 0;
    }
    inv.amountPaid += amount;
    inv.amountDue -= amount;
    if (inv.amountDue <= 0.005) {
      inv.status = 'paid';
      inv.amountDue = 0;
    }
    cn.notes.push({ date: new Date().toISOString(), text: 'Allocated $' + amount.toFixed(2) + ' to ' + inv.number, user: this.currentUser.name });
    inv.notes.push({ date: new Date().toISOString(), text: 'Credit note ' + cn.number + ' applied: $' + amount.toFixed(2), user: this.currentUser.name });
    this.notify();
  },

  deleteCreditNote(id) {
    const cn = this.getCreditNoteById(id);
    if (!cn) return;
    cn.status = 'deleted';
    this.notify();
  },

  // Repeating invoice mutations
  createRepeatingInvoice(data) {
    const ri = {
      id: 'rep_' + String(this._nextRepeatId++).padStart(3, '0'),
      contactId: data.contactId,
      status: data.status || 'draft',
      frequency: data.frequency || 'monthly',
      startDate: data.startDate,
      nextDate: data.nextDate || data.startDate,
      endDate: data.endDate || '',
      currency: data.currency || 'AUD',
      brandingThemeId: data.brandingThemeId || 'theme_standard',
      taxMode: data.taxMode || this.invoiceSettings.defaultTaxMode,
      saveAs: data.saveAs || 'draft',
      lineItems: data.lineItems || [],
      dueDate: data.dueDate || this.invoiceSettings.defaultDueDate,
      reference: data.reference || '',
      emailSubject: data.emailSubject || '',
      emailBody: data.emailBody || ''
    };
    this.repeatingInvoices.push(ri);
    this.notify();
    return ri;
  },

  updateRepeatingInvoice(id, data) {
    const ri = this.getRepeatingInvoiceById(id);
    if (!ri) return null;
    Object.assign(ri, data);
    this.notify();
    return ri;
  },

  deleteRepeatingInvoice(id) {
    const idx = this.repeatingInvoices.findIndex(r => r.id === id);
    if (idx !== -1) {
      this.repeatingInvoices.splice(idx, 1);
      this.notify();
    }
  },

  // Branding theme mutations
  createBrandingTheme(data) {
    const theme = {
      id: 'theme_' + (this._nextThemeId++),
      name: data.name,
      isDefault: false,
      logoUrl: data.logoUrl || '',
      paymentTerms: data.paymentTerms || '',
      termsAndConditions: data.termsAndConditions || '',
      showTaxNumber: data.showTaxNumber !== false,
      showPaymentAdvice: data.showPaymentAdvice !== false
    };
    this.brandingThemes.push(theme);
    this.notify();
    return theme;
  },

  updateBrandingTheme(id, data) {
    const theme = this.getBrandingThemeById(id);
    if (!theme) return null;
    Object.assign(theme, data);
    this.notify();
    return theme;
  },

  setDefaultTheme(id) {
    this.brandingThemes.forEach(t => { t.isDefault = (t.id === id); });
    this.notify();
  },

  deleteBrandingTheme(id) {
    const idx = this.brandingThemes.findIndex(t => t.id === id);
    if (idx !== -1 && !this.brandingThemes[idx].isDefault) {
      this.brandingThemes.splice(idx, 1);
      this.notify();
    }
  },

  // Invoice settings
  updateInvoiceSettings(data) {
    Object.assign(this.invoiceSettings, data);
    this.notify();
  },

  // Reminder mutations
  updateReminder(id, data) {
    const rem = this.invoiceReminders.find(r => r.id === id);
    if (!rem) return;
    Object.assign(rem, data);
    this.notify();
  },

  toggleReminder(id) {
    const rem = this.invoiceReminders.find(r => r.id === id);
    if (!rem) return;
    rem.enabled = !rem.enabled;
    this.notify();
  },

  addReminder(data) {
    const rem = {
      id: 'rem_' + String(this._nextReminderId++).padStart(3, '0'),
      enabled: true,
      timing: data.timing || 'after',
      days: data.days || 7,
      subject: data.subject || '',
      body: data.body || '',
      includeInvoicePdf: data.includeInvoicePdf !== false,
      includeSummary: data.includeSummary !== false
    };
    this.invoiceReminders.push(rem);
    this.notify();
    return rem;
  },

  deleteReminder(id) {
    const idx = this.invoiceReminders.findIndex(r => r.id === id);
    if (idx !== -1) {
      this.invoiceReminders.splice(idx, 1);
      this.notify();
    }
  },

  // Contact mutations
  createContact(data) {
    const con = {
      id: 'con_' + String(this._nextContactId++).padStart(3, '0'),
      name: data.name,
      email: data.email || '',
      phone: data.phone || '',
      contactPerson: data.contactPerson || '',
      address: data.address || '',
      taxNumber: data.taxNumber || '',
      defaultThemeId: 'theme_standard',
      defaultDueDate: this.invoiceSettings.defaultDueDate,
      defaultTaxRateId: 'tax_gst',
      outstandingBalance: 0,
      overdueBalance: 0,
      isCustomer: true,
      isSupplier: false
    };
    this.contacts.push(con);
    this.notify();
    return con;
  },

  updateContact(id, data) {
    const con = this.getContactById(id);
    if (!con) return;
    Object.assign(con, data);
    this.notify();
  },

  // Helper
  _calcDueDate(invoiceDate) {
    const dd = this.invoiceSettings.defaultDueDate;
    const d = new Date(invoiceDate + 'T00:00:00');
    if (dd.type === 'daysAfterInvoice') {
      d.setDate(d.getDate() + dd.days);
    } else if (dd.type === 'endOfFollowingMonth') {
      d.setMonth(d.getMonth() + 2, 0);
    } else if (dd.type === 'endOfCurrentMonth') {
      d.setMonth(d.getMonth() + 1, 0);
    } else if (dd.type === 'daysAfterEndOfMonth') {
      d.setMonth(d.getMonth() + 1, 0);
      d.setDate(d.getDate() + dd.days);
    }
    return d.toISOString().split('T')[0];
  },

  // Search across all transaction types
  search(query) {
    if (!query || query.trim().length === 0) return [];
    const q = query.toLowerCase().trim();
    const results = [];

    this.invoices.forEach(inv => {
      if (inv.status === 'deleted') return;
      const contact = this.getContactById(inv.contactId);
      if (
        inv.number.toLowerCase().includes(q) ||
        (contact && contact.name.toLowerCase().includes(q)) ||
        inv.reference.toLowerCase().includes(q) ||
        String(inv.total).includes(q)
      ) {
        results.push({ type: 'invoice', id: inv.id, number: inv.number, contact: contact ? contact.name : '', date: inv.date, total: inv.total, status: inv.status });
      }
    });

    this.quotes.forEach(quo => {
      if (quo.status === 'deleted') return;
      const contact = this.getContactById(quo.contactId);
      if (
        quo.number.toLowerCase().includes(q) ||
        (contact && contact.name.toLowerCase().includes(q)) ||
        quo.reference.toLowerCase().includes(q) ||
        String(quo.total).includes(q)
      ) {
        results.push({ type: 'quote', id: quo.id, number: quo.number, contact: contact ? contact.name : '', date: quo.date, total: quo.total, status: quo.status });
      }
    });

    this.creditNotes.forEach(cn => {
      if (cn.status === 'deleted') return;
      const contact = this.getContactById(cn.contactId);
      if (
        cn.number.toLowerCase().includes(q) ||
        (contact && contact.name.toLowerCase().includes(q)) ||
        cn.reference.toLowerCase().includes(q) ||
        String(cn.total).includes(q)
      ) {
        results.push({ type: 'creditNote', id: cn.id, number: cn.number, contact: contact ? contact.name : '', date: cn.date, total: cn.total, status: cn.status });
      }
    });

    return results;
  }
};

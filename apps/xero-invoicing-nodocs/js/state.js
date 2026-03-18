/* state.js — Centralized state management for Xero Invoicing */
/* eslint-disable */

const AppState = {
    // ----- Persistent data -----
    contacts: [],
    invoices: [],
    payments: [],
    taxRates: [],
    accountCodes: [],
    bankAccounts: [],
    currencies: [],
    brandingThemes: [],
    settings: {},
    _nextInvoiceId: 114,
    _nextContactId: 26,
    _nextPaymentId: 100,
    _nextLineItemId: 10000,
    _seedVersion: SEED_DATA_VERSION,

    // ----- UI state (not persisted) -----
    currentView: 'invoices',
    currentItemId: null,
    invoiceFilters: { status: '', search: '', dateFrom: '', dateTo: '', contact: '' },
    invoiceSortField: 'issueDate',
    invoiceSortDir: 'desc',
    invoicePage: 1,
    invoicePageSize: 20,
    selectedInvoiceIds: [],
    contactFilters: { search: '' },
    contactPage: 1,
    contactPageSize: 20,

    _subscribers: [],
    _initializing: false,

    // ========== Initialization ==========

    init() {
        this._initializing = true;
        const saved = this._loadPersisted();
        if (saved) {
            this.contacts = saved.contacts || [];
            this.invoices = saved.invoices || [];
            this.payments = saved.payments || [];
            this.taxRates = saved.taxRates || [];
            this.accountCodes = saved.accountCodes || [];
            this.bankAccounts = saved.bankAccounts || [];
            this.currencies = saved.currencies || [];
            this.brandingThemes = saved.brandingThemes || [];
            this.settings = saved.settings || {};
            this._nextInvoiceId = saved._nextInvoiceId || 114;
            this._nextContactId = saved._nextContactId || 26;
            this._nextPaymentId = saved._nextPaymentId || 100;
            this._nextLineItemId = saved._nextLineItemId || 10000;
        } else {
            this._loadSeedData();
        }
        this._initializing = false;
        this._pushStateToServer();
    },

    _loadSeedData() {
        this.contacts = JSON.parse(JSON.stringify(CONTACTS));
        this.invoices = JSON.parse(JSON.stringify(INVOICES));
        this.payments = JSON.parse(JSON.stringify(PAYMENTS));
        this.taxRates = JSON.parse(JSON.stringify(TAX_RATES));
        this.accountCodes = JSON.parse(JSON.stringify(ACCOUNT_CODES));
        this.bankAccounts = JSON.parse(JSON.stringify(BANK_ACCOUNTS));
        this.currencies = JSON.parse(JSON.stringify(CURRENCIES));
        this.brandingThemes = JSON.parse(JSON.stringify(BRANDING_THEMES));
        this.settings = JSON.parse(JSON.stringify(DEFAULT_SETTINGS));
        this._nextInvoiceId = 114;
        this._nextContactId = 26;
        this._nextPaymentId = this.payments.length + 1;
        this._nextLineItemId = 10000;
        this._seedVersion = SEED_DATA_VERSION;
    },

    resetToSeedData() {
        this._loadSeedData();
        localStorage.removeItem('xeroInvoicingState');
        this.currentView = 'invoices';
        this.currentItemId = null;
        this.invoiceFilters = { status: '', search: '', dateFrom: '', dateTo: '', contact: '' };
        this.invoiceSortField = 'issueDate';
        this.invoiceSortDir = 'desc';
        this.invoicePage = 1;
        this.selectedInvoiceIds = [];
        this._pushStateToServer();
        this._notifySubscribers();
    },

    // ========== Persistence ==========

    _loadPersisted() {
        try {
            const raw = localStorage.getItem('xeroInvoicingState');
            if (!raw) return null;
            const parsed = JSON.parse(raw);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('xeroInvoicingState');
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    },

    _persist() {
        const data = {
            contacts: this.contacts,
            invoices: this.invoices,
            payments: this.payments,
            taxRates: this.taxRates,
            accountCodes: this.accountCodes,
            bankAccounts: this.bankAccounts,
            currencies: this.currencies,
            brandingThemes: this.brandingThemes,
            settings: this.settings,
            _nextInvoiceId: this._nextInvoiceId,
            _nextContactId: this._nextContactId,
            _nextPaymentId: this._nextPaymentId,
            _nextLineItemId: this._nextLineItemId,
            _seedVersion: this._seedVersion,
        };
        localStorage.setItem('xeroInvoicingState', JSON.stringify(data));
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
            contacts: this.contacts,
            invoices: this.invoices,
            payments: this.payments,
            taxRates: this.taxRates,
            accountCodes: this.accountCodes,
            bankAccounts: this.bankAccounts,
            currencies: this.currencies,
            brandingThemes: this.brandingThemes,
            settings: this.settings,
            _nextInvoiceId: this._nextInvoiceId,
            _nextContactId: this._nextContactId,
            _nextPaymentId: this._nextPaymentId,
            _nextLineItemId: this._nextLineItemId,
            _seedVersion: this._seedVersion,
        };
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        this._notifySubscribers();
    },

    subscribe(fn) {
        this._subscribers.push(fn);
    },

    _notifySubscribers() {
        this._subscribers.forEach(fn => fn());
    },

    // ========== Getters ==========

    getContactById(id) {
        return this.contacts.find(c => c.id === id) || null;
    },

    getContactName(contactId) {
        const c = this.getContactById(contactId);
        return c ? c.name : 'Unknown';
    },

    getInvoiceById(id) {
        return this.invoices.find(inv => inv.id === id) || null;
    },

    getPaymentsForInvoice(invoiceId) {
        return this.payments.filter(p => p.invoiceId === invoiceId);
    },

    getTaxRateById(id) {
        return this.taxRates.find(t => t.id === id) || null;
    },

    getAccountByCode(code) {
        return this.accountCodes.find(a => a.code === code) || null;
    },

    getBankAccountById(id) {
        return this.bankAccounts.find(b => b.id === id) || null;
    },

    getBrandingThemeById(id) {
        return this.brandingThemes.find(b => b.id === id) || null;
    },

    getCurrencyByCode(code) {
        return this.currencies.find(c => c.code === code) || null;
    },

    getContactOutstandingBalance(contactId) {
        return this.invoices
            .filter(inv => inv.contactId === contactId && (inv.status === 'awaiting_payment' || inv.status === 'overdue'))
            .reduce((sum, inv) => sum + inv.amountDue, 0);
    },

    // ========== Filtered/Sorted Invoices ==========

    getFilteredInvoices() {
        let result = [...this.invoices];
        const f = this.invoiceFilters;

        if (f.status) {
            result = result.filter(inv => inv.status === f.status);
        }
        if (f.contact) {
            result = result.filter(inv => inv.contactId === f.contact);
        }
        if (f.dateFrom) {
            result = result.filter(inv => inv.issueDate >= f.dateFrom);
        }
        if (f.dateTo) {
            result = result.filter(inv => inv.issueDate <= f.dateTo);
        }
        if (f.search) {
            const q = f.search.toLowerCase();
            result = result.filter(inv => {
                const contact = this.getContactById(inv.contactId);
                return inv.invoiceNumber.toLowerCase().includes(q) ||
                    (inv.reference && inv.reference.toLowerCase().includes(q)) ||
                    (contact && contact.name.toLowerCase().includes(q));
            });
        }

        // Sort
        const dir = this.invoiceSortDir === 'asc' ? 1 : -1;
        const field = this.invoiceSortField;
        result.sort((a, b) => {
            let va = a[field];
            let vb = b[field];
            if (field === 'contactName') {
                va = this.getContactName(a.contactId);
                vb = this.getContactName(b.contactId);
            }
            if (va == null) va = '';
            if (vb == null) vb = '';
            if (typeof va === 'number' && typeof vb === 'number') return (va - vb) * dir;
            return String(va).localeCompare(String(vb)) * dir;
        });

        return result;
    },

    getPagedInvoices() {
        const all = this.getFilteredInvoices();
        const start = (this.invoicePage - 1) * this.invoicePageSize;
        return {
            items: all.slice(start, start + this.invoicePageSize),
            total: all.length,
            page: this.invoicePage,
            pageSize: this.invoicePageSize,
            totalPages: Math.ceil(all.length / this.invoicePageSize)
        };
    },

    getFilteredContacts() {
        let result = [...this.contacts];
        const q = this.contactFilters.search;
        if (q) {
            const lq = q.toLowerCase();
            result = result.filter(c =>
                c.name.toLowerCase().includes(lq) ||
                c.email.toLowerCase().includes(lq) ||
                (c.phone && c.phone.includes(lq))
            );
        }
        result.sort((a, b) => a.name.localeCompare(b.name));
        return result;
    },

    getPagedContacts() {
        const all = this.getFilteredContacts();
        const start = (this.contactPage - 1) * this.contactPageSize;
        return {
            items: all.slice(start, start + this.contactPageSize),
            total: all.length,
            page: this.contactPage,
            pageSize: this.contactPageSize,
            totalPages: Math.ceil(all.length / this.contactPageSize)
        };
    },

    // ========== Dashboard stats ==========

    getDashboardStats() {
        const now = new Date();
        const active = this.invoices.filter(inv => inv.status !== 'voided' && inv.status !== 'draft');
        const outstanding = this.invoices.filter(inv => inv.status === 'awaiting_payment' || inv.status === 'overdue');
        const overdue = this.invoices.filter(inv => inv.status === 'overdue');
        const paid = this.invoices.filter(inv => inv.status === 'paid');

        const totalInvoiced = active.reduce((s, inv) => s + inv.total, 0);
        const totalOutstanding = outstanding.reduce((s, inv) => s + inv.amountDue, 0);
        const totalOverdue = overdue.reduce((s, inv) => s + inv.amountDue, 0);
        const totalPaid = paid.reduce((s, inv) => s + inv.total, 0);

        // Aging buckets
        const aging = { current: 0, days1_30: 0, days31_60: 0, days61_90: 0, days90plus: 0 };
        outstanding.forEach(inv => {
            const due = new Date(inv.dueDate);
            const daysPast = Math.floor((now - due) / 86400000);
            if (daysPast <= 0) aging.current += inv.amountDue;
            else if (daysPast <= 30) aging.days1_30 += inv.amountDue;
            else if (daysPast <= 60) aging.days31_60 += inv.amountDue;
            else if (daysPast <= 90) aging.days61_90 += inv.amountDue;
            else aging.days90plus += inv.amountDue;
        });

        return {
            totalInvoiced: Math.round(totalInvoiced * 100) / 100,
            totalOutstanding: Math.round(totalOutstanding * 100) / 100,
            totalOverdue: Math.round(totalOverdue * 100) / 100,
            totalPaid: Math.round(totalPaid * 100) / 100,
            invoiceCount: this.invoices.length,
            outstandingCount: outstanding.length,
            overdueCount: overdue.length,
            paidCount: paid.length,
            draftCount: this.invoices.filter(inv => inv.status === 'draft').length,
            aging: {
                current: Math.round(aging.current * 100) / 100,
                days1_30: Math.round(aging.days1_30 * 100) / 100,
                days31_60: Math.round(aging.days31_60 * 100) / 100,
                days61_90: Math.round(aging.days61_90 * 100) / 100,
                days90plus: Math.round(aging.days90plus * 100) / 100,
            }
        };
    },

    // ========== Invoice Mutations ==========

    createInvoice(data) {
        const id = 'inv_' + this._nextInvoiceId++;
        const num = this.settings.invoiceNumberPrefix + String(this.settings.invoiceNumberNextNumber).padStart(this.settings.invoiceNumberPadding, '0');
        this.settings.invoiceNumberNextNumber++;

        // Calculate totals
        let subtotal = 0;
        let taxTotal = 0;
        const lineItems = (data.lineItems || []).map(li => {
            const lt = Math.round(li.quantity * li.unitPrice * 100) / 100;
            subtotal += lt;
            const rate = this.getTaxRateById(li.taxRateId);
            if (rate) taxTotal += lt * (rate.rate / 100);
            return {
                id: 'li_' + this._nextLineItemId++,
                description: li.description || '',
                quantity: li.quantity || 0,
                unitPrice: li.unitPrice || 0,
                taxRateId: li.taxRateId || 'tax_1',
                accountCode: li.accountCode || '200',
                lineTotal: lt
            };
        });
        subtotal = Math.round(subtotal * 100) / 100;
        taxTotal = Math.round(taxTotal * 100) / 100;
        const total = Math.round((subtotal + taxTotal) * 100) / 100;

        const now = new Date().toISOString();
        const invoice = {
            id: id,
            invoiceNumber: data.invoiceNumber || num,
            reference: data.reference || '',
            contactId: data.contactId || '',
            status: data.status || 'draft',
            issueDate: data.issueDate || new Date().toISOString().split('T')[0],
            dueDate: data.dueDate || '',
            currency: data.currency || 'NZD',
            lineItems: lineItems,
            subtotal: subtotal,
            taxTotal: taxTotal,
            total: total,
            amountPaid: 0,
            amountDue: total,
            notes: data.notes || '',
            brandingThemeId: data.brandingThemeId || this.settings.defaultBrandingThemeId,
            createdAt: now,
            updatedAt: now,
            sentAt: null,
            paidAt: null,
            voidedAt: null,
            activity: [{ type: 'created', date: now, user: 'System', detail: 'Invoice created' }]
        };

        if (data.status === 'awaiting_approval' || data.status === 'awaiting_payment') {
            invoice.activity.push({ type: 'approved', date: now, user: 'System', detail: 'Invoice approved' });
        }

        this.invoices.push(invoice);
        this.notify();
        return invoice;
    },

    updateInvoice(id, updates) {
        const inv = this.getInvoiceById(id);
        if (!inv) return null;

        if (updates.lineItems) {
            let subtotal = 0;
            let taxTotal = 0;
            updates.lineItems = updates.lineItems.map(li => {
                const lt = Math.round((li.quantity || 0) * (li.unitPrice || 0) * 100) / 100;
                subtotal += lt;
                const rate = this.getTaxRateById(li.taxRateId || 'tax_1');
                if (rate) taxTotal += lt * (rate.rate / 100);
                return {
                    id: li.id || ('li_' + this._nextLineItemId++),
                    description: li.description || '',
                    quantity: li.quantity || 0,
                    unitPrice: li.unitPrice || 0,
                    taxRateId: li.taxRateId || 'tax_1',
                    accountCode: li.accountCode || '200',
                    lineTotal: lt
                };
            });
            subtotal = Math.round(subtotal * 100) / 100;
            taxTotal = Math.round(taxTotal * 100) / 100;
            const total = Math.round((subtotal + taxTotal) * 100) / 100;
            updates.subtotal = subtotal;
            updates.taxTotal = taxTotal;
            updates.total = total;
            updates.amountDue = Math.round((total - inv.amountPaid) * 100) / 100;
        }

        Object.assign(inv, updates);
        inv.updatedAt = new Date().toISOString();
        this.notify();
        return inv;
    },

    deleteInvoice(id) {
        const idx = this.invoices.findIndex(inv => inv.id === id);
        if (idx === -1) return false;
        this.invoices.splice(idx, 1);
        this.payments = this.payments.filter(p => p.invoiceId !== id);
        this.notify();
        return true;
    },

    approveInvoice(id) {
        const inv = this.getInvoiceById(id);
        if (!inv || (inv.status !== 'draft' && inv.status !== 'awaiting_approval')) return false;
        inv.status = 'awaiting_payment';
        inv.updatedAt = new Date().toISOString();
        inv.activity.push({ type: 'approved', date: new Date().toISOString(), user: 'System', detail: 'Invoice approved' });
        this.notify();
        return true;
    },

    sendInvoice(id) {
        const inv = this.getInvoiceById(id);
        if (!inv) return false;
        if (inv.status === 'draft') {
            inv.status = 'awaiting_payment';
            inv.activity.push({ type: 'approved', date: new Date().toISOString(), user: 'System', detail: 'Invoice approved' });
        }
        inv.sentAt = new Date().toISOString();
        inv.updatedAt = new Date().toISOString();
        const contact = this.getContactById(inv.contactId);
        inv.activity.push({ type: 'sent', date: inv.sentAt, user: 'System', detail: 'Email sent to ' + (contact ? contact.email : 'contact') });
        this.notify();
        return true;
    },

    markAsSent(id) {
        const inv = this.getInvoiceById(id);
        if (!inv) return false;
        if (inv.status === 'draft' || inv.status === 'awaiting_approval') {
            inv.status = 'awaiting_payment';
        }
        inv.sentAt = inv.sentAt || new Date().toISOString();
        inv.updatedAt = new Date().toISOString();
        inv.activity.push({ type: 'marked_sent', date: new Date().toISOString(), user: 'System', detail: 'Invoice marked as sent' });
        this.notify();
        return true;
    },

    voidInvoice(id) {
        const inv = this.getInvoiceById(id);
        if (!inv || inv.status === 'voided') return false;
        inv.status = 'voided';
        inv.voidedAt = new Date().toISOString();
        inv.updatedAt = new Date().toISOString();
        inv.activity.push({ type: 'voided', date: inv.voidedAt, user: 'System', detail: 'Invoice voided' });
        this.notify();
        return true;
    },

    copyInvoice(id) {
        const source = this.getInvoiceById(id);
        if (!source) return null;
        const data = {
            contactId: source.contactId,
            reference: source.reference ? source.reference + ' (copy)' : '',
            currency: source.currency,
            lineItems: source.lineItems.map(li => ({
                description: li.description,
                quantity: li.quantity,
                unitPrice: li.unitPrice,
                taxRateId: li.taxRateId,
                accountCode: li.accountCode
            })),
            notes: source.notes,
            brandingThemeId: source.brandingThemeId,
            issueDate: new Date().toISOString().split('T')[0],
            dueDate: '',
            status: 'draft'
        };
        return this.createInvoice(data);
    },

    // ========== Payment Mutations ==========

    addPayment(invoiceId, paymentData) {
        const inv = this.getInvoiceById(invoiceId);
        if (!inv) return null;

        const payment = {
            id: 'pay_' + this._nextPaymentId++,
            invoiceId: invoiceId,
            date: paymentData.date || new Date().toISOString().split('T')[0],
            amount: paymentData.amount || 0,
            bankAccountId: paymentData.bankAccountId || 'bank_1',
            reference: paymentData.reference || '',
            note: paymentData.note || '',
            exchangeRate: paymentData.exchangeRate || 1
        };

        this.payments.push(payment);

        inv.amountPaid = Math.round((inv.amountPaid + payment.amount) * 100) / 100;
        inv.amountDue = Math.round((inv.total - inv.amountPaid) * 100) / 100;

        if (inv.amountDue <= 0.005) {
            inv.status = 'paid';
            inv.paidAt = new Date().toISOString();
            inv.amountDue = 0;
        }

        inv.updatedAt = new Date().toISOString();
        inv.activity.push({
            type: 'payment',
            date: new Date().toISOString(),
            user: 'System',
            detail: 'Payment of $' + payment.amount.toFixed(2) + ' received'
        });

        this.notify();
        return payment;
    },

    deletePayment(paymentId) {
        const payIdx = this.payments.findIndex(p => p.id === paymentId);
        if (payIdx === -1) return false;
        const payment = this.payments[payIdx];
        const inv = this.getInvoiceById(payment.invoiceId);

        this.payments.splice(payIdx, 1);

        if (inv) {
            inv.amountPaid = Math.round((inv.amountPaid - payment.amount) * 100) / 100;
            if (inv.amountPaid < 0) inv.amountPaid = 0;
            inv.amountDue = Math.round((inv.total - inv.amountPaid) * 100) / 100;
            if (inv.status === 'paid') {
                inv.status = 'awaiting_payment';
                inv.paidAt = null;
            }
            inv.updatedAt = new Date().toISOString();
        }

        this.notify();
        return true;
    },

    // ========== Contact Mutations ==========

    createContact(data) {
        const id = 'con_' + this._nextContactId++;
        const contact = {
            id: id,
            name: data.name || '',
            email: data.email || '',
            phone: data.phone || '',
            billingAddress: data.billingAddress || { street: '', city: '', region: '', postalCode: '', country: 'New Zealand' },
            taxId: data.taxId || '',
            contactType: data.contactType || 'customer',
            createdAt: new Date().toISOString()
        };
        this.contacts.push(contact);
        this.notify();
        return contact;
    },

    updateContact(id, updates) {
        const contact = this.getContactById(id);
        if (!contact) return null;
        Object.assign(contact, updates);
        this.notify();
        return contact;
    },

    deleteContact(id) {
        const hasInvoices = this.invoices.some(inv => inv.contactId === id);
        if (hasInvoices) return false;
        const idx = this.contacts.findIndex(c => c.id === id);
        if (idx === -1) return false;
        this.contacts.splice(idx, 1);
        this.notify();
        return true;
    },

    // ========== Settings Mutations ==========

    updateSettings(updates) {
        Object.assign(this.settings, updates);
        this.notify();
    },

    // ========== Bulk Actions ==========

    bulkApprove(invoiceIds) {
        let count = 0;
        invoiceIds.forEach(id => {
            const inv = this.getInvoiceById(id);
            if (inv && (inv.status === 'draft' || inv.status === 'awaiting_approval')) {
                inv.status = 'awaiting_payment';
                inv.updatedAt = new Date().toISOString();
                inv.activity.push({ type: 'approved', date: new Date().toISOString(), user: 'System', detail: 'Invoice approved (bulk)' });
                count++;
            }
        });
        if (count > 0) this.notify();
        return count;
    },

    bulkSend(invoiceIds) {
        let count = 0;
        invoiceIds.forEach(id => {
            if (this.sendInvoice(id)) count++;
        });
        return count;
    },

    bulkDelete(invoiceIds) {
        let count = 0;
        invoiceIds.forEach(id => {
            const inv = this.getInvoiceById(id);
            if (inv && inv.status === 'draft') {
                if (this.deleteInvoice(id)) count++;
            }
        });
        return count;
    },

    // ========== Next Invoice Number Preview ==========

    getNextInvoiceNumber() {
        return this.settings.invoiceNumberPrefix + String(this.settings.invoiceNumberNextNumber).padStart(this.settings.invoiceNumberPadding, '0');
    },
};

/* app.js — Router, event delegation, and lifecycle for Xero Invoicing */
/* eslint-disable */

const App = {
    _openDropdown: null,
    _currentPaymentInvoiceId: null,
    _currentEditContactId: null,
    _lineItems: [],

    init() {
        AppState.init();
        this._setupSSE();
        AppState.subscribe(() => this.render());
        this._parseRoute();
        this.render();
        window.addEventListener('hashchange', () => { this._parseRoute(); this.render(); });
        document.addEventListener('click', (e) => this._handleClick(e));
        document.addEventListener('input', (e) => this._handleInput(e));
        document.addEventListener('change', (e) => this._handleChange(e));
    },

    _setupSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = (e) => {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
                window.location.hash = '#/invoices';
            }
        };
    },

    _parseRoute() {
        const hash = window.location.hash.replace('#/', '') || 'dashboard';
        const parts = hash.split('/');
        const view = parts[0];
        const id = parts[1] || null;

        if (view === 'invoices' && id) {
            AppState.currentView = 'invoice-detail';
            AppState.currentItemId = id;
        } else if (view === 'invoices') {
            AppState.currentView = 'invoices';
            AppState.currentItemId = null;
        } else if (view === 'new-invoice') {
            AppState.currentView = 'new-invoice';
            AppState.currentItemId = null;
        } else if (view === 'edit-invoice') {
            AppState.currentView = 'edit-invoice';
            AppState.currentItemId = id;
        } else if (view === 'contacts' && id) {
            AppState.currentView = 'contact-detail';
            AppState.currentItemId = id;
        } else if (view === 'contacts') {
            AppState.currentView = 'contacts';
            AppState.currentItemId = null;
        } else if (view === 'settings') {
            AppState.currentView = 'settings';
            AppState.currentItemId = null;
        } else if (view === 'dashboard') {
            AppState.currentView = 'dashboard';
            AppState.currentItemId = null;
        } else {
            AppState.currentView = 'dashboard';
            AppState.currentItemId = null;
        }
    },

    navigate(route) {
        window.location.hash = '#/' + route;
    },

    render() {
        document.getElementById('sidebarNav').innerHTML = Views.renderSidebar();
        document.getElementById('contentWrapper').innerHTML = Views.renderContent();

        // After rendering invoice form, capture line items state
        if (AppState.currentView === 'new-invoice' || AppState.currentView === 'edit-invoice') {
            this._captureLineItems();
        }
    },

    // ========== Click Handling ==========

    _handleClick(e) {
        const target = e.target;

        // Close open dropdowns on outside click
        if (this._openDropdown) {
            const dd = document.getElementById(this._openDropdown);
            if (dd && !dd.contains(target)) {
                const menu = document.getElementById(this._openDropdown + '-menu');
                if (menu) menu.style.display = 'none';
                this._openDropdown = null;
            }
        }

        // Route links
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            e.preventDefault();
            this.navigate(routeEl.dataset.route);
            return;
        }

        // Actions
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            this._handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // Dropdown triggers
        const triggerEl = target.closest('[data-dropdown-trigger]');
        if (triggerEl) {
            e.preventDefault();
            e.stopPropagation();
            const ddId = triggerEl.dataset.dropdownTrigger;
            this._toggleDropdown(ddId);
            return;
        }

        // Dropdown items
        const ddItemEl = target.closest('[data-dropdown-item]');
        if (ddItemEl) {
            e.preventDefault();
            e.stopPropagation();
            this._handleDropdownSelect(ddItemEl);
            return;
        }

        // Modal overlay click to close
        if (target.id === 'modalOverlay') {
            Components.closeModal();
            return;
        }
    },

    _toggleDropdown(ddId) {
        const menuId = ddId + '-menu';
        const menu = document.getElementById(menuId);
        if (!menu) return;

        if (this._openDropdown && this._openDropdown !== ddId) {
            const prev = document.getElementById(this._openDropdown + '-menu');
            if (prev) prev.style.display = 'none';
        }

        if (menu.style.display === 'none') {
            menu.style.display = 'block';
            this._openDropdown = ddId;
        } else {
            menu.style.display = 'none';
            this._openDropdown = null;
        }
    },

    _handleDropdownSelect(el) {
        const ddId = el.dataset.dropdownItem;
        const value = el.dataset.value;
        const label = el.textContent;

        // Update trigger display text
        const dropdown = document.getElementById(ddId);
        if (dropdown) {
            const textEl = dropdown.querySelector('.dropdown-text');
            if (textEl) textEl.textContent = label;
            const searchEl = dropdown.querySelector('.dropdown-search-input');
            if (searchEl) searchEl.value = label;

            // Update selected state
            dropdown.querySelectorAll('.dropdown-item').forEach(item => item.classList.remove('selected'));
            el.classList.add('selected');
        }

        // Close menu
        const menu = document.getElementById(ddId + '-menu');
        if (menu) menu.style.display = 'none';
        this._openDropdown = null;

        // Handle specific dropdowns
        if (ddId === 'filter-status') {
            AppState.invoiceFilters.status = value;
            AppState.invoicePage = 1;
            this.render();
        } else if (ddId === 'filter-contact') {
            AppState.invoiceFilters.contact = value;
            AppState.invoicePage = 1;
            this.render();
        } else if (ddId === 'settings-due-terms') {
            // handled on save
        } else if (ddId === 'settings-tax-rate') {
            // handled on save
        } else if (ddId === 'settings-branding-theme') {
            // handled on save
        } else if (ddId === 'settings-penalty-freq') {
            // handled on save
        } else if (ddId.startsWith('line-tax-') || ddId.startsWith('line-acc-')) {
            // Line item dropdown changed - recalculate
            this._captureLineItems();
            this._updateFormTotals();
        }
    },

    // ========== Action Handling ==========

    _handleAction(action, el) {
        switch (action) {
            case 'new-invoice':
                this.navigate('new-invoice');
                break;
            case 'edit-invoice':
                this.navigate('edit-invoice/' + el.dataset.id);
                break;
            case 'save-invoice-draft':
                this._saveInvoice('draft');
                break;
            case 'save-invoice-approve':
                this._saveInvoice('awaiting_payment');
                break;
            case 'approve-invoice':
                AppState.approveInvoice(el.dataset.id);
                Components.showToast('Invoice approved');
                break;
            case 'send-invoice':
                AppState.sendInvoice(el.dataset.id);
                Components.showToast('Invoice sent');
                break;
            case 'mark-sent':
                AppState.markAsSent(el.dataset.id);
                Components.showToast('Invoice marked as sent');
                break;
            case 'void-invoice':
                Components.confirm('Are you sure you want to void this invoice? This cannot be undone.', () => {
                    AppState.voidInvoice(el.dataset.id);
                    Components.showToast('Invoice voided');
                    Components.closeModal();
                });
                break;
            case 'delete-invoice':
                Components.confirmDanger('Are you sure you want to delete this draft invoice?', () => {
                    AppState.deleteInvoice(el.dataset.id);
                    this.navigate('invoices');
                    Components.showToast('Invoice deleted');
                    Components.closeModal();
                });
                break;
            case 'copy-invoice':
                var newInv = AppState.copyInvoice(el.dataset.id);
                if (newInv) {
                    this.navigate('edit-invoice/' + newInv.id);
                    Components.showToast('Invoice copied');
                }
                break;
            case 'add-payment':
                this._showPaymentModal(el.dataset.id);
                break;
            case 'save-payment':
                this._savePayment();
                break;
            case 'delete-payment':
                Components.confirmDanger('Remove this payment?', () => {
                    AppState.deletePayment(el.dataset.id);
                    Components.showToast('Payment removed');
                    Components.closeModal();
                });
                break;
            case 'add-line-item':
                this._addLineItem();
                break;
            case 'remove-line-item':
                this._removeLineItem(parseInt(el.dataset.idx));
                break;
            case 'sort-invoices':
                this._sortInvoices(el.dataset.field);
                break;
            case 'toggle-select-all':
                this._toggleSelectAll();
                break;
            case 'toggle-select-invoice':
                this._toggleSelectInvoice(el.dataset.id);
                break;
            case 'clear-selection':
                AppState.selectedInvoiceIds = [];
                this.render();
                break;
            case 'bulk-approve':
                var count = AppState.bulkApprove(AppState.selectedInvoiceIds);
                AppState.selectedInvoiceIds = [];
                Components.showToast(count + ' invoice(s) approved');
                break;
            case 'bulk-send':
                var count2 = AppState.bulkSend(AppState.selectedInvoiceIds);
                AppState.selectedInvoiceIds = [];
                Components.showToast(count2 + ' invoice(s) sent');
                break;
            case 'bulk-delete':
                Components.confirmDanger('Delete selected draft invoices?', () => {
                    var count3 = AppState.bulkDelete(AppState.selectedInvoiceIds);
                    AppState.selectedInvoiceIds = [];
                    Components.showToast(count3 + ' draft(s) deleted');
                    Components.closeModal();
                });
                break;
            case 'prev-page':
                if (AppState.currentView === 'invoices' || AppState.currentView === 'invoice-detail') {
                    if (AppState.invoicePage > 1) { AppState.invoicePage--; this.render(); }
                } else if (AppState.currentView === 'contacts') {
                    if (AppState.contactPage > 1) { AppState.contactPage--; this.render(); }
                }
                break;
            case 'next-page':
                if (AppState.currentView === 'invoices') {
                    const maxP = Math.ceil(AppState.getFilteredInvoices().length / AppState.invoicePageSize);
                    if (AppState.invoicePage < maxP) { AppState.invoicePage++; this.render(); }
                } else if (AppState.currentView === 'contacts') {
                    const maxPC = Math.ceil(AppState.getFilteredContacts().length / AppState.contactPageSize);
                    if (AppState.contactPage < maxPC) { AppState.contactPage++; this.render(); }
                }
                break;
            case 'goto-page':
                var page = parseInt(el.dataset.page);
                if (AppState.currentView === 'invoices') {
                    AppState.invoicePage = page;
                } else if (AppState.currentView === 'contacts') {
                    AppState.contactPage = page;
                }
                this.render();
                break;
            case 'new-contact':
                this._showContactModal(null);
                break;
            case 'edit-contact':
                this._showContactModal(el.dataset.id);
                break;
            case 'save-contact':
                this._saveContact();
                break;
            case 'delete-contact':
                Components.confirmDanger('Delete this contact? This cannot be undone.', () => {
                    if (AppState.deleteContact(el.dataset.id)) {
                        this.navigate('contacts');
                        Components.showToast('Contact deleted');
                    } else {
                        Components.showToast('Cannot delete: contact has invoices');
                    }
                    Components.closeModal();
                });
                break;
            case 'quick-add-contact':
                this._showContactModal(null, true);
                break;
            case 'save-settings':
                this._saveSettings();
                break;
            case 'close-modal':
                Components.closeModal();
                break;
            case 'confirm-modal':
                if (Components._confirmCallback) {
                    Components._confirmCallback();
                    Components._confirmCallback = null;
                }
                break;
        }
    },

    // ========== Input Handling ==========

    _handleInput(e) {
        const target = e.target;
        const id = target.id;

        // Invoice filters
        if (id === 'filter-search') {
            AppState.invoiceFilters.search = target.value;
            AppState.invoicePage = 1;
            this.render();
            // Re-focus the search input after render
            const el = document.getElementById('filter-search');
            if (el) { el.focus(); el.selectionStart = el.selectionEnd = target.value.length; }
            return;
        }
        if (id === 'filter-date-from') {
            AppState.invoiceFilters.dateFrom = target.value;
            AppState.invoicePage = 1;
            this.render();
            const el = document.getElementById('filter-date-from');
            if (el) { el.focus(); el.selectionStart = el.selectionEnd = target.value.length; }
            return;
        }
        if (id === 'filter-date-to') {
            AppState.invoiceFilters.dateTo = target.value;
            AppState.invoicePage = 1;
            this.render();
            const el = document.getElementById('filter-date-to');
            if (el) { el.focus(); el.selectionStart = el.selectionEnd = target.value.length; }
            return;
        }
        if (id === 'contact-search') {
            AppState.contactFilters.search = target.value;
            AppState.contactPage = 1;
            this.render();
            const el = document.getElementById('contact-search');
            if (el) { el.focus(); el.selectionStart = el.selectionEnd = target.value.length; }
            return;
        }

        // Line item fields - recalculate on input
        if (target.dataset.lineField) {
            this._onLineItemInput(target);
            return;
        }

        // Searchable dropdown input
        if (target.dataset.dropdownSearch) {
            const ddId = target.dataset.dropdownSearch;
            const menu = document.getElementById(ddId + '-menu');
            if (menu) {
                menu.style.display = 'block';
                this._openDropdown = ddId;
                const query = target.value.toLowerCase();
                menu.querySelectorAll('.dropdown-item').forEach(item => {
                    const text = item.textContent.toLowerCase();
                    item.style.display = text.includes(query) ? '' : 'none';
                });
            }
            return;
        }
    },

    _handleChange(e) {
        const target = e.target;

        // Toggle switches
        if (target.dataset.toggle) {
            if (target.dataset.toggle === 'settings-penalty-enabled') {
                const details = document.getElementById('penalty-details');
                if (details) details.style.display = target.checked ? '' : 'none';
            }
        }
    },

    // ========== Line Items Management ==========

    _captureLineItems() {
        const rows = document.querySelectorAll('.line-item-row');
        this._lineItems = [];
        rows.forEach((row, idx) => {
            const desc = row.querySelector('[data-line-field="description"]');
            const qty = row.querySelector('[data-line-field="quantity"]');
            const price = row.querySelector('[data-line-field="unitPrice"]');
            const taxDd = document.getElementById('line-tax-' + idx);
            const accDd = document.getElementById('line-acc-' + idx);

            const taxSelected = taxDd ? taxDd.querySelector('.dropdown-item.selected') : null;
            const accSelected = accDd ? accDd.querySelector('.dropdown-item.selected') : null;

            const q = parseFloat(qty ? qty.value : 0) || 0;
            const p = parseFloat(price ? price.value : 0) || 0;
            const lt = Math.round(q * p * 100) / 100;

            this._lineItems.push({
                description: desc ? desc.value : '',
                quantity: q,
                unitPrice: p,
                taxRateId: taxSelected ? taxSelected.dataset.value : 'tax_1',
                accountCode: accSelected ? accSelected.dataset.value : '200',
                lineTotal: lt
            });
        });
    },

    _onLineItemInput(target) {
        const row = target.closest('.line-item-row');
        if (!row) return;

        const qty = row.querySelector('[data-line-field="quantity"]');
        const price = row.querySelector('[data-line-field="unitPrice"]');
        const q = parseFloat(qty ? qty.value : 0) || 0;
        const p = parseFloat(price ? price.value : 0) || 0;
        const lt = Math.round(q * p * 100) / 100;

        const totalEl = row.querySelector('.line-total');
        if (totalEl) totalEl.textContent = Components.formatCurrency(lt);

        this._captureLineItems();
        this._updateFormTotals();
    },

    _updateFormTotals() {
        let subtotal = 0;
        let taxTotal = 0;
        this._lineItems.forEach(li => {
            subtotal += li.lineTotal;
            const rate = AppState.getTaxRateById(li.taxRateId);
            if (rate) taxTotal += li.lineTotal * (rate.rate / 100);
        });
        subtotal = Math.round(subtotal * 100) / 100;
        taxTotal = Math.round(taxTotal * 100) / 100;
        const total = Math.round((subtotal + taxTotal) * 100) / 100;

        const subEl = document.getElementById('form-subtotal');
        const taxEl = document.getElementById('form-tax');
        const totalEl = document.getElementById('form-total');
        if (subEl) subEl.textContent = Components.formatCurrency(subtotal);
        if (taxEl) taxEl.textContent = Components.formatCurrency(taxTotal);
        if (totalEl) totalEl.textContent = Components.formatCurrency(total);
    },

    _addLineItem() {
        this._captureLineItems();
        const tbody = document.getElementById('lineItemsBody');
        if (!tbody) return;

        const idx = this._lineItems.length;
        const taxOpts = AppState.taxRates.map(t => ({ value: t.id, label: t.name }));
        const accOpts = AppState.accountCodes.filter(a => a.type === 'Revenue').map(a => ({ value: a.code, label: a.code + ' - ' + a.name }));
        const newLi = { description: '', quantity: 1, unitPrice: 0, taxRateId: AppState.settings.defaultTaxRateId, accountCode: '200', lineTotal: 0 };

        const temp = document.createElement('tbody');
        temp.innerHTML = Views._renderLineItemRow(newLi, idx, taxOpts, accOpts);
        const newRow = temp.firstElementChild;
        tbody.appendChild(newRow);

        this._lineItems.push(newLi);
        // Focus the new description field
        const descInput = newRow.querySelector('[data-line-field="description"]');
        if (descInput) descInput.focus();
    },

    _removeLineItem(idx) {
        this._captureLineItems();
        if (this._lineItems.length <= 1) return; // Must have at least 1 line

        // Re-render the line items section
        this._lineItems.splice(idx, 1);

        const tbody = document.getElementById('lineItemsBody');
        if (!tbody) return;

        const taxOpts = AppState.taxRates.map(t => ({ value: t.id, label: t.name }));
        const accOpts = AppState.accountCodes.filter(a => a.type === 'Revenue').map(a => ({ value: a.code, label: a.code + ' - ' + a.name }));

        let html = '';
        this._lineItems.forEach((li, i) => {
            html += Views._renderLineItemRow(li, i, taxOpts, accOpts);
        });
        tbody.innerHTML = html;
        this._updateFormTotals();
    },

    // ========== Save Handlers ==========

    _saveInvoice(status) {
        this._captureLineItems();

        const contactDd = document.getElementById('invoice-contact');
        const contactSelected = contactDd ? contactDd.querySelector('.dropdown-item.selected') : null;
        const contactId = contactSelected ? contactSelected.dataset.value : '';

        const invoiceNumber = (document.getElementById('invoice-number') || {}).value || '';
        const reference = (document.getElementById('invoice-reference') || {}).value || '';
        const issueDate = (document.getElementById('invoice-date') || {}).value || '';
        const dueDate = (document.getElementById('invoice-due-date') || {}).value || '';

        const currDd = document.getElementById('invoice-currency');
        const currSelected = currDd ? currDd.querySelector('.dropdown-item.selected') : null;
        const currency = currSelected ? currSelected.dataset.value : 'NZD';

        const themeDd = document.getElementById('invoice-theme');
        const themeSelected = themeDd ? themeDd.querySelector('.dropdown-item.selected') : null;
        const brandingThemeId = themeSelected ? themeSelected.dataset.value : '';

        const notes = (document.getElementById('invoice-notes') || {}).value || '';

        // Validation
        if (!contactId) {
            Components.showToast('Please select a contact');
            return;
        }
        if (!issueDate) {
            Components.showToast('Please enter an invoice date');
            return;
        }
        if (!dueDate) {
            Components.showToast('Please enter a due date');
            return;
        }
        if (this._lineItems.length === 0 || this._lineItems.every(li => !li.description && li.quantity === 0)) {
            Components.showToast('Please add at least one line item');
            return;
        }

        const data = {
            contactId,
            invoiceNumber,
            reference,
            issueDate,
            dueDate,
            currency,
            brandingThemeId,
            notes,
            lineItems: this._lineItems,
            status: status
        };

        if (AppState.currentView === 'edit-invoice' && AppState.currentItemId) {
            AppState.updateInvoice(AppState.currentItemId, data);
            Components.showToast('Invoice updated');
            this.navigate('invoices/' + AppState.currentItemId);
        } else {
            const inv = AppState.createInvoice(data);
            Components.showToast('Invoice created');
            this.navigate('invoices/' + inv.id);
        }
    },

    _showPaymentModal(invoiceId) {
        this._currentPaymentInvoiceId = invoiceId;
        const body = Views.renderPaymentModal(invoiceId);
        Components.showModal('Record Payment', body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="save-payment" data-testid="save-payment-btn">Save Payment</button>');
    },

    _savePayment() {
        const invoiceId = this._currentPaymentInvoiceId;
        if (!invoiceId) return;

        const amount = parseFloat((document.getElementById('payment-amount') || {}).value) || 0;
        const date = (document.getElementById('payment-date') || {}).value || '';
        const reference = (document.getElementById('payment-reference') || {}).value || '';
        const note = (document.getElementById('payment-note') || {}).value || '';

        const bankDd = document.getElementById('payment-bank');
        const bankSelected = bankDd ? bankDd.querySelector('.dropdown-item.selected') : null;
        const bankAccountId = bankSelected ? bankSelected.dataset.value : 'bank_1';

        let exchangeRate = 1;
        const exRateEl = document.getElementById('payment-exchange-rate');
        if (exRateEl) exchangeRate = parseFloat(exRateEl.value) || 1;

        if (amount <= 0) {
            Components.showToast('Please enter a valid amount');
            return;
        }
        if (!date) {
            Components.showToast('Please enter a payment date');
            return;
        }

        AppState.addPayment(invoiceId, { amount, date, bankAccountId, reference, note, exchangeRate });
        Components.closeModal();
        Components.showToast('Payment recorded');
    },

    _showContactModal(contactId, quickAdd) {
        this._currentEditContactId = contactId;
        const title = contactId ? 'Edit Contact' : 'New Contact';
        const body = Views.renderContactModal(contactId);
        const saveAction = quickAdd ? 'save-contact-quick' : 'save-contact';
        Components.showModal(title, body,
            '<button class="btn btn-secondary" data-action="close-modal">Cancel</button>' +
            '<button class="btn btn-primary" data-action="' + saveAction + '" data-testid="save-contact-btn">Save</button>', true);
    },

    _saveContact(quickAdd) {
        const name = (document.getElementById('contact-name') || {}).value || '';
        const email = (document.getElementById('contact-email') || {}).value || '';
        const phone = (document.getElementById('contact-phone') || {}).value || '';
        const street = (document.getElementById('contact-street') || {}).value || '';
        const city = (document.getElementById('contact-city') || {}).value || '';
        const region = (document.getElementById('contact-region') || {}).value || '';
        const postalCode = (document.getElementById('contact-postal') || {}).value || '';
        const country = (document.getElementById('contact-country') || {}).value || 'New Zealand';
        const taxId = (document.getElementById('contact-taxid') || {}).value || '';

        if (!name) {
            Components.showToast('Please enter a contact name');
            return;
        }
        if (!email) {
            Components.showToast('Please enter an email address');
            return;
        }

        const data = {
            name, email, phone, taxId,
            billingAddress: { street, city, region, postalCode, country }
        };

        if (this._currentEditContactId) {
            AppState.updateContact(this._currentEditContactId, data);
            Components.showToast('Contact updated');
        } else {
            const contact = AppState.createContact(data);
            Components.showToast('Contact created');
            // If quick add from invoice form, select the new contact in dropdown
            if (quickAdd) {
                // Re-render will pick up the new contact
            }
        }
        Components.closeModal();
    },

    _saveSettings() {
        const dueDd = document.getElementById('settings-due-terms');
        const dueSelected = dueDd ? dueDd.querySelector('.dropdown-item.selected') : null;

        const taxDd = document.getElementById('settings-tax-rate');
        const taxSelected = taxDd ? taxDd.querySelector('.dropdown-item.selected') : null;

        const themeDd = document.getElementById('settings-branding-theme');
        const themeSelected = themeDd ? themeDd.querySelector('.dropdown-item.selected') : null;

        const freqDd = document.getElementById('settings-penalty-freq');
        const freqSelected = freqDd ? freqDd.querySelector('.dropdown-item.selected') : null;

        const updates = {
            defaultDueDateTerms: dueSelected ? dueSelected.dataset.value : AppState.settings.defaultDueDateTerms,
            defaultTaxRateId: taxSelected ? taxSelected.dataset.value : AppState.settings.defaultTaxRateId,
            defaultBrandingThemeId: themeSelected ? themeSelected.dataset.value : AppState.settings.defaultBrandingThemeId,
            invoiceNumberPrefix: (document.getElementById('settings-inv-prefix') || {}).value || 'INV-',
            invoiceNumberNextNumber: parseInt((document.getElementById('settings-inv-next') || {}).value) || 1,
            invoiceNumberPadding: parseInt((document.getElementById('settings-inv-padding') || {}).value) || 4,
            defaultEmailSubject: (document.getElementById('settings-email-subject') || {}).value || '',
            defaultEmailBody: (document.getElementById('settings-email-body') || {}).value || '',
            latePenaltyEnabled: document.getElementById('settings-penalty-enabled') ? document.getElementById('settings-penalty-enabled').checked : false,
            latePenaltyRate: parseFloat((document.getElementById('settings-penalty-rate') || {}).value) || 0,
            latePenaltyFrequency: freqSelected ? freqSelected.dataset.value : 'monthly',
            companyName: (document.getElementById('settings-company-name') || {}).value || '',
            companyEmail: (document.getElementById('settings-company-email') || {}).value || '',
            companyPhone: (document.getElementById('settings-company-phone') || {}).value || '',
            companyAddress: (document.getElementById('settings-company-address') || {}).value || '',
            companyTaxId: (document.getElementById('settings-company-taxid') || {}).value || '',
        };

        AppState.updateSettings(updates);
        Components.showToast('Settings saved');
    },

    // ========== Sort/Select Helpers ==========

    _sortInvoices(field) {
        if (AppState.invoiceSortField === field) {
            AppState.invoiceSortDir = AppState.invoiceSortDir === 'asc' ? 'desc' : 'asc';
        } else {
            AppState.invoiceSortField = field;
            AppState.invoiceSortDir = field === 'invoiceNumber' || field === 'contactName' || field === 'reference' ? 'asc' : 'desc';
        }
        AppState.invoicePage = 1;
        this.render();
    },

    _toggleSelectAll() {
        const paged = AppState.getPagedInvoices();
        const allSelected = paged.items.every(inv => AppState.selectedInvoiceIds.includes(inv.id));
        if (allSelected) {
            AppState.selectedInvoiceIds = [];
        } else {
            AppState.selectedInvoiceIds = paged.items.map(inv => inv.id);
        }
        this.render();
    },

    _toggleSelectInvoice(id) {
        const idx = AppState.selectedInvoiceIds.indexOf(id);
        if (idx > -1) {
            AppState.selectedInvoiceIds.splice(idx, 1);
        } else {
            AppState.selectedInvoiceIds.push(id);
        }
        this.render();
    },
};

// Handle save-contact-quick action for quick-add from invoice form
const _origHandleAction = App._handleAction.bind(App);
App._handleAction = function(action, el) {
    if (action === 'save-contact-quick') {
        App._saveContact(true);
        return;
    }
    _origHandleAction(action, el);
};

window.addEventListener('DOMContentLoaded', () => { App.init(); });

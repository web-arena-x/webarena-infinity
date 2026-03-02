const App = {
  _openDropdownId: null,
  _formLineItems: [],
  _formPrefix: '',
  _currentPage: 1,
  _pageSize: 25,

  init() {
    AppState.init();
    AppState.subscribe(() => App.render());
    window.addEventListener('hashchange', () => { App.parseRoute(); App.render(); });
    document.addEventListener('click', (e) => App.handleClick(e));
    document.addEventListener('change', (e) => App.handleChange(e));
    document.addEventListener('input', (e) => App.handleInput(e));
    document.addEventListener('keydown', (e) => App.handleKeydown(e));
    App._connectSSE();
    App.parseRoute();
    App.render();
    AppState._pushStateToServer();
  },

  parseRoute() {
    const hash = window.location.hash || '#/dashboard';
    const parts = hash.replace('#/', '').split('/');
    const view = parts[0] || 'dashboard';

    const validViews = ['dashboard', 'invoices', 'quotes', 'credit-notes', 'repeating-invoices', 'settings', 'templates', 'reminders', 'search'];
    if (validViews.includes(view)) {
      AppState.currentView = view;
      AppState.currentSubView = parts[1] || '';
      AppState.currentId = parts[2] || parts[1] || null;
    } else {
      AppState.currentView = 'dashboard';
      AppState.currentSubView = '';
      AppState.currentId = null;
    }

    if (view === 'invoices' && parts[1] === 'new') {
      AppState.currentSubView = 'new';
      AppState.currentId = null;
    } else if (view === 'invoices' && parts[1] === 'edit' && parts[2]) {
      AppState.currentSubView = 'edit';
      AppState.currentId = parts[2];
    } else if (view === 'invoices' && parts[1] && parts[1] !== 'new' && parts[1] !== 'edit') {
      AppState.currentSubView = 'detail';
      AppState.currentId = parts[1];
    }

    if (view === 'quotes' && parts[1] === 'new') {
      AppState.currentSubView = 'new';
    } else if (view === 'quotes' && parts[1] === 'edit' && parts[2]) {
      AppState.currentSubView = 'edit';
      AppState.currentId = parts[2];
    } else if (view === 'quotes' && parts[1] && parts[1] !== 'new' && parts[1] !== 'edit') {
      AppState.currentSubView = 'detail';
      AppState.currentId = parts[1];
    }

    if (view === 'credit-notes' && parts[1] === 'new') {
      AppState.currentSubView = 'new';
    } else if (view === 'credit-notes' && parts[1] === 'edit' && parts[2]) {
      AppState.currentSubView = 'edit';
      AppState.currentId = parts[2];
    } else if (view === 'credit-notes' && parts[1] && parts[1] !== 'new' && parts[1] !== 'edit') {
      AppState.currentSubView = 'detail';
      AppState.currentId = parts[1];
    }

    if (view === 'repeating-invoices' && parts[1] === 'new') {
      AppState.currentSubView = 'new';
    } else if (view === 'repeating-invoices' && parts[1] === 'edit' && parts[2]) {
      AppState.currentSubView = 'edit';
      AppState.currentId = parts[2];
    } else if (view === 'repeating-invoices' && parts[1] && parts[1] !== 'new' && parts[1] !== 'edit') {
      AppState.currentSubView = 'detail';
      AppState.currentId = parts[1];
    }

    if (view === 'templates' && parts[1] === 'new') {
      AppState.currentSubView = 'new';
    } else if (view === 'templates' && parts[1] === 'edit' && parts[2]) {
      AppState.currentSubView = 'edit';
      AppState.currentId = parts[2];
    }

    if (view === 'reminders' && parts[1] === 'new') {
      AppState.currentSubView = 'new';
    } else if (view === 'reminders' && parts[1] === 'edit' && parts[2]) {
      AppState.currentSubView = 'edit';
      AppState.currentId = parts[2];
    }

    AppState.selectedIds = new Set();
    App._currentPage = 1;
  },

  navigate(route) {
    AppState.searchResults = null;
    AppState.searchQuery = '';
    window.location.hash = '#/' + route;
  },

  render() {
    const sidebar = document.getElementById('sidebarNav');
    if (sidebar) sidebar.innerHTML = Views.renderSidebar();

    const content = document.getElementById('contentWrapper');
    if (!content) return;

    let html = '';
    const view = AppState.currentView;
    const sub = AppState.currentSubView;

    if (AppState.searchResults !== null) {
      html = Views.renderSearchResults(AppState.searchResults);
    } else if (view === 'dashboard') {
      html = Views.renderDashboard();
    } else if (view === 'invoices') {
      if (sub === 'new') {
        html = Views.renderInvoiceForm(null);
      } else if (sub === 'edit' && AppState.currentId) {
        html = Views.renderInvoiceForm(AppState.getInvoiceById(AppState.currentId));
      } else if (sub === 'detail' && AppState.currentId) {
        html = Views.renderInvoiceDetail(AppState.getInvoiceById(AppState.currentId));
      } else {
        html = Views.renderInvoiceList();
      }
    } else if (view === 'quotes') {
      if (sub === 'new') {
        html = Views.renderQuoteForm(null);
      } else if (sub === 'edit' && AppState.currentId) {
        html = Views.renderQuoteForm(AppState.getQuoteById(AppState.currentId));
      } else if (sub === 'detail' && AppState.currentId) {
        html = Views.renderQuoteDetail(AppState.getQuoteById(AppState.currentId));
      } else {
        html = Views.renderQuoteList();
      }
    } else if (view === 'credit-notes') {
      if (sub === 'new') {
        html = Views.renderCreditNoteForm(null);
      } else if (sub === 'edit' && AppState.currentId) {
        html = Views.renderCreditNoteForm(AppState.getCreditNoteById(AppState.currentId));
      } else if (sub === 'detail' && AppState.currentId) {
        html = Views.renderCreditNoteDetail(AppState.getCreditNoteById(AppState.currentId));
      } else {
        html = Views.renderCreditNoteList();
      }
    } else if (view === 'repeating-invoices') {
      if (sub === 'new') {
        html = Views.renderRepeatingInvoiceForm(null);
      } else if (sub === 'edit' && AppState.currentId) {
        html = Views.renderRepeatingInvoiceForm(AppState.getRepeatingInvoiceById(AppState.currentId));
      } else {
        html = Views.renderRepeatingInvoiceList();
      }
    } else if (view === 'settings') {
      html = Views.renderSettings();
    } else if (view === 'templates') {
      if (sub === 'new') {
        html = Views.renderThemeForm(null);
      } else if (sub === 'edit' && AppState.currentId) {
        html = Views.renderThemeForm(AppState.getBrandingThemeById(AppState.currentId));
      } else {
        html = Views.renderTemplates();
      }
    } else if (view === 'reminders') {
      if (sub === 'new') {
        html = Views.renderReminderForm(null);
      } else if (sub === 'edit' && AppState.currentId) {
        html = Views.renderReminderForm(AppState.invoiceReminders.find(r => r.id === AppState.currentId));
      } else {
        html = Views.renderReminders();
      }
    }

    content.innerHTML = html;

    // Modal overlay
    const modalContainer = document.getElementById('modalContainer');
    if (modalContainer) {
      if (AppState.modalState) {
        modalContainer.innerHTML = AppState.modalState;
        modalContainer.style.display = 'block';
      } else {
        modalContainer.innerHTML = '';
        modalContainer.style.display = 'none';
      }
    }

    // Update form totals after render
    this._updateFormTotals();
  },

  // ---- Click handler ----
  handleClick(e) {
    const target = e.target;

    // Close dropdowns on outside click
    const dropdown = target.closest('.custom-dropdown');
    if (!dropdown && App._openDropdownId) {
      App._closeAllDropdowns();
    }

    // Route links
    const routeEl = target.closest('[data-route]');
    if (routeEl) {
      e.preventDefault();
      const route = routeEl.dataset.route;
      const tab = routeEl.dataset.tab;
      if (tab) AppState.currentTab = tab;
      App.navigate(route);
      return;
    }

    // Dropdown trigger
    const ddTrigger = target.closest('[data-dropdown]');
    if (ddTrigger) {
      e.preventDefault();
      e.stopPropagation();
      const ddId = ddTrigger.dataset.dropdown;
      App._toggleDropdown(ddId);
      return;
    }

    // Dropdown item
    const ddItem = target.closest('.dropdown-item[data-value]');
    if (ddItem) {
      e.preventDefault();
      e.stopPropagation();
      const ddId = ddItem.dataset.dropdownId;
      const value = ddItem.dataset.value;
      App._handleDropdownSelect(ddId, value);
      return;
    }

    // Checkbox
    const checkbox = target.closest('.row-checkbox');
    if (checkbox) {
      const id = checkbox.dataset.checkId;
      if (AppState.selectedIds.has(id)) {
        AppState.selectedIds.delete(id);
      } else {
        AppState.selectedIds.add(id);
      }
      App.render();
      return;
    }

    // Actions
    const actionEl = target.closest('[data-action]');
    if (actionEl) {
      // Don't close modal from clicks inside the modal that bubble to backdrop
      if (actionEl.dataset.action === 'close-modal' && actionEl.classList.contains('modal-backdrop') && target.closest('.modal')) {
        return;
      }
      e.preventDefault();
      App.handleAction(actionEl.dataset.action, actionEl);
      return;
    }
  },

  handleAction(action, el) {
    const id = el ? el.dataset.id : null;

    switch (action) {
      // Navigation
      case 'new-invoice': App.navigate('invoices/new'); break;
      case 'new-quote': App.navigate('quotes/new'); break;
      case 'new-credit-note': App.navigate('credit-notes/new'); break;
      case 'new-repeating': App.navigate('repeating-invoices/new'); break;
      case 'new-theme': App.navigate('templates/new'); break;
      case 'new-reminder': App.navigate('reminders/new'); break;

      case 'view-invoice': App.navigate('invoices/' + id); break;
      case 'view-quote': App.navigate('quotes/' + id); break;
      case 'view-credit-note': App.navigate('credit-notes/' + id); break;
      case 'view-repeating': App.navigate('repeating-invoices/edit/' + id); break;

      case 'edit-invoice': App.navigate('invoices/edit/' + id); break;
      case 'edit-quote': App.navigate('quotes/edit/' + id); break;
      case 'edit-credit-note': App.navigate('credit-notes/edit/' + id); break;
      case 'edit-theme': App.navigate('templates/edit/' + id); break;
      case 'edit-reminder': App.navigate('reminders/edit/' + id); break;

      case 'back-to-invoices': App.navigate('invoices'); break;
      case 'back-to-quotes': App.navigate('quotes'); break;
      case 'back-to-credit-notes': App.navigate('credit-notes'); break;
      case 'cancel-form': window.history.back(); break;

      // Tab switching
      case 'switch-tab':
        AppState.currentTab = el.dataset.tab;
        App._currentPage = 1;
        App.render();
        break;

      // Invoice actions
      case 'approve-invoice': AppState.approveInvoice(id); Components.showToast('Invoice approved'); break;
      case 'submit-for-approval': AppState.submitForApproval(id); Components.showToast('Submitted for approval'); break;
      case 'send-invoice': AppState.sendInvoice(id); Components.showToast('Invoice sent'); break;
      case 'mark-sent': AppState.markInvoiceSent(id); Components.showToast('Marked as sent'); break;
      case 'void-invoice':
        AppState.modalState = Components.confirmDialog('Void Invoice', 'Are you sure you want to void this invoice? This cannot be undone.', 'confirm-void-invoice', 'Void');
        App.render();
        break;
      case 'confirm-void-invoice':
        AppState.voidInvoice(AppState.currentId);
        AppState.modalState = null;
        Components.showToast('Invoice voided');
        break;
      case 'delete-invoice':
        AppState.modalState = Components.confirmDialog('Delete Invoice', 'Are you sure you want to delete this invoice?', 'confirm-delete-invoice', 'Delete');
        App.render();
        break;
      case 'confirm-delete-invoice':
        AppState.deleteInvoice(AppState.currentId);
        AppState.modalState = null;
        App.navigate('invoices');
        Components.showToast('Invoice deleted');
        break;
      case 'copy-invoice': {
        const copy = AppState.copyInvoice(id);
        if (copy) { App.navigate('invoices/' + copy.id); Components.showToast('Invoice copied'); }
        break;
      }
      case 'create-cn-from-invoice': {
        const inv = AppState.getInvoiceById(id);
        if (inv) {
          App.navigate('credit-notes/new');
          // Store context for pre-filling
          App._prefillCN = { contactId: inv.contactId, reference: 'Re: ' + inv.number, lineItems: JSON.parse(JSON.stringify(inv.lineItems)), taxMode: inv.taxMode };
        }
        break;
      }

      // Payment
      case 'show-add-payment': {
        const inv = AppState.getInvoiceById(id);
        if (inv) { AppState.modalState = Views.renderPaymentModal(inv); App.render(); }
        break;
      }
      case 'confirm-add-payment': {
        const invId = el.dataset.invoiceId;
        const date = document.getElementById('pay-date').value;
        const amount = parseFloat(document.getElementById('pay-amount').value);
        const reference = document.getElementById('pay-reference').value;
        const accountId = App._getDropdownValue('pay-account') || 'acc_090';
        if (!date || isNaN(amount) || amount <= 0) {
          Components.showToast('Please enter a valid date and amount', 'error');
          break;
        }
        AppState.addPayment(invId, { date, amount, reference, accountId });
        AppState.modalState = null;
        Components.showToast('Payment recorded');
        break;
      }
      case 'remove-payment': {
        const invId = el.dataset.invoiceId;
        const payId = el.dataset.paymentId;
        AppState.removePayment(invId, payId);
        Components.showToast('Payment removed');
        break;
      }

      // Save invoice
      case 'save-invoice-draft': App._saveInvoice('draft'); break;
      case 'save-invoice-submit': App._saveInvoice('awaiting_approval'); break;
      case 'save-invoice-approve': App._saveInvoice('awaiting_payment'); break;
      case 'save-invoice': App._updateInvoice(el.dataset.id); break;

      // Quote actions
      case 'send-quote': AppState.sendQuote(id); Components.showToast('Quote sent'); break;
      case 'accept-quote': AppState.acceptQuote(id); Components.showToast('Quote accepted'); break;
      case 'decline-quote': AppState.declineQuote(id); Components.showToast('Quote declined'); break;
      case 'delete-quote': AppState.deleteQuote(id); App.navigate('quotes'); Components.showToast('Quote deleted'); break;
      case 'copy-quote': {
        const copy = AppState.copyQuote(id);
        if (copy) { App.navigate('quotes/' + copy.id); Components.showToast('Quote copied'); }
        break;
      }
      case 'invoice-from-quote': {
        const inv = AppState.createInvoiceFromQuote(id);
        if (inv) { App.navigate('invoices/' + inv.id); Components.showToast('Invoice created from quote'); }
        break;
      }
      case 'save-quote-draft': App._saveQuote('draft'); break;
      case 'save-quote-send': App._saveQuote('sent'); break;
      case 'save-quote': App._updateQuote(el.dataset.id); break;

      // Credit note actions
      case 'approve-credit-note': AppState.approveCreditNote(id); Components.showToast('Credit note approved'); break;
      case 'delete-credit-note': AppState.deleteCreditNote(id); App.navigate('credit-notes'); Components.showToast('Credit note deleted'); break;
      case 'show-allocate-cn': {
        const cn = AppState.getCreditNoteById(id);
        if (cn) { AppState.modalState = Views.renderAllocateModal(cn); App.render(); }
        break;
      }
      case 'confirm-allocate-cn': {
        const cnId = el.dataset.cnId;
        const invoiceId = App._getDropdownValue('alloc-invoice');
        const amount = parseFloat(document.getElementById('alloc-amount').value);
        if (!invoiceId || isNaN(amount) || amount <= 0) {
          Components.showToast('Select an invoice and enter a valid amount', 'error');
          break;
        }
        AppState.allocateCreditNote(cnId, invoiceId, amount);
        AppState.modalState = null;
        Components.showToast('Credit allocated');
        break;
      }
      case 'save-cn-draft': App._saveCreditNote('draft'); break;
      case 'save-cn-approve': App._saveCreditNote('awaiting_payment'); break;
      case 'save-credit-note': App._updateCreditNote(el.dataset.id); break;

      // Repeating invoice
      case 'save-repeating-new': App._saveRepeating(null); break;
      case 'save-repeating': App._saveRepeating(el.dataset.id); break;
      case 'delete-repeating':
        AppState.deleteRepeatingInvoice(id);
        Components.showToast('Repeating invoice deleted');
        break;

      // Settings
      case 'save-settings': App._saveSettings(); break;

      // Branding themes
      case 'save-theme-new': App._saveTheme(null); break;
      case 'save-theme': App._saveTheme(el.dataset.id); break;
      case 'set-default-theme': AppState.setDefaultTheme(id); Components.showToast('Default theme updated'); break;
      case 'delete-theme': AppState.deleteBrandingTheme(id); Components.showToast('Theme deleted'); break;

      // Reminders
      case 'toggle-reminder': AppState.toggleReminder(id); break;
      case 'delete-reminder': AppState.deleteReminder(id); Components.showToast('Reminder deleted'); break;
      case 'save-reminder-new': App._saveReminder(null); break;
      case 'save-reminder': App._saveReminder(el.dataset.id); break;

      // Modal
      case 'close-modal':
        AppState.modalState = null;
        App.render();
        break;

      // Toast
      case 'close-toast':
        el.closest('.toast').remove();
        break;

      // Line items
      case 'add-line': App._addLine(el.dataset.prefix); break;
      case 'remove-line': App._removeLine(el.dataset.prefix, parseInt(el.dataset.lineIdx)); break;

      // Search
      case 'do-search': App._doSearch(); break;
      case 'clear-search':
        AppState.searchResults = null;
        AppState.searchQuery = '';
        document.getElementById('searchInput').value = '';
        App.render();
        break;

      // Select all
      case 'select-all': {
        const checkAll = el.querySelector('input[type=checkbox]') || el;
        // Toggle all visible
        const rows = document.querySelectorAll('.row-checkbox');
        rows.forEach(r => {
          if (checkAll.checked) {
            AppState.selectedIds.add(r.dataset.checkId);
          } else {
            AppState.selectedIds.delete(r.dataset.checkId);
          }
        });
        App.render();
        break;
      }
    }
  },

  // ---- Change handler ----
  handleChange(e) {
    const target = e.target;
    if (target.id && target.id.startsWith('toggle-rem-')) {
      const remId = target.dataset.id;
      if (remId) AppState.toggleReminder(remId);
    }
    // Settings toggles
    if (target.id === 'set-show-tax' || target.id === 'set-show-disc' || target.id === 'set-show-code') {
      // Will be saved on "Save Settings" click
    }
  },

  // ---- Input handler ----
  handleInput(e) {
    const target = e.target;

    // Searchable dropdown filtering
    if (target.dataset.searchableDropdown) {
      const ddId = target.dataset.searchableDropdown;
      const menu = document.getElementById(ddId + '-menu');
      if (menu) {
        const q = target.value.toLowerCase();
        menu.style.display = 'block';
        const items = menu.querySelectorAll('.dropdown-item');
        items.forEach(item => {
          item.style.display = item.textContent.toLowerCase().includes(q) ? '' : 'none';
        });
      }
    }

    // Recalculate line item totals on any numeric input
    if (target.id && (target.id.includes('-qty-') || target.id.includes('-price-') || target.id.includes('-disc-'))) {
      App._updateFormTotals();
    }
  },

  // ---- Keydown handler ----
  handleKeydown(e) {
    if (e.key === 'Enter' && e.target.id === 'searchInput') {
      App._doSearch();
    }
    if (e.key === 'Escape') {
      if (AppState.modalState) {
        AppState.modalState = null;
        App.render();
      }
      App._closeAllDropdowns();
    }
  },

  // ---- Dropdown helpers ----
  _toggleDropdown(ddId) {
    const menu = document.getElementById(ddId + '-menu');
    if (!menu) return;
    if (App._openDropdownId === ddId) {
      menu.style.display = 'none';
      App._openDropdownId = null;
    } else {
      App._closeAllDropdowns();
      menu.style.display = 'block';
      App._openDropdownId = ddId;
    }
  },

  _closeAllDropdowns() {
    document.querySelectorAll('.dropdown-menu').forEach(m => { m.style.display = 'none'; });
    App._openDropdownId = null;
  },

  _handleDropdownSelect(ddId, value) {
    // Update trigger text
    const dd = document.getElementById(ddId);
    if (dd) {
      const trigger = dd.querySelector('.dropdown-trigger .dropdown-text');
      const input = dd.querySelector('.dropdown-search-input');
      const item = dd.querySelector('.dropdown-item[data-value="' + value + '"]');
      const label = item ? item.textContent : value;
      if (trigger) trigger.textContent = label;
      if (input) input.value = label;
      // Mark active
      dd.querySelectorAll('.dropdown-item').forEach(i => i.classList.remove('active'));
      if (item) item.classList.add('active');
    }
    App._closeAllDropdowns();

    // Handle item selection for line items (auto-fill description/price)
    if (ddId.match(/^(inv|quo|cn|rep)-item-\d+$/)) {
      const parts = ddId.split('-');
      const prefix = parts[0];
      const idx = parts[2];
      const selectedItem = AppState.getItemById(value);
      if (selectedItem) {
        const descEl = document.getElementById(prefix + '-desc-' + idx);
        const priceEl = document.getElementById(prefix + '-price-' + idx);
        const accDd = document.getElementById(prefix + '-acc-' + idx);
        const taxDd = document.getElementById(prefix + '-tax-' + idx);
        if (descEl && !descEl.value) descEl.value = selectedItem.description;
        if (priceEl && parseFloat(priceEl.value) === 0) priceEl.value = selectedItem.unitPrice;
        if (accDd) App._setDropdownValue(prefix + '-acc-' + idx, selectedItem.accountId);
        if (taxDd) App._setDropdownValue(prefix + '-tax-' + idx, selectedItem.taxRateId);
        App._updateFormTotals();
      }
    }
  },

  _getDropdownValue(ddId) {
    const dd = document.getElementById(ddId);
    if (!dd) return '';
    const active = dd.querySelector('.dropdown-item.active');
    return active ? active.dataset.value : '';
  },

  _setDropdownValue(ddId, value) {
    const dd = document.getElementById(ddId);
    if (!dd) return;
    dd.querySelectorAll('.dropdown-item').forEach(i => i.classList.remove('active'));
    const item = dd.querySelector('.dropdown-item[data-value="' + value + '"]');
    if (item) {
      item.classList.add('active');
      const trigger = dd.querySelector('.dropdown-trigger .dropdown-text');
      if (trigger) trigger.textContent = item.textContent;
    }
  },

  // ---- Line item management ----
  _addLine(prefix) {
    const tbody = document.querySelector('#' + prefix + '-line-items tbody');
    if (!tbody) return;
    const idx = tbody.querySelectorAll('.line-item-row').length;
    // Re-render the form to add a new line
    const currentLines = App._collectLineItems(prefix);
    currentLines.push({ id: AppState.generateLineItemId(), itemId: '', description: '', quantity: 1, unitPrice: 0, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' });
    App._reRenderLineItems(prefix, currentLines);
  },

  _removeLine(prefix, idx) {
    const currentLines = App._collectLineItems(prefix);
    if (currentLines.length <= 1) return;
    currentLines.splice(idx, 1);
    App._reRenderLineItems(prefix, currentLines);
  },

  _reRenderLineItems(prefix, lineItems) {
    const container = document.getElementById(prefix + '-line-items');
    if (!container) return;
    // Save and restore by re-rendering just the line items section
    const isRepeating = prefix === 'rep';
    if (isRepeating) {
      container.innerHTML = App._buildRepLineItemsHtml(lineItems, prefix);
    } else {
      container.innerHTML = App._buildLineItemsHtml(lineItems, prefix);
    }
    App._updateFormTotals();
  },

  _buildLineItemsHtml(lineItems, prefix) {
    const itemOpts = [{ value: '', label: '-- Select Item --' }].concat(AppState.items.filter(i => i.isSold).map(i => ({ value: i.id, label: i.code + ' - ' + i.description })));
    const accountOpts = AppState.getRevenueAccounts().map(a => ({ value: a.id, label: a.code + ' - ' + a.name }));
    const taxOpts = AppState.getOutputTaxRates().map(t => ({ value: t.id, label: t.name + ' (' + t.rate + '%)' }));
    const regionOpts = [{ value: '', label: 'None' }].concat(AppState.trackingCategories.find(tc => tc.id === 'track_region') ? AppState.trackingCategories.find(tc => tc.id === 'track_region').options.map(o => ({ value: o.id, label: o.name })) : []);
    const deptOpts = [{ value: '', label: 'None' }].concat(AppState.trackingCategories.find(tc => tc.id === 'track_dept') ? AppState.trackingCategories.find(tc => tc.id === 'track_dept').options.map(o => ({ value: o.id, label: o.name })) : []);

    let html = '<table class="data-table editable-table"><thead><tr>';
    html += '<th>Item</th><th>Description</th><th class="col-narrow">Qty</th><th class="col-narrow">Price</th><th class="col-narrow">Disc %</th><th>Account</th><th>Tax</th><th>Region</th><th>Department</th><th class="col-narrow text-right">Amount</th><th></th></tr></thead><tbody>';
    lineItems.forEach((li, idx) => {
      const amt = li.quantity * li.unitPrice * (1 - (li.discountPercent || 0) / 100);
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
      html += '<td class="text-right line-amount">' + Components.formatCurrency(amt) + '</td>';
      html += '<td><button class="btn-icon btn-remove-line" data-action="remove-line" data-prefix="' + prefix + '" data-line-idx="' + idx + '">&times;</button></td>';
      html += '</tr>';
    });
    html += '</tbody></table>';
    html += '<button class="btn btn-secondary btn-sm" data-action="add-line" data-prefix="' + prefix + '">+ Add Line</button>';
    return html;
  },

  _buildRepLineItemsHtml(lineItems, prefix) {
    const itemOpts = [{ value: '', label: '-- Select --' }].concat(AppState.items.filter(i => i.isSold).map(i => ({ value: i.id, label: i.code + ' - ' + i.description })));
    const accountOpts = AppState.getRevenueAccounts().map(a => ({ value: a.id, label: a.code + ' - ' + a.name }));
    const taxOpts = AppState.getOutputTaxRates().map(t => ({ value: t.id, label: t.name + ' (' + t.rate + '%)' }));

    let html = '<table class="data-table editable-table"><thead><tr>';
    html += '<th>Item</th><th>Description</th><th class="col-narrow">Qty</th><th class="col-narrow">Price</th><th>Account</th><th>Tax</th><th></th></tr></thead><tbody>';
    lineItems.forEach((li, idx) => {
      html += '<tr class="line-item-row" data-line-idx="' + idx + '">';
      html += '<td>' + Components.dropdown(prefix + '-item-' + idx, itemOpts, li.itemId || '', 'Item', 'compact-dropdown') + '</td>';
      html += '<td><input type="text" class="form-input compact" id="' + prefix + '-desc-' + idx + '" value="' + Components.escapeHtml(li.description) + '" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="' + prefix + '-qty-' + idx + '" value="' + li.quantity + '" min="0" step="0.01" /></td>';
      html += '<td><input type="number" class="form-input compact text-right" id="' + prefix + '-price-' + idx + '" value="' + li.unitPrice + '" min="0" step="0.01" /></td>';
      html += '<td>' + Components.dropdown(prefix + '-acc-' + idx, accountOpts, li.accountId, 'Account', 'compact-dropdown') + '</td>';
      html += '<td>' + Components.dropdown(prefix + '-tax-' + idx, taxOpts, li.taxRateId, 'Tax', 'compact-dropdown') + '</td>';
      html += '<td><button class="btn-icon btn-remove-line" data-action="remove-line" data-prefix="' + prefix + '" data-line-idx="' + idx + '">&times;</button></td>';
      html += '</tr>';
    });
    html += '</tbody></table>';
    html += '<button class="btn btn-secondary btn-sm" data-action="add-line" data-prefix="' + prefix + '">+ Add Line</button>';
    return html;
  },

  _collectLineItems(prefix) {
    const rows = document.querySelectorAll('#' + prefix + '-line-items .line-item-row');
    const items = [];
    rows.forEach((row, idx) => {
      items.push({
        id: AppState.generateLineItemId(),
        itemId: App._getDropdownValue(prefix + '-item-' + idx),
        description: (document.getElementById(prefix + '-desc-' + idx) || {}).value || '',
        quantity: parseFloat((document.getElementById(prefix + '-qty-' + idx) || {}).value) || 0,
        unitPrice: parseFloat((document.getElementById(prefix + '-price-' + idx) || {}).value) || 0,
        discountPercent: parseFloat((document.getElementById(prefix + '-disc-' + idx) || {}).value) || 0,
        accountId: App._getDropdownValue(prefix + '-acc-' + idx) || 'acc_200',
        taxRateId: App._getDropdownValue(prefix + '-tax-' + idx) || 'tax_gst',
        trackingRegion: App._getDropdownValue(prefix + '-region-' + idx) || '',
        trackingDept: App._getDropdownValue(prefix + '-dept-' + idx) || ''
      });
    });
    return items;
  },

  _calcTotals(lineItems, taxMode) {
    let subtotal = 0;
    let taxTotal = 0;
    lineItems.forEach(li => {
      const lineAmt = li.quantity * li.unitPrice * (1 - (li.discountPercent || 0) / 100);
      const taxRate = AppState.getTaxRateById(li.taxRateId);
      const rate = taxRate ? taxRate.rate / 100 : 0;
      if (taxMode === 'inclusive') {
        const excl = lineAmt / (1 + rate);
        subtotal += excl;
        taxTotal += lineAmt - excl;
      } else if (taxMode === 'exclusive') {
        subtotal += lineAmt;
        taxTotal += lineAmt * rate;
      } else {
        subtotal += lineAmt;
      }
    });
    return { subtotal: Math.round(subtotal * 100) / 100, taxTotal: Math.round(taxTotal * 100) / 100, total: Math.round((subtotal + taxTotal) * 100) / 100 };
  },

  _updateFormTotals() {
    ['inv', 'quo', 'cn'].forEach(prefix => {
      const container = document.getElementById(prefix + '-totals');
      if (!container) return;
      const taxModeVal = App._getDropdownValue(prefix + '-tax-mode') || 'exclusive';
      const lineItems = App._collectLineItems(prefix);
      const totals = App._calcTotals(lineItems, taxModeVal);
      container.innerHTML = '<div class="total-row"><span>Subtotal</span><span>' + Components.formatCurrency(totals.subtotal) + '</span></div>' +
        '<div class="total-row"><span>Tax</span><span>' + Components.formatCurrency(totals.taxTotal) + '</span></div>' +
        '<div class="total-row total-main"><span>Total</span><span>' + Components.formatCurrency(totals.total) + '</span></div>';
    });
  },

  // ---- Save helpers ----
  _saveInvoice(status) {
    const contactId = App._getDropdownValue('inv-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const date = document.getElementById('inv-date').value;
    const dueDate = document.getElementById('inv-due-date').value;
    const reference = document.getElementById('inv-reference').value;
    const currency = App._getDropdownValue('inv-currency') || 'AUD';
    const themeId = App._getDropdownValue('inv-theme') || 'theme_standard';
    const taxMode = App._getDropdownValue('inv-tax-mode') || 'exclusive';
    const title = document.getElementById('inv-title').value;
    const summary = document.getElementById('inv-summary').value;
    const lineItems = App._collectLineItems('inv');
    const totals = App._calcTotals(lineItems, taxMode);

    const inv = AppState.createInvoice({
      contactId, status, date, dueDate, reference, currency,
      brandingThemeId: themeId, taxMode, lineItems, title, summary,
      ...totals
    });
    if (status === 'awaiting_payment') {
      inv.sentAt = new Date().toISOString();
    }
    App.navigate('invoices/' + inv.id);
    Components.showToast('Invoice created');
  },

  _updateInvoice(id) {
    const contactId = App._getDropdownValue('inv-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const date = document.getElementById('inv-date').value;
    const dueDate = document.getElementById('inv-due-date').value;
    const reference = document.getElementById('inv-reference').value;
    const currency = App._getDropdownValue('inv-currency') || 'AUD';
    const themeId = App._getDropdownValue('inv-theme') || 'theme_standard';
    const taxMode = App._getDropdownValue('inv-tax-mode') || 'exclusive';
    const title = document.getElementById('inv-title').value;
    const summary = document.getElementById('inv-summary').value;
    const lineItems = App._collectLineItems('inv');
    const totals = App._calcTotals(lineItems, taxMode);

    AppState.updateInvoice(id, {
      contactId, date, dueDate, reference, currency,
      brandingThemeId: themeId, taxMode, lineItems, title, summary,
      ...totals
    });
    App.navigate('invoices/' + id);
    Components.showToast('Invoice saved');
  },

  _saveQuote(status) {
    const contactId = App._getDropdownValue('quo-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const date = document.getElementById('quo-date').value;
    const expiryDate = document.getElementById('quo-expiry-date').value;
    const reference = document.getElementById('quo-reference').value;
    const currency = App._getDropdownValue('quo-currency') || 'AUD';
    const themeId = App._getDropdownValue('quo-theme') || 'theme_standard';
    const taxMode = App._getDropdownValue('quo-tax-mode') || 'exclusive';
    const title = document.getElementById('quo-title').value;
    const summary = document.getElementById('quo-summary').value;
    const terms = document.getElementById('quo-terms').value;
    const lineItems = App._collectLineItems('quo');
    const totals = App._calcTotals(lineItems, taxMode);

    const quo = AppState.createQuote({
      contactId, status, date, expiryDate, reference, currency,
      brandingThemeId: themeId, taxMode, lineItems, title, summary, terms, ...totals
    });
    if (status === 'sent') quo.sentAt = new Date().toISOString();
    AppState.notify();
    App.navigate('quotes/' + quo.id);
    Components.showToast('Quote created');
  },

  _updateQuote(id) {
    const contactId = App._getDropdownValue('quo-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const date = document.getElementById('quo-date').value;
    const expiryDate = document.getElementById('quo-expiry-date').value;
    const reference = document.getElementById('quo-reference').value;
    const currency = App._getDropdownValue('quo-currency') || 'AUD';
    const themeId = App._getDropdownValue('quo-theme') || 'theme_standard';
    const taxMode = App._getDropdownValue('quo-tax-mode') || 'exclusive';
    const title = document.getElementById('quo-title').value;
    const summary = document.getElementById('quo-summary').value;
    const terms = document.getElementById('quo-terms').value;
    const lineItems = App._collectLineItems('quo');
    const totals = App._calcTotals(lineItems, taxMode);

    AppState.updateQuote(id, {
      contactId, date, expiryDate, reference, currency,
      brandingThemeId: themeId, taxMode, lineItems, title, summary, terms, ...totals
    });
    App.navigate('quotes/' + id);
    Components.showToast('Quote saved');
  },

  _saveCreditNote(status) {
    const contactId = App._getDropdownValue('cn-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const date = document.getElementById('cn-date').value;
    const reference = document.getElementById('cn-reference').value;
    const taxMode = App._getDropdownValue('cn-tax-mode') || 'exclusive';
    const lineItems = App._collectLineItems('cn');
    const totals = App._calcTotals(lineItems, taxMode);

    const cn = AppState.createCreditNote({ contactId, status, date, reference, taxMode, lineItems, ...totals });
    App.navigate('credit-notes/' + cn.id);
    Components.showToast('Credit note created');
  },

  _updateCreditNote(id) {
    const contactId = App._getDropdownValue('cn-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const date = document.getElementById('cn-date').value;
    const reference = document.getElementById('cn-reference').value;
    const taxMode = App._getDropdownValue('cn-tax-mode') || 'exclusive';
    const lineItems = App._collectLineItems('cn');
    const totals = App._calcTotals(lineItems, taxMode);

    AppState.updateCreditNote(id, { contactId, date, reference, taxMode, lineItems, ...totals });
    App.navigate('credit-notes/' + id);
    Components.showToast('Credit note saved');
  },

  _saveRepeating(id) {
    const contactId = App._getDropdownValue('rep-contact');
    if (!contactId) { Components.showToast('Please select a contact', 'error'); return; }
    const data = {
      contactId,
      frequency: App._getDropdownValue('rep-frequency') || 'monthly',
      startDate: document.getElementById('rep-start-date').value,
      nextDate: document.getElementById('rep-next-date').value,
      endDate: document.getElementById('rep-end-date').value,
      saveAs: App._getDropdownValue('rep-save-as') || 'draft',
      brandingThemeId: App._getDropdownValue('rep-theme') || 'theme_standard',
      taxMode: App._getDropdownValue('rep-tax-mode') || 'exclusive',
      reference: document.getElementById('rep-reference').value,
      status: 'active',
      lineItems: App._collectLineItems('rep')
    };

    if (id) {
      AppState.updateRepeatingInvoice(id, data);
      Components.showToast('Repeating invoice updated');
    } else {
      AppState.createRepeatingInvoice(data);
      Components.showToast('Repeating invoice created');
    }
    App.navigate('repeating-invoices');
  },

  _saveSettings() {
    AppState.updateInvoiceSettings({
      invoicePrefix: document.getElementById('set-inv-prefix').value,
      invoiceNextNumber: parseInt(document.getElementById('set-inv-next').value) || 1,
      creditNotePrefix: document.getElementById('set-cn-prefix').value,
      creditNoteNextNumber: parseInt(document.getElementById('set-cn-next').value) || 1,
      quotePrefix: document.getElementById('set-quo-prefix').value,
      quoteNextNumber: parseInt(document.getElementById('set-quo-next').value) || 1,
      defaultDueDate: {
        type: App._getDropdownValue('set-due-type') || 'daysAfterInvoice',
        days: parseInt(document.getElementById('set-due-days').value) || 30
      },
      defaultTaxMode: App._getDropdownValue('set-tax-mode') || 'exclusive',
      showTaxColumn: document.getElementById('set-show-tax').checked,
      showDiscountColumn: document.getElementById('set-show-disc').checked,
      showItemCode: document.getElementById('set-show-code').checked
    });
    AppState._nextInvoiceNum = parseInt(document.getElementById('set-inv-next').value) || AppState._nextInvoiceNum;
    AppState._nextQuoteNum = parseInt(document.getElementById('set-quo-next').value) || AppState._nextQuoteNum;
    AppState._nextCreditNoteNum = parseInt(document.getElementById('set-cn-next').value) || AppState._nextCreditNoteNum;
    AppState.notify();
    Components.showToast('Settings saved');
  },

  _saveTheme(id) {
    const name = document.getElementById('theme-name').value.trim();
    if (!name) { Components.showToast('Theme name is required', 'error'); return; }
    const data = {
      name,
      paymentTerms: document.getElementById('theme-payment-terms').value,
      termsAndConditions: document.getElementById('theme-terms').value,
      showTaxNumber: document.getElementById('theme-show-tax').checked,
      showPaymentAdvice: document.getElementById('theme-show-advice').checked
    };
    if (id) {
      AppState.updateBrandingTheme(id, data);
      Components.showToast('Theme updated');
    } else {
      AppState.createBrandingTheme(data);
      Components.showToast('Theme created');
    }
    App.navigate('templates');
  },

  _saveReminder(id) {
    const data = {
      timing: App._getDropdownValue('rem-timing') || 'before',
      days: parseInt(document.getElementById('rem-days').value) || 7,
      subject: document.getElementById('rem-subject').value,
      body: document.getElementById('rem-body').value,
      includeInvoicePdf: document.getElementById('rem-incl-pdf').checked,
      includeSummary: document.getElementById('rem-incl-summary').checked
    };
    if (id) {
      AppState.updateReminder(id, data);
      Components.showToast('Reminder updated');
    } else {
      AppState.addReminder(data);
      Components.showToast('Reminder added');
    }
    App.navigate('reminders');
  },

  _doSearch() {
    const input = document.getElementById('searchInput');
    if (!input) return;
    const q = input.value.trim();
    if (!q) {
      AppState.searchResults = null;
    } else {
      AppState.searchQuery = q;
      AppState.searchResults = AppState.search(q);
    }
    App.render();
  },

  // ---- SSE ----
  _connectSSE() {
    const evtSource = new EventSource('/api/events');
    evtSource.onmessage = (e) => {
      if (e.data === 'reset') {
        AppState.resetToSeedData();
        App.navigate('dashboard');
      }
    };
  }
};

window.addEventListener('DOMContentLoaded', () => App.init());

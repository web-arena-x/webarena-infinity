const Components = {
  escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#039;');
  },

  formatCurrency(amount, currency) {
    const c = currency || 'AUD';
    const curr = CURRENCIES.find(cu => cu.code === c);
    const sym = curr ? curr.symbol : '$';
    if (amount < 0) return '-' + sym + Math.abs(amount).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return sym + amount.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  },

  formatDate(dateStr) {
    if (!dateStr) return '';
    const d = new Date(dateStr + (dateStr.includes('T') ? '' : 'T00:00:00'));
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return d.getDate() + ' ' + months[d.getMonth()] + ' ' + d.getFullYear();
  },

  formatDateFull(dateStr) {
    if (!dateStr) return '';
    const d = new Date(dateStr + (dateStr.includes('T') ? '' : 'T00:00:00'));
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    return d.getDate() + ' ' + months[d.getMonth()] + ' ' + d.getFullYear();
  },

  formatDateTime(dateStr) {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const hrs = d.getHours();
    const mins = String(d.getMinutes()).padStart(2, '0');
    const ampm = hrs >= 12 ? 'PM' : 'AM';
    const hr12 = hrs % 12 || 12;
    return d.getDate() + ' ' + months[d.getMonth()] + ' ' + d.getFullYear() + ', ' + hr12 + ':' + mins + ' ' + ampm;
  },

  todayStr() {
    return new Date().toISOString().split('T')[0];
  },

  statusBadge(status) {
    const labels = {
      draft: 'Draft',
      awaiting_approval: 'Awaiting Approval',
      awaiting_payment: 'Awaiting Payment',
      paid: 'Paid',
      voided: 'Voided',
      deleted: 'Deleted',
      sent: 'Sent',
      accepted: 'Accepted',
      declined: 'Declined',
      invoiced: 'Invoiced',
      active: 'Active'
    };
    const classes = {
      draft: 'badge-draft',
      awaiting_approval: 'badge-awaiting',
      awaiting_payment: 'badge-awaiting',
      paid: 'badge-paid',
      voided: 'badge-voided',
      deleted: 'badge-voided',
      sent: 'badge-sent',
      accepted: 'badge-accepted',
      declined: 'badge-declined',
      active: 'badge-active'
    };
    return '<span class="status-badge ' + (classes[status] || 'badge-draft') + '">' + (labels[status] || status) + '</span>';
  },

  dropdown(id, options, selectedValue, placeholder, extraClass) {
    const selected = options.find(o => o.value === selectedValue);
    const displayText = selected ? Components.escapeHtml(selected.label) : (placeholder || 'Select...');
    let html = '<div class="custom-dropdown ' + (extraClass || '') + '" id="' + id + '" data-testid="' + id + '">';
    html += '<div class="dropdown-trigger" data-dropdown="' + id + '">';
    html += '<span class="dropdown-text">' + displayText + '</span>';
    html += '<span class="dropdown-arrow">&#9662;</span>';
    html += '</div>';
    html += '<div class="dropdown-menu" id="' + id + '-menu">';
    options.forEach(opt => {
      const isActive = opt.value === selectedValue ? ' active' : '';
      html += '<div class="dropdown-item' + isActive + '" data-value="' + Components.escapeHtml(opt.value) + '" data-dropdown-id="' + id + '">' + Components.escapeHtml(opt.label) + '</div>';
    });
    html += '</div></div>';
    return html;
  },

  searchableDropdown(id, options, selectedValue, placeholder) {
    const selected = options.find(o => o.value === selectedValue);
    const displayText = selected ? Components.escapeHtml(selected.label) : '';
    let html = '<div class="custom-dropdown searchable-dropdown" id="' + id + '" data-testid="' + id + '">';
    html += '<input type="text" class="dropdown-search-input" id="' + id + '-input" data-searchable-dropdown="' + id + '" placeholder="' + (placeholder || 'Search...') + '" value="' + displayText + '" autocomplete="off" />';
    html += '<div class="dropdown-menu" id="' + id + '-menu">';
    options.forEach(opt => {
      const isActive = opt.value === selectedValue ? ' active' : '';
      html += '<div class="dropdown-item' + isActive + '" data-value="' + Components.escapeHtml(opt.value) + '" data-dropdown-id="' + id + '">' + Components.escapeHtml(opt.label) + '</div>';
    });
    html += '</div></div>';
    return html;
  },

  toggle(id, checked, label) {
    let html = '<label class="toggle-row" data-testid="' + id + '">';
    html += '<span class="toggle-label">' + Components.escapeHtml(label) + '</span>';
    html += '<span class="toggle-switch">';
    html += '<input type="checkbox" id="' + id + '" ' + (checked ? 'checked' : '') + ' />';
    html += '<span class="toggle-slider"></span>';
    html += '</span></label>';
    return html;
  },

  textInput(id, value, placeholder, type) {
    return '<input type="' + (type || 'text') + '" class="form-input" id="' + id + '" data-testid="' + id + '" value="' + Components.escapeHtml(value || '') + '" placeholder="' + Components.escapeHtml(placeholder || '') + '" />';
  },

  dateInput(id, value) {
    return '<input type="text" class="form-input date-input" id="' + id + '" data-testid="' + id + '" value="' + Components.escapeHtml(value || '') + '" placeholder="YYYY-MM-DD" pattern="\\d{4}-\\d{2}-\\d{2}" />';
  },

  textarea(id, value, placeholder, rows) {
    return '<textarea class="form-textarea" id="' + id + '" data-testid="' + id + '" placeholder="' + Components.escapeHtml(placeholder || '') + '" rows="' + (rows || 3) + '">' + Components.escapeHtml(value || '') + '</textarea>';
  },

  button(label, action, style, extraAttrs) {
    const cls = style === 'primary' ? 'btn btn-primary' : style === 'danger' ? 'btn btn-danger' : style === 'success' ? 'btn btn-success' : 'btn btn-secondary';
    return '<button class="' + cls + '" data-action="' + action + '"' + (extraAttrs || '') + '>' + Components.escapeHtml(label) + '</button>';
  },

  iconButton(icon, action, title, extraAttrs) {
    return '<button class="btn-icon" data-action="' + action + '" title="' + Components.escapeHtml(title || '') + '"' + (extraAttrs || '') + '>' + icon + '</button>';
  },

  modal(id, title, bodyHtml, footerHtml) {
    let html = '<div class="modal-backdrop" id="' + id + '-backdrop" data-action="close-modal" data-modal-id="' + id + '">';
    html += '<div class="modal" id="' + id + '">';
    html += '<div class="modal-header"><h3>' + Components.escapeHtml(title) + '</h3>';
    html += '<button class="modal-close" data-action="close-modal" data-modal-id="' + id + '">&times;</button></div>';
    html += '<div class="modal-body">' + bodyHtml + '</div>';
    if (footerHtml) html += '<div class="modal-footer">' + footerHtml + '</div>';
    html += '</div></div>';
    return html;
  },

  toast(message, type) {
    const cls = type === 'error' ? 'toast-error' : type === 'warning' ? 'toast-warning' : 'toast-success';
    return '<div class="toast ' + cls + '"><span class="toast-message">' + Components.escapeHtml(message) + '</span><button class="toast-close" data-action="close-toast">&times;</button></div>';
  },

  showToast(message, type) {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const div = document.createElement('div');
    div.innerHTML = Components.toast(message, type || 'success');
    container.appendChild(div.firstChild);
    setTimeout(() => {
      const toast = container.querySelector('.toast');
      if (toast) toast.remove();
    }, 4000);
  },

  emptyState(icon, title, message, actionLabel, actionName) {
    let html = '<div class="empty-state">';
    html += '<div class="empty-icon">' + icon + '</div>';
    html += '<h3>' + Components.escapeHtml(title) + '</h3>';
    html += '<p>' + Components.escapeHtml(message) + '</p>';
    if (actionLabel) {
      html += '<button class="btn btn-primary" data-action="' + actionName + '">' + Components.escapeHtml(actionLabel) + '</button>';
    }
    html += '</div>';
    return html;
  },

  confirmDialog(title, message, confirmAction, confirmLabel) {
    const body = '<p>' + Components.escapeHtml(message) + '</p>';
    const footer = '<button class="btn btn-secondary" data-action="close-modal" data-modal-id="confirmModal">Cancel</button> ' +
      '<button class="btn btn-danger" data-action="' + confirmAction + '">'+Components.escapeHtml(confirmLabel || 'Confirm')+'</button>';
    return Components.modal('confirmModal', title, body, footer);
  },

  pagination(currentPage, totalItems, pageSize) {
    const totalPages = Math.ceil(totalItems / pageSize);
    if (totalPages <= 1) return '';
    const start = (currentPage - 1) * pageSize + 1;
    const end = Math.min(currentPage * pageSize, totalItems);
    let html = '<div class="pagination">';
    html += '<span class="pagination-info">Showing ' + start + '-' + end + ' of ' + totalItems + '</span>';
    html += '<button class="btn-icon pagination-prev" data-action="prev-page"' + (currentPage <= 1 ? ' disabled' : '') + '>&#8249;</button>';
    html += '<button class="btn-icon pagination-next" data-action="next-page"' + (currentPage >= totalPages ? ' disabled' : '') + '>&#8250;</button>';
    html += '</div>';
    return html;
  },

  tabs(tabs, activeTab) {
    let html = '<div class="tabs">';
    tabs.forEach(tab => {
      const active = tab.id === activeTab ? ' active' : '';
      const count = tab.count !== undefined ? ' <span class="tab-count">(' + tab.count + ')</span>' : '';
      html += '<button class="tab' + active + '" data-action="switch-tab" data-tab="' + tab.id + '">' + Components.escapeHtml(tab.label) + count + '</button>';
    });
    html += '</div>';
    return html;
  },

  tableHeader(columns) {
    let html = '<thead><tr>';
    columns.forEach(col => {
      const style = col.width ? ' style="width:' + col.width + '"' : '';
      const cls = col.align ? ' class="text-' + col.align + '"' : '';
      html += '<th' + style + cls + '>' + Components.escapeHtml(col.label) + '</th>';
    });
    html += '</tr></thead>';
    return html;
  },

  avatar(name) {
    const initials = (name || '?').split(' ').map(w => w[0]).join('').substring(0, 2).toUpperCase();
    const colors = ['#1a73e8', '#e8710a', '#0d652d', '#b31412', '#7b1fa2', '#00796b', '#c2185b', '#455a64'];
    const hash = name ? name.split('').reduce((a, c) => a + c.charCodeAt(0), 0) : 0;
    const color = colors[hash % colors.length];
    return '<div class="avatar" style="background:' + color + '">' + initials + '</div>';
  }
};

/* ================================================================
   Shopify Theme Editor — Custom UI Components
   ================================================================ */

const Components = {

  // ── Utility ─────────────────────────────────────────────────
  escapeHtml(str) {
    if (str == null) return '';
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  },

  escapeAttr(str) {
    if (str == null) return '';
    return String(str).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  },

  // ── Toast ───────────────────────────────────────────────────
  showToast(message, type = 'info', duration = 3000) {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add('visible'));
    setTimeout(() => {
      toast.classList.remove('visible');
      setTimeout(() => toast.remove(), 300);
    }, duration);
  },

  // ── Modal ───────────────────────────────────────────────────
  showModal(title, bodyHtml, footerHtml, opts = {}) {
    const overlay = document.getElementById('modalOverlay');
    const titleEl = document.getElementById('modalTitle');
    const bodyEl = document.getElementById('modalBody');
    const footerEl = document.getElementById('modalFooter');
    if (!overlay) return;
    titleEl.textContent = title;
    bodyEl.innerHTML = bodyHtml;
    footerEl.innerHTML = footerHtml || '';
    overlay.classList.add('active');
    if (opts.onOpen) opts.onOpen();
  },

  closeModal() {
    const overlay = document.getElementById('modalOverlay');
    if (overlay) overlay.classList.remove('active');
  },

  confirm(title, message, onConfirm) {
    this.showModal(title,
      `<p>${this.escapeHtml(message)}</p>`,
      `<button class="btn btn-secondary" data-modal-cancel>Cancel</button>
       <button class="btn btn-danger" data-modal-confirm>Confirm</button>`,
      {
        onOpen: () => {
          const overlay = document.getElementById('modalOverlay');
          overlay.querySelector('[data-modal-cancel]').onclick = () => this.closeModal();
          overlay.querySelector('[data-modal-confirm]').onclick = () => { this.closeModal(); onConfirm(); };
        }
      }
    );
  },

  // ── Custom Dropdown ─────────────────────────────────────────
  dropdown(id, options, selectedValue, opts = {}) {
    const placeholder = opts.placeholder || 'Select...';
    const searchable = opts.searchable || false;
    const selectedOpt = options.find(o => o.value === selectedValue);
    const displayText = selectedOpt ? this.escapeHtml(selectedOpt.label) : placeholder;

    let searchHtml = '';
    if (searchable) {
      searchHtml = `<input type="text" class="dropdown-search-input" placeholder="Search..." />`;
    }

    const optionsHtml = options.map(o =>
      `<div class="dropdown-item${o.value === selectedValue ? ' selected' : ''}" data-value="${this.escapeAttr(o.value)}">${this.escapeHtml(o.label)}</div>`
    ).join('');

    return `<div class="custom-dropdown" id="${id}" data-dropdown-id="${id}">
      <div class="dropdown-trigger" tabindex="0">${displayText}<span class="dropdown-arrow">&#9662;</span></div>
      <div class="dropdown-menu">
        ${searchHtml}
        <div class="dropdown-options">${optionsHtml}</div>
      </div>
    </div>`;
  },

  // ── Color Picker (hex input + swatch) ───────────────────────
  colorPicker(id, value, opts = {}) {
    const label = opts.label || '';
    const swatchStyle = value ? `background:${this.escapeAttr(value)}` : 'background:#ffffff';
    return `<div class="color-picker-field" data-color-picker-id="${id}">
      ${label ? `<label class="field-label">${this.escapeHtml(label)}</label>` : ''}
      <div class="color-picker-row">
        <div class="color-swatch" style="${swatchStyle}"></div>
        <input type="text" class="color-hex-input" id="${id}" value="${this.escapeAttr(value || '')}" placeholder="#000000" data-color-input="${id}" />
      </div>
    </div>`;
  },

  // ── Range Slider ────────────────────────────────────────────
  rangeSlider(id, value, min, max, opts = {}) {
    const step = opts.step || 1;
    const label = opts.label || '';
    const unit = opts.unit || '';
    return `<div class="range-slider-field">
      ${label ? `<label class="field-label">${this.escapeHtml(label)}</label>` : ''}
      <div class="range-slider-row">
        <input type="range" id="${id}" class="range-slider" min="${min}" max="${max}" step="${step}" value="${value}" data-range-id="${id}" />
        <span class="range-value" data-range-value="${id}">${value}${unit}</span>
      </div>
    </div>`;
  },

  // ── Toggle Switch ───────────────────────────────────────────
  toggleSwitch(id, checked, opts = {}) {
    const label = opts.label || '';
    return `<div class="toggle-field">
      <label class="toggle-label" for="${id}">
        <span class="toggle-text">${this.escapeHtml(label)}</span>
        <div class="toggle-switch${checked ? ' active' : ''}" data-toggle-id="${id}">
          <div class="toggle-knob"></div>
        </div>
        <input type="checkbox" id="${id}" class="toggle-input" ${checked ? 'checked' : ''} style="display:none" />
      </label>
    </div>`;
  },

  // ── Text Input ──────────────────────────────────────────────
  textInput(id, value, opts = {}) {
    const label = opts.label || '';
    const placeholder = opts.placeholder || '';
    const multiline = opts.multiline || false;
    const inputHtml = multiline
      ? `<textarea id="${id}" class="text-input" placeholder="${this.escapeAttr(placeholder)}" rows="4">${this.escapeHtml(value || '')}</textarea>`
      : `<input type="text" id="${id}" class="text-input" value="${this.escapeAttr(value || '')}" placeholder="${this.escapeAttr(placeholder)}" />`;
    return `<div class="text-input-field">
      ${label ? `<label class="field-label" for="${id}">${this.escapeHtml(label)}</label>` : ''}
      ${inputHtml}
    </div>`;
  },

  // ── Number Input ────────────────────────────────────────────
  numberInput(id, value, opts = {}) {
    const label = opts.label || '';
    const min = opts.min != null ? `min="${opts.min}"` : '';
    const max = opts.max != null ? `max="${opts.max}"` : '';
    const step = opts.step != null ? `step="${opts.step}"` : '';
    return `<div class="text-input-field">
      ${label ? `<label class="field-label" for="${id}">${this.escapeHtml(label)}</label>` : ''}
      <input type="number" id="${id}" class="text-input" value="${value}" ${min} ${max} ${step} />
    </div>`;
  },

  // ── Section Tree Item ───────────────────────────────────────
  sectionTreeItem(section, isSelected) {
    const visIcon = section.visible ? '&#128065;' : '&#128065;&#xFE0E;';
    const visClass = section.visible ? 'visible' : 'hidden';
    const selClass = isSelected ? ' selected' : '';
    const blocksHtml = section.blocks
      .sort((a, b) => a.order - b.order)
      .map(block => {
        const bSel = AppState.selectedBlockId === block.id ? ' selected' : '';
        const bVis = block.visible ? 'visible' : 'hidden';
        return `<div class="tree-block${bSel}" data-block-id="${block.id}">
          <span class="tree-block-name" data-select-block="${block.id}">${this.escapeHtml(block.name)}</span>
          <button class="tree-vis-btn ${bVis}" data-toggle-block-vis="${block.id}" title="Toggle visibility">${block.visible ? '&#128065;' : '&#128065;&#xFE0E;'}</button>
        </div>`;
      }).join('');

    return `<div class="tree-section${selClass}" data-section-id="${section.id}">
      <div class="tree-section-header">
        <span class="tree-drag-handle">&#9776;</span>
        <span class="tree-section-name" data-select-section="${section.id}">${this.escapeHtml(section.name)}</span>
        <button class="tree-vis-btn ${visClass}" data-toggle-section-vis="${section.id}" title="Toggle visibility">${visIcon}</button>
      </div>
      <div class="tree-section-blocks">${blocksHtml}</div>
    </div>`;
  },

  // ── Section Type Picker Modal ───────────────────────────────
  showSectionTypePicker(onSelect) {
    const categories = {};
    AVAILABLE_SECTION_TYPES.forEach(t => {
      if (!categories[t.category]) categories[t.category] = [];
      categories[t.category].push(t);
    });

    let bodyHtml = '<div class="section-type-picker">';
    for (const [cat, types] of Object.entries(categories)) {
      bodyHtml += `<div class="section-type-category"><h4>${this.escapeHtml(cat)}</h4>`;
      types.forEach(t => {
        bodyHtml += `<button class="section-type-option" data-section-type="${t.type}">${this.escapeHtml(t.name)}</button>`;
      });
      bodyHtml += '</div>';
    }
    bodyHtml += '</div>';

    this.showModal('Add section', bodyHtml, '', {
      onOpen: () => {
        document.querySelectorAll('[data-section-type]').forEach(btn => {
          btn.onclick = () => {
            this.closeModal();
            onSelect(btn.dataset.sectionType);
          };
        });
      }
    });
  },

  // ── Block Type Picker Modal ─────────────────────────────────
  showBlockTypePicker(sectionType, onSelect) {
    const types = BLOCK_TYPES[sectionType] || [];
    if (types.length === 0) {
      this.showToast('No block types available for this section', 'warning');
      return;
    }

    let bodyHtml = '<div class="block-type-picker">';
    types.forEach(t => {
      bodyHtml += `<button class="section-type-option" data-block-type="${t.type}">${this.escapeHtml(t.name)}</button>`;
    });
    bodyHtml += '</div>';

    this.showModal('Add block', bodyHtml, '', {
      onOpen: () => {
        document.querySelectorAll('[data-block-type]').forEach(btn => {
          btn.onclick = () => {
            this.closeModal();
            onSelect(btn.dataset.blockType);
          };
        });
      }
    });
  }
};

// ── Global event delegation for dropdowns ─────────────────────────
document.addEventListener('click', function(e) {
  // Toggle dropdown
  const trigger = e.target.closest('.dropdown-trigger');
  if (trigger) {
    const dropdown = trigger.closest('.custom-dropdown');
    const wasOpen = dropdown.classList.contains('open');
    // Close all dropdowns first
    document.querySelectorAll('.custom-dropdown.open').forEach(d => d.classList.remove('open'));
    if (!wasOpen) {
      dropdown.classList.add('open');
      const searchInput = dropdown.querySelector('.dropdown-search-input');
      if (searchInput) { searchInput.value = ''; searchInput.focus(); }
    }
    return;
  }

  // Select dropdown item
  const item = e.target.closest('.dropdown-item');
  if (item) {
    const dropdown = item.closest('.custom-dropdown');
    const value = item.dataset.value;
    const label = item.textContent;
    const trigger = dropdown.querySelector('.dropdown-trigger');
    trigger.innerHTML = Components.escapeHtml(label) + '<span class="dropdown-arrow">&#9662;</span>';
    dropdown.querySelectorAll('.dropdown-item').forEach(i => i.classList.remove('selected'));
    item.classList.add('selected');
    dropdown.classList.remove('open');
    dropdown.dispatchEvent(new CustomEvent('change', { detail: { value } }));
    return;
  }

  // Toggle switch
  const toggle = e.target.closest('.toggle-switch');
  if (toggle) {
    toggle.classList.toggle('active');
    const input = toggle.parentElement.querySelector('.toggle-input');
    if (input) {
      input.checked = toggle.classList.contains('active');
      input.dispatchEvent(new Event('change', { bubbles: true }));
    }
    return;
  }

  // Close dropdowns on outside click
  if (!e.target.closest('.custom-dropdown')) {
    document.querySelectorAll('.custom-dropdown.open').forEach(d => d.classList.remove('open'));
  }
});

// Dropdown search filtering
document.addEventListener('input', function(e) {
  if (e.target.classList.contains('dropdown-search-input')) {
    const query = e.target.value.toLowerCase();
    const options = e.target.closest('.dropdown-menu').querySelectorAll('.dropdown-item');
    options.forEach(opt => {
      opt.style.display = opt.textContent.toLowerCase().includes(query) ? '' : 'none';
    });
  }
});

// Color swatch update on hex input
document.addEventListener('input', function(e) {
  if (e.target.classList.contains('color-hex-input')) {
    const field = e.target.closest('.color-picker-field');
    if (field) {
      const swatch = field.querySelector('.color-swatch');
      if (swatch && e.target.value) {
        swatch.style.background = e.target.value;
      }
    }
  }
});

// Range slider value display
document.addEventListener('input', function(e) {
  if (e.target.classList.contains('range-slider')) {
    const id = e.target.dataset.rangeId;
    const valueEl = document.querySelector(`[data-range-value="${id}"]`);
    if (valueEl) {
      const unit = valueEl.textContent.replace(/[\d.]+/, '').trim();
      valueEl.textContent = e.target.value + (unit || '');
    }
  }
});

// Modal overlay close
document.addEventListener('click', function(e) {
  if (e.target.id === 'modalOverlay') {
    Components.closeModal();
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    Components.closeModal();
  }
});

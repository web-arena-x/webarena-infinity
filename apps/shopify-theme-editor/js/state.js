/* ================================================================
   Shopify Theme Editor — State Management
   ================================================================ */

const STORAGE_KEY = 'shopifyThemeEditorState';

// ── Load persisted data from localStorage ─────────────────────────
function _loadPersistedData() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (parsed._seedVersion !== SEED_DATA_VERSION) {
      localStorage.removeItem(STORAGE_KEY);
      return null;
    }
    return parsed;
  } catch (e) {
    localStorage.removeItem(STORAGE_KEY);
    return null;
  }
}

// ── Build initial data from seed constants ────────────────────────
function _loadSeedData() {
  return {
    _seedVersion: SEED_DATA_VERSION,
    theme: { name: "Dawn", status: "Live" },
    themeSettings: JSON.parse(JSON.stringify(THEME_SETTINGS)),
    templates: JSON.parse(JSON.stringify(TEMPLATES)),
    sections: JSON.parse(JSON.stringify(SECTIONS)),
    products: JSON.parse(JSON.stringify(PRODUCTS)),
    collections: JSON.parse(JSON.stringify(COLLECTIONS)),
    markets: JSON.parse(JSON.stringify(MARKETS)),
    _nextSectionId: _nextSectionId,
    _nextBlockId: _nextBlockId,
    _nextColorSchemeId: _nextColorSchemeId
  };
}

const _initial = _loadPersistedData() || _loadSeedData();

// ── AppState ──────────────────────────────────────────────────────
const AppState = {
  // --- Persisted data ---
  _seedVersion: _initial._seedVersion,
  theme: _initial.theme,
  themeSettings: _initial.themeSettings,
  templates: _initial.templates,
  sections: _initial.sections,
  products: _initial.products,
  collections: _initial.collections,
  markets: _initial.markets,
  _nextSectionId: _initial._nextSectionId,
  _nextBlockId: _initial._nextBlockId,
  _nextColorSchemeId: _initial._nextColorSchemeId,

  // --- Transient UI state (NOT persisted) ---
  currentTemplate: "home",
  selectedSectionId: null,
  selectedBlockId: null,
  sidebarView: "sections",       // "sections" | "themeSettings"
  themeSettingsCategory: null,    // current theme settings category being edited
  screenSize: "desktop",         // "desktop" | "mobile" | "fullscreen"
  previewInspectorActive: false,
  undoStack: [],
  redoStack: [],
  hasUnsavedChanges: false,

  // --- Listeners ---
  _listeners: [],
  subscribe(fn) { this._listeners.push(fn); },
  notify() {
    this._listeners.forEach(fn => fn(this));
    this._persist();
  },

  // ── Persistence ─────────────────────────────────────────────
  _getPersistable() {
    return {
      _seedVersion: this._seedVersion,
      theme: this.theme,
      themeSettings: this.themeSettings,
      templates: this.templates,
      sections: this.sections,
      products: this.products,
      collections: this.collections,
      markets: this.markets,
      _nextSectionId: this._nextSectionId,
      _nextBlockId: this._nextBlockId,
      _nextColorSchemeId: this._nextColorSchemeId
    };
  },

  _persist() {
    const data = this._getPersistable();
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); } catch(e) {}
    this._pushStateToServer(data);
  },

  _pushStateToServer(data) {
    fetch('/api/state', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).catch(() => {});
  },

  resetToSeedData() {
    localStorage.removeItem(STORAGE_KEY);
    const seed = _loadSeedData();
    Object.assign(this, seed);
    this.currentTemplate = "home";
    this.selectedSectionId = null;
    this.selectedBlockId = null;
    this.sidebarView = "sections";
    this.themeSettingsCategory = null;
    this.undoStack = [];
    this.redoStack = [];
    this.hasUnsavedChanges = false;
    this.notify();
  },

  // ── Undo / Redo ─────────────────────────────────────────────
  _pushUndo() {
    this.undoStack.push(JSON.stringify(this._getPersistable()));
    if (this.undoStack.length > 50) this.undoStack.shift();
    this.redoStack = [];
    this.hasUnsavedChanges = true;
  },

  undo() {
    if (this.undoStack.length === 0) return;
    this.redoStack.push(JSON.stringify(this._getPersistable()));
    const prev = JSON.parse(this.undoStack.pop());
    Object.assign(this, prev);
    this.notify();
  },

  redo() {
    if (this.redoStack.length === 0) return;
    this.undoStack.push(JSON.stringify(this._getPersistable()));
    const next = JSON.parse(this.redoStack.pop());
    Object.assign(this, next);
    this.notify();
  },

  save() {
    this.undoStack = [];
    this.redoStack = [];
    this.hasUnsavedChanges = false;
    this.notify();
  },

  // ── Section queries ─────────────────────────────────────────
  getSectionsForTemplate(templateId) {
    return this.sections
      .filter(s => s.templateId === templateId)
      .sort((a, b) => {
        const groupOrder = { header: 0, template: 1, footer: 2 };
        if (groupOrder[a.group] !== groupOrder[b.group])
          return groupOrder[a.group] - groupOrder[b.group];
        return a.order - b.order;
      });
  },

  getSectionsByGroup(templateId, group) {
    return this.sections
      .filter(s => s.templateId === templateId && s.group === group)
      .sort((a, b) => a.order - b.order);
  },

  getSection(sectionId) {
    return this.sections.find(s => s.id === sectionId);
  },

  getBlock(blockId) {
    for (const section of this.sections) {
      const block = section.blocks.find(b => b.id === blockId);
      if (block) return block;
    }
    return null;
  },

  // ── Section mutations ───────────────────────────────────────
  addSection(templateId, group, sectionType) {
    this._pushUndo();
    const typeDef = AVAILABLE_SECTION_TYPES.find(t => t.type === sectionType);
    if (!typeDef) return null;

    const existing = this.getSectionsByGroup(templateId, group);
    const newOrder = existing.length > 0 ? Math.max(...existing.map(s => s.order)) + 1 : 0;
    const sectionId = "section_" + this._nextSectionId;
    this._nextSectionId++;

    const section = {
      id: sectionId,
      type: sectionType,
      name: typeDef.name,
      templateId: templateId,
      group: group,
      order: newOrder,
      visible: true,
      collapsed: false,
      settings: { colorSchemeId: "scheme_1" },
      blocks: []
    };

    this.sections.push(section);
    this.selectedSectionId = sectionId;
    this.selectedBlockId = null;
    this.notify();
    return sectionId;
  },

  removeSection(sectionId) {
    this._pushUndo();
    this.sections = this.sections.filter(s => s.id !== sectionId);
    if (this.selectedSectionId === sectionId) {
      this.selectedSectionId = null;
      this.selectedBlockId = null;
    }
    this.notify();
  },

  moveSectionUp(sectionId) {
    this._pushUndo();
    const section = this.getSection(sectionId);
    if (!section) return;
    const group = this.getSectionsByGroup(section.templateId, section.group);
    const idx = group.findIndex(s => s.id === sectionId);
    if (idx <= 0) return;

    const prev = group[idx - 1];
    const tmpOrder = section.order;
    section.order = prev.order;
    prev.order = tmpOrder;
    this.notify();
  },

  moveSectionDown(sectionId) {
    this._pushUndo();
    const section = this.getSection(sectionId);
    if (!section) return;
    const group = this.getSectionsByGroup(section.templateId, section.group);
    const idx = group.findIndex(s => s.id === sectionId);
    if (idx < 0 || idx >= group.length - 1) return;

    const next = group[idx + 1];
    const tmpOrder = section.order;
    section.order = next.order;
    next.order = tmpOrder;
    this.notify();
  },

  toggleSectionVisibility(sectionId) {
    this._pushUndo();
    const section = this.getSection(sectionId);
    if (section) {
      section.visible = !section.visible;
      this.notify();
    }
  },

  duplicateSection(sectionId) {
    this._pushUndo();
    const src = this.getSection(sectionId);
    if (!src) return null;

    const newSectionId = "section_" + this._nextSectionId;
    this._nextSectionId++;

    const group = this.getSectionsByGroup(src.templateId, src.group);
    const newOrder = Math.max(...group.map(s => s.order)) + 1;

    const newBlocks = src.blocks.map(b => {
      const newBlockId = "block_" + this._nextBlockId;
      this._nextBlockId++;
      return { ...JSON.parse(JSON.stringify(b)), id: newBlockId, sectionId: newSectionId };
    });

    const newSection = {
      ...JSON.parse(JSON.stringify(src)),
      id: newSectionId,
      name: src.name + " (copy)",
      order: newOrder,
      blocks: newBlocks
    };

    this.sections.push(newSection);
    this.notify();
    return newSectionId;
  },

  updateSectionSettings(sectionId, settings) {
    this._pushUndo();
    const section = this.getSection(sectionId);
    if (section) {
      Object.assign(section.settings, settings);
      this.notify();
    }
  },

  updateSectionName(sectionId, name) {
    this._pushUndo();
    const section = this.getSection(sectionId);
    if (section) {
      section.name = name;
      this.notify();
    }
  },

  // ── Block mutations ─────────────────────────────────────────
  addBlock(sectionId, blockType) {
    this._pushUndo();
    const section = this.getSection(sectionId);
    if (!section) return null;

    const blockTypes = BLOCK_TYPES[section.type] || [];
    const typeDef = blockTypes.find(bt => bt.type === blockType);
    if (!typeDef) return null;

    const newBlockId = "block_" + this._nextBlockId;
    this._nextBlockId++;

    const newOrder = section.blocks.length > 0 ? Math.max(...section.blocks.map(b => b.order)) + 1 : 0;

    const block = {
      id: newBlockId,
      type: blockType,
      name: typeDef.name,
      sectionId: sectionId,
      order: newOrder,
      visible: true,
      settings: {}
    };

    section.blocks.push(block);
    this.selectedBlockId = newBlockId;
    this.notify();
    return newBlockId;
  },

  removeBlock(blockId) {
    this._pushUndo();
    for (const section of this.sections) {
      const idx = section.blocks.findIndex(b => b.id === blockId);
      if (idx !== -1) {
        section.blocks.splice(idx, 1);
        if (this.selectedBlockId === blockId) {
          this.selectedBlockId = null;
        }
        this.notify();
        return;
      }
    }
  },

  moveBlockUp(blockId) {
    this._pushUndo();
    const block = this.getBlock(blockId);
    if (!block) return;
    const section = this.getSection(block.sectionId);
    if (!section) return;

    const sorted = [...section.blocks].sort((a, b) => a.order - b.order);
    const idx = sorted.findIndex(b => b.id === blockId);
    if (idx <= 0) return;

    const prev = sorted[idx - 1];
    const tmpOrder = block.order;
    block.order = prev.order;
    prev.order = tmpOrder;
    this.notify();
  },

  moveBlockDown(blockId) {
    this._pushUndo();
    const block = this.getBlock(blockId);
    if (!block) return;
    const section = this.getSection(block.sectionId);
    if (!section) return;

    const sorted = [...section.blocks].sort((a, b) => a.order - b.order);
    const idx = sorted.findIndex(b => b.id === blockId);
    if (idx < 0 || idx >= sorted.length - 1) return;

    const next = sorted[idx + 1];
    const tmpOrder = block.order;
    block.order = next.order;
    next.order = tmpOrder;
    this.notify();
  },

  toggleBlockVisibility(blockId) {
    this._pushUndo();
    const block = this.getBlock(blockId);
    if (block) {
      block.visible = !block.visible;
      this.notify();
    }
  },

  duplicateBlock(blockId) {
    this._pushUndo();
    const block = this.getBlock(blockId);
    if (!block) return null;
    const section = this.getSection(block.sectionId);
    if (!section) return null;

    const newBlockId = "block_" + this._nextBlockId;
    this._nextBlockId++;

    const newOrder = Math.max(...section.blocks.map(b => b.order)) + 1;
    const newBlock = {
      ...JSON.parse(JSON.stringify(block)),
      id: newBlockId,
      order: newOrder
    };

    section.blocks.push(newBlock);
    this.notify();
    return newBlockId;
  },

  updateBlockSettings(blockId, settings) {
    this._pushUndo();
    const block = this.getBlock(blockId);
    if (block) {
      Object.assign(block.settings, settings);
      this.notify();
    }
  },

  // ── Theme settings mutations ────────────────────────────────
  updateThemeSettings(category, values) {
    this._pushUndo();
    if (typeof this.themeSettings[category] === 'object' && this.themeSettings[category] !== null) {
      Object.assign(this.themeSettings[category], values);
    } else {
      this.themeSettings[category] = values;
    }
    this.notify();
  },

  addColorScheme() {
    this._pushUndo();
    const newId = "scheme_" + this._nextColorSchemeId;
    this._nextColorSchemeId++;
    const scheme = {
      id: newId,
      name: "Scheme " + newId.split('_')[1],
      background: "#ffffff",
      backgroundGradient: "",
      text: "#121212",
      solidButtonBackground: "#121212",
      solidButtonLabel: "#ffffff",
      outlineButton: "#121212",
      shadow: "#121212"
    };
    this.themeSettings.colors.schemes.push(scheme);
    this.notify();
    return newId;
  },

  removeColorScheme(schemeId) {
    this._pushUndo();
    this.themeSettings.colors.schemes = this.themeSettings.colors.schemes.filter(s => s.id !== schemeId);
    this.notify();
  },

  updateColorScheme(schemeId, values) {
    this._pushUndo();
    const scheme = this.themeSettings.colors.schemes.find(s => s.id === schemeId);
    if (scheme) {
      Object.assign(scheme, values);
      this.notify();
    }
  },

  // ── Theme style ─────────────────────────────────────────────
  applyThemeStyle(styleId) {
    this._pushUndo();
    const style = THEME_STYLES.find(s => s.id === styleId);
    if (!style) return;

    // Apply style settings over current theme settings
    if (style.settings.typography) {
      Object.assign(this.themeSettings.typography, style.settings.typography);
    }
    if (style.settings.buttons) {
      Object.assign(this.themeSettings.buttons, style.settings.buttons);
    }
    if (style.settings.animations) {
      Object.assign(this.themeSettings.animations, style.settings.animations);
    }
    this.themeSettings.activeThemeStyle = styleId;
    this.notify();
  },

  // ── Resource mutations ──────────────────────────────────────
  updateProduct(productId, values) {
    this._pushUndo();
    const product = this.products.find(p => p.id === productId);
    if (product) {
      Object.assign(product, values);
      this.notify();
    }
  },

  updateCollection(collectionId, values) {
    this._pushUndo();
    const collection = this.collections.find(c => c.id === collectionId);
    if (collection) {
      Object.assign(collection, values);
      this.notify();
    }
  }
};

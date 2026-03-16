// Figma Text & Typography - State Management
const AppState = {
    // Persistent data
    textLayers: [],
    textStyles: [],
    fontFamilies: [],
    preferences: {},
    fileInfo: null,
    currentUser: null,

    // ID counters
    _nextTextLayerId: 100,
    _nextTextStyleId: 100,
    _nextLinkId: 100,

    // UI state (transient, not persisted)
    currentSection: 'layers',
    selectedLayerId: null,
    activeModal: null,
    modalData: null,
    toastMessage: null,
    searchQuery: '',
    fontSearchQuery: '',
    fontFilter: 'all',
    editingField: null,
    expandedOpenTypeCategory: null,
    activeTab: 'basics',

    // Observer pattern
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
        if (persisted) {
            this.textLayers = persisted.textLayers || [];
            this.textStyles = persisted.textStyles || [];
            this.fontFamilies = persisted.fontFamilies || [];
            this.preferences = persisted.preferences || {};
            this.fileInfo = persisted.fileInfo || null;
            this.currentUser = persisted.currentUser || null;
            this._nextTextLayerId = persisted._nextTextLayerId || 100;
            this._nextTextStyleId = persisted._nextTextStyleId || 100;
            this._nextLinkId = persisted._nextLinkId || 100;
        } else {
            this._loadSeedData();
        }
    },

    _loadSeedData() {
        this.textLayers = JSON.parse(JSON.stringify(TEXT_LAYERS));
        this.textStyles = JSON.parse(JSON.stringify(TEXT_STYLES));
        this.fontFamilies = JSON.parse(JSON.stringify(FONT_FAMILIES));
        this.preferences = JSON.parse(JSON.stringify(PREFERENCES));
        this.fileInfo = JSON.parse(JSON.stringify(FILE_INFO));
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
    },

    _loadPersistedData() {
        try {
            const saved = localStorage.getItem('figmaTextTypographyState');
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('figmaTextTypographyState');
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    },

    _persist() {
        const state = this.getSerializableState();
        localStorage.setItem('figmaTextTypographyState', JSON.stringify(state));
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
            textLayers: this.textLayers,
            textStyles: this.textStyles,
            fontFamilies: this.fontFamilies,
            preferences: this.preferences,
            fileInfo: this.fileInfo,
            currentUser: this.currentUser,
            _nextTextLayerId: this._nextTextLayerId,
            _nextTextStyleId: this._nextTextStyleId,
            _nextLinkId: this._nextLinkId
        };
    },

    resetToSeedData() {
        localStorage.removeItem('figmaTextTypographyState');
        this._loadSeedData();
        this.currentSection = 'layers';
        this.selectedLayerId = null;
        this.activeModal = null;
        this.modalData = null;
        this.toastMessage = null;
        this.searchQuery = '';
        this.fontSearchQuery = '';
        this.editingField = null;
        this.notify();
    },

    // ---- Helper getters ----

    getSelectedLayer() {
        if (!this.selectedLayerId) return null;
        return this.textLayers.find(l => l.id === this.selectedLayerId) || null;
    },

    getTextStyle(styleId) {
        if (!styleId) return null;
        return this.textStyles.find(s => s.id === styleId) || null;
    },

    getFontFamily(name) {
        return this.fontFamilies.find(f => f.name === name) || null;
    },

    getFilteredFonts() {
        let fonts = this.fontFamilies;
        const filter = this.fontFilter;

        if (filter === 'popular') {
            fonts = fonts.filter(f => f.popular);
        } else if (filter === 'installed') {
            fonts = fonts.filter(f => f.source === 'installed');
        } else if (filter === 'google') {
            fonts = fonts.filter(f => f.source === 'google');
        } else if (filter === 'variable') {
            fonts = fonts.filter(f => f.isVariable);
        } else if (filter === 'in-file') {
            const usedFonts = new Set(this.textLayers.map(l => l.fontFamily));
            fonts = fonts.filter(f => usedFonts.has(f.name));
        } else if (filter === 'organization') {
            fonts = fonts.filter(f => f.source === 'organization' || f.source === 'installed');
        }

        if (this.fontSearchQuery) {
            const q = this.fontSearchQuery.toLowerCase();
            fonts = fonts.filter(f => f.name.toLowerCase().includes(q));
        }

        return fonts;
    },

    getLayersForSearch() {
        if (!this.searchQuery) return this.textLayers;
        const q = this.searchQuery.toLowerCase();
        return this.textLayers.filter(l =>
            l.name.toLowerCase().includes(q) ||
            l.content.toLowerCase().includes(q) ||
            l.fontFamily.toLowerCase().includes(q)
        );
    },

    // ---- Layer mutations ----

    selectLayer(layerId) {
        this.selectedLayerId = layerId;
        this.editingField = null;
        this.activeTab = 'basics';
        this.expandedOpenTypeCategory = null;
    },

    createTextLayer(content) {
        const id = `tl_${String(this._nextTextLayerId++).padStart(3, '0')}`;
        const prefs = this.preferences;
        const layer = {
            id,
            name: content.substring(0, 20) || 'New Text',
            content: content || 'Type something',
            fontFamily: prefs.defaultFontFamily,
            fontStyle: prefs.defaultFontStyle,
            fontSize: prefs.defaultFontSize,
            lineHeight: JSON.parse(JSON.stringify(prefs.defaultLineHeight)),
            letterSpacing: JSON.parse(JSON.stringify(prefs.defaultLetterSpacing)),
            paragraphSpacing: 0,
            paragraphIndent: 0,
            horizontalAlign: prefs.defaultHorizontalAlign,
            verticalAlign: 'top',
            textDecoration: 'none',
            letterCase: 'none',
            textDirection: prefs.defaultTextDirection,
            resizing: 'auto-width',
            truncation: { enabled: false, maxLines: null },
            listStyle: 'none',
            listSpacing: 0,
            hangingPunctuation: false,
            hangingList: false,
            verticalTrim: false,
            links: [],
            openTypeFeatures: { liga: true, kern: true },
            textStyleId: null,
            variableAxes: {},
            width: null,
            height: null,
            x: 40,
            y: 40 + this.textLayers.length * 40,
            locked: false,
            visible: true,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        this.textLayers.push(layer);
        this.selectedLayerId = id;
        this.notify();
        return layer;
    },

    deleteTextLayer(layerId) {
        const idx = this.textLayers.findIndex(l => l.id === layerId);
        if (idx === -1) return;
        this.textLayers.splice(idx, 1);
        if (this.selectedLayerId === layerId) {
            this.selectedLayerId = null;
        }
        this.notify();
    },

    duplicateTextLayer(layerId) {
        const src = this.textLayers.find(l => l.id === layerId);
        if (!src) return;
        const id = `tl_${String(this._nextTextLayerId++).padStart(3, '0')}`;
        const copy = JSON.parse(JSON.stringify(src));
        copy.id = id;
        copy.name = src.name + ' (copy)';
        copy.y = src.y + 40;
        copy.createdAt = new Date().toISOString();
        copy.updatedAt = new Date().toISOString();
        this.textLayers.push(copy);
        this.selectedLayerId = id;
        this.notify();
    },

    updateLayerProperty(layerId, property, value) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer[property] = value;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerContent(layerId, content) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.content = content;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerFont(layerId, fontFamily, fontStyle) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.fontFamily = fontFamily;
        if (fontStyle) layer.fontStyle = fontStyle;
        const font = this.getFontFamily(fontFamily);
        if (font && font.isVariable) {
            const axes = {};
            (font.variableAxes || []).forEach(a => { axes[a.tag] = a.default; });
            layer.variableAxes = axes;
        } else {
            layer.variableAxes = {};
        }
        layer.updatedAt = new Date().toISOString();
        if (!this.preferences.recentFonts.includes(fontFamily)) {
            this.preferences.recentFonts.unshift(fontFamily);
            if (this.preferences.recentFonts.length > 10) {
                this.preferences.recentFonts.pop();
            }
        }
        this.notify();
    },

    updateLayerFontSize(layerId, size) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        const s = Math.max(1, Math.min(1000, parseFloat(size) || 16));
        layer.fontSize = s;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerLineHeight(layerId, value, unit) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        if (value === 'auto') {
            layer.lineHeight = { value: 'auto', unit: 'auto' };
        } else {
            layer.lineHeight = { value: parseFloat(value) || 0, unit: unit || layer.lineHeight.unit };
        }
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerLetterSpacing(layerId, value, unit) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.letterSpacing = { value: parseFloat(value) || 0, unit: unit || layer.letterSpacing.unit };
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerAlignment(layerId, alignment) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.horizontalAlign = alignment;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerVerticalAlignment(layerId, alignment) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.verticalAlign = alignment;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerDecoration(layerId, decoration) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.textDecoration = decoration;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerLetterCase(layerId, letterCase) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.letterCase = letterCase;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerDirection(layerId, direction) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.textDirection = direction;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerResizing(layerId, mode) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.resizing = mode;
        if (mode === 'auto-width') {
            layer.width = null;
            layer.height = null;
        } else if (mode === 'auto-height') {
            if (!layer.width) layer.width = 400;
            layer.height = null;
        } else if (mode === 'fixed') {
            if (!layer.width) layer.width = 400;
            if (!layer.height) layer.height = 200;
        }
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerTruncation(layerId, enabled, maxLines) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.truncation = {
            enabled: enabled,
            maxLines: enabled ? (parseInt(maxLines) || 3) : null
        };
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerListStyle(layerId, style) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.listStyle = style;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerListSpacing(layerId, spacing) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.listSpacing = Math.max(0, parseFloat(spacing) || 0);
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerParagraphSpacing(layerId, spacing) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.paragraphSpacing = Math.max(0, parseFloat(spacing) || 0);
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerParagraphIndent(layerId, indent) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.paragraphIndent = Math.max(0, parseFloat(indent) || 0);
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    toggleLayerHangingPunctuation(layerId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.hangingPunctuation = !layer.hangingPunctuation;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    toggleLayerHangingList(layerId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.hangingList = !layer.hangingList;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    toggleLayerVerticalTrim(layerId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.verticalTrim = !layer.verticalTrim;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    toggleLayerOpenTypeFeature(layerId, feature) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        if (!layer.openTypeFeatures) layer.openTypeFeatures = {};
        layer.openTypeFeatures[feature] = !layer.openTypeFeatures[feature];
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerVariableAxis(layerId, axisTag, value) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        if (!layer.variableAxes) layer.variableAxes = {};
        layer.variableAxes[axisTag] = parseFloat(value);
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLayerDimensions(layerId, width, height) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        if (width !== undefined) layer.width = width ? parseFloat(width) : null;
        if (height !== undefined) layer.height = height ? parseFloat(height) : null;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    toggleLayerVisibility(layerId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.visible = !layer.visible;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    toggleLayerLock(layerId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.locked = !layer.locked;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    renameLayer(layerId, name) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer || !name.trim()) return;
        layer.name = name.trim();
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    // ---- Link mutations ----

    addLink(layerId, startIndex, endIndex, url) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        const id = `lnk_${String(this._nextLinkId++).padStart(3, '0')}`;
        layer.links.push({ id, startIndex, endIndex, url });
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    removeLink(layerId, linkId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.links = layer.links.filter(l => l.id !== linkId);
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    updateLink(layerId, linkId, url) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        const link = layer.links.find(l => l.id === linkId);
        if (!link) return;
        link.url = url;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    // ---- Text Style mutations ----

    createTextStyle(name, layerId) {
        const layer = layerId ? this.textLayers.find(l => l.id === layerId) : null;
        const id = `ts_${String(this._nextTextStyleId++).padStart(3, '0')}`;
        const style = {
            id,
            name: name || 'Untitled Style',
            fontFamily: layer ? layer.fontFamily : this.preferences.defaultFontFamily,
            fontStyle: layer ? layer.fontStyle : this.preferences.defaultFontStyle,
            fontSize: layer ? layer.fontSize : this.preferences.defaultFontSize,
            lineHeight: layer ? JSON.parse(JSON.stringify(layer.lineHeight)) : JSON.parse(JSON.stringify(this.preferences.defaultLineHeight)),
            letterSpacing: layer ? JSON.parse(JSON.stringify(layer.letterSpacing)) : JSON.parse(JSON.stringify(this.preferences.defaultLetterSpacing)),
            paragraphSpacing: layer ? layer.paragraphSpacing : 0,
            paragraphIndent: layer ? layer.paragraphIndent : 0,
            textDecoration: layer ? layer.textDecoration : 'none',
            letterCase: layer ? layer.letterCase : 'none',
            listStyle: layer ? layer.listStyle : 'none',
            openTypeFeatures: layer ? JSON.parse(JSON.stringify(layer.openTypeFeatures)) : { liga: true, kern: true },
            description: '',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        this.textStyles.push(style);
        if (layer) {
            layer.textStyleId = id;
            layer.updatedAt = new Date().toISOString();
        }
        this.notify();
        return style;
    },

    updateTextStyle(styleId, updates) {
        const style = this.textStyles.find(s => s.id === styleId);
        if (!style) return;
        Object.assign(style, updates);
        style.updatedAt = new Date().toISOString();
        // Update all layers using this style
        this.textLayers.forEach(layer => {
            if (layer.textStyleId === styleId) {
                layer.fontFamily = style.fontFamily;
                layer.fontStyle = style.fontStyle;
                layer.fontSize = style.fontSize;
                layer.lineHeight = JSON.parse(JSON.stringify(style.lineHeight));
                layer.letterSpacing = JSON.parse(JSON.stringify(style.letterSpacing));
                layer.paragraphSpacing = style.paragraphSpacing;
                layer.paragraphIndent = style.paragraphIndent;
                layer.textDecoration = style.textDecoration;
                layer.letterCase = style.letterCase;
                layer.listStyle = style.listStyle;
                layer.openTypeFeatures = JSON.parse(JSON.stringify(style.openTypeFeatures));
                layer.updatedAt = new Date().toISOString();
            }
        });
        this.notify();
    },

    deleteTextStyle(styleId) {
        this.textStyles = this.textStyles.filter(s => s.id !== styleId);
        this.textLayers.forEach(layer => {
            if (layer.textStyleId === styleId) {
                layer.textStyleId = null;
            }
        });
        this.notify();
    },

    applyTextStyle(layerId, styleId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        const style = this.textStyles.find(s => s.id === styleId);
        if (!layer || !style) return;
        layer.textStyleId = styleId;
        layer.fontFamily = style.fontFamily;
        layer.fontStyle = style.fontStyle;
        layer.fontSize = style.fontSize;
        layer.lineHeight = JSON.parse(JSON.stringify(style.lineHeight));
        layer.letterSpacing = JSON.parse(JSON.stringify(style.letterSpacing));
        layer.paragraphSpacing = style.paragraphSpacing;
        layer.paragraphIndent = style.paragraphIndent;
        layer.textDecoration = style.textDecoration;
        layer.letterCase = style.letterCase;
        layer.listStyle = style.listStyle;
        layer.openTypeFeatures = JSON.parse(JSON.stringify(style.openTypeFeatures));
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    detachTextStyle(layerId) {
        const layer = this.textLayers.find(l => l.id === layerId);
        if (!layer) return;
        layer.textStyleId = null;
        layer.updatedAt = new Date().toISOString();
        this.notify();
    },

    // ---- Preference mutations ----

    updatePreference(key, value) {
        this.preferences[key] = value;
        this.notify();
    },

    // ---- Toast ----

    showToast(message) {
        this.toastMessage = message;
        this.notify();
        setTimeout(() => {
            this.toastMessage = null;
            this.notify();
        }, 3000);
    }
};

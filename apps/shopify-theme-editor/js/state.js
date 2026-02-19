// ============================================================
// state.js — Centralized state management for Shopify Theme Editor
// ============================================================

const AppState = {
    // ---- Core data (persisted) ----
    currentUser: null,
    themes: [],
    templates: [],
    sections: [],
    blocks: [],
    themeSettings: [],
    colorSchemes: [],

    // ---- ID counters ----
    _nextThemeId: 8,
    _nextTemplateId: 33,
    _nextSectionId: 42,
    _nextBlockId: 33,
    _nextColorSchemeId: 6,

    // ---- UI state (transient - not persisted) ----
    currentRoute: '/',
    routeParams: {},
    queryParams: {},
    selectedThemeId: 1,
    selectedTemplateId: null,
    selectedSectionId: null,
    selectedBlockId: null,
    sidebarOpen: true,
    modalOpen: false,
    toasts: [],
    validationErrors: {},
    editorMode: 'desktop', // desktop, mobile, fullscreen

    // ---- Subscribers ----
    _subscribers: [],

    // ---- Initialize ----
    init() {
        const persisted = this._loadPersisted();
        if (persisted) {
            this.currentUser = persisted.currentUser;
            this.themes = persisted.themes;
            this.templates = persisted.templates;
            this.sections = persisted.sections;
            this.blocks = persisted.blocks;
            this.themeSettings = persisted.themeSettings;
            this._nextThemeId = persisted._nextThemeId;
            this._nextTemplateId = persisted._nextTemplateId;
            this._nextSectionId = persisted._nextSectionId;
            this._nextBlockId = persisted._nextBlockId;
            this._nextColorSchemeId = persisted._nextColorSchemeId || 6;
        } else {
            this._loadSeedData();
        }

        // Select live theme by default
        const liveTheme = this.themes.find(t => t.status === 'live');
        if (liveTheme) {
            this.selectedThemeId = liveTheme.id;
        }

        this.notify();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.themes = JSON.parse(JSON.stringify(THEMES));
        this.templates = JSON.parse(JSON.stringify(TEMPLATES));
        this.sections = JSON.parse(JSON.stringify(SECTIONS));
        this.blocks = JSON.parse(JSON.stringify(BLOCKS));
        this.themeSettings = JSON.parse(JSON.stringify(THEME_SETTINGS));
        this._nextThemeId = 8;
        this._nextTemplateId = 33;
        this._nextSectionId = 42;
        this._nextBlockId = 33;
        this._nextColorSchemeId = 6;
    },

    // ---- Persistence ----
    _loadPersisted() {
        try {
            const saved = localStorage.getItem('shopifyThemeEditorState');
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('shopifyThemeEditorState');
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    },

    _persist() {
        const persistable = {
            _seedVersion: SEED_DATA_VERSION,
            currentUser: this.currentUser,
            themes: this.themes,
            templates: this.templates,
            sections: this.sections,
            blocks: this.blocks,
            themeSettings: this.themeSettings,
            _nextThemeId: this._nextThemeId,
            _nextTemplateId: this._nextTemplateId,
            _nextSectionId: this._nextSectionId,
            _nextBlockId: this._nextBlockId,
            _nextColorSchemeId: this._nextColorSchemeId
        };
        localStorage.setItem('shopifyThemeEditorState', JSON.stringify(persistable));
        this._pushStateToServer();
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
            currentUser: this.currentUser,
            themes: this.themes,
            templates: this.templates,
            sections: this.sections,
            blocks: this.blocks,
            themeSettings: this.themeSettings,
            _nextThemeId: this._nextThemeId,
            _nextTemplateId: this._nextTemplateId,
            _nextSectionId: this._nextSectionId,
            _nextBlockId: this._nextBlockId,
            _nextColorSchemeId: this._nextColorSchemeId
        };
    },

    // ---- Subscription ----
    subscribe(fn) {
        this._subscribers.push(fn);
        return () => {
            this._subscribers = this._subscribers.filter(s => s !== fn);
        };
    },

    notify() {
        this._persist();
        this._subscribers.forEach(fn => fn(this));
    },

    // ---- Reset ----
    resetToSeedData() {
        localStorage.removeItem('shopifyThemeEditorState');
        this._loadSeedData();
        this.currentRoute = '/';
        this.routeParams = {};
        this.queryParams = {};
        this.selectedThemeId = 1;
        this.selectedTemplateId = null;
        this.selectedSectionId = null;
        this.selectedBlockId = null;
        this.validationErrors = {};
        this.toasts = [];
    },

    // ==============================
    // Theme Management
    // ==============================

    getTheme(id) {
        return this.themes.find(t => t.id === id);
    },

    getLiveTheme() {
        return this.themes.find(t => t.status === 'live');
    },

    getSelectedTheme() {
        return this.getTheme(this.selectedThemeId);
    },

    publishTheme(themeId) {
        this.themes.forEach(t => {
            if (t.status === 'live') t.status = 'draft';
        });
        const theme = this.getTheme(themeId);
        if (theme) {
            theme.status = 'live';
            theme.updatedAt = new Date().toISOString();
        }
        this.notify();
    },

    renameTheme(themeId, newName) {
        const theme = this.getTheme(themeId);
        if (theme) {
            theme.name = newName;
            theme.updatedAt = new Date().toISOString();
            this.notify();
        }
    },

    duplicateTheme(themeId) {
        const source = this.getTheme(themeId);
        if (!source) return null;

        const newId = this._nextThemeId++;
        const newTheme = JSON.parse(JSON.stringify(source));
        newTheme.id = newId;
        newTheme.name = 'Copy of ' + source.name;
        newTheme.status = 'draft';
        newTheme.createdAt = new Date().toISOString();
        newTheme.updatedAt = new Date().toISOString();
        newTheme.lastSaved = new Date().toISOString();
        this.themes.push(newTheme);

        // Duplicate templates, sections, blocks for the new theme
        const templateMap = {};
        const sourceTemplates = this.templates.filter(t => t.themeId === themeId);
        sourceTemplates.forEach(st => {
            const newTid = this._nextTemplateId++;
            templateMap[st.id] = newTid;
            const newTemplate = JSON.parse(JSON.stringify(st));
            newTemplate.id = newTid;
            newTemplate.themeId = newId;
            this.templates.push(newTemplate);
        });

        const sectionMap = {};
        const sourceSections = this.sections.filter(s => s.themeId === themeId);
        sourceSections.forEach(ss => {
            const newSid = this._nextSectionId++;
            sectionMap[ss.id] = newSid;
            const newSection = JSON.parse(JSON.stringify(ss));
            newSection.id = newSid;
            newSection.themeId = newId;
            newSection.templateId = templateMap[ss.templateId] || ss.templateId;
            this.sections.push(newSection);
        });

        const sourceBlocks = this.blocks.filter(b => b.themeId === themeId);
        sourceBlocks.forEach(sb => {
            const newBid = this._nextBlockId++;
            const newBlock = JSON.parse(JSON.stringify(sb));
            newBlock.id = newBid;
            newBlock.themeId = newId;
            newBlock.sectionId = sectionMap[sb.sectionId] || sb.sectionId;
            this.blocks.push(newBlock);
        });

        // Duplicate theme settings
        const sourceSettings = this.themeSettings.find(ts => ts.themeId === themeId);
        if (sourceSettings) {
            const newSettings = JSON.parse(JSON.stringify(sourceSettings));
            newSettings.themeId = newId;
            this.themeSettings.push(newSettings);
        }

        this.notify();
        return newTheme;
    },

    deleteTheme(themeId) {
        const theme = this.getTheme(themeId);
        if (!theme || theme.status === 'live') return false;

        this.themes = this.themes.filter(t => t.id !== themeId);
        this.templates = this.templates.filter(t => t.themeId !== themeId);
        const sectionIds = this.sections.filter(s => s.themeId === themeId).map(s => s.id);
        this.sections = this.sections.filter(s => s.themeId !== themeId);
        this.blocks = this.blocks.filter(b => b.themeId !== themeId);
        this.themeSettings = this.themeSettings.filter(ts => ts.themeId !== themeId);

        if (this.selectedThemeId === themeId) {
            const live = this.getLiveTheme();
            this.selectedThemeId = live ? live.id : (this.themes[0]?.id || null);
        }
        this.notify();
        return true;
    },

    addTheme(name, source, architecture) {
        const newId = this._nextThemeId++;
        const theme = {
            id: newId,
            name: name,
            status: 'draft',
            version: '1.0',
            architecture: architecture || ARCHITECTURE_TYPES.ONLINE_STORE_2,
            source: source || 'shopify',
            price: 0,
            lastSaved: new Date().toISOString(),
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString(),
            updateAvailable: false,
            updateVersion: null,
            previewUrl: '',
            customCss: '',
            themeStyle: 'default'
        };
        this.themes.push(theme);

        // Add default templates for new theme
        const defaultTypes = ['product', 'collection', 'page', 'blog', 'cart', 'search'];
        defaultTypes.forEach(type => {
            const tid = this._nextTemplateId++;
            this.templates.push({
                id: tid, themeId: newId,
                name: 'Default ' + type,
                type: type,
                handle: type,
                isDefault: true
            });

            // Add header and footer sections to each template
            const hid = this._nextSectionId++;
            this.sections.push({
                id: hid, templateId: tid, themeId: newId,
                type: 'header', name: 'Header', area: 'header',
                position: 0, hidden: false, customCss: '', colorSchemeId: 1
            });

            const fid = this._nextSectionId++;
            this.sections.push({
                id: fid, templateId: tid, themeId: newId,
                type: 'footer', name: 'Footer', area: 'footer',
                position: 0, hidden: false, customCss: '', colorSchemeId: 1
            });
        });

        // Add default theme settings
        this.themeSettings.push({
            themeId: newId,
            logo: { url: '', altText: '', width: 120 },
            favicon: { url: '' },
            colors: JSON.parse(JSON.stringify(DEFAULT_COLOR_SCHEMES)),
            typography: { headingFont: 'Assistant', bodyFont: 'Assistant', fontSizeScale: 100 },
            layout: { pageWidth: 1200, sectionSpacing: 36, gridHorizontalSpacing: 12, gridVerticalSpacing: 12 },
            animations: { revealOnScroll: true, hoverEffect: HOVER_EFFECTS.NONE },
            buttons: { style: BUTTON_STYLES.ROUNDED, borderRadius: 4 },
            variantPills: { style: BUTTON_STYLES.ROUNDED },
            inputs: { style: INPUT_STYLES.OUTLINED, borderRadius: 4 },
            badges: { salePosition: BADGE_POSITIONS.TOP_LEFT, saleShape: BADGE_SHAPES.RECTANGLE, soldOutPosition: BADGE_POSITIONS.BOTTOM_LEFT, soldOutShape: BADGE_SHAPES.RECTANGLE },
            socialLinks: JSON.parse(JSON.stringify(DEFAULT_SOCIAL_LINKS)),
            searchBehavior: { enableSuggestions: true, showVendor: true, showPrice: true },
            currencyFormat: { showCurrencyCode: false },
            cart: { type: CART_TYPES.DRAWER, showVendor: false, enableNote: true, emptyDrawerCollection: '', cartColorSchemeId: 1 },
            customCss: ''
        });

        this.notify();
        return theme;
    },

    // ==============================
    // Template Management
    // ==============================

    getTemplatesForTheme(themeId) {
        return this.templates.filter(t => t.themeId === themeId);
    },

    getTemplate(id) {
        return this.templates.find(t => t.id === id);
    },

    createTemplate(themeId, name, type, baseTemplateId) {
        const tid = this._nextTemplateId++;
        const handle = type + '.' + name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
        const template = {
            id: tid,
            themeId: themeId,
            name: name,
            type: type,
            handle: handle,
            isDefault: false
        };
        this.templates.push(template);

        // Copy sections from base template or create default ones
        if (baseTemplateId) {
            const baseSections = this.sections.filter(s => s.templateId === baseTemplateId);
            baseSections.forEach(bs => {
                const newSid = this._nextSectionId++;
                const newSection = JSON.parse(JSON.stringify(bs));
                newSection.id = newSid;
                newSection.templateId = tid;
                this.sections.push(newSection);

                // Copy blocks
                const baseBlocks = this.blocks.filter(b => b.sectionId === bs.id);
                baseBlocks.forEach(bb => {
                    const newBid = this._nextBlockId++;
                    const newBlock = JSON.parse(JSON.stringify(bb));
                    newBlock.id = newBid;
                    newBlock.sectionId = newSid;
                    this.blocks.push(newBlock);
                });
            });
        } else {
            // Add header and footer
            const hid = this._nextSectionId++;
            this.sections.push({
                id: hid, templateId: tid, themeId: themeId,
                type: 'header', name: 'Header', area: 'header',
                position: 0, hidden: false, customCss: '', colorSchemeId: 1
            });
            const fid = this._nextSectionId++;
            this.sections.push({
                id: fid, templateId: tid, themeId: themeId,
                type: 'footer', name: 'Footer', area: 'footer',
                position: 0, hidden: false, customCss: '', colorSchemeId: 1
            });
        }

        this.notify();
        return template;
    },

    deleteTemplate(templateId) {
        const template = this.getTemplate(templateId);
        if (!template || template.isDefault) return false;

        const sectionIds = this.sections.filter(s => s.templateId === templateId).map(s => s.id);
        this.blocks = this.blocks.filter(b => !sectionIds.includes(b.sectionId));
        this.sections = this.sections.filter(s => s.templateId !== templateId);
        this.templates = this.templates.filter(t => t.id !== templateId);
        this.notify();
        return true;
    },

    // ==============================
    // Section Management
    // ==============================

    getSectionsForTemplate(templateId) {
        return this.sections.filter(s => s.templateId === templateId)
            .sort((a, b) => {
                const areaOrder = { header: 0, template: 1, footer: 2 };
                if (areaOrder[a.area] !== areaOrder[b.area]) return areaOrder[a.area] - areaOrder[b.area];
                return a.position - b.position;
            });
    },

    getSection(id) {
        return this.sections.find(s => s.id === id);
    },

    addSection(templateId, themeId, sectionType, area, name) {
        const existingSections = this.sections.filter(s => s.templateId === templateId && s.area === area);
        const totalSections = this.sections.filter(s => s.templateId === templateId);
        if (totalSections.length >= 25) return null; // Max 25 sections

        const maxPos = existingSections.reduce((max, s) => Math.max(max, s.position), -1);
        const sid = this._nextSectionId++;
        const section = {
            id: sid,
            templateId: templateId,
            themeId: themeId,
            type: sectionType,
            name: name || SECTION_TYPES.find(st => st.id === sectionType)?.name || sectionType,
            area: area,
            position: maxPos + 1,
            hidden: false,
            customCss: '',
            colorSchemeId: 1
        };
        this.sections.push(section);
        this.notify();
        return section;
    },

    removeSection(sectionId) {
        this.blocks = this.blocks.filter(b => b.sectionId !== sectionId);
        this.sections = this.sections.filter(s => s.id !== sectionId);
        if (this.selectedSectionId === sectionId) this.selectedSectionId = null;
        this.notify();
    },

    duplicateSection(sectionId) {
        const source = this.getSection(sectionId);
        if (!source) return null;

        const totalSections = this.sections.filter(s => s.templateId === source.templateId);
        if (totalSections.length >= 25) return null;

        const newSid = this._nextSectionId++;
        const newSection = JSON.parse(JSON.stringify(source));
        newSection.id = newSid;
        newSection.name = source.name + ' (copy)';
        newSection.position = source.position + 1;

        // Shift positions of sections after the original
        this.sections.forEach(s => {
            if (s.templateId === source.templateId && s.area === source.area && s.position > source.position) {
                s.position++;
            }
        });

        this.sections.push(newSection);

        // Duplicate blocks
        const sourceBlocks = this.blocks.filter(b => b.sectionId === sectionId);
        sourceBlocks.forEach(sb => {
            const newBid = this._nextBlockId++;
            const newBlock = JSON.parse(JSON.stringify(sb));
            newBlock.id = newBid;
            newBlock.sectionId = newSid;
            this.blocks.push(newBlock);
        });

        this.notify();
        return newSection;
    },

    hideSection(sectionId) {
        const section = this.getSection(sectionId);
        if (section) {
            section.hidden = !section.hidden;
            this.notify();
        }
    },

    renameSection(sectionId, newName) {
        const section = this.getSection(sectionId);
        if (section && newName.trim()) {
            section.name = newName.trim();
            this.notify();
        }
    },

    moveSectionUp(sectionId) {
        const section = this.getSection(sectionId);
        if (!section || section.position === 0) return;

        const sibling = this.sections.find(s =>
            s.templateId === section.templateId &&
            s.area === section.area &&
            s.position === section.position - 1
        );
        if (sibling) {
            sibling.position++;
            section.position--;
            this.notify();
        }
    },

    moveSectionDown(sectionId) {
        const section = this.getSection(sectionId);
        if (!section) return;

        const sibling = this.sections.find(s =>
            s.templateId === section.templateId &&
            s.area === section.area &&
            s.position === section.position + 1
        );
        if (sibling) {
            sibling.position--;
            section.position++;
            this.notify();
        }
    },

    updateSectionCustomCss(sectionId, css) {
        const section = this.getSection(sectionId);
        if (section) {
            section.customCss = css.substring(0, 500);
            this.notify();
        }
    },

    updateSectionColorScheme(sectionId, colorSchemeId) {
        const section = this.getSection(sectionId);
        if (section) {
            section.colorSchemeId = colorSchemeId;
            this.notify();
        }
    },

    // ==============================
    // Block Management
    // ==============================

    getBlocksForSection(sectionId) {
        return this.blocks.filter(b => b.sectionId === sectionId)
            .sort((a, b) => a.position - b.position);
    },

    getBlock(id) {
        return this.blocks.find(b => b.id === id);
    },

    addBlock(sectionId, themeId, blockType, name) {
        const section = this.getSection(sectionId);
        if (!section) return null;

        // Check template block limit (1250)
        const templateBlocks = this.blocks.filter(b => {
            const bSection = this.getSection(b.sectionId);
            return bSection && bSection.templateId === section.templateId;
        });
        if (templateBlocks.length >= 1250) return null;

        const existingBlocks = this.blocks.filter(b => b.sectionId === sectionId);
        const maxPos = existingBlocks.reduce((max, b) => Math.max(max, b.position), -1);
        const bid = this._nextBlockId++;
        const block = {
            id: bid,
            sectionId: sectionId,
            themeId: themeId,
            type: blockType,
            name: name || BLOCK_TYPES.find(bt => bt.id === blockType)?.name || blockType,
            position: maxPos + 1,
            hidden: false,
            settings: {}
        };
        this.blocks.push(block);
        this.notify();
        return block;
    },

    removeBlock(blockId) {
        this.blocks = this.blocks.filter(b => b.id !== blockId);
        if (this.selectedBlockId === blockId) this.selectedBlockId = null;
        this.notify();
    },

    duplicateBlock(blockId) {
        const source = this.getBlock(blockId);
        if (!source) return null;

        const newBid = this._nextBlockId++;
        const newBlock = JSON.parse(JSON.stringify(source));
        newBlock.id = newBid;
        newBlock.name = source.name + ' (copy)';
        newBlock.position = source.position + 1;

        this.blocks.forEach(b => {
            if (b.sectionId === source.sectionId && b.position > source.position) {
                b.position++;
            }
        });

        this.blocks.push(newBlock);
        this.notify();
        return newBlock;
    },

    hideBlock(blockId) {
        const block = this.getBlock(blockId);
        if (block) {
            block.hidden = !block.hidden;
            this.notify();
        }
    },

    renameBlock(blockId, newName) {
        const block = this.getBlock(blockId);
        if (block && newName.trim()) {
            block.name = newName.trim();
            this.notify();
        }
    },

    moveBlockUp(blockId) {
        const block = this.getBlock(blockId);
        if (!block || block.position === 0) return;

        const sibling = this.blocks.find(b =>
            b.sectionId === block.sectionId &&
            b.position === block.position - 1
        );
        if (sibling) {
            sibling.position++;
            block.position--;
            this.notify();
        }
    },

    moveBlockDown(blockId) {
        const block = this.getBlock(blockId);
        if (!block) return;

        const sibling = this.blocks.find(b =>
            b.sectionId === block.sectionId &&
            b.position === block.position + 1
        );
        if (sibling) {
            sibling.position--;
            block.position++;
            this.notify();
        }
    },

    updateBlockSettings(blockId, settings) {
        const block = this.getBlock(blockId);
        if (block) {
            Object.assign(block.settings, settings);
            this.notify();
        }
    },

    // ==============================
    // Theme Settings Management
    // ==============================

    getThemeSettings(themeId) {
        return this.themeSettings.find(ts => ts.themeId === themeId);
    },

    updateThemeSettings(themeId, path, value) {
        const settings = this.getThemeSettings(themeId);
        if (!settings) return;

        const parts = path.split('.');
        let obj = settings;
        for (let i = 0; i < parts.length - 1; i++) {
            obj = obj[parts[i]];
            if (!obj) return;
        }
        obj[parts[parts.length - 1]] = value;
        this.notify();
    },

    // ---- Color Scheme operations ----
    addColorScheme(themeId) {
        const settings = this.getThemeSettings(themeId);
        if (!settings || settings.colors.length >= 21) return null;

        const newScheme = {
            id: this._nextColorSchemeId++,
            name: 'Scheme ' + (settings.colors.length + 1),
            isDefault: false,
            background: '#ffffff',
            backgroundGradient: '',
            text: '#121212',
            solidButtonBg: '#121212',
            solidButtonText: '#ffffff',
            outlineButton: '#121212',
            shadow: '#121212'
        };
        settings.colors.push(newScheme);
        this.notify();
        return newScheme;
    },

    updateColorScheme(themeId, schemeId, field, value) {
        const settings = this.getThemeSettings(themeId);
        if (!settings) return;

        const scheme = settings.colors.find(c => c.id === schemeId);
        if (scheme) {
            scheme[field] = value;
            this.notify();
        }
    },

    removeColorScheme(themeId, schemeId) {
        const settings = this.getThemeSettings(themeId);
        if (!settings) return false;

        const scheme = settings.colors.find(c => c.id === schemeId);
        if (!scheme || scheme.isDefault) return false;

        settings.colors = settings.colors.filter(c => c.id !== schemeId);

        // Reset sections using this color scheme to default
        this.sections.filter(s => s.themeId === themeId && s.colorSchemeId === schemeId)
            .forEach(s => { s.colorSchemeId = 1; });

        this.notify();
        return true;
    },

    // ---- Social Links ----
    updateSocialLink(themeId, platform, url) {
        const settings = this.getThemeSettings(themeId);
        if (settings && settings.socialLinks.hasOwnProperty(platform)) {
            settings.socialLinks[platform] = url;
            this.notify();
        }
    },

    // ---- Theme Custom CSS ----
    updateThemeCustomCss(themeId, css) {
        const theme = this.getTheme(themeId);
        if (theme) {
            theme.customCss = css.substring(0, 1500);
            this.notify();
        }
    }
};

// ---- SSE listener for reset ----
(function() {
    const eventSource = new EventSource('/api/events');
    eventSource.onmessage = function(e) {
        if (e.data === 'reset') {
            AppState.resetToSeedData();
            AppState.notify();
            if (typeof Router !== 'undefined') {
                Router.navigate('/');
            }
        }
    };
})();

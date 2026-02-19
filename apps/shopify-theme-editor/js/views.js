// ============================================================
// views.js — All view renderers for the Shopify Theme Editor
// ============================================================

const Views = {

    // ==============================
    // Themes List (Home Page)
    // ==============================
    themes() {
        const liveTheme = AppState.getLiveTheme();
        const otherThemes = AppState.themes.filter(t => t.status !== 'live');

        return `<div class="page-header">
            <h1>Themes</h1>
            <div class="page-header-actions">
                <button class="btn btn-primary" id="addThemeBtn" data-testid="add-theme-btn">Add theme</button>
            </div>
        </div>

        ${liveTheme ? `
        <div class="section-group">
            <h2 class="section-title">Current theme</h2>
            <div class="themes-grid">
                ${Components.themeCard(liveTheme)}
            </div>
        </div>` : ''}

        <div class="section-group">
            <h2 class="section-title">Theme library <span class="count-badge">${otherThemes.length}</span></h2>
            <div class="themes-grid">
                ${otherThemes.map(t => Components.themeCard(t)).join('')}
            </div>
        </div>

        <div class="section-group">
            <div class="reset-section">
                <button class="btn btn-secondary" id="resetDataBtn" data-testid="reset-data-btn">Reset to default data</button>
                <span class="reset-hint">Restore all themes and settings to their original state</span>
            </div>
        </div>`;
    },

    // ==============================
    // Theme Editor View
    // ==============================
    editor(themeId) {
        const theme = AppState.getTheme(themeId);
        if (!theme) return '<div class="error-page"><h2>Theme not found</h2></div>';

        const templates = AppState.getTemplatesForTheme(themeId);
        const selectedTemplate = AppState.selectedTemplateId
            ? AppState.getTemplate(AppState.selectedTemplateId)
            : templates[0];

        if (selectedTemplate && !AppState.selectedTemplateId) {
            AppState.selectedTemplateId = selectedTemplate.id;
        }

        const sections = selectedTemplate
            ? AppState.getSectionsForTemplate(selectedTemplate.id)
            : [];

        const headerSections = sections.filter(s => s.area === 'header');
        const templateSections = sections.filter(s => s.area === 'template');
        const footerSections = sections.filter(s => s.area === 'footer');

        const settings = AppState.getThemeSettings(themeId);

        // Template dropdown options
        const templateOptions = templates.map(t => ({
            value: String(t.id),
            label: t.name + (t.isDefault ? '' : ' (custom)')
        }));

        return `<div class="editor-layout">
            <div class="editor-topbar">
                <div class="editor-topbar-left">
                    <button class="btn btn-icon" data-action="back-to-themes" data-testid="back-btn" title="Back to themes">&larr;</button>
                    <span class="editor-theme-name">${Components.escapeHtml(theme.name)}</span>
                    ${Components.statusBadge(theme.status)}
                </div>
                <div class="editor-topbar-center">
                    ${Components.dropdown('templateSelector', templateOptions, String(selectedTemplate?.id || ''), { placeholder: 'Select template' })}
                </div>
                <div class="editor-topbar-right">
                    <div class="editor-view-modes">
                        <button class="btn btn-icon ${AppState.editorMode === 'desktop' ? 'active' : ''}" data-action="set-mode" data-mode="desktop" title="Desktop">&#128187;</button>
                        <button class="btn btn-icon ${AppState.editorMode === 'mobile' ? 'active' : ''}" data-action="set-mode" data-mode="mobile" title="Mobile">&#128241;</button>
                    </div>
                </div>
            </div>

            <div class="editor-content">
                <div class="editor-sidebar" id="editorSidebar">
                    <div class="sidebar-section">
                        <div class="sidebar-header" data-collapse="header-sections">
                            <span class="collapse-icon">&#9660;</span>
                            <span>Header</span>
                            <button class="btn btn-icon btn-xs" data-action="add-section" data-area="header" data-template-id="${selectedTemplate?.id}" title="Add section">+</button>
                        </div>
                        <div class="sidebar-content" id="header-sections">
                            ${headerSections.map(s => Components.sectionTreeItem(s, AppState.getBlocksForSection(s.id))).join('')}
                        </div>
                    </div>

                    <div class="sidebar-section">
                        <div class="sidebar-header" data-collapse="template-sections">
                            <span class="collapse-icon">&#9660;</span>
                            <span>Template</span>
                            <button class="btn btn-icon btn-xs" data-action="add-section" data-area="template" data-template-id="${selectedTemplate?.id}" title="Add section">+</button>
                        </div>
                        <div class="sidebar-content" id="template-sections">
                            ${templateSections.map(s => Components.sectionTreeItem(s, AppState.getBlocksForSection(s.id))).join('')}
                        </div>
                    </div>

                    <div class="sidebar-section">
                        <div class="sidebar-header" data-collapse="footer-sections">
                            <span class="collapse-icon">&#9660;</span>
                            <span>Footer</span>
                            <button class="btn btn-icon btn-xs" data-action="add-section" data-area="footer" data-template-id="${selectedTemplate?.id}" title="Add section">+</button>
                        </div>
                        <div class="sidebar-content" id="footer-sections">
                            ${footerSections.map(s => Components.sectionTreeItem(s, AppState.getBlocksForSection(s.id))).join('')}
                        </div>
                    </div>

                    <div class="sidebar-divider"></div>

                    <div class="sidebar-nav">
                        <div class="sidebar-nav-item" data-action="open-theme-settings" data-testid="theme-settings-btn">
                            <span class="sidebar-nav-icon">&#9881;</span>
                            <span>Theme settings</span>
                        </div>
                    </div>
                </div>

                <div class="editor-preview" id="editorPreview">
                    ${this._renderPreview(theme, selectedTemplate, sections)}
                </div>

                <div class="editor-settings-panel ${AppState.selectedSectionId || AppState.selectedBlockId ? 'active' : ''}" id="settingsPanel">
                    ${this._renderSettingsPanel(themeId)}
                </div>
            </div>
        </div>`;
    },

    _renderPreview(theme, template, sections) {
        if (!template) return '<div class="preview-empty">Select a template to preview</div>';

        const templateSections = sections.filter(s => s.area === 'template' && !s.hidden);

        return `<div class="preview-frame ${AppState.editorMode === 'mobile' ? 'preview-mobile' : ''}">
            <div class="preview-header">
                <div class="preview-header-bar">
                    <span class="preview-store-name">${Components.escapeHtml(AppState.currentUser.storeName)}</span>
                    <div class="preview-header-nav">
                        <span>Shop</span><span>About</span><span>Contact</span><span>&#128722;</span>
                    </div>
                </div>
            </div>
            <div class="preview-body">
                ${templateSections.map(s => this._renderPreviewSection(s)).join('')}
            </div>
            <div class="preview-footer">
                <div class="preview-footer-bar">
                    <span>&copy; ${new Date().getFullYear()} ${Components.escapeHtml(AppState.currentUser.storeName)}</span>
                </div>
            </div>
        </div>`;
    },

    _renderPreviewSection(section) {
        const blocks = AppState.getBlocksForSection(section.id).filter(b => !b.hidden);
        const isSelected = AppState.selectedSectionId === section.id;

        let contentHtml = '';
        switch (section.type) {
            case 'image-banner':
                contentHtml = `<div class="preview-banner">
                    ${blocks.map(b => {
                        if (b.type === 'heading') return `<h1>${Components.escapeHtml(b.settings.text || '')}</h1>`;
                        if (b.type === 'text') return `<p>${Components.escapeHtml(b.settings.text || '')}</p>`;
                        if (b.type === 'button') return `<button class="preview-btn">${Components.escapeHtml(b.settings.text || 'Button')}</button>`;
                        return '';
                    }).join('')}
                </div>`;
                break;
            case 'rich-text':
                contentHtml = `<div class="preview-rich-text">
                    ${blocks.map(b => {
                        if (b.type === 'heading') return `<h2>${Components.escapeHtml(b.settings.text || '')}</h2>`;
                        if (b.type === 'text') return `<p>${Components.escapeHtml(b.settings.text || '')}</p>`;
                        if (b.type === 'button') return `<button class="preview-btn-outline">${Components.escapeHtml(b.settings.text || 'Button')}</button>`;
                        return '';
                    }).join('')}
                </div>`;
                break;
            case 'featured-collection':
                contentHtml = `<div class="preview-collection">
                    <h2>Featured Collection</h2>
                    <div class="preview-product-grid">
                        <div class="preview-product-card"><div class="preview-product-img"></div><span>Product 1</span></div>
                        <div class="preview-product-card"><div class="preview-product-img"></div><span>Product 2</span></div>
                        <div class="preview-product-card"><div class="preview-product-img"></div><span>Product 3</span></div>
                    </div>
                </div>`;
                break;
            case 'newsletter':
                contentHtml = `<div class="preview-newsletter">
                    ${blocks.map(b => {
                        if (b.type === 'heading') return `<h2>${Components.escapeHtml(b.settings.text || '')}</h2>`;
                        if (b.type === 'text') return `<p>${Components.escapeHtml(b.settings.text || '')}</p>`;
                        if (b.type === 'email-form') return `<div class="preview-email-form"><input type="text" placeholder="Email" disabled /><button class="preview-btn">Subscribe</button></div>`;
                        return '';
                    }).join('')}
                </div>`;
                break;
            case 'multicolumn':
                contentHtml = `<div class="preview-multicolumn">
                    ${blocks.map(b => {
                        if (b.type === 'column') return `<div class="preview-column"><strong>${Components.escapeHtml(b.settings.title || '')}</strong><p>${Components.escapeHtml(b.settings.text || '')}</p></div>`;
                        return '';
                    }).join('')}
                </div>`;
                break;
            case 'image-with-text':
                contentHtml = `<div class="preview-image-text">
                    <div class="preview-image-placeholder"></div>
                    <div class="preview-text-side">
                        ${blocks.map(b => {
                            if (b.type === 'heading') return `<h2>${Components.escapeHtml(b.settings.text || '')}</h2>`;
                            if (b.type === 'text') return `<p>${Components.escapeHtml(b.settings.text || '')}</p>`;
                            if (b.type === 'button') return `<button class="preview-btn">${Components.escapeHtml(b.settings.text || 'Button')}</button>`;
                            return '';
                        }).join('')}
                    </div>
                </div>`;
                break;
            case 'contact-form':
                contentHtml = `<div class="preview-contact">
                    ${blocks.map(b => {
                        if (b.type === 'heading') return `<h1>${Components.escapeHtml(b.settings.text || '')}</h1>`;
                        if (b.type === 'text') return `<p>${Components.escapeHtml(b.settings.text || '')}</p>`;
                        return '';
                    }).join('')}
                    <div class="preview-form"><input disabled placeholder="Name"/><input disabled placeholder="Email"/><textarea disabled placeholder="Message"></textarea><button class="preview-btn">Send</button></div>
                </div>`;
                break;
            default:
                contentHtml = `<div class="preview-generic"><span class="preview-section-label">${Components.escapeHtml(section.name)}</span></div>`;
        }

        return `<div class="preview-section ${isSelected ? 'preview-section-selected' : ''}" data-section-id="${section.id}">
            ${contentHtml}
        </div>`;
    },

    // ==============================
    // Settings Panel (Right sidebar)
    // ==============================
    _renderSettingsPanel(themeId) {
        if (AppState.selectedBlockId) {
            return this._renderBlockSettings(AppState.selectedBlockId);
        }
        if (AppState.selectedSectionId) {
            return this._renderSectionSettings(AppState.selectedSectionId, themeId);
        }
        return '<div class="settings-empty"><p>Select a section or block to edit its settings</p></div>';
    },

    _renderSectionSettings(sectionId, themeId) {
        const section = AppState.getSection(sectionId);
        if (!section) return '';

        const settings = AppState.getThemeSettings(themeId);
        const colorSchemes = settings ? settings.colors : [];
        const colorOptions = colorSchemes.map(c => ({ value: String(c.id), label: c.name }));
        const blocks = AppState.getBlocksForSection(sectionId);
        const blockTypesForSection = BLOCK_TYPES.filter(bt => bt.sections.includes(section.type));

        return `<div class="settings-panel-content">
            <div class="settings-panel-header">
                <button class="btn btn-icon btn-xs" data-action="close-settings">&larr;</button>
                <h3>${Components.escapeHtml(section.name)}</h3>
            </div>

            <div class="settings-section">
                <h4>Section settings</h4>
                ${Components.formField('Name', Components.textInput('sectionName', section.name))}
                ${Components.formField('Color scheme', Components.dropdown('sectionColorScheme', colorOptions, String(section.colorSchemeId)))}
                ${Components.formField('Custom CSS', Components.textarea('sectionCustomCss', section.customCss, { rows: 3, maxLength: 500 }),
                    { hint: 'Max 500 characters. Scoped to this section.' })}
            </div>

            <div class="settings-section">
                <h4>Blocks <span class="count-badge">${blocks.length}</span></h4>
                <div class="block-list">
                    ${blocks.map(b => `
                        <div class="block-list-item ${b.hidden ? 'block-hidden' : ''}" data-block-id="${b.id}">
                            <span class="block-drag">&#8942;&#8942;</span>
                            <span class="block-name" data-action="select-block" data-block-id="${b.id}">${Components.escapeHtml(b.name)}</span>
                            <div class="block-actions">
                                <button class="btn btn-icon btn-xs" data-action="hide-block" data-block-id="${b.id}" title="${b.hidden ? 'Show' : 'Hide'}">${b.hidden ? '&#128065;' : '&#128064;'}</button>
                                <button class="btn btn-icon btn-xs" data-action="move-block-up" data-block-id="${b.id}" title="Move up">&uarr;</button>
                                <button class="btn btn-icon btn-xs" data-action="move-block-down" data-block-id="${b.id}" title="Move down">&darr;</button>
                                <button class="btn btn-icon btn-xs" data-action="duplicate-block" data-block-id="${b.id}" title="Duplicate">&#8943;</button>
                                <button class="btn btn-icon btn-xs btn-danger-icon" data-action="remove-block" data-block-id="${b.id}" title="Remove">&times;</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
                ${blockTypesForSection.length > 0 ? `
                <div class="add-block-section">
                    ${Components.dropdown('addBlockType', blockTypesForSection.map(bt => ({ value: bt.id, label: bt.name })), '', { placeholder: 'Choose block type' })}
                    <button class="btn btn-secondary btn-sm" data-action="add-block" data-section-id="${sectionId}">Add block</button>
                </div>` : ''}
            </div>

            <div class="settings-section">
                <h4>Section actions</h4>
                <div class="section-actions-group">
                    <button class="btn btn-secondary btn-sm" data-action="hide-section" data-section-id="${sectionId}">${section.hidden ? 'Show section' : 'Hide section'}</button>
                    <button class="btn btn-secondary btn-sm" data-action="duplicate-section" data-section-id="${sectionId}">Duplicate</button>
                    <button class="btn btn-secondary btn-sm" data-action="move-section-up" data-section-id="${sectionId}">Move up</button>
                    <button class="btn btn-secondary btn-sm" data-action="move-section-down" data-section-id="${sectionId}">Move down</button>
                    <button class="btn btn-danger btn-sm" data-action="remove-section" data-section-id="${sectionId}">Remove section</button>
                </div>
            </div>
        </div>`;
    },

    _renderBlockSettings(blockId) {
        const block = AppState.getBlock(blockId);
        if (!block) return '';

        let settingsHtml = '';
        switch (block.type) {
            case 'heading':
                settingsHtml = `
                    ${Components.formField('Heading text', Components.textInput('blockText', block.settings.text || ''))}
                    ${Components.formField('Size', Components.dropdown('blockSize', [
                        { value: 'h1', label: 'Heading 1' },
                        { value: 'h2', label: 'Heading 2' },
                        { value: 'h3', label: 'Heading 3' },
                        { value: 'h4', label: 'Heading 4' }
                    ], block.settings.size || 'h2'))}`;
                break;
            case 'text':
                settingsHtml = Components.formField('Text', Components.textarea('blockText', block.settings.text || '', { rows: 4 }));
                break;
            case 'button':
                settingsHtml = `
                    ${Components.formField('Button label', Components.textInput('blockText', block.settings.text || ''))}
                    ${Components.formField('Link', Components.textInput('blockLink', block.settings.link || '', { placeholder: '/collections/all' }))}
                    ${Components.formField('Style', Components.dropdown('blockStyle', [
                        { value: 'solid', label: 'Solid' },
                        { value: 'outline', label: 'Outline' }
                    ], block.settings.style || 'solid'))}`;
                break;
            case 'announcement':
                settingsHtml = `
                    ${Components.formField('Text', Components.textInput('blockText', block.settings.text || ''))}
                    ${Components.formField('Link', Components.textInput('blockLink', block.settings.link || '', { placeholder: '/collections/sale' }))}`;
                break;
            case 'column':
                settingsHtml = `
                    ${Components.formField('Title', Components.textInput('blockTitle', block.settings.title || ''))}
                    ${Components.formField('Description', Components.textarea('blockText', block.settings.text || '', { rows: 3 }))}`;
                break;
            case 'menu':
                settingsHtml = `
                    ${Components.formField('Heading', Components.textInput('blockTitle', block.settings.title || ''))}
                    ${Components.formField('Menu', Components.dropdown('blockMenu', [
                        { value: 'main-menu', label: 'Main menu' },
                        { value: 'footer', label: 'Footer menu' }
                    ], block.settings.menu || 'main-menu'))}`;
                break;
            default:
                settingsHtml = '<p class="settings-note">No configurable settings for this block type.</p>';
        }

        return `<div class="settings-panel-content">
            <div class="settings-panel-header">
                <button class="btn btn-icon btn-xs" data-action="back-to-section">&larr;</button>
                <h3>${Components.escapeHtml(block.name)}</h3>
            </div>

            <div class="settings-section">
                <h4>Block settings</h4>
                ${Components.formField('Name', Components.textInput('blockName', block.name))}
                ${settingsHtml}
            </div>

            <div class="settings-section">
                <h4>Block actions</h4>
                <div class="section-actions-group">
                    <button class="btn btn-secondary btn-sm" data-action="hide-block" data-block-id="${blockId}">${block.hidden ? 'Show block' : 'Hide block'}</button>
                    <button class="btn btn-secondary btn-sm" data-action="duplicate-block" data-block-id="${blockId}">Duplicate</button>
                    <button class="btn btn-danger btn-sm" data-action="remove-block" data-block-id="${blockId}">Remove block</button>
                </div>
            </div>
        </div>`;
    },

    // ==============================
    // Theme Settings Page
    // ==============================
    themeSettings(themeId) {
        const theme = AppState.getTheme(themeId);
        const settings = AppState.getThemeSettings(themeId);
        if (!theme || !settings) return '<div class="error-page"><h2>Theme settings not found</h2></div>';

        const activeTab = AppState.queryParams.settingsTab || 'colors';

        const tabList = [
            { id: 'logo', label: 'Logo' },
            { id: 'colors', label: 'Colors' },
            { id: 'typography', label: 'Typography' },
            { id: 'layout', label: 'Layout' },
            { id: 'animations', label: 'Animations' },
            { id: 'buttons', label: 'Buttons' },
            { id: 'inputs', label: 'Inputs' },
            { id: 'badges', label: 'Badges' },
            { id: 'social', label: 'Social media' },
            { id: 'search', label: 'Search' },
            { id: 'currency', label: 'Currency' },
            { id: 'cart', label: 'Cart' },
            { id: 'custom-css', label: 'Custom CSS' }
        ];

        return `<div class="editor-layout">
            <div class="editor-topbar">
                <div class="editor-topbar-left">
                    <button class="btn btn-icon" data-action="back-to-editor" data-testid="back-to-editor-btn" title="Back to editor">&larr;</button>
                    <span class="editor-theme-name">Theme settings - ${Components.escapeHtml(theme.name)}</span>
                </div>
                <div class="editor-topbar-right"></div>
            </div>
            <div class="settings-page-layout">
                <div class="settings-tabs-sidebar">
                    ${tabList.map(t => `
                        <div class="settings-tab-item ${t.id === activeTab ? 'active' : ''}" data-settings-tab="${t.id}" data-testid="settings-tab-${t.id}">
                            ${Components.escapeHtml(t.label)}
                        </div>
                    `).join('')}
                </div>
                <div class="settings-tab-content">
                    ${this._renderSettingsTab(themeId, activeTab, settings)}
                </div>
            </div>
        </div>`;
    },

    _renderSettingsTab(themeId, tab, settings) {
        switch (tab) {
            case 'logo':
                return this._renderLogoSettings(themeId, settings);
            case 'colors':
                return this._renderColorSettings(themeId, settings);
            case 'typography':
                return this._renderTypographySettings(themeId, settings);
            case 'layout':
                return this._renderLayoutSettings(themeId, settings);
            case 'animations':
                return this._renderAnimationSettings(themeId, settings);
            case 'buttons':
                return this._renderButtonSettings(themeId, settings);
            case 'inputs':
                return this._renderInputSettings(themeId, settings);
            case 'badges':
                return this._renderBadgeSettings(themeId, settings);
            case 'social':
                return this._renderSocialSettings(themeId, settings);
            case 'search':
                return this._renderSearchSettings(themeId, settings);
            case 'currency':
                return this._renderCurrencySettings(themeId, settings);
            case 'cart':
                return this._renderCartSettings(themeId, settings);
            case 'custom-css':
                return this._renderCustomCssSettings(themeId, settings);
            default:
                return '<p>Select a settings category</p>';
        }
    },

    _renderLogoSettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Logo</h2>
            ${Components.formField('Logo alt text', Components.textInput('logoAltText', settings.logo.altText, { placeholder: 'Describe your logo' }))}
            ${Components.formField('Desktop logo width', Components.rangeInput('logoWidth', settings.logo.width, 50, 300, { unit: 'px' }))}
            <h2 class="mt-lg">Favicon</h2>
            ${Components.infoBox('Favicons display in browser tabs, history, and bookmarks. Recommended size: 32x32px.')}
        </div>`;
    },

    _renderColorSettings(themeId, settings) {
        const schemes = settings.colors;
        return `<div class="settings-content">
            <h2>Color schemes <span class="count-badge">${schemes.length}/21</span></h2>
            ${Components.infoBox('Define up to 21 color schemes. Assign them to sections and blocks.')}

            <div class="color-schemes-grid">
                ${schemes.map(s => Components.colorSchemePreview(s, false)).join('')}
                ${schemes.length < 21 ? `<div class="color-scheme-add" data-action="add-color-scheme" data-testid="add-color-scheme-btn">
                    <span>+</span><span>Add scheme</span>
                </div>` : ''}
            </div>

            <div id="colorSchemeEditor">
                ${schemes.length > 0 ? this._renderColorSchemeEditor(themeId, schemes[0]) : ''}
            </div>
        </div>`;
    },

    _renderColorSchemeEditor(themeId, scheme) {
        return `<div class="color-scheme-detail" data-scheme-id="${scheme.id}">
            <h3>Editing: ${Components.escapeHtml(scheme.name)}</h3>
            ${Components.formField('Scheme name', Components.textInput('schemeName', scheme.name))}
            ${Components.formField('Background', Components.colorInput('schemeBg', scheme.background))}
            ${Components.formField('Background gradient', Components.textInput('schemeBgGradient', scheme.backgroundGradient, { placeholder: 'e.g. linear-gradient(135deg, #667eea 0%, #764ba2 100%)' }))}
            ${Components.formField('Text', Components.colorInput('schemeText', scheme.text))}
            ${Components.formField('Solid button background', Components.colorInput('schemeSolidBtnBg', scheme.solidButtonBg))}
            ${Components.formField('Solid button text', Components.colorInput('schemeSolidBtnText', scheme.solidButtonText))}
            ${Components.formField('Outline button', Components.colorInput('schemeOutlineBtn', scheme.outlineButton))}
            ${Components.formField('Shadow', Components.colorInput('schemeShadow', scheme.shadow))}
            ${!scheme.isDefault ? `<button class="btn btn-danger btn-sm mt-md" data-action="remove-color-scheme" data-scheme-id="${scheme.id}">Remove scheme</button>` : ''}
        </div>`;
    },

    _renderTypographySettings(themeId, settings) {
        const allFonts = [...FONT_LIBRARY, ...SYSTEM_FONTS].sort();
        const fontOptions = allFonts.map(f => ({ value: f, label: f }));
        const scaleOptions = [];
        for (let s = 100; s <= 150; s += 5) {
            scaleOptions.push({ value: String(s), label: s + '%' });
        }

        return `<div class="settings-content">
            <h2>Typography</h2>
            ${Components.formField('Heading font', Components.dropdown('headingFont', fontOptions, settings.typography.headingFont, { searchable: true }))}
            ${Components.formField('Body font', Components.dropdown('bodyFont', fontOptions, settings.typography.bodyFont, { searchable: true }))}
            ${Components.formField('Font size scale', Components.dropdown('fontSizeScale', scaleOptions, String(settings.typography.fontSizeScale)))}
        </div>`;
    },

    _renderLayoutSettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Layout</h2>
            ${Components.formField('Page width', Components.rangeInput('pageWidth', settings.layout.pageWidth, 1000, 1600, { unit: 'px' }))}
            ${Components.formField('Space between sections', Components.rangeInput('sectionSpacing', settings.layout.sectionSpacing, 0, 100, { unit: 'px' }))}
            <h3 class="mt-lg">Grid</h3>
            ${Components.formField('Horizontal spacing', Components.rangeInput('gridHSpacing', settings.layout.gridHorizontalSpacing, 0, 40, { unit: 'px' }))}
            ${Components.formField('Vertical spacing', Components.rangeInput('gridVSpacing', settings.layout.gridVerticalSpacing, 0, 40, { unit: 'px' }))}
        </div>`;
    },

    _renderAnimationSettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Animations</h2>
            ${Components.checkbox('revealOnScroll', settings.animations.revealOnScroll, 'Reveal sections on scroll')}
            ${Components.formField('Hover effect', Components.dropdown('hoverEffect', [
                { value: 'none', label: 'None' },
                { value: 'vertical-lift', label: 'Vertical lift' },
                { value: '3d-lift', label: '3D lift' }
            ], settings.animations.hoverEffect))}
        </div>`;
    },

    _renderButtonSettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Buttons</h2>
            ${Components.formField('Button style', Components.dropdown('buttonStyle', [
                { value: 'rounded', label: 'Rounded' },
                { value: 'square', label: 'Square' },
                { value: 'pill', label: 'Pill' }
            ], settings.buttons.style))}
            ${Components.formField('Border radius', Components.rangeInput('buttonRadius', settings.buttons.borderRadius, 0, 40, { unit: 'px' }))}
            <h3 class="mt-lg">Variant pills</h3>
            ${Components.formField('Pill style', Components.dropdown('variantPillStyle', [
                { value: 'rounded', label: 'Rounded' },
                { value: 'square', label: 'Square' },
                { value: 'pill', label: 'Pill' }
            ], settings.variantPills.style))}
        </div>`;
    },

    _renderInputSettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Inputs</h2>
            ${Components.formField('Input style', Components.dropdown('inputStyle', [
                { value: 'outlined', label: 'Outlined' },
                { value: 'filled', label: 'Filled' },
                { value: 'underlined', label: 'Underlined' }
            ], settings.inputs.style))}
            ${Components.formField('Border radius', Components.rangeInput('inputRadius', settings.inputs.borderRadius, 0, 40, { unit: 'px' }))}
        </div>`;
    },

    _renderBadgeSettings(themeId, settings) {
        const positionOptions = [
            { value: 'top-left', label: 'Top left' },
            { value: 'top-right', label: 'Top right' },
            { value: 'bottom-left', label: 'Bottom left' },
            { value: 'bottom-right', label: 'Bottom right' }
        ];
        const shapeOptions = [
            { value: 'rectangle', label: 'Rectangle' },
            { value: 'circle', label: 'Circle' }
        ];

        return `<div class="settings-content">
            <h2>Badges</h2>
            <h3>Sale badge</h3>
            ${Components.formField('Position', Components.dropdown('saleBadgePos', positionOptions, settings.badges.salePosition))}
            ${Components.formField('Shape', Components.dropdown('saleBadgeShape', shapeOptions, settings.badges.saleShape))}
            <h3 class="mt-lg">Sold out badge</h3>
            ${Components.formField('Position', Components.dropdown('soldOutBadgePos', positionOptions, settings.badges.soldOutPosition))}
            ${Components.formField('Shape', Components.dropdown('soldOutBadgeShape', shapeOptions, settings.badges.soldOutShape))}
        </div>`;
    },

    _renderSocialSettings(themeId, settings) {
        const platforms = [
            { key: 'instagram', label: 'Instagram' },
            { key: 'tiktok', label: 'TikTok' },
            { key: 'facebook', label: 'Facebook' },
            { key: 'pinterest', label: 'Pinterest' },
            { key: 'twitter', label: 'Twitter / X' },
            { key: 'youtube', label: 'YouTube' },
            { key: 'linkedin', label: 'LinkedIn' },
            { key: 'snapchat', label: 'Snapchat' },
            { key: 'tumblr', label: 'Tumblr' },
            { key: 'vimeo', label: 'Vimeo' }
        ];

        return `<div class="settings-content">
            <h2>Social media</h2>
            ${Components.infoBox('Add links to your social media accounts. These display in the footer.')}
            ${platforms.map(p =>
                Components.formField(p.label, Components.textInput('social_' + p.key, settings.socialLinks[p.key] || '', { placeholder: 'https://' + p.key + '.com/...' }))
            ).join('')}
        </div>`;
    },

    _renderSearchSettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Search behavior</h2>
            ${Components.checkbox('searchSuggestions', settings.searchBehavior.enableSuggestions, 'Enable search suggestions')}
            ${Components.checkbox('searchShowVendor', settings.searchBehavior.showVendor, 'Show product vendor in suggestions')}
            ${Components.checkbox('searchShowPrice', settings.searchBehavior.showPrice, 'Show product price in suggestions')}
        </div>`;
    },

    _renderCurrencySettings(themeId, settings) {
        return `<div class="settings-content">
            <h2>Currency format</h2>
            ${Components.checkbox('showCurrencyCode', settings.currencyFormat.showCurrencyCode, 'Show currency codes with prices')}
        </div>`;
    },

    _renderCartSettings(themeId, settings) {
        const colorSchemeOptions = settings.colors.map(c => ({ value: String(c.id), label: c.name }));
        return `<div class="settings-content">
            <h2>Cart</h2>
            ${Components.formField('Cart type', Components.dropdown('cartType', [
                { value: 'drawer', label: 'Drawer', description: 'Side panel that keeps the customer on the page' },
                { value: 'page', label: 'Page', description: 'Full cart page for checkout' },
                { value: 'popup', label: 'Popup notification', description: 'Brief notification when adding to cart' }
            ], settings.cart.type))}
            ${Components.checkbox('cartShowVendor', settings.cart.showVendor, 'Show vendor')}
            ${Components.checkbox('cartEnableNote', settings.cart.enableNote, 'Enable cart note')}
            ${settings.cart.type === 'drawer' ? Components.formField('Cart drawer color scheme', Components.dropdown('cartColorScheme', colorSchemeOptions, String(settings.cart.cartColorSchemeId))) : ''}
        </div>`;
    },

    _renderCustomCssSettings(themeId, settings) {
        const theme = AppState.getTheme(themeId);
        return `<div class="settings-content">
            <h2>Custom CSS</h2>
            ${Components.warningBox('Custom CSS rules may stop working with theme updates. Max 1500 characters.')}
            ${Components.formField('CSS', Components.textarea('themeCustomCss', theme?.customCss || '', { rows: 10, maxLength: 1500 }))}
        </div>`;
    },

    // ==============================
    // Add Section Modal
    // ==============================
    _showAddSectionModal(templateId, themeId, area) {
        const availableSections = SECTION_TYPES.filter(st => {
            if (area === 'header') return st.area === 'header' || st.area === 'template';
            if (area === 'footer') return st.area === 'footer' || st.area === 'template';
            return st.area === 'template';
        });

        const bodyHtml = `
            <div class="section-picker">
                <input type="text" id="sectionSearchInput" class="form-input" placeholder="Search sections..." data-testid="section-search" />
                <div class="section-picker-grid" id="sectionPickerGrid">
                    ${availableSections.map(st => `
                        <div class="section-picker-item" data-section-type="${st.id}" data-testid="section-type-${st.id}">
                            <div class="section-picker-icon">${st.icon}</div>
                            <div class="section-picker-name">${Components.escapeHtml(st.name)}</div>
                        </div>
                    `).join('')}
                </div>
            </div>`;

        Components.showModal('Add section', bodyHtml, '', { wide: true });

        setTimeout(() => {
            // Search
            const searchInput = document.getElementById('sectionSearchInput');
            if (searchInput) {
                searchInput.addEventListener('input', (e) => {
                    const q = e.target.value.toLowerCase();
                    document.querySelectorAll('.section-picker-item').forEach(item => {
                        const name = item.querySelector('.section-picker-name').textContent.toLowerCase();
                        item.style.display = name.includes(q) ? '' : 'none';
                    });
                });
            }

            // Selection
            document.querySelectorAll('.section-picker-item').forEach(item => {
                item.addEventListener('click', () => {
                    const sectionType = item.dataset.sectionType;
                    const sectionDef = SECTION_TYPES.find(st => st.id === sectionType);
                    AppState.addSection(templateId, themeId, sectionType, area, sectionDef?.name);
                    Components.closeModal();
                    Components.showToast('Section added', 'success');
                    Router.render();
                });
            });
        }, 100);
    },

    // ==============================
    // Create Template Modal
    // ==============================
    _showCreateTemplateModal(themeId) {
        const templateTypeOptions = TEMPLATE_TYPES.filter(t => ['product', 'collection', 'page', 'blog', 'blog-post'].includes(t))
            .map(t => `<div class="dropdown-item" data-value="${t}">${t}</div>`);

        const existingTemplates = AppState.getTemplatesForTheme(themeId);
        const baseOptions = existingTemplates.map(t => ({ value: String(t.id), label: t.name }));

        const bodyHtml = `
            ${Components.formField('Template name', Components.textInput('newTemplateName', '', { placeholder: 'e.g., Summer Sale' }), { required: true })}
            ${Components.formField('Template type', Components.dropdown('newTemplateType', [
                { value: 'product', label: 'Product' },
                { value: 'collection', label: 'Collection' },
                { value: 'page', label: 'Page' },
                { value: 'blog', label: 'Blog' },
                { value: 'blog-post', label: 'Blog post' }
            ], 'product'))}
            ${Components.formField('Based on', Components.dropdown('newTemplateBase', [
                { value: '', label: 'Empty template' },
                ...baseOptions
            ], ''))}
        `;

        Components.showModal('Create template', bodyHtml,
            `<button class="btn btn-secondary" onclick="Components.closeModal()">Cancel</button>
             <button class="btn btn-primary" id="createTemplateConfirmBtn">Create</button>`
        );

        setTimeout(() => {
            const btn = document.getElementById('createTemplateConfirmBtn');
            if (btn) {
                btn.addEventListener('click', () => {
                    const name = document.getElementById('newTemplateName')?.value;
                    const type = document.getElementById('newTemplateType')?.dataset.value || 'product';
                    const baseId = document.getElementById('newTemplateBase')?.dataset.value;

                    if (!name || !name.trim()) {
                        Components.showToast('Template name is required', 'error');
                        return;
                    }

                    const template = AppState.createTemplate(themeId, name.trim(), type, baseId ? parseInt(baseId) : null);
                    if (template) {
                        Components.closeModal();
                        Components.showToast('Template created', 'success');
                        AppState.selectedTemplateId = template.id;
                        Router.render();
                    }
                });
            }
        }, 100);
    },

    // ==============================
    // Rename Theme Modal
    // ==============================
    _showRenameThemeModal(themeId) {
        const theme = AppState.getTheme(themeId);
        if (!theme) return;

        const bodyHtml = Components.formField('Theme name', Components.textInput('renameThemeInput', theme.name), { required: true });

        Components.showModal('Rename theme', bodyHtml,
            `<button class="btn btn-secondary" onclick="Components.closeModal()">Cancel</button>
             <button class="btn btn-primary" id="renameThemeConfirmBtn">Save</button>`
        );

        setTimeout(() => {
            const btn = document.getElementById('renameThemeConfirmBtn');
            if (btn) {
                btn.addEventListener('click', () => {
                    const name = document.getElementById('renameThemeInput')?.value;
                    if (name && name.trim()) {
                        AppState.renameTheme(themeId, name.trim());
                        Components.closeModal();
                        Components.showToast('Theme renamed', 'success');
                        Router.render();
                    }
                });
            }
        }, 100);
    },

    // ==============================
    // Add Theme Modal
    // ==============================
    _showAddThemeModal() {
        if (AppState.themes.length >= AppState.currentUser.maxThemes) {
            Components.showToast(`Maximum ${AppState.currentUser.maxThemes} themes reached`, 'error');
            return;
        }

        const bodyHtml = `
            ${Components.formField('Theme name', Components.textInput('newThemeName', '', { placeholder: 'My new theme' }), { required: true })}
            ${Components.formField('Source', Components.dropdown('newThemeSource', [
                { value: 'shopify', label: 'Free Shopify theme' },
                { value: 'theme-store', label: 'Theme Store' },
                { value: 'upload', label: 'Upload ZIP file' }
            ], 'shopify'))}
            ${Components.formField('Architecture', Components.dropdown('newThemeArch', [
                { value: 'online_store_2.0', label: 'Online Store 2.0' },
                { value: 'theme_blocks', label: 'Theme Blocks (latest)' }
            ], 'online_store_2.0'))}
        `;

        Components.showModal('Add theme', bodyHtml,
            `<button class="btn btn-secondary" onclick="Components.closeModal()">Cancel</button>
             <button class="btn btn-primary" id="addThemeConfirmBtn">Add theme</button>`
        );

        setTimeout(() => {
            const btn = document.getElementById('addThemeConfirmBtn');
            if (btn) {
                btn.addEventListener('click', () => {
                    const name = document.getElementById('newThemeName')?.value;
                    const source = document.getElementById('newThemeSource')?.dataset.value || 'shopify';
                    const arch = document.getElementById('newThemeArch')?.dataset.value || 'online_store_2.0';

                    if (!name || !name.trim()) {
                        Components.showToast('Theme name is required', 'error');
                        return;
                    }

                    const theme = AppState.addTheme(name.trim(), source, arch);
                    if (theme) {
                        Components.closeModal();
                        Components.showToast('Theme added', 'success');
                        Router.render();
                    }
                });
            }
        }, 100);
    }
};

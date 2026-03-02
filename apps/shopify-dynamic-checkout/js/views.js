/* ============================================================
   Shopify Dynamic Checkout – View Renderers
   ============================================================ */

const Views = {

    // ---- Sidebar ----
    renderSidebar() {
        const view = AppState.currentView;
        const items = [
            { route: '#/themes', icon: this._iconTheme(), label: 'Themes', view: 'themes' },
            { route: '#/theme-editor', icon: this._iconEditor(), label: 'Theme editor', view: 'theme-editor' },
            { route: '#/products', icon: this._iconProducts(), label: 'Products', view: 'products' },
            { route: '#/payments', icon: this._iconPayments(), label: 'Payments', view: 'payments' },
            { route: '#/compatibility', icon: this._iconCompat(), label: 'Compatibility', view: 'compatibility' },
            { route: '#/activity', icon: this._iconActivity(), label: 'Activity log', view: 'activity' }
        ];

        const activeViews = {
            'themes': 'themes',
            'theme-detail': 'themes',
            'theme-editor': 'theme-editor',
            'theme-settings-colors': 'theme-editor',
            'theme-settings-typography': 'theme-editor',
            'products': 'products',
            'product-detail': 'products',
            'payments': 'payments',
            'compatibility': 'compatibility',
            'activity': 'activity'
        };
        const activeView = activeViews[view] || view;

        const issues = AppState.getCompatibilityIssues();
        const warningCount = issues.filter(i => i.severity === 'warning').length;

        return `
            <div class="sidebar-section">
                <div class="sidebar-section-title">Online Store</div>
                ${items.slice(0, 2).map(item => `
                    <a class="sidebar-item ${activeView === item.view ? 'active' : ''}" data-route="${item.route}">
                        <span class="sidebar-icon">${item.icon}</span>
                        <span class="sidebar-label">${item.label}</span>
                    </a>`).join('')}
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">Store</div>
                ${items.slice(2, 3).map(item => `
                    <a class="sidebar-item ${activeView === item.view ? 'active' : ''}" data-route="${item.route}">
                        <span class="sidebar-icon">${item.icon}</span>
                        <span class="sidebar-label">${item.label}</span>
                    </a>`).join('')}
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">Settings</div>
                ${items.slice(3).map(item => `
                    <a class="sidebar-item ${activeView === item.view ? 'active' : ''}" data-route="${item.route}">
                        <span class="sidebar-icon">${item.icon}</span>
                        <span class="sidebar-label">${item.label}</span>
                        ${item.view === 'compatibility' && warningCount > 0 ? `<span class="sidebar-badge warning">${warningCount}</span>` : ''}
                    </a>`).join('')}
            </div>`;
    },

    // ---- Content router ----
    renderContent() {
        switch (AppState.currentView) {
            case 'themes': return this.renderThemesList();
            case 'theme-detail': return this.renderThemeDetail();
            case 'theme-editor': return this.renderThemeEditor();
            case 'theme-settings-colors': return this.renderThemeSettingsColors();
            case 'theme-settings-typography': return this.renderThemeSettingsTypography();
            case 'products': return this.renderProductsList();
            case 'product-detail': return this.renderProductDetail();
            case 'payments': return this.renderPayments();
            case 'compatibility': return this.renderCompatibility();
            case 'activity': return this.renderActivityLog();
            default: return this.renderThemesList();
        }
    },

    // ================================================================
    // THEMES LIST
    // ================================================================
    renderThemesList() {
        const published = AppState.getPublishedTheme();
        const others = AppState.themes.filter(t => t.role !== 'main');

        let html = `<div class="page-header">
            <h1>Themes</h1>
        </div>`;

        // Published theme
        if (published) {
            html += `
            <div class="card" data-testid="published-theme">
                <div class="card-header">
                    <h2>Current theme</h2>
                    <div class="card-actions">
                        <button class="btn btn-secondary" data-action="view-theme" data-theme-id="${published.id}">Customize</button>
                        <button class="btn btn-primary" data-action="edit-theme" data-theme-id="${published.id}">Edit theme</button>
                    </div>
                </div>
                <div class="theme-card-body">
                    <div class="theme-preview-placeholder">
                        <div class="theme-preview-colors">
                            <div class="color-dot" style="background:${Components.escapeAttr(published.settings.colors.accentColor)}"></div>
                            <div class="color-dot" style="background:${Components.escapeAttr(published.settings.colors.primaryText)}"></div>
                            <div class="color-dot" style="background:${Components.escapeAttr(published.settings.colors.secondaryBg)}"></div>
                        </div>
                    </div>
                    <div class="theme-info">
                        <h3>${Components.escapeHtml(published.name)}</h3>
                        ${Components.statusBadge('main')}
                        <div class="theme-meta">
                            <span>Version ${Components.escapeHtml(published.version)}</span>
                            <span>by ${Components.escapeHtml(published.author)}</span>
                            <span>Updated ${Components.timeAgo(published.lastUpdated)}</span>
                        </div>
                    </div>
                </div>
            </div>`;
        }

        // Other themes
        html += `
        <div class="card" data-testid="other-themes">
            <div class="card-header">
                <h2>Theme library</h2>
            </div>
            <div class="theme-library-list">`;

        others.forEach(theme => {
            html += `
                <div class="theme-library-item" data-testid="theme-${theme.id}">
                    <div class="theme-library-preview">
                        <div class="theme-preview-colors">
                            <div class="color-dot" style="background:${Components.escapeAttr(theme.settings.colors.accentColor)}"></div>
                            <div class="color-dot" style="background:${Components.escapeAttr(theme.settings.colors.primaryText)}"></div>
                        </div>
                    </div>
                    <div class="theme-library-info">
                        <div class="theme-library-name">
                            <strong>${Components.escapeHtml(theme.name)}</strong>
                            ${Components.statusBadge(theme.role)}
                        </div>
                        <div class="theme-meta">
                            <span>v${Components.escapeHtml(theme.version)}</span>
                            <span>by ${Components.escapeHtml(theme.author)}</span>
                            <span>Updated ${Components.timeAgo(theme.lastUpdated)}</span>
                        </div>
                    </div>
                    <div class="theme-library-actions">
                        <button class="btn btn-secondary btn-sm" data-action="view-theme" data-theme-id="${theme.id}">Customize</button>
                        <button class="btn btn-secondary btn-sm" data-action="edit-theme" data-theme-id="${theme.id}">Edit theme</button>
                        <button class="btn btn-primary btn-sm" data-action="publish-theme" data-theme-id="${theme.id}">Publish</button>
                    </div>
                </div>`;
        });

        html += '</div></div>';
        return html;
    },

    // ================================================================
    // THEME DETAIL (Customize)
    // ================================================================
    renderThemeDetail() {
        const theme = AppState.getThemeById(AppState.currentThemeId);
        if (!theme) return Components.emptyState('', 'Theme not found', 'The selected theme could not be found.');

        const templates = AppState.getTemplatesForTheme(theme.id);

        let html = Components.breadcrumb([
            { label: 'Themes', route: '#/themes' },
            { label: theme.name }
        ]);

        html += `<div class="page-header">
            <h1>${Components.escapeHtml(theme.name)}</h1>
            ${Components.statusBadge(theme.role)}
        </div>`;

        // Templates section
        html += `
        <div class="card" data-testid="templates-card">
            <div class="card-header">
                <h2>Product templates</h2>
                <button class="btn btn-primary btn-sm" data-action="create-template" data-theme-id="${theme.id}">Create alternate template</button>
            </div>
            <div class="template-list">`;

        templates.forEach(tmpl => {
            html += `
                <div class="template-item" data-testid="template-${tmpl.id}">
                    <div class="template-info">
                        <strong>${Components.escapeHtml(tmpl.name)}</strong>
                        ${tmpl.isDefault ? '<span class="badge badge-default">Default</span>' : '<span class="badge badge-alternate">Alternate</span>'}
                        <div class="template-meta">
                            <span>Handle: <code>${Components.escapeHtml(tmpl.handle)}</code></span>
                            <span>Button: "${Components.escapeHtml(tmpl.buyButtonText)}"</span>
                        </div>
                    </div>
                    <div class="template-controls">
                        ${Components.toggle('tmpl-checkout-' + tmpl.id, tmpl.showAcceleratedCheckout, 'Show accelerated checkout buttons', { 'template-id': tmpl.id })}
                    </div>
                    <div class="template-actions">
                        ${!tmpl.isDefault ? `<button class="btn btn-text btn-sm btn-danger-text" data-action="delete-template" data-template-id="${tmpl.id}">Delete</button>` : ''}
                    </div>
                </div>`;
        });

        html += '</div></div>';

        // Button preview
        html += `
        <div class="card" data-testid="button-preview-card">
            <div class="card-header">
                <h2>Button preview</h2>
            </div>
            <div class="card-body">
                <p class="help-text">Preview how accelerated checkout buttons will appear with the current theme and payment settings.</p>
                ${templates.map(tmpl => `
                    <div class="preview-section">
                        <h4>${Components.escapeHtml(tmpl.name)}</h4>
                        ${Components.checkoutButtonPreview(theme, tmpl, AppState.paymentMethods)}
                    </div>
                `).join('')}
            </div>
        </div>`;

        // Products using this theme's templates
        html += `
        <div class="card" data-testid="products-by-template">
            <div class="card-header">
                <h2>Products by template</h2>
            </div>
            <div class="card-body">`;

        templates.forEach(tmpl => {
            const prods = AppState.products.filter(p => p.templateId === tmpl.id);
            html += `
                <div class="template-products-section">
                    <h4>${Components.escapeHtml(tmpl.name)} <span class="count">(${prods.length} products)</span></h4>
                    ${prods.length > 0 ? `
                        <div class="product-chips">
                            ${prods.map(p => `<span class="product-chip" data-route="#/products/${p.id}">${Components.escapeHtml(p.title)}</span>`).join('')}
                        </div>` : '<p class="help-text">No products assigned to this template.</p>'}
                </div>`;
        });

        html += '</div></div>';
        return html;
    },

    // ================================================================
    // THEME EDITOR
    // ================================================================
    renderThemeEditor() {
        const themeId = AppState.editingThemeId || (AppState.getPublishedTheme() || {}).id;
        const theme = themeId ? AppState.getThemeById(themeId) : null;
        if (!theme) return Components.emptyState('', 'No theme selected', 'Select a theme to edit from the Themes page.');

        const pages = AppState.getPagesForTheme(theme.id);
        const templates = AppState.getTemplatesForTheme(theme.id);
        const currentPageId = AppState.editorPage || (pages.length > 0 ? pages[0].id : null);
        const currentPage = pages.find(p => p.id === currentPageId);

        let html = Components.breadcrumb([
            { label: 'Themes', route: '#/themes' },
            { label: theme.name + ' - Editor' }
        ]);

        html += `<div class="page-header">
            <h1>Theme editor: ${Components.escapeHtml(theme.name)}</h1>
            ${Components.statusBadge(theme.role)}
        </div>`;

        // Editor layout: sidebar + main
        html += '<div class="editor-layout">';

        // Editor sidebar with page navigation
        html += '<div class="editor-sidebar">';

        // Theme selector
        html += `<div class="editor-theme-selector">
            ${Components.dropdown('editor-theme-select',
                AppState.themes.map(t => ({ value: t.id, label: t.name + (t.role === 'main' ? ' (Published)' : '') })),
                theme.id, 'Select theme...')}
        </div>`;

        // Page navigation
        html += `
        <div class="editor-nav">
            <div class="editor-nav-title">Pages</div>
            ${pages.map(p => `
                <a class="editor-nav-item ${p.id === currentPageId ? 'active' : ''}" data-action="editor-select-page" data-page-id="${p.id}">
                    <span class="editor-nav-icon">${this._getPageIcon(p.type)}</span>
                    ${Components.escapeHtml(p.name)}
                </a>`).join('')}
        </div>`;

        // Template selector (only on product pages)
        if (currentPage && currentPage.type === 'product') {
            html += `
            <div class="editor-nav">
                <div class="editor-nav-title">Product templates</div>
                ${templates.map(t => `
                    <a class="editor-nav-item ${t.id === AppState.currentTemplateId ? 'active' : ''}" data-action="editor-select-template" data-template-id="${t.id}">
                        ${Components.escapeHtml(t.name)}
                        ${t.isDefault ? '<span class="badge badge-sm">Default</span>' : ''}
                    </a>`).join('')}
            </div>`;
        }

        // Theme settings links
        html += `
        <div class="editor-nav">
            <div class="editor-nav-title">Theme settings</div>
            <a class="editor-nav-item" data-route="#/theme-settings/colors">
                <span class="editor-nav-icon">${this._iconPalette()}</span>
                Colors
            </a>
            <a class="editor-nav-item" data-route="#/theme-settings/typography">
                <span class="editor-nav-icon">${this._iconType()}</span>
                Typography
            </a>
        </div>`;

        html += '</div>'; // .editor-sidebar

        // Editor main content
        html += '<div class="editor-main">';

        if (currentPage) {
            html += this._renderEditorPageContent(theme, currentPage, templates);
        }

        html += '</div>'; // .editor-main
        html += '</div>'; // .editor-layout

        return html;
    },

    _renderEditorPageContent(theme, page, templates) {
        const sections = AppState.getSectionsForPage(page.id);
        let html = `<h2>${Components.escapeHtml(page.name)}</h2>`;

        if (page.type === 'product') {
            // Product page template settings
            const tmplId = AppState.currentTemplateId || (templates.length > 0 ? templates[0].id : null);
            const tmpl = tmplId ? AppState.getTemplateById(tmplId) : null;

            if (tmpl) {
                html += `
                <div class="editor-section" data-testid="product-info-section">
                    <div class="editor-section-header" data-action="toggle-editor-section" data-section="product-info">
                        <span>Product information</span>
                        <svg class="section-arrow" viewBox="0 0 20 20" width="16" height="16"><path d="M5 7.5L10 12.5L15 7.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
                    </div>
                    <div class="editor-section-content">
                        <div class="editor-block" data-testid="buy-buttons-block">
                            <div class="editor-block-header" data-action="toggle-editor-block" data-block="buy-buttons">
                                <span>Buy buttons</span>
                                <svg class="section-arrow" viewBox="0 0 20 20" width="12" height="12"><path d="M5 7.5L10 12.5L15 7.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
                            </div>
                            <div class="editor-block-content">
                                ${Components.toggle('editor-checkout-' + tmpl.id, tmpl.showAcceleratedCheckout, 'Show accelerated checkout buttons', { 'template-id': tmpl.id })}
                                <div class="field-group">
                                    <label class="field-label">Button text</label>
                                    <input type="text" class="text-input" value="${Components.escapeAttr(tmpl.buyButtonText)}" data-action="update-buy-button-text" data-template-id="${tmpl.id}" />
                                </div>
                                ${Components.toggle('editor-qty-' + tmpl.id, tmpl.showQuantitySelector, 'Show quantity selector', { 'template-id': tmpl.id, 'field': 'quantity' })}
                            </div>
                        </div>
                    </div>
                </div>`;

                // Preview
                html += `
                <div class="editor-preview">
                    <h3>Preview</h3>
                    ${Components.checkoutButtonPreview(theme, tmpl, AppState.paymentMethods)}
                </div>`;
            }
        } else if (page.type === 'home') {
            // Home page sections
            html += '<div class="editor-sections-list">';

            sections.forEach(section => {
                html += this._renderEditorSection(section, theme);
            });

            html += `
                <button class="btn btn-secondary add-section-btn" data-action="add-section" data-theme-id="${theme.id}" data-page-id="${page.id}">
                    <svg viewBox="0 0 20 20" width="16" height="16"><path d="M10 5v10M5 10h10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
                    Add section
                </button>
            </div>`;
        } else {
            html += `<p class="help-text">Select a section to edit its settings.</p>`;
            sections.forEach(section => {
                html += this._renderEditorSection(section, theme);
            });
        }

        return html;
    },

    _renderEditorSection(section, theme) {
        let html = `
            <div class="editor-section" data-testid="section-${section.id}">
                <div class="editor-section-header" data-action="toggle-editor-section" data-section="${section.id}">
                    <span>${Components.escapeHtml(section.label)}</span>
                    <svg class="section-arrow" viewBox="0 0 20 20" width="16" height="16"><path d="M5 7.5L10 12.5L15 7.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
                </div>
                <div class="editor-section-content ${AppState.editorSection === section.id ? 'open' : ''}">`;

        if (section.type === 'featured_product') {
            const product = section.productId ? AppState.getProductById(section.productId) : null;
            html += `
                <div class="field-group">
                    <label class="field-label">Product</label>
                    ${Components.dropdown('section-product-' + section.id,
                        AppState.products.filter(p => p.status === 'active').map(p => ({ value: p.id, label: p.title })),
                        section.productId, 'Select product...')}
                </div>
                ${Components.toggle('section-checkout-' + section.id, section.showAcceleratedCheckout, 'Show accelerated checkout buttons', { 'section-id': section.id })}
                ${section.showAcceleratedCheckout && product ? `
                    <div class="section-preview">
                        <h4>Button preview</h4>
                        ${Components.checkoutButtonPreview(theme, { showAcceleratedCheckout: true, buyButtonText: 'Add to cart' }, AppState.paymentMethods)}
                    </div>` : ''}
                <button class="btn btn-text btn-sm btn-danger-text" data-action="remove-section" data-section-id="${section.id}">Remove section</button>`;
        } else if (section.type === 'product_information') {
            if (section.blocks) {
                html += '<div class="editor-blocks">';
                section.blocks.forEach(block => {
                    html += `
                        <div class="editor-block-item">
                            <span>${Components.escapeHtml(block.label)}</span>
                            ${block.type === 'buy_buttons' ? '<span class="badge badge-sm">Checkout settings</span>' : ''}
                        </div>`;
                });
                html += '</div>';
            }
        } else {
            html += `<p class="help-text">Configure ${Components.escapeHtml(section.label)} settings.</p>`;
        }

        html += '</div></div>';
        return html;
    },

    // ================================================================
    // THEME SETTINGS - COLORS
    // ================================================================
    renderThemeSettingsColors() {
        const themeId = AppState.editingThemeId || (AppState.getPublishedTheme() || {}).id;
        const theme = themeId ? AppState.getThemeById(themeId) : null;
        if (!theme) return Components.emptyState('', 'No theme selected', 'Select a theme to edit.');

        const colors = theme.settings.colors;

        let html = Components.breadcrumb([
            { label: 'Themes', route: '#/themes' },
            { label: theme.name, route: '#/theme-editor' },
            { label: 'Colors' }
        ]);

        html += `<div class="page-header">
            <h1>Colors — ${Components.escapeHtml(theme.name)}</h1>
        </div>`;

        html += `
        <div class="card" data-testid="color-settings">
            <div class="card-header"><h2>Accelerated checkout button</h2></div>
            <div class="card-body">
                <p class="help-text">Customize the background and text color of your unbranded accelerated checkout buttons. Branded buttons (Shop Pay, Apple Pay, etc.) cannot be customized.</p>
                ${Components.colorPicker('color-accent-bg', colors.accentButtonBg, 'Button background')}
                ${Components.colorPicker('color-accent-text', colors.accentButtonText, 'Button text')}
                <div class="color-preview-section">
                    <h4>Preview</h4>
                    <button class="preview-buy-now" style="background:${Components.escapeAttr(colors.accentButtonBg)};color:${Components.escapeAttr(colors.accentButtonText)};font-family:${Components.escapeAttr(theme.settings.typography.buttonFont)},sans-serif">Buy it now</button>
                </div>
            </div>
        </div>`;

        html += `
        <div class="card">
            <div class="card-header"><h2>General colors</h2></div>
            <div class="card-body">
                ${Components.colorPicker('color-primary-bg', colors.primaryBg, 'Primary background')}
                ${Components.colorPicker('color-primary-text', colors.primaryText, 'Primary text')}
                ${Components.colorPicker('color-secondary-bg', colors.secondaryBg, 'Secondary background')}
                ${Components.colorPicker('color-secondary-text', colors.secondaryText, 'Secondary text')}
                ${Components.colorPicker('color-accent', colors.accentColor, 'Accent color')}
            </div>
        </div>`;

        html += `
        <div class="page-actions">
            <button class="btn btn-primary" data-action="save-colors" data-theme-id="${theme.id}">Save</button>
        </div>`;

        return html;
    },

    // ================================================================
    // THEME SETTINGS - TYPOGRAPHY
    // ================================================================
    renderThemeSettingsTypography() {
        const themeId = AppState.editingThemeId || (AppState.getPublishedTheme() || {}).id;
        const theme = themeId ? AppState.getThemeById(themeId) : null;
        if (!theme) return Components.emptyState('', 'No theme selected', 'Select a theme to edit.');

        const typo = theme.settings.typography;

        let html = Components.breadcrumb([
            { label: 'Themes', route: '#/themes' },
            { label: theme.name, route: '#/theme-editor' },
            { label: 'Typography' }
        ]);

        html += `<div class="page-header">
            <h1>Typography — ${Components.escapeHtml(theme.name)}</h1>
        </div>`;

        html += `
        <div class="card" data-testid="typography-settings">
            <div class="card-header"><h2>Font families</h2></div>
            <div class="card-body">
                <p class="help-text">The button font setting affects the text on your accelerated checkout buttons. Branded buttons are not affected.</p>
                ${Components.fontDropdown('font-heading', typo.headingFont, 'Heading font')}
                ${Components.fontDropdown('font-body', typo.bodyFont, 'Body font')}
                ${Components.fontDropdown('font-button', typo.buttonFont, 'Button font')}
            </div>
        </div>`;

        html += `
        <div class="card">
            <div class="card-header"><h2>Font scale</h2></div>
            <div class="card-body">
                <div class="field-group">
                    <label class="field-label">Heading scale (%)</label>
                    <input type="text" class="text-input text-input-sm" id="heading-scale" value="${typo.headingScale}" data-action="input-change" />
                </div>
                <div class="field-group">
                    <label class="field-label">Body scale (%)</label>
                    <input type="text" class="text-input text-input-sm" id="body-scale" value="${typo.bodyScale}" data-action="input-change" />
                </div>
            </div>
        </div>`;

        html += `
        <div class="card">
            <div class="card-header"><h2>Button preview</h2></div>
            <div class="card-body">
                <button class="preview-buy-now" style="background:${Components.escapeAttr(theme.settings.colors.accentButtonBg)};color:${Components.escapeAttr(theme.settings.colors.accentButtonText)};font-family:${Components.escapeAttr(typo.buttonFont)},sans-serif">Buy it now</button>
                <p class="help-text" style="margin-top:12px">Font: ${Components.escapeHtml(typo.buttonFont)}</p>
            </div>
        </div>`;

        html += `
        <div class="page-actions">
            <button class="btn btn-primary" data-action="save-typography" data-theme-id="${theme.id}">Save</button>
        </div>`;

        return html;
    },

    // ================================================================
    // PRODUCTS LIST
    // ================================================================
    renderProductsList() {
        const { items, total, page, totalPages } = AppState.getPagedProducts();
        const published = AppState.getPublishedTheme();
        const templates = published ? AppState.getTemplatesForTheme(published.id) : [];

        let html = `<div class="page-header">
            <h1>Products</h1>
        </div>`;

        // Toolbar
        html += `
        <div class="toolbar" data-testid="products-toolbar">
            ${Components.searchInput(AppState.searchQuery, 'Search products...')}
            <div class="toolbar-filters">
                ${Components.dropdown('product-status-filter',
                    [
                        { value: 'all', label: 'All statuses' },
                        { value: 'active', label: 'Active' },
                        { value: 'draft', label: 'Draft' },
                        { value: 'archived', label: 'Archived' }
                    ], AppState.productFilter, 'Status')}
                ${Components.dropdown('product-sort',
                    [
                        { value: 'title_asc', label: 'Title A-Z' },
                        { value: 'title_desc', label: 'Title Z-A' },
                        { value: 'created_desc', label: 'Newest first' },
                        { value: 'created_asc', label: 'Oldest first' },
                        { value: 'updated_desc', label: 'Recently updated' },
                        { value: 'vendor_asc', label: 'Vendor A-Z' },
                        { value: 'type_asc', label: 'Product type A-Z' }
                    ], AppState.productSort, 'Sort by')}
            </div>
        </div>`;

        if (items.length === 0) {
            html += Components.emptyState(
                '<svg viewBox="0 0 48 48" width="48" height="48"><rect x="8" y="12" width="32" height="24" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 18h32" stroke="currentColor" stroke-width="2"/></svg>',
                'No products found',
                AppState.searchQuery ? 'Try adjusting your search or filters.' : 'Add products to your store to manage checkout buttons.'
            );
        } else {
            html += `
            <div class="card">
                <table class="data-table" data-testid="products-table">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Status</th>
                            <th>Template</th>
                            <th>Checkout buttons</th>
                            <th>Vendor</th>
                            <th>Type</th>
                        </tr>
                    </thead>
                    <tbody>`;

            items.forEach(product => {
                const tmpl = AppState.getTemplateById(product.templateId);
                const hasCheckout = tmpl ? tmpl.showAcceleratedCheckout : false;
                const checkoutBlocked = product.hasGiftCardRecipientFields;

                html += `
                    <tr class="product-row" data-route="#/products/${product.id}" data-testid="product-${product.id}">
                        <td>
                            <div class="product-cell">
                                <strong>${Components.escapeHtml(product.title)}</strong>
                                <span class="product-variants-count">${product.variants.length} variants</span>
                            </div>
                        </td>
                        <td>${Components.statusBadge(product.status)}</td>
                        <td><span class="template-label">${tmpl ? Components.escapeHtml(tmpl.name) : '—'}</span></td>
                        <td>
                            ${checkoutBlocked
                                ? '<span class="checkout-status blocked">Blocked (gift card)</span>'
                                : (hasCheckout
                                    ? '<span class="checkout-status enabled">Enabled</span>'
                                    : '<span class="checkout-status disabled">Disabled</span>')}
                        </td>
                        <td>${Components.escapeHtml(product.vendor)}</td>
                        <td>${Components.escapeHtml(product.productType)}</td>
                    </tr>`;
            });

            html += '</tbody></table></div>';
            html += Components.pagination(page, totalPages, total);
        }

        return html;
    },

    // ================================================================
    // PRODUCT DETAIL
    // ================================================================
    renderProductDetail() {
        const product = AppState.getProductById(AppState.currentProductId);
        if (!product) return Components.emptyState('', 'Product not found', 'The selected product could not be found.');

        const published = AppState.getPublishedTheme();
        const templates = published ? AppState.getTemplatesForTheme(published.id) : [];
        const currentTmpl = AppState.getTemplateById(product.templateId);

        let html = Components.breadcrumb([
            { label: 'Products', route: '#/products' },
            { label: product.title }
        ]);

        html += `<div class="page-header">
            <h1>${Components.escapeHtml(product.title)}</h1>
            ${Components.statusBadge(product.status)}
        </div>`;

        // Product info
        html += `
        <div class="card" data-testid="product-info">
            <div class="card-header"><h2>Product details</h2></div>
            <div class="card-body">
                <div class="detail-grid">
                    <div class="detail-item"><span class="detail-label">Vendor</span><span class="detail-value">${Components.escapeHtml(product.vendor)}</span></div>
                    <div class="detail-item"><span class="detail-label">Type</span><span class="detail-value">${Components.escapeHtml(product.productType)}</span></div>
                    <div class="detail-item"><span class="detail-label">Created</span><span class="detail-value">${Components.formatDate(product.createdAt)}</span></div>
                    <div class="detail-item"><span class="detail-label">Updated</span><span class="detail-value">${Components.formatDate(product.updatedAt)}</span></div>
                    <div class="detail-item"><span class="detail-label">Tags</span><span class="detail-value">${product.tags.map(t => `<span class="tag">${Components.escapeHtml(t)}</span>`).join(' ')}</span></div>
                    ${product.hasGiftCardRecipientFields ? '<div class="detail-item full-width">' + Components.infoBox('This product has active gift card recipient fields. Accelerated checkout buttons won\'t display.', 'warning') + '</div>' : ''}
                </div>
            </div>
        </div>`;

        // Template assignment
        html += `
        <div class="card" data-testid="template-assignment">
            <div class="card-header"><h2>Theme template</h2></div>
            <div class="card-body">
                <p class="help-text">Assign a product template to control whether accelerated checkout buttons appear for this product.</p>
                <div class="field-group">
                    <label class="field-label">Product template</label>
                    ${Components.dropdown('product-template-' + product.id,
                        templates.map(t => ({
                            value: t.id,
                            label: t.name + (t.showAcceleratedCheckout ? ' (checkout enabled)' : ' (checkout disabled)')
                        })),
                        product.templateId, 'Select template...')}
                </div>
                ${currentTmpl ? `
                <div class="template-status-info">
                    <strong>Current template:</strong> ${Components.escapeHtml(currentTmpl.name)}<br>
                    <strong>Accelerated checkout:</strong> ${currentTmpl.showAcceleratedCheckout ? '<span class="checkout-status enabled">Enabled</span>' : '<span class="checkout-status disabled">Disabled</span>'}
                </div>` : ''}
            </div>
        </div>`;

        // Product status
        html += `
        <div class="card" data-testid="product-status">
            <div class="card-header"><h2>Product status</h2></div>
            <div class="card-body">
                ${Components.dropdown('product-status-' + product.id,
                    [
                        { value: 'active', label: 'Active' },
                        { value: 'draft', label: 'Draft' },
                        { value: 'archived', label: 'Archived' }
                    ], product.status, 'Status')}
            </div>
        </div>`;

        // Variants
        html += `
        <div class="card" data-testid="product-variants">
            <div class="card-header"><h2>Variants <span class="count">(${product.variants.length})</span></h2></div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Variant</th>
                        <th>Price</th>
                        <th>Compare at</th>
                        <th>SKU</th>
                        <th>Inventory</th>
                    </tr>
                </thead>
                <tbody>
                    ${product.variants.map(v => `
                        <tr>
                            <td>${Components.escapeHtml(v.title)}</td>
                            <td>${Components.formatPrice(v.price)}</td>
                            <td>${v.compareAtPrice ? Components.formatPrice(v.compareAtPrice) : '—'}</td>
                            <td><code>${Components.escapeHtml(v.sku)}</code></td>
                            <td>${v.inventoryQty !== null ? v.inventoryQty : '—'}</td>
                        </tr>`).join('')}
                </tbody>
            </table>
        </div>`;

        // Button preview
        if (published && currentTmpl) {
            html += `
            <div class="card" data-testid="product-checkout-preview">
                <div class="card-header"><h2>Checkout button preview</h2></div>
                <div class="card-body">
                    ${product.hasGiftCardRecipientFields
                        ? Components.infoBox('Accelerated checkout buttons are not available for products with gift card recipient fields.', 'info')
                        : Components.checkoutButtonPreview(published, currentTmpl, AppState.paymentMethods)}
                </div>
            </div>`;
        }

        return html;
    },

    // ================================================================
    // PAYMENTS
    // ================================================================
    renderPayments() {
        const accelerated = AppState.paymentMethods.filter(pm => pm.type === 'accelerated');
        const other = AppState.paymentMethods.filter(pm => pm.type !== 'accelerated');

        let html = `<div class="page-header">
            <h1>Payment settings</h1>
        </div>`;

        // Shop Promise
        html += `
        <div class="card" data-testid="shop-promise-settings">
            <div class="card-header">
                <h2>Shop Promise</h2>
            </div>
            <div class="card-body">
                <p class="help-text">When Shop Promise is active, Shop Pay is prioritized over other accelerated checkout methods.</p>
                ${Components.toggle('shop-promise-toggle', AppState.shopPromise.isActive, 'Enable Shop Promise')}
                ${AppState.shopPromise.isActive ? `
                <div class="shop-promise-details">
                    <div class="field-group">
                        <label class="field-label">Estimated delivery (days)</label>
                        <div class="range-inputs">
                            <input type="text" class="text-input text-input-sm" id="promise-min-days" value="${AppState.shopPromise.estimatedDeliveryDays.min}" data-action="input-change" />
                            <span>to</span>
                            <input type="text" class="text-input text-input-sm" id="promise-max-days" value="${AppState.shopPromise.estimatedDeliveryDays.max}" data-action="input-change" />
                        </div>
                    </div>
                    <div class="field-group">
                        <label class="field-label">Free shipping threshold ($)</label>
                        <input type="text" class="text-input text-input-sm" id="promise-threshold" value="${AppState.shopPromise.freeShippingThreshold}" data-action="input-change" />
                    </div>
                </div>` : ''}
            </div>
        </div>`;

        // Accelerated checkout methods
        html += `
        <div class="card" data-testid="accelerated-methods">
            <div class="card-header">
                <h2>Accelerated checkout methods</h2>
            </div>
            <div class="card-body">
                <p class="help-text">These payment methods display as branded accelerated checkout buttons on your store. Only active methods appear as buttons.</p>
                <div class="payment-methods-list">
                    ${accelerated.map(pm => this._renderPaymentMethod(pm)).join('')}
                </div>
            </div>
        </div>`;

        // Other payment methods
        html += `
        <div class="card" data-testid="other-methods">
            <div class="card-header">
                <h2>Other payment methods</h2>
            </div>
            <div class="card-body">
                <div class="payment-methods-list">
                    ${other.map(pm => this._renderPaymentMethod(pm)).join('')}
                </div>
            </div>
        </div>`;

        // Test buttons section
        html += `
        <div class="card" data-testid="test-buttons">
            <div class="card-header">
                <h2>Test accelerated checkout buttons</h2>
            </div>
            <div class="card-body">
                <p class="help-text">Add debug parameters to your store URL to preview how different accelerated checkout buttons appear. Only active payment methods can be tested.</p>
                <div class="test-buttons-list">
                    ${accelerated.map(pm => `
                        <div class="test-button-item ${pm.isActive ? '' : 'inactive'}">
                            <div class="test-button-info">
                                ${Components.paymentLogo(pm)}
                                <span>${Components.escapeHtml(pm.name)}</span>
                                ${pm.browserRestrictions ? `<span class="restriction-badge">${pm.browserRestrictions === 'safari_only' ? 'Safari only' : pm.browserRestrictions}</span>` : ''}
                                ${pm.regionRestrictions ? `<span class="restriction-badge">${pm.regionRestrictions.join(', ')} only</span>` : ''}
                            </div>
                            <div class="test-button-url">
                                <code>?shopify-debug=true&show=${Components.escapeHtml(pm.debugParam)}</code>
                            </div>
                            <span class="test-button-status">${pm.isActive ? 'Active' : 'Inactive'}</span>
                        </div>`).join('')}
                    <div class="test-button-item">
                        <div class="test-button-info">
                            <div class="payment-logo-placeholder" style="background:#6B7280">U</div>
                            <span>Unbranded (Buy it now)</span>
                        </div>
                        <div class="test-button-url">
                            <code>?shopify-debug=true&show=checkout</code>
                        </div>
                        <span class="test-button-status">Always available</span>
                    </div>
                </div>
            </div>
        </div>`;

        return html;
    },

    _renderPaymentMethod(pm) {
        return `
            <div class="payment-method-item" data-testid="payment-${pm.id}">
                <div class="payment-method-info">
                    ${Components.paymentLogo(pm)}
                    <div class="payment-method-details">
                        <strong>${Components.escapeHtml(pm.name)}</strong>
                        <span class="payment-method-desc">${Components.escapeHtml(pm.description)}</span>
                        ${pm.browserRestrictions ? `<span class="restriction-note">Restriction: ${pm.browserRestrictions === 'safari_only' ? 'Safari only' : pm.browserRestrictions}</span>` : ''}
                        ${pm.regionRestrictions ? `<span class="restriction-note">Available in: ${pm.regionRestrictions.join(', ')}</span>` : ''}
                    </div>
                </div>
                <div class="payment-method-toggle">
                    ${Components.toggle('payment-' + pm.id, pm.isActive, '', { 'payment-id': pm.id })}
                </div>
            </div>`;
    },

    // ================================================================
    // COMPATIBILITY
    // ================================================================
    renderCompatibility() {
        const issues = AppState.getCompatibilityIssues();
        const conflictingApps = AppState.getConflictingApps();
        const conflictingAttrs = AppState.getConflictingCartAttributes();

        let html = `<div class="page-header">
            <h1>Compatibility</h1>
        </div>`;

        // Summary
        const warnings = issues.filter(i => i.severity === 'warning').length;
        const infos = issues.filter(i => i.severity === 'info').length;

        html += `
        <div class="card" data-testid="compatibility-summary">
            <div class="card-header"><h2>Compatibility check</h2></div>
            <div class="card-body">
                ${warnings > 0 || infos > 0
                    ? `<div class="compat-summary">
                        ${warnings > 0 ? `<div class="compat-stat warning"><span class="compat-count">${warnings}</span><span>Warnings</span></div>` : ''}
                        ${infos > 0 ? `<div class="compat-stat info"><span class="compat-count">${infos}</span><span>Info</span></div>` : ''}
                    </div>`
                    : Components.infoBox('No compatibility issues detected. Accelerated checkout buttons are fully compatible with your store configuration.', 'success')}
            </div>
        </div>`;

        if (issues.length > 0) {
            html += `
            <div class="card" data-testid="compatibility-issues">
                <div class="card-header"><h2>Issues</h2></div>
                <div class="card-body">
                    <div class="issues-list">
                        ${issues.map(issue => `
                            <div class="issue-item issue-${issue.severity}" data-testid="issue-${issue.entityId || 'general'}">
                                <div class="issue-icon">
                                    ${issue.severity === 'warning'
                                        ? '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92z" fill="currentColor"/><text x="10" y="14" text-anchor="middle" fill="white" font-size="10" font-weight="bold">!</text></svg>'
                                        : '<svg viewBox="0 0 20 20" width="20" height="20"><circle cx="10" cy="10" r="8" fill="currentColor"/><text x="10" y="14" text-anchor="middle" fill="white" font-size="10" font-weight="bold">i</text></svg>'}
                                </div>
                                <div class="issue-content">
                                    <strong>${Components.escapeHtml(issue.title)}</strong>
                                    <p>${Components.escapeHtml(issue.description)}</p>
                                </div>
                            </div>`).join('')}
                    </div>
                </div>
            </div>`;
        }

        // Installed apps
        html += `
        <div class="card" data-testid="installed-apps">
            <div class="card-header"><h2>Installed apps</h2></div>
            <div class="card-body">
                <p class="help-text">Apps that may conflict with accelerated checkout buttons are highlighted.</p>
                <div class="apps-list">
                    ${AppState.installedApps.map(app => `
                        <div class="app-item ${app.conflictsWithCheckout && app.isActive ? 'conflicting' : ''}">
                            <div class="app-info">
                                <strong>${Components.escapeHtml(app.name)}</strong>
                                <span class="app-developer">by ${Components.escapeHtml(app.developer)}</span>
                                <span class="app-desc">${Components.escapeHtml(app.description)}</span>
                                ${app.conflictsWithCheckout ? `<span class="conflict-badge">Potential conflict</span>` : ''}
                            </div>
                            <div class="app-toggle">
                                ${Components.toggle('app-' + app.id, app.isActive, app.isActive ? 'Active' : 'Inactive', { 'app-id': app.id })}
                            </div>
                        </div>`).join('')}
                </div>
            </div>
        </div>`;

        // Cart attributes
        html += `
        <div class="card" data-testid="cart-attributes">
            <div class="card-header"><h2>Cart attributes</h2></div>
            <div class="card-body">
                <p class="help-text">Accelerated checkout buttons don't support cart attributes. Active conflicting attributes may cause issues.</p>
                <div class="cart-attrs-list">
                    ${AppState.cartAttributes.map(attr => `
                        <div class="cart-attr-item ${attr.conflictsWithCheckout && attr.isActive ? 'conflicting' : ''}">
                            <div class="cart-attr-info">
                                <strong>${Components.escapeHtml(attr.name)}</strong>
                                <span class="cart-attr-type">${Components.escapeHtml(attr.type)}</span>
                                <span class="cart-attr-desc">${Components.escapeHtml(attr.description)}</span>
                                ${attr.conflictsWithCheckout ? '<span class="conflict-badge">Conflicts with checkout</span>' : ''}
                            </div>
                            <div class="cart-attr-toggle">
                                ${Components.toggle('cattr-' + attr.id, attr.isActive, '', { 'attr-id': attr.id })}
                            </div>
                        </div>`).join('')}
                </div>
            </div>
        </div>`;

        return html;
    },

    // ================================================================
    // ACTIVITY LOG
    // ================================================================
    renderActivityLog() {
        const logs = AppState.activityLog;

        let html = `<div class="page-header">
            <h1>Activity log</h1>
        </div>`;

        html += `
        <div class="card" data-testid="activity-log">
            <div class="card-body">
                ${logs.length === 0
                    ? Components.emptyState('', 'No activity yet', 'Actions performed on themes, templates, and payment settings will appear here.')
                    : `<div class="activity-list">
                        ${logs.map(log => `
                            <div class="activity-item" data-testid="log-${log.id}">
                                <div class="activity-icon">${this._getActivityIcon(log.action)}</div>
                                <div class="activity-content">
                                    <strong>${Components.escapeHtml(log.details)}</strong>
                                    <span class="activity-time">${Components.formatDateTime(log.timestamp)}</span>
                                </div>
                            </div>`).join('')}
                    </div>`}
            </div>
        </div>`;

        return html;
    },

    // ---- Helper: Activity icon ----
    _getActivityIcon(action) {
        if (action.includes('enabled') || action.includes('activated')) {
            return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" fill="#059669"/></svg>';
        }
        if (action.includes('disabled') || action.includes('deactivated')) {
            return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" fill="#DC2626"/></svg>';
        }
        if (action.includes('published')) {
            return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zm1 11H9v-2h2v2zm0-4H9V5h2v4z" fill="#2563EB"/></svg>';
        }
        if (action.includes('created') || action.includes('added')) {
            return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" fill="#7C3AED"/></svg>';
        }
        if (action.includes('changed') || action.includes('toggled')) {
            return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" fill="#D97706"/></svg>';
        }
        return '<svg viewBox="0 0 20 20" width="16" height="16"><circle cx="10" cy="10" r="3" fill="#6B7280"/></svg>';
    },

    // ---- Helper: Page icon ----
    _getPageIcon(type) {
        switch (type) {
            case 'home': return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" fill="currentColor"/></svg>';
            case 'product': return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.884l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.116l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4z" fill="currentColor"/></svg>';
            case 'collection': return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z" fill="currentColor"/></svg>';
            case 'cart': return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z" fill="currentColor"/></svg>';
            case 'blog': return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z" fill="currentColor"/><path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h1a2 2 0 002-2V9a2 2 0 00-2-2h-1z" fill="currentColor"/></svg>';
            default: return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" fill="currentColor"/></svg>';
        }
    },

    // ---- Sidebar icons ----
    _iconTheme() { return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4V8h12v7z" fill="currentColor"/></svg>'; },
    _iconEditor() { return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" fill="currentColor"/></svg>'; },
    _iconProducts() { return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.884l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.116l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4z" fill="currentColor"/></svg>'; },
    _iconPayments() { return '<svg viewBox="0 0 20 20" width="16" height="16"><path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" fill="currentColor"/><path fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" fill="currentColor"/></svg>'; },
    _iconCompat() { return '<svg viewBox="0 0 20 20" width="16" height="16"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" fill="currentColor"/></svg>'; },
    _iconActivity() { return '<svg viewBox="0 0 20 20" width="16" height="16"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" fill="currentColor"/></svg>'; },
    _iconPalette() { return '<svg viewBox="0 0 20 20" width="14" height="14"><path d="M4 2a2 2 0 00-2 2v11a3 3 0 106 0V4a2 2 0 00-2-2H4zm1 14a1 1 0 100-2 1 1 0 000 2zm5-1.757l4.9-4.9a2 2 0 000-2.828L13.485 5.1a2 2 0 00-2.828 0L10 5.757v8.486z" fill="currentColor"/></svg>'; },
    _iconType() { return '<svg viewBox="0 0 20 20" width="14" height="14"><path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 01-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" fill="currentColor"/></svg>'; }
};

/* ============================================================
   Shopify Dynamic Checkout – State Management
   ============================================================ */

const AppState = {
    // ---- Persistent data ----
    currentUser: null,
    themes: [],
    templates: [],
    themePages: [],
    themeSections: [],
    paymentMethods: [],
    shopPromise: null,
    products: [],
    collections: [],
    installedApps: [],
    cartAttributes: [],
    activityLog: [],
    availableFonts: [],

    // ---- ID counters ----
    _nextThemeId: 1,
    _nextTemplateId: 1,
    _nextSectionId: 1,
    _nextProductId: 1,
    _nextAppId: 1,
    _nextLogId: 1,
    _nextCartAttrId: 1,
    _nextCollectionId: 1,

    _seedVersion: null,

    // ---- UI state (not persisted) ----
    currentView: 'themes',
    currentThemeId: null,
    currentProductId: null,
    currentTemplateId: null,
    editingThemeId: null,
    editorPage: null,
    editorSection: null,
    searchQuery: '',
    productFilter: 'all',
    productSort: 'title_asc',
    paymentFilter: 'all',
    toastMessage: null,
    toastType: 'info',
    modalOpen: false,
    modalType: null,
    modalData: null,
    sidebarCollapsed: false,
    currentPage: 1,
    pageSize: 10,

    // ---- Listeners ----
    _listeners: [],

    // ---- Initialization ----
    init() {
        const saved = this._loadFromStorage();
        if (saved && saved._seedVersion === SeedData.SEED_DATA_VERSION) {
            this._applySavedState(saved);
        } else {
            this._loadSeedData();
        }
        this._pushStateToServer();
    },

    _loadFromStorage() {
        try {
            const raw = localStorage.getItem('shopifyDynamicCheckoutState');
            if (!raw) return null;
            return JSON.parse(raw);
        } catch (e) {
            return null;
        }
    },

    _applySavedState(saved) {
        this.currentUser = saved.currentUser;
        this.themes = saved.themes;
        this.templates = saved.templates;
        this.themePages = saved.themePages;
        this.themeSections = saved.themeSections;
        this.paymentMethods = saved.paymentMethods;
        this.shopPromise = saved.shopPromise;
        this.products = saved.products;
        this.collections = saved.collections;
        this.installedApps = saved.installedApps;
        this.cartAttributes = saved.cartAttributes;
        this.activityLog = saved.activityLog;
        this.availableFonts = saved.availableFonts;
        this._nextThemeId = saved._nextThemeId;
        this._nextTemplateId = saved._nextTemplateId;
        this._nextSectionId = saved._nextSectionId;
        this._nextProductId = saved._nextProductId;
        this._nextAppId = saved._nextAppId;
        this._nextLogId = saved._nextLogId;
        this._nextCartAttrId = saved._nextCartAttrId;
        this._nextCollectionId = saved._nextCollectionId;
        this._seedVersion = saved._seedVersion;
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(SeedData.CURRENT_USER));
        this.themes = JSON.parse(JSON.stringify(SeedData.THEMES));
        this.templates = JSON.parse(JSON.stringify(SeedData.TEMPLATES));
        this.themePages = JSON.parse(JSON.stringify(SeedData.THEME_PAGES));
        this.themeSections = JSON.parse(JSON.stringify(SeedData.THEME_SECTIONS));
        this.paymentMethods = JSON.parse(JSON.stringify(SeedData.PAYMENT_METHODS));
        this.shopPromise = JSON.parse(JSON.stringify(SeedData.SHOP_PROMISE));
        this.products = JSON.parse(JSON.stringify(SeedData.PRODUCTS));
        this.collections = JSON.parse(JSON.stringify(SeedData.COLLECTIONS));
        this.installedApps = JSON.parse(JSON.stringify(SeedData.INSTALLED_APPS));
        this.cartAttributes = JSON.parse(JSON.stringify(SeedData.CART_ATTRIBUTES));
        this.activityLog = JSON.parse(JSON.stringify(SeedData.ACTIVITY_LOG));
        this.availableFonts = JSON.parse(JSON.stringify(SeedData.AVAILABLE_FONTS));
        Object.assign(this, JSON.parse(JSON.stringify(SeedData.INITIAL_NEXT_IDS)));
        this._seedVersion = SeedData.SEED_DATA_VERSION;
    },

    resetToSeedData() {
        localStorage.removeItem('shopifyDynamicCheckoutState');
        this._loadSeedData();
        this.currentView = 'themes';
        this.currentThemeId = null;
        this.currentProductId = null;
        this.currentTemplateId = null;
        this.editingThemeId = null;
        this.editorPage = null;
        this.editorSection = null;
        this.searchQuery = '';
        this.productFilter = 'all';
        this.productSort = 'title_asc';
        this.paymentFilter = 'all';
        this.toastMessage = null;
        this.modalOpen = false;
        this.modalType = null;
        this.modalData = null;
        this.currentPage = 1;
        this.notify();
    },

    // ---- Serialization ----
    getSerializableState() {
        return {
            currentUser: this.currentUser,
            themes: this.themes,
            templates: this.templates,
            themePages: this.themePages,
            themeSections: this.themeSections,
            paymentMethods: this.paymentMethods,
            shopPromise: this.shopPromise,
            products: this.products,
            collections: this.collections,
            installedApps: this.installedApps,
            cartAttributes: this.cartAttributes,
            activityLog: this.activityLog,
            availableFonts: this.availableFonts,
            _nextThemeId: this._nextThemeId,
            _nextTemplateId: this._nextTemplateId,
            _nextSectionId: this._nextSectionId,
            _nextProductId: this._nextProductId,
            _nextAppId: this._nextAppId,
            _nextLogId: this._nextLogId,
            _nextCartAttrId: this._nextCartAttrId,
            _nextCollectionId: this._nextCollectionId,
            _seedVersion: this._seedVersion
        };
    },

    // ---- Persistence & notification ----
    _persist() {
        localStorage.setItem('shopifyDynamicCheckoutState', JSON.stringify(this.getSerializableState()));
    },

    _pushStateToServer() {
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.getSerializableState())
        }).catch(() => {});
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        this._listeners.forEach(fn => fn());
    },

    subscribe(fn) {
        this._listeners.push(fn);
    },

    // ---- Activity logging ----
    _addLog(action, details, extraFields) {
        const entry = {
            id: 'log_' + this._nextLogId++,
            action,
            userId: this.currentUser.id,
            timestamp: new Date().toISOString(),
            details,
            ...extraFields
        };
        this.activityLog.unshift(entry);
        if (this.activityLog.length > 200) {
            this.activityLog = this.activityLog.slice(0, 200);
        }
    },

    // ---- Getters ----
    getThemeById(id) { return this.themes.find(t => t.id === id); },
    getPublishedTheme() { return this.themes.find(t => t.role === 'main'); },
    getTemplateById(id) { return this.templates.find(t => t.id === id); },
    getTemplatesForTheme(themeId) { return this.templates.filter(t => t.themeId === themeId); },
    getProductById(id) { return this.products.find(p => p.id === id); },
    getPaymentMethodById(id) { return this.paymentMethods.find(pm => pm.id === id); },
    getActiveAcceleratedMethods() { return this.paymentMethods.filter(pm => pm.type === 'accelerated' && pm.isActive); },
    getCollectionById(id) { return this.collections.find(c => c.id === id); },
    getAppById(id) { return this.installedApps.find(a => a.id === id); },
    getConflictingApps() { return this.installedApps.filter(a => a.conflictsWithCheckout && a.isActive); },
    getConflictingCartAttributes() { return this.cartAttributes.filter(ca => ca.conflictsWithCheckout && ca.isActive); },
    getPagesForTheme(themeId) { return this.themePages.filter(p => p.themeId === themeId); },
    getSectionsForPage(pageId) { return this.themeSections.filter(s => s.pageId === pageId).sort((a, b) => a.position - b.position); },
    getSectionById(id) { return this.themeSections.find(s => s.id === id); },

    getFilteredProducts() {
        let list = [...this.products];

        if (this.searchQuery) {
            const q = this.searchQuery.toLowerCase();
            list = list.filter(p =>
                p.title.toLowerCase().includes(q) ||
                p.vendor.toLowerCase().includes(q) ||
                p.productType.toLowerCase().includes(q) ||
                p.tags.some(t => t.toLowerCase().includes(q))
            );
        }

        if (this.productFilter !== 'all') {
            list = list.filter(p => p.status === this.productFilter);
        }

        switch (this.productSort) {
            case 'title_asc': list.sort((a, b) => a.title.localeCompare(b.title)); break;
            case 'title_desc': list.sort((a, b) => b.title.localeCompare(a.title)); break;
            case 'created_desc': list.sort((a, b) => b.createdAt.localeCompare(a.createdAt)); break;
            case 'created_asc': list.sort((a, b) => a.createdAt.localeCompare(b.createdAt)); break;
            case 'updated_desc': list.sort((a, b) => b.updatedAt.localeCompare(a.updatedAt)); break;
            case 'vendor_asc': list.sort((a, b) => a.vendor.localeCompare(b.vendor)); break;
            case 'type_asc': list.sort((a, b) => a.productType.localeCompare(b.productType)); break;
        }

        return list;
    },

    getPagedProducts() {
        const filtered = this.getFilteredProducts();
        const start = (this.currentPage - 1) * this.pageSize;
        return {
            items: filtered.slice(start, start + this.pageSize),
            total: filtered.length,
            page: this.currentPage,
            totalPages: Math.ceil(filtered.length / this.pageSize)
        };
    },

    // ---- Compatibility Checks ----
    getCompatibilityIssues() {
        const issues = [];
        const conflictApps = this.getConflictingApps();
        const conflictAttrs = this.getConflictingCartAttributes();

        conflictApps.forEach(app => {
            issues.push({
                type: 'app_conflict',
                severity: 'warning',
                title: `App conflict: ${app.name}`,
                description: app.conflictReason,
                entityId: app.id,
                entityType: 'app'
            });
        });

        conflictAttrs.forEach(attr => {
            issues.push({
                type: 'cart_attribute_conflict',
                severity: 'warning',
                title: `Cart attribute: ${attr.name}`,
                description: `Accelerated checkout doesn't support cart attributes like "${attr.name}".`,
                entityId: attr.id,
                entityType: 'cartAttribute'
            });
        });

        // Gift card products with recipient fields
        this.products.filter(p => p.hasGiftCardRecipientFields && p.status === 'active').forEach(p => {
            issues.push({
                type: 'gift_card_recipient',
                severity: 'info',
                title: `Gift card: ${p.title}`,
                description: 'Products with active recipient fields won\'t display accelerated checkout buttons.',
                entityId: p.id,
                entityType: 'product'
            });
        });

        // Button text conflicts
        const published = this.getPublishedTheme();
        if (published) {
            const templates = this.getTemplatesForTheme(published.id);
            templates.forEach(tmpl => {
                if (tmpl.showAcceleratedCheckout && (tmpl.buyButtonText === 'Buy it now' || tmpl.buyButtonText === 'Buy now')) {
                    issues.push({
                        type: 'button_text_conflict',
                        severity: 'warning',
                        title: `Confusing button text: ${tmpl.name}`,
                        description: `The "Add to cart" button text "${tmpl.buyButtonText}" may confuse customers since the unbranded accelerated checkout button also says "Buy it now".`,
                        entityId: tmpl.id,
                        entityType: 'template'
                    });
                }
            });
        }

        // No accelerated methods active
        if (this.getActiveAcceleratedMethods().length === 0) {
            issues.push({
                type: 'no_accelerated_methods',
                severity: 'info',
                title: 'No accelerated checkout methods active',
                description: 'Only the unbranded "Buy it now" button will display since no third-party accelerated checkout methods are activated.',
                entityId: null,
                entityType: null
            });
        }

        return issues;
    },

    // ---- Mutations ----

    // -- Theme operations --
    publishTheme(themeId) {
        this.themes.forEach(t => {
            if (t.role === 'main') t.role = 'unpublished';
        });
        const theme = this.getThemeById(themeId);
        if (theme) {
            theme.role = 'main';
            theme.lastUpdated = new Date().toISOString();
            this._addLog('theme_published', `Published ${theme.name} v${theme.version}`, { themeId });
        }
        this.notify();
    },

    updateThemeColors(themeId, colors) {
        const theme = this.getThemeById(themeId);
        if (theme) {
            Object.assign(theme.settings.colors, colors);
            theme.lastUpdated = new Date().toISOString();
            this._addLog('theme_color_changed', `Updated button colors on ${theme.name}`, { themeId });
        }
        this.notify();
    },

    updateThemeTypography(themeId, typography) {
        const theme = this.getThemeById(themeId);
        if (theme) {
            Object.assign(theme.settings.typography, typography);
            theme.lastUpdated = new Date().toISOString();
            this._addLog('font_changed', `Updated typography on ${theme.name}`, { themeId });
        }
        this.notify();
    },

    // -- Template operations --
    toggleTemplateCheckout(templateId, enabled) {
        const tmpl = this.getTemplateById(templateId);
        if (tmpl) {
            tmpl.showAcceleratedCheckout = enabled;
            const action = enabled ? 'checkout_buttons_enabled' : 'checkout_buttons_disabled';
            this._addLog(action, `${enabled ? 'Enabled' : 'Disabled'} accelerated checkout on ${tmpl.name}`, { themeId: tmpl.themeId, templateId });
        }
        this.notify();
    },

    updateTemplateBuyButtonText(templateId, text) {
        const tmpl = this.getTemplateById(templateId);
        if (tmpl) {
            tmpl.buyButtonText = text;
        }
        this.notify();
    },

    toggleTemplateQuantitySelector(templateId, enabled) {
        const tmpl = this.getTemplateById(templateId);
        if (tmpl) {
            tmpl.showQuantitySelector = enabled;
        }
        this.notify();
    },

    createAlternateTemplate(themeId, name) {
        const id = 'tmpl_' + this._nextTemplateId++;
        const handle = 'product.' + name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        const tmpl = {
            id,
            themeId,
            name,
            handle,
            isDefault: false,
            isAlternate: true,
            showAcceleratedCheckout: false,
            showQuantitySelector: true,
            buyButtonText: 'Add to cart',
            createdAt: new Date().toISOString()
        };
        this.templates.push(tmpl);
        this._addLog('template_created', `Created alternate template: ${name}`, { themeId, templateId: id });
        this.notify();
        return id;
    },

    deleteTemplate(templateId) {
        const tmpl = this.getTemplateById(templateId);
        if (!tmpl || tmpl.isDefault) return;

        // Reset products using this template to default
        const defaultTmpl = this.templates.find(t => t.themeId === tmpl.themeId && t.isDefault);
        if (defaultTmpl) {
            this.products.forEach(p => {
                if (p.templateId === templateId) {
                    p.templateId = defaultTmpl.id;
                }
            });
        }
        this.templates = this.templates.filter(t => t.id !== templateId);
        this._addLog('template_deleted', `Deleted template: ${tmpl.name}`, { themeId: tmpl.themeId, templateId });
        this.notify();
    },

    // -- Section operations --
    toggleSectionCheckout(sectionId, enabled) {
        const section = this.getSectionById(sectionId);
        if (section) {
            section.showAcceleratedCheckout = enabled;
            this._addLog('section_checkout_toggled',
                `${enabled ? 'Enabled' : 'Disabled'} accelerated checkout on section`, { themeId: section.themeId, sectionId });
        }
        this.notify();
    },

    addFeaturedProductSection(themeId, pageId, productId) {
        const id = 'sec_' + this._nextSectionId++;
        const existingSections = this.getSectionsForPage(pageId);
        const section = {
            id,
            themeId,
            pageId,
            type: 'featured_product',
            label: 'Featured product',
            productId: productId || null,
            showAcceleratedCheckout: false,
            position: existingSections.length,
            visible: true
        };
        this.themeSections.push(section);
        this._addLog('featured_product_section_added', 'Added Featured product section', { themeId, sectionId: id });
        this.notify();
        return id;
    },

    updateSectionProduct(sectionId, productId) {
        const section = this.getSectionById(sectionId);
        if (section) {
            section.productId = productId;
        }
        this.notify();
    },

    removeSection(sectionId) {
        this.themeSections = this.themeSections.filter(s => s.id !== sectionId);
        this.notify();
    },

    // -- Payment method operations --
    togglePaymentMethod(methodId, active) {
        const method = this.getPaymentMethodById(methodId);
        if (method) {
            method.isActive = active;
            method.activatedAt = active ? new Date().toISOString() : method.activatedAt;
            const action = active ? 'payment_method_activated' : 'payment_method_deactivated';
            this._addLog(action, `${active ? 'Activated' : 'Deactivated'} ${method.name}`, { paymentMethodId: methodId });
        }
        this.notify();
    },

    // -- Shop Promise --
    toggleShopPromise(active) {
        this.shopPromise.isActive = active;
        this.shopPromise.prioritizesShopPay = active;
        const action = active ? 'shop_promise_enabled' : 'shop_promise_disabled';
        this._addLog(action, `${active ? 'Enabled' : 'Disabled'} Shop Promise`);
        this.notify();
    },

    updateShopPromise(updates) {
        Object.assign(this.shopPromise, updates);
        this.notify();
    },

    // -- Product operations --
    assignProductTemplate(productId, templateId) {
        const product = this.getProductById(productId);
        if (product) {
            product.templateId = templateId;
            product.updatedAt = new Date().toISOString();
            const tmpl = this.getTemplateById(templateId);
            this._addLog('product_template_changed', `Assigned ${product.title} to ${tmpl ? tmpl.name : 'unknown'} template`, { productId, templateId });
        }
        this.notify();
    },

    updateProductStatus(productId, status) {
        const product = this.getProductById(productId);
        if (product) {
            product.status = status;
            product.updatedAt = new Date().toISOString();
        }
        this.notify();
    },

    // -- Cart attribute operations --
    toggleCartAttribute(attrId, active) {
        const attr = this.cartAttributes.find(a => a.id === attrId);
        if (attr) {
            attr.isActive = active;
        }
        this.notify();
    },

    // -- App operations --
    toggleApp(appId, active) {
        const app = this.getAppById(appId);
        if (app) {
            app.isActive = active;
        }
        this.notify();
    }
};

/* ============================================================
   Shopify Dynamic Checkout – App Controller
   ============================================================ */

const App = {

    init() {
        AppState.init();
        this._setupSSE();
        AppState.subscribe(() => this.render());
        this._parseRoute();
        this.render();

        window.addEventListener('hashchange', () => {
            this._parseRoute();
            this.render();
        });

        document.addEventListener('click', (e) => this._handleClick(e));
        document.addEventListener('input', (e) => this._handleInput(e));
        document.addEventListener('change', (e) => this._handleChange(e));
        document.addEventListener('keydown', (e) => this._handleKeydown(e));
    },

    _setupSSE() {
        const es = new EventSource('/api/events');
        es.onmessage = (e) => {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
                window.location.hash = '#/themes';
            }
        };
    },

    _parseRoute() {
        const hash = window.location.hash || '#/themes';
        const parts = hash.replace('#/', '').split('/');

        // Close any open dropdowns
        this._closeAllDropdowns();

        if (parts[0] === 'themes' && parts.length === 1) {
            AppState.currentView = 'themes';
        } else if (parts[0] === 'themes' && parts[1]) {
            AppState.currentView = 'theme-detail';
            AppState.currentThemeId = parts[1];
        } else if (parts[0] === 'theme-editor') {
            AppState.currentView = 'theme-editor';
            if (parts[1]) {
                AppState.editingThemeId = parts[1];
            }
        } else if (parts[0] === 'theme-settings' && parts[1] === 'colors') {
            AppState.currentView = 'theme-settings-colors';
        } else if (parts[0] === 'theme-settings' && parts[1] === 'typography') {
            AppState.currentView = 'theme-settings-typography';
        } else if (parts[0] === 'products' && parts.length === 1) {
            AppState.currentView = 'products';
        } else if (parts[0] === 'products' && parts[1]) {
            AppState.currentView = 'product-detail';
            AppState.currentProductId = parts[1];
        } else if (parts[0] === 'payments') {
            AppState.currentView = 'payments';
        } else if (parts[0] === 'compatibility') {
            AppState.currentView = 'compatibility';
        } else if (parts[0] === 'activity') {
            AppState.currentView = 'activity';
        }
    },

    render() {
        const sidebar = document.getElementById('sidebarNav');
        const content = document.getElementById('contentWrapper');

        if (sidebar) sidebar.innerHTML = Views.renderSidebar();
        if (content) content.innerHTML = Views.renderContent();

        // Update store name in header
        const storeNameEl = document.getElementById('storeName');
        if (storeNameEl) storeNameEl.textContent = AppState.currentUser.storeName;

        // Update compatibility badge
        const issues = AppState.getCompatibilityIssues();
        const warnings = issues.filter(i => i.severity === 'warning').length;
        const compatBadge = document.getElementById('compatBadge');
        if (compatBadge) {
            compatBadge.textContent = warnings > 0 ? warnings : '';
            compatBadge.style.display = warnings > 0 ? 'inline-flex' : 'none';
        }

        // Show toast if pending
        this._showToast();
    },

    // ---- Toast system ----
    _showToast() {
        const container = document.getElementById('toastContainer');
        if (!container) return;

        if (AppState.toastMessage) {
            container.innerHTML = Components.toast(AppState.toastMessage, AppState.toastType);
            container.style.display = 'block';
            const msg = AppState.toastMessage;
            AppState.toastMessage = null;
            setTimeout(() => {
                if (container.querySelector('.toast-message') &&
                    container.querySelector('.toast-message').textContent === msg) {
                    container.style.display = 'none';
                    container.innerHTML = '';
                }
            }, 4000);
        }
    },

    _toast(message, type) {
        AppState.toastMessage = message;
        AppState.toastType = type || 'success';
        this._showToast();
    },

    // ---- Event handlers ----
    _handleClick(e) {
        const target = e.target;

        // Route navigation
        const routeEl = target.closest('[data-route]');
        if (routeEl) {
            e.preventDefault();
            window.location.hash = routeEl.dataset.route;
            return;
        }

        // Action dispatch
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            e.preventDefault();
            this._handleAction(actionEl.dataset.action, actionEl);
            return;
        }

        // Product row click
        const productRow = target.closest('.product-row');
        if (productRow && productRow.dataset.route) {
            window.location.hash = productRow.dataset.route;
            return;
        }

        // Close dropdowns when clicking outside
        if (!target.closest('[data-dropdown]')) {
            this._closeAllDropdowns();
        }
    },

    _handleAction(action, el) {
        switch (action) {
            // ---- Toggle switch ----
            case 'toggle': {
                const currentlyActive = el.classList.contains('active');
                const newValue = !currentlyActive;

                // Template checkout toggle
                if (el.dataset.templateId) {
                    if (el.dataset.field === 'quantity') {
                        AppState.toggleTemplateQuantitySelector(el.dataset.templateId, newValue);
                    } else {
                        AppState.toggleTemplateCheckout(el.dataset.templateId, newValue);
                    }
                    this._toast(newValue ? 'Accelerated checkout enabled' : 'Accelerated checkout disabled');
                }
                // Payment method toggle
                else if (el.dataset.paymentId) {
                    AppState.togglePaymentMethod(el.dataset.paymentId, newValue);
                    const method = AppState.getPaymentMethodById(el.dataset.paymentId);
                    this._toast(`${method ? method.name : 'Payment method'} ${newValue ? 'activated' : 'deactivated'}`);
                }
                // Section checkout toggle
                else if (el.dataset.sectionId) {
                    AppState.toggleSectionCheckout(el.dataset.sectionId, newValue);
                    this._toast(newValue ? 'Checkout buttons enabled for section' : 'Checkout buttons disabled for section');
                }
                // Shop Promise toggle
                else if (el.id === 'shop-promise-toggle') {
                    AppState.toggleShopPromise(newValue);
                    this._toast(newValue ? 'Shop Promise enabled' : 'Shop Promise disabled');
                }
                // App toggle
                else if (el.dataset.appId) {
                    AppState.toggleApp(el.dataset.appId, newValue);
                }
                // Cart attribute toggle
                else if (el.dataset.attrId) {
                    AppState.toggleCartAttribute(el.dataset.attrId, newValue);
                }
                break;
            }

            // ---- Dropdown ----
            case 'dropdown-toggle': {
                const dropdownId = el.dataset.dropdownId;
                const dropdown = document.getElementById(dropdownId);
                if (!dropdown) break;
                const menu = dropdown.querySelector('.dropdown-menu');
                if (!menu) break;
                const isOpen = menu.style.display !== 'none';
                this._closeAllDropdowns();
                if (!isOpen) {
                    menu.style.display = 'block';
                }
                break;
            }

            case 'dropdown-select': {
                const dropdownId = el.dataset.dropdownId;
                const value = el.dataset.value;
                this._closeAllDropdowns();
                this._handleDropdownSelect(dropdownId, value);
                break;
            }

            // ---- Theme actions ----
            case 'edit-theme': {
                AppState.editingThemeId = el.dataset.themeId;
                window.location.hash = '#/theme-editor';
                break;
            }

            case 'view-theme': {
                AppState.currentThemeId = el.dataset.themeId;
                window.location.hash = '#/themes/' + el.dataset.themeId;
                break;
            }

            case 'publish-theme': {
                const theme = AppState.getThemeById(el.dataset.themeId);
                if (theme) {
                    AppState.modalOpen = true;
                    AppState.modalType = 'confirm-publish';
                    AppState.modalData = { themeId: el.dataset.themeId };
                    const container = document.getElementById('modalContainer');
                    if (container) {
                        container.innerHTML = Components.confirmDialog(
                            'Publish theme',
                            `Are you sure you want to publish "${theme.name}"? It will replace your current live theme.`,
                            'Publish', 'confirm-publish-theme', false
                        );
                    }
                }
                break;
            }

            case 'confirm-publish-theme': {
                if (AppState.modalData && AppState.modalData.themeId) {
                    AppState.publishTheme(AppState.modalData.themeId);
                    this._closeModal();
                    this._toast('Theme published successfully');
                }
                break;
            }

            // ---- Template actions ----
            case 'create-template': {
                AppState.modalOpen = true;
                AppState.modalType = 'create-template';
                AppState.modalData = { themeId: el.dataset.themeId };
                const container = document.getElementById('modalContainer');
                if (container) {
                    container.innerHTML = Components.modal(
                        'Create alternate template',
                        `<div class="field-group">
                            <label class="field-label">Template name</label>
                            <input type="text" class="text-input" id="new-template-name" placeholder="e.g. Product - Express checkout" />
                        </div>
                        <p class="help-text">Create an alternate product template to show or hide accelerated checkout buttons for specific products.</p>`,
                        `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                         <button class="btn btn-primary" data-action="save-new-template">Create template</button>`
                    );
                    setTimeout(() => {
                        const input = document.getElementById('new-template-name');
                        if (input) input.focus();
                    }, 100);
                }
                break;
            }

            case 'save-new-template': {
                const nameInput = document.getElementById('new-template-name');
                if (!nameInput || !nameInput.value.trim()) {
                    this._toast('Please enter a template name', 'error');
                    break;
                }
                const themeId = AppState.modalData ? AppState.modalData.themeId : null;
                if (themeId) {
                    AppState.createAlternateTemplate(themeId, nameInput.value.trim());
                    this._closeModal();
                    this._toast('Template created');
                }
                break;
            }

            case 'delete-template': {
                const tmpl = AppState.getTemplateById(el.dataset.templateId);
                if (tmpl) {
                    AppState.modalOpen = true;
                    AppState.modalData = { templateId: el.dataset.templateId };
                    const container = document.getElementById('modalContainer');
                    if (container) {
                        container.innerHTML = Components.confirmDialog(
                            'Delete template',
                            `Delete "${tmpl.name}"? Products using this template will be reassigned to the default template.`,
                            'Delete', 'confirm-delete-template', true
                        );
                    }
                }
                break;
            }

            case 'confirm-delete-template': {
                if (AppState.modalData && AppState.modalData.templateId) {
                    AppState.deleteTemplate(AppState.modalData.templateId);
                    this._closeModal();
                    this._toast('Template deleted');
                }
                break;
            }

            // ---- Editor actions ----
            case 'editor-select-page': {
                AppState.editorPage = el.dataset.pageId;
                AppState.editorSection = null;
                AppState.currentTemplateId = null;
                this.render();
                break;
            }

            case 'editor-select-template': {
                AppState.currentTemplateId = el.dataset.templateId;
                this.render();
                break;
            }

            case 'toggle-editor-section': {
                const sectionId = el.dataset.section;
                AppState.editorSection = AppState.editorSection === sectionId ? null : sectionId;
                this.render();
                break;
            }

            case 'toggle-editor-block': {
                // Toggle visibility of block content
                const content = el.nextElementSibling || el.parentElement.querySelector('.editor-block-content');
                if (content) {
                    content.classList.toggle('open');
                }
                break;
            }

            case 'add-section': {
                const themeId = el.dataset.themeId;
                const pageId = el.dataset.pageId;
                AppState.addFeaturedProductSection(themeId, pageId, null);
                this._toast('Featured product section added');
                break;
            }

            case 'remove-section': {
                AppState.removeSection(el.dataset.sectionId);
                this._toast('Section removed');
                break;
            }

            // ---- Color actions ----
            case 'save-colors': {
                const themeId = el.dataset.themeId;
                const colors = {};
                const fields = {
                    'color-accent-bg': 'accentButtonBg',
                    'color-accent-text': 'accentButtonText',
                    'color-primary-bg': 'primaryBg',
                    'color-primary-text': 'primaryText',
                    'color-secondary-bg': 'secondaryBg',
                    'color-secondary-text': 'secondaryText',
                    'color-accent': 'accentColor'
                };
                for (const [inputId, field] of Object.entries(fields)) {
                    const input = document.getElementById(inputId);
                    if (input) colors[field] = input.value;
                }
                AppState.updateThemeColors(themeId, colors);
                this._toast('Colors saved');
                break;
            }

            case 'color-text-change': {
                // Live preview handled on input
                break;
            }

            // ---- Typography actions ----
            case 'save-typography': {
                const themeId = el.dataset.themeId;
                const typography = {};
                const fontFields = { 'font-heading': 'headingFont', 'font-body': 'bodyFont', 'font-button': 'buttonFont' };
                for (const [dropdownId, field] of Object.entries(fontFields)) {
                    const dropdown = document.getElementById(dropdownId);
                    if (dropdown) {
                        const valueEl = dropdown.querySelector('.dropdown-value');
                        if (valueEl) typography[field] = valueEl.textContent;
                    }
                }
                const headingScale = document.getElementById('heading-scale');
                const bodyScale = document.getElementById('body-scale');
                if (headingScale) typography.headingScale = parseInt(headingScale.value) || 100;
                if (bodyScale) typography.bodyScale = parseInt(bodyScale.value) || 100;

                AppState.updateThemeTypography(themeId, typography);
                this._toast('Typography saved');
                break;
            }

            // ---- Product actions ----
            case 'update-buy-button-text': {
                AppState.updateTemplateBuyButtonText(el.dataset.templateId, el.value);
                break;
            }

            // ---- Search ----
            case 'search': break; // handled in _handleInput
            case 'clear-search': {
                AppState.searchQuery = '';
                AppState.currentPage = 1;
                AppState.notify();
                break;
            }

            // ---- Pagination ----
            case 'prev-page': {
                if (AppState.currentPage > 1) {
                    AppState.currentPage--;
                    AppState.notify();
                }
                break;
            }
            case 'next-page': {
                const { totalPages } = AppState.getPagedProducts();
                if (AppState.currentPage < totalPages) {
                    AppState.currentPage++;
                    AppState.notify();
                }
                break;
            }
            case 'go-to-page': {
                AppState.currentPage = parseInt(el.dataset.page) || 1;
                AppState.notify();
                break;
            }

            // ---- Modal ----
            case 'close-modal':
            case 'close-modal-overlay': {
                if (action === 'close-modal-overlay' && !el.classList.contains('modal-overlay')) break;
                this._closeModal();
                break;
            }

            // ---- Toast ----
            case 'close-toast': {
                const container = document.getElementById('toastContainer');
                if (container) {
                    container.style.display = 'none';
                    container.innerHTML = '';
                }
                break;
            }
        }
    },

    _handleDropdownSelect(dropdownId, value) {
        // Product status filter
        if (dropdownId === 'product-status-filter') {
            AppState.productFilter = value;
            AppState.currentPage = 1;
            AppState.notify();
        }
        // Product sort
        else if (dropdownId === 'product-sort') {
            AppState.productSort = value;
            AppState.currentPage = 1;
            AppState.notify();
        }
        // Editor theme selector
        else if (dropdownId === 'editor-theme-select') {
            AppState.editingThemeId = value;
            AppState.editorPage = null;
            AppState.editorSection = null;
            AppState.currentTemplateId = null;
            AppState.notify();
        }
        // Product template assignment
        else if (dropdownId.startsWith('product-template-')) {
            const productId = dropdownId.replace('product-template-', '');
            AppState.assignProductTemplate(productId, value);
            this._toast('Template assigned');
        }
        // Product status change
        else if (dropdownId.startsWith('product-status-')) {
            const productId = dropdownId.replace('product-status-', '');
            AppState.updateProductStatus(productId, value);
            this._toast('Product status updated');
        }
        // Section product selection
        else if (dropdownId.startsWith('section-product-')) {
            const sectionId = dropdownId.replace('section-product-', '');
            AppState.updateSectionProduct(sectionId, value);
        }
        // Font dropdown selections
        else if (dropdownId.startsWith('font-')) {
            // Just update the display, actual save happens on Save button click
            const dropdown = document.getElementById(dropdownId);
            if (dropdown) {
                const valueEl = dropdown.querySelector('.dropdown-value');
                if (valueEl) valueEl.textContent = value;
            }
        }
    },

    _handleInput(e) {
        const el = e.target;

        // Search
        if (el.classList.contains('search-input')) {
            AppState.searchQuery = el.value;
            AppState.currentPage = 1;
            // Debounce render
            clearTimeout(this._searchTimeout);
            this._searchTimeout = setTimeout(() => AppState.notify(), 200);
        }

        // Color text input
        if (el.dataset.action === 'color-text-change') {
            const val = el.value;
            if (/^#[0-9A-Fa-f]{6}$/.test(val)) {
                const swatch = el.parentElement.querySelector('.color-swatch-preview');
                if (swatch) swatch.style.background = val;
            }
        }

        // Buy button text
        if (el.dataset.action === 'update-buy-button-text') {
            AppState.updateTemplateBuyButtonText(el.dataset.templateId, el.value);
        }
    },

    _handleChange(e) {
        // No native selects used
    },

    _handleKeydown(e) {
        if (e.key === 'Escape') {
            this._closeAllDropdowns();
            this._closeModal();
        }

        // Toggle switches with Enter/Space
        if ((e.key === 'Enter' || e.key === ' ') && e.target.classList.contains('toggle-switch')) {
            e.preventDefault();
            this._handleAction('toggle', e.target);
        }

        // Submit on Enter in modal
        if (e.key === 'Enter' && e.target.id === 'new-template-name') {
            e.preventDefault();
            const saveBtn = document.querySelector('[data-action="save-new-template"]');
            if (saveBtn) saveBtn.click();
        }
    },

    _closeAllDropdowns() {
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
            menu.style.display = 'none';
        });
    },

    _closeModal() {
        AppState.modalOpen = false;
        AppState.modalType = null;
        AppState.modalData = null;
        const container = document.getElementById('modalContainer');
        if (container) container.innerHTML = '';
    },

    _searchTimeout: null
};

// Boot
document.addEventListener('DOMContentLoaded', () => App.init());

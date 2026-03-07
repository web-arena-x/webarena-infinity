// Figma Text & Typography - App Controller
const App = {
    _sseConnection: null,
    _openDropdownId: null,

    init() {
        AppState.init();
        AppState.subscribe(() => this.render());

        this.parseRoute();
        this.render();
        AppState._pushStateToServer();

        document.addEventListener('click', (e) => this.handleClick(e));
        document.addEventListener('input', (e) => this.handleInput(e));
        document.addEventListener('change', (e) => this.handleChange(e));
        document.addEventListener('keydown', (e) => this.handleKeydown(e));
        document.addEventListener('contextmenu', (e) => this.handleContextMenu(e));

        window.addEventListener('hashchange', () => {
            this.parseRoute();
            this.render();
        });

        this._initSSE();
    },

    parseRoute() {
        const hash = window.location.hash || '#/layers';
        const section = hash.replace('#/', '') || 'layers';
        const valid = ['layers', 'properties', 'styles', 'fonts', 'settings'];
        AppState.currentSection = valid.includes(section) ? section : 'layers';
    },

    navigate(section) {
        window.location.hash = '#/' + section;
    },

    render() {
        const sidebar = document.getElementById('sidebarNav');
        if (sidebar) sidebar.innerHTML = Views.renderSidebar();

        const content = document.getElementById('mainContent');
        if (content) content.innerHTML = Views.renderContent();

        const modalContainer = document.getElementById('modalContainer');
        if (modalContainer) modalContainer.innerHTML = Views.renderModal();

        const toastEl = document.getElementById('toastContainer');
        if (toastEl) toastEl.innerHTML = Components.toast(AppState.toastMessage);

        if (AppState.activeModal) {
            setTimeout(() => {
                const input = document.querySelector('.modal-input, .modal-textarea');
                if (input) input.focus();
            }, 50);
        }
    },

    // ============================================================
    // Event Handlers
    // ============================================================

    handleClick(e) {
        const target = e.target;

        // Close dropdowns on outside click
        if (this._openDropdownId && !target.closest('.custom-dropdown')) {
            this._closeAllDropdowns();
        }

        // ---- Data-action dispatch ----
        const actionEl = target.closest('[data-action]');
        if (actionEl) {
            const action = actionEl.dataset.action;
            e.preventDefault();
            e.stopPropagation();

            switch (action) {
                // Navigation
                case 'navigate':
                    this.navigate(actionEl.dataset.section);
                    break;

                // Layer actions
                case 'selectLayer':
                    AppState.selectLayer(actionEl.dataset.layerId);
                    this.render();
                    break;
                case 'createLayer':
                    AppState.activeModal = 'createLayer';
                    this.render();
                    break;
                case 'confirmCreateLayer': {
                    const textarea = document.getElementById('modal-layer-content');
                    const content = textarea ? textarea.value : '';
                    AppState.createTextLayer(content);
                    AppState.activeModal = null;
                    AppState.showToast('Text layer created.');
                    break;
                }
                case 'deleteLayerPrompt':
                    AppState.activeModal = 'deleteLayer';
                    this.render();
                    break;
                case 'confirmDeleteLayer':
                    if (AppState.selectedLayerId) {
                        AppState.deleteTextLayer(AppState.selectedLayerId);
                        AppState.activeModal = null;
                        AppState.showToast('Layer deleted.');
                    }
                    break;
                case 'duplicateLayer':
                    if (AppState.selectedLayerId) {
                        AppState.duplicateTextLayer(AppState.selectedLayerId);
                        AppState.showToast('Layer duplicated.');
                    }
                    break;
                case 'renameLayerPrompt':
                    AppState.activeModal = 'renameLayer';
                    this.render();
                    break;
                case 'confirmRenameLayer': {
                    const nameInput = document.getElementById('modal-layer-name');
                    if (nameInput && AppState.selectedLayerId) {
                        AppState.renameLayer(AppState.selectedLayerId, nameInput.value);
                        AppState.activeModal = null;
                        AppState.showToast('Layer renamed.');
                    }
                    break;
                }
                case 'toggleVisibility':
                    AppState.toggleLayerVisibility(actionEl.dataset.layerId);
                    break;
                case 'toggleLock':
                    AppState.toggleLayerLock(actionEl.dataset.layerId);
                    break;

                // Style actions
                case 'openCreateStyleModal':
                    AppState.modalData = actionEl.dataset.layerId ? { layerId: actionEl.dataset.layerId } : null;
                    AppState.activeModal = 'createStyle';
                    this.render();
                    break;
                case 'confirmCreateStyle': {
                    const name = document.getElementById('modal-style-name');
                    const desc = document.getElementById('modal-style-desc');
                    const layerId = AppState.modalData ? AppState.modalData.layerId : null;
                    const style = AppState.createTextStyle(name ? name.value : '', layerId);
                    if (desc && desc.value) {
                        AppState.updateTextStyle(style.id, { description: desc.value });
                    }
                    AppState.activeModal = null;
                    AppState.modalData = null;
                    AppState.showToast('Text style created.');
                    break;
                }
                case 'editStyleModal':
                    AppState.modalData = { styleId: actionEl.dataset.styleId };
                    AppState.activeModal = 'editStyle';
                    this.render();
                    break;
                case 'confirmEditStyle': {
                    if (AppState.modalData && AppState.modalData.styleId) {
                        const updates = {};
                        const nameEl = document.getElementById('modal-edit-style-name');
                        const descEl = document.getElementById('modal-edit-style-desc');
                        const sizeEl = document.getElementById('modal-edit-style-size');

                        if (nameEl) updates.name = nameEl.value;
                        if (descEl) updates.description = descEl.value;
                        if (sizeEl) updates.fontSize = parseFloat(sizeEl.value) || 16;

                        const fontDd = document.getElementById('dd-edit-style-font');
                        if (fontDd) updates.fontFamily = fontDd.dataset.value;

                        const weightDd = document.getElementById('dd-edit-style-weight');
                        if (weightDd) updates.fontStyle = weightDd.dataset.value;

                        const caseDd = document.getElementById('dd-edit-style-case');
                        if (caseDd) updates.letterCase = caseDd.dataset.value;

                        const decoDd = document.getElementById('dd-edit-style-decoration');
                        if (decoDd) updates.textDecoration = decoDd.dataset.value;

                        AppState.updateTextStyle(AppState.modalData.styleId, updates);
                        AppState.activeModal = null;
                        AppState.modalData = null;
                        AppState.showToast('Style updated. All layers using this style have been updated.');
                    }
                    break;
                }
                case 'deleteStyle':
                    AppState.modalData = { styleId: actionEl.dataset.styleId };
                    AppState.activeModal = 'deleteStyle';
                    this.render();
                    break;
                case 'confirmDeleteStyle':
                    if (AppState.modalData && AppState.modalData.styleId) {
                        AppState.deleteTextStyle(AppState.modalData.styleId);
                        AppState.activeModal = null;
                        AppState.modalData = null;
                        AppState.showToast('Style deleted.');
                    }
                    break;
                case 'detachStyle':
                    AppState.detachTextStyle(actionEl.dataset.layerId);
                    AppState.showToast('Style detached.');
                    break;
                case 'openApplyStyleModal':
                    AppState.modalData = { layerId: actionEl.dataset.layerId };
                    AppState.activeModal = 'applyStyle';
                    this.render();
                    break;
                case 'confirmApplyStyle':
                    AppState.applyTextStyle(actionEl.dataset.layerId, actionEl.dataset.styleId);
                    AppState.activeModal = null;
                    AppState.modalData = null;
                    AppState.showToast('Style applied.');
                    break;

                // Font actions
                case 'setFontFilter':
                    AppState.fontFilter = actionEl.dataset.filter;
                    this.render();
                    break;
                case 'applyFont':
                    if (AppState.selectedLayerId) {
                        AppState.updateLayerFont(AppState.selectedLayerId, actionEl.dataset.fontName);
                        AppState.showToast(`Font "${actionEl.dataset.fontName}" applied.`);
                    }
                    break;
                case 'openFontPicker':
                    AppState.modalData = { layerId: actionEl.dataset.layerId };
                    AppState.fontSearchQuery = '';
                    AppState.activeModal = 'fontPicker';
                    this.render();
                    break;
                case 'selectFontFromPicker':
                    if (AppState.modalData && AppState.modalData.layerId) {
                        AppState.updateLayerFont(AppState.modalData.layerId, actionEl.dataset.fontName);
                        AppState.activeModal = null;
                        AppState.modalData = null;
                        AppState.showToast(`Font changed to "${actionEl.dataset.fontName}".`);
                    }
                    break;

                // Links
                case 'openAddLinkModal':
                    AppState.modalData = { layerId: actionEl.dataset.layerId };
                    AppState.activeModal = 'addLink';
                    this.render();
                    break;
                case 'confirmAddLink': {
                    const start = parseInt(document.getElementById('modal-link-start').value) || 0;
                    const end = parseInt(document.getElementById('modal-link-end').value) || 0;
                    const url = document.getElementById('modal-link-url').value.trim();
                    if (url && end > start && AppState.modalData) {
                        AppState.addLink(AppState.modalData.layerId, start, end, url);
                        AppState.activeModal = null;
                        AppState.modalData = null;
                        AppState.showToast('Link added.');
                    }
                    break;
                }
                case 'editLink': {
                    const layer = AppState.textLayers.find(l => l.id === actionEl.dataset.layerId);
                    const link = layer ? layer.links.find(l => l.id === actionEl.dataset.linkId) : null;
                    if (link) {
                        AppState.modalData = { layerId: actionEl.dataset.layerId, linkId: actionEl.dataset.linkId, url: link.url };
                        AppState.activeModal = 'editLink';
                        this.render();
                    }
                    break;
                }
                case 'confirmEditLink': {
                    const url = document.getElementById('modal-edit-link-url').value.trim();
                    if (url && AppState.modalData) {
                        AppState.updateLink(AppState.modalData.layerId, AppState.modalData.linkId, url);
                        AppState.activeModal = null;
                        AppState.modalData = null;
                        AppState.showToast('Link updated.');
                    }
                    break;
                }
                case 'removeLink':
                    AppState.removeLink(actionEl.dataset.layerId, actionEl.dataset.linkId);
                    AppState.showToast('Link removed.');
                    break;

                // OpenType
                case 'toggleOpenType':
                    AppState.toggleLayerOpenTypeFeature(actionEl.dataset.layerId, actionEl.dataset.feature);
                    break;
                case 'toggleOtCategory':
                    AppState.expandedOpenTypeCategory =
                        AppState.expandedOpenTypeCategory === actionEl.dataset.category ? null : actionEl.dataset.category;
                    this.render();
                    break;

                // Tabs
                case 'switchTab':
                    AppState.activeTab = actionEl.dataset.tab;
                    this.render();
                    break;

                // Modal
                case 'closeModal':
                    AppState.activeModal = null;
                    AppState.modalData = null;
                    this.render();
                    break;
            }
            return;
        }

        // ---- Dropdown trigger ----
        const dropdownTrigger = target.closest('.dropdown-trigger');
        if (dropdownTrigger) {
            const ddId = dropdownTrigger.dataset.dropdownId;
            this._toggleDropdown(ddId);
            return;
        }

        // ---- Dropdown item selection ----
        const dropdownItem = target.closest('.dropdown-item');
        if (dropdownItem) {
            const ddId = dropdownItem.dataset.dropdownId;
            const value = dropdownItem.dataset.value;
            this._handleDropdownSelect(ddId, value);
            return;
        }

        // ---- Toggle switch ----
        const toggleSwitch = target.closest('.toggle-switch');
        if (toggleSwitch && !toggleSwitch.dataset.action) {
            const toggleId = toggleSwitch.dataset.toggleId;
            if (toggleId) this._handleToggle(toggleId);
            return;
        }

        // ---- Button group item ----
        const groupItem = target.closest('.btn-group-item');
        if (groupItem) {
            const groupId = groupItem.dataset.groupId;
            const value = groupItem.dataset.value;
            this._handleButtonGroup(groupId, value);
            return;
        }

        // ---- Font selector click ----
        const fontSelector = target.closest('.font-selector');
        if (fontSelector) {
            AppState.modalData = { layerId: fontSelector.dataset.layerId };
            AppState.fontSearchQuery = '';
            AppState.activeModal = 'fontPicker';
            this.render();
            return;
        }

        // ---- Modal overlay click ----
        if (target.classList.contains('modal-overlay')) {
            AppState.activeModal = null;
            AppState.modalData = null;
            this.render();
            return;
        }

        // ---- Layer double-click for rename ----
        const layerName = target.closest('.layer-name');
        if (layerName && target.closest('.layer-row.selected')) {
            AppState.activeModal = 'renameLayer';
            this.render();
            return;
        }
    },

    handleInput(e) {
        const id = e.target.id;
        const val = e.target.value;
        const layerId = AppState.selectedLayerId;

        // Search inputs
        if (id === 'layer-search') {
            AppState.searchQuery = val;
            this.render();
            return;
        }
        if (id === 'font-search' || id === 'font-picker-search') {
            AppState.fontSearchQuery = val;
            this.render();
            return;
        }

        if (!layerId) return;

        // Number inputs for properties
        if (id === 'input-font-size') {
            const size = parseFloat(val);
            if (size && size > 0) AppState.updateLayerFontSize(layerId, size);
        }
        if (id === 'input-line-height') {
            const layer = AppState.getSelectedLayer();
            if (layer) AppState.updateLayerLineHeight(layerId, val === '' ? 'auto' : val);
        }
        if (id === 'input-letter-spacing') {
            AppState.updateLayerLetterSpacing(layerId, val);
        }
        if (id === 'input-para-spacing') {
            AppState.updateLayerParagraphSpacing(layerId, val);
        }
        if (id === 'input-para-indent') {
            AppState.updateLayerParagraphIndent(layerId, val);
        }
        if (id === 'input-list-spacing') {
            AppState.updateLayerListSpacing(layerId, val);
        }
        if (id === 'input-max-lines') {
            const layer = AppState.getSelectedLayer();
            if (layer) AppState.updateLayerTruncation(layerId, true, val);
        }
        if (id === 'input-width') {
            AppState.updateLayerDimensions(layerId, val, undefined);
        }
        if (id === 'input-height') {
            AppState.updateLayerDimensions(layerId, undefined, val);
        }

        // Settings inputs
        if (id === 'input-nudge') {
            AppState.updatePreference('nudgeAmount', parseFloat(val) || 1);
        }
        if (id === 'input-big-nudge') {
            AppState.updatePreference('bigNudgeAmount', parseFloat(val) || 10);
        }

        // Variable font slider inputs
        if (id.startsWith('slider-') && !id.endsWith('-value')) {
            const axisTag = id.replace('slider-', '');
            AppState.updateLayerVariableAxis(layerId, axisTag, val);
            const valInput = document.getElementById(id + '-value');
            if (valInput) valInput.value = val;
            // Update slider background
            const slider = e.target;
            const min = parseFloat(slider.min);
            const max = parseFloat(slider.max);
            const pct = ((parseFloat(val) - min) / (max - min)) * 100;
            slider.style.background = `linear-gradient(to right, var(--accent) ${pct}%, var(--bg-tertiary) ${pct}%)`;
        }
        if (id.endsWith('-value') && id.startsWith('slider-')) {
            const axisTag = id.replace('slider-', '').replace('-value', '');
            AppState.updateLayerVariableAxis(layerId, axisTag, val);
            const slider = document.getElementById('slider-' + axisTag);
            if (slider) {
                slider.value = val;
                const min = parseFloat(slider.min);
                const max = parseFloat(slider.max);
                const pct = ((parseFloat(val) - min) / (max - min)) * 100;
                slider.style.background = `linear-gradient(to right, var(--accent) ${pct}%, var(--bg-tertiary) ${pct}%)`;
            }
        }
    },

    handleChange(e) {
        // handled by input for most cases
    },

    handleKeydown(e) {
        // Enter in modal -> confirm
        if (e.key === 'Enter' && AppState.activeModal) {
            const confirmBtn = document.querySelector('.modal-footer .btn-primary, .modal-footer .btn-danger');
            if (confirmBtn && !confirmBtn.disabled) {
                confirmBtn.click();
            }
            return;
        }
        // Escape -> close modal/dropdown
        if (e.key === 'Escape') {
            if (AppState.activeModal) {
                AppState.activeModal = null;
                AppState.modalData = null;
                this.render();
            } else if (this._openDropdownId) {
                this._closeAllDropdowns();
            }
            return;
        }
        // Delete/Backspace with layer selected (not in input)
        if ((e.key === 'Delete' || e.key === 'Backspace') && AppState.selectedLayerId && !AppState.activeModal) {
            if (!['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
                AppState.activeModal = 'deleteLayer';
                this.render();
            }
        }
    },

    handleContextMenu(e) {
        const layerRow = e.target.closest('.layer-row');
        if (layerRow) {
            e.preventDefault();
            const layerId = layerRow.querySelector('[data-layer-id]')?.dataset?.layerId;
            if (layerId) {
                AppState.selectLayer(layerId);
                // Show context menu (simplified)
                this.render();
            }
        }
    },

    // ============================================================
    // Dropdown Helpers
    // ============================================================

    _toggleDropdown(ddId) {
        const dd = document.getElementById(ddId);
        if (!dd) return;
        const menu = dd.querySelector('.dropdown-menu');
        if (!menu) return;

        if (this._openDropdownId === ddId) {
            this._closeAllDropdowns();
        } else {
            this._closeAllDropdowns();
            menu.classList.add('open');
            dd.classList.add('open');
            this._openDropdownId = ddId;
        }
    },

    _closeAllDropdowns() {
        document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
        document.querySelectorAll('.custom-dropdown.open').forEach(d => d.classList.remove('open'));
        this._openDropdownId = null;
    },

    _handleDropdownSelect(ddId, value) {
        this._closeAllDropdowns();
        const layerId = AppState.selectedLayerId;

        // Update the dropdown's data-value
        const dd = document.getElementById(ddId);
        if (dd) dd.dataset.value = value;

        switch (ddId) {
            case 'dd-font-style':
                if (layerId) AppState.updateLayerProperty(layerId, 'fontStyle', value);
                break;
            case 'dd-line-height-unit':
                if (layerId) {
                    const layer = AppState.getSelectedLayer();
                    if (layer) AppState.updateLayerLineHeight(layerId, layer.lineHeight.value, value);
                }
                break;
            case 'dd-letter-spacing-unit':
                if (layerId) {
                    const layer = AppState.getSelectedLayer();
                    if (layer) AppState.updateLayerLetterSpacing(layerId, layer.letterSpacing.value, value);
                }
                break;
            case 'dd-letter-case':
                if (layerId) AppState.updateLayerLetterCase(layerId, value);
                break;
            case 'dd-list-style':
                if (layerId) AppState.updateLayerListStyle(layerId, value);
                break;

            // Settings dropdowns
            case 'dd-default-font':
                AppState.updatePreference('defaultFontFamily', value);
                break;
            case 'dd-default-style':
                AppState.updatePreference('defaultFontStyle', value);
                break;
            case 'dd-default-size':
                AppState.updatePreference('defaultFontSize', parseFloat(value));
                break;
            case 'dd-default-align':
                AppState.updatePreference('defaultHorizontalAlign', value);
                break;
            case 'dd-default-direction':
                AppState.updatePreference('defaultTextDirection', value);
                break;
            case 'dd-spelling-lang':
                AppState.updatePreference('spellingLanguage', value);
                break;

            // Edit style modal dropdowns
            case 'dd-edit-style-font':
            case 'dd-edit-style-weight':
            case 'dd-edit-style-case':
            case 'dd-edit-style-decoration':
                // Values stored in dropdown data-value, read on confirm
                break;
        }

        this.render();
    },

    // ============================================================
    // Toggle Helpers
    // ============================================================

    _handleToggle(toggleId) {
        const layerId = AppState.selectedLayerId;

        switch (toggleId) {
            case 'toggle-hanging-punct':
                if (layerId) AppState.toggleLayerHangingPunctuation(layerId);
                break;
            case 'toggle-hanging-list':
                if (layerId) AppState.toggleLayerHangingList(layerId);
                break;
            case 'toggle-truncation':
                if (layerId) {
                    const layer = AppState.getSelectedLayer();
                    if (layer) AppState.updateLayerTruncation(layerId, !layer.truncation.enabled, 3);
                }
                break;
            case 'toggle-vertical-trim':
                if (layerId) AppState.toggleLayerVerticalTrim(layerId);
                break;

            // Settings toggles
            case 'toggle-smart-quotes':
                AppState.updatePreference('smartQuotes', !AppState.preferences.smartQuotes);
                break;
            case 'toggle-smart-symbols':
                AppState.updatePreference('smartSymbols', !AppState.preferences.smartSymbols);
                break;
            case 'toggle-snap-grid':
                AppState.updatePreference('snapToGrid', !AppState.preferences.snapToGrid);
                break;
            case 'toggle-font-preview':
                AppState.updatePreference('showFontPreview', !AppState.preferences.showFontPreview);
                break;
        }
    },

    // ============================================================
    // Button Group Helpers
    // ============================================================

    _handleButtonGroup(groupId, value) {
        const layerId = AppState.selectedLayerId;

        switch (groupId) {
            case 'bg-h-align':
                if (layerId) AppState.updateLayerAlignment(layerId, value);
                break;
            case 'bg-v-align':
                if (layerId) AppState.updateLayerVerticalAlignment(layerId, value);
                break;
            case 'bg-resizing':
                if (layerId) AppState.updateLayerResizing(layerId, value);
                break;
            case 'bg-decoration':
                if (layerId) AppState.updateLayerDecoration(layerId, value);
                break;
            case 'bg-direction':
                if (layerId) AppState.updateLayerDirection(layerId, value);
                break;
        }

        this.render();
    },

    // ============================================================
    // SSE
    // ============================================================

    _initSSE() {
        this._sseConnection = new EventSource('/api/events');
        this._sseConnection.onmessage = (e) => {
            if (e.data === 'reset') {
                AppState.resetToSeedData();
                window.location.hash = '#/layers';
                this.render();
            }
        };
    }
};

document.addEventListener('DOMContentLoaded', () => App.init());

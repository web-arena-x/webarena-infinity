// ============================================================
// app.js — Hash-based router and event handler attachment
// ============================================================

const Router = {
    routes: {
        '/': () => Views.themes(),
        '/editor/:themeId': (params) => Views.editor(parseInt(params.themeId)),
        '/settings/:themeId': (params) => Views.themeSettings(parseInt(params.themeId))
    },

    navigate(path) {
        window.location.hash = '#' + path;
    },

    getCurrentPath() {
        return window.location.hash.slice(1) || '/';
    },

    parsePath(path) {
        const [pathPart, queryPart] = path.split('?');
        const segments = pathPart.split('/').filter(Boolean);

        // Parse query params
        const queryParams = {};
        if (queryPart) {
            queryPart.split('&').forEach(p => {
                const [k, v] = p.split('=');
                queryParams[decodeURIComponent(k)] = decodeURIComponent(v || '');
            });
        }

        return { segments, queryParams };
    },

    matchRoute(path) {
        const { segments, queryParams } = this.parsePath(path);
        AppState.queryParams = queryParams;

        for (const [pattern, handler] of Object.entries(this.routes)) {
            const patternSegments = pattern.split('/').filter(Boolean);

            if (patternSegments.length !== segments.length) continue;

            const params = {};
            let match = true;

            for (let i = 0; i < patternSegments.length; i++) {
                if (patternSegments[i].startsWith(':')) {
                    params[patternSegments[i].slice(1)] = segments[i];
                } else if (patternSegments[i] !== segments[i]) {
                    match = false;
                    break;
                }
            }

            if (match) {
                AppState.currentRoute = path;
                AppState.routeParams = params;
                return handler(params);
            }
        }

        // Default to themes list
        AppState.currentRoute = '/';
        return Views.themes();
    },

    render() {
        const path = this.getCurrentPath();
        const content = this.matchRoute(path);
        const wrapper = document.getElementById('contentWrapper');
        if (wrapper) {
            wrapper.innerHTML = content;
            this.attachHandlers();
        }
    },

    attachHandlers() {
        // ---- Theme card actions ----
        document.querySelectorAll('[data-action="customize"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', (e) => {
                const themeId = parseInt(e.target.dataset.themeId);
                AppState.selectedThemeId = themeId;
                AppState.selectedTemplateId = null;
                AppState.selectedSectionId = null;
                AppState.selectedBlockId = null;
                Router.navigate('/editor/' + themeId);
            });
        });

        document.querySelectorAll('[data-action="publish"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', (e) => {
                const themeId = parseInt(e.target.dataset.themeId);
                const theme = AppState.getTheme(themeId);
                Components.confirm('Publish theme',
                    `Are you sure you want to publish "${theme?.name}"? This will replace your current live theme.`,
                    () => {
                        AppState.publishTheme(themeId);
                        Components.showToast('Theme published', 'success');
                        Router.render();
                    }
                );
            });
        });

        document.querySelectorAll('[data-action="theme-menu"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const themeId = e.target.closest('[data-theme-id]').dataset.themeId;
                const menu = document.getElementById('themeMenu' + themeId);
                document.querySelectorAll('.theme-menu.active').forEach(m => {
                    if (m !== menu) m.classList.remove('active');
                });
                if (menu) menu.classList.toggle('active');
            });
        });

        document.querySelectorAll('[data-action="rename"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                Views._showRenameThemeModal(parseInt(btn.dataset.themeId));
            });
        });

        document.querySelectorAll('[data-action="duplicate"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.duplicateTheme(parseInt(btn.dataset.themeId));
                Components.showToast('Theme duplicated', 'success');
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="preview"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                Components.showToast('Preview link copied to clipboard', 'info');
            });
        });

        document.querySelectorAll('[data-action="delete"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                const themeId = parseInt(btn.dataset.themeId);
                const theme = AppState.getTheme(themeId);
                Components.confirm('Delete theme',
                    `Are you sure you want to delete "${theme?.name}"? This action cannot be undone.`,
                    () => {
                        AppState.deleteTheme(themeId);
                        Components.showToast('Theme deleted', 'success');
                        Router.render();
                    },
                    { danger: true, confirmText: 'Delete' }
                );
            });
        });

        // ---- Add theme button ----
        const addThemeBtn = document.getElementById('addThemeBtn');
        if (addThemeBtn && !addThemeBtn._handlerAttached) {
            addThemeBtn._handlerAttached = true;
            addThemeBtn.addEventListener('click', () => Views._showAddThemeModal());
        }

        // ---- Reset data button ----
        const resetBtn = document.getElementById('resetDataBtn');
        if (resetBtn && !resetBtn._handlerAttached) {
            resetBtn._handlerAttached = true;
            resetBtn.addEventListener('click', () => {
                Components.confirm('Reset all data',
                    'This will restore all themes and settings to their original state. All changes will be lost.',
                    () => {
                        AppState.resetToSeedData();
                        AppState.notify();
                        Components.showToast('Data reset to defaults', 'success');
                        Router.navigate('/');
                    },
                    { danger: true, confirmText: 'Reset' }
                );
            });
        }

        // ---- Editor: Back to themes ----
        document.querySelectorAll('[data-action="back-to-themes"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.selectedSectionId = null;
                AppState.selectedBlockId = null;
                Router.navigate('/');
            });
        });

        // ---- Editor: Back to editor from settings ----
        document.querySelectorAll('[data-action="back-to-editor"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                Router.navigate('/editor/' + AppState.selectedThemeId);
            });
        });

        // ---- Template selector ----
        const templateSelector = document.getElementById('templateSelector');
        if (templateSelector && !templateSelector._handlerAttached) {
            templateSelector._handlerAttached = true;
            templateSelector.addEventListener('change', (e) => {
                const templateId = parseInt(e.detail.value);
                AppState.selectedTemplateId = templateId;
                AppState.selectedSectionId = null;
                AppState.selectedBlockId = null;
                Router.render();
            });
        }

        // ---- View mode ----
        document.querySelectorAll('[data-action="set-mode"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.editorMode = btn.dataset.mode;
                Router.render();
            });
        });

        // ---- Open theme settings ----
        document.querySelectorAll('[data-action="open-theme-settings"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                Router.navigate('/settings/' + AppState.selectedThemeId);
            });
        });

        // ---- Section tree items ----
        document.querySelectorAll('.tree-section-header .tree-label').forEach(label => {
            if (label._handlerAttached) return;
            label._handlerAttached = true;
            label.addEventListener('click', () => {
                const sectionId = parseInt(label.dataset.sectionId);
                AppState.selectedSectionId = sectionId;
                AppState.selectedBlockId = null;
                Router.render();
            });
        });

        document.querySelectorAll('.tree-expand').forEach(arrow => {
            if (arrow._handlerAttached) return;
            arrow._handlerAttached = true;
            arrow.addEventListener('click', (e) => {
                const sectionId = arrow.dataset.sectionId;
                const blocksEl = document.getElementById('sectionBlocks' + sectionId);
                if (blocksEl) {
                    blocksEl.classList.toggle('collapsed');
                    arrow.classList.toggle('collapsed');
                }
            });
        });

        // ---- Block tree items ----
        document.querySelectorAll('.tree-block').forEach(block => {
            if (block._handlerAttached) return;
            block._handlerAttached = true;
            block.addEventListener('click', () => {
                const blockId = parseInt(block.dataset.blockId);
                const b = AppState.getBlock(blockId);
                if (b) {
                    AppState.selectedBlockId = blockId;
                    AppState.selectedSectionId = b.sectionId;
                    Router.render();
                }
            });
        });

        // ---- Preview section click ----
        document.querySelectorAll('.preview-section').forEach(el => {
            if (el._handlerAttached) return;
            el._handlerAttached = true;
            el.addEventListener('click', () => {
                const sectionId = parseInt(el.dataset.sectionId);
                AppState.selectedSectionId = sectionId;
                AppState.selectedBlockId = null;
                Router.render();
            });
        });

        // ---- Add section buttons ----
        document.querySelectorAll('[data-action="add-section"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const area = btn.dataset.area;
                const templateId = parseInt(btn.dataset.templateId);
                Views._showAddSectionModal(templateId, AppState.selectedThemeId, area);
            });
        });

        // ---- Section settings actions ----
        this._attachSectionActions();
        this._attachBlockActions();
        this._attachSettingsInputs();
        this._attachThemeSettingsInputs();
        this._attachSettingsTabNavigation();

        // ---- Close settings panel ----
        document.querySelectorAll('[data-action="close-settings"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.selectedSectionId = null;
                AppState.selectedBlockId = null;
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="back-to-section"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.selectedBlockId = null;
                Router.render();
            });
        });

        // ---- Collapse headers ----
        document.querySelectorAll('[data-collapse]').forEach(header => {
            if (header._handlerAttached) return;
            header._handlerAttached = true;
            header.addEventListener('click', (e) => {
                if (e.target.tagName === 'BUTTON') return;
                const targetId = header.dataset.collapse;
                const target = document.getElementById(targetId);
                if (target) {
                    target.classList.toggle('collapsed');
                    header.querySelector('.collapse-icon')?.classList.toggle('collapsed');
                }
            });
        });
    },

    _attachSectionActions() {
        document.querySelectorAll('[data-action="hide-section"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.hideSection(parseInt(btn.dataset.sectionId));
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="duplicate-section"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.duplicateSection(parseInt(btn.dataset.sectionId));
                Components.showToast('Section duplicated', 'success');
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="remove-section"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                Components.confirm('Remove section',
                    'Are you sure you want to remove this section? All blocks in this section will also be removed.',
                    () => {
                        AppState.removeSection(parseInt(btn.dataset.sectionId));
                        Components.showToast('Section removed', 'success');
                        Router.render();
                    },
                    { danger: true, confirmText: 'Remove' }
                );
            });
        });

        document.querySelectorAll('[data-action="move-section-up"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.moveSectionUp(parseInt(btn.dataset.sectionId));
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="move-section-down"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.moveSectionDown(parseInt(btn.dataset.sectionId));
                Router.render();
            });
        });
    },

    _attachBlockActions() {
        document.querySelectorAll('[data-action="select-block"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                const blockId = parseInt(btn.dataset.blockId);
                const block = AppState.getBlock(blockId);
                if (block) {
                    AppState.selectedBlockId = blockId;
                    AppState.selectedSectionId = block.sectionId;
                    Router.render();
                }
            });
        });

        document.querySelectorAll('[data-action="hide-block"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.hideBlock(parseInt(btn.dataset.blockId));
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="duplicate-block"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.duplicateBlock(parseInt(btn.dataset.blockId));
                Components.showToast('Block duplicated', 'success');
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="remove-block"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.removeBlock(parseInt(btn.dataset.blockId));
                Components.showToast('Block removed', 'success');
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="move-block-up"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.moveBlockUp(parseInt(btn.dataset.blockId));
                Router.render();
            });
        });

        document.querySelectorAll('[data-action="move-block-down"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                AppState.moveBlockDown(parseInt(btn.dataset.blockId));
                Router.render();
            });
        });

        // Add block
        document.querySelectorAll('[data-action="add-block"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                const sectionId = parseInt(btn.dataset.sectionId);
                const typeDropdown = document.getElementById('addBlockType');
                const blockType = typeDropdown?.dataset.value;
                if (!blockType) {
                    Components.showToast('Select a block type first', 'warning');
                    return;
                }
                const blockDef = BLOCK_TYPES.find(bt => bt.id === blockType);
                AppState.addBlock(sectionId, AppState.selectedThemeId, blockType, blockDef?.name);
                Components.showToast('Block added', 'success');
                Router.render();
            });
        });
    },

    _attachSettingsInputs() {
        // Section name
        const sectionName = document.getElementById('sectionName');
        if (sectionName && !sectionName._handlerAttached) {
            sectionName._handlerAttached = true;
            sectionName.addEventListener('change', () => {
                AppState.renameSection(AppState.selectedSectionId, sectionName.value);
            });
        }

        // Section color scheme dropdown
        const sectionColorScheme = document.getElementById('sectionColorScheme');
        if (sectionColorScheme && !sectionColorScheme._handlerAttached) {
            sectionColorScheme._handlerAttached = true;
            sectionColorScheme.addEventListener('change', (e) => {
                AppState.updateSectionColorScheme(AppState.selectedSectionId, parseInt(e.detail.value));
            });
        }

        // Section custom CSS
        const sectionCss = document.getElementById('sectionCustomCss');
        if (sectionCss && !sectionCss._handlerAttached) {
            sectionCss._handlerAttached = true;
            sectionCss.addEventListener('change', () => {
                AppState.updateSectionCustomCss(AppState.selectedSectionId, sectionCss.value);
            });
        }

        // Block settings
        this._attachBlockSettingsInputs();
    },

    _attachBlockSettingsInputs() {
        if (!AppState.selectedBlockId) return;
        const block = AppState.getBlock(AppState.selectedBlockId);
        if (!block) return;

        // Block name
        const blockName = document.getElementById('blockName');
        if (blockName && !blockName._handlerAttached) {
            blockName._handlerAttached = true;
            blockName.addEventListener('change', () => {
                AppState.renameBlock(AppState.selectedBlockId, blockName.value);
            });
        }

        // Block text
        const blockText = document.getElementById('blockText');
        if (blockText && !blockText._handlerAttached) {
            blockText._handlerAttached = true;
            blockText.addEventListener('change', () => {
                AppState.updateBlockSettings(AppState.selectedBlockId, { text: blockText.value });
                Router.render();
            });
        }

        // Block title
        const blockTitle = document.getElementById('blockTitle');
        if (blockTitle && !blockTitle._handlerAttached) {
            blockTitle._handlerAttached = true;
            blockTitle.addEventListener('change', () => {
                AppState.updateBlockSettings(AppState.selectedBlockId, { title: blockTitle.value });
                Router.render();
            });
        }

        // Block link
        const blockLink = document.getElementById('blockLink');
        if (blockLink && !blockLink._handlerAttached) {
            blockLink._handlerAttached = true;
            blockLink.addEventListener('change', () => {
                AppState.updateBlockSettings(AppState.selectedBlockId, { link: blockLink.value });
            });
        }

        // Block size dropdown
        const blockSize = document.getElementById('blockSize');
        if (blockSize && !blockSize._handlerAttached) {
            blockSize._handlerAttached = true;
            blockSize.addEventListener('change', (e) => {
                AppState.updateBlockSettings(AppState.selectedBlockId, { size: e.detail.value });
            });
        }

        // Block style dropdown
        const blockStyle = document.getElementById('blockStyle');
        if (blockStyle && !blockStyle._handlerAttached) {
            blockStyle._handlerAttached = true;
            blockStyle.addEventListener('change', (e) => {
                AppState.updateBlockSettings(AppState.selectedBlockId, { style: e.detail.value });
            });
        }

        // Block menu dropdown
        const blockMenu = document.getElementById('blockMenu');
        if (blockMenu && !blockMenu._handlerAttached) {
            blockMenu._handlerAttached = true;
            blockMenu.addEventListener('change', (e) => {
                AppState.updateBlockSettings(AppState.selectedBlockId, { menu: e.detail.value });
            });
        }
    },

    _attachThemeSettingsInputs() {
        const themeId = AppState.selectedThemeId;
        const settings = AppState.getThemeSettings(themeId);
        if (!settings) return;

        // Logo settings
        this._bindInput('logoAltText', v => AppState.updateThemeSettings(themeId, 'logo.altText', v));
        this._bindRange('logoWidth', v => AppState.updateThemeSettings(themeId, 'logo.width', parseInt(v)));

        // Typography
        this._bindDropdown('headingFont', v => AppState.updateThemeSettings(themeId, 'typography.headingFont', v));
        this._bindDropdown('bodyFont', v => AppState.updateThemeSettings(themeId, 'typography.bodyFont', v));
        this._bindDropdown('fontSizeScale', v => AppState.updateThemeSettings(themeId, 'typography.fontSizeScale', parseInt(v)));

        // Layout
        this._bindRange('pageWidth', v => AppState.updateThemeSettings(themeId, 'layout.pageWidth', parseInt(v)));
        this._bindRange('sectionSpacing', v => AppState.updateThemeSettings(themeId, 'layout.sectionSpacing', parseInt(v)));
        this._bindRange('gridHSpacing', v => AppState.updateThemeSettings(themeId, 'layout.gridHorizontalSpacing', parseInt(v)));
        this._bindRange('gridVSpacing', v => AppState.updateThemeSettings(themeId, 'layout.gridVerticalSpacing', parseInt(v)));

        // Animations
        this._bindCheckbox('revealOnScroll', v => AppState.updateThemeSettings(themeId, 'animations.revealOnScroll', v));
        this._bindDropdown('hoverEffect', v => AppState.updateThemeSettings(themeId, 'animations.hoverEffect', v));

        // Buttons
        this._bindDropdown('buttonStyle', v => AppState.updateThemeSettings(themeId, 'buttons.style', v));
        this._bindRange('buttonRadius', v => AppState.updateThemeSettings(themeId, 'buttons.borderRadius', parseInt(v)));
        this._bindDropdown('variantPillStyle', v => AppState.updateThemeSettings(themeId, 'variantPills.style', v));

        // Inputs
        this._bindDropdown('inputStyle', v => AppState.updateThemeSettings(themeId, 'inputs.style', v));
        this._bindRange('inputRadius', v => AppState.updateThemeSettings(themeId, 'inputs.borderRadius', parseInt(v)));

        // Badges
        this._bindDropdown('saleBadgePos', v => AppState.updateThemeSettings(themeId, 'badges.salePosition', v));
        this._bindDropdown('saleBadgeShape', v => AppState.updateThemeSettings(themeId, 'badges.saleShape', v));
        this._bindDropdown('soldOutBadgePos', v => AppState.updateThemeSettings(themeId, 'badges.soldOutPosition', v));
        this._bindDropdown('soldOutBadgeShape', v => AppState.updateThemeSettings(themeId, 'badges.soldOutShape', v));

        // Search
        this._bindCheckbox('searchSuggestions', v => AppState.updateThemeSettings(themeId, 'searchBehavior.enableSuggestions', v));
        this._bindCheckbox('searchShowVendor', v => AppState.updateThemeSettings(themeId, 'searchBehavior.showVendor', v));
        this._bindCheckbox('searchShowPrice', v => AppState.updateThemeSettings(themeId, 'searchBehavior.showPrice', v));

        // Currency
        this._bindCheckbox('showCurrencyCode', v => AppState.updateThemeSettings(themeId, 'currencyFormat.showCurrencyCode', v));

        // Cart
        this._bindDropdown('cartType', v => { AppState.updateThemeSettings(themeId, 'cart.type', v); Router.render(); });
        this._bindCheckbox('cartShowVendor', v => AppState.updateThemeSettings(themeId, 'cart.showVendor', v));
        this._bindCheckbox('cartEnableNote', v => AppState.updateThemeSettings(themeId, 'cart.enableNote', v));
        this._bindDropdown('cartColorScheme', v => AppState.updateThemeSettings(themeId, 'cart.cartColorSchemeId', parseInt(v)));

        // Custom CSS
        this._bindTextarea('themeCustomCss', v => AppState.updateThemeCustomCss(themeId, v));

        // Social links
        ['instagram', 'tiktok', 'facebook', 'pinterest', 'twitter', 'youtube', 'linkedin', 'snapchat', 'tumblr', 'vimeo'].forEach(platform => {
            this._bindInput('social_' + platform, v => AppState.updateSocialLink(themeId, platform, v));
        });

        // Color scheme interactions
        document.querySelectorAll('.color-scheme-card').forEach(card => {
            if (card._handlerAttached) return;
            card._handlerAttached = true;
            card.addEventListener('click', () => {
                const schemeId = parseInt(card.dataset.schemeId);
                const scheme = settings.colors.find(c => c.id === schemeId);
                if (scheme) {
                    const editor = document.getElementById('colorSchemeEditor');
                    if (editor) {
                        editor.innerHTML = Views._renderColorSchemeEditor(themeId, scheme);
                        Router._attachColorSchemeEditorInputs(themeId, schemeId);
                    }
                }
            });
        });

        document.querySelectorAll('[data-action="add-color-scheme"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                const scheme = AppState.addColorScheme(themeId);
                if (scheme) {
                    Components.showToast('Color scheme added', 'success');
                    Router.render();
                } else {
                    Components.showToast('Maximum 21 color schemes', 'error');
                }
            });
        });

        // Attach color scheme editor inputs if visible
        const csEditor = document.querySelector('.color-scheme-detail');
        if (csEditor) {
            const schemeId = parseInt(csEditor.dataset.schemeId);
            this._attachColorSchemeEditorInputs(themeId, schemeId);
        }
    },

    _attachColorSchemeEditorInputs(themeId, schemeId) {
        this._bindInput('schemeName', v => AppState.updateColorScheme(themeId, schemeId, 'name', v));
        this._bindColorInput('schemeBg', v => AppState.updateColorScheme(themeId, schemeId, 'background', v));
        this._bindInput('schemeBgGradient', v => AppState.updateColorScheme(themeId, schemeId, 'backgroundGradient', v));
        this._bindColorInput('schemeText', v => AppState.updateColorScheme(themeId, schemeId, 'text', v));
        this._bindColorInput('schemeSolidBtnBg', v => AppState.updateColorScheme(themeId, schemeId, 'solidButtonBg', v));
        this._bindColorInput('schemeSolidBtnText', v => AppState.updateColorScheme(themeId, schemeId, 'solidButtonText', v));
        this._bindColorInput('schemeOutlineBtn', v => AppState.updateColorScheme(themeId, schemeId, 'outlineButton', v));
        this._bindColorInput('schemeShadow', v => AppState.updateColorScheme(themeId, schemeId, 'shadow', v));

        document.querySelectorAll('[data-action="remove-color-scheme"]').forEach(btn => {
            if (btn._handlerAttached) return;
            btn._handlerAttached = true;
            btn.addEventListener('click', () => {
                const sid = parseInt(btn.dataset.schemeId);
                Components.confirm('Remove color scheme',
                    'Are you sure? Sections using this scheme will revert to the default.',
                    () => {
                        AppState.removeColorScheme(themeId, sid);
                        Components.showToast('Color scheme removed', 'success');
                        Router.render();
                    },
                    { danger: true }
                );
            });
        });
    },

    _attachSettingsTabNavigation() {
        document.querySelectorAll('[data-settings-tab]').forEach(tab => {
            if (tab._handlerAttached) return;
            tab._handlerAttached = true;
            tab.addEventListener('click', () => {
                const tabId = tab.dataset.settingsTab;
                Router.navigate('/settings/' + AppState.selectedThemeId + '?settingsTab=' + tabId);
            });
        });
    },

    // ---- Binding helpers ----
    _bindInput(id, handler) {
        const el = document.getElementById(id);
        if (el && !el._handlerAttached) {
            el._handlerAttached = true;
            el.addEventListener('change', () => handler(el.value));
        }
    },

    _bindTextarea(id, handler) {
        const el = document.getElementById(id);
        if (el && !el._handlerAttached) {
            el._handlerAttached = true;
            el.addEventListener('change', () => handler(el.value));
        }
    },

    _bindCheckbox(id, handler) {
        const el = document.getElementById(id);
        if (el && !el._handlerAttached) {
            el._handlerAttached = true;
            el.addEventListener('change', () => handler(el.checked));
        }
    },

    _bindDropdown(id, handler) {
        const el = document.getElementById(id);
        if (el && !el._handlerAttached) {
            el._handlerAttached = true;
            el.addEventListener('change', (e) => handler(e.detail.value));
        }
    },

    _bindRange(id, handler) {
        const el = document.getElementById(id);
        if (el && !el._handlerAttached) {
            el._handlerAttached = true;
            el.addEventListener('input', () => {
                const valueEl = document.getElementById(id + 'Value');
                if (valueEl) valueEl.textContent = el.value + (el.dataset.unit || 'px');
                handler(el.value);
            });
        }
    },

    _bindColorInput(id, handler) {
        const el = document.getElementById(id);
        if (el && !el._handlerAttached) {
            el._handlerAttached = true;
            el.addEventListener('change', () => {
                const val = el.value;
                if (/^#[0-9A-Fa-f]{6}$/.test(val)) {
                    const swatch = document.getElementById(id + 'Swatch');
                    if (swatch) swatch.style.background = val;
                    handler(val);
                }
            });
        }
    }
};

// ---- Initialize ----
document.addEventListener('DOMContentLoaded', () => {
    AppState.init();

    window.addEventListener('hashchange', () => Router.render());
    Router.render();
});

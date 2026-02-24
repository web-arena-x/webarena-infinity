/* ================================================================
   Shopify Theme Editor — Application Controller
   ================================================================ */

(function() {
  'use strict';

  // ── DOM References ──────────────────────────────────────────
  const sidebar = document.getElementById('sidebar');
  const sidebarContent = document.getElementById('sidebarContent');
  const settingsPanel = document.getElementById('settingsPanel');
  const previewWindow = document.getElementById('previewWindow');
  const tabSections = document.getElementById('tabSections');
  const tabThemeSettings = document.getElementById('tabThemeSettings');

  // Menu bar elements
  const templateSelector = document.getElementById('templateSelector');
  const marketSelector = document.getElementById('marketSelector');
  const btnUndo = document.getElementById('btnUndo');
  const btnRedo = document.getElementById('btnRedo');
  const btnSave = document.getElementById('btnSave');
  const btnInspector = document.getElementById('btnInspector');
  const btnDesktop = document.getElementById('btnDesktop');
  const btnMobile = document.getElementById('btnMobile');
  const btnFullscreen = document.getElementById('btnFullscreen');

  // ── Render cycle ────────────────────────────────────────────
  function render() {
    // Sidebar tabs
    tabSections.classList.toggle('active', AppState.sidebarView === 'sections');
    tabThemeSettings.classList.toggle('active', AppState.sidebarView === 'themeSettings');

    // Sidebar content
    if (AppState.sidebarView === 'sections') {
      sidebarContent.innerHTML = Views.renderSectionsTab();
    } else {
      sidebarContent.innerHTML = Views.renderThemeSettingsTab();
    }

    // Settings panel
    settingsPanel.innerHTML = Views.renderSettingsPanel();

    // Preview
    previewWindow.innerHTML = Views.renderPreview();

    // Menu bar state
    btnUndo.disabled = AppState.undoStack.length === 0;
    btnRedo.disabled = AppState.redoStack.length === 0;
    btnSave.classList.toggle('has-changes', AppState.hasUnsavedChanges);
    btnInspector.classList.toggle('active', AppState.previewInspectorActive);

    btnDesktop.classList.toggle('active', AppState.screenSize === 'desktop');
    btnMobile.classList.toggle('active', AppState.screenSize === 'mobile');
    btnFullscreen.classList.toggle('active', AppState.screenSize === 'fullscreen');

    // Attach event handlers
    attachHandlers();
  }

  // ── Event handlers ──────────────────────────────────────────
  function attachHandlers() {
    // Section tree: select section
    document.querySelectorAll('[data-select-section]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        AppState.selectedSectionId = el.dataset.selectSection;
        AppState.selectedBlockId = null;
        render();
      });
    });

    // Section tree: select block
    document.querySelectorAll('[data-select-block]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        const block = AppState.getBlock(el.dataset.selectBlock);
        if (block) {
          AppState.selectedSectionId = block.sectionId;
          AppState.selectedBlockId = el.dataset.selectBlock;
        }
        render();
      });
    });

    // Section tree: toggle section visibility
    document.querySelectorAll('[data-toggle-section-vis]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        AppState.toggleSectionVisibility(el.dataset.toggleSectionVis);
      });
    });

    // Section tree: toggle block visibility
    document.querySelectorAll('[data-toggle-block-vis]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        AppState.toggleBlockVisibility(el.dataset.toggleBlockVis);
      });
    });

    // Add section button
    document.querySelectorAll('[data-add-section]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        const group = el.dataset.addSection;
        Components.showSectionTypePicker((type) => {
          AppState.addSection(AppState.currentTemplate, group, type);
        });
      });
    });

    // Theme settings categories
    document.querySelectorAll('[data-theme-category]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        AppState.themeSettingsCategory = el.dataset.themeCategory;
        AppState.selectedSectionId = null;
        AppState.selectedBlockId = null;
        render();
      });
    });

    // Preview section click
    document.querySelectorAll('[data-preview-section]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        AppState.selectedSectionId = el.dataset.previewSection;
        AppState.selectedBlockId = null;
        AppState.sidebarView = 'sections';
        render();
      });
    });

    // Settings panel: back to sections list
    document.querySelectorAll('[data-deselect-section]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        AppState.selectedSectionId = null;
        AppState.selectedBlockId = null;
        render();
      });
    });

    // Settings panel: back to section from block
    document.querySelectorAll('[data-back-to-section]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        AppState.selectedBlockId = null;
        render();
      });
    });

    // Remove section
    document.querySelectorAll('[data-remove-section]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        Components.confirm('Remove section', 'Are you sure you want to remove this section?', () => {
          AppState.removeSection(el.dataset.removeSection);
        });
      });
    });

    // Remove block
    document.querySelectorAll('[data-remove-block]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        AppState.removeBlock(el.dataset.removeBlock);
      });
    });

    // Move block up/down
    document.querySelectorAll('[data-move-block-up]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', (e) => { e.stopPropagation(); AppState.moveBlockUp(el.dataset.moveBlockUp); });
    });
    document.querySelectorAll('[data-move-block-down]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', (e) => { e.stopPropagation(); AppState.moveBlockDown(el.dataset.moveBlockDown); });
    });

    // Duplicate block
    document.querySelectorAll('[data-duplicate-block]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', (e) => { e.stopPropagation(); AppState.duplicateBlock(el.dataset.duplicateBlock); });
    });

    // Add block
    document.querySelectorAll('[data-add-block-to]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        const section = AppState.getSection(el.dataset.addBlockTo);
        if (section) {
          Components.showBlockTypePicker(section.type, (blockType) => {
            AppState.addBlock(section.id, blockType);
          });
        }
      });
    });

    // Color scheme: edit
    document.querySelectorAll('[data-edit-scheme]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        showColorSchemeEditor(el.dataset.editScheme);
      });
    });

    // Color scheme: remove
    document.querySelectorAll('[data-remove-scheme]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        Components.confirm('Remove color scheme', 'Are you sure?', () => {
          AppState.removeColorScheme(el.dataset.removeScheme);
        });
      });
    });

    // Add color scheme
    const addSchemeBtn = document.getElementById('addColorSchemeBtn');
    if (addSchemeBtn && !addSchemeBtn._handlerAttached) {
      addSchemeBtn._handlerAttached = true;
      addSchemeBtn.addEventListener('click', () => {
        const newId = AppState.addColorScheme();
        showColorSchemeEditor(newId);
      });
    }

    // Theme style buttons
    document.querySelectorAll('[data-apply-style]').forEach(el => {
      if (el._handlerAttached) return;
      el._handlerAttached = true;
      el.addEventListener('click', () => {
        AppState.applyThemeStyle(el.dataset.applyStyle);
      });
    });

    // Attach settings panel input handlers
    attachSettingsInputHandlers();
  }

  // ── Settings input change handlers ──────────────────────────
  function attachSettingsInputHandlers() {
    const panel = settingsPanel;
    if (!panel || panel._inputHandlersAttached) return;
    panel._inputHandlersAttached = true;

    panel.addEventListener('change', handleSettingsChange);
    panel.addEventListener('input', debounce(handleSettingsInput, 300));
  }

  function handleSettingsChange(e) {
    const target = e.target;

    // Toggle switches
    if (target.classList.contains('toggle-input')) {
      const checked = target.checked;
      applySettingValue(target.id, checked);
      return;
    }

    // Custom dropdown change events
    if (e.detail && e.detail.value !== undefined) {
      const dropdown = e.target.closest('.custom-dropdown');
      if (dropdown) {
        applySettingValue(dropdown.id, e.detail.value);
      }
      return;
    }
  }

  function handleSettingsInput(e) {
    const target = e.target;

    // Range sliders
    if (target.classList.contains('range-slider')) {
      applySettingValue(target.id, parseFloat(target.value));
      return;
    }

    // Text inputs
    if (target.classList.contains('text-input') || target.classList.contains('color-hex-input')) {
      applySettingValue(target.id, target.value);
      return;
    }

    // Textareas
    if (target.tagName === 'TEXTAREA') {
      applySettingValue(target.id, target.value);
      return;
    }

    // Number inputs
    if (target.type === 'number') {
      applySettingValue(target.id, parseFloat(target.value));
      return;
    }
  }

  function applySettingValue(inputId, value) {
    if (!inputId) return;

    // Theme settings mapping (prefix-based)
    const mappings = {
      // Typography
      'typo-headingFont': () => AppState.updateThemeSettings('typography', { headingFont: value }),
      'typo-headingFontSizeScale': () => AppState.updateThemeSettings('typography', { headingFontSizeScale: value }),
      'typo-bodyFont': () => AppState.updateThemeSettings('typography', { bodyFont: value }),
      'typo-bodyFontSizeScale': () => AppState.updateThemeSettings('typography', { bodyFontSizeScale: value }),

      // Layout
      'layout-pageWidth': () => AppState.updateThemeSettings('layout', { pageWidth: value }),
      'layout-sectionSpacing': () => AppState.updateThemeSettings('layout', { sectionSpacing: value }),
      'layout-gridHorizontalSpace': () => AppState.updateThemeSettings('layout', { gridHorizontalSpace: value }),
      'layout-gridVerticalSpace': () => AppState.updateThemeSettings('layout', { gridVerticalSpace: value }),

      // Logo
      'logo-altText': () => AppState.updateThemeSettings('logo', { altText: value }),
      'logo-desktopLogoWidth': () => AppState.updateThemeSettings('logo', { desktopLogoWidth: value }),
      'logo-faviconAltText': () => AppState.updateThemeSettings('logo', { faviconAltText: value }),

      // Animations
      'anim-revealSectionsOnScroll': () => AppState.updateThemeSettings('animations', { revealSectionsOnScroll: value }),
      'anim-hoverEffect': () => AppState.updateThemeSettings('animations', { hoverEffect: value }),

      // Buttons
      'btn-borderRadius': () => AppState.updateThemeSettings('buttons', { borderRadius: value }),
      'btn-shadow': () => AppState.updateThemeSettings('buttons', { shadow: value }),
      'btn-border': () => AppState.updateThemeSettings('buttons', { border: value }),

      // Variant pills
      'vp-shape': () => AppState.updateThemeSettings('variantPills', { shape: value }),
      'vp-border': () => AppState.updateThemeSettings('variantPills', { border: value }),

      // Inputs
      'inp-shape': () => AppState.updateThemeSettings('inputs', { shape: value }),
      'inp-border': () => AppState.updateThemeSettings('inputs', { border: value }),

      // Product cards
      'pc-style': () => AppState.updateThemeSettings('productCards', { style: value }),
      'pc-imageRatio': () => AppState.updateThemeSettings('productCards', { imageRatio: value }),
      'pc-showSecondImageOnHover': () => AppState.updateThemeSettings('productCards', { showSecondImageOnHover: value }),
      'pc-showVendor': () => AppState.updateThemeSettings('productCards', { showVendor: value }),
      'pc-showRating': () => AppState.updateThemeSettings('productCards', { showRating: value }),

      // Collection cards
      'cc-style': () => AppState.updateThemeSettings('collectionCards', { style: value }),
      'cc-imageRatio': () => AppState.updateThemeSettings('collectionCards', { imageRatio: value }),

      // Blog cards
      'bc-style': () => AppState.updateThemeSettings('blogCards', { style: value }),
      'bc-showDate': () => AppState.updateThemeSettings('blogCards', { showDate: value }),
      'bc-showAuthor': () => AppState.updateThemeSettings('blogCards', { showAuthor: value }),

      // Content containers
      'cc2-borderRadius': () => AppState.updateThemeSettings('contentContainers', { borderRadius: value }),
      'cc2-shadow': () => AppState.updateThemeSettings('contentContainers', { shadow: value }),

      // Media
      'media-borderRadius': () => AppState.updateThemeSettings('media', { borderRadius: value }),
      'media-shadow': () => AppState.updateThemeSettings('media', { shadow: value }),

      // Dropdowns/popups
      'dp-borderRadius': () => AppState.updateThemeSettings('dropdownsAndPopups', { borderRadius: value }),
      'dp-shadow': () => AppState.updateThemeSettings('dropdownsAndPopups', { shadow: value }),

      // Drawers
      'dr-borderRadius': () => AppState.updateThemeSettings('drawers', { borderRadius: value }),
      'dr-shadow': () => AppState.updateThemeSettings('drawers', { shadow: value }),

      // Badges
      'badge-salePosition': () => AppState.updateThemeSettings('badges', { salePosition: value }),
      'badge-saleShape': () => AppState.updateThemeSettings('badges', { saleShape: value }),
      'badge-saleColor': () => AppState.updateThemeSettings('badges', { saleColor: value }),
      'badge-soldOutPosition': () => AppState.updateThemeSettings('badges', { soldOutPosition: value }),
      'badge-soldOutShape': () => AppState.updateThemeSettings('badges', { soldOutShape: value }),

      // Brand information
      'brand-showBrandImage': () => AppState.updateThemeSettings('brandInformation', { showBrandImage: value }),
      'brand-showBrandDescription': () => AppState.updateThemeSettings('brandInformation', { showBrandDescription: value }),
      'brand-showSocialMediaLinks': () => AppState.updateThemeSettings('brandInformation', { showSocialMediaLinks: value }),

      // Social media
      'social-facebook': () => AppState.updateThemeSettings('socialMedia', { facebook: value }),
      'social-instagram': () => AppState.updateThemeSettings('socialMedia', { instagram: value }),
      'social-twitter': () => AppState.updateThemeSettings('socialMedia', { twitter: value }),
      'social-tiktok': () => AppState.updateThemeSettings('socialMedia', { tiktok: value }),
      'social-snapchat': () => AppState.updateThemeSettings('socialMedia', { snapchat: value }),
      'social-pinterest': () => AppState.updateThemeSettings('socialMedia', { pinterest: value }),
      'social-tumblr': () => AppState.updateThemeSettings('socialMedia', { tumblr: value }),
      'social-youtube': () => AppState.updateThemeSettings('socialMedia', { youtube: value }),
      'social-vimeo': () => AppState.updateThemeSettings('socialMedia', { vimeo: value }),
      'social-linkedin': () => AppState.updateThemeSettings('socialMedia', { linkedin: value }),

      // Search behavior
      'search-enableSuggestions': () => AppState.updateThemeSettings('searchBehavior', { enableSuggestions: value }),
      'search-showVendor': () => AppState.updateThemeSettings('searchBehavior', { showVendor: value }),
      'search-showPrice': () => AppState.updateThemeSettings('searchBehavior', { showPrice: value }),

      // Currency format
      'currency-showCurrencyCodes': () => AppState.updateThemeSettings('currencyFormat', { showCurrencyCodes: value }),

      // Cart
      'cart-type': () => AppState.updateThemeSettings('cart', { type: value }),
      'cart-showVendor': () => AppState.updateThemeSettings('cart', { showVendor: value }),
      'cart-enableCartNote': () => AppState.updateThemeSettings('cart', { enableCartNote: value }),
      'cart-drawerCollection': () => AppState.updateThemeSettings('cart', { drawerCollection: value }),
      'cart-drawerColorSchemeId': () => AppState.updateThemeSettings('cart', { drawerColorSchemeId: value }),

      // Custom CSS
      'custom-css': () => { AppState.themeSettings.customCSS = value; AppState._pushUndo(); AppState.notify(); },

      // Section settings
      'section-name': () => {
        if (AppState.selectedSectionId) AppState.updateSectionName(AppState.selectedSectionId, value);
      },
      'section-colorSchemeId': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { colorSchemeId: value });
      },
      'section-autoPlay': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { autoPlay: value });
      },
      'section-slideInterval': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { slideInterval: value });
      },
      'section-title': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { title: value });
      },
      'section-collectionId': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { collectionId: parseInt(value) || value });
      },
      'section-productsToShow': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { productsToShow: value });
      },
      'section-height': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { height: value });
      },
      'section-columnsDesktop': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { columnsDesktop: value });
      },
      'section-fullWidth': () => {
        if (AppState.selectedSectionId) AppState.updateSectionSettings(AppState.selectedSectionId, { fullWidth: value });
      },

      // Block settings
      'block-text': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { text: value }); },
      'block-link': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { link: value }); },
      'block-heading': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { heading: value }); },
      'block-subheading': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { subheading: value }); },
      'block-buttonLabel': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { buttonLabel: value }); },
      'block-buttonLink': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { buttonLink: value }); },
      'block-size': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { size: value }); },
      'block-label': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { label: value }); },
      'block-style': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { style: value }); },
      'block-title': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { title: value }); },
      'block-linkLabel': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { linkLabel: value }); },
      'block-linkUrl': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { linkUrl: value }); },
      'block-collectionId': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { collectionId: parseInt(value) || value }); },
      'block-placeholder': () => { if (AppState.selectedBlockId) AppState.updateBlockSettings(AppState.selectedBlockId, { placeholder: value }); },
    };

    const handler = mappings[inputId];
    if (handler) handler();
  }

  // ── Color scheme editor modal ───────────────────────────────
  function showColorSchemeEditor(schemeId) {
    const scheme = AppState.themeSettings.colors.schemes.find(s => s.id === schemeId);
    if (!scheme) return;

    const bodyHtml = `<div class="color-scheme-editor">
      ${Components.textInput('cse-name', scheme.name, { label: 'Name' })}
      ${Components.colorPicker('cse-background', scheme.background, { label: 'Background' })}
      ${Components.textInput('cse-backgroundGradient', scheme.backgroundGradient, { label: 'Background gradient', placeholder: 'e.g. linear-gradient(135deg, #667eea, #764ba2)' })}
      ${Components.colorPicker('cse-text', scheme.text, { label: 'Text' })}
      ${Components.colorPicker('cse-solidButtonBackground', scheme.solidButtonBackground, { label: 'Solid button background' })}
      ${Components.colorPicker('cse-solidButtonLabel', scheme.solidButtonLabel, { label: 'Solid button label' })}
      ${Components.colorPicker('cse-outlineButton', scheme.outlineButton, { label: 'Outline button' })}
      ${Components.colorPicker('cse-shadow', scheme.shadow, { label: 'Shadow' })}
    </div>`;

    Components.showModal('Edit color scheme: ' + scheme.name, bodyHtml,
      `<button class="btn btn-secondary" data-modal-cancel>Cancel</button>
       <button class="btn btn-primary" data-modal-save>Save</button>`,
      {
        onOpen: () => {
          const overlay = document.getElementById('modalOverlay');
          overlay.querySelector('[data-modal-cancel]').onclick = () => Components.closeModal();
          overlay.querySelector('[data-modal-save]').onclick = () => {
            const getVal = (id) => document.getElementById(id) ? document.getElementById(id).value : '';
            AppState.updateColorScheme(schemeId, {
              name: getVal('cse-name'),
              background: getVal('cse-background'),
              backgroundGradient: getVal('cse-backgroundGradient'),
              text: getVal('cse-text'),
              solidButtonBackground: getVal('cse-solidButtonBackground'),
              solidButtonLabel: getVal('cse-solidButtonLabel'),
              outlineButton: getVal('cse-outlineButton'),
              shadow: getVal('cse-shadow')
            });
            Components.closeModal();
          };
        }
      }
    );
  }

  // ── Utility ─────────────────────────────────────────────────
  function debounce(fn, ms) {
    let timer;
    return function(...args) {
      clearTimeout(timer);
      timer = setTimeout(() => fn.apply(this, args), ms);
    };
  }

  // ── SSE Connection ──────────────────────────────────────────
  function connectSSE() {
    const es = new EventSource('/api/events');
    es.onmessage = (event) => {
      if (event.data === 'reset') {
        AppState.resetToSeedData();
      }
    };
    es.onerror = () => {
      // Reconnect handled automatically by EventSource
    };
  }

  // ── Initialize ──────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    // Subscribe to state changes
    AppState.subscribe(() => render());

    // Sidebar tab switching
    tabSections.addEventListener('click', () => {
      AppState.sidebarView = 'sections';
      AppState.themeSettingsCategory = null;
      render();
    });
    tabThemeSettings.addEventListener('click', () => {
      AppState.sidebarView = 'themeSettings';
      AppState.selectedSectionId = null;
      AppState.selectedBlockId = null;
      render();
    });

    // Menu bar: template selector
    templateSelector.addEventListener('change', (e) => {
      if (e.detail && e.detail.value) {
        AppState.currentTemplate = e.detail.value;
        AppState.selectedSectionId = null;
        AppState.selectedBlockId = null;
        render();
      }
    });

    // Menu bar: buttons
    btnUndo.addEventListener('click', () => AppState.undo());
    btnRedo.addEventListener('click', () => AppState.redo());
    btnSave.addEventListener('click', () => {
      AppState.save();
      Components.showToast('Theme saved successfully', 'success');
    });

    btnInspector.addEventListener('click', () => {
      AppState.previewInspectorActive = !AppState.previewInspectorActive;
      render();
    });

    btnDesktop.addEventListener('click', () => { AppState.screenSize = 'desktop'; render(); });
    btnMobile.addEventListener('click', () => { AppState.screenSize = 'mobile'; render(); });
    btnFullscreen.addEventListener('click', () => { AppState.screenSize = 'fullscreen'; render(); });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'z' && !e.shiftKey) {
        e.preventDefault();
        AppState.undo();
      }
      if ((e.ctrlKey || e.metaKey) && (e.key === 'y' || (e.key === 'z' && e.shiftKey))) {
        e.preventDefault();
        AppState.redo();
      }
      if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        AppState.save();
        Components.showToast('Theme saved successfully', 'success');
      }
    });

    // Custom dropdown event delegation for settings panel
    settingsPanel.addEventListener('change', (e) => {
      const dropdown = e.target.closest('.custom-dropdown');
      if (dropdown && e.detail && e.detail.value !== undefined) {
        applySettingValue(dropdown.id, e.detail.value);
      }
    });

    // Initial push state to server
    AppState._pushStateToServer(AppState._getPersistable());

    // Connect to SSE
    connectSSE();

    // Initial render
    render();
  });

})();

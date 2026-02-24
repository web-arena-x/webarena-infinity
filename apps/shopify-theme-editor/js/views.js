/* ================================================================
   Shopify Theme Editor — View Renderers
   ================================================================ */

const Views = {

  // ── Sidebar: Sections Tab ───────────────────────────────────
  renderSectionsTab() {
    const templateId = AppState.currentTemplate;
    const headerSections = AppState.getSectionsByGroup(templateId, 'header');
    const templateSections = AppState.getSectionsByGroup(templateId, 'template');
    const footerSections = AppState.getSectionsByGroup(templateId, 'footer');

    let html = '';

    // Header group
    html += `<div class="section-group" data-group="header">
      <div class="section-group-header">
        <span class="section-group-label">Header</span>
      </div>
      <div class="section-group-items">`;
    headerSections.forEach(s => { html += Components.sectionTreeItem(s, AppState.selectedSectionId === s.id); });
    html += `</div></div>`;

    // Template group
    html += `<div class="section-group" data-group="template">
      <div class="section-group-header">
        <span class="section-group-label">Template</span>
      </div>
      <div class="section-group-items">`;
    templateSections.forEach(s => { html += Components.sectionTreeItem(s, AppState.selectedSectionId === s.id); });
    html += `</div>
      <button class="add-section-btn" data-add-section="template">+ Add section</button>
    </div>`;

    // Footer group
    html += `<div class="section-group" data-group="footer">
      <div class="section-group-header">
        <span class="section-group-label">Footer</span>
      </div>
      <div class="section-group-items">`;
    footerSections.forEach(s => { html += Components.sectionTreeItem(s, AppState.selectedSectionId === s.id); });
    html += `</div></div>`;

    return html;
  },

  // ── Sidebar: Theme Settings Tab ─────────────────────────────
  renderThemeSettingsTab() {
    const categories = [
      { key: 'logo', label: 'Logo' },
      { key: 'colors', label: 'Colors' },
      { key: 'typography', label: 'Typography' },
      { key: 'layout', label: 'Layout' },
      { key: 'animations', label: 'Animations' },
      { key: 'buttons', label: 'Buttons' },
      { key: 'variantPills', label: 'Variant pills' },
      { key: 'inputs', label: 'Inputs' },
      { key: 'productCards', label: 'Product cards' },
      { key: 'collectionCards', label: 'Collection cards' },
      { key: 'blogCards', label: 'Blog cards' },
      { key: 'contentContainers', label: 'Content containers' },
      { key: 'media', label: 'Media' },
      { key: 'dropdownsAndPopups', label: 'Dropdowns and pop-ups' },
      { key: 'drawers', label: 'Drawers' },
      { key: 'badges', label: 'Badges' },
      { key: 'brandInformation', label: 'Brand information' },
      { key: 'socialMedia', label: 'Social media' },
      { key: 'searchBehavior', label: 'Search behavior' },
      { key: 'currencyFormat', label: 'Currency format' },
      { key: 'cart', label: 'Cart' },
      { key: 'customCSS', label: 'Custom CSS' },
      { key: 'activeThemeStyle', label: 'Theme style' }
    ];

    return `<div class="theme-settings-list">
      ${categories.map(c =>
        `<div class="theme-settings-item${AppState.themeSettingsCategory === c.key ? ' active' : ''}" data-theme-category="${c.key}">
          ${Components.escapeHtml(c.label)}
        </div>`
      ).join('')}
    </div>`;
  },

  // ── Settings Panel ──────────────────────────────────────────
  renderSettingsPanel() {
    // Theme settings category
    if (AppState.sidebarView === 'themeSettings' && AppState.themeSettingsCategory) {
      return this.renderThemeSettingsPanel(AppState.themeSettingsCategory);
    }

    // Block settings
    if (AppState.selectedBlockId) {
      return this.renderBlockSettings(AppState.selectedBlockId);
    }

    // Section settings
    if (AppState.selectedSectionId) {
      return this.renderSectionSettings(AppState.selectedSectionId);
    }

    return '<div class="settings-empty"><p>Select a section, block, or theme setting to edit.</p></div>';
  },

  // ── Theme Settings Panels ───────────────────────────────────
  renderThemeSettingsPanel(category) {
    const ts = AppState.themeSettings;
    let html = '';

    switch (category) {
      case 'logo':
        html = `<div class="settings-panel" data-settings-for="logo">
          <h3>Logo</h3>
          ${Components.textInput('logo-altText', ts.logo.altText, { label: 'Logo alt text', placeholder: 'Describe your logo' })}
          ${Components.rangeSlider('logo-desktopLogoWidth', ts.logo.desktopLogoWidth, 50, 300, { label: 'Desktop logo width', unit: 'px' })}
          ${Components.textInput('logo-faviconAltText', ts.logo.faviconAltText, { label: 'Favicon alt text' })}
        </div>`;
        break;

      case 'colors':
        html = `<div class="settings-panel" data-settings-for="colors">
          <h3>Colors</h3>
          <div class="color-schemes-list">
            ${ts.colors.schemes.map(s => `
              <div class="color-scheme-entry" data-scheme-id="${s.id}">
                <div class="color-scheme-header">
                  <span class="color-scheme-name">${Components.escapeHtml(s.name)}</span>
                  <button class="btn-icon" data-edit-scheme="${s.id}" title="Edit">&#9998;</button>
                  <button class="btn-icon btn-danger-icon" data-remove-scheme="${s.id}" title="Remove">&times;</button>
                </div>
                <div class="color-scheme-swatches">
                  <div class="mini-swatch" style="background:${Components.escapeAttr(s.background)}" title="Background"></div>
                  <div class="mini-swatch" style="background:${Components.escapeAttr(s.text)}" title="Text"></div>
                  <div class="mini-swatch" style="background:${Components.escapeAttr(s.solidButtonBackground)}" title="Button"></div>
                </div>
              </div>
            `).join('')}
          </div>
          <button class="btn btn-secondary" id="addColorSchemeBtn">+ Add color scheme</button>
        </div>`;
        break;

      case 'typography':
        html = `<div class="settings-panel" data-settings-for="typography">
          <h3>Typography</h3>
          ${Components.dropdown('typo-headingFont',
            FONT_LIBRARY.map(f => ({ value: f, label: f })),
            ts.typography.headingFont,
            { label: 'Heading font', searchable: true }
          )}
          <label class="field-label">Heading font</label>
          ${Components.rangeSlider('typo-headingFontSizeScale', ts.typography.headingFontSizeScale, 100, 150, { label: 'Font size scale', unit: '%', step: 5 })}
          ${Components.dropdown('typo-bodyFont',
            FONT_LIBRARY.map(f => ({ value: f, label: f })),
            ts.typography.bodyFont,
            { label: 'Body font', searchable: true }
          )}
          <label class="field-label">Body font</label>
          ${Components.rangeSlider('typo-bodyFontSizeScale', ts.typography.bodyFontSizeScale, 100, 150, { label: 'Body font size scale', unit: '%', step: 5 })}
        </div>`;
        break;

      case 'layout':
        html = `<div class="settings-panel" data-settings-for="layout">
          <h3>Layout</h3>
          ${Components.rangeSlider('layout-pageWidth', ts.layout.pageWidth, 1000, 1600, { label: 'Page width', unit: 'px' })}
          ${Components.rangeSlider('layout-sectionSpacing', ts.layout.sectionSpacing, 0, 100, { label: 'Section spacing', unit: 'px' })}
          ${Components.rangeSlider('layout-gridHorizontalSpace', ts.layout.gridHorizontalSpace, 0, 40, { label: 'Grid horizontal space', unit: 'px' })}
          ${Components.rangeSlider('layout-gridVerticalSpace', ts.layout.gridVerticalSpace, 0, 40, { label: 'Grid vertical space', unit: 'px' })}
        </div>`;
        break;

      case 'animations':
        html = `<div class="settings-panel" data-settings-for="animations">
          <h3>Animations</h3>
          ${Components.toggleSwitch('anim-revealSectionsOnScroll', ts.animations.revealSectionsOnScroll, { label: 'Reveal sections on scroll' })}
          ${Components.dropdown('anim-hoverEffect',
            [{ value: 'None', label: 'None' }, { value: 'Vertical lift', label: 'Vertical lift' }, { value: '3D lift', label: '3D lift' }],
            ts.animations.hoverEffect
          )}
          <label class="field-label">Hover effect</label>
        </div>`;
        break;

      case 'buttons':
        html = `<div class="settings-panel" data-settings-for="buttons"><h3>Buttons</h3>
          ${Components.rangeSlider('btn-borderRadius', ts.buttons.borderRadius, 0, 40, { label: 'Border radius', unit: 'px' })}
          ${Components.dropdown('btn-shadow', [{value:'None',label:'None'},{value:'Small',label:'Small'},{value:'Medium',label:'Medium'},{value:'Large',label:'Large'}], ts.buttons.shadow)}
          <label class="field-label">Shadow</label>
          ${Components.dropdown('btn-border', [{value:'None',label:'None'},{value:'Outline',label:'Outline'}], ts.buttons.border)}
          <label class="field-label">Border</label>
        </div>`;
        break;

      case 'variantPills':
        html = `<div class="settings-panel" data-settings-for="variantPills"><h3>Variant pills</h3>
          ${Components.dropdown('vp-shape', [{value:'Rectangle',label:'Rectangle'},{value:'Pill',label:'Pill'}], ts.variantPills.shape)}
          <label class="field-label">Shape</label>
          ${Components.dropdown('vp-border', [{value:'None',label:'None'},{value:'Outline',label:'Outline'}], ts.variantPills.border)}
          <label class="field-label">Border</label>
        </div>`;
        break;

      case 'inputs':
        html = `<div class="settings-panel" data-settings-for="inputs"><h3>Inputs</h3>
          ${Components.dropdown('inp-shape', [{value:'Rectangle',label:'Rectangle'},{value:'Pill',label:'Pill'}], ts.inputs.shape)}
          <label class="field-label">Shape</label>
          ${Components.dropdown('inp-border', [{value:'None',label:'None'},{value:'Outline',label:'Outline'}], ts.inputs.border)}
          <label class="field-label">Border</label>
        </div>`;
        break;

      case 'productCards':
        html = `<div class="settings-panel" data-settings-for="productCards"><h3>Product cards</h3>
          ${Components.dropdown('pc-style', [{value:'Standard',label:'Standard'},{value:'Card',label:'Card'}], ts.productCards.style)}
          <label class="field-label">Style</label>
          ${Components.dropdown('pc-imageRatio', [{value:'Adapt',label:'Adapt'},{value:'Portrait',label:'Portrait'},{value:'Square',label:'Square'}], ts.productCards.imageRatio)}
          <label class="field-label">Image ratio</label>
          ${Components.toggleSwitch('pc-showSecondImageOnHover', ts.productCards.showSecondImageOnHover, { label: 'Show second image on hover' })}
          ${Components.toggleSwitch('pc-showVendor', ts.productCards.showVendor, { label: 'Show vendor' })}
          ${Components.toggleSwitch('pc-showRating', ts.productCards.showRating, { label: 'Show rating' })}
        </div>`;
        break;

      case 'collectionCards':
        html = `<div class="settings-panel" data-settings-for="collectionCards"><h3>Collection cards</h3>
          ${Components.dropdown('cc-style', [{value:'Standard',label:'Standard'},{value:'Card',label:'Card'}], ts.collectionCards.style)}
          <label class="field-label">Style</label>
          ${Components.dropdown('cc-imageRatio', [{value:'Adapt',label:'Adapt'},{value:'Portrait',label:'Portrait'},{value:'Square',label:'Square'}], ts.collectionCards.imageRatio)}
          <label class="field-label">Image ratio</label>
        </div>`;
        break;

      case 'blogCards':
        html = `<div class="settings-panel" data-settings-for="blogCards"><h3>Blog cards</h3>
          ${Components.dropdown('bc-style', [{value:'Standard',label:'Standard'},{value:'Card',label:'Card'}], ts.blogCards.style)}
          <label class="field-label">Style</label>
          ${Components.toggleSwitch('bc-showDate', ts.blogCards.showDate, { label: 'Show date' })}
          ${Components.toggleSwitch('bc-showAuthor', ts.blogCards.showAuthor, { label: 'Show author' })}
        </div>`;
        break;

      case 'contentContainers':
        html = `<div class="settings-panel" data-settings-for="contentContainers"><h3>Content containers</h3>
          ${Components.rangeSlider('cc2-borderRadius', ts.contentContainers.borderRadius, 0, 40, { label: 'Border radius', unit: 'px' })}
          ${Components.dropdown('cc2-shadow', [{value:'None',label:'None'},{value:'Small',label:'Small'},{value:'Medium',label:'Medium'}], ts.contentContainers.shadow)}
          <label class="field-label">Shadow</label>
        </div>`;
        break;

      case 'media':
        html = `<div class="settings-panel" data-settings-for="media"><h3>Media</h3>
          ${Components.rangeSlider('media-borderRadius', ts.media.borderRadius, 0, 40, { label: 'Border radius', unit: 'px' })}
          ${Components.dropdown('media-shadow', [{value:'None',label:'None'},{value:'Small',label:'Small'},{value:'Medium',label:'Medium'}], ts.media.shadow)}
          <label class="field-label">Shadow</label>
        </div>`;
        break;

      case 'dropdownsAndPopups':
        html = `<div class="settings-panel" data-settings-for="dropdownsAndPopups"><h3>Dropdowns and pop-ups</h3>
          ${Components.rangeSlider('dp-borderRadius', ts.dropdownsAndPopups.borderRadius, 0, 40, { label: 'Border radius', unit: 'px' })}
          ${Components.dropdown('dp-shadow', [{value:'None',label:'None'},{value:'Small',label:'Small'},{value:'Medium',label:'Medium'}], ts.dropdownsAndPopups.shadow)}
          <label class="field-label">Shadow</label>
        </div>`;
        break;

      case 'drawers':
        html = `<div class="settings-panel" data-settings-for="drawers"><h3>Drawers</h3>
          ${Components.rangeSlider('dr-borderRadius', ts.drawers.borderRadius, 0, 40, { label: 'Border radius', unit: 'px' })}
          ${Components.dropdown('dr-shadow', [{value:'None',label:'None'},{value:'Small',label:'Small'},{value:'Medium',label:'Medium'}], ts.drawers.shadow)}
          <label class="field-label">Shadow</label>
        </div>`;
        break;

      case 'badges':
        html = `<div class="settings-panel" data-settings-for="badges"><h3>Badges</h3>
          ${Components.dropdown('badge-salePosition', [{value:'Top left',label:'Top left'},{value:'Top right',label:'Top right'},{value:'Bottom left',label:'Bottom left'},{value:'Bottom right',label:'Bottom right'}], ts.badges.salePosition)}
          <label class="field-label">Sale badge position</label>
          ${Components.dropdown('badge-saleShape', [{value:'Rectangle',label:'Rectangle'},{value:'Circle',label:'Circle'}], ts.badges.saleShape)}
          <label class="field-label">Sale badge shape</label>
          ${Components.colorPicker('badge-saleColor', ts.badges.saleColor, { label: 'Sale badge color' })}
          ${Components.dropdown('badge-soldOutPosition', [{value:'Top left',label:'Top left'},{value:'Top right',label:'Top right'},{value:'Bottom left',label:'Bottom left'},{value:'Bottom right',label:'Bottom right'}], ts.badges.soldOutPosition)}
          <label class="field-label">Sold out badge position</label>
          ${Components.dropdown('badge-soldOutShape', [{value:'Rectangle',label:'Rectangle'},{value:'Circle',label:'Circle'}], ts.badges.soldOutShape)}
          <label class="field-label">Sold out badge shape</label>
        </div>`;
        break;

      case 'brandInformation':
        html = `<div class="settings-panel" data-settings-for="brandInformation"><h3>Brand information</h3>
          ${Components.toggleSwitch('brand-showBrandImage', ts.brandInformation.showBrandImage, { label: 'Show brand image' })}
          ${Components.toggleSwitch('brand-showBrandDescription', ts.brandInformation.showBrandDescription, { label: 'Show brand description' })}
          ${Components.toggleSwitch('brand-showSocialMediaLinks', ts.brandInformation.showSocialMediaLinks, { label: 'Show social media links' })}
        </div>`;
        break;

      case 'socialMedia':
        html = `<div class="settings-panel" data-settings-for="socialMedia"><h3>Social media</h3>
          ${Components.textInput('social-facebook', ts.socialMedia.facebook, { label: 'Facebook', placeholder: 'https://facebook.com/...' })}
          ${Components.textInput('social-instagram', ts.socialMedia.instagram, { label: 'Instagram', placeholder: 'https://instagram.com/...' })}
          ${Components.textInput('social-twitter', ts.socialMedia.twitter, { label: 'Twitter', placeholder: 'https://twitter.com/...' })}
          ${Components.textInput('social-tiktok', ts.socialMedia.tiktok, { label: 'TikTok', placeholder: 'https://tiktok.com/...' })}
          ${Components.textInput('social-snapchat', ts.socialMedia.snapchat, { label: 'Snapchat', placeholder: 'https://snapchat.com/...' })}
          ${Components.textInput('social-pinterest', ts.socialMedia.pinterest, { label: 'Pinterest', placeholder: 'https://pinterest.com/...' })}
          ${Components.textInput('social-tumblr', ts.socialMedia.tumblr, { label: 'Tumblr', placeholder: 'https://tumblr.com/...' })}
          ${Components.textInput('social-youtube', ts.socialMedia.youtube, { label: 'YouTube', placeholder: 'https://youtube.com/...' })}
          ${Components.textInput('social-vimeo', ts.socialMedia.vimeo, { label: 'Vimeo', placeholder: 'https://vimeo.com/...' })}
          ${Components.textInput('social-linkedin', ts.socialMedia.linkedin, { label: 'LinkedIn', placeholder: 'https://linkedin.com/...' })}
        </div>`;
        break;

      case 'searchBehavior':
        html = `<div class="settings-panel" data-settings-for="searchBehavior"><h3>Search behavior</h3>
          ${Components.toggleSwitch('search-enableSuggestions', ts.searchBehavior.enableSuggestions, { label: 'Enable search suggestions' })}
          ${Components.toggleSwitch('search-showVendor', ts.searchBehavior.showVendor, { label: 'Show product vendor' })}
          ${Components.toggleSwitch('search-showPrice', ts.searchBehavior.showPrice, { label: 'Show product price' })}
        </div>`;
        break;

      case 'currencyFormat':
        html = `<div class="settings-panel" data-settings-for="currencyFormat"><h3>Currency format</h3>
          ${Components.toggleSwitch('currency-showCurrencyCodes', ts.currencyFormat.showCurrencyCodes, { label: 'Show currency codes' })}
        </div>`;
        break;

      case 'cart':
        html = `<div class="settings-panel" data-settings-for="cart"><h3>Cart</h3>
          ${Components.dropdown('cart-type', [{value:'Drawer',label:'Drawer'},{value:'Page',label:'Page'},{value:'Popup notification',label:'Popup notification'}], ts.cart.type)}
          <label class="field-label">Cart type</label>
          ${Components.toggleSwitch('cart-showVendor', ts.cart.showVendor, { label: 'Show vendor' })}
          ${Components.toggleSwitch('cart-enableCartNote', ts.cart.enableCartNote, { label: 'Enable cart note' })}
          ${Components.dropdown('cart-drawerCollection',
            [{ value: '', label: 'None' }].concat(AppState.collections.map(c => ({ value: c.title, label: c.title }))),
            ts.cart.drawerCollection,
            { searchable: true }
          )}
          <label class="field-label">Drawer collection</label>
          ${Components.dropdown('cart-drawerColorSchemeId',
            ts.colors.schemes.map(s => ({ value: s.id, label: s.name })),
            ts.cart.drawerColorSchemeId
          )}
          <label class="field-label">Drawer color scheme</label>
        </div>`;
        break;

      case 'customCSS':
        html = `<div class="settings-panel" data-settings-for="customCSS"><h3>Custom CSS</h3>
          ${Components.textInput('custom-css', ts.customCSS, { label: 'Custom CSS code', placeholder: '/* Your custom CSS here */', multiline: true })}
        </div>`;
        break;

      case 'activeThemeStyle':
        html = `<div class="settings-panel" data-settings-for="activeThemeStyle"><h3>Theme style</h3>
          <div class="theme-style-list">
            ${THEME_STYLES.map(s =>
              `<button class="theme-style-option${ts.activeThemeStyle === s.id ? ' active' : ''}" data-apply-style="${s.id}">${Components.escapeHtml(s.name)}</button>`
            ).join('')}
          </div>
        </div>`;
        break;

      default:
        html = `<div class="settings-panel"><h3>${Components.escapeHtml(category)}</h3><p>Settings panel coming soon.</p></div>`;
    }

    return html;
  },

  // ── Section Settings ────────────────────────────────────────
  renderSectionSettings(sectionId) {
    const section = AppState.getSection(sectionId);
    if (!section) return '';

    let fieldsHtml = '';

    // Common section settings
    fieldsHtml += Components.textInput('section-name', section.name, { label: 'Section name' });

    if (section.settings.colorSchemeId !== undefined) {
      fieldsHtml += Components.dropdown('section-colorSchemeId',
        AppState.themeSettings.colors.schemes.map(s => ({ value: s.id, label: s.name })),
        section.settings.colorSchemeId
      );
      fieldsHtml += '<label class="field-label">Color scheme</label>';
    }

    // Type-specific settings
    switch (section.type) {
      case 'slideshow':
        fieldsHtml += Components.toggleSwitch('section-autoPlay', section.settings.autoPlay || false, { label: 'Auto-play' });
        fieldsHtml += Components.rangeSlider('section-slideInterval', section.settings.slideInterval || 5, 1, 10, { label: 'Slide interval', unit: 's' });
        break;
      case 'featured_collection':
        fieldsHtml += Components.textInput('section-title', section.settings.title || '', { label: 'Title' });
        fieldsHtml += Components.dropdown('section-collectionId',
          AppState.collections.map(c => ({ value: String(c.id), label: c.title })),
          String(section.settings.collectionId || '')
        );
        fieldsHtml += '<label class="field-label">Collection</label>';
        fieldsHtml += Components.rangeSlider('section-productsToShow', section.settings.productsToShow || 8, 2, 24, { label: 'Products to show' });
        break;
      case 'image_banner':
        fieldsHtml += Components.dropdown('section-height',
          [{value:'Small',label:'Small'},{value:'Medium',label:'Medium'},{value:'Large',label:'Large'}],
          section.settings.height || 'Medium'
        );
        fieldsHtml += '<label class="field-label">Height</label>';
        break;
      case 'multicolumn':
        fieldsHtml += Components.textInput('section-title', section.settings.title || '', { label: 'Title' });
        fieldsHtml += Components.rangeSlider('section-columnsDesktop', section.settings.columnsDesktop || 3, 1, 6, { label: 'Columns (desktop)' });
        break;
      case 'collection_list':
        fieldsHtml += Components.textInput('section-title', section.settings.title || '', { label: 'Title' });
        fieldsHtml += Components.rangeSlider('section-columnsDesktop', section.settings.columnsDesktop || 4, 1, 6, { label: 'Columns (desktop)' });
        break;
      case 'newsletter':
        fieldsHtml += Components.toggleSwitch('section-fullWidth', section.settings.fullWidth || false, { label: 'Full width' });
        break;
    }

    // Blocks list
    const blocksHtml = section.blocks.sort((a, b) => a.order - b.order).map(block => {
      const bSel = AppState.selectedBlockId === block.id ? ' selected' : '';
      return `<div class="block-list-item${bSel}" data-select-block="${block.id}">
        <span>${Components.escapeHtml(block.name)}</span>
        <div class="block-actions">
          <button class="btn-icon" data-move-block-up="${block.id}" title="Move up">&#9650;</button>
          <button class="btn-icon" data-move-block-down="${block.id}" title="Move down">&#9660;</button>
          <button class="btn-icon" data-duplicate-block="${block.id}" title="Duplicate">&#10697;</button>
          <button class="btn-icon btn-danger-icon" data-remove-block="${block.id}" title="Remove">&times;</button>
        </div>
      </div>`;
    }).join('');

    const addBlockBtn = (BLOCK_TYPES[section.type] && BLOCK_TYPES[section.type].length > 0)
      ? `<button class="btn btn-secondary add-block-btn" data-add-block-to="${section.id}">+ Add block</button>`
      : '';

    return `<div class="settings-panel section-settings" data-settings-for-section="${sectionId}">
      <div class="settings-panel-header">
        <button class="btn-back" data-deselect-section>&larr; Back</button>
        <h3>${Components.escapeHtml(section.name)}</h3>
      </div>
      ${fieldsHtml}
      <div class="section-blocks-area">
        <h4>Blocks</h4>
        ${blocksHtml}
        ${addBlockBtn}
      </div>
      <div class="section-danger-zone">
        <button class="btn btn-danger" data-remove-section="${sectionId}">Remove section</button>
      </div>
    </div>`;
  },

  // ── Block Settings ──────────────────────────────────────────
  renderBlockSettings(blockId) {
    const block = AppState.getBlock(blockId);
    if (!block) return '';

    let fieldsHtml = '';

    switch (block.type) {
      case 'announcement':
        fieldsHtml += Components.textInput('block-text', block.settings.text || '', { label: 'Text' });
        fieldsHtml += Components.textInput('block-link', block.settings.link || '', { label: 'Link' });
        break;
      case 'slide':
        fieldsHtml += Components.textInput('block-heading', block.settings.heading || '', { label: 'Heading' });
        fieldsHtml += Components.textInput('block-subheading', block.settings.subheading || '', { label: 'Subheading' });
        fieldsHtml += Components.textInput('block-buttonLabel', block.settings.buttonLabel || '', { label: 'Button label' });
        fieldsHtml += Components.textInput('block-buttonLink', block.settings.buttonLink || '', { label: 'Button link' });
        break;
      case 'heading':
        fieldsHtml += Components.textInput('block-text', block.settings.text || '', { label: 'Heading text' });
        fieldsHtml += Components.dropdown('block-size',
          [{value:'Small',label:'Small'},{value:'Medium',label:'Medium'},{value:'Large',label:'Large'}],
          block.settings.size || 'Medium'
        );
        fieldsHtml += '<label class="field-label">Size</label>';
        break;
      case 'text':
        fieldsHtml += Components.textInput('block-text', block.settings.text || '', { label: 'Text', multiline: true });
        break;
      case 'button':
        fieldsHtml += Components.textInput('block-label', block.settings.label || '', { label: 'Label' });
        fieldsHtml += Components.textInput('block-link', block.settings.link || '', { label: 'Link' });
        fieldsHtml += Components.dropdown('block-style',
          [{value:'Primary',label:'Primary'},{value:'Secondary',label:'Secondary'}],
          block.settings.style || 'Primary'
        );
        fieldsHtml += '<label class="field-label">Style</label>';
        break;
      case 'column':
        fieldsHtml += Components.textInput('block-title', block.settings.title || '', { label: 'Title' });
        fieldsHtml += Components.textInput('block-text', block.settings.text || '', { label: 'Text', multiline: true });
        fieldsHtml += Components.textInput('block-linkLabel', block.settings.linkLabel || '', { label: 'Link label' });
        fieldsHtml += Components.textInput('block-linkUrl', block.settings.linkUrl || '', { label: 'Link URL' });
        break;
      case 'collection':
        fieldsHtml += Components.dropdown('block-collectionId',
          AppState.collections.map(c => ({ value: String(c.id), label: c.title })),
          String(block.settings.collectionId || '')
        );
        fieldsHtml += '<label class="field-label">Collection</label>';
        break;
      case 'email_form':
        fieldsHtml += Components.textInput('block-buttonLabel', block.settings.buttonLabel || '', { label: 'Button label' });
        fieldsHtml += Components.textInput('block-placeholder', block.settings.placeholder || '', { label: 'Placeholder' });
        break;
      default:
        fieldsHtml += '<p>Edit settings for this block type.</p>';
        break;
    }

    return `<div class="settings-panel block-settings" data-settings-for-block="${blockId}">
      <div class="settings-panel-header">
        <button class="btn-back" data-back-to-section="${block.sectionId}">&larr; Back</button>
        <h3>${Components.escapeHtml(block.name)}</h3>
      </div>
      ${fieldsHtml}
      <div class="section-danger-zone">
        <button class="btn btn-danger" data-remove-block="${blockId}">Remove block</button>
      </div>
    </div>`;
  },

  // ── Preview Window ──────────────────────────────────────────
  renderPreview() {
    const sections = AppState.getSectionsForTemplate(AppState.currentTemplate);
    const inspectorActive = AppState.previewInspectorActive;

    let html = '<div class="preview-sections">';

    sections.forEach(section => {
      const hidden = !section.visible;
      const classes = ['preview-section'];
      if (hidden && !inspectorActive) return; // skip hidden when inspector off
      if (hidden) classes.push('preview-hidden');
      if (AppState.selectedSectionId === section.id) classes.push('preview-selected');
      if (section.group === 'header') classes.push('preview-header');
      if (section.group === 'footer') classes.push('preview-footer');

      const blockNames = section.blocks
        .filter(b => b.visible)
        .sort((a, b) => a.order - b.order)
        .map(b => Components.escapeHtml(b.name))
        .join(', ');

      html += `<div class="${classes.join(' ')}" data-preview-section="${section.id}">
        <div class="preview-section-label">${Components.escapeHtml(section.name)}</div>
        ${blockNames ? `<div class="preview-section-blocks">${blockNames}</div>` : ''}
        ${hidden ? '<div class="preview-hidden-badge">Hidden</div>' : ''}
      </div>`;
    });

    html += '</div>';
    return html;
  }
};

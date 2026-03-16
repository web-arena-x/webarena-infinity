// Figma Text & Typography - Views
const Views = {

    // ---- Sidebar ----
    renderSidebar() {
        const sections = [
            { id: 'layers', label: 'Layers', icon: '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M8 1L1 5l7 4 7-4-7-4z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M1 8l7 4 7-4" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M1 11l7 4 7-4" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>' },
            { id: 'properties', label: 'Typography', icon: '<svg width="16" height="16" viewBox="0 0 16 16"><text x="2" y="13" font-size="14" font-weight="bold" fill="currentColor">T</text></svg>' },
            { id: 'styles', label: 'Text Styles', icon: '<svg width="16" height="16" viewBox="0 0 16 16"><rect x="1" y="1" width="14" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="4" y1="5" x2="12" y2="5" stroke="currentColor" stroke-width="1.5"/><line x1="4" y1="8" x2="10" y2="8" stroke="currentColor" stroke-width="1.5"/><line x1="4" y1="11" x2="8" y2="11" stroke="currentColor" stroke-width="1.5"/></svg>' },
            { id: 'fonts', label: 'Fonts', icon: '<svg width="16" height="16" viewBox="0 0 16 16"><text x="0" y="13" font-size="12" fill="currentColor">Ag</text></svg>' },
            { id: 'settings', label: 'Settings', icon: '<svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="3" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3 3l1.5 1.5M11.5 11.5L13 13M13 3l-1.5 1.5M4.5 11.5L3 13" stroke="currentColor" stroke-width="1.5"/></svg>' }
        ];

        return `
            <div class="sidebar-header">
                <div class="sidebar-logo">
                    <svg width="20" height="20" viewBox="0 0 20 20"><rect width="20" height="20" rx="4" fill="#7B61FF"/><text x="4" y="15" font-size="13" font-weight="bold" fill="white">T</text></svg>
                </div>
                <div class="sidebar-title">
                    <div class="file-name">${AppState.fileInfo ? AppState.fileInfo.name : 'Untitled'}</div>
                    <div class="page-name">${AppState.fileInfo ? AppState.fileInfo.currentPage : ''}</div>
                </div>
            </div>
            <nav class="sidebar-nav">
                ${sections.map(s => `
                    <a class="nav-item ${AppState.currentSection === s.id ? 'active' : ''}"
                       data-action="navigate" data-section="${s.id}">
                        <span class="nav-icon">${s.icon}</span>
                        <span class="nav-label">${s.label}</span>
                    </a>
                `).join('')}
            </nav>
            <div class="sidebar-footer">
                <div class="sidebar-user">
                    <div class="user-avatar" style="background-color: ${AppState.currentUser ? AppState.currentUser.avatarColor : '#999'}">
                        ${AppState.currentUser ? AppState.currentUser.name.split(' ').map(w => w[0]).join('') : 'U'}
                    </div>
                    <div class="user-info">
                        <div class="user-name">${AppState.currentUser ? AppState.currentUser.name : 'User'}</div>
                        <div class="user-role">${AppState.currentUser ? AppState.currentUser.role : ''}</div>
                    </div>
                </div>
            </div>`;
    },

    // ---- Main Content Router ----
    renderContent() {
        switch (AppState.currentSection) {
            case 'layers': return this.renderLayers();
            case 'properties': return this.renderProperties();
            case 'styles': return this.renderStyles();
            case 'fonts': return this.renderFonts();
            case 'settings': return this.renderSettings();
            default: return this.renderLayers();
        }
    },

    // ============================================================
    // Layers Panel
    // ============================================================
    renderLayers() {
        const layers = AppState.getLayersForSearch();
        return `
            <div class="content-panel">
                ${Components.sectionHeader('Text Layers', `${AppState.textLayers.length} layers in this file`)}
                <div class="toolbar">
                    <div class="search-box">
                        <svg class="search-icon" width="14" height="14" viewBox="0 0 14 14"><circle cx="6" cy="6" r="5" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="10" y1="10" x2="13" y2="13" stroke="currentColor" stroke-width="1.5"/></svg>
                        <input type="text" class="search-input" id="layer-search"
                            placeholder="Search layers..." value="${AppState.searchQuery}">
                    </div>
                    <button class="btn btn-primary btn-sm" data-action="createLayer">
                        <svg width="12" height="12" viewBox="0 0 12 12"><line x1="6" y1="0" x2="6" y2="12" stroke="currentColor" stroke-width="2"/><line x1="0" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="2"/></svg>
                        New Text
                    </button>
                </div>
                <div class="layers-list">
                    ${layers.length === 0 ?
                        Components.emptyState(
                            '<svg width="40" height="40" viewBox="0 0 40 40"><text x="8" y="30" font-size="32" fill="var(--text-tertiary)">T</text></svg>',
                            'No text layers',
                            AppState.searchQuery ? 'No layers match your search.' : 'Create a new text layer to get started.'
                        ) :
                        layers.map(layer => this._renderLayerRow(layer)).join('')
                    }
                </div>
            </div>`;
    },

    _renderLayerRow(layer) {
        const isSelected = AppState.selectedLayerId === layer.id;
        const style = AppState.getTextStyle(layer.textStyleId);
        const truncContent = layer.content.length > 50 ? layer.content.substring(0, 50) + '...' : layer.content;
        return `
            <div class="layer-row ${isSelected ? 'selected' : ''} ${!layer.visible ? 'hidden-layer' : ''} ${layer.locked ? 'locked-layer' : ''}"
                 data-action="selectLayer" data-layer-id="${layer.id}">
                <div class="layer-icon">
                    <svg width="14" height="14" viewBox="0 0 14 14"><text x="2" y="12" font-size="12" fill="currentColor">T</text></svg>
                </div>
                <div class="layer-info">
                    <div class="layer-name${isSelected ? ' renameable' : ''}"${isSelected ? ' data-action="renameLayerPrompt"' : ''}>${Components._escapeHtml(layer.name)}</div>
                    <div class="layer-meta">
                        ${layer.fontFamily} ${layer.fontStyle} &middot; ${layer.fontSize}px
                        ${style ? ` &middot; <span class="style-tag">${style.name}</span>` : ''}
                    </div>
                    <div class="layer-preview-text">${Components._escapeHtml(truncContent.replace(/\n/g, ' '))}</div>
                </div>
                <div class="layer-actions">
                    <button class="layer-action-btn" data-action="toggleVisibility" data-layer-id="${layer.id}" title="${layer.visible ? 'Hide' : 'Show'}">
                        ${layer.visible ?
                            '<svg width="14" height="14" viewBox="0 0 14 14"><ellipse cx="7" cy="7" rx="6" ry="4" fill="none" stroke="currentColor" stroke-width="1.2"/><circle cx="7" cy="7" r="2" fill="currentColor"/></svg>' :
                            '<svg width="14" height="14" viewBox="0 0 14 14"><line x1="1" y1="1" x2="13" y2="13" stroke="currentColor" stroke-width="1.5"/><ellipse cx="7" cy="7" rx="6" ry="4" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.4"/></svg>'
                        }
                    </button>
                    <button class="layer-action-btn" data-action="toggleLock" data-layer-id="${layer.id}" title="${layer.locked ? 'Unlock' : 'Lock'}">
                        ${layer.locked ?
                            '<svg width="14" height="14" viewBox="0 0 14 14"><rect x="3" y="6" width="8" height="7" rx="1" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M5 6V4a2 2 0 0 1 4 0v2" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>' :
                            '<svg width="14" height="14" viewBox="0 0 14 14"><rect x="3" y="6" width="8" height="7" rx="1" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M5 6V4a2 2 0 0 1 4 0" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'
                        }
                    </button>
                </div>
            </div>`;
    },

    // ============================================================
    // Typography Properties Panel
    // ============================================================
    renderProperties() {
        const layer = AppState.getSelectedLayer();
        if (!layer) {
            return `
                <div class="content-panel">
                    ${Components.sectionHeader('Typography', 'Text properties and formatting')}
                    ${Components.emptyState(
                        '<svg width="40" height="40" viewBox="0 0 40 40"><text x="8" y="30" font-size="32" fill="var(--text-tertiary)">T</text></svg>',
                        'No layer selected',
                        'Select a text layer from the Layers panel to edit its typography properties.'
                    )}
                </div>`;
        }

        const font = AppState.getFontFamily(layer.fontFamily);
        const hasVariable = font && font.isVariable;
        const tabs = [
            { id: 'basics', label: 'Basics' },
            { id: 'details', label: 'Details' }
        ];
        if (hasVariable) tabs.push({ id: 'variable', label: 'Variable' });

        return `
            <div class="content-panel">
                <div class="panel-header-bar">
                    <h2 class="panel-title">Typography</h2>
                    <div class="selected-layer-name">${Components._escapeHtml(layer.name)}</div>
                </div>

                <div class="type-tabs">
                    ${tabs.map(t => `
                        <button class="type-tab ${AppState.activeTab === t.id ? 'active' : ''}"
                            data-action="switchTab" data-tab="${t.id}">${t.label}</button>
                    `).join('')}
                </div>

                ${AppState.activeTab === 'basics' ? this._renderBasicsTab(layer, font) : ''}
                ${AppState.activeTab === 'details' ? this._renderDetailsTab(layer, font) : ''}
                ${AppState.activeTab === 'variable' && hasVariable ? this._renderVariableTab(layer, font) : ''}

                <div class="preview-section">
                    <div class="preview-header">
                        <h3>Preview</h3>
                    </div>
                    ${Components.textPreview(layer)}
                </div>
            </div>`;
    },

    _renderBasicsTab(layer, font) {
        const style = AppState.getTextStyle(layer.textStyleId);
        const fontStyles = font ? font.styles : ['Regular', 'Bold'];

        return `
            <div class="properties-section">
                ${style ? `
                    <div class="applied-style-banner">
                        <span class="style-indicator"></span>
                        <span class="style-name">${style.name}</span>
                        <button class="btn-text btn-xs" data-action="detachStyle" data-layer-id="${layer.id}">Detach</button>
                    </div>
                ` : `
                    <div class="style-action-row">
                        <button class="btn-text btn-xs" data-action="openCreateStyleModal" data-layer-id="${layer.id}">Create text style</button>
                        <button class="btn-text btn-xs" data-action="openApplyStyleModal" data-layer-id="${layer.id}">Apply style</button>
                    </div>
                `}

                ${Components.propertyRow('Font', `
                    <div class="font-selector" data-action="openFontPicker" data-layer-id="${layer.id}">
                        <span class="font-name">${layer.fontFamily}</span>
                        <svg class="dropdown-arrow" width="10" height="6" viewBox="0 0 10 6"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
                    </div>
                `)}

                ${Components.propertyRow('Style',
                    Components.dropdown('dd-font-style', layer.fontStyle, fontStyles)
                )}

                ${Components.propertyRow('Size',
                    Components.numberInput('input-font-size', layer.fontSize, 1, 1000, 1, 'px')
                )}

                ${Components.propertyRow('Line height', `
                    <div class="compound-input">
                        ${Components.numberInput('input-line-height',
                            layer.lineHeight.value === 'auto' ? 'auto' : layer.lineHeight.value,
                            0, 500, 1, '')}
                        ${Components.dropdown('dd-line-height-unit', layer.lineHeight.unit === 'auto' ? 'px' : layer.lineHeight.unit, LINE_HEIGHT_UNITS, 'unit-dropdown')}
                    </div>
                `)}

                ${Components.propertyRow('Letter spacing', `
                    <div class="compound-input">
                        ${Components.numberInput('input-letter-spacing', layer.letterSpacing.value, -1, 10, 0.01, '')}
                        ${Components.dropdown('dd-letter-spacing-unit', layer.letterSpacing.unit, LETTER_SPACING_UNITS, 'unit-dropdown')}
                    </div>
                `)}

                <div class="property-row">
                    <label class="property-label">Alignment</label>
                    <div class="property-control">
                        ${Components.buttonGroup('bg-h-align', HORIZONTAL_ALIGNMENTS.map(a => ({
                            value: a, label: a.charAt(0).toUpperCase() + a.slice(1), icon: Components.alignIcon(a)
                        })), layer.horizontalAlign)}
                    </div>
                </div>

                ${layer.resizing === 'fixed' ? `
                    <div class="property-row">
                        <label class="property-label">Vertical align</label>
                        <div class="property-control">
                            ${Components.buttonGroup('bg-v-align', VERTICAL_ALIGNMENTS.map(a => ({
                                value: a, label: a.charAt(0).toUpperCase() + a.slice(1), icon: Components.vertAlignIcon(a)
                            })), layer.verticalAlign)}
                        </div>
                    </div>
                ` : ''}

                <div class="property-row">
                    <label class="property-label">Resizing</label>
                    <div class="property-control">
                        ${Components.buttonGroup('bg-resizing', RESIZING_MODES.map(m => ({
                            value: m, label: m.replace('-', ' '), icon: Components.resizingIcon(m)
                        })), layer.resizing)}
                    </div>
                </div>

                ${(layer.resizing === 'fixed' || layer.resizing === 'auto-height') ? `
                    ${Components.propertyRow('Width',
                        Components.numberInput('input-width', layer.width || '', 1, 10000, 1, 'px')
                    )}
                ` : ''}

                ${layer.resizing === 'fixed' ? `
                    ${Components.propertyRow('Height',
                        Components.numberInput('input-height', layer.height || '', 1, 10000, 1, 'px')
                    )}
                ` : ''}

                <div class="property-divider"></div>

                <div class="property-row">
                    <label class="property-label">Decoration</label>
                    <div class="property-control">
                        ${Components.buttonGroup('bg-decoration', [
                            { value: 'none', label: 'None', icon: '<svg width="16" height="14" viewBox="0 0 16 14"><text x="2" y="12" font-size="12" fill="currentColor">Ab</text></svg>' },
                            { value: 'underline', label: 'Underline', icon: '<svg width="16" height="14" viewBox="0 0 16 14"><text x="2" y="10" font-size="10" fill="currentColor">Ab</text><line x1="1" y1="13" x2="15" y2="13" stroke="currentColor" stroke-width="1.5"/></svg>' },
                            { value: 'strikethrough', label: 'Strikethrough', icon: '<svg width="16" height="14" viewBox="0 0 16 14"><text x="2" y="12" font-size="12" fill="currentColor">Ab</text><line x1="0" y1="7" x2="16" y2="7" stroke="currentColor" stroke-width="1.5"/></svg>' }
                        ], layer.textDecoration)}
                    </div>
                </div>

                ${Components.propertyRow('Letter case',
                    Components.dropdown('dd-letter-case', layer.letterCase, LETTER_CASES.map(c => ({
                        value: c, label: c === 'none' ? 'None' : c === 'small-caps' ? 'Small Caps' : c.charAt(0).toUpperCase() + c.slice(1)
                    })))
                )}

                ${Components.propertyRow('Direction',
                    Components.buttonGroup('bg-direction', [
                        { value: 'ltr', label: 'Left to Right', icon: '<svg width="16" height="12" viewBox="0 0 16 12"><line x1="0" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="2"/><path d="M9 2l4 4-4 4" fill="none" stroke="currentColor" stroke-width="2"/></svg>' },
                        { value: 'rtl', label: 'Right to Left', icon: '<svg width="16" height="12" viewBox="0 0 16 12"><line x1="4" y1="6" x2="16" y2="6" stroke="currentColor" stroke-width="2"/><path d="M7 2l-4 4 4 4" fill="none" stroke="currentColor" stroke-width="2"/></svg>' }
                    ], layer.textDirection)
                )}
            </div>`;
    },

    _renderDetailsTab(layer, font) {
        const availableFeatures = font ? font.openTypeFeatures : [];
        const featuresByCategory = {};
        availableFeatures.forEach(f => {
            const info = OPENTYPE_FEATURE_DESCRIPTIONS[f];
            if (!info) return;
            if (!featuresByCategory[info.category]) featuresByCategory[info.category] = [];
            featuresByCategory[info.category].push({ tag: f, ...info });
        });

        return `
            <div class="properties-section">
                <h3 class="subsection-title">Paragraph</h3>

                ${Components.propertyRow('Paragraph spacing',
                    Components.numberInput('input-para-spacing', layer.paragraphSpacing, 0, 200, 1, 'px')
                )}

                ${Components.propertyRow('Paragraph indent',
                    Components.numberInput('input-para-indent', layer.paragraphIndent, 0, 500, 1, 'px')
                )}

                ${Components.toggle('toggle-hanging-punct', layer.hangingPunctuation, 'Hanging punctuation', 'Move opening quotes outside bounding box')}

                <div class="property-divider"></div>

                <h3 class="subsection-title">Lists</h3>

                ${Components.propertyRow('List style',
                    Components.dropdown('dd-list-style', layer.listStyle, LIST_STYLES.map(s => ({
                        value: s, label: s === 'none' ? 'No list' : s.charAt(0).toUpperCase() + s.slice(1)
                    })))
                )}

                ${layer.listStyle !== 'none' ? `
                    ${Components.propertyRow('List spacing',
                        Components.numberInput('input-list-spacing', layer.listSpacing, 0, 100, 1, 'px')
                    )}

                    ${Components.toggle('toggle-hanging-list', layer.hangingList, 'Hanging list', 'Move bullets/numbers outside bounding box')}
                ` : ''}

                <div class="property-divider"></div>

                <h3 class="subsection-title">Truncation</h3>

                ${Components.toggle('toggle-truncation', layer.truncation.enabled, 'Truncate text', 'Show ellipsis when text overflows')}

                ${layer.truncation.enabled ? `
                    ${Components.propertyRow('Max lines',
                        Components.numberInput('input-max-lines', layer.truncation.maxLines || 1, 1, 100, 1, '')
                    )}
                ` : ''}

                <div class="property-divider"></div>

                ${Components.toggle('toggle-vertical-trim', layer.verticalTrim, 'Vertical trim', 'Remove extra space above and below text')}

                <div class="property-divider"></div>

                <h3 class="subsection-title">Links</h3>

                <div class="links-list">
                    ${layer.links.length === 0 ?
                        '<div class="no-links-msg">No links in this text layer.</div>' :
                        layer.links.map(link => `
                            <div class="link-row" data-link-id="${link.id}">
                                <div class="link-info">
                                    <div class="link-text">"${Components._escapeHtml(layer.content.substring(link.startIndex, link.endIndex))}"</div>
                                    <div class="link-url">${Components._escapeHtml(link.url)}</div>
                                </div>
                                <div class="link-actions">
                                    <button class="layer-action-btn" data-action="editLink" data-layer-id="${layer.id}" data-link-id="${link.id}" title="Edit link">
                                        <svg width="12" height="12" viewBox="0 0 12 12"><path d="M8.5 1.5l2 2-7 7H1.5v-2l7-7z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>
                                    </button>
                                    <button class="layer-action-btn" data-action="removeLink" data-layer-id="${layer.id}" data-link-id="${link.id}" title="Remove link">
                                        <svg width="12" height="12" viewBox="0 0 12 12"><line x1="2" y1="2" x2="10" y2="10" stroke="currentColor" stroke-width="1.5"/><line x1="10" y1="2" x2="2" y2="10" stroke="currentColor" stroke-width="1.5"/></svg>
                                    </button>
                                </div>
                            </div>
                        `).join('')
                    }
                    <button class="btn btn-text btn-sm" data-action="openAddLinkModal" data-layer-id="${layer.id}">
                        <svg width="12" height="12" viewBox="0 0 12 12"><line x1="6" y1="0" x2="6" y2="12" stroke="currentColor" stroke-width="2"/><line x1="0" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="2"/></svg>
                        Add link
                    </button>
                </div>

                <div class="property-divider"></div>

                <h3 class="subsection-title">OpenType Features</h3>
                <div class="opentype-features">
                    ${Object.entries(featuresByCategory).map(([category, features]) => `
                        <div class="ot-category">
                            <button class="ot-category-header" data-action="toggleOtCategory" data-category="${category}">
                                <span>${category}</span>
                                <svg class="ot-chevron ${AppState.expandedOpenTypeCategory === category ? 'expanded' : ''}" width="10" height="6" viewBox="0 0 10 6"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
                            </button>
                            ${AppState.expandedOpenTypeCategory === category ? `
                                <div class="ot-features-list">
                                    ${features.map(f => `
                                        <div class="ot-feature-row">
                                            <div class="ot-feature-info">
                                                <span class="ot-feature-name">${f.name}</span>
                                                <span class="ot-feature-tag">${f.tag}</span>
                                            </div>
                                            <div class="toggle-switch ${layer.openTypeFeatures[f.tag] ? 'active' : ''}"
                                                 data-action="toggleOpenType" data-layer-id="${layer.id}" data-feature="${f.tag}">
                                                <div class="toggle-knob"></div>
                                            </div>
                                        </div>
                                    `).join('')}
                                </div>
                            ` : ''}
                        </div>
                    `).join('')}
                    ${Object.keys(featuresByCategory).length === 0 ? '<div class="no-features-msg">No OpenType features available for this font.</div>' : ''}
                </div>
            </div>`;
    },

    _renderVariableTab(layer, font) {
        if (!font || !font.isVariable) return '';
        const axes = font.variableAxes || [];

        return `
            <div class="properties-section">
                <h3 class="subsection-title">Variable Font Axes</h3>
                <p class="section-description">Adjust axes to fine-tune the font appearance. Each axis controls a different aspect of the typeface.</p>
                ${axes.map(axis => {
                    const currentVal = layer.variableAxes[axis.tag] !== undefined ? layer.variableAxes[axis.tag] : axis.default;
                    return `
                        <div class="variable-axis-row">
                            <div class="axis-info">
                                <span class="axis-name">${axis.name}</span>
                                <span class="axis-tag">${axis.tag}</span>
                            </div>
                            <div class="axis-control">
                                ${Components.slider(`slider-${axis.tag}`, currentVal, axis.min, axis.max, axis.tag === 'wght' ? 1 : 0.1)}
                                <div class="axis-range">
                                    <span>${axis.min}</span>
                                    <span>${axis.max}</span>
                                </div>
                            </div>
                        </div>`;
                }).join('')}
            </div>`;
    },

    // ============================================================
    // Text Styles Panel
    // ============================================================
    renderStyles() {
        const styles = AppState.textStyles;
        return `
            <div class="content-panel">
                ${Components.sectionHeader('Text Styles', `${styles.length} styles defined`)}
                <div class="toolbar">
                    <button class="btn btn-primary btn-sm" data-action="openCreateStyleModal">
                        <svg width="12" height="12" viewBox="0 0 12 12"><line x1="6" y1="0" x2="6" y2="12" stroke="currentColor" stroke-width="2"/><line x1="0" y1="6" x2="12" y2="6" stroke="currentColor" stroke-width="2"/></svg>
                        New Style
                    </button>
                </div>
                <div class="styles-list">
                    ${styles.map(style => this._renderStyleCard(style)).join('')}
                </div>
            </div>`;
    },

    _renderStyleCard(style) {
        const usedBy = AppState.textLayers.filter(l => l.textStyleId === style.id).length;
        return `
            <div class="style-card" data-style-id="${style.id}">
                <div class="style-card-preview" style="font-size: ${Math.min(style.fontSize, 28)}px; ${style.letterCase === 'uppercase' ? 'text-transform:uppercase;' : style.letterCase === 'small-caps' ? 'font-variant:small-caps;' : ''} ${style.textDecoration === 'underline' ? 'text-decoration:underline;' : style.textDecoration === 'strikethrough' ? 'text-decoration:line-through;' : ''}">
                    Ag
                </div>
                <div class="style-card-info">
                    <div class="style-card-name">${Components._escapeHtml(style.name)}</div>
                    <div class="style-card-meta">${style.fontFamily} ${style.fontStyle} &middot; ${style.fontSize}px</div>
                    ${style.description ? `<div class="style-card-desc">${Components._escapeHtml(style.description)}</div>` : ''}
                    <div class="style-card-usage">${usedBy} layer${usedBy !== 1 ? 's' : ''} using this style</div>
                </div>
                <div class="style-card-actions">
                    <button class="layer-action-btn" data-action="editStyleModal" data-style-id="${style.id}" title="Edit style">
                        <svg width="14" height="14" viewBox="0 0 14 14"><path d="M10 2l2 2-8 8H2v-2l8-8z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>
                    </button>
                    <button class="layer-action-btn" data-action="deleteStyle" data-style-id="${style.id}" title="Delete style">
                        <svg width="14" height="14" viewBox="0 0 14 14"><path d="M3 4v8h8V4M1 4h12M5 4V2h4v2M6 6v4M8 6v4" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>
                    </button>
                </div>
            </div>`;
    },

    // ============================================================
    // Fonts Panel
    // ============================================================
    renderFonts() {
        const fonts = AppState.getFilteredFonts();
        return `
            <div class="content-panel">
                ${Components.sectionHeader('Font Browser', `Browse and preview available fonts`)}
                <div class="toolbar">
                    <div class="search-box">
                        <svg class="search-icon" width="14" height="14" viewBox="0 0 14 14"><circle cx="6" cy="6" r="5" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="10" y1="10" x2="13" y2="13" stroke="currentColor" stroke-width="1.5"/></svg>
                        <input type="text" class="search-input" id="font-search"
                            placeholder="Search fonts..." value="${AppState.fontSearchQuery}">
                    </div>
                </div>
                <div class="font-filters">
                    ${FONT_FILTERS.map(f => `
                        <button class="filter-btn ${AppState.fontFilter === f.id ? 'active' : ''}"
                            data-action="setFontFilter" data-filter="${f.id}">${f.label}</button>
                    `).join('')}
                </div>
                <div class="font-count">${fonts.length} font${fonts.length !== 1 ? 's' : ''}</div>
                <div class="fonts-list">
                    ${fonts.length === 0 ?
                        Components.emptyState(
                            '<svg width="40" height="40" viewBox="0 0 40 40"><text x="6" y="30" font-size="28" fill="var(--text-tertiary)">Ag</text></svg>',
                            'No fonts found',
                            'Try a different search or filter.'
                        ) :
                        fonts.map(f => this._renderFontCard(f)).join('')
                    }
                </div>
            </div>`;
    },

    _renderFontCard(font) {
        const usedBy = AppState.textLayers.filter(l => l.fontFamily === font.name).length;
        return `
            <div class="font-card" data-font-name="${font.name.replace(/"/g, '&quot;')}">
                <div class="font-card-header">
                    <div class="font-card-name">${font.name}</div>
                    <div class="font-card-badges">
                        ${font.isVariable ? Components.badge('Variable', 'info') : ''}
                        ${font.popular ? Components.badge('Popular', 'success') : ''}
                        ${font.language ? Components.badge(font.language, 'default') : ''}
                        ${font.rtl ? Components.badge('RTL', 'warning') : ''}
                    </div>
                </div>
                <div class="font-card-preview">
                    <span>The quick brown fox jumps over the lazy dog 0123456789</span>
                </div>
                <div class="font-card-meta">
                    <span class="font-category">${font.category}</span>
                    <span class="font-source">${font.source === 'google' ? 'Google Fonts' : font.source === 'installed' ? 'Installed' : font.source}</span>
                    <span class="font-styles-count">${font.styles.length} style${font.styles.length !== 1 ? 's' : ''}</span>
                    ${usedBy > 0 ? `<span class="font-usage">${usedBy} layer${usedBy !== 1 ? 's' : ''}</span>` : ''}
                </div>
                <div class="font-card-styles">
                    ${font.styles.slice(0, 5).map(s => `<span class="font-style-chip">${s}</span>`).join('')}
                    ${font.styles.length > 5 ? `<span class="font-style-chip more">+${font.styles.length - 5}</span>` : ''}
                </div>
                ${font.isVariable && font.variableAxes ? `
                    <div class="font-card-axes">
                        ${font.variableAxes.map(a => `<span class="axis-chip" title="${a.name}: ${a.min}-${a.max}">${a.tag}</span>`).join('')}
                    </div>
                ` : ''}
                ${AppState.selectedLayerId ? `
                    <button class="btn btn-sm btn-subtle font-apply-btn" data-action="applyFont" data-font-name="${font.name.replace(/"/g, '&quot;')}">
                        Apply to layer
                    </button>
                ` : ''}
            </div>`;
    },

    // ============================================================
    // Settings Panel
    // ============================================================
    renderSettings() {
        const prefs = AppState.preferences;
        return `
            <div class="content-panel">
                ${Components.sectionHeader('Settings', 'Configure default text properties and preferences')}

                <div class="settings-group">
                    <h3 class="subsection-title">Smart Features</h3>
                    ${Components.toggle('toggle-smart-quotes', prefs.smartQuotes, 'Smart quotes', 'Convert straight quotes to curly quotes')}
                    ${Components.toggle('toggle-smart-symbols', prefs.smartSymbols, 'Smart symbols', 'Auto-convert character combinations to symbols')}
                    ${prefs.smartSymbols ? `
                        <div class="smart-symbols-table">
                            <div class="symbols-header">
                                <span>Type</span><span>Result</span><span>Name</span>
                            </div>
                            ${SMART_SYMBOLS.map(s => `
                                <div class="symbols-row">
                                    <code>${Components._escapeHtml(s.input)}</code>
                                    <span class="symbol-output">${s.output}</span>
                                    <span class="symbol-name">${s.name}</span>
                                </div>
                            `).join('')}
                        </div>
                    ` : ''}
                </div>

                <div class="property-divider"></div>

                <div class="settings-group">
                    <h3 class="subsection-title">Default Text Properties</h3>

                    ${Components.propertyRow('Font family',
                        Components.dropdown('dd-default-font', prefs.defaultFontFamily,
                            AppState.fontFamilies.map(f => f.name))
                    )}

                    ${Components.propertyRow('Font style',
                        Components.dropdown('dd-default-style', prefs.defaultFontStyle,
                            ['Thin', 'Extra Light', 'Light', 'Regular', 'Medium', 'Semi Bold', 'Bold', 'Extra Bold', 'Black'])
                    )}

                    ${Components.propertyRow('Font size',
                        Components.dropdown('dd-default-size', prefs.defaultFontSize,
                            FONT_SIZE_PRESETS.map(s => ({ value: s, label: s + 'px' })))
                    )}

                    ${Components.propertyRow('Alignment',
                        Components.dropdown('dd-default-align', prefs.defaultHorizontalAlign,
                            HORIZONTAL_ALIGNMENTS.map(a => ({ value: a, label: a.charAt(0).toUpperCase() + a.slice(1) })))
                    )}

                    ${Components.propertyRow('Text direction',
                        Components.dropdown('dd-default-direction', prefs.defaultTextDirection,
                            TEXT_DIRECTIONS.map(d => ({ value: d, label: d === 'ltr' ? 'Left to Right' : 'Right to Left' })))
                    )}
                </div>

                <div class="property-divider"></div>

                <div class="settings-group">
                    <h3 class="subsection-title">Spelling</h3>
                    ${Components.propertyRow('Language',
                        Components.dropdown('dd-spelling-lang', prefs.spellingLanguage, SPELLING_LANGUAGES)
                    )}
                </div>

                <div class="property-divider"></div>

                <div class="settings-group">
                    <h3 class="subsection-title">Canvas</h3>
                    ${Components.toggle('toggle-snap-grid', prefs.snapToGrid, 'Snap to grid')}
                    ${Components.toggle('toggle-font-preview', prefs.showFontPreview, 'Show font preview on hover')}
                    ${Components.propertyRow('Nudge amount',
                        Components.numberInput('input-nudge', prefs.nudgeAmount, 0.1, 100, 0.1, 'px')
                    )}
                    ${Components.propertyRow('Big nudge amount',
                        Components.numberInput('input-big-nudge', prefs.bigNudgeAmount, 1, 100, 1, 'px')
                    )}
                </div>

                <div class="property-divider"></div>

                <div class="settings-group">
                    <h3 class="subsection-title">Recent Fonts</h3>
                    <div class="recent-fonts-list">
                        ${prefs.recentFonts.map((f, i) => `
                            <div class="recent-font-row">
                                <span class="recent-font-num">${i + 1}.</span>
                                <span class="recent-font-name">${f}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>`;
    },

    // ============================================================
    // Modal Rendering
    // ============================================================
    renderModal() {
        if (!AppState.activeModal) return '';

        switch (AppState.activeModal) {
            case 'createLayer':
                return Components.modal('createLayerModal', 'New Text Layer', `
                    <div class="modal-field">
                        <label class="modal-label">Text content</label>
                        <textarea class="modal-textarea" id="modal-layer-content" rows="3" placeholder="Type something..."></textarea>
                    </div>
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-primary" id="confirm-create-layer" data-action="confirmCreateLayer">Create</button>
                `);

            case 'createStyle':
                return Components.modal('createStyleModal', 'Create Text Style', `
                    <div class="modal-field">
                        <label class="modal-label">Style name</label>
                        <input type="text" class="modal-input" id="modal-style-name" placeholder="e.g., Heading/H1" value="">
                    </div>
                    <div class="modal-field">
                        <label class="modal-label">Description</label>
                        <input type="text" class="modal-input" id="modal-style-desc" placeholder="Optional description" value="">
                    </div>
                    ${AppState.modalData && AppState.modalData.layerId ? `
                        <div class="modal-info-box">Properties will be copied from the selected layer.</div>
                    ` : ''}
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-primary" id="confirm-create-style" data-action="confirmCreateStyle">Create</button>
                `);

            case 'editStyle':
                return this._renderEditStyleModal();

            case 'applyStyle':
                return this._renderApplyStyleModal();

            case 'addLink':
                return Components.modal('addLinkModal', 'Add Link', `
                    <div class="modal-field">
                        <label class="modal-label">Start index</label>
                        <input type="number" class="modal-input" id="modal-link-start" placeholder="0" min="0" value="0">
                    </div>
                    <div class="modal-field">
                        <label class="modal-label">End index</label>
                        <input type="number" class="modal-input" id="modal-link-end" placeholder="10" min="1" value="">
                    </div>
                    <div class="modal-field">
                        <label class="modal-label">URL</label>
                        <input type="url" class="modal-input" id="modal-link-url" placeholder="https://example.com" value="">
                    </div>
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-primary" id="confirm-add-link" data-action="confirmAddLink">Add Link</button>
                `);

            case 'editLink':
                const linkData = AppState.modalData;
                return Components.modal('editLinkModal', 'Edit Link', `
                    <div class="modal-field">
                        <label class="modal-label">URL</label>
                        <input type="url" class="modal-input" id="modal-edit-link-url"
                            value="${linkData ? linkData.url.replace(/"/g, '&quot;') : ''}">
                    </div>
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-primary" data-action="confirmEditLink">Save</button>
                `);

            case 'fontPicker':
                return this._renderFontPickerModal();

            case 'renameLayer':
                const rl = AppState.getSelectedLayer();
                return Components.modal('renameLayerModal', 'Rename Layer', `
                    <div class="modal-field">
                        <label class="modal-label">Layer name</label>
                        <input type="text" class="modal-input" id="modal-layer-name"
                            value="${rl ? rl.name.replace(/"/g, '&quot;') : ''}">
                    </div>
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-primary" data-action="confirmRenameLayer">Rename</button>
                `);

            case 'deleteLayer':
                return Components.modal('deleteLayerModal', 'Delete Layer', `
                    <p>Are you sure you want to delete this text layer? This action cannot be undone.</p>
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-danger" data-action="confirmDeleteLayer">Delete</button>
                `);

            case 'deleteStyle':
                return Components.modal('deleteStyleModal', 'Delete Text Style', `
                    <p>Are you sure you want to delete this text style? Layers using this style will be detached.</p>
                `, `
                    <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
                    <button class="btn btn-danger" data-action="confirmDeleteStyle">Delete</button>
                `);

            default:
                return '';
        }
    },

    _renderEditStyleModal() {
        const style = AppState.modalData ? AppState.textStyles.find(s => s.id === AppState.modalData.styleId) : null;
        if (!style) return '';

        const font = AppState.getFontFamily(style.fontFamily);
        const fontStyles = font ? font.styles : ['Regular', 'Bold'];

        return Components.modal('editStyleModal', 'Edit Text Style', `
            <div class="modal-field">
                <label class="modal-label">Name</label>
                <input type="text" class="modal-input" id="modal-edit-style-name"
                    value="${style.name.replace(/"/g, '&quot;')}">
            </div>
            <div class="modal-field">
                <label class="modal-label">Description</label>
                <input type="text" class="modal-input" id="modal-edit-style-desc"
                    value="${(style.description || '').replace(/"/g, '&quot;')}">
            </div>
            <div class="modal-field">
                <label class="modal-label">Font family</label>
                ${Components.dropdown('dd-edit-style-font', style.fontFamily,
                    AppState.fontFamilies.map(f => f.name))}
            </div>
            <div class="modal-field">
                <label class="modal-label">Font style</label>
                ${Components.dropdown('dd-edit-style-weight', style.fontStyle, fontStyles)}
            </div>
            <div class="modal-field">
                <label class="modal-label">Font size</label>
                <input type="number" class="modal-input" id="modal-edit-style-size"
                    value="${style.fontSize}" min="1" max="1000">
            </div>
            <div class="modal-field">
                <label class="modal-label">Line height</label>
                <div class="compound-input">
                    <input type="number" class="modal-input" id="modal-edit-style-line-height"
                        value="${style.lineHeight.value === 'auto' ? '' : style.lineHeight.value}" min="0" max="500" step="1">
                    ${Components.dropdown('dd-edit-style-lh-unit', style.lineHeight.unit === 'auto' ? 'px' : style.lineHeight.unit, LINE_HEIGHT_UNITS, 'unit-dropdown')}
                </div>
            </div>
            <div class="modal-field">
                <label class="modal-label">Letter case</label>
                ${Components.dropdown('dd-edit-style-case', style.letterCase,
                    LETTER_CASES.map(c => ({ value: c, label: c === 'none' ? 'None' : c === 'small-caps' ? 'Small Caps' : c.charAt(0).toUpperCase() + c.slice(1) })))}
            </div>
            <div class="modal-field">
                <label class="modal-label">Decoration</label>
                ${Components.dropdown('dd-edit-style-decoration', style.textDecoration,
                    TEXT_DECORATIONS.map(d => ({ value: d, label: d.charAt(0).toUpperCase() + d.slice(1) })))}
            </div>
        `, `
            <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
            <button class="btn btn-primary" data-action="confirmEditStyle">Save Changes</button>
        `, 'modal-wide');
    },

    _renderApplyStyleModal() {
        const styles = AppState.textStyles;
        return Components.modal('applyStyleModal', 'Apply Text Style', `
            <div class="style-picker-list">
                ${styles.map(s => `
                    <div class="style-picker-item" data-action="confirmApplyStyle"
                         data-style-id="${s.id}" data-layer-id="${AppState.modalData ? AppState.modalData.layerId : ''}">
                        <div class="style-picker-preview" style="font-size: ${Math.min(s.fontSize, 20)}px;">Ag</div>
                        <div class="style-picker-info">
                            <div class="style-picker-name">${s.name}</div>
                            <div class="style-picker-meta">${s.fontFamily} ${s.fontStyle} ${s.fontSize}px</div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `, `
            <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
        `);
    },

    _renderFontPickerModal() {
        const fonts = AppState.getFilteredFonts();
        return Components.modal('fontPickerModal', 'Choose Font', `
            <div class="font-picker-search">
                <input type="text" class="modal-input" id="font-picker-search"
                    placeholder="Search fonts..." value="${AppState.fontSearchQuery}">
            </div>
            <div class="font-picker-filters">
                ${FONT_FILTERS.map(f => `
                    <button class="filter-chip ${AppState.fontFilter === f.id ? 'active' : ''}"
                        data-action="setFontFilter" data-filter="${f.id}">${f.label}</button>
                `).join('')}
            </div>
            <div class="font-picker-list">
                ${fonts.map(f => `
                    <div class="font-picker-item" data-action="selectFontFromPicker"
                         data-font-name="${f.name.replace(/"/g, '&quot;')}">
                        <div class="font-picker-name">${f.name}</div>
                        <div class="font-picker-preview">The quick brown fox</div>
                        <div class="font-picker-meta">
                            ${f.isVariable ? '<span class="badge badge-info badge-sm">Variable</span>' : ''}
                            <span>${f.styles.length} styles</span>
                        </div>
                    </div>
                `).join('')}
            </div>
        `, `
            <button class="btn btn-secondary" data-action="closeModal">Cancel</button>
        `, 'modal-tall');
    }
};

// ============================================================
// views.js — View renderers for Clio Matters (CLM) app
// All functions return HTML strings. Read from AppState, use
// Components for reusable rendering helpers. No native OS UI.
// ============================================================
/* eslint-disable */

const Views = {

    // ============================================================
    // 1. SIDEBAR
    // ============================================================

    renderSidebar() {
        const view = AppState.currentView;
        const collapsed = App._sidebarCollapsed || false;
        const cls = collapsed ? 'sidebar collapsed' : 'sidebar';

        const navItems = [
            { route: '#/matters', icon: '&#9776;', label: 'Matters', viewMatch: ['matters-list', 'matter-form', 'matter-dashboard'] },
            { route: '#/stages', icon: '&#9638;', label: 'Stages', viewMatch: ['stages'] },
            { route: '#/settings', icon: '&#9881;', label: 'Settings', viewMatch: ['settings'] },
            { route: '#/recovery-bin', icon: '&#128465;', label: 'Recovery Bin', viewMatch: ['recovery-bin'] }
        ];

        let navHtml = '';
        navItems.forEach(item => {
            const active = item.viewMatch.includes(view) ? ' active' : '';
            navHtml += `
                <div class="nav-item${active}" data-route="${item.route}">
                    <span class="nav-item-icon">${item.icon}</span>
                    ${collapsed ? '' : `<span class="nav-item-label">${item.label}</span>`}
                </div>
            `;
        });

        return `
            <div class="${cls}">
                <div class="sidebar-logo">
                    <div class="logo-text">${collapsed ? 'CLM' : 'Meridian Law Group'}</div>
                </div>
                <nav class="sidebar-nav">
                    ${navHtml}
                </nav>
                <div class="sidebar-footer">
                    <button class="btn btn-icon sidebar-collapse-btn" data-action="toggle-sidebar" title="${collapsed ? 'Expand' : 'Collapse'}">
                        ${collapsed ? '&#9654;' : '&#9664;'}
                    </button>
                </div>
            </div>
        `;
    },

    // ============================================================
    // 2. MATTERS LIST VIEW
    // ============================================================

    renderMattersListView() {
        const { matters, totalCount, totalPages } = AppState.getFilteredMatters();
        const allMatters = AppState.matters;
        const openCount = allMatters.filter(m => m.status === 'open').length;
        const pendingCount = allMatters.filter(m => m.status === 'pending').length;
        const closedCount = allMatters.filter(m => m.status === 'closed').length;
        const allCount = allMatters.length;

        // Tab bar
        const tabs = [
            { key: 'all', label: 'All', count: allCount },
            { key: 'open', label: 'Open', count: openCount },
            { key: 'pending', label: 'Pending', count: pendingCount },
            { key: 'closed', label: 'Closed', count: closedCount }
        ];

        const tabBarHtml = tabs.map(tab => {
            const active = AppState.statusFilter === tab.key ? ' active' : '';
            return `<button class="tab-btn${active}" data-action="set-status-filter" data-status="${tab.key}">${escapeHtml(tab.label)} <span class="tab-count">(${tab.count})</span></button>`;
        }).join('');

        // Filter dropdowns
        const practiceAreaOptions = [{ value: '', label: 'All Practice Areas' }].concat(
            AppState.practiceAreas.map(pa => ({ value: pa.id, label: pa.name }))
        );
        const attorneyOptions = [{ value: '', label: 'All Attorneys' }].concat(
            AppState.users.filter(u => u.role === 'attorney' || u.role === 'partner').map(u => ({ value: u.id, label: u.name }))
        );
        const billingOptions = [
            { value: '', label: 'All Billing Methods' },
            { value: 'hourly', label: 'Hourly' },
            { value: 'contingency', label: 'Contingency Fee' },
            { value: 'flat_rate', label: 'Flat Rate' }
        ];

        const practiceAreaFilter = Components.renderDropdown(
            'filter-practice-area',
            practiceAreaOptions,
            AppState.filters.practiceAreaId || '',
            'Practice Area'
        );
        const attorneyFilter = Components.renderDropdown(
            'filter-responsible-attorney',
            attorneyOptions,
            AppState.filters.responsibleAttorneyId || '',
            'Responsible Attorney'
        );
        const billingFilter = Components.renderDropdown(
            'filter-billing-method',
            billingOptions,
            AppState.filters.billingMethod || '',
            'Billing Method'
        );

        // Active filter chips
        let chipHtml = '';
        if (AppState.filters.practiceAreaId) {
            const pa = AppState.getPracticeAreaById(AppState.filters.practiceAreaId);
            if (pa) {
                chipHtml += Components.renderTag(pa.name, true, 'data-action="remove-filter" data-filter-key="practiceAreaId"');
            }
        }
        if (AppState.filters.responsibleAttorneyId) {
            const att = AppState.getUserById(AppState.filters.responsibleAttorneyId);
            if (att) {
                chipHtml += Components.renderTag(att.name, true, 'data-action="remove-filter" data-filter-key="responsibleAttorneyId"');
            }
        }
        if (AppState.filters.billingMethod) {
            const labels = { hourly: 'Hourly', contingency: 'Contingency Fee', flat_rate: 'Flat Rate' };
            chipHtml += Components.renderTag(labels[AppState.filters.billingMethod] || AppState.filters.billingMethod, true, 'data-action="remove-filter" data-filter-key="billingMethod"');
        }
        if (AppState.searchQuery) {
            chipHtml += Components.renderTag('Search: ' + AppState.searchQuery, true, 'data-action="clear-search"');
        }
        const chipBar = chipHtml ? `<div class="filter-chips">${chipHtml}</div>` : '';

        // Bulk actions
        const selectedCount = AppState.selectedMatterIds.length;
        const bulkBar = selectedCount > 0 ? `
            <div class="bulk-actions-bar">
                <span class="bulk-count">${selectedCount} selected</span>
                <button class="btn btn-sm btn-secondary" data-action="bulk-close">Close Selected</button>
                <button class="btn btn-sm btn-danger" data-action="bulk-delete">Delete Selected</button>
                <button class="btn btn-sm btn-secondary" data-action="bulk-update-status">Update Status</button>
            </div>
        ` : '';

        // Table
        const columns = [
            {
                key: 'number',
                label: 'Matter #',
                sortable: true,
                width: '120px',
                render: (row) => `<a class="matter-link" data-route="#/matters/${row.id}">${escapeHtml(AppState.formatMatterNumber(row))}</a>`
            },
            {
                key: 'description',
                label: 'Description',
                sortable: true,
                render: (row) => {
                    const desc = row.description || '';
                    return escapeHtml(desc.length > 50 ? desc.substring(0, 50) + '...' : desc);
                }
            },
            {
                key: 'status',
                label: 'Status',
                sortable: true,
                width: '100px',
                render: (row) => Components.renderStatusBadge(row.status)
            },
            {
                key: 'clientId',
                label: 'Client',
                sortable: false,
                render: (row) => {
                    const client = row.clientId ? AppState.getContactById(row.clientId) : null;
                    if (!client) return '<span class="text-muted">--</span>';
                    const name = client.name || ((client.firstName || '') + ' ' + (client.lastName || '')).trim();
                    return `<a class="client-link" data-action="view-contact" data-id="${client.id}">${escapeHtml(name)}</a>`;
                }
            },
            {
                key: 'practiceAreaId',
                label: 'Practice Area',
                sortable: false,
                render: (row) => {
                    if (!row.practiceAreaId) return '<span class="text-muted">--</span>';
                    const pa = AppState.getPracticeAreaById(row.practiceAreaId);
                    return pa ? escapeHtml(pa.name) : '<span class="text-muted">--</span>';
                }
            },
            {
                key: 'responsibleAttorneyId',
                label: 'Responsible Attorney',
                sortable: false,
                render: (row) => {
                    if (!row.responsibleAttorneyId) return '<span class="text-muted">--</span>';
                    const user = AppState.getUserById(row.responsibleAttorneyId);
                    if (!user) return '<span class="text-muted">--</span>';
                    return `<span class="attorney-cell">${Components.renderAvatar(user, 'sm')} <span>${escapeHtml(user.name)}</span></span>`;
                }
            },
            {
                key: 'openDate',
                label: 'Open Date',
                sortable: true,
                width: '110px',
                render: (row) => Components.formatDate(row.openDate)
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '100px',
                render: (row) => `
                    <div class="row-actions">
                        <button class="btn btn-icon btn-xs" data-route="#/matters/${row.id}/edit" title="Edit">&#9998;</button>
                        <button class="btn btn-icon btn-xs" data-action="duplicate-matter" data-id="${row.id}" title="Duplicate">&#10064;</button>
                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-matter" data-id="${row.id}" title="Delete">&#128465;</button>
                    </div>
                `
            }
        ];

        const tableHtml = Components.renderTable(columns, matters, {
            selectable: true,
            selectedIds: AppState.selectedMatterIds,
            emptyMessage: 'No matters found matching your criteria'
        });

        const paginationHtml = Components.renderPagination(AppState.currentPage, totalPages, totalCount);

        return `
            <div class="matters-list-view">
                <div class="view-header">
                    <h1>Matters</h1>
                    <button class="btn btn-primary" data-route="#/matters/new">+ New Matter</button>
                </div>

                <div class="tab-bar">
                    ${tabBarHtml}
                </div>

                <div class="toolbar">
                    ${Components.renderSearchInput(AppState.searchQuery, 'Search matters...')}
                    <div class="toolbar-filters">
                        ${practiceAreaFilter}
                        ${attorneyFilter}
                        ${billingFilter}
                    </div>
                    <button class="btn btn-secondary btn-sm" data-action="export-csv" title="Export CSV">&#128196; Export CSV</button>
                </div>

                ${chipBar}
                ${bulkBar}

                <div class="table-container">
                    ${tableHtml}
                </div>

                ${paginationHtml}
            </div>
        `;
    },

    // ============================================================
    // 3. MATTER FORM VIEW (Create / Edit)
    // ============================================================

    renderMatterFormView(matterId = null) {
        const isEdit = matterId !== null;
        const matter = isEdit ? AppState.getMatterById(matterId) : null;

        if (isEdit && !matter) {
            return Components.renderEmptyState('&#128196;', 'Matter Not Found', 'The requested matter could not be found.', 'Back to Matters', '#/matters');
        }

        const title = isEdit ? `Edit Matter: ${escapeHtml(AppState.formatMatterNumber(matter))}` : 'New Matter';
        const breadcrumbItems = isEdit
            ? [{ label: 'Matters', route: '#/matters' }, { label: AppState.formatMatterNumber(matter), route: `#/matters/${matterId}` }, { label: 'Edit' }]
            : [{ label: 'Matters', route: '#/matters' }, { label: 'New Matter' }];

        // --- Matter Details Section ---
        const statusOptions = [
            { value: 'open', label: 'Open' },
            { value: 'pending', label: 'Pending' },
            { value: 'closed', label: 'Closed' }
        ];
        const contactOptions = AppState.contacts.map(c => {
            const name = c.name || ((c.firstName || '') + ' ' + (c.lastName || '')).trim();
            return { value: c.id, label: name };
        });
        const userOptions = AppState.users.map(u => ({ value: u.id, label: u.name }));
        const practiceAreaOptions = [{ value: '', label: 'None' }].concat(
            AppState.practiceAreas.map(pa => ({ value: pa.id, label: pa.name }))
        );

        const matterDetailsContent = `
            <div class="form-group">
                <label for="matter-description">Description <span class="required">*</span></label>
                <textarea id="matter-description" class="form-control" rows="3" required data-field="description">${isEdit ? escapeHtml(matter.description) : ''}</textarea>
            </div>
            ${isEdit ? `
                <div class="form-group">
                    <label>Status</label>
                    ${Components.renderDropdown('matter-status', statusOptions, matter.status, 'Select status')}
                </div>
            ` : ''}
            <div class="form-group">
                <label>Client <span class="required">*</span></label>
                ${Components.renderDropdown('matter-client', contactOptions, isEdit ? matter.clientId : '', 'Select client...', true)}
            </div>
            <div class="form-group">
                <label>Responsible Attorney</label>
                ${Components.renderDropdown('matter-responsible-attorney', userOptions, isEdit ? matter.responsibleAttorneyId : (AppState.currentUser ? AppState.currentUser.id : ''), 'Select attorney...', true)}
            </div>
            <div class="form-group">
                <label>Originating Attorney</label>
                ${Components.renderDropdown('matter-originating-attorney', userOptions, isEdit ? matter.originatingAttorneyId : '', 'Select attorney...', true)}
            </div>
            <div class="form-group">
                <label>Responsible Staff</label>
                ${Components.renderDropdown('matter-responsible-staff', userOptions, isEdit && matter.responsibleStaffId ? matter.responsibleStaffId : '', 'Select staff...', true)}
            </div>
            <div class="form-group">
                <label for="matter-client-ref">Client Reference Number</label>
                <input type="text" id="matter-client-ref" class="form-control" data-field="clientReferenceNumber" value="${isEdit && matter.clientReferenceNumber ? escapeHtml(matter.clientReferenceNumber) : ''}" />
            </div>
            <div class="form-group">
                <label for="matter-location">Location</label>
                <input type="text" id="matter-location" class="form-control" data-field="location" value="${isEdit && matter.location ? escapeHtml(matter.location) : ''}" />
            </div>
            <div class="form-group">
                <label>Practice Area</label>
                ${Components.renderDropdown('matter-practice-area', practiceAreaOptions, isEdit ? (matter.practiceAreaId || '') : '', 'Select practice area...')}
            </div>
            <div class="form-group">
                <label for="matter-open-date">Open Date</label>
                <input type="text" id="matter-open-date" class="form-control" data-field="openDate" placeholder="YYYY-MM-DD" value="${isEdit ? escapeHtml(matter.openDate || '') : new Date().toISOString().split('T')[0]}" />
            </div>
        `;

        // --- Template Section ---
        const templateOptions = [{ value: '', label: 'None' }].concat(
            AppState.matterTemplates.map(t => ({ value: t.id, label: t.name }))
        );
        const templateContent = `
            <div class="form-group">
                <label>Use Template</label>
                ${Components.renderDropdown('matter-template', templateOptions, '', 'Select template...')}
            </div>
            <button class="btn btn-secondary btn-sm" data-action="apply-template">Apply Template</button>
        `;

        // --- Permissions Section ---
        const permType = isEdit && matter.permissions && matter.permissions.type === 'specific' ? 'specific' : 'everyone';
        const selectedUsers = isEdit && matter.permissions ? (matter.permissions.userIds || []) : [];
        const selectedGroups = isEdit && matter.permissions ? (matter.permissions.groupIds || []) : [];
        const groupOptions = (AppState.groups || []).map(g => ({ value: g.id, label: g.name }));

        const permissionsContent = `
            <div class="form-group">
                <div class="radio-group">
                    <label class="radio-option">
                        <input type="radio" name="permission-type" value="everyone" ${permType === 'everyone' ? 'checked' : ''} data-field="permissionType" />
                        <span class="radio-label">Everyone</span>
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="permission-type" value="specific" ${permType === 'specific' ? 'checked' : ''} data-field="permissionType" />
                        <span class="radio-label">Specific users or groups</span>
                    </label>
                </div>
            </div>
            <div class="permission-specific-fields" style="${permType === 'specific' ? '' : 'display:none'}">
                <div class="form-group">
                    <label>Users</label>
                    ${Components.renderMultiDropdown('matter-perm-users', userOptions, selectedUsers, 'Select users...')}
                </div>
                <div class="form-group">
                    <label>Groups</label>
                    ${Components.renderMultiDropdown('matter-perm-groups', groupOptions, selectedGroups, 'Select groups...')}
                </div>
            </div>
        `;

        // --- Billing Preferences Section ---
        const billingMethod = isEdit ? (matter.billingMethod || 'hourly') : 'hourly';
        const billable = isEdit && matter.billing ? (matter.billing.billable !== false) : true;
        const currencyOptions = (AppState.currencies || []).map(c => ({ value: c.code, label: c.code + ' - ' + c.name }));
        if (currencyOptions.length === 0) {
            currencyOptions.push({ value: 'USD', label: 'USD - US Dollar' });
        }
        const billingMethodOptions = [
            { value: 'hourly', label: 'Hourly' },
            { value: 'contingency', label: 'Contingency Fee' },
            { value: 'flat_rate', label: 'Flat Rate' }
        ];
        const currentCurrency = isEdit && matter.billing && matter.billing.currency ? matter.billing.currency : 'USD';
        const budget = isEdit && matter.billing ? (matter.billing.budget || '') : '';
        const minTrust = isEdit && matter.billing ? (matter.billing.minimumTrustBalance || '') : '';

        let contingencyFields = '';
        if (billingMethod === 'contingency') {
            const feeRecipient = isEdit && matter.billing ? (matter.billing.feeRecipientId || '') : '';
            const feePct = isEdit && matter.billing ? (matter.billing.contingencyPercentage || '') : '';
            contingencyFields = `
                <div class="form-group" id="contingency-fields">
                    <label>Fee Recipient</label>
                    ${Components.renderDropdown('billing-fee-recipient', userOptions, feeRecipient, 'Select recipient...', true)}
                    <label for="billing-contingency-pct" class="mt-2">Contingency Percentage (%)</label>
                    <input type="number" id="billing-contingency-pct" class="form-control" data-field="contingencyPercentage" value="${escapeHtml(String(feePct))}" min="0" max="100" step="0.5" />
                </div>
            `;
        }

        let flatRateFields = '';
        if (billingMethod === 'flat_rate') {
            const feeAmount = isEdit && matter.billing ? (matter.billing.flatRateAmount || '') : '';
            const feeRecipient = isEdit && matter.billing ? (matter.billing.feeRecipientId || '') : '';
            flatRateFields = `
                <div class="form-group" id="flat-rate-fields">
                    <label for="billing-flat-amount">Fee Amount</label>
                    <input type="number" id="billing-flat-amount" class="form-control" data-field="flatRateAmount" value="${escapeHtml(String(feeAmount))}" min="0" step="0.01" />
                    <label class="mt-2">Fee Recipient</label>
                    ${Components.renderDropdown('billing-flat-recipient', userOptions, feeRecipient, 'Select recipient...', true)}
                </div>
            `;
        }

        const billingContent = `
            <div class="form-group">
                ${Components.renderToggle('billing-billable', billable, 'Billable')}
            </div>
            <div class="form-group">
                <label>Billing Method</label>
                ${Components.renderDropdown('billing-method', billingMethodOptions, billingMethod, 'Select method...')}
            </div>
            <div class="form-group">
                <label>Currency</label>
                ${Components.renderDropdown('billing-currency', currencyOptions, currentCurrency, 'Select currency...')}
            </div>
            ${contingencyFields}
            ${flatRateFields}
            <div class="form-group">
                <label for="billing-budget">Budget</label>
                <input type="number" id="billing-budget" class="form-control" data-field="budget" value="${escapeHtml(String(budget))}" min="0" step="0.01" />
            </div>
            <div class="form-group">
                <label for="billing-min-trust">Minimum Trust Balance</label>
                <input type="number" id="billing-min-trust" class="form-control" data-field="minimumTrustBalance" value="${escapeHtml(String(minTrust))}" min="0" step="0.01" />
            </div>
        `;

        // --- Personal Injury Preferences Section ---
        const selectedPA = isEdit && matter.practiceAreaId ? AppState.getPracticeAreaById(matter.practiceAreaId) : null;
        const isPICase = selectedPA && selectedPA.name && selectedPA.name.toLowerCase().includes('personal injury');
        const deductionOrder = isEdit && matter.billing && matter.billing.deductionOrder ? matter.billing.deductionOrder : 'fees_first';

        const piContent = `
            <div class="form-group">
                <div class="radio-group">
                    <label class="radio-option">
                        <input type="radio" name="deduction-order" value="fees_first" ${deductionOrder === 'fees_first' ? 'checked' : ''} data-field="deductionOrder" />
                        <span class="radio-label">Deduct legal fees first, then expenses</span>
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="deduction-order" value="expenses_first" ${deductionOrder === 'expenses_first' ? 'checked' : ''} data-field="deductionOrder" />
                        <span class="radio-label">Deduct expenses first, then legal fees</span>
                    </label>
                </div>
            </div>
        `;

        // --- Related Contacts Section ---
        const relationships = isEdit ? (matter.relationships || []) : [];
        const relationshipTypeOptions = (AppState.relationshipTypes || []).map(rt => ({ value: rt.id || rt.value || rt, label: rt.name || rt.label || rt }));
        let relatedHtml = '';
        relationships.forEach((rel, idx) => {
            const contact = rel.contactId ? AppState.getContactById(rel.contactId) : null;
            const contactName = contact ? (contact.name || ((contact.firstName || '') + ' ' + (contact.lastName || '')).trim()) : 'Unknown';
            const relType = rel.relationship || rel.type || '';
            const isBillRecipient = rel.billRecipient || false;
            relatedHtml += `
                <div class="related-contact-row" data-index="${idx}">
                    <span class="related-contact-name">${escapeHtml(contactName)}</span>
                    <span class="related-contact-type">${escapeHtml(relType)}</span>
                    ${Components.renderCheckbox('bill-recipient-' + idx, isBillRecipient, 'Bill Recipient')}
                    <button class="btn btn-icon btn-xs btn-danger-icon" data-action="remove-related-contact" data-index="${idx}" title="Remove">&#128465;</button>
                </div>
            `;
        });

        const relatedContactsContent = `
            <div class="related-contacts-list">
                ${relatedHtml || '<p class="text-muted">No related contacts added.</p>'}
            </div>
            <div class="add-related-contact-form" id="add-related-contact-form" style="display:none">
                <div class="form-group">
                    <label>Contact</label>
                    ${Components.renderDropdown('new-related-contact', contactOptions, '', 'Select contact...', true)}
                </div>
                <div class="form-group">
                    <label>Relationship</label>
                    ${Components.renderDropdown('new-related-relationship', relationshipTypeOptions, '', 'Select relationship...')}
                </div>
                <div class="form-group">
                    ${Components.renderCheckbox('new-related-bill-recipient', false, 'Bill Recipient')}
                </div>
                <button class="btn btn-sm btn-primary" data-action="save-related-contact">Add</button>
                <button class="btn btn-sm btn-secondary" data-action="cancel-related-contact">Cancel</button>
            </div>
            <button class="btn btn-secondary btn-sm mt-2" data-action="show-add-related-contact">+ Add Related Contact</button>
        `;

        // --- Custom Fields Section ---
        const customFieldDefs = AppState.customFieldDefinitions || [];
        const customFieldValues = isEdit ? (matter.customFields || {}) : {};
        let customFieldsHtml = '';
        if (customFieldDefs.length === 0) {
            customFieldsHtml = '<p class="text-muted">No custom fields defined.</p>';
        } else {
            customFieldDefs.forEach(field => {
                const val = customFieldValues[field.id] || customFieldValues[field.name] || '';
                if (field.type === 'date') {
                    customFieldsHtml += `
                        <div class="form-group">
                            <label for="custom-field-${field.id}">${escapeHtml(field.name)}</label>
                            <input type="text" id="custom-field-${field.id}" class="form-control" data-custom-field="${escapeHtml(field.id)}" placeholder="YYYY-MM-DD" value="${escapeHtml(String(val))}" />
                        </div>
                    `;
                } else if (field.type === 'currency') {
                    customFieldsHtml += `
                        <div class="form-group">
                            <label for="custom-field-${field.id}">${escapeHtml(field.name)}</label>
                            <input type="number" id="custom-field-${field.id}" class="form-control" data-custom-field="${escapeHtml(field.id)}" step="0.01" value="${escapeHtml(String(val))}" />
                        </div>
                    `;
                } else {
                    customFieldsHtml += `
                        <div class="form-group">
                            <label for="custom-field-${field.id}">${escapeHtml(field.name)}</label>
                            <input type="text" id="custom-field-${field.id}" class="form-control" data-custom-field="${escapeHtml(field.id)}" value="${escapeHtml(String(val))}" />
                        </div>
                    `;
                }
            });
        }

        // --- Document Folders Section ---
        const folders = isEdit && matter.folders ? matter.folders : [];
        let foldersHtml = '';
        folders.forEach((folder, idx) => {
            foldersHtml += `
                <div class="folder-row" data-index="${idx}">
                    <span class="folder-name">${escapeHtml(folder.name || '')}</span>
                    <span class="folder-category">${escapeHtml(folder.category || '')}</span>
                    <button class="btn btn-icon btn-xs btn-danger-icon" data-action="remove-document-folder" data-index="${idx}" title="Remove">&#128465;</button>
                </div>
            `;
        });

        const foldersContent = `
            <div class="folders-list">
                ${foldersHtml || '<p class="text-muted">No document folders added.</p>'}
            </div>
            <button class="btn btn-secondary btn-sm mt-2" data-action="add-document-folder">+ Add Folder</button>
        `;

        // --- Notifications Section ---
        const notifRecipients = isEdit && matter.notificationRecipients ? matter.notificationRecipients : [];
        let notifHtml = '';
        notifRecipients.forEach((recipient, idx) => {
            const user = AppState.getUserById(recipient.userId || recipient);
            const userName = user ? user.name : 'Unknown';
            notifHtml += `
                <div class="notification-recipient-row" data-index="${idx}">
                    <span>${escapeHtml(userName)}</span>
                    <button class="btn btn-icon btn-xs btn-danger-icon" data-action="remove-notification-recipient" data-index="${idx}" title="Remove">&#128465;</button>
                </div>
            `;
        });

        const notificationsContent = `
            <div class="notification-recipients-list">
                ${notifHtml || '<p class="text-muted">No notification recipients configured.</p>'}
            </div>
            <button class="btn btn-secondary btn-sm mt-2" data-action="add-notification-recipient">+ Add Recipient</button>
        `;

        // --- Reports Section ---
        const useFirmSettings = isEdit && matter.reports ? (matter.reports.useFirmSettings !== false) : true;
        const origAlloc = isEdit && matter.reports ? (matter.reports.originatingAttorneyAllocation || '') : '';
        const respAlloc = isEdit && matter.reports ? (matter.reports.responsibleAttorneyAllocation || '') : '';

        const reportsContent = `
            <div class="form-group">
                ${Components.renderToggle('reports-use-firm-settings', useFirmSettings, 'Use firm settings')}
            </div>
            <div class="form-group">
                <label for="reports-orig-alloc">Originating Attorney Allocation (%)</label>
                <input type="number" id="reports-orig-alloc" class="form-control" data-field="originatingAttorneyAllocation" value="${escapeHtml(String(origAlloc))}" min="0" max="100" step="1" />
            </div>
            <div class="form-group">
                <label for="reports-resp-alloc">Responsible Attorney Allocation (%)</label>
                <input type="number" id="reports-resp-alloc" class="form-control" data-field="responsibleAttorneyAllocation" value="${escapeHtml(String(respAlloc))}" min="0" max="100" step="1" />
            </div>
        `;

        // Assemble all sections
        const sections = [
            Components.renderFormSection('matter-details', 'Matter Details', matterDetailsContent, true),
            Components.renderFormSection('template', 'Template', templateContent, false),
            Components.renderFormSection('permissions', 'Permissions', permissionsContent, false),
            Components.renderFormSection('billing', 'Billing Preferences', billingContent, true),
            isPICase ? Components.renderFormSection('personal-injury', 'Personal Injury Preferences', piContent, true) : '',
            Components.renderFormSection('related-contacts', 'Related Contacts', relatedContactsContent, false),
            Components.renderFormSection('custom-fields', 'Custom Fields', customFieldsHtml, false),
            Components.renderFormSection('document-folders', 'Document Folders', foldersContent, false),
            Components.renderFormSection('notifications', 'Notifications', notificationsContent, false),
            Components.renderFormSection('reports', 'Reports', reportsContent, false)
        ].filter(Boolean).join('');

        // Form actions
        const formActions = `
            <div class="form-actions">
                <button class="btn btn-primary" data-action="save-matter">Save Matter</button>
                <button class="btn btn-secondary" data-action="save-and-conflict-check">Save and Run Conflict Check</button>
                <button class="btn btn-secondary" data-route="${isEdit ? '#/matters/' + matterId : '#/matters'}">Cancel</button>
                ${isEdit ? `<button class="btn btn-danger" data-action="delete-matter" data-id="${matterId}">Delete Matter</button>` : ''}
            </div>
        `;

        return `
            <div class="matter-form-view">
                ${Components.renderBreadcrumb(breadcrumbItems)}
                <div class="view-header">
                    <h1>${title}</h1>
                </div>
                <form class="matter-form" id="matter-form" data-matter-id="${isEdit ? matterId : ''}">
                    ${sections}
                    ${formActions}
                </form>
            </div>
        `;
    },

    // ============================================================
    // 4. MATTER DASHBOARD VIEW
    // ============================================================

    renderMatterDashboardView(matterId) {
        const matter = AppState.getMatterById(matterId);
        if (!matter) {
            return Components.renderEmptyState('&#128196;', 'Matter Not Found', 'The requested matter could not be found.', 'Back to Matters', '#/matters');
        }

        const breadcrumbItems = [
            { label: 'Matters', route: '#/matters' },
            { label: AppState.formatMatterNumber(matter) }
        ];

        // Sub-tabs
        const subTabs = ['overview', 'damages', 'medical-records', 'settlement'];
        const subTabLabels = { overview: 'Overview', damages: 'Damages', 'medical-records': 'Medical Records', settlement: 'Settlement' };
        const activeSubTab = AppState.currentSubTab || 'overview';

        const subTabBar = subTabs.map(tab => {
            const active = activeSubTab === tab ? ' active' : '';
            return `<button class="tab-btn${active}" data-action="change-sub-tab" data-tab="${tab}">${subTabLabels[tab]}</button>`;
        }).join('');

        let content = '';
        switch (activeSubTab) {
            case 'overview':
                content = Views._renderOverviewSubTab(matter);
                break;
            case 'damages':
                content = Views._renderDamagesSubTab(matter);
                break;
            case 'medical-records':
                content = Views._renderMedicalRecordsSubTab(matter);
                break;
            case 'settlement':
                content = Views._renderSettlementSubTab(matter);
                break;
            default:
                content = Views._renderOverviewSubTab(matter);
        }

        return `
            <div class="matter-dashboard-view">
                ${Components.renderBreadcrumb(breadcrumbItems)}
                <div class="view-header">
                    <h1>${escapeHtml(matter.description || AppState.formatMatterNumber(matter))}</h1>
                </div>
                <div class="tab-bar sub-tab-bar">
                    ${subTabBar}
                </div>
                <div class="dashboard-content">
                    ${content}
                </div>
            </div>
        `;
    },

    // ---- Overview Sub-tab ----
    _renderOverviewSubTab(matter) {
        const financials = AppState.getMatterFinancials(matter.id);
        const client = matter.clientId ? AppState.getContactById(matter.clientId) : null;
        const responsibleAtty = matter.responsibleAttorneyId ? AppState.getUserById(matter.responsibleAttorneyId) : null;
        const originatingAtty = matter.originatingAttorneyId ? AppState.getUserById(matter.originatingAttorneyId) : null;
        const practiceArea = matter.practiceAreaId ? AppState.getPracticeAreaById(matter.practiceAreaId) : null;
        const activityLog = AppState.getActivityLogForMatter(matter.id);
        const limitedLog = activityLog.slice(0, 20);

        // Stage name
        let stageName = '--';
        if (matter.stageId && practiceArea && practiceArea.stages) {
            const stage = practiceArea.stages.find(s => s.id === matter.stageId);
            if (stage) stageName = stage.name;
        }

        // --- Financial Widget ---
        const trustBalance = matter.billing && matter.billing.trustBalance != null ? matter.billing.trustBalance : 0;
        const budget = matter.billing && matter.billing.budget ? matter.billing.budget : null;
        const totalSpent = financials.workInProgress + financials.outstandingBalance + financials.totalExpenses;

        const financialWidget = `
            <div class="widget financial-widget">
                <h3>Financial Summary</h3>
                <div class="financial-grid">
                    <div class="financial-item">
                        <span class="financial-label">Work in Progress</span>
                        <span class="financial-value">${Components.renderCurrency(financials.workInProgress)}</span>
                    </div>
                    <div class="financial-item">
                        <span class="financial-label">Outstanding Balance</span>
                        <span class="financial-value">${Components.renderCurrency(financials.outstandingBalance)}</span>
                    </div>
                    <div class="financial-item">
                        <span class="financial-label">Trust Balance</span>
                        <span class="financial-value">${Components.renderCurrency(trustBalance)}</span>
                    </div>
                    ${budget ? `
                        <div class="financial-item full-width">
                            ${Components.renderProgressBar(totalSpent, budget, 'Budget')}
                        </div>
                    ` : ''}
                    <div class="financial-item">
                        <span class="financial-label">Total Time</span>
                        <span class="financial-value">${financials.totalTime.toFixed(1)} hrs</span>
                    </div>
                    <div class="financial-item">
                        <span class="financial-label">Total Expenses</span>
                        <span class="financial-value">${Components.renderCurrency(financials.totalExpenses)}</span>
                    </div>
                </div>
                <div class="widget-actions">
                    <button class="btn btn-sm btn-primary" data-action="quick-bill" data-matter-id="${matter.id}">Quick Bill</button>
                    <button class="btn btn-sm btn-secondary" data-action="add-time-entry" data-matter-id="${matter.id}">Add Time</button>
                    <button class="btn btn-sm btn-secondary" data-action="add-expense" data-matter-id="${matter.id}">Add Expense</button>
                </div>
            </div>
        `;

        // --- Timeline Widget ---
        let timelineHtml = '';
        if (limitedLog.length === 0) {
            timelineHtml = '<p class="text-muted">No activity recorded yet.</p>';
        } else {
            timelineHtml = limitedLog.map(entry => {
                const user = entry.userId ? AppState.getUserById(entry.userId) : null;
                const userName = user ? user.name : 'System';
                const actionDesc = Views._formatActivityAction(entry);
                return `
                    <div class="timeline-entry">
                        <div class="timeline-avatar">${Components.renderAvatar(user, 'sm')}</div>
                        <div class="timeline-body">
                            <span class="timeline-user">${escapeHtml(userName)}</span>
                            <span class="timeline-action">${escapeHtml(actionDesc)}</span>
                            <span class="timeline-time">${Components.formatDateTime(entry.timestamp)}</span>
                        </div>
                    </div>
                `;
            }).join('');
        }

        const timelineWidget = `
            <div class="widget timeline-widget">
                <h3>Recent Activity</h3>
                <div class="timeline-list">
                    ${timelineHtml}
                </div>
                ${activityLog.length > 20 ? `<a class="view-all-link" data-action="view-all-activity" data-matter-id="${matter.id}">View All (${activityLog.length})</a>` : ''}
            </div>
        `;

        // --- Status dropdown for inline change ---
        const statusOptions = [
            { value: 'open', label: 'Open' },
            { value: 'pending', label: 'Pending' },
            { value: 'closed', label: 'Closed' }
        ];

        // --- Details Widget ---
        const detailsWidget = `
            <div class="widget details-widget">
                <h3>Matter Details</h3>
                <div class="detail-pairs">
                    <div class="detail-pair">
                        <span class="detail-label">Matter #</span>
                        <span class="detail-value">${escapeHtml(AppState.formatMatterNumber(matter))}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Description</span>
                        <span class="detail-value">${escapeHtml(matter.description || '--')}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Status</span>
                        <span class="detail-value">
                            ${Components.renderStatusBadge(matter.status)}
                            ${Components.renderDropdown('dashboard-status', statusOptions, matter.status, 'Change status')}
                        </span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Stage</span>
                        <span class="detail-value">${escapeHtml(stageName)}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Practice Area</span>
                        <span class="detail-value">${practiceArea ? escapeHtml(practiceArea.name) : '--'}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Responsible Attorney</span>
                        <span class="detail-value">${responsibleAtty ? `${Components.renderAvatar(responsibleAtty, 'sm')} ${escapeHtml(responsibleAtty.name)}` : '--'}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Originating Attorney</span>
                        <span class="detail-value">${originatingAtty ? escapeHtml(originatingAtty.name) : '--'}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Billing Method</span>
                        <span class="detail-value">${escapeHtml(Views._formatBillingMethod(matter.billingMethod))}</span>
                    </div>
                    <div class="detail-pair">
                        <span class="detail-label">Open Date</span>
                        <span class="detail-value">${Components.formatDate(matter.openDate)}</span>
                    </div>
                    ${matter.closedDate ? `
                        <div class="detail-pair">
                            <span class="detail-label">Closed Date</span>
                            <span class="detail-value">${Components.formatDate(matter.closedDate)}</span>
                        </div>
                    ` : ''}
                    ${matter.statuteOfLimitations ? `
                        <div class="detail-pair">
                            <span class="detail-label">Statute of Limitations</span>
                            <span class="detail-value">${Components.formatDate(matter.statuteOfLimitations)}</span>
                        </div>
                    ` : ''}
                </div>
                <div class="widget-actions">
                    <button class="btn btn-sm btn-primary" data-route="#/matters/${matter.id}/edit">Edit Matter</button>
                    <button class="btn btn-sm btn-secondary" data-action="duplicate-matter" data-id="${matter.id}">Duplicate</button>
                </div>
            </div>
        `;

        // --- Contacts Widget ---
        let contactHtml = '';
        if (client) {
            const clientName = client.name || ((client.firstName || '') + ' ' + (client.lastName || '')).trim();
            const address = [client.address, client.city, client.state, client.zip].filter(Boolean).join(', ');
            contactHtml = `
                <div class="contact-card primary-contact">
                    <div class="contact-header">
                        <strong>${escapeHtml(clientName)}</strong>
                        <span class="contact-type-badge">Client</span>
                    </div>
                    <div class="contact-details">
                        ${client.phone ? `<div class="contact-detail"><span class="detail-icon">&#9742;</span> ${escapeHtml(client.phone)}</div>` : ''}
                        ${client.email ? `<div class="contact-detail"><span class="detail-icon">&#9993;</span> <a href="mailto:${escapeHtml(client.email)}" data-action="email-contact" data-email="${escapeHtml(client.email)}">${escapeHtml(client.email)}</a></div>` : ''}
                        ${address ? `<div class="contact-detail"><span class="detail-icon">&#9873;</span> ${escapeHtml(address)} <button class="btn btn-icon btn-xs" data-action="copy-address" data-address="${escapeHtml(address)}" title="Copy">&#128203;</button></div>` : ''}
                    </div>
                    ${client.tags && client.tags.length > 0 ? `
                        <div class="contact-tags">
                            ${client.tags.map(tag => Components.renderTag(tag)).join('')}
                        </div>
                    ` : ''}
                </div>
            `;
        } else {
            contactHtml = '<p class="text-muted">No client assigned.</p>';
        }

        const contactsWidget = `
            <div class="widget contacts-widget">
                <h3>Client</h3>
                ${contactHtml}
            </div>
        `;

        // --- Related Contacts Widget ---
        const relationships = matter.relationships || [];
        const sortOptions = [
            { value: 'name-asc', label: 'Name A-Z' },
            { value: 'name-desc', label: 'Name Z-A' },
            { value: 'list-order', label: 'List order' }
        ];
        let relatedContactsList = '';
        if (relationships.length === 0) {
            relatedContactsList = '<p class="text-muted">No related contacts.</p>';
        } else {
            relatedContactsList = relationships.map((rel, idx) => {
                const contact = rel.contactId ? AppState.getContactById(rel.contactId) : null;
                const contactName = contact ? (contact.name || ((contact.firstName || '') + ' ' + (contact.lastName || '')).trim()) : 'Unknown';
                const relType = rel.relationship || rel.type || '';
                return `
                    <div class="related-contact-card" data-index="${idx}">
                        <div class="related-contact-name">${escapeHtml(contactName)}</div>
                        <div class="related-contact-relationship">${escapeHtml(relType)}</div>
                        ${contact && contact.phone ? `<div class="related-contact-phone">${escapeHtml(contact.phone)}</div>` : ''}
                        ${contact && contact.email ? `<div class="related-contact-email">${escapeHtml(contact.email)}</div>` : ''}
                    </div>
                `;
            }).join('');
        }

        const relatedContactsWidget = `
            <div class="widget related-contacts-widget">
                <div class="widget-header-row">
                    <h3>Related Contacts</h3>
                    ${Components.renderDropdown('related-contacts-sort', sortOptions, 'list-order', 'Sort by')}
                </div>
                <div class="related-contacts-list">
                    ${relatedContactsList}
                </div>
                <button class="btn btn-sm btn-secondary mt-2" data-action="show-add-related-contact">+ Add Related Contact</button>
            </div>
        `;

        // --- Custom Fields Widget ---
        const customFieldDefs = AppState.customFieldDefinitions || [];
        const customFieldValues = matter.customFields || {};
        let customFieldsDisplay = '';
        if (customFieldDefs.length === 0) {
            customFieldsDisplay = '<p class="text-muted">No custom fields defined.</p>';
        } else {
            customFieldsDisplay = customFieldDefs.map(field => {
                const val = customFieldValues[field.id] || customFieldValues[field.name] || '';
                let displayVal = escapeHtml(String(val)) || '--';
                if (field.type === 'date' && val) {
                    displayVal = Components.formatDate(val);
                } else if (field.type === 'currency' && val) {
                    displayVal = Components.renderCurrency(Number(val));
                }
                return `
                    <div class="detail-pair">
                        <span class="detail-label">${escapeHtml(field.name)}</span>
                        <span class="detail-value">${displayVal}</span>
                    </div>
                `;
            }).join('');
        }

        const customFieldsWidget = `
            <div class="widget custom-fields-widget">
                <h3>Custom Fields</h3>
                <div class="detail-pairs">
                    ${customFieldsDisplay}
                </div>
            </div>
        `;

        return `
            <div class="dashboard-grid">
                <div class="dashboard-left">
                    ${financialWidget}
                    ${timelineWidget}
                </div>
                <div class="dashboard-right">
                    ${detailsWidget}
                    ${contactsWidget}
                    ${relatedContactsWidget}
                    ${customFieldsWidget}
                </div>
            </div>
        `;
    },

    // ---- Damages Sub-tab ----
    _renderDamagesSubTab(matter) {
        const damages = AppState.getDamagesForMatter(matter.id);
        const summary = AppState.getDamageSummary(matter.id);

        // Summary cards
        const totalBilled = summary._total || 0;
        const totalPaid = damages.filter(d => d.paid).reduce((s, d) => s + (d.amount || 0), 0);
        const totalSpecial = summary.special || 0;
        const totalGeneral = summary.general || 0;
        const totalOther = summary.other || 0;

        const summaryCards = `
            <div class="summary-cards">
                <div class="summary-card">
                    <div class="summary-card-label">Total Billed Damages</div>
                    <div class="summary-card-value">${Components.renderCurrency(totalBilled)}</div>
                </div>
                <div class="summary-card">
                    <div class="summary-card-label">Total Paid Damages</div>
                    <div class="summary-card-value">${Components.renderCurrency(totalPaid)}</div>
                </div>
                <div class="summary-card">
                    <div class="summary-card-label">Total Special</div>
                    <div class="summary-card-value">${Components.renderCurrency(totalSpecial)}</div>
                </div>
                <div class="summary-card">
                    <div class="summary-card-label">Total General</div>
                    <div class="summary-card-value">${Components.renderCurrency(totalGeneral)}</div>
                </div>
                <div class="summary-card">
                    <div class="summary-card-label">Total Other</div>
                    <div class="summary-card-value">${Components.renderCurrency(totalOther)}</div>
                </div>
            </div>
        `;

        // Filter tabs
        const damageFilter = App._damageFilter || 'all';
        const filterTabs = ['all', 'special', 'general', 'other'].map(type => {
            const active = damageFilter === type ? ' active' : '';
            const label = type.charAt(0).toUpperCase() + type.slice(1);
            return `<button class="tab-btn tab-sm${active}" data-action="filter-damages" data-type="${type}">${label}</button>`;
        }).join('');

        // Filtered damages
        let filteredDamages = damages;
        if (damageFilter !== 'all') {
            filteredDamages = damages.filter(d => d.type === damageFilter);
        }

        // Damages table
        const columns = [
            {
                key: 'description',
                label: 'Name',
                render: (row) => escapeHtml(row.description || row.name || '--')
            },
            {
                key: 'amount',
                label: 'Amount',
                render: (row) => Components.renderCurrency(row.amount)
            },
            {
                key: 'type',
                label: 'Type',
                render: (row) => `<span class="damage-type-badge ${escapeHtml(row.type || 'general')}">${escapeHtml((row.type || 'general').charAt(0).toUpperCase() + (row.type || 'general').slice(1))}</span>`
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '80px',
                render: (row) => `
                    <div class="row-actions">
                        <button class="btn btn-icon btn-xs" data-action="edit-damage" data-id="${row.id}" title="Edit">&#9998;</button>
                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-damage" data-id="${row.id}" title="Delete">&#128465;</button>
                    </div>
                `
            }
        ];

        const tableHtml = Components.renderTable(columns, filteredDamages, {
            emptyMessage: 'No damages recorded for this matter'
        });

        return `
            <div class="damages-sub-tab">
                ${summaryCards}
                <div class="section-header">
                    <div class="tab-bar tab-bar-inline">
                        ${filterTabs}
                    </div>
                    <button class="btn btn-primary btn-sm" data-action="add-damage" data-matter-id="${matter.id}">+ Add Damage</button>
                </div>
                <div class="table-container">
                    ${tableHtml}
                </div>
            </div>
        `;
    },

    // ---- Medical Records Sub-tab ----
    _renderMedicalRecordsSubTab(matter) {
        const providers = AppState.getMedicalProvidersForMatter(matter.id);

        // Search and filters
        const searchVal = '';
        const treatmentStatusOptions = [
            { value: '', label: 'All Treatment Status' },
            { value: 'active', label: 'Active' },
            { value: 'completed', label: 'Completed' },
            { value: 'pending', label: 'Pending' }
        ];
        const recordStatusOptions = [
            { value: '', label: 'All Record Status' },
            { value: 'requested', label: 'Requested' },
            { value: 'received', label: 'Received' },
            { value: 'pending', label: 'Pending' },
            { value: 'overdue', label: 'Overdue' }
        ];
        const billStatusOptions = [
            { value: '', label: 'All Bill Status' },
            { value: 'outstanding', label: 'Outstanding' },
            { value: 'paid', label: 'Paid' },
            { value: 'adjusted', label: 'Adjusted' }
        ];
        const sortOptions = [
            { value: 'name-asc', label: 'Name A-Z' },
            { value: 'name-desc', label: 'Name Z-A' },
            { value: 'newest', label: 'Newest' },
            { value: 'oldest', label: 'Oldest' }
        ];

        const searchInput = `
            <div class="search-input-wrapper">
                <span class="search-icon">&#128269;</span>
                <input type="text" class="search-input" id="medical-search"
                    value="${escapeHtml(searchVal)}" placeholder="Search providers..."
                    data-action="medical-search-input" />
                ${searchVal ? '<button class="search-clear" data-action="clear-medical-search">&times;</button>' : ''}
            </div>
        `;

        const filtersRow = `
            <div class="toolbar medical-toolbar">
                ${searchInput}
                <div class="toolbar-filters">
                    ${Components.renderDropdown('filter-treatment-status', treatmentStatusOptions, (App._medicalFilters || {}).treatmentStatus || '', 'Treatment Status')}
                    ${Components.renderDropdown('filter-record-status', recordStatusOptions, (App._medicalFilters || {}).recordStatus || '', 'Record Status')}
                    ${Components.renderDropdown('filter-bill-status', billStatusOptions, (App._medicalFilters || {}).billStatus || '', 'Bill Status')}
                    ${Components.renderDropdown('medical-sort', sortOptions, App._medicalSort || 'name-asc', 'Sort by')}
                </div>
                <button class="btn btn-primary btn-sm" data-action="add-provider" data-matter-id="${matter.id}">+ Add Provider</button>
            </div>
        `;

        // Filter and sort providers
        let filteredProviders = [...providers];
        if (searchVal) {
            const q = searchVal.toLowerCase();
            filteredProviders = filteredProviders.filter(p => (p.name || '').toLowerCase().includes(q));
        }

        // Sort
        const sortKey = App._medicalSort || 'name-asc';
        filteredProviders.sort((a, b) => {
            switch (sortKey) {
                case 'name-asc': return (a.name || '').localeCompare(b.name || '');
                case 'name-desc': return (b.name || '').localeCompare(a.name || '');
                case 'newest': return new Date(b.createdDate || 0) - new Date(a.createdDate || 0);
                case 'oldest': return new Date(a.createdDate || 0) - new Date(b.createdDate || 0);
                default: return 0;
            }
        });

        // Provider cards
        let providerCardsHtml = '';
        if (filteredProviders.length === 0) {
            providerCardsHtml = Components.renderEmptyState('&#127973;', 'No Medical Providers', 'Add a medical provider to start tracking records and bills.', '+ Add Provider', '');
        } else {
            providerCardsHtml = filteredProviders.map(provider => {
                return Views._renderMedicalProviderCard(provider, matter.id);
            }).join('');
        }

        return `
            <div class="medical-records-sub-tab">
                ${filtersRow}
                <div class="provider-cards-list">
                    ${providerCardsHtml}
                </div>
            </div>
        `;
    },

    _renderMedicalProviderCard(provider, matterId) {
        // Get records and bills for this provider
        const records = (AppState.medicalRecords || []).filter(r => r.providerId === provider.id);
        const bills = (AppState.medicalBills || []).filter(b => b.providerId === provider.id);

        const treatmentStatus = provider.treatmentStatus || 'active';
        const treatmentStart = provider.treatmentStartDate || provider.createdDate;
        const treatmentEnd = provider.treatmentEndDate || null;

        // Record request info
        const recordRequestDate = provider.recordRequestDate || null;
        const recordRequestStatus = provider.recordRequestStatus || 'not_requested';
        const recordFollowUp = provider.recordFollowUpDate || null;

        // Bill request info
        const billRequestDate = provider.billRequestDate || null;
        const billRequestStatus = provider.billRequestStatus || 'not_requested';
        const billFollowUp = provider.billFollowUpDate || null;

        // Records list
        let recordsListHtml = '';
        if (records.length > 0) {
            recordsListHtml = `
                <div class="expandable-section" id="records-section-${provider.id}">
                    <div class="expandable-header" data-action="toggle-expand" data-target="records-list-${provider.id}">
                        <span class="expand-icon">&#9654;</span> Records (${records.length})
                    </div>
                    <div class="expandable-body" id="records-list-${provider.id}" style="display:none">
                        ${records.map(rec => `
                            <div class="record-row" data-record-id="${rec.id}">
                                <span class="record-name">${escapeHtml(rec.description || rec.type || 'Record')}</span>
                                <span class="record-date">${Components.formatDate(rec.date)}</span>
                                <span class="record-status">${Components.renderStatusBadge(rec.status || 'pending')}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        // Bills list
        let billsListHtml = '';
        if (bills.length > 0) {
            billsListHtml = `
                <div class="expandable-section" id="bills-section-${provider.id}">
                    <div class="expandable-header" data-action="toggle-expand" data-target="bills-list-${provider.id}">
                        <span class="expand-icon">&#9654;</span> Bills (${bills.length})
                    </div>
                    <div class="expandable-body" id="bills-list-${provider.id}" style="display:none">
                        ${bills.map(bill => `
                            <div class="bill-row" data-bill-id="${bill.id}">
                                <span class="bill-desc">${escapeHtml(bill.description || 'Bill')}</span>
                                <span class="bill-amount">${Components.renderCurrency(bill.amount)}</span>
                                <span class="bill-adjustment">${Components.renderCurrency(bill.adjustments)}</span>
                                <span class="bill-insurance">${Components.renderCurrency(bill.insurancePaid)}</span>
                                <span class="bill-balance">${Components.renderCurrency(bill.balance)}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        return `
            <div class="provider-card" data-provider-id="${provider.id}">
                <div class="provider-card-header">
                    <div class="provider-name-row">
                        <h4>${escapeHtml(provider.name)}</h4>
                        ${Components.renderStatusBadge(treatmentStatus)}
                    </div>
                    ${provider.specialty ? `<div class="provider-specialty">${escapeHtml(provider.specialty)}</div>` : ''}
                    <div class="provider-dates">
                        <span>Treatment: ${Components.formatDate(treatmentStart)}${treatmentEnd ? ' - ' + Components.formatDate(treatmentEnd) : ' - Present'}</span>
                    </div>
                </div>

                <div class="provider-card-body">
                    <div class="request-section">
                        <div class="request-row">
                            <span class="request-label">Record Request:</span>
                            ${recordRequestDate ? `
                                <span class="request-date">${Components.formatDate(recordRequestDate)}</span>
                                ${Components.renderStatusBadge(recordRequestStatus)}
                                ${recordFollowUp ? `<span class="follow-up">Follow-up: ${Components.formatDate(recordFollowUp)}</span>` : ''}
                            ` : '<span class="text-muted">Not requested</span>'}
                        </div>
                        <div class="request-row">
                            <span class="request-label">Bill Request:</span>
                            ${billRequestDate ? `
                                <span class="request-date">${Components.formatDate(billRequestDate)}</span>
                                ${Components.renderStatusBadge(billRequestStatus)}
                                ${billFollowUp ? `<span class="follow-up">Follow-up: ${Components.formatDate(billFollowUp)}</span>` : ''}
                            ` : '<span class="text-muted">Not requested</span>'}
                        </div>
                    </div>

                    ${recordsListHtml}
                    ${billsListHtml}
                </div>

                <div class="provider-card-footer">
                    <button class="btn btn-sm btn-secondary" data-action="edit-provider" data-id="${provider.id}">Edit Provider</button>
                    <button class="btn btn-sm btn-danger" data-action="delete-provider" data-id="${provider.id}">Delete Provider</button>
                </div>
            </div>
        `;
    },

    // ---- Settlement Sub-tab ----
    _renderSettlementSubTab(matter) {
        const settlement = AppState.getSettlement(matter.id);
        const summary = AppState.getSettlementSummary(matter.id);
        const expenseSummary = AppState.getExpenseSummaryForMatter(matter.id);
        const matterBills = (AppState.medicalBills || []).filter(b => b.matterId === matter.id);

        // Deduction order text
        const deductionText = summary.deductionOrder === 'fees_first'
            ? 'Deducting legal fees first, then expenses'
            : 'Deducting expenses first, then legal fees';

        // Settlement Calculator Summary
        const calculatorCard = `
            <div class="widget settlement-calculator">
                <h3>Settlement Calculator</h3>
                <div class="settlement-summary-rows">
                    <div class="settlement-row">
                        <span class="settlement-label">Total Recoveries</span>
                        <span class="settlement-value">${Components.renderCurrency(summary.grossRecovery)}</span>
                    </div>
                    <div class="settlement-row deduction">
                        <span class="settlement-label">- Legal Fees</span>
                        <span class="settlement-value">${Components.renderCurrency(summary.totalLegalFees)}</span>
                    </div>
                    <div class="settlement-row deduction">
                        <span class="settlement-label">- Matter Expenses</span>
                        <span class="settlement-value">${Components.renderCurrency(summary.totalCaseExpenses)}</span>
                    </div>
                    <div class="settlement-row deduction">
                        <span class="settlement-label">- Liens &amp; Outstanding Balances</span>
                        <span class="settlement-value">${Components.renderCurrency(summary.totalLiens)}</span>
                    </div>
                    <div class="settlement-row net-total">
                        <span class="settlement-label"><strong>= Net Client Compensation</strong></span>
                        <span class="settlement-value"><strong>${Components.renderCurrency(summary.netClientCompensation)}</strong></span>
                    </div>
                </div>
                <div class="deduction-order-indicator">
                    <span class="text-muted">${escapeHtml(deductionText)}</span>
                </div>
            </div>
        `;

        // --- Recoveries Section ---
        const recoveryColumns = [
            {
                key: 'source',
                label: 'Source',
                render: (row) => escapeHtml(row.source || row.type || '--')
            },
            {
                key: 'amount',
                label: 'Amount',
                render: (row) => Components.renderCurrency(row.amount)
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '80px',
                render: (row) => `
                    <div class="row-actions">
                        <button class="btn btn-icon btn-xs" data-action="edit-recovery" data-id="${row.id}" data-matter-id="${matter.id}" title="Edit">&#9998;</button>
                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-recovery" data-id="${row.id}" data-matter-id="${matter.id}" title="Delete">&#128465;</button>
                    </div>
                `
            }
        ];

        const recoveriesSection = `
            <div class="settlement-section">
                <div class="section-header">
                    <h4>Recoveries</h4>
                    <button class="btn btn-sm btn-primary" data-action="add-recovery" data-matter-id="${matter.id}">+ Add Recovery</button>
                </div>
                ${Components.renderTable(recoveryColumns, settlement.recoveries, { emptyMessage: 'No recoveries recorded' })}
            </div>
        `;

        // --- Legal Fees Section ---
        const legalFeeColumns = [
            {
                key: 'type',
                label: 'Fee Source',
                render: (row) => escapeHtml(row.description || row.type || '--')
            },
            {
                key: 'recipient',
                label: 'Recipient',
                render: (row) => {
                    if (row.recipientId) {
                        const user = AppState.getUserById(row.recipientId);
                        return user ? escapeHtml(user.name) : '--';
                    }
                    return '--';
                }
            },
            {
                key: 'percentage',
                label: 'Rate',
                render: (row) => row.percentage ? escapeHtml(row.percentage + '%') : '--'
            },
            {
                key: 'discount',
                label: 'Discount',
                render: (row) => row.discount ? Components.renderCurrency(row.discount) : '--'
            },
            {
                key: 'feeAmount',
                label: 'Fee Amount',
                render: (row) => {
                    if (row.flatAmount > 0) return Components.renderCurrency(row.flatAmount);
                    if (row.percentage > 0) return Components.renderCurrency(summary.grossRecovery * (row.percentage / 100));
                    return '--';
                }
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '80px',
                render: (row) => `
                    <div class="row-actions">
                        <button class="btn btn-icon btn-xs" data-action="edit-legal-fee" data-id="${row.id}" data-matter-id="${matter.id}" title="Edit">&#9998;</button>
                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-legal-fee" data-id="${row.id}" data-matter-id="${matter.id}" title="Delete">&#128465;</button>
                    </div>
                `
            }
        ];

        const legalFeesSection = `
            <div class="settlement-section">
                <div class="section-header">
                    <h4>Legal Fees</h4>
                    <button class="btn btn-sm btn-primary" data-action="add-legal-fee" data-matter-id="${matter.id}">+ Add Legal Fee</button>
                </div>
                ${Components.renderTable(legalFeeColumns, settlement.legalFees, { emptyMessage: 'No legal fees recorded' })}
            </div>
        `;

        // --- Matter Expenses Section (read-only from activities) ---
        const expenseByCategory = expenseSummary.byCategory || {};
        const expenseRows = Object.entries(expenseByCategory).map(([category, total]) => ({
            id: category,
            category: category,
            total: total
        }));

        const expenseColumns = [
            {
                key: 'category',
                label: 'Category',
                render: (row) => escapeHtml(row.category)
            },
            {
                key: 'total',
                label: 'Total Amount',
                render: (row) => Components.renderCurrency(row.total)
            }
        ];

        const expensesSection = `
            <div class="settlement-section">
                <div class="section-header">
                    <h4>Matter Expenses</h4>
                    <span class="text-muted">(from Activities)</span>
                </div>
                ${Components.renderTable(expenseColumns, expenseRows, { emptyMessage: 'No expenses recorded' })}
                <div class="section-total">
                    <strong>Total: ${Components.renderCurrency(expenseSummary.total)}</strong>
                </div>
            </div>
        `;

        // --- Non-Medical Liens Section ---
        const lienColumns = [
            {
                key: 'lienholder',
                label: 'Lien Holder',
                render: (row) => escapeHtml(row.lienholder || '--')
            },
            {
                key: 'type',
                label: 'Description',
                render: (row) => escapeHtml(row.type || '--')
            },
            {
                key: 'amount',
                label: 'Amount',
                render: (row) => Components.renderCurrency(row.amount)
            },
            {
                key: 'negotiatedAmount',
                label: 'Reduction',
                render: (row) => row.negotiatedAmount != null ? Components.renderCurrency(row.amount - row.negotiatedAmount) : '--'
            },
            {
                key: 'netAmount',
                label: 'Net Amount',
                render: (row) => Components.renderCurrency(row.negotiatedAmount != null ? row.negotiatedAmount : row.amount)
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '80px',
                render: (row) => `
                    <div class="row-actions">
                        <button class="btn btn-icon btn-xs" data-action="edit-lien" data-id="${row.id}" data-matter-id="${matter.id}" title="Edit">&#9998;</button>
                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-lien" data-id="${row.id}" data-matter-id="${matter.id}" title="Delete">&#128465;</button>
                    </div>
                `
            }
        ];

        const liensSection = `
            <div class="settlement-section">
                <div class="section-header">
                    <h4>Non-Medical Liens</h4>
                    <button class="btn btn-sm btn-primary" data-action="add-lien" data-matter-id="${matter.id}">+ Add Lien</button>
                </div>
                ${Components.renderTable(lienColumns, settlement.nonMedicalLiens, { emptyMessage: 'No non-medical liens recorded' })}
            </div>
        `;

        // --- Outstanding Balances Section ---
        const balanceColumns = [
            {
                key: 'type',
                label: 'Responsibility',
                render: (row) => escapeHtml(row.type || '--')
            },
            {
                key: 'creditor',
                label: 'Balance Holder',
                render: (row) => escapeHtml(row.creditor || '--')
            },
            {
                key: 'notes',
                label: 'Description',
                render: (row) => escapeHtml(row.notes || '--')
            },
            {
                key: 'originalAmount',
                label: 'Balance',
                render: (row) => Components.renderCurrency(row.originalAmount)
            },
            {
                key: 'negotiatedAmount',
                label: 'Reduction',
                render: (row) => row.negotiatedAmount != null ? Components.renderCurrency(row.originalAmount - row.negotiatedAmount) : '--'
            },
            {
                key: 'netAmount',
                label: 'Net',
                render: (row) => Components.renderCurrency(row.negotiatedAmount != null ? row.negotiatedAmount : row.originalAmount)
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '80px',
                render: (row) => `
                    <div class="row-actions">
                        <button class="btn btn-icon btn-xs" data-action="edit-outstanding-balance" data-id="${row.id}" data-matter-id="${matter.id}" title="Edit">&#9998;</button>
                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-outstanding-balance" data-id="${row.id}" data-matter-id="${matter.id}" title="Delete">&#128465;</button>
                    </div>
                `
            }
        ];

        const balancesSection = `
            <div class="settlement-section">
                <div class="section-header">
                    <h4>Outstanding Balances</h4>
                    <button class="btn btn-sm btn-primary" data-action="add-outstanding-balance" data-matter-id="${matter.id}">+ Add Balance</button>
                </div>
                ${Components.renderTable(balanceColumns, settlement.outstandingBalances, { emptyMessage: 'No outstanding balances recorded' })}
            </div>
        `;

        // --- Medical Liens Section (read-only from medical bills) ---
        const medicalLienRows = matterBills.filter(b => (b.balance || 0) > 0).map(bill => {
            const provider = (AppState.medicalProviders || []).find(p => p.id === bill.providerId);
            return {
                id: bill.id,
                provider: provider ? provider.name : 'Unknown',
                amount: bill.balance || 0
            };
        });

        const medicalLienColumns = [
            {
                key: 'provider',
                label: 'Provider',
                render: (row) => escapeHtml(row.provider)
            },
            {
                key: 'amount',
                label: 'Amount',
                render: (row) => Components.renderCurrency(row.amount)
            }
        ];

        const medicalLiensSection = `
            <div class="settlement-section">
                <div class="section-header">
                    <h4>Medical Liens</h4>
                    <span class="text-muted">(from Medical Bills)</span>
                </div>
                ${Components.renderTable(medicalLienColumns, medicalLienRows, { emptyMessage: 'No medical liens' })}
                ${medicalLienRows.length > 0 ? `
                    <div class="section-total">
                        <strong>Total: ${Components.renderCurrency(summary.totalMedicalBillLiens)}</strong>
                    </div>
                ` : ''}
            </div>
        `;

        // Generate Settlement Statement button
        const hasRecoveries = settlement.recoveries.length > 0;
        const generateBtn = hasRecoveries
            ? `<button class="btn btn-primary" data-action="generate-settlement-statement" data-matter-id="${matter.id}">Generate Settlement Statement</button>`
            : '';

        return `
            <div class="settlement-sub-tab">
                ${calculatorCard}
                ${recoveriesSection}
                ${legalFeesSection}
                ${expensesSection}
                ${liensSection}
                ${balancesSection}
                ${medicalLiensSection}
                <div class="settlement-actions">
                    ${generateBtn}
                </div>
            </div>
        `;
    },

    // ============================================================
    // 5. STAGES VIEW (Kanban)
    // ============================================================

    renderStagesView() {
        const practiceAreaOptions = [{ value: '', label: 'Select Practice Area...' }].concat(
            AppState.practiceAreas.map(pa => ({ value: pa.id, label: pa.name }))
        );
        const selectedPAId = AppState.stagesSelectedPracticeAreaId;
        const selectedPA = selectedPAId ? AppState.getPracticeAreaById(selectedPAId) : null;

        const selectorHtml = `
            <div class="stages-selector">
                <label class="stages-selector-label">Practice Area</label>
                ${Components.renderDropdown('stages-practice-area', practiceAreaOptions, selectedPAId || '', 'Select Practice Area...', false)}
            </div>
        `;

        if (!selectedPA) {
            return `
                <div class="stages-view">
                    <div class="view-header">
                        <h1>Stages</h1>
                    </div>
                    ${selectorHtml}
                    ${Components.renderEmptyState('&#9638;', 'Select a Practice Area', 'Choose a practice area above to view its stage pipeline.')}
                </div>
            `;
        }

        const stages = selectedPA.stages || [];
        if (stages.length === 0) {
            return `
                <div class="stages-view">
                    <div class="view-header">
                        <h1>Stages</h1>
                    </div>
                    ${selectorHtml}
                    ${Components.renderEmptyState('&#9638;', 'No Stages Defined', 'This practice area has no stages. Add stages in Settings.', 'Go to Settings', '#/settings')}
                </div>
            `;
        }

        // Build kanban columns
        const sortedStages = [...stages].sort((a, b) => (a.order || 0) - (b.order || 0));
        const mattersInPA = AppState.getMattersForPracticeArea(selectedPAId);

        const columnsHtml = sortedStages.map(stage => {
            const mattersInStage = mattersInPA.filter(m => m.stageId === stage.id);
            const cardsHtml = mattersInStage.map(m => {
                const client = m.clientId ? AppState.getContactById(m.clientId) : null;
                const clientName = client ? (client.name || ((client.firstName || '') + ' ' + (client.lastName || '')).trim()) : '--';
                const desc = m.description || '';
                const truncDesc = desc.length > 40 ? desc.substring(0, 40) + '...' : desc;

                // Days at stage (calculated from updatedDate)
                const daysAtStage = Math.max(0, Math.floor((Date.now() - new Date(m.updatedDate || m.createdDate).getTime()) / (1000 * 60 * 60 * 24)));
                const statusColor = m.status === 'open' ? 'green' : (m.status === 'pending' ? 'yellow' : 'gray');

                return `
                    <div class="kanban-card" data-route="#/matters/${m.id}" data-matter-id="${m.id}">
                        <div class="kanban-card-status-bar ${statusColor}"></div>
                        <div class="kanban-card-header">
                            <span class="kanban-card-number">${escapeHtml(AppState.formatMatterNumber(m))}</span>
                            <div class="kanban-card-menu">
                                <button class="btn btn-icon btn-xs kanban-menu-toggle" data-matter-id="${m.id}" title="Actions">&#8942;</button>
                                <div class="kanban-menu" id="kanban-menu-${m.id}" style="display:none">
                                    <div class="kanban-menu-item" data-action="kanban-switch-pa" data-id="${m.id}">Switch Practice Area</div>
                                    ${m.status === 'open'
                                        ? `<div class="kanban-menu-item" data-action="kanban-toggle-status" data-id="${m.id}">Mark as Pending</div>`
                                        : `<div class="kanban-menu-item" data-action="kanban-toggle-status" data-id="${m.id}">Mark as Open</div>`
                                    }
                                    <div class="kanban-menu-item" data-action="kanban-close-matter" data-id="${m.id}">Close Matter</div>
                                </div>
                            </div>
                        </div>
                        <div class="kanban-card-desc">${escapeHtml(truncDesc)}</div>
                        <div class="kanban-card-client">${escapeHtml(clientName)}</div>
                        <div class="kanban-card-days">${daysAtStage} day${daysAtStage !== 1 ? 's' : ''} at stage</div>
                    </div>
                `;
            }).join('');

            return `
                <div class="kanban-column" data-stage-id="${stage.id}">
                    <div class="kanban-column-header">
                        <span class="kanban-column-title">${escapeHtml(stage.name)}</span>
                        <span class="kanban-column-count">${mattersInStage.length}</span>
                    </div>
                    <div class="kanban-column-body">
                        ${cardsHtml || '<div class="kanban-empty">No matters</div>'}
                    </div>
                </div>
            `;
        }).join('');

        return `
            <div class="stages-view">
                <div class="view-header">
                    <h1>Stages</h1>
                </div>
                ${selectorHtml}
                <div class="kanban-board">
                    ${columnsHtml}
                </div>
            </div>
        `;
    },

    // ============================================================
    // 6. SETTINGS VIEW
    // ============================================================

    renderSettingsView() {
        const activeTab = AppState.settingsTab || 'practice-areas';

        const settingsTabs = [
            { key: 'practice-areas', label: 'Practice Areas' },
            { key: 'matter-templates', label: 'Matter Templates' },
            { key: 'matter-numbering', label: 'Matter Numbering' },
            { key: 'notifications', label: 'Notifications' }
        ];

        const tabsHtml = settingsTabs.map(tab => {
            const active = activeTab === tab.key ? ' active' : '';
            return `<div class="settings-tab-item${active}" data-action="settings-tab" data-tab="${tab.key}">${escapeHtml(tab.label)}</div>`;
        }).join('');

        let contentHtml = '';
        switch (activeTab) {
            case 'practice-areas':
                contentHtml = Views._renderPracticeAreasSettings();
                break;
            case 'matter-templates':
                contentHtml = Views._renderMatterTemplatesSettings();
                break;
            case 'matter-numbering':
                contentHtml = Views._renderMatterNumberingSettings();
                break;
            case 'notifications':
                contentHtml = Views._renderNotificationsSettings();
                break;
            default:
                contentHtml = Views._renderPracticeAreasSettings();
        }

        return `
            <div class="settings-view">
                <div class="view-header">
                    <h1>Settings</h1>
                </div>
                <div class="settings-layout">
                    <div class="settings-sidebar">
                        ${tabsHtml}
                    </div>
                    <div class="settings-content">
                        ${contentHtml}
                    </div>
                </div>
            </div>
        `;
    },

    _renderPracticeAreasSettings() {
        const practiceAreas = AppState.practiceAreas || [];
        const expandedPAs = App._expandedPracticeAreas || new Set();

        let listHtml = '';
        if (practiceAreas.length === 0) {
            listHtml = '<p class="text-muted">No practice areas defined.</p>';
        } else {
            listHtml = practiceAreas.map(pa => {
                const matterCount = AppState.getMattersForPracticeArea(pa.id).length;
                const stageCount = pa.stages ? pa.stages.length : 0;
                const isExpanded = expandedPAs.has(pa.id);

                let stagesListHtml = '';
                if (isExpanded && pa.stages && pa.stages.length > 0) {
                    const sortedStages = [...pa.stages].sort((a, b) => (a.order || 0) - (b.order || 0));
                    stagesListHtml = `
                        <div class="pa-stages-list">
                            ${sortedStages.map((stage, idx) => `
                                <div class="pa-stage-row" data-stage-id="${stage.id}" data-practice-area-id="${pa.id}">
                                    <span class="stage-reorder-handle" title="Drag to reorder">&#9776;</span>
                                    <span class="stage-name">${escapeHtml(stage.name)}</span>
                                    <div class="stage-actions">
                                        <button class="btn btn-icon btn-xs" data-action="edit-stage" data-stage-id="${stage.id}" data-practice-area-id="${pa.id}" title="Edit">&#9998;</button>
                                        <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-stage" data-stage-id="${stage.id}" data-practice-area-id="${pa.id}" title="Delete">&#128465;</button>
                                    </div>
                                </div>
                            `).join('')}
                            <button class="btn btn-sm btn-secondary mt-2" data-action="add-stage" data-practice-area-id="${pa.id}">+ Add Stage</button>
                        </div>
                    `;
                } else if (isExpanded) {
                    stagesListHtml = `
                        <div class="pa-stages-list">
                            <p class="text-muted">No stages defined.</p>
                            <button class="btn btn-sm btn-secondary mt-2" data-action="add-stage" data-practice-area-id="${pa.id}">+ Add Stage</button>
                        </div>
                    `;
                }

                return `
                    <div class="pa-list-item ${isExpanded ? 'expanded' : ''}" data-pa-id="${pa.id}">
                        <div class="pa-list-row" data-action="toggle-practice-area-stages" data-id="${pa.id}">
                            <span class="pa-expand-icon">${isExpanded ? '&#9660;' : '&#9654;'}</span>
                            <span class="pa-name">${escapeHtml(pa.name)}</span>
                            <span class="pa-meta">${stageCount} stage${stageCount !== 1 ? 's' : ''} &middot; ${matterCount} matter${matterCount !== 1 ? 's' : ''}</span>
                            <div class="pa-actions">
                                <button class="btn btn-icon btn-xs" data-action="edit-practice-area" data-id="${pa.id}" title="Edit">&#9998;</button>
                                <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-practice-area" data-id="${pa.id}" title="Delete">&#128465;</button>
                            </div>
                        </div>
                        ${stagesListHtml}
                    </div>
                `;
            }).join('');
        }

        return `
            <div class="settings-section">
                <div class="section-header">
                    <h2>Practice Areas</h2>
                    <button class="btn btn-primary btn-sm" data-action="add-practice-area">+ Add Practice Area</button>
                </div>
                <div class="pa-list">
                    ${listHtml}
                </div>
            </div>
        `;
    },

    _renderMatterTemplatesSettings() {
        const templates = AppState.matterTemplates || [];

        let listHtml = '';
        if (templates.length === 0) {
            listHtml = '<p class="text-muted">No matter templates defined.</p>';
        } else {
            listHtml = templates.map(tmpl => {
                const pa = tmpl.practiceAreaId ? AppState.getPracticeAreaById(tmpl.practiceAreaId) : null;
                const billingLabel = Views._formatBillingMethod(tmpl.billingMethod);

                return `
                    <div class="template-list-item" data-template-id="${tmpl.id}">
                        <div class="template-info">
                            <span class="template-name">${escapeHtml(tmpl.name)}</span>
                            <span class="template-meta">
                                ${pa ? escapeHtml(pa.name) : 'No practice area'}
                                &middot; ${escapeHtml(billingLabel)}
                                ${tmpl.isDefault ? ' &middot; <span class="default-badge">Default</span>' : ''}
                            </span>
                        </div>
                        <div class="template-actions">
                            <button class="btn btn-icon btn-xs" data-action="edit-template" data-id="${tmpl.id}" title="Edit">&#9998;</button>
                            ${!tmpl.isDefault ? `<button class="btn btn-xs btn-secondary" data-action="set-default-template" data-id="${tmpl.id}" title="Set as Default">Set Default</button>` : ''}
                            <button class="btn btn-icon btn-xs btn-danger-icon" data-action="delete-template" data-id="${tmpl.id}" title="Delete">&#128465;</button>
                        </div>
                    </div>
                `;
            }).join('');
        }

        return `
            <div class="settings-section">
                <div class="section-header">
                    <h2>Matter Templates</h2>
                    <button class="btn btn-primary btn-sm" data-action="create-template">+ Create Template</button>
                </div>
                <div class="template-list">
                    ${listHtml}
                </div>
            </div>
        `;
    },

    _renderMatterNumberingSettings() {
        const scheme = AppState.numberingScheme || {};
        const mode = scheme.mode || 'auto';
        const prefix = scheme.prefix || '';
        const padLength = scheme.padLength || 5;
        const separator = scheme.separator || '-';
        const appendClientName = scheme.appendClientName || false;
        const startNumber = scheme.startNumber || 1;

        // Format preview
        const previewNum = String(startNumber).padStart(padLength, '0');
        const preview = prefix ? prefix + separator + previewNum : previewNum;

        const separatorOptions = [
            { value: '-', label: 'Hyphen (-)' },
            { value: '.', label: 'Period (.)' },
            { value: '/', label: 'Slash (/)' },
            { value: '_', label: 'Underscore (_)' }
        ];

        const padLengthOptions = [
            { value: 3, label: '3 digits' },
            { value: 4, label: '4 digits' },
            { value: 5, label: '5 digits' },
            { value: 6, label: '6 digits' }
        ];

        return `
            <div class="settings-section">
                <div class="section-header">
                    <h2>Matter Numbering</h2>
                </div>

                <div class="numbering-preview">
                    <span class="numbering-preview-label">Current Format:</span>
                    <span class="numbering-preview-value">${escapeHtml(preview)}${appendClientName ? separator + 'ClientName' : ''}</span>
                </div>

                <div class="form-group">
                    <label>Format</label>
                    <div class="radio-group">
                        <label class="radio-option">
                            <input type="radio" name="numbering-mode" value="auto" ${mode === 'auto' ? 'checked' : ''} data-field="numberingMode" />
                            <span class="radio-label">Automatic</span>
                        </label>
                        <label class="radio-option">
                            <input type="radio" name="numbering-mode" value="manual" ${mode === 'manual' ? 'checked' : ''} data-field="numberingMode" />
                            <span class="radio-label">Manual</span>
                        </label>
                    </div>
                </div>

                <div class="auto-numbering-fields" ${mode !== 'auto' ? 'style="display:none"' : ''}>
                    <div class="form-group">
                        <label for="numbering-prefix">Prefix</label>
                        <input type="text" id="numbering-prefix" class="form-control" data-field="numberingPrefix" value="${escapeHtml(prefix)}" placeholder="e.g. MLG" />
                    </div>
                    <div class="form-group">
                        <label>Number Padding</label>
                        ${Components.renderDropdown('numbering-pad-length', padLengthOptions, padLength, 'Select padding...')}
                    </div>
                    <div class="form-group">
                        <label>Separator</label>
                        ${Components.renderDropdown('numbering-separator', separatorOptions, separator, 'Select separator...')}
                    </div>
                    <div class="form-group">
                        ${Components.renderCheckbox('numbering-append-client', appendClientName, 'Include client name in number')}
                    </div>
                </div>

                <div class="form-group">
                    <label for="numbering-start">Starting Number</label>
                    <input type="number" id="numbering-start" class="form-control" data-field="numberingStart" value="${startNumber}" min="1" />
                </div>

                <div class="form-group">
                    ${Components.renderCheckbox('numbering-update-existing', false, 'Update existing matters to new format')}
                </div>

                <div class="form-actions">
                    <button class="btn btn-primary" data-action="save-numbering">Save Changes</button>
                </div>
            </div>
        `;
    },

    _renderNotificationsSettings() {
        const settings = AppState.notificationSettings || {};

        const notifTypes = [
            { key: 'matterCreated', label: 'Matter Created' },
            { key: 'matterUpdated', label: 'Matter Updated' },
            { key: 'matterClosed', label: 'Matter Closed' },
            { key: 'matterDeleted', label: 'Matter Deleted' },
            { key: 'taskDue', label: 'Task Due' },
            { key: 'trustLow', label: 'Trust Balance Low' },
            { key: 'statuteApproaching', label: 'Statute of Limitations Approaching' },
            { key: 'newTimeEntry', label: 'New Time Entry' },
            { key: 'newExpense', label: 'New Expense' },
            { key: 'settlementUpdated', label: 'Settlement Updated' }
        ];

        const togglesHtml = notifTypes.map(nt => {
            const active = settings[nt.key] !== false;
            return Components.renderToggle('notification-' + nt.key, active, nt.label);
        }).join('');

        return `
            <div class="settings-section">
                <div class="section-header">
                    <h2>Notifications</h2>
                </div>
                <div class="notification-toggles">
                    ${togglesHtml}
                </div>
                <div class="form-actions">
                    <button class="btn btn-primary" data-action="save-notifications">Save</button>
                </div>
            </div>
        `;
    },

    // ============================================================
    // 7. RECOVERY BIN VIEW
    // ============================================================

    renderRecoveryBinView() {
        const deletedMatters = AppState.deletedMatters || [];

        const columns = [
            {
                key: 'type',
                label: 'Type',
                width: '80px',
                render: () => 'Matter'
            },
            {
                key: 'number',
                label: 'Name / Number',
                render: (row) => escapeHtml(AppState.formatMatterNumber(row))
            },
            {
                key: 'description',
                label: 'Description',
                render: (row) => {
                    const desc = row.description || '';
                    return escapeHtml(desc.length > 60 ? desc.substring(0, 60) + '...' : desc);
                }
            },
            {
                key: 'deletedBy',
                label: 'Deleted By',
                render: (row) => {
                    // Try to find user from activity log
                    const logEntry = (AppState.activityLog || []).find(
                        l => l.entityType === 'matter' && l.entityId === row.id && l.action === 'deleted'
                    );
                    if (logEntry && logEntry.userId) {
                        const user = AppState.getUserById(logEntry.userId);
                        return user ? escapeHtml(user.name) : '--';
                    }
                    return AppState.currentUser ? escapeHtml(AppState.currentUser.name) : '--';
                }
            },
            {
                key: 'deletedDate',
                label: 'Deleted Date',
                render: (row) => Components.formatDateTime(row.deletedDate)
            },
            {
                key: '_actions',
                label: 'Actions',
                width: '100px',
                render: (row) => `
                    <button class="btn btn-sm btn-primary" data-action="recover-matter" data-id="${row.id}">Recover</button>
                `
            }
        ];

        const tableHtml = deletedMatters.length > 0
            ? Components.renderTable(columns, deletedMatters, { emptyMessage: 'Recovery bin is empty' })
            : Components.renderEmptyState('&#128465;', 'Recovery Bin is Empty', 'Deleted matters will appear here for up to 6 months.');

        return `
            <div class="recovery-bin-view">
                <div class="view-header">
                    <h1>Recovery Bin</h1>
                </div>
                ${Components.renderInfoBox('Deleted matters are retained for 6 months before being permanently removed.')}
                <div class="table-container">
                    ${tableHtml}
                </div>
            </div>
        `;
    },

    // ============================================================
    // 8. MODAL RENDERER
    // ============================================================

    renderModal() {
        const modal = AppState.modalData;
        if (!modal) return '';

        let title = modal.title || '';
        let body = modal.body || '';
        let footer = modal.footer || '';

        // If it's a confirm-type modal, delegate to Components
        if (modal.type === 'confirm') {
            const confirmData = Components.renderConfirmModal(
                modal.title || 'Confirm',
                modal.message || 'Are you sure?',
                modal.confirmLabel || 'Confirm',
                modal.confirmClass || 'btn-danger'
            );
            title = confirmData.title;
            body = confirmData.body;
            footer = confirmData.footer;
        } else if (modal.type === 'form') {
            title = modal.title || 'Form';
            body = modal.body || '';
            footer = modal.footer || `
                <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                <button class="btn btn-primary" data-action="submit-modal-form">Save</button>
            `;
        } else if (modal.type === 'info') {
            title = modal.title || 'Information';
            body = modal.body || '';
            footer = `<button class="btn btn-primary" data-action="close-modal">OK</button>`;
        }

        return `
            <div class="modal-overlay" data-action="close-modal-overlay">
                <div class="modal" id="app-modal">
                    <div class="modal-header">
                        <h2 class="modal-title">${escapeHtml(title)}</h2>
                        <button class="modal-close" data-action="close-modal">&times;</button>
                    </div>
                    <div class="modal-body">
                        ${body}
                    </div>
                    ${footer ? `<div class="modal-footer">${footer}</div>` : ''}
                </div>
            </div>
        `;
    },

    // ============================================================
    // HELPER METHODS
    // ============================================================

    _formatBillingMethod(method) {
        const labels = {
            hourly: 'Hourly',
            contingency: 'Contingency Fee',
            flat_rate: 'Flat Rate'
        };
        return labels[method] || method || '--';
    },

    _formatActivityAction(entry) {
        const action = entry.action || '';
        const entityType = entry.entityType || '';
        const details = entry.details || {};

        switch (action) {
            case 'created':
                return 'created ' + entityType + (details.description ? ': ' + details.description : '');
            case 'updated':
                if (details && Object.keys(details).length > 0) {
                    const fields = Object.keys(details).filter(k => k !== 'from' && k !== 'to');
                    if (fields.length > 0) {
                        return 'updated ' + fields.join(', ') + ' on ' + entityType;
                    }
                }
                return 'updated ' + entityType;
            case 'deleted':
                return 'deleted ' + entityType + (details.description ? ': ' + details.description : '');
            case 'closed':
                return 'closed matter';
            case 'reopened':
                return 'reopened matter';
            case 'recovered':
                return 'recovered ' + entityType + ' from recovery bin';
            case 'status_changed':
                return 'changed status to ' + (details.status || 'unknown');
            case 'stage_changed':
                return 'moved matter to a new stage';
            default:
                return action + ' ' + entityType;
        }
    }
};

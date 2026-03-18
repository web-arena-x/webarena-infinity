// ============================================================
// views.js — View renderers for Gmail Accounts & Contacts
// ============================================================

const Views = {

    // ---- Sidebar ----
    renderSidebar() {
        const C = Components;
        const filter = AppState.contactsFilter;
        let html = `<div class="sidebar">`;

        // Logo / header
        html += `<div class="sidebar-header">
            <div class="sidebar-logo">
                <span class="material-icons" style="color:#4285F4;font-size:28px;">contacts</span>
                <span class="sidebar-title">Contacts</span>
            </div>
        </div>`;

        // Create contact button
        html += `<div class="sidebar-action">
            <button class="btn btn-primary btn-create" data-action="open-create-contact">
                <span class="material-icons btn-icon">add</span> Create contact
            </button>
        </div>`;

        // Navigation
        html += `<nav class="sidebar-nav">`;
        html += this._navItem('contacts', 'all', 'people', 'Contacts', AppState.contacts.length);
        html += this._navItem('contacts', 'frequently', 'history', 'Frequently contacted', null);
        html += this._navItem('contacts', 'starred', 'star', 'Starred', AppState.contacts.filter(c => c.isStarred).length);
        html += this._navItem('other-contacts', 'other', 'person_outline', 'Other contacts', AppState.otherContacts.length);
        html += this._navItem('merge-suggestions', 'merge', 'merge_type', 'Merge & fix', AppState.mergeSuggestions.filter(s => !s.dismissed).length);
        html += `</nav>`;

        // Labels section
        html += `<div class="sidebar-section">`;
        html += `<div class="sidebar-section-header">
            <span class="sidebar-section-title">Labels</span>
            <button class="icon-btn icon-btn-sm" data-action="open-create-label" title="Create label">
                <span class="material-icons">add</span>
            </button>
        </div>`;
        for (const label of AppState.contactLabels) {
            const isActive = filter === label.id;
            html += `<div class="nav-item ${isActive ? 'nav-active' : ''}" data-action="filter-by-label" data-label-id="${label.id}">
                <span class="label-dot" style="background:${label.color}"></span>
                <span class="nav-label">${C.escapeHtml(label.name)}</span>
                <span class="nav-count">${label.contactCount}</span>
                <button class="icon-btn icon-btn-xs nav-edit" data-action="edit-label" data-label-id="${label.id}" title="Edit label">
                    <span class="material-icons">edit</span>
                </button>
            </div>`;
        }
        html += `</div>`;

        // More navigation
        html += `<nav class="sidebar-nav sidebar-nav-bottom">`;
        html += this._sidebarNavItem('import-export', 'import_export', 'Import & Export');
        html += this._sidebarNavItem('delegates', 'supervisor_account', 'Delegates');
        html += this._sidebarNavItem('linked-services', 'link', 'Linked Services');
        html += this._sidebarNavItem('settings', 'settings', 'Settings');
        html += `</nav>`;

        html += `</div>`;
        return html;
    },

    _navItem(view, filter, icon, label, count) {
        const isActive = (AppState.currentView === view || AppState.currentView === 'contacts') && AppState.contactsFilter === filter;
        const isOther = view === 'other-contacts' && AppState.currentView === 'other-contacts';
        const isMerge = view === 'merge-suggestions' && AppState.currentView === 'merge-suggestions';
        const active = isActive || isOther || isMerge ? ' nav-active' : '';
        return `<div class="nav-item${active}" data-action="navigate" data-view="${view}" data-filter="${filter}">
            <span class="material-icons nav-icon">${icon}</span>
            <span class="nav-label">${label}</span>
            ${count !== null && count !== undefined ? `<span class="nav-count">${count}</span>` : ''}
        </div>`;
    },

    _sidebarNavItem(view, icon, label) {
        const active = AppState.currentView === view ? ' nav-active' : '';
        return `<div class="nav-item${active}" data-action="navigate" data-view="${view}">
            <span class="material-icons nav-icon">${icon}</span>
            <span class="nav-label">${label}</span>
        </div>`;
    },

    // ---- Main Content ----
    renderMain() {
        switch (AppState.currentView) {
            case 'contacts': return this.renderContacts();
            case 'other-contacts': return this.renderOtherContacts();
            case 'merge-suggestions': return this.renderMergeSuggestions();
            case 'delegates': return this.renderDelegates();
            case 'linked-services': return this.renderLinkedServices();
            case 'import-export': return this.renderImportExport();
            case 'settings': return this.renderSettings();
            default: return this.renderContacts();
        }
    },

    // ---- Contacts View ----
    renderContacts() {
        const C = Components;
        const paged = AppState.getPagedContacts();
        let html = `<div class="main-content">`;

        // Toolbar
        html += `<div class="toolbar">`;
        html += `<div class="toolbar-left">`;
        html += C.searchBar('contact-search', AppState.searchQuery, 'Search contacts');
        html += `</div>`;
        html += `<div class="toolbar-right">`;
        html += `<div class="toolbar-sort">`;
        html += C.dropdown('sort-by', [
            { value: 'firstName', label: 'First name' },
            { value: 'lastName', label: 'Last name' },
            { value: 'email', label: 'Email' },
            { value: 'company', label: 'Company' },
            { value: 'updatedAt', label: 'Last updated' }
        ], AppState.contactsSortBy, 'Sort by');
        html += `</div>`;
        html += `<button class="icon-btn" data-action="toggle-sort-dir" title="Toggle sort direction">
            <span class="material-icons">${AppState.contactsSortDir === 'asc' ? 'arrow_upward' : 'arrow_downward'}</span>
        </button>`;
        html += `</div>`;
        html += `</div>`;

        // Filter title
        const filterTitle = this._getFilterTitle();
        html += `<div class="content-header">
            <h1 class="content-title">${C.escapeHtml(filterTitle)}</h1>
            <span class="content-count">${paged.total} contact${paged.total !== 1 ? 's' : ''}</span>
        </div>`;

        // Contact list
        if (paged.contacts.length === 0) {
            html += C.emptyState('person_off', 'No contacts found',
                AppState.searchQuery ? 'Try a different search term.' : 'Create a new contact to get started.',
                AppState.searchQuery ? null : 'Create contact', 'open-create-contact');
        } else {
            // Table header
            html += `<div class="contact-table">`;
            html += `<div class="contact-table-header">
                <div class="ct-col ct-name">Name</div>
                <div class="ct-col ct-email">Email</div>
                <div class="ct-col ct-phone">Phone number</div>
                <div class="ct-col ct-company">Company</div>
                <div class="ct-col ct-labels">Labels</div>
                <div class="ct-col ct-actions"></div>
            </div>`;

            for (const contact of paged.contacts) {
                const name = (contact.firstName + ' ' + contact.lastName).trim();
                const selected = contact.id === AppState.selectedContactId;
                html += `<div class="contact-row ${selected ? 'contact-selected' : ''}" data-contact-id="${contact.id}" data-action="select-contact">`;
                html += `<div class="ct-col ct-name">
                    <div class="ct-name-cell">
                        ${C.avatar(name || contact.email, contact.avatarColor, 32)}
                        <span class="ct-name-text">${C.escapeHtml(name || contact.email)}</span>
                    </div>
                </div>`;
                html += `<div class="ct-col ct-email">${C.escapeHtml(contact.email)}</div>`;
                html += `<div class="ct-col ct-phone">${C.escapeHtml(contact.phone || '')}</div>`;
                html += `<div class="ct-col ct-company">${C.escapeHtml(contact.company || '')}</div>`;
                html += `<div class="ct-col ct-labels">`;
                if (contact.labels) {
                    for (const lblId of contact.labels.slice(0, 3)) {
                        const lbl = AppState.contactLabels.find(l => l.id === lblId);
                        if (lbl) html += C.labelChip(lbl);
                    }
                    if (contact.labels.length > 3) {
                        html += `<span class="label-more">+${contact.labels.length - 3}</span>`;
                    }
                }
                html += `</div>`;
                html += `<div class="ct-col ct-actions">
                    <button class="icon-btn contact-star ${contact.isStarred ? 'starred' : ''}"
                        data-action="toggle-star" data-contact-id="${contact.id}">
                        <span class="material-icons">${contact.isStarred ? 'star' : 'star_border'}</span>
                    </button>
                    <button class="icon-btn" data-action="edit-contact" data-contact-id="${contact.id}">
                        <span class="material-icons">edit</span>
                    </button>
                    <button class="icon-btn" data-action="delete-contact" data-contact-id="${contact.id}">
                        <span class="material-icons">delete</span>
                    </button>
                </div>`;
                html += `</div>`;
            }
            html += `</div>`;
        }

        html += C.pagination(paged.page, paged.totalPages, paged.total);
        html += `</div>`;
        return html;
    },

    _getFilterTitle() {
        if (AppState.contactsFilter === 'all') return 'Contacts';
        if (AppState.contactsFilter === 'starred') return 'Starred';
        if (AppState.contactsFilter === 'frequently') return 'Frequently contacted';
        const label = AppState.contactLabels.find(l => l.id === AppState.contactsFilter);
        return label ? label.name : 'Contacts';
    },

    // ---- Contact Detail Panel ----
    renderContactDetail() {
        const C = Components;
        const contact = AppState.getContactById(AppState.selectedContactId);
        if (!contact) return '';

        const name = (contact.firstName + ' ' + contact.lastName).trim();
        let html = `<div class="detail-panel">`;

        // Header
        html += `<div class="detail-header">
            <button class="icon-btn" data-action="close-detail" title="Close">
                <span class="material-icons">close</span>
            </button>
            <div class="detail-actions">
                <button class="icon-btn" data-action="edit-contact" data-contact-id="${contact.id}" title="Edit">
                    <span class="material-icons">edit</span>
                </button>
                <button class="icon-btn" data-action="delete-contact" data-contact-id="${contact.id}" title="Delete">
                    <span class="material-icons">delete</span>
                </button>
            </div>
        </div>`;

        // Profile
        html += `<div class="detail-profile">
            ${C.avatar(name, contact.avatarColor, 80)}
            <h2 class="detail-name">${C.escapeHtml(name || contact.email)}</h2>
            ${contact.jobTitle ? `<p class="detail-title">${C.escapeHtml(contact.jobTitle)}</p>` : ''}
            ${contact.company ? `<p class="detail-company">${C.escapeHtml(contact.company)}</p>` : ''}
            <button class="icon-btn contact-star ${contact.isStarred ? 'starred' : ''}"
                data-action="toggle-star" data-contact-id="${contact.id}">
                <span class="material-icons">${contact.isStarred ? 'star' : 'star_border'}</span>
            </button>
        </div>`;

        // Contact details
        html += `<div class="detail-section">
            <h3 class="detail-section-title">Contact details</h3>`;

        html += this._detailRow('email', 'Email', contact.email);
        if (contact.secondaryEmail) html += this._detailRow('email', 'Secondary email', contact.secondaryEmail);
        if (contact.phone) html += this._detailRow('phone', 'Phone', contact.phone);
        if (contact.secondaryPhone) html += this._detailRow('phone', 'Secondary phone', contact.secondaryPhone);
        if (contact.address) html += this._detailRow('location_on', 'Address', contact.address);
        if (contact.birthday) html += this._detailRow('cake', 'Birthday', this._formatBirthday(contact.birthday));
        if (contact.website) html += this._detailRow('language', 'Website', contact.website);
        html += `</div>`;

        // Labels
        html += `<div class="detail-section">
            <h3 class="detail-section-title">Labels</h3>
            <div class="detail-labels">`;
        if (contact.labels && contact.labels.length > 0) {
            for (const lblId of contact.labels) {
                const lbl = AppState.contactLabels.find(l => l.id === lblId);
                if (lbl) {
                    html += `<div class="detail-label-chip">
                        ${C.labelChip(lbl)}
                        <button class="icon-btn icon-btn-xs" data-action="remove-label-from-contact"
                            data-contact-id="${contact.id}" data-label-id="${lblId}" title="Remove label">
                            <span class="material-icons">close</span>
                        </button>
                    </div>`;
                }
            }
        }
        html += `<button class="btn btn-text btn-sm" data-action="open-label-picker" data-contact-id="${contact.id}">
            <span class="material-icons btn-icon">label</span> Add label
        </button>`;
        html += `</div></div>`;

        // Notes
        html += `<div class="detail-section">
            <h3 class="detail-section-title">Notes</h3>
            <p class="detail-notes">${C.escapeHtml(contact.notes || 'No notes')}</p>
        </div>`;

        // History
        const history = AppState.getHistoryForContact(contact.id);
        if (history.length > 0) {
            html += `<div class="detail-section">
                <h3 class="detail-section-title">Edit history</h3>
                <div class="detail-history">`;
            for (const h of history.slice(0, 5)) {
                html += `<div class="history-item">
                    <span class="material-icons history-icon">${this._historyIcon(h.action)}</span>
                    <div class="history-info">
                        <span class="history-text">${this._historyText(h)}</span>
                        <span class="history-time">${C.formatDateTime(h.timestamp)}</span>
                    </div>
                </div>`;
            }
            html += `</div></div>`;
        }

        // Metadata
        html += `<div class="detail-section detail-meta">
            <div class="meta-row"><span class="meta-label">Source:</span> <span class="meta-value">${C.escapeHtml(contact.source)}</span></div>
            <div class="meta-row"><span class="meta-label">Created:</span> <span class="meta-value">${C.formatDateTime(contact.createdAt)}</span></div>
            <div class="meta-row"><span class="meta-label">Updated:</span> <span class="meta-value">${C.formatDateTime(contact.updatedAt)}</span></div>
        </div>`;

        html += `</div>`;
        return html;
    },

    _detailRow(icon, label, value) {
        return `<div class="detail-row">
            <span class="material-icons detail-row-icon">${icon}</span>
            <div class="detail-row-content">
                <span class="detail-row-label">${Components.escapeHtml(label)}</span>
                <span class="detail-row-value">${Components.escapeHtml(value)}</span>
            </div>
        </div>`;
    },

    _formatBirthday(dateStr) {
        if (!dateStr) return '';
        const parts = dateStr.split('-');
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return `${months[parseInt(parts[1]) - 1]} ${parseInt(parts[2])}, ${parts[0]}`;
    },

    _historyIcon(action) {
        const icons = { created: 'person_add', edited: 'edit', label_added: 'label', label_removed: 'label_off' };
        return icons[action] || 'history';
    },

    _historyText(h) {
        if (h.action === 'created') return 'Contact created';
        if (h.action === 'edited') return `Changed ${h.field}: "${h.oldValue || ''}" → "${h.newValue || ''}"`;
        if (h.action === 'label_added') return `Added label "${h.newValue}"`;
        if (h.action === 'label_removed') return `Removed label "${h.oldValue}"`;
        return h.action;
    },

    // ---- Other Contacts ----
    renderOtherContacts() {
        const C = Components;
        let html = `<div class="main-content">`;
        html += `<div class="content-header">
            <h1 class="content-title">Other contacts</h1>
            <span class="content-count">${AppState.otherContacts.length} contact${AppState.otherContacts.length !== 1 ? 's' : ''}</span>
        </div>`;
        html += `<p class="content-description">Contacts auto-saved from people you've emailed. You can add them to your contacts or delete them.</p>`;

        if (AppState.otherContacts.length === 0) {
            html += C.emptyState('person_outline', 'No other contacts', 'Auto-saved contacts from email interactions will appear here.');
        } else {
            html += `<div class="other-contacts-list">`;
            const sorted = [...AppState.otherContacts].sort((a, b) =>
                new Date(b.lastInteraction) - new Date(a.lastInteraction));
            for (const contact of sorted) {
                html += C.otherContactCard(contact);
            }
            html += `</div>`;
        }
        html += `</div>`;
        return html;
    },

    // ---- Merge Suggestions ----
    renderMergeSuggestions() {
        const C = Components;
        const suggestions = AppState.mergeSuggestions.filter(s => !s.dismissed);
        let html = `<div class="main-content">`;
        html += `<div class="content-header">
            <h1 class="content-title">Merge & fix</h1>
            <span class="content-count">${suggestions.length} suggestion${suggestions.length !== 1 ? 's' : ''}</span>
        </div>`;

        if (suggestions.length === 0) {
            html += C.emptyState('check_circle', 'All clean!', 'No duplicate contacts found.');
        } else {
            for (const suggestion of suggestions) {
                html += `<div class="merge-card" data-merge-id="${suggestion.id}">
                    <div class="merge-header">
                        <span class="material-icons merge-icon">merge_type</span>
                        <span class="merge-reason">${C.escapeHtml(suggestion.reason)}</span>
                    </div>
                    <div class="merge-contacts">`;
                for (const cId of suggestion.contacts) {
                    const c = AppState.getContactById(cId);
                    if (c) {
                        const name = (c.firstName + ' ' + c.lastName).trim();
                        html += `<div class="merge-contact-item">
                            ${C.avatar(name, c.avatarColor, 32)}
                            <div>
                                <div class="merge-contact-name">${C.escapeHtml(name)}</div>
                                <div class="merge-contact-email">${C.escapeHtml(c.email)}</div>
                            </div>
                        </div>`;
                    }
                }
                html += `</div>`;
                html += `<div class="merge-actions">
                    <button class="btn btn-primary btn-sm" data-action="merge-contacts" data-merge-id="${suggestion.id}">Merge</button>
                    <button class="btn btn-secondary btn-sm" data-action="dismiss-merge" data-merge-id="${suggestion.id}">Dismiss</button>
                </div>`;
                html += `</div>`;
            }
        }
        html += `</div>`;
        return html;
    },

    // ---- Delegates ----
    renderDelegates() {
        const C = Components;
        const settings = AppState.accountSettings;
        let html = `<div class="main-content">`;
        html += `<div class="content-header">
            <h1 class="content-title">Delegate access</h1>
        </div>`;
        html += `<p class="content-description">Grant others access to read, send, and delete emails on your behalf. Delegates cannot use chat or change your password. You can add up to ${settings.collaborationSettings.maxDelegates} delegates.</p>`;

        // Add delegate button
        html += `<div class="section-actions">
            <button class="btn btn-primary" data-action="open-add-delegate">
                <span class="material-icons btn-icon">person_add</span> Add a delegate
            </button>
        </div>`;

        // Delegates list
        if (AppState.delegates.length === 0) {
            html += C.emptyState('supervisor_account', 'No delegates', 'Add a delegate to grant them access to your email.');
        } else {
            html += `<div class="delegates-list">`;
            for (const d of AppState.delegates) {
                html += `<div class="delegate-card" data-delegate-id="${d.id}">
                    <div class="delegate-info">
                        ${C.avatar(d.name, '#757575', 40)}
                        <div class="delegate-details">
                            <div class="delegate-name">${C.escapeHtml(d.name)}</div>
                            <div class="delegate-email">${C.escapeHtml(d.email)}</div>
                            <div class="delegate-meta">Added ${C.formatDate(d.addedAt)}${d.activatedAt ? ' · Activated ' + C.formatDate(d.activatedAt) : ''}</div>
                        </div>
                    </div>
                    <div class="delegate-actions">
                        ${C.statusBadge(d.status)}
                        <button class="icon-btn" data-action="remove-delegate" data-delegate-id="${d.id}" title="Remove delegate">
                            <span class="material-icons">close</span>
                        </button>
                    </div>
                </div>`;
            }
            html += `</div>`;
        }

        // Delegate info
        html += `<div class="info-section">
            <h3 class="info-title">About delegation</h3>
            <div class="info-grid">
                <div class="info-card">
                    <span class="material-icons info-card-icon">check_circle</span>
                    <div class="info-card-content">
                        <strong>What delegates can do:</strong>
                        <ul><li>Read your email</li><li>Send email on your behalf</li><li>Delete email messages</li></ul>
                    </div>
                </div>
                <div class="info-card">
                    <span class="material-icons info-card-icon" style="color:var(--color-danger);">cancel</span>
                    <div class="info-card-content">
                        <strong>What delegates cannot do:</strong>
                        <ul><li>Use Google Chat</li><li>Change your password</li><li>Change account settings</li></ul>
                    </div>
                </div>
                <div class="info-card">
                    <span class="material-icons info-card-icon" style="color:var(--color-warning);">schedule</span>
                    <div class="info-card-content">
                        <strong>Activation:</strong>
                        <p>After adding a delegate, they must confirm. Invitations expire in 1 week. It can take up to 24 hours for access to activate.</p>
                    </div>
                </div>
            </div>
        </div>`;

        html += `</div>`;
        return html;
    },

    // ---- Linked Services ----
    renderLinkedServices() {
        const C = Components;
        let html = `<div class="main-content">`;
        html += `<div class="content-header">
            <h1 class="content-title">Linked Google Services</h1>
        </div>`;
        html += `<p class="content-description">Under the EU's Digital Markets Act (DMA), you can choose which Google services are linked to your account. Linked services can share data to personalize your experience.</p>`;

        // Linkable services
        html += `<div class="section-block">
            <h3 class="section-title">Services you can link or unlink</h3>
            <div class="services-list">`;
        for (const svc of AppState.linkedServices) {
            html += `<div class="service-card" data-service-id="${svc.id}">
                <div class="service-info">
                    <span class="material-icons service-icon">${svc.icon}</span>
                    <div class="service-details">
                        <div class="service-name">${C.escapeHtml(svc.name)}</div>
                        <div class="service-desc">${C.escapeHtml(svc.description)}</div>
                    </div>
                </div>
                <label class="toggle-switch">
                    <input type="checkbox" data-toggle="linked-service" data-service-id="${svc.id}" ${svc.isLinked ? 'checked' : ''}>
                    <span class="toggle-slider"></span>
                </label>
            </div>`;
        }
        html += `</div></div>`;

        // Always linked services
        html += `<div class="section-block">
            <h3 class="section-title">Always linked services</h3>
            <p class="section-description">These services are always linked to your Google Account and cannot be unlinked.</p>
            <div class="services-list services-always-linked">`;
        for (const svc of AppState.alwaysLinkedServices) {
            html += `<div class="service-card service-always-linked">
                <div class="service-info">
                    <span class="material-icons service-icon">check_circle</span>
                    <div class="service-details">
                        <div class="service-name">${C.escapeHtml(svc.name)}</div>
                        <div class="service-desc">${C.escapeHtml(svc.description)}</div>
                    </div>
                </div>
                <span class="service-locked">
                    <span class="material-icons">lock</span> Always linked
                </span>
            </div>`;
        }
        html += `</div></div>`;

        // Info note
        html += `<div class="info-box">
            <span class="material-icons">info</span>
            <p>Regardless of your linking choices, Google may still use data across services for fraud prevention, spam protection, security, and legal compliance. You remain signed into all Google services.</p>
        </div>`;

        html += `</div>`;
        return html;
    },

    // ---- Import & Export ----
    renderImportExport() {
        const C = Components;
        let html = `<div class="main-content">`;
        html += `<div class="content-header">
            <h1 class="content-title">Import & Export</h1>
        </div>`;

        // Import section
        html += `<div class="section-block">
            <h3 class="section-title">Import contacts</h3>
            <p class="section-description">Import contacts from a CSV or vCard file.</p>
            <div class="import-area" data-action="trigger-import">
                <span class="material-icons import-icon">cloud_upload</span>
                <p class="import-text">Click to select a file</p>
                <p class="import-formats">Supported formats: CSV, vCard (.vcf)</p>
            </div>
        </div>`;

        // Export section
        html += `<div class="section-block">
            <h3 class="section-title">Export contacts</h3>
            <p class="section-description">Export your contacts to a file for backup or transfer.</p>
            <div class="export-options">`;
        html += C.dropdown('export-format', [
            { value: 'google_csv', label: 'Google CSV' },
            { value: 'outlook_csv', label: 'Outlook CSV' },
            { value: 'vcard', label: 'vCard (for iOS contacts)' }
        ], 'google_csv', 'Export format');
        html += `<div class="export-scope">`;
        html += `<label class="radio-option"><input type="radio" name="export-scope" value="all" checked data-radio="export-scope"> All contacts (${AppState.contacts.length})</label>`;
        html += `<label class="radio-option"><input type="radio" name="export-scope" value="starred" data-radio="export-scope"> Starred contacts (${AppState.contacts.filter(c => c.isStarred).length})</label>`;
        html += `<label class="radio-option"><input type="radio" name="export-scope" value="label" data-radio="export-scope"> By label</label>`;
        html += `</div>`;
        html += `<button class="btn btn-primary" data-action="export-contacts">
            <span class="material-icons btn-icon">download</span> Export
        </button>`;
        html += `</div></div>`;

        // History
        if (AppState.importExportHistory.length > 0) {
            html += `<div class="section-block">
                <h3 class="section-title">History</h3>
                <div class="ie-history-list">`;
            for (const entry of AppState.importExportHistory.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))) {
                html += `<div class="ie-history-item">
                    <span class="material-icons ie-icon">${entry.type === 'import' ? 'cloud_upload' : 'cloud_download'}</span>
                    <div class="ie-details">
                        <div class="ie-name">${C.escapeHtml(entry.fileName)}</div>
                        <div class="ie-meta">${entry.type === 'import' ? 'Imported' : 'Exported'} ${entry.count} contacts · ${C.formatDate(entry.timestamp)} · ${C.escapeHtml(entry.format)}</div>
                    </div>
                    ${C.statusBadge(entry.status)}
                </div>`;
            }
            html += `</div></div>`;
        }

        html += `</div>`;
        return html;
    },

    // ---- Settings ----
    renderSettings() {
        const C = Components;
        const settings = AppState.accountSettings;
        const user = AppState.currentUser;
        const tab = AppState.settingsTab;
        let html = `<div class="main-content">`;
        html += `<div class="content-header">
            <h1 class="content-title">Settings</h1>
        </div>`;

        // Tab bar
        html += `<div class="tabs">`;
        html += `<button class="tab ${tab === 'general' ? 'tab-active' : ''}" data-action="settings-tab" data-tab="general">General</button>`;
        html += `<button class="tab ${tab === 'account' ? 'tab-active' : ''}" data-action="settings-tab" data-tab="account">Account</button>`;
        html += `<button class="tab ${tab === 'privacy' ? 'tab-active' : ''}" data-action="settings-tab" data-tab="privacy">Privacy</button>`;
        html += `<button class="tab ${tab === 'notifications' ? 'tab-active' : ''}" data-action="settings-tab" data-tab="notifications">Notifications</button>`;
        html += `<button class="tab ${tab === 'sync' ? 'tab-active' : ''}" data-action="settings-tab" data-tab="sync">Sync & Google Sync</button>`;
        html += `</div>`;

        html += `<div class="settings-content">`;

        if (tab === 'general') {
            html += this._renderGeneralSettings(settings);
        } else if (tab === 'account') {
            html += this._renderAccountSettings(user);
        } else if (tab === 'privacy') {
            html += this._renderPrivacySettings(settings);
        } else if (tab === 'notifications') {
            html += this._renderNotificationSettings(settings);
        } else if (tab === 'sync') {
            html += this._renderSyncSettings(settings);
        }

        html += `</div></div>`;
        return html;
    },

    _renderGeneralSettings(settings) {
        const C = Components;
        let html = '';
        html += `<div class="settings-section">
            <h3 class="settings-section-title">Contacts display</h3>`;
        html += C.dropdown('contacts-sort-setting', [
            { value: 'firstName', label: 'First name' },
            { value: 'lastName', label: 'Last name' }
        ], settings.contactsSortBy, 'Sort contacts by');
        html += `<div class="form-field">
            <label class="form-label">Name display order</label>`;
        html += C.dropdown('contacts-display-order', [
            { value: 'firstLast', label: 'First name first (e.g., John Smith)' },
            { value: 'lastFirst', label: 'Last name first (e.g., Smith, John)' }
        ], settings.contactsDisplayOrder, 'Display order');
        html += `</div></div>`;

        html += `<div class="settings-section">
            <h3 class="settings-section-title">Auto-save contacts</h3>
            <p class="settings-description">When enabled, Gmail automatically saves contacts when you send emails to new people.</p>`;
        html += C.toggle('auto-save-contacts', 'Automatically add contacts',
            settings.autoSaveContacts, 'Save contacts from people you email');
        html += `</div>`;

        html += `<div class="settings-section">
            <h3 class="settings-section-title">Collaboration</h3>`;
        html += C.toggle('share-docs-in-email', 'Share Google Docs in email',
            settings.collaborationSettings.shareDocsInEmail, 'Allow sharing and updating permissions for Google Docs directly in Gmail');
        html += C.toggle('show-contact-info', 'Show contact info on emails',
            settings.collaborationSettings.showContactInfo, 'Display sender contact information when viewing emails');
        html += `</div>`;
        return html;
    },

    _renderAccountSettings(user) {
        const C = Components;
        let html = '';
        html += `<div class="settings-section">
            <h3 class="settings-section-title">Your profile</h3>
            <div class="profile-card">
                ${C.avatar(user.name, user.avatarColor, 64)}
                <div class="profile-info">
                    <div class="profile-name">${C.escapeHtml(user.name)}</div>
                    <div class="profile-email">${C.escapeHtml(user.email)}</div>
                </div>
            </div>`;

        html += C.textInput('user-name', 'Name', user.name, 'Your name', true);
        html += C.textInput('user-email', 'Primary email', user.email, '', false, 'email');
        html += `<div class="form-field">
            <label class="form-label">Alternate email addresses</label>`;
        for (let i = 0; i < user.alternateEmails.length; i++) {
            html += `<div class="inline-field">
                <input type="email" class="form-input" value="${C.escapeAttr(user.alternateEmails[i])}" data-alt-email-idx="${i}" disabled>
            </div>`;
        }
        html += `</div>`;
        html += C.textInput('user-phone', 'Phone', user.phone, '+1 (xxx) xxx-xxxx');
        html += C.textInput('user-recovery-email', 'Recovery email', user.recoveryEmail, 'Recovery email address');
        html += C.textInput('user-recovery-phone', 'Recovery phone', user.recoveryPhone, 'Recovery phone number');
        html += `<button class="btn btn-primary" data-action="save-profile">Save changes</button>`;
        html += `</div>`;

        html += `<div class="settings-section">
            <h3 class="settings-section-title">Login & security</h3>`;
        html += C.toggle('remember-password', 'Remember password',
            AppState.accountSettings.loginSettings.rememberPassword,
            'Allow your browser to save your password');
        html += C.toggle('auto-sign-in', 'Auto sign-in',
            AppState.accountSettings.loginSettings.autoSignIn,
            'Automatically sign you in when you visit Gmail');
        html += C.toggle('two-factor-enabled', 'Two-factor authentication',
            AppState.accountSettings.loginSettings.twoFactorEnabled,
            'Require a second step when signing in');

        if (AppState.accountSettings.loginSettings.twoFactorEnabled) {
            html += `<div class="form-field nested-setting">
                <label class="form-label">2FA method</label>`;
            html += C.dropdown('two-factor-method', [
                { value: 'authenticator', label: 'Authenticator app' },
                { value: 'sms', label: 'Text message (SMS)' },
                { value: 'security_key', label: 'Security key' }
            ], AppState.accountSettings.loginSettings.twoFactorMethod);
            html += `</div>`;
        }
        html += `</div>`;

        return html;
    },

    _renderPrivacySettings(settings) {
        const C = Components;
        let html = '';
        html += `<div class="settings-section">
            <h3 class="settings-section-title">Profile visibility</h3>`;

        html += `<div class="form-field">
            <label class="form-label">Who can see your profile photo</label>`;
        html += C.dropdown('privacy-photo', [
            { value: 'everyone', label: 'Everyone' },
            { value: 'contacts_only', label: 'Contacts only' },
            { value: 'nobody', label: 'Nobody' }
        ], settings.privacySettings.showProfilePhoto);
        html += `</div>`;

        html += `<div class="form-field">
            <label class="form-label">Who can see your email address</label>`;
        html += C.dropdown('privacy-email', [
            { value: 'everyone', label: 'Everyone' },
            { value: 'contacts_only', label: 'Contacts only' },
            { value: 'nobody', label: 'Nobody' }
        ], settings.privacySettings.showEmail);
        html += `</div>`;

        html += `<div class="form-field">
            <label class="form-label">Who can see your phone number</label>`;
        html += C.dropdown('privacy-phone', [
            { value: 'everyone', label: 'Everyone' },
            { value: 'contacts_only', label: 'Contacts only' },
            { value: 'nobody', label: 'Nobody' }
        ], settings.privacySettings.showPhone);
        html += `</div>`;

        html += C.toggle('activity-tracking', 'Activity tracking',
            settings.privacySettings.activityTracking,
            'Allow Google to track your activity for personalized recommendations');
        html += `</div>`;

        return html;
    },

    _renderNotificationSettings(settings) {
        const C = Components;
        let html = '';
        html += `<div class="settings-section">
            <h3 class="settings-section-title">Email notifications</h3>`;
        html += C.toggle('notif-delegate-activity', 'Delegate activity',
            settings.notificationSettings.delegateActivity,
            'Get notified when delegates read, send, or delete emails');
        html += C.toggle('notif-contact-changes', 'Contact changes',
            settings.notificationSettings.contactChanges,
            'Get notified when contacts update their information');
        html += C.toggle('notif-security-alerts', 'Security alerts',
            settings.notificationSettings.securityAlerts,
            'Get notified about security events like new sign-ins');
        html += C.toggle('notif-linked-service-updates', 'Linked service updates',
            settings.notificationSettings.linkedServiceUpdates,
            'Get notified about changes to your linked Google services');
        html += `</div>`;
        return html;
    },

    _renderSyncSettings(settings) {
        const C = Components;
        let html = '';

        // Google Sync deprecation warning
        html += `<div class="warning-box">
            <span class="material-icons">warning</span>
            <div>
                <strong>Google Sync has been deprecated</strong>
                <p>Google Sync ended on March 14, 2025. It did not support OAuth, 2-Step Verification, or security keys. If you were using Google Sync, please transition to native Google Account sign-in on your iOS/iPad devices.</p>
            </div>
        </div>`;

        html += `<div class="settings-section">
            <h3 class="settings-section-title">Sync settings</h3>`;
        html += C.toggle('contacts-sync', 'Contacts sync',
            settings.syncSettings.contactsSync,
            'Sync contacts across your devices');
        html += C.toggle('calendar-sync', 'Calendar sync',
            settings.syncSettings.calendarSync,
            'Sync calendar events across your devices');
        html += C.toggle('email-sync', 'Email sync',
            settings.syncSettings.emailSync,
            'Sync email across your devices');
        html += `</div>`;

        html += `<div class="settings-section">
            <h3 class="settings-section-title">Transition from Google Sync</h3>
            <p class="settings-description">If you were previously using Google Sync on iOS/iPad:</p>
            <ol class="transition-steps">
                <li>Go to your device's <strong>Settings</strong> > <strong>Mail</strong> > <strong>Accounts</strong></li>
                <li>Find and remove the Google Sync account</li>
                <li>Tap <strong>Add Account</strong> > <strong>Google</strong></li>
                <li>Sign in with your Google Account</li>
                <li>Enable Mail, Contacts, and Calendar sync</li>
            </ol>`;
        html += C.toggle('google-sync-deprecation-ack', 'I have transitioned off Google Sync',
            settings.syncSettings.googleSyncDeprecationAcknowledged,
            'Acknowledge that you have moved away from Google Sync');
        html += `</div>`;

        return html;
    },

    // ---- Modals ----

    renderCreateContactModal() {
        const C = Components;
        let body = '';
        body += `<div class="modal-form">`;
        body += `<div class="form-row">`;
        body += C.textInput('new-contact-first', 'First name', '', 'First name', true);
        body += C.textInput('new-contact-last', 'Last name', '', 'Last name');
        body += `</div>`;
        body += C.textInput('new-contact-email', 'Email', '', 'email@example.com', true, 'email');
        body += C.textInput('new-contact-phone', 'Phone', '', '+1 (xxx) xxx-xxxx');
        body += C.textInput('new-contact-company', 'Company', '', 'Company name');
        body += C.textInput('new-contact-job', 'Job title', '', 'Job title');
        body += C.textInput('new-contact-address', 'Address', '', 'Street address');
        body += C.textInput('new-contact-secondary-email', 'Secondary email', '', 'Secondary email', false, 'email');
        body += C.textInput('new-contact-secondary-phone', 'Secondary phone', '', 'Secondary phone');
        body += C.textInput('new-contact-birthday', 'Birthday', '', 'YYYY-MM-DD');
        body += C.textInput('new-contact-website', 'Website', '', 'https://...');
        body += C.textarea('new-contact-notes', 'Notes', '', 'Add notes about this contact');

        // Labels checkboxes
        body += `<div class="form-field">
            <label class="form-label">Labels</label>
            <div class="label-checkboxes">`;
        for (const label of AppState.contactLabels) {
            body += `<label class="checkbox-option">
                <input type="checkbox" data-new-contact-label="${label.id}">
                <span class="label-dot" style="background:${label.color}"></span>
                ${C.escapeHtml(label.name)}
            </label>`;
        }
        body += `</div></div>`;
        body += `</div>`;

        const footer = `
            <button class="btn btn-secondary" data-action="close-modal" data-modal="create-contact-modal">Cancel</button>
            <button class="btn btn-primary" data-action="save-new-contact">Save</button>
        `;
        return C.modal('create-contact-modal', 'Create contact', body, footer);
    },

    renderEditContactModal(contact) {
        const C = Components;
        let body = '';
        body += `<div class="modal-form">`;
        body += `<div class="form-row">`;
        body += C.textInput('edit-contact-first', 'First name', contact.firstName, 'First name', true);
        body += C.textInput('edit-contact-last', 'Last name', contact.lastName, 'Last name');
        body += `</div>`;
        body += C.textInput('edit-contact-email', 'Email', contact.email, 'email@example.com', true, 'email');
        body += C.textInput('edit-contact-phone', 'Phone', contact.phone, '+1 (xxx) xxx-xxxx');
        body += C.textInput('edit-contact-company', 'Company', contact.company, 'Company name');
        body += C.textInput('edit-contact-job', 'Job title', contact.jobTitle, 'Job title');
        body += C.textInput('edit-contact-address', 'Address', contact.address, 'Street address');
        body += C.textInput('edit-contact-secondary-email', 'Secondary email', contact.secondaryEmail, 'Secondary email', false, 'email');
        body += C.textInput('edit-contact-secondary-phone', 'Secondary phone', contact.secondaryPhone, 'Secondary phone');
        body += C.textInput('edit-contact-birthday', 'Birthday', contact.birthday, 'YYYY-MM-DD');
        body += C.textInput('edit-contact-website', 'Website', contact.website, 'https://...');
        body += C.textarea('edit-contact-notes', 'Notes', contact.notes, 'Add notes about this contact');

        body += `<div class="form-field">
            <label class="form-label">Labels</label>
            <div class="label-checkboxes">`;
        for (const label of AppState.contactLabels) {
            const checked = contact.labels && contact.labels.includes(label.id) ? 'checked' : '';
            body += `<label class="checkbox-option">
                <input type="checkbox" data-edit-contact-label="${label.id}" ${checked}>
                <span class="label-dot" style="background:${label.color}"></span>
                ${C.escapeHtml(label.name)}
            </label>`;
        }
        body += `</div></div>`;
        body += `</div>`;

        const footer = `
            <button class="btn btn-secondary" data-action="close-modal" data-modal="edit-contact-modal">Cancel</button>
            <button class="btn btn-primary" data-action="save-edited-contact" data-contact-id="${contact.id}">Save</button>
        `;
        return C.modal('edit-contact-modal', 'Edit contact', body, footer);
    },

    renderCreateLabelModal() {
        const C = Components;
        const colors = ['#EA4335', '#34A853', '#4285F4', '#FBBC04', '#FF6D01', '#9C27B0',
            '#009688', '#795548', '#607D8B', '#F44336', '#00BCD4', '#E91E63',
            '#FF9800', '#673AB7', '#2196F3', '#8BC34A', '#CDDC39', '#FF5722'];
        let body = '';
        body += `<div class="modal-form">`;
        body += C.textInput('new-label-name', 'Label name', '', 'Enter label name', true);
        body += `<div class="form-field">
            <label class="form-label">Color</label>
            <div class="color-picker">`;
        for (const color of colors) {
            body += `<button class="color-swatch" data-color="${color}" style="background:${color}" title="${color}"></button>`;
        }
        body += `</div></div>`;
        body += `</div>`;
        const footer = `
            <button class="btn btn-secondary" data-action="close-modal" data-modal="create-label-modal">Cancel</button>
            <button class="btn btn-primary" data-action="save-new-label">Create</button>
        `;
        return C.modal('create-label-modal', 'Create label', body, footer);
    },

    renderEditLabelModal(label) {
        const C = Components;
        const colors = ['#EA4335', '#34A853', '#4285F4', '#FBBC04', '#FF6D01', '#9C27B0',
            '#009688', '#795548', '#607D8B', '#F44336', '#00BCD4', '#E91E63',
            '#FF9800', '#673AB7', '#2196F3', '#8BC34A', '#CDDC39', '#FF5722'];
        let body = '';
        body += `<div class="modal-form">`;
        body += C.textInput('edit-label-name', 'Label name', label.name, 'Enter label name', true);
        body += `<div class="form-field">
            <label class="form-label">Color</label>
            <div class="color-picker">`;
        for (const color of colors) {
            const selected = color === label.color ? ' color-selected' : '';
            body += `<button class="color-swatch${selected}" data-color="${color}" style="background:${color}" title="${color}"></button>`;
        }
        body += `</div></div>`;
        body += `</div>`;
        const footer = `
            <button class="btn btn-danger" data-action="delete-label" data-label-id="${label.id}" style="margin-right:auto">Delete</button>
            <button class="btn btn-secondary" data-action="close-modal" data-modal="edit-label-modal">Cancel</button>
            <button class="btn btn-primary" data-action="save-edited-label" data-label-id="${label.id}">Save</button>
        `;
        return C.modal('edit-label-modal', 'Edit label', body, footer);
    },

    renderAddDelegateModal() {
        const C = Components;
        const activeCount = AppState.delegates.filter(d => d.status === 'active' || d.status === 'pending').length;
        const maxDelegates = AppState.accountSettings.collaborationSettings.maxDelegates;
        let body = '';
        body += `<div class="modal-form">`;
        if (activeCount >= maxDelegates) {
            body += `<div class="error-box">You have reached the maximum number of delegates (${maxDelegates}).</div>`;
        } else {
            body += `<p class="modal-description">Enter the Gmail address of the person you'd like to add as a delegate. They'll need to confirm the invitation within 1 week.</p>`;
            body += C.textInput('delegate-email', 'Email address', '', 'name@gmail.com', true, 'email');
            body += C.textInput('delegate-name', 'Name (optional)', '', 'Delegate name');
            body += `<div class="info-box info-box-sm">
                <span class="material-icons">info</span>
                <p>Identity verification may be required. It can take up to 24 hours for delegate access to activate after confirmation.</p>
            </div>`;
        }
        body += `</div>`;
        const footer = activeCount >= maxDelegates ? `
            <button class="btn btn-secondary" data-action="close-modal" data-modal="add-delegate-modal">Close</button>
        ` : `
            <button class="btn btn-secondary" data-action="close-modal" data-modal="add-delegate-modal">Cancel</button>
            <button class="btn btn-primary" data-action="save-new-delegate">Add delegate</button>
        `;
        return C.modal('add-delegate-modal', 'Add a delegate', body, footer);
    },

    renderLabelPickerModal(contactId) {
        const C = Components;
        const contact = AppState.getContactById(contactId);
        if (!contact) return '';
        let body = `<div class="label-picker-list">`;
        for (const label of AppState.contactLabels) {
            const checked = contact.labels && contact.labels.includes(label.id) ? 'checked' : '';
            body += `<label class="label-picker-item">
                <input type="checkbox" data-label-picker="${label.id}" data-contact-id="${contactId}" ${checked}>
                <span class="label-dot" style="background:${label.color}"></span>
                <span>${C.escapeHtml(label.name)}</span>
            </label>`;
        }
        body += `</div>`;
        const footer = `<button class="btn btn-primary" data-action="close-modal" data-modal="label-picker-modal">Done</button>`;
        return C.modal('label-picker-modal', 'Manage labels', body, footer);
    },

    // ---- Top Bar ----
    renderTopBar() {
        const C = Components;
        const user = AppState.currentUser;
        let html = `<div class="topbar">`;
        html += `<div class="topbar-left">
            <button class="icon-btn" data-action="toggle-sidebar" title="Menu">
                <span class="material-icons">menu</span>
            </button>
            <div class="topbar-brand">
                <span class="material-icons topbar-logo-icon" style="color:#4285F4;">contacts</span>
                <span class="topbar-app-name">Contacts</span>
            </div>
        </div>`;
        html += `<div class="topbar-center">`;
        html += C.searchBar('global-search', '', 'Search contacts');
        html += `</div>`;
        html += `<div class="topbar-right">
            <button class="icon-btn" data-action="open-help" title="Help">
                <span class="material-icons">help_outline</span>
            </button>
            <button class="icon-btn" data-action="open-settings-menu" title="Settings">
                <span class="material-icons">settings</span>
            </button>
            <div class="topbar-profile" data-action="toggle-profile-menu">
                ${C.avatar(user.name, user.avatarColor, 32)}
            </div>
        </div>`;
        html += `</div>`;
        return html;
    }
};

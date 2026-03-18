/* views.js — View renderers for Gmail Accounts & Contacts */

const Views = {

    renderSidebar() {
        const v = AppState.currentView;
        const contactCount = AppState.contacts.length;
        const starredCount = AppState.getStarredContacts().length;
        const otherCount = AppState.otherContacts.length;
        const groupsHtml = AppState.contactGroups.map(g => {
            const count = AppState.getContactsForGroup(g.id).length;
            const active = (v === 'contacts' && AppState.contactFilter === g.id) || (v === 'group-detail' && AppState.currentGroupId === g.id);
            return `<a class="nav-item nav-sub${active ? ' active' : ''}" data-route="contacts" data-filter="${Components.escapeAttr(g.id)}" data-testid="nav-group-${Components.escapeAttr(g.id)}">
                <span class="nav-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
                <span class="nav-label">${Components.escapeHtml(g.name)}</span>
                <span class="nav-count">${count}</span>
            </a>`;
        }).join('');

        return `
            <div class="nav-section">
                <div class="nav-section-title">Contacts</div>
                ${this._navItem('contacts', 'all', 'All Contacts', this._iconContacts(), contactCount, v === 'contacts' && AppState.contactFilter === 'all')}
                ${this._navItem('contacts', 'starred', 'Starred', this._iconStar(), starredCount, v === 'contacts' && AppState.contactFilter === 'starred')}
                <div class="nav-group-header">
                    <span>Labels</span>
                    <button class="nav-group-add" data-action="new-group" data-testid="new-group-btn" title="Create label">+</button>
                </div>
                ${groupsHtml}
            </div>
            <div class="nav-section">
                <div class="nav-section-title">Other</div>
                ${this._navItemSimple('other-contacts', 'Other contacts', this._iconOther(), otherCount, v === 'other-contacts')}
                ${this._navItemSimple('directory', 'Directory', this._iconDirectory(), AppState.directory.length, v === 'directory')}
            </div>
            <div class="nav-section">
                <div class="nav-section-title">Settings</div>
                ${this._navItemSimple('account', 'Account', this._iconAccount(), null, v === 'account')}
                ${this._navItemSimple('send-mail-as', 'Send mail as', this._iconSendAs(), null, v === 'send-mail-as')}
                ${this._navItemSimple('delegation', 'Delegation', this._iconDelegation(), null, v === 'delegation')}
                ${this._navItemSimple('import-export', 'Import/Export', this._iconImport(), null, v === 'import-export')}
            </div>
        `;
    },

    _navItem(route, filter, label, icon, count, active) {
        return `<a class="nav-item${active ? ' active' : ''}" data-route="${Components.escapeAttr(route)}" data-filter="${Components.escapeAttr(filter)}" data-testid="nav-${Components.escapeAttr(filter)}">
            <span class="nav-icon">${icon}</span>
            <span class="nav-label">${Components.escapeHtml(label)}</span>
            ${count != null ? `<span class="nav-count">${count}</span>` : ''}
        </a>`;
    },

    _navItemSimple(route, label, icon, count, active) {
        return `<a class="nav-item${active ? ' active' : ''}" data-route="${Components.escapeAttr(route)}" data-testid="nav-${Components.escapeAttr(route)}">
            <span class="nav-icon">${icon}</span>
            <span class="nav-label">${Components.escapeHtml(label)}</span>
            ${count != null ? `<span class="nav-count">${count}</span>` : ''}
        </a>`;
    },

    // ─── Content dispatcher ───
    renderContent() {
        switch (AppState.currentView) {
            case 'contacts': return AppState.currentContactId ? this.renderContactDetail() : this.renderContactList();
            case 'contact-detail': return this.renderContactDetail();
            case 'new-contact': return this.renderContactForm();
            case 'edit-contact': return this.renderContactForm(AppState.currentContactId);
            case 'group-detail': return this.renderGroupDetail();
            case 'other-contacts': return this.renderOtherContacts();
            case 'directory': return this.renderDirectory();
            case 'merge-duplicates': return this.renderMergeDuplicates();
            case 'account': return this.renderAccountSettings();
            case 'send-mail-as': return this.renderSendMailAs();
            case 'delegation': return this.renderDelegation();
            case 'import-export': return this.renderImportExport();
            default: return this.renderContactList();
        }
    },

    // ─── Contact List ───
    renderContactList() {
        const contacts = AppState.getFilteredContacts();
        const total = contacts.length;
        const page = AppState.currentPage;
        const pageSize = AppState.pageSize;
        const paged = contacts.slice((page - 1) * pageSize, page * pageSize);
        const selected = AppState.selectedContactIds;
        const allOnPageSelected = paged.length > 0 && paged.every(c => selected.includes(c.id));

        let filterLabel = 'All Contacts';
        if (AppState.contactFilter === 'starred') {
            filterLabel = 'Starred';
        } else if (AppState.contactFilter !== 'all') {
            const grp = AppState.getGroupById(AppState.contactFilter);
            if (grp) filterLabel = grp.name;
        }

        let html = '<div class="content-header">';
        html += `<h1>${Components.escapeHtml(filterLabel)} <span class="count-label">(${total})</span></h1>`;
        html += '<div class="header-actions">';
        html += '<button class="btn btn-secondary" data-action="merge-duplicates" data-testid="merge-duplicates-btn">Merge duplicates</button>';
        html += '<button class="btn btn-primary" data-action="new-contact" data-testid="new-contact-btn">+ Create contact</button>';
        html += '</div></div>';

        // Toolbar
        html += '<div class="toolbar">';
        html += `<div class="search-box"><input type="text" class="form-input search-input" id="contactSearch" placeholder="Search contacts..." value="${Components.escapeAttr(AppState.searchQuery)}" data-testid="contact-search"></div>`;
        html += '<div class="toolbar-right">';
        html += Components.dropdown('sortDropdown', [
            { value: 'firstName', label: 'First name' },
            { value: 'lastName', label: 'Last name' },
            { value: 'email', label: 'Email' },
            { value: 'recentlyAdded', label: 'Recently added' }
        ], AppState.contactSort, 'Sort by');
        html += '</div></div>';

        // Bulk actions bar
        if (selected.length > 0) {
            html += '<div class="bulk-actions">';
            html += `<span>${selected.length} selected</span>`;
            html += '<button class="btn btn-sm" data-action="bulk-add-to-group" data-testid="bulk-add-group">Add to label</button>';
            html += '<button class="btn btn-sm btn-danger" data-action="bulk-delete" data-testid="bulk-delete">Delete</button>';
            html += '<button class="btn btn-sm" data-action="clear-selection">Clear</button>';
            html += '</div>';
        }

        if (paged.length === 0) {
            html += Components.emptyState(this._iconContacts(), 'No contacts found',
                AppState.searchQuery ? 'Try a different search term' : 'Create your first contact');
        } else {
            html += '<div class="contact-table">';
            html += '<div class="contact-table-header">';
            html += `<div class="col-check"><input type="checkbox" data-action="select-all-page" ${allOnPageSelected ? 'checked' : ''} data-testid="select-all"></div>`;
            html += '<div class="col-name">Name</div>';
            html += '<div class="col-email">Email</div>';
            html += '<div class="col-phone">Phone</div>';
            html += '<div class="col-company">Company / Title</div>';
            html += '<div class="col-labels">Labels</div>';
            html += '</div>';

            paged.forEach(c => {
                html += this._renderContactRow(c, selected.includes(c.id));
            });
            html += '</div>';
        }

        html += Components.pagination(page, total, pageSize);
        return html;
    },

    _renderContactRow(c, isSelected) {
        const name = ((c.firstName || '') + ' ' + (c.lastName || '')).trim() || c.email;
        const color = Components.getAvatarColor(name);
        const groups = (c.groups || []).map(gid => AppState.getGroupById(gid)).filter(Boolean);
        const groupBadges = groups.slice(0, 3).map(g => Components.groupBadge(g)).join('');
        const moreGroups = groups.length > 3 ? `<span class="more-badge">+${groups.length - 3}</span>` : '';

        let html = `<div class="contact-row${isSelected ? ' selected' : ''}" data-contact-id="${Components.escapeAttr(c.id)}" data-testid="contact-row-${Components.escapeAttr(c.id)}">`;
        html += `<div class="col-check"><input type="checkbox" data-action="toggle-select" data-id="${Components.escapeAttr(c.id)}" ${isSelected ? 'checked' : ''}></div>`;
        html += `<div class="col-name"><div class="contact-name-cell">${Components.avatar(name, 28, color)}`;
        html += `<span class="contact-name-text">${Components.escapeHtml(name)}</span>`;
        if (c.starred) html += '<span class="star-icon filled" data-action="toggle-star" data-id="' + Components.escapeAttr(c.id) + '">&#9733;</span>';
        else html += '<span class="star-icon" data-action="toggle-star" data-id="' + Components.escapeAttr(c.id) + '">&#9734;</span>';
        html += '</div></div>';
        html += `<div class="col-email">${Components.escapeHtml(c.email || '')}</div>`;
        html += `<div class="col-phone">${Components.escapeHtml(c.phone || '')}</div>`;
        html += `<div class="col-company">${Components.escapeHtml(c.company || '')}${c.jobTitle ? '<br><small>' + Components.escapeHtml(c.jobTitle) + '</small>' : ''}</div>`;
        html += `<div class="col-labels">${groupBadges}${moreGroups}</div>`;
        html += '</div>';
        return html;
    },

    // ─── Contact Detail ───
    renderContactDetail() {
        const c = AppState.getContactById(AppState.currentContactId);
        if (!c) return Components.emptyState('', 'Contact not found', 'This contact may have been deleted.');

        const name = ((c.firstName || '') + ' ' + (c.lastName || '')).trim() || c.email;
        const color = Components.getAvatarColor(name);
        const groups = (c.groups || []).map(gid => AppState.getGroupById(gid)).filter(Boolean);

        let html = '<div class="content-header">';
        html += '<div class="breadcrumb"><a data-route="contacts" data-filter="all">Contacts</a> / <span>' + Components.escapeHtml(name) + '</span></div>';
        html += '</div>';

        html += '<div class="contact-detail">';
        html += '<div class="contact-detail-header">';
        html += Components.avatar(name, 80, color);
        html += '<div class="contact-detail-title">';
        html += `<h1>${Components.escapeHtml(name)}`;
        if (c.starred) html += ' <span class="star-icon filled" data-action="toggle-star" data-id="' + Components.escapeAttr(c.id) + '">&#9733;</span>';
        else html += ' <span class="star-icon" data-action="toggle-star" data-id="' + Components.escapeAttr(c.id) + '">&#9734;</span>';
        html += '</h1>';
        if (c.company || c.jobTitle) {
            html += '<p class="contact-subtitle">';
            if (c.jobTitle) html += Components.escapeHtml(c.jobTitle);
            if (c.jobTitle && c.company) html += ' at ';
            if (c.company) html += Components.escapeHtml(c.company);
            html += '</p>';
        }
        html += '</div>';
        html += '<div class="contact-detail-actions">';
        html += `<button class="btn btn-primary" data-action="edit-contact" data-id="${Components.escapeAttr(c.id)}" data-testid="edit-contact-btn">Edit</button>`;
        html += `<button class="btn btn-danger" data-action="delete-contact" data-id="${Components.escapeAttr(c.id)}" data-testid="delete-contact-btn">Delete</button>`;
        html += '</div></div>';

        html += '<div class="detail-grid">';

        // Contact info
        html += '<div class="detail-section"><h3>Contact Information</h3>';
        html += '<div class="detail-fields">';
        if (c.email) html += this._detailField('Email', c.email);
        if (c.phone) html += this._detailField('Phone', c.phone);
        if (c.address) html += this._detailField('Address', c.address);
        if (c.birthday) html += this._detailField('Birthday', Components.formatDate(c.birthday + 'T00:00:00Z'));
        html += '</div></div>';

        // Labels
        html += '<div class="detail-section"><h3>Labels</h3>';
        if (groups.length > 0) {
            html += '<div class="detail-labels">' + groups.map(g => Components.groupBadge(g)).join('') + '</div>';
        } else {
            html += '<p class="text-muted">No labels assigned</p>';
        }
        html += '</div>';

        // Notes
        if (c.notes) {
            html += '<div class="detail-section"><h3>Notes</h3>';
            html += `<p>${Components.escapeHtml(c.notes)}</p></div>`;
        }

        // Metadata
        html += '<div class="detail-section"><h3>Details</h3>';
        html += '<div class="detail-fields">';
        html += this._detailField('Created', Components.formatDateTime(c.createdAt));
        html += this._detailField('Updated', Components.timeAgo(c.updatedAt));
        html += '</div></div>';

        html += '</div></div>';
        return html;
    },

    _detailField(label, value) {
        return `<div class="detail-field"><span class="detail-label">${Components.escapeHtml(label)}</span><span class="detail-value">${Components.escapeHtml(value)}</span></div>`;
    },

    // ─── Contact Form ───
    renderContactForm(contactId) {
        const c = contactId ? AppState.getContactById(contactId) : null;
        const title = c ? 'Edit Contact' : 'New Contact';
        const breadcrumb = c ? `<a data-route="contacts" data-filter="all">Contacts</a> / <a data-route="contact-detail" data-id="${Components.escapeAttr(c.id)}">${Components.escapeHtml((c.firstName + ' ' + c.lastName).trim())}</a> / Edit` :
            '<a data-route="contacts" data-filter="all">Contacts</a> / New';

        let html = '<div class="content-header"><div class="breadcrumb">' + breadcrumb + '</div></div>';
        html += `<div class="form-container"><h2>${Components.escapeHtml(title)}</h2>`;
        html += '<div class="form-grid">';
        html += '<div class="form-row two-col">';
        html += '<div class="form-field">' + Components.textInput('firstName', c ? c.firstName : '', 'First name', 'First name') + '</div>';
        html += '<div class="form-field">' + Components.textInput('lastName', c ? c.lastName : '', 'Last name', 'Last name') + '</div>';
        html += '</div>';
        html += '<div class="form-field">' + Components.textInput('contactEmail', c ? c.email : '', 'email@example.com', 'Email *') + '</div>';
        html += '<div class="form-field">' + Components.textInput('contactPhone', c ? c.phone : '', '+1 (555) 123-4567', 'Phone') + '</div>';
        html += '<div class="form-row two-col">';
        html += '<div class="form-field">' + Components.textInput('contactCompany', c ? c.company : '', 'Company name', 'Company') + '</div>';
        html += '<div class="form-field">' + Components.textInput('contactJobTitle', c ? c.jobTitle : '', 'Job title', 'Job title') + '</div>';
        html += '</div>';
        html += '<div class="form-field">' + Components.textInput('contactAddress', c ? c.address : '', 'Full address', 'Address') + '</div>';
        html += '<div class="form-field">' + Components.textInput('contactBirthday', c ? c.birthday : '', 'YYYY-MM-DD', 'Birthday') + '</div>';
        html += '<div class="form-field">' + Components.textarea('contactNotes', c ? c.notes : '', 'Add notes...', 'Notes') + '</div>';

        // Group checkboxes
        html += '<div class="form-field"><label class="form-label">Labels</label><div class="checkbox-grid">';
        AppState.contactGroups.forEach(g => {
            const checked = c && c.groups && c.groups.includes(g.id);
            html += Components.checkbox('group-' + g.id, checked, g.name);
        });
        html += '</div></div>';

        html += '</div>';
        html += '<div class="form-actions">';
        html += '<button class="btn btn-secondary" data-action="cancel-form">Cancel</button>';
        html += `<button class="btn btn-primary" data-action="save-contact" data-id="${Components.escapeAttr(contactId || '')}" data-testid="save-contact-btn">Save</button>`;
        html += '</div></div>';

        return html;
    },

    // ─── Group Detail ───
    renderGroupDetail() {
        const g = AppState.getGroupById(AppState.currentGroupId);
        if (!g) return Components.emptyState('', 'Label not found', '');

        const contacts = AppState.getContactsForGroup(g.id);

        let html = '<div class="content-header">';
        html += `<div class="breadcrumb"><a data-route="contacts" data-filter="all">Contacts</a> / ${Components.escapeHtml(g.name)}</div>`;
        html += '<div class="header-actions">';
        html += `<button class="btn btn-sm" data-action="rename-group" data-id="${Components.escapeAttr(g.id)}" data-testid="rename-group-btn">Rename</button>`;
        html += `<button class="btn btn-sm btn-danger" data-action="delete-group" data-id="${Components.escapeAttr(g.id)}" data-testid="delete-group-btn">Delete</button>`;
        html += '</div></div>';

        html += `<h2>${Components.escapeHtml(g.name)} <span class="count-label">(${contacts.length} contacts)</span></h2>`;

        if (contacts.length === 0) {
            html += Components.emptyState('', 'No contacts in this label', 'Add contacts to this label from the contact list');
        } else {
            html += '<div class="contact-table"><div class="contact-table-header">';
            html += '<div class="col-name">Name</div>';
            html += '<div class="col-email">Email</div>';
            html += '<div class="col-phone">Phone</div>';
            html += '<div class="col-company">Company</div>';
            html += '<div class="col-actions">Actions</div>';
            html += '</div>';
            contacts.forEach(c => {
                const name = ((c.firstName || '') + ' ' + (c.lastName || '')).trim() || c.email;
                const color = Components.getAvatarColor(name);
                html += `<div class="contact-row" data-contact-id="${Components.escapeAttr(c.id)}">`;
                html += `<div class="col-name"><div class="contact-name-cell">${Components.avatar(name, 28, color)}<span class="contact-name-text">${Components.escapeHtml(name)}</span></div></div>`;
                html += `<div class="col-email">${Components.escapeHtml(c.email || '')}</div>`;
                html += `<div class="col-phone">${Components.escapeHtml(c.phone || '')}</div>`;
                html += `<div class="col-company">${Components.escapeHtml(c.company || '')}</div>`;
                html += `<div class="col-actions"><button class="btn btn-sm btn-danger" data-action="remove-from-group" data-contact-id="${Components.escapeAttr(c.id)}" data-group-id="${Components.escapeAttr(g.id)}">Remove</button></div>`;
                html += '</div>';
            });
            html += '</div>';
        }
        return html;
    },

    // ─── Other Contacts ───
    renderOtherContacts() {
        const contacts = AppState.getFilteredOtherContacts();

        let html = '<div class="content-header"><h1>Other Contacts <span class="count-label">(' + contacts.length + ')</span></h1></div>';
        html += '<p class="section-description">People you\'ve interacted with via email who aren\'t in your contacts.</p>';
        html += `<div class="toolbar"><div class="search-box"><input type="text" class="form-input search-input" id="otherContactSearch" placeholder="Search other contacts..." value="${Components.escapeAttr(AppState.otherContactSearch)}" data-testid="other-contact-search"></div></div>`;

        if (contacts.length === 0) {
            html += Components.emptyState('', 'No other contacts found', '');
        } else {
            html += '<div class="contact-table"><div class="contact-table-header">';
            html += '<div class="col-name">Name / Email</div>';
            html += '<div class="col-interactions">Interactions</div>';
            html += '<div class="col-last-contact">Last interaction</div>';
            html += '<div class="col-actions">Actions</div>';
            html += '</div>';
            contacts.forEach(c => {
                const displayName = ((c.firstName || '') + ' ' + (c.lastName || '')).trim() || c.email;
                const color = Components.getAvatarColor(c.email);
                html += `<div class="contact-row" data-other-contact-id="${Components.escapeAttr(c.id)}">`;
                html += `<div class="col-name"><div class="contact-name-cell">${Components.avatar(displayName, 28, color)}<div><span class="contact-name-text">${Components.escapeHtml(displayName)}</span>`;
                if (displayName !== c.email) html += `<br><small class="text-muted">${Components.escapeHtml(c.email)}</small>`;
                html += '</div></div></div>';
                html += `<div class="col-interactions">${c.interactionCount} emails</div>`;
                html += `<div class="col-last-contact">${Components.timeAgo(c.lastInteraction)}</div>`;
                html += '<div class="col-actions">';
                html += `<button class="btn btn-sm btn-primary" data-action="promote-other" data-id="${Components.escapeAttr(c.id)}" data-testid="promote-${Components.escapeAttr(c.id)}">Add to contacts</button>`;
                html += `<button class="btn btn-sm btn-danger" data-action="delete-other" data-id="${Components.escapeAttr(c.id)}">Delete</button>`;
                html += '</div></div>';
            });
            html += '</div>';
        }
        return html;
    },

    // ─── Directory ───
    renderDirectory() {
        const entries = AppState.getFilteredDirectory();
        const departments = [...new Set(AppState.directory.map(d => d.department))].sort();

        let html = '<div class="content-header"><h1>Directory <span class="count-label">(' + entries.length + ')</span></h1></div>';
        html += '<p class="section-description">Your organization\'s directory at TechCorp.</p>';
        html += `<div class="toolbar"><div class="search-box"><input type="text" class="form-input search-input" id="directorySearch" placeholder="Search by name, email, department..." value="${Components.escapeAttr(AppState.directorySearch)}" data-testid="directory-search"></div></div>`;

        if (entries.length === 0) {
            html += Components.emptyState('', 'No results found', 'Try a different search term');
        } else {
            html += '<div class="contact-table"><div class="contact-table-header">';
            html += '<div class="col-name">Name</div>';
            html += '<div class="col-email">Email</div>';
            html += '<div class="col-dept">Department</div>';
            html += '<div class="col-title">Title</div>';
            html += '<div class="col-location">Location</div>';
            html += '</div>';
            entries.forEach(d => {
                const color = Components.getAvatarColor(d.name);
                html += '<div class="contact-row directory-row">';
                html += `<div class="col-name"><div class="contact-name-cell">${Components.avatar(d.name, 28, color)}<span class="contact-name-text">${Components.escapeHtml(d.name)}</span></div></div>`;
                html += `<div class="col-email">${Components.escapeHtml(d.email)}</div>`;
                html += `<div class="col-dept"><span class="dept-badge">${Components.escapeHtml(d.department)}</span></div>`;
                html += `<div class="col-title">${Components.escapeHtml(d.title)}</div>`;
                html += `<div class="col-location">${Components.escapeHtml(d.location)}</div>`;
                html += '</div>';
            });
            html += '</div>';
        }
        return html;
    },

    // ─── Account Settings ───
    renderAccountSettings() {
        const u = AppState.currentUser;
        let html = '<div class="content-header"><h1>Account Settings</h1></div>';
        html += '<div class="settings-container">';

        // Profile info
        html += '<div class="settings-section">';
        html += '<h2>Google Account</h2>';
        html += '<div class="settings-card">';
        html += '<div class="profile-header">';
        html += Components.avatar(u.firstName + ' ' + u.lastName, 64, '#1a73e8');
        html += '<div class="profile-info">';
        html += `<h3>${Components.escapeHtml(u.firstName + ' ' + u.lastName)}</h3>`;
        html += `<p class="text-muted">${Components.escapeHtml(u.email)}</p>`;
        html += '</div></div>';
        html += '<div class="settings-fields">';
        html += this._settingsField('Name', u.firstName + ' ' + u.lastName, 'edit-name');
        html += this._settingsField('Email', u.email, null);
        html += this._settingsField('Recovery email', u.recoveryEmail || 'Not set', 'edit-recovery-email');
        html += this._settingsField('Recovery phone', u.recoveryPhone || 'Not set', 'edit-recovery-phone');
        html += '</div></div></div>';

        // Security
        html += '<div class="settings-section">';
        html += '<h2>Sign-in &amp; Security</h2>';
        html += '<div class="settings-card">';
        html += '<div class="settings-fields">';
        html += this._settingsField('Password', 'Last changed ' + Components.formatDate(u.lastPasswordChange), 'change-password');
        html += `<div class="settings-field-row"><span class="settings-field-label">2-Step Verification</span><span class="settings-field-value">${u.twoStepVerification ? '<span class="badge badge-success">On</span>' : '<span class="badge badge-warning">Off</span>'}</span><button class="btn btn-sm" data-action="toggle-2sv" data-testid="toggle-2sv-btn">${u.twoStepVerification ? 'Turn off' : 'Turn on'}</button></div>`;
        html += '</div></div>';

        // App Passwords
        html += '<div class="settings-card">';
        html += '<h3>App Passwords</h3>';
        html += '<p class="text-muted">App-specific passwords for third-party mail clients.</p>';
        if (AppState.appPasswords.length > 0) {
            html += '<div class="app-password-list">';
            AppState.appPasswords.forEach(ap => {
                html += `<div class="app-password-item" data-testid="app-password-${Components.escapeAttr(ap.id)}">`;
                html += `<div><strong>${Components.escapeHtml(ap.name)}</strong><br><small class="text-muted">Created ${Components.formatDate(ap.createdAt)}${ap.lastUsed ? ' &middot; Last used ' + Components.timeAgo(ap.lastUsed) : ''}</small></div>`;
                html += `<button class="btn btn-sm btn-danger" data-action="delete-app-password" data-id="${Components.escapeAttr(ap.id)}">Revoke</button>`;
                html += '</div>';
            });
            html += '</div>';
        }
        html += '<button class="btn btn-sm btn-primary" data-action="new-app-password" data-testid="new-app-password-btn">Generate app password</button>';
        html += '</div></div>';

        html += '</div>';
        return html;
    },

    _settingsField(label, value, action) {
        let html = '<div class="settings-field-row">';
        html += `<span class="settings-field-label">${Components.escapeHtml(label)}</span>`;
        html += `<span class="settings-field-value">${value}</span>`;
        if (action) {
            html += `<button class="btn btn-sm" data-action="${Components.escapeAttr(action)}" data-testid="${Components.escapeAttr(action)}-btn">Edit</button>`;
        }
        html += '</div>';
        return html;
    },

    // ─── Send Mail As ───
    renderSendMailAs() {
        let html = '<div class="content-header"><h1>Send Mail As</h1></div>';
        html += '<div class="settings-container">';

        // Reply-from setting
        html += '<div class="settings-section">';
        html += '<h2>When replying to a message</h2>';
        html += '<div class="settings-card">';
        html += Components.radioGroup('replyFrom', [
            { value: 'default', label: 'Always reply from default address', description: 'Replies will always come from your default "From" address' },
            { value: 'same', label: 'Reply from the same address the message was sent to', description: 'Replies will use the address the original message was delivered to' }
        ], AppState.replyFromSetting);
        html += '</div></div>';

        // Aliases list
        html += '<div class="settings-section">';
        html += '<h2>Email Addresses</h2>';
        html += '<p class="section-description">You can send mail as any of these addresses.</p>';
        html += '<div class="alias-list">';
        AppState.aliases.forEach(a => {
            html += `<div class="alias-item${a.isDefault ? ' alias-default' : ''}" data-testid="alias-${Components.escapeAttr(a.id)}">`;
            html += '<div class="alias-info">';
            html += `<strong>${Components.escapeHtml(a.name)}</strong> &lt;${Components.escapeHtml(a.email)}&gt;`;
            if (a.isPrimary) html += ' <span class="badge badge-default">Primary</span>';
            if (a.isDefault) html += ' <span class="badge badge-success">Default</span>';
            if (a.smtpServer) html += `<br><small class="text-muted">via ${Components.escapeHtml(a.smtpServer)}:${Components.escapeHtml(a.smtpPort)}</small>`;
            html += '</div>';
            html += '<div class="alias-actions">';
            if (!a.isDefault) html += `<button class="btn btn-sm" data-action="set-default-alias" data-id="${Components.escapeAttr(a.id)}" data-testid="default-${Components.escapeAttr(a.id)}">Make default</button>`;
            if (!a.isPrimary) {
                html += `<button class="btn btn-sm" data-action="edit-alias" data-id="${Components.escapeAttr(a.id)}" data-testid="edit-alias-${Components.escapeAttr(a.id)}">Edit</button>`;
                html += `<button class="btn btn-sm btn-danger" data-action="delete-alias" data-id="${Components.escapeAttr(a.id)}" data-testid="delete-alias-${Components.escapeAttr(a.id)}">Remove</button>`;
            }
            html += '</div></div>';
        });
        html += '</div>';
        html += '<button class="btn btn-primary" data-action="new-alias" data-testid="new-alias-btn">Add another email address</button>';
        html += '</div></div>';

        return html;
    },

    // ─── Delegation ───
    renderDelegation() {
        let html = '<div class="content-header"><h1>Email Delegation</h1></div>';
        html += '<div class="settings-container">';
        html += '<p class="section-description">Grant other people access to read, send, and delete messages on your behalf. Delegates can also manage your contacts.</p>';

        html += '<div class="settings-section">';
        html += '<h2>Delegates</h2>';
        if (AppState.delegates.length === 0) {
            html += '<p class="text-muted">No delegates configured.</p>';
        } else {
            html += '<div class="delegate-list">';
            AppState.delegates.forEach(d => {
                html += `<div class="delegate-item" data-testid="delegate-${Components.escapeAttr(d.id)}">`;
                html += '<div class="delegate-info">';
                html += `${Components.avatar(d.name, 32, Components.getAvatarColor(d.name))}`;
                html += `<div><strong>${Components.escapeHtml(d.name)}</strong><br><small class="text-muted">${Components.escapeHtml(d.email)}</small></div>`;
                html += '</div>';
                html += `<div class="delegate-status">${Components.statusBadge(d.status)}</div>`;
                html += `<button class="btn btn-sm btn-danger" data-action="remove-delegate" data-id="${Components.escapeAttr(d.id)}" data-testid="remove-delegate-${Components.escapeAttr(d.id)}">Remove</button>`;
                html += '</div>';
            });
            html += '</div>';
        }
        html += '<button class="btn btn-primary" data-action="add-delegate" data-testid="add-delegate-btn">Add delegate</button>';
        html += '</div></div>';

        return html;
    },

    // ─── Import / Export ───
    renderImportExport() {
        let html = '<div class="content-header"><h1>Import &amp; Export</h1></div>';
        html += '<div class="settings-container">';

        // Check mail from other accounts
        html += '<div class="settings-section">';
        html += '<h2>Check Mail From Other Accounts</h2>';
        html += '<p class="section-description">Import mail from other email accounts using POP3.</p>';
        if (AppState.importAccounts.length > 0) {
            html += '<div class="import-list">';
            AppState.importAccounts.forEach(imp => {
                html += `<div class="import-item" data-testid="import-${Components.escapeAttr(imp.id)}">`;
                html += '<div class="import-info">';
                html += `<strong>${Components.escapeHtml(imp.email)}</strong>`;
                html += ` ${Components.statusBadge(imp.status)}`;
                html += `<br><small class="text-muted">Server: ${Components.escapeHtml(imp.server)}:${Components.escapeHtml(imp.port)} (${imp.useSSL ? 'SSL' : 'No SSL'})</small>`;
                if (imp.labelIncoming) html += `<br><small class="text-muted">Label: ${Components.escapeHtml(imp.labelIncoming)}</small>`;
                if (imp.errorMessage) html += `<br><small class="text-danger">${Components.escapeHtml(imp.errorMessage)}</small>`;
                html += `<br><small class="text-muted">Last checked: ${Components.timeAgo(imp.lastChecked)}</small>`;
                html += '</div>';
                html += `<button class="btn btn-sm btn-danger" data-action="remove-import" data-id="${Components.escapeAttr(imp.id)}" data-testid="remove-import-${Components.escapeAttr(imp.id)}">Remove</button>`;
                html += '</div>';
            });
            html += '</div>';
        }
        html += '<button class="btn btn-primary" data-action="add-import" data-testid="add-import-btn">Add a mail account</button>';
        html += '</div>';

        // Export
        html += '<div class="settings-section">';
        html += '<h2>Export Contacts</h2>';
        html += '<p class="section-description">Download your contacts in CSV or vCard format.</p>';
        html += '<div class="settings-card">';
        html += '<div class="export-options">';
        html += Components.radioGroup('exportFormat', [
            { value: 'csv', label: 'Google CSV', description: 'Compatible with Google Contacts import' },
            { value: 'outlook-csv', label: 'Outlook CSV', description: 'Compatible with Microsoft Outlook' },
            { value: 'vcard', label: 'vCard', description: 'Compatible with Apple Contacts and other apps' }
        ], 'csv');
        html += '<div class="export-scope">';
        html += Components.radioGroup('exportScope', [
            { value: 'all', label: 'All contacts (' + AppState.contacts.length + ')' },
            { value: 'starred', label: 'Starred contacts (' + AppState.getStarredContacts().length + ')' }
        ], 'all');
        html += '</div>';
        html += '<button class="btn btn-primary" data-action="export-contacts" data-testid="export-btn">Export</button>';
        html += '</div></div></div>';

        html += '</div>';
        return html;
    },

    // ─── Merge Duplicates ───
    renderMergeDuplicates() {
        const pairs = AppState.findDuplicates();

        let html = '<div class="content-header">';
        html += '<div class="breadcrumb"><a data-route="contacts" data-filter="all">Contacts</a> / Merge duplicates</div>';
        html += '</div>';
        html += '<h1>Merge Duplicate Contacts</h1>';
        html += '<p class="section-description">Review potential duplicate contacts and merge them. The primary contact\'s data is kept; empty fields are filled from the duplicate.</p>';

        if (pairs.length === 0) {
            html += Components.emptyState('', 'No duplicates found', 'Your contacts look clean — no potential duplicates detected.');
        } else {
            html += `<p style="margin-bottom:16px"><strong>${pairs.length}</strong> potential duplicate${pairs.length !== 1 ? 's' : ''} found.</p>`;
            pairs.forEach((pair, idx) => {
                const a = pair.a;
                const b = pair.b;
                const nameA = ((a.firstName || '') + ' ' + (a.lastName || '')).trim() || a.email;
                const nameB = ((b.firstName || '') + ' ' + (b.lastName || '')).trim() || b.email;
                const colorA = Components.getAvatarColor(nameA);
                const colorB = Components.getAvatarColor(nameB);

                html += '<div class="merge-pair" data-testid="merge-pair-' + idx + '">';
                html += '<div class="merge-pair-header">';
                html += '<span class="badge badge-warning">' + Components.escapeHtml(pair.reason) + '</span>';
                html += '</div>';
                html += '<div class="merge-pair-body">';

                // Contact A
                html += '<div class="merge-card">';
                html += '<div class="merge-card-header">' + Components.avatar(nameA, 36, colorA);
                html += '<div><strong>' + Components.escapeHtml(nameA) + '</strong>';
                if (a.email) html += '<br><small class="text-muted">' + Components.escapeHtml(a.email) + '</small>';
                html += '</div></div>';
                if (a.phone) html += '<div class="merge-field"><span class="detail-label">Phone</span><span>' + Components.escapeHtml(a.phone) + '</span></div>';
                if (a.company) html += '<div class="merge-field"><span class="detail-label">Company</span><span>' + Components.escapeHtml(a.company) + '</span></div>';
                if (a.jobTitle) html += '<div class="merge-field"><span class="detail-label">Title</span><span>' + Components.escapeHtml(a.jobTitle) + '</span></div>';
                html += '<button class="btn btn-sm btn-primary merge-keep-btn" data-action="merge-keep" data-keep-id="' + Components.escapeAttr(a.id) + '" data-merge-id="' + Components.escapeAttr(b.id) + '">Keep this</button>';
                html += '</div>';

                // VS divider
                html += '<div class="merge-vs">VS</div>';

                // Contact B
                html += '<div class="merge-card">';
                html += '<div class="merge-card-header">' + Components.avatar(nameB, 36, colorB);
                html += '<div><strong>' + Components.escapeHtml(nameB) + '</strong>';
                if (b.email) html += '<br><small class="text-muted">' + Components.escapeHtml(b.email) + '</small>';
                html += '</div></div>';
                if (b.phone) html += '<div class="merge-field"><span class="detail-label">Phone</span><span>' + Components.escapeHtml(b.phone) + '</span></div>';
                if (b.company) html += '<div class="merge-field"><span class="detail-label">Company</span><span>' + Components.escapeHtml(b.company) + '</span></div>';
                if (b.jobTitle) html += '<div class="merge-field"><span class="detail-label">Title</span><span>' + Components.escapeHtml(b.jobTitle) + '</span></div>';
                html += '<button class="btn btn-sm btn-primary merge-keep-btn" data-action="merge-keep" data-keep-id="' + Components.escapeAttr(b.id) + '" data-merge-id="' + Components.escapeAttr(a.id) + '">Keep this</button>';
                html += '</div>';

                html += '</div></div>';
            });
        }
        return html;
    },

    // ─── Icons ───
    _iconContacts() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>';
    },
    _iconStar() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>';
    },
    _iconOther() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/></svg>';
    },
    _iconDirectory() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>';
    },
    _iconAccount() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>';
    },
    _iconSendAs() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>';
    },
    _iconDelegation() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>';
    },
    _iconImport() {
        return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';
    }
};

// ============================================================
// views.js — View renderers for Gmail Organize & Manage app
// ============================================================

const Views = {

    // ============================================================
    // SIDEBAR
    // ============================================================

    renderSidebar() {
        const view = AppState.currentView;
        const inboxLabel = AppState.labels.find(l => l.id === 'INBOX');
        const starredLabel = AppState.labels.find(l => l.id === 'STARRED');
        const snoozedLabel = AppState.labels.find(l => l.id === 'SNOOZED');
        const sentLabel = AppState.labels.find(l => l.id === 'SENT');
        const draftLabel = AppState.labels.find(l => l.id === 'DRAFT');
        const importantLabel = AppState.labels.find(l => l.id === 'IMPORTANT');
        const allMailLabel = AppState.labels.find(l => l.id === 'ALL_MAIL');
        const spamLabel = AppState.labels.find(l => l.id === 'SPAM');
        const trashLabel = AppState.labels.find(l => l.id === 'TRASH');

        const inboxUnread = inboxLabel ? inboxLabel.unreadCount : 0;
        const draftCount = draftLabel ? draftLabel.messageCount : 0;
        const spamCount = spamLabel ? spamLabel.messageCount : 0;

        const systemItems = [
            { route: 'inbox', icon: 'inbox', label: 'Inbox', count: inboxUnread, countType: 'unread' },
            { route: 'starred', icon: 'starred', label: 'Starred', count: 0 },
            { route: 'snoozed', icon: 'snoozed', label: 'Snoozed', count: 0 },
            { route: 'sent', icon: 'sent', label: 'Sent', count: 0 },
            { route: 'drafts', icon: 'drafts', label: 'Drafts', count: draftCount },
            { route: 'important', icon: 'important', label: 'Important', count: 0 },
            { route: 'allmail', icon: 'allmail', label: 'All Mail', count: 0 },
            { route: 'spam', icon: 'spam', label: 'Spam', count: spamCount },
            { route: 'trash', icon: 'trash', label: 'Trash', count: 0 },
        ];

        let html = '';

        // System labels
        html += '<div class="nav-section">';
        for (const item of systemItems) {
            const active = view === item.route ? ' active' : '';
            const countHtml = item.count > 0
                ? `<span class="nav-item-count" data-testid="sidebar-count-${Components.escapeAttr(item.route)}">${item.count}</span>`
                : '';
            html += `<div class="nav-item${active}" data-route="${Components.escapeAttr(item.route)}" data-testid="sidebar-${Components.escapeAttr(item.route)}">`;
            html += `<span class="nav-item-icon">${Components.navIcon(item.icon)}</span>`;
            html += `<span class="nav-item-text">${Components.escapeHtml(item.label)}</span>`;
            html += countHtml;
            html += `</div>`;
        }
        html += '</div>';

        // User Labels section
        html += '<div class="nav-section">';
        html += '<div class="nav-section-header">';
        html += '<span>Labels</span>';
        html += `<button class="nav-expand-btn" data-action="toggle-labels" data-testid="toggle-labels-btn" style="width:auto;padding:0;height:auto;font-size:18px">`;
        html += AppState.expandedLabels ? '&#9662;' : '&#9656;';
        html += '</button>';
        html += '</div>';

        if (AppState.expandedLabels) {
            const topLevelLabels = AppState.getTopLevelUserLabels();
            for (const label of topLevelLabels) {
                html += Views._renderLabelNavItem(label, view, false);
                // Render children
                const children = AppState.getChildLabels(label.id);
                for (const child of children) {
                    html += Views._renderLabelNavItem(child, view, true);
                }
            }

            // Create new label button
            html += `<div class="nav-item" data-action="create-label" data-testid="create-label-btn">`;
            html += `<span class="nav-item-icon">${Components.navIcon('createLabel')}</span>`;
            html += `<span class="nav-item-text">Create new label</span>`;
            html += `</div>`;
        }
        html += '</div>';

        return html;
    },

    _renderLabelNavItem(label, currentView, isNested) {
        const active = currentView === label.id ? ' active' : '';
        const nested = isNested ? ' nested' : '';
        const colorDot = label.color
            ? `<span class="nav-item-color" style="background:${Components.escapeAttr(label.color.background)}"></span>`
            : `<span class="nav-item-icon">${Components.navIcon('label')}</span>`;
        const countHtml = label.unreadCount > 0
            ? `<span class="nav-item-count">${label.unreadCount}</span>`
            : '';

        let html = `<div class="nav-item${active}${nested}" data-route="label/${Components.escapeAttr(label.id)}" data-testid="sidebar-label-${Components.escapeAttr(label.id)}">`;
        html += colorDot;
        html += `<span class="nav-item-text">${Components.escapeHtml(label.name)}</span>`;
        html += countHtml;
        html += `</div>`;
        return html;
    },

    // ============================================================
    // TOOLBAR
    // ============================================================

    renderToolbar(view, emails) {
        const selectedCount = AppState.selectedEmailIds.size;
        const allEmails = emails || [];
        const paged = AppState.getPagedEmails(allEmails);

        let html = '<div class="toolbar-left">';

        // Checkbox + dropdown arrow
        html += '<div class="toolbar-checkbox-wrapper">';
        const allOnPageSelected = paged.items.length > 0 && paged.items.every(e => AppState.selectedEmailIds.has(e.id));
        const someSelected = paged.items.some(e => AppState.selectedEmailIds.has(e.id));
        const cbState = allOnPageSelected ? 'checked' : '';
        html += `<input type="checkbox" class="toolbar-checkbox" id="selectAllCheckbox" data-action="select-all" data-testid="select-all-checkbox" ${cbState}>`;
        html += `<button class="toolbar-dropdown-arrow" data-action="select-dropdown" data-testid="select-dropdown-btn">&#9662;</button>`;
        html += '</div>';

        if (selectedCount > 0) {
            // Selection actions toolbar
            html += `<button class="toolbar-btn" data-action="archive-selected" data-testid="toolbar-archive" title="Archive">${Components.toolbarIcon('archive')}</button>`;
            html += `<button class="toolbar-btn" data-action="spam-selected" data-testid="toolbar-spam" title="Report spam">${Components.toolbarIcon('spam')}</button>`;
            html += `<button class="toolbar-btn" data-action="delete-selected" data-testid="toolbar-delete" title="Delete">${Components.toolbarIcon('delete')}</button>`;
            html += '<div class="toolbar-separator"></div>';

            // Mark read/unread
            const anyUnread = [...AppState.selectedEmailIds].some(id => {
                const e = AppState.getEmailById(id);
                return e && !e.isRead;
            });
            if (anyUnread) {
                html += `<button class="toolbar-btn" data-action="mark-read-selected" data-testid="toolbar-mark-read" title="Mark as read">${Components.toolbarIcon('markRead')}</button>`;
            } else {
                html += `<button class="toolbar-btn" data-action="mark-unread-selected" data-testid="toolbar-mark-unread" title="Mark as unread">${Components.toolbarIcon('markUnread')}</button>`;
            }

            html += `<button class="toolbar-btn" data-action="snooze-selected" data-testid="toolbar-snooze" title="Snooze">${Components.toolbarIcon('snooze')}</button>`;
            html += `<button class="toolbar-btn" data-action="label-selected" data-testid="toolbar-label" title="Labels">${Components.toolbarIcon('label')}</button>`;
            html += `<button class="toolbar-btn" data-action="move-to-selected" data-testid="toolbar-move-to" title="Move to">${Components.toolbarIcon('moveTo')}</button>`;
            html += `<button class="toolbar-btn" data-action="more-actions" data-testid="toolbar-more" title="More">${Components.toolbarIcon('more')}</button>`;
        } else {
            // Default actions
            html += `<button class="toolbar-btn" data-action="refresh" data-testid="toolbar-refresh" title="Refresh">${Components.toolbarIcon('refresh')}</button>`;

            // View-specific buttons
            if (view === 'trash') {
                html += `<button class="btn btn-text" data-action="empty-trash" data-testid="empty-trash-btn" style="font-size:13px">Empty Trash now</button>`;
            }
            if (view === 'spam') {
                html += `<button class="btn btn-text" data-action="empty-spam" data-testid="empty-spam-btn" style="font-size:13px">Delete all spam messages</button>`;
            }
        }
        html += '</div>';

        // Center - pagination info
        html += '<div class="toolbar-center">';
        if (allEmails.length > 0) {
            html += `<span class="pagination-info" data-testid="pagination-info">${paged.start}-${paged.end} of ${paged.total}</span>`;
        }
        html += '</div>';

        // Right - pagination buttons
        html += '<div class="toolbar-right">';
        html += `<button class="toolbar-btn" data-action="prev-page" data-testid="toolbar-prev-page" title="Newer" ${!paged.hasPrev ? 'disabled' : ''}>${Components.toolbarIcon('prevPage')}</button>`;
        html += `<button class="toolbar-btn" data-action="next-page" data-testid="toolbar-next-page" title="Older" ${!paged.hasNext ? 'disabled' : ''}>${Components.toolbarIcon('nextPage')}</button>`;
        html += '</div>';

        return html;
    },

    renderCategoryTabs() {
        const categories = [
            { id: 'primary', label: 'Primary' },
            { id: 'social', label: 'Social' },
            { id: 'promotions', label: 'Promotions' },
            { id: 'updates', label: 'Updates' },
            { id: 'forums', label: 'Forums' },
        ];

        const catSettings = AppState.settings.categoriesEnabled || {};

        let html = '<div class="category-tabs" data-testid="category-tabs">';
        for (const cat of categories) {
            if (!catSettings[cat.id]) continue;
            const active = AppState.currentCategory === cat.id ? ' active' : '';
            const catEmails = AppState.getInboxEmailsByCategory(cat.id);
            const unreadCount = catEmails.filter(e => !e.isRead).length;
            html += `<button class="category-tab${active}" data-category="${Components.escapeAttr(cat.id)}" data-testid="category-tab-${Components.escapeAttr(cat.id)}">`;
            html += `<span class="category-tab-icon">${Components.categoryIcon(cat.id)}</span>`;
            html += Components.escapeHtml(cat.label);
            if (unreadCount > 0) {
                html += `<span class="category-tab-count">${unreadCount}</span>`;
            }
            html += `</button>`;
        }
        html += '</div>';
        return html;
    },

    // ============================================================
    // EMAIL LIST
    // ============================================================

    renderEmailList(emails) {
        if (!emails || emails.length === 0) {
            return Views._renderEmptyState(AppState.currentView);
        }

        let html = '<div class="email-list" data-testid="email-list">';
        for (const email of emails) {
            html += Views._renderEmailRow(email);
        }
        html += '</div>';
        return html;
    },

    _renderEmailRow(email) {
        const selected = AppState.selectedEmailIds.has(email.id) ? ' selected' : '';
        const unread = !email.isRead ? ' unread' : '';
        const isChecked = AppState.selectedEmailIds.has(email.id) ? 'checked' : '';
        const showImportance = AppState.settings.importanceMarkers;

        let html = `<div class="email-item${selected}${unread}" data-email-id="${email.id}" data-testid="email-item-${email.id}">`;

        // Checkbox
        html += `<input type="checkbox" class="email-checkbox" data-email-id="${email.id}" data-testid="email-checkbox-${email.id}" ${isChecked}>`;

        // Star
        const starClass = email.isStarred ? ' starred' : '';
        html += `<button class="email-star${starClass}" data-email-id="${email.id}" data-testid="email-star-${email.id}">`;
        html += Components.starIcon(email.starType, email.isStarred);
        html += `</button>`;

        // Importance marker
        if (showImportance) {
            html += `<button ${email.isImportant ? 'class="email-important marked"' : 'class="email-important"'} data-email-id="${email.id}" data-testid="email-important-${email.id}">`;
            html += email.isImportant ? '&#9654;' : '&#9655;';
            html += `</button>`;
        }

        // Sender
        const senderName = email.isDraft ? 'Draft' : Components.escapeHtml(email.from.name);
        const senderClass = email.isDraft ? ' style="color:var(--color-danger)"' : '';
        html += `<span class="email-sender"${senderClass}>${senderName}</span>`;

        // Content: subject + labels + snippet
        html += '<div class="email-content">';
        html += `<span class="email-subject-text">${Components.escapeHtml(email.subject)}</span>`;

        // User label badges inline
        const userLabelBadges = Views._getEmailUserLabels(email);
        if (userLabelBadges.length > 0) {
            html += '<span class="email-labels">';
            for (const label of userLabelBadges) {
                html += Components.labelBadge(label);
            }
            html += '</span>';
        }

        html += `<span class="email-snippet">${Components.escapeHtml(email.snippet)}</span>`;
        html += '</div>';

        // Attachment icon
        if (email.hasAttachments) {
            html += '<span class="email-attachment-icon" title="Has attachment">';
            html += '<svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentColor" d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5c0-1.38 1.12-2.5 2.5-2.5s2.5 1.12 2.5 2.5v10.5c0 .55-.45 1-1 1s-1-.45-1-1V6H10v9.5c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5V5c0-2.21-1.79-4-4-4S7 2.79 7 5v12.5c0 3.04 2.46 5.5 5.5 5.5s5.5-2.46 5.5-5.5V6h-1.5z"/></svg>';
            html += '</span>';
        }

        // Snooze indicator
        if (email.isSnoozed && email.snoozeUntil) {
            html += `<span class="snooze-badge" title="Snoozed until ${Components.escapeAttr(Components.formatDateTime(email.snoozeUntil))}">`;
            html += Components.toolbarIcon('snooze');
            html += `<span>${Components.formatDate(email.snoozeUntil)}</span>`;
            html += '</span>';
        }

        // Date
        html += `<span class="email-date">${Components.formatDate(email.date)}</span>`;

        // Hover actions
        if (AppState.settings.hoverActions) {
            html += '<div class="email-hover-actions">';
            html += `<button class="hover-action-btn" data-action="archive-email" data-email-id="${email.id}" title="Archive">${Components.toolbarIcon('archive')}</button>`;
            html += `<button class="hover-action-btn" data-action="delete-email" data-email-id="${email.id}" title="Delete">${Components.toolbarIcon('delete')}</button>`;
            if (!email.isRead) {
                html += `<button class="hover-action-btn" data-action="mark-read-email" data-email-id="${email.id}" title="Mark as read">${Components.toolbarIcon('markRead')}</button>`;
            } else {
                html += `<button class="hover-action-btn" data-action="mark-unread-email" data-email-id="${email.id}" title="Mark as unread">${Components.toolbarIcon('markUnread')}</button>`;
            }
            html += `<button class="hover-action-btn" data-action="snooze-email" data-email-id="${email.id}" title="Snooze">${Components.toolbarIcon('snooze')}</button>`;
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    _getEmailUserLabels(email) {
        const labels = [];
        for (const labelId of email.labels) {
            const label = AppState.getLabelById(labelId);
            if (label && label.type === 'user') {
                labels.push(label);
            }
        }
        return labels;
    },

    _renderEmptyState(view) {
        const states = {
            inbox: { icon: Components.navIcon('inbox'), title: 'Your inbox is empty', text: 'Emails that arrive in your inbox will appear here.' },
            starred: { icon: Components.navIcon('starred'), title: 'No starred messages', text: 'Stars let you give messages a special status to make them easier to find. To star a message, click on the star outline beside any message or conversation.' },
            snoozed: { icon: Components.navIcon('snoozed'), title: 'No snoozed messages', text: 'Snooze emails to have them reappear at a later time.' },
            sent: { icon: Components.navIcon('sent'), title: 'No sent messages', text: 'Messages you have sent will appear here.' },
            drafts: { icon: Components.navIcon('drafts'), title: 'No drafts', text: 'You don\'t have any saved drafts. Composing a new message will automatically save a draft.' },
            trash: { icon: Components.navIcon('trash'), title: 'Trash is empty', text: 'Messages that have been in Trash more than 30 days will be automatically deleted.' },
            spam: { icon: Components.navIcon('spam'), title: 'Hooray, no spam here!', text: 'Spam messages will be automatically deleted after 30 days.' },
            important: { icon: Components.navIcon('important'), title: 'No important messages', text: 'Gmail analyzes your messages to predict what\'s important. Messages marked as important will appear here.' },
            allmail: { icon: Components.navIcon('allmail'), title: 'No mail', text: 'Your All Mail folder is empty.' },
            search: { icon: '<svg width="48" height="48" viewBox="0 0 24 24"><path fill="currentColor" d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>', title: 'No results found', text: 'Try different search terms or check your spelling.' },
        };
        const state = states[view] || { icon: Components.navIcon('label'), title: 'No messages', text: 'There are no messages with this label.' };
        return Components.emptyState(state.icon, state.title, state.text);
    },

    // ============================================================
    // EMAIL DETAIL
    // ============================================================

    renderEmailDetail(email) {
        if (!email) {
            return Components.emptyState(
                Components.navIcon('inbox'),
                'Message not found',
                'The message you are looking for could not be found.'
            );
        }

        // Get thread messages if conversation view is on
        let threadEmails = [email];
        if (AppState.settings.conversationView) {
            threadEmails = AppState.getEmailsByThread(email.threadId);
            if (threadEmails.length === 0) threadEmails = [email];
        }

        let html = '<div class="email-detail" data-testid="email-detail">';

        // Back button + subject + labels
        html += '<div class="email-detail-header">';
        html += `<button class="toolbar-btn" data-action="back-to-list" data-testid="back-to-list" title="Back to list" style="margin-right:8px">`;
        html += '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>';
        html += '</button>';
        html += `<h2 class="email-detail-subject" data-testid="email-detail-subject">${Components.escapeHtml(email.subject)}</h2>`;

        // Labels
        const userLabels = Views._getEmailUserLabels(email);
        if (userLabels.length > 0) {
            html += '<div class="email-detail-labels">';
            for (const label of userLabels) {
                html += Components.labelBadge(label);
            }
            html += '</div>';
        }
        html += '</div>';

        // Toolbar actions for detail view
        html += '<div style="display:flex;gap:4px;margin-bottom:16px">';
        html += `<button class="toolbar-btn" data-action="archive-email" data-email-id="${email.id}" title="Archive">${Components.toolbarIcon('archive')}</button>`;
        html += `<button class="toolbar-btn" data-action="spam-email" data-email-id="${email.id}" title="Report spam">${Components.toolbarIcon('spam')}</button>`;
        html += `<button class="toolbar-btn" data-action="delete-email" data-email-id="${email.id}" title="Delete">${Components.toolbarIcon('delete')}</button>`;
        html += '<div class="toolbar-separator"></div>';
        if (!email.isRead) {
            html += `<button class="toolbar-btn" data-action="mark-read-email" data-email-id="${email.id}" title="Mark as read">${Components.toolbarIcon('markRead')}</button>`;
        } else {
            html += `<button class="toolbar-btn" data-action="mark-unread-email" data-email-id="${email.id}" title="Mark as unread">${Components.toolbarIcon('markUnread')}</button>`;
        }
        html += `<button class="toolbar-btn" data-action="snooze-email" data-email-id="${email.id}" title="Snooze">${Components.toolbarIcon('snooze')}</button>`;
        html += `<button class="toolbar-btn" data-action="label-selected" data-testid="detail-label-btn" title="Labels">${Components.toolbarIcon('label')}</button>`;
        html += `<button class="toolbar-btn" data-action="move-to-selected" data-testid="detail-move-btn" title="Move to">${Components.toolbarIcon('moveTo')}</button>`;
        html += '</div>';

        // Messages in thread
        html += '<div class="email-detail-messages" data-testid="email-detail-messages">';
        for (let i = 0; i < threadEmails.length; i++) {
            const msg = threadEmails[i];
            const isLast = i === threadEmails.length - 1;
            html += Views._renderMessageCard(msg, isLast);
        }
        html += '</div>';

        // Reply / Reply All / Forward buttons
        html += '<div style="display:flex;gap:8px;margin-top:16px;padding:16px 0 16px 68px">';
        html += `<button class="btn btn-secondary" data-action="reply" data-email-id="${email.id}" data-testid="reply-btn">`;
        html += `${Components.toolbarIcon('reply')}<span>Reply</span></button>`;
        html += `<button class="btn btn-secondary" data-action="reply-all" data-email-id="${email.id}" data-testid="reply-all-btn">`;
        html += `${Components.toolbarIcon('replyAll')}<span>Reply all</span></button>`;
        html += `<button class="btn btn-secondary" data-action="forward" data-email-id="${email.id}" data-testid="forward-btn">`;
        html += `${Components.toolbarIcon('forward')}<span>Forward</span></button>`;
        html += '</div>';

        html += '</div>';
        return html;
    },

    _renderMessageCard(msg, expanded) {
        const contact = CONTACTS.find(c => c.email === msg.from.email);
        const avatarColor = contact ? contact.avatarColor : '#5f6368';

        let html = `<div class="email-message-card" data-message-id="${msg.id}" data-testid="message-card-${msg.id}">`;

        // Header
        html += '<div class="email-message-header">';
        html += Components.avatar(msg.from.name, avatarColor, 40);

        html += '<div class="email-message-meta">';
        html += `<div class="email-message-sender">${Components.escapeHtml(msg.from.name)} `;
        html += `<span style="font-weight:400;color:var(--text-secondary);font-size:12px">&lt;${Components.escapeHtml(msg.from.email)}&gt;</span></div>`;

        // Recipients
        const toNames = msg.to.map(t => Components.escapeHtml(t.name || t.email)).join(', ');
        html += `<div class="email-message-info">to ${toNames}`;
        if (msg.cc && msg.cc.length > 0) {
            const ccNames = msg.cc.map(c => Components.escapeHtml(c.name || c.email)).join(', ');
            html += `, cc: ${ccNames}`;
        }
        html += '</div>';
        html += '</div>';

        // Date
        html += `<span class="email-message-date" title="${Components.escapeAttr(Components.formatFullDate(msg.date))}">${Components.formatDateTime(msg.date)}</span>`;

        // Message actions
        html += '<div class="email-message-actions">';
        html += `<button class="toolbar-btn" data-action="reply" data-email-id="${msg.id}" title="Reply">${Components.toolbarIcon('reply')}</button>`;
        html += `<button class="toolbar-btn" data-action="more-message-actions" data-email-id="${msg.id}" title="More">${Components.toolbarIcon('more')}</button>`;
        html += '</div>';

        html += '</div>';

        // Body (always show for last message, collapsed snippet for others)
        if (expanded) {
            html += '<div class="email-message-body" data-testid="message-body-' + msg.id + '">';
            // Render body preserving line breaks
            const bodyHtml = Components.escapeHtml(msg.body || msg.snippet)
                .replace(/\n/g, '<br>');
            html += `<p>${bodyHtml}</p>`;
            html += '</div>';

            // Attachments
            if (msg.hasAttachments && msg.attachments && msg.attachments.length > 0) {
                html += '<div class="email-message-attachments" data-testid="message-attachments-' + msg.id + '">';
                for (const att of msg.attachments) {
                    html += `<div class="attachment-chip" data-testid="attachment-${Components.escapeAttr(att.name)}">`;
                    html += '<svg width="16" height="16" viewBox="0 0 24 24"><path fill="currentColor" d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zM6 20V4h7v5h5v11H6z"/></svg>';
                    html += `<span>${Components.escapeHtml(att.name)}</span>`;
                    html += `<span style="color:var(--text-secondary);font-size:12px">${Components.escapeHtml(att.size)}</span>`;
                    html += '</div>';
                }
                html += '</div>';
            }
        } else {
            html += `<div class="email-message-body" style="cursor:pointer" data-action="expand-message" data-message-id="${msg.id}">`;
            html += `<p style="color:var(--text-secondary)">${Components.escapeHtml(msg.snippet)}</p>`;
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    // ============================================================
    // SETTINGS PAGE
    // ============================================================

    renderSettings() {
        const s = AppState.settings;
        const tab = AppState.settingsTab || 'general';

        const tabs = [
            { id: 'general', label: 'General' },
            { id: 'labels', label: 'Labels' },
            { id: 'inbox', label: 'Inbox' },
            { id: 'filters', label: 'Filters and Blocked Addresses' },
        ];

        let html = '<div class="settings-page" data-testid="settings-page">';
        html += '<h1>Settings</h1>';

        // Tabs
        html += '<div class="settings-tabs" data-testid="settings-tabs">';
        for (const t of tabs) {
            const active = tab === t.id ? ' active' : '';
            html += `<button class="settings-tab${active}" data-settings-tab="${Components.escapeAttr(t.id)}" data-testid="settings-tab-${Components.escapeAttr(t.id)}">${Components.escapeHtml(t.label)}</button>`;
        }
        html += '</div>';

        // Tab content
        switch (tab) {
            case 'general':
                html += Views._renderSettingsGeneral(s);
                break;
            case 'labels':
                html += Views._renderSettingsLabels();
                break;
            case 'inbox':
                html += Views._renderSettingsInbox(s);
                break;
            case 'filters':
                html += Views._renderSettingsFilters();
                break;
        }

        // Save Changes button
        html += '<div class="settings-save-bar">';
        html += '<button class="btn btn-secondary" data-action="cancel-settings" data-testid="settings-cancel">Cancel</button>';
        html += '<button class="btn btn-primary" data-action="save-settings" data-testid="settings-save">Save Changes</button>';
        html += '</div>';

        html += '</div>';
        return html;
    },

    _renderSettingsGeneral(s) {
        let html = '';

        // Language
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Language</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Gmail display language</div>';
        html += '<div class="settings-row-control">';
        html += Components.dropdown('language-dropdown', [
            { id: 'English (US)', name: 'English (US)' },
            { id: 'English (UK)', name: 'English (UK)' },
            { id: 'Spanish', name: 'Spanish' },
            { id: 'French', name: 'French' },
            { id: 'German', name: 'German' },
            { id: 'Japanese', name: 'Japanese' },
            { id: 'Chinese (Simplified)', name: 'Chinese (Simplified)' },
            { id: 'Korean', name: 'Korean' },
            { id: 'Portuguese (Brazil)', name: 'Portuguese (Brazil)' },
            { id: 'Hindi', name: 'Hindi' },
            { id: 'Arabic', name: 'Arabic' },
            { id: 'Italian', name: 'Italian' },
        ], s.language);
        html += '</div></div>';
        html += '</div>';

        // Phone number (static display)
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Phone number</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Phone number</div>';
        html += '<div class="settings-row-control">';
        html += '<span style="font-size:14px;color:var(--text-secondary)">Not set. Used for account recovery.</span>';
        html += '</div></div>';
        html += '</div>';

        // Default reply behavior
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Default reply behavior</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">When replying to a message</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('reply-behavior', [
            { id: 'reply', name: 'Reply' },
            { id: 'reply-all', name: 'Reply all' },
        ], s.defaultReplyBehavior);
        html += '</div></div>';
        html += '</div>';

        // Undo Send
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Undo Send</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Send cancellation period</div>';
        html += '<div class="settings-row-control">';
        html += Components.dropdown('undo-send-dropdown', [
            { id: 5, name: '5 seconds' },
            { id: 10, name: '10 seconds' },
            { id: 20, name: '20 seconds' },
            { id: 30, name: '30 seconds' },
        ], s.undoSendDelay);
        html += '</div></div>';
        html += '</div>';

        // Conversation View
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Conversation View</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Group emails into conversations</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('conversationView', [
            { id: 'on', name: 'Conversation view on' },
            { id: 'off', name: 'Conversation view off' },
        ], s.conversationView ? 'on' : 'off');
        html += '</div></div>';
        html += '</div>';

        // Density
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Density</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Display density</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('density', [
            { id: 'default', name: 'Default' },
            { id: 'comfortable', name: 'Comfortable' },
            { id: 'compact', name: 'Compact' },
        ], s.density);
        html += '</div></div>';
        html += '</div>';

        // Send and Archive
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Send and Archive</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Show "Send & Archive" button in reply</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('sendAndArchive', [
            { id: 'on', name: 'Show "Send & Archive" button in reply' },
            { id: 'off', name: 'Hide "Send & Archive" button in reply' },
        ], s.sendAndArchive ? 'on' : 'off');
        html += '</div></div>';
        html += '</div>';

        // Hover Actions
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Hover Actions</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Enable hover actions</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('hoverActions', [
            { id: 'on', name: 'Enable hover actions' },
            { id: 'off', name: 'Disable hover actions' },
        ], s.hoverActions ? 'on' : 'off');
        html += '</div></div>';
        html += '</div>';

        // Nudges
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Nudges</div>';
        html += Components.toggle('setting-nudge-reply', s.nudges.suggestEmailsToReply,
            'Suggest emails to reply to',
            'Emails you might have forgotten to respond to will appear at the top of your inbox');
        html += Components.toggle('setting-nudge-followup', s.nudges.suggestEmailsToFollowUp,
            'Suggest emails to follow up on',
            'Sent emails you might need to follow up on will appear at the top of your inbox');
        html += '</div>';

        // Auto-Advance
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Auto-advance</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">After archiving or deleting a conversation</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('auto-advance', [
            { id: 'newer', name: 'Go to the next (newer) conversation' },
            { id: 'older', name: 'Go to the previous (older) conversation' },
            { id: 'list', name: 'Go back to the threadlist' },
        ], s.autoAdvance);
        html += '</div></div>';
        html += '</div>';

        // Keyboard Shortcuts
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Keyboard shortcuts</div>';
        html += Components.toggle('setting-keyboard-shortcuts', s.keyboardShortcutsEnabled,
            'Keyboard shortcuts',
            'Enable keyboard shortcuts for faster navigation');
        html += '</div>';

        // Desktop Notifications
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Desktop Notifications</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Email notifications</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('desktop-notifications', [
            { id: 'off', name: 'Mail notifications off' },
            { id: 'important', name: 'Important mail notifications on' },
            { id: 'all', name: 'New mail notifications on' },
        ], s.desktopNotifications);
        html += '</div></div>';
        html += '</div>';

        // Stars
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Stars</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Stars in use</div>';
        html += '<div class="settings-row-control">';
        html += '<div style="display:flex;gap:8px;flex-wrap:wrap;font-size:20px">';
        const allStars = ['yellow-star','orange-star','red-star','purple-star','blue-star','green-star','yellow-bang','red-bang','purple-question','orange-guillemet','blue-info'];
        for (const star of allStars) {
            const enabled = (s.enabledStars || []).includes(star);
            const opacity = enabled ? '1' : '0.3';
            html += `<span class="star-toggle" data-star="${Components.escapeAttr(star)}" data-testid="star-toggle-${Components.escapeAttr(star)}" style="cursor:pointer;opacity:${opacity}" title="${Components.escapeAttr(star)}">`;
            html += Components.starIcon(star, true);
            html += '</span>';
        }
        html += '</div>';
        html += '</div></div>';
        html += '</div>';

        // Max page size
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Maximum page size</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Show this many conversations per page</div>';
        html += '<div class="settings-row-control">';
        html += Components.dropdown('page-size-dropdown', [
            { id: 10, name: '10' },
            { id: 25, name: '25' },
            { id: 50, name: '50' },
            { id: 100, name: '100' },
        ], s.maxPageSize);
        html += '</div></div>';
        html += '</div>';

        // Button labels
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Button labels</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Display button labels or icons</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('button-labels', [
            { id: 'icons', name: 'Icons' },
            { id: 'text', name: 'Text' },
        ], s.buttonLabels);
        html += '</div></div>';
        html += '</div>';

        // Dynamic email
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Dynamic email</div>';
        html += Components.toggle('setting-dynamic-email', s.dynamicEmail,
            'Enable dynamic email',
            'Allow email senders to include interactive content in their emails');
        html += '</div>';

        return html;
    },

    _renderSettingsLabels() {
        let html = '';

        // System labels
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">System labels</div>';
        html += '<table style="width:100%;border-collapse:collapse">';
        html += '<thead><tr>';
        html += '<th style="text-align:left;padding:8px 0;font-size:13px;color:var(--text-secondary);font-weight:500">Label</th>';
        html += '<th style="text-align:center;padding:8px 0;font-size:13px;color:var(--text-secondary);font-weight:500;width:100px">Show in label list</th>';
        html += '<th style="text-align:center;padding:8px 0;font-size:13px;color:var(--text-secondary);font-weight:500;width:100px">Show in message list</th>';
        html += '</tr></thead>';
        html += '<tbody>';

        const systemLabels = AppState.labels.filter(l => l.type === 'system' && !l.id.startsWith('CATEGORY_'));
        for (const label of systemLabels) {
            html += `<tr style="border-bottom:1px solid var(--border-light)" data-testid="label-settings-row-${Components.escapeAttr(label.id)}">`;
            html += `<td style="padding:8px 0;font-size:14px">${Components.escapeHtml(label.name)}</td>`;
            html += '<td style="text-align:center;padding:8px 0">';
            html += Components.radioGroup('labelList_' + label.id, [
                { id: 'show', name: 'show' },
                { id: 'hide', name: 'hide' },
            ], label.visible ? 'show' : 'hide');
            html += '</td>';
            html += '<td style="text-align:center;padding:8px 0">';
            html += Components.radioGroup('labelMsg_' + label.id, [
                { id: 'show', name: 'show' },
                { id: 'hide', name: 'hide' },
            ], label.visible ? 'show' : 'hide');
            html += '</td>';
            html += '</tr>';
        }
        html += '</tbody></table>';
        html += '</div>';

        // User labels
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title" style="display:flex;justify-content:space-between;align-items:center">Labels';
        html += `<button class="btn btn-text" data-action="create-label" data-testid="settings-create-label">Create new label</button>`;
        html += '</div>';
        html += '<table style="width:100%;border-collapse:collapse">';
        html += '<thead><tr>';
        html += '<th style="text-align:left;padding:8px 0;font-size:13px;color:var(--text-secondary);font-weight:500">Label</th>';
        html += '<th style="text-align:center;padding:8px 0;font-size:13px;color:var(--text-secondary);font-weight:500;width:100px">Show</th>';
        html += '<th style="text-align:right;padding:8px 0;font-size:13px;color:var(--text-secondary);font-weight:500;width:120px">Actions</th>';
        html += '</tr></thead>';
        html += '<tbody>';

        const userLabels = AppState.getUserLabels();
        for (const label of userLabels) {
            const indent = label.parentId ? 'padding-left:24px;' : '';
            const colorDot = label.color
                ? `<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:${Components.escapeAttr(label.color.background)};margin-right:8px;vertical-align:middle"></span>`
                : '';
            html += `<tr style="border-bottom:1px solid var(--border-light)" data-testid="label-settings-row-${Components.escapeAttr(label.id)}">`;
            html += `<td style="padding:8px 0;font-size:14px;${indent}">${colorDot}${Components.escapeHtml(label.name)}</td>`;
            html += '<td style="text-align:center;padding:8px 0">';
            html += `<label class="toggle-switch" data-testid="label-visibility-${Components.escapeAttr(label.id)}">`;
            html += `<input type="checkbox" data-action="toggle-label-visibility" data-label-id="${Components.escapeAttr(label.id)}" ${label.visible ? 'checked' : ''}>`;
            html += '<span class="toggle-slider"></span></label>';
            html += '</td>';
            html += '<td style="text-align:right;padding:8px 0">';
            html += `<a style="font-size:13px;color:var(--color-primary);cursor:pointer;margin-right:12px" data-action="edit-label" data-label-id="${Components.escapeAttr(label.id)}" data-testid="edit-label-${Components.escapeAttr(label.id)}">edit</a>`;
            html += `<a style="font-size:13px;color:var(--color-danger);cursor:pointer" data-action="delete-label" data-label-id="${Components.escapeAttr(label.id)}" data-testid="delete-label-${Components.escapeAttr(label.id)}">remove</a>`;
            html += '</td>';
            html += '</tr>';
        }
        html += '</tbody></table>';
        html += '</div>';

        return html;
    },

    _renderSettingsInbox(s) {
        let html = '';

        // Inbox type
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Inbox type</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Inbox type</div>';
        html += '<div class="settings-row-control">';
        html += Components.dropdown('inbox-type-dropdown', [
            { id: 'default', name: 'Default' },
            { id: 'important-first', name: 'Important first' },
            { id: 'unread-first', name: 'Unread first' },
            { id: 'starred-first', name: 'Starred first' },
            { id: 'priority', name: 'Priority Inbox' },
            { id: 'multiple', name: 'Multiple Inboxes' },
        ], s.inboxType);
        html += '</div></div>';
        html += '</div>';

        // Categories
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Categories</div>';
        html += '<p style="font-size:13px;color:var(--text-secondary);margin-bottom:12px">Choose which categories to show as tabs in your inbox</p>';
        const catNames = ['primary', 'social', 'promotions', 'updates', 'forums'];
        for (const cat of catNames) {
            const catLabel = cat.charAt(0).toUpperCase() + cat.slice(1);
            const checked = s.categoriesEnabled && s.categoriesEnabled[cat];
            html += '<div class="settings-item">';
            html += `<div class="settings-item-label">${Components.escapeHtml(catLabel)}</div>`;
            html += `<label class="toggle-switch" data-testid="category-toggle-${Components.escapeAttr(cat)}">`;
            html += `<input type="checkbox" id="cat-${Components.escapeAttr(cat)}" data-action="toggle-category" data-category="${Components.escapeAttr(cat)}" ${checked ? 'checked' : ''} ${cat === 'primary' ? 'disabled' : ''}>`;
            html += '<span class="toggle-slider"></span></label>';
            html += '</div>';
        }
        html += '</div>';

        // Importance markers
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Importance markers</div>';
        html += Components.toggle('setting-importance-markers', s.importanceMarkers,
            'Show markers',
            'Show importance markers next to messages that Gmail predicts are important');
        html += '</div>';

        // Reading pane
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Reading pane</div>';
        html += '<div class="settings-row">';
        html += '<div class="settings-row-label">Reading pane position</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('preview-pane', [
            { id: 'none', name: 'No split' },
            { id: 'right', name: 'Right of inbox' },
            { id: 'bottom', name: 'Below inbox' },
        ], s.previewPane);
        html += '</div></div>';
        html += '</div>';

        // Multiple Inboxes
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Multiple Inboxes</div>';
        html += '<p style="font-size:13px;color:var(--text-secondary);margin-bottom:12px">Configure sections when inbox type is set to "Multiple Inboxes"</p>';

        const sections = s.multipleInboxSections || [];
        for (let i = 0; i < sections.length; i++) {
            const sec = sections[i];
            html += `<div style="display:flex;gap:12px;align-items:center;margin-bottom:8px;padding:8px 0;border-bottom:1px solid var(--border-light)" data-testid="multiple-inbox-section-${i}">`;
            html += `<span style="font-size:13px;color:var(--text-secondary);width:60px;flex-shrink:0">Section ${i + 1}</span>`;
            html += `<input type="text" class="form-input" data-field="multi-inbox-query-${i}" value="${Components.escapeAttr(sec.query)}" placeholder="Search query" style="flex:1">`;
            html += `<input type="text" class="form-input" data-field="multi-inbox-name-${i}" value="${Components.escapeAttr(sec.name)}" placeholder="Section name" style="width:120px">`;
            html += `</div>`;
        }

        html += '<div class="settings-row" style="margin-top:12px">';
        html += '<div class="settings-row-label">Multiple inbox position</div>';
        html += '<div class="settings-row-control">';
        html += Components.radioGroup('multipleInboxPosition', [
            { id: 'right', name: 'Right side of the inbox' },
            { id: 'above', name: 'Above the inbox' },
            { id: 'below', name: 'Below the inbox' },
        ], s.multipleInboxPosition);
        html += '</div></div>';
        html += '</div>';

        return html;
    },

    _renderSettingsFilters() {
        let html = '';

        // Filters
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title" style="display:flex;justify-content:space-between;align-items:center">Filters';
        html += `<button class="btn btn-text" data-action="create-filter" data-testid="create-filter-btn">Create a new filter</button>`;
        html += '</div>';
        html += '<p style="font-size:13px;color:var(--text-secondary);margin-bottom:12px">The following filters are applied to all incoming mail:</p>';

        if (AppState.filters.length === 0) {
            html += '<p style="font-size:14px;color:var(--text-secondary);padding:12px 0">You don\'t have any filters. Filters let you automatically manage incoming messages.</p>';
        } else {
            for (const filter of AppState.filters) {
                html += Views._renderFilterListItem(filter);
            }
        }
        html += '</div>';

        // Blocked Addresses
        html += '<div class="settings-group">';
        html += '<div class="settings-group-title">Blocked Addresses</div>';
        html += '<p style="font-size:13px;color:var(--text-secondary);margin-bottom:12px">Messages from blocked addresses will be sent to Spam.</p>';

        if (AppState.blockedSenders.length === 0) {
            html += '<p style="font-size:14px;color:var(--text-secondary);padding:12px 0">You have no blocked addresses.</p>';
        } else {
            for (const blocked of AppState.blockedSenders) {
                html += `<div class="blocked-sender-item" data-testid="blocked-sender-${Components.escapeAttr(blocked.email)}">`;
                html += `<div>`;
                html += `<span class="blocked-sender-email">${Components.escapeHtml(blocked.email)}</span>`;
                html += `<div style="font-size:12px;color:var(--text-secondary)">Blocked ${Components.formatDate(blocked.blockedAt)}</div>`;
                html += `</div>`;
                html += `<button class="unblock-btn" data-action="unblock-sender" data-sender-email="${Components.escapeAttr(blocked.email)}" data-testid="unblock-${Components.escapeAttr(blocked.email)}">unblock</button>`;
                html += `</div>`;
            }
        }
        html += '</div>';

        return html;
    },

    _renderFilterListItem(filter) {
        const c = filter.criteria;
        const a = filter.actions;

        // Build criteria description
        let criteriaText = '';
        const parts = [];
        if (c.from) parts.push(`From: ${c.from}`);
        if (c.to) parts.push(`To: ${c.to}`);
        if (c.subject) parts.push(`Subject: ${c.subject}`);
        if (c.hasWords) parts.push(`Has the words: ${c.hasWords}`);
        if (c.doesntHave) parts.push(`Doesn't have: ${c.doesntHave}`);
        if (c.hasAttachment) parts.push('Has attachment');
        if (c.size) parts.push(`Size ${c.sizeComparison} than ${c.size} ${c.sizeUnit}`);
        criteriaText = parts.join(', ');

        // Build actions description
        const actionParts = [];
        if (a.label) {
            const label = AppState.getLabelById(a.label);
            actionParts.push(`Apply label "${label ? label.name : a.label}"`);
        }
        if (a.archive) actionParts.push('Skip Inbox');
        if (a.markRead) actionParts.push('Mark as read');
        if (a.star) actionParts.push('Star it');
        if (a.forward) actionParts.push(`Forward to ${a.forward}`);
        if (a.delete) actionParts.push('Delete it');
        if (a.neverSpam) actionParts.push('Never send to Spam');
        if (a.alwaysImportant) actionParts.push('Always mark as important');
        if (a.neverImportant) actionParts.push('Never mark as important');
        if (a.category) actionParts.push(`Categorize as ${a.category}`);
        const actionsText = actionParts.join(', ') || 'No actions';

        let html = `<div class="filter-list-item" data-testid="filter-${Components.escapeAttr(filter.id)}">`;
        html += '<div>';
        html += `<div class="filter-criteria">Matches: ${Components.escapeHtml(criteriaText || 'All mail')}</div>`;
        html += `<div class="filter-actions-desc">Do this: ${Components.escapeHtml(actionsText)}</div>`;
        html += '</div>';
        html += '<div class="filter-item-actions">';
        html += `<a data-action="edit-filter" data-filter-id="${Components.escapeAttr(filter.id)}" data-testid="edit-filter-${Components.escapeAttr(filter.id)}">edit</a>`;
        html += `<a data-action="delete-filter" data-filter-id="${Components.escapeAttr(filter.id)}" data-testid="delete-filter-${Components.escapeAttr(filter.id)}">delete</a>`;
        html += '</div>';
        html += '</div>';
        return html;
    },

    // ============================================================
    // COMPOSE
    // ============================================================

    renderCompose(draft) {
        // Populate compose fields if we have a draft or reply context
        if (!draft) return;

        const toField = document.getElementById('composeTo');
        const ccField = document.getElementById('composeCc');
        const subjectField = document.getElementById('composeSubject');
        const bodyField = document.getElementById('composeBody');

        if (toField && draft.to) {
            toField.value = Array.isArray(draft.to)
                ? draft.to.map(t => t.email || t).join(', ')
                : draft.to;
        }
        if (ccField && draft.cc) {
            ccField.value = Array.isArray(draft.cc)
                ? draft.cc.map(c => c.email || c).join(', ')
                : draft.cc;
            const ccFieldWrapper = document.getElementById('composeCcField');
            if (ccFieldWrapper && draft.cc.length > 0) {
                ccFieldWrapper.style.display = '';
            }
        }
        if (subjectField && draft.subject !== undefined) {
            subjectField.value = draft.subject;
        }
        if (bodyField && draft.body !== undefined) {
            bodyField.value = draft.body;
        }
    },

    // ============================================================
    // SEARCH RESULTS
    // ============================================================

    renderSearchResults(results) {
        if (!results || results.length === 0) {
            return Views._renderEmptyState('search');
        }

        const sorted = AppState.sortEmails(results);
        const paged = AppState.getPagedEmails(sorted);

        let html = '';
        html += `<div style="padding:12px 16px;font-size:14px;color:var(--text-secondary);border-bottom:1px solid var(--border-light)" data-testid="search-results-header">`;
        html += `Search results for "${Components.escapeHtml(AppState.searchQuery)}" (${results.length} result${results.length !== 1 ? 's' : ''})`;
        html += '</div>';

        html += '<div class="email-list" data-testid="search-results-list">';
        for (const email of paged.items) {
            html += Views._renderEmailRow(email);
        }
        html += '</div>';

        return html;
    },

    // ============================================================
    // LABEL PICKER (for applying labels to emails)
    // ============================================================

    renderLabelPicker(emailIds) {
        const userLabels = AppState.getUserLabels();
        // Determine which labels are already applied to all selected emails
        const allEmails = emailIds.map(id => AppState.getEmailById(id)).filter(Boolean);

        let html = '<div class="label-picker" data-testid="label-picker">';
        html += '<div class="label-picker-header">Label as:</div>';
        html += '<div class="label-picker-search">';
        html += '<input type="text" placeholder="Search labels" data-action="filter-label-picker" data-testid="label-picker-search">';
        html += '</div>';
        html += '<div class="label-picker-list">';

        for (const label of userLabels) {
            // Check if all selected emails have this label
            const allHaveLabel = allEmails.every(e => e.labels.includes(label.id));
            const someHaveLabel = allEmails.some(e => e.labels.includes(label.id)) && !allHaveLabel;
            const checked = allHaveLabel ? 'checked' : '';
            const indeterminate = someHaveLabel ? 'data-indeterminate="true"' : '';

            const colorDot = label.color
                ? `<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:${Components.escapeAttr(label.color.background)};flex-shrink:0"></span>`
                : '';

            html += `<label class="label-picker-item" data-testid="label-picker-item-${Components.escapeAttr(label.id)}">`;
            html += `<input type="checkbox" data-action="apply-label" data-label-id="${Components.escapeAttr(label.id)}" ${checked} ${indeterminate}>`;
            html += colorDot;
            html += `<span>${Components.escapeHtml(label.name)}</span>`;
            html += '</label>';
        }

        html += '</div>';
        html += '<div class="label-picker-footer">';
        html += `<a style="font-size:13px;color:var(--color-primary);cursor:pointer" data-action="create-label" data-testid="label-picker-create">Create new</a>`;
        html += '</div>';
        html += '</div>';
        return html;
    },

    // ============================================================
    // MOVE TO PICKER
    // ============================================================

    renderMoveToMenu() {
        const items = [
            { action: 'move-to-inbox', icon: 'moveToInbox', label: 'Inbox' },
            { action: 'move-to-trash', icon: 'delete', label: 'Trash' },
            { action: 'move-to-spam', icon: 'spam', label: 'Spam' },
        ];

        let html = '<div class="context-menu open" data-testid="move-to-menu">';
        for (const item of items) {
            html += `<div class="context-menu-item" data-action="${Components.escapeAttr(item.action)}" data-testid="move-to-${Components.escapeAttr(item.action)}">`;
            html += `<span class="context-menu-item-icon">${Components.toolbarIcon(item.icon)}</span>`;
            html += `<span>${Components.escapeHtml(item.label)}</span>`;
            html += '</div>';
        }

        // Separator + user labels
        const userLabels = AppState.getUserLabels();
        if (userLabels.length > 0) {
            html += '<div class="context-menu-divider"></div>';
            for (const label of userLabels) {
                const colorDot = label.color
                    ? `<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:${Components.escapeAttr(label.color.background)}"></span>`
                    : `<span class="context-menu-item-icon">${Components.navIcon('label')}</span>`;
                html += `<div class="context-menu-item" data-action="move-to-label" data-label-id="${Components.escapeAttr(label.id)}" data-testid="move-to-label-${Components.escapeAttr(label.id)}">`;
                html += colorDot;
                html += `<span>${Components.escapeHtml(label.name)}</span>`;
                html += '</div>';
            }
        }
        html += '</div>';
        return html;
    },

    // ============================================================
    // MORE ACTIONS MENU
    // ============================================================

    renderMoreActionsMenu() {
        const selectedIds = [...AppState.selectedEmailIds];
        const anyMuted = selectedIds.some(id => {
            const e = AppState.getEmailById(id);
            return e && e.isMuted;
        });

        let html = '<div class="context-menu open" data-testid="more-actions-menu">';
        html += `<div class="context-menu-item" data-action="mark-read-selected"><span class="context-menu-item-icon">${Components.toolbarIcon('markRead')}</span><span>Mark as read</span></div>`;
        html += `<div class="context-menu-item" data-action="mark-unread-selected"><span class="context-menu-item-icon">${Components.toolbarIcon('markUnread')}</span><span>Mark as unread</span></div>`;
        html += '<div class="context-menu-divider"></div>';
        html += `<div class="context-menu-item" data-action="mark-important-selected"><span class="context-menu-item-icon">${Components.importanceIcon(true)}</span><span>Mark as important</span></div>`;
        html += `<div class="context-menu-item" data-action="mark-not-important-selected"><span class="context-menu-item-icon">${Components.importanceIcon(false)}</span><span>Mark as not important</span></div>`;
        html += '<div class="context-menu-divider"></div>';
        if (anyMuted) {
            html += `<div class="context-menu-item" data-action="unmute-selected"><span class="context-menu-item-icon">${Components.toolbarIcon('markRead')}</span><span>Unmute</span></div>`;
        } else {
            html += `<div class="context-menu-item" data-action="mute-selected"><span class="context-menu-item-icon">${Components.toolbarIcon('archive')}</span><span>Mute</span></div>`;
        }
        html += '</div>';
        return html;
    },

    // ============================================================
    // SELECT DROPDOWN (All, None, Read, Unread, Starred, Unstarred)
    // ============================================================

    renderSelectDropdown() {
        let html = '<div class="context-menu open" data-testid="select-dropdown-menu">';
        html += '<div class="context-menu-item" data-action="select-all-page">All</div>';
        html += '<div class="context-menu-item" data-action="select-none">None</div>';
        html += '<div class="context-menu-item" data-action="select-read">Read</div>';
        html += '<div class="context-menu-item" data-action="select-unread">Unread</div>';
        html += '<div class="context-menu-item" data-action="select-starred">Starred</div>';
        html += '<div class="context-menu-item" data-action="select-unstarred">Unstarred</div>';
        html += '</div>';
        return html;
    },

    // ============================================================
    // SNOOZE PICKER (wraps Components.snoozePicker)
    // ============================================================

    renderSnoozePicker() {
        return Components.snoozePicker();
    },

    // ============================================================
    // SEARCH OPTIONS PANEL
    // ============================================================

    renderSearchOptions() {
        let html = '';
        html += '<div class="search-options-row">';
        html += '<label>From</label>';
        html += '<input type="text" class="form-input" id="searchFrom" data-testid="search-from" placeholder="">';
        html += '</div>';
        html += '<div class="search-options-row">';
        html += '<label>To</label>';
        html += '<input type="text" class="form-input" id="searchTo" data-testid="search-to" placeholder="">';
        html += '</div>';
        html += '<div class="search-options-row">';
        html += '<label>Subject</label>';
        html += '<input type="text" class="form-input" id="searchSubject" data-testid="search-subject" placeholder="">';
        html += '</div>';
        html += '<div class="search-options-row">';
        html += '<label>Has the words</label>';
        html += '<input type="text" class="form-input" id="searchHasWords" data-testid="search-has-words" placeholder="">';
        html += '</div>';
        html += '<div class="search-options-row">';
        html += '<label>Doesn\'t have</label>';
        html += '<input type="text" class="form-input" id="searchDoesntHave" data-testid="search-doesnt-have" placeholder="">';
        html += '</div>';
        html += '<div class="search-options-row">';
        html += '<label>Has attachment</label>';
        html += '<input type="checkbox" id="searchHasAttachment" data-testid="search-has-attachment" style="width:auto">';
        html += '</div>';

        html += '<div class="search-options-actions">';
        html += `<button class="btn btn-text" data-action="create-filter-from-search" data-testid="search-create-filter">Create filter</button>`;
        html += '<div>';
        html += `<button class="btn btn-secondary" data-action="close-search-options" style="margin-right:8px">Close</button>`;
        html += `<button class="btn btn-primary" data-action="advanced-search" data-testid="advanced-search-btn">Search</button>`;
        html += '</div>';
        html += '</div>';

        return html;
    },

    // ============================================================
    // CREATE / EDIT LABEL MODAL CONTENT
    // ============================================================

    renderCreateLabelModal(existingLabel) {
        const isEdit = !!existingLabel;
        const title = isEdit ? 'Edit label' : 'New label';
        const name = isEdit ? existingLabel.name : '';
        const currentColor = isEdit ? existingLabel.color : null;
        const parentId = isEdit ? existingLabel.parentId || '' : '';

        const topLevelLabels = AppState.getTopLevelUserLabels();
        const parentOptions = [{ id: '', name: '(no parent)' }];
        for (const l of topLevelLabels) {
            if (!isEdit || l.id !== existingLabel.id) {
                parentOptions.push({ id: l.id, name: l.name });
            }
        }

        let bodyHtml = '';
        bodyHtml += '<div class="form-group">';
        bodyHtml += Components.textInput('labelNameInput', name, 'Enter label name', 'Label name');
        bodyHtml += '</div>';

        bodyHtml += '<div class="form-group">';
        bodyHtml += '<label class="form-label">Nest label under</label>';
        bodyHtml += Components.dropdown('labelParentDropdown', parentOptions, parentId);
        bodyHtml += '</div>';

        bodyHtml += '<div class="form-group">';
        bodyHtml += '<label class="form-label">Label color</label>';
        bodyHtml += Components.labelColorPicker(currentColor);
        bodyHtml += '</div>';

        const footerHtml = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" id="saveLabelBtn" data-testid="save-label-btn"${isEdit ? ' data-label-id="' + Components.escapeAttr(existingLabel.id) + '"' : ''}>${isEdit ? 'Save' : 'Create'}</button>
        `;

        return { title, bodyHtml, footerHtml };
    },

    // ============================================================
    // CREATE / EDIT FILTER MODAL CONTENT
    // ============================================================

    renderCreateFilterModal(existingFilter) {
        const isEdit = !!existingFilter;
        const title = isEdit ? 'Edit filter' : 'Create filter';
        const c = isEdit ? existingFilter.criteria : { from: '', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' };
        const a = isEdit ? existingFilter.actions : { label: null, archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: null };

        const userLabels = AppState.getUserLabels();
        const labelOptions = [{ id: '', name: '(none)' }];
        for (const l of userLabels) {
            labelOptions.push({ id: l.id, name: l.name });
        }

        const catOptions = [
            { id: '', name: '(none)' },
            { id: 'primary', name: 'Primary' },
            { id: 'social', name: 'Social' },
            { id: 'promotions', name: 'Promotions' },
            { id: 'updates', name: 'Updates' },
            { id: 'forums', name: 'Forums' },
        ];

        let bodyHtml = '';
        bodyHtml += '<div style="font-size:13px;font-weight:600;color:var(--text-secondary);margin-bottom:12px">Criteria</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>From</label>';
        bodyHtml += `<input type="text" class="form-input" id="filterFrom" data-testid="filter-from" value="${Components.escapeAttr(c.from)}">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>To</label>';
        bodyHtml += `<input type="text" class="form-input" id="filterTo" data-testid="filter-to" value="${Components.escapeAttr(c.to)}">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>Subject</label>';
        bodyHtml += `<input type="text" class="form-input" id="filterSubject" data-testid="filter-subject" value="${Components.escapeAttr(c.subject)}">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>Has the words</label>';
        bodyHtml += `<input type="text" class="form-input" id="filterHasWords" data-testid="filter-has-words" value="${Components.escapeAttr(c.hasWords)}">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>Doesn\'t have</label>';
        bodyHtml += `<input type="text" class="form-input" id="filterDoesntHave" data-testid="filter-doesnt-have" value="${Components.escapeAttr(c.doesntHave)}">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>Has attachment</label>';
        bodyHtml += `<input type="checkbox" id="filterHasAttachment" data-testid="filter-has-attachment" ${c.hasAttachment ? 'checked' : ''} style="width:auto">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-row">';
        bodyHtml += '<label>Size</label>';
        bodyHtml += `<input type="number" class="form-input" id="filterSize" data-testid="filter-size" value="${c.size || ''}" placeholder="Size" style="width:80px">`;
        bodyHtml += Components.dropdown('filterSizeUnit', [
            { id: 'MB', name: 'MB' },
            { id: 'KB', name: 'KB' },
            { id: 'Bytes', name: 'Bytes' },
        ], c.sizeUnit);
        bodyHtml += Components.dropdown('filterSizeComparison', [
            { id: 'greater', name: 'greater than' },
            { id: 'less', name: 'less than' },
        ], c.sizeComparison);
        bodyHtml += '</div>';

        bodyHtml += '<div style="font-size:13px;font-weight:600;color:var(--text-secondary);margin:16px 0 12px">Actions</div>';

        bodyHtml += '<div class="filter-actions-group">';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionArchive" data-testid="filter-action-archive" ${a.archive ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionArchive">Skip the Inbox (Archive it)</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionMarkRead" data-testid="filter-action-read" ${a.markRead ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionMarkRead">Mark as read</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionStar" data-testid="filter-action-star" ${a.star ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionStar">Star it</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += '<label style="width:100px">Apply the label</label>';
        bodyHtml += Components.dropdown('filterActionLabel', labelOptions, a.label || '');
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += '<label style="width:100px">Forward to</label>';
        bodyHtml += `<input type="text" class="form-input" id="filterActionForward" data-testid="filter-action-forward" value="${Components.escapeAttr(a.forward || '')}" placeholder="email address" style="flex:1">`;
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionDelete" data-testid="filter-action-delete" ${a.delete ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionDelete">Delete it</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionNeverSpam" data-testid="filter-action-never-spam" ${a.neverSpam ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionNeverSpam">Never send it to Spam</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionAlwaysImportant" data-testid="filter-action-always-important" ${a.alwaysImportant ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionAlwaysImportant">Always mark it as important</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += `<input type="checkbox" id="filterActionNeverImportant" data-testid="filter-action-never-important" ${a.neverImportant ? 'checked' : ''}>`;
        bodyHtml += '<label for="filterActionNeverImportant">Never mark it as important</label>';
        bodyHtml += '</div>';

        bodyHtml += '<div class="filter-action-item">';
        bodyHtml += '<label style="width:100px">Categorize as</label>';
        bodyHtml += Components.dropdown('filterActionCategory', catOptions, a.category || '');
        bodyHtml += '</div>';

        bodyHtml += '</div>';

        const footerHtml = `
            <button class="btn btn-secondary" data-action="close-modal">Cancel</button>
            <button class="btn btn-primary" id="saveFilterBtn" data-testid="save-filter-btn"${isEdit ? ' data-filter-id="' + Components.escapeAttr(existingFilter.id) + '"' : ''}>
                ${isEdit ? 'Update filter' : 'Create filter'}
            </button>
        `;

        return { title, bodyHtml, footerHtml };
    },

    // ============================================================
    // MAIN RENDER DISPATCHER
    // ============================================================

    render() {
        const view = AppState.currentView;

        // Sidebar
        const sidebarNav = document.getElementById('sidebarNav');
        if (sidebarNav) {
            sidebarNav.innerHTML = Views.renderSidebar();
        }

        // User avatar
        const userAvatar = document.getElementById('userAvatar');
        if (userAvatar && AppState.currentUser) {
            userAvatar.style.background = AppState.currentUser.avatarColor || '#1a73e8';
            const initials = AppState.currentUser.name.split(' ').map(w => w[0]).join('').substring(0, 2).toUpperCase();
            const initialsEl = document.getElementById('userInitials');
            if (initialsEl) initialsEl.textContent = initials;
        }

        // Density
        document.body.classList.remove('density-comfortable', 'density-compact');
        if (AppState.settings.density === 'comfortable') document.body.classList.add('density-comfortable');
        if (AppState.settings.density === 'compact') document.body.classList.add('density-compact');

        // Settings page takes over main content
        if (view === 'settings') {
            const toolbar = document.getElementById('toolbar');
            if (toolbar) toolbar.innerHTML = '';
            const content = document.getElementById('contentWrapper');
            if (content) content.innerHTML = Views.renderSettings();
            return;
        }

        // Email detail view
        if (AppState.currentEmailId) {
            const email = AppState.getEmailById(AppState.currentEmailId);
            const toolbar = document.getElementById('toolbar');
            if (toolbar) toolbar.innerHTML = '';
            const content = document.getElementById('contentWrapper');
            if (content) content.innerHTML = Views.renderEmailDetail(email);
            // Mark as read
            if (email && !email.isRead) {
                AppState.markAsRead([email.id]);
            }
            return;
        }

        // Search results
        if (AppState.searchResults !== null) {
            const toolbar = document.getElementById('toolbar');
            if (toolbar) toolbar.innerHTML = Views.renderToolbar('search', AppState.searchResults);
            const content = document.getElementById('contentWrapper');
            if (content) content.innerHTML = Views.renderSearchResults(AppState.searchResults);
            return;
        }

        // Normal list views
        let emails;
        if (view === 'inbox' && AppState.settings.categoriesEnabled) {
            emails = AppState.getInboxEmailsByCategory(AppState.currentCategory);
        } else {
            emails = AppState.getEmailsForView(view);
        }

        // Toolbar
        const toolbar = document.getElementById('toolbar');
        if (toolbar) {
            toolbar.innerHTML = Views.renderToolbar(view, emails);
        }

        // Content
        const content = document.getElementById('contentWrapper');
        if (content) {
            let contentHtml = '';
            // Category tabs for inbox view
            if (view === 'inbox' && AppState.settings.categoriesEnabled) {
                contentHtml += Views.renderCategoryTabs();
            }
            contentHtml += Views.renderEmailList(emails);
            content.innerHTML = contentHtml;
        }
    },
};

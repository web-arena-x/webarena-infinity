const Views = {

    // ---- Sidebar ----
    renderSidebar() {
        const unreadCount = AppState.getUnreadCount();
        const folders = [
            { id: 'inbox', name: 'Inbox', icon: '📥', count: unreadCount },
            { id: 'done', name: 'Done', icon: '✅', count: 0 },
            { id: 'reminders', name: 'Reminders', icon: '⏰', count: AppState.folderCounts.reminders || 0 },
            { id: 'sent', name: 'Sent', icon: '📤', count: 0 },
            { id: 'drafts', name: 'Drafts', icon: '📝', count: AppState.folderCounts.drafts || 0 },
            { id: 'scheduled', name: 'Scheduled', icon: '📅', count: AppState.folderCounts.scheduled || 0 },
            { id: 'trash', name: 'Trash', icon: '🗑️', count: 0 },
            { id: 'spam', name: 'Spam', icon: '⚠️', count: 0 }
        ];

        let html = '<div class="sidebar-header">';
        html += Components.avatar(AppState.currentUser.name, 36);
        html += `<div class="sidebar-user"><div class="sidebar-user-name">${Components.escapeHtml(AppState.currentUser.name)}</div>`;
        html += `<div class="sidebar-user-email">${Components.escapeHtml(AppState.currentUser.email)}</div></div></div>`;

        html += `<button class="compose-btn" data-action="compose"><span class="compose-icon">✏️</span> Compose</button>`;

        html += '<div class="sidebar-search"><input type="text" id="sidebarSearch" class="sidebar-search-input" placeholder="Search mail..." data-action="search-focus"><span class="search-shortcut">/</span></div>';

        html += '<nav class="sidebar-nav">';
        for (const f of folders) {
            const active = AppState.selectedFolder === f.id && !AppState.selectedEmailId && AppState.currentView !== 'settings' && AppState.currentView !== 'label' && AppState.currentView !== 'search' ? ' active' : '';
            html += `<a class="sidebar-nav-item${active}" data-action="navigate-folder" data-folder="${f.id}">`;
            html += `<span class="nav-icon">${f.icon}</span>`;
            html += `<span class="nav-label">${Components.escapeHtml(f.name)}</span>`;
            if (f.count > 0) {
                html += Components.badge(f.count);
            }
            html += '</a>';
        }
        html += '</nav>';

        // Labels section
        const userLabels = AppState.labels.filter(l => !l.isSystem);
        if (userLabels.length > 0) {
            html += '<div class="sidebar-section">';
            html += '<div class="sidebar-section-header">Labels</div>';
            for (const label of userLabels) {
                const active = AppState.currentView === 'label' && AppState.selectedLabelId === label.id ? ' active' : '';
                const bg = label.color ? label.color.background : '#e8eaed';
                html += `<a class="sidebar-nav-item sidebar-label${active}" data-action="navigate-label" data-label-id="${Components.escapeAttr(label.id)}">`;
                html += `<span class="label-dot" style="background:${bg}"></span>`;
                html += `<span class="nav-label">${Components.escapeHtml(label.name)}</span>`;
                html += '</a>';
            }
            html += '</div>';
        }

        html += '<div class="sidebar-footer">';
        html += `<a class="sidebar-nav-item${AppState.currentView === 'settings' ? ' active' : ''}" data-action="navigate-settings"><span class="nav-icon">⚙️</span><span class="nav-label">Settings</span></a>`;
        html += '</div>';

        return html;
    },

    // ---- Split Inbox Tabs ----
    renderSplitTabs() {
        if (AppState.selectedFolder !== 'inbox') return '';
        if (!AppState.settings.splitInbox.enabled) return '';

        const splitCounts = AppState.getSplitCounts();
        const activeSplits = AppState.splits.filter(s =>
            AppState.settings.splitInbox.splits.includes(s.id)
        ).sort((a, b) => a.order - b.order);

        let html = '<div class="split-tabs">';
        for (const split of activeSplits) {
            const active = AppState.selectedSplit === split.id ? ' active' : '';
            const count = splitCounts[split.id] || 0;
            html += `<button class="split-tab${active}" data-action="select-split" data-split-id="${Components.escapeAttr(split.id)}">`;
            html += `<span class="split-tab-name">${Components.escapeHtml(split.name)}</span>`;
            html += `<span class="split-tab-count">${count}</span>`;
            html += '</button>';
        }
        html += '</div>';
        return html;
    },

    // ---- Email List ----
    renderEmailList(emails, title) {
        if (title === undefined) title = '';

        if (!emails || emails.length === 0) {
            if (AppState.selectedFolder === 'inbox') {
                return Components.emptyState('Inbox Zero!', 'You\'ve reached Inbox Zero. Great work!', '🎉');
            }
            return Components.emptyState('No messages', 'Nothing to see here.', '📭');
        }

        let html = '';
        if (title) {
            html += `<div class="email-list-header"><h2>${Components.escapeHtml(title)}</h2></div>`;
        }

        html += '<div class="email-list">';
        for (const email of emails) {
            const unread = !email.isRead ? ' unread' : '';
            const selected = AppState.selectedEmailId === email.id ? ' selected' : '';
            const starred = email.isStarred ? ' starred' : '';

            html += `<div class="email-row${unread}${selected}${starred}" data-action="open-email" data-email-id="${Components.escapeAttr(email.id)}">`;

            // Star
            html += `<div class="email-star">${Components.starIcon(email.isStarred, email.id)}</div>`;

            // Avatar
            html += `<div class="email-avatar">${Components.avatar(email.from.name, 32)}</div>`;

            // From
            html += `<div class="email-from">${Components.escapeHtml(email.from.name)}</div>`;

            // Subject + snippet
            html += '<div class="email-content">';
            html += `<span class="email-subject">${Components.escapeHtml(email.subject)}</span>`;
            if (email.snippet) {
                html += `<span class="email-snippet"> — ${Components.escapeHtml(email.snippet)}</span>`;
            }
            html += '</div>';

            // Labels
            const emailLabels = email.labels.map(lid => AppState.labels.find(l => l.id === lid)).filter(Boolean);
            if (emailLabels.length > 0) {
                html += '<div class="email-labels">';
                for (const label of emailLabels) {
                    html += Components.labelTag(label);
                }
                html += '</div>';
            }

            // Indicators row
            html += '<div class="email-indicators">';
            if (email.reminder) html += Components.reminderBadge(email.reminder);
            if (email.hasAttachments) html += Components.attachmentBadge(email.attachments);
            html += '</div>';

            // Date
            html += `<div class="email-date">${Components.formatDate(email.date)}</div>`;

            // Read status (for sent emails)
            if (email.folder === 'sent' || (email.from.email === AppState.currentUser.email)) {
                html += `<div class="email-read-status">${Components.readStatusIndicator(email.readStatus)}</div>`;
            }

            html += '</div>';
        }
        html += '</div>';
        return html;
    },

    // ---- Email Detail View ----
    renderEmailDetail(emailId) {
        const email = AppState.getEmailById(emailId);
        if (!email) return Components.emptyState('Email not found', 'This email no longer exists.', '❓');

        // Get thread messages if any
        const threadEmails = AppState.getThreadEmails(email.threadId);
        const isThread = threadEmails.length > 1;

        let html = '<div class="email-detail">';

        // Toolbar
        html += '<div class="email-detail-toolbar">';
        html += `<button class="btn-icon" data-action="back-to-list" title="Back">←</button>`;
        html += '<div class="toolbar-spacer"></div>';
        html += `<button class="btn-icon" data-action="mark-done-current" title="Mark Done (E)">✅</button>`;
        html += `<button class="btn-icon" data-action="reminder-current" title="Remind Me (H)">⏰</button>`;
        html += `<button class="btn-icon" data-action="move-current" title="Move (V)">📁</button>`;
        html += `<button class="btn-icon" data-action="label-current" title="Label">🏷️</button>`;
        html += `<button class="btn-icon" data-action="trash-current" title="Trash">🗑️</button>`;
        html += `<button class="btn-icon" data-action="toggle-star-current" title="Star">★</button>`;
        html += `<button class="btn-icon" data-action="mark-unread-current" title="Mark Unread">📩</button>`;
        html += `<button class="btn-icon" data-action="unsubscribe-current" title="Unsubscribe (Ctrl+U)">🚫</button>`;
        html += '</div>';

        // Subject header
        html += '<div class="email-detail-header">';
        html += `<h2 class="email-detail-subject">${Components.escapeHtml(email.subject)}</h2>`;
        // Labels
        const emailLabels = email.labels.map(lid => AppState.labels.find(l => l.id === lid)).filter(Boolean);
        if (emailLabels.length > 0) {
            html += '<div class="email-detail-labels">';
            for (const label of emailLabels) html += Components.labelTag(label);
            html += '</div>';
        }
        html += '</div>';

        // Render messages (thread or single)
        const messages = isThread ? threadEmails : [email];
        const allMessages = [...messages];
        if (email.threadMessages && email.threadMessages.length > 0 && !isThread) {
            for (const tm of email.threadMessages) {
                allMessages.push(tm);
            }
            allMessages.sort((a, b) => new Date(a.date) - new Date(b.date));
        }

        for (let i = 0; i < allMessages.length; i++) {
            const msg = allMessages[i];
            const isLast = i === allMessages.length - 1;
            const collapsed = !isLast && allMessages.length > 2 ? ' collapsed' : '';

            html += `<div class="email-message${collapsed}" data-message-index="${i}">`;

            // Message header
            html += '<div class="message-header">';
            html += Components.avatar(msg.from.name, 40);
            html += '<div class="message-header-info">';
            html += `<div class="message-from">${Components.escapeHtml(msg.from.name)} <span class="message-email">&lt;${Components.escapeHtml(msg.from.email)}&gt;</span></div>`;
            html += '<div class="message-meta">';
            html += `<span class="message-to">to ${(msg.to || []).map(t => Components.escapeHtml(t.name || t.email)).join(', ')}`;
            if (msg.cc && msg.cc.length > 0) {
                html += `, cc: ${msg.cc.map(c => Components.escapeHtml(c.name || c.email)).join(', ')}`;
            }
            html += '</span>';
            html += `<span class="message-date">${Components.formatFullDate(msg.date)}</span>`;
            html += '</div></div>';

            // Read status for sent messages
            if (msg.readStatus && msg.readStatus.enabled) {
                html += `<div class="message-read-status">${Components.readStatusIndicator(msg.readStatus)}</div>`;
            }
            html += '</div>';

            // Message body
            html += `<div class="message-body">${msg.body || ''}</div>`;

            // Attachments
            if (msg.hasAttachments && msg.attachments && msg.attachments.length > 0) {
                html += '<div class="message-attachments">';
                for (const att of msg.attachments) {
                    html += `<div class="attachment-item"><span class="attachment-icon">📎</span><span class="attachment-name">${Components.escapeHtml(att.name)}</span><span class="attachment-size">${att.size}</span></div>`;
                }
                html += '</div>';
            }

            html += '</div>';
        }

        // Reply/Forward toolbar at bottom
        html += '<div class="email-reply-bar">';
        html += `<button class="btn btn-default reply-btn" data-action="reply" data-email-id="${Components.escapeAttr(email.id)}"><span>↩</span> Reply</button>`;
        html += `<button class="btn btn-default reply-btn" data-action="reply-all" data-email-id="${Components.escapeAttr(email.id)}"><span>↩↩</span> Reply All</button>`;
        html += `<button class="btn btn-default reply-btn" data-action="forward" data-email-id="${Components.escapeAttr(email.id)}"><span>↪</span> Forward</button>`;
        html += '</div>';

        // Popover containers (hidden by default, shown on button click)
        html += '<div id="reminderPopover" class="popover" style="display:none"></div>';
        html += '<div id="labelPopover" class="popover" style="display:none"></div>';
        html += '<div id="folderPopover" class="popover" style="display:none"></div>';

        html += '</div>';
        return html;
    },

    // ---- Composer ----
    renderComposer(draft) {
        if (!draft) draft = AppState.composerDraft || {};

        let html = '<div class="composer">';
        html += '<div class="composer-header">';
        html += `<span class="composer-title">${draft.replyTo ? 'Reply' : draft.forwardOf ? 'Forward' : 'New Message'}</span>`;
        html += `<button class="btn-icon" data-action="close-composer" title="Close">✕</button>`;
        html += '</div>';

        html += '<div class="composer-fields">';
        // To field
        html += '<div class="composer-field"><label>To</label>';
        html += `<input type="text" id="composeTo" class="composer-input" value="${Components.escapeAttr((draft.to || []).map(t => t.email).join(', '))}" placeholder="Recipients">`;
        html += `<span class="composer-cc-toggle" data-action="toggle-cc">Cc</span>`;
        html += `<span class="composer-bcc-toggle" data-action="toggle-bcc">Bcc</span>`;
        html += '</div>';

        // Cc field
        html += `<div class="composer-field composer-cc" id="composeCcField" style="display:${(draft.cc && draft.cc.length > 0) ? 'flex' : 'none'}"><label>Cc</label>`;
        html += `<input type="text" id="composeCc" class="composer-input" value="${Components.escapeAttr((draft.cc || []).map(t => t.email).join(', '))}" placeholder="Cc recipients"></div>`;

        // Bcc field
        html += `<div class="composer-field composer-bcc" id="composeBccField" style="display:${(draft.bcc && draft.bcc.length > 0) ? 'flex' : 'none'}"><label>Bcc</label>`;
        html += `<input type="text" id="composeBcc" class="composer-input" value="${Components.escapeAttr((draft.bcc || []).map(t => t.email).join(', '))}" placeholder="Bcc recipients"></div>`;

        // Subject
        html += '<div class="composer-field"><label>Subject</label>';
        html += `<input type="text" id="composeSubject" class="composer-input" value="${Components.escapeAttr(draft.subject || '')}" placeholder="Subject"></div>`;

        html += '</div>';

        // Body
        html += `<div class="composer-body" id="composeBody" contenteditable="true" data-placeholder="Write your message...">${draft.body || ''}</div>`;

        // Signature
        if (AppState.settings.signatures && AppState.settings.signatures.default) {
            html += `<div class="composer-signature">${AppState.settings.signatures.default}</div>`;
        }

        // Toolbar
        html += '<div class="composer-toolbar">';
        html += `<button class="btn btn-primary" data-action="send-email">Send</button>`;
        html += `<button class="btn btn-default" data-action="schedule-send" title="Schedule Send">🕐 Schedule</button>`;
        html += `<button class="btn-icon" data-action="insert-snippet" title="Insert Snippet (;)">📋</button>`;
        html += `<button class="btn-icon" data-action="attach-file" title="Attach">📎</button>`;
        html += `<button class="btn-icon" data-action="discard-draft" title="Discard">🗑️</button>`;
        html += '</div>';

        html += '</div>';
        return html;
    },

    // ---- Search Results ----
    renderSearchResults() {
        let html = '<div class="search-view">';
        html += '<div class="search-header">';
        html += `<input type="text" id="searchInput" class="search-main-input" value="${Components.escapeAttr(AppState.searchQuery)}" placeholder="Search emails... (from:, to:, subject:, has:attachment, is:unread)" autofocus>`;
        html += '</div>';

        if (AppState.searchQuery && AppState.searchResults.length === 0) {
            html += Components.emptyState('No results', `No emails match "${AppState.searchQuery}"`, '🔍');
        } else if (AppState.searchResults.length > 0) {
            html += `<div class="search-results-count">${AppState.searchResults.length} result${AppState.searchResults.length !== 1 ? 's' : ''}</div>`;
            html += Views.renderEmailList(AppState.searchResults);
        } else {
            html += '<div class="search-tips">';
            html += '<h3>Search operators</h3>';
            html += '<div class="search-tip"><code>from:</code> Search by sender</div>';
            html += '<div class="search-tip"><code>to:</code> Search by recipient</div>';
            html += '<div class="search-tip"><code>subject:</code> Search by subject</div>';
            html += '<div class="search-tip"><code>has:attachment</code> Emails with attachments</div>';
            html += '<div class="search-tip"><code>is:unread</code> Unread emails</div>';
            html += '<div class="search-tip"><code>is:starred</code> Starred emails</div>';
            html += '<div class="search-tip"><code>label:</code> Search by label</div>';
            html += '<div class="search-tip"><code>in:</code> Search by folder</div>';
            html += '</div>';
        }
        html += '</div>';
        return html;
    },

    // ---- Settings View ----
    renderSettings() {
        const tabs = [
            { id: 'general', label: 'General' },
            { id: 'split-inbox', label: 'Split Inbox' },
            { id: 'labels', label: 'Labels' },
            { id: 'auto-labels', label: 'Auto Labels' },
            { id: 'reminders', label: 'Reminders' },
            { id: 'read-statuses', label: 'Read Statuses' },
            { id: 'auto-drafts', label: 'Auto Drafts' },
            { id: 'calendar', label: 'Calendar' },
            { id: 'snippets', label: 'Snippets' },
            { id: 'auto-archive', label: 'Auto Archive' },
            { id: 'signatures', label: 'Signatures' },
            { id: 'blocked', label: 'Blocked Senders' }
        ];

        const activeTab = AppState.settingsTab || 'general';

        let html = '<div class="settings-view">';
        html += '<div class="settings-header"><h2>Settings</h2></div>';

        // Tabs
        html += '<div class="settings-tabs">';
        for (const tab of tabs) {
            const active = activeTab === tab.id ? ' active' : '';
            html += `<button class="settings-tab${active}" data-action="settings-tab" data-tab="${tab.id}">${Components.escapeHtml(tab.label)}</button>`;
        }
        html += '</div>';

        // Tab content
        html += '<div class="settings-content">';
        const methodName = 'renderSettings_' + activeTab.replace(/-/g, '_');
        if (typeof Views[methodName] === 'function') {
            html += Views[methodName]();
        } else {
            html += '<p>Settings panel coming soon.</p>';
        }
        html += '</div>';

        html += '</div>';
        return html;
    },

    // ---- Settings Sub-panels ----

    renderSettings_general() {
        const s = AppState.settings.general;
        let html = '<div class="settings-panel">';
        html += '<h3>Appearance</h3>';
        html += Components.dropdown('setting-theme', 'Theme', [
            { value: 'dark', label: 'Dark' },
            { value: 'light', label: 'Light' },
            { value: 'auto', label: 'Auto' }
        ], s.theme);

        html += Components.dropdown('setting-density', 'Display density', [
            { value: 'compact', label: 'Compact' },
            { value: 'comfortable', label: 'Comfortable' },
            { value: 'spacious', label: 'Spacious' }
        ], s.density);

        html += '<h3>Behavior</h3>';
        html += Components.toggle('setting-keyboard-shortcuts', 'Keyboard shortcuts', s.keyboardShortcuts, 'Enable keyboard shortcuts for faster navigation');
        html += Components.toggle('setting-desktop-notifications', 'Desktop notifications', s.desktopNotifications, 'Show desktop notifications for new emails');
        html += Components.toggle('setting-sound-notifications', 'Sound notifications', s.soundNotifications, 'Play sound for new emails');
        html += Components.toggle('setting-auto-advance', 'Auto-advance', s.autoAdvance, 'Automatically advance to next message after an action');

        html += Components.dropdown('setting-undo-send', 'Undo send delay', [
            { value: '5', label: '5 seconds' },
            { value: '10', label: '10 seconds' },
            { value: '20', label: '20 seconds' },
            { value: '30', label: '30 seconds' }
        ], String(s.undoSendDelay));

        html += Components.dropdown('setting-default-reply', 'Default reply action', [
            { value: 'reply', label: 'Reply' },
            { value: 'reply-all', label: 'Reply All' }
        ], s.defaultReplyAction);

        html += '</div>';
        return html;
    },

    renderSettings_split_inbox() {
        const s = AppState.settings.splitInbox;
        let html = '<div class="settings-panel">';
        html += '<h3>Split Inbox</h3>';
        html += Components.toggle('setting-split-enabled', 'Enable Split Inbox', s.enabled, 'Divide your inbox into focused sections');

        if (s.enabled) {
            html += '<div class="splits-list">';
            html += '<h4>Active Splits</h4>';
            const activeSplits = AppState.splits.filter(sp => s.splits.includes(sp.id)).sort((a, b) => a.order - b.order);
            for (const split of activeSplits) {
                html += `<div class="split-item">`;
                html += `<span class="split-name">${Components.escapeHtml(split.icon || '')} ${Components.escapeHtml(split.name)}</span>`;
                if (!split.isDefault) {
                    html += `<button class="btn-icon btn-small" data-action="remove-split" data-split-id="${Components.escapeAttr(split.id)}" title="Remove">✕</button>`;
                }
                html += '</div>';
            }
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    renderSettings_labels() {
        const userLabels = AppState.labels.filter(l => !l.isSystem);
        let html = '<div class="settings-panel">';
        html += '<h3>Labels</h3>';
        html += `<button class="btn btn-primary" data-action="create-label">+ Create Label</button>`;
        html += '<div class="labels-list">';
        for (const label of userLabels) {
            const bg = label.color ? label.color.background : '#e8eaed';
            const fg = label.color ? label.color.text : '#5f6368';
            html += `<div class="label-setting-item">`;
            html += `<span class="label-swatch-large" style="background:${bg};color:${fg}"></span>`;
            html += `<span class="label-setting-name">${Components.escapeHtml(label.name)}</span>`;
            html += `<button class="btn-icon btn-small" data-action="edit-label" data-label-id="${Components.escapeAttr(label.id)}" title="Edit">✏️</button>`;
            html += `<button class="btn-icon btn-small" data-action="delete-label" data-label-id="${Components.escapeAttr(label.id)}" title="Delete">🗑️</button>`;
            html += '</div>';
        }
        html += '</div></div>';
        return html;
    },

    renderSettings_auto_labels() {
        let html = '<div class="settings-panel">';
        html += '<h3>Auto Labels</h3>';
        html += '<p class="settings-description">AI-powered labels that automatically categorize your email.</p>';
        html += '<div class="auto-labels-list">';
        for (const al of AppState.autoLabels) {
            html += `<div class="auto-label-item">`;
            html += Components.toggle('auto-label-' + al.id, al.name, al.isEnabled, al.description);
            html += '</div>';
        }
        html += '</div></div>';
        return html;
    },

    renderSettings_reminders() {
        const s = AppState.settings.reminders;
        let html = '<div class="settings-panel">';
        html += '<h3>Reminders</h3>';

        html += `<div class="setting-row"><label>Default reminder time</label>`;
        html += Components.dropdown('setting-reminder-time', 'Default time', [
            { value: '08:00', label: '8:00 AM' },
            { value: '09:00', label: '9:00 AM' },
            { value: '10:00', label: '10:00 AM' },
            { value: '12:00', label: '12:00 PM' },
            { value: '14:00', label: '2:00 PM' },
            { value: '17:00', label: '5:00 PM' }
        ], s.defaultTime);
        html += '</div>';

        html += '<h4>Auto Reminders</h4>';
        html += '<p class="settings-description">Automatically remind you to follow up on sent emails that haven\'t received a reply.</p>';
        html += Components.radioGroup('auto-reminders', [
            { value: 'all-follow-ups', label: 'All messages that need a follow-up', description: 'AI detects sent messages without replies' },
            { value: 'external-only', label: 'Messages with external recipients only', description: 'Only track emails to people outside your organization' },
            { value: 'off', label: 'Off', description: 'Disable auto reminders' }
        ], s.autoReminders);

        html += Components.dropdown('setting-reminder-delay', 'Auto reminder delay', [
            { value: '1', label: '1 day' },
            { value: '2', label: '2 days' },
            { value: '3', label: '3 days' },
            { value: '5', label: '5 days' },
            { value: '7', label: '7 days' }
        ], String(s.autoReminderDelay));

        html += '</div>';
        return html;
    },

    renderSettings_read_statuses() {
        const s = AppState.settings.readStatuses;
        let html = '<div class="settings-panel">';
        html += '<h3>Read Statuses</h3>';
        html += Components.toggle('setting-read-statuses', 'Enable read statuses', s.enabled, 'Track when your sent emails are opened');
        html += Components.toggle('setting-team-read-statuses', 'Team read statuses', s.teamReadStatuses, 'Share read status data across your team');
        html += Components.toggle('setting-team-reply-indicators', 'Team reply indicators', s.teamReplyIndicators, 'See when a teammate is drafting a reply');
        html += Components.toggle('setting-recent-opens', 'Recent Opens feed', s.recentOpensEnabled, 'Show a real-time feed of email opens');
        html += '</div>';
        return html;
    },

    renderSettings_auto_drafts() {
        const s = AppState.settings.autoDrafts;
        let html = '<div class="settings-panel">';
        html += '<h3>Auto Drafts</h3>';
        html += '<p class="settings-description">When a reminder returns, Auto Drafts generates a follow-up draft in your voice.</p>';
        html += Components.toggle('setting-auto-drafts-followups', 'Follow-up drafts', s.followUps, 'Auto-draft follow-ups for emails still awaiting replies');
        html += Components.toggle('setting-auto-drafts-scheduling', 'Scheduling drafts', s.scheduling, 'Auto-draft replies when someone asks to meet');
        html += '</div>';
        return html;
    },

    renderSettings_calendar() {
        const s = AppState.settings.calendar;
        let html = '<div class="settings-panel">';
        html += '<h3>Calendar</h3>';

        html += Components.dropdown('setting-calendar-view', 'Default view', [
            { value: 'day', label: 'Day' },
            { value: 'week', label: 'Week' }
        ], s.defaultView);

        html += Components.dropdown('setting-week-start', 'Week starts on', [
            { value: 'sunday', label: 'Sunday' },
            { value: 'monday', label: 'Monday' }
        ], s.weekStartsOn);

        html += Components.toggle('setting-show-weekends', 'Show weekends', s.showWeekends, 'Display Saturday and Sunday in the week view');

        html += Components.dropdown('setting-meeting-duration', 'Default meeting duration', [
            { value: '15', label: '15 minutes' },
            { value: '30', label: '30 minutes' },
            { value: '45', label: '45 minutes' },
            { value: '60', label: '60 minutes' }
        ], String(s.defaultMeetingDuration));

        html += Components.dropdown('setting-meeting-link-provider', 'Meeting link', [
            { value: 'google-meet', label: 'Google Meet' },
            { value: 'zoom', label: 'Zoom' },
            { value: 'none', label: 'None' }
        ], s.meetingLinkProvider);

        html += Components.dropdown('setting-event-notifications', 'Event notifications', [
            { value: 'none', label: 'None' },
            { value: '5-minutes', label: '5 minutes before' },
            { value: '10-minutes', label: '10 minutes before' },
            { value: '15-minutes', label: '15 minutes before' },
            { value: '30-minutes', label: '30 minutes before' }
        ], s.eventNotifications);

        html += '<h4>Calendars</h4>';
        for (const cal of s.calendars) {
            html += `<div class="calendar-setting-item">`;
            html += `<span class="calendar-dot" style="background:${cal.color}"></span>`;
            html += `<span>${Components.escapeHtml(cal.name)}</span>`;
            html += `<span class="calendar-provider">${Components.escapeHtml(cal.provider)}</span>`;
            html += `<label class="toggle-switch"><input type="checkbox" ${cal.enabled ? 'checked' : ''} data-action="toggle-calendar" data-calendar-id="${Components.escapeAttr(cal.id)}"><span class="toggle-slider"></span></label>`;
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    renderSettings_snippets() {
        let html = '<div class="settings-panel">';
        html += '<h3>Snippets</h3>';
        html += `<button class="btn btn-primary" data-action="create-snippet">+ Create Snippet</button>`;
        html += '<div class="snippets-list">';

        // Personal snippets
        const personal = AppState.snippets.filter(s => !s.isShared);
        if (personal.length > 0) {
            html += '<h4>My Snippets</h4>';
            for (const snippet of personal) {
                html += Views._renderSnippetItem(snippet);
            }
        }

        // Team snippets
        const team = AppState.snippets.filter(s => s.isShared);
        if (team.length > 0) {
            html += '<h4>Team Snippets</h4>';
            for (const snippet of team) {
                html += Views._renderSnippetItem(snippet);
            }
        }

        html += '</div></div>';
        return html;
    },

    _renderSnippetItem(snippet) {
        let html = `<div class="snippet-item" data-snippet-id="${Components.escapeAttr(snippet.id)}">`;
        html += `<div class="snippet-name">${Components.escapeHtml(snippet.name)}</div>`;
        html += '<div class="snippet-meta">';
        html += `<span>by ${Components.escapeHtml(snippet.author)}</span>`;
        html += `<span class="snippet-metrics">${snippet.metrics.sends} sends · ${snippet.metrics.openRate}% open · ${snippet.metrics.responseRate}% reply</span>`;
        html += '</div>';
        html += '<div class="snippet-actions">';
        html += `<button class="btn-icon btn-small" data-action="edit-snippet" data-snippet-id="${Components.escapeAttr(snippet.id)}" title="Edit">✏️</button>`;
        html += `<button class="btn-icon btn-small" data-action="delete-snippet" data-snippet-id="${Components.escapeAttr(snippet.id)}" title="Delete">🗑️</button>`;
        if (!snippet.isShared) {
            html += `<button class="btn btn-small btn-default" data-action="share-snippet" data-snippet-id="${Components.escapeAttr(snippet.id)}">Share with team</button>`;
        }
        html += '</div></div>';
        return html;
    },

    renderSettings_auto_archive() {
        const s = AppState.settings.autoArchive;
        let html = '<div class="settings-panel">';
        html += '<h3>Auto Archive</h3>';
        html += '<p class="settings-description">Emails matching specified Auto Labels skip the inbox and go to Done.</p>';
        html += Components.toggle('setting-auto-archive-enabled', 'Enable Auto Archive', s.enabled, 'Automatically archive matching emails');

        if (s.enabled) {
            html += '<h4>Auto Labels to Auto Archive</h4>';
            for (const al of AppState.autoLabels) {
                const checked = s.autoLabels.includes(al.id);
                html += `<label class="auto-archive-item"><input type="checkbox" ${checked ? 'checked' : ''} data-action="toggle-auto-archive-label" data-autolabel-id="${Components.escapeAttr(al.id)}"><span>${Components.escapeHtml(al.name)}</span></label>`;
            }
        }

        html += '</div>';
        return html;
    },

    renderSettings_signatures() {
        const sig = AppState.settings.signatures.default;
        let html = '<div class="settings-panel">';
        html += '<h3>Signature</h3>';
        html += '<p class="settings-description">Your signature is appended to all outgoing emails.</p>';
        html += `<div class="signature-editor" id="signatureEditor" contenteditable="true">${sig || ''}</div>`;
        html += `<button class="btn btn-primary" data-action="save-signature" style="margin-top:12px">Save Signature</button>`;
        html += '</div>';
        return html;
    },

    renderSettings_blocked() {
        let html = '<div class="settings-panel">';
        html += '<h3>Blocked Senders</h3>';
        if (AppState.blockedSenders.length === 0) {
            html += '<p class="settings-description">No blocked senders.</p>';
        } else {
            html += '<div class="blocked-list">';
            for (const b of AppState.blockedSenders) {
                html += `<div class="blocked-item"><span>${Components.escapeHtml(b.email)}</span><span class="blocked-date">Blocked ${Components.formatDate(b.blockedAt)}</span>`;
                html += `<button class="btn btn-small btn-default" data-action="unblock-sender" data-email="${Components.escapeAttr(b.email)}">Unblock</button></div>`;
            }
            html += '</div>';
        }
        html += '</div>';
        return html;
    },

    // ---- Calendar Sidebar ----
    renderCalendarSidebar() {
        const today = new Date();
        const todayStr = today.toISOString().split('T')[0];

        const todayEvents = AppState.calendarEvents.filter(e => {
            const eventDate = e.start.split('T')[0];
            return eventDate === todayStr;
        }).sort((a, b) => new Date(a.start) - new Date(b.start));

        let html = '<div class="calendar-sidebar">';
        html += '<div class="calendar-sidebar-header">';
        html += `<h3>Today</h3>`;
        html += `<span class="calendar-date">${today.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' })}</span>`;
        html += `<button class="btn-icon" data-action="toggle-calendar-sidebar" title="Toggle calendar">📅</button>`;
        html += '</div>';

        if (todayEvents.length === 0) {
            html += '<div class="calendar-empty">No events today</div>';
        } else {
            html += '<div class="calendar-events">';
            for (const event of todayEvents) {
                const calSetting = AppState.settings.calendar.calendars.find(c => c.name === event.calendar);
                const color = calSetting ? calSetting.color : event.color || '#4285f4';

                html += `<div class="calendar-event" style="border-left:3px solid ${color}" data-action="view-event" data-event-id="${Components.escapeAttr(event.id)}">`;
                html += `<div class="calendar-event-time">${event.isAllDay ? 'All day' : Components.formatCalendarTime(event.start) + ' \u2013 ' + Components.formatCalendarTime(event.end)}</div>`;
                html += `<div class="calendar-event-title">${Components.escapeHtml(event.title)}</div>`;
                if (event.location) {
                    html += `<div class="calendar-event-location">${Components.escapeHtml(event.location)}</div>`;
                }
                if (event.meetingLink) {
                    html += `<div class="calendar-event-link">🔗 Join meeting</div>`;
                }
                html += '</div>';
            }
            html += '</div>';
        }

        html += `<button class="btn btn-default calendar-create-btn" data-action="create-event">+ Create Event</button>`;
        html += '</div>';
        return html;
    },

    // ---- Recent Opens Sidebar ----
    renderRecentOpens() {
        if (!AppState.settings.readStatuses.recentOpensEnabled) return '';

        let html = '<div class="recent-opens">';
        html += '<h3>Recent Opens</h3>';
        for (const open of AppState.recentOpens.slice(0, 10)) {
            html += `<div class="recent-open-item" data-action="open-email" data-email-id="${Components.escapeAttr(open.emailId)}">`;
            html += Components.avatar(open.recipientName, 24);
            html += `<div class="recent-open-info"><span class="recent-open-name">${Components.escapeHtml(open.recipientName)}</span>`;
            html += `<span class="recent-open-time">${Components.timeAgo(open.openedAt)} · ${open.device}</span></div></div>`;
        }
        html += '</div>';
        return html;
    },

    // ---- Snippet Picker (for inserting into composer) ----
    renderSnippetPicker() {
        let html = '<div class="snippet-picker">';
        html += '<div class="snippet-picker-header">Insert Snippet</div>';
        html += '<input type="text" id="snippetSearch" class="snippet-search-input" placeholder="Search snippets...">';
        html += '<div class="snippet-picker-list" id="snippetPickerList">';
        for (const snippet of AppState.snippets) {
            html += `<div class="snippet-picker-item" data-action="use-snippet" data-snippet-id="${Components.escapeAttr(snippet.id)}">`;
            html += `<div class="snippet-picker-name">${Components.escapeHtml(snippet.name)}</div>`;
            html += `<div class="snippet-picker-preview">${Components.escapeHtml((snippet.body || '').replace(/<[^>]*>/g, '').substring(0, 80))}...</div>`;
            html += '</div>';
        }
        html += '</div></div>';
        return html;
    }
};

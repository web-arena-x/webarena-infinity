/* ============================================================
   views.js — View rendering functions for Linear Account Settings
   ============================================================ */

const Views = {

    // ── Sidebar Navigation ───────────────────────────────────

    renderSidebar() {
        const sections = [
            { id: 'profile', label: 'Profile', icon: 'profile' },
            { id: 'preferences', label: 'Preferences', icon: 'preferences' },
            { id: 'notifications', label: 'Notifications', icon: 'notifications' },
            { id: 'security', label: 'Security & Access', icon: 'security' }
        ];

        let html = '<div class="sidebar-section">';
        html += '<div class="sidebar-header">Account</div>';

        for (const sec of sections) {
            const active = AppState.currentSection === sec.id ? ' active' : '';
            html += `<div class="nav-item${active}" data-route="${sec.id}" data-testid="nav-${sec.id}">`;
            html += `<span class="nav-icon">${Components.navIcon(sec.icon)}</span>`;
            html += `<span class="nav-label">${Components.escapeHtml(sec.label)}</span>`;
            html += `</div>`;
        }

        html += '</div>';

        // Workspace info at bottom
        const ws = AppState.workspaces[0];
        if (ws) {
            html += '<div class="sidebar-workspace">';
            html += `<div class="workspace-icon" style="background:${ws.logoColor}">${Components.escapeHtml(ws.name.substring(0, 1))}</div>`;
            html += `<div class="workspace-info">`;
            html += `<div class="workspace-name">${Components.escapeHtml(ws.name)}</div>`;
            html += `<div class="workspace-plan">${Components.escapeHtml(ws.plan)} plan</div>`;
            html += `</div></div>`;
        }

        return html;
    },

    // ── Profile Section ──────────────────────────────────────

    renderProfile() {
        const user = AppState.currentUser;
        let html = '<div class="settings-page" data-testid="profile-page">';
        html += '<h1 class="page-title">Profile</h1>';
        html += '<p class="page-description">Manage how other team members see you in your Linear workspace.</p>';

        // Avatar section
        html += '<div class="settings-card">';
        html += '<div class="profile-avatar-section">';
        html += '<div class="profile-avatar-wrapper">';
        html += Components.avatar(user, 80);
        html += `<button class="avatar-edit-btn" data-action="edit-avatar" title="Change avatar">${Components.pencilIcon()}</button>`;
        html += '</div>';
        html += '<div class="profile-avatar-info">';
        html += '<div class="profile-avatar-hint">Click to change your profile photo</div>';
        html += '</div>';
        html += '</div></div>';

        // Name and username
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Personal information</h2>';

        // Full name
        html += '<div class="field-row">';
        html += '<div class="field-label">Full name</div>';
        html += '<div class="field-value-row">';
        if (AppState.editingField === 'fullName') {
            html += `<input type="text" class="inline-edit-input" id="edit-fullName" value="${Components.escapeAttr(user.fullName)}" data-field="fullName" autofocus>`;
            html += '<button class="btn btn-small btn-primary" data-action="save-field" data-field="fullName">Save</button>';
            html += '<button class="btn btn-small btn-secondary" data-action="cancel-edit">Cancel</button>';
        } else {
            html += `<span class="field-value" data-testid="field-fullName">${Components.escapeHtml(user.fullName)}</span>`;
            html += `<button class="field-edit-btn" data-action="start-edit" data-field="fullName" title="Edit">${Components.pencilIcon()}</button>`;
        }
        html += '</div></div>';

        // Username
        html += '<div class="field-row">';
        html += '<div class="field-label">Username</div>';
        html += '<div class="field-value-row">';
        if (AppState.editingField === 'username') {
            html += `<input type="text" class="inline-edit-input" id="edit-username" value="${Components.escapeAttr(user.username)}" data-field="username" autofocus>`;
            html += '<button class="btn btn-small btn-primary" data-action="save-field" data-field="username">Save</button>';
            html += '<button class="btn btn-small btn-secondary" data-action="cancel-edit">Cancel</button>';
        } else {
            html += `<span class="field-value" data-testid="field-username">${Components.escapeHtml(user.username)}</span>`;
            html += `<button class="field-edit-btn" data-action="start-edit" data-field="username" title="Edit">${Components.pencilIcon()}</button>`;
        }
        html += '</div></div>';

        // Email
        html += '<div class="field-row">';
        html += '<div class="field-label">Email address</div>';
        html += '<div class="field-value-row">';
        if (AppState.editingField === 'email') {
            html += `<input type="text" class="inline-edit-input" id="edit-email" value="${Components.escapeAttr(user.email)}" data-field="email" autofocus>`;
            html += '<button class="btn btn-small btn-primary" data-action="save-field" data-field="email">Save</button>';
            html += '<button class="btn btn-small btn-secondary" data-action="cancel-edit">Cancel</button>';
        } else {
            html += `<span class="field-value" data-testid="field-email">${Components.escapeHtml(user.email)}</span>`;
            html += `<button class="field-edit-btn" data-action="start-edit" data-field="email" title="Edit">${Components.pencilIcon()}</button>`;
        }
        html += '</div>';
        html += '<div class="field-hint">Changing your email will update it across all workspaces.</div>';
        html += '</div>';

        html += '</div>'; // end settings-card

        // Connected Accounts
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Connected accounts</h2>';
        html += '<p class="card-description">Software integrations associated with your account.</p>';

        if (AppState.connectedAccounts.length === 0) {
            html += Components.emptyState('No connected accounts', 'Connect your accounts to integrate with other services.');
        } else {
            html += '<div class="connected-accounts-list">';
            for (const acct of AppState.connectedAccounts) {
                html += '<div class="connected-account-item" data-account-id="' + Components.escapeAttr(acct.id) + '">';
                html += `<div class="connected-account-icon">${Components.providerIcon(acct.providerIcon)}</div>`;
                html += '<div class="connected-account-info">';
                html += `<div class="connected-account-provider">${Components.escapeHtml(acct.provider)}</div>`;
                html += `<div class="connected-account-email">${Components.escapeHtml(acct.accountEmail)}</div>`;
                html += '</div>';
                html += `<div class="connected-account-date">Connected ${Components.formatDate(acct.connectedAt)}</div>`;
                html += `<button class="btn btn-small btn-secondary btn-disconnect" data-action="disconnect-account" data-account-id="${Components.escapeAttr(acct.id)}">Disconnect</button>`;
                html += '</div>';
            }
            html += '</div>';
        }
        html += '</div>'; // end settings-card

        // Workspaces section
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Workspaces</h2>';
        html += '<div class="workspaces-list">';
        for (const ws of AppState.workspaces) {
            html += '<div class="workspace-item" data-workspace-id="' + Components.escapeAttr(ws.id) + '">';
            html += `<div class="workspace-item-icon" style="background:${ws.logoColor}">${Components.escapeHtml(ws.name.substring(0, 1))}</div>`;
            html += '<div class="workspace-item-info">';
            html += `<div class="workspace-item-name">${Components.escapeHtml(ws.name)}</div>`;
            html += `<div class="workspace-item-meta">${Components.escapeHtml(ws.plan)} plan &middot; ${ws.memberCount} members &middot; ${Components.escapeHtml(ws.currentUserRole)}</div>`;
            html += '</div>';
            if (ws.currentUserRole !== 'Owner') {
                html += `<button class="btn btn-small btn-danger-outline" data-action="leave-workspace" data-workspace-id="${Components.escapeAttr(ws.id)}">Leave workspace</button>`;
            }
            html += '</div>';
        }
        html += '</div></div>';

        html += '</div>'; // end settings-page
        return html;
    },

    // ── Preferences Section ──────────────────────────────────

    renderPreferences() {
        const prefs = AppState.preferences;
        let html = '<div class="settings-page" data-testid="preferences-page">';
        html += '<h1 class="page-title">Preferences</h1>';
        html += '<p class="page-description">Adjust your preferences to personalize your workflow.</p>';

        // General
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">General</h2>';

        // Default home view
        html += '<div class="setting-row">';
        html += '<div class="setting-info">';
        html += '<div class="setting-label">Default home view</div>';
        html += '<div class="setting-description">The view that opens when you log in to Linear.</div>';
        html += '</div>';
        html += '<div class="setting-control">';
        html += Components.dropdown('homeView', HOME_VIEW_OPTIONS.map(v => ({ value: v, label: v })), prefs.general.defaultHomeView);
        html += '</div>';
        html += '</div>';

        // Display full names
        html += Components.toggle('displayFullNames', prefs.general.displayFullNames, 'Display full names', 'Show team members\' full names instead of usernames.');

        // First day of the week
        html += '<div class="setting-row">';
        html += '<div class="setting-info">';
        html += '<div class="setting-label">First day of the week</div>';
        html += '<div class="setting-description">Choose how calendars display your weeks.</div>';
        html += '</div>';
        html += '<div class="setting-control">';
        html += Components.dropdown('firstDayOfWeek', FIRST_DAY_OPTIONS.map(v => ({ value: v, label: v })), prefs.general.firstDayOfWeek);
        html += '</div>';
        html += '</div>';

        // Convert emoticons
        html += Components.toggle('convertEmoticonToEmoji', prefs.general.convertEmoticonToEmoji, 'Convert text emoticons into emojis', 'Automatically convert text emoticons like :) into emoji.');

        html += '</div>'; // end card

        // Interface and Theme
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Interface and theme</h2>';

        // Theme
        html += '<div class="setting-row">';
        html += '<div class="setting-info">';
        html += '<div class="setting-label">Theme</div>';
        html += '<div class="setting-description">Choose your preferred color scheme.</div>';
        html += '</div>';
        html += '<div class="setting-control">';
        html += Components.radioGroup('theme', THEME_OPTIONS.map(t => ({ value: t.id, label: t.label, description: t.description })), prefs.interfaceAndTheme.theme);
        html += '</div>';
        html += '</div>';

        // Font size
        html += '<div class="setting-row">';
        html += '<div class="setting-info">';
        html += '<div class="setting-label">Font size</div>';
        html += '<div class="setting-description">Adjust the font size for the interface.</div>';
        html += '</div>';
        html += '<div class="setting-control">';
        html += Components.dropdown('fontSize', FONT_SIZE_OPTIONS.map(f => ({ value: f.id, label: f.label })), prefs.interfaceAndTheme.fontSize);
        html += '</div>';
        html += '</div>';

        // Pointer cursor
        html += Components.toggle('usePointerCursor', prefs.interfaceAndTheme.usePointerCursor, 'Use pointer cursor', 'Show a pointer cursor when hovering over interactive elements.');

        html += '</div>'; // end card

        // Desktop application
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Desktop application</h2>';

        html += Components.toggle('openLinksInDesktopApp', prefs.desktopApp.openLinksInDesktopApp, 'Open Linear URLs in desktop app', 'Attempt to open Linear URLs in the desktop app instead of the browser.');
        html += Components.toggle('showNotificationBadge', prefs.desktopApp.showNotificationBadge, 'Show notification badge', 'Display notification badges on your desktop app icon.');
        html += Components.toggle('enableSpellCheck', prefs.desktopApp.enableSpellCheck, 'Enable spell check', 'Enable spell checking in text inputs.');

        html += '</div>'; // end card

        // Automations and Workflows
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Automations and workflows</h2>';

        html += Components.toggle('autoAssignOnCreate', prefs.automationsAndWorkflows.autoAssignOnCreate, 'Auto-assign issues you create to yourself', 'Automatically assign issues to you when you create them.');
        html += Components.toggle('autoAssignOnStarted', prefs.automationsAndWorkflows.autoAssignOnStarted, 'Auto-assign issues on started status', 'Automatically assign issues to you when you move them to a started status.');

        // Git attachment format
        html += '<div class="setting-row">';
        html += '<div class="setting-info">';
        html += '<div class="setting-label">Git attachment format</div>';
        html += '<div class="setting-description">Choose how git attachments are displayed.</div>';
        html += '</div>';
        html += '<div class="setting-control">';
        html += Components.dropdown('gitAttachmentFormat', GIT_ATTACHMENT_FORMAT_OPTIONS.map(v => ({ value: v, label: v })), prefs.automationsAndWorkflows.gitAttachmentFormat);
        html += '</div>';
        html += '</div>';

        html += Components.toggle('onGitBranchCopyMoveToStarted', prefs.automationsAndWorkflows.onGitBranchCopyMoveToStarted, 'On git branch copy, move issue to started status', 'Move the issue to the first started status when you copy the git branch name.');
        html += Components.toggle('onGitBranchCopyAutoAssign', prefs.automationsAndWorkflows.onGitBranchCopyAutoAssign, 'On git branch copy, auto-assign to yourself', 'Auto-assign the issue to you when you copy the git branch name.');

        html += '</div>'; // end card

        html += '</div>'; // end settings-page
        return html;
    },

    // ── Notifications Section ────────────────────────────────

    renderNotifications() {
        let html = '<div class="settings-page" data-testid="notifications-page">';
        html += '<h1 class="page-title">Notifications</h1>';
        html += '<p class="page-description">Configure how and where you receive notifications from Linear.</p>';

        // Notification channels
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Notification channels</h2>';
        html += '<p class="card-description">Choose which channels you want to receive notifications through. A green dot means the channel is enabled.</p>';

        html += '<div class="notification-channels">';
        for (const channel of AppState.notificationChannels) {
            html += Views._renderNotificationChannel(channel);
        }
        html += '</div>';
        html += '</div>';

        // Email digest preferences
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Email digest delivery</h2>';
        html += '<p class="card-description">Configure when email notifications are sent.</p>';

        const edp = AppState.emailDigestPreferences;
        html += Components.toggle('sendImmediatelyOnUrgent', edp.sendImmediatelyOnUrgent, 'Send immediately for urgent issues', 'Send notification email immediately if an issue assigned to you is marked urgent or breaches SLA.');
        html += Components.toggle('delayLowPriorityOutsideWorkHours', edp.delayLowPriorityOutsideWorkHours, 'Delay low priority outside work hours', 'Delay low priority email notifications outside work hours until the next day. Work hours are 8 AM - 6 PM in your timezone.');

        html += '</div>';

        // Communication preferences
        html += '<div class="settings-card">';
        html += '<h2 class="card-title">Communication preferences</h2>';
        html += '<p class="card-description">Choose the types of communications you\'d like to receive from Linear.</p>';

        const cp = AppState.communicationPreferences;
        html += Components.toggle('comm-changelog', cp.changelog, 'Changelogs', 'Receive updates about new features and changes.');
        html += Components.toggle('comm-dpaUpdates', cp.dpaUpdates, 'DPA updates', 'Receive updates about Data Processing Agreement changes.');
        html += Components.toggle('comm-productAnnouncements', cp.productAnnouncements, 'Product announcements', 'Receive product announcements and feature highlights.');
        html += Components.toggle('comm-tipsAndTutorials', cp.tipsAndTutorials, 'Tips and tutorials', 'Receive helpful tips and tutorials for using Linear.');
        html += Components.toggle('comm-communityUpdates', cp.communityUpdates, 'Community updates', 'Receive updates from the Linear community.');

        html += '</div>';

        html += '</div>'; // end settings-page
        return html;
    },

    _renderNotificationChannel(channel) {
        let html = `<div class="notification-channel" data-channel-id="${Components.escapeAttr(channel.id)}" data-testid="channel-${Components.escapeAttr(channel.id)}">`;
        html += '<div class="channel-header" data-action="toggle-channel-details" data-channel-id="' + Components.escapeAttr(channel.id) + '">';
        html += `<div class="channel-status">${Components.statusDot(channel.enabled)}</div>`;
        html += '<div class="channel-info">';
        html += `<div class="channel-name">${Components.escapeHtml(channel.name)}</div>`;
        html += `<div class="channel-description">${Components.escapeHtml(channel.description)}</div>`;
        html += '</div>';
        html += `<div class="channel-arrow">${Components.chevronRightIcon()}</div>`;
        html += '</div>';

        // Expandable detail
        const expanded = AppState._expandedChannelId === channel.id;
        html += `<div class="channel-details${expanded ? ' expanded' : ''}">`;

        // Master toggle
        html += '<div class="channel-master-toggle">';
        html += Components.toggle('channel-enable-' + channel.id, channel.enabled, 'Enable ' + channel.name + ' notifications');
        html += '</div>';

        // Individual settings
        html += '<div class="channel-settings">';
        for (const setting of channel.settings) {
            html += '<div class="channel-setting-item">';
            html += Components.toggle(setting.id, setting.enabled, setting.label);
            html += '</div>';
        }
        html += '</div>';

        html += '</div>'; // end channel-details
        html += '</div>'; // end notification-channel
        return html;
    },

    // ── Security & Access Section ────────────────────────────

    renderSecurity() {
        let html = '<div class="settings-page" data-testid="security-page">';
        html += '<h1 class="page-title">Security & Access</h1>';
        html += '<p class="page-description">Manage your account security, sessions, and access credentials.</p>';

        // Sessions
        html += Views._renderSessionsCard();

        // Passkeys
        html += Views._renderPasskeysCard();

        // API Keys
        html += Views._renderApiKeysCard();

        // Authorized Applications
        html += Views._renderAuthorizedAppsCard();

        html += '</div>'; // end settings-page
        return html;
    },

    _renderSessionsCard() {
        let html = '<div class="settings-card">';
        html += '<div class="card-header-row">';
        html += '<div>';
        html += '<h2 class="card-title">Sessions</h2>';
        html += '<p class="card-description">See and manage your active sessions. Inactive sessions expire after 30 days.</p>';
        html += '</div>';
        if (AppState.sessions.length > 1) {
            html += '<button class="btn btn-small btn-danger-outline" data-action="revoke-all-sessions">Revoke all</button>';
        }
        html += '</div>';

        if (AppState.sessions.length === 0) {
            html += Components.emptyState('No sessions', 'No active sessions found.');
        } else {
            html += '<div class="sessions-list">';
            for (const session of AppState.sessions) {
                html += Views._renderSessionItem(session);
            }
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    _renderSessionItem(session) {
        const expanded = AppState.expandedSessionId === session.id;
        let html = `<div class="session-item${session.isCurrent ? ' current' : ''}${expanded ? ' expanded' : ''}" data-session-id="${Components.escapeAttr(session.id)}">`;

        html += '<div class="session-main" data-action="toggle-session" data-session-id="' + Components.escapeAttr(session.id) + '">';
        html += `<div class="session-device-icon">${Components.deviceIcon(session.sourceType)}</div>`;
        html += '<div class="session-info">';
        html += `<div class="session-device">${Components.escapeHtml(session.deviceName)}`;
        if (session.isCurrent) {
            html += ' <span class="session-current-badge">Current</span>';
        }
        html += '</div>';
        html += `<div class="session-meta">${Components.escapeHtml(session.browser)} &middot; ${Components.escapeHtml(session.location)} &middot; ${Components.timeAgo(session.lastSeen)}</div>`;
        html += '</div>';

        if (!session.isCurrent) {
            html += `<button class="btn btn-small btn-secondary session-revoke-btn" data-action="revoke-session" data-session-id="${Components.escapeAttr(session.id)}">Revoke access</button>`;
        }
        html += '</div>'; // end session-main

        // Expanded details
        if (expanded) {
            html += '<div class="session-details">';
            html += '<div class="session-detail-row"><span class="detail-label">IP Address</span><span class="detail-value">' + Components.escapeHtml(session.ipAddress) + '</span></div>';
            html += '<div class="session-detail-row"><span class="detail-label">Operating System</span><span class="detail-value">' + Components.escapeHtml(session.os) + '</span></div>';
            html += '<div class="session-detail-row"><span class="detail-label">Source Type</span><span class="detail-value">' + Components.escapeHtml(session.sourceType) + '</span></div>';
            html += '<div class="session-detail-row"><span class="detail-label">Signed In</span><span class="detail-value">' + Components.formatDateTime(session.signedInAt) + '</span></div>';
            html += '<div class="session-detail-row"><span class="detail-label">Last Seen</span><span class="detail-value">' + Components.formatDateTime(session.lastSeen) + '</span></div>';
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    _renderPasskeysCard() {
        let html = '<div class="settings-card">';
        html += '<div class="card-header-row">';
        html += '<div>';
        html += '<h2 class="card-title">Passkeys</h2>';
        html += '<p class="card-description">Passkeys allow secure and fast login without passwords. Supported by all major browsers and password managers.</p>';
        html += '</div>';
        html += `<button class="btn btn-small btn-primary" data-action="add-passkey">${Components.plusIcon()} Add passkey</button>`;
        html += '</div>';

        if (AppState.passkeys.length === 0) {
            html += Components.emptyState('No passkeys', 'Register a passkey for faster, more secure login.');
        } else {
            html += '<div class="passkeys-list">';
            for (const pk of AppState.passkeys) {
                html += '<div class="passkey-item" data-passkey-id="' + Components.escapeAttr(pk.id) + '">';
                html += `<div class="passkey-icon">${Components.keyIcon()}</div>`;
                html += '<div class="passkey-info">';
                html += `<div class="passkey-name" data-testid="passkey-name-${Components.escapeAttr(pk.id)}">${Components.escapeHtml(pk.name)}</div>`;
                html += `<div class="passkey-meta">Added ${Components.formatDate(pk.createdAt)} &middot; Last used ${Components.timeAgo(pk.lastUsedAt)}</div>`;
                html += '</div>';
                html += '<div class="passkey-actions">';
                html += `<button class="icon-btn" data-action="rename-passkey" data-passkey-id="${Components.escapeAttr(pk.id)}" title="Rename">${Components.pencilIcon()}</button>`;
                html += `<button class="icon-btn icon-btn-danger" data-action="remove-passkey" data-passkey-id="${Components.escapeAttr(pk.id)}" title="Remove">${Components.trashIcon()}</button>`;
                html += '</div>';
                html += '</div>';
            }
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    _renderApiKeysCard() {
        let html = '<div class="settings-card">';
        html += '<div class="card-header-row">';
        html += '<div>';
        html += '<h2 class="card-title">Personal API keys</h2>';
        html += '<p class="card-description">Create and manage API keys associated with your account.</p>';
        html += '</div>';
        html += `<button class="btn btn-small btn-primary" data-action="create-api-key">${Components.plusIcon()} Create key</button>`;
        html += '</div>';

        if (AppState.apiKeys.length === 0) {
            html += Components.emptyState('No API keys', 'Create an API key to access the Linear API.');
        } else {
            html += '<div class="api-keys-list">';
            for (const key of AppState.apiKeys) {
                html += '<div class="api-key-item" data-key-id="' + Components.escapeAttr(key.id) + '">';
                html += `<div class="api-key-icon">${Components.shieldIcon()}</div>`;
                html += '<div class="api-key-info">';
                html += `<div class="api-key-label" data-testid="api-key-label-${Components.escapeAttr(key.id)}">${Components.escapeHtml(key.label)}</div>`;
                html += `<div class="api-key-prefix">${Components.escapeHtml(key.prefix)}...****</div>`;
                html += '<div class="api-key-meta">';
                html += `Created ${Components.formatDate(key.createdAt)}`;
                if (key.lastUsedAt) {
                    html += ` &middot; Last used ${Components.timeAgo(key.lastUsedAt)}`;
                } else {
                    html += ' &middot; Never used';
                }
                if (key.expiresAt) {
                    const expires = new Date(key.expiresAt);
                    const now = new Date();
                    const daysUntil = Math.ceil((expires - now) / 86400000);
                    if (daysUntil <= 0) {
                        html += ' &middot; <span class="text-danger">Expired</span>';
                    } else if (daysUntil <= 30) {
                        html += ` &middot; <span class="text-warning">Expires in ${daysUntil} days</span>`;
                    } else {
                        html += ` &middot; Expires ${Components.formatDate(key.expiresAt)}`;
                    }
                }
                html += '</div>';
                html += '</div>';
                html += '<div class="api-key-actions">';
                html += `<button class="btn btn-small btn-secondary" data-action="revoke-api-key" data-key-id="${Components.escapeAttr(key.id)}">Revoke</button>`;
                html += '</div>';
                html += '</div>';
            }
            html += '</div>';
        }

        html += '</div>';
        return html;
    },

    _renderAuthorizedAppsCard() {
        let html = '<div class="settings-card">';
        html += '<div class="card-header-row">';
        html += '<div>';
        html += '<h2 class="card-title">Authorized applications</h2>';
        html += '<p class="card-description">View and manage OAuth applications authorized to access your account.</p>';
        html += '</div>';
        html += '</div>';

        if (AppState.authorizedApps.length === 0) {
            html += Components.emptyState('No authorized applications', 'No applications have been authorized to access your account.');
        } else {
            html += '<div class="authorized-apps-list">';
            for (const app of AppState.authorizedApps) {
                html += '<div class="authorized-app-item" data-app-id="' + Components.escapeAttr(app.id) + '">';
                html += `<div class="authorized-app-icon">${Components.appIcon(app.name)}</div>`;
                html += '<div class="authorized-app-info">';
                html += `<div class="authorized-app-name">${Components.escapeHtml(app.name)}</div>`;
                html += `<div class="authorized-app-desc">${Components.escapeHtml(app.description)}</div>`;
                html += '<div class="authorized-app-permissions">';
                for (const perm of app.permissions) {
                    html += `<span class="permission-badge">${Components.escapeHtml(perm)}</span>`;
                }
                html += '</div>';
                html += `<div class="authorized-app-meta">Authorized ${Components.formatDate(app.authorizedAt)} &middot; Last used ${Components.timeAgo(app.lastUsedAt)}</div>`;
                html += '</div>';
                html += `<button class="btn btn-small btn-secondary" data-action="revoke-app" data-app-id="${Components.escapeAttr(app.id)}">Revoke access</button>`;
                html += '</div>';
            }
            html += '</div>';
        }

        html += '</div>';
        return html;
    }
};

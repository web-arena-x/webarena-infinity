// ============================================================
// views.js — View renderers for each settings page
// ============================================================

const Views = {

    // ==================== PROFILE ====================

    profile() {
        const user = AppState.currentUser;
        const errors = AppState.validationErrors;

        let html = '';
        html += Components.renderBreadcrumb([
            { label: 'Settings', route: '/profile' },
            { label: 'Account' },
            { label: 'Profile' }
        ]);

        html += '<div class="page-header"><h1>Profile</h1></div>';
        html += '<p class="page-description">Personalize how other team members see you in your workspace.</p>';

        // Avatar section
        html += '<div class="settings-section" data-testid="section-avatar">';
        html += '<div class="avatar-section">';
        html += `<div class="avatar-wrapper">`;
        html += Components.avatar(user, 80);
        html += `<button class="avatar-edit-btn" data-action="change-avatar" data-testid="change-avatar-btn" title="Change avatar"><span class="edit-icon">&#9998;</span></button>`;
        html += `</div>`;
        html += `<div class="avatar-info"><p class="avatar-hint">Click to update your profile picture. Once updated, you can only replace it with another photo.</p></div>`;
        html += '</div>';
        html += '</div>';

        // Name and Username
        html += '<div class="settings-section" data-testid="section-name">';
        html += Components.sectionHeader('Name and Username');
        html += '<div class="form-grid">';
        html += Components.textInput('profileName', user.name, { label: 'Full name', placeholder: 'Enter your full name', error: errors.name || '' });
        html += Components.textInput('profileUsername', user.username, { label: 'Username', placeholder: 'Enter your username', error: errors.username || '' });
        html += '</div>';
        html += '<div class="form-actions">';
        html += '<button class="btn btn-primary" data-action="save-name" data-testid="save-name-btn">Save changes</button>';
        html += '</div>';
        html += '</div>';

        // Email Address
        html += '<div class="settings-section" data-testid="section-email">';
        html += Components.sectionHeader('Email address');
        html += `<div class="email-display">`;
        html += `<span class="email-value" data-testid="current-email">${Components.escapeHtml(user.email)}</span>`;
        html += `<button class="btn btn-secondary btn-sm" data-action="change-email" data-testid="change-email-btn">Change</button>`;
        html += `</div>`;
        html += Components.infoBox('Changing your email address will change it for all workspaces using this email.');
        html += '</div>';

        // Pronouns
        html += '<div class="settings-section" data-testid="section-pronouns">';
        html += Components.sectionHeader('Pronouns');
        html += Components.textInput('profilePronouns', user.pronouns, { label: 'Pronouns', placeholder: 'e.g., they/them, she/her, he/him' });
        html += '<div class="form-actions">';
        html += '<button class="btn btn-primary" data-action="save-pronouns" data-testid="save-pronouns-btn">Save</button>';
        html += '</div>';
        html += '</div>';

        // Timezone
        html += '<div class="settings-section" data-testid="section-timezone">';
        html += Components.sectionHeader('Timezone');
        html += Components.dropdown('profileTimezone', TIMEZONES.map(tz => ({ id: tz, name: tz })), user.timezone, { label: 'Timezone' });
        html += '<div class="form-actions">';
        html += '<button class="btn btn-primary" data-action="save-timezone" data-testid="save-timezone-btn">Save</button>';
        html += '</div>';
        html += '</div>';

        // Connected Accounts
        html += '<div class="settings-section" data-testid="section-connected-accounts">';
        html += Components.sectionHeader('Connected Accounts', {
            description: 'Software integrations where each user has their own account. This helps Linear associate your Linear user with third-party integration actions.',
            action: '<button class="btn btn-secondary btn-sm" data-action="add-connected-account" data-testid="add-connected-account-btn">Connect account</button>'
        });

        if (AppState.connectedAccounts.length === 0) {
            html += Components.emptyState('No connected accounts', { icon: '&#128279;' });
        } else {
            html += '<div class="list-container" data-testid="connected-accounts-list">';
            for (const account of AppState.connectedAccounts) {
                html += `<div class="list-item" data-testid="connected-account-${Components.escapeAttr(account.id)}">`;
                html += `<div class="list-item-left">`;
                html += `<div class="list-item-icon">${Views._providerIcon(account.provider)}</div>`;
                html += `<div class="list-item-info">`;
                html += `<div class="list-item-title">${Components.escapeHtml(account.provider)}</div>`;
                html += `<div class="list-item-subtitle">${Components.escapeHtml(account.username)} &middot; ${Components.escapeHtml(account.email)}</div>`;
                html += `</div></div>`;
                html += `<div class="list-item-right">`;
                html += `<span class="list-item-meta">Connected ${Components.formatDate(account.connectedAt)}</span>`;
                html += `<button class="btn btn-danger btn-sm" data-action="disconnect-account" data-account-id="${account.id}" data-testid="disconnect-${Components.escapeAttr(account.id)}">Disconnect</button>`;
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }
        html += '</div>';

        // Leave Workspace
        html += '<div class="settings-section danger-section" data-testid="section-leave-workspace">';
        html += Components.sectionHeader('Leave workspace');
        html += '<p class="section-warning-text">Once removed, you no longer have access to the workspace. An admin will have to unsuspend your account in order for you to log back in.</p>';
        html += '<button class="btn btn-danger" data-action="leave-workspace" data-testid="leave-workspace-btn">Leave workspace</button>';
        html += '</div>';

        return html;
    },

    // ==================== PREFERENCES ====================

    preferences() {
        const prefs = AppState.preferences;

        let html = '';
        html += Components.renderBreadcrumb([
            { label: 'Settings', route: '/profile' },
            { label: 'Account' },
            { label: 'Preferences' }
        ]);

        html += '<div class="page-header"><h1>Preferences</h1></div>';
        html += '<p class="page-description">Adjust your preferences to help you move faster and personalize your workflow.</p>';

        // General
        html += '<div class="settings-section" data-testid="section-general">';
        html += Components.sectionHeader('General');

        html += Components.dropdown('defaultHomeView',
            HOME_VIEW_OPTIONS,
            prefs.defaultHomeView,
            { label: 'Default home view' }
        );

        html += Components.toggle('displayFullNames', prefs.displayFullNames, {
            label: 'Display full names',
            description: 'Show team members\' full names instead of usernames'
        });

        html += Components.dropdown('firstDayOfWeek',
            FIRST_DAY_OPTIONS,
            prefs.firstDayOfWeek,
            { label: 'First day of the week' }
        );

        html += Components.toggle('convertTextEmoticons', prefs.convertTextEmoticons, {
            label: 'Convert text emoticons into emojis',
            description: 'Automatically convert text emoticons like :) into emojis'
        });

        html += '</div>';

        // Interface and Theme
        html += '<div class="settings-section" data-testid="section-interface">';
        html += Components.sectionHeader('Interface and theme');

        html += Components.dropdown('fontSize',
            FONT_SIZE_OPTIONS,
            prefs.fontSize,
            { label: 'Font size' }
        );

        html += Components.toggle('cursorPointer', prefs.cursorPointer, {
            label: 'Pointer cursor on interactive elements',
            description: 'Show a pointer cursor when hovering over clickable elements'
        });

        html += Components.dropdown('theme',
            THEME_OPTIONS,
            prefs.theme,
            { label: 'Theme' }
        );

        html += Components.textInput('customThemeName', prefs.customThemeName, {
            label: 'Custom theme name',
            placeholder: 'Enter a custom theme name (optional)'
        });

        html += '</div>';

        // Desktop Application
        html += '<div class="settings-section" data-testid="section-desktop">';
        html += Components.sectionHeader('Desktop application');

        html += Components.toggle('openLinearURLsInDesktopApp', prefs.openLinearURLsInDesktopApp, {
            label: 'Open Linear URLs in desktop app',
            description: 'Attempt to open Linear URLs in the desktop application'
        });

        html += Components.toggle('notificationBadge', prefs.notificationBadge, {
            label: 'Notification badge',
            description: 'Show notification badge on desktop app icon'
        });

        html += Components.toggle('spellCheck', prefs.spellCheck, {
            label: 'Spell check',
            description: 'Enable spell checking in text fields'
        });

        html += '</div>';

        // Automations and Workflows
        html += '<div class="settings-section" data-testid="section-automations">';
        html += Components.sectionHeader('Automations and workflows');

        html += Components.toggle('autoAssignOnCreate', prefs.autoAssignOnCreate, {
            label: 'Auto-assign issues you create to yourself',
            description: 'Automatically assign issues you create to yourself'
        });

        html += Components.toggle('autoAssignOnStarted', prefs.autoAssignOnStarted, {
            label: 'Auto-assign on move to started',
            description: 'Auto-assign issues to yourself when you move them to a started status'
        });

        html += Components.dropdown('gitAttachmentFormat',
            GIT_ATTACHMENT_FORMAT_OPTIONS,
            prefs.gitAttachmentFormat,
            { label: 'Git attachment format' }
        );

        html += Components.toggle('gitBranchMoveToStarted', prefs.gitBranchMoveToStarted, {
            label: 'On git branch copy, move issue to started status',
            description: 'Move the issue to the first started status when copying the git branch name'
        });

        html += Components.toggle('gitBranchAutoAssign', prefs.gitBranchAutoAssign, {
            label: 'On git branch copy, auto-assign to yourself',
            description: 'Auto-assign the issue to yourself when copying the git branch name'
        });

        html += '</div>';

        return html;
    },

    // ==================== NOTIFICATIONS ====================

    notifications() {
        let html = '';
        html += Components.renderBreadcrumb([
            { label: 'Settings', route: '/profile' },
            { label: 'Account' },
            { label: 'Notifications' }
        ]);

        html += '<div class="page-header"><h1>Notifications</h1></div>';
        html += '<p class="page-description">Receive alerts on important updates in the Linear desktop app, mobile app, Slack, or email.</p>';

        // Notification Channels
        html += '<div class="settings-section" data-testid="section-channels">';
        html += Components.sectionHeader('Notification channels', {
            description: 'Configure which channels you want to receive notifications through.'
        });

        html += '<div class="channel-grid" data-testid="channel-grid">';
        for (const [key, channel] of Object.entries(AppState.notificationChannels)) {
            html += `<div class="channel-card ${channel.enabled ? 'enabled' : 'disabled'}" data-testid="channel-${key}">`;
            html += `<div class="channel-card-header">`;
            html += `<div class="channel-card-title">`;
            html += Components.statusBadge(channel.enabled ? 'enabled' : 'disabled');
            html += `<span>${Components.escapeHtml(channel.name)}</span>`;
            html += `</div>`;
            html += Components.toggle(`channel-${key}`, channel.enabled, {});
            html += `</div>`;
            html += `<p class="channel-card-description">${Components.escapeHtml(channel.description)}</p>`;
            html += `</div>`;
        }
        html += '</div>';

        html += Components.infoBox('Notifications are grouped. For example, if you enable status changes, you will be notified for status, priority, and blocking relationship changes together.');

        html += '</div>';

        // Notification Groups
        html += '<div class="settings-section" data-testid="section-notification-groups">';
        html += Components.sectionHeader('Notification types', {
            description: 'Choose which types of notifications to receive on each channel.'
        });

        html += '<div class="notification-groups-table">';
        // Header
        html += '<div class="ng-header">';
        html += '<div class="ng-name-col">Notification type</div>';
        for (const [key, channel] of Object.entries(AppState.notificationChannels)) {
            html += `<div class="ng-channel-col">${Components.escapeHtml(channel.name)}</div>`;
        }
        html += '</div>';

        // Rows
        for (const group of AppState.notificationGroups) {
            html += `<div class="ng-row" data-testid="ng-row-${group.id}">`;
            html += `<div class="ng-name-col">`;
            html += `<div class="ng-name">${Components.escapeHtml(group.name)}</div>`;
            html += `<div class="ng-description">${Components.escapeHtml(group.description)}</div>`;
            html += `</div>`;
            for (const [key, channel] of Object.entries(AppState.notificationChannels)) {
                const isEnabled = group.channels[key];
                const channelDisabled = !channel.enabled;
                html += `<div class="ng-channel-col">`;
                html += `<div class="toggle-switch mini ${isEnabled ? 'on' : 'off'} ${channelDisabled ? 'disabled' : ''}" data-testid="ng-toggle-${group.id}-${key}" data-group-id="${group.id}" data-channel-id="${key}" data-checked="${isEnabled}" role="switch" aria-checked="${isEnabled}" tabindex="0">`;
                html += `<div class="toggle-knob"></div>`;
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }
        html += '</div>';
        html += '</div>';

        // Email Digest Settings
        html += '<div class="settings-section" data-testid="section-email-digest">';
        html += Components.sectionHeader('Email digest settings', {
            description: 'Email digests send a summary of unread notifications with time delays based on urgency.'
        });

        html += Components.toggle('sendImmediatelyOnUrgent', AppState.emailDigestSettings.sendImmediatelyOnUrgent, {
            label: 'Send immediately for urgent issues',
            description: 'Send a notification email immediately if an issue assigned to you is marked urgent'
        });

        html += Components.toggle('sendImmediatelyOnSLABreach', AppState.emailDigestSettings.sendImmediatelyOnSLABreach, {
            label: 'Send immediately on SLA breach',
            description: 'Send a notification email immediately when an issue breaches its SLA'
        });

        html += Components.toggle('delayLowPriorityToWorkHours', AppState.emailDigestSettings.delayLowPriorityToWorkHours, {
            label: 'Delay low priority emails to work hours',
            description: 'Delay low priority notification emails until work hours the next day (8 am - 6 pm in your timezone)'
        });

        html += '</div>';

        // Communication Preferences
        html += '<div class="settings-section" data-testid="section-communication">';
        html += Components.sectionHeader('Communication preferences', {
            description: 'Customize the types of updates you receive from Linear.'
        });

        html += Components.toggle('changelog', AppState.communicationPreferences.changelog, {
            label: 'Changelog updates',
            description: 'Receive updates about new features and improvements'
        });

        html += Components.toggle('dpaUpdates', AppState.communicationPreferences.dpaUpdates, {
            label: 'DPA updates',
            description: 'Receive updates about Data Processing Agreement changes'
        });

        html += Components.toggle('productUpdates', AppState.communicationPreferences.productUpdates, {
            label: 'Product updates',
            description: 'Receive product announcements and newsletters'
        });

        html += Components.toggle('tips', AppState.communicationPreferences.tips, {
            label: 'Tips and best practices',
            description: 'Receive tips on how to use Linear more effectively'
        });

        html += '</div>';

        // Issue Subscriptions
        html += '<div class="settings-section" data-testid="section-subscriptions">';
        html += Components.sectionHeader('Issue subscriptions', {
            description: 'You are automatically subscribed to issues you create, are assigned to, or are @mentioned in.'
        });

        if (AppState.issueSubscriptions.length === 0) {
            html += Components.emptyState('No issue subscriptions', { icon: '&#128276;' });
        } else {
            html += '<div class="list-container" data-testid="subscriptions-list">';
            for (const sub of AppState.issueSubscriptions) {
                html += `<div class="list-item" data-testid="subscription-${Components.escapeAttr(sub.id)}">`;
                html += `<div class="list-item-left">`;
                html += `<div class="list-item-info">`;
                html += `<div class="list-item-title"><span class="issue-id">${Components.escapeHtml(sub.issueId)}</span> ${Components.escapeHtml(sub.issueTitle)}</div>`;
                html += `<div class="list-item-subtitle">${Components.escapeHtml(sub.teamName)} &middot; ${Components.escapeHtml(sub.reason)} &middot; ${Components.timeAgo(sub.subscribedAt)}</div>`;
                html += `</div></div>`;
                html += `<div class="list-item-right">`;
                html += `<button class="btn btn-secondary btn-sm" data-action="unsubscribe" data-sub-id="${sub.id}" data-testid="unsubscribe-${Components.escapeAttr(sub.id)}">Unsubscribe</button>`;
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }

        html += '</div>';

        return html;
    },

    // ==================== SECURITY & ACCESS ====================

    security() {
        let html = '';
        html += Components.renderBreadcrumb([
            { label: 'Settings', route: '/profile' },
            { label: 'Account' },
            { label: 'Security & Access' }
        ]);

        html += '<div class="page-header"><h1>Security & Access</h1></div>';
        html += '<p class="page-description">Manage your account security, sessions, and authorized applications.</p>';

        // Sessions
        html += '<div class="settings-section" data-testid="section-sessions">';
        html += Components.sectionHeader('Sessions', {
            description: 'View and manage connected devices.',
            action: AppState.sessions.filter(s => !s.isCurrent).length > 0
                ? '<button class="btn btn-danger btn-sm" data-action="revoke-all-sessions" data-testid="revoke-all-sessions-btn">Revoke all</button>'
                : ''
        });

        html += Components.infoBox('Inactive sessions will be automatically expired after 30 days.');

        if (AppState.sessions.length === 0) {
            html += Components.emptyState('No active sessions');
        } else {
            html += '<div class="list-container" data-testid="sessions-list">';
            for (const session of AppState.sessions) {
                html += `<div class="list-item session-item ${session.isCurrent ? 'current-session' : ''}" data-testid="session-${Components.escapeAttr(session.id)}" data-session-id="${session.id}">`;
                html += `<div class="list-item-left">`;
                html += `<div class="session-icon">${Views._sessionIcon(session.sourceType)}</div>`;
                html += `<div class="list-item-info">`;
                html += `<div class="list-item-title">${Components.escapeHtml(session.deviceName)} ${session.isCurrent ? '<span class="current-badge">Current</span>' : ''}</div>`;
                html += `<div class="list-item-subtitle">${Components.escapeHtml(session.sourceType)} &middot; ${Components.escapeHtml(session.location)} &middot; Last seen ${Components.timeAgo(session.lastSeenAt)}</div>`;
                html += `</div></div>`;
                html += `<div class="list-item-right">`;
                html += `<button class="btn btn-secondary btn-sm" data-action="view-session" data-session-id="${session.id}" data-testid="view-session-${Components.escapeAttr(session.id)}">Details</button>`;
                if (!session.isCurrent) {
                    html += `<button class="btn btn-danger btn-sm" data-action="revoke-session" data-session-id="${session.id}" data-testid="revoke-session-${Components.escapeAttr(session.id)}">Revoke</button>`;
                }
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }
        html += '</div>';

        // Passkeys
        html += '<div class="settings-section" data-testid="section-passkeys">';
        html += Components.sectionHeader('Passkeys', {
            description: 'Passkeys allow secure and fast login without passwords. Supported by all major browsers, mobile operating systems, and password managers like 1Password.',
            action: '<button class="btn btn-primary btn-sm" data-action="add-passkey" data-testid="add-passkey-btn">Register device</button>'
        });

        if (AppState.passkeys.length === 0) {
            html += Components.emptyState('No passkeys registered', { icon: '&#128273;' });
        } else {
            html += '<div class="list-container" data-testid="passkeys-list">';
            for (const pk of AppState.passkeys) {
                html += `<div class="list-item" data-testid="passkey-${Components.escapeAttr(pk.id)}">`;
                html += `<div class="list-item-left">`;
                html += `<div class="list-item-icon"><span class="passkey-icon">&#128273;</span></div>`;
                html += `<div class="list-item-info">`;
                html += `<div class="list-item-title">${Components.escapeHtml(pk.name)}</div>`;
                html += `<div class="list-item-subtitle">Registered ${Components.formatDate(pk.createdAt)} &middot; Last used ${pk.lastUsedAt ? Components.timeAgo(pk.lastUsedAt) : 'Never'}</div>`;
                html += `</div></div>`;
                html += `<div class="list-item-right">`;
                html += `<button class="btn btn-secondary btn-sm" data-action="rename-passkey" data-passkey-id="${pk.id}" data-testid="rename-passkey-${Components.escapeAttr(pk.id)}">Rename</button>`;
                html += `<button class="btn btn-danger btn-sm" data-action="remove-passkey" data-passkey-id="${pk.id}" data-testid="remove-passkey-${Components.escapeAttr(pk.id)}">Remove</button>`;
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }
        html += '</div>';

        // Personal API Keys
        html += '<div class="settings-section" data-testid="section-api-keys">';
        html += Components.sectionHeader('Personal API keys', {
            description: 'Create and manage API keys associated with your account.',
            action: '<button class="btn btn-primary btn-sm" data-action="create-api-key" data-testid="create-api-key-btn">Create key</button>'
        });

        if (AppState.apiKeys.length === 0) {
            html += Components.emptyState('No API keys', { icon: '&#128272;' });
        } else {
            html += '<div class="list-container" data-testid="api-keys-list">';
            for (const key of AppState.apiKeys) {
                html += `<div class="list-item" data-testid="api-key-${Components.escapeAttr(key.id)}">`;
                html += `<div class="list-item-left">`;
                html += `<div class="list-item-icon"><span class="key-icon">&#128272;</span></div>`;
                html += `<div class="list-item-info">`;
                html += `<div class="list-item-title">${Components.escapeHtml(key.label)}</div>`;
                html += `<div class="list-item-subtitle"><code>${Components.escapeHtml(key.prefix)}</code> &middot; Created ${Components.formatDate(key.createdAt)} &middot; Last used ${key.lastUsedAt ? Components.timeAgo(key.lastUsedAt) : 'Never'}</div>`;
                html += `</div></div>`;
                html += `<div class="list-item-right">`;
                html += `<button class="btn btn-secondary btn-sm" data-action="rename-api-key" data-key-id="${key.id}" data-testid="rename-api-key-${Components.escapeAttr(key.id)}">Rename</button>`;
                html += `<button class="btn btn-danger btn-sm" data-action="revoke-api-key" data-key-id="${key.id}" data-testid="revoke-api-key-${Components.escapeAttr(key.id)}">Revoke</button>`;
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }
        html += '</div>';

        // Authorized Applications
        html += '<div class="settings-section" data-testid="section-authorized-apps">';
        html += Components.sectionHeader('Authorized applications', {
            description: 'View and manage OAuth applications that have been granted access to your account.'
        });

        if (AppState.authorizedApps.length === 0) {
            html += Components.emptyState('No authorized applications');
        } else {
            html += '<div class="list-container" data-testid="authorized-apps-list">';
            for (const app of AppState.authorizedApps) {
                html += `<div class="list-item" data-testid="auth-app-${Components.escapeAttr(app.id)}">`;
                html += `<div class="list-item-left">`;
                html += `<div class="list-item-icon">${Views._appIcon(app.icon)}</div>`;
                html += `<div class="list-item-info">`;
                html += `<div class="list-item-title">${Components.escapeHtml(app.name)}</div>`;
                html += `<div class="list-item-subtitle">${Components.escapeHtml(app.description)}</div>`;
                html += `<div class="list-item-permissions">${app.permissions.map(p => Components.permissionBadge(p)).join(' ')}</div>`;
                html += `</div></div>`;
                html += `<div class="list-item-right">`;
                html += `<span class="list-item-meta">Authorized ${Components.formatDate(app.authorizedAt)}</span>`;
                html += `<button class="btn btn-danger btn-sm" data-action="revoke-app" data-app-id="${app.id}" data-testid="revoke-app-${Components.escapeAttr(app.id)}">Revoke access</button>`;
                html += `</div>`;
                html += `</div>`;
            }
            html += '</div>';
        }
        html += '</div>';

        return html;
    },

    // ==================== Helper Methods ====================

    _providerIcon(provider) {
        const icons = {
            'GitHub': '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>',
            'GitLab': '<svg width="20" height="20" viewBox="0 0 24 24" fill="#FC6D26"><path d="M23.6 9.593L13.5.288a1.282 1.282 0 00-3 0L.4 9.593a2.567 2.567 0 00-.08 2.816l11.07 15.272a1.128 1.128 0 001.82 0L24.28 12.41a2.567 2.567 0 00-.08-2.816h-.6z"/></svg>',
            'Slack': '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0 018.834 24a2.528 2.528 0 01-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 01-2.521-2.52A2.528 2.528 0 018.834 0a2.528 2.528 0 012.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 012.521 2.521 2.528 2.528 0 01-2.521 2.521H2.522A2.528 2.528 0 010 8.834a2.528 2.528 0 012.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 012.522-2.521A2.528 2.528 0 0124 8.834a2.528 2.528 0 01-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 01-2.523 2.521 2.527 2.527 0 01-2.52-2.521V2.522A2.527 2.527 0 0115.165 0a2.528 2.528 0 012.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 012.523 2.522A2.528 2.528 0 0115.165 24a2.527 2.527 0 01-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 01-2.52-2.523 2.526 2.526 0 012.52-2.52h6.313A2.527 2.527 0 0124 15.165a2.528 2.528 0 01-2.522 2.523h-6.313z"/></svg>',
            'Figma': '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M15.852 8.981h-4.588V0h4.588c2.476 0 4.49 2.014 4.49 4.49s-2.014 4.491-4.49 4.491zM12.735 7.51h3.117c1.665 0 3.019-1.355 3.019-3.019s-1.355-3.019-3.019-3.019h-3.117V7.51zM8.148 24c-2.476 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h4.588v4.441c0 2.503-2.014 4.539-4.588 4.539zm-.001-7.509a3.023 3.023 0 00-3.019 3.019c0 1.665 1.365 3.068 3.019 3.068 1.683 0 3.117-1.372 3.117-3.068v-3.019H8.147zM8.148 8.981c-2.476 0-4.49-2.014-4.49-4.49S5.672 0 8.148 0h4.588v8.981H8.148zm0-7.51a3.023 3.023 0 00-3.019 3.019c0 1.665 1.355 3.019 3.019 3.019h3.117V1.471H8.148zM8.148 15.02c-2.476 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h4.588v8.981H8.148zm0-7.51a3.023 3.023 0 00-3.019 3.02c0 1.664 1.355 3.019 3.019 3.019h3.117V7.51H8.148zM15.852 15.02h-4.588v-8.98h4.588c2.476 0 4.49 2.013 4.49 4.49 0 2.476-2.014 4.49-4.49 4.49zm0-7.51h-3.117v5.999h3.117c1.665 0 3.019-1.355 3.019-3.019s-1.354-3.02-3.019-3.02z"/></svg>',
            'Google': '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>'
        };
        return icons[provider] || `<span class="provider-letter">${(provider || '?')[0]}</span>`;
    },

    _sessionIcon(sourceType) {
        const icons = {
            'Desktop App': '&#128187;',
            'Web Browser': '&#127760;',
            'Mobile App': '&#128241;',
            'API Client': '&#9881;',
            'CLI': '&#62;_'
        };
        return `<span class="session-type-icon">${icons[sourceType] || '&#128187;'}</span>`;
    },

    _appIcon(iconName) {
        const icons = {
            'github': '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>',
            'slack': '<svg width="24" height="24" viewBox="0 0 24 24" fill="#E01E5A"><path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zm1.271 0a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0 018.834 24a2.528 2.528 0 01-2.521-2.522v-6.313z"/></svg>',
            'figma': '<svg width="24" height="24" viewBox="0 0 24 24" fill="#F24E1E"><path d="M15.852 8.981h-4.588V0h4.588c2.476 0 4.49 2.014 4.49 4.49s-2.014 4.491-4.49 4.491z"/></svg>',
            'sentry': '<svg width="24" height="24" viewBox="0 0 24 24" fill="#362D59"><circle cx="12" cy="12" r="10"/><text x="12" y="16" text-anchor="middle" fill="white" font-size="12" font-weight="bold">S</text></svg>',
            'zendesk': '<svg width="24" height="24" viewBox="0 0 24 24" fill="#03363D"><circle cx="12" cy="12" r="10"/><text x="12" y="16" text-anchor="middle" fill="white" font-size="12" font-weight="bold">Z</text></svg>',
            'notion': '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><rect x="2" y="2" width="20" height="20" rx="3" fill="none" stroke="currentColor" stroke-width="1.5"/><text x="12" y="16" text-anchor="middle" font-size="12" font-weight="bold">N</text></svg>'
        };
        return icons[iconName] || `<span class="app-icon-placeholder">${(iconName || '?')[0].toUpperCase()}</span>`;
    }
};

/* ============================================================
   data.js — Seed data for the Linear Account Settings app
   ============================================================ */

const SEED_DATA_VERSION = 1;

// ── Current User ──────────────────────────────────────────────
const CURRENT_USER = {
    id: 'usr_10001',
    fullName: 'Alexandra Chen',
    username: 'alexchen',
    email: 'alexandra.chen@acmetech.io',
    avatarUrl: null,
    avatarColor: '#5E6AD2',
    timezone: 'America/Los_Angeles',
    role: 'Admin',
    createdAt: '2024-03-15T09:00:00Z',
    updatedAt: '2026-02-28T14:30:00Z'
};

// ── Workspaces ────────────────────────────────────────────────
const WORKSPACES = [
    {
        id: 'ws_001',
        name: 'Acme Tech',
        slug: 'acme-tech',
        logoColor: '#5E6AD2',
        memberCount: 47,
        plan: 'Business',
        createdAt: '2024-01-10T08:00:00Z',
        currentUserRole: 'Admin'
    },
    {
        id: 'ws_002',
        name: 'Side Project Labs',
        slug: 'side-project-labs',
        logoColor: '#26B5CE',
        memberCount: 5,
        plan: 'Free',
        createdAt: '2025-06-20T12:00:00Z',
        currentUserRole: 'Member'
    }
];

// ── Connected Accounts ────────────────────────────────────────
const CONNECTED_ACCOUNTS = [
    {
        id: 'conn_001',
        provider: 'Google',
        providerIcon: 'google',
        accountEmail: 'alexandra.chen@gmail.com',
        connectedAt: '2024-03-15T09:05:00Z',
        status: 'active'
    },
    {
        id: 'conn_002',
        provider: 'GitHub',
        providerIcon: 'github',
        accountEmail: 'alexchen',
        connectedAt: '2024-03-16T10:20:00Z',
        status: 'active'
    },
    {
        id: 'conn_003',
        provider: 'GitLab',
        providerIcon: 'gitlab',
        accountEmail: 'alexandra.chen',
        connectedAt: '2025-01-08T15:45:00Z',
        status: 'active'
    },
    {
        id: 'conn_004',
        provider: 'Slack',
        providerIcon: 'slack',
        accountEmail: 'alexandra.chen@acmetech.io',
        connectedAt: '2024-04-02T11:30:00Z',
        status: 'active'
    },
    {
        id: 'conn_005',
        provider: 'Figma',
        providerIcon: 'figma',
        accountEmail: 'alexandra.chen@acmetech.io',
        connectedAt: '2024-09-14T08:15:00Z',
        status: 'active'
    }
];

// ── Preferences ───────────────────────────────────────────────
const PREFERENCES = {
    general: {
        defaultHomeView: 'Active issues',
        displayFullNames: true,
        firstDayOfWeek: 'Monday',
        convertEmoticonToEmoji: true
    },
    interfaceAndTheme: {
        theme: 'system',
        fontSize: 'default',
        usePointerCursor: false,
        customTheme: null
    },
    desktopApp: {
        openLinksInDesktopApp: true,
        showNotificationBadge: true,
        enableSpellCheck: true
    },
    automationsAndWorkflows: {
        autoAssignOnCreate: false,
        autoAssignOnStarted: false,
        gitAttachmentFormat: 'Title only',
        onGitBranchCopyMoveToStarted: true,
        onGitBranchCopyAutoAssign: true
    }
};

// ── Notification Settings ─────────────────────────────────────
const NOTIFICATION_CHANNELS = [
    {
        id: 'notif_desktop',
        name: 'Desktop',
        icon: 'desktop',
        enabled: true,
        description: 'Receive notifications via the Linear desktop app',
        settings: [
            { id: 'desktop_issue_assigned', label: 'Issue assigned to you', enabled: true },
            { id: 'desktop_issue_status', label: 'Status changes on subscribed issues', enabled: true },
            { id: 'desktop_issue_comment', label: 'New comments on subscribed issues', enabled: true },
            { id: 'desktop_issue_mention', label: 'Mentioned in an issue or comment', enabled: true },
            { id: 'desktop_project_update', label: 'Project updates', enabled: false },
            { id: 'desktop_cycle_update', label: 'Cycle updates', enabled: false },
            { id: 'desktop_sla_breach', label: 'SLA breach warnings', enabled: true }
        ]
    },
    {
        id: 'notif_mobile',
        name: 'Mobile',
        icon: 'mobile',
        enabled: true,
        description: 'Receive push notifications on your mobile device',
        settings: [
            { id: 'mobile_issue_assigned', label: 'Issue assigned to you', enabled: true },
            { id: 'mobile_issue_status', label: 'Status changes on subscribed issues', enabled: false },
            { id: 'mobile_issue_comment', label: 'New comments on subscribed issues', enabled: true },
            { id: 'mobile_issue_mention', label: 'Mentioned in an issue or comment', enabled: true },
            { id: 'mobile_project_update', label: 'Project updates', enabled: false },
            { id: 'mobile_cycle_update', label: 'Cycle updates', enabled: false },
            { id: 'mobile_sla_breach', label: 'SLA breach warnings', enabled: true }
        ]
    },
    {
        id: 'notif_email',
        name: 'Email',
        icon: 'email',
        enabled: true,
        description: 'Receive email digests summarizing your unread notifications',
        settings: [
            { id: 'email_issue_assigned', label: 'Issue assigned to you', enabled: true },
            { id: 'email_issue_status', label: 'Status changes on subscribed issues', enabled: true },
            { id: 'email_issue_comment', label: 'New comments on subscribed issues', enabled: true },
            { id: 'email_issue_mention', label: 'Mentioned in an issue or comment', enabled: true },
            { id: 'email_project_update', label: 'Project updates', enabled: true },
            { id: 'email_cycle_update', label: 'Cycle updates', enabled: false },
            { id: 'email_sla_breach', label: 'SLA breach warnings', enabled: true }
        ]
    },
    {
        id: 'notif_slack',
        name: 'Slack',
        icon: 'slack',
        enabled: false,
        description: 'Receive notifications in Slack channels',
        settings: [
            { id: 'slack_issue_assigned', label: 'Issue assigned to you', enabled: false },
            { id: 'slack_issue_status', label: 'Status changes on subscribed issues', enabled: false },
            { id: 'slack_issue_comment', label: 'New comments on subscribed issues', enabled: false },
            { id: 'slack_issue_mention', label: 'Mentioned in an issue or comment', enabled: false },
            { id: 'slack_project_update', label: 'Project updates', enabled: false },
            { id: 'slack_cycle_update', label: 'Cycle updates', enabled: false },
            { id: 'slack_sla_breach', label: 'SLA breach warnings', enabled: false }
        ]
    }
];

const EMAIL_DIGEST_PREFERENCES = {
    sendImmediatelyOnUrgent: true,
    delayLowPriorityOutsideWorkHours: true,
    workHoursStart: '08:00',
    workHoursEnd: '18:00'
};

const COMMUNICATION_PREFERENCES = {
    changelog: true,
    dpaUpdates: true,
    productAnnouncements: true,
    tipsAndTutorials: false,
    communityUpdates: false
};

// ── Sessions ──────────────────────────────────────────────────
const SESSIONS = [
    {
        id: 'sess_001',
        deviceName: 'MacBook Pro 16"',
        browser: 'Chrome 122',
        os: 'macOS Sonoma',
        location: 'San Francisco, CA',
        ipAddress: '198.51.100.42',
        lastSeen: '2026-03-02T10:15:00Z',
        signedInAt: '2026-02-01T08:30:00Z',
        isCurrent: true,
        sourceType: 'Desktop'
    },
    {
        id: 'sess_002',
        deviceName: 'iPhone 15 Pro',
        browser: 'Linear iOS',
        os: 'iOS 18.3',
        location: 'San Francisco, CA',
        ipAddress: '198.51.100.43',
        lastSeen: '2026-03-01T22:45:00Z',
        signedInAt: '2026-01-15T12:00:00Z',
        isCurrent: false,
        sourceType: 'Mobile'
    },
    {
        id: 'sess_003',
        deviceName: 'Windows Desktop',
        browser: 'Firefox 134',
        os: 'Windows 11',
        location: 'New York, NY',
        ipAddress: '203.0.113.88',
        lastSeen: '2026-02-28T16:30:00Z',
        signedInAt: '2026-02-20T09:15:00Z',
        isCurrent: false,
        sourceType: 'Desktop'
    },
    {
        id: 'sess_004',
        deviceName: 'iPad Air',
        browser: 'Safari 18',
        os: 'iPadOS 18.3',
        location: 'San Francisco, CA',
        ipAddress: '198.51.100.44',
        lastSeen: '2026-02-25T11:20:00Z',
        signedInAt: '2026-02-10T14:45:00Z',
        isCurrent: false,
        sourceType: 'Tablet'
    },
    {
        id: 'sess_005',
        deviceName: 'Linux Workstation',
        browser: 'Chrome 121',
        os: 'Ubuntu 24.04',
        location: 'Austin, TX',
        ipAddress: '192.0.2.156',
        lastSeen: '2026-02-15T09:00:00Z',
        signedInAt: '2026-01-05T10:30:00Z',
        isCurrent: false,
        sourceType: 'Desktop'
    },
    {
        id: 'sess_006',
        deviceName: 'Pixel 8',
        browser: 'Linear Android',
        os: 'Android 15',
        location: 'Chicago, IL',
        ipAddress: '198.51.100.99',
        lastSeen: '2026-02-10T07:30:00Z',
        signedInAt: '2025-12-20T16:00:00Z',
        isCurrent: false,
        sourceType: 'Mobile'
    },
    {
        id: 'sess_007',
        deviceName: 'MacBook Air M3',
        browser: 'Safari 18',
        os: 'macOS Sonoma',
        location: 'Portland, OR',
        ipAddress: '203.0.113.201',
        lastSeen: '2026-02-05T13:45:00Z',
        signedInAt: '2025-11-30T08:00:00Z',
        isCurrent: false,
        sourceType: 'Desktop'
    },
    {
        id: 'sess_008',
        deviceName: 'Windows Laptop',
        browser: 'Edge 122',
        os: 'Windows 11',
        location: 'Seattle, WA',
        ipAddress: '192.0.2.77',
        lastSeen: '2026-01-28T10:00:00Z',
        signedInAt: '2025-10-15T11:30:00Z',
        isCurrent: false,
        sourceType: 'Desktop'
    }
];

// ── Passkeys ──────────────────────────────────────────────────
const PASSKEYS = [
    {
        id: 'pk_001',
        name: 'MacBook Pro Touch ID',
        createdAt: '2025-04-10T09:00:00Z',
        lastUsedAt: '2026-03-01T08:30:00Z',
        deviceType: 'platform'
    },
    {
        id: 'pk_002',
        name: 'YubiKey 5C NFC',
        createdAt: '2025-06-22T14:30:00Z',
        lastUsedAt: '2026-02-15T10:00:00Z',
        deviceType: 'cross-platform'
    }
];

// ── Personal API Keys ─────────────────────────────────────────
const API_KEYS = [
    {
        id: 'apikey_001',
        label: 'CI/CD Pipeline',
        prefix: 'lin_api_a3f8',
        createdAt: '2025-01-12T10:00:00Z',
        lastUsedAt: '2026-03-02T06:00:00Z',
        expiresAt: null
    },
    {
        id: 'apikey_002',
        label: 'Slack Bot Integration',
        prefix: 'lin_api_7b2c',
        createdAt: '2025-03-05T15:30:00Z',
        lastUsedAt: '2026-02-28T12:00:00Z',
        expiresAt: '2026-06-05T15:30:00Z'
    },
    {
        id: 'apikey_003',
        label: 'Personal Scripts',
        prefix: 'lin_api_e9d1',
        createdAt: '2025-08-20T09:45:00Z',
        lastUsedAt: '2026-01-10T08:00:00Z',
        expiresAt: null
    },
    {
        id: 'apikey_004',
        label: 'Metrics Dashboard',
        prefix: 'lin_api_4f6a',
        createdAt: '2025-11-01T14:00:00Z',
        lastUsedAt: '2026-02-20T16:30:00Z',
        expiresAt: '2026-05-01T14:00:00Z'
    },
    {
        id: 'apikey_005',
        label: 'Staging Environment',
        prefix: 'lin_api_1c8e',
        createdAt: '2026-01-15T11:00:00Z',
        lastUsedAt: null,
        expiresAt: null
    }
];

// ── Authorized OAuth Applications ─────────────────────────────
const AUTHORIZED_APPS = [
    {
        id: 'oauth_001',
        name: 'Raycast',
        icon: 'raycast',
        description: 'Quick launcher integration',
        permissions: ['read:issues', 'write:issues', 'read:projects'],
        authorizedAt: '2025-02-14T09:00:00Z',
        lastUsedAt: '2026-03-01T17:30:00Z'
    },
    {
        id: 'oauth_002',
        name: 'Zapier',
        icon: 'zapier',
        description: 'Workflow automation platform',
        permissions: ['read:issues', 'write:issues', 'read:projects', 'write:projects', 'read:teams'],
        authorizedAt: '2025-04-20T13:00:00Z',
        lastUsedAt: '2026-02-28T22:00:00Z'
    },
    {
        id: 'oauth_003',
        name: 'Notion',
        icon: 'notion',
        description: 'Documentation and wiki sync',
        permissions: ['read:issues', 'read:projects'],
        authorizedAt: '2025-05-10T11:30:00Z',
        lastUsedAt: '2026-02-25T14:15:00Z'
    },
    {
        id: 'oauth_004',
        name: 'Sentry',
        icon: 'sentry',
        description: 'Error tracking integration',
        permissions: ['read:issues', 'write:issues', 'read:teams'],
        authorizedAt: '2025-07-01T08:45:00Z',
        lastUsedAt: '2026-03-02T03:00:00Z'
    },
    {
        id: 'oauth_005',
        name: 'Intercom',
        icon: 'intercom',
        description: 'Customer support ticket sync',
        permissions: ['read:issues', 'write:issues'],
        authorizedAt: '2025-08-15T16:00:00Z',
        lastUsedAt: '2026-02-20T09:30:00Z'
    },
    {
        id: 'oauth_006',
        name: 'Loom',
        icon: 'loom',
        description: 'Video recording attachments',
        permissions: ['read:issues'],
        authorizedAt: '2025-10-05T10:00:00Z',
        lastUsedAt: '2026-01-15T13:00:00Z'
    },
    {
        id: 'oauth_007',
        name: 'Retool',
        icon: 'retool',
        description: 'Internal tools dashboard',
        permissions: ['read:issues', 'read:projects', 'read:teams', 'read:cycles'],
        authorizedAt: '2025-11-20T14:30:00Z',
        lastUsedAt: '2026-02-10T11:00:00Z'
    },
    {
        id: 'oauth_008',
        name: 'Statuspage',
        icon: 'statuspage',
        description: 'Incident status page updates',
        permissions: ['read:issues', 'write:issues'],
        authorizedAt: '2026-01-05T09:00:00Z',
        lastUsedAt: '2026-02-01T15:45:00Z'
    }
];

// ── Home View Options ─────────────────────────────────────────
const HOME_VIEW_OPTIONS = [
    'All issues',
    'Active issues',
    'Current cycle',
    'Inbox',
    'My Issues',
    'Favorited Views',
    'Favorited Projects'
];

// ── First Day of Week Options ─────────────────────────────────
const FIRST_DAY_OPTIONS = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Saturday'
];

// ── Theme Options ─────────────────────────────────────────────
const THEME_OPTIONS = [
    { id: 'light', label: 'Light', description: 'Default light theme' },
    { id: 'dark', label: 'Dark', description: 'Dark mode' },
    { id: 'system', label: 'System', description: 'Match your system preference' }
];

// ── Font Size Options ─────────────────────────────────────────
const FONT_SIZE_OPTIONS = [
    { id: 'small', label: 'Small' },
    { id: 'default', label: 'Default' },
    { id: 'large', label: 'Large' }
];

// ── Git Attachment Format Options ─────────────────────────────
const GIT_ATTACHMENT_FORMAT_OPTIONS = [
    'Title only',
    'Title and repository'
];

// ── ID counters ───────────────────────────────────────────────
const INITIAL_NEXT_IDS = {
    _nextApiKeyId: 6,
    _nextPasskeyId: 3,
    _nextSessionId: 9,
    _nextConnectedAccountId: 6,
    _nextOAuthAppId: 9
};

// ============================================================
// data.js — Rich, realistic seed data for Linear Account Settings
// ============================================================

// Bump this version whenever seed data changes to invalidate stale localStorage.
const SEED_DATA_VERSION = 1;

// ---- Enums / Constants ----

const HOME_VIEW_OPTIONS = [
    { id: 'all_issues', name: 'All issues' },
    { id: 'active_issues', name: 'Active issues' },
    { id: 'current_cycle', name: 'Current cycle' },
    { id: 'inbox', name: 'Inbox' },
    { id: 'my_issues', name: 'My Issues' },
    { id: 'favorited_views', name: 'Favorited Views' },
    { id: 'favorited_projects', name: 'Favorited Projects' }
];

const FIRST_DAY_OPTIONS = [
    { id: 'sunday', name: 'Sunday' },
    { id: 'monday', name: 'Monday' },
    { id: 'saturday', name: 'Saturday' }
];

const THEME_OPTIONS = [
    { id: 'light', name: 'Light' },
    { id: 'dark', name: 'Dark' },
    { id: 'system', name: 'System preference' }
];

const FONT_SIZE_OPTIONS = [
    { id: 'small', name: 'Small' },
    { id: 'default', name: 'Default' },
    { id: 'large', name: 'Large' }
];

const GIT_ATTACHMENT_FORMAT_OPTIONS = [
    { id: 'title_only', name: 'Title only' },
    { id: 'title_and_repo', name: 'Title and repository' }
];

const NOTIFICATION_CHANNEL_STATUS = {
    ENABLED: { id: 'enabled', name: 'Enabled', color: 'green' },
    DISABLED: { id: 'disabled', name: 'Disabled', color: 'gray' }
};

const SESSION_SOURCE_TYPES = [
    'Desktop App', 'Web Browser', 'Mobile App', 'API Client', 'CLI'
];

const TIMEZONES = [
    'UTC',
    'America/New_York', 'America/Chicago', 'America/Denver',
    'America/Los_Angeles', 'America/Toronto', 'America/Sao_Paulo',
    'America/Mexico_City', 'America/Vancouver',
    'Europe/London', 'Europe/Dublin', 'Europe/Berlin', 'Europe/Paris',
    'Europe/Madrid', 'Europe/Warsaw', 'Europe/Amsterdam', 'Europe/Stockholm',
    'Africa/Cairo', 'Africa/Lagos', 'Africa/Johannesburg',
    'Asia/Kolkata', 'Asia/Tokyo', 'Asia/Shanghai', 'Asia/Singapore',
    'Asia/Seoul', 'Asia/Dubai', 'Asia/Hong_Kong',
    'Australia/Sydney', 'Australia/Melbourne',
    'Pacific/Auckland', 'Pacific/Honolulu'
];

// ---- Workspace Info ----
const WORKSPACE = {
    id: 'ws-7kx92f',
    name: 'Nextera Labs',
    slug: 'nextera-labs',
    plan: 'Business',
    createdAt: '2023-04-10T08:00:00Z'
};

// ---- Current User ----
const CURRENT_USER = {
    id: 1,
    name: 'Jordan Rivera',
    username: 'jordan.rivera',
    email: 'jordan.rivera@nextera.io',
    avatar: null,
    avatarColor: '#5E6AD2',
    pronouns: 'they/them',
    timezone: 'America/New_York',
    profileVisibility: 'public',
    createdAt: '2023-04-10T09:00:00Z',
    lastActivityAt: '2026-02-18T14:22:00Z'
};

// ---- Other workspace members (for connected accounts display, etc.) ----
const WORKSPACE_MEMBERS = [
    CURRENT_USER,
    {
        id: 2, name: 'Mei-Lin Chang', username: 'mei.chang',
        email: 'mei.chang@nextera.io', avatar: null, avatarColor: '#26B5CE',
        pronouns: 'she/her', timezone: 'Asia/Tokyo',
        profileVisibility: 'public',
        createdAt: '2023-04-12T10:00:00Z', lastActivityAt: '2026-02-17T09:00:00Z'
    },
    {
        id: 3, name: 'Tomás Herrera', username: 'tomas.herrera',
        email: 'tomas.herrera@nextera.io', avatar: null, avatarColor: '#F2994A',
        pronouns: 'he/him', timezone: 'America/Mexico_City',
        profileVisibility: 'public',
        createdAt: '2023-05-01T14:00:00Z', lastActivityAt: '2026-02-18T11:30:00Z'
    },
    {
        id: 4, name: 'Priya Patel', username: 'priya.patel',
        email: 'priya.patel@nextera.io', avatar: null, avatarColor: '#EB5757',
        pronouns: 'she/her', timezone: 'Asia/Kolkata',
        profileVisibility: 'internal',
        createdAt: '2023-06-15T08:00:00Z', lastActivityAt: '2026-02-16T16:00:00Z'
    },
    {
        id: 5, name: 'Alexei Volkov', username: 'alexei.volkov',
        email: 'alexei.volkov@nextera.io', avatar: null, avatarColor: '#6FCF97',
        pronouns: 'he/him', timezone: 'Europe/Berlin',
        profileVisibility: 'public',
        createdAt: '2023-07-20T12:00:00Z', lastActivityAt: '2026-02-18T08:45:00Z'
    },
    {
        id: 6, name: 'Amara Okafor', username: 'amara.okafor',
        email: 'amara.okafor@nextera.io', avatar: null, avatarColor: '#BB6BD9',
        pronouns: 'she/her', timezone: 'Africa/Lagos',
        profileVisibility: 'public',
        createdAt: '2023-09-03T09:00:00Z', lastActivityAt: '2026-02-17T19:00:00Z'
    },
    {
        id: 7, name: 'Liam O\'Brien', username: 'liam.obrien',
        email: 'liam.obrien@nextera.io', avatar: null, avatarColor: '#F2C94C',
        pronouns: 'he/him', timezone: 'Europe/Dublin',
        profileVisibility: 'public',
        createdAt: '2024-01-08T10:00:00Z', lastActivityAt: '2026-02-18T10:15:00Z'
    },
    {
        id: 8, name: 'Suki Nakamura', username: 'suki.nakamura',
        email: 'suki.nakamura@nextera.io', avatar: null, avatarColor: '#2D9CDB',
        pronouns: 'she/her', timezone: 'Asia/Tokyo',
        profileVisibility: 'private',
        createdAt: '2024-03-22T07:00:00Z', lastActivityAt: '2026-02-15T22:30:00Z'
    },
    {
        id: 9, name: 'Raj Kapoor', username: 'raj.kapoor',
        email: 'raj.kapoor@nextera.io', avatar: null, avatarColor: '#219653',
        pronouns: 'he/him', timezone: 'Asia/Kolkata',
        profileVisibility: 'public',
        createdAt: '2024-05-10T11:00:00Z', lastActivityAt: '2026-02-18T13:00:00Z'
    },
    {
        id: 10, name: 'Elena Vasquez', username: 'elena.vasquez',
        email: 'elena.vasquez@nextera.io', avatar: null, avatarColor: '#9B51E0',
        pronouns: 'she/her', timezone: 'America/Sao_Paulo',
        profileVisibility: 'public',
        createdAt: '2024-08-15T09:00:00Z', lastActivityAt: '2026-02-17T15:00:00Z'
    }
];

// ---- Preferences ----
const PREFERENCES = {
    // General
    defaultHomeView: 'active_issues',
    displayFullNames: true,
    firstDayOfWeek: 'monday',
    convertTextEmoticons: true,

    // Interface and theme
    fontSize: 'default',
    cursorPointer: false,
    theme: 'system',
    customThemeName: '',
    customThemeCSS: '',

    // Desktop application
    openLinearURLsInDesktopApp: true,
    notificationBadge: true,
    spellCheck: true,

    // Automations and workflows
    autoAssignOnCreate: false,
    autoAssignOnStarted: false,
    gitAttachmentFormat: 'title_only',
    gitBranchMoveToStarted: true,
    gitBranchAutoAssign: false
};

// ---- Notification Settings ----
const NOTIFICATION_CHANNELS = {
    desktop: {
        id: 'desktop',
        name: 'Desktop',
        enabled: true,
        description: 'Receive notifications via the Linear desktop app'
    },
    mobile: {
        id: 'mobile',
        name: 'Mobile',
        enabled: true,
        description: 'Receive push notifications on your mobile device'
    },
    email: {
        id: 'email',
        name: 'Email',
        enabled: true,
        description: 'Receive email digest notifications'
    },
    slack: {
        id: 'slack',
        name: 'Slack',
        enabled: true,
        description: 'Receive notifications via Slack'
    }
};

// Notification groups (each group has multiple notification types bundled together)
const NOTIFICATION_GROUPS = [
    {
        id: 'issue_status',
        name: 'Issue status changes',
        description: 'Completions, cancellations, priority changes, and blocking relationships',
        channels: {
            desktop: true,
            mobile: false,
            email: true,
            slack: true
        }
    },
    {
        id: 'issue_assignment',
        name: 'Issue assignments',
        description: 'When issues are assigned or unassigned to you',
        channels: {
            desktop: true,
            mobile: false,
            email: true,
            slack: true
        }
    },
    {
        id: 'comments',
        name: 'Comments and mentions',
        description: 'New comments on subscribed issues and @mentions',
        channels: {
            desktop: true,
            mobile: false,
            email: true,
            slack: true
        }
    },
    {
        id: 'project_updates',
        name: 'Project updates',
        description: 'Project status changes, milestones, and progress updates',
        channels: {
            desktop: true,
            mobile: false,
            email: false,
            slack: true
        }
    },
    {
        id: 'cycle_updates',
        name: 'Cycle updates',
        description: 'Cycle starts, ends, and progress summaries',
        channels: {
            desktop: false,
            mobile: false,
            email: true,
            slack: false
        }
    },
    {
        id: 'sla_breaches',
        name: 'SLA breaches',
        description: 'When issues breach their SLA targets',
        channels: {
            desktop: true,
            mobile: false,
            email: true,
            slack: true
        }
    },
    {
        id: 'team_activity',
        name: 'Team activity',
        description: 'New members joining, team configuration changes',
        channels: {
            desktop: false,
            mobile: false,
            email: false,
            slack: false
        }
    }
];

// Email digest settings
const EMAIL_DIGEST_SETTINGS = {
    sendImmediatelyOnUrgent: true,
    sendImmediatelyOnSLABreach: false,
    delayLowPriorityToWorkHours: true
};

// Communication preferences
const COMMUNICATION_PREFERENCES = {
    changelog: true,
    dpaUpdates: true,
    productUpdates: false,
    tips: true
};

// ---- Sessions ----
const SESSIONS = [
    {
        id: 'sess-a1b2c3d4',
        deviceName: 'MacBook Pro 16"',
        sourceType: 'Desktop App',
        location: 'New York, NY, US',
        ipAddress: '203.45.167.89',
        signedInAt: '2026-01-05T09:12:00Z',
        lastSeenAt: '2026-02-18T14:22:00Z',
        isCurrent: true,
        browser: 'Linear Desktop 2.4.1',
        os: 'macOS Sequoia 15.3'
    },
    {
        id: 'sess-e5f6g7h8',
        deviceName: 'Chrome on Windows',
        sourceType: 'Web Browser',
        location: 'New York, NY, US',
        ipAddress: '203.45.167.90',
        signedInAt: '2026-02-10T11:30:00Z',
        lastSeenAt: '2026-02-17T16:45:00Z',
        isCurrent: false,
        browser: 'Chrome 122.0',
        os: 'Windows 11'
    },
    {
        id: 'sess-i9j0k1l2',
        deviceName: 'iPhone 15 Pro',
        sourceType: 'Mobile App',
        location: 'Newark, NJ, US',
        ipAddress: '198.51.100.42',
        signedInAt: '2025-12-20T08:00:00Z',
        lastSeenAt: '2026-02-16T07:30:00Z',
        isCurrent: false,
        browser: 'Linear iOS 3.1.2',
        os: 'iOS 18.2'
    },
    {
        id: 'sess-m3n4o5p6',
        deviceName: 'Safari on MacBook Air',
        sourceType: 'Web Browser',
        location: 'Brooklyn, NY, US',
        ipAddress: '172.16.254.1',
        signedInAt: '2026-01-28T14:20:00Z',
        lastSeenAt: '2026-02-12T09:10:00Z',
        isCurrent: false,
        browser: 'Safari 18.3',
        os: 'macOS Sequoia 15.3'
    },
    {
        id: 'sess-q7r8s9t0',
        deviceName: 'Firefox on Ubuntu',
        sourceType: 'Web Browser',
        location: 'San Francisco, CA, US',
        ipAddress: '10.0.0.15',
        signedInAt: '2026-01-15T10:00:00Z',
        lastSeenAt: '2026-01-22T18:30:00Z',
        isCurrent: false,
        browser: 'Firefox 134.0',
        os: 'Ubuntu 24.04'
    },
    {
        id: 'sess-u1v2w3x4',
        deviceName: 'iPad Pro 12.9"',
        sourceType: 'Mobile App',
        location: 'New York, NY, US',
        ipAddress: '203.45.167.91',
        signedInAt: '2025-11-05T09:00:00Z',
        lastSeenAt: '2025-12-28T13:45:00Z',
        isCurrent: false,
        browser: 'Linear iPadOS 3.0.8',
        os: 'iPadOS 18.1'
    },
    {
        id: 'sess-y5z6a7b8',
        deviceName: 'linear-cli',
        sourceType: 'CLI',
        location: 'New York, NY, US',
        ipAddress: '203.45.167.89',
        signedInAt: '2026-02-01T16:00:00Z',
        lastSeenAt: '2026-02-14T11:20:00Z',
        isCurrent: false,
        browser: 'linear-cli 1.2.0',
        os: 'macOS Sequoia 15.3'
    }
];

// ---- Passkeys ----
const PASSKEYS = [
    {
        id: 'pk-1a2b3c',
        name: 'MacBook Pro Touch ID',
        createdAt: '2025-06-15T10:00:00Z',
        lastUsedAt: '2026-02-18T09:00:00Z',
        deviceType: 'platform'
    },
    {
        id: 'pk-4d5e6f',
        name: '1Password',
        createdAt: '2025-09-20T14:30:00Z',
        lastUsedAt: '2026-02-10T11:30:00Z',
        deviceType: 'cross-platform'
    }
];

// ---- Personal API Keys ----
const API_KEYS = [
    {
        id: 'key-x1y2z3',
        label: 'CI/CD Pipeline',
        prefix: 'lin_api_x1y2...z3',
        createdAt: '2025-03-10T09:00:00Z',
        lastUsedAt: '2026-02-18T06:00:00Z'
    },
    {
        id: 'key-a4b5c6',
        label: 'Personal Automation',
        prefix: 'lin_api_a4b5...c6',
        createdAt: '2025-08-22T15:00:00Z',
        lastUsedAt: '2026-02-15T22:00:00Z'
    },
    {
        id: 'key-d7e8f9',
        label: 'Monitoring Dashboard',
        prefix: 'lin_api_d7e8...f9',
        createdAt: '2025-11-05T11:00:00Z',
        lastUsedAt: '2026-01-30T14:00:00Z'
    }
];

// ---- Authorized OAuth Applications ----
const AUTHORIZED_APPS = [
    {
        id: 'app-gh01',
        name: 'GitHub',
        icon: 'github',
        description: 'Source code integration for pull requests and branches',
        permissions: ['read:issues', 'write:issues', 'read:pull_requests', 'write:webhooks'],
        authorizedAt: '2023-04-15T10:00:00Z',
        lastUsedAt: '2026-02-18T14:00:00Z'
    },
    {
        id: 'app-sl02',
        name: 'Slack',
        icon: 'slack',
        description: 'Team communication and notification integration',
        permissions: ['read:messages', 'write:messages', 'read:channels'],
        authorizedAt: '2023-04-15T10:30:00Z',
        lastUsedAt: '2026-02-18T12:00:00Z'
    },
    {
        id: 'app-fg03',
        name: 'Figma',
        icon: 'figma',
        description: 'Design file linking and preview integration',
        permissions: ['read:files', 'read:comments'],
        authorizedAt: '2023-06-20T14:00:00Z',
        lastUsedAt: '2026-02-14T09:00:00Z'
    },
    {
        id: 'app-sn04',
        name: 'Sentry',
        icon: 'sentry',
        description: 'Error tracking and issue auto-creation',
        permissions: ['read:issues', 'write:issues', 'read:projects'],
        authorizedAt: '2024-01-10T11:00:00Z',
        lastUsedAt: '2026-02-18T07:00:00Z'
    },
    {
        id: 'app-zd05',
        name: 'Zendesk',
        icon: 'zendesk',
        description: 'Customer support ticket integration',
        permissions: ['read:tickets', 'write:tickets'],
        authorizedAt: '2024-09-05T09:00:00Z',
        lastUsedAt: '2026-02-11T16:00:00Z'
    },
    {
        id: 'app-nt06',
        name: 'Notion',
        icon: 'notion',
        description: 'Document and wiki linking',
        permissions: ['read:pages', 'read:databases'],
        authorizedAt: '2025-02-14T13:00:00Z',
        lastUsedAt: '2026-01-25T10:00:00Z'
    }
];

// ---- Connected Accounts (user-level integrations) ----
const CONNECTED_ACCOUNTS = [
    {
        id: 'conn-gh01',
        provider: 'GitHub',
        username: 'jordanrivera',
        email: 'jordan@github.com',
        connectedAt: '2023-04-15T10:00:00Z',
        status: 'active'
    },
    {
        id: 'conn-gl02',
        provider: 'GitLab',
        username: 'jordan.rivera',
        email: 'jordan.rivera@gitlab.com',
        connectedAt: '2023-05-20T09:00:00Z',
        status: 'active'
    },
    {
        id: 'conn-sl03',
        provider: 'Slack',
        username: 'jordan.rivera',
        email: 'jordan.rivera@nextera.io',
        connectedAt: '2023-04-15T10:30:00Z',
        status: 'active'
    },
    {
        id: 'conn-fg04',
        provider: 'Figma',
        username: 'jordan.rivera',
        email: 'jordan.rivera@nextera.io',
        connectedAt: '2023-06-20T14:00:00Z',
        status: 'active'
    },
    {
        id: 'conn-ggl05',
        provider: 'Google',
        username: 'jordan.rivera',
        email: 'jordan.rivera@gmail.com',
        connectedAt: '2024-02-10T11:00:00Z',
        status: 'active'
    }
];

// ---- Issue Subscriptions (for notifications demo) ----
const ISSUE_SUBSCRIPTIONS = [
    {
        id: 'sub-001',
        issueId: 'NEX-1042',
        issueTitle: 'Migrate authentication to OAuth 2.0',
        teamName: 'Backend',
        reason: 'assigned',
        subscribedAt: '2026-02-10T09:00:00Z'
    },
    {
        id: 'sub-002',
        issueId: 'NEX-987',
        issueTitle: 'Fix dashboard performance regression',
        teamName: 'Frontend',
        reason: 'created',
        subscribedAt: '2026-02-05T14:00:00Z'
    },
    {
        id: 'sub-003',
        issueId: 'NEX-1105',
        issueTitle: 'Add dark mode support for mobile app',
        teamName: 'Mobile',
        reason: 'mentioned',
        subscribedAt: '2026-02-15T11:00:00Z'
    },
    {
        id: 'sub-004',
        issueId: 'NEX-1089',
        issueTitle: 'Update API rate limiting implementation',
        teamName: 'Platform',
        reason: 'manual',
        subscribedAt: '2026-02-12T16:00:00Z'
    },
    {
        id: 'sub-005',
        issueId: 'NEX-1120',
        issueTitle: 'Design new onboarding flow',
        teamName: 'Design',
        reason: 'mentioned',
        subscribedAt: '2026-02-17T10:00:00Z'
    },
    {
        id: 'sub-006',
        issueId: 'NEX-856',
        issueTitle: 'Refactor notification service architecture',
        teamName: 'Backend',
        reason: 'created',
        subscribedAt: '2026-01-20T08:00:00Z'
    },
    {
        id: 'sub-007',
        issueId: 'NEX-1134',
        issueTitle: 'Implement webhook retry logic',
        teamName: 'Platform',
        reason: 'assigned',
        subscribedAt: '2026-02-18T09:00:00Z'
    },
    {
        id: 'sub-008',
        issueId: 'NEX-1098',
        issueTitle: 'Customer data export compliance',
        teamName: 'Security',
        reason: 'manual',
        subscribedAt: '2026-02-13T14:00:00Z'
    }
];

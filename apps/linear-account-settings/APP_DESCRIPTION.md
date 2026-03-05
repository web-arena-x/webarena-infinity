# Linear Account Settings

## Summary

A faithful replica of Linear's Account Settings pages, covering Profile, Preferences, Notifications, and Security & Access. The app uses hash-based routing (`#/profile`, `#/preferences`, `#/notifications`, `#/security`) to navigate between four settings sections. Users can edit their profile information, configure workspace preferences, manage notification channels, and control security credentials. All state is persisted to localStorage and synced to the server via PUT /api/state on every mutation.

## Main Sections / Pages

### 1. Profile (`#/profile`)
- **Avatar display** with initials and color; edit button (demo-only, shows toast).
- **Personal information**: Full name, username, email address — each editable inline with pencil icon hover reveal, inline text input, Save/Cancel buttons.
- **Connected accounts**: List of 5 connected services (Google, GitHub, GitLab, Slack, Figma) each with provider icon, account identifier, connection date, and a Disconnect button (appears on hover, confirmation dialog).
- **Workspaces**: List of joined workspaces showing name, plan, member count, user role, and a "Leave workspace" button for non-owner workspaces (confirmation dialog).

### 2. Preferences (`#/preferences`)
- **General**:
  - Default home view — custom dropdown with 7 options (All issues, Active issues, Current cycle, Inbox, My Issues, Favorited Views, Favorited Projects)
  - Display full names — toggle switch
  - First day of the week — custom dropdown with 4 options (Sunday, Monday, Tuesday, Saturday)
  - Convert text emoticons into emojis — toggle switch
- **Interface and theme**:
  - Theme — radio group with 3 options (Light, Dark, System)
  - Font size — custom dropdown with 3 options (Small, Default, Large)
  - Use pointer cursor — toggle switch
- **Desktop application**:
  - Open Linear URLs in desktop app — toggle switch
  - Show notification badge — toggle switch
  - Enable spell check — toggle switch
- **Automations and workflows**:
  - Auto-assign issues you create to yourself — toggle switch
  - Auto-assign issues on started status — toggle switch
  - Git attachment format — custom dropdown with 2 options (Title only, Title and repository)
  - On git branch copy, move issue to started status — toggle switch
  - On git branch copy, auto-assign to yourself — toggle switch

### 3. Notifications (`#/notifications`)
- **Notification channels**: 4 channels (Desktop, Mobile, Email, Slack) each shown as an expandable card with:
  - Green/gray status dot indicating enabled/disabled
  - Channel name and description
  - Click to expand/collapse detail panel
  - Master enable/disable toggle per channel
  - 7 individual notification type toggles per channel:
    - Issue assigned to you
    - Status changes on subscribed issues
    - New comments on subscribed issues
    - Mentioned in an issue or comment
    - Project updates
    - Cycle updates
    - SLA breach warnings
  - Disabling a channel disables all its individual settings; enabling an individual setting auto-enables the channel
- **Email digest delivery**:
  - Send immediately for urgent issues — toggle switch
  - Delay low priority outside work hours — toggle switch
- **Communication preferences**: 5 toggles controlling communications from Linear:
  - Changelogs
  - DPA updates
  - Product announcements
  - Tips and tutorials
  - Community updates

### 4. Security & Access (`#/security`)
- **Sessions**: List of 8 sessions showing device name, browser, location, time ago. Current session has a "Current" badge. Non-current sessions show "Revoke access" on hover. Click session row to expand details (IP address, OS, source type, sign-in date, last seen). "Revoke all" button removes all non-current sessions.
- **Passkeys**: List of 2 passkeys with name, creation date, last used. "Add passkey" button opens a modal with name input. Each passkey has rename (pencil) and remove (trash) icon buttons appearing on hover. Remove shows confirmation dialog.
- **Personal API keys**: List of 5 API keys with label, masked prefix, creation date, last used, and optional expiration info (with warning/danger colors for near-expiry/expired). "Create key" button opens modal. Each key has "Revoke" button.
- **Authorized applications**: List of 8 OAuth apps with name, description, permission badges, authorization date, last used. Each has "Revoke access" button with confirmation dialog.

## Data Model

### CurrentUser
| Field | Type | Example |
|-------|------|---------|
| id | string | `usr_10001` |
| fullName | string | `Alexandra Chen` |
| username | string | `alexchen` |
| email | string | `alexandra.chen@acmetech.io` |
| avatarUrl | string\|null | `null` |
| avatarColor | string | `#5E6AD2` |
| timezone | string | `America/Los_Angeles` |
| role | string | `Admin` |
| createdAt | ISO string | `2024-03-15T09:00:00Z` |
| updatedAt | ISO string | `2026-02-28T14:30:00Z` |

### Workspace
| Field | Type | Example |
|-------|------|---------|
| id | string | `ws_001` |
| name | string | `Acme Tech` |
| slug | string | `acme-tech` |
| logoColor | string | `#5E6AD2` |
| memberCount | number | `47` |
| plan | string | `Business` |
| createdAt | ISO string | |
| currentUserRole | string | `Admin` |

### ConnectedAccount
| Field | Type | Example |
|-------|------|---------|
| id | string | `conn_001` |
| provider | string | `Google` |
| providerIcon | string | `google` |
| accountEmail | string | `alexandra.chen@gmail.com` |
| connectedAt | ISO string | |
| status | string | `active` |

### Preferences (nested object)
- `general.defaultHomeView` — string (one of HOME_VIEW_OPTIONS)
- `general.displayFullNames` — boolean
- `general.firstDayOfWeek` — string (one of FIRST_DAY_OPTIONS)
- `general.convertEmoticonToEmoji` — boolean
- `interfaceAndTheme.theme` — string (`light`, `dark`, `system`)
- `interfaceAndTheme.fontSize` — string (`small`, `default`, `large`)
- `interfaceAndTheme.usePointerCursor` — boolean
- `interfaceAndTheme.customTheme` — null
- `desktopApp.openLinksInDesktopApp` — boolean
- `desktopApp.showNotificationBadge` — boolean
- `desktopApp.enableSpellCheck` — boolean
- `automationsAndWorkflows.autoAssignOnCreate` — boolean
- `automationsAndWorkflows.autoAssignOnStarted` — boolean
- `automationsAndWorkflows.gitAttachmentFormat` — string
- `automationsAndWorkflows.onGitBranchCopyMoveToStarted` — boolean
- `automationsAndWorkflows.onGitBranchCopyAutoAssign` — boolean

### NotificationChannel
| Field | Type | Example |
|-------|------|---------|
| id | string | `notif_desktop` |
| name | string | `Desktop` |
| icon | string | `desktop` |
| enabled | boolean | `true` |
| description | string | |
| settings | array of NotificationSetting | |

### NotificationSetting
| Field | Type | Example |
|-------|------|---------|
| id | string | `desktop_issue_assigned` |
| label | string | `Issue assigned to you` |
| enabled | boolean | `true` |

### EmailDigestPreferences
| Field | Type | Example |
|-------|------|---------|
| sendImmediatelyOnUrgent | boolean | `true` |
| delayLowPriorityOutsideWorkHours | boolean | `true` |
| workHoursStart | string | `08:00` |
| workHoursEnd | string | `18:00` |

### CommunicationPreferences
| Field | Type | Example |
|-------|------|---------|
| changelog | boolean | `true` |
| dpaUpdates | boolean | `true` |
| productAnnouncements | boolean | `true` |
| tipsAndTutorials | boolean | `false` |
| communityUpdates | boolean | `false` |

### Session
| Field | Type | Example |
|-------|------|---------|
| id | string | `sess_001` |
| deviceName | string | `MacBook Pro 16"` |
| browser | string | `Chrome 122` |
| os | string | `macOS Sonoma` |
| location | string | `San Francisco, CA` |
| ipAddress | string | `198.51.100.42` |
| lastSeen | ISO string | |
| signedInAt | ISO string | |
| isCurrent | boolean | `true` |
| sourceType | string | `Desktop` |

### Passkey
| Field | Type | Example |
|-------|------|---------|
| id | string | `pk_001` |
| name | string | `MacBook Pro Touch ID` |
| createdAt | ISO string | |
| lastUsedAt | ISO string\|null | |
| deviceType | string | `platform` |

### ApiKey
| Field | Type | Example |
|-------|------|---------|
| id | string | `apikey_001` |
| label | string | `CI/CD Pipeline` |
| prefix | string | `lin_api_a3f8` |
| createdAt | ISO string | |
| lastUsedAt | ISO string\|null | |
| expiresAt | ISO string\|null | |

### AuthorizedApp
| Field | Type | Example |
|-------|------|---------|
| id | string | `oauth_001` |
| name | string | `Raycast` |
| icon | string | `raycast` |
| description | string | `Quick launcher integration` |
| permissions | string[] | `['read:issues', 'write:issues']` |
| authorizedAt | ISO string | |
| lastUsedAt | ISO string | |

## Navigation Structure

The app uses hash-based routing with a sidebar navigation:

```
Settings > Account
├── Profile        (#/profile)     — default view
├── Preferences    (#/preferences)
├── Notifications  (#/notifications)
└── Security & Access (#/security)
```

Clicking a sidebar item navigates to that section. The current section is highlighted in the sidebar with a purple background. Workspace info is shown at the bottom of the sidebar.

## Form Controls and Their Options

### Custom Dropdowns
| ID | Options |
|----|---------|
| `homeView` | All issues, Active issues, Current cycle, Inbox, My Issues, Favorited Views, Favorited Projects |
| `firstDayOfWeek` | Sunday, Monday, Tuesday, Saturday |
| `fontSize` | Small, Default, Large |
| `gitAttachmentFormat` | Title only, Title and repository |

### Toggle Switches (all boolean on/off)
- Profile: none
- Preferences: `displayFullNames`, `convertEmoticonToEmoji`, `usePointerCursor`, `openLinksInDesktopApp`, `showNotificationBadge`, `enableSpellCheck`, `autoAssignOnCreate`, `autoAssignOnStarted`, `onGitBranchCopyMoveToStarted`, `onGitBranchCopyAutoAssign`
- Notifications: per-channel master toggle (`channel-enable-{channelId}`), 28 individual notification settings (7 per channel x 4 channels), `sendImmediatelyOnUrgent`, `delayLowPriorityOutsideWorkHours`, 5 communication toggles
- Security: none

### Radio Groups
| Name | Options |
|------|---------|
| `theme` | Light, Dark, System |

### Inline Edit Fields (Profile page)
- Full name (`edit-fullName`)
- Username (`edit-username`)
- Email address (`edit-email`)

## Seed Data Summary

### Current User
- **Alexandra Chen** (`alexchen`), email: `alexandra.chen@acmetech.io`, role: Admin, avatar color: `#5E6AD2`

### Workspaces (2)
1. **Acme Tech** — Business plan, 47 members, user is Admin
2. **Side Project Labs** — Free plan, 5 members, user is Member

### Connected Accounts (5)
1. **Google** — `alexandra.chen@gmail.com`
2. **GitHub** — `alexchen`
3. **GitLab** — `alexandra.chen`
4. **Slack** — `alexandra.chen@acmetech.io`
5. **Figma** — `alexandra.chen@acmetech.io`

### Preferences (seed defaults)
- Default home view: Active issues
- Display full names: ON
- First day of week: Monday
- Convert emoticons: ON
- Theme: System
- Font size: Default
- Pointer cursor: OFF
- Open in desktop app: ON
- Notification badge: ON
- Spell check: ON
- Auto-assign on create: OFF
- Auto-assign on started: OFF
- Git attachment format: Title only
- Git branch copy → started: ON
- Git branch copy → auto-assign: ON

### Notification Channels (4)
1. **Desktop** — enabled, 5/7 settings ON (project updates and cycle updates OFF)
2. **Mobile** — enabled, 4/7 settings ON (status changes, project updates, cycle updates OFF)
3. **Email** — enabled, 6/7 settings ON (cycle updates OFF)
4. **Slack** — disabled, all settings OFF

### Email Digest
- Send immediately on urgent: ON
- Delay low priority outside work hours: ON

### Communication Preferences
- Changelogs: ON, DPA updates: ON, Product announcements: ON, Tips & tutorials: OFF, Community updates: OFF

### Sessions (8)
1. **MacBook Pro 16"** (Current) — Chrome 122, macOS Sonoma, San Francisco, CA
2. **iPhone 15 Pro** — Linear iOS, iOS 18.3, San Francisco, CA
3. **Windows Desktop** — Firefox 134, Windows 11, New York, NY
4. **iPad Air** — Safari 18, iPadOS 18.3, San Francisco, CA
5. **Linux Workstation** — Chrome 121, Ubuntu 24.04, Austin, TX
6. **Pixel 8** — Linear Android, Android 15, Chicago, IL
7. **MacBook Air M3** — Safari 18, macOS Sonoma, Portland, OR
8. **Windows Laptop** — Edge 122, Windows 11, Seattle, WA

### Passkeys (2)
1. **MacBook Pro Touch ID** — platform, created 2025-04-10
2. **YubiKey 5C NFC** — cross-platform, created 2025-06-22

### Personal API Keys (5)
1. **CI/CD Pipeline** (`lin_api_a3f8`) — no expiry, last used today
2. **Slack Bot Integration** (`lin_api_7b2c`) — expires 2026-06-05
3. **Personal Scripts** (`lin_api_e9d1`) — no expiry
4. **Metrics Dashboard** (`lin_api_4f6a`) — expires 2026-05-01
5. **Staging Environment** (`lin_api_1c8e`) — no expiry, never used

### Authorized OAuth Applications (8)
1. **Raycast** — read:issues, write:issues, read:projects
2. **Zapier** — read:issues, write:issues, read:projects, write:projects, read:teams
3. **Notion** — read:issues, read:projects
4. **Sentry** — read:issues, write:issues, read:teams
5. **Intercom** — read:issues, write:issues
6. **Loom** — read:issues
7. **Retool** — read:issues, read:projects, read:teams, read:cycles
8. **Statuspage** — read:issues, write:issues

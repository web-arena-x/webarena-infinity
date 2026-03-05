# Superhuman Mail — App Description

## Summary

A faithful functional replica of the Superhuman email client — a premium, keyboard-first email application built around the philosophy of Inbox Zero. The app features a dark-themed three-pane layout (sidebar, main content, calendar sidebar), split inbox for prioritized triage, full email management (compose, reply, forward, archive, remind), AI-powered features (auto labels, auto drafts, auto reminders), snippets (reusable templates), calendar integration, read status tracking, and a command palette for rapid navigation.

## Main Sections / Pages

1. **Inbox** — Split into focused sections (Important, Other, Calendar, Newsletters) with email triage
2. **Email Detail** — Full conversation view with reply/forward/action toolbar
3. **Composer** — New email, reply, reply-all, forward with To/Cc/Bcc/Subject/Body
4. **Done (Archive)** — Archived emails, fully searchable
5. **Reminders** — Emails with manual or auto reminders set
6. **Sent** — Sent emails with read status tracking
7. **Drafts** — Saved drafts
8. **Scheduled** — Emails scheduled for later sending
9. **Trash** — Deleted emails
10. **Spam** — Spam-filtered emails
11. **Labels** — User-created label views (clicking a label shows all emails with that label)
12. **Search** — Full-text and operator-based search across all emails
13. **Settings** — 12 configuration sub-panels (see below)
14. **Calendar Sidebar** — Today's events in the right sidebar
15. **Command Palette** — Quick-access command search (Cmd+K / Ctrl+K)

## Implemented Features and UI Interactions

### Email Management
- **View emails** in list format with sender, subject, snippet preview, date, and indicators
- **Open email detail** to read full message body, thread messages, and attachments
- **Mark Done (E key)** — Archives email to Done folder
- **Set Reminder (H key)** — Opens reminder picker with preset times (Later today, Tomorrow, Next week) or custom date/time
- **Move to Folder (V key)** — Opens folder picker (Inbox, Done, Trash, Spam)
- **Star / Unstar (S key)** — Toggle star on email
- **Mark Read / Unread (U key)** — Toggle read status
- **Trash (# key)** — Move to trash
- **Delete permanently** — Remove email entirely
- **Label emails** — Apply/remove user-created labels via label picker
- **Unsubscribe (Ctrl+U)** — Block sender and archive/trash all their emails
- **Get Me To Zero** — Bulk archive entire inbox with options to preserve unread/starred

### Split Inbox
- **Tab / Shift+Tab** to cycle through splits
- **Important** split — Person-to-person messages (split type = "important")
- **Other** split — Automated messages and mailing lists (split type = "other")
- **Calendar** split — Calendar invites and scheduling emails (split type = "calendar")
- **Newsletters** split — Auto-labeled newsletter emails
- Each split shows total email count

### Email Composition
- **Compose new email (C key)** — Opens composer overlay
- **Reply (R key)** — Reply to sender
- **Reply All (Shift+R)** — Reply to all recipients
- **Forward (F key)** — Forward with original message quoted
- **To, Cc, Bcc fields** — Cc/Bcc hidden by default, toggle to show
- **Subject line**
- **Rich text body** (contenteditable)
- **Insert Snippet** — Insert reusable template into body
- **Schedule Send** — Schedule email for later delivery
- **Discard draft** — Delete without saving
- **Auto-save drafts** — Closing composer with content saves as draft
- **Undo Send** — Toast with undo button after sending (configurable delay: 5/10/20/30s)

### Search
- **Full-text search** across subject, from, snippet, body
- **Operator-based search:**
  - `from:` — Search by sender name or email
  - `to:` — Search by recipient
  - `subject:` — Search by subject line
  - `has:attachment` — Emails with attachments
  - `is:unread` — Unread emails only
  - `is:starred` — Starred emails only
  - `label:` — Emails with specific label
  - `in:` — Emails in specific folder
- Search tips displayed when no query entered

### Command Palette (Cmd+K / Ctrl+K)
- Type-ahead fuzzy search across 30+ commands
- **Navigation commands:** Go to Inbox, Done, Reminders, Sent, Drafts, Trash, Spam, Snippets, Settings, any Label
- **Action commands:** Compose, Mark Done, Remind Me, Reply, Reply All, Forward, Move, Star, Mark Unread, Trash, Unsubscribe, Get Me To Zero, Create Snippet, Create Event
- **Settings commands:** Read Statuses, Split Inbox Library, Auto Label Library, Calendar Settings, Reminder Settings
- Keyboard shortcut hints shown next to each command
- Arrow key navigation, Enter to select

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| C | Compose new email |
| E | Mark Done (archive) |
| J | Next email in list |
| K | Previous email in list |
| R | Reply |
| Shift+R | Reply All |
| F | Forward |
| H | Set Reminder |
| V | Move to folder |
| S | Star / Unstar |
| U | Mark Unread |
| # | Trash |
| / | Search |
| Tab | Next split |
| Shift+Tab | Previous split |
| Escape | Close composer/palette/go back |
| Cmd+K | Command palette |
| Ctrl+U | Unsubscribe |

### Reminders
- **Manual reminders** — Set via H key or reminder picker
- Preset options: Later today, Tomorrow (9am), Next week (Mon 9am)
- Custom date and time picker
- **Auto reminders** — Configurable to track all follow-ups, external only, or off
- Configurable auto reminder delay (1-7 days)
- Emails with reminders shown in Reminders folder

### Snippets (Templates)
- **Create snippet** — Name, body content, optional placeholders
- **Edit snippet** — Update name, body, sharing status
- **Delete snippet**
- **Share with team** — Toggle snippet visibility to team
- **Insert snippet into composer** — Variable replacement ({recipientFirstName}, {senderName}, {senderFirstName})
- **Snippet metrics** — Sends count, open rate, response rate displayed
- Personal vs Team snippets separated in settings

### Calendar
- **Today's events** in right sidebar
- Events color-coded by calendar (Work = blue, Personal = green)
- Event details: time, title, location, meeting link
- **Create event** — Title, date, start/end time, location, description
- **View event details** — Modal with attendees, status, description
- **Delete event**
- Configurable calendars (enable/disable)

### Read Statuses
- **Sent email tracking** — Check marks indicate sent (✓) vs opened (✓✓)
- Hover shows open timestamp, device, location
- **Recent Opens feed** — Real-time list of email opens
- **Team read statuses** — Shared across team
- **Team reply indicators** — See when teammate is drafting

### Labels
- **System labels** — Inbox, Done, Drafts, Sent, Trash, Spam, Reminders, Scheduled
- **User-created labels** — Custom name and color
- **Create label** — Modal with name + color picker (10 color options)
- **Edit label** — Change name and color
- **Delete label** — Removes label from all emails
- **Apply/remove labels** on emails via label picker
- **Navigate to label** — View all emails with that label
- Labels displayed in sidebar with color dots

### Auto Labels (AI-Powered)
- **Newsletters** — Newsletter emails
- **Receipts** — Purchase receipts and invoices
- **Travel** — Flight/hotel/travel confirmations
- **Social** — Social media notifications
- **Updates** — Automated service updates
- **Finance** — Banking and financial notifications
- Each can be enabled/disabled independently

### Auto Archive
- Toggle on/off
- Select which auto labels to auto-archive (skip inbox)

### Settings (12 Sub-panels)

**1. General**
- Theme: Dark / Light / Auto (dropdown)
- Display density: Compact / Comfortable / Spacious (dropdown)
- Keyboard shortcuts: toggle
- Desktop notifications: toggle
- Sound notifications: toggle
- Auto-advance: toggle
- Undo send delay: 5s / 10s / 20s / 30s (dropdown)
- Default reply action: Reply / Reply All (dropdown)

**2. Split Inbox**
- Enable/disable split inbox: toggle
- View active splits with remove button for custom splits

**3. Labels**
- List all user labels with color swatches
- Create, edit, delete labels

**4. Auto Labels**
- Toggle each auto label on/off
- Descriptions for each auto label

**5. Reminders**
- Default reminder time: 8am/9am/10am/12pm/2pm/5pm (dropdown)
- Auto reminders: All follow-ups / External only / Off (radio group)
- Auto reminder delay: 1/2/3/5/7 days (dropdown)

**6. Read Statuses**
- Enable read statuses: toggle
- Team read statuses: toggle
- Team reply indicators: toggle
- Recent Opens feed: toggle

**7. Auto Drafts**
- Follow-up drafts: toggle
- Scheduling drafts: toggle

**8. Calendar**
- Default view: Day / Week (dropdown)
- Week starts on: Sunday / Monday (dropdown)
- Show weekends: toggle
- Default meeting duration: 15/30/45/60 min (dropdown)
- Meeting link provider: Google Meet / Zoom / None (dropdown)
- Event notifications: None / 5/10/15/30 min (dropdown)
- Calendars list: Work / Personal with enable/disable toggles

**9. Snippets**
- List personal and team snippets
- Create, edit, delete, share snippets
- View metrics (sends, open rate, response rate)

**10. Auto Archive**
- Enable/disable auto archive
- Select auto labels for auto-archiving

**11. Signatures**
- Rich text signature editor (contenteditable)
- Save button

**12. Blocked Senders**
- List blocked senders with block date
- Unblock button for each

## Data Model

### Entities

**Email** (125 total)
- `id`: string (email_001 to email_125)
- `threadId`: string (groups conversation messages)
- `subject`: string
- `from`: { name, email }
- `to`: [{ name, email }]
- `cc`: [{ name, email }]
- `bcc`: [{ name, email }]
- `body`: string (HTML)
- `snippet`: string (plain text preview, first ~100 chars)
- `date`: ISO datetime string
- `isRead`: boolean
- `isStarred`: boolean
- `folder`: string (inbox, done, sent, drafts, trash, spam, scheduled)
- `split`: string (important, other, calendar)
- `labels`: [string] (label IDs)
- `autoLabels`: [string] (auto label IDs)
- `hasAttachments`: boolean
- `attachments`: [{ name, size, type }]
- `readStatus`: { enabled: bool, opens: [{ timestamp, device, location }] }
- `reminder`: null | { date: ISO string, type: 'manual' | 'auto' }
- `isDraft`: boolean
- `isScheduled`: boolean
- `scheduledTime`: null | ISO string
- `threadMessages`: [message objects] (inline thread messages)

**Contact** (28 total)
- `id`: string (c_001 to c_028)
- `name`: string
- `email`: string
- `company`: string
- `avatar`: null
- `initials`: string (2 chars)
- `isTeammate`: boolean

**Label** (18 total: 8 system + 10 user)
- `id`: string (label_1 to label_10 for user labels)
- `name`: string
- `color`: { background, text }
- `isSystem`: boolean
- `isAutoLabel`: boolean

**Auto Label** (6 total)
- `id`: string (autolabel_newsletters, etc.)
- `name`: string
- `description`: string
- `isEnabled`: boolean
- `criteria`: { from: [], subject: [], aiPrompt: string }

**Split** (4 total)
- `id`: string (split_important, split_other, split_calendar, split_newsletters)
- `name`: string
- `icon`: string (emoji)
- `isDefault`: boolean
- `criteria`: { type: string } or { autoLabels: [string] }
- `order`: number

**Folder** (8 total)
- `id`: string (inbox, done, reminders, sent, drafts, scheduled, trash, spam)
- `name`: string
- `icon`: string
- `count`: number (computed)

**Snippet** (9 total)
- `id`: string (snippet_01 to snippet_09)
- `name`: string
- `body`: string (HTML)
- `variables`: [string]
- `placeholders`: [string]
- `isShared`: boolean
- `author`: string
- `metrics`: { sends: number, openRate: number, responseRate: number }
- `createdAt`: ISO datetime
- `updatedAt`: ISO datetime

**Calendar Event** (16 total)
- `id`: string (event_01 to event_16)
- `title`: string
- `start`: ISO datetime
- `end`: ISO datetime
- `location`: string
- `description`: string
- `attendees`: [{ name, email, status: 'accepted'|'declined'|'tentative'|'pending' }]
- `meetingLink`: string
- `calendar`: string ('Work' or 'Personal')
- `color`: string (hex)
- `isAllDay`: boolean
- `recurrence`: null | string

**Settings** (nested object)
- `general`: { theme, density, language, timezone, keyboardShortcuts, desktopNotifications, soundNotifications, autoAdvance, undoSendDelay, defaultReplyAction }
- `splitInbox`: { enabled, splits[] }
- `reminders`: { defaultTime, autoReminders, autoReminderDelay }
- `readStatuses`: { enabled, teamReadStatuses, teamReplyIndicators, recentOpensEnabled }
- `autoDrafts`: { followUps, scheduling, schedulingCcTeammate, schedulingPrompt }
- `calendar`: { defaultView, weekStartsOn, workingHoursStart, workingHoursEnd, showWeekends, defaultMeetingDuration, meetingLink, meetingLinkProvider, eventNotifications, secondaryTimezone, calendars[] }
- `autoArchive`: { enabled, autoLabels[] }
- `smartSend`: { enabled }
- `signatures`: { default }

**Current User**
- `id`: usr_001
- `name`: Alex Morgan
- `email`: alex.morgan@techcorp.io
- `timezone`: America/New_York
- `plan`: business

**Blocked Sender** (2 total)
- `email`: string
- `blockedAt`: ISO datetime

**Recent Opens** (15 total)
- `emailId`: string
- `recipientName`: string
- `recipientEmail`: string
- `openedAt`: ISO datetime
- `device`: string ('desktop' | 'mobile')

### Relationships
- Emails reference contacts by name/email in from/to/cc/bcc fields
- Emails have label IDs referencing the labels array
- Emails have autoLabel IDs referencing the autoLabels array
- Email split field maps to split criteria
- Thread emails share a threadId
- Calendar event attendees reference contacts by email
- Snippets reference currentUser as author
- Recent opens reference emailIds and contact names/emails
- Settings.splitInbox.splits references split IDs
- Settings.autoArchive.autoLabels references auto label IDs
- Settings.calendar.calendars is an embedded array

## Navigation Structure

### Hash-based Routing
| Route | View |
|-------|------|
| `#/inbox` | Inbox with split tabs (default) |
| `#/done` | Done/Archive folder |
| `#/sent` | Sent folder |
| `#/drafts` | Drafts folder |
| `#/scheduled` | Scheduled folder |
| `#/reminders` | Reminders folder |
| `#/trash` | Trash folder |
| `#/spam` | Spam folder |
| `#/email/{id}` | Email detail view |
| `#/label/{id}` | Label email list |
| `#/starred` | Starred emails |
| `#/search` | Search view |
| `#/settings` | Settings (general tab) |
| `#/settings/{tab}` | Settings with specific tab |

### How to Reach Each Section
- **Folders**: Click in sidebar, or use command palette (Cmd+K > "Go to...")
- **Email detail**: Click any email row in a list
- **Compose**: Click "Compose" button in sidebar, press C, or Cmd+K > "Compose"
- **Settings**: Click "Settings" in sidebar footer, or Cmd+K > "Go to Settings"
- **Settings tabs**: Click tab in settings view, or Cmd+K > specific settings name
- **Search**: Click search input in sidebar, press /, or Cmd+K > "Search"
- **Labels**: Click label name in sidebar
- **Calendar**: Always visible in right sidebar
- **Command Palette**: Cmd+K or Ctrl+K from anywhere

## Form Controls, Dropdowns, Toggles, and Options

### Dropdowns (Custom, not native `<select>`)
| ID | Label | Options |
|----|-------|---------|
| setting-theme | Theme | Dark, Light, Auto |
| setting-density | Display density | Compact, Comfortable, Spacious |
| setting-undo-send | Undo send delay | 5 seconds, 10 seconds, 20 seconds, 30 seconds |
| setting-default-reply | Default reply action | Reply, Reply All |
| setting-reminder-time | Default reminder time | 8:00 AM, 9:00 AM, 10:00 AM, 12:00 PM, 2:00 PM, 5:00 PM |
| setting-reminder-delay | Auto reminder delay | 1 day, 2 days, 3 days, 5 days, 7 days |
| setting-calendar-view | Default calendar view | Day, Week |
| setting-week-start | Week starts on | Sunday, Monday |
| setting-meeting-duration | Default meeting duration | 15 minutes, 30 minutes, 45 minutes, 60 minutes |
| setting-meeting-link-provider | Meeting link | Google Meet, Zoom, None |
| setting-event-notifications | Event notifications | None, 5 minutes before, 10 minutes before, 15 minutes before, 30 minutes before |

### Toggle Switches
| ID | Label | Default |
|----|-------|---------|
| setting-keyboard-shortcuts | Keyboard shortcuts | On |
| setting-desktop-notifications | Desktop notifications | On |
| setting-sound-notifications | Sound notifications | Off |
| setting-auto-advance | Auto-advance | On |
| setting-split-enabled | Enable Split Inbox | On |
| setting-read-statuses | Enable read statuses | On |
| setting-team-read-statuses | Team read statuses | On |
| setting-team-reply-indicators | Team reply indicators | On |
| setting-recent-opens | Recent Opens feed | On |
| setting-auto-drafts-followups | Follow-up drafts | On |
| setting-auto-drafts-scheduling | Scheduling drafts | On |
| setting-show-weekends | Show weekends | On |
| setting-auto-archive-enabled | Enable Auto Archive | Off |
| auto-label-{id} | Each auto label name | Varies |
| Calendar toggles | Each calendar enable/disable | On |

### Radio Groups
| Name | Options | Default |
|------|---------|---------|
| auto-reminders | All messages that need a follow-up, Messages with external recipients only, Off | all-follow-ups |

### Text Inputs / Text Areas
- Search input (sidebar and search view)
- Command palette input
- Composer fields: To, Cc, Bcc, Subject
- Composer body (contenteditable div)
- Signature editor (contenteditable div)
- Modal form fields: Label name, Snippet name/body, Event title/date/time/location/description, Reminder date/time, Schedule date/time

## Seed Data Summary

### Current User
- **Alex Morgan** — VP of Engineering at TechCorp (alex.morgan@techcorp.io), Business plan

### Contacts (28)
**Teammates (TechCorp, 8):**
Jamie Chen, Priya Patel, Marcus Williams, Sofia Reyes, Daniel Park, Rachel Kim, Tom Nguyen, Elena Vasquez

**External (20):**
Contacts from companies: Vertex Capital, Acme Ventures, SolarPeak, CloudNine Labs, NovaTech, DataStream, InfoSec Pro, Urban Design Co, Greenfield Analytics, Quantum Computing Inc, etc.

### Emails (125)
- **57 in inbox** (29 important, 19 other, 9 calendar)
- **40 in done** (archived)
- **10 in sent**
- **5 drafts**
- **3 scheduled**
- **5 in trash**
- **5 in spam**
- **29 unread**, 8 starred, 19 with attachments, 5 with reminders
- Content: P0 incidents, Series B fundraising, contract reviews, candidate interviews, customer renewals, AWS alerts, GitHub PRs, newsletters, travel bookings, receipts, social notifications, Figma comments, sprint summaries, etc.

### Labels (10 user-created)
Project Alpha (blue), Urgent (red), Finance (yellow), Hiring (green), Design (purple), Infrastructure (teal), Client Work (orange), Personal (gray), Marketing (pink), Legal (dark teal)

### Auto Labels (6)
Newsletters, Receipts, Travel, Social, Updates, Finance — each with enable/disable toggle

### Splits (4)
Important (⭐), Other (📋), Calendar (📅), 📰 News

### Snippets (9)
Meeting Follow-up, Introduction Template, Project Status Update, Interview Scheduling, Thank You Note, Out of Office, Feature Request Response, Bug Report Acknowledgment, Weekly Summary

### Calendar Events (16)
Events spanning March 2-16, 2026: team standups, 1:1s, external meetings, all-hands, design reviews, lunch meetings, personal events

### Blocked Senders (2)
spam@fakecorp.com, promos@cheapdeals.biz

### Recent Opens (15)
Recent read receipt entries from various contacts opening Alex's sent emails

# GitLab Plan & Track

## Summary

A project planning and tracking application replicating GitLab's "Plan and Track" features for a software engineering team at AcmeCorp working on their "platform-v4" project. The app provides issue tracking, epic management, milestone planning, iteration/sprint management, label organization, Kanban boards, and a personal to-do list. All data persists in localStorage and syncs to the server on every mutation.

## Main Sections / Pages

### 1. Issues (default view)
- **List view** (`#/issues`): Filterable, sortable, paginated table of all issues
- **Detail view** (`#/issues/{id}`): Full issue with description, sidebar fields, time tracking, and timelogs
- **New issue** (`#/new-issue`): Form with all fields
- **Edit issue** (`#/edit-issue/{id}`): Pre-populated form

### 2. Boards (`#/boards`)
- Kanban board view with configurable columns
- Three pre-configured boards: Development Board, Bug Triage, Sprint Board
- Drag-and-drop cards between lists
- Open (backlog) and Closed columns always present

### 3. Epics (`#/epics`)
- **List view**: Open and closed epics grouped by status
- **Detail view** (`#/epics/{id}`): Epic with child issues, child epics, progress bar, sidebar
- **New/Edit epic** forms

### 4. Milestones (`#/milestones`)
- **List view**: Active and closed milestones with progress bars
- **Detail view** (`#/milestones/{id}`): Stats (open/closed/weight/time), issue lists
- **New/Edit milestone** forms

### 5. Iterations (`#/iterations`)
- Grouped by iteration cadence
- Each cadence shows current, upcoming, and completed iterations
- **Detail view** (`#/iterations/{id}`): Stats and issue breakdown
- **New cadence** and **New iteration** forms

### 6. Labels (`#/labels`)
- Management page showing all labels grouped by scope
- Scoped labels (e.g., `priority::high`) displayed distinctly from regular labels
- **New/Edit label** forms with color picker

### 7. To-Do List (`#/todos`)
- Three tabs: To Do (pending), Snoozed, Done
- Snooze with preset durations (1 hour, later today, tomorrow, next week)
- Mark done, restore, and mark-all-done actions

## Complete List of Implemented Features and UI Interactions

### Issue Management
- Create, edit, and delete issues
- Open/close (toggle status) issues
- Filter issues by: status (open/closed/all), assignee, milestone, label, search text
- Sort issues by: created date, updated date, due date, title, weight (asc/desc)
- Paginated issue list (20 per page)
- Issue detail sidebar with inline editors for: assignees, labels, milestone, iteration, epic, health status, due date, weight, time estimate
- Confidential issue indicator
- Health status badges (on track, needs attention, at risk)
- Overdue date highlighting
- Time tracking: set estimates, add time entries with date/summary, delete timelogs

### Epic Management
- Create, edit epics
- Open/close epics
- Nested epics (parent/child relationships)
- Epic progress bar (based on child issue completion)
- Epic labels (group labels only)
- Epic detail shows child epics and child issues

### Milestone Management
- Create, edit milestones
- Active/closed status toggle
- Progress tracking (open vs closed issues)
- Start date and due date
- Milestone detail shows stats: open count, closed count, total weight, time spent

### Iteration Management
- Iteration cadences: create, edit
- Cadence settings: automatic scheduling, duration in weeks, upcoming count, roll-over toggle
- Manual iterations within non-automatic cadences
- Iteration statuses: current, upcoming, closed
- Iteration detail with issue breakdown and stats

### Label Management
- Create, edit, delete labels
- Scoped labels (`scope::value` format) with distinct visual treatment
- Color picker with 30 preset colors
- Label type: project or group
- Label descriptions
- Issue count per label

### Board Management
- Multiple boards with tab switching
- Board lists based on label or milestone
- Drag-and-drop cards between lists
- Board cards show: title, labels, assignees, due date, weight
- Built-in Open (backlog) and Closed lists

### To-Do List
- Pending, snoozed, done tabs with counts
- Snooze with presets: 1 hour, 4 hours, tomorrow 8AM, next week
- Mark individual or all todos as done
- Restore done todos back to pending
- Remove snooze from snoozed items
- Todo shows: action type, author, target title, time ago

### General UI
- Hash-based routing (SPA navigation without page reloads)
- Toast notifications for all actions
- Confirmation dialogs for destructive actions
- Custom dropdown menus (no native `<select>`)
- Custom modal dialogs for inline sidebar editing
- GitLab-themed design with purple accent color
- Sidebar navigation with active state and counts
- Breadcrumb navigation on detail/form pages
- Pagination with page numbers

## Data Model

### Users (15 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `usr_1` through `usr_15` |
| name | string | Full name |
| username | string | Short username |
| email | string | Email address |
| avatarColor | string | Hex color for avatar circle |
| role | string | Owner, Maintainer, Developer, Reporter, or Guest |

### Issues (56 records: 47 open, 9 closed)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `issue_1` through `issue_56` |
| iid | number | Display number (1-56) |
| title | string | Issue title |
| description | string | Full description text |
| status | string | `open` or `closed` |
| assignees | string[] | Array of user IDs |
| labels | string[] | Array of label IDs |
| milestoneId | string\|null | Reference to milestone |
| iterationId | string\|null | Reference to iteration |
| epicId | string\|null | Reference to epic |
| weight | number\|null | Positive integer |
| dueDate | string\|null | `YYYY-MM-DD` format |
| startDate | string\|null | `YYYY-MM-DD` format |
| healthStatus | string\|null | `on_track`, `needs_attention`, or `at_risk` |
| timeEstimate | number | Seconds (0 = no estimate) |
| timeSpent | number | Seconds (0 = no time logged) |
| confidential | boolean | Whether issue is confidential |
| authorId | string | User who created the issue |
| createdAt | string | ISO 8601 timestamp |
| updatedAt | string | ISO 8601 timestamp |
| closedAt | string\|null | ISO 8601 timestamp when closed |
| taskIds | string[] | Child task IDs (unused, reserved) |
| linkedIssueIds | string[] | Related issue IDs (unused, reserved) |

### Labels (30 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `lbl_1` through `lbl_30` |
| title | string | Label name (e.g., `priority::critical`, `security`) |
| description | string | What the label means |
| color | string | Background hex color |
| textColor | string | Text hex color |
| type | string | `project` or `group` |
| scoped | boolean | Whether it's a scoped label (contains `::`) |

**Scoped label groups:**
- `priority::` — critical, high, medium, low
- `workflow::` — ready, in-progress, review, done
- `type::` — bug, feature, improvement, documentation, task
- `component::` — frontend, backend, api, database, infrastructure

**Regular labels:** needs-discussion, good-first-issue, security, performance, UX, breaking-change, regression, technical-debt, blocked, design-needed, accessibility, testing

### Milestones (8 records: 7 active, 1 closed)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `ms_1` through `ms_8` |
| title | string | e.g., "v4.0 - Platform Redesign" |
| description | string | Milestone description |
| startDate | string\|null | `YYYY-MM-DD` |
| dueDate | string\|null | `YYYY-MM-DD` |
| status | string | `active` or `closed` |
| createdAt | string | ISO 8601 |

**Active milestones:** v4.0 - Platform Redesign, v4.1 - Performance, v4.2 - Security Hardening, v4.3 - Mobile Optimization, v5.0 - Enterprise Edition, Backlog, Q1 2026 Planning
**Closed:** v3.9 - Maintenance

### Iteration Cadences (3 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `cad_1` through `cad_3` |
| title | string | Cadence name |
| description | string | Description |
| automatic | boolean | Whether iterations are auto-created |
| startDate | string\|null | When cadence starts |
| durationWeeks | number\|null | Weeks per iteration |
| upcomingIterations | number\|null | How many to auto-create |
| rollOver | boolean | Move incomplete issues to next iteration |
| active | boolean | Whether cadence is active |

**Cadences:** Sprint Cadence (2-week, automatic, rollover), Monthly Planning (4-week, automatic), Release Cycle (manual)

### Iterations (12 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `iter_1` through `iter_12` |
| title | string | e.g., "Sprint 26" |
| cadenceId | string | Parent cadence reference |
| startDate | string | `YYYY-MM-DD` |
| dueDate | string | `YYYY-MM-DD` |
| status | string | `current`, `upcoming`, or `closed` |
| createdAt | string | ISO 8601 |

**Sprint Cadence:** Sprint 23-28 (23-25 closed, 26 current, 27-28 upcoming)
**Monthly Planning:** January (closed), February (current), March (upcoming)
**Release Cycle:** 4.0 Alpha (closed), 4.0 Beta (closed), 4.0 RC (current)

### Epics (11 records: 10 open, 1 closed)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `epic_1` through `epic_11` |
| iid | number | Display number |
| title | string | Epic title |
| description | string | Full description |
| status | string | `open` or `closed` |
| startDate | string\|null | `YYYY-MM-DD` |
| dueDate | string\|null | `YYYY-MM-DD` |
| labels | string[] | Label IDs (group labels) |
| healthStatus | string\|null | `on_track`, `needs_attention`, `at_risk` |
| authorId | string | Creator user ID |
| confidential | boolean | |
| parentEpicId | string\|null | Parent epic for hierarchy |
| createdAt | string | ISO 8601 |
| updatedAt | string | ISO 8601 |

**Epic hierarchy:**
- Platform Redesign → Frontend Modernization, API v3 Migration
- Performance Initiative → Database Optimization, Caching Layer Implementation
- Security Hardening (confidential, at risk)
- Mobile App v2, Documentation Overhaul, Enterprise SSO Integration
- Analytics Dashboard (closed)

### Boards (3 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `board_1` through `board_3` |
| name | string | Board name |
| lists | object[] | Array of list definitions |

Each list has: id, type (`label` or `milestone`), labelId or milestoneId, position.

**Boards:**
1. Development Board — lists: workflow::ready, workflow::in-progress, workflow::review, workflow::done
2. Bug Triage — lists: priority::critical, priority::high, priority::medium, priority::low
3. Sprint Board — lists: v4.0, v4.1, v4.2 milestones

### Todos (15 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `todo_1` through `todo_15` |
| targetType | string | `issue` or `epic` |
| targetId | string | Reference to issue or epic |
| action | string | `assigned`, `mentioned`, or `review_requested` |
| status | string | `pending`, `snoozed`, or `done` |
| authorId | string | Who triggered the todo |
| createdAt | string | ISO 8601 |
| snoozedUntil | string\|null | When snooze expires |

**Distribution:** 8 pending, 2 snoozed, 5 done

### Timelogs (18 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | `tl_1` through `tl_18` |
| issueId | string | Issue this time was logged against |
| userId | string | Who logged the time |
| timeSpent | number | Seconds spent |
| summary | string | What was worked on |
| spentAt | string | ISO 8601 date |

## Navigation Structure

| Route | View | How to reach |
|-------|------|-------------|
| `#/issues` | Issue list | Sidebar → Issues |
| `#/issues/{id}` | Issue detail | Click any issue row |
| `#/new-issue` | New issue form | Issues → "New issue" button |
| `#/edit-issue/{id}` | Edit issue form | Issue detail → "Edit" button |
| `#/boards` | Board view | Sidebar → Boards |
| `#/epics` | Epic list | Sidebar → Epics |
| `#/epics/{id}` | Epic detail | Click any epic row |
| `#/new-epic` | New epic form | Epics → "New epic" button |
| `#/edit-epic/{id}` | Edit epic form | Epic detail → "Edit" button |
| `#/milestones` | Milestone list | Sidebar → Milestones |
| `#/milestones/{id}` | Milestone detail | Click any milestone row |
| `#/new-milestone` | New milestone form | Milestones → "New milestone" button |
| `#/edit-milestone/{id}` | Edit milestone form | Milestone detail → "Edit" button |
| `#/iterations` | Iteration list | Sidebar → Iterations |
| `#/iterations/{id}` | Iteration detail | Click any iteration row |
| `#/new-cadence` | New cadence form | Iterations → "New cadence" button |
| `#/edit-cadence/{id}` | Edit cadence form | Cadence → "Edit" button |
| `#/new-iteration` | New iteration form | Cadence → "Add iteration" button |
| `#/labels` | Label list | Sidebar → Labels |
| `#/new-label` | New label form | Labels → "New label" button |
| `#/edit-label/{id}` | Edit label form | Label row → "Edit" button |
| `#/todos` | To-do list | Sidebar → To-Do List, or top-bar checkmark icon |

## Available Form Controls, Dropdowns, Toggles, and Options

### Issue Form
- **Title**: text input (required)
- **Description**: textarea
- **Assignees**: checkbox grid of all 15 users
- **Labels**: checkbox grid of all 30 labels
- **Milestone**: custom dropdown (active milestones only)
- **Iteration**: custom dropdown (non-closed iterations)
- **Epic**: custom dropdown (open epics only)
- **Start date**: text input (YYYY-MM-DD)
- **Due date**: text input (YYYY-MM-DD)
- **Weight**: number input (min 0)
- **Confidential**: checkbox

### Issue Detail Sidebar Editors (via modal dialogs)
- **Assignees**: checkbox list of users
- **Labels**: checkbox list of all labels
- **Milestone**: radio list (None + active milestones)
- **Iteration**: radio list (None + non-closed iterations)
- **Epic**: radio list (None + open epics)
- **Health status**: radio list (None, On track, Needs attention, At risk)
- **Due date**: text input with Clear button
- **Weight**: number input with Clear button
- **Time estimate**: text input accepting duration strings (e.g., "2h 30m", "1d", "3w")
- **Add time entry**: time spent (duration string), date (YYYY-MM-DD), summary (text)

### Issue Filters
- **Status tabs**: Open, Closed, All
- **Search**: text input for title/description search
- **Assignee dropdown**: Any, or specific user
- **Milestone dropdown**: Any, or specific active milestone
- **Label dropdown**: multi-select checkboxes for labels
- **Sort dropdown**: Created date, Updated date, Due date, Title, Weight (toggle asc/desc)

### Epic Form
- **Title**: text input (required)
- **Description**: textarea
- **Labels**: checkbox grid (group labels only)
- **Parent epic**: custom dropdown (open epics)
- **Start date**, **Due date**: text inputs
- **Confidential**: checkbox

### Milestone Form
- **Title**: text input (required)
- **Description**: textarea
- **Start date**, **Due date**: text inputs

### Cadence Form
- **Title**: text input (required)
- **Description**: textarea
- **Automatic scheduling**: checkbox
- **Start date**: text input
- **Duration (weeks)**: number input (1-52)
- **Upcoming iterations**: number input (1-10)
- **Roll over**: checkbox

### Iteration Form
- **Title**: text input (required)
- **Cadence**: custom dropdown (manual cadences only)
- **Start date**, **Due date**: text inputs

### Label Form
- **Title**: text input (use `::` for scoped labels)
- **Description**: textarea
- **Type**: custom dropdown (Project, Group)
- **Color**: color swatch picker (30 colors) with live preview

### To-Do Actions
- **Snooze picker**: 1 hour, Later today (4h), Tomorrow (8 AM), Next week
- **Tab switching**: To Do, Snoozed, Done

## Seed Data Summary

### Users (15)
Sarah Chen (Owner), Marcus Johnson (Maintainer), Priya Patel (Maintainer), James O'Brien (Dev), Aisha Mohammed (Dev), Luca Rossi (Dev), Nina Kowalski (Dev), David Kim (Dev), Fatima Al-Rashid (Reporter), Chen Wei (Dev), Alex Thompson (Dev), Maria Garcia (Reporter), Raj Kapoor (Guest), Yuki Tanaka (Dev), Oliver Schmidt (Maintainer)

### Issues (56)
- 47 open, 9 closed
- Span milestones: v4.0 (most), v4.1, v4.2, v4.3, v5.0, Backlog, Q1 2026, v3.9 (closed)
- Various labels: bugs, features, improvements, docs, tasks
- Assigned across 13 team members, some unassigned
- Weight range: 1-21
- Time estimates: 30 min to 48 hours
- 5 confidential issues (security related)
- Health statuses: on_track, needs_attention, at_risk, and null

### Labels (30)
- 18 scoped (4 priority, 4 workflow, 5 type, 5 component)
- 12 unscoped (needs-discussion, good-first-issue, security, performance, etc.)

### Milestones (8)
v4.0 (Dec 2025-Feb 2026), v4.1 (Mar-Apr 2026), v4.2 (Apr-May 2026), v4.3 (Jun-Jul 2026), v5.0 (Aug-Nov 2026), Backlog (no dates), Q1 2026, v3.9 (closed)

### Iterations (12)
6 sprints (bi-weekly), 3 monthly, 3 release cycles. Mix of closed/current/upcoming.

### Epics (11)
10 open, 1 closed. Two hierarchies: Platform Redesign (3 epics), Performance Initiative (3 epics). Plus standalone epics for Security, Mobile, Docs, SSO, Analytics.

### Boards (3)
Development Board (workflow labels), Bug Triage (priority labels), Sprint Board (milestone-based)

### Todos (15)
8 pending, 2 snoozed, 5 done. Actions: assigned, mentioned, review_requested.

### Timelogs (18)
Distributed across 10 issues, logged by 9 users. Time range: 1.5h to 8h per entry.

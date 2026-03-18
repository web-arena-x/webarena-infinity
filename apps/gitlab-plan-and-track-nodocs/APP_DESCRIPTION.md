# GitLab Plan and Track — App Description

## Summary

A faithful replica of GitLab's Plan and Track features — the project management and issue tracking capabilities of the GitLab DevOps platform. The app implements issue tracking, kanban boards, milestones, iterations (sprints), epics, roadmap visualization, time tracking, labels management, quick actions via slash commands, and a notification system. All within a single-page application with a GitLab-inspired sidebar navigation.

The project context is "DevTronics Platform" — a fictional software product with 12 team members actively working across multiple milestones and epics.

## Main Sections/Pages

1. **Issues List** — Paginated table of all issues with filtering, sorting, search, and bulk actions
2. **Issue Detail** — Full issue view with description, metadata sidebar, comments, activity feed, and related issues
3. **New Issue Form** — Issue creation form with all metadata fields and template selection
4. **Labels** — Label management with create/edit/delete, color picker, scoped labels
5. **Milestones** — Milestone list (active/closed tabs), milestone detail with issue breakdown and time tracking
6. **Boards** — Kanban board with drag-and-drop, configurable label-based columns, board filtering
7. **Iterations** — Sprint management organized by cadence, with burndown visualization
8. **Epics** — Epic list with filtering, epic detail with child issues and timeline
9. **Roadmap** — Gantt-style timeline view of epics with progress indicators
10. **Time Tracking** — Report showing time estimates vs. time spent by milestone and label
11. **Notifications** — Notification feed with read/unread status and notification level preferences

## Implemented Features and UI Interactions

### Issues
- List view with columns: title, status, assignee(s), labels, milestone, weight, due date, created date
- Filter by: status (open/closed/all), author, assignee, label (multi-select), milestone, sort order
- Sort by: created date, updated date, due date, priority, weight (ascending/descending)
- Full-text search across title, description, and issue number
- Pagination (20 per page) with page navigation
- Bulk actions: close, assign, add label, set milestone (via checkbox selection)
- Issue types: issue, incident, task
- Inline title editing (click to edit)
- Description editing with Markdown support
- Issue close/reopen
- Comment system with Markdown rendering
- Quick actions in comments: /close, /reopen, /assign, /unassign, /label, /unlabel, /milestone, /weight, /due, /estimate, /spend
- Related issues (blocks, is blocked by, related to) — add/remove
- Confidential issue toggle
- Subscribe/unsubscribe to issue notifications

### Issue Detail Sidebar
- Assignees — multi-select searchable dropdown
- Labels — multi-select searchable dropdown with color swatches, removable chips, scoped label enforcement
- Milestone — dropdown selection (active milestones only)
- Iteration — dropdown selection (current/upcoming iterations only)
- Weight — numeric input (0-99)
- Due date — text input (YYYY-MM-DD) with clear button
- Confidential — toggle switch
- Time tracking — estimate/spent bar, input fields for adding time (e.g., "4h 30m")
- Notifications — subscribe/unsubscribe button

### Labels Management
- List of all labels grouped by scoped/regular
- Each label shows: color badge, name, description, issue count
- Create new label: name, description, color picker (20 preset colors + hex input)
- Edit label (modal form)
- Delete label (removes from all issues, epics, board lists)
- Scoped labels (e.g., `priority::high`) displayed with `::` separator

### Milestones
- List view with active/closed tabs
- Each milestone card shows: title, dates, description, progress bar, open/closed counts
- Create milestone: title, description, start date, due date
- Edit milestone (modal form)
- Close/reopen milestone
- Delete milestone (clears from all issues)
- Milestone detail view: description, date range, progress bar, time tracking summary, open/closed issue lists

### Boards (Kanban)
- Default board: "Development Board" with columns: Open, To Do, In Progress, Review, Done, Closed
- Drag-and-drop issues between columns
- Moving to "Closed" column closes the issue
- Moving from "Closed" reopens the issue
- Label-based columns (moving adds/removes the label, handles scoped labels)
- Board filtering by assignee and milestone
- Add new label-based list (modal with label dropdown)
- Remove label-based lists
- Issue cards show: title, labels (non-status, max 3), issue number, weight, assignee avatars
- "New issue" button per column
- Confidential icon on cards

### Iterations (Sprints)
- Organized by cadence (e.g., "Engineering Sprints" 2-week, "Design Cycles" 3-week)
- Each cadence section shows current, upcoming, and closed iterations
- Current iteration highlighted with badge and left border
- Each iteration card: title, date range, progress bar, issue/weight counts
- Create iteration: cadence selection, title, start date, end date
- Iteration detail view: status badge, cadence info, date range, progress, stats grid (total issues, completed, open, total weight, completed weight), burndown visualization, open/closed issue lists

### Epics
- List view with open/closed/all filter tabs and search
- Each epic card: title, status badge, description preview, progress bar, issue counts, date range, author, labels
- Create epic: title, description, start date, due date, labels, confidential toggle
- Close/reopen epic
- Epic detail view: description (Markdown), progress bar and stats, timeline visualization, child issues list with table, add child issue dropdown
- Epic sidebar: labels, start date, due date, confidential status

### Roadmap
- Gantt-style horizontal timeline
- Each epic displayed as a bar spanning start-to-due date
- Bar shows progress fill based on completed child issues
- Month column headers
- Zoom level control (weeks/months/quarters dropdown)
- Click epic label to navigate to epic detail

### Time Tracking
- Summary cards: total estimated, total spent, remaining
- Per-milestone breakdown with time tracking bars
- Per-label breakdown with time tracking bars
- Time displayed in human-readable format (e.g., "4h 30m")

### Notifications
- Notification feed sorted by date (newest first)
- Unread notifications highlighted with blue background
- Notification types: assigned, mentioned, comment, status change, label change, milestone change
- Mark individual notification as read
- Mark all as read
- Click notification to navigate to the related issue
- Notification level preference: global, watch, on mention, disabled

### Quick Actions (Slash Commands)
Supported in comment box:
- `/close` — close the issue
- `/reopen` — reopen the issue
- `/assign @username` — assign user
- `/unassign @username` — remove assignee
- `/label ~labelname` — add label (handles scoped label replacement)
- `/unlabel ~labelname` — remove label
- `/milestone %title` — set milestone
- `/weight N` — set weight
- `/due YYYY-MM-DD` — set due date
- `/estimate Xh[Ym]` — set time estimate
- `/spend Xh[Ym]` — add time spent

## Data Model

### Users (12 users)
Fields: id, username, name, email, avatar_color, role
Roles: Owner, Maintainer, Developer, Reporter, Guest

### Labels (20 labels)
Fields: id, name, description, color, textColor, scoped
Types: Regular labels (bug, feature, documentation, performance, security, UX, backend, frontend, devops, tech-debt, needs-investigation, breaking-change) and scoped labels (priority::critical/high/medium/low, status::to-do/in-progress/review/done)

### Milestones (7 milestones)
Fields: id, title, description, startDate, dueDate, status (active/closed)
Milestones: v1.0 Foundation (closed), v1.1 Stability (closed), v1.2 Hotfixes (closed), v2.0 API Overhaul (active), v2.1 Integrations (active), v3.0 Enterprise (active), Backlog (active)

### Iteration Cadences (2 cadences)
Fields: id, title, description, durationWeeks, autoSchedule, startDate

### Iterations (13 iterations)
Fields: id, cadenceId, title, startDate, endDate, status (closed/current/upcoming)
Engineering Sprints: Sprint 1-8 (2-week cadence)
Design Cycles: Design Cycle 1-5 (3-week cadence)

### Epics (10 epics)
Fields: id, title, description, status, startDate, dueDate, labels, authorId, confidential, childIssueIds, childEpicIds, createdAt, updatedAt
Epics: User Authentication Overhaul, API v3 Migration, Performance Optimization Phase 2, Mobile Responsive Redesign, CI/CD Pipeline Modernization, Accessibility Compliance, Data Export & Reporting (closed), Enterprise SSO Integration (confidential), Search Infrastructure Upgrade, Notification System Revamp

### Issues (130 issues)
Fields: id, title, description, type (issue/incident/task), status (open/closed), authorId, assigneeIds (array), labelIds (array), milestoneId, iterationId, weight, dueDate, confidential, timeEstimate (seconds), timeSpent (seconds), createdAt, updatedAt, closedAt, relatedIssues (array of {issueId, type})
Distribution: 101 open, 29 closed; types: issue, incident, task

### Comments (20 seed comments)
Fields: id, issueId, authorId, body, createdAt, updatedAt, type

### Activity Log (15 seed entries)
Fields: id, issueId, userId, action, detail, createdAt
Action types: created_issue, closed_issue, reopened_issue, assigned, unassigned, added_label, removed_label, changed_label, changed_milestone, changed_iteration

### Boards (1 board)
Fields: id, name, lists (array of {id, type, title, position, labelId})
Board "Development Board" lists: Open (backlog), To Do (status::to-do), In Progress (status::in-progress), Review (status::review), Done (status::done), Closed

### Notifications (20 seed notifications)
Fields: id, userId, type, issueId, actorId, read, createdAt, message

### Notification Settings
Fields: level (global/watch/on_mention/disabled), email (bool), web (bool)

### Issue Templates (3 templates)
Fields: id, name, content (Markdown)
Templates: Bug Report, Feature Request, Task

### Project
Fields: id, name, path, description, visibility, createdAt

## Navigation Structure

**Sidebar navigation** (always visible, fixed left):
- Issues → Issues list (default view)
- Boards → Kanban board view
- Labels → Labels management
- Milestones → Milestones list
- Iterations → Iterations by cadence
- Epics → Epics list
- Roadmap → Timeline view
- Time tracking → Time tracking report
- Notifications → Notification feed

**Issue detail** — accessed by clicking any issue row in lists or board cards
**New issue** — accessed via "New issue" button on issues list
**Milestone detail** — accessed by clicking a milestone card
**Iteration detail** — accessed by clicking an iteration card
**Epic detail** — accessed by clicking an epic card

## Available Form Controls, Dropdowns, Toggles, and Their Options

### Dropdowns (all custom-built, searchable)
- **Author filter**: Any author + all 12 users
- **Assignee filter**: Any assignee + all 12 users
- **Label filter**: All 20 labels (multi-select with color swatches)
- **Milestone filter**: Any milestone + 7 milestones
- **Sort**: Newest, Oldest, Recently updated, Least recently updated, Due date (earliest/latest), Priority (highest/lowest), Weight (highest/lowest)
- **Issue template**: No template, Bug Report, Feature Request, Task
- **Issue type**: Issue, Incident, Task
- **Iteration cadence** (in create form): Engineering Sprints, Design Cycles
- **Notification level**: Global, Watch, On mention, Disabled
- **Roadmap zoom**: Weeks, Months, Quarters
- **Board filter assignee**: Any assignee + all 12 users
- **Board filter milestone**: Any milestone + all milestones
- **Related issue type**: Related to, Blocks, Is blocked by

### Toggles
- Confidential issue toggle (issue detail sidebar + new issue form)

### Text Inputs
- Issue title, description (textarea with Markdown)
- Comment editor (textarea with Markdown + quick actions)
- Weight (numeric, 0-99)
- Due date (YYYY-MM-DD text input)
- Time estimate/spend (e.g., "4h 30m")
- Search input (issues list, epics list)
- Label name, description, color hex
- Milestone title, description, start date, due date
- Iteration title, start date, end date
- Epic title, description, start date, due date

### Color Picker
- 20 preset colors + custom hex input

## Seed Data Summary

### Users (12)
Sarah Chen (Owner), Marek Kowalski (Maintainer), Ana Garcia (Maintainer), Jun Nakamura (Developer), Priya Sharma (Developer), Tom Ramirez (Developer), Li Wei (Developer), Emily Okonkwo (Developer), Karl Fischer (Reporter), Natalie Moreau (Reporter), David Kim (Developer), Ravi Singh (Guest)

Current user: Sarah Chen (id: 1)

### Issues (130)
- 101 open, 29 closed
- Types: 125 issues, 1 incident, 4 tasks
- Spread across milestones: v1.0 (7 closed), v1.1 (8 closed), v1.2 (2 closed), v2.0 API Overhaul (34 issues), v2.1 Integrations (19 issues), v3.0 Enterprise (11 issues), Backlog (19 issues), no milestone (remaining)
- Weight range: 1-13 (Fibonacci-like)
- Time tracking: many issues have estimates and time spent
- Some issues are confidential (issues #46, #57, #58, #59)
- Issues have related issues (blocks, is_blocked_by, related_to relationships)

### Labels (20)
Regular: bug, feature, documentation, performance, security, UX, backend, frontend, devops, tech-debt, needs-investigation, breaking-change
Scoped: priority::critical/high/medium/low, status::to-do/in-progress/review/done

### Milestones (7)
v1.0 Foundation (closed), v1.1 Stability (closed), v1.2 Hotfixes (closed), v2.0 API Overhaul (active), v2.1 Integrations (active), v3.0 Enterprise (active), Backlog (active, no dates)

### Epics (10)
User Authentication Overhaul, API v3 Migration, Performance Optimization Phase 2, Mobile Responsive Redesign, CI/CD Pipeline Modernization, Accessibility Compliance, Data Export & Reporting (closed), Enterprise SSO Integration (confidential), Search Infrastructure Upgrade, Notification System Revamp

### Iterations (13 across 2 cadences)
Engineering Sprints: Sprint 1-5 (closed), Sprint 6 (current), Sprint 7-8 (upcoming)
Design Cycles: Design Cycle 1-3 (closed), Design Cycle 4 (current), Design Cycle 5 (upcoming)

### Board
Development Board with 6 lists: Open, To Do, In Progress, Review, Done, Closed

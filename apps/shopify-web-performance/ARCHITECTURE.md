# Architecture Documentation

## Table of Contents
1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Data Model](#data-model)
4. [State Management & Persistence](#state-management--persistence)
5. [Routing](#routing)
6. [UI Component System](#ui-component-system)
7. [Task Workflows](#task-workflows)
8. [Verifying Operations via the Backend](#verifying-operations-via-the-backend)
9. [Data Relationships Reference](#data-relationships-reference)

---

## Overview

This is a single-page application (SPA) that replicates Shopify's Web Performance Dashboard. It is built with **pure HTML, CSS, and JavaScript** (no frameworks, no build step). All data is stored **in-memory** in a centralized `AppState` object and **persisted to `localStorage`** across page reloads. A Python HTTP server provides state sync and Server-Sent Events for external tool integration.

### How to Run

```bash
python3 server.py --port 8000
# Open http://localhost:8000 in a browser
```

### Technology Constraints

- No frameworks (React, Vue, etc.)
- No native OS UI elements (`<select>`, `alert()`, `<input type="date">`, etc.)
- All dropdowns, modals, toasts, and date inputs are custom HTML/CSS/JS
- All data lives in the browser (localStorage + in-memory), synced to server via PUT /api/state

---

## File Structure

```
index.html              App shell (sidebar, topbar, modal, toast containers)
css/styles.css          All styles (Shopify-inspired theme)
js/data.js              Seed data constants (store, themes, apps, pages, performance records, etc.)
js/state.js             Centralized AppState with mutations, queries, persistence
js/components.js        Reusable UI components (dropdowns, modals, toasts, badges, forms, charts)
js/views.js             All view renderers and modal/action helpers
js/app.js               Hash-based router and event handler attachment
server.py               HTTP server with state sync API and SSE
Dockerfile              Container definition
tasks.json              30 tasks (10 easy, 10 medium, 10 hard)
tasks/                  Task verifier Python scripts
sanity_check.py         Automated verifier sanity check
```

### Load Order

Scripts are loaded synchronously in `index.html` in this order:

1. **`data.js`** — Defines all constant seed data (`STORE`, `THEMES`, `APPS`, `PAGES`, `PERFORMANCE_RECORDS`, etc.)
2. **`state.js`** — Creates `AppState` using persisted data (from localStorage) or seed data
3. **`components.js`** — Defines the `Components` utility object
4. **`views.js`** — Defines the `Views` object (depends on `AppState` and `Components`)
5. **`app.js`** — Defines the `Router` and calls `initApp()` on DOMContentLoaded

Each script tag uses a `?v=1` cache-busting query parameter.

---

## Data Model

### Core Entities

| Entity | Key Fields | Stored In |
|--------|-----------|-----------|
| **Store** | `name`, `url`, `domain`, `plan`, `passwordProtected`, `currency`, `timezone` | `AppState.store` |
| **Current User** | `id`, `name`, `email`, `role`, `avatarColor` | `AppState.currentUser` |
| **Theme** | `id`, `name`, `version`, `author`, `active`, `family`, `os2Compatible`, `settings`, `performanceScore` | `AppState.themes[]` |
| **App** | `id`, `name`, `developer`, `category`, `installed`, `status`, `performanceImpact`, `scriptLoadTime`, `settings` | `AppState.apps[]` |
| **Page** | `id`, `name`, `path`, `pageType`, `monitored`, `priority`, `addedAt` | `AppState.pages[]` |
| **Performance Record** | `id`, `pageId`, `date`, `deviceType`, `lcp`, `inp`, `cls` | `AppState.performanceRecords[]` |
| **Event** | `id`, `title`, `type`, `date`, `description`, `affectedMetric`, `impact` | `AppState.events[]` |
| **Alert Rule** | `id`, `name`, `metric`, `condition`, `threshold`, `enabled`, `pageType`, `deviceType`, `emailNotifications` | `AppState.alertRules[]` |
| **Optimization** | `id`, `title`, `description`, `metric`, `priority`, `category`, `status`, `estimatedImpact`, `pageAffected` | `AppState.optimizations[]` |
| **Saved Report** | `id`, `name`, `metric`, `reportType`, `deviceType`, `dateRange`, `pageType`, `createdAt` | `AppState.savedReports[]` |
| **Performance Budget** | `metric` → `{ target, warning }` | `AppState.performanceBudgets` |

### Constants

| Constant | Values | Purpose |
|----------|--------|---------|
| `METRIC_THRESHOLDS` | LCP: good ≤2500ms, moderate ≤4000ms; INP: good ≤200ms, moderate ≤500ms; CLS: good ≤0.1, moderate ≤0.25 | Rating performance |
| `DEVICE_TYPES` | `all`, `desktop`, `mobile` | Filtering records |
| `DATE_RANGES` | `today`, `last_7_days`, `last_30_days` | Report time ranges |
| `PAGE_TYPES` | `home`, `product`, `collection`, `cart`, `blog`, `page`, `search`, `account`, `checkout` | Page classification |
| `EVENT_TYPES` | `app_installed`, `app_uninstalled`, `theme_changed`, `theme_updated`, `code_change`, `custom` | Event annotation types |
| `OPTIMIZATION_CATEGORIES` | `images`, `apps`, `theme`, `scripts`, `fonts`, `videos`, `other` | Optimization grouping |
| `OPTIMIZATION_STATUSES` | `pending`, `in_progress`, `completed`, `dismissed` | Optimization lifecycle |
| `OPTIMIZATION_PRIORITIES` | `critical`, `high`, `medium`, `low` | Priority levels |
| `REPORT_TYPES` | `over_time`, `by_page_url`, `by_page_type` | Report grouping |
| `METRICS` | `LCP` (ms), `INP` (ms), `CLS` (unitless) | Core Web Vitals |

### Theme Settings

Each theme has a `settings` object:

| Setting | Type | Values | Description |
|---------|------|--------|-------------|
| `pageTransitions` | boolean | true/false | Animated page transitions |
| `lazyLoading` | boolean | true/false | Lazy load images below fold |
| `stickyHeader` | boolean | true/false | Fixed header on scroll |
| `predictiveSearch` | boolean | true/false | Search suggestions |
| `cartType` | string | `drawer`, `page` | Cart display mode |
| `paginationLimit` | number | 12, 16, 20, 24, 32 | Products per page |
| `animationsEnabled` | boolean | true/false | CSS animations |

### App Settings

Each app has an `installed` boolean and a `settings` object with app-specific configuration. The `performanceImpact` object tracks per-metric impact (`{ lcp, inp, cls }`).

---

## State Management & Persistence

### AppState Object (`state.js`)

`AppState` is a single global object that holds all application data. It follows an observer pattern for reactivity.

#### Lifecycle

```
Page Load
   │
   ├─ _loadPersistedData()  ─── reads from localStorage('shopifyWebPerfAppState')
   │   │
   │   ├─ Found? → Check _seedVersion matches SEED_DATA_VERSION
   │   │   ├─ Match? → Parse JSON, return data
   │   │   └─ Mismatch? → Discard stale data, return null
   │   └─ Not found / error? → return null
   │
   ├─ _loadSeedData()  ─── deep-clones all constants from data.js
   │
   └─ AppState initialized from persisted data OR seed data
```

#### Mutation Flow

Every mutation method follows this pattern:

```
User action (click, form submit)
    │
    ├─ Calls AppState mutation method (e.g., installApp, addAlertRule)
    │     │
    │     ├─ Modifies in-memory data
    │     └─ Calls this.notify()
    │            │
    │            ├─ Notifies all subscribers (listeners)
    │            └─ Calls this._persist()
    │                   │
    │                   ├─ Serializes state to localStorage
    │                   └─ PUTs JSON to /api/state (fire-and-forget)
    │
    └─ UI update (toast, router refresh/navigate)
```

#### What Is Persisted

Persisted to `localStorage` under key `shopifyWebPerfAppState`:
- `store`, `currentUser`, `themes`, `apps`, `pages`, `performanceRecords`
- `events`, `performanceBudgets`, `alertRules`, `optimizations`, `savedReports`
- `_nextThemeId`, `_nextAppId`, `_nextPageId`, `_nextEventId`, `_nextAlertId`, `_nextOptimizationId`, `_nextReportId`
- `_seedVersion`

**Not** persisted (transient UI state):
- `currentRoute`, `routeParams`, `sidebarOpen`, `modalOpen`, `validationErrors`, `toasts`, `_listeners`

#### Reset Mechanism

`AppState.resetToSeedData()`:
1. Removes the localStorage key
2. Deep-clones all seed data from `data.js`
3. Replaces all AppState collections
4. Notifies listeners
5. PUTs the seed state to `/api/state`

Available in the UI via Settings > "Reset all data to defaults".

### Key Mutation Methods

| Method | Description |
|--------|-------------|
| `updateStore(data)` | Merges properties into `AppState.store` |
| `activateTheme(id)` | Sets `active: true` on target, `active: false` on all others |
| `updateThemeSettings(id, settings)` | Merges settings into theme's `settings` object |
| `installApp(id)` | Sets `installed: true`, `installedAt`, `status: 'active'` |
| `uninstallApp(id)` | Sets `installed: false`, `status: 'inactive'`, clears `installedAt` |
| `addPage(data)` | Creates new page with auto-incremented ID |
| `updatePage(id, data)` | Merges properties into existing page |
| `removePage(id)` | Removes page from array |
| `addEvent(data)` | Creates new event with auto-incremented ID |
| `updateEvent(id, data)` | Merges properties into existing event |
| `removeEvent(id)` | Removes event from array |
| `addAlertRule(data)` | Creates new alert with auto-incremented ID |
| `updateAlertRule(id, data)` | Merges properties into existing alert |
| `removeAlertRule(id)` | Removes alert from array |
| `addOptimization(data)` | Creates new optimization with auto-incremented ID |
| `updateOptimization(id, data)` | Merges properties into existing optimization |
| `removeOptimization(id)` | Removes optimization from array |
| `addSavedReport(data)` | Creates new report with auto-incremented ID |
| `removeSavedReport(id)` | Removes report from array |
| `updatePerformanceBudget(metric, data)` | Updates budget target/warning for a metric |

### Key Query Methods

| Method | Description |
|--------|-------------|
| `getActiveTheme()` | Returns the theme with `active: true` |
| `getInstalledApps()` | Returns apps with `installed: true` |
| `getAvailableApps()` | Returns apps with `installed: false` |
| `getMonitoredPages()` | Returns pages with `monitored: true` |
| `getAggregateMetrics(filters)` | Computes average LCP, INP, CLS across filtered records |
| `getRating(metric, value)` | Returns `good`, `moderate`, or `poor` based on thresholds |
| `getPerformanceOverTime(filters)` | Groups records by date for time-series charts |
| `getMetricsByPage(filters)` | Groups records by page for comparison |
| `getMetricsByPageType(filters)` | Groups records by page type |

---

## Routing

### Hash-Based Router (`app.js`)

The app uses hash-based routing. URLs look like `http://localhost:8000/#/themes/1`.

#### Route Table

| Pattern | Handler | Description |
|---------|---------|-------------|
| `/` | `Views.home()` | Dashboard with metric overview |
| `/themes` | `Views.themes()` | Theme list |
| `/themes/:id` | `Views.themeDetail(id)` | Theme detail and settings |
| `/apps` | `Views.apps()` | App list (installed + available) |
| `/apps/:id` | `Views.appDetail(id)` | App detail and settings |
| `/reports` | `Views.reports()` | Report overview (grid of report types) |
| `/reports/:type/:metric` | `Views.reportDetail(type, metric)` | Specific report with chart |
| `/pages` | `Views.pages()` | Page monitoring list |
| `/pages/:id` | `Views.pageDetail(id)` | Page-level performance |
| `/optimizations` | `Views.optimizations()` | Optimization recommendations |
| `/alerts` | `Views.alerts()` | Alert rule management |
| `/events` | `Views.events()` | Event annotation timeline |
| `/settings` | `Views.settings()` | Store settings, budgets, reset |

#### Rendering Cycle

```
Router.navigate(path)
    │
    ├─ Parse path and query params
    ├─ Update AppState.currentRoute and AppState.routeParams
    ├─ Push to browser history
    └─ Router.render()
         │
         ├─ Match route pattern → call view handler → get HTML string
         ├─ Set contentWrapper.innerHTML = html
         ├─ Update sidebar active state
         └─ Router.attachHandlers()  (bind event listeners to new DOM elements)
```

#### Event Handler Attachment

After each render, `Router.attachHandlers()` scans the DOM for interactive elements and binds event listeners. Elements are flagged (e.g., `el._handlerAttached = true`) to prevent duplicate bindings. This covers:

- Route links (`[data-route]`)
- Tab items (`.tab-item`)
- Action buttons (activate theme, install/uninstall app, save settings, etc.)
- Modal triggers (add page, add event, add alert, add optimization, create report)
- Status updates (complete optimization, dismiss optimization, enable/disable alert)

---

## UI Component System

### Components Object (`components.js`)

All reusable UI elements are methods on the global `Components` object. They return HTML strings for embedding in view templates.

#### Key Components

| Component | Method | Description |
|-----------|--------|-------------|
| Custom Dropdown | `Components.dropdown(id, options, selectedValue, opts)` | Div-based dropdown with search support |
| Modal | `Components.showModal(title, body, footer)` | Opens the global modal overlay |
| Toast | `Components.showToast(message, type, duration)` | Timed notification popup |
| Confirm Dialog | `Components.confirm(title, msg, onConfirm, opts)` | Modal with cancel/confirm buttons |
| Tabs | `Components.tabs(id, items, activeTab)` | Tab bar rendering |
| Badges | `Components.badge()`, `statusBadge()`, `ratingBadge()` | Status indicators |
| Metric Card | `Components.metricCard(metric, value, rating)` | Core Web Vital display card |
| Distribution Bar | `Components.distributionBar(good, moderate, poor)` | Color-coded percentage bar |
| Bar Chart | `Components.barChart(data, opts)` | Horizontal/vertical bar chart |
| Data Table | `Components.dataTable(headers, rows, opts)` | Sortable data table |
| Form Fields | `Components.formField()`, `textInput()`, `numberInput()`, `textarea()`, `checkbox()`, `toggleSwitch()`, `dateInput()` | Form building blocks |
| Info Boxes | `Components.infoBox()`, `warningBox()` | Alert/information boxes |
| Event Timeline | `Components.eventTimeline(events)` | Vertical timeline display |
| Utilities | `Components.escapeHtml()`, `escapeAttr()`, `formatDate()`, `formatMetricValue()` | HTML escaping, formatting |

#### Custom Dropdown Behavior

Dropdowns fire a custom `change` event with `detail.value` when an item is selected. Global event delegation handles:
- Opening/closing on trigger click
- Item selection (updates `data-value` attribute and trigger text)
- Click-outside-to-close
- Search filtering within dropdown menus

#### Modal System

Single global modal container in `index.html`:
```
#modalOverlay > #modalContainer > (#modalHeader + #modalBody + #modalFooter)
```
`Components.showModal()` populates these elements and adds the `.active` class. `Components.closeModal()` removes it. `Components.confirm()` is a convenience wrapper with cancel/confirm buttons.

---

## Task Workflows

### 1. Change Store Settings

**UI Path**: Settings page > Store section > form fields > "Save"

**State Changes**: `AppState.updateStore(data)` — merges properties into `AppState.store` via `Object.assign()`.

**Verifiable fields**: `name`, `domain`, `passwordProtected`, `currency`, `timezone`.

### 2. Activate Theme

**UI Path**: Themes page > theme card > "Activate" button

**State Changes**: `AppState.activateTheme(id)` — sets target `active: true`, sets all others to `active: false`.

### 3. Update Theme Settings

**UI Path**: Themes page > theme card > click > Theme detail > Settings tab > form > "Save settings"

**State Changes**: `AppState.updateThemeSettings(id, settings)` — merges into `theme.settings`.

**Settings**: `pageTransitions`, `lazyLoading`, `stickyHeader`, `predictiveSearch`, `cartType`, `paginationLimit`, `animationsEnabled`.

### 4. Install / Uninstall App

**UI Path**: Apps page > available app > "Install" / installed app > "Uninstall"

**State Changes**:
- `AppState.installApp(id)` — sets `installed: true`, records `installedAt` timestamp, sets `status: 'active'`
- `AppState.uninstallApp(id)` — sets `installed: false`, clears `installedAt`, sets `status: 'inactive'`

### 5. Update App Settings

**UI Path**: Apps page > installed app > click > App detail > Settings section > "Save settings"

**State Changes**: Modifies `app.settings` properties directly and calls `notify()`.

### 6. Add / Remove Monitored Page

**UI Path**: Pages page > "Add page" > modal > form > "Add" / page row > "Remove"

**State Changes**:
- `AppState.addPage(data)` — creates page with `id`, `name`, `path`, `pageType`, `monitored: true`, `priority`, `addedAt`
- `AppState.removePage(id)` — filters page from array

### 7. Toggle Page Monitoring

**UI Path**: Pages page > page row > monitoring toggle

**State Changes**: `AppState.updatePage(id, { monitored: true/false })`.

### 8. Add / Edit / Remove Event Annotation

**UI Path**: Events page > "Add event" / event row > "Edit" / event row > "Remove"

**State Changes**:
- `AppState.addEvent(data)` — creates event with `id`, `title`, `type`, `date`, `description`, `affectedMetric`, `impact`
- `AppState.updateEvent(id, data)` — merges properties
- `AppState.removeEvent(id)` — filters from array

### 9. Add / Edit / Remove Alert Rule

**UI Path**: Alerts page > "Add alert" / alert row > "Edit" / alert row > "Delete"

**State Changes**:
- `AppState.addAlertRule(data)` — creates alert with `id`, `name`, `metric`, `condition`, `threshold`, `enabled`, `pageType`, `deviceType`, `emailNotifications`
- `AppState.updateAlertRule(id, data)` — merges properties (also used to enable/disable)
- `AppState.removeAlertRule(id)` — filters from array

### 10. Add / Update / Remove Optimization

**UI Path**: Optimizations page > "Add optimization" / optimization card > "Mark completed" / "Dismiss"

**State Changes**:
- `AppState.addOptimization(data)` — creates with `id`, `title`, `description`, `metric`, `priority`, `category`, `status: 'pending'`, `estimatedImpact`, `pageAffected`
- `AppState.updateOptimization(id, data)` — changes `status` to `completed` or `dismissed`
- `AppState.removeOptimization(id)` — filters from array

### 11. Create / Delete Saved Report

**UI Path**: Reports page > "Create report" / report card > "Delete"

**State Changes**:
- `AppState.addSavedReport(data)` — creates with `id`, `name`, `metric`, `reportType`, `deviceType`, `dateRange`, `pageType`, `createdAt`
- `AppState.removeSavedReport(id)` — filters from array

### 12. Update Performance Budget

**UI Path**: Settings page > Performance Budgets section > form > "Save"

**State Changes**: `AppState.updatePerformanceBudget(metric, { target, warning })`.

### 13. Reset All Data

**UI Path**: Settings page > "Reset all data to defaults"

**State Changes**: `AppState.resetToSeedData()` — clears localStorage, restores seed data, re-pushes to server.

---

## Verifying Operations via the Backend

The server provides a state sync API that external verifiers use to check application state.

### Server API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/state` | GET | Read the current application state |
| `/api/state` | PUT | Update server-side state copy (called by browser on every mutation) |
| `/api/reset` | POST | Reset to seed data and notify browsers via SSE |
| `/api/events` | GET | Server-Sent Events stream for push commands |

### Verifier Pattern

Each verifier is a Python script at `tasks/task_<id>.py` with a `verify(server_url)` function:

```python
def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    state = resp.json()
    # Check conditions against state
    # Return (True, "success message") or (False, "failure message")
```

### Accessing State in Verifiers

The state JSON structure mirrors `AppState._getPersistable()`:

```python
state["store"]               # Store object
state["themes"]              # List of theme objects
state["apps"]                # List of app objects
state["pages"]               # List of page objects
state["performanceRecords"]  # List of performance record objects
state["events"]              # List of event objects
state["alertRules"]          # List of alert rule objects
state["optimizations"]       # List of optimization objects
state["savedReports"]        # List of saved report objects
state["performanceBudgets"]  # Dict: { lcp: {target, warning}, inp: {...}, cls: {...} }
```

### Sanity Check

`sanity_check.py` automates verification:
1. Loads seed data via Node.js (evaluating `data.js`)
2. For each task: reset to seed → apply solve function → push state → run verifier
3. Reports PASS/FAIL for all 30 tasks

---

## Data Relationships Reference

```
Store (singleton)
 ├── Themes (many; exactly one has active=true)
 │    └── settings (object with theme-specific config)
 ├── Apps (many; installed=true/false)
 │    ├── performanceImpact { lcp, inp, cls }
 │    └── settings (object with app-specific config)
 ├── Pages (many; monitored=true/false)
 │    └── performanceRecords (many; linked by pageId)
 ├── Events (many; event annotations with dates)
 ├── AlertRules (many; enabled=true/false)
 ├── Optimizations (many; status lifecycle)
 ├── SavedReports (many; configured report views)
 └── PerformanceBudgets (object: lcp, inp, cls targets)
```

### Seed Data Summary

| Collection | Count | ID Range |
|-----------|-------|----------|
| Themes | 6 | 1-6 |
| Apps | 10 | 1-10 (8 installed, 2 available) |
| Pages | 12 | 1-12 (11 monitored, 1 not) |
| Performance Records | 660 | (30 days × 11 pages × 2 device types) |
| Events | 8 | 1-8 |
| Alert Rules | 6 | 1-6 |
| Optimizations | 8 | 1-8 |
| Saved Reports | 4 | 1-4 |

Auto-increment counters start after the last seed ID:
- `_nextThemeId: 7`
- `_nextAppId: 11`
- `_nextPageId: 13`
- `_nextEventId: 9`
- `_nextAlertId: 7`
- `_nextOptimizationId: 9`
- `_nextReportId: 5`

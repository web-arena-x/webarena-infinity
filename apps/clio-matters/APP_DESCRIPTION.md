# Clio Matters - Legal Case Management System

## Summary

Clio Matters is a legal case management web application for the fictional "Meridian Law Group" law firm. It provides comprehensive matter (case) management including creation, editing, status tracking, kanban-based stage pipelines, financial tracking, personal injury features (damages, medical records, settlement calculations), and firm-wide settings management. The application simulates a production legal practice management system based on Clio Manage documentation.

## Main Sections/Pages

### 1. Matters List (`#/matters`)
- Table view of all 120 matters with sortable columns
- Status tabs: All (120), Open (78), Pending (27), Closed (18) -- note: 3 statuses only
- Search bar: searches matter number, description, and client name
- Filter dropdowns: Practice Area, Responsible Attorney, Billing Method
- Active filter chips with removal
- Bulk actions: Close Selected, Delete Selected, Update Status (shown when rows selected)
- Row selection via checkboxes (individual and select-all)
- Pagination (25 per page)
- Export to CSV
- Each row shows: checkbox, Matter #, Description, Status badge, Client, Practice Area, Responsible Attorney (avatar+name), Open Date
- Row actions: Edit (pencil), Duplicate (copy), Delete (trash)

### 2. Matter Creation Form (`#/matters/new`)
- Multi-section collapsible form for creating new matters
- Sections: Matter Details, Template, Permissions, Billing Preferences, Personal Injury Preferences, Related Contacts, Custom Fields, Document Folders, Notifications, Reports
- Actions: Save Matter, Save and Run Conflict Check, Cancel

### 3. Matter Edit Form (`#/matters/{id}/edit`)
- Same form as creation, pre-populated with existing matter data
- Additional action: Delete Matter (danger button)
- Status field editable (Open/Pending/Closed)

### 4. Matter Dashboard (`#/matters/{id}`)
- Breadcrumb: Matters / {matter number}
- Matter title (full description)
- Sub-tab navigation: Overview, Damages, Medical Records, Settlement

#### Overview Sub-tab
Two-column layout:
- **Left column:**
  - Financial Summary widget: Work in Progress, Outstanding Balance, Trust Balance, Budget progress bar, Total Time, Total Expenses
  - Action buttons: Quick Bill, Add Time, Add Expense
  - Recent Activity timeline (newest first, up to 20 entries with avatars)
- **Right column:**
  - Matter Details widget: all fields as label/value pairs, inline status change dropdown, Edit Matter and Duplicate buttons
  - Client widget: primary contact with phone, email, address, tags
  - Related Contacts widget: sortable list (A-Z, Z-A, List order), Add Related Contact button
  - Custom Fields widget: displays configured custom field values

#### Damages Sub-tab (`#/matters/{id}/damages`)
- Summary cards: Total Billed Damages, Total Paid Damages, Total Special, Total General, Total Other
- Filter tabs: All, Special, General, Other
- Add Damage button
- Table: Name, Amount, Type, Actions (edit/delete)

#### Medical Records Sub-tab (`#/matters/{id}/medical-records`)
- Search by provider name
- Filter dropdowns: Treatment Status, Record Status, Bill Status
- Sort: Name A-Z, Name Z-A, Newest, Oldest
- Add Provider button
- Provider cards showing: provider name, description, treatment dates, treatment status, record request info, bill request info
- Expandable sections for records and bills per provider

#### Settlement Sub-tab (`#/matters/{id}/settlement`)
- Settlement Calculator card: Total Recoveries - Legal Fees - Expenses - Liens = Net Client Compensation
- Deduction order display (fees first vs expenses first)
- Recoveries table with Add button
- Legal Fees table with Add button
- Matter Expenses table (read-only, grouped by category from activities)
- Non-Medical Liens table with Add button
- Outstanding Balances table with Add button
- Medical Liens table (read-only, from medical bills)
- Generate Settlement Statement button

### 5. Stages/Kanban View (`#/stages`)
- Practice Area dropdown selector (13 practice areas)
- Kanban board with columns per stage
- Matter cards showing: number, description (truncated), client, days at stage, status color bar
- Card actions via three-dot menu: Switch Practice Area, Mark as Pending/Open, Close Matter

### 6. Settings (`#/settings`)
Sidebar tabs:
- **Practice Areas** (`#/settings/practice-areas`): List with name, stage count, matter count; Add/Edit/Delete; expandable stages per area
- **Matter Templates** (`#/settings/templates`): List with name, practice area, billing method, default indicator; Create/Edit/Delete/Set Default
- **Matter Numbering** (`#/settings/numbering`): Format configuration (auto/manual, padding, separator, client name), starting number, update existing
- **Notifications** (`#/settings/notifications`): Toggle switches for notification types

### 7. Recovery Bin (`#/recovery-bin`)
- Lists deleted matters (6 in seed data)
- Shows: Type, Name/Number, Description, Deleted By, Deleted Date
- Recover button per item
- Info message about 6-month retention policy

## Complete Feature List

### Matter CRUD
- Create matter with all fields
- Edit matter (reopen closed matters first)
- Delete matter (soft-delete to recovery bin)
- Recover deleted matters
- Duplicate matter (creates copy with new number)
- Close matter (sets status to closed, records closedDate)
- Reopen matter (sets status to open)

### Bulk Operations
- Bulk close selected matters
- Bulk delete selected matters
- Bulk update status

### Filtering & Search
- Status filter tabs (All/Open/Pending/Closed)
- Text search across matter number, description, client name
- Practice area filter dropdown
- Responsible attorney filter dropdown
- Billing method filter dropdown
- Active filter chips with clear/remove

### Sorting & Pagination
- Sort by any table column (ascending/descending toggle)
- 25 items per page with prev/next and page number navigation
- Shows count indicator ("Showing 1-25 of 120")

### Export
- CSV export of matters list

### Financial Tracking
- Work in Progress (sum of approved unbilled time entries)
- Outstanding Balance (sum of billed entries)
- Trust Balance per matter
- Budget tracking with progress bar
- Total Time and Total Expenses aggregation

### Personal Injury Features
- Damages tracking (Special, General, Other types)
- Medical provider management with treatment tracking
- Medical record and bill management
- Settlement calculator with deduction order logic
- Recovery amounts with legal fees
- Non-medical liens with reductions
- Outstanding balances (client vs lawyer responsibility)
- Medical liens (auto-populated from medical bills)

### Kanban Stages
- Practice area-based kanban boards (up to 15 stages per area)
- Matter cards with status indicators
- Stage management in settings (create, edit, delete, reorder)

### Templates
- Up to 200 matter templates
- Default template (auto-applied to new matters)
- Template sections: details, billing, custom fields, document folders

### Numbering Scheme
- Configurable format (auto or manual)
- Zero-padded sequential numbers
- Client name appended to number

### Permissions
- Matter visibility: Everyone or Specific Users/Groups
- Block specific users from accessing matters

### Notifications
- Configurable notification types: matter updates, deletions, budget updates, threshold alerts, trust balance

### Data Persistence
- All state persisted to localStorage on every mutation
- State pushed to server via PUT /api/state on every change
- Seed data version stamp for cache invalidation
- SSE-based reset listener for evaluation harness

## Data Model

### Matters (120 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique ID (e.g., 'matter_1') |
| number | string | Zero-padded number (e.g., '00001') |
| displayNumber | string | Formatted display (e.g., '00001-Patterson') |
| description | string | Full case description |
| status | string | 'open', 'pending', or 'closed' |
| billingMethod | string | 'hourly', 'contingency', or 'flat_rate' |
| clientId | string | FK to contacts |
| responsibleAttorneyId | string | FK to users |
| originatingAttorneyId | string | FK to users |
| responsibleStaffId | string | FK to users (optional) |
| clientReferenceNumber | string | Internal tracking number |
| location | string | Court/incident location |
| practiceAreaId | string | FK to practice areas |
| stageId | string | FK to stage within practice area |
| openDate | string | Date (YYYY-MM-DD) |
| pendingDate | string | Date or null |
| closedDate | string | Date or null |
| createdDate | string | ISO timestamp |
| templateId | string | FK to templates (optional) |
| permissions | object | { type: 'everyone'|'specific', userIds: [], groupIds: [] } |
| blockedUsers | array | User IDs blocked from this matter |
| relationships | array | [{ contactId, relationship, billRecipient }] |
| customFields | object | Key-value pairs keyed by cf_* IDs |
| billing | object | { billable, method, currency, rates, budget, budgetUsed, trustBalance, minimumTrust, contingencyFee, flatRate } |
| personalInjury | object | { deductionOrder: 'fees_first'|'expenses_first' } or null |
| notifications | array | [{ userId, types: [] }] |
| documentFolders | array | [{ id, name, category }] |
| reports | object | { useFirmSettings, originatingPct, responsiblePct } |
| deleted | boolean | Soft delete flag |

### Contacts (70 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'contact_1' |
| type | string | 'person' or 'company' |
| firstName | string | First name (persons) |
| lastName | string | Last name (persons) |
| companyName | string | Company name (companies) |
| displayName | string | Computed display name |
| email | string | Email address |
| phone | string | Phone number |
| address | string | Full address |
| tags | array | String tags |
| createdAt | string | ISO timestamp |

### Users (16 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'user_1' |
| name | string | Full name |
| email | string | Email |
| role | string | administrator, attorney, associate, paralegal, legal_assistant, of_counsel |
| hourlyRate | number | Dollar rate per hour |
| avatarColor | string | Hex color for avatar circle |

### Groups (6 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'group_1' |
| name | string | Group name |
| userIds | array | User IDs in the group |

### Practice Areas (13 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'pa_1' |
| name | string | Practice area name |
| stages | array | [{ id, name, order }] (3-5 per area) |

### Damages (38 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'dmg_1' |
| matterId | string | FK to matter |
| name | string | Damage description |
| amount | number | Dollar amount |
| type | string | 'special', 'general', or 'other' |

### Medical Providers (12 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'mp_1' |
| matterId | string | FK to matter |
| contactId | string | FK to contact |
| description | string | Provider description |
| firstTreatmentDate | string | Date |
| lastTreatmentDate | string | Date |
| treatmentComplete | boolean | Treatment status |
| recordRequestDate | string | Date |
| recordFollowUpDate | string | Date |
| recordStatus | string | not_requested, requested, received, incomplete, certified |
| billRequestDate | string | Date |
| billFollowUpDate | string | Date |
| billStatus | string | Same options as recordStatus |

### Medical Records (16 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'mr_1' |
| providerId | string | FK to medical provider |
| matterId | string | FK to matter |
| fileName | string | Document file name |
| receivedDate | string | Date |
| startDate | string | Date |
| endDate | string | Date |
| status | string | received or incomplete |
| comments | array | [{ id, userId, text, createdAt }] |

### Medical Bills (16 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'mb_1' |
| providerId | string | FK to medical provider |
| matterId | string | FK to matter |
| fileName | string | Bill document name |
| billDate | string | Date |
| receivedDate | string | Date |
| billAmount | number | Total bill amount |
| adjustment | number | Pre-settlement adjustment |
| payers | array | [{ contactId, amountPaid, isLien }] |
| balanceOwed | number | Remaining balance |
| balanceLien | boolean | Whether balance is a lien |
| outstandingBalance | boolean | Whether balance is outstanding |
| status | string | received or incomplete |

### Settlements (6 matters have settlement data)
Per-matter structure:
| Field | Type | Description |
|-------|------|-------------|
| recoveries | array | [{ id, sourceContactId, sourceName, amount }] |
| legalFees | array | [{ id, recoveryId, recipientId, rate, discount, referralFees }] |
| nonMedicalLiens | array | [{ id, holderContactId, description, amount, reduction }] |
| outstandingBalances | array | [{ id, responsibility, holderContactId, description, balanceOwing, reduction }] |

### Time Entries (208 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'te_1' |
| matterId | string | FK to matter |
| userId | string | FK to user |
| date | string | Date |
| hours | number | Hours worked |
| rate | number | Hourly rate |
| description | string | Entry description |
| billable | boolean | Whether billable |
| status | string | draft, pending, approved, billed |

### Expenses (85 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'exp_1' |
| matterId | string | FK to matter |
| userId | string | FK to user |
| date | string | Date |
| amount | number | Dollar amount |
| category | string | Expense category |
| description | string | Expense description |
| billable | boolean | Whether billable |

### Matter Templates (7 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'template_1' |
| name | string | Template name |
| isDefault | boolean | Whether default template |
| description | string | Template description |
| practiceAreaId | string | FK to practice area |
| billable | boolean | Default billable setting |
| billingMethod | string | Default billing method |
| deductionOrder | string | Default deduction order |
| customFields | object | Default custom field values |
| documentFolders | array | Default folder structure |

### Custom Field Definitions (12 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'cf_1' |
| name | string | Field display name |
| type | string | text, date, currency, number, dropdown, checkbox |
| required | boolean | Whether required |

### Activity Log (155 records)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'log_1' |
| matterId | string | FK to matter |
| userId | string | FK to user |
| action | string | created, edited, status_changed, stage_changed, etc. |
| entityType | string | matter, damage, provider, etc. |
| entityId | string | FK to affected entity |
| details | string | Human-readable description |
| timestamp | string | ISO timestamp |

### Deleted Matters (6 records, in Recovery Bin)
| Field | Type | Description |
|-------|------|-------------|
| id | string | e.g., 'del_matter_1' |
| originalMatterId | string | Original matter ID |
| number | string | Matter number |
| displayNumber | string | Formatted display number |
| description | string | Matter description |
| clientName | string | Client name |
| deletedBy | string | User ID who deleted |
| deletedAt | string | ISO timestamp |
| type | string | Always 'matter' |

### Numbering Scheme
| Field | Type | Description |
|-------|------|-------------|
| format | string | 'auto' or 'manual' |
| template | string | Display format template |
| separator | string | '-' |
| startingNumber | number | First number |
| nextNumber | number | Next available |
| yearDigits | number | 4 |
| numberPadding | number | 5 (zero-padded) |

### Firm Settings
| Field | Type | Description |
|-------|------|-------------|
| name | string | 'Meridian Law Group' |
| defaultTemplateId | string | FK to default template |
| updateMatterNameOnSave | boolean | Auto-update numbering |
| recoveryBinRetentionDays | number | 180 days |
| primaryPracticeAreaId | string | FK to primary practice area |

## Navigation Structure

| Route | View | How to Reach |
|-------|------|-------------|
| `#/matters` | Matters List | Sidebar "Matters" link, default view |
| `#/matters/new` | Create Matter | "+ New Matter" button on list |
| `#/matters/{id}` | Matter Dashboard (Overview) | Click matter number in list |
| `#/matters/{id}/edit` | Edit Matter | "Edit Matter" button on dashboard |
| `#/matters/{id}/damages` | Matter Damages | "Damages" sub-tab on dashboard |
| `#/matters/{id}/medical-records` | Medical Records | "Medical Records" sub-tab |
| `#/matters/{id}/settlement` | Settlement | "Settlement" sub-tab |
| `#/stages` | Kanban Stages | Sidebar "Stages" link |
| `#/settings` | Settings | Sidebar "Settings" link |
| `#/settings/practice-areas` | Practice Areas Settings | Settings sidebar tab |
| `#/settings/templates` | Templates Settings | Settings sidebar tab |
| `#/settings/numbering` | Numbering Settings | Settings sidebar tab |
| `#/settings/notifications` | Notifications Settings | Settings sidebar tab |
| `#/recovery-bin` | Recovery Bin | Sidebar "Recovery Bin" link |

## Available Form Controls

### Dropdowns (all custom, no native `<select>`)
- **Status**: Open, Pending, Closed
- **Client**: 70 contacts (searchable)
- **Responsible Attorney**: 16 users (searchable)
- **Originating Attorney**: 16 users (searchable)
- **Responsible Staff**: 16 users (searchable)
- **Practice Area**: 13 practice areas
- **Template**: 7 matter templates
- **Billing Method**: Hourly, Contingency Fee, Flat Rate
- **Currency**: USD, CAD, GBP, EUR, AUD
- **Damage Type**: Special, General, Other
- **Record/Bill Status**: Not Yet Requested, Requested, Received, Incomplete, Certified
- **Treatment Status**: In Treatment, Treatment Complete
- **Relationship Type**: 15 options (Spouse, Parent, Child, Sibling, Guardian, Employer, Co-defendant, Witness, Expert Witness, Insurance Adjuster, Opposing Party, Opposing Counsel, Medical Provider, Caretaker, Other)
- **Outstanding Balance Responsibility**: Client, Lawyer
- **Sort order**: various per context
- **Practice Area** (stages view): 13 options

### Toggles
- Billable (matter billing preferences)
- Use Firm Settings (reports)
- Update Matter Name on Save (numbering)
- Update Existing Matters (numbering)
- Notification types (5 toggles)

### Text Inputs
- Description (textarea)
- Client Reference Number
- Location
- Open Date (YYYY-MM-DD format)
- Budget amount
- Minimum Trust Balance
- Contingency percentage
- Flat rate amount
- Custom field values (text, date, currency types)
- Damage name and amount
- Recovery amount
- Legal fee rate and discount
- Lien amount and reduction
- Balance amount and reduction
- Practice area name
- Stage name
- Template name
- Starting matter number
- Number padding

### Checkboxes
- Row selection (matters list)
- Select all (matters list header)
- Bill recipient (related contacts)
- Include client name in number (numbering)

### Radio Buttons
- Permissions: Everyone / Specific Users or Groups
- Deduction order: Fees first / Expenses first

## Seed Data Summary

### Firm: Meridian Law Group

### Users (16)
| Name | Role | Rate |
|------|------|------|
| Sarah Chen (current user) | Administrator | $350/hr |
| Marcus Williams | Attorney | $425/hr |
| Diana Reyes | Attorney | $475/hr |
| Thomas O'Brien | Of Counsel | $550/hr |
| Priya Sharma | Associate | $275/hr |
| Kevin Nakamura | Associate | $250/hr |
| Lisa Tran | Paralegal | $150/hr |
| Robert Jackson | Attorney | $400/hr |
| Angela Martinez | Paralegal | $145/hr |
| David Kim | Associate | $285/hr |
| Jennifer Walsh | Legal Assistant | $125/hr |
| Michael Foster | Attorney | $450/hr |
| Rachel Goldstein | Of Counsel | $525/hr |
| James Cooper | Associate | $260/hr |
| Carlos Mendez | Associate | $270/hr |
| Natalie Park | Attorney | $410/hr |

### Groups (6)
- Litigation Team, Corporate Group, Family Law Team, Criminal Defense Team, PI Team, Administrative Staff

### Practice Areas (13) with stages
- Personal Injury (5 stages: Intake, Investigation, Demand, Litigation, Settlement/Trial) - 26 matters
- Family Law (4 stages) - 15 matters
- Criminal Defense (4 stages) - 13 matters
- Corporate/Business Law (4 stages) - 13 matters
- Real Estate (3 stages) - 9 matters
- Employment Law (4 stages) - 9 matters
- Estate Planning (3 stages) - 7 matters
- Immigration (4 stages) - 7 matters
- Medical Malpractice (4 stages) - 5 matters
- Intellectual Property (4 stages) - 5 matters
- Bankruptcy (3 stages) - 4 matters
- Tax Law (3 stages) - 4 matters
- Environmental Law (3 stages) - 3 matters

### Contacts (70)
Mix of person and company types with diverse names, phone numbers, emails, addresses across US cities. Includes clients, medical providers, opposing parties, insurance companies, and related individuals.

### Matter Templates (7)
1. Personal Injury - Auto Accident [DEFAULT]
2. Personal Injury - Slip and Fall
3. Family Law - Divorce
4. Criminal Defense - General
5. Corporate - Formation
6. Real Estate - Purchase
7. Employment - Discrimination

### Custom Field Definitions (12)
Court Case Number, Opposing Counsel, Statute of Limitations, Insurance Company, Policy Limit, Judge Assigned, Jurisdiction, Case Value Estimate, Referring Attorney, Conflict Check Date, Priority Level, Notes

### Matters (120)
- 78 Open, 27 Pending, 18 Closed
- 65 Hourly, 38 Contingency, 24 Flat Rate
- Distributed across all 13 practice areas
- Dates spanning 2024-2026
- Realistic legal case descriptions (e.g., "Patterson v. Metro Transit Authority - Bus accident resulting in back injury")
- Various budget amounts ($0 to $500K+)
- Some with restricted permissions and blocked users

### Supporting Data
- 38 damages records (for PI matters) - mix of Special, General, Other
- 12 medical providers with treatment tracking
- 16 medical records, 16 medical bills
- 6 settlement records with recoveries, fees, liens
- 208 time entries across matters
- 85 expense entries in 15 categories
- 155 activity log entries
- 6 deleted matters in recovery bin

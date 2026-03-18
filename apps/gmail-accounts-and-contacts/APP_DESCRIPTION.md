# Gmail Accounts & Contacts

## Summary

A web application replicating Google Contacts and Gmail account management features, including contact management (CRUD, labels, search, star/unstar), email delegation, linked Google services management (EU DMA compliance), import/export, merge suggestions, and account settings (login security, privacy, sync, notifications). Built as a single-page app with a sidebar-based navigation system.

## Main Sections/Pages

1. **Contacts** (default view) - Contact list with table view, search, sort, filter, pagination
2. **Frequently Contacted** - Filtered view of frequently-used contacts
3. **Starred** - Filtered view of starred contacts
4. **Other Contacts** - Auto-saved contacts from email interactions
5. **Merge & Fix** - Duplicate contact merge suggestions
6. **Import & Export** - Import/export contacts in CSV and vCard formats
7. **Delegates** - Email delegation management
8. **Linked Services** - DMA-compliant Google service linking
9. **Settings** - Five tabs: General, Account, Privacy, Notifications, Sync & Google Sync

## Implemented Features and UI Interactions

### Contact Management
- View contacts in a table layout with columns: Name, Email, Phone, Company, Labels
- Create new contacts via modal form (first name, last name, email, phone, company, job title, address, secondary email/phone, birthday, website, notes, labels)
- Edit existing contacts via modal form
- Delete contacts with confirmation dialog
- Star/unstar contacts (toggle)
- Search contacts by name, email, company, phone, or job title
- Sort contacts by first name, last name, email, company, or last updated date
- Toggle sort direction (ascending/descending)
- Pagination (25 contacts per page)
- Contact detail panel (right side) showing all fields, labels, edit history, metadata

### Contact Labels
- 12 pre-defined labels: Family, Friends, Work, VIP Clients, Gym Buddies, College Alumni, Neighbors, Book Club, Vendors, Emergency, Travel Contacts, Healthcare
- Create new labels with name and color picker (18 colors)
- Edit label name and color
- Delete labels
- Filter contacts by label (sidebar click)
- Add/remove labels from contacts via detail panel or edit form
- Label chips displayed in contact table rows

### Other Contacts (Auto-saved)
- View auto-saved contacts from email interactions
- Move other contacts to main contacts (person_add)
- Delete other contacts
- Sorted by last interaction date

### Merge & Fix
- Duplicate contact merge suggestions (e.g., same company)
- Merge contacts (combines data from secondary into primary)
- Dismiss merge suggestions

### Delegation
- View delegates with status badges (active, pending, expired)
- Add new delegates via modal (email + name)
- Remove delegates with confirmation dialog
- Maximum 10 delegates (configurable)
- Info cards explaining delegation permissions and activation timeline

### Linked Services (DMA)
- 7 linkable services: Google Search, YouTube, Google Ads, Google Play, Chrome, Google Shopping, Google Maps
- Toggle link/unlink for each service
- 15 always-linked services displayed (locked, cannot unlink)
- Info box about data sharing policies

### Import & Export
- Import area (drag-and-drop style, CSV/vCard)
- Export with format dropdown: Google CSV, Outlook CSV, vCard
- Export scope: All contacts, Starred, By label
- Import/export history list with status badges

### Settings
#### General Tab
- Contact sort order (first name / last name)
- Name display order (first-last / last-first)
- Auto-save contacts toggle
- Collaboration settings: Share Google Docs in email, Show contact info on emails

#### Account Tab
- Profile card with avatar
- Editable fields: Name, Phone, Recovery email, Recovery phone
- Alternate emails display (read-only)
- Login & security: Remember password, Auto sign-in, Two-factor authentication toggle
- 2FA method dropdown: Authenticator app, SMS, Security key (conditional on 2FA enabled)

#### Privacy Tab
- Profile photo visibility: Everyone, Contacts only, Nobody
- Email visibility: Everyone, Contacts only, Nobody
- Phone number visibility: Everyone, Contacts only, Nobody
- Activity tracking toggle

#### Notifications Tab
- Delegate activity notifications
- Contact changes notifications
- Security alerts notifications
- Linked service updates notifications

#### Sync & Google Sync Tab
- Google Sync deprecation warning banner
- Contacts sync toggle
- Calendar sync toggle
- Email sync toggle
- Google Sync transition instructions (iOS/iPad steps)
- "I have transitioned off Google Sync" acknowledgment toggle

### Global UI
- Top bar with logo, search bar, help, settings, profile avatar
- Collapsible sidebar with navigation
- Custom dropdown menus (no native select elements)
- Toggle switches for all boolean settings
- Toast notifications (success, error, warning, info)
- Confirmation dialogs for destructive actions
- Empty states with icons and action buttons

## Data Model

### Contact
- `id` (string, e.g., "contact_01")
- `firstName`, `lastName` (strings)
- `email` (string, primary email)
- `phone` (string)
- `company` (string)
- `jobTitle` (string)
- `address` (string)
- `secondaryEmail`, `secondaryPhone` (strings)
- `birthday` (string, "YYYY-MM-DD")
- `website` (string)
- `notes` (string)
- `labels` (string[], label IDs like "clabel_1")
- `isStarred` (boolean)
- `avatarColor` (string, hex color)
- `createdAt`, `updatedAt` (ISO timestamps)
- `source` (string: "manual", "auto", "auto-promoted")

### Other Contact (auto-saved)
- `id` (string, e.g., "other_01")
- `firstName`, `lastName` (strings, often empty)
- `email` (string)
- `name` (string, display name)
- `source` ("auto")
- `savedAt` (ISO timestamp)
- `interactionCount` (number)
- `lastInteraction` (ISO timestamp)

### Contact Label
- `id` (string, e.g., "clabel_1")
- `name` (string)
- `color` (string, hex color)
- `contactCount` (number, auto-calculated)

### Delegate
- `id` (string, e.g., "delegate_1")
- `email` (string)
- `name` (string)
- `status` (string: "active", "pending", "expired")
- `addedAt` (ISO timestamp)
- `activatedAt` (ISO timestamp or null)
- `permissions` (object: readEmail, sendEmail, deleteEmail, manageChat, changePassword - all booleans)

### Linked Service
- `id` (string, e.g., "svc_1")
- `name` (string)
- `icon` (string, Material Icons name)
- `isLinked` (boolean)
- `category` (string: "core", "advertising", "commerce")
- `description` (string)

### Always Linked Service
- `id` (string, e.g., "asvc_1")
- `name` (string)
- `description` (string)

### Current User
- `id`, `name`, `email` (strings)
- `alternateEmails` (string[])
- `phone` (string)
- `avatarColor` (string)
- `recoveryEmail`, `recoveryPhone` (strings)
- `language`, `timezone` (strings)
- `createdAt`, `lastLogin` (ISO timestamps)

### Account Settings
- `autoSaveContacts` (boolean)
- `contactsSortBy` (string: "firstName" or "lastName")
- `contactsDisplayOrder` (string: "firstLast" or "lastFirst")
- `loginSettings` (object): rememberPassword, autoSignIn, twoFactorEnabled (booleans); twoFactorMethod (string: "authenticator", "sms", "security_key"); recoveryEmailVerified, recoveryPhoneVerified (booleans)
- `syncSettings` (object): googleSyncEnabled, googleSyncDeprecationAcknowledged, contactsSync, calendarSync, emailSync (booleans)
- `collaborationSettings` (object): allowDelegates (boolean), maxDelegates (number), shareDocsInEmail, showContactInfo (booleans)
- `privacySettings` (object): showProfilePhoto, showEmail, showPhone (strings: "everyone", "contacts_only", "nobody"); activityTracking (boolean)
- `notificationSettings` (object): delegateActivity, contactChanges, securityAlerts, linkedServiceUpdates (booleans)

### Contact History
- `id` (string)
- `contactId` (string)
- `action` (string: "created", "edited", "label_added", "label_removed")
- `field` (string or null)
- `oldValue`, `newValue` (string or null)
- `timestamp` (ISO timestamp)
- `actor` (string, email)

### Import/Export History
- `id` (string)
- `type` (string: "import" or "export")
- `format` (string: "CSV", "Google CSV", "Outlook CSV", "vCard")
- `fileName` (string)
- `count` (number)
- `timestamp` (ISO timestamp)
- `status` (string: "completed")

### Merge Suggestion
- `id` (string)
- `contacts` (string[], contact IDs)
- `reason` (string)
- `dismissed` (boolean)

## Navigation Structure

- **Sidebar** (always visible, collapsible):
  - Create contact button
  - Contacts (default)
  - Frequently contacted
  - Starred
  - Other contacts
  - Merge & fix
  - Labels section (12 labels with counts, each clickable to filter)
  - Import & Export
  - Delegates
  - Linked Services
  - Settings
- **Top bar**: Menu toggle, brand logo, global search, help, settings shortcut, profile avatar
- Contact detail panel opens on the right when a contact is selected (contacts view only)

## Available Form Controls

### Dropdowns
- Sort by: First name, Last name, Email, Company, Last updated
- Export format: Google CSV, Outlook CSV, vCard
- Contact sort setting: First name, Last name
- Name display order: First name first, Last name first
- 2FA method: Authenticator app, Text message (SMS), Security key
- Privacy - photo visibility: Everyone, Contacts only, Nobody
- Privacy - email visibility: Everyone, Contacts only, Nobody
- Privacy - phone visibility: Everyone, Contacts only, Nobody

### Toggles
- Auto-save contacts
- Share Google Docs in email
- Show contact info on emails
- Remember password
- Auto sign-in
- Two-factor authentication
- Activity tracking
- Delegate activity notifications
- Contact changes notifications
- Security alerts notifications
- Linked service updates notifications
- Contacts sync
- Calendar sync
- Email sync
- Google Sync deprecation acknowledged
- Linked service toggles (7 services)

### Buttons
- Create contact
- Create label
- Add a delegate
- Save changes (profile)
- Export contacts
- Merge contacts
- Dismiss merge suggestion
- Delete label
- Remove delegate

## Seed Data Summary

### Current User
- Alex Johnson (alex.johnson@gmail.com) with alternate emails a.johnson@workplace.io and alexj.dev@gmail.com

### Contacts (40 total)
- 24 professional contacts: Sarah Chen (TechCorp VP), Marcus Williams (DesignHub Creative Director), Emily Rodriguez (StartupVentures Managing Partner), James O'Brien (Morrison & Associates Senior Partner), Priya Sharma (CloudNine Lead Backend Engineer), David Kim (FinancePlus CFO), and others across various companies and roles
- 4 family contacts: Margaret Johnson (mom), Richard Johnson (dad), Laura Johnson-Martinez (sister), Leo Martinez (brother-in-law)
- 4 healthcare/services: Dr. Patricia Nguyen, Mike Chen (dentist), Greg Hoffman (financial advisor), Diana Castillo (yoga instructor)
- 8 friends/social: Jake Morrison, Samantha Lee, Chris Evans, Ben Walker, Yuki Tanaka, Tony Russo, and others
- Starred contacts: Sarah Chen, Marcus Williams, Emily Rodriguez, Priya Sharma, Kevin Zhao, Maya Patel, Margaret Johnson, Richard Johnson, Laura Johnson-Martinez, Jake Morrison

### Other Contacts (20 total)
- Mix of service emails (support@vercel.com, billing@aws.amazon.com, noreply@github.com) and personal contacts (Jason Blake, Tina Marshall, Alex Rivera, etc.)
- Interaction counts ranging from 1 to 55

### Contact Labels (12)
- Family (#EA4335), Friends (#34A853), Work (#4285F4), VIP Clients (#FBBC04), Gym Buddies (#FF6D01), College Alumni (#9C27B0), Neighbors (#009688), Book Club (#795548), Vendors (#607D8B), Emergency (#F44336), Travel Contacts (#00BCD4), Healthcare (#E91E63)

### Delegates (4)
- Maya Patel (active since Jun 2025)
- Laura Johnson-Martinez (active since Dec 2024)
- Priya Sharma (pending, added Mar 5, 2026)
- Jake Morrison (expired, added Feb 20, 2026)

### Linked Services (7 linkable)
- Linked: Google Search, YouTube, Google Play, Chrome, Google Maps
- Unlinked: Google Ads, Google Shopping

### Always Linked Services (15)
- Google Contacts, Android Services, Google Drive, Gmail, Google Calendar, Google Photos, Google Keep, Google Meet, Google Chat, Google Docs, Google Sheets, Google Slides, Google Translate, Google Assistant, Google Fit

### Account Settings Defaults
- Auto-save contacts: enabled
- Two-factor auth: enabled (authenticator app)
- Remember password: enabled
- Auto sign-in: enabled
- Contacts/Calendar/Email sync: all enabled
- Google Sync deprecated: acknowledged
- Privacy: Profile photo (everyone), Email (contacts only), Phone (nobody)
- Notifications: Delegate activity and security alerts enabled; contact changes disabled

### Import/Export History (4 entries)
- 2 imports (Outlook CSV 2020, iPhone vCard 2024)
- 2 exports (Google CSV 2025, vCard 2026)

### Merge Suggestions (2)
- Priya Sharma + Raj Kapoor (same company: CloudNine)
- Sophie Laurent + Elena Volkov (same company: EuroDesign)

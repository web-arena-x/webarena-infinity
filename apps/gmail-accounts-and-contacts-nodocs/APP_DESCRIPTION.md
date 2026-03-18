# Gmail — Accounts & Contacts

## Summary

A faithful replica of the Gmail Accounts and Contacts management area. The app covers account settings (profile, security, app passwords), email alias management (Send Mail As), delegation, mail import/export, a full contacts manager with labels/groups, merge duplicate contacts, an auto-saved "Other Contacts" list, and an organization directory. All data persists via localStorage and syncs to the server on every mutation.

## Main Sections / Pages

| Section | Route (hash) | Description |
|---|---|---|
| Contacts (All) | `#/contacts` | Paginated, searchable, sortable contact list with multi-select |
| Contacts (Starred) | `#/contacts` (filter=starred) | Starred contacts filter |
| Contacts (by Label) | `#/contacts` (filter=grp_*) | Contacts filtered by a specific label/group |
| Contact Detail | `#/contact/{id}` | Full contact information display |
| New Contact | `#/new-contact` | Create contact form |
| Edit Contact | `#/edit-contact/{id}` | Edit contact form |
| Group Detail | `#/group/{id}` | View contacts in a specific label, with remove option |
| Merge Duplicates | `#/merge-duplicates` | Find and merge potential duplicate contacts |
| Other Contacts | `#/other-contacts` | Auto-saved contacts from email interactions |
| Directory | `#/directory` | Organization directory (TechCorp colleagues) |
| Account Settings | `#/account` | Profile info, recovery options, password, 2FA, app passwords |
| Send Mail As | `#/send-mail-as` | Email aliases and reply-from settings |
| Delegation | `#/delegation` | Email delegates management |
| Import/Export | `#/import-export` | POP3 mail import and contacts export |

## Implemented Features & UI Interactions

### Contacts Manager
- View all contacts in a paginated table (25 per page)
- Search contacts by name, email, company, phone, or job title
- Sort contacts by first name, last name, email, or recently added (custom dropdown)
- Filter contacts by label (sidebar navigation) or starred
- Star/unstar contacts (click star icon)
- Select multiple contacts via checkboxes
- Select all on current page via header checkbox
- Bulk add selected contacts to label(s) via modal
- Bulk delete selected contacts with confirmation
- Create new contact with form fields: first name, last name, email, phone, company, job title, address, birthday, notes, label checkboxes
- Edit existing contact (same form, pre-populated)
- Delete contact with confirmation dialog
- View contact detail page showing all info, labels, notes, and metadata

### Merge Duplicate Contacts
- Accessible via "Merge duplicates" button on the contacts list
- Finds potential duplicates by: same email address, same full name, or same last name + same company
- Displays pairs side-by-side with matching reason badge
- Shows key fields (phone, company, job title) for each contact in the pair
- "Keep this" button on each side: keeps the selected contact, merges empty fields from the other, removes the duplicate
- Groups from the merged contact are added to the kept contact

### Contact Labels/Groups
- View labels in sidebar with member counts
- Create new label via modal (+ button in sidebar)
- Rename label via modal
- Delete label with confirmation (contacts are preserved)
- View contacts within a specific label
- Remove individual contact from a label
- Add contacts to labels via bulk action or contact edit form

### Other Contacts
- View auto-saved contacts from email interactions
- Search other contacts by name or email
- See interaction count and last interaction time
- Promote an other contact to main contacts list
- Delete an other contact

### Directory
- View organization directory (TechCorp employees)
- Search directory by name, email, department, or title
- See department, title, and location for each colleague

### Account Settings
- View profile (name, email) with avatar
- Edit name via modal (first name, last name)
- Edit recovery email via modal
- Edit recovery phone via modal
- Change password via modal (current, new, confirm; minimum 8 chars validation)
- Toggle 2-Step Verification on/off
- View app passwords list with creation date and last used
- Generate new app password via modal (app name required)
- Revoke (delete) app password with confirmation

### Send Mail As (Aliases)
- View list of email aliases (primary, default, SMTP info)
- Set reply-from behavior: always default address vs. same address message was sent to (radio buttons)
- Set default "From" address for any alias
- Add new email alias via modal (name, email, SMTP server, port, username, SSL toggle)
- Edit existing alias via modal
- Remove alias with confirmation (primary cannot be removed; if default is removed, primary becomes default)

### Email Delegation
- View list of delegates with name, email, and status (active/pending)
- Add delegate via modal (email, optional name; status starts as "pending")
- Remove delegate with confirmation

### Import/Export
- View list of POP3 import accounts with status, server details, label, last checked
- Add new POP3 import account via modal (email, server, port, username, label, SSL toggle, leave-on-server toggle)
- Remove import account with confirmation
- Export contacts: choose format (Google CSV / Outlook CSV / vCard) and scope (all / starred) via radio buttons
- Export triggers browser file download

## Data Model

### Entities and Fields

**currentUser** (single object)
- `id`, `firstName`, `lastName`, `email`, `recoveryEmail`, `recoveryPhone`, `profilePhoto`, `twoStepVerification` (boolean), `lastPasswordChange` (ISO timestamp), `createdAt`

**contacts** (array, 120 seed records)
- `id` (ct_1..ct_120), `firstName`, `lastName`, `email`, `phone`, `company`, `jobTitle`, `address`, `birthday` (YYYY-MM-DD), `notes`, `starred` (boolean), `groups` (array of group IDs), `createdAt`, `updatedAt`

**contactGroups** (array, 10 seed records)
- `id` (grp_1..grp_10), `name`, `system` (boolean), `createdAt`, `updatedAt`

**aliases** (array, 4 seed records)
- `id` (alias_1..alias_4), `name`, `email`, `isPrimary` (boolean), `isDefault` (boolean), `replyFrom` ("default"|"alias"), `smtpServer`, `smtpPort`, `smtpUsername`, `useSSL` (boolean), `createdAt`

**delegates** (array, 3 seed records)
- `id` (del_1..del_3), `email`, `name`, `status` ("active"|"pending"), `addedAt`

**importAccounts** (array, 2 seed records)
- `id` (imp_1..imp_2), `email`, `server`, `port`, `username`, `useSSL` (boolean), `leaveOnServer` (boolean), `labelIncoming`, `status` ("active"|"error"), `lastChecked`, `errorMessage` (optional), `addedAt`

**otherContacts** (array, 25 seed records)
- `id` (oc_1..oc_25), `firstName`, `lastName`, `email`, `lastInteraction` (ISO timestamp), `interactionCount` (number)

**directory** (array, 25 seed records)
- `id` (dir_1..dir_25), `name`, `email`, `department`, `title`, `location`, `phone`, `manager`

**appPasswords** (array, 3 seed records)
- `id` (ap_1..ap_3), `name`, `createdAt`, `lastUsed`

**replyFromSetting** (string: "default" | "same")

### Relationships
- contacts ↔ contactGroups: many-to-many via `contact.groups[]` array of group IDs
- delegates reference TechCorp employees by email
- directory entries correspond to some contacts (same email addresses)
- importAccounts are independent entities

## Navigation Structure

**Sidebar sections:**
1. **Contacts** — "All Contacts", "Starred", then Labels (each contact group with count)
2. **Other** — "Other contacts", "Directory"
3. **Settings** — "Account", "Send mail as", "Delegation", "Import/Export"

Clicking a sidebar item navigates via hash routing. Contact rows in the table are clickable to go to detail. Breadcrumbs provide back navigation. The "Merge duplicates" button on the contact list navigates to the merge view.

## Available Form Controls

### Dropdowns (custom, not native `<select>`)
- **Sort contacts:** First name, Last name, Email, Recently added

### Toggle switches
- SSL toggle (alias form, import form)
- Leave on server toggle (import form)
- 2-Step Verification toggle (account settings)

### Radio buttons
- Reply-from setting: "Always reply from default address" / "Reply from same address"
- Export format: Google CSV / Outlook CSV / vCard
- Export scope: All contacts / Starred contacts

### Checkboxes
- Contact selection (per row + select all)
- Label assignment in contact form (one checkbox per label)
- Bulk add-to-label modal (one checkbox per label)

### Text inputs
- Contact fields: first name, last name, email, phone, company, job title, address, birthday (text, YYYY-MM-DD), notes (textarea)
- Search inputs: contacts, other contacts, directory
- Account: name, recovery email, recovery phone, password fields
- Alias: name, email, SMTP server, port, username
- Delegate: email, name
- Import: email, server, port, username, label
- App password: name

## Seed Data Summary

### Contacts (120 total)
- **Family (grp_1):** David Chen, Linda Chen, Kevin Chen, Amy Chen-Wu, Robert Chen, Diane Chen, Laura Chen-Watkins, Stanley Chen (8 members)
- **Work (grp_2):** James Wu, Priya Sharma, Alex Martinez, Mei Zhang, Tom O'Brien, Nina Patel, Marcus Johnson, Lisa Kim, Ryan Nguyen, Hannah Cohen, Diana Ross-Taylor, Carlos Mendoza, Sophia Andersson, Alicia Hernandez, Megan Foster-Kim, Kira Volkov (16 members)
- **Friends (grp_3):** Jake Morrison, Emma Thompson, Liam O'Sullivan, Aisha Rahman, Ben Watkins, Max Wellington, Samantha Park-Williams, Nora Eriksson, Laura Chen-Watkins, Monica Reyes, Karen White, Frank Dubois (12 members)
- **Engineering Team (grp_4):** James Wu, Priya Sharma, Alex Martinez, Mei Zhang, Tom O'Brien, Nina Patel, Marcus Johnson, Ryan Nguyen, Philip Okonkwo, Damian Kowalczyk, Kira Volkov (11 members)
- **Investors (grp_5):** Derek Hoffman, Victoria Blackwell, Hiroshi Tanaka, Catherine Duval, Ibrahim Okafor, Ethan Goldstein (6 members)
- **College Alumni (grp_6):** Jake Morrison, Rachel Park, Derek Hoffman, Mia Santos-Rivera, Tyler Brooks, Zoe Adams, Samantha Park-Williams, Adrian Costa, Alice Nakamura (9 members)
- **Book Club (grp_7):** Ben Watkins, Olivia Grant, Daniel Reeves, Grace Liu (4 members)
- **Conference Contacts (grp_8):** Satoshi Yamamoto, Fatima Al-Hassan, Patrick van der Berg, Ingrid Johansson, Wei Zhao, Elena Petrova, Charlotte Müller, + 25 more international contacts (39 members total)
- **Vendors (grp_9):** Gregory Foster (Datadog), Michelle Torres (Cloudflare), Andrew Blackstone (Snowflake), Jessica Singh (AWS), Samuel Lee (PagerDuty), + 17 more vendor contacts (22 members total)
- **VIP (grp_10):** Marcus Johnson, Diana Ross-Taylor, Derek Hoffman, Victoria Blackwell, Catherine Duval, Satoshi Yamamoto, Douglas Kim, Jessica Singh, Ethan Goldstein, Nicholas Harper (10 members)
- Contacts with no group: Natalie Dubois, Henry Wright, Leah Mitchell, Jasmine Tran, Rebecca Stone, Timothy Buchanan, Sophie Williams, Penny Crawford (8 ungrouped)
- **Starred contacts:** David Chen, Linda Chen, Kevin Chen, James Wu, Priya Sharma, Marcus Johnson, Jake Morrison, Ben Watkins, Derek Hoffman, Victoria Blackwell, Satoshi Yamamoto, Jessica Singh, Ethan Goldstein, Nicholas Harper (14 starred)

### Other Contacts (25)
- Mix of automated services (noreply@github.com, notifications@slack.com), businesses (support@vercel.com), and individuals
- Interaction counts range from 1 to 342
- Last interactions span from Jan 2026 to Mar 2026

### Directory (25 TechCorp employees)
- Departments: Engineering (12), Sales (2), Finance (1), Design (2), Operations (1), HR (1), Legal (1), Marketing (1), Product (1), Customer Support (1), Data Science (1), DevOps (1)
- Locations: San Francisco, Stockholm, New York

### Aliases (4)
- sarah.chen@techcorp.io (primary, default)
- support@techcorp.io (via SMTP)
- schen@alumni.stanford.edu (via SMTP)
- sarah@chen-family.org (via SMTP)

### Delegates (3)
- James Wu (active), Priya Sharma (active), Alex Martinez (pending)

### Import Accounts (2)
- sarahchen.personal@gmail.com (active)
- sarah@old-startup.com (error: server unreachable)

### App Passwords (3)
- Thunderbird on MacBook, Mail on iPhone, Outlook Desktop

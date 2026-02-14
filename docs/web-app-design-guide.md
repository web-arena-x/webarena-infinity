# Project Specification: Documentation-Driven System Replication

## Objective
Reconstruct a web application that reflects the **core operational logic, constraints, and behaviors** described in a selected set of inter-connected, user-facing documentation. The goal is fidelity to documented behavior, not feature completeness of the original system.

## Scope
- **Included**
  - User-facing documentation (guides, how-tos, conceptual explanations)
  - Key workflows, rules, constraints, and system behaviors explicitly or implicitly defined in the documents
- **Excluded**
  - Undocumented features
  - Administrative, internal, or unrelated functionalities from the larger parent project
  - Optimizations or enhancements not supported by documentation

## Guiding Principles
- Documentation is the **source of truth**
- Ambiguities must be **explicitly identified and resolved** via reasonable assumptions
- The resulting system should behave as a **faithful functional replica**, not a visual clone

## System Inputs and Outputs

### Inputs
- A curated set of inter-connected documentation files
    - User actions inferred from documentation (e.g., form submissions, configuration steps, navigation flows)
    - System state variables implied by documented behavior (e.g., user status, configuration state)

### Outputs
- A working web application that:
  - Implements the documented workflows and logic
  - Enforces documented constraints and rules
  - Produces user-visible outcomes consistent with the documentation
- A mapping (implicit or explicit) between:
  - Documentation sections → system features / behaviors
- Clearly documented assumptions for any undefined or ambiguous behavior

## General Principles

### 1. No OS-Level UI Elements

All UI components **must be built using pure HTML, CSS, and JavaScript** to ensure consistent behavior and compatibility with browser automation tools such as Playwright.

#### ❌ Avoid
- Native `<select>` dropdowns (OS-dependent rendering)
- `alert()`, `confirm()`, `prompt()` dialogs
- Native file pickers (`<input type="file">`)
- Native date/time pickers (`<input type="date">`, `<input type="time">`)
- Native color pickers (`<input type="color">`)

#### ✅ Use Instead
- Custom dropdowns built with `<div>`, `<ul>`, `<li>`
- Custom modal dialogs using HTML structure and CSS styling
- Custom file upload UIs (hidden inputs allowed)
- Custom date/time selectors (text inputs or calendar widgets)
- Custom color palettes built with divs or buttons

**Example: Custom Dropdown**
```html
<div class="custom-dropdown">
    <div class="dropdown-trigger">Select option</div>
    <div class="dropdown-menu">
        <div class="dropdown-item">Option 1</div>
        <div class="dropdown-item">Option 2</div>
    </div>
</div>
```

### 2. Rich & Authentic Data

Mock pages must use **realistic, diverse data**, not placeholders. The goal is to reflect real-world complexity.

#### Data Requirements
- **Multiple options**: 5–10+ items per dropdown
- **Varied data**: different formats, types, and statuses
- **Metadata**: IDs, timestamps, descriptions, pricing
- **Real-world patterns**: realistic naming conventions (e.g. `ami-0c02fb55b8d6c2f89`)
- **Edge cases**: long names, special characters, uncommon states

**Example**
```javascript
// ❌ Poor data
const instances = ['t2.micro', 't2.small'];

// ✅ Rich data
const instances = [
    { name: 't2.nano', vcpu: 1, memory: 0.5, price: 0.0058, freeTier: true },
    { name: 't3.micro', vcpu: 2, memory: 1, price: 0.0104, freeTier: true },
    { name: 't3.small', vcpu: 2, memory: 2, price: 0.0208, freeTier: false },
    { name: 'm5.large', vcpu: 2, memory: 8, price: 0.096, freeTier: false }
    // 5+, 10+, or more entries as needed
];
```

### 3. Form Validation & Constraints

Real-world applications enforce validation rules. Mock pages must implement realistic constraints.

#### Validation Types

**A. Required Fields**
- Clearly mark mandatory fields
- Show visual feedback for empty or invalid values
- Disable submission when required fields are missing

**B. Conditional Requirements**
- Field requirements depend on other selections  
- Example: Key pair required for Linux, optional for Windows

**C. Format Validation**
- Email, IP address, and URL formats
- Character limits (min/max length)
- Allowed character sets

**D. Range Validation**
- Numeric min/max values
- Date ranges
- File size limits

**Example**
```javascript
function validateForm() {
    const errors = {};

    if (!state.selectedKeyPair && state.os === 'linux') {
        errors.keyPair = 'Key pair required for Linux instances';
    }

    if (state.storageSize < state.minStorageSize) {
        errors.storage = `Minimum ${state.minStorageSize} GiB required`;
    }

    return Object.keys(errors).length === 0;
}
```

### 4. Field Dependencies

Fields must update dynamically based on related selections.

#### Common Patterns

**A. Parent–Child Relationships**
- VPC → Subnet
- Country → State → City
- Category → Subcategory

**B. Configuration Dependencies**
- OS → Minimum storage
- Architecture → Instance compatibility
- Region → Pricing

**C. Conditional Visibility**
- Show/hide sections dynamically
- Enable/disable fields based on prerequisites
- Display warnings for risky combinations

**Example**
```javascript
function onVPCChange(vpcId) {
    const subnets = getSubnetsForVPC(vpcId);
    updateSubnetDropdown(subnets);

    if (subnets.length > 0) {
        selectSubnet(subnets[0]);
    }
}

function onOSChange(os) {
    const config = osConfig[os];
    state.minStorageSize = config.minStorage;

    if (state.currentStorage < config.minStorage) {
        state.currentStorage = config.minStorage;
        updateStorageInput(config.minStorage);
    }
}
```

### 5. Real-Time Validation

Validation should occur as users interact, not only on submit.

#### Triggers
- **On input**: text fields (with debouncing if needed)
- **On change**: dropdowns, checkboxes, radios
- **On blur**: emails, URLs
- **On dependency change**: related field updates

**Submit Button State**
```javascript
function updateSubmitButton() {
    const isValid = validateForm();
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.disabled = !isValid;
    submitBtn.style.opacity = isValid ? '1' : '0.5';
    submitBtn.style.cursor = isValid ? 'pointer' : 'not-allowed';
}
```

### 6. Visual Feedback

Provide immediate and clear feedback for all interactions.

#### Validation States
```css
.field-error {
    border-color: #d13212 !important;
}

.error-message {
    color: #d13212;
    font-size: 12px;
    margin-top: 4px;
}
```

#### Message Types
```html
<div class="info-box">ℹ️ Helpful tip</div>
<div class="warning-box">⚠️ Warning message</div>
<div class="error-box">❌ Error message</div>
<div class="success-box">✓ Success message</div>
```

### 7. State Management

Maintain a centralized application state for complex interactions.

```javascript
const appState = {
    selectedOS: 'amazon-linux',
    selectedInstanceType: 't3.micro',
    selectedVPC: 'vpc-default',

    minStorageSize: 8,
    maxInstances: 100,

    validationErrors: {},
    expandedSections: [],
    modalOpen: false
};
```

### 8. Accessibility & Testability

Design for both humans and automation tools.

#### Best Practices
- Semantic IDs (e.g. `instanceTypeDropdown`)
- `data-testid` attributes
- Predictable class naming
- Keyboard navigation
- ARIA labels (recommended)

```html
<button
    id="launchInstanceBtn"
    data-testid="launch-button"
    aria-label="Launch instance">
    Launch instance
</button>
```

### 9. Modal Dialogs

Use custom modals for confirmations, forms, and alerts.

```html
<div class="modal-overlay" id="confirmModal">
    <div class="modal">
        <div class="modal-header">
            <h2>Confirm Action</h2>
            <button onclick="closeModal('confirmModal')">×</button>
        </div>
        <div class="modal-body"></div>
        <div class="modal-footer">
            <button onclick="closeModal('confirmModal')">Cancel</button>
            <button onclick="confirmAction()">Confirm</button>
        </div>
    </div>
</div>
```

### 10. Data Persistence

All application data **must persist across page reloads** using browser-local storage (`localStorage`). The application must not lose user-created or user-modified data on refresh, navigation, or tab closure.

#### Requirements
- **Persist on every mutation**: Any operation that changes application state (create, update, delete) must save the updated state to `localStorage`
- **Load on startup**: On page load, the application must check for saved state in `localStorage` and restore it. If no saved state exists, fall back to the initial seed data
- **Seed data as default**: The hardcoded mock data serves as the initial seed. Once the user makes any change, the persisted version takes precedence
- **Reset capability**: Provide a mechanism to clear persisted state and restore the original seed data
- **Serialization safety**: Data must survive JSON round-tripping. Objects referenced by identity (e.g., role constants) must be compared by value (e.g., `.level`, `.name`), not by reference. See "Structured Data Serialization" below for details
- **Notify on every mutation path**: Every code path that modifies state must trigger persistence — not just centralized mutation methods but also inline handlers (e.g., toggling a boolean on `currentUser`). A missed persistence call means external verifiers see stale data

#### What to Persist
- All entity collections (users, groups, projects, organizations)
- All relationship data (memberships, shares)
- Auto-increment ID counters
- Current user profile state

#### What NOT to Persist
- Transient UI state (open modals, current route, toast messages, sidebar state)
- Computed/derived data (inherited memberships, ancestor chains)

#### Seed Data Versioning

When seed data changes (e.g., fixing permissions, adding entities), browsers with stale `localStorage` will load outdated state and ignore the updated seed data. This causes subtle, hard-to-diagnose failures — for example, a permission that was added to seed data won't take effect because the browser is still using the old persisted state.

To prevent this, the application must implement a **seed data version stamp**:

1. Define a version constant (e.g., `SEED_DATA_VERSION = 2`) in the seed data module. Bump it whenever seed data changes.
2. Include the version in the seed data object returned by the seed loader.
3. On startup, when loading persisted state from `localStorage`, compare the stored version against the current `SEED_DATA_VERSION`. If they differ, discard the stale `localStorage` and fall back to fresh seed data.
4. Include the version in the persistable state object so that newly persisted state carries the current version stamp.

```javascript
// In seed data module
const SEED_DATA_VERSION = 2;

// Loading persisted data
function loadPersistedData() {
    const saved = localStorage.getItem('appState');
    if (!saved) return null;
    const parsed = JSON.parse(saved);
    if (parsed._seedVersion !== SEED_DATA_VERSION) {
        localStorage.removeItem('appState');
        return null; // falls back to fresh seed data
    }
    return parsed;
}
```

**Example**
```javascript
function saveState() {
    const persistable = {
        users: appState.users,
        groups: appState.groups,
        projects: appState.projects,
        // ... other entity collections
        _nextId: appState._nextId
    };
    localStorage.setItem('appState', JSON.stringify(persistable));
}

function loadState() {
    const saved = localStorage.getItem('appState');
    if (saved) {
        const parsed = JSON.parse(saved);
        Object.assign(appState, parsed);
    }
}
```

### 11. Structured Data Serialization

When state objects contain **nested references** (e.g., enum-like constants, configuration objects), the serialized (JSON) representation preserves the full structure. External consumers of the API (verifiers, tests, integrations) must account for this.

#### The Problem

```javascript
// Roles defined as structured objects:
const ROLES = {
    OWNER: { id: 50, name: 'Owner', level: 50 },
    DEVELOPER: { id: 30, name: 'Developer', level: 30 },
};

// A record references the object:
{ userId: 1, role: ROLES.OWNER, ... }
```

When serialized to JSON, `role` becomes `{"id": 50, "name": "Owner", "level": 50}` — **not** the string `"Owner"`. Any external code comparing `role == "Owner"` will always fail.

#### The Rule

**Never compare structured fields against plain strings.** Always dereference to the primitive value:

```python
# Correct
record["role"]["name"] == "Owner"
record.get("maxRole", {}).get("name") == "Reporter"

# Wrong — always False after serialization
record["role"] == "Owner"
```

This applies to any field that stores an object reference rather than a scalar value.

### 12. Implementation Checklist

- [ ] Replace native UI elements with custom components  
- [ ] Populate realistic, diverse data  
- [ ] Implement all validation rules  
- [ ] Add field dependencies and cascading updates  
- [ ] Enable real-time validation  
- [ ] Manage submit button state  
- [ ] Use info/warning/error messages appropriately  
- [ ] Implement custom modals  
- [ ] Add descriptive IDs and test selectors  
- [ ] Verify compatibility with Playwright  
- [ ] Ensure no OS-level UI remains
- [ ] Persist all data to `localStorage` on every mutation
- [ ] Restore persisted state on page load
- [ ] Provide a reset-to-seed-data mechanism
- [ ] Every inline state mutation calls the persistence/notify function
- [ ] External consumers (verifiers, tests) dereference structured objects — never compare to strings
- [ ] Seed data has a version stamp; persisted state is invalidated when seed data changes
- [ ] Dropdown labels use human-readable display names, not internal paths or slugs
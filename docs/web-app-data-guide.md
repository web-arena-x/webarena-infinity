# Data Requirements

Mock data must simulate real-world scale, distribution, relationships, and historical depth — not just variety. The goal is to replicate how production systems feel and behave under realistic data conditions.

---

## 1. Sufficient Volume & Density

Avoid minimal datasets. Real systems rarely contain only a handful of records.

### Minimum Volume Expectations (Guideline)

- Lists (emails, projects, tickets, users, orders): 100–1,000+ records
- Dropdown options: 5–20+ entries
- Nested/related entities: multiple layers deep
- Activity logs/history: dozens to hundreds of entries
- Notifications/messages: varied timestamps across time

The UI must demonstrate:

- Pagination or infinite scrolling
- Filtering across large datasets
- Sorting by multiple dimensions
- Search returning partial matches across many results

A dataset with 3 records is a demo. A dataset with 437 records across 12 categories feels real.

---

## 2. Realistic Distribution (Not Uniform)

Real-world data is unevenly distributed.

### Avoid

- Equal counts in every category
- Perfectly spaced timestamps
- All entities having identical metadata

### Instead

- Some categories heavy, others sparse
- Bursts of activity (e.g., 20 events in one hour, none for 2 days)
- Mixture of:
  - Active records
  - Stale records
  - Archived records
  - Failed or error states

Example patterns:

- 60% active, 25% inactive, 10% pending, 5% failed
- 70% of records created within last 30 days, 30% older
- A few extremely large or edge-case items among mostly normal ones

---

## 3. Realistic Metadata

Each entity should include multiple attributes reflecting real systems.

### Include

- Unique IDs (UUIDs or realistic internal IDs)
- Creation timestamps
- Last-updated timestamps
- Status fields
- Owner/creator references
- Tags/labels/categories
- Optional descriptive fields
- Boolean flags (archived, starred, pinned, verified)
- Version numbers where appropriate

Example structure:

{
    id: "msg_9f3a2c81",
    createdAt: "2026-02-14T08:21:33Z",
    updatedAt: "2026-02-14T09:05:02Z",
    status: "unread",
    category: "primary",
    tags: ["finance", "invoice"],
    priority: "high",
    sizeKB: 248,
    hasAttachments: true
}

Entities must feel operational, not decorative.

---

## 4. Relational Integrity

Data must reflect relationships between entities.

### Examples of Relationships

- User → Projects → Tasks
- Organization → Members → Roles
- Folder → Messages
- Order → Line Items → Products
- Account → Permissions → Resources

Relationships must:

- Reference valid existing entities
- Reflect consistent state (no orphaned records unless intentionally testing errors)
- Enforce documented constraints (e.g., role levels, ownership limits)

Include:

- Many-to-many relationships
- Parent-child hierarchies
- Cross-linked references
- Shared or collaborative ownership

---

## 5. Historical Depth

Systems evolve over time. Mock data must simulate temporal history.

### Include

- Older records with legacy statuses
- Renamed entities
- Completed workflows
- Cancelled operations
- Reopened items
- Edited content
- Audit logs or activity trails

Example:

history: [
    { action: "created", timestamp: "...", actorId: 12 },
    { action: "status_changed", from: "pending", to: "approved", timestamp: "...", actorId: 7 },
    { action: "edited", field: "description", timestamp: "...", actorId: 12 }
]

A system without history feels artificial.

---

## 6. Edge Cases & Outliers

Include abnormal but realistic data.

### Examples

- Extremely long names
- Special characters
- Missing optional fields
- Very large numbers
- Very small numbers
- Zero values
- Maximum allowed values
- Rare states
- Near-expiry timestamps
- Duplicate display names but unique IDs

The UI must gracefully handle:

- Overflow text
- Empty states
- Maximum constraints
- Validation boundaries

---

## 7. State Diversity

Not all records should be in the ideal state.

Include:

- Draft
- Pending approval
- Rejected
- Suspended
- Archived
- Soft-deleted
- Flagged
- Expired
- Locked
- Conflict states

Systems must reflect lifecycle progression.

---

## 8. Search & Filtering Realism

Search must return:

- Exact matches
- Partial matches
- Cross-field matches (if documented)
- Overlapping results

Filters should meaningfully reduce large datasets.

### Avoid

- Filters that only match 1–2 items
- Search that always returns perfect results

### Include

- Cases with no results
- Cases with many results
- Overlapping filter combinations

---

## 9. Cross-User & Permission Variation

If the system involves users or roles:

- Different users must have different data visibility
- Ownership must affect permissions
- Role-based restrictions must impact available actions
- Shared items must reflect collaboration

Data must include:

- Private records
- Shared records
- Organization-level records
- Restricted content

---

## 10. Realistic Naming Conventions

Use domain-consistent naming patterns:

- IDs: usr_10294, proj_88421, inv_2026_00012
- Slugs: enterprise-onboarding-q1
- Emails: alex.morgan@company.io
- Tags: lowercase, hyphenated
- Versions: v1.2.4
- SKUs: PRO-ENT-2026

### Avoid

- item1
- testUser
- abc123

---

## 11. Performance Simulation Awareness

Large datasets should expose:

- Loading states
- Pagination UI
- Batch operations
- Count indicators (e.g., "1–50 of 842")
- Lazy rendering patterns (if implemented)

The system must appear capable of operating at scale.

---

## 12. Data Evolution Compatibility

Mock data must:

- Survive JSON serialization
- Maintain referential consistency
- Include versioning if seed data changes
- Avoid relying on object reference identity
- Use stable IDs for relationships

---

# Final Principle

The dataset should be large enough, varied enough, and interconnected enough that removing 90% of it would noticeably degrade realism.

If a tester can immediately see that the system is powered by 10 handcrafted records, the realism requirement has failed.
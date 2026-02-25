# 360 Reporting (Project)

Source: https://v2.support.procore.com/product-manuals/reports-project/permissions-360-reporting-360-reports

---

Table of Contents

## 360 Reports

Procore's 360 Reporting tools require two separate permission layers to access **360 Reports**:

1. Permissions to **create and manage reports.**
2. Permissions to **access reporting data.**

### 1. Permissions to Create and Manage Reports

Learn which user permissions are required to take the described actions in this tool.

| | The action is available on Procore's Web, iOS, and/or Android application.

Users can take the action with this permission level.

Users can take this action with this permission level AND one or more additional requirements, like [granular permissions](/faq-what-are-permissions-in-procore-and-how-do-they-work).

| General Tasks | None | Read Only | Standard | Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| Configure Advanced Settings  Web |  |  |  |  | Users must have 'Admin' level permissions to the **Project or Company Directory** tool to take this action. |
| Copy Report  Web |  |  |  |  |  |
| Create a Calculated Column  Web |  |  |  |  |  |
| Create a Report  Web |  |  |  |  |  |
| Create a Report Using a Template  Web |  |  |  |  |  |
| Create a User Activity Report  Web |  |  |  |  | Users must have 'Admin' level permissions to the **Project or Company Directory** tool to take this action. |
| Delete a Report  Web |  |  |  |  |  |
| Distribute Report  Web |  |  |  |  |  |
| Edit a Report  Web |  |  |  |  |  |
| Export a Report  Web |  |  |  |  |  |
| Promote a Project Report to the Company Level  Web |  |  |  |  | Users must have 'Admin' level permissions to the **Company Directory** to perform this action. |
| Share a Report  Web |  |  |  |  |  |
| View a Report  Web |  |  |  |  |  |

### 2. Permissions for Data Access

You need the following permissions levels in the source tool to view the relevant data:

### Action Plans

Permissions**Show/Hide Details**

| Data Field Group | Action Plans Tool Permissions | Notes |
| --- | --- | --- |
| Action Plan | Admin | None |
| Action Plan Approver | Admin | None |
| Action Plan Completed Receiver | Admin | None |
| Action Plan Line Item | Admin | None |
| Action Plan Line Item Assignee | Admin | None |
| Action Plan Line Item Record | Admin | None |
| Action Plan Line Item Record Request | Admin | None |
| Action Plan Line Item Reference | Admin | None |

### Admin

Permissions**Show/Hide Details**

| Data Field Group | Project Admin Tool Permissions | Notes |
| --- | --- | --- |
| Project | Read Only, Standard, Admin | None |
| Project Distribution Group | Read Only, Standard, Admin | None |
| Project Note | Read Only, Standard, Admin | None |
| Project Permissions | Read Only, Standard, Admin | None |
| Project Task | Read Only, Standard, Admin | None |
| Project Roles | Read Only, Standard, Admin | None |

### Bidding

Permissions**Show/Hide Details**

| Data Field Group | Bidding Tool Permissions | Notes |
| --- | --- | --- |
| Bid | Read Only | None |
| Bid Form | Read Only | None |
| Bid Item | Read Only | None |
| Bid Package | Read Only | None |
| Bid Vendor | Read Only | None |

### Budget

Permissions**Show/Hide Details**

| Data Field Group | Budget Tool Permissions | Notes |
| --- | --- | --- |
| Actual Production Quantities | Read Only, Standard, Admin | **Part of Labor Productivity**. Data Field Group is also supported with source tool permissions on the **Timesheets** tool. |
| Budget Change | Read Only, Standard, Admin | Requires **ERP Integrations** to see ERP status fields |
| Budget Change Workflow Steps & Assignment Duration | Read Only | Requires Company **Workflows** |
| Budget Change Adjustment Line Item | Read Only, Standard, Admin | None |
| Budget Code | None, Read Only, Standard, Admin | **This is a structural attribute**.   There isn't a single, direct permission setting. Visibility is contextual to the projects on which you have been granted source tool access. |
| Budget Forecast Line Item | Read Only, Standard, Admin | None |
| Budget Line Item | Read Only, Standard, Admin | None |
| Budgeted Production Quantities | Read Only, Standard, Admin | **Part of Labor Productivity**. Data Field Group is also supported with source tool permissions on the **Timesheets** tool. |
| ERP Job Costs Summary | Read Only, Standard, Admin | Requires **ERP Integrations** |
| Labor Productivity | Read Only, Standard, Admin | **Part of Labor Productivity**. Data Field Group is also supported with source tool permissions on the **Timesheets** tool. |
| Monitored Resource | Read Only, Standard, Admin | None |

### Change Events

Permissions**Show/Hide Details**

| Data Field Group | Change Events Tool Permissions | Notes |
| --- | --- | --- |
| Change Event | Read Only, Standard, Admin | None |
| Change Event Line Item | Read Only, Standard, Admin | None |
| Change Event Production Quantity | Read Only, Standard, Admin | None |

### Commitments

Permissions**Show/Hide Details**

| Data Field Group | Commitments Tool Permissions | Notes |
| --- | --- | --- |
| Commitment | Admin | None |
| Commitment Change Order | Admin | Requires **Change Management** |
| Commitment Change Order Line Item | Admin | Requires **Change Management** |
| Commitment Change Order Markup | Admin | Requires **Change Management** |
| Commitment Change Order Request | Admin | Requires **Change Management** |
| Commitment Line Item | Admin | None |
| Commitment Potential Change Order | Admin | Requires **Change Management** |
| Commitment Workflow Responses | Admin | Requires Company **Workflows** |
| Request for Quote | Read Only, Standard, Admin | None |
| Request for Quote Quote | Read Only, Standard, Admin | None |
| Request for Quote Response | Read Only | None |
| Subcontractor Invoice | Admin | Requires **Invoice Management**. |
| Subcontractor Invoice Line Item | Admin | Requires **Invoice Management**. |

### Coordination Issues

Permissions**Show/Hide Details**

| Data Field Group | Coordination Issues Tool Permissions |
| --- | --- |
| Coordination Issue | Read Only |

### Correspondence

*Note:* Super Private correspondences are excluded.

Permissions**Show/Hide Details**

| Data Field Group | Correspondence Tool Permissions | Notes |
| --- | --- | --- |
| Correspondence | Admin | **Access Granted by Correspondence Type (e.g., Delay Notice, RFI).**  Users with 'Admin' permissions for a specific Correspondence Type can view all of that type's items.  Note that Super Private correspondence is never included in 360 Reports. |
| Correspondence Assignee | Admin | **Access Granted by Correspondence Type (e.g., Delay Notice, RFI).**  Users with 'Admin' permissions for a specific Correspondence Type can view all of that type's items.  Note that Super Private correspondence is never included in 360 Reports. |
| Correspondence Distribution List | Admin | **Access Granted by Correspondence Type (e.g., Delay Notice, RFI).**  Users with 'Admin' permissions for a specific Correspondence Type can view all of that type's items.  Note that Super Private correspondence is never included in 360 Reports. |
| Correspondence Response | Admin | **Access Granted by Correspondence Type (e.g., Delay Notice, RFI).**  Users with 'Admin' permissions for a specific Correspondence Type can view all of that type's items.  Note that Super Private correspondence is never included in 360 Reports. |
| Correspondence Schedule Task | Read Only | **Access Granted by Correspondence Type (e.g., Delay Notice, RFI).**  Users with 'Admin' permissions for a specific Correspondence Type can view all of that type's items.  Note that Super Private correspondence is never included in 360 Reports. |

### Crews

Permissions**Show/Hide Details**

| Data Field Group | Crews Tool Permissions | Notes |
| --- | --- | --- |
| Crew | Read Only | None |

### Daily Log

Permissions**Show/Hide Details**

| Data Field Group | Daily Log Tool Permissions | Notes |
| --- | --- | --- |
| Daily Log Accident | Admin | None |
| Daily Log Completion | Admin | None |
| Daily Log Construction Report | Admin | None |
| Daily Log Delay | Admin | None |
| Daily Log Delivery | Admin | None |
| Daily Log Dumpster | Admin | None |
| Daily Log Equipment | Admin | None |
| Daily Log Inspection | Admin | None |
| Daily Log Manpower | Admin | None |
| Daily Log Note | Admin | None |
| Daily Log Observed Weather Condition | Admin | None |
| Daily Log Phone Call | Admin | None |
| Daily Log Plan Revision | Admin | None |
| Daily Log Productivity | Admin | None |
| Daily Log Quantity | Admin | None |
| Daily Log Safety Violation | Admin | None |
| Daily Log Scheduled Work | Admin | None |
| Daily Log Scheduled Work Task | Admin | None |
| Daily Log Visitor | Admin | None |
| Daily Log Waste | Admin | None |

### Direct Costs

Permissions**Show/Hide Details**

| Data Field Group | Direct Costs Tool Permissions | Notes |
| --- | --- | --- |
| Direct Cost | Read Only | None |
| Direct Cost Line Item | Read Only | None |

### Directory

Permissions**Show/Hide Details**

| Data Field Group | Directory Tool Permissions | Notes |
| --- | --- | --- |
| Company (Vendor) - Used in Company 360 Reporting | None, Read Only, Standard, Admin | **Data is contextual.**  The data you see depends on the report you are running and your project access permissions.  **Example**: If you have permission to 'Project ABC' you will see vendor data for 'Project ABC' |
| Company (Vendor) - Used in Project 360 Reporting | None, Read Only, Standard, Admin | **Data is contextual.**  The data you see depends on the report you are running and your project access permissions.  **Example**: If you have permission to 'Project ABC' you will see vendor data for 'Project ABC' |
| Company Comments | Read Only, Standard, Admin | None |
| Company Global Insurance | Read Only, Standard, Admin | None |
| Company Project Insurance | Read Only, Standard, Admin | None |
| Contact | Read Only, Standard, Admin | None |
| Employees | Read Only | **Data is contextual.**  The data you see depends on the report you are running and your project access permissions.  **Example**: If you have permission to 'Project ABC' you will see vendor data for 'Project ABC' |
| User | Read Only, Standard, Admin | **Data is contextual.**  The data you see depends on the report you are running and your project access permissions.  **Example**: If you have permission to 'Project ABC' you will see vendor data for 'Project ABC' |

### Documents

Permissions**Show/Hide Details**

| Data Field Group | Documents Tool Permission | Notes |
| --- | --- | --- |
| Company Folder/Document | Admin | Also requires 'Admin' level permissions on the Company Directory. |
| Folder/Document | Admin | Also requires 'Admin' level permissions on the Company Directory. |
| Folder/Document Watcher | Admin | Also requires 'Admin' level permissions on the Company Directory. |

### Drawings

Permissions**Show/Hide Details**

| Data Field Group | Drawings Tool Permissions | Notes |
| --- | --- | --- |
| Drawing | Admin | None |
| Drawing Markup Link | Admin | None |

### Estimating

Permissions**Show/Hide Details**

| Data Field Group | Estimating Tool Permissions | Notes |
| --- | --- | --- |
| Estimate | Read Only, Standard, Admin | None |
| Estimate Adjustment | Read Only, Standard, Admin | None |
| Estimate Budget Included Item | Read Only, Standard, Admin | None |
| Estimate Budget Item | Read Only, Standard, Admin | None |
| Estimate Layer | Read Only, Standard, Admin | None |
| Estimate Layer Group | Read Only, Standard, Admin | None |
| Estimating Project | Read Only, Standard, Admin | None |

### Forms

Permissions**Show/Hide Details**

| Data Field Group | Forms Tool Permissions | Notes |
| --- | --- | --- |
| Form | Admin | None |

### Incidents

Permissions**Show/Hide Details**

| Data Field Group | Incidents Tool Permissions | Notes |
| --- | --- | --- |
| Incident | Admin | None |
| Incident Action | Admin | None |
| Incident Alert | Admin | None |
| Incident Distribution Member | Admin | None |
| Incident Injury Body Part | Admin | None |
| Incident Record | Admin | None |

### Inspections

Permissions**Show/Hide Details**

| Data Field Group | Inspections Tool Permissions | Notes |
| --- | --- | --- |
| Inspection | Admin | None |
| Inspection Assignee | Admin | None |
| Inspection Distribution List | Admin | None |
| Inspection Item | Admin | None |
| Inspection Item Activity | Admin | None |
| Inspection Item Comment | Admin | None |
| Inspection Item Reference | Admin | None |
| Inspection Item Signature Request | Admin | None |
| Inspection Schedule | Admin | None |
| Inspection Schedule Assignee | Admin | None |
| Inspection Schedule Distribution List | Admin | None |
| Inspection Signature Request | Admin | None |

### Instructions

Permissions**Show/Hide Details**

| Data Field Group | Instructions Tool Permissions | Notes |
| --- | --- | --- |
| Instruction | Admin | None |

### Meetings

Permissions**Show/Hide Details**

| Data Field Group | Meetings Tool Permissions | Notes |
| --- | --- | --- |
| Meeting | Admin | None |
| Meeting Attendee | Admin | None |
| Meeting Item | Admin | None |
| Meeting Item Assignee | Admin | None |
| Meeting Item Attendee | Admin | None |

### Observations

Permissions**Show/Hide Details**

| Data Field Group | Observations Tool Permissions | Notes |
| --- | --- | --- |
| Observation | Admin | None |
| Observation Activity | Admin | None |
| Observation Distribution Member | Admin | None |

### Payments

Permissions**Show/Hide Details**

| Data Field Group | Payments Tool Permissions | Notes |
| --- | --- | --- |
| Contract Compliance | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Disbursement | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Early Pay Enrollment | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Lien Waiver | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Manual Holds | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Beneficiary | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Invite | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Issued | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Permissions | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Project Controls | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Received | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Payment Required Settings | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Subtier Lien Waivers | Admin | Requires **Invoice Management** and **Procore Pay**. |
| Subtiers | Admin | Requires **Invoice Management** and **Procore Pay**. |

### Photos

Permissions**Show/Hide Details**

| Data Field Group | Photos Tool Permissions | Notes |
| --- | --- | --- |
| Photo | Admin | None |

### Prime Contracts (Funding/Client Contracts)

Permissions**Show/Hide Details**

| **Data Field Group** | **Source Tool Permissions** | **Notes** |
| --- | --- | --- |
| Owner Invoice | Admin | Requires **Invoice Management**. |
| Owner Invoice Workflow Steps & Assignment Duration | Admin | Requires **Invoice Management** and Company **Workflows**. |
| Owner Invoice Line Item | Admin | Requires **Invoice Management**. |
| Prime Contract | Admin | None |
| Prime Contract Workflow Steps & Assignment Duration | Admin | Requires **Invoice Management** and Company **Workflows**. |
| Prime Contract Change Order | Admin | Requires **Change Management**. |
| Prime Contract Change Order Workflow Steps & Assignment Duration | Admin | Requires **Change Management** and Company **Workflows**. |
| Prime Contract Change Order Line Item | Admin | Requires **Change Management**. |
| Prime Contract Change Order Markup | Admin | Requires **Change Management**. |
| Prime Contract Change Order Request | Admin | Requires **Change Management**. |
| Prime Contract Change Order Workflow Responses | Admin | Requires **Change Management**. |
| Prime Contract Change Order Workflow Steps | Admin | Requires **Change Management**. |
| Prime Contract Line Item | Admin | None |
| Prime Contract Potential Change Order | Admin | Requires **Change Management**. |
| Prime Potential Change Order Production Quantity | Read Only, Standard, Admin | Requires **Change Management**. |

### Punch List

Permissions**Show/Hide Details**

| Data Field Group | Punch List Tool Permissions | Notes |
| --- | --- | --- |
| Punch Item | Admin | None |
| Punch Item Assignee | Admin | None |
| Punch Item Ball In Court | Admin | None |
| Punch Item Comments | Admin | None |
| Punch Item Distribution Member | Admin | None |

### RFIs

Permissions**Show/Hide Details**

| Data Field Group | RFI Tool Permissions | Notes |
| --- | --- | --- |
| RFI Distribution List | Admin | None |
| RFI | Admin | None |
| RFI Assignee | Admin | None |
| RFI Question | Admin | None |
| RFI Response | Admin | None |

### Schedule

Permissions**Show/Hide Details**

| Data Field Group | Schedule Tool Permissions | Notes |
| --- | --- | --- |
| Schedule Calendar Item | Admin | None |
| Schedule Lookahead | Read Only | None |
| Schedule Lookahead Task | Read Only | None |
| Schedule Task | Read Only | None |
| Schedule Task Request | Read Only | None |

### Specifications

Permissions**Show/Hide Details**

| Data Field Group | Specifications Tool Permissions | Notes |
| --- | --- | --- |
| Specifications | Read Only, Standard, Admin | None |

### Submittals

Permissions**Show/Hide Details**

| Data Field Group | Submittals Tool Permissions | Notes |
| --- | --- | --- |
| Submittal | Admin | None |
| Submittal Approver | Admin | None |
| Submittal Ball In Court | Admin | None |
| Submittal Distribution List | Admin | None |

### T&M Tickets

Permissions**Show/Hide Details**

| DataField Group | Tasks Tool Permissions | Notes |
| --- | --- | --- |
| T&M Ticket | Read Only, Standard, Admin | None |
| T&M Ticket Equipment | Read Only, Standard, Admin | None |
| T&M Ticket Labor | Read Only, Standard, Admin | None |
| T&M Ticket Material | Read Only, Standard, Admin | None |

### Tasks

Permissions**Show/Hide Details**

| Data Field Group | Task Tool Permissions | Notes |
| --- | --- | --- |
| Task | Admin | None |
| Task Activity | Admin | None |
| Task Assignee | Admin | None |
| Task Distribution Member | Admin | None |

### Timesheets

Permissions**Show/Hide Details**

| Data Field Group | Timesheets Tool Permissions | Notes |
| --- | --- | --- |
| Actual Production Quantities | Read Only, Standard, Admin | **Part of Labor Productivity**. Data Field Group is also supported with source tool permissions on the **Budget** tool. |
| Budgeted Production Quantities | Read Only, Standard, Admin | **Part of Labor Productivity**. Data Field Group is also supported with source tool permissions on the **Budget** tool. |
| Labor Productivity | Read Only, Standard, Admin | **Part of Labor Productivity**. Data Field Group is also supported with source tool permissions on the **Budget** tool. |
| Timecard Entry | Read Only, Standard, Admin | None |
# What are custom fields and which Procore tools support them? - Procore

Source: https://support.procore.com/faq/what-are-custom-fields-and-which-procore-tools-support-them

---

##### **NOTE: This page is linked in the Procore web app**

**Location**: [https://app.procore.com/11733/compan...ts/383087/edit](https://app.procore.com/11733/company/admin/configurable_field_sets/383087/edit "https://app.procore.com/11733/company/admin/configurable_field_sets/383087/edit")

- Company Admin > Project Settings > Fieldsets > Edit > Learn More

## Answer

Custom fields allow you to add extra, specialized information fields to many Procore project tools. It is important to understand that Procore has two (2) different types of custom fields:

- **Company Level Custom Fields**:

  - Created in the Company Admin Tool.
  - Allow you to add the same custom fields across all projects that use a specific tool.
  - **This FAQ focuses on Company Level custom fields.**
- **Project-Specific Custom Fields**:

  - Created directly in the configuration settings of specific Procore tools on a specific project.
  - Only apply to the single project they were created in.

When you create a Company Level Custom Field, you must define two (2) main properties:

- **Field Type**: This determines the kid of data the field collects (e.g., Plain Text, Number, Checkbox, etc.).
- **Visibility**: This controls how the field behaves for project users. Many fields can also be set to **Required**, **Optional**, or **Hidden**.

##### Tip

**Interested in building a custom app or integration using the Procore API?** Procore's API endpoints respect the custom fields that you create in the Procore web application. All the tools listed in the table below also support custom fields through the API. To learn more, visit the Procore Developers enter at [![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://developers.procore.com/ "https://developers.procore.com/") [developers.procore.com](https://developers.procore.com/ "https://developers.procore.com/"). We also recommend these resources: [![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14) Working with Configurable Fieldsets](https://developers.procore.com/documentation/tutorial-config-fieldsets "https://developers.procore.com/documentation/tutorial-config-fieldsets") and [![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14) List Configurable Field Sets](https://developers.procore.com/reference/rest/v1/configurable-field-sets "https://developers.procore.com/reference/rest/v1/configurable-field-sets").

### Supported Tools

Company Administrators can create custom fields for these Procore tools. For instructions, see [Create New Custom Fields](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-custom-fields "Create New Custom Fields").

##### Note

![icon-mindtouch-table-mobile.png](https://support.procore.com/@api/deki/files/91426/icon-mindtouch-table-mobile.png?revision=1&size=bestfit&width=20&height=20) Indicates custom fields are available when using the Procore mobile app.

| ******Procore Tool****** | ****Fieldset(s)**** | ****Field Limit**** | ****Notes**** |
| --- | --- | --- | --- |
| ******Admin (Project)****** | Project | 15 | One (1) global fieldset for all new and existing projects.  Some fields display on Bid Board. |
| ******Action Plans******  ****icon-mindtouch-table-mobile.png**** | Action Plan Type | 10 | One (1) fieldset per Action Plan Type. |
| ******Change Events****** | Change Events | 10 | Requires Change Management. One (1) fieldset for the Change Events tool. |
| ******Change Orders****** | Change Order | 10 | Requires Change Management. Works with Commitments & Prime Contracts. |
| ******Commitments****** | Purchase Orders, Subcontracts | 30 | One (1) fieldset for each Commitment Type. |
| ******Coordination Issues****** | Procore Default | 10 | One (1) fieldset for the Coordination Issues tool. |
| ******Correspondence******  ****icon-mindtouch-table-mobile.png**** | Correspondence Type | 15 | One (1) fieldset per Correspondence Type. |
| ******Daily Log******  ****icon-mindtouch-table-mobile.png**** | Accident Log, Call Log Daily, Construction Report, Delay Log, Delivery Log, Dumpster Log, Equipment Log, Inspection Log, Manpower Log, Notes Log, Observed Weather Conditions, Plan Revision Log, Productivity Log, Quantity Log, Safety Violation Log, Visitors Log, Waste Log, Work Log | 10 | One (1) fieldset per Daily Log Type. |
| ******Document Management****** | All Fieldsets | 20 |  |
| ******Documents (Project)******  ****icon-mindtouch-table-mobile.png**** | Documents | 10 | Custom fields are always optional (cannot be marked as required). |
| ******Drawings****** | Drawing Revisions | 10 | Data entry is revision-specific. Entries do not carry over to new revisions. |
| ******Equipment****** | Equipment Category | 10 | One (1) fieldset per Equipment Category. |
| ******Incidents******  ****icon-mindtouch-table-mobile.png**** | Incident, Injury/Illness, Property Damage, Environmental, Near Miss, Witness Statement, Action | 15 | One (1) fieldset per Incident Type. |
| ******Inspections******  ****icon-mindtouch-table-mobile.png**** | Unassociated, Quality, Safety, Commissioning, Environmental | 10 | One (1) fieldset per Inspection Type. |
| ******Invoicing / Progress Billings****** | Subcontractor Invoices or Progress Billings | 30 | Tool name may vary by company. See [What tool names and terms are different in Procore for general contractors, owners and specialty contractors?](https://support.procore.com/faq/what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors "What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?") |
| ******My Time******  ****icon-mindtouch-table-mobile.png**** | General Information | 10 | One (1) fieldset for the My Time app. |
| ******Observations******  ****icon-mindtouch-table-mobile.png**** | Commissioning, Environmental, Quality, Safety, Warranty, Work to Complete | 10 | One (1) fieldset per Observation Type. |
| ******Prime Contracts / Client Contracts / Funding****** | Client Contracts, Fundings, or Prime Contracts | 30 | Tool name may vary by company. See [What tool names and terms are different in Procore for general contractors, owners and specialty contractors?](https://support.procore.com/faq/what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors "What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?") |
| ******Punch List******  ****icon-mindtouch-table-mobile.png**** | Punch Item | 10 | One (1) fieldset for the Punch List tool. |
| ******RFIs******  ****icon-mindtouch-table-mobile.png**** | RFI | 10 | One (1) fieldset for the RFIs tool |
| ******Specifications****** | Specification Section Revision | 10 | One (1) fieldset for the Specifications tool. |
| ******Submittals******  ****icon-mindtouch-table-mobile.png**** | Submittal Log | 10 | One (1) fieldset for the Submittals tool. |
| ******T&M Tickets******  ****icon-mindtouch-table-mobile.png**** | General Information, Labor, Materials, Equipment, Subcontractors | 10 | One (1) fieldset for each listed section. |
| ******Timesheets******  ****icon-mindtouch-table-mobile.png**** | General Information | 10 | One (1) fieldset for the Timesheets tool. |

## See Also

- [Create New Custom Fields](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-custom-fields "Create New Custom Fields")
- [What field types are available for Custom Fields in Procore Tools?](https://support.procore.com/faq/what-field-types-are-available-for-custom-fields-in-procore-tools "What field types are available for Custom Fields in Procore Tools?")
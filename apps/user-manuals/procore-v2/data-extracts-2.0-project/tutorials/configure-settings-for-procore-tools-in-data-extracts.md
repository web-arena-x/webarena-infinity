# Configure Settings for Procore Tools in Data Extracts

Source: https://v2.support.procore.com/product-manuals/data-extracts-2.0-project/tutorials/configure-settings-for-procore-tools-in-data-extracts

---

### Background

In the Data Extracts 2.0 tool, you can configure the settings of various Procore tools when creating and editing extracts.

### Things to Consider

- [Required User Permissions](/product-manuals/data-extracts-2.0-project/permissions)
- **Additional Information:**

 - No settings are available for the Directory, Documents, Photos, Change Orders, and Models tools.
 - Attachments associated with the Change Orders tool's items are included in the extract by default.
 - All data for the Models tool is included in the extract by default.

### Configure Settings

You can configure the settings of various Procore tools to specify the exact content you want to include in your extract.

| **Procore Tools** | **Settings** | **Steps** |
| --- | --- | --- |
| Action Plans | Attachments | Select one of these options:   - **Cover Sheet only (Exclude attachments):** Select to include only the cover sheet associated with action plan items in the extract. - **Include attachments as separate files in an Action Plan's folder:** Select to include attachments associated with action plan items as separate files in the extract. - **Merge attachments and records with the Cover Sheet in a single PDF:** Select to merge attachments, records, and cover sheet associated with action plan items into a single PDF in the extract.   *Note:* Attachments associated with action plan items are included as separate files by default. |
| Bidding Change Events Correspondence Emails Forms Incidents Inspections Meetings Prime Contract Invoices Prime Contracts Punch List Purchase Orders Subcontractor Invoices Subcontracts | Include Attachments | Unmark this checkbox if you do not want to include attachments associated with items in the extract. *Note:* By default, this checkbox is selected. |
| Daily Log | Log Status | Select the status of logs to be included in the extract. *Note:* 'Approved' and 'Rejected' statuses are included by default. You can remove them if required. |
| Daily Log | Log Type | Select the type of logs to be included in the extract. *Note:* All log types are included by default. You can remove them if required. |
| Daily Log | Exclude Empty Days | Unmark this checkbox to include days when the daily logs are not completed. *Note:* By default, this checkbox is selected. |
| Daily Log | Include Attachments | Unmark this checkbox to exclude attachments associated with daily log items in the extract. *Note:* By default, this checkbox is selected. |
| Daily Log | Month & Year | Use the **<** and **>** buttons to navigate to the required month and year. *Note:* By default, the current month and year are selected. |
| Daily Log | Today | Click **Today** to view the daily logs starting from today onwards. |
| Drawings | Include Attachments | Unmark this checkbox to exclude attachments associated with items in the extract. *Note:* By default, this checkbox is selected. |
| Drawings | Revision | Select one of these options:   - **Include All:** Select to include all items in the extract. - **Include only Current:** Select to include only the current revision of items in the extract. *Note:* Only the current revision of items is included by default. |
| Submittals | Include Attachments | Unmark this checkbox to exclude attachments associated with items in the extract. *Note:* By default, this checkbox is selected. |
| Submittals | Revision | Select one of these options:   - **Include All:** Select to include all items in the extract. - **Include only Current:** Select to include only the current revision of items in the extract. *Note:* Only the current revision of items is included by default. |
| Observations | Include Attachments | Unmark this checkbox to exclude attachments associated with Observation items in the extract. *Note:* By default, this checkbox is selected. |
| Observations | Include Linked Drawings | Mark this checkbox to include drawings linked with Observation items in the extract. *Note:* Linked drawings are not included by default. |
| RFI | Include Attachments | Unmark this checkbox to exclude attachments associated with RFI items in the extract. *Note:* By default, this checkbox is selected. |
| RFI | Include Official Response Only | Unmark this checkbox to include RFIs regardless of whether they have an official response in the extract. *Note:* By default, this checkbox is selected. |
| Specifications | Revision | Select one of these options:   - **Include All:** Select to include all specifications in the extract. - **Include only Current:** Select to include only the current revision of specifications in the extract. *Note:* Only the current revision of specifications is included by default. |
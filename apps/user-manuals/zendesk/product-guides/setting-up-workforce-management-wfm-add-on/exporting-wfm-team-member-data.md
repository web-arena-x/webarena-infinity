# Exporting WFM team member data

Source: https://support.zendesk.com/hc/en-us/articles/7446311222042-Exporting-WFM-team-member-data

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

The [User management page](https://support.zendesk.com/hc/en-us/articles/7052274669338) in Zendesk Workforce management
(WFM) provides a central place for admins to view their team members’ information, such as
their role, teams, assigned workstreams, and so on. This article describes how admins can
export WFM team-member data to a comma-separated values (CSV) file.

By exporting team member data into a spreadsheet you can analyze your agents
information, pinpoint areas for improvement, or use it as a backup file

This article includes the following sections:

- [Generating an export of WFM team
  members](#topic_ab2_zqr_tbc)
- [WFM team member data included in
  CSV file](#topic_lqk_tds_tbc)

## Generating an export of WFM team members

You can export all team members’ data from the User management page in
Zendesk WFM.

**To generate an export of team members**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **User management**.
2. Click **Export CSV**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_user_mgmt_export.png)

   You’ll receive an email with a link to download your CSV file
   when the export is complete.

## WFM team member data included in CSV file

The following table lists the fields included in the CSV file.

| Data | Description |
| --- | --- |
| WFM ID | The team member’s numeric ID. |
| Name | The team member’s full name. |
| Email | The team member’s primary email address. |
| Role | The team member’s assigned WFM role. For example, Agent. |
| Zendesk Default Group | The team member's [default](https://support.zendesk.com/hc/en-us/articles/4408828237722) group in Zendesk. |
| Teams | The teams the team member is assigned to. |
| Workstreams | The workstreams the team member is assigned to. |
| Location | The team member’s assigned location. The team member can be assigned to only one location. |
| Shift | The team member’s assigned shift. |
| Status | The team member’s WFM status. The value can be either active or inactive. |
| Tracking | If task lock is turned on or off for the team member. Note: You will only see Task lock listed here for users who had this setting activated manually by an admin. Users who have task lock activated via account settings are not listed here. See [Activating task lock](https://support.zendesk.com/hc/en-us/articles/6443329357210). |
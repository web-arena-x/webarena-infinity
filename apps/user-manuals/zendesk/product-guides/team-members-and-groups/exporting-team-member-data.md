# Exporting team-member data

Source: https://support.zendesk.com/hc/en-us/articles/5407034434842-Exporting-team-member-data

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > People > Team > Team members

The [Team members](https://support.zendesk.com/hc/en-us/articles/4408843830938) page in Zendesk Admin Center
provides a central place for administrators to add and manage team members (your staff,
agents, and admins). This article describes how admins can export team-member data to a
CSV file.

Exporting team-member data to a CSV file allows you to manage your team members in a
common format used by many other systems. You might want to use this information to
reconcile your agent seat usage and team structure, or manage licenses.

Activating data exports isn’t required to export team-member data.

Note: Other types of data can be exported if data exports are activated. See [Exporting ticket, user, or organization data from your
account](https://support.zendesk.com/hc/en-us/articles/4408886165402).

This article includes the following sections:

- [Generating an export of team
  members](#topic_ncb_lql_nwb)
- [Team member data included in CSV
  file](#topic_rnz_brl_nwb)

## Generating an export of team members

You can generate an export of all team members’ data from the Team members page in
Admin Center.

**To generate an export of team members**

1. In [Admin
   Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team
   members**.
2. Click the **Actions** menu, then select **Export team
   members**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/team_mbr_export_menu_1.png)

   The export starts to generate.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Export_tm_mmbr_generate_msg.png)

You can continue to work in your account while it generates. Zendesk sends you an
email with a link to download your CSV file when the export is complete.

The length of time to generate the export varies based on the number of team members
in your account and other data in their profiles, such as the length of their names
and email addresses.

## Team member data included in CSV file

The following table lists the fields included in the CSV file.

| Data | Description |
| --- | --- |
| ID | The team member’s numeric ID. |
| Name | The team member’s full name. |
| Email | The team member’s primary email address. |
| Suspended | Displays either TRUE or FALSE depending on whether the team member has been suspended. |
| Date created | The date when the team member’s profile was created. |
| Last updated | The date the team member’s profile was last updated. |
| Last sign-in | The date the team member last signed in. |
| Time zone | The time zone in which the team member is located. |
| Language | The language set in the team member’s profile. |
| Primary Group | The team member's [default](https://support.zendesk.com/hc/en-us/articles/4408828237722) group. |
| Groups | A list of all the groups the team member is part of. Group names are separated by a pipe ( | ). |
| Tags | A list of all tags added to the team member. Tag names are separated by a pipe ( | ). |
| Organization | The organization to which the team member belongs. |
| Notes | Any notes added to the team member’s profile. |
| Details | Additional details added to the team member’s profile. For example, an address. |
| Chat role | The team member's assigned role in live chat or messaging. |
| Explore role | The team member's assigned role in Explore. |
| Guide role | The team member's assigned role in Guide. |
| Support role | The team member's assigned role in Support. |
| Talk role | The team member's assigned role in Talk. |
| Note: All product roles appear in the export. If your account doesn’t have a product or a team member has not been assigned a role in a product, "No role" appears. | |
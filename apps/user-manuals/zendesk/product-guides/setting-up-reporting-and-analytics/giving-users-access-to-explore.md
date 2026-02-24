# Giving users access to Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408836002970-Giving-users-access-to-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

Verified AI summary ◀▼

Admins can manage user access to Explore by assigning roles, allowing you to control who can create, view, or edit reports and dashboards. Depending on your plan, you can use Explore roles or custom roles to tailor access levels. Users can also check their own permissions to understand what data they can access in reports and dashboards.

Admins can control whether a user can access Explore and what they can see and do within it.
For example, you might want some users to be able to create and view reports, and other users
to have view-only access to dashboards.

To control access to Explore, you use roles. The role names and the method you use to
associate them with users depends on your plan.

This article contains the following topics:

- [Understanding Explore access](#topic_r5m_f3z_2tb)
- [Giving or modifying Explore access with Explore roles (Professional only)](#topic_dgk_tkr_sjb)
- [Giving or modifying Explore access with custom roles (Enterprise only)](#topic_ygz_hkr_sjb)
- [Checking your Explore permissions](#topic_c2t_2tj_1cc)

## Understanding Explore access

Whether a Zendesk user has access to Explore by default depends on the plan you have and
the type of user. You can modify or remove access to Explore at any time by following the
steps in this article.

Tip: If you're not sure which Explore plan you have, see
[About the Zendesk Explore plan types](https://support.zendesk.com/hc/en-us/articles/4408823356186) to see which version of
Explore is included with the various Suite plans.

If you have:

- **Explore Lite**, all of your Support users have view-only access to the prebuilt
  dashboards by default.
- **Explore Professional**, default access to Explore depends on the role selected when
  the user was created:
  - **Light agents** in Support have Viewer access in Explore.
  - **Staff** and **Contributors** in Support have no access to Explore and must
    be manually granted access.
  - **Administrators** in Support have Admin access in Explore.
- **Explore Enterprise**, default access to Explore is defined by the user's custom
  role. See [Giving or modifying Explore access
  with custom roles (Enterprise only)](#topic_ygz_hkr_sjb) for details.

Watch the video below for an overview of how a fictitious company uses Explore permissions
to control access to sensitive data between different office locations.

*Explore ticket group permissions (10:29)*

## Giving or modifying Explore access with Explore roles (Professional only)

Note: If you use custom roles in Zendesk Support, see [Giving or modifying Explore access with custom
roles (Enterprise only)](#topic_ygz_hkr_sjb) instead.

Explore roles are configured in Admin Center. You must be a Support administrator
to configure users.

**To give or modify user access to Explore**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Search for and select a user's profile to open it.
3. On the **Roles and access** tab, select the **Access** checkbox next to
   **Analytics**. If you don't enable this checkbox, the user cannot access Explore,
   regardless of any other access settings.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_role_update2.png)
4. In the **Role** drop-down, select the appropriate role:

   | Role | Permissions |
   | --- | --- |
   | Admin | Includes all Editor permissions plus the following:  - Update permissions for datasets (see [Setting Explore dataset   permissions](https://support.zendesk.com/hc/en-us/articles/4408831563802)) - Change default colors for charts and color-encoded metrics - Edit Excel settings when exporting dashboards. This includes column and   tab separators, decimal precision, decimal separator, and thousands   separator - Manage dashboard delivery schedules for all Explore users - View and edit all dashboards across the account, regardless of who the   dashboards were created by or shared with - Configure [dataset exports](https://support.zendesk.com/hc/en-us/articles/6037992005914) |
   | Editor | - Create and customize new dashboards, reports, and datasets - Edit created and shared dashboards, reports, and datasets - Share dashboards with Zendesk users or groups - Set dashboard email delivery schedules (see [Scheduling dashboard deliveries](https://support.zendesk.com/hc/en-us/articles/4408843602714-Sharing-dashboards-through-email)) |
   | Viewer | - View dashboards shared with them - Cannot create reports or dashboards |
5. Click **Save**.

## Giving or modifying Explore access with custom roles (Enterprise only)

If you're on an Enterprise plan, admins configure access to Explore using [custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882). Custom roles let you control access to various
Zendesk products to multiple users simultaneously.

If you apply any of the standard custom roles to any of your users, they will be
automatically granted the following Explore role:

| Support Enterprise custom role | Explore role |
| --- | --- |
| Admin (system) | Manage reports, dashboards and datasets (Admin) |
| Team lead (custom) | Manage reports and dashboards (Editor) |
| Staff (custom) | View dashboards (Viewer) |
| Contributor (system) | View dashboards (Viewer) |
| Advisor (custom) | View dashboards (Viewer) |
| Light agent (system) | View dashboards (Viewer) Note: If you have light agents in your Zendesk instance and assign them the Light agent custom role, they will be able to view any dashboards that have been shared with them (applicable only on [Enterprise plans and Explore Legacy plans](https://support.zendesk.com/hc/en-us/articles/4408823356186)). |
| New custom role | View dashboards (Viewer) |

System roles cannot be customized, but custom roles can. Additionally, you can configure
access to Explore in your own custom roles.

**To configure Explore access permissions in a custom role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. From the list of roles, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) for the custom role you want to
   configure Explore access for and click **Edit**.
3. On the role’s settings page, scroll down to the **Reporting and analytics** section
   and configure the following **Explore** settings as needed:

   |  |  |
   | --- | --- |
   | **Role** | **Permissions** |
   | No access | Cannot access Explore |
   | View dashboards (Viewer) | Data from groups they belong to (Limited viewer)  - View dashboards shared with them   - Can see historical data only for the Support groups that     the user is included in   - Cannot see live data - Cannot create reports or dashboards - Cannot access settings Data from selected groups (Limited viewer)  **Data they can view and report on**  - **Data from brands and groups they belong to:** Restrict access to   only data in brands and groups that the user is part of. - **Data from selected brands and groups:** Opens two menus where you   can select the brands and groups that the user can report on. - **All data:** No brand or group restrictions are applied. - View dashboards shared with them   - Can see historical data only for the Support groups you     specify   - Cannot see live data - Cannot create reports or dashboards - Cannot access settings All data (Full viewer)  - View dashboards shared with them    - Can see historical data for all Support groups   - Can see live data - Cannot create reports or dashboards - Cannot access settings |
   | Manage reports and dashboards (Editor) | Data from groups they belong to (Limited editor)  - Create and customize reports from all datasets   - Can see and work with historical data only for the Support     groups that the user is included in   - Cannot see or work with live data - Cannot share dashboards externally through links, schedule or   receive dashboard deliveries, or create dashboard restrictions - Cannot access settings Data from selected groups (Limited editor)  - Create and customize reports for the Support groups you   specify   - Can see and work with historical data for any dataset they     have permission to   - Cannot see or work with live data - Cannot share dashboards externally through links, schedule or   receive dashboard deliveries, or create dashboard restrictions - Cannot access settings All data (Full editor)  - Create and customize reports from any [dataset they have permissions for](https://support.zendesk.com/hc/en-us/articles/4408831563802)   as well as live data - Create and customize dashboards - Create custom datasets - Edit reports, dashboards, and datasets created by other   users - Share dashboards with Zendesk users or groups - Schedule and receive dashboard deliveries - Create dashboard restrictions |
   | Manage reports, dashboards and dataset permissions (Admin) | Includes all Editor permissions for the All ticket data option, plus the following permissions:  - Update dataset permissions - Change default colors for charts and color-encoded   metrics - Edit Excel settings (including column and tab separators,   decimal precision and separator, and thousands separator) when exporting   dashboards - Manage dashboard delivery schedules for all Explore users |

   Note: Explore doesn't distinguish between private and public ticket groups. Any user
   with "All data" access in Explore can view all private and public ticket groups. You
   can use the limited editor permissions described in this article to restrict ticket
   group visibility for users.
4. Click **Save**.

Now, whenever the custom role is assigned to one or more users, that user will be granted
the Explore access level you configured.

## Checking your Explore permissions

Users with access to Explore can check their own level of access to data within Explore.
This helps you understand what data you can expect to see in reports and dashboards.

**To check your Explore permissions**

1. In Explore, click your profile icon in the top right.
2. Select **Data access**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_checking_your_access.png)

   The **Data you can access** window shows
   you which ticket groups and datasets you currently have access to.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_data_you_can_access_example.png)
# Reporting on the number of Zendesk tickets linked to a Jira issue

Source: https://support.zendesk.com/hc/en-us/articles/10042720591898-Reporting-on-the-number-of-Zendesk-tickets-linked-to-a-Jira-issue

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The integration lets you track the number of support tickets linked to each Jira issue, helping prioritize tasks based on customer demand. Set it up by adding custom fields in Jira to display ticket counts and IDs. This feature updates automatically when tickets are linked or unlinked, providing clear visibility into customer requests related to specific Jira issues.

The Zendesk Support for Jira integration allows Jira issues to be sorted by the number of Zendesk Support tickets linked to each issue. This can help your developers prioritize their work by elevating Jira issues that have a larger number of customers requesting a specific feature or reporting the same bug.

This article includes the following topics:

- [Understanding how linked tickets are reported in Jira](#topic_s4r_mws_3x)
- [Setting up the integration to display linked tickets in Jira](#topic_yfl_vbt_4hc)

## Understanding how linked tickets are reported in Jira

The linked tickets reporting feature lets you track the number of Zendesk tickets linked to each Jira issue, along with their IDs.
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_linked_tickets.png)

To use this feature, custom fields must be added to your Jira projects. The setup process requires a Jira admin to create one or both of these custom fields:

- A paragraph field to list ticket IDs
- A number field to count the number of tickets

Then, the administrator must add one or both of these fields to Jira project pages.
Each of these custom fields can be used independently.

After completing the setup, the feature automatically updates and displays the following information:

- When a ticket is *linked* to a Jira issue, the Zendesk Ticket Count field is incremented by one, and the ticket ID is appended to the Zendesk Ticket IDs field.
- When a ticket is *unlinked* from a Jira issue, the Zendesk Ticket Count field is decreased by one, and its ID is deleted from the Zendesk Ticket IDs field.
- If a Jira instance is linked to multiple Zendesk accounts, a prefix is added to each ticket ID, separated by a dash (-), to identify tickets and avoid ambiguity.

Note: Jira displays these custom fields only when there are tickets linked to a particular Jira issue.

## Setting up the integration to display linked tickets in Jira

Setting up linked tickets in Jira is a two-step process:

- [Turning on linked ticket reporting in Admin Center](#topic_pxh_fbt_4hc)
- [Setting up linked ticket reporting in Jira](#topic_vdl_mbt_4hc)

### Turning on linked ticket reporting in Admin Center

First, turn on linked ticket reporting in Admin Center.

**To turn on linked ticket reporting**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you are setting up.
4. On the Support app tab, select **Turn on linked ticket reporting in Jira**.
5. Click **Save**.

### Setting up linked ticket reporting in Jira

Next, create the custom fields in Jira and add them to your pages.

**To set up the linked tickets reporting feature**

1. In Jira, click the Settings (cog) icon on the upper-right, and select **Issues**.
2. Select **Fields** > **Custom fields** from the left navigation panel.
3. On the Custom fields page, click **Create custom field** in the upper-right corner.
4. On the field type selection page, click **Paragraph**, then click **Next**.
5. On the text field configuration page, enter a name and description for the text field.

   The **Name** field is case-sensitive and must be entered precisely as shown below.

   - **Name:** Zendesk Ticket IDs
   - **Description:** Lists the Zendesk ticket IDs related to the Jira issue in a comma-separated string.
6. Click **Create**.
7. On the next page, use the checkboxes to select which pages the field should appear on, then click **Update**.
8. Click **Add custom field** in the upper right corner.
9. On the field type selection page, select **Number Field**, then click **Next**.
10. On the number field configuration page, enter a name and description for the number field.

    The **Name** field is case-sensitive and must be entered precisely as shown below.

    - **Name:** Zendesk Ticket Count
    - **Description:** Number of Zendesk tickets linked to Jira issue
11. Click **Create**.
12. On the field association page, use the checkboxes to select the pages the number field should appear on, then click **Update**.
13. Confirm the fields are displayed on the correct pages.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/JIRA_setup_zdfields.png)
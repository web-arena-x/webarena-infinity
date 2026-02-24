# Reporting on the number of Zendesk tickets linked to a Jira issue (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408843823642-Reporting-on-the-number-of-Zendesk-tickets-linked-to-a-Jira-issue-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Track the number of support tickets linked to each Jira issue to help prioritize tasks based on customer demand. Set up custom fields in Jira to display ticket IDs and counts. When tickets are linked or unlinked, these fields automatically update, providing a clear view of issue impact.
This feature requires a Jira admin to create and configure the necessary fields.

The Zendesk Support for Jira integration allows Jira issues to be sorted by the number of Zendesk Support tickets linked to each issue. This can help your developers prioritize their work by elevating Jira issues that have a larger number of customers asking for a specific feature, or reporting the same bug.

For information about ticket linking, see [Creating a link to an existing Jira issue from a ticket](https://support.zendesk.com/hc/en-us/articles/4408827996058#topic_thj_3wc_zm).

Related articles:

- [Setting up Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408837969946)
- [Using the Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408827996058)
- [Updating a ticket when the status of a Jira issue changes](https://support.zendesk.com/hc/en-us/articles/4408832025114)

## Setting up linked tickets reporting in Jira

The linked tickets reporting feature allows you to keep track of the number of Zendesk tickets linked to each Jira issue and their IDs.
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_linked_tickets.png)

To enable this feature, custom fields must be added to your Jira projects. The setup process requires a Jira administrator to create one or both of these custom fields:

- A paragraph field, for the list of Zendesk ticket IDs
- A number field, to count the number of ticket IDs

Then, the administrator needs to add one or both of these fields to the screens of the Jira projects. Each of these custom fields can be used independently of the other.

After completing the setup, the feature automatically updates and displays the following information:

- When a Zendesk ticket is *linked* to a Jira issue, the Zendesk Ticket Count field is incremented by one, and its ID is appended to the Zendesk Ticket IDs field.
- When a Zendesk ticket is *unlinked* from a Jira issue, the Zendesk Ticket Count field is decreased by one, and its ID is deleted from the Zendesk Ticket IDs field.

Note: Jira only displays these custom fields if there are tickets linked to a particular Jira issue.

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
7. On the next page, use the checkboxes to select which screens the field should appear on, then click **Update**.
8. Click **Add custom field** in the upper right corner.
9. On the field type selection page, select **Number Field**, then click **Next**.
10. On the number field configuration page, enter a name and description for the number field.

    The **Name** field is case-sensitive and must be entered precisely as shown below.

    - **Name:** Zendesk Ticket Count
    - **Description:** Number of Zendesk tickets linked to Jira issue
11. Click **Create**.
12. On the field association page, use the checkboxes to select the screens the number field should appear on, then click **Update**.
13. Confirm the fields are displayed on the correct screens.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/JIRA_setup_zdfields.png)
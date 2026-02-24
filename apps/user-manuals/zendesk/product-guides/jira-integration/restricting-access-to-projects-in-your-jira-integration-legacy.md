# Restricting access to projects in your Jira integration (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408839373850-Restricting-access-to-projects-in-your-Jira-integration-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By default, all Jira projects are available through the integration.
However, a Jira administrator can restrict access to Jira projects. This feature provides the benefit of limiting access to sensitive information stored in specific Jira projects, and creates a better user experience by only showing relevant projects in the Jira app in Support.

Note: This restriction does not apply to other admin-controlled integration features such as [Jira workflow integration](https://support.zendesk.com/hc/en-us/articles/4408832025114)
and [field syncing](https://support.zendesk.com/hc/en-us/articles/4408825394458).
These features only work on linked tickets and the linking functionality is dependent on project restrictions.

**To restrict a Jira project from appearing in the Jira integration**

1. Log in to your Jira account. You must have admin privileges to make these changes.
2. Click the **Settings** cog, then select **Apps**> **Manage apps** > **Zendesk Support for JIRA** > **Configure**.
3. Click the **Project Restrictions** tab on the left sidebar to open the **Project Restrictions** page.
4. Move your projects into the allowed or restricted groups using the control buttons:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_restrictions.png)
5. Click **Save** to save your changes.

When you save these settings:

- Only allowed projects appear in the project selection when creating an issue in the Jira app in Support:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_restricted_projects.png)
- Only issues in allowed projects appear in search results when linking an issue in the Jira app in Support:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_restricted_issue.png)

Restricting a project does not affect previously linked issues. Issues that have been linked before a project was restricted remain untouched.
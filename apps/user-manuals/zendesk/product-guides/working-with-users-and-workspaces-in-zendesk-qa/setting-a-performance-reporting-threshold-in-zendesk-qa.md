# Setting a performance reporting threshold in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043700991514-Setting-a-performance-reporting-threshold-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Set performance reporting thresholds to monitor customer interactions and ensure agents meet quality standards. Customize thresholds for each workspace, with green indicating scores that meet or exceed the threshold and red for those that don't. Understand the difference between threshold and baseline scores to interpret dashboard color codes accurately. This helps maintain consistent quality assurance across your support operations.

Location:  Zendesk QA > Settings > Users, bots, and workspaces

Admins, account managers, and workspace managers can configure thresholds for each
workspace in Zendesk Quality assurance (QA). These customizable metrics help you monitor
customer interactions to ensure agents are meeting your unique quality standards.

The thresholds defined for your workspaces are displayed on the [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690) with color codes: green for scores that meet or
exceed the threshold, and red for scores that do not.

For example, if your internal key performance indicator (KPI) for quality assurance
is 80%, set the threshold accordingly. Scores below this threshold will appear red on the
dashboard.

This article contains the following topics:

- [Setting the performance reporting
  threshold](#set_threshold)
- [Understanding the
  difference between a threshold and the baseline score](#understanding_threshold_baseline)

**Related articles**

- [Accessing and viewing the Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690)
- [Understanding the pass rate in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043668650266)

## Setting the performance reporting threshold

Thresholds are configured for workspaces. All review scores within a workspace are
evaluated against the threshold.

**To set the threshold for a workspace**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner, then select **Users, bots, and workspaces**.
2. Under **Workspaces**, click the name of the workspace you want to manage
   the threshold for.
3. Click **Threshold**.
4. Adjust the **Threshold** slider to set the desired value for the workspace.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_workspace_threshold.png)

When you view the [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690) for this workspace, the colors will reflect your
KPIs.

## Understanding the difference between a threshold and the baseline score

You may notice different colors between the Score and the Pass/Fail columns in dashboards and
cards because they are color-coded based on different metrics.

The colors in the Pass/Fail column are based on the [pass rate baseline score](https://support.zendesk.com/hc/en-us/articles/7043668650266), while the colors in the Score column
reflect the workspace threshold on the [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690). If the threshold you configure is the same as
the baseline score, the color-coding in the Score and Pass/Fail columns will match. However,
when the values are different, you can see a score displayed with a green background while
the corresponding Pass/Fail value is displayed with a red background, or vice versa.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_scores_by_reviews.png)
# Getting started with Zendesk Explore: Hands-on tutorial

Source: https://support.zendesk.com/hc/en-us/articles/4408824320794-Getting-started-with-Zendesk-Explore-Hands-on-tutorial

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you’ll use what you've learned in the [getting started guide](https://support.zendesk.com/hc/en-us/articles/4408831710618-Getting-started-with-Zendesk-Explore) to create and share a simple Zendesk Explore dashboard that reflects a common business scenario.

This dashboard shows the following information:

1. For each agent in your organization, show the number of tickets assigned to them.
2. Give the ability to filter the tickets by status. For example, for a selected agent, show only their tickets in a solved state.

Tip: These steps are an introduction to the basic workflow of creating and sharing a dashboard. However, we encourage you to experiment. If you want to choose different metrics and attributes, change the chart type, or wonder what an option does, try it!

If you need more help with anything you find, take a look at the [Zendesk Explore resources](https://support.zendesk.com/hc/en-us/articles/4408846357018-Zendesk-Explore-resources)
article.

This article contains the following sections:

- [Before you start](#topic_acg_3qd_t2b)
- [Step 1: Create a report](#topic_uqw_jvd_t2b)
- [Step 2: Create a dashboard](#topic_qtr_nvd_t2b)
- [Step 3: Share your dashboard](#topic_ztf_pvd_t2b)
- [Next steps](#topic_jnj_rvd_t2b)

## Before you start

Before you can complete this walkthrough, ensure that:

- Zendesk Support contains ticket and agent data. While Explore integrates with all Zendesk channels, for this example, you'll use the **Support:
 Tickets** dataset. If you are just starting with Zendesk, the reports you generate might not show much data for the first few days.
- Your user account is set up to use Explore. Additionally, ensure you have the **Admin** or **Editor** user role. For more information, see [Adding users to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970-Adding-users-to-Explore).

## Step 1: Create a report

In this step, you'll create a report that asks questions about your business data in Zendesk Support. You'll start by connecting to a *dataset*.

### Get started

1. In Zendesk Support, open the [product tray](https://support.zendesk.com/hc/en-us/articles/4408838272410).
2. From the list of products, click **Analytics**. Explore opens and displays the dashboard library.
3. In the Explore sidebar, click the reports icon (![reports button](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)).
4. On the **Reports library** page, click **New report**.
5. On the **Select a dataset** page, choose **Support** >
   **Support - Tickets**, and then click **Start report**.

The report builder opens with a blank report.

![Blank report page](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore-444.png)

### Define the report's metric

The first thing you need to add is the metric for this report. This means what you are measuring. In this example, it’s the total number of tickets stored in Zendesk Support. Perform the following steps to define your report's metric.

1. In the **Metrics** section of the report builder, click **Add**.
2. From the list of Metrics, expand **Tickets**, choose **Tickets**, then click **Apply**.
3. Explore takes the metric you added, and automatically displays results based on it.

![Simple Explore query](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_query.png)

While simple (a count of how many tickets you have), it’s a good example of how Explore dynamically displays results based on your metrics and attributes. Now, you can add attributes to get more interesting results.

### Define the report's attributes

Now that you’ve defined your report's metric, you’ll make this report more interesting by adding some attributes. First, you’ll add a column to the report so you can see which agents are assigned which ticket.

#### Add the assignee name

1. In the **Columns** section, click **Add**.
2. From the list of attributes, expand **Assignee**, choose **Assignee name**, and then click **Apply**.
3. Once again, Explore automatically processes the change you’ve made, figures out the best way to present it (in this case, a bar graph), and displays your results.

![Adding a column to an Explore query](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_column.png)

#### Add the ticket status

Remember that we also want to be able to filter the results by the ticket status. For example, we might want to only display tickets for ‘Robert Stack’ with a status of Solved.

1. In the **Rows** section, click **Add**.
2. From the list of attributes, expand **Ticket**, choose **Ticket status**, and then click **Apply**.
3. Once again, Explore recalculates the report and displays the results. Now, when you choose a ticket status, you’ll see only the number of tickets with that status for each agent.

   Note: You can select one or more of the Ticket Status items, or select them all by clicking the **Ticket Status** heading.

![Adding a row to an Explore report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_row.png)

### Name the report

Explore automatically names the report when you save it. In the case of the example report above, Explore saves it as **COUNT (Tickets) crossed with Ticket status per Assignee name**. You can either use this name, or give the report a name of your own.

**To name the report**

1. In the report builder, click the report name text.
2. Enter a name for the report (for example, New test report).

### Save the report

Now you have a completed the report, make sure that you save it. If you close your browser, or navigate to another page without saving, your changes will be lost.

1. In the report builder, click **Save**.
2. You'll see a confirmation message to indicate your report was saved.

Tip: You can also save a report directly to a new dashboard by selecting **Add to Dashboard**.

## Step 2: Create a dashboard

Usually, after you've created reports, you’ll want to group a bunch of them together, add some interactivity (for example, selecting a date range), and add other text and graphics to make a really great looking report. In this step, you’ll learn how to make a dashboard from the reports you created in Step 1.

There are two ways to create a dashboard. You can save a report right into a new dashboard, or you can create the dashboard first, and then add in the report. In this example, you’ll use the second method.

### Get started

1. From the product tray in Zendesk Support, choose the Explore icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_main_icon.png)).
2. In the Zendesk Explore sidebar, click the dashboards icon (![Dashboards button](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)).
3. On the **Dashboards** page, click **New dashboard**.

A new, blank dashboard opens in the dashboard builder.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_blankdashboard.png)

### Add a widget

If you've read [Getting started with Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618-Getting-started-with-Zendesk-Explore), you'll know that *widgets* add information and interactivity to a dashboard. Widgets might include a report, an image, and interactive elements like a date chooser.

The most important widget you need in this dashboard is your report. Use the following steps to get the report onto your dashboard:

1. In your blank dashboard, click **Add** > **Add report**.
2. On the **Add report** page, click the report you created in [Step 1: Create a report](#topic_uqw_jvd_t2b), then click **Add reports**.
3. After a moment, the report will be displayed on your dashboard.
4. Click and hold in the title bar of the widget to move it where you want it on the dashboard.
5. Select the widget, then drag any corner or edge to resize the widget.

Finally, give your dashboard a title like **People and tickets analysis**.
Double-click the existing title (on a new dashboard, it will read **Untitled**), then enter your new title. You'll end up with something that looks like the following:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_qsg_draft33.png)

You've now created a simple dashboard. We encourage you to explore all of the settings and widgets on the Dashboard page. There is a lot you can do!

For example, you could add a graphic containing your company logo, change the colors and fonts used, or create and add more reports. If you want some starting points for further exploration, see [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418-Adding-a-new-dashboard) and [Customizing dashboards](https://support.zendesk.com/hc/en-us/articles/4408819770906-Customizing-your-dashboard).

## Step 3: Share your dashboard

In the previous lesson, you created a dashboard but, currently, only you can view it.
To get the most from it, you will likely want to share it with others. There are a number of ways you can do this (see [Sharing dashboards](https://support.zendesk.com/hc/en-us/articles/4408827282714-Sharing-dashboards)), but as you are already in the dashboard builder, you'll use that here.

1. In the dashboard you created, click **Share**.

   ![Explore share dashboard button](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_share.png)
2. In the **Share dashboard** list, choose the Zendesk groups who you want to share this dashboard with.

   Tip: *Groups* are collections of users that you set up in Zendesk Support. For details, see [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130).
3. Click **Invite**.

After a few moments, the people you invited will receive an email with the subject line "(*your name*) has shared a Zendesk Explore dashboard with you". If they click the **Start Exploring** link in the email, they will see the dashboard you created.

Finally, an important point to remember. If you make changes to this dashboard after you share it, you'll need to click **Publish** to make the changes visible to anyone you shared the dashboard with.

## Next steps

These steps have covered the basic Zendesk Explore workflow. However, Explore is a powerful product that gives you many capabilities to query, present, and share your business information. To continue learning about Explore, visit the following two links:

- [Getting started with Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618-Getting-started-with-Zendesk-Explore) - Contains overview information about Explore, and links to more in-depth information.
- [Zendesk Explore resources](https://support.zendesk.com/hc/en-us/articles/4408846357018) - Contains links to Zendesk and community tips to help you get the most from Explore.
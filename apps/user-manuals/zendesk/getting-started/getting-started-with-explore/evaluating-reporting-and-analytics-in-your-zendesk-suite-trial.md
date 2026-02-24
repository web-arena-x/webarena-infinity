# Evaluating reporting and analytics in your Zendesk Suite trial

Source: https://support.zendesk.com/hc/en-us/articles/4408846698650-Evaluating-reporting-and-analytics-in-your-Zendesk-Suite-trial

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

This part of the [Zendesk Suite trial evaluation guide](https://support.zendesk.com/hc/en-us/articles/4408839376154) helps you evaluate reporting and analytics features in the Zendesk Suite to see how they'll work for you. Your trial is on the Suite Professional plan and includes Explore Professional features.

Explore for reporting and analytics gives you the tools you need to analyze, understand, and share your business information. Information for most Zendesk features can be reported in easy to read prebuilt reports that you can filter to your own needs. When you want to dig deeper, you can use Explore's powerful reporting tools to build your own reports.

Follow the steps in this guide to try out reporting and analytics. Each task typically takes less than 10 minutes to complete (though activating Explore in step 1 can take a bit longer).

This article contains the following sections:

- [Step 1: Activate Explore](#topic_zyt_t5w_r4b)
- [Step 2: Take a look at the prebuilt dashboards](#topic_j3q_gvw_r4b)
- [Step 3: Create a simple custom report (Professional and Enterprise)](#topic_ifr_gvw_r4b)
- [Step 4: Create a dashboard (Professional and Enterprise)](#topic_utr_gvw_r4b)
- [Step 5: Share your dashboard](#topic_i3s_gvw_r4b)
- [What's next?](#topic_twv_mvw_r4b)

## Step 1: Activate Explore

Before you can start digging into your data, you'll need to activate Explore. This is a necessary step as you might have already created tickets in Support, articles in Guide, or tested other support processes. Explore needs to examine the products you have installed and read in the necessary data you'll need to view and create reports. This is a once only operation for you to perform and might take up to two hours. Don't worry, your agents won't have to perform this step.

### Try it out

In this section, you'll open and activate Explore for the first time. If another admin has already done this, you can skip activation, but you'll need to make sure that an admin has given you access to complete the rest of this evaluation.

**To open and activate Explore**

1. From any Zendesk product, open the [product tray](https://support.zendesk.com/hc/en-us/articles/4408838272410) and click **Analytics**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/product_tray_v2.png)
2. Explore opens on the activation page. Click **Activate** to start setting things up. This might take up to two hours, but if you are testing a new account, it will usually take less time. In the meantime, have a cup of coffee and browse through the [Explore help center](https://support.zendesk.com/hc/en-us/categories/360001735914) to read about some of the things you'll be able to do. You can have Explore notify you with an email once setup is complete.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_activation_3.png)
3. Once Explore notifies you that it's finished setting up, you're ready to go.
   If you want any other agents to help evaluate Explore, you'll need to give them access. Read [Giving agents access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970) if you want to do this.

## Step 2: Take a look at the prebuilt dashboards

Now that you've set up Explore, you can start looking at some of the best practices dashboards that Zendesk created for you. A dashboard is a collection of reports collected on one or more pages. The available dashboards change regularly, but you can read all about them in [Understanding dashboards](https://support.zendesk.com/hc/en-us/articles/4408846844826) or, as you'll learn shortly, you can just browse the list yourself.

### Try it out

In this example, you'll take a look at the prebuilt Zendesk Support dashboard to discover the average number of tickets created in your Zendesk instance each day of the week.

**To see the report**

1. In any Zendesk product, open the product tray.
2. Click **Explore** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_product_icon.png)) . Explore opens showing a list of available dashboards.
3. From the list of dashboards, choose the **Zendesk Support** dashboard.
4. In the Zendesk Support dashboard, scroll down until you see the **Average tickets created by day of week report**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-7.png)

Tip: If you're wondering how often these reports update with new information, it depends on which plan you're using. Explore Lite reports update every day, Explore Professional and Enterprise reports update once an hour (though Explore Enterprise also features some reports that update in near-real-time). For detailed information, see [Data refresh intervals for Explore plans](https://support.zendesk.com/hc/en-us/articles/4408823242778).

If you're using Explore Lite, you can skip to the [What's next?](#topic_twv_mvw_r4b) section, but if you're interested in the more advanced reports you can create and share with Explore Professional and Enterprise, feel free to read on.

## Step 3: Create a simple custom report (Professional and Enterprise)

Sometimes, the prebuilt dashboards don't contain exactly the report that you need. In many cases however, you can create your own. Explore Professional and Enterprise include many hundreds of metrics and attributes you can use to mix-and-match your own reports. In this section, you'll learn a basic example of creating a custom report and learn how to find many more examples.

### Try it out

In this custom report, you'll create a simple report that shows one-touch tickets. These are tickets that were solved with only one agent reply. This report is a great way to gain context into your support efforts. Feel free to experiment with the various settings to get different results.

**To create the report**

1. In Explore, click the reports (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, click **Support** >
   **Support - Tickets** and then click **Start report**. The report builder opens.
4. Next, add your metric, the thing you want to measure. In this case, you'll add the number of one-touch tickets. In the **Metrics** panel, click **Add**.
5. From the list of metrics, choose **Agent replies distribution**
   > **One-touch tickets**, then click **Apply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_recipe_18.png)

   Explore displays the total number of one-touch tickets in your account.
6. Explore reports can return a lot of data. Using filters is a great way to restrict the results you return. In the **Filters** panel, click **Add**.
7. From the list of attributes, choose **Time - Ticket solved** >
   **Ticket solved - Date**, then click **Apply**.
8. In the **Filters** panel, click the **Ticket solved - Date** filter you just added.
9. On the filter page, click **Edit date ranges**.
10. On the **Advanced** tab of the **Date range** page, choose an appropriate range to view, such as 30 days in the past, then click **Apply**.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_recipe_19.png)
11. In the **Columns** panel, click **Add**.
12. From the list of attributes, choose **Time - Ticket solved** >
    **Ticket solved - Date**, then click **Apply.**
13. From the visualization type menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)), choose a **Line** chart.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_recipe_222.png)
14. Click the title at the top of the report (by default, "New report") and enter a new name for it like **One-touch tickets by date**.
15. When you're finished, click **Save**.

For a more detailed introduction, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530). This custom report was taken from our extensive collection of sample Explore reports known as recipes. See them all at [Explore recipes reference](https://support.zendesk.com/hc/en-us/articles/4409149172890).

## Step 4: Create a dashboard (Professional and Enterprise)

Reports are great, but you'll usually want to collect bunch of reports together to send them to others in your organization. Explore *dashboards* are used to accomplish this. There are two ways you can do this:

- Create a copy of an existing dashboard or one of the prebuilt dashboards and edit it.
- Create a brand new dashboard.

### Try it out

In this example, you'll create a new dashboard and add the report you created in [Step 3](#topic_ifr_gvw_r4b).

To find all you need to know to create your own dashboards, see [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418).

**To create the dashboard**

1. In Explore, click the **Dashboards library** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) on the left side bar.
2. Click **New dashboard**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_new_dashboard.png)

   A new blank dashboard opens.
3. In your new dashboard, click **Add** > **Add report**.
4. On the **Add report** page, choose the **One-touch tickets by date** report you created in [Step 3](#topic_ifr_gvw_r4b), then click **Add reports**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_eval_trial_2.png)
5. Your report is added to the dashboard. You'll notice it probably looks too small or is in the wrong place. You can drag it around and resize it just like you'd resize a window on your computer.
6. Once you've got the report positioned just how you want it, click the title at the top of the dashboard (by default **Untitled**) and give the dashboard a name like **One-touch tickets dashboard**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_eval_trial_3.png)

   The dashboard is saved automatically. Keep it open and move onto [Step 5](#topic_i3s_gvw_r4b).

To find all you need to know to create your own dashboards, see [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418).

## Step 5: Share your dashboard

You can share dashboards with agents in your Zendesk account, groups of agents, and with some Explore plans, people who don't have an account in your Zendesk instance.

### Try it out

In this example, you'll share your dashboard with a single person.

**To share your dashboard**

1. In your dashboard, click **Share**.
2. On the **Share dashboard** page, find and select the people or groups you want to share the dashboard with (this example uses "Rob Stack"). You can type a partial name into the filter box to filter how many names and groups are shown in the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_eval_trial_4.png)
3. When you are finished, click **Invite**.

The people you invite will receive an email. The email contains a link they can click to access the dashboard. If you later make updates to the dashboard, the people you invited will not see the updates unless you *publish* the dashboard first (from the same menu you found the **Share** command).

To learn all you need to know about sharing dashboards, see [Sharing dashboards](https://support.zendesk.com/hc/en-us/articles/4408827282714).

## What's next?

If you're ready to start digging further into Explore, start with out [getting started guide](https://support.zendesk.com/hc/en-us/articles/4408831710618). To see all of the Explore documentation and information about free training, see [Zendesk Explore resources for reporting and analytics](https://support.zendesk.com/hc/en-us/articles/4408846357018).
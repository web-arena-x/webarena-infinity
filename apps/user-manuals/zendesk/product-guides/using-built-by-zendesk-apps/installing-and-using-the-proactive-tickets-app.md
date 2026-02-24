# Installing and using the Proactive Tickets app

Source: https://support.zendesk.com/hc/en-us/articles/4408828120218-Installing-and-using-the-Proactive-Tickets-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Here are some ways you might want to use proactive tickets:

- **Manage business renewals:** Create proactive tickets when your customers are coming up to their subscription renewals. With subscription type or renewal date stored in a custom user field in your account, you can target specific customer types.
- **Online retailers:** Proactively reach out to customers based on their service changes, purchase history, or order fulfillment status. Knowing your buyers' history can help you anticipate potential issues with their experience, driving up revenue and reducing abandonment.
- **Internal help desks:**Notify users within your organization of service disruptions or policy changes. Keeping your employees up and running reduces downtime and maintains their productivity.

To help you get started, this guide will walk through:

- [Important considerations](#h_01GQ3MT7V7Z9ZWWXHCMPZZS994)
- [Installing the Proactive Tickets app](#installation_proactive)
- [Creating proactive tickets campaigns](#using_pro_active)
- [Best practices for your proactive ticket campaigns](#bestpractice_proactive)
- [Release Notes](#h_8cbb633c-99ec-48c7-9af1-e6214d00dded)

## Important considerations

- You must set a default time zone on your [user profile](https://support.zendesk.com/hc/en-us/articles/4408835022490) to use the Proactive Tickets app. If a default time zone isn't set, you will encounter a blank page when running a search.
- The Proactive Tickets app does not work with [custom ticket statuses.](https://support.zendesk.com/hc/en-us/articles/4412575861018) The app is only compatible with [system ticket status fields](../../agent-guide/ticket-basics/updating-and-solving-tickets.md#topic_i3y_np1_vt).
- When searching for customers, only 20 display in search results at a time. To create more than 20 tickets at once, increase the number of users per page. See [How can I send more than 20 tickets at a time through the Proactive Tickets app?](https://support.zendesk.com/hc/en-us/articles/6461221673754)
- When searching for information in custom user fields, use the key that names the custom field. If you are looking for a specific multi-word phrase (such as “renewal date”), enclose it in quotes. This ensures that you receive exact matches. 
 Example: To search for the custom field named "renewal date," you would enter it as follows: custom\_field\_name: "renewal date".

## Installing the Proactive Tickets app

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Apps and integrations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)) in the sidebar, then select **Apps > Zendesk Support apps**.
2. Click **Marketplace** at the top of the page and then enter "Proactive Tickets" in the Marketplace search bar.
3. Double-click the Proactive Tickets app icon and click **Install**.

After the app is installed, you'll see the Proactive Tickets (![](https://support.zendesk.com/hc/article_attachments/7856445814426)) icon appear in the left navigation bar.

## Creating proactive ticket campaigns

It's best practice to double check your customer list and make sure that you are sending to the correct group of customers.

To create a campaign using the Proactive Tickets app, agents must have permissions to create and edit shared views.

**To create a proactive ticket campaign**

1. Click the Proactive Tickets (![](https://support.zendesk.com/hc/article_attachments/7856445814426)) icon in the left navigation bar.
2. Enter search criteria to create a filtered list of customers, then click **Search**. 
   Use the text field at the top to search all user fields. For example, type an organization name, tag, or last name in the text field, and the app will search all user fields to find results. 
   You can also use individual fields to search for customers. For example, to create a list of customers at the Petipet organization with a VIP tag on their profile, type **Petipet** in the **Organization** field and **VIP** in the **Tags** field.
3. Select the customers in the list, then select **Create ticket**.
4. Enter a unique name in the **Name your campaign**field. The name will be added as a tag to all the tickets for this campaign. You can use this tag to create custom reports.
5. Enter remaining details, like the subject, description, ticket status, and assignee, in the **Create your proactive ticket**section.  

   Note: If you're creating proactive tickets with a Solved status, make sure to fill out any required fields on the ticket form before proceeding.
6. Select a macro to run on the proactive tickets as they are created
7. Click **Next** to preview your proactive ticket.
8. Review your proactive ticket details and click **Send** to send your campaign.
9. Once your tickets are all created, a confirmation page appears. Additionally, Zendesk will automatically create a ticket view for your campaign. Click **G****o to ticket view** and use that dedicated view to manage your proactive tickets.

Zendesk creates proactive tickets at a rate limit of 200 tickets per minute. Depending on how many proactive tickets you're creating, it might take a few minutes for your entire campaign to run. Please do not leave the screen during this time.

## Best practices for your proactive ticket campaigns

In addition to setting up the Proactive Tickets app, you can set up other aspects of your Zendesk to support your proactive ticket campaigns.

**Before you create proactive tickets:**

- Your proactive tickets will follow the existing workflows you have set up in your Zendesk. Review your triggers setup to make sure you want your proactive tickets to follow the same workflow. To create a dedicated workflow for your proactive tickets, you'll need to set up a trigger based on the unique tag for your proactive ticket campaign. See [Streamlining workflows with triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) for setup help.
- Meet with your team to communicate the objectives and create an action plan for your proactive tickets campaign. Identify queue management, triage, and escalation strategies. With a prepared plan of attack, your team will be more efficient and productive in managing your proactive communication.
- Create other relevant tools, like macros to speed up repetitive responses, to support your proactive ticket campaign. See [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602) for setup help.

**As you create your proactive tickets:**

- Make sure that you do not create more proactive tickets than your team can reasonably support. If you're planning on proactively communicating with your customers, you'll want to be prepared to be able to respond back quickly and efficiently. A great way to gauge how many tickets your agents can support is by simply looking at your agents' ticket resolution power, as measured by tickets solved per day.
- Be mindful of your customers when creating proactive tickets on their behalf. Just like any other outbound customer communication, you want to be careful on how often you "reach out" or "spam" them.
- Double-check your customer lists before sending out your proactive ticket campaign. We recommend that you create no more than 1,000 proactive tickets per campaign, so make sure your customer list has fewer than 1,000 customers. If you need to send to more customers, you'll need multiple campaigns.

**After you create your proactive tickets:**

- Check out the ticket view Zendesk automatically creates for you. You can use this view to organize and manage your proactive tickets. You can customize this ticket view to fit your needs. See [Using views to manage workflows](https://support.zendesk.com/hc/en-us/articles/4408888828570) for setup help.
- To report on your proactive ticket campaign, you can use the unique tag that was created for your proactive ticket campaign. You'll need to use Insights to create custom reports based off of this tag. See [Insights tag reporting: Reporting on tickets with one or more tags](https://support.zendesk.com/hc/en-us/articles/4408838291738) for more information.

## Release Notes

**Version 2.3.1 - 2022-05-24**

- Improvements
 - Allow HTML content for ticket description

**Version 2.2.2 - 2021-05-10**

- Improvements
 - Fixed several issues with translations and alignment issues

**Version 2.2.1 - 2021-01-25**

- Improvements
 - Added a more specific error message when the agent doesn't have the correct permissions to run a campaign and create the tickets

**Version 2.2.0**

- Improvements
 - Allows sending campaign to failed users
 - Updated alert message when campaign fails

**Version 2.1.0 - 2020-05-20**

- Improvements
 - Search Enhancements
 - Ability to run a macro when Proactive tickets campaign runs (**Basic Plan**)
- Bug fixes 
 - Characters in non-English languages being truncated
 - Fixed an issue where it was searching/including suspended users
 - Fixed an issue where markdown language wasn't working in ticket description.

**Version 2.2.0 - 2020-11-20**

- Improvements
 - Allow sending campaign to failed users
- Bug fixes
 - Add corresponding error text for unauthorized access instead of generic vague message
 - Localization and UI update

**Version 2.3.0 - 2021-07-30**

- Convert and incorporate paid features into the Free plan
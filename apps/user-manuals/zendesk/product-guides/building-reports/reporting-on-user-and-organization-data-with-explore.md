# Reporting on user and organization data with Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408836304282-Reporting-on-user-and-organization-data-with-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

While Explore is great for reporting on your tickets, help center page views, calls, and chats,
you can also use it to report about users and organizations associated with your
account. The Support: Tickets dataset contains many metrics and attributes you can use
to report on users, organizations, and more. See [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594) to learn more
about what you can report on.

Note: Users and organizations do not have to have a support ticket associated with them
in order to be counted in these reports.

In this article, you can get started by creating the following two simple, but useful
reports:

- [Displaying the number of users in each organization associated with your Zendesk account](#topic_nck_342_s4b)
- [Displaying users associated with your Zendesk account](#topic_qn2_t42_s4b)
- [Next steps](#topic_e3b_syt_t4b)

## Displaying the number of users in each organization associated with your Zendesk account

A ticket organization is a group you create into which you place users, for example
*VIP customers*, or *Beta testing*. In this example, you'll create a
report that shows all of your organizations and how many users are assigned to
each.

Note: When reporting on [custom organization fields](https://support.zendesk.com/hc/en-us/articles/4408842677786), Explore
always references the first or default organization of the ticket requester (the
*Requester organization name*), not the *Ticket organization name*
field. If a [user has been added to multiple
organizations](https://support.zendesk.com/hc/en-us/articles/4408838309530), or if *Ticket organization name* is different
than *Requester organization name*, then the custom organization fields in
reports might not correctly reflect the ticket organization being reported on.
For example, if a requester is assigned to Organization A (Default) and
Organization B, but the ticket organization is set to Organization B, Explore
reports reporting on custom ticket organization will return Organization A
(Default).

**To display organizations associated with your account**

1. In Explore, click the reports ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, click **Support** >
   **Support - Tickets**, then click **Start report**. The report builder
   opens.
4. Next, add your metrics, the things you want to measure; in this case,
   the number of organizations associated with your account. In the **Metrics**
   panel, click **Add**.
5. From the list of metrics, choose **Users and organizations** >
   **Users**, then click **Apply**. Explore displays the number of users
   in your account.
6. Now, you'll slice this data to show the name of each organization. In the
   **Rows** panel, click **Add**.
7. From the list of attributes, choose **Ticket organization** > **Requester
   organization name**, then click **Apply**. Explore displays a list of
   all of your organizations and the number of users in each. If there is a blank
   line at the top of your table, this indicates users who are not assigned to an
   organization. If you want to remove this line, click the **Requester
   organization name** attribute and exclude any NULL values.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_orgs_1.png)

For more information about ticket organizations, see [Organizing tickets and users](https://support.zendesk.com/hc/en-us/articles/4408883609370).

### More ideas

While you've started with a simple example, try adding more attributes to make
the report more useful. For example:

- Add the attribute **Requester organization domains** to see the domains
  associated with each organization.
- Add the attribute **Requester organization status** to see which
  organizations are currently active.

## Displaying users associated with your Zendesk account

This is a great report that shows all users and agents associated with your Zendesk
account and how many ticket requests they've made.

**To display users associated with your Zendesk account and their ticket
requests**

1. In Explore, click the reports ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, click **Support** >
   **Support - Tickets**, then click **Start report**. The report builder
   opens.
4. Next, add your metrics, the things you want to measure; in this case,
   the number of organizations associated with your account. In the **Metrics**
   panel, click **Add**.
5. From the list of metrics, choose **Users and organizations** >
   **Users**, then click **Apply**. Explore displays the total number of
   users associated with your account.
6. Next, you'll add the users names and their Zendesk role to the report. In the
   **Rows** panel, click **Add**.
7. From the list of attributes, choose **Requester/user** > **Requester
   name** and **Requester role**, then click **Apply**. Explore
   displays a list of all users in your account together with their role.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_orgs_2.png)

There are many hundreds of metrics and attributes you can report on with Explore so
feel free to experiment with these examples using [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594) for
ideas.

## Next steps

If you haven't already found them, our extensive collection of [Explore recipes](https://support.zendesk.com/hc/en-us/articles/4409149172890) gives you some great, self-contained
examples of using Explore to report on real-world scenarios. Here are links to a few
examples that will help you report on user and organization information:

- [Explore recipe: Displaying organizations with
  no users](https://support.zendesk.com/hc/en-us/articles/4408835510810)
- [Explore recipe: Displaying users with no
  ticket requests](https://support.zendesk.com/hc/en-us/articles/4408830337178)
- [Explore recipe: Displaying organizations with
  no tickets](https://support.zendesk.com/hc/en-us/articles/4408846245658)
# Creating distribution pools (round robin) for allocating leads, contacts, and deals

Source: https://support.zendesk.com/hc/en-us/articles/4408839201178-Creating-distribution-pools-round-robin-for-allocating-leads-contacts-and-deals

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

Many sales teams work with new leads, contacts, and deals using a structured process where the leads, contacts, and deals are evenly allocated to members of a team, based on different factors, for example, the location of a representative.

You can use the object distribution feature to:

- Create one or more distribution pools, for leads, contacts, or deals distribution
- Assign individual users, or with Enterprise and Elite plans, assign whole [teams, groups](https://support.zendesk.com/hc/en-us/articles/4408832118554-Working-with-groups-and-teams-in-Sell-Enterprise-and-Elite-), or [roles](https://support.zendesk.com/hc/en-us/articles/4408825410458-EAP-Setting-up-a-role-in-Sell) to a distribution pool
- Use the distribution pool to automatically assign leads, contacts, or deals to the users in the pool, in a *round robin*.

Note: You can create one distribution pool on most Sell plans (not available on the lowest Sell plan). If you are on the two highest Sell plans, you can create multiple distribution pools.

You need admin rights to set up and manage distribution pools, however distribution pools are visible to all users.

When you have created a distribution pool, you can [assign](https://support.zendesk.com/hc/en-us/articles/4408823875354-Assigning-distribution-pools-in-Sell) it anywhere in Sell that you assign an owner for a lead, contact, or deal.

This article covers the following topics:

- [Creating a distribution pool](#topic_zsh_lm2_jtb)
- [Editing a distribution pool](#topic_jg5_lm2_jtb)
- [Deleting a distribution pool](#topic_njg_mm2_jtb)

## Creating a distribution pool

In **[Settings > Business Rules > Distributions](https://app.futuresimple.com/settings/distributions)**, you can create a distribution pool for allocating leads, contacts, or deals. Each pool is individual to the object type, for example, a leads distribution pool only allocates leads, and a deals distribution pool only allocates deals.

You can create distribution pools and allocate users to distribution pools manually. Creating a distribution pool creates a phantom user so you can use API to query the ID of that user, and assign leads, contacts, and deals to the user ID (via API or Zapier). For more information, see [Sell REST API](https://developers.getbase.com/docs/rest/articles/introduction).

**To create a distribution pool**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Business Rules > Distributions](https://app.futuresimple.com/settings/distributions)**.
2. Click the **Leads**, **Contacts**, or **Deals** tab, depending on which type of distribution pool you want to create.
3. If you have not previously set up a distribution pool for this object type, click **Add your first distribution**. If you have existing distribution pools for this object type, click **Add new distribution**.
4. Enter the following information in the new distribution window:
   - **Distribution name**: use a meaningful name for the distribution pool. This name will appear everywhere that a user name appears, so it is important that this easily identifies the team that it relates to, and it is useful to specify that it is a distribution group.
   - **Distribution type**: this is round robin (this is the only distribution type currently available).
   - **Rotate between**: click to select users or group members, team members, or [role members](https://support.zendesk.com/hc/en-us/articles/4408825410458-EAP-Setting-up-a-role-in-Sell), if you have these set up for your organization.

     You can only choose one type for the distribution, that is, either a set of specific users, groups, teams, or roles.

     Note: There is a limit of 200 users, teams, groups, or roles in a distribution pool. For example, you can add up to 200 groups to a distribution, regardless of the number of users in each group.
   - To add users, click **Users** and select each user from the drop down list, or start typing part of the name in this field to get a shortlist of users to add. Add all the users that you want to be part of this distribution pool. As you add, the users are displayed.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_add_distribution_user.png)
   - To add teams, groups, or roles, click **Team members**, **Group members**, or **Role members** and start typing part of the name to get a shortlist of the teams, groups, or roles that you can add. Alternatively make a selection from the drop down list. As you add, the users in that team, group, or role are displayed.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_add_distribution_group.png)
5. Click **Create**.

   You'll see your new distribution pool is created, showing the users included in the pool. If you added one or more teams, groups, or roles, every user is listed.

   If there are many users in a distribution pool, you can hover over the number of additional users to see their names.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_distribute_user_names.png)

You are now ready to start [assigning distributions pools](https://support.zendesk.com/hc/en-us/articles/4408823875354-Assigning-distribution-pools-in-Sell) in Sell. See [Distributing leads, contacts, and deals](https://support.zendesk.com/hc/en-us/articles/4408821347226-Distributing-leads-contacts-and-deals-across-your-Sell-team) for more information on the rules that are applied when you use distribution pools.

## Editing a distribution pool

You can edit an existing distribution pool to change the name, or members of the pool.

Note: If you remove users from this distribution pool, this does not affect any leads, contacts, or deals that were previously allocated to that user.

**To edit a distribution pool**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Business Rules > Distributions](https://app.futuresimple.com/settings/distributions)**.
2. Click the **Leads**, **Contacts**, or **Deals** tab, depending on which type of distribution pool you want to edit.
3. Click the name of the distribution pool you want to edit.
4. You can change the distribution name.

   This will change the name in all places that the distribution pool is available to select.
5. You can change the type of distribution for the pool. You can only choose one type for the distribution, that is, either a set of specific users, groups, teams, or roles.

   Click **Users**, or **Team members**, **Group members**, or **Role members**, if you have these set up for your organization, and select or search to add.

   Note: If you choose a new option for the pool rotation, the previous selection is removed. For example, if you had previously selected **Users** and added individual users, and you choose **Team members**, all users previously added to the pool are removed.
6. You can change the members that are included in the pool, by adding or deleting users, groups, teams, or roles, depending on which type of pool you have created.
   - To add users, click **Users** and select from the list or search for each user.
   - To add teams, groups, or roles, click **Team members**, **Group members**, or **Role members** and select from the list or search for each team, group, or role.
   - To delete from the distribution pool, click the **X** next to the user, group, team, or role name.

     Note: You can't remove individual members from a group, team, or role. You have to remove the entire group, team, or role.
7. Click **Save**.

   You'll see your distribution pool is saved, showing the users included in the pool. If you added one or more teams, groups, or roles, every user is listed.

## Deleting a distribution pool

To delete a distribution pool

- Click the **Trashcan** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) next to the distribution pool. Any leads, contacts, or deals, that were allocated using this distribution pool are not affected (as they have already been allocated to a user), however new leads, contacts, and deals will not be allocated to users in the pool.

The distribution pool is removed from all parts of the product.

You must either create a new distribution pool for allocating new leads, contacts, or deals, or allocate them manually to users.
# Matter Permissions and Rates

Source: https://help.clio.com/hc/en-us/articles/9286062516123-Matter-Permissions-and-Rates

---

In Clio Manage, you can specify whether a matter is visible only to you, all firm users, and/or a group of firm users using matter permissions, and you can add billing rates specific to matters that you work on. Administrators also have the option to view which matters they are restricted from viewing, update matter permissions in bulk, and block specific users from accessing matters. 

**Note:** You cannot set matter permissions or rates in Clio Grow.

## Set matter permissions

All firm users can set permissions when creating or editing a matter. Matters are visible to all firm users by default, but you can also choose specific groups and/or users that have access to the matter. If you select specific groups and/or users, only those groups and/or users will have access to the matter. Learn how to [create a group](https://help.clio.com/hc/en-us/articles/9200279456667-Account-Users-and-Permissions#h_01HE334MQS44J4JZ2MTKX2PZQZ).

**Note:** You can add a maximum of 20 users and/or groups to a single matter. Once you have added 20, you will no longer be able to add any more users and/or groups.

**Important:** Users who do not have access to a matter may still be able to view the matter’s bills if they have billing or accounts permissions and view matter details when running reports if they have reports permissions.

1. Go to **Matters**, find your matter, and then click **Edit**. You can also search for the matter in the search bar and click **Edit matter**.
2. Scroll down to the **Matter permissions** section.
3. Under **Firm users with access**, select either **Everyone** or **Specific users or groups**.   
   - **Everyone:** If you select this option, all firm users will have access to this matter.
   - **Specific users or groups:** If you select this option, you can choose up to 20 firm users and/or groups of users to have access to this matter. Select your users and/or groups under **Add users or groups**. Once added, you can remove a user or group by clicking the minus symbol.
4. Click **Save matter**.

## View and update matter permissions in bulk

Firm administrators have the option to filter and view matters that they are restricted from accessing in the matters table and the option to update matter permissions in bulk. These actions allow you to audit and correct permissions across matters and ensure that matter details are only visible to users with appropriate permissions.

**Note:** Only administrators can perform these actions.

Admin view Update permissions in bulk

1. Go to **Matters** > **Matters.**
2. Click **Filters.**
3. Under **Admin view**, select either **Matters I have full access** to or **Matters I am restricted from**.   
   - **Matters I have full access:** If you select this option, the matters table will only show matters that you have full access to.
   - **Matters I am restricted from:** If you select this option, the matters table will only show matters that you are restricted from viewing.
4. Click **Apply filters.**

**Important:** When you edit matter permissions in bulk, the new permission edits you make will replace the existing permissions. This means that only the new users selected to have access and receive notifications for the matter will have access to the matter. Users previously added to the matter will no longer have access unless they are selected again.

1. Go to **Matters** > **Matters.**
2. Check the box next to each matter for which you want to change permissions.  
   - The new matter permissions that you choose will affect all of the selected matters.
   - You can select up to 200 matters to edit in bulk.
3. Click **Edit** and select **Update matter permissions**.
4. Under **Choose which firm users will have access going forward**, select either **Everyone** or **Specific users or groups**.   
   - **Everyone:** If you select this option, all firm users will have access to this matter.
   - **Specific users or groups:** If you select this option, you can choose up to 20 firm users and/or groups of users to have access to this matter. Select your users and/or groups under **Add users or groups**. Once added, you can remove a user or group by clicking the minus symbol.
5. *Optional:* Under **Choose who will receive matter notifications going forward**, select the firm users who you want to receive notifications for various matter events. Learn more about user notifications [here](https://help.clio.com/hc/en-us/articles/9290346939547-Set-Up-Clio-Manage#user-notifications-0-7).
6. Click **Update permissions**.

## Block users from accessing matters

If your are an administrator on your firm's account, you can block specific users from viewing or accessing details of any matter they should not have permission to access. You can block users one matter at a time in the matter form or in bulk from the main **Matters** tab, allowing you to easily restrict users from accessing matters where there may be conflicts of interest. You can unblock users at any time. Learn more about blocking users on a single matter in the matter form [here](https://help.clio.com/hc/en-us/articles/9285959663131#h_01GEK791XBF1JJ0VYC8BQTG9MW).

**Note:** Blocking users will override group permissions. This means that if a specific firm user is part of a group that has permission to access the matter, blocking that user will prevent them from accessing the matter regardless of any group they may be a part of.

**Tip:** Users who have access to a matter can view blocked users for that matter in the **Timeline** and **Details** sections of the matter's **Dashboard** and in the **Firm Feed**.

1. Go to the main **Matters** tab.
2. Check the box next to the matters that you want to block specific users from accessing.
3. At the top of the table, click **Edit** and then select **Block users.**
4. Under **Select users**, select the user(s) that you do not want accessing the matter.
   - If you previously blocked a user on a matter and you want to continue to block them, you will need to select the user again in order to retain the block.
5. Click **Block users**.

## Add matter rates

When creating new time entries in Clio Manage, the default rate applied to the time entries is the client or matter rate. If neither of these rates is specified, the time entry will default to the user rate or activity description rate. If you specify a matter rate, the time entries will default to this rate unless you enter a custom rate.

You can add more than one matter rate to a matter. For example, if you add a matter rate for yourself, your time entries will default to this matter rate for that matter. And if you also add a matter rate for another user or groups of users for the same matter, and one of those users creates a time entry for the matter, the time entry will default to the specified matter rate.

**Tip**: Learn more about [activity rates and rate hierarchy](https://clio.zendesk.com/hc/en-us/articles/9289801180187) and how to [create user groups](https://help.clio.com/hc/en-us/articles/9200279456667-Account-Users-and-Permissions#h_01HE334MQS44J4JZ2MTKX2PZQZ).

1. Go to **Matters** and click **Edit**. You can also search for the matter in the search bar and click **Edit matter**.
2. Go to the **Billing preference** section.
3. Under **Billing method**, select **Hourly**.
4. Under **Custom billing rates**, click **Add a custom billing rate**.
5. Select user(s) and/or groups and the rate for those users and/or groups.
6. Click **Save matter**.
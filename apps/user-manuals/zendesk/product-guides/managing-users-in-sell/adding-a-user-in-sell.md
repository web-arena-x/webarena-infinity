# Adding a user in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408823441050-Adding-a-user-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can add a user to your account if you have enough [seats (licenses)](https://support.zendesk.com/hc/en-us/articles/4408886107418) in your Sell subscription.

You need admin rights to add users.

This article covers the following topics:

- [Creating a user (on the two lowest Sell plans)](#topic_j3b_pw2_jtb)
- [Creating a user (on the two highest Sell plans)](#topic_h2r_pw2_jtb)

Note: If you use [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408824375450) to give a user access to Sell, make sure you [set their access permissions](https://support.zendesk.com/hc/en-us/articles/4408824037658) in Sell also. Otherwise, they will not be able to use Sell.

## Creating a user (on the two lowest Sell plans)

When you create a new user, you can choose between limited and full access permissions (see [Understanding access levels and privileges](https://support.zendesk.com/hc/en-us/articles/4408821340826)).

**To create a user**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Manage
   > Users](https://app.futuresimple.com/permissions)**.
2. Click **New user**.

   Note: If you don't have enough licenses, you are prompted to add more seats to accommodate the new user (see [adding and removing licenses](https://support.zendesk.com/hc/en-us/articles/4408886107418)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_add_user.png)
3. In **Add a new user**, enter the following details:
   - **Full Name**: this is how the user's name will be displayed in Sell.
   - **Email**: this is the email address where the user's activation instructions are sent, and also the address the user will use to log in to Sell.
   - **Assign permissions**: select either full access, or limited access (see the definitions for [access levels](https://support.zendesk.com/hc/en-us/articles/4408821340826)).
   - **Leads** (visible if you selected Limited access): select whether the user can view and update all leads in the account, or only their own leads.
   - **Contacts** (visible if you selected **Limited access**): select whether the user can view and update all contacts in the account, or only their own contacts.
   - **Prospects and customers** (visible if you selected **Limited access**):
     select whether the user can view and update all prospects and customers in the account, or only their own prospects and customers. A prospect is a contact with an active deal, and a customer is a contact with a closed deal.
   - **Deals** (visible if you selected Limited access): select whether the user can view and update all deals in the account, or only their own deals.
   - **Admin permissions**: check the box to grant the user full administrative privileges, (see [Managing user permissions](https://support.zendesk.com/hc/en-us/articles/4408831572890)).
4. Click **Send invitation**. The new user is created, and an activation email is sent to the email address you specified.
5. When the user clicks the activation button in the email, a web browser opens and they are prompted to complete their account registration. When the user clicks **Complete Registration**, their account is activated.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_account_registration.png)

## Creating a user (on the two highest Sell plans)

If you activated advanced permissions, you can choose to specify more granular access or you can create custom roles to define permissions that can be applied to multiple users.

If you want to work with custom roles, you'll need to create one or more roles (see [setting up roles](https://support.getbase.com/hc/en-us/articles/360035692131)).

If you don't want to use custom roles or individual user permissions, use these instructions to create a new user.

**To create a user**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Manage
   > Users](https://app.futuresimple.com/permissions)**.
2. Click **New user**.

   Note: If you don't have enough licenses, you are prompted to add more seats to accommodate the new user (see [adding and removing licenses](https://support.getbase.com/hc/en-us/articles/203133679)).
3. In **Create a new user**, enter the following details:
   - **Full Name**: this is how the user's name will be displayed in Sell
   - **Email**: this is the email address where the user's invitation is sent, and also the address the user will use to log in to Sell.
   - **Manager**: the manager of this user.
   - **Group**: the group this user is part of, if one is defined (see [working with teams and groups in Sell](https://support.getbase.com/hc/en-us/articles/204182345-Working-with-groups-and-teams-in-Sell)). The default setting is None. You can create a new group here, and add the user to it.
   - **Pipelines**: if you have multiple deal pipelines specified, choose which pipeline the user will be working with.
   - **Role**: select a role. You'll see one or more roles here if you've set up [custom roles](https://support.getbase.com/hc/en-us/articles/360035692131).
   - **Configure permissions**: if you select a role, this section is hidden. This is because you specify permissions in the role. If you have not selected a role, you specify at a granular level the view, create, update, reassignment, and delete permissions that your user has when working with contacts, leads, and deals.
   - **This user has Admin privileges**: check the box to grant the user full administrative privileges (see [Managing user permissions)](https://support.getbase.com/hc/en-us/articles/203424919-How-do-I-manage-user-permissions-and-data-access-in-Base-).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_user_add_image3.png)
4. Click **Save**. Your new user is created, and an activation email is sent to the email address you specified.
5. When the user clicks the activation link in their email, a web browser opens and they are prompted to complete their account registration. Then, when the user clicks **Complete Registration**, their account is activated.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_user_add_image4.png)
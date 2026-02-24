# Adding and updating users in Amazon Connect

Source: https://support.zendesk.com/hc/en-us/articles/9459094577562-Adding-and-updating-users-in-Amazon-Connect

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Learn how to manage your contact center by adding and updating users in Amazon Connect. You can manually add users or import them using a CSV file, defining login credentials, routing and security profiles, and phone type. Update user details anytime, including resetting passwords. This process helps ensure your team has the right access and tools for effective customer support.

Users in Amazon Connect are the agents and supervisors who manage your contact center. You can add users manually or by importing them in a CSV file. Each user has attributes that determine their roles and capabilities.

When adding a user, you specify the following details:

- **Login credentials:** User name and password
- **Routing profile:** Routing rules that determine the types of contacts the user can handle and their routing priority
- **Security profile:** User permissions within Amazon Connect, which determine access to features and settings
- **Phone type:** Phone type for voice contacts, either a softphone or a desk phone

This article contains the following topics:

- [Adding a user manually](#topic_xbj_xzx_xfc)
- [Bulk importing users](#topic_yzr_11y_xfc)
- [Updating users](#topic_n2w_mt4_ngc)

## Adding a user manually

You can add a user manually from the Amazon Connect console.

**To add a user manually**

1. From the [Amazon Connect Console](https://aws.amazon.com/connect/), select **Users** > **User management**.
2. Click **Add new users**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_3.png)
3. On the Add user page, click **Add a user manually**.
4. Enter the users details including name, user (sign in) name, and contact details.
5. In the Settings section, assign a security profile, typically agent or admin.
6. Assign a routing profile based on the user's role.
7. Under Phone, select whether the new user will use a soft phone or a desk phone.
8. Click **Save**.

   The new user is available in your Amazon Connect instance.

## Bulk importing users

You can import multiple users from an existing folder using a CSV file.

**To import users using a CSV file**

1. In the [Amazon Connect Console](https://aws.amazon.com/connect/), select **Users** > **User management**.
2. Click **Add new users**, then **Import users using a .csv template**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_4.png)
3. Download the CSV template provided on the page.

   Be sure to use the template so that you have all the necessary details for each user.
4. Enter user details in the CSV template for each user.
5. Click **Upload file**, then browse to the CSV file.
6. Click **Upload file and verify**.

   The new users are available in your Amazon Connect instance.

## Updating users

After you've added users, you can update their details at any time. Additionally, you can reset their password.

**To update a user**

1. In the [Amazon Connect Console](https://aws.amazon.com/connect/), select **Users** > **User management**.
2. On the User management page, click any user to open their page.
3. After you've finished making changes, click **Save**.
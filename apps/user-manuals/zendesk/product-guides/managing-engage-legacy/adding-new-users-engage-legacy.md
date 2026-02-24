# Adding New Users (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731474369050-Adding-New-Users-Engage-Legacy

---

Users in Amazon Connect are the agents and supervisors who handle and manage your contact center. Each user has a routing profile, security profile, and other attributes that determine their roles and capabilities.

‍

## How to add new users

When adding a new user, you specify their details, including:

- **Login credentials:** Username and password.
- **Routing Profile:** The routing rules that apply to the user. Determines the types of contacts they can handle and their routing priority.
- **Security Profile:** The user's permissions within Amazon Connect. Determines their access to features and settings.
- **Phone Type:** The type of phone the user will use for voice contacts, either a softphone or a desk phone.

### Create a user manually

To add a new user:

1. From the [Amazon Connect Console](https://aws.amazon.com/connect/) navigate to **Users** then **User management**.
2. Click **Add new users**.
3. Fill in the details such as first name, last name, username, etc.
4. Assign routing profile and security profile based on the user's role.
5. Click **Save**.

![](https://support.zendesk.com/hc/article_attachments/9731449478298)

## Import users using a .csv template

You can also import users from an existing directory. Bulk importing users is an efficient way to add multiple users to your Amazon Connect instance:

1. In the [Amazon Connect Console](https://aws.amazon.com/connect/), navigate to **Users**, then **User management**.
2. Click **Add new users**, then **Import users**.
3. Download the CSV template provided on the page. Use this template to ensure you have all the necessary details for each user, including name, username, password, routing profile, security profile, etc.
4. Fill out the CSV template with your users' details.
5. Click **Upload file**, browse and upload the filled out CSV file.
6. Click **Upload file and verify**.
7. The new users are now available in your Amazon Connect instance.

‍

![](https://support.zendesk.com/hc/article_attachments/9731449491354)

For more on adding users please see the AWS documentation:

<https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html>

‍
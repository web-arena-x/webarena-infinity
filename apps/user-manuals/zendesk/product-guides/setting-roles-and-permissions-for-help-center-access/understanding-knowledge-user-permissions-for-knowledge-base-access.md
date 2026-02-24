# Understanding Knowledge user permissions for knowledge base access

Source: https://support.zendesk.com/hc/en-us/articles/4408827797274-Understanding-Knowledge-user-permissions-for-knowledge-base-access

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Learn how to manage user permissions for your knowledge base. Use user segments to define who can view, edit, and publish articles. Create custom user segments to refine access for signed-in users and staff. Build management permissions to control editing and publishing rights, and apply these permissions at the article level to ensure appropriate access for agents and managers.

Knowledge *user permissions* include:

- **View permissions** for viewing content in the help center knowledge base. View permissions include both internal and external users.
- **Management permissions** for creating, editing, and publishing content in the help center knowledge base. Management permissions include internal users only.

User permissions are defined by *user segments*. You can apply user segments to articles to define user viewing permissions. You can also use user segments to build management permissions, which you then apply to articles to define agent editing and publishing permissions.

The process for building and applying permissions has the following steps:

1. [Start with the building block, user segments](#topic_jsw_1np_gfb)
2. [Build management permission for editing and publishing](#topic_azr_bnp_gfb)
3. [Apply user permissions to articles](#topic_akn_cnp_gfb)

## Step 1: Start with the building block, user segments

User segments are the building block of user permissions. A user segment is a group of agents and end users defined by a specific set of attributes. Before you build or set your user permissions, you'll want to make sure you have created the necessary users segments to define your user groupings.

There are two built-in user segments by default:

- **Signed-in users** includes users who are signed-in to your Help Center
- **Agents and managers** includes all agents and Knowledge admins

You can create custom user segments to further refine those groups of users as follows:

- Signed-in users, based on tags and organizations created in Admin Center
- Staff (agents and admins), based on tags and groups created in Admin Center

To create users segments, see [Creating user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_segments.png)

## Step 2: Build management permissions for editing and publishing

User permissions include content view permissions and management permissions. You do not need to build view permissions-you can apply up to 10 user segments directly to an article to set the view permissions for that article-so you can skip this step for view permissions.
You must build management permissions to define editing and publishing rights for agents, then apply them to an article to set agent management permissions for that article.

In addition to the existing predefined management permission, you can also activate the predefined editor and publisher permission (Enterprise only):

- **Managers** is active by default and gives only Knowledge admins edit and publish permission.
- **Editors and publishers** (this requires Enterprise) gives all agents and admins edit permission, but gives only Knowledge admins publish permission.

You can create management permissions based on user segments. On Professional, edit and publish permissions are assigned together, to a user segment of agents. On Enterprise, editing and publishing permissions are separate, so that they can be assigned to different user segments.

To create management permissions, see [Creating management permissions to define agent editing and publishing rights](https://support.zendesk.com/hc/en-us/articles/4408827952538).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_permissions.png)

## Step 3: Apply user permissions to articles

You apply user permissions at the article level. You cannot apply permissions to a category or section.

- **View permissions** Apply up to 10 user segments to an article to set the view permissions for that article. To apply view permissions, see [Setting view permissions on articles with user segments](https://support.zendesk.com/hc/en-us/articles/4408824005914).
- **Management permissions** You apply management permissions to define editing and publishing rights for agents, then apply it to an article to set agent management permissions for that article. To apply management permissions, see [Setting agent editing and publishing permissions on knowledge base articles](https://support.zendesk.com/hc/en-us/articles/4408834435738).
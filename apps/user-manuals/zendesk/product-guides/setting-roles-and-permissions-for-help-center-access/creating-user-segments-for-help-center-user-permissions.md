# Creating user segments for help center user permissions

Source: https://support.zendesk.com/hc/en-us/articles/4408837707290-Creating-user-segments-for-help-center-user-permissions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

A *user segment* is a collection of end users and agents, defined by a specific set of attributes and used to determine access to help center content. User segments are the building blocks for both viewing and management user permissions.

- **Viewing permissions**: You can apply:
 - One user segment to each help center and community topic to define viewing access for those resources. Users must belong to the specified user segment in order to have access.
 - Up to 10 user segments to each article in your knowledge base. Any user who belongs to at least one of the applied user segments will be able to view that article.
- **Management permissions**: You can apply user segments when building management permissions for articles. After they're built, you can apply management permissions to knowledge base articles to define who has permission to edit and publish those articles.

There are two built-in user segments by default:

- **Signed-in users**, includes users who are signed-in to your help center
- **Agents and admins**, includes all agents (including light agents) and admins

You can create custom user segments to further refine those groups of users as follows:

- **Signed-in users** (internal and external). These segments are created in Admin Center and can be based on tags, organizations, individual users, or all of them combined.
- **Staff** (internal). These segments are created in Admin Center and are based on tags, groups, individual users, or all of them combined.

Knowledge admins have access to all content, regardless of any user segments they belong to.
Because Knowledge admins have access to all content, their user profiles will display all custom user segments. You must be a Knowledge admin to create user segments.

This article covers the following topics:

- [Understanding access restrictions for user segments](#topic_u43_4jf_zz)
- [Creating user segments](#topic_tql_pjf_zz)

## Understanding access restrictions for user segments

Every user segment starts with a base user type of signed-in users or staff (agents and admins). From there, you can create a subset of users based on tags, organizations, groups, and individual users as follows:

- **Signed-in users** can be restricted by tags, organizations, individual users, or a combination of all three. Tags must be on the user or an organization they belong to.

 When you create a user segment based on tags for signed-in users, you can require that *all* specified tags match for the agent to be included and/or you can require that *at least one* of the specified tags match for the user to be included. For organizations, the user must belong to *at least one* of the specified organizations.

 Signed-in agents must have any required tags, agents do not have to belong to any of the specified organizations to be included in the user segment, so the organization is ignored for agents.

 Individual users do not need to meet any filters to be included in a user segment, in fact if **only** individual users are in a user segment, the segment will contain **only** those users.
- **Staff** (agents and admins), can be restricted by tags, groups, individual users, or a combination of all three.

 When you create a user segment based on tags for staff, you can require that *all* specified tags match for the agent to be included or you can require that *at least one* of the specified tags match for the agent to be included. For groups, the agent must belong to *at least one* of the specified groups.

 Knowledge admins have access to all content, regardless of the user segments that they belong to.

 Individual users do not need to meet any filters to be included in the user segment, and if **only** individual users are in a user segment, the segment will contain **only** those users.

**To define user segments, refer to the following table**

Table 1.

| User role | Restrict by tags (users need *all* tags) | Restrict by tags (users need *any* of the tags) | Restrict by organizations (users need at least one org) | Restrict by groups (users need at least one group) | Restrict by individual users |
| --- | --- | --- | --- | --- | --- |
| **Signed-in users** | YES | YES | YES (ignored for agents) | NO | YES |
| **Staff** | YES | YES | NO | YES | YES |

## Creating user segments

The two access types for user segments are: *signed-in users* and *staff*. You can create custom user segments to further refine those two groups of users as follows:

- **Signed-in users** (internal and external), are created in Admin Center. These segments are based on tags, organizations, individual users, or a combination of all three.
- **Staff** (internal), are created in Admin Center. These segments are based on tags, groups, individual users, or a combination of all three.

You can create as many as 200 user segments per account. If you have multiple brands in your account, then your user segments are shared across all brands.

Knowledge admins have access to all content, regardless of the user segments they belong to.

**To create a user segment**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **User permissions** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_user_permissions.png)) in the sidebar.
2. On the **User Segments** page, click **Add new**.

   If you receive an error message, that means you have reached the maximum number of 200 user segments. You can delete some user segments if you want to continue.
3. Enter a **Name** for this user segment.
4. Select a **User type** as the base of your user segment.

   - **Signed-in users** - includes internal and external users who create an account and sign in to your help center.
   - **Staff** - is for internal users only, including agents and Knowledge admins.

     ![Create user segment](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_user_segments_create.png)
5. Click **Filter by tag**.

   Then click the drop down menu to select a tag:

   - **Users and organizations matching ALL of these tags**: *all* of the tags must be on the user or org to be included in the user segment.
   - **Users and organizations matching ANY of these tags**: *one or more* of the tags must be on the user or org to be included in the user segment.

   You can add up to 50 tags each in **Users and organizations matching ALL of these tags** and **Users and organizations matching any of these tags**. Not all available tags appear on the list, so use search or scroll to find the tags that you are looking for. You can choose any tag that is applied to existing users or organizations. The tags can be on the user profile or, in the case of end-users, inherited through an organization.

   A list of matching users appears to your right. Agents do not appear on the list of matching users. If there are more than 30 matching users, click **View all matching users**, then you will see the full list.

   Note: You must have user tags enabled to create a user segment based on tags.
   For more information, see [Enabling user and organization tagging](https://support.zendesk.com/hc/en-us/articles/4408881573658#topic_czm_tew_qc).
6. (Optional) You can further refine your user segment by doing one of the following:
   - For signed-in users - if you want to restrict by organization, then select an organization from the drop down menu, and click **Filter by organizations**.
   - For staff members - if you want to restrict by group, then select a group from the drop down menu, and click **Filter by groups**.

     The user must belong to *at least one* of the organizations or groups to be included in the user segment.
     You can add up to 50 organizations or groups to a user segment. The exception is that organization is ignored for signed-in agents. Agents do not need to belong to any of the organizations to be included in the user segment.

     The list of matching users will update accordingly.
7. To add users to a new user segment, click **Add individual users**.

   You can add up to 50 additional individual users, regardless of the number of users in the group, tag, or organization filters you've specified. As you add users, the list of matching users updates.

   Note: If you add individual users, they are added to the user segment regardless of any group, tag, or organization filters that you may have already set.
8. Click **Create segment**.

   See the following topics for more information on how you can apply user segments:

   - [Set view permissions on knowledge base articles](https://support.zendesk.com/hc/en-us/articles/4408824005914)
   - [Create management permissions to define agent editing and publishing rights](https://support.zendesk.com/hc/en-us/articles/4408827952538)
   - [Set view access for community topics](https://support.zendesk.com/hc/en-us/articles/4408845814170)
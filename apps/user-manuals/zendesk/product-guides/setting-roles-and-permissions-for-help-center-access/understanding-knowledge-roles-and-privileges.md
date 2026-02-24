# Understanding Knowledge roles and privileges

Source: https://support.zendesk.com/hc/en-us/articles/4408827842458-Understanding-Knowledge-roles-and-privileges

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Support agents have Knowledge agent privileges by default. Support admins have Knowledge admin privileges. You can [give agents Knowledge admin privileges](https://support.zendesk.com/hc/en-us/articles/4408845823386) as needed.

This article covers the following topics:

- [Knowledge user roles overview](#topic_dvd_db5_nv)
- [Knowledge user privileges by role](#topic_glb_bts_zw)
- [Setting content viewing and editing access for agents](#topic_ccv_jts_zw)

Related articles:

- [Changing an agent's role to grant Knowledge admin privileges](https://support.zendesk.com/hc/en-us/articles/4408845823386)
- [Understanding Knowledge user permissions for content access](https://support.zendesk.com/hc/en-us/articles/4408827797274)

## Knowledge user roles overview

Knowledge supports the following user roles with different help center access privileges:

- **Anonymous user** is anybody who visits the help center without signing in.
- **End user** is somebody who has created an account and signed in to the help center.
- **Knowledge Viewer** is an internal staff member who has the same permissions as an end user. This person can view articles but cannot be granted edit and publish permissions.
- **Knowledge Agent** is any Support agent who can be granted [edit and publish permission](https://support.zendesk.com/hc/en-us/articles/4408827952538).

 If you have light agents, they can also create and edit articles where they have been given permission.

 Note: Permission for agents to view and edit knowledge base articles or community posts is not part of the role permissions, but is set at the article level for the knowledge base and at the topic level for community (see [Setting content viewing and editing access](#topic_ccv_jts_zw)).
- **Knowledge admin** has full privileges in Knowledge.
 All Support admins have Knowledge admin privileges.

For a list of specific permissions by role, see the next section [Knowledge user privileges by role](#topic_glb_bts_zw).

## Knowledge user privileges by role

The following table shows Knowledge user privileges by role.

Article creation, management, and publishing privileges are not determined by the user's role, but are determined by user permissions. For a complete list of agent privileges granted by user permissions, see [Understanding agent privileges for user management permissions](https://support.zendesk.com/hc/en-us/articles/4408827952538#topic_tmz_zrp_gfb).

Note: Some features listed in the table below require Community forums.

| Permission X indicates which actions are available for each user type. | Anonymous user (Anyone) | End-user (Signed-in users) | Knowledge viewer | Knowledge agent | Knowledge admin |
| --- | --- | --- | --- | --- | --- |
| **END USER ACTIONS** | | | | | |
| Manage subscriptions and requests (if available) | | X | | | |
| Comment on articles and posts (if enabled) | | X | X | X | X |
| Add posts to the community (if available) | | X | X | X | X |
| Vote on articles and posts | X (if anonymous voting is enabled) | X | X | X | X |
| Subscribe to articles and sections in the KB | | X | X | X | X |
| Follow posts and topics in the community (if available) | | X | X | X | X |
| **HELP CENTER SET UP** | | | | | |
| Customize the help center | | | | | X |
| Manage help center settings | | | | | X |
| **KB MANAGEMENT** | | | | | |
| Edit and publish permissions | | | | X (Where enabled. See [Setting content viewing and editing access for agents](#topic_ccv_jts_zw)) | X |
| View restricted content | | | | X (Where enabled. See [Setting content viewing and editing access for agents](#topic_ccv_jts_zw)) | X |
| Enable languages for the help center | | | | | X |
| Add, edit, or delete categories and sections | | | | | X |
| Reorder articles, sections, and categories | | | | | X |
| Edit or delete comments on articles | | | | | X |
| Create a ticket from a comment on a knowledge base article | | | | X | X |
| **COMMUNITY MANAGEMENT** (if available) | | | | | X |
| Set access restrictions on any community topic | | | | | X |
| Add, edit, or delete community topics | | | | | X |
| Reorder community topics | | | | | X |
| Pin or feature a community post | | | | | X |
| Close a community post for comments | | | | | X |
| Edit or delete comments on a community post | | | | | X |
| Change status of a community post | | | | | X |
| Create a ticket from a community post or comment | | | | X | X |
| Manage spam | | | | | X |
| Moderate user content | | | | | X |

## Setting content viewing and editing access for agents

Knowledge admins have full access to the help center, including the ability to view all articles and the ability to add, edit, and publish all content. These privileges are not part of the Knowledge agent role by default, but are set at the article level for the knowledge base and at the topic level for community.

For the knowledge base, see the following articles to set agent viewing and editing access:

- [Setting agent editing and publishing permissions on knowledge base articles](https://support.zendesk.com/hc/en-us/articles/4408834435738)
- [Setting view permissions on articles with user segments](https://support.zendesk.com/hc/en-us/articles/4408824005914)
- [Understanding agent privileges for user management permissions](https://support.zendesk.com/hc/en-us/articles/4408827952538#topic_tmz_zrp_gfb)

For community, see the following articles to set agent viewing and editing access:

- [Restricting access to help center community content](https://support.zendesk.com/hc/en-us/articles/4408845814170)
- [Allowing agents to edit and delete articles in community topics](https://support.zendesk.com/hc/en-us/articles/4408821305498)
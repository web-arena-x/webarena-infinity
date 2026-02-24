# Creating management permissions to define agent editing and publishing rights

Source: https://support.zendesk.com/hc/en-us/articles/4408827952538-Creating-management-permissions-to-define-agent-editing-and-publishing-rights

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Note: On Suite Growth and Professional or Guide Professional, edit and publish permissions are
assigned together to a user segment of agents. On Enterprise plans, editing and publishing
permissions are assigned separately, so that they can be assigned to different user
segments.

*Management permissions* define editing and publishing permissions for agents. You apply
management permissions to an article to determine agent editing and publishing access for that
article.

There is one pre-defined management permission, plus a pre-defined editor and publisher
permission that can be activated if you are on an Enterprise plan:

- **Admins** is active by default and gives only Knowledge admins edit and publish
  permission.
- **Editors and publishers** (Enterprise plans only), gives all agents and admins edit
  permission, but gives only Knowledge admins publish permission.

Depending on your account, you might also have an **Agents and managers** management
permission pre-generated for you. You can create custom management permissions as needed, up
to 200.

This article covers the following topics:

- [Creating management permissions for
  agents](#topic_hy2_zrp_gfb)
- [Understanding agent privileges by user
  management permissions](#topic_tmz_zrp_gfb)

## Creating management permissions for agents

Management permissions include editing and publishing permissions. You can grant management
permissions to any agents, including light agents, so that they can participate in the
article creation and management process.

To build management permissions, you choose a user segment. See [Creating user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) to give those agents editing and publishing
permissions. You then apply that management permission to the appropriate articles. You must
be a Knowledge admin to create management permissions.

**To create management permissions**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **User permissions**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_user_permissions.png)) in the sidebar.
2. Click **Management permissions**.
3. Click **Add new**.
4. Enter a name for this management permission.
5. In **Permissions**, select one or more existing user segments of agents or click
   **Add new user segment** to create a new user segment.

   The first five Staff user
   segments appear by default. If you do not see your user segment, start typing in the
   permissions box, and matching user segments will appear.

   - **On Suite Growth and Professional or Guide Professional**, you assign edit and
     publish permissions *together* to a user segment of agents.

     Agents with edit
     and publish permissions can view, create, and update articles, as well as submit
     for review, publish, unpublish, and archive articles, where this management
     permission is applied. See the [complete list of agent privileges.](#topic_tmz_zrp_gfb)
   - **On Enterprise plans**, you assign edit permissions and publish permissions
     *separately* to the same or different user segments of agents.

     Agents with
     edit permissions can view, create, and update articles, as well as submit articles
     for review where this management permission is applied. Agents with publish
     permissions have edit permissions, plus they can publish, unpublish, and archive
     articles. See the [complete list of agent privileges.](#topic_tmz_zrp_gfb)
6. Click **Create**.

After you create management permissions, you can apply it to an article to determine agent
editing and publishing access for that article. You can apply management permissions to
[an existing article](https://support.zendesk.com/hc/en-us/articles/4408839258778#topic_1rt_tdq_cy) or [a new article](https://support.zendesk.com/hc/en-us/articles/4408839258778).

Knowledge admins can apply any management permissions to an article, while agents can apply
only the management permissions they belong to.

## Understanding agent privileges by user management permissions

Management permissions include editing and publishing permissions.

Note: Remember, on Suite Growth and Professional or Guide Professional, edit and publish
permissions are assigned together and give agents one set of management privileges for
knowledge base articles. On Enterprise plans, editing and publishing permissions are
assigned separately and give agents separate edit and publish privileges knowledge base
articles.

The following table includes the complete list of agent privileges granted by edit and
publish permissions for each plan. An x mark (x) indictes which plans include the privilege.
Guide Legacy customers should refer to the Guide Professional column.

| **Privilege** | **Suite Team** | **Suite Growth and Professional** **Guide Professional** | **Suite Enterprise and Enterprise Plus** **Guide Enterprise** | | |
| --- | --- | --- | --- | --- | --- |
|  | **Edit and publish permissions** | **Edit and publish permissions** | **Edit permissions** | | **Publish permissions** |
|  |  |  | **New unpublished article** | **Existing published article** |  |
| Update title | x | x | x | x | x |
| Update section | x | x | x |  | x |
| Update labels |  | x | x |  | x |
| Update body | x | x | x | x | x |
| Update author | x | x | x |  | x |
| Add inline attachments | x | x | x | x | x |
| Remove inline attachments | x | x | x | x | x |
| Add translation | x | x | x | x | x |
| Delete translation | x | x | x |  | x |
| Set source translation | x | x | x |  | x |
| Flag translation | x | x | x | x | x |
| Add block attachment | x | x | x |  | x |
| Remove block attachment | x | x | x |  | x |
| Preview / Show in help center | x | x | x | x | x |
| Set management permissions | x | x | x |  | x |
| Set view permissions | x | x | x |  | x |
| Promote article | x | x | x |  | x |
| Open for comments | x | x | x |  | x |
| View revisions |  | x | x | x | x |
| Restore revision |  | x | x | x | x |
| Apply template |  |  | x |  | x |
| Preview | x | x | x | x | x |
| Create article | x | x | x | x | x |
| Submit for review |  |  | x | x | x |
| Assign |  |  | x | x | x |
| Approve |  |  |  |  | x |
| Publish | x | x |  |  | x |
| Schedule publishing |  |  |  |  | x |
| Unpublish | x | x |  |  | x |
| Archive article | x | x | x |  | x |
| Restore article | Admins only | | | | |
| Delete article | Admins only | | | | |
| View history | Admins only | | | | |
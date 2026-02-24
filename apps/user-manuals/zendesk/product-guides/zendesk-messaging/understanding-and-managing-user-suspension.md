# Understanding and managing user suspension

Source: https://support.zendesk.com/hc/en-us/articles/8009733465370-Understanding-and-managing-user-suspension

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins and authorized agents can suspend users who disrupt operations or spam. Suspended users can't sign in, create tickets, or receive notifications, and their requests go to the suspended queue. You can manage who can suspend users by adjusting role permissions. View and manage suspended users from the Customers page to maintain control over user interactions.

Admins and agents with permission can suspend end users who hassle agents or spam your organization, post repetitive content, send unsolicited or abusive messages, or otherwise take agents’ time and focus. Additionally, admins can suspend internal users (agents) when needed.

This article describes what happens when an end user is suspended, how admins can grant end-user suspension permission to agents, and how to identify suspended end users, and how conversations are managed when an end user is suspended. See [Suspending end users](https://support.zendesk.com/hc/en-us/articles/4408889293978) for information on suspending and unsuspending end users.

This article includes the following sections:

- [About suspended end users](#topic_erq_nfg_fhc)
- [Managing who can suspend users](#topic_j4d_cbs_xgc)
- [Viewing and managing the Suspended users list](#topic_czl_5gm_fdc)

Related articles:

- [Suspending end users](https://support.zendesk.com/hc/en-us/articles/4408889293978)
- [Suspending an agent’s account](../team-members-and-groups/downgrading-and-removing-an-agent.md#topic_zfr_vq5_w2b)
- [About banning IP addresses from messaging channels](https://support.zendesk.com/hc/en-us/articles/9418700382618)

## About suspended end users

End-user suspension permissions are determined by the role assigned to an agent. If an agent’s role allows them to edit [end-user profiles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_tep_mig_bd), they can also suspend messaging users. See [Managing who can suspend users](#topic_j4d_cbs_xgc) for more information.

When you suspend an end user:

- The *Suspended* tag is added to the [user’s profile](https://support.zendesk.com/hc/en-us/articles/4408835022490), their [user essentials card](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_q5j_kpz_vkb), and next to their entry in the Customers list.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_tag.png)
- The user can't sign in or create new tickets through any channel, or through the API.
- Users *aren't* notified that they have been suspended.
- New support requests received from the user’s registered identities are added to the suspended tickets queue.
- The user no longer receives notifications from help center articles or sections they follow.
- If a ticket requester is suspended, they won't receive email notifications for the ticket.
- Suspended CC'd users don't receive notifications. Additionally, any email replies they send are sent to the suspended tickets queue. If a ticket has multiple CC'd users and at least one of them is suspended, none of the CC'd users will receive notifications.
- A ticket won't be created if a suspended user calls any of your Zendesk phone lines.

Additionally, if the end user is suspended from a **messaging ticket**:

- The [related messaging session ends](https://support.zendesk.com/hc/en-us/articles/8009788438042).
- The conversation [becomes inactive](https://support.zendesk.com/hc/en-us/articles/7043034053658).
- The messaging channel option in *that ticket’s* composer is turned off. Agents can no longer add messages to the conversation.
- User messages in *that ticket’s* conversation are no longer added to the ticket.
- If your account is using [multi-conversations](https://support.zendesk.com/hc/en-us/articles/8195486407706), users can continue to interact with any other ongoing conversations as if they have not been suspended. This means that messages in these conversations from suspended users will be viewable by agents, and added to the conversation’s ticket.

If a user has active tickets when they are suspended, suspending them will not immediately block them from interacting with those tickets. They will no longer be able to reply to existing tickets when one of the following events occur:

- The [ticket status](https://support.zendesk.com/hc/en-us/articles/4408832151834#id_xsq_5f5_st) is updated to Pending, On-Hold, or Solved.
- The ticket is [Closed](https://support.zendesk.com/hc/en-us/articles/4408832151834).
- An agent [ends the ticket’s related messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042).
- The related messaging conversation [becomes inactive](https://support.zendesk.com/hc/en-us/articles/7043034053658).

## Managing who can suspend users

End-user suspension permissions are determined by the role assigned to an agent. If an agent’s role allows them to edit [end-user profiles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_tep_mig_bd), they can also suspend messaging users.

Note: By default, only the Admin system role can suspend end users. If you’re on a Suite Enterprise plan, you can create a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) to permit non-admins permission to suspend end users.

**To configure messaging user suspension permissions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Select or create a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) to configure for end-user suspension.
3. Scroll to the **People** section on the role’s configuration page, then under **Manage end users**, select one of the following:
   - **View only**, which allows agents to view the [Suspended user list](https://support.zendesk.com/knowledge/revisions/QnJhbmQ6MzYwMDAyMjU2OTIw/QXJ0aWNsZTo4MDA5NzMzNDY1MzcwOjU5/en-us?showDiff=true#topic_wqm_2b5_bdc) and details for each suspended user, but does not let them suspend users.
   - **Add, edit, and assume profiles in organizations they belong to**, which allows agents to suspend end users who are part of the same organization.
   - **Add, edit, and assume profiles for any end users**, which allows agents to suspend any end user.
   - **Add, edit, delete, and assume profiles for any end users**, which allows agents to suspend any end user.
4. Click **Save** at the bottom of the page.

## Viewing and managing the Suspended users list

Suspension details are available from the Suspended users list on the Customers page.

**To view suspension details for a user**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Customers** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.
2. Click **Suspended users** from the **Customer lists** to show a list of suspended users.
3. Find a user and select **Edit** from the options menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-suspend-list.png)

   Details about the suspended user appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-suspend-edit.png)

Additionally, you can search for suspended users on the [Customers page](https://support.zendesk.com/hc/en-us/articles/4408828129946) using the is\_suspended term.

For example:

- **is\_suspended:true Otis** returns all users named Otis who have been suspended.
- **is\_suspended:true** returns all users who have been suspended.

If you've just suspended a user, it might take a few minutes for the suspended user to be displayed in the list. Wait for a few minutes, then refresh your browser page.
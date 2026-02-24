# Creating private ticket groups and granting agents access

Source: https://support.zendesk.com/hc/en-us/articles/4988173561370-Creating-private-ticket-groups-and-granting-agents-access

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Create private ticket groups to control who can view specific tickets. Only agents in these groups can access the tickets unless added as a CC or follower. Admins and team leaders can view all private group tickets by default. To manage access, adjust permissions at the role level, ensuring agents have the necessary access to support their tasks effectively.

Location: Admin Center > People > Team >
Groups

[Groups](https://support.zendesk.com/hc/en-us/articles/4408886146842) are used to create collections of agents based on criteria those agents have in common. You can create private ticket groups to designate a group of team members who can see tickets with otherwise restricted access.

When a ticket is assigned to a private group, only agents who are members of that group can see the contents of the ticket, unless the agent is explicitly added as a CC or follower. If the agent is the requester they can't access the ticket in the Agent Workspace. Instead, they can access these tickets as an end user, either [through email or the help center](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_qgd_mqd_yy).

This article contains the following sections:

- [Creating private ticket groups](#topic_lvk_kz3_dvb)
- [Granting agents access to tickets in private groups](#topic_l21_rbj_dvb)

## Creating private ticket groups

You can make a group private to restrict access to the tickets assigned to it. You must be an admin or an [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to create groups.

**To create a new private ticket group**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Groups**.
2. Click **Add group**.
3. Enter a **Group name**.
4. Optionally, enter a **Description**.
5. Select **Make it private**. This can’t be undone.
6. If you want to make this the default group for your account, select **Set as default**.

   All new team members will automatically be assigned to this group.

   Note: Your account’s default group and a team member’s default group are two separate types of defaults. To learn more about this distinction, see [Changing the default group for your account or team member](https://support.zendesk.com/hc/en-us/articles/4408828237722).
7. Under Add group members, click the plus sign ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Groups_new_plus_sign.png) ) next to the name of the team member you want to add.

   Alternatively, you can click **Add all** to add all team members in the list to the group.

   To help find team members, you can search the list by team member name or email.
8. Continue to add team members as needed, then click **Save**.

   The new group is created and labeled as private.

**To convert an existing group to private**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Groups**.
2. In the list of groups, find the group you want to edit and click its name.
3. Select **Make it private**.

   Note: If you convert an existing group to private, you cannot make it public again.
4. Click **Save.**

   The new group is created and labeled as private.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Groups_new_index_page.png)

## **Granting agents access to tickets in private groups**

Access to tickets, including tickets in private groups, is [set at the role level](https://support.zendesk.com/hc/en-us/articles/4408882153882). Among [native agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_clf_k5q_qk), Admins and Team Leaders can see tickets in private groups by default. For custom roles, you can configure them to have access to tickets in private groups.

**To edit private ticket access for a role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. On the role for which you want to edit access, click the options icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Under **Tickets they can access**, make your changes to the ticket permissions.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ptg_role_permissions.png)

   Agents with *Requested by end users in their organizations* ticket access can still view private group tickets linked to their organizations.
4. Click **Save**.
# Viewing and managing team member group membership

Source: https://support.zendesk.com/hc/en-us/articles/4408821536794-Viewing-and-managing-team-member-group-membership

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Groups](https://support.zendesk.com/hc/en-us/articles/4408886146842#topic_iny_3jg_sz) are used to create collections of team members based on criteria those team members have in common. You can add or remove team members from the Groups page when you [create a new group](https://support.zendesk.com/hc/en-us/articles/4408894175130) or [edit an existing group](https://support.zendesk.com/hc/en-us/articles/4408821199258#topic_zhr_14b_wqb).

All team members must belong to at least one group. When you add a new team member, the team member is automatically added to your account’s default group.

Team members can belong to multiple groups. You can manage the groups that an individual team member belongs to, add or remove team members from groups in bulk, and change a team member's default group at any time in their profile.

This article contains the following sections:

- [Viewing group members](#topic_gg5_24p_cxb)
- [Adding group members](#topic_skt_qrs_4nb)
- [Removing group members](#topic_ddl_4rs_4nb)
- [Adding or removing team members from groups in bulk](#topic_dy3_zg3_zdc)
- [Updating group assignments from a team member's profile](#topic_khk_zsp_cxb)

Related articles:

- [About the Groups page](https://support.zendesk.com/hc/en-us/articles/4408831652890)
- [Changing the default group for your account or a team member](https://support.zendesk.com/hc/en-us/articles/4408828237722)

## Viewing group members

You can view group membership in two different ways:

- View all team members in a single group from a group's page
- View team members' group membership from the Team members page

### Viewing which team members are in a group

When you create a new group or edit an existing group, you can view and search for team members by name and email. You can also view team members' product access and Support roles, such as Admin or Light agent.

**To view team members in a group**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Groups**.
2. In the list of groups, click the group’s name.

   Under Group members, the list of team members in the group displays.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Groups_new_view_members.png)

   Under Add group members, a list displays the team members available to add to the group.

### Viewing which groups a team member is in

View your team members’ group membership from the Team members page.

**To view team member’s group membership**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
 **People** in the sidebar, then select **Team > Team members**.

 The default group associated with each team member appears in the Group column.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/team_members_group_brand_columns.png)

 If a team member belongs to multiple groups, click the **+more** link to view additional group memberships.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/group_team_member_multiple_membership.png)

## Adding group members

You can add team members to a group from the Groups page in Admin center.

**To add team members to a group**

1. Go to the [Groups page](https://support.zendesk.com/hc/en-us/articles/4408831652890#topic_nrp_yd1_mqb) and click a group's name to open it for editing.
2. Under Add group members, click the plus sign ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Groups_new_plus_sign.png) ) next to the name of the team member you want to add.

   Alternatively, you can click **Add all** to add all team members in the list to the group.

   To help find team members, you can search the list by team member name or email.
3. Continue to add team members as needed, then click **Save**.

   The team member(s) are added to the group. On the Groups page, the number of team members in the group is updated.

   Note: If you add more than 100 team members to a group, the number of members in the group may take a few moments to update.

## Removing group members

You can remove team members from a group from the Groups page in Admin center.

As a best practice, you should [reassign any tickets](https://support.zendesk.com/hc/en-us/articles/4408887127450) assigned to the team member being removed. If you don't reassign them, then tickets that aren’t closed are reassigned to the group (see [About removing group members](#topic_zt1_srp_cxb)).

Depending on how an admin has set up your account, you may be able to configure how a departing team member's solved tickets are automatically reassigned. See [Setting reassignment options for groups' solved tickets](https://support.zendesk.com/hc/en-us/articles/7431999772954).

**To remove team members from a group**

1. Go to the [Groups page](https://support.zendesk.com/hc/en-us/articles/4408831652890#topic_nrp_yd1_mqb) and click a group's name to open it for editing.
2. On the right side of the page under Group members, click the trash can icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png) ) next to the name of the team member you want to remove.

   Alternatively, you can click the Actions menu, then select **Remove all members**.

   To help find team members, you can search the list by team member name or email.
3. Continue to remove team members as needed, then click **Save**.

   The team member(s) are removed from the group. On the Groups page, the number of members in the group is updated.

   Note: If you remove more than 100 team members from a group, the number of team members in the group may take a few moments to appear updated.

### About removing group members

If an admin has turned on solved ticket reassignment, a departing team member's solved tickets are reassigned according to the options configured. The options for solved ticket reassignment can be configured at either the account or group level. See [Understanding solved ticket reassignment options](https://support.zendesk.com/hc/en-us/articles/7431999772954#topic_z2c_33f_3cc)
for more information.

When solved ticket reassignment options aren't configured, the following default behavior occurs when you remove a team member from a group without first reassigning their solved tickets:

- If the team member removing the other team member from the group is also a member of the group, tickets are reassigned to the team member who removed the other team member.
- If the team member removing the other team member from the group isn't a member of the group, tickets are reassigned to the first team member in the group with an active ID (excluding light agents and agents lacking permissions required to be assigned the tickets).

 Note: The first team member is the team member with the lowest user ID, based on when the agent account was created in Zendesk (the oldest active agent account).
 It is not based on when they were added to the group, or alphabetically by first or last name.
- If there are no other team members in the group, tickets are reassigned to the account owner.

## Adding or removing team members from groups in bulk

Because team members can belong to multiple groups, you can quickly manage any of the groups they belong to from the Team members page. You can add or remove up to 100 team members at a time from existing groups.

To manage the membership of a single group, see [Adding group members](#topic_skt_qrs_4nb) or [Removing group members](#topic_ddl_4rs_4nb) instead.

**To add or remove team members from groups in bulk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Search for the team members you want to update, then select them in the list.

   You can select one or more team members.
3. Click **Manage group membership**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_team_members_bulk_select.png)
4. In **Add to group** and **Remove from group**, select the groups you'd like to add or remove for the team member.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/group_membership_bulk_manage.png)

   Note that team members won’t be removed from their default groups. You can [change a team member's default group from their user profile](https://support.zendesk.com/hc/en-us/articles/4408828237722#topic_jsd_kss_4nb).
5. Click **Save**.

## Updating group assignments from a team member's profile

You can manage which groups a team member belongs to from their profile.

**To add a team member to a group from their profile**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Find the team member and click **Manage in Support**.
3. On the [team member's profile](../../agent-guide/customer-management-and-profiles/viewing-and-editing-your-user-profile-in-zendesk-support.md#topic_pvf_1yt_p1b), click in the **Groups** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/changingdefault_1.png)

   A list of groups appears with the groups the team member belongs to highlighted.
4. Select any groups you want to add the team member to.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/changingdefault_3.png)
5. (Optional) You can also change the team member's Default group if you want. See [Changing the default group for your account or a team member](https://support.zendesk.com/hc/en-us/articles/4408828237722).
6. Click **Close**.

**To remove a team member from a group from their profile**

1. (Optional) Reassign any tickets assigned to the team member being removed (see [About removing group members](#topic_zt1_srp_cxb)).
2. On the [team member's profile](../../agent-guide/customer-management-and-profiles/viewing-and-editing-your-user-profile-in-zendesk-support.md#topic_pvf_1yt_p1b), click in the **Groups** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/changingdefault_1.png)

   A list of groups appears with the team member's groups highlighted.
3. Deselect any groups you want to remove the team member from.
4. Click **Close**.
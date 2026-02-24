# Setting reassignment options for groups' solved tickets

Source: https://support.zendesk.com/hc/en-us/articles/7431999772954-Setting-reassignment-options-for-groups-solved-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

[Groups](https://support.zendesk.com/hc/en-us/articles/4408886146842#topic_iny_3jg_sz) are collections of team members based on criteria those team members have in common. When an agent is deleted, downgraded to an end user, or [removed from a group](https://support.zendesk.com/hc/en-us/articles/4408821536794-Adding-and-removing-team-members-from-groups#topic_ddl_4rs_4nb), their assigned tickets, including solved tickets, should be [reassigned](https://support.zendesk.com/hc/en-us/articles/4408887127450).

Admins can turn on automatic reassignment options that determine how departing agents' solved tickets are reassigned. For example, you may want their solved tickets to be reassigned randomly within a group or to a particular agent.

After turning on solved ticket reassignment options, you can set the default solved ticket reassignment behavior for all groups in your account. You can also allow reassignment behavior to be configured per group. Configuring options for each of your groups gives you the flexibility to choose the reassignment behavior that best suits your groups’ needs.

By setting automatic reassignment options, whether at the account-level or group-level, departing agents' solved tickets are automatically reassigned based on your selections and you don't have to manually reassign them.

This article contains the following topics:

- [Understanding solved ticket reassignment options](#topic_z2c_33f_3cc)
- [Turning on solved ticket reassignment](#topic_xk2_jhf_3cc)
- [Setting account-level reassignment options](#topic_fv5_cjf_3cc)
- [Setting group-level reassignment options](#topic_jyt_nlf_3cc)
- [Resetting all groups to the account-level option](#topic_u1k_5xv_zcc)
- [Viewing groups' reassignment options](#topic_x3g_bmf_3cc)

Related articles:

- [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130)
- [Managing groups](https://support.zendesk.com/hc/en-us/articles/4408821199258)

## Understanding solved ticket reassignment options

The original (legacy) behavior for reassigning solved tickets when an agent is deleted, downgraded to an end user, or removed, is to reassign their solved tickets to the admin removing them or the longest active team member in the group. On Enterprise plans, this could also be an [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to manage group membership.

The longest active team member is the team member with the lowest user ID. This is based on when their account was created in Zendesk; it is not based on when they were added to the group or alphabetically by first or last name.

After [turning on solved ticket reassignment](#topic_xk2_jhf_3cc), you can change how a departing agent’s solved tickets are reassigned with the following options:

| Reassignment option | Description |
| --- | --- |
| To an admin or longest active team member | Reassigns the departing agent's solved tickets to the admin removing them or the longest active team member in the group. On Enterprise plans, this could also be an [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to manage group membership. This option is the same as the original (legacy) behavior. |
| Reassign solved tickets to the group without any team member assigned | Reassigns the solved tickets to the group. No particular agent is assigned the solved tickets. |
| Reassign solved tickets to a random team member | Reassigns an agent’s solved tickets to a random agent within the group, distributing the attribution equally. |
| Reassign tickets to selected team member | Reassigns an agent’s solved tickets to a particular agent. This option appears only at the group level. |
| Reassign tickets to the account level setting | Reassigns an agent’s solved tickets based on your account’s default reassignment behavior. This option appears only at the group level. |

## Turning on solved ticket reassignment

An admin must first turn on solve ticket reassignment before you can change your group reassignment options.

**To turn on solved ticket reassignment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Solved ticket reassignment** to expand it.
3. Select **Turn on solved ticket reassignment**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/turn_on_solved_reassign2A.png)
4. Click **Save**.

   You can now set the [account-level reassignment behavior](#topic_fv5_cjf_3cc) or [turn on the option to configure reassignment options per group](#topic_g4b_xhf_3cc).
   Make sure you [understand what each option does](#topic_z2c_33f_3cc) before making any changes.

   If you turn off solved ticket reassignment after configuring reassignment options for your account or groups, the reassignment behavior for all your groups will revert back to the original (legacy) behavior. If you turn solved ticket reassignment back on, though, your previously configured options are saved and will reactivate.

### Turning on group-level reassignment options

An admin must turn on the option to allow reassignment options be configured per group.
When you turn on show solved ticket reassignment, the options appear on each groups’ admin page.

Note: You can turn this option on, configure the reassignment behavior for each of your groups, then turn this option off. The reassignment behavior you configure for each group persists; however, any new groups you create will inherit your account’s default reassignment option.

**To turn on group-level reassignment options**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Solved ticket reassignment** to expand it.
3. Make sure that **Turn on solved ticket reassignment** is selected.
4. Select **Show solved ticket reassignment**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/solved_reassign_show_groupA.png)
5. Click **Save**.

   The reassignment options now appear in each of your groups and can be configured. You may need to refresh the page for the options to appear when you navigate to a group's admin page for the first time after turning this on.

## Setting account-level reassignment options

An admin can set a default reassignment option for your account. When you select an option for your account, any new groups you create will follow the set reassignment option. Your existing groups will continue to follow the original (legacy) reassignment behavior unless you [reset all groups to the account-level option](#topic_u1k_5xv_zcc).

**To set an account-level reassignment option**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Solved ticket reassignment** to expand it.
3. Make sure that **Turn on solved ticket reassignment** is selected.
4. Click the drop-down menu and select an option.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/solved_reassign_account_level2A.png)

   See [Understanding solved ticket reassignment options](#topic_z2c_33f_3cc).
5. Click **Save**.

## Setting group-level reassignment options

If an admin has turned on the option for [show solved ticket reassignment](#topic_g4b_xhf_3cc), you can configure the reassignment behavior for each of your groups.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Groups**.
2. [Create a new group](https://support.zendesk.com/hc/en-us/articles/4408894175130) or select an existing group from the list to [edit](managing-groups.md#topic_zhr_14b_wqb).
3. In the **Solved ticket reassignment behavior** section, select one of the options.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_solved_tickets_reassignment.png)

   See [Understanding solved ticket reassignment options](#topic_z2c_33f_3cc).
4. Click **Save**.

## Resetting all groups to the account-level option

An admin can reset all groups to your account's default reassignment behavior. Resetting all groups to the account-level reassignment behavior means that any individual group-level options will no longer apply.

**To reset all groups to the account's default reassignment behavior**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Select **Force all the groups to assume the account level default now**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/reassign_solved_reset_all_groups.png)
3. Click **Save**.

   Your groups now follow your account's default reassignment behavior and the reassignment value for each of your groups is updated on the Groups page.

## Viewing groups’ reassignment options

If an admin has turned on the option for [show solved ticket reassignment](#topic_g4b_xhf_3cc), you can view each of your groups’ reassignment behavior from the Groups page. You can still view this information even if the option for show solved ticket reassignment is later turned off.

**To view your groups’ reassignment options**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
 **People** in the sidebar, then select **Team > Groups**.

 The Reassignment Value column displays each group’s reassignment option.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/solved_reassign_group_view.png)
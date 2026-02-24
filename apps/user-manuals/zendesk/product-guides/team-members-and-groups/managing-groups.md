# Managing groups

Source: https://support.zendesk.com/hc/en-us/articles/4408821199258-Managing-groups

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > People > Team > Groups

[Groups](https://support.zendesk.com/hc/en-us/articles/4408886146842#topic_iny_3jg_sz) are collections of team members based on criteria those team members have in common.

From the [Groups page](https://support.zendesk.com/hc/en-us/articles/4408831652890), you can view a group’s open tickets, edit your groups’ names, [add and remove team members from a group](https://support.zendesk.com/hc/en-us/articles/4408821536794), delete groups, and [change the default group](https://support.zendesk.com/hc/en-us/articles/4408828237722#topic_i4k_y4y_spb) for your account.

This article covers the following topics:

- [Viewing a group's tickets](#topic_bkf_23p_cxb)
- [Editing groups](#topic_zhr_14b_wqb)
- [Deleting groups](#topic_gmg_dpb_wqb)

## Viewing a group's tickets

You can view a group’s open tickets from the Groups page.

**To view a group’s open tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Groups**.
2. In the group’s row, click the **Options** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), then select **View open tickets**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Groups_new_open_tickets.png)

   A new tab opens and lists the group's open tickets.

## Editing groups

Edit your existing groups from the Groups page in Admin center.

**To edit a group**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Groups**.
2. In the list of groups, find the group you want to edit and click its name.

   Use the search bar to help find a group.
3. Make your changes. You can:
   - Search for and add team members to groups or remove team members from groups (see [Adding and removing team members from a group](https://support.zendesk.com/hc/en-us/articles/4408821536794)).
   - Change the group name.

     Note: Renaming a group has no effect on your business rules. Your business rules (triggers, macros, and automations) are automatically updated with the new name. See [Using groups](https://support.zendesk.com/hc/en-us/articles/4408839035546). However, renaming a group does impact Explore reports. If you [filter a report](https://support.zendesk.com/hc/en-us/articles/4408825475354) by a group name that is later changed, the report no longer returns the expected results because the filter continues using the previous group name. You must manually update report filters to select the new group name.
   - Change or add a group description.
   - (Enterprise only) Click **Make it private** to make the group private and convert all tickets assigned to the group to private. This can't be undone. See [About private ticket groups](https://support.zendesk.com/hc/en-us/articles/4767122732058).
   - Click **Set as default** to make this group the one that all new agents are automatically added to.

     Note: Your account’s default group and a team member’s default group are two separate types of defaults. To learn more about this distinction, see [Changing the default group for your account or team member](https://support.zendesk.com/hc/en-us/articles/4408828237722).
   - Click the **Actions** menu to view all open tickets, remove all team members from the group, or delete the group.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Groups_new_edit_page.png)
   - If an admin has turned on group level reassignment options, you can change how a departing agent's solved tickets are reassigned. See [Setting reassignment options for groups' solved tickets](https://support.zendesk.com/hc/en-us/articles/7431999772954-) to learn more.
4. Click **Save**.

## Deleting groups

You can delete groups you no longer need.

Before you delete a group, be sure to take the following actions, if necessary:

- **Reset the default group.** If the group is set as the default group for your account or as the default group for any team member, you need to change the default group for the account and team members (see [Changing the default group](https://support.zendesk.com/hc/en-us/articles/4408828237722)).
- **Reassign tickets assigned to the group.** You should reassign any tickets that are currently assigned to the group or to agents in that group to a new group. You can do this in bulk by finding all the tickets in [advanced search](https://support.zendesk.com/hc/en-us/articles/4408835086106) with the following search string:

  ```
  status<closed group:"Group Name"
  ```

When you delete a group, any business rules you set up using the deleted group will no longer function properly. If tickets are assigned to the group, the group is removed from those tickets along with any team members in the group and the ticket will return to unassigned. You can see these updates in the [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970#topic_wgg_hwn_scb).

**To delete a group**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Groups**.
2. In the list of groups, find the group you want to delete. You can use the search bar to help find a group.
3. In the group’s row, click the **Options** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), then select **Delete**.

   Alternatively, you can delete a group when you open it for editing by clicking the **Actions** menu, then selecting **Delete group**.

   A message appears asking if you are sure you want to delete the group.
4. Click **Delete**.
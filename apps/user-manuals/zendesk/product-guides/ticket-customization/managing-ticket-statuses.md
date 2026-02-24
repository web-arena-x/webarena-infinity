# Managing ticket statuses

Source: https://support.zendesk.com/hc/en-us/articles/4412575941402-Managing-ticket-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Tickets >
Ticket statuses

When you [activate custom ticket
statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), you can manage ticket statuses by editing,
activating or deactivating, and deleting ticket statuses. You can also
change the default ticket status of a category.

You must be an admin to manage ticket statuses.

This article includes these sections:

- [Editing ticket
  statuses](#topic_wqd_t1h_vrb)
- [Changing the default
  ticket status of a category](#topic_zgh_dbh_vrb)
- [Activating and
  deactivating a ticket status](#topic_qbl_32h_vrb)
- [Deleting custom ticket
  statuses](#topic_mpy_sfy_txb)

Related articles:

- [Creating custom ticket
  statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018)

## Editing ticket statuses

You can edit any ticket status, including standard ticket statuses and
custom ticket statuses. When you edit a ticket status name, the
change is reflected in your reports.

You must be an admin to edit ticket statuses.

**To edit a ticket status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket
   statuses**.

   The **Ticket statuses** page
   is displayed.
2. (Optional) Use the [search bar or
   filters](https://support.zendesk.com/hc/en-us/articles/4892092747162#topic_x3c_btn_q5b) to find the ticket statuses you
   want to edit.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_filters_button.png)
3. Move the cursor over a ticket status, then
   click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)).
4. Click **Edit**.

   The **Edit ticket
   status** page displays.

   Note: You can edit
   nearly all of the configuration options on this
   page; however, you can't move an existing ticket
   status to a different status category.
5. Configure the options for the status.

   For information
   about the options that appear on this page, see
   [Configuration
   options for ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018#topic_otl_drg_vrb).
6. Click **Save**.

### Editing a standard ticket status

Your standard ticket statuses include New, Open, Pending,
On-hold, and Solved. While standard ticket statuses can be
edited just like custom ticket statuses, they differ from
custom statuses because they include system placeholders by
default.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_standard_edit_placeholders.png)

When you edit your standard ticket statuses, these placeholders
are lost. If you'd like to reset a standard ticket status
with its original, default placeholders, refer to the
placeholders below. Where it says "statusname", replace that
text with the standard status name.

For example, if you wanted to reset the agent view name of the
New status you would enter
`{{zd.status_new}}`. To reset the end
user view of the New status, enter
`{{zd.status_end_user_new}}`.

**Standard ticket status default placeholders**

- **Name (agent view)**:
  `{{zd.status_statusname}}`
- **Description (agent view)**:
  `{{zd.status_statusname_description}}`
- **Name (end user view)**:
  `{{zd.status_end_user_statusname}}`
- **Description (end user view)**:
  `{{zd.status_end_user_statusname_description}}`

To learn more about placeholders, see [Zendesk Support
placeholders reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

## Changing the default ticket status of a category

After you’ve created at least one ticket status in a category, you can
change the default ticket status of the status category. Each status
category includes a default ticket status. This default ticket
status is used by your [standard triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346).

You must be an admin to change the default status of a category.

**To view the default ticket status of a category**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket
   statuses**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) on the right
   side and select **Default**.

   The Default column
   appears and the Default label is displayed in the
   row of each category’s default ticket
   status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cst_default_options.png)

**To change the default ticket status of a category**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket
   statuses**.
2. In the table, in the (first) heading row,
   click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) on the right
   side and select **Status category settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_sort_statuses.png)
3. Under the default ticket status of a category
   that you want to change, use the drop-down list to
   select the new default ticket status.
4. Click **Save**.

## Activating and deactivating a ticket status

Your account can have up to 100 ticket statuses, but it's recommended
that you limit the number of active ticket statuses in your account
to keep things manageable. All active ticket statuses appear in the
status picker, in the ticket interface.

Note: Deactivating a ticket status is not the same as deactivating the
entire custom ticket status experience. See [Activating custom ticket
statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306).

If you have more than 10 active ticket statuses, the status picker will
display the first 10 active ticket statuses. Agents will need to
scroll down to see the rest.

When a ticket status is deactivated, it's removed from the status picker
and agents will no longer be able to assign that status to tickets.
However, deactivating a ticket status doesn’t delete it and you can
reactivate it at any time. Any tickets using the deactivated ticket
status will still retain the status.

If you want to delete a ticket status, you must deactivate it first.

Admins can activate and deactivate ticket statuses.

**To activate or deactivate a ticket status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket
   statuses**.
2. Move the cursor over the ticket status, click the
   options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), and then click
   **Activate** or **Deactivate**.

## Deleting custom ticket statuses

After deactivating a custom ticket status, you can delete the status if
it’s not applied to any active tickets.

Active tickets are any tickets that aren’t in the Closed state. This
means that solved tickets that aren’t yet closed are considered
active tickets. To learn more about how tickets are solved and
closed when using custom ticket statuses, see [About closed tickets solved
with a custom ticket status](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zlx_pyk_fdc).

Check if your business rules (such as triggers and
automations) use a custom ticket status before deleting the status.
Business rules that use a deleted custom ticket status will not
run.

You must be an admin to delete custom ticket statuses.

**To delete a custom ticket status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket
   statuses**.

   By default, the filter for active ticket
   statuses is applied.
2. Click **Clear filters** to display deactivated ticket
   statuses.
3. Move the cursor over a custom ticket status, click the options
   menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), and then click
   **Delete**.

   The option to delete the ticket
   status only displays if the ticket status has been
   deactivated already.

   If the ticket status is
   being used on any active tickets, a message appears.
   Click **Cancel** to go back, then remove the
   status from any active tickets, including solved
   tickets that aren't closed.

   Note: You might
   experience a delay when deleting a status if you
   just updated active tickets to a different status
   from the custom ticket status you’re trying to
   delete. Wait a few minutes and then try
   again.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_delete_warn.png)

   If the ticket status isn’t
   being used on any active tickets, a confirmation
   message appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_delete_confirm.png)
4. Click **Delete**.
# Making conditional ticket fields required 

Source: https://support.zendesk.com/hc/en-us/articles/4408846008218-Making-conditional-ticket-fields-required

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Tickets > Forms

This article describes how to make a conditional field a required ticket field.
It also explains how ticket field and ticket form requirement settings in
your admin settings affect each other. You must be an admin to make
conditional ticket fields required.

This article includes these sections:

- [Finding requirement settings](#topic_b3l_wtk_1jb)
- [Ticket field requirement settings](#topic_x2s_g5k_1jb)
- [Conditional ticket field requirement settings](#topic_ijq_45k_1jb)
- [Making conditional ticket fields required](#topic_vdh_2vk_1jb)
- [Resolving unexpected alerts about required fields](#topic_szt_x4h_kkb)

## Finding requirement settings

You can find ticket field requirement settings in Admin Center
on both the Fields and Forms pages. If you want to make a
conditional field required, check the requirement settings in both
places to make sure everything is set correctly.

**To view ticket field requirement settings**

- Go to Admin Center > Objects and rules > Tickets > Fields, then open a ticket field for
  editing.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_fields_required_setting.png)

  See [Ticket field requirement
  settings](#topic_x2s_g5k_1jb) for more information.

**To view conditional ticket field settings**

1. Go to Admin Center > Objects and rules > Tickets > Forms.
2. Move the cursor over the ticket form whose conditions
   you want to view, then click the options menu
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ctf_menu_icon.png)) and select
   **Conditions**.
3. Click the expand icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_expand_icon.png)) to view the conditions
   on the ticket form.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_form_view_conditions.png)

See [Conditional ticket
field requirement settings](#topic_ijq_45k_1jb) for more information.

## Ticket field requirement settings

You can find ticket field requirement settings in Admin Center on the
Fields page when creating or editing a ticket field (see [Editing ticket
fields](https://support.zendesk.com/hc/en-us/articles/4408828883738#topic_vgj_3gw_jz)).

| Settings | Description |
| --- | --- |
| Required to solve a ticket  Required to submit a ticket | [**Required to solve a ticket** and **Required to submit a ticket** are settings on ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794) (from **Manage > Ticket Fields**). They can be overridden by conditional ticket fields.  On conditions for agents:   - If **Required to solve a ticket**   is enabled on the ticket field, **Require** is   automatically set to **When solved**. - Making a field **Required** makes   the field **Required to solve** in most cases.   Agents cannot solve the ticket until they complete   the required field.   On conditions for end users:   - If **Required to submit a ticket**   is enabled on the ticket field, **Required** is   automatically set to **On   submit**. - Making a field **Required** makes the field   **Required to submit a ticket**. End users   cannot submit the request until they complete the   required field. |

## Conditional ticket field requirement settings

You can find conditional ticket field required settings in Admin Center
on the Forms page when creating or editing a ticket form (see [Creating conditional ticket
fields and adding them to forms](https://support.zendesk.com/hc/en-us/articles/4408834799770#topic_vkc_tsl_rgb)).

| Settings | Description |
| --- | --- |
| Required | Use the **Required** drop-down list to specify when the field is a required field. By default, **Required** reflects the requirement setting on the ticket field (from **Manage > Ticket Fields**). You can manually clear the **Required** field, if you want to, which will make the ticket field optional on the ticket form. |
| Always | Selecting **Always** makes the field required in all cases, regardless of ticket status.  Note the following about how this settings works:   - When you select **Always,** all other   settings in the list are cleared. - Selecting **Always** has a different result   than selecting all of the ticket statuses in the   list (**When new**, **When open**, **When   pending**, **When on-hold**, **When   solved**). - When you select or clear all of the   ticket statuses in the list, **Always** doesn’t   automatically get enabled or disabled. - When **Required** is   **Always**, and the **Status** ticket field   (one of your system fields in your **Ticket   Fields** admin settings) is set to [**Enable on-hold   status**](https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-your-Zendesk#topic_kdz_5qn_b3), the field is required when the   ticket is **On-hold**. |
| Never | Selecting **Never** clears all of the ticket statuses in the list (**When new**, **When open**, **When pending**, **When on-hold**, **When solved**), including **Always**. |
| New  Open  Pending  On-hold  Solved | These are the standard ticket statuses. If selected, the ticket field is required when submitting the ticket with this status.  If you've [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), then additional ticket statuses may be available for selection. |

## Making conditional ticket fields required

Before you proceed, make sure you reviewed the rest of the
information in this article and understand how ticket field and
ticket form requirement settings affect each other.

You may want to open the ticket field for editing (go to Admin Center > Objects and rules > Tickets > Fields) and note whether **Required to solve a ticket** or
**Required to submit a ticket** are selected.

**To make conditional ticket fields required**

1. [Create a new
   condition for the ticket field](https://support.zendesk.com/hc/en-us/articles/4408834799770-Creating-conditional-ticket-fields-in-Zendesk-Support-Professional-Add-on-and-Enterprise-#topic_vkc_tsl_rgb) or go to Admin Center > Objects and rules > Tickets > Forms to edit an existing ticket form.
2. Move the cursor over a ticket form, then click the options menu
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ctf_menu_icon.png)) and select
   **Conditions**.
3. Click the expand icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_expand_icon.png)), then click the edit
   icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_edit_icon.png).
4. Select the requirement settings you want to use.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditional_ticket_form_required.png)

   Make sure you understand how
   the requirement settings you noted in step 1 will
   affect the behavior of your conditional ticket
   field. Clear any settings you don’t want to
   use.
5. If you are adding a new condition, click **Add**.
   If you are updating an existing condition, click
   **Update**.
6. When you are done, remember to click **Save** to
   save the changes to the ticket form. Otherwise, your changes
   will be lost.

## Resolving unexpected alerts about required fields

Your agents may encounter situations where they try to submit a
ticket, but then encounter an alert that states that a particular
field is still needed. For example, something like this:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ctf_alert_required_field.png)

This can happen even though the field didn’t appear to be
required.

The default ticket behavior may create a circumstance where a
field becomes required, even though it wasn’t originally marked in
the ticket interface as required (with an asterisk).

If you have questions about default ticket behavior (sometimes
called “system ticket rules”), we recommend that you review [About system ticket
rules](https://support.zendesk.com/hc/en-us/articles/4408894213018) to get a better understanding about how they
work.

**Example scenario**

Let’s say you have a group with only one agent in it. Then, you
create a new ticket that is routed to the group by a trigger. [The ticket status will
automatically become Open](https://support.zendesk.com/hc/en-us/articles/4408827594266) (instead of **New**) and
the agent will become the assignee (instead of the group).

If there is a conditional field that is required **When
Open**, you will see an alert when you try to submit the
ticket as **New**, if the required field was not filled out.
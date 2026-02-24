# Creating conditional ticket fields

Source: https://support.zendesk.com/hc/en-us/articles/4408834799770-Creating-conditional-ticket-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Tickets > Forms

You can create conditional ticket fields to control the appearance and behavior
of ticket fields in [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858). For example, you
can limit the number of ticket fields that appear in ticket forms, and
control the sequence in which ticket fields are presented to end users.

You must be an admin to create and manage conditional ticket fields.

This article includes these sections:

- [About conditional ticket
  fields](#topic_ydk_2b1_phb)
- [Creating conditional ticket fields and adding them to ticket forms](#topic_vkc_tsl_rgb)
- [About conditions and
  conditional statements](#topic_psv_cln_rgb)
- [Editing, duplicating, and
  removing conditional ticket fields on ticket
  forms](#topic_fqq_jvz_4hb)
- [How conditional ticket fields are saved](#topic_yr2_5pr_13b)
- [Using conditional ticket fields with Web Widget (Classic)](#topic_cr2_5pn_rgb)

## About conditional ticket fields

With conditional ticket fields, only the fields that admins want agents
and end users to see appear in [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858).
Initially, only a few fields appear in the form. As the user fills
in their answers, the form progressively adds sub-fields based on
the users’ answers. This helps you collect more granular and
relevant information about their problem or request.

For example, when you add a condition to a ticket form, you specify
whether the condition is for agents or end users.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_choose_role.png)

Conditions for agents affect ticket fields that appear in the agent
interface, as well as agent replies to tickets submitted through the
help center. When an agent submits a ticket as the requester, that
ticket's conditional fields must be fulfilled before agents can
reply to it in the help center.

Conditions for end users affect ticket fields in forms that appear in the
help center and [Web
Widget (Classic)](#topic_cr2_5pn_rgb).

By limiting the number of fields that initially display, you
make it so that agents and end users complete only the fields that
are required or relevant fields. This results in a better experience
and time-savings for both end users and agents.

## Creating conditional ticket fields and adding them to ticket forms

Adding conditions to ticket forms creates conditional ticket fields that
agents and end users encounter when they complete a ticket form.
Each form can have up to 1500 conditions per user type.

Note: If you delete a ticket form, the conditions associated with that form
are permanently deleted.

**To add conditions to ticket forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Move the cursor over the ticket form that you want to add
   conditions to, then click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ctf_menu_icon.png)) on the right side and
   select **Conditions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ctf_menu_conditions.png)

   A new page appears.
3. From the **Conditions for** drop-down list, choose a type of
   user (**Agents** or **End users**).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_choose_role.png)
4. To view the conditions that are already on the ticket form,
   click the expand icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_expand_icon.png)) to expand the
   sections.

   You can [edit, duplicate, and delete
   conditions](#topic_fqq_jvz_4hb) at this stage also, if you want
   to.
5. Click the **Add condition** button.
6. In the dialog box that displays, [create a conditional statement by
   defining these items](#topic_psv_cln_rgb). When you are done,
   click the **Add** button to add the condition to the
   ticket form.
   - When filling out this field
   - If value is
   - Then show these fields
   - Required (see [Making conditional
     ticket fields required](https://support.zendesk.com/hc/en-us/articles/4408846008218))

   The **Add another** check box causes the dialog
   box to remain open after you click the **Add**
   button, so that you can continue to add another
   condition, if needed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_add_another.png)
7. Once you are done, remember to click the **Save** button to
   save the changes to the ticket form. Otherwise, your changes
   are lost.

## About conditions and conditional statements

A *conditional ticket field* is a ticket field within a ticket form
that only appears to agents and end users some of the time, under
certain circumstances. Those circumstances are defined by the admin
in a condition (or condition statement), which is an if-then
statement, or rule, that is associated with a specific ticket
form.

For example, notice that the words *if* and *then* are used in
the interface where the admin creates a condition for end users.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_ifthen_enduser.png)

The same thing happens with conditions for agents. If-then statements are
always part of creating conditions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conditions_ifthen_agents.png)

It's important to note that **Required** is different depending on
whether the condition is for an end user or an agent (see the
screenshots above). For more information about these differences,
see [Making conditional ticket
fields required](https://support.zendesk.com/hc/en-us/articles/4408846008218).

This table explains the parts of a conditional statement in more
detail.

| Setting | Description |
| --- | --- |
| When filling out this field | Specify a field that you want to apply conditions to. This will be the “conditional ticket field.”  These are the types of fields you can select and apply conditions to:   - Drop-down fields (values   selected) - Check boxes (checked or not) - Text fields (specific strings) - Multi-line text fields (specific   strings) - Priority field (values   selected) - Ticket type field (values   selected)   For a field to appear in this list, it must have already been [added to the ticket form](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_h4l_mkp_knb). |
| If value is | Specify the value that the conditional ticket field (as defined in **When filling out this field**) must be in order for other fields to appear in the ticket form. |
| Then show these fields | Specify fields that will appear when the conditional ticket field (as defined in **When filling out this field**) is set to the correct value (as defined in **If value is**).  You can specify any fields on the ticket form, except for:   - Subject - Description   For a field to appear in this list, it must have already been [added to the ticket form](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_h4l_mkp_knb). |
| Required | For information about making a conditional field required, and how ticket form requirement settings in your admin settings affect each other, see [Making conditional ticket fields required](https://support.zendesk.com/hc/en-us/articles/4408846008218). |

You can't apply conditions to the *system fields* described in [About ticket fields](../ticket-management/about-ticket-fields.md),
except for Priority and Type. You also can't apply conditions to
these type of *custom fields* described in [Adding custom fields to your
tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794):

- Multi-select
- Numeric
- Decimal
- Date
- Regex
- Lookup relationship

## Editing, duplicating, and removing conditional ticket fields on ticket forms

You can edit or remove conditions on ticket forms. You can also duplicate
an existing condition, edit the duplicate, and then save the
duplicate as a new condition on the same ticket form. However, you
can't copy and paste a condition into another ticket form.

**To manage your conditional ticket fields**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Move the cursor over the ticket form where you want to manage
   the conditions, then click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ctf_menu_icon.png)) on the right side and
   select **Conditions**.
3. Click any of the following icons to edit, duplicate, or delete
   the selected condition:

   |  |  |
   | --- | --- |
   |  | Use the edit icon to change a condition. Make your changes in the dialog box that appears, and then click the **Update** button. |
   |  | Use the duplicate icon to duplicate (copy) a condition. Modify the duplicate in the dialog box that appears, and then click the **Add** button.  The reason you have to modify the duplicate is because the **If value is** part of the condition statement must be unique (you can’t use the value in another condition on the ticket form). |
   |  | Use the delete icon to delete a condition. |

## How conditional ticket fields are saved

Selections from conditional ticket fields are retained while
you remain in the ticket, even if you make a field invisible, or
change the ticket form. However, when you submit the ticket, only
the fields that are visible are saved. If you exit, then re-enter a
ticket, any unsaved field selections are not retained.

If you want to save all conditional ticket field selections you
make on a ticket, you must submit the ticket while each field you
want to save is visible.

**Example:**

You have three drop-down ticket fields, **Parent**, **Child
1**, and **Child 2**.

1. From the **Parent** drop-down list, select **Show child
   1** and select **Susan** for the **Child 1**
   field value.

   ![Custom field example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cf2-save.png)
2. Without submitting the ticket, select **Show child 2** from
   the **Parent** drop-down list and select **Peter** for
   the **Child 2** field value.

   ![Custom field example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cf1-save.png)
3. With **Show child 2** selected, submit the ticket.

   **Show child 2** and **Peter** are
   saved. However, you can select **Show child 1**
   and see that the value **Susan** is
   retained.
4. Without submitting the ticket, exit and re-enter the
   ticket.

   Now, under **Show child 1,** the value
   **Susan** is empty. This is because you never
   submitted the ticket and saved this value while
   **Show child 1** was displayed.
5. With **Show child 1** displayed, and **Susan** selected,
   submit the ticket to save these values.

   Now,
   whenever you exit and re-enter the ticket, the
   values for both **Show child 1** and **Show
   child 2** are retained because you submitted the
   ticket and saved each of these values while they
   were visible.

## Using conditional ticket fields with Web Widget (Classic)

If a ticket form includes conditional ticket fields, and ticket forms are
enabled in Web Widget (Classic) from your admin settings,
conditional ticket fields are presented to end users in Web Widget
(Classic).

Web Widget (Classic) supports most native conditional ticket fields (but
not from the [Conditional Fields
app](https://support.zendesk.com/hc/en-us/articles/203662476)). The **Priority** and **Type** fields are not
supported in Web Widget (Classic). If you apply conditions to these
fields, they appear in the agent interface and in ticket forms that
appear in the help center, but not in Web Widget (Classic).

**To confirm that tickets forms are enabled in Web Widget
(Classic)**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
  **Channels** in the sidebar, then select **Classic > Web Widget**.

For more information about using ticket forms in the Web Widget
(Classic), see the section about ticket forms in [Configuring components in Web
Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258), and [Using custom ticket fields
and ticket forms with Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408834218522).
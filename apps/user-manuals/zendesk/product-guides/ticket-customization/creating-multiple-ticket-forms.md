# Creating multiple ticket forms

Source: https://support.zendesk.com/hc/en-us/articles/4408846520858-Creating-multiple-ticket-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Tickets > Forms

Admins and [agents in custom roles with
permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create multiple ticket forms to support
different request types from customers. A ticket form is a set of predefined
ticket fields for a specific support request.

The ticket form determines the fields and data a ticket contains and the order in
which these fields appear in a ticket. If custom ticket statuses have been
activated in your account, admins can also associate certain ticket statuses
to specific forms so that only relevant statuses are displayed to agents.
See [About form ticket
statuses](https://support.zendesk.com/hc/en-us/articles/7755811560346).

You can create up to 300 ticket forms in your account.

This article contains the following topics:

- [Creating ticket
  forms](#topic_srd_k3b_lk)
- [Cloning ticket
  forms](#topic_uq3_4dc_cdb)

Related articles:

- [Editing and managing ticket
  forms](https://support.zendesk.com/hc/en-us/articles/5494868102426)

## Creating ticket forms

You can create multiple ticket forms for different support requests. For
example, you might create different forms, with different fields,
for different products. Or you might create different forms for
different workflows, such as "Hardware request" or "Refund
request."

Forms can be visible to end users and agents or to agents only. If
multiple forms are visible to end users, then end users choose the
appropriate form to submit their request.

Ticket field properties are set at the field level, not the form level.
So a ticket field's properties will be the same in all ticket forms
where the field appears. You cannot set form-specific properties for
a field.

For example, if you set a field to be required, it will be required on
all ticket forms where it is used. You cannot make the same field
required on one form but optional on another form.

You can use conditional ticket fields to hide and show fields in your
ticket forms (see [Creating conditional ticket
fields](https://support.zendesk.com/hc/en-us/articles/4408834799770)).

Tip: Before you start, see our guide for designing
ticket forms, [Optimizing your
ticket forms for a better agent and end user
experience](https://support.zendesk.com/hc/en-us/articles/4408882701338?option=2).

**To create a ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click **Add form**.
3. Click **New form** to edit the name of the ticket
   form.

   This is the name agents see from the ticket
   form drop-down list in the ticket
   interface.
4. If you want the form to be visible to end users, select
   the **Editable for end users** check box.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_editable.png)

   If you
   want the ticket form to appear to end users with a
   different name, enter the name into the **Title
   shown to end users** field. This is the name end
   users see in the support request form drop-down
   list.

   If you select **Editable for end
   users**, but don't enter an end user name for
   the form, the agent form name is used as the end
   user form name.
5. If you want to restrict the form to specific brands,
   deselect **Apply to all brands** and use the
   field below the check box to select the brands that
   should use this form. For more information, see
   [Branded ticket forms](https://support.zendesk.com/hc/en-us/articles/4408822414490).

   Tip: You cannot set a default ticket
   form for a group, but you can create a trigger
   that sets the "Ticket: Form" property. This
   enables you to set the ticket form based on the
   conditions you choose after a ticket is
   created.
6. Drag any ticket field from the right side, and drop it
   onto the ticket form on the left side, to add it to
   the ticket form.

   Alternatively, click the **Plus
   sign** (+) to add a ticket field to the
   form.

   You can also search for the ticket
   field you want to add and sort fields by various
   criteria (name, date modified, date created).

   Note: You can only add *active* ticket fields
   to a ticket form. If you want to add a field that
   is not available, you need to [activate that
   ticket field first](https://support.zendesk.com/hc/en-us/articles/4408832419738).
7. If you want to remove a ticket field from the form,
   click the **X** to remove it.

   By default, the
   ticket form includes several system fields. Of the
   system fields, only Type and Priority can be
   removed.
8. Drag ticket fields on the form to rearrange them.
9. Click **Save**.

The new ticket form appears in the list of active ticket forms.

If you create multiple ticket forms that are visible to end users, you
can customize the instructions that end users see for ticket forms
to help them choose the correct form. For more information, see
[Presenting ticket forms to end
users](https://support.zendesk.com/hc/en-us/articles/4408842873498).

## Cloning ticket forms

Cloning a ticket form creates a copy that you can modify and use for some
other purpose.

**To clone a ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Move the cursor over the ticket form that you want to clone and
   then click the menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_menu_icon.png)) on the right side when it
   appears.
3. Click **Clone**.

   The clone is immediately created and saved
   to your list of ticket forms. A page where you can
   make edits to the clone appears.
4. Change the name of the clone.

   The title of clone is the same
   as the parent (the ticket form you used to create
   the clone), unless you change it.
5. Update the clone as described above, in [Editing ticket
   forms](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_c5x_l3b_lk).
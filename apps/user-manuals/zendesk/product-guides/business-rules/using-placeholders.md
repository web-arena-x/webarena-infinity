# Using placeholders

Source: https://support.zendesk.com/hc/en-us/articles/4408887218330-Using-placeholders

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Placeholders are references to ticket, user, and [custom](https://support.zendesk.com/hc/en-us/articles/5914453843994) data that you include in the subject and body of email notifications. Without them it would be impossible to create automated messages. When you specify placeholders, remember they are case sensitive. For the complete list of placeholders see [Placeholder reference for business rules](https://support.zendesk.com/hc/en-us/articles/4408886858138).

Support includes [system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018) that suppress placeholders in ticket triggers in certain situations. System ticket rules are predefined rules that you cannot change, modify, or override, which dictate the standard behavior of Support. These rules may sometimes make it seem like placeholders in ticket triggers failed to work, but this isn’t a mistake. These rules protect you because they prevent spammers from using your account to distribute spam messages. See [Understanding placeholder suppression rules](https://support.zendesk.com/hc/en-us/articles/4408833443226).

This article includes these sections:

- [Using placeholders in business rules](#topic_qyc_zyb_4fb)
- [Using placeholders for custom fields](#topic_nfp_nja_vb)
- [Using placeholders for checkbox custom fields](#topic_nfn_yxq_j2b)

Related articles:

- [Zendesk Support placeholders reference](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-placeholders-reference)
- [Understanding placeholder suppression rules](https://support.zendesk.com/hc/en-us/articles/4408833443226)

## Using placeholders in business rules

Placeholders can be used in some, but not all, business rule actions.
When placeholders are supported, a **View available placeholders** button is visible beneath the field.
Placeholders are formatted within matched double curly brackets.
Usually they are used in notification messages and reference ticket properties. If a placeholder references a field that doesn't have a value, the placeholder is blank in the automation, trigger, or macro.

Here’s an example of how placeholders are used in an email notification:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/placeholders.png)

For the complete list of placeholders, and where they can be used, see [Zendesk Support placeholders reference](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-placeholders-reference). If you want more control on how placeholder data is selected and displayed, see [Understanding Liquid markup](understanding-liquid-markup-and-zendesk-support.md).

### Using placeholders in macros

When you apply a macro containing a placeholder to a ticket, the placeholder is evaluated according to what is currently true about the ticket. If the output of the evaluation returns any information, it is added as a ticket comment. For example, if a macro that returns the ticket ID is run on a ticket that has not been saved (and therefore has no ticket number yet), the ticket comments aren't updated. The macro is not re-evaluated when the ticket is saved. You could manually add the placeholder to the ticket using the placeholder {{ticket.id}}. This would allow it to be evaluated when you submit the ticket, and the value returned by the placeholder would be added to the ticket comments.

When using macros with [problem and incident tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898), you often need use a backward slash (\) to escape the placeholder so that it populates the appropriate value within the related incident tickets. For example: `Hello \{{ticket.requester.first_name}}`

## Using placeholders for custom fields

Placeholders are generated automatically, based on the ticket, current user, and custom object properties. These are referred to as system placeholders.

When you add custom fields for tickets, users, organizations, and custom objects, they are also available as placeholders. You can use placeholders for your custom fields as you would any other system placeholder. Every custom field has a unique ID or key. When you create a custom ticket field, the ID is automatically generated for you. When you create a custom user, custom org, or custom object field, you enter a unique key that cannot be edited once it is set.

Custom fields are not included in the list of available placeholders, but all custom fields [except drop-downs](#topic_wcz_x5s_rbc) follow this simple naming pattern that references their unique ID or key.

| | |
| --- | --- |
| Ticket custom fields | {{ticket.ticket\_field\_*<field ID number>*}} |
| User custom fields | {{ticket.requester.custom\_fields.*<field\_key>*}} |
| Organization custom fields | {{ticket.organization.custom\_fields.*<field\_key>*}} |
| Custom object fields | {{custom\_object.*<object\_key>*.custom\_fields.*<field\_key>*}} |

For example, a custom ticket field like this has the following placeholder:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/placeholder_custom_field.png)

```
{{ticket.ticket_field_505156}}
```

### Using placeholders for a custom drop-down field

The placeholder name for the options in a custom drop-down list follows a different pattern. There's only one placeholder for all four drop-down list options because this is a reference to the option that was selected. The ID is for the custom drop-down list because options do not have IDs.
Again, this is a reference to the single option that was selected.

| | |
| --- | --- |
| Ticket custom drop-down fields Ticket custom multi-select fields | - To display the value of the selected option,   use: {{ticket.ticket\_field\_option\_title\_*<field   ID number>*}} - To display the tags associated with the   selected option,   use: {{ticket.ticket\_field\_*<field ID   number>*}} |
| User custom drop-down fields | {{ticket.requester.custom\_fields.*<field\_key>*.title}} |
| Organization custom drop-down fields | {{ticket.organization.custom\_fields.*<field\_key>*.title}} |
| Custom object drop-down fields | {{custom\_object.*<object\_key>*.custom\_fields.*<field\_key>*.title}} |

Note: Take note of the syntax, as the placement of *title* in the placeholder varies, depending on the type of custom field.

For example, the placeholder for a drop-down list for a custom ticket field would look like this:

`{{ticket.ticket_field_option_title_515416}}`

To locate the custom field ID or key, see [Finding the field key or field ID for a custom field](https://support.zendesk.com/hc/en-us/articles/9199731160474).

### Using placeholders for a custom lookup relationship field

Lookup relationship fields are a type of custom field that is used to define relationships between objects. They are supported for all of the standard Zendesk objects (tickets, users, and organizations) and custom objects.

In addition to using placeholders to surface data related to the primary object, such as a ticket requester's name, you can also use placeholders to surface data in related records.
For example, if you have a ticket with a lookup relationship field that points to a user, you could use placeholders to reference data about that user. Similarly, you could use a placeholder to reference ticket data through a custom object's lookup relationship field and vice versa. For the purposes of these placeholders, the standard ticket *requester* and *organization* fields are treated as lookup relationship fields.

To reference data in related records, use the lookup relationship field's field key. This will follow the pattern for custom fields. See [examples](#topic_b4k_1zn_zbc).

You can also use placeholders supported for the target object in a lookup relationship field. For example, a lookup relationship field that points to users can leverage the [user data placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138#topic_qdz_opl_rc).

Placeholders referencing data through a ticket lookup relationship field can be used in ticket triggers and macros. Placeholders referencing data through custom object lookup relationship fields can be used in object triggers.

#### Examples of using placeholders to retrieve data from related records

**Working with the ticket *Requester* field**

For example, the *Requester* field in a ticket is functionally a lookup relationship field pointing to a user. If you've defined a user lookup relationship field with a field key of *manager* that points to another user, then you could use the following placeholder to display the asset requester's manager's name:

`ticket.requester.custom_fields.manager`

You could also take it one step further because you're working with the ticket requester field, and create a side conversation email to the ticket requester's manager using the following placeholder:

`ticket.requester.custom_fields.manager.email`

This is great for approval workflows, where you might need to notify the manager or get the manager's sign-off.

**Working with custom organization lookup relationship fields**

The *Organization* field is another standard ticket field that is functionally a lookup relationship field pointing to an organization. You could use organization lookup relationship fields to associate an organization with a custom object named *contract*. Then you could leverage the ticket's *organization* field to retrieve data from the contract record associated with the organization, which itself (the organization) is associated with the ticket, and use the following placeholder to communicate the contract's end date:

`{{ticket.organization.custom_fields.contract.custom_fields.end_date}}`

Both the *requester* and *organization* ticket fields are special cases because they are standard ticket fields that function as lookup relationship fields. Therefore, you can go two "hops" deep with the lookup relationship field placeholders to retrieve data from a record related to the record related to the primary object. In the example above, the ticket is the primary object, the ticket's organization is the first "hop", and the contract record related to the organization is the second "hop."

When dealing with custom lookup relationship fields, you can go only one "hop" deep into the record directly related to the primary object.

**Working with custom lookup relationship fields**

An example of working with custom lookup relationship fields might be a ticket lookup relationship field with a field key of *2698798899085* that points to a custom object named *Order*. The order object has a custom drop-down field with the field key *order\_status*. To reference the status of the order record that's associated with the ticket, use the following placeholder:

`{{ticket.ticket_field_2698798899085.custom_fields.order_status.title}}`

When working with drop-down fields, you must include `.title` in the placeholder to return the selected value.

### Using placeholders for a custom checkbox field

You can use placeholders in combination with [Liquid markup](understanding-liquid-markup-and-zendesk-support.md)
to verify if a checkbox (custom field) has been selected on a ticket and provide customized output based on the checkbox status (selected or not selected).

When you use Liquid markup `if/else/case` statements for checkbox custom ticket fields, remember that the checkbox field has a value of **0** or **1**, not **false** or **true**. For example:

```
{% if ticket.ticket_field_<insert field_id here> contains 1 %}
checkbox is checked
{% else %}
checkbox is unchecked (or null)
{% endif %}
```
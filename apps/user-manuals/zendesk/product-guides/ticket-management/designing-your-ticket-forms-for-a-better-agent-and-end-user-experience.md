# Designing your ticket forms for a better agent and end-user experience

Source: https://support.zendesk.com/hc/en-us/articles/4408882701338-Designing-your-ticket-forms-for-a-better-agent-and-end-user-experience

---

Suite | Any plan

Support | Any plan

At least one ticket form, also referred to as a contact form, is available in all Zendesk Support plans and provides your end users with an easy way to request support by entering data into a simple form.

You can create custom ticket fields to customize your ticket form. This means that you can tailor your ticket form to collect the kinds of data you want when an end user requests support. For example, you might want to prompt them to select the product they’re using from a predefined list.

You can also create multiple ticket forms and use conditional ticket fields. Having multiple ticket forms enables you to present different forms to your end users, who can then choose the ticket form that best suits the type of support they are requesting. Conditional fields allow you to control the appearance and behavior of ticket fields in your ticket forms.

This article explains how ticket forms and custom ticket fields work, what your end users see when they use a ticket form, what your agents see in the ticket interface, and how to use the data captured by ticket forms and custom fields to automate your support workflow.

This article covers the following topics:

- [Understanding ticket forms and how they look to your end users and agents](#topic_c5r_f4t_3mb)
- [Customizing ticket forms](#topic_kkt_drt_3mb)
- [Using custom ticket fields to route and view tickets](#topic_djh_mvt_3mb)

- [Understanding ticket forms and how they look to your end users and agents](#topic_c5r_f4t_3mb)
- [Customizing ticket forms](#topic_kkt_drt_3mb)
- [Using custom ticket fields to route and view tickets](#topic_djh_mvt_3mb)
- [Using multiple ticket forms](#topic_mjk_hxt_3mb)
- [Using conditional ticket fields in your ticket forms](#topic_qkq_txt_3mb)

## Understanding ticket forms and how they look to your end users and agents

All Zendesk Suite and Support plans include at least one pre-defined ticket form: *Default ticket form*. This ticket form is designed for general customer service requests and can be used as-is or [modified](https://support.zendesk.com/hc/en-us/articles/5494868102426) with custom ticket fields. Custom fields in a ticket form provide an excellent way to gather any unique information needed to properly route and resolve incoming tickets.

On Employee Service Suite plans, the following ticket forms, designed for common HR and IT scenarios, are also pre-defined and can be [used](https://support.zendesk.com/hc/en-us/articles/9012803758362) out of the box, [modified](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_h4l_mkp_knb) with custom ticket fields, or [deactivated](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_y1x_1bc_cdb) if not needed:

- [SAMPLE] New hire onboarding
- [SAMPLE] General HR inquiry
- [SAMPLE] Payroll question
- [SAMPLE] Leave request
- [SAMPLE] Parental leave questions
- [SAMPLE] New laptop request
- [SAMPLE] Software access
- [SAMPLE] Hardware/software issue

In addition to the standard ticket forms, some plans allow you to [create custom ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858). When using multiple ticket forms, you can create even more customized and targeted prompts for support information details. For example, you can present your end users with a drop-down list of support categories that, when selected, displays the ticket form that has been customized for that request type. A support request for a Product issue could then be much more detailed, containing custom fields relevant to that type of support issue.

An example of this is a custom form specifically for billing issues, which would include custom ticket fields such as a Purchase Order Number, Account Number, and Account Name.

![custom form example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_custom_form_billing.png)

Compared to simply providing your customers with an email address to send an email message to, the ticket form imposes a structure on the support request (in other words, here are the data fields that you need to complete to submit a support request to us). Using the ticket form, you can eliminate the email channel altogether, if you prefer this method of requesting support.

### How end users see your ticket form

Your ticket form can be presented to your end users in two ways: via your help center on the **Submit a request** page and by using the Web Widget (Classic) to place your ticket form on any website you choose.

![submit request form](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_submit_request_form.png)

This example shows the default ticket form, showing the default (system) fields. This is the version you have in your Zendesk Support account before you’ve added any custom ticket fields to it.

Web Widget (Classic) displays your ticket form embedded into your website. It also enables you to include other help center features such as access to your knowledge base and live chat.

![submit support request web widget](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_enduser_leavemsgattatchment_selected.png)

For more information about the features of Web Widget (Classic), see [Using Web Widget (Classic) to embed customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218).

### What your end users see when you’re using multiple ticket forms

When you’re using multiple ticket forms, your end users are first presented with a drop-down list with options. Each option displays a separate ticket form.

![mutlipe ticket forms](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticketforms_end_user.png)

After they’ve chosen an option, the ticket form is displayed and they can enter and submit their support request.

Web Widget (Classic) also displays these options as a list that end users must select before a ticket form is displayed.

![mutliple ticket forms web widget](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_tkt_form_ex.png)

For more information about using multiple ticket forms with Web Widget (Classic), see [Using custom ticket fields and ticket forms with Web Widget (Classic).](https://support.zendesk.com/hc/en-us/articles/4408834218522)

### How your agents view ticket form data in Support

The data that was collected when the ticket form was submitted becomes elements of the ticket that is created. The subject field becomes the subject in the ticket, the description becomes the body of the message, the requester’s name and email address (if not matched to an existing end user in your Support account) becomes a new user record that is paired with the ticket.

When your ticket form contains a custom field, that data is added as additional data in the ticket (added to the ticket sidebar). For example, if you added a custom drop-down field for your end users to select from, that field is also shown in the ticket sidebar for agents to see.

![ticket fields agent view](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_ticket_form_custom_field_example.png)

When you’ve captured this data, you can use it in your business rules, to create views, and to include in reports. See [Using custom ticket fields to route and view tickets](#topic_djh_mvt_3mb) below.

When using multiple ticket forms, the ticket form that was used to submit the request is displayed in the ticket forms drop-down in the ticket interface.

![multiple forms agent view](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_ticket_form_dropdown.png)

Any custom fields that were included in the selected form are also shown in the ticket sidebar, same as the example above.

## Customizing ticket forms

You customize what data to include on your ticket form by creating custom ticket fields and adding those fields to your ticket form. You also have a number of options for if and how your custom fields are displayed to end users and agents.

To create or modify ticket forms, you first need to ensure all of the ticket fields you need have been created. Ticket fields are the building blocks for your ticket forms. See [About ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098) and [Adding custom fields to your tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794).

![ticket system fields](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_ticket_fields_system_fields.png)

The system fields include essential support request data. The subject and description fields are always required and cannot be removed from the ticket form, although you can rename them. The other system fields are used after the support request has been submitted via the ticket form and a ticket is created. For example, after a new ticket is received, it is assigned to an agent or group, its priority can be set and so on. These are not shown to end users on the ticket form.

### Creating custom ticket fields that end users interact with

To add custom ticket fields that you want end users to enter data into, you must make the custom ticket field visible to end users.

Focus on the essential data that will help you best determine what exactly your end users need help with. You don’t want to overload your form with lots of fields because that might prevent your end users from completing the form. Keep your ticket form as short and simple as possible. We recommend that you include no more than 10 to 12 fields in total, and that you name your custom ticket fields with your customers in mind. Don’t use industry jargon in your ticket field titles.

When [creating custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794) to be used in your ticket forms, you'll do the following:

1. [Choose your custom field type](#topic_dc2_qst_3mb__ol_igh_1yd_fdc).
2. [Set visibility permissions for the field](#topic_xmq_d5t_3mb).
3. [Indicate whether the field is required to submit a request](#topic_mh5_q5t_3mb).
4. [Indiciate whether the field is required to solve a ticket](#topic_dk1_cvt_3mb).

After creating the fields, you'll [create](https://support.zendesk.com/hc/en-us/articles/4408846520858) or [edit](https://support.zendesk.com/hc/en-us/articles/4408836460698) a ticket form to include the new ticket fields.

#### Choosing your custom field type

You’ll first be prompted to choose what type of data field you want to create. These are standard form fields for collecting typical kinds of data.

![custom field type chooser](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/field_types_picker.png)

You can create any of the following types of ticket fields for use in your ticket forms:

- **Drop-down**: This field type allows you to create a list of options that the end user can choose from. For example, a list of products, what kind of support issue they need help with, and so on. The selected item is also added as a ticket tag, which can be used for routing the ticket, setting ticket priority, and so on. See [Using custom ticket fields to route and view tickets](#topic_djh_mvt_3mb).

  Note: Drop-down field lists can contain multiple levels of organization. See [Organizing drop-down list options](https://support.zendesk.com/hc/en-us/articles/4408829395738).
- **Multi-select**: This field type also allows you to create a list. However, the items in this type of list can be multi-selected, meaning that end users can choose more than one item in the list. This field type is useful when there are multiple conditions that might affect the type of support that is required. The items that are selected also become ticket tags.

  ![multiselect field](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_custom_ticket_field_multiselect.png)
- **Text**: This field holds a small amount of information (for example, a subject line).
- **Multi-line**: This is also a text field, but it allows more text on multiple lines (this is used, for example, as the field type for the Description field).
- **Checkbox**: This field is used for a single data point and the end user can choose it or not. The field selection is shown to agents in the ticket interface (it’s either selected or it’s not).
- **Numeric**: This field is used to capture a string of numbers, such as an account number.

  For common types of number data that follow fixed patterns, such as phone numbers and zip codes, you use the Regex field.
- **Decimal**: This field, also a numeric field, allows you to add a decimal point. You could use this field to prompt end users for currency values.
- **Date**: When the end user clicks this field, a date picker appears and a date can be selected. You can use this to prompt for a purchase date or appointment date, for example.
- **Credit card**: This field accepts credit card numbers in standard formats. If the number entered is not in a valid credit card format, the end user is warned and the data is not accepted.
- **Regex**: This field uses regular expressions to prompt for standard types of data such as URLs, zip codes, and date formats. For example, this is a regular expression used to validate a five-digit zip code: \b[0-9]{5}(?:-[0-9]{4})?\b. You can create your own regular expressions using Rubular.
- **Lookup relationship fields**: Enable users to select records related to them and their ticket. For example, if they're submitting a ticket requesting a refund, you might want the user to select the order or asset related to their request.

For more information about the best uses of some of the field types, see [Some useful examples of end user custom fields used for routing](#topic_eq3_lwt_3mb) below.

#### Setting field visibility permissions

When you’re setting up a new custom ticket field, you also need to set its visibility permissions. For fields that you want your end users to see and enter data into, you need to make it visible to them on the ticket form.

![custom field permissions](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_custom_field_permisions.png)

For the field to be visible and usable by end users, you must select **Editable by end users**. This displays the field on the ticket form and allows end users to enter data as part of their request. You also need to enter a field name into **Title shown to end users**.

The other permission related to end users, **Read-only for end users**, is used when you have a field that is controlled by agents, but that you also want end users to see when they’re viewing their tickets in the customer portal in your help center. For example, you may want your end users to see what the ticket status is. This setting does not affect what end users see on the ticket form.

If you create a custom field but don’t want it to be displayed to end users, you just need to make sure that you’ve not selected the **Editable by end users** permission setting.

Note: While these settings control the visibility of the ticket field itself, the options available within fields, such as a lookup relationship field, depend on the pre-defined values or permissions defined for the related object.

#### Requiring fields when end users submit requests

The other important end user setting is **Required to submit a request**, which requires that end users enter or select data for the field.

![custom field required](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_custom_field_required.png)

When you set a field as required, the end user is not able to submit the form until all the required data has been entered or selected. Fields that are not set as required will be labeled as **(optional)** on the ticket form.

Note: When you create a new ticket field and select the **Required to submit a request** checkbox, this only applies to end user created tickets. Agents can still create a ticket regardless of whether the custom field is configured.

#### Requiring fields when agents solve tickets

Just as you can require end users to enter data into a field, you can also require agents to do the same as a requirement for solving the ticket. For this, you select the **Required to solve a ticket** setting.

![custom field required agents](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_custom_field_required_agent.png)

The custom field is marked as required in the ticket interface and the ticket cannot be solved until the data has been selected or entered.

## Using custom ticket fields to route and view tickets

Custom ticket fields help you to capture the data you need to help you solve your customers’ support requests. After you’ve got that data, it can be used to create views and reports of your tickets and to automatically route incoming requests to the team or person who can best serve their support needs and solve the ticket as quickly as possible.

The drop-down list, multi-select, and checkbox custom ticket fields can be used for routing your tickets. This is because each of these fields create tags that are also inserted into the ticket. You can add tags to your triggers, automations, and views. This is how you can automatically route incoming tickets to a specific group or agent, for example.

![custom ticket field options](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dropdown_custom_field_tags.png)

The drop-down and multi-select fields automatically generate tags as you enter field options for your custom ticket field. With the checkbox field, you have the option of adding a tag to the field. When the ticket form is submitted, the data from these custom fields also generate tags in the ticket.

![custom field tags](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_tags_added_custom_field.png)

You use your tags as a condition in your business rules and then take action when those conditions are present.

![trigger tags](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_trigger_tags.png)

In this example (a trigger), the ‘refund’ tag was generated by a custom drop-down ticket field that prompts end users to enter the type of support issue that they are contacting you about. Knowing that the support request is about acquiring a refund, the trigger actions can be used to automatically route the ticket to a Group or assigned to a specific agent.

Custom ticket fields, tags, and business rules used together can create automated workflows for handling incoming support requests and creating views of your tickets. For more information, see [Understanding custom ticket fields in business rules and views](https://support.zendesk.com/hc/en-us/articles/4408834953114) and [Using custom ticket fields in business rules and views](https://support.zendesk.com/hc/en-us/articles/4408887162394).

When creating reports that include your custom ticket fields, it’s best to select the fields themselves, not the tag that they generate. For more information, see [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538).

### Some useful examples of end user custom fields used for routing

Here are some ideas for custom ticket fields that you might want to add to your ticket form to use for routing your tickets.

**Reason/How can we help?** - Use a drop-down field to provide your end users with a list of the types of support that makes sense for your business (for example: Billing, Cancellation, Complaint, Inquiry, Feedback, Sales, Update My Account, Change My Subscription).

**Product** - Use a drop-down field to ask your end users to select the product they’re having a problem with.

**Device** - Use a drop-down field to ask your end users to select the device they are using, which might be relevant if they’re having trouble accessing your site or using your mobile device app.

**Internet browser and version** - Similar to the device field, you can use a drop-down field to prompt for the internet browser name and version they’re using, which may be very useful in understanding their support issue.

**Do you have an account?** - This is simply two options in a dropdown field: Yes and No. The dropdown field tags for these would be something like “account\_yes’ and ‘account\_no’. You could also use a checkbox field and add the ‘account\_yes’ tag (tags are only added to a ticket when the checkbox is selected).

Note: An excellent example of many of these fields in use is the Dashlane submit a request page, which you can review [here](https://support.dashlane.com/hc/en-us/requests/new).

### Using agent-only custom fields for routing and follow up

You can create agent only custom ticket fields (not visible to your end users on the ticket form) that can also be used for routing and following up on tickets. There are two that we recommend: an ‘About’ drop-down field and a ‘Resolution’ drop-down field.

#### The ‘About’ field

The ‘About’ field is similar to the end user visible ‘Reason/How can we help’ drop-down field that was described above. It provides categorized support issues to help you gather more specific data. You might use both fields simultaneously, but the advantage of the agent only ‘About’ field is that it can be, and usually is, much more detailed and contains internal categories that you would not want your end users to see.

After a ticket is received and triaged, the agent can select the About category and the ticket can be routed using an automation. Having this detail in tickets is also good for creating views and reporting on tickets. For example, you can monitor and analyze open and resolved tickets based on these categories to identify what areas are giving end users the most trouble and so on.

For more information about the internal use of the ‘About’ field, see [The 'About' Field](https://support.zendesk.com/hc/en-us/articles/4409155792026). To use custom fields in reports, see [Reporting with custom fields](../building-reports/reporting-with-custom-fields.md).

#### The ‘Resolution’ field

The ‘Resolution’ field is useful for tracking how tickets are resolved and what type of action was necessary to solve the ticket. It’s the *how* to the ‘About’ field’s *what*.

![resolution custom ticket field](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/resolutionfield2.png)

Knowing how an issue was solved, generally, can help you determine what actions you can take to help deflect these types of support issues becoming tickets. For example, tickets that were solved by explaining how to use the product, for example, indicate that you should probably be providing more documentation in your knowledge base so that the end user doesn’t need to request support.

For more information about the ‘Resolution’ field, see [Using the 'Resolution' field](https://support.zendesk.com/hc/en-us/articles/4408822200346).

## Using multiple ticket forms

All Zendesk Suite and Support plans have a standard, pre-defined ticket field named *Default ticket field*. Depending on your plan, you might be able to create custom ticket forms as well. Multiple forms allow you to create more specific and useful ticket forms that prompt your users to enter data for different types of support issues and requests.

You can have up to 300 active ticket forms, including both the standard forms and any custom forms you create.

Ticket forms are [created](https://support.zendesk.com/hc/en-us/articles/4408846520858) and [managed](https://support.zendesk.com/hc/en-us/articles/4408836460698) on the Ticket Forms page in Admin Center.

![multiple ticket forms](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_multiple_ticket_forms.png)

When creating or updating a ticket form, start with the Ticket fields page in Admin Center, where you can [create custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794) that you want to add to your ticket forms. After the custom fields exist, you can add them to [new](https://support.zendesk.com/hc/en-us/articles/4408846520858) or [existing](https://support.zendesk.com/hc/en-us/articles/5494868102426) ticket forms.

All of your active ticket forms are displayed to your end users on the [Submit a request page](https://support.zendesk.com/hc/en-us/articles/4408842873498) and in Web Widget (Classic) (see [Using custom ticket fields and ticket forms with Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408834218522) and [Enabling multiple ticket forms in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408834218522#topic_bpg_wrp_jz)).

For more detailed information about using multiple ticket forms, see [Creating multiple ticket forms to support different request types](https://support.zendesk.com/hc/en-us/articles/4408846520858).

## Using conditional ticket fields in your ticket forms

Conditional ticket fields allow you to control the appearance and behavior of ticket fields on your ticket forms. As an example, you can set up a custom ticket field to display another custom ticket field when end users select a specific value in a drop-down list.

![ticket forms add conditions](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_ticket_form_add_conditions.png)

To make that example easier to understand, imagine that you’ve got a drop-down field prompting end users for the type of support issue they need help with (a ‘Reason/How can we help?’ field). When an end user selects ‘Can’t log in’ from that list, a new drop-down field appears on the ticket form. This new field prompts them to select the internet browser they’re using.

You set conditions on your ticket forms from the Ticket Forms page in Admin Center and then define a simple *when, if, then* formula for how the form is displayed when the conditions are met.

![ticket form conditions](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_ticket_form_conditions_formula.png)

You can also define conditions for agents, which affects how they interact with ticket field data in the ticket interface in Support.

Conditional ticket fields can also be set as required to complete the form. See [Making conditional ticket fields required](https://support.zendesk.com/hc/en-us/articles/4408846008218).

For more information about using conditional ticket fields, see [Creating conditional ticket fields in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408834799770) and [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858).
# About custom fields and custom field types

Source: https://support.zendesk.com/hc/en-us/articles/4408838961562-About-custom-fields-and-custom-field-types

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can add custom fields for tickets, users, and organizations.

This article contains the following sections:

- [About custom fields](#topic_dpz_bgb_2fc)
- [About custom field types](#topic_inh_1gb_2fc)

## About custom fields

Custom fields provide the flexibility necessary to capture a variety of customer, ticket,
and organization details. Not only can the additional information captured by custom fields
be useful for agents to see, but you can also use custom fields in the following ways:

- You can use drop-down list, multi-select, and checkbox custom fields that generate tags in automations, macros, triggers, reports, and views (see [Understanding custom ticket fields, tags, and business
  rules](https://support.zendesk.com/hc/en-us/articles/4408834953114)).
- As placeholders in macros, ticket comments, and notification messages (see [Placeholders for custom fields](https://support.zendesk.com/hc/en-us/articles/4408887218330#topic_nfp_nja_vb)).
- Lookup relationship fields can be used in triggers and views (see [Using lookup relationship fields in triggers and
  views](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_pgk_llh_vtb).
- In reporting (Professional and Enterprise plans) (see [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538)).
- In search (see [Searching custom user and organization
  fields](https://support.zendesk.com/hc/en-us/articles/4408883318554#topic_pyt_m1s_vk)).

Custom user and organization fields are visible only to team members. End users can't see
them. However, admins can make ticket fields visible to end users in addition to team
members.

You can create different [types of custom
fields](#topic_inh_1gb_2fc). To get started with custom fields, see:

- [Adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794)
- [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866)
- [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786)
- [Defining a custom object's schema with custom
  fields](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_cq4_1sn_lwb)

## About custom field types

The following table details the types of custom fields you can add.

Note: Some field types,
such as drop-down, multi-select, and checkbox, generate tags. Don't re-use tags across
custom fields. In the event that a tag is duplicated on a record, such as a ticket, the
fields associated with the tag become uneditable until the duplication is
removed.

Table 1. Custom field types

| Types | Description |
| --- | --- |
| Drop-down | This field enables you to create a list of options for users to select. Each option is a combination of a title and a tag. The title is displayed to users and the tag is used as a ticket property that you can use in business rules. You can create up to 2,000 values in a custom drop-down list, with a maximum length of 255 characters per field. You can select which field appears as the default option in the drop-down list or choose to not display a field value as a default.  Note: Configuring a default option in a drop-down list only applies to new tickets that are created by agents through the Agent Workspace or created by users wherever the ticket form is displayed. If you change an existing ticket form to one that contains a drop-down list with a default option, the default option is not displayed.  You can organize drop-down list options into categories (see [Organizing drop-down list options](https://support.zendesk.com/hc/en-us/articles/4408829395738)). |
| Multi-select | This field allows users to choose multiple options from a predetermined list. You can create up to 2,000 values in a custom multi-select list. You can organize options into categories (see [Organizing drop-down list options](https://support.zendesk.com/hc/en-us/articles/4408829395738)). |
| Text | This is a simple single line text input.   The character limit for this field is 65,536. |
| Multi-line | This is a multiple line text input.   The character limit for this field is 65,536. |
| Checkbox | This is used to capture a Yes/No value. Enter a tag to be added to the ticket when the checkbox is selected. Use the tag to filter your views, triggers, and automations. |
| Numeric | This is for simple numeric input (no decimals). Values entered in custom number fields for organizations, users, and custom objects can't exceed 12 digits. There are no restrictions on the length of values in custom number fields for tickets. |
| Decimal | This is for numbers that contain decimals. |
| Date | Custom date fields allow your users to select a date from a date picker. Users can choose the current date or any date in the past or future. **Community tip!** Colin shows how to use custom date fields to set reminders for tickets. Check it out in our [community forums](https://support.zendesk.com/hc/en-us/community/posts/203459786).    If you use webhooks or other methods to change a custom date field in tickets, do not include hours or a timezone. It will cause an error.  Note: The formatting of the field value and calendar differs based on the [language selected in a user's profile](https://support.zendesk.com/hc/en-us/articles/4408822762650). However, the date is always saved in the `YYYY-MM-DD` format. |
| Credit card | This field allows users to enter a credit card number. Only the last four digits are visible to agents and stored by Zendesk. Note: Credit card fields are not supported in user and organization fields. |
| Regex | You can enter a regular expression to create an input mask to validate proper entry of numbers in fixed patterns (telephone numbers, zip codes, social security numbers, etc).   Here's a regular expression for a U.S. social security number. This expression requires three sets of numbers (0-9 only) in a pattern of 3-2-4 and each separated by a dash:  \b[0-9]{3}-[0-9]{2}-[0-9]{4}\b  Other common regular expressions include:  - URL validation: ^(http|https):\/\/[a-z0-9]+([-.]{1}[a-z0-9]+)\*\.[a-z]{2,5}(([0-9]{1,5})?\/.\*)?$ - Five-digit zip codes: \b[0-9]{5}(?:-[0-9]{4})?\b - yyyy-mm-dd date: \b([0-9]{4})-(1[0-2]|0?[1-9])-(3[0-1]|[1-2][0-9]|0?[1-9])\b  Regular expressions can't exceed 255 characters.  For more information about regular expressions, see [Regular Expressions Language - Quick Reference](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) on the Microsoft website. Zendesk uses Ruby to process regular expressions, which might vary slightly from other language implementations. For differences, see [Using Regular Expressions with Ruby](https://www.regular-expressions.info/ruby.html) on the regular-expressions.info website. |
| Lookup relationship | Custom lookup relationship fields allow admins to define custom relationships that can exist between tickets, users, organizations, and custom objects. Team members can then establish those relationships while working on tickets, editing user profiles, editing organizations, or managing custom objects. Additionally, for custom objects, admins can define relationships with brands and articles. See [Using lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770).  The lookup relationship field is not supported in search or Explore. |
# Using custom ticket fields in business rules and views

Source: https://support.zendesk.com/hc/en-us/articles/4408887162394-Using-custom-ticket-fields-in-business-rules-and-views

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Custom ticket fields, while incredibly useful, are not equally available as conditions across business rules and views. This article explains which custom field types and conditions you can use in business rules and views, and how to use them.

Note: For more detailed information on the interaction with custom ticket fields, business rules, and views, see [Understanding custom ticket fields in business rules and views](https://support.zendesk.com/hc/en-us/articles/4408834953114).

This article contains the following topics:

- [Permitted business rules and view conditions](#topic_uyy_22q_htb)
- [About custom ticket fields in business rules and views](#topic_tvd_g2q_htb)

## Permitted business rules and view conditions

The following business rules and views conditions are permitted for the respective custom field types.

Note: Views are only available for a limited number of custom field types. For more information on this interaction, see [Understanding custom ticket fields and views](https://support.zendesk.com/hc/en-us/articles/4408834953114#topic_znk_mnk_xj).

| Custom field type | Trigger conditions | Automation conditions | SLA conditions | View conditions |
| --- | --- | --- | --- | --- |
| **Drop-down** | - Is - Is not - Present - Not present   *Includes all drop down values* | - Is - Is not - Present - Not present   *Includes all drop down values* | - Is - Is not - Present - Not present   *Includes all drop down values* | - Is - Is not - Present - Not present   *Includes all drop down values* |
| **Multi-select** | - Includes - Does not include - Present - Not present | - Includes - Does not include - Present - Not present | - Includes - Does not include - Present - Not present | - Includes - Does not include - Present - Not present |
| **Text** | - Present - Not present | *Not available* | *Not available* | *Not available* |
| **Multi-line** | - Present - Not present | *Not available* | *Not available* | *Not available* |
| **Number** | - Present - Not present | *Not available* | *Not available* | *Not available* |
| **Decimal** | - Present - Not present | *Not available* | *Not available* | *Not available* |
| **Checkbox** | - Is checked - Is unchecked | - Is checked - Is unchecked   *Only available if checkbox is set to add a tag* | - Is checked - Is unchecked | - Is checked - Is unchecked   *Only available if checkbox is set to add a tag* |
| **Date** | - Is - Is not - Present - Not present - Before - Before or on - After - After or on - Is within the previous\* - Is not within the previous - Is within the next - Is not within the next - Changed - Changed to - Changed from - Not changed - Not changed to - Not changed from | - Is - Before - Before or on - After - After or on - Is within the previous\* - Is within the next | - Is - Is not - Before - Before or on - After - After or on | - Is - Before - Before or on - After - After or on - Is within the previous - Is within the next |
| **Regex** | - Present - Not present | *Not available* | *Not available* | *Not available* |
| **Lookup relationship** | - Is - Is not - Present - Not present   *Includes all filtered values* | *Not available* | *Not available* | - Is - Is not - Present - Not present   *Includes all filtered values* |

Note: Using a custom date field with the `Is within the previous` trigger or automation condition may not work as expected. See [Using a custom date field as a trigger condition](https://support.zendesk.com/hc/en-us/articles/4408883449626) and [Using a custom date field as an automation condition](https://support.zendesk.com/hc/en-us/articles/6037856210202).

## About custom ticket fields in business rules and views

This section provides more information about individual custom ticket fields and their availability with business rules and views.

- [Drop-down fields](#topic_yq4_tfq_htb)
- [Multi-select fields](#topic_gzb_5fq_htb)
- [Text, multi-line text, numeric, and decimal fields](#topic_olz_5fq_htb)
- [Checkbox fields](#topic_vp3_wfq_htb)

### Drop-down fields

Custom drop-down field values are available for use across all views and business rules. Drop-down field values have a finite amount of predefined value options.
For more information, see [Understanding how creating, deactivating, or deleting ticket fields impacts tickets](https://support.zendesk.com/hc/en-us/articles/4408886624410).

When using drop-down fields within conditions, the field will appear as follows:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_dropdown_in_busi_rule_condition.png)

### Multi-select fields

Multi-select fields provide the option to choose multiple values from a list.
This can then leverage the values set for the field equally across all business rules and views. You can either select to check for the presence of any value for the field or more granularly for specific values.

For example, checking for the presence of any value:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_busi_rule_mutliselect_present_condition.png)

If you need to check for the presence of a specific value in the multi-select field, you can specify individual field values as conditions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_busi_rule_multiselect_value_condition.png)

### Lookup relationship fields

Lookup relationship fields provide the option to choose from a filtered list of users, organizations, and tickets in your account. You can add the fields to users, organizations, and tickets to establish relationships with other users, organizations, and tickets. See [Understanding lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_xcn_2gp_mtb). You can use lookup relationship fields in the conditions of views and triggers. You can also use them in the actions of triggers to set the values of the fields.

In the following example, the first condition of a trigger is a user lookup relationship field named *Support manager*.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-condition.png)

### Text, multi-line text, numeric, and decimal fields

Custom text, mutli-line text, numeric, and decimal fields are only available for use as a condition for triggers. You can only check whether a value is present or not. The actual content of these fields can't be matched with any string or specific words.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_textNumDec_busi_rule_condition.png)

### Checkbox fields

Checkboxes are available across all business rules and views. For use in automations and views, the checkbox must have a tag. If your checkbox doesn't add a tag when checked, checkboxes won't appear as an option for use in automations and views.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_checkbox_busi_rule_condition.png)
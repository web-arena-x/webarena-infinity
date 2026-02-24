# Working with data types in Explore formulas

Source: https://support.zendesk.com/hc/en-us/articles/5784398875802-Working-with-data-types-in-Explore-formulas

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

After you [understand the basics of writing Explore formulas](https://support.zendesk.com/hc/en-us/articles/4408836190362), the next step is to understand how data types interact with formulas. This article introduces the concept of data types, shows you how to use them within formulas, and helps you troubleshoot issues that might occur.

This article contains the following topics:

- [Understanding data types](#topic_a5r_lgs_sxb)
- [Troubleshooting data type errors in the formula editor](#topic_qmp_mgs_sxb)

## Understanding data types

Data type refers to the format of a piece of information that's added to a formula, typically as a value within a function. The table below summarizes the data types that Explore uses.

Knowing how data types interact with and operate within a function is imperative to writing a properly constructed formula in Explore. To check which data types a function requires, see [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746).

| **Data type** | **Examples** |
| --- | --- |
| **Number** Used for all metrics, numeric attributes, and numbers without quotation marks. | Metrics   - VALUE(First reply time (min)) - COUNT(Tickets) - AVG(Agent replies)   Attributes   - [Ticket ID] - [Assignee ID] - [Leg instance]   Values   - 123 - 4500 - 3.5 |
| **Text** The majority of the attributes are of the text data type. Any values typed in inside quotation marks also have the text data type. | Attributes   - [Ticket group] - [Assignee name] - [Ticket created - Date]   Values   - "Support" - "Anna Sting" - "2022-05-24" - "123" - "true" - "empty string" |
| **Boolean** Applies to attributes that have only two values: True or False. Values True and False, typed in without quotation marks, are considered to be boolean type. | Attributes   - Comment present - Call recorded   Values   - True - False |
| **Timestamp** Applies to attributes that show a specific date and time. | Attributes   - [Ticket created - Timestamp] - [Call - Timestamp]   Values   - "2023-05-18T22:16:07" - "2020-04-25T13:02:00" |
| **Array** Used for values inserted in multi-value functions such as IN or INCLUDES\_ALL. | Values   - IN([Ticket status], ARRAY("Open", "Pending")) - INCLUDES\_ALL([Ticket tags], "white", "black") |
| **Null** Reserved for the NULL value. | Values   - Null |

## Troubleshooting data type errors in the formula editor

If your formula uses incorrect data types, a warning message appears in real time as you write or edit the formula. The error message identifies which data type you used and provides guidance about which data type should be used instead.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_formula_editor_data_type_warning.png)

The table below shows some examples of data type warnings you might see in the formula editor, including incorrect and correct versions of a formula.

| **Warning** | **Incorrect formula** | **Correct formula** |
| --- | --- | --- |
| Can't use different types in the THEN statement. 1 is number and "0" is text. Use the same type. | IF [Ticket status]="Open" THEN 1 ELSE "0" ENDIF | - IF [Ticket status]="Open" THEN 1 ELSE 0 ENDIF - IF [Ticket status]="Open" THEN “1” ELSE “0” ENDIF |
| Can't use different types in the SWITCH statement. "1" is text and 2 is number. Use the same type. | SWITCH ([Ticket group]) {CASE "Support": "1"CASE "IT": 2 } | SWITCH ([Ticket group]) {CASE "Support": "1"CASE "IT": “2” } |
| Can't use text in this function. Use number. | INTEGER([NPS comment]) | INTEGER(VALUE(NPS rate)) |
| Can't use 1 as number and 2 as number. Use only booleans. | 1 OR 2 | TRUE OR FALSE |
| Can't use [Ticket assigned - Date] as text and [Ticket solved - Date] as text. Use only numbers. | [Ticket assigned - Date] > [Ticket solved - Date] | DATE\_TO\_TIMESTAMP([Ticket assigned - Date]) >DATE\_TO\_TIMESTAMP( [Ticket solved - Date]) |
| Can't use [Ticket group] as text and [Ticket ID] as number. Use only numbers or only text. | [Ticket group]+[Ticket ID] | [Ticket group]+STRING([Ticket ID]) |
| Can't use VALUE(Agent replies) as number and 2 as text. Use only numbers. | VALUE(Agent replies)>”2” | VALUE(Agent replies)>2 |

Tip: For more troubleshooting help, see [Troubleshooting errors in Explore formulas](https://support.zendesk.com/hc/en-us/articles/5870960937498).
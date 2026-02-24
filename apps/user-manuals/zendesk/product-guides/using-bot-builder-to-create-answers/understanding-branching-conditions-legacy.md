# Understanding branching conditions (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5280598023450-Understanding-branching-conditions-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article describes functionality
available only to customers who had a drafted or published AI agent as of February
2, 2025. For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Building dialogues for AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

You can configure the **Branch by condition** step to evaluate data stored in [variables](https://support.zendesk.com/hc/en-us/articles/5480101976218) and branch a messaging AI agent conversation
based on that data.

This article includes the following sections:

- [Branch by condition step
  basics](#topic_a2d_q31_jwb)
- [Condition
  elements](#topic_lrt_p31_jwb)
- [Nested conditions](#topic_xww_qnl_pwb)

## Branch by condition step basics

When you add a new
**Branch by condition**
step to your answer flow,
the following settings are included:

- **Name**
  that identifies the step on the canvas.
- **Two default branches**
  that must be configured before the answer
  flow can be published:

  - **If this**: If the branch's conditions are met, the
    conversation follows the branch's steps
  - **Else**: If the conversation doesn't match the
    conditions of any other branch, the conversation follows
    this branch's steps

Branch by condition can have up to six branches, including the Else branch. The
Else branch is required and cannot be removed from the step. You can add up to
four additional branches, to a maximum of six branches.

To add an additional branch, click
**Add branch**
and configure the following
settings for each branch:

- **Name**
  that describes the condition for the branch. This name
  appears as the branch name on the canvas.
- **Condition**
  that includes the following elements:

  - **Variable**: The data that will be evaluated to see if
    the condition is met.
  - **Operator**: How the data from the variable and value
    are compared. Includes
    *is*,
    *is not,*
    *contains*, and
    *does not contain*.
  - **Value**: Value expected for the condition specified by
    the operator.

  See
  [Condition
  elements](#topic_lrt_p31_jwb)
  for more information.

You can combine conditions for a branch using the
**AND/OR**
drop-down. For
example, the following branch checks whether a user is located in Australia or
the United States.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-or-condition-example.png)

A conversation can only follow one branch. Branches are evaluated in the order
they are included in the step. End users that meet the criteria of more than one
branch will be sent down the first branch with matched criteria, from top to
bottom in the step's configuration panel or left to right on the canvas.
Branches can be reordered by dragging the condition panes on the canvas.

## Condition elements

Conditions are comprised of
[variables](#topic_hhd_xrm_gwb),
[operators](#topic_bdj_xrm_gwb), and
[values](#topic_hk4_xrm_gwb).

### About variables

A [variable](https://support.zendesk.com/hc/en-us/articles/5480101976218) is a container for data related to a
conversation, such as a customer's location or membership status. A
variable's data can come from information collected in an **Ask for
Details** or **Make API call** step or [messaging authentication metadata](https://support.zendesk.com/hc/en-us/articles/5314129059482).

In a
condition, a variable's value is compared to a static value. Variables
are added to the condition using a drop-down menu.

For more
information about variable types and creating variables, see [Using variables to personalize AI agent answers](https://support.zendesk.com/hc/en-us/articles/5480101976218).

### About operators

The operator determines how the variable's data is compared to the
value. Operators are added to a condition using a drop-down menu.

The following operators are available. All operator matching is case-insensitive.

| When I’m using the conditional step in bot builder… | Available operators |
| --- | --- |
| I want to be able to evaluate data stored as a **number** | Operators for Zendesk known use cases for evaluating numbers:   - Equal to or greater than - Equal to or less than - Greater than - Less than - Equal to - Not equal to |
| I want to be able to evaluate data stored as a **string** | Operators for Zendesk known use cases for evaluating strings:   - Is - Is not - Contains - Does not contain - Starts with - Ends with |

### About values

A value is static data that's compared to a variable.
It represents the expected data for a variable. For example, in a condition that
checks whether a customer's
`membership_status`is "platinum",
"platinum" is the value.

The input field used to specify a condition's value varies based on the variable. For the
**Authenticated status** variable, you specify the condition's value
using a boolean drop-down field. For other variables, you specify the
condition's value using a text input field.

Note: The authenticated status
variable is only available as a branching option if you have [created a messaging key for JWT
authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746).

[Customer variables](https://support.zendesk.com/hc/en-us/articles/5480101976218#topic_yyz_dkh_twb) collected during an [Ask for details](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_i5r_grz_n5b) step require a corresponding custom
ticket field. For customer variables using a drop-down ticket field, use the
associated tag as the value for a condition. For example, the
`membership_status`drop-down field accepts a "Platinum level"
value with a related "platinum\_level" tag. To check whether the customer has a
platinum membership status, use "platinum\_level" as the value in the condition.

## Nested conditions

A nested condition is a condition that contains two or more conditions inside it. You
can use nested conditions to build complex logic that relies on multiple conditions.
They are especially useful when combining conditions using both
**AND**
and
**OR**.

For example, the following branch uses a nested condition to check if the user meets
the following criteria:

- The user has a “platinum” membership status AND
- The user is located in one of the following countries:
  - Australia OR
  - The United States

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/nested-condition-example.png)

You can only nest conditions up to three levels deep. Each level, including the top
level, can contain up to six conditions.
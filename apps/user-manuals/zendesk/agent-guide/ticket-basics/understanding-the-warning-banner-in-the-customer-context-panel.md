# Understanding the warning banner in the customer context panel

Source: https://support.zendesk.com/hc/en-us/articles/4408846631194-Understanding-the-warning-banner-in-the-customer-context-panel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When a returning customer (authenticated or unauthenticated) requests a live chat and
fills out a [pre-chat form](https://support.zendesk.com/hc/en-us/articles/4408829170458) with information that does
not exactly match their existing user profile – for example, they enter the same
name and email address but a different phone number – a warning banner appears in
the customer [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) that alerts the agent to these conflicts.
Using the information in the banner, an agent can update the visitor’s user profile
to resolve the discrepancy.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pre-chat_info_alert_customer_context.png)

This article includes the following topics:

- [About the warning banner](#topic_gfb_mt2_jqb)
- [Resolving information conflicts](#topic_wjg_mt2_jqb)

## About the warning banner

The presence of the warning banner is *informational only*. Only the
pre-chat data that does not match the existing user data is displayed in the banner.
The information does not affect the customer’s account or profile information. The
banner can remain in the customer context panel without impacting the customer’s
account or the agent’s workflow.

The warning banner only appears when:

- Pre-chat forms are enabled for chat requests.
- The customer is a *returning* visitor (authenticated or
  unauthenticated), requesting a *live chat* (this feature is not currently
  available for messaging conversation requests).
- There is an *unresolved* discrepancy between the information
  collected in the pre-chat form and the data in the customer’s user profile. When
  the discrepancy is [resolved](#topic_wjg_mt2_jqb), the banner disappears.
- The agent viewing the ticket is chat-enabled.

Matches are determined by comparing the field values submitted in the pre-chat forms.
When fields are left empty, they are not considered mismatches, even when other form
fields match existing user data.

For example, if returning customer fills out the pre-chat form and matches the name,
email, or phone number field but leaves one or more of these fields blank, the blank
fields will not trigger the warning banner. You can prevent this situation by
requiring the customer to fill out all fields before submitting the form.

In addition, when a customer leaves the name field blank, it is automatically filled
with a randomly-generated name in the Agent Workspace. These names are not
considered mismatches.

It’s important to note, as well, that the information in the banner is
*dynamic*. That is, if the customer updates their contact details in the
chat widget, the details displayed in the alert are also updated. If the updated
data matches their profile information, the alert will disappear.

## Resolving information conflicts

As noted above, the warning banner remains visible in the customer context
panel until the information conflict is resolved.

There are two ways to resolve a conflict and remove the banner from the
context panel:

- The agent can update the customer’s profile to match the information
  in the banner.
- The customer can update their information in the chat widget to match
  their profile.

**To update a customer’s profile from the Agent Workspace**

1. In the customer context panel, click the **Edit** icon at the top
   of the profile.
2. [Edit](https://support.zendesk.com/hc/en-us/articles/4408893585178#topic_vmc_tvn_x1b) the customer profile. The updated
   information is saved automatically.
3. Click on the ticket tab to return to the Agent Workspace.
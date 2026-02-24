# Routing automatically triaged tickets using omnichannel routing

Source: https://support.zendesk.com/hc/en-us/articles/4766535251610-Routing-automatically-triaged-tickets-using-omnichannel-routing

---

If you've set up bothintelligent triageandomnichannel routing, you can incorporate intelligent triage insights into your omnichannel workflows for email and messaging tickets.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Enhance your ticket routing by combining intelligent triage with omnichannel routing. Use ticket intent, language, and sentiment to create custom triggers that direct tickets to the right support group. This setup helps manage priorities and improve response times. You can also create triggers for specific intents, languages, sentiments, and spam, ensuring tickets are handled by the most suitable agents.

If you've set up both [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) and [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), you can incorporate intelligent triage
insights into your omnichannel workflows for email and messaging tickets.

Pairing these two features lets you incorporate a ticket's intent, language, and
sentiment into your routing rules, while still taking availability, capacity, skills,
and ticket priority into consideration.

This article gives you examples of triggers you can create based on intelligent triage
information and use with omnichannel routing. You can use these examples as starting
points and customize the details for your purposes. Keep in mind that intelligent triage
prediction values are available only in English when you're creating triggers; however,
intelligent triage can evaluate content in the languages listed [here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

Note: Intelligent triage conditions don’t work with the
**Ticket** | **Is** | **Created** condition. When adding conditions related
to intent, language, or sentiment in the triggers, use the **Status** | **Is** |
**New** condition instead. See [Why didn’t my intelligent triage trigger run during ticket
creation?](https://support.zendesk.com/hc/en-us/articles/5940673936026)

This article contains the following topics:

- [Creating a routing trigger based on a specific intent](#topic_k43_4hs_25b)
- [Creating a routing trigger based on an intent and language](#topic_pxc_rhs_25b)
- [Creating a routing trigger based on sentiment](#topic_bv1_z3h_hwb)
- [Creating a spam routing trigger based on intent](#topic_dk4_d1d_3xb)

Related articles:

- [Choosing a routing method for automatically
  triaged tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506)
- [Routing automatically triaged tickets using
  standalone skills-based routing](https://support.zendesk.com/hc/en-us/articles/6191493148186)

## Creating a routing trigger based on a specific intent

You can create a trigger that assigns tickets to a group based on the intent of the
ticket. This helps you direct tickets to the agents most qualified to help the
requester.

The example below defines a trigger that assigns a group and priority to tickets that
meet the specified conditions, including the intent.

**To create a trigger based on an intent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Create trigger**.
3. In **Trigger name**, enter a name for the trigger (such as **Assign to
   <group> based on <specific> intent**, customized with relevant
   details of your trigger).
4. (Optional) Enter a **Description** for your trigger.
5. Select a **Category** for your trigger.
6. In the **Conditions** pane, under **Meet ALL of the following
   conditions**, add the following conditions:
   - (If you’re routing email tickets) **Ticket > Tags** | **Contains at
     least one of the following** | <enter your omnichannel
     auto-routing trigger>
   - **Ticket > Status** | **Is** | **New**
   - **Ticket > Intent** | **Is** | <select the intent you want the
     trigger to be based on>
   - **Ticket > Tags** | **Contains none of the following** |
     triage\_trigger\_fired
   - **Ticket > Agent replies** | **Less than** | **1**
   - (Optional) **Ticket > Intent confidence** | **Is not** |
     **Low**
7. In the **Actions** pane, add the following actions:
   - **Ticket > Add tags** | **triage\_trigger\_fired**
   - **Ticket > Group** | <select the group you want the tickets to be
     assigned to>
   - **Ticket > Priority** | <select whatever priority level makes
     sense for your use case>
8. Click **Create trigger**.

The **triage\_trigger\_fired** tag helps ensure that your trigger runs only once on
each ticket. The trigger adds the tag the first time it runs, and after that, the
presence of the tag prevents the trigger from running again. The **Agent
replies** condition performs a similar function. In the event that the tag is
accidentally deleted, this condition prevents the trigger from running on a ticket
on which an agent has already replied.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ml_automated_triage_triggers_1.png)

## Creating a routing trigger based on an intent and language

You can also create a trigger that assigns tickets based on a combination of intent
and language. This might be helpful if you have language-specific customer service
groups.

The example below defines a trigger that assigns a group and priority to tickets that
meet the specified conditions, including the intent and language.

**To create a trigger based on intent and language**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Create trigger**.
3. In **Trigger name**, enter a name for the trigger (such as **Assign
   <language> tickets to <group> based on <specific> intent**,
   customized with relevant details of your trigger).
4. (Optional) Enter a **Description** for your trigger.
5. Select a **Category** for your trigger.
6. In the **Conditions** pane, under **Meet ALL of the following
   conditions**, add the following conditions:
   - (If you’re routing email tickets) **ticket > Tags** | **Contains at
     least one of the following** | <enter your omnichannel
     auto-routing trigger>
   - **Ticket > Status** | **Is** | **New**
   - **Ticket > Intent** | **Is** | <select the intent you want the
     trigger to be based on>
   - **Ticket > Language** | **Is** | <select the language you want
     the trigger to be based on>
   - **Ticket > Tags** | **Contains none of the following** |
     **triage\_trigger\_fired**
   - **Ticket > Agent replies** | **Less than** | **1**
   - (Optional) **Ticket > Intent confidence** | **Is not** |
     **Low**
7. In the **Actions** pane, add the following actions:
   - **Ticket > Add tags** | **triage\_trigger\_fired**
   - **Ticket > Group** | <select the group you want the tickets to be
     assigned to>
   - **Ticket > Priority** | <select whatever priority level makes
     sense for your use case>
8. Click **Create trigger**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ml_automated_triage_triggers_2.png)

## Creating a routing trigger based on sentiment

You can create a trigger that assigns tickets with a specific sentiment,
like Negative and Very negative, to a group specially trained to handle these kinds
of situations.

The example below defines a trigger that assigns a group and priority to tickets that
meet the specified conditions, including the sentiment.

**To create a trigger based on sentiment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Create trigger**.
3. In **Trigger name**, enter a name for the trigger (such as **Assign to
   <group> based on negative sentiment**, customized with relevant
   details of your trigger).
4. (Optional) Enter a **Description** for your trigger.
5. Select a **Category** for your trigger.
6. In the **Conditions** pane, under **Meet ALL of the following
   conditions**, add the following conditions:
   - (If you’re routing email tickets) **Ticket > Tags** | **Contains at
     least one of the following** | <enter your omnichannel
     auto-routing trigger>
   - **Ticket > Status** | **Is** | **New**
   - **Ticket > Tags** | **Contains none of the following** |
     **triage\_trigger\_fired**
   - **Ticket > Agent replies** | **Less than** | **1**
   - (Optional) **Ticket > Sentiment confidence** | **Is not** |
     **Low**
7. Under **Meet ANY of the following conditions**, add the following
   conditions:
   - **Ticket > Sentiment** | **Is** | **Negative**
   - **Ticket > Sentiment** | **Is** | **Very negative**
8. In the **Actions** pane, add the following actions:
   - **Ticket > Add tags** | **triage\_trigger\_fired**
   - **Ticket > Group** | <select the group you want the tickets to be
     assigned to>
   - **Ticket > Priority** | <select whatever priority level makes
     sense for your use case>
9. Click **Create trigger**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ml_intelligent_triage_triggers_sentiment.png)

## Creating a spam routing trigger based on intent

You can create a trigger that automatically sends any requests that intelligent
triage has identified as spam to a specified queue. When agents don’t have to deal
with spam requests, they can spend more time on customer requests.

The example trigger below assigns spam tickets to a specified group. Choose a
different action in the Actions pane if you prefer to handle spam tickets a
different way.

Note: Before creating a spam routing trigger, make sure that
tickets aren't being inadvertently marked as spam.

**To create a spam routing trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Create trigger**.
3. In **Trigger name**, enter a name for the trigger (such as **Spam
   routing**).
4. (Optional) Enter a **Description** for your trigger.
5. Select a **Category** for your trigger.
6. In the **Conditions** pane, under **Meet ALL of the following
   conditions**, add the following conditions:
   - (If you’re routing email tickets) **Ticket > Tags** | **Contains
     at least one of the following** | <enter your omnichannel
     auto-routing trigger>
   - **Ticket > Status** | **Is** | **New**
   - **Ticket > Intent** | **Is** | **Spam**
   - **Ticket > Tags** | **Contains none of the following** |
     **triage\_trigger\_fired**
   - **Ticket > Agent replies** | **Less than** | **1**
   - **Ticket > Intent confidence** | **Is** | **High**
7. In the **Actions** pane, add the following actions:
   - **Ticket > Add tags** | **triage\_trigger\_fired**
   - **Ticket > Group** | <select a group that spam tickets should
     be assigned to>
   - **Ticket > Priority** | **Low**
8. Click **Create trigger**.
# Configuring intelligent triage for the agent experience

Source: https://support.zendesk.com/hc/en-us/articles/6298065502874-Configuring-intelligent-triage-for-the-agent-experience

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Configure intelligent triage to enhance the agent experience by displaying customer intent and sentiment in ticket headers. Control agent access to auto-filled fields, allowing manual updates if needed. Adjust ticket forms to show or hide these fields, depending on your needs. This setup helps agents quickly access relevant information and provides insights into where AI predictions may need adjustments.

[Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) leverages uses artificial intelligence
(AI) to automatically analyze new support tickets by predicting customer intent,
sentiment, and language, and enriches tickets with actionable details, such as product
names.

This article describes how to configure intelligent triage for the agent experience. By
configuring how the information intelligent triage detects appears in the Agent
Workspace—such as displaying intent and sentiment in the ticket header—you can make
relevant information available to your agents at a glance. Additionally, you can control
agent access to auto-filled fields within ticket forms, allowing for manual updates if
needed.

This article contains the following topics:

- [Displaying intent and sentiment in the ticket header](#topic_at4_t3x_s2c)
- [Determining whether agents can see and update intelligent triage fields](#topic_vx1_4n3_fzb)

Related articles:

- [Automatically detecting customer intent,
  language, and sentiment](https://support.zendesk.com/hc/en-us/articles/4550640560538)

## Displaying intent and sentiment in the ticket header

For intent and sentiment, you can configure whether the detected information is
displayed in the ticket header of the conversation for agents.

The view how this information appears to agents, see [Viewing intelligent triage predictions in tickets](https://support.zendesk.com/hc/en-us/articles/4685355428250).

**To display intent and sentiment in the ticket header**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Agent copilot > Auto assist**.
2. Scroll down to the **Ticket context** section.
3. Click the **Show intent in the header** checkbox to display the intent
   that's been detected in the conversation.
4. Click the **Show sentiment in the header** checkbox to display the
   sentiment detected in the conversation.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_hub_ticket_context_settings.png)
5. Click **Save**.

## Determining whether agents can see and update intelligent triage fields

When intelligent triage is turned on, the system automatically fills out the intent,
sentiment, and language fields, but admins can control whether the fields are
displayed and editable for agents. To see how these fields appear to agents, see
[Viewing intelligent triage predictions in
tickets](https://www.google.com/url?q=https://support.zendesk.com/hc/en-us/articles/4685355428250%23topic_uqd_3kh_xcc&sa=D&source=docs&ust=1757615269278155&usg=AOvVaw3jGKrOiXyEsCtByZIB-FYg).

Whether the fields appear by default depends on your ticket forms. Specifically:

- If you **have a single ticket form**, the intelligent triage fields are
  automatically visible in tickets.

  Edit your ticket form to remove the new
  fields if you don’t want agents to be able to see and change these fields in
  tickets.
- If you **have multiple ticket forms**, the intelligent triage fields are not
  automatically visible in tickets. You can edit your forms by adding the fields
  so that agents can see and update them in tickets.

  Any [entities](https://support.zendesk.com/hc/en-us/articles/6711181959194#topic_qv4_xkt_zbc) you created must also
  have their custom fields added to your forms.

Note: If you want to use the intelligent triage field values only for reporting or API
use, you don’t need to add them to any ticket forms.

When the intent, sentiment, and language fields are displayed to agents, they can
update the values in the fields if they feel they're not correct.

Tip: You can [report on agents' manual updates](https://support.zendesk.com/hc/en-us/articles/4550629802650) to
the intelligent triage prediction fields, which helps you discover trends in the
types of tickets where intelligent triage isn't correctly predicting the intent,
sentiment, or language.

**To add or remove intelligent triage fields in tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Follow one of the options below:
   - For a single ticket form, [open the ticket form](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_c5x_l3b_lk) for
     editing, then click the **x** on the field you want to remove.
     You can drag a field onto the ticket form if you want to add it
     back.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_form_single_remove_field.png)
   - For multiple ticket forms, [open the ticket form](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_c5x_l3b_lk), then
     drag the intelligent triage fields you want to add onto your form.
     You can click the x on the field if you want to remove it from the
     form.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ticket_form_add_field.png)
3. Click **Save**.
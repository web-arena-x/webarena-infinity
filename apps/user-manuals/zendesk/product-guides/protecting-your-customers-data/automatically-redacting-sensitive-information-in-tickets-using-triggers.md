# Automatically redacting sensitive information in tickets using triggers 

Source: https://support.zendesk.com/hc/en-us/articles/9248330321050-Automatically-redacting-sensitive-information-in-tickets-using-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

With the Advanced Data Privacy and Protection add-on, you can automate the redaction of sensitive information in tickets using triggers. This feature helps you manage personally identifiable information (PII) by setting conditions to redact data like passwords, credit card numbers, and social security numbers. Redaction events are logged for auditing, but be cautious as redactions are irreversible.

Customers with the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906) can use [redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882) to highlight personally identifiable information (PII) within ticket comments. While this feature helps agents identify PII, manually reviewing and redacting this data can be time-consuming if you have a large volume of PII in your tickets.

To streamline this process, admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) to automate the redaction process, giving them complete control over when and how PII is protected in Zendesk.

Important:

- Ticket redaction cannot be reversed. Use caution when creating triggers to redact data.
- This feature shouldn't be used with the [automatic credit card redaction feature](https://support.zendesk.com/hc/en-us/articles/4408822124314) due to potential conflicts.

Watch the video below to learn more about setting up and using triggers for automatic redaction.

Automatic redaction with triggers: Protecting data privacy with AI (3:00)

This article contains the following topics:

- [Understanding automatic redaction](#topic_bb4_gr1_gfc)
- [Configuring ticket triggers to redact sensitive information](#topic_hbh_jr1_gfc)

## Understanding automatic redaction

Automatic redaction leverages ticket triggers and redaction suggestions to remove sensitive data from ticket comments, reducing or eliminating time spent identifying and redacting PII during ticket handling.

When a ticket trigger fires, it can execute an action that automatically redacts the selected PII on non-closed tickets that meet the trigger conditions, unless an agent has explicitly chosen to [ignore a specific redaction suggestion](https://support.zendesk.com/hc/en-us/articles/6669399593882#topic_emg_2xt_ncc).
Triggers allow you to specifiy conditions for redacting various types of PII, depending on the stage of the conversation.

For example, advanced redaction allows you to do the following:

- Redact passwords, bank account numbers, and credit card numbers when tickets are created or updated.
- Redact social security numbers and date of birth when a tag is added to a ticket to confirm verification is complete.
- Redact email address, phone number, and address when the ticket status is changed to Closed.

As with manual redaction, the PII is obscured in ticket comments using a black bar, and a *redacted\_content* tag is automatically added to the ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_obscured_all_828_update.png)

Redaction events are recorded in the [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970) log, providing an audit trail to confirm that data has been deleted. The log includes the comment ID where the PII was redacted, the name of the trigger that fired, and the added ticket tag.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/redaction_events_log.png)

Redacting PII using triggers has certain limitations that align with redaction suggestions. See [Redaction suggestion limitations](https://support.zendesk.com/hc/en-us/articles/6669399593882#topic_hlr_shx_m1c).

## Configuring ticket triggers to redact sensitive information

Before creating ticket triggers for automatic redaction, you must have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906) with [redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882) turned on.

**To create a ticket trigger for automatic redaction**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Redaction suggestions**.
2. Select the types of PII you'd like to redact (credit card number, bank account number, driver's license, etc.) automatically. See [Turning on and configuring redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882#topic_r1v_sgx_m1c).
3. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
4. [Create](https://support.zendesk.com/hc/en-us/articles/4408886797466#topic_qfk_s23_vsb) or [edit](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb) a ticket trigger.
5. Click **Add condition** to set up the trigger to meet **All** or **Any** conditions.
6. Click **Add action** and set the actions that occur when the trigger's conditions are met.

   In this case, include the **Ticket** >
   **Redact** action, and select the types of PII to redact in the **Value** field. The PII types available in the drop-down field are those you configured for redaction suggestions.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_trigger_redaction_action.png)
7. Click **Create trigger**.
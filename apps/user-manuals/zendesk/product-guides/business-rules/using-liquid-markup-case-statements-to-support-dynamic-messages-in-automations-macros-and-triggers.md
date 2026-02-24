# Using Liquid markup case statements to support dynamic messages in automations, macros, and triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408842967578-Using-Liquid-markup-case-statements-to-support-dynamic-messages-in-automations-macros-and-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Liquid markup is commonly used in business rules to customize comments and email notifications. Liquid markup case statements enable you to define multiple messages to be used dynamically based on some attribute of the ticket.

This article provides a few examples, such as supporting responses in [multiple languages](https://support.zendesk.com/hc/en-us/articles/4408888770714). Many companies and organizations support end users who speak languages other than English. There are several ways to manage this. For more complex messages or many languages, we recommend using [dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066). For simple messages in a few languages, liquid markup can be a great fit.

This article includes the following topics:

- [Using a Liquid markup case statement to support multiple languages](#topic_qdf_qjq_fzb)
- [Using a Liquid markup case statement to dynamically change the text based on a dropdown field's value](#topic_avr_fvg_l1c)
- [Using a Liquid markup case statement to create other dynamic responses](#topic_y14_rjq_fzb)

## Using a Liquid markup case statement to support multiple languages

When your account supports multiple languages, users can specify their preferred language in their profiles. Then, you can reference the user's preferred language in a series of conditional statements within the body of the message you're defining for the automation, macro, or trigger.

The following example shows the email body for a trigger's **Notify by: User email** action. In this case, the account's default language is English, so we didn't need to label it within the Liquid markup formatting.

```
{% case ticket.requester.language %}

{% when 'Italiano' %}

Ciao,

La tua richiesta (#{{ticket.id}}) è stata ricevuta, è stato esaminato dal nostro staff di assistenza.

Per esaminare lo stato della richiesta e aggiungere ulteriori commenti, segui il link qui sotto:
http://{{ticket.url}}

{% when 'Danish' %}

Hej,

Din anmodning (# {{ticket.id}}) er blevet modtaget og bliver gennemgået af vores supportmedarbejdere.

At gennemgå status for anmodningen og tilføje yderligere kommentarer, skal du følge nedenstående link:
http:// {{ticket.url}}

{% else %} 

Hello,

Your request (#{{ticket.id}}) has been received, and is being reviewed by our support staff. 

To review the status of the request and add additional comments, follow the link below:
http://{{ticket.url}}

{% endcase %}
```

## Using a Liquid markup case statement to dynamically change the text based on a dropdown field's value

If you've defined custom drop-down ticket fields, you might find yourself wanting to define a trigger action or macro response that changes depending on which value is selected in the drop-down field. In this scenario, you can use the following example case statement as a template, where

- `FIELDID` is replaced with your custom drop-down field's ID.
- Each `{% when "Value X" %}` statement is replaced with one of the drop-down field's defined options.
- Each `Your text X here.` statement is replaced with your desired response for the field value preceding it.

```
{% case ticket.ticket_field_option_title_FIELDID %}
{% when "Value 1" %}
Your text 1 here.
{% when "Value 2" %}
Your text 2 here.
{% when "Value 3" %}
Your text 3 here.
{% else %}
-
{% endcase %}
```

## Using a Liquid markup case statement to create other dynamic responses

You can use a similar structure to create dynamic responses in contexts other than preferred language. For example, a similar case structure could be used if you wanted to respond based on the user's organization. In that scenario, you'd define the case as `{% case ticket.organization.name %}` and the repsonse for each organization would be preceded by `{% when 'OrganizationName' %}`.
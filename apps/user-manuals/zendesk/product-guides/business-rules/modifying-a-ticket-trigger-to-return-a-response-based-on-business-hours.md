# Modifying a ticket trigger to return a response based on business hours

Source: https://support.zendesk.com/hc/en-us/articles/4408829256218-Modifying-a-ticket-trigger-to-return-a-response-based-on-business-hours

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

You can use conditions or Liquid markup to modify ticket triggers that are based on business hours.

This article includes the following topics:

- [Using conditions with triggers that are based on business hours](#h_01EDCE8F800RQHQ228EHFYBVJ3)
- [Using Liquid markup with triggers that are based on business hours](#h_01EDCE8MJCBH866KGVQ800SCHB)

**Related articles**

- [Triggers based on business hours](https://support.zendesk.com/hc/en-us/articles/4408842938522-Setting-your-business-hours-Plus-and-Enterprise-#topic_bh1_mz2_4p)
- [Setting your schedule with business hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522)

## Using conditions with ticket triggers that are based on business hours

You can create ticket triggers based on business hours using the **Ticket: Within business hours** condition, instead of using Liquid markup. This enables you to build ticket triggers that fire based on whether an event occurs during business hours or outside of business hours.

For more information, read about these conditions in [Ticket triggers based on business hours](https://support.zendesk.com/hc/en-us/articles/4408842938522-Setting-your-business-hours-Plus-and-Enterprise-#topic_bh1_mz2_4p) and [Ticket triggers conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408893545882):

- Ticket: Within business hours?
- Ticket: Within (schedule)

## Using Liquid markup with ticket triggers that are based on business hours

Alternatively, you can use Liquid markup to create different responses in your business rules based on ticket properties. This example shows how you can modify the **Notify requester of received request** ticket trigger (or any other ticket trigger that serves the same purpose) to return a response based on your business hours.

```
{% if ticket.in_business_hours == 'true' %}

Hello {{ticket.requester.first_name}}

Your request (#{{ticket.id}}) has been received and is being reviewed by our support staff. 

To review the status of the request and add additional comments, follow the link below:
http://{{ticket.url}}

{% else %}

Hello {{ticket.requester.first_name}}

Your request (#{{ticket.id}}) has been received and will be reviewed by our support staff during regular business hours (Monday - Friday, 8am - 6pm PST). 

To review the status of the request and add additional comments, follow the link below:
http://{{ticket.url}}

{% endif %}
```

Using a simple if/else statement, the first response is sent if the request is received during business hours and the other is sent if it is not. The if statement tests the `ticket.in_business_hours` property and responds accordingly. The ticket property is in the same format that you're familiar with when it's used as a placeholder, although not contained within double curly brackets for the simple reason that it's not being used as output here but rather as part of the logic determining what will be included in the comment when it's sent to the requester as an email notification.

For more information on how Liquid markup can be used, see [Understanding Liquid markup and Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408883291290).
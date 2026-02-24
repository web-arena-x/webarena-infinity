# Setting up business rules for multiple brands

Source: https://support.zendesk.com/hc/en-us/articles/4408842973338-Setting-up-business-rules-for-multiple-brands

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Triggers and automations in Zendesk are collectively referred to as *business rules*. They perform automatic actions to update tickets, notify users, and organize your work. In your Zendesk, business rules can affect all tickets, or you can use conditional statements to include or exclude specific sets of tickets.

So, if you support multiple brands in your Zendesk, you can design triggers to affect tickets from a specific brand (or exclude it), just as you would use triggers to affect tickets from a specific organization (or exclude a specific organization).

In short, you have only one set of triggers. This article will show you how to create brand conditions for triggers.

Excluding or Including Brands

You might want to exclude a brand or multiple brands from a trigger.

For example, if you have a trigger that escalates priority of tickets for a specific customer organization, you might want to raise the alarm for only one specific product. Maybe the customer paid for a higher degree of service for one product, but not all, so the priority escalation should happen for one brand only.

For this purpose, you have a number of options. Triggers aren’t tied directly to brands, but you can use conditions to scope by brand.

Here are four scenarios:

- To exclude one brand from a trigger, you can use a [brand] [is not] condition in the "Meet all of the following" section: 

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/exclude1.png) 
 The trigger will affect tickets in all brands except Omniwear Kids
- To exclude several brands, you can use multiple [brand] [is not] conditions in the "Meet all of the following" section: 

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/excludemany.png) 
 The trigger will affect tickets in all brands except Omniwear Kids and Omniwear Sports

- To restrict a trigger to a specific brand, you can use a [brand] [is] condition in the "Meet all of the following" section: 
 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/restric1.png) 
 The trigger will only affect tickets with the Omniwear Sports brand

- To restrict to a specific set of brands, you can use multiple [brand] [is] conditions in the "Meet any of the following" section: 
 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/restrictmany.png) 
 The trigger will only affect tickets with the Omniwear Formal or Omniwear Kids brands
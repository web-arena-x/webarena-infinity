# Getting started with Zendesk Suite - Part 7: Managing support requests during non-business hours

Source: https://support.zendesk.com/hc/en-us/articles/4945055494170-Getting-started-with-Zendesk-Suite-Part-7-Managing-support-requests-during-non-business-hours

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Articles in the series

- [Introduction: Getting started with Zendesk Suite](https://support.zendesk.com/hc/en-us/articles/4408881937306)
- [Part 1: Accessing Zendesk Suite admin settings](https://support.zendesk.com/hc/en-us/articles/4944856070426)
- [Part 2: Adding team members](https://support.zendesk.com/hc/en-us/articles/4944849237658)
- [Part 3: Understanding how end user accounts are handled](https://support.zendesk.com/hc/en-us/articles/4944925937818)
- [Part 4: Managing user access security and authentication](https://support.zendesk.com/hc/en-us/articles/4944919944730)
- [Part 5: Adding support channels](https://support.zendesk.com/hc/en-us/articles/4944930820506)
- [Part 6: Routing incoming support requests](https://support.zendesk.com/hc/en-us/articles/4944922385050)
- [Part 7: Managing support requests during non-business hours](https://support.zendesk.com/hc/en-us/articles/4945055494170)
- [Part 8: Guaranteeing customer support expectations with service level agreements](https://support.zendesk.com/hc/en-us/articles/4944993140762)
- [Part 9: Reporting on support activity](https://support.zendesk.com/hc/en-us/articles/4944968790426)
- [Part 10: Enabling customer satisfaction ratings](https://support.zendesk.com/hc/en-us/articles/4944994159130)
- [Part 11: Leveraging AI features with Zendesk](https://support.zendesk.com/hc/en-us/articles/6501074649242)
- [Part 12: Using the Zendesk developer platform to extend your support solution](https://support.zendesk.com/hc/en-us/articles/4944970330138)
- [Part 13: Rolling out your Zendesk Suite support solution](https://support.zendesk.com/hc/en-us/articles/4944970747418)
- [Part 14: Additional features](https://support.zendesk.com/hc/en-us/articles/6579939982746)

An important aspect of managing your flow of incoming support requests is to set the customer’s expectation about when their request will be responded to when you’re not available.

If you’re not providing 24/7 support to your customers, you’ll need to have a workflow in place for following up with customers, regardless of when they contact you. You do this in Zendesk Suite by creating a business hour schedule that can then be used to automatically inform your customers about your availability and when you’ll be able to respond.

You set this up in Admin Center.

![Set business schedule](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zsuite_set_schedule.png)

You set the days and hours that you are available and when a request comes in outside those hours the customer is notified. For example, an email message support request during non-business hours generates an email message reply that you use to indicate when the customer can expect to be contacted and also direct them to your self-service articles in your help center.

This is done with a trigger that evaluates if the message has been received during non-business hours and then generates a notification to inform the customer if it has been. You can also create automations (time-based responses based on several business hour conditions).

How business hours are used differs across the many channels you can add. The email message example above is straightforward (receive an email message, reply with an email message). You can respond to a tweet with a tweet. A chat request can automatically be responded to with a prompt for the customer to send you an offline message instead. These are common examples.

![Business hours notification in Chat](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_oh3.png)

For more information about setting up business hours, see [Setting your schedule with business hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522).

As mentioned earlier in this article, you can also use Zendesk bots to automatically reply to several different types of support requests. See [Understanding everywhere you can use Zendesk bots](https://support.zendesk.com/hc/en-us/articles/4408821281818).

Continue to [Part 8: Guaranteeing customer support expectations with service level agreements](https://support.zendesk.com/hc/en-us/articles/4944993140762-Getting-started-with-Zendesk-Suite-Part-9-Guaranteeing-customer-support-expectations-with-service-level-agreements).
# Customizing when your customer satisfaction (CSAT) survey is sent

Source: https://support.zendesk.com/hc/en-us/articles/4408886194202-Customizing-when-your-customer-satisfaction-CSAT-survey-is-sent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

When you [send a customer satisfaction (CSAT) survey](https://support.zendesk.com/hc/en-us/articles/7689997846554) to your customers, it’s set up by default to send the survey 24 hours after the customer's ticket has been solved (not closed). You can customize when the survey is sent.

Customer satisfaction is really nothing but a placeholder that you can use in any notification sent out by a trigger or automation. Yes, Zendesk provides a system automation specifically for customer satisfaction, but you can modify it or even remove it altogether in favor of a trigger. See [Managing your CSAT survey, channels, and rules](https://support.zendesk.com/hc/en-us/articles/8054625864602#topic_h5b_j2d_5cc).

Remember, the default automation sends the CSAT survey 24 hours after the ticket is solved. You can easily increase or decrease the length of time between when the ticket is solved and when the survey is sent by editing the automation.

![csat-hrssincesolved-36.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/csat-hrssincesolved-36.png)

If you’re taking advantage of user and organization tagging, you may want to send customer satisfaction to only a subset of your user base. For example, you might want to ensure that users tagged with “partner” never get a customer satisfaction survey. You would add this condition under “ALL”:

![customizing_csr_3.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customizing_csr_3.png)

If you are concerned that your users are receiving too much email, consider combining the “solved” email notification with the customer satisfaction survey. To achieve this, simply deactivate the customer satisfaction automation, then go into triggers and edit your “solved” notification trigger. Add the customer satisfaction placeholder {{satisfaction.rating\_section}} into your notification.

![customizing_csr_4.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customizing_csr_4.png)
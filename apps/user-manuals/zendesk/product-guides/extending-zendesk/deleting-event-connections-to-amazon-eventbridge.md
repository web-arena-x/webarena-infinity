# Deleting event connections to Amazon EventBridge

Source: https://support.zendesk.com/hc/en-us/articles/4408824521114-Deleting-event-connections-to-Amazon-EventBridge

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Important: Zendesk has discontinued the Events Connector for Amazon EventBridge. You can't configure new events with the Zendesk Events Connector. Existing event connections will continue to work until December 1, 2025. Consider [using webhooks to integrate with Amazon EventBridge](https://support.zendesk.com/hc/en-us/articles/7778413975322).

Amazon EventBridge is an event bus service which consumes event data streaming from Zendesk. Events received in Amazon EventBridge can be redirected to AWS services such as AWS Lambda, Amazon SNS, Amazon SQS, and Amazon Kinesis streams. This allows event-driven applications to be built which can subscribe and react to Zendesk events.

You cannot create new events using the Events Connector for Amazon EventBridge, but you can delete any existing connections as needed.

Although Zendesk have discontinued the Events Connector for Amazon EventBridge, you can [use webhooks to integrate with Amazon EventBridge](https://support.zendesk.com/hc/en-us/articles/7778413975322).

Related information:

- [Events schema for Amazon EventBridge](https://developer.zendesk.com/api-reference/event-connectors/events-for-amazon-eventbridge/introduction/)
- [Publishing SNS notifications for Zendesk ticket events](https://developer.zendesk.com/documentation/event-connectors/events-for-amazon-eventbridge/publishing-sns-notifications-for-zendesk-ticket-events)
- [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/index.html)
- [Reducing custom code by using advanced rules in Amazon EventBridge](https://aws.amazon.com/blogs/compute/reducing-custom-code-by-using-advanced-rules-in-amazon-eventbridge/)

## Deleting an event connection

When deleting an event connection, you must first delete an event rule associated with an event bus in AWS EventBridge before deleting the event bus. If it is not done first, an event bus cannot be deleted.

**To disconnect an event connection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **Integrations > Integrations**.
2. In **Amazon Web Services**, click **Configure**.
3. Disconnect the event source in the Zendesk Connector interface by clicking **Disconnect**.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/eventbridge_connector_disconnect.png)
4. Confirm to disconnect the event source. A notification confirming event source disconnection is displayed, and events will immediately stop streaming. It can take up to 20 seconds for the event source status to register as disconnected in Amazon EventBridge.
5. In Amazon EventBridge, delete the rule associated with the event bus. For more information, see [Deleting or Disabling an EventBridge Rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/delete-or-disable-rule.html).
6. Remove the event bus in the AWS Event Console. For more information, see the [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/index.html).
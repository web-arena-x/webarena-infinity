# Understanding Contact Center concepts

Source: https://support.zendesk.com/hc/en-us/articles/9459103231770-Understanding-Contact-Center-concepts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Learn about Amazon Connect contact flows and queues to enhance your contact center integration. Understand how to log contact attributes and send data back with Contact Lens. Key features include agent status and presence synchronization, smart resolution codes for contact categorization, and alert banners for important updates. These tools help streamline operations and improve customer interactions.

This article covers some key concepts and features to help you to optimize and expand your Contact Center integration.

This article contains the following sections:

- [About Amazon Connect security](#topic_d5m_dwm_yfc)
- [About Amazon Connect contact flows and queues](#topic_e5m_dwm_yfc)
- [About key features sending attribute data back to Zendesk](#topic_gnk_2wm_yfc)

## About Amazon Connect security

Security in Amazon Connect covers identity and access management, encryption in transit and at rest, data retention, and contact data redaction (for example, via Contact Lens). Review these controls before configuring flows, queues, and any attributes sent to Zendesk. For details, see the AWS documentation: [Security in Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/security.html).

## About Amazon Connect contact flows and queues

It's important to understand what contact flows and queues are in Amazon Connect.

**Contact flows**

A flow defines the customer experience with your contact center from start to finish. Amazon Connect includes a set of default flows so you can quickly set up and run a contact center. You can also create custom flows for your specific scenario.

See the Amazon Connect documentation to learn more about [flows in Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html).‍

**Queues**

There are two types of queues:

- **Standard queues**: Contacts wait before they are routed to and accepted by agents.
- **Agent queues**: Contacts are routed to agent queues when explicitly sent there as part of a flow. For example, you might route contacts to a specific agent who's responsible for a specific issue type, such as billing or premium support. Or you might use agent queues to route to an agent's voicemail. These queues are created automatically when you add an agent to your contact center.

See the Amazon Connect documentation to learn more about [queues in Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-queues-standard-and-agent.html).

## About key features sending attribute data back to Zendesk

When logging contact attributes in Amazon Connect with Contact Lens, certain steps are required to allow Amazon Connect to send the attribute data to Zendesk. For more information, see the Amazon Connect documentation [Enable conversational analytics in Amazon Connect Contact Lens](https://docs.aws.amazon.com/connect/latest/adminguide/enable-analytics.html).

After you enable conversational analytics, you can learn more about the following features:

- **Agent status** is set either in Zendesk or Contact Center and can be synchronized between Zendesk and Contact Center. See the Amazon Connect documentation about [agent status](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html).
- **Agent presence** helps agents easily transfer calls to other available agents. See this article about [agent presence](https://support.zendesk.com/hc/en-us/articles/9696113111706).
- **Smart resolution codes** automates the process of categorizing contacts and reduces the time required to categorize contacts, while also improving the accuracy of categorization. See [smart resolution codes](https://support.zendesk.com/hc/en-us/articles/9696160652058).
- **Alert banners** inform your agents of important information when communicating with your customers. Admins can configure messages to show to agents in Contact Center, such as network outages, flight delays, or severe weather. See this article about [alert banners](https://resources.localmeasure.com/articles/alert-banners).
# About the live chat-to-messaging migration wizard

Source: https://support.zendesk.com/hc/en-us/articles/9435865466906-About-the-live-chat-to-messaging-migration-wizard

---

Important: The migration wizard will only available to accounts receiving live chat-to-messaging migration assistance. See [our announcement](https://support.zendesk.com/hc/en-us/articles/9460252937114) for more information.

As part of the migration from live chat to messaging, a migration wizard will help you replicate your live chat configuration on messaging channels.

The live chat settings that will be migrated to messaging include:

- **Chat triggers**. All the Chat triggers that can be migrated to messaging can be found in Admin Center on the [Messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562) page. See [Managing chat triggers when migratring from live chat to messaging](https://support.zendesk.com/hc/en-us/articles/4408822204698) for more information.
- **Operating Hours**. Messaging uses [business hours](https://support.zendesk.com/hc/en-us/articles/4408842938522), which are similar to Chat’s operating hours. As part of the migration, we’ll convert your operating hours to business hours. Once business hours are migrated you can set your Web Widget schedule and availability. Business hours can be accessed and configured in Admin Center under **Objects and rules > Business rules > Schedule**, and are applied to a messaging channel on that channel’s configuration page. See [Configuring messaging responses and business hours](https://support.zendesk.com/hc/en-us/articles/4500737327258).
- **Pre-chat and offline forms**. If you’re using pre-chat or offline forms, we’ll configure your messaging Web Widget to collect the same end-user information in the default messaging response, and send an identical follow-up message. See [Configuring messaging responses and business hours](https://support.zendesk.com/hc/en-us/articles/4500737327258).

 | Example: default messaging response during business hours | Example: default messaging response with follow-up message outside of business hours |
 | --- | --- |
 | | |
- **End chat**: Messaging’s end session setting performs similarly to the end chat feature. The setting allows agents to end the messaging session and release agent capacity. See [About ending messaging sessions](https://support.zendesk.com/hc/en-us/articles/8009788438042).
- **Automatic idle settings**: In messaging, the capacity release and conversation inactivity settings define how long a conversation remains active, and what happens to the ticket when the conversation becomes inactive. By default, we’ll set the inactivity timer to 10 minutes and will release agent capacity when that limit is reached. See [Automatically releasing agent capacity for inactive messaging conversations](https://support.zendesk.com/hc/en-us/articles/7043034053658).
- **Wait time**: You can display the estimated wait time and queue position so your customers know when they can expect an agent reply. Wait times in messaging are managed in Admin Center with [messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562). See [Displaying estimated wait time in messaging conversations](https://support.zendesk.com/hc/en-us/articles/8009787999514-Displaying-estimated-wait-time-in-messaging-conversations).
- **Goals and conversion tracking**: Your live chat business goals are converted to messaging goals as part of the migration. Messaging goals allow you to track customer actions and see which agents are responsible for driving those actions. See [Tracking customer actions with messaging goals](https://support.zendesk.com/hc/en-us/articles/9435878261402).
- **Banned visitors**: Visitors you have banned from live chat will be migrated to messaging as suspended users. In messaging, end users can be suspended individually, or banned by IP address. See [Suspending messaging users](https://support.zendesk.com/hc/en-us/articles/8009733465370) and [About banning IP addresses from messaging channels](https://support.zendesk.com/hc/en-us/articles/9418700382618).
- **Chat ratings**: -If you’re using a satisfaction survey to gather customer feedback, customer satisfaction (CSAT) ratings will be activated in messaging. When a messaging conversation ends, customers will be prompted to leave feedback. See [About the CSAT user experience for email and messaging](../measuring-success/about-the-csat-customer-satisfaction-user-experience-for-email-and-messaging.md).
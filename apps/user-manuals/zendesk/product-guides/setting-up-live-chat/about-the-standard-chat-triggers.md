# About the standard chat triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408834380442-About-the-standard-chat-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Note: The triggers in this article apply to accounts using the Zendesk Chat product. If you are using Zendesk's messaging functionality, see [Understanding messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562).

To help you get up and running with some best practices for a typical chat workflow, Zendesk Chat comes with a set of standard chat triggers in your account. You can use these Chat triggers as they are, modify them, or duplicate them and make adjustments to the duplicate.

By default, all of these standard chat triggers are inactive in your account. You can [activate the triggers](https://support.zendesk.com/hc/en-us/articles/8554265015322#topic_usf_bdp_sdc) you want to use.

For more information about creating, modifying, and duplicating chat triggers, see [Creating chat triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762-Working-with-Chat-triggers) and [Editing and managing chat triggers](https://support.zendesk.com/hc/en-us/articles/8554265015322).

The default chat triggers are:

- [Chat Rescuer](#h_01ECR03BBYZZJ53S198WFH7NZ6)
- [Proactive Greeting](#h_01ECR03JKKF7AVAKJYBZM7G5GT)
- [Checkout Page](#h_01ECR03YT5MBMMZ0TGS80WFSG8)
- [First Reply](#h_01ECR0502DPWXFFA49GQZB7JYW)
- [Languages](#h_01ECR056QY4AVGES478J60K131)
- [Message Tagged Visitors](#h_01ECR33RQV6M27A5BJPVSYB4QV)
- [Pricing Page](#h_01ECR9G39D7ZAAY5H31WEW3EN5)
- [Proactive Greeting by Name](#h_01ECR9H1WGTW3KE3GM8YNW5XA5)
- [Product Discounts](#h_01ECR9JFSQXDJ9TA82WRZ9HDCN)
- [Request Contact Details](#h_01ECR9JQQTZ5FNBG4VJRBS0DYB)
- [Tag Repeat Visitors](#h_01ECR9K05P316VZW6W4FXR4T9E)

## Chat Rescuer

This trigger is designed to send an auto-response to a visitor who has requested a chat if your agent has not joined the chat or respond after 60 seconds. The message helps keep your visitor engaged if there is a large queue or a bit of wait before an agent can connect and chat with the visitor.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor requests a chat**
- **Check conditions: Check all of the following conditions**
 - **Account status | Not equal | Offline**
 - **Still on site | 60**
 - **Visitor served | Is false**
- **Perform the following actions**
 - **Set triggered | Is true**
 - **Send message to visitor |**Customer Service | We apologize for keeping you waiting. Our operators are busy at the moment, please leave us a message with your email address and we'll get back to you shortly.

## Proactive Greeting

This trigger is designed to send a proactive message to any new visitors to your site, 30 seconds after they arrive. This means, if someone who has never been to your site before comes to your website, 30 seconds after they arrive, the chat widget will pop up on their page with the message "Welcome! Can we help you with anything?". If the visitor replies to that proactive message, it initiates a chat request. For more information and recipes for additional proactive greetings, see this article: [Targeting key visitors with proactive chat](https://support.zendesk.com/hc/en-us/articles/4408883473178-Targeting-key-visitors-with-proactive-chat).

Note: If you use department routing, [proactive messages may bypass any routing you have set up in the pre-chat form or other triggers](https://support.zendesk.com/hc/en-us/articles/4408830703258). Add the action **set visitor department**to the triggers below to make sure these proactive chat conversations route to the correct department or agent.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions** 
 - **Still on site | 30**
 - **Visitor previous visits | Equals |** 0
 - **Visitor requesting chat | Is false**
 - **Visitor served | Is false**
- **Perform the following actions** 
 - **Send message to visitor |**Customer Service | Welcome! Can we help you with anything?

## Checkout Page

The Checkout Page trigger is more of a skeleton to get you started than a ready-to-go trigger. It is designed as an example for Zendesk customers who work in retail, but it can also be adapted for other purposes. As is, this trigger is designed to reduce cart abandonment by engaging customers who are lingering on the checkout page for more than 60 seconds.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions** 
 - **Visitor page URL | Equals |**www.zendesk.com/cart
 - **Still on site | 60**
 - **Visitor requesting chat | Is false**
 - **Visitor served | Is false**
- **Perform the following actions** 
 - **Send message to visitor |** Stephanie | Hi, are you having any trouble checking out? Feel free to reach out to us with any questions.

## First Reply

This trigger is designed to send an automated first reply to a visitor requesting a chat so they know their request is being attended to. The automatic message will be sent 5 seconds after the visitor has requested a chat.

Tip: If you would like to extend the time the trigger waits to send a message to a site visitor, consider removing the **Wait**action and using a **Still on site**or **Still on page**condition instead.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor requests a chat**
- **Check conditions: Check all of the following conditions**
 - **Visitor requesting chat | Is true**
 - **Visitor served | Is false**
- **Perform the following actions** 
 - **Wait |**5
 - **Send message to visitor |** Customer Service | Thanks for your message, please wait a moment while our agents attend to you.

## Languages

This trigger is designed to be used as a jumping-off point for Zendesk customers that serve visitors in multiple different languages. If you get visitors from a different country, use this trigger to send an automated greeting in the visitor's native language. [Duplicate this trigger and create a different version for each language](https://support.zendesk.com/hc/en-us/articles/4409147863450) you want to serve.

The default trigger that comes with the account is set up to serve visitors chatting in from France.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions**
 - **Visitor country code | Equals |**FR
 - **Visitor requesting chat | Is false**
 - **Visitor served | Is false**
 - **Still on site | 60**
- **Perform the following actions** 
 - **Send message to visitor |**Service client | Bonjour. Est-ce que je peux vous aider?

## Message Tagged Visitors

This trigger is designed to send a targeted message to a specific set of visitors that have a tag indicating they have visited your site 5 times. This trigger works in unison with the [Tag Repeat Visitors](#h_01ECR9K05P316VZW6W4FXR4T9E) default chat trigger, so make sure that trigger is enabled as well for this trigger to work properly.

Tip: You can duplicate or adapt this trigger and use it to target visitors for a number of other reasons simply by changing what tag it acts on. Just make sure you also create the complimentary trigger that adds that tag to your visitors. See [Understanding different types of tags in Chat](https://support.zendesk.com/hc/en-us/articles/4408888643866).

The default trigger is designed to act on the tag "5times".

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions**
 - **Still on site | 30**
 - **Visitor requesting chat | Is false**
 - **Visitor served | Is false**
 - **Visitor tag | Contains (case sensitive) |**5times
- **Perform the following actions** 
 - **Send message to visitor |**Customer Service | Hi, welcome back to our site! Is there anything we can help you with?

## Pricing Page

This trigger is designed to ask customers who are lingering on the pricing page if they need any help.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions**
 - **Visitor page URL | Contains |** pricing
 - **Still on site | 30**
 - **Visitor requesting chat | Is false**
 - **Visitor served | Is false**
- **Perform the following actions** 
 - **Send message to visitor |**Customer Service | Hi, are you interested in our paid plans?

## Proactive Greeting by Name

This trigger is designed to Personalize your greeting to registered returning visitors by including their name. This makes them feel valued, making them more likely to interact over chat.

This trigger fires only when the system is able to identify a visitor's name. It will not fire on returning visitors that still have the name "Visitor####".

Tip: Consider adding some additional conditions to this trigger such as **Visitor requesting chat | Is false** to stop it from firing on visitors who have requested a chat or are being served by an agent.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions**
 - **Visitor previous visits | Greater than or equal to |**1
 - **Visitor name | Does not contain |**Visitor
- **Perform the following actions** 
 - **Wait |**30
 - **Send message to visitor |**Customer Service | Hi @visitor\_name, welcome back! What can we help you with?

## Product Discounts

This is another skeleton trigger designed to be built on and customized to your own needs. This trigger is designed for retailers and allows you to offer your returning customers a discount on one of your products or services.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor requests a chat**
- **Check conditions: Check all of the following conditions**
 - **Visitor tag URL | Contains |**[product name]
 - **Still on page | 30**
 - **Visitor requesting chat | Is false**
 - **Visitor served | Is false**
- **Perform the following actions** 
 - **Send message to visitor |**Customer Service | Hi, are you interested in [insert product name]? We're offering a one-time 20% discount. Chat with me to find out more.

## Request Contact Details

This trigger is designed to fire when your account status is set to **Away****.** In that case, your site visitors will still be offered the option to request a chat, but no agents will be actively available to reply to the chat. This trigger will send a proactive message letting the visitor know you are away and asking them to leave their email address so you can get back to them as soon as your agents are back online.

Tip: Your account is in an **Away**status if at least one of your agents is set to **Away**and none of your agents are set to **Online**. See [Setting your chat availability status](https://support.zendesk.com/hc/en-us/articles/4408828519706-Setting-your-chat-availability-status).

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor requests a chat**
- **Check conditions: Check all of the following conditions**
 - **Account status | Equals | Away**
- **Perform the following actions** 
 - **Add tag |**Away\_request
 - **Send message to visitor |**Customer Service | Hi, sorry we are away at the moment. Please leave your email address and we will get back to you as soon as possible.

## Tag Repeat Visitors

This trigger is designed to work with the [Message Tagged Visitors](#h_01ECR33RQV6M27A5BJPVSYB4QV) default trigger. This trigger adds a tag to a visitor that has visited your site 5 or more times. This tag can also be used in reporting to identify potential customers who are very interested in your brand.

The conditions of the trigger are set up as follows:

- **Run trigger: When a visitor has loaded the chat widget**
- **Check conditions: Check all of the following conditions**
 - **Visitor previous visits | greater than or equal to |**5
- **Perform the following actions** 
 - **Add tag |** 5times
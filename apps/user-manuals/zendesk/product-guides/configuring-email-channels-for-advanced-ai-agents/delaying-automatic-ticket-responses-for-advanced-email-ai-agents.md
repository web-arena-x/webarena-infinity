# Delaying automatic ticket responses for advanced email AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357772433562-Delaying-automatic-ticket-responses-for-advanced-email-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

### **What is Ticket Reply Delay?**

By default, the end user would receive an immediate response to their email request when using ticket automation.

With Ticket Reply Delay, you have the option to delay your responses.

### **Why you might want to use it**

Responses arriving right after the original email are less likely to be opened. Either they are hidden after a confirmation email or your customers might mistake them for one. Either way, it is often not clear, that the response they received seconds after their inquiry includes the answer to their question.

### **How to use it**

To set up Ticket Reply Delays for all your email responses on an AI agent (with the exception of test widget conversations), navigate to Settings -> AI agent settings and find [Reply Delay (minutes)](https://support.zendesk.com/hc/en-us/articles/8357756721178-Settings-Explained#:~:text=confidence%20thresholds%20here-,Reply%20Delay,-You%20can%20decide). To enable delayed responses, set up a delay amount that is higher than 0.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_16409507893138.png)

With delays enabled, now you can navigate to Settings -> Actions, to set up AI agent-level Actions. We recommend using the “[Reply delay timer started](https://support.zendesk.com/hc/en-us/articles/8357756651290#:~:text=Reply%20Sent%20After%20Delay)” event to add tags to your tickets them temporarily hide them from Agents’ view, as delayed responses are not visible in CRMs before they are sent. 

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_16409539436434.png)

Once the delay period has passed, with the “Reply sent after delay” event, you can modify the tags again to make the tickets visible again to Agents.

Tag (or equivalent) management through Actions is only available in Zendesk, Freshdesk, and Salesforce.

Please note that Actions are executed instantly when a response node is reached, only the ticket responses are delayed. 

###
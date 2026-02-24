# Gathering and managing metadata for Sunshine Conversations and advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357757971866-Gathering-and-managing-metadata-for-Sunshine-Conversations-and-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

This article applies only to the [Sunshine Conversations messaging widget](https://docs.smooch.io/guide/web-messenger/), which is in maintenance mode. For similar information about the Zendesk Web Widget instead, see [Using messaging metadata with the Zendesk Web Widget and SDKs](https://support.zendesk.com/hc/en-us/articles/5658339908378).

The AI agent needs access to certain user-specific information for successful end-to-end automation that is personalized and delivers the best customer experience to your users. What are my options?

- [Gathering Metadata](#h_01GDAKXMXSJQ81X333ARVM0PNT)
- [Sunshine Conversation Requirements](#h_01GDAKXSTS6QAS5D83C2J2X0V9)
- [AI agents - Advanced Requirements](#h_01GDAKYEV2FT7TFTDVXHRDRWYP)
- [Update Zendesk Custom Fields](#h_01GDAMT02ZKV2GAS238Y267V2D)
  - [Option 1: Get tag values](#Get-the-tag-values)
  - [Option 2: Field Value ID](#h_01GDATMHFQH5QMH806MV9541VX)

### Gathering Metadata

In case we want to access some custom user information (that isn’t directly available to the AI agent in the frontend, such as the website), we recommend doing this via API integration as it makes it a lot simpler. This way, you can also reuse the integration for different channels (meaning, you don’t need to redo it for web, mobile SDK and social media channels).

This is also the approach Zendesk takes: most customer data is retrieved by API directly instead of first saving the information to SunCo and then retrieved by the AI agent.

However, some information is available to the AI agent in the frontend, such as the website, and therefore can be added to the user metadata.

As an example: *A user is logged in and requests a chat on their Booking page where they’re reviewing the details of their latest booking.*

▶️ By looking at the page URL, I can see the booking reference is visible. 

▶️ I can also see the page where the chat started from - along with locale information

▶️ Frontend also reveals whether the user is logged in to their account

As a general rule, it’s best to include information to SunCo metadata that is already available to us - like the URL of the page chat started on, whether the customer is logged in, or which channel they are using. The information available varies from client to client.

### Sunshine Conversation Requirements

In order to retrieve this Metadata, the SunCo chat widget needs to be updated. Adjust the SunCo chat widget script to capture and include all relevant metadata information the AI agent should know when a customer requests chat.

Below you can find an example, however, please do refer to [Sunshine Conversations](https://docs.smooch.io/guide/using-metadata/) for the most up-to-date information on this,

```
Smooch.updateUser({  
  
   email: 'example@email.com',  
  
   metadata: {  
  
       latestOrderNumber: 'order number',  
  
       loggedIn: 'true',  
  
  customerType: 'customer type'  
  
   }  
  
})
```

More information for adjusting the widget snippet [on Zendesk / SunCo gitHub](https://github.com/zendesk/sunshine-conversations-web#updateuseruser) and [Smooch API reference](https://docs.smooch.io/rest/#operation/updateUser)

### AI agents - Advanced Requirements

Now that you are retrieving this information, it needs to be saved to the session.

You do this with [actions](https://support.zendesk.com/hc/en-us/articles/8357756651290) to get and save metadata to the session and update it to Zendesk after the conversation with the customer endsThis can be done at the AI agent-level by adding the [Get User action](https://support.zendesk.com/hc/en-us/articles/8357734565402) to get and save the metadata information to the session. You would need to reference the Metadata Key with the names from the widget snippet (but you can save them as whatever you want):

![Screenshot_2022-09-19_at_12.23.53.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screenshot_2022-09-19_at_12.23.53.png)

The above action saves the user metadata information to the conversation session. This means, the AI agent doesn’t need to ask for this information from the user again but can update them to Zendesk through pass control (screenshot below). This way, your Support Agents won’t need to update these ticket fields manually. 

![Screenshot_2022-09-19_at_12.23.39.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screenshot_2022-09-19_at_12.23.39.png)  
  
  
When you want to update the metadata field after saving it to the session, you will need to use the Field ID from Zendesk - which you can find by going to Zendesk Admin Center > People > User Fields

A recommendation from our side is to use [conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234) to check whether the above information exists in the session, and if not, use the AI agent to ask for this information from the user

![Screenshot_2022-09-19_at_12.23.27.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screenshot_2022-09-19_at_12.23.27.png)

## Update Zendesk Custom Fields

Something to bear in mind is that SunCo doesn’t have an integration with Zendesk - this means AI agents - Advanced can’t access custom field information directly through metadata or other SunCo action. 

Custom Fields, however, can be updated via pass control i.e. when the AI agent escalates to Zendesk Agent Workspace or a ticket is created.  
  
The SunCo action `Update User` can be used to update custom fields in Zendesk, both free text and drop-down fields. 

Each Zendesk drop-down field value has an associated tag. This is what you would typically use in ZD Chat integrations to select drop-down items.

The difference with SunCo is that instead of updating the field, we can just set the tag directly. As long as it matches the tag associated with the field value, it *also* selects that option in the drop-down automatically.

### Get Tag Values

- In Zendesk, go to Settings > Ticket Fields and open the field you’re looking to update.
- In the Field Values section, click the Show Tags option at the top right to see the corresponding tags for each drop-down value.

### Add the SunCo action

For this, we’ll use `Add Tags`to add the tag. All tags will be added to the list of existing tags. This is a free text field, so you can type the name of the tag you would like to be applied. Multiple tags can be added using the plus button. 

![image__16_.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_image__16_.png)
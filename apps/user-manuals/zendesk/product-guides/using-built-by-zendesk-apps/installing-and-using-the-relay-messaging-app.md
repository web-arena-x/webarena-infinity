# Installing and using the Relay messaging app

Source: https://support.zendesk.com/hc/en-us/articles/7051551958426-Installing-and-using-the-Relay-messaging-app

---

This article includes instructions on setting up and using the Relay messaging app.

Important: You are responsible for using the WhatsApp and text features in Relay in compliance with all applicable laws. Certain jurisdictions may require end-user consent prior to initiating telephonic outreach. Meta requires end-user opt-in prior to sending proactive messages. By using these features, you agree that you have received the required consent.

[The Relay bulk messaging app by Zendesk Labs](https://www.zendesk.com/marketplace/apps/support/1040322) enables businesses to proactively reach out to their end users on either WhatsApp or SMS. This functionality up levels your customer support to create a proactive, engaging customer experience.

This article contains the following topics:

- [Before you begin](#h_01HYZZ5C9DJMK55KABX415RTPV)
- [Installing and configuring the app](#h_01HYZZ5C9DTDGAW13Z97FEJYW6)
- [Using the app](#h_01HYZZ5C9DSGCCMSJVFK40Y0XZ)
- [Best practices](#h_01HZ4Y5X3B6R8A8HV212P7XAJJ)

## Before you begin

Relay helps brands bring better support experiences to their consumers through proactive messaging for support use cases. Before you get started, make sure that the following prerequisites are in place:

- Zendesk Suite Professional or higher.
- At least one integration with WhatsApp and/or SMS (Twilio or MessageBird) via Sunshine Conversations or Talk Text.  
  Learn how to [set up a WhatsApp](../third-party-and-social-messaging-channels/adding-whatsapp-channels-to-the-agent-workspace.md) or [SMS channel with Sunshine Conversations](https://docs.smooch.io/guide/twilio-sms/#configuring-twilio).  
  [Add SMS as a channel through Talk Text](../setting-up-and-using-text/getting-started-with-text.md)
- You need to be signed in as a Zendesk admin to complete the setup.
- You must [activate Custom Objects](../custom-data/activating-custom-objects.md).
- You must have [permission to add, view, edit, and delete custom objects](https://support.zendesk.com/hc/en-us/articles/6034260247066-Configuring-agent-access-to-custom-object-records).
- For Talk text customers, agents who will use the app must have [access to Zendesk Talk](https://support.zendesk.com/hc/en-us/articles/4408882966170-Giving-agents-access-to-Talk).
- The agent must have admin or team lead permissions to use Talk Text with the Relay app.

## Installing and configuring the app

In this section, you'll learn how to install and configure the Relay app.

**To install the app**

1. In the Zendesk Marketplace, [go to the Relay app](https://www.zendesk.com/marketplace/apps/support/1040322).
2. In the upper-right of the page, click **Install**.
3. Select your account and click **Install**.

**To configure the app**

**If you want to use Sunshine Conversations channels (WhatsApp, Twilio, or MessageBird)**

1. In Admin Center, go to Apps and integrations > Conversations API.
2. Click **Create API**.
3. Enter a name for the API key.
4. Click **Next**.
5. Save the app ID, key ID, and secret key to a safe place.
6. Next, in the [Sunco token generator](https://zendesklabs.zendesk.com/hc/en-us/p/sunco-token-generator), you'll build a secure authorization token
7. In the Sunco token generator, input your saved key ID and secret key.
8. Click **Generate token**.
9. Save the displayed authorization token in a safe place.
10. Enter the app ID and authorization token.

**If you want to use Talk text**

1. In Admin Center, go to Channels > Text.
2. Click **Add number.**
3. Fill out your Zendesk subdomain under the subdomain settings. The subdomain is a unique identifier of your Zendesk account, which appears before .zendesk.com in your account URL.

**Finishing the configuration**

1. Optionally, you can change the number of blackout days to prevent you from sending a duplicate template to someone within the number of days referenced.
2. You can restrict the app to certain staff by role or by group.
3. All users of Relay must have [permission to add, view, edit, and delete custom objects](https://support.zendesk.com/hc/en-us/articles/6034260247066-Configuring-agent-access-to-custom-object-records).
4. Click **Install**.

## Using the app

Now that you've installed the app, in the following sections, you'll learn about using it:

- [Viewing existing campaigns](#h_01K1KBVGKWNC4Q54K6AQA6CCKE)
- [Creating a new campaign](#h_01K1KBBYXSV64Q428DGM5CEX9J)
- [Sending a new campaign](#h_01K1KE26B4DAMWFREGSSEK4QW3)
- [Viewing existing messaging templates](#h_01HYZZ5C9DEFN6JPN0PNCKR2CP)
- [Creating a new message template](#h_01HYZZ5C9DQW2VFXP3MKWE6V0G)
- [Creating an audience segment](#h_01HYZZ5C9E5YXKWGE2TN10Y0BB)

### Viewing existing campaigns

To view the messaging campaigns you’ve sent, navigate to the campaigns tab.

A report for each campaign can be viewed by clicking on the three dots to the right of the campaign.

![](https://support.zendesk.com/hc/article_attachments/9566434388378)

### Creating a new campaign

**To create a new campaign**

1. Click **Create campaign**.
2. Enter a name for your campaign.
3. Select the template you want to use
4. Select the integration you want to send the template with
5. Select your audience using one of the following methods:
   - Use a saved audience segment if one has been created.
   - Use a search query using [Zendesk advanced search syntax](../../agent-guide/ticket-basics/using-zendesk-support-advanced-search.md#topic_j4c_44w_rm). Common data points used in this audience creation include user tags, custom user fields, created dates, and system user fields.
   - Use a set of conditions.

Relay will present each dynamic value that was identified when the template was created.   
- Static types should be used if, for example, you’re going to send the same template each week, and want to change the day of the week each time. Every user receiving this template will receive the same value in a single send, but you can change that value the next time you send it.  
- Dynamic values will pull in relevant system user fields and all custom user fields.

### Sending a new campaign

You'll now be able to see a summary of the channel you will send to and the total audience.

**To send a new campaign**

- Click **Send**.  
  Do not navigate to a different page in Relay until sending is complete. You can navigate to other pages within Support on other tabs.  
  Your audience must stay below 10,000 users. If your audience exceeds this threshold, then you will miss users in your search results.  
  Relay will send about eight messages per second for Sunshine conversations or 4 per second for Talk text, which equates to a maximum of 28k messages per hour or 14k messages per hour, respectively

### Viewing existing messaging templates

In the Templates tab, you can view all templates you've created.

![](https://support.zendesk.com/hc/article_attachments/9566434388634)

You can click through each template, toggle between the SMS and WhatsApp previews, and view the status of the template for each integration.

SMS templates will be “Ready” at all times, as there is no overseeing body approving or rejecting templates.

### Creating a new message template

To create a new message template

1. On the Relay notification page, click **Create template from header**.
2. Enter a unique and descriptive name for your template. Meta does not permit some characters in the template name. These will be automatically removed or adjusted.
3. Select which integrations you want this template to be available on.
4. WhatsApp requires several additional pieces of information before approving a template for sending.
   - Select the category for this message template. Relay does not support the Authentication message category. For more information about the Message category, [see here](https://developers.facebook.com/docs/whatsapp/updates-to-pricing/new-template-guidelines/).
   - Select the language for this message template.
5. Optionally, enter a header. For images, documents, or videos, you need to provide a URL for where the attachment is hosted. You can use the Zendesk help center article attachments for this purpose. For WhatsApp, if you plan to create a template with attachments such as an image, video, or document, use WhatsApp Business Manager to do so. Relay only supports text as a template header for WhatsApp.
6. Enter the Body of your message. Some elements of rich text won’t be supported on different channels, but you can see the outcome in the preview.
7. Optionally, create Buttons to drive action from your recipient
   - Calls to action can be links or buttons to place a call
   - Quick replies are responses the recipient will send back to you
   - Calls to action and quick replies cannot be combined in a single message
   - Configure dynamic values. You can use dynamic values in the header, body, and buttons. Start a dynamic value with a double bracket {{ then enter an example of what the value will look like, then close the double bracket. Example: Hello, {{Clarice}} Dynamic values will then be populated in the send step with either static values (for example,  Happy {{Monday}} ) or dynamic values populated from User data points.

**Submit template**

If this template is on a WhatsApp channel, the template will be submitted to Meta and returned within 24 hours with approval or rejection. Often this takes just minutes. Then, your SMS templates will be ready immediately for sending.

1. On the Relay notification page, click **Create**.
2. Enter a unique and descriptive name for your template. Certain characters are not permitted by Meta. These will be automatically deleted or adjusted.
3. Select which integrations you want this template to be available on.

**Message step**

WhatsApp requires several additional pieces of information prior to approving a template for sending.  
**To set up WhatsApp**

1. Select the category for the message template. Relay does not support the Authentication message category. For more information about the message category, [see here](https://developers.facebook.com/docs/whatsapp/updates-to-pricing/new-template-guidelines/).
2. Select the language for the message template.
3. Optional: Enter a Header. For images, documents, or videos, you need to provide a URL for where the attachment is hosted. You can use the Zendesk Help Center Article Attachments for this purpose.
4. Enter the Body of your message. Some elements of rich text won’t be supported on different channels, but you can see the outcome in the Preview.
5. Optional: Enter Buttons to drive action from your recipient
   - Calls to Action can be Links or Buttons to place a call
   - Quick Replies are responses that the recipient will send back to you
   - Calls to Action and Quick Replies cannot be combined in a single message
6. Dynamic Values
   - You can use Dynamic Values in the Header, Body, and/or the Buttons. Start a Dynamic Value with a double bracket {{ then enter an *example* of what the value will look like, then close the double bracket. Example: Hello, {{Clarice}}
   - Dynamic Values will then be populated in the Send step with either static values (for example,  Happy {{Monday}} ) or dynamic values populated from user data points.

**Submit template**

When you submit a template, if it is on a WhatsApp channel, the template will be submitted to Meta and returned within 24 hours with approval or rejection. This process often takes just minutes, after which your SMS templates will be ready immediately for sending.

### Creating an audience segment

An audience comprises the people who will receive your message.

**To create an audience segment**

- Click **Create audience segment**.

Audiences can be created using one of two methods:

- Write your query to build your audience using [Zendesk advanced search syntax](../../agent-guide/ticket-basics/using-zendesk-support-advanced-search.md#topic_j4c_44w_rm). Common data points used in this audience creation include user tags, custom user fields, created dates, and system user fields.
- Build your audience using a set of conditions. These conditions are predefined filters that can be used to curate an audience.

This step is crucial for targeting your audience accurately and avoiding spamming your customers or employees. Refer to the search syntax article to verify the appropriate search operators and other relevant details. 

Recommendation: Spot check users that are returned in the search to confirm that they meet the audience criteria you intended.

You can add contacts from the excluded list to the included list from the Manage audience page. Contacts that match your search criteria are excluded only if you have sent that exact template to that user previously, in the time frame specified in your app configuration.

You can remove contacts from the included list from the Manage Audience page. You might do this if you have extenuating circumstances that make you want to remove someone, even if they meet the search criteria.

![](https://support.zendesk.com/hc/article_attachments/9566434391066)

Once finished, the audience segment can be saved for reuse when creating a campaign.

## Best Practices

- Always send a test message to yourself to ensure your links are working correctly.
- Store end-user opt-in status somewhere on their user record, and include this as a filter on your search query when you're sending your campaign. This could be a user tag, a check box, or similar.
- Include a call-to-action on every message to drive end-user engagement.
- It's possible your end users won't know that they can respond to your messages. You may want to include an invitation to ask questions in your templates, for example, "Let me know if you have any questions."
- Remember that WhatsApp and SMS are different from an email channel. Your messages should be short and sweet, with an optional call-to-action for more information. No one wants to receive a paragraph in a text message.
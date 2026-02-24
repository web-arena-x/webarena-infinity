# Updating dropdown fields in Zendesk through Sunshine Conversations

Source: https://support.zendesk.com/hc/en-us/articles/8357765534618-Updating-dropdown-fields-in-Zendesk-through-Sunshine-Conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The Sunshine Conversations action [Update User](https://support.zendesk.com/hc/en-us/articles/8357734565402-Actions-Overview-Sunshine-Conversations#2-update-user) can be used to update custom fields in Zendesk, both free text and drop-down fields.

For free text, it's straightforward (just use the Zendesk field ID) and described in the [Actions Overview - Sunshine Conversations](https://support.zendesk.com/hc/en-us/articles/8357734565402) article, but for drop-down fields, you can either:

- [Get the tag associated with the field value](#h_01GS83ZVJ0V16323N5CRZBN0BT)
- [Get the field value ID that you want to use](#h_01GS8407WKSK9GD1F5KDJXCWKS)

#### If you need to update different fields at different times in the conversation, it’s better to use Option 2 with the field value IDs.

## Option 1: Tags

Each Zendesk drop-down field value has an associated tag. This is what you would typically use in Zendesk Chat integrations to select drop-down items.

The difference with Sunshine Conversations is that instead of updating the field, we can just set the tag directly. As long as it matches the tag associated with the field value, it also selects that option in the drop-down automatically.

### Get Tag Value

In Zendesk, go to **Setting > Ticket Fields** and open the field you’re looking to update.

In the Field Values section, click the Show Tags option at the top right to see the corresponding tags for each drop-down value.

### Add Sunshine Conversation Action

For this, we’ll use the [Add Tag action](https://support.zendesk.com/hc/en-us/articles/8357734565402-Actions-Overview-Sunshine-Conversations#6-add-tags).

![Screenshot_2023-02-14_at_15.14.48.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_10086485369106.png)

## Option 2: Field Value IDs

These field value IDs are available via the Zendesk API via an API call or in the browser. Here’s how you can get them and use them:

### 1) Via the API

Make sure Zendesk is set up to allow API calls Activate the Zendesk API in **Zendesk Support > Channels > API**

For the easiest authentication, enable “Password access” (you can disable it right after you get the field information)

Use the List Ticket Fields request Zendesk documentation [here.](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/#list-ticket-fields)

1. Open Terminal (if you’re using Windows, you might need to [install cURL](https://developer.zendesk.com/documentation/developer-tools/getting-started/installing-and-using-curl/) first before you can do this in the command line)
2. Copy this command, replacing the {placeholders} with the correct values from the Zendesk instance: `curl https://{subdomain}.zendesk.com/api/v2/ticket_fields.json -v -u {email_address}:{password}`
3. Hit Enter

Copy the resulting JSON from the end of the message in Terminal starting at “ticket\_fields”

### 2) Via the browser

1. Sign in to Zendesk as an admin.
2. Go to this URL in your browser: `https://{subdomain}.zendesk.com/api/v2/ticket_fields.json`
3. Right-click to save the file if it doesn’t download automatically.

Once you have the ticket\_fields.json file, you can…

### Find the field value ID

Paste the JSON in a text editor, ideally one with JSON formatting like VSCode or Sublime

Locate the name of the field, e.g. “Ticket Reason”

Find the property “custom\_field\_option” where you’ll see a list of the drop-down values and their IDs. It should look like this:

![97da0a72-9fb7-4d2e-82d9-31e0343382ba.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_10086600972818.png)

## Add Sunshine Conversation Actions

In the AI agents - Advanced dashboard, add an [Update User Metadata action](https://support.zendesk.com/hc/en-us/articles/8357734565402-Actions-Overview-Sunshine-Conversations#2-update-user) at the AI agent or dialogue level.

For the Key, add the ID of the field to be updated

For the Value, add the ID of the drop-down value to select

Here’s what it should look like:

![Screenshot_2023-02-14_at_15.14.24.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_10086503528082.png)
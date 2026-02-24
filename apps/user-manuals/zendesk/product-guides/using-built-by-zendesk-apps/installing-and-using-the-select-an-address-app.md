# Installing and using the Select an Address app

Source: https://support.zendesk.com/hc/en-us/articles/4408830888730-Installing-and-using-the-Select-an-Address-app

---

The [Select an Address](https://www.zendesk.com/apps/support/46799/select-an-address/) app allows admins and agents to change the default support address associated with a ticket. This allows for greater personalization of outbound messages and easier routing of inbound tickets to appropriate groups.

This article contains the following topics:

- [Installing the app](#h_5f9c248b-04b4-40cc-9e56-14cca0dfe2ad)
- [Configuring the app](#h_a6a134ab-ecda-4e7e-962b-c649e621726f)
- [Using the app](#h_22762b1b-b3d5-4273-9592-8069e70eb15b)
- [Limitations](#h_01HXSPG7GMWZ10C87RWTEYEK5G)

## Installing the app

The Select an Address app is installed from the [Zendesk Marketplace](https://www.zendesk.com/apps/support/46799/select-an-address/).

**To install the app**

1. On the [Select an Address app listing](https://www.zendesk.com/marketplace/apps/support/46799/select-an-address/) on the Zendesk Marketplace, click **Install**.
2. Select the Zendesk account to install the app then click **Install**.
3. In the Installation section, enter a name for the app, and select [configuration options](#h_a6a134ab-ecda-4e7e-962b-c649e621726f).
4. Enable group and role restrictions if required.
5. Click **Install**.

The app settings can be changed after installation by navigating to **Admin** > **Apps** > **Zendesk Support Apps**, andunder the **Currently installed** tab, click the **Select an Address app** dropdown options, and select **Change settings**.

## Configuring the app

You can configure the following settings for the app.

**Group email addresses by brand**

Select this checkbox to group your email addresses by brand. The selection box in the app first displays the brand then email addresses allowed for that brand.

**Default to last used email address for new tickets**

Select this option to set the recipient field to the last email address used when a new ticket was created in Support.

This option is primarily intended for agents who typically create many new tickets in batches so they don't have to change the address with each ticket.

This setting overrides:

- Any email address set by the brand
- The **Apply email to group mapping on all Open tickets** setting
- The **Default email address for groups** setting

**Apply email to group mapping on all Open tickets**

When this option is turned on, mappings from the **Default address for groups**setting will apply when an agent views and saves any ticket with an Open status.

If the group isn't defined, the app will use the default email address for the brand and not the prior email address.

This option works based on the current signed-in agent’s group, NOT the ticket’s group.

For example:

{"Group A":"groupa@zendesk.com",  
"Group B":"groupb@zendesk.com"}  
  
If an agent in Group A is on the ticket AND the ticket is in Open state, then the groupa@zendesk.com address is selected. If an agent in Group B is on the ticket, groupb@zendesk.com address is selected. If the ticket status is NOT in Open state, the app doesn’t update the group mapping specified in the app setting.

The app updates the recipient field only if the current recipient field is empty or if the current recipient is NOT one of the addresses mapped to a group (any of the current agent’s groups) defaults or allowed addresses.

**Default email address for groups**

You can also set up default addresses by group. Agents can select from these email addresses in the **Select an address** app dropdown field in the sidebar of the ticket (see [Using the app](#h_22762b1b-b3d5-4273-9592-8069e70eb15b)). The email addresses displayed in the sidebar reflect the group of the agent currently working the ticket.

Any addresses used here must already be listed in the [support addresses](https://support.zendesk.com/hc/en-us/articles/4408842868506) for your Zendesk instance. These can be found by going to **Admin Center** > **Channels** > **Email**. New emails can be added by clicking **Add address**.

Specify different default email addresses for each group in JSON format. In the following example, agents in Group A would see email1@example.com as their default email address, while agents in Group B would see email2@example.com as their default email address. Make sure to include the opening and closing curly braces, quotes around each item or set of items, and commas between each group.

```
{"Group A": "email1@example.com",  
"Group B": "email2@example.com"}
```

Zendesk checks the current agent's groups to determine which email addresses to display.

If the agent is part of multiple groups:

- The app uses the agent's default group to map the default address for new tickets created directly in Support.
- If no address is associated with the agent's default group, the first address, alphabetically, will be used from any of the other agent's groups.
- If the default address in one of the agent's groups matches the brand of the ticket, that address takes precedence and is applied as the default address.

The agent's default group will also be used if an existing ticket with a **New**

Note: End-user submitted tickets will default to the support address it was received within the app, and the mappings set in **Default address for groups** will apply **Default:** to the listed support address dropdown.

**Email addresses by group**

In the **Email addresses by group** field, specify the allowed email addresses for each group in JSON format. Zendesk checks the current agent's groups to determine which email addresses to display.

In the following example, agents in Group A would see email1@example.com and email2@example.com as the email addresses available for their use in support emails. Agents in Group B would see email2@example.com and email3@example.com as the email addresses available for use. As shown in the example, the same email address can be used for more than one group. Make sure to include the opening and closing curly braces, quotes around each item or set of items, and commas between each group.

```
{"Group A": "email1@example.com, email2@example.com",  
"Group B": "email2@example.com, email3@example.com"}
```

**Disable automatic selection of address for agents in the following groups**

To turn off the automatic selection of addresses for agents in certain groups, enter a comma-separated list of group IDs.  This can be useful for Admins if they just want to go in and review a ticket set with a **New** status but not update the address.

Example: 32239293942, 29502829834

## Using the app

When choosing an address to appear as the "from" address on a support ticket, select the appropriate email address in the dropdown of the app. **The email addresses that appear reflect the allowed addresses you've configured for the current agent's groups (not the groups of the assignee).** Default email addresses are prefaced with "Default:".

![](https://support.zendesk.com/hc/article_attachments/7856435698714)

### Proactive tickets

The Select an Address app will satisfy the **Received at** condition in business rules while creating proactive tickets. For more information, see the article: [Trigger conditions and actions reference.](https://support.zendesk.com/hc/en-us/articles/4408893545882-Trigger-conditions-and-actions-reference)

## Limitations

- The app does not work on [side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746).
- At least one email address must exist in the ticket for the app to function. For example, the app won't work if a ticket is an outbound or inbound Talk call only and no email appears in the ticket body.
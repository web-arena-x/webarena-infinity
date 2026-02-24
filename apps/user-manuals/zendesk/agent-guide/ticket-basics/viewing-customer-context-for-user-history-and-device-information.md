# Viewing customer context for user, history, and device information

Source: https://support.zendesk.com/hc/en-us/articles/4408829170458-Viewing-customer-context-for-user-history-and-device-information

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Access customer context through the context panel to view user profiles, interaction history, and device information. This feature helps you understand customer needs by displaying essential details like contact info, recent interactions, and pages viewed. You can also update user profiles and filter interactions by application or event type, enhancing your ability to provide personalized support.

This article describes how to view customer context in the context panel, including additional user profiles and events from applications other than Zendesk. You must have the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to use the context panel.

This article includes the following sections:

- [About customer context](#topic_y1j_x4z_vkb)
- [Displaying customer context in a ticket](#topic_ycf_dpz_vkb)
- [Using the user essentials card](#topic_q5j_kpz_vkb)
- [Viewing interaction history](#topic_nq1_qnm_xsb)
- [Using pages viewed](#topic_ehg_1qz_vkb)
- [Viewing device information (live chat and messaging)](#topic_mgz_ljm_3bc)

**Related articles**

- [Using the context panel in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408836526362)
- [Adding Sunshine user profiles and events to customer context](https://support.zendesk.com/hc/en-us/articles/4408828663322)

## About customer context

To provide better, faster, and more personalized responses to customers, you can view customer context in a ticket. By default, customer context includes:

- A **user essentials card** with details about the support requester, including contact information, time zone, and language.
- **Interactions** with a list of recent conversations, tickets, and and other related events from the requester. Agents can use this to better understand what the requester needed help with recently.
- **Pages viewed** which displays the 20 most recent account web pages or help center articles viewed by the requester. Formerly known as Visitor Path.
- **Device information** For live chat and messaging, displays useful device information associated with the user, including location, IP address, device type, OS, and browser.

 Light agents, contributors, and agents in a Chat-only role can't view end user device information.

Additionally, if [enabled](https://support.zendesk.com/hc/en-us/articles/4408828663322) by your administrator, customer context can include additional user profiles and interaction history (events) from applications other than Zendesk.

## Displaying customer context in a ticket

When viewing a ticket , you can open the customer context panel to view more information about the support requester. The conext panel is closed by default.

**To view customer context**

- Click the **User** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customer_context_user_icon-aw.png)

## Using the user essentials card

The user essentials card displays basic profile information about the ticket requester, including user name, contact information, social identities, organization membership, time zone, and preferred language.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customer_context_essentials.png)

You can [make basic updates to the user essentials card](#topic_nj4_ylm_xsb). If [allowed](https://support.zendesk.com/hc/en-us/articles/4408828663322) by an account administrator, you can also [view the requester’s additional user profiles](#topic_x35_wrz_vkb) for integrated third-party applications.

(Professional plans and above) If [configured by an admin](https://support.zendesk.com/hc/en-us/articles/5768595554714), the user essentials card may display additional information about the ticket requester. This information can include additional contact information, or custom fields, such as a membership ID.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customized_essentials_card.png)

Note: While an admin may have configured additional fields for the user essentials card, the fields will only display in the context panel if they contain a value.

### Updating the user essentials card

You can update the user essentials card by adding a note, or editing the requester’s Zendesk user profile.

**To add a note to the user essentials card**

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. In the user essentials card, enter your comments in the user notes text editor (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customer_context_note_icon.png)). Text added here becomes part of the requester’s profile and is not associated with the specific ticket.

**To edit the requester's profile**

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. In the essentials card, click the view more details icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_view_more_details.png)). This opens the profile page. See [Viewing a user’s profile in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408822762650) to learn more about the information in the profile.

### Viewing additional user profiles

Depending on which applications your account supports, your customers may have more than one user profile. For example, your customer may have a Shopify user profile in addition to their Zendesk user profile. To help you resolve customer issues, it can be useful for you to see each profile.

Note: The third-party user profiles you see in customer context are typically not the complete user profile from an application. Instead, the profiles show only what application developers choose to present to Zendesk.

This option is only available if [enabled](https://support.zendesk.com/hc/en-us/articles/4408828663322) by an account administrator.

**To switch between profiles**

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. In the essentials card, click the Profiles menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/profiles_menu_icon.png)) next to the user’s name and select the profile you want to view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/profiles_switch.png)
3. If there are more than 10 fields in the profile, you can click **View all** at the bottom of the list to see a full description. Click **View less** to collapse the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/profiles_shopify.png)

## Viewing interaction history

Interactions list the requester’s recent Zendesk user events, as well as events for any other integrated applications. You can [view or preview the tickets in this list](#topic_vwt_xnm_xsb), and filter the interactions to locate specific events.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customer_context_interactions.png)

### Viewing a ticket in the interaction history

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of a ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. Hover over the title of any ticket in the interaction history to see a preview, or click the ticket title to open the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customer_context_preview.png)

   If a ticket displays the subject "Incident," this means that the ticket was created with no subject.

   Note: Archived tickets are excluded from the interaction history. For information about how to view archived tickets, see [About ticket archiving](https://support.zendesk.com/hc/en-us/articles/4408887617050).

### Filtering interactions (user events)

Your customers may have interactions for more than one application. To help you resolve customer issues, it can be useful for you to filter user events by application or event type.

**To filter interaction events**

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. In **Interactions**, click the **filter** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/interactions_filter_icon.png)).
3. Use the drop-down top select the events you want to view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/events_filter_apps.png)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/events_filter_event_type.png)

   You can view:

   - All events for all applications
   - All events for a specific application
   - A specific type of event for an application
4. To clear the filter, click the refresh icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/interactions_refresh_icon.png)).

## Using pages viewed

Customer context also includes **Pages viewed** (also called visitor path), which displays the 20 most-recent web pages, app screens, or help center articles viewed by the requester. Tracking begins when an end user first lands on any page with a Web Widget or mobile SDK embedded in it, and only pages with a widget or SDK embedded are recorded. The list is updated in real time – it shows what the requester is currently viewing, and updates if they move to another page, screen, or article.

The chat visitor path persists only while a chat session is active. This is because the visitor path loses significance when a chat session ends. In Messaging, the visitor path persists across sessions.

Light agents can't access the Pages viewed list.

Note: On a mobile app, you must use the Page View API to display the path. see the developer documentation for [iOS](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/ios/advanced_integration/#visitor-path) and [Android](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/android/advanced_integration/#visitor-path) for more information.

**To view the pages viewed list**

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. In **Pages viewed**, click the down arrow (v) to expand the list.

   This displays the web pages, app screens, or help center articles the requester has viewed, including what the requester is currently viewing, that meet the criteria listed above.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pages_viewed_aw.png)
3. If the customer is using the Web Widget to conduct the conversation, click any link in the list to open the pages they have viewed. A path in a conversation initiated via a mobile SDK *does not* include active links.
4. If there are more than three events in the list (or more than 10 for live chat conversations), click the **View all** link at the bottom of the visitor path to see an expanded list, with a maximum of 20 events.

### The warning banner (live chat only)

The Chat path may also display a warning banner, alerting the agent to a discrepancy between the visitor's existing profile and the data collected in a pre-chat form. This banner is informational-only. See [Understanding the warning banner in the customer context panel](https://support.zendesk.com/hc/en-us/articles/4408846631194)
for more information.

## Viewing device information (live chat and messaging)

When the device information activated in the Agent Workspace, agents can view it in the customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362). Device information is view only.

**To view device information**

1. Click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. Expand the **Device information** section.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/device_information_aw.png)
3. (Messaging tickets only) Click the reload icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/reload_icon-device_info.png)) to refresh the information.
# Asks

Asks turns requests like bug reports, questions, and IT needs into actionable issues in Linear.

> [!NOTE]
> Available to workspaces on our [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans. Additional features available to Enterprise workspaces through Advanced Linear Asks.

![Linear logo and Asks logo](https://webassets.linear.app/images/ornj730p/production/cafe02ae27a254a6eda1dc00b00d91d063cd7656-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Linear Asks gives organizations a powerful tool to manage common workplace requests. Once enabled, anyone can create an Ask to send their request to the relevant Linear team—even if they don’t have a Linear account—via Slack or email.

### Purpose and use cases

Linear Asks is purpose-built to support internal requests that are typically scattered across tools or lost in chat threads. It’s ideal for:

* **Engineering teams** receiving bug reports from non-technical staff
* **IT and support teams** fielding hardware, access, or setup questions
* **Operations and HR** gathering requests from across the company
* **Product and design** teams collecting feedback or feature requests

By providing familiar and low-friction channels, Asks allows teams to quickly make requests without context switching.

### Multi-channel request intake

Linear Asks supports multiple intake channels to meet teams where they already work:

Asks with Slack | Asks with email --- | --- Users can submit Asks directly from Slack, using a simple flow that turns messages into issues without leaving the conversation.

When Asks are submitted to a Linear team, they will always arrive in the team's Triage where they can be reviewed, prioritized, and assigned.

Asks issues in Linear have a comment thread synced with Slack. Any replies to this shared comment thread will cross-post to the Asks Slack thread and notify the creator of the Ask (and vice versa). | Set up a custom email address (e.g., `helpdesk@acme.com`) to automatically forward messages to a unique Linear intake address.

Each email received will create a new Linear issue, using the email subject as the issue title and the message body as the description. Senders will receive a confirmation email letting them know any replies they send will be synced to the same Linear issue.

A synced thread will be visible within the Linear issue. Teams can reply to the original email directly from this thread and view any incoming responses as they arrive.

> [!NOTE]
> It’s important to note that Asks via email intake is not designed for high-volume, front-line customer support, therefore feature development does not reflect those found in other customer support tools—first response times, NPS scores, etc. As part of Linear's development, we will continue to evolve the feature for internal requests.

### Linear Asks vs Advanced Linear Asks

Asks features are available in both Business and Enterprise plans, with additional features available to Enterprise workspaces as follows: 

Feature | Business

(Linear Asks) | Enterprise

(Advanced Linear Asks)
--- | --- | --- Email intake & replies | ✔ | ✔ Custom email domains | ✔ | ✔ Private Asks (DMs & Linear Asks bot) | ✔ | ✔ Asks fields | ✔ | ✔ Auto-create on :ticket: emoji reaction | ✔ | ✔ Form templates support | ✔ | ✔ Asks in private Slack channels | | ✔ Per-channel configurations | | ✔ Auto-create on new message | | ✔ Multiple Slack workspaces | | ✔

---

## Using Linear Asks with Slack

### Configure Asks

#### Install Asks

1. Navigate to [Settings > Features > Asks](https://linear.app/settings/asks)
2. Click the "+" icon under Slack intake to **Connect Asks integration**
3. Authenticate into a Slack workspace

#### Connect teams and invite @Linear Asks

1. Click the three dots next to **Private Asks** or **All public Slack channels**.
2. Hover over **Add teams to channel**
3. Select the team to add to a private Ask or a public Slack channel. Repeat this process for each channel that will be used to create Asks. DMs do not need to be added as channels.
4. Add Asks to each channel using `/invite @Linear Asks` in Slack

There are some Asks that you’ll want to keep private between the requester and the team managing the issue. Add these sensitive requests under the Private Asks section in Asks settings. Private Asks includes Asks in DMs or created in the Asks app home (Apps > Linear Asks in Slack's sidebar). Asks templates added to Private Asks are available when creating Asks in DMs.

> [!NOTE]
> Ensure that the Linear teams you connect to Private Asks are also private. This guarantees that only members of the desired Linear team will see content shared on that issue.

#### Per-channel configuration

1. Click **Add channel** button
2. Select the correct Slack workspace
3. Select the specific channel
4. Click **Allow**
5. Add Asks to each channel using `/invite @Linear Asks` in Slack

> [!NOTE]
> To set up Asks with a private channel, use a channel-specific configuration.

#### Add templates to channels

If you wish to allow users to submit Asks without selecting a template, keep "Create Asks without a template" enabled.

Select available templates under each team. Workspace level templates are not available for use with Asks.

Asks templates added to Private Asks are available when creating Asks in DMs.

#### Enable auto-creation

Configure automations in settings to allow Asks to be created automatically. Asks auto-creation is not supported in DMs.

Select a default template by hovering over the template you wish to use, and clicking "Set as default". This template will apply to auto-created Asks in the set context. The description of the template will not be used and will be replaced by the user's message. If you'd just like to select a default team, consider selecting a default of "Create Asks without a template."

##### On 🎫 emoji

By default, users can turn a message in Slack into an Ask by reacting to it with the 🎫 (:ticket:) emoji. This can be turned off in Asks settings as shown below. Starting a Slack message with 🎫 will also trigger this behavior. 

![channel specific settings for auto-creation](https://webassets.linear.app/images/ornj730p/production/97a93b1802e88163e116b2cc7aa7c1fc071a5a91-1400x510.png?q=95&auto=format&dpr=2)

Bot-posted messages can create an ask on 🎫 if the bot's message's first character is 🎫. 

If multiple Linear teams are associated with the channel or channel type in your Asks settings, the 🎫 emoji will create an issue in the team template marked "default."

##### On every new message

For Slack channels meant solely for the creation of Asks, you can enable auto-creation whenever a new message is posted to the channel. This is common for channels such as #it-asks or #bugs, in which you want all messages to be triaged. This feature is available on Enterprise plans only as it requires a single-channel configuration.

To exempt a message from creating an Ask with this setting on, begin the message with 📢 or 📣 emojis.

Please note that this auto-creation on new messages is not available in private channels

##### On mentioning Asks

If desired, Slack users can also create an ask by mentioning `@Linear Asks` in the body of their Slack message. 

<details>
<summary>View in Settings</summary>
![On bot mention selected in Asks settings](https://webassets.linear.app/images/ornj730p/production/71a682a280b322873fb4e08dc097d532a033917f-1634x576.png?q=95&auto=format&dpr=2)
</details>

##### On bot-posted messages

Bot-posted messages can create an Ask automatically if the bot's message begins with 🎫. Use this behavior when auto-create Asks "on 🎫 reaction" or "On new message" is enabled. On Business plans, you can still use this functionality to allow bot messages to create Asks, provided the bot message is sent in a public channel.

<details>
<summary>View in settings</summary>
![Settings showing Asks auto-create on new message turned on](https://webassets.linear.app/images/ornj730p/production/cf8decfafc05650050dccd5b26dae8af3b475a43-1666x426.png?q=95&auto=format&dpr=2)
</details>

### Set permissions for managing Asks

Linear admins can determine whether Asks channels, teams and templates can be managed by all users, or admins only.

![Allow members to manage Asks](https://webassets.linear.app/images/ornj730p/production/a39ecbd9a59ce94927a590c95f9950fb64430bdb-721x154.png?q=95&auto=format&dpr=2)

### Customer field visibility

For organizations using Customer requests, Asks has the capacity to surface a customer field. This can be helpful when someone wants to associate a particular Slack message with a particular customer. With customer requests on, this happens automatically when the Slack message was sent by your actual customer, but not if it's being raised internally. 

This field is sensitive, as it contains the list of your customers. 

Choose to make the field available to Linear users only in Slack, all members in your Slack workspace, or Slack members and Guests.

### Customize templates

When creating Asks from a template, the newly created issue will use the properties assigned to the template by default. Create or edit templates under Template settings for the relevant team. Workspace-level templates cannot be associated with Linear Asks. 

There are a variety of formatting tools you can use to customize the behavior of a particular template. Form templates are particularly useful in combination with Asks. Learn more about template fields [here](https://linear.app/docs/issue-templates).

> [!NOTE]
> If you set required form template fields on a default template for a channel, auto-creation options will not be available.

### Submit Asks in Slack

From any connected Slack channel, use the following actions to create an Ask:

Creation method | Location --- | --- Create from an existing Slack message | Overflow menu on a Slack message Create from a slash command | Use the /asks slash command in Slack and hit Enter Create Private Asks | In your DM with Asks in Slack (Apps > Asks from the sidebar), select the option to Create Private Ask Auto-create with emoji | Apply the 🎫 (:ticket:) emoji to a message in Slack Auto-create on new public channel messages | Configure in Asks settings per-channel Auto-create on @Linear Asks | Configure in Asks settings per-channel

Once created, Asks will create a threaded reply with a link to the Ask and connected Linear issue. The Slack thread and Linear issue share a synced comment thread, so comments and files can be shared across both applications.

Whoever submits the Asks can see the issue status, assignee, and reply in the synced comment thread. They will be notified on the thread automatically when the Ask is completed, canceled, or re-opened.

Users with a Linear account will be able to make updates to Asks from Slack using the Quick Actions menu, including changing the status and assigning it to themselves.

### Manage your Asks from Slack

**View Asks**

Navigate to the Linear Asks bot in Slack. See a list of all active and closed Asks in Linear Asks > Home tab. Click _Open thread_ to go to the Ask in the channel it was created. You can also view Asks and their threads (including private Asks) in the Messages tab.

**Mark as urgent**

If your Ask is urgent, you can choose to override its default priority by selecting the _Mark as urgent_ option in your Ask's unfurl menu. This will also apply a siren emoji to your Ask for better visibility in Slack.

**See status and assignee**

Asks app home will show the real-time status and assignee of your Ask. You'll also be notified in the original thread when your issue leaves Triage (all Asks start in Triage), and when it's completed, canceled, or reopened. In a shared channel using Asks, users from the other organization will not see Asks app home.

**Reply and share files**

Reply to the Slack thread to ask questions, follow up on the Ask, or even send files, screenshots, and video to the assignee working on your Ask. All replies are sent to the Linear issue on a synced comment thread.

**Close Asks**

You’ll get a notification on the thread whenever a comment is posted to the Ask and when the Ask is completed, canceled, or re-opened. When completed, the Ask message will also have a ✅ on the original Ask.

Requestors can close their own Asks in Slack from _Linear Asks > Home_ by changing its status. 

---

## Using Linear Asks with email

### Permissions

Admins can add new email, edit, or delete a custom intake email. Members can change settings related to the configured email (team/template/sync-reply/customer requests).

### Configure

1. Navigate to [Settings > Asks](https://linear.app/settings/asks)
2. Click the “+” icon for **Add Asks intake email**
3. Select the Linear team and [optional] issue template that should be applied to incoming emails to this address.
4. A unique forwarding email will be created.
5. [Configure email forwarding](https://linear.app/docs/linear-asks#configure-email-forwarding-in-google-workspace) so emails sent to your custom email address are forwarded to the unique Linear email address.
6. _(Optional)_ If you want your replies to appear from your custom email address, upload the provided DNS records to your DNS hosting provider, or provide these records to an engineer on your team. If this step is skipped, the replies will still be delivered, but they will come from a Linear address (issues@linear.app) instead of your own.

### Configure email forwarding

<details>
<summary>Configure email forwarding in Google Workspace</summary>
You will need administrator permissions to set up email forwarding in your Google Workspace.

> [!NOTE]
> We do not recommend using Google Groups to set up forwarding as it modifies email headers which can result in several downstream issues.

Refer to Google’s help documents in [Forward email to a third-party CRM](https://support.google.com/a/answer/10486484?product_name=UnuFlow&hl=en&visit_id=638690871651590812-3129432273&rd=1&src=supportwidget0&hl=en) for more details.
</details>

<details>
<summary>Configure email forwarding in Microsoft 365</summary>
1. Log into your [Microsoft 365 Admin Center](https://admin.microsoft.com/)
2. Select the mailbox that you wish to configure forwarding for:
 1. **Shared mailbox:** On the admin center homepage, go to the _Teams & groups > Shared mailboxes_ page. Select the mailbox, then select **Edit** in the "Email forwarding" section.
 2. **User:** On the admin center homepage, go to the _Users > Active users_ page. Select the user, then the mail tab and select **Manage email forwarding** in the "Email forwarding" section.
3. On the "Shared mailbox" email forwarding side panel, select the "Forward all email sent to this mailbox" checkbox.
4. Enter your Linear intake email address copied from Linear Email Asks Settings
5. Select **Save**

> [!NOTE]
> Automatic forwarding needs to be enabled in your anti-spam outbound policy before trying to verify your forwarding setup. This is found in the [Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-office-365/outbound-spam-policies-configure).

Refer to Microsoft's help documents in [Configure email forwarding in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/email/configure-email-forwarding?view=o365-worldwide).
</details>

<details>
<summary>Configure email forwarding for other email providers</summary>
Refer to your providers routing/forwarding instructions.
</details>

### Configure DMARC Policy Requirements

Linear Asks email integration supports a wide range of DMARC configurations. Our primary requirement is that domain alignment is set to **relaxed**:

* `aspf=r` (relaxed SPF alignment)
* `adkim=r` (relaxed DKIM alignment)

Strict alignment (`aspf=s` or `adkim=s`) is not supported and will cause delivery or authentication issues.

#### **Default Policy**

We recommend starting with a neutral monitoring policy:

`v=DMARC1;p=none`

This is our default recommendation because it does not interfere with existing email setups and allows domains to collect DMARC reports before enforcing stricter rules.

#### **Enforcing Policies**

If desired, customers may use a more restrictive policy such as:

* `p=quarantine`
* `p=reject`

As long as relaxed alignment (`aspf=r`, `adkim=r`) is maintained, these policies are fully compatible with Linear Asks.

### Configure the reply sender email address

To have replies appear from your custom email address instead of the default Linear address (`issues@linear.app`), you'll need to update your DNS settings. **Add the provided DNS records** to your DNS hosting provider. Alternatively, share them with your engineering team for implementation.

**Important:** If you skip this step, replies will still be delivered, but they'll be sent from Linear’s default email (`issues@linear.app)` address rather than your own.

### Synced email thread

![Synced email thread](https://webassets.linear.app/images/ornj730p/production/8483ed7271453dc3f42888a71803c886cb052dfa-1604x776.png?q=95&auto=format&dpr=2)

When an issue is created from an email, a synced thread will appear in the Linear issue, allowing members in Linear to communicate with requesters directly.

* Any new email reply to the original email thread will appear as a comment in the synced thread within Linear
* Any new comment on the synced Linear thread will be sent out as a new email to the email thread

This keeps all context centralized in Linear while enabling seamless communication with non-Linear users.

### Customize auto-replies

By default, new emails are sent by Asks when an issue is first created, and again when it's completed or canceled. Customize which messages are sent, and their copy in Settings > Asks > Email Intake > [Email address].

![Shows how to customize auto-replies](https://webassets.linear.app/images/ornj730p/production/6e08009215e8519086fc1c87cb7a9dc51b21a1f3-756x459.png?q=95&auto=format&dpr=2)

### Enable customer requests

Toggle this feature on to automatically link inbound emails with customers based on the sender’s email domain. Refer to [customer requests](https://linear.app/docs/customer-requests) feature for more details.

---

## FAQ

<details>
<summary>Can Asks be used in shared Slack Connect channels?</summary>
Yes! In a shared channel initiated by your organization, use Asks as you would in a public channel.

Users in the channel from _external_ Slack workspaces can create issues in your Linear workspace by applying the 🎫 `:ticket:` emoji reaction or mentioning `@Linear Asks` if enabled in Asks settings. If you've enabled auto-creation on every new message in the channel, this will create issues from the messages of both internal and external users.

Entrypoints to Asks not mentioned above are unavailable to external users in a shared channel.

External users can also mark their Ask as urgent through the overflow menu in its unfurl.
</details>

<details>
<summary>Why are there multiple Asks icons in a Slack thread?</summary>
There is a limitation to the Slack integration where it will show up as a new person for every unique `User via Linear` response. There is not a way to fully get around some duplication in avatars.
</details>

<details>
<summary>Can I link a Slack thread to an Linear issue over API to create a synced thread?</summary>
Yes, you can link an existing Slack thread to a Linear issue over our API. To do so, pass `syncToCommentThread: true` in the input to the `attachmentLinkSlack `mutation (documentation is available [here](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/Mutation?query=attachmentLinkSlack#attachmentLinkSlack).)
</details>

<details>
<summary>Can Asks be used in multi-person DMs?</summary>
If you start a DM with multiple users that includes _Linear Asks_ as a recipient from the beginning, you'll be able to use Asks there. However, as Slack will not allow you to add a bot user to an ongoing multi-person DM, you cannot create an Ask from an ongoing conversation that did not have _Linear Asks_ in it from the start.

On Enterprise Linear plans, you can workaround this if desired by converting the multi-person DM to a private channel. Then, adding a configuration for that channel in Linear's Asks settings will allow you to create Asks from that private channel.
</details>

<details>
<summary>Can I use Asks in multi-workspace channels on an Enterprise Grid? </summary>
Yes, though some setup is required.

1. Check which workspaces in your Grid the channel belongs to in Slack. 
2. Ensure that each of those workspaces is connected to Asks in Linear > Settings > Asks
3. From that same Asks settings page, open each workspace and add the channel. Ensure that your auto-create settings are the same to ensure consistent behavior.
</details>

<details>
<summary>When do URLs associated with an Ask show unfurl previews in Slack?</summary>
* If an Ask is associated with a private team, it will never unfurl in Slack
* Please ensure that "Enable unfurls and actions in Slack" is toggled on in Settings > Integrations > Asks if you wish to see Asks unfurls in Slack.
</details>

<details>
<summary>Why am I not seeing some linked private channels in Asks settings?</summary>
We only show private channels in Asks settings if we can verify that you belong to those channels in Slack. If you do belong to the channel:

* Please ensure you've linked your Slack account to Linear in Settings > Connected Accounts
* Double check the Linear Asks bot is a member of the private channel. It can be added using `/invite @Linear Asks` if it's not already a member. After doing so, refresh your Linear client with Cmd/Ctrl + R and check settings again.
</details>

<details>
<summary>Can I configure email forwarding from inbox settings?</summary>
You can use per-account Gmail forwarding, which requires no Google Workspace admin permissions. This requires you to have a dedicated Gmail user—costing money—and requires confirming access to the intake address where Gmail will send an email with an activation code to the intake address that you will need to input back into Gmail settings.

![Email forwarding from inbox settings](https://webassets.linear.app/images/ornj730p/production/599c4660688b67df4a584b70552bbaa3bb49d455-1147x452.png?q=95&auto=format&dpr=2)
</details>

<details>
<summary>DNS Error using email Asks with Microsoft 365</summary>
When hitting the error

`550 5.7.520 Access denied, Your organization does not allow external forwarding. Please contact your administrator for further assistance. AS(7555)`

Microsoft 365 (Outlook) by default blocks automatic forwarding to external email addresses to prevent data exfiltration/phishing abuse, even if you set up an inbox rule to forward. You will need an admin to explicitly allow it in the Exchange or Defender policies.

**Allow external forwarding as Exchange admin:**

1. Navigate to **Microsoft 365 Admin Center**
2. Open the **Exchange Admin Center (EAC)**
3. Navigate to **Mail Flow → Remote Domains**
4. Edit the default (or relevant) remote domain (usually `*`)
5. Set "Allow automatic forwarding" to **"On"**

**Fix via Microsoft 365 Defender UI**

1. Go to [https://security.microsoft.com/antispam](https://security.microsoft.com/antispam)
2. Go to **Email & Collaboration → Policies & Rules → Threat policies → Anti-spam policies**
3. Click into your **Outbound spam filter policy** (likely called “Default”).
4. Scroll down to the **"Automatic forwarding rules"** section.
5. Set it to **"On – allow automatic forwarding"**
6. Save the policy.
</details>

<details>
<summary>"Address not found" error</summary>
Double check your forwarding settings to ensure it is set up for the custom email address to be forwarded to the Linear intake email address.
</details>

# About banning IP addresses from messaging channels

Source: https://support.zendesk.com/hc/en-us/articles/9418700382618-About-banning-IP-addresses-from-messaging-channels

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Note: The feature described in this article is similar to [banning visitors by IP address in live chat](https://support.zendesk.com/hc/en-us/articles/4408824467098).

You can restrict end-user access to your Zendesk messaging channels by banning their IP address.
When an IP address is banned from your Web Widget, iOS SDK, and Android SDK messaging channels, all end users from the banned address will be unable to conduct conversations with your AI or human agents.

This article includes the following sections:

- [Considerations when banning IP addresses from messaging channels](#topic_fhl_tc1_wfc)
- [IP address banning permissions for user roles](#topic_itk_myj_xfc)
- [Identifying banned IP addresses](#topic_gyl_sch_dgc)
- [The end-user experience](#topic_ztg_z2h_dgc)

Related articles:

- [Restricting access to messaging channels by IP address](https://support.zendesk.com/hc/en-us/articles/9418691150106)
- [Managing IP addresses banned from messaging channels](https://support.zendesk.com/hc/en-us/articles/9535836802074)
- [Accessing and using the Banned IP addresses page in Admin Center](https://support.zendesk.com/hc/en-us/articles/9435777614874)

## Considerations when banning IP addresses from messaging channels

IP banning for messaging channels is available on all accounts that meet the feature requirements and is applied at the account level. That is, the ability to ban IP addresses is the same across all web and mobile messaging channels associated with your account.

You can specify individual IP addresses, or a range of IP addresses. See [Restricting access to messaging channels by IP address](https://support.zendesk.com/hc/en-us/articles/9418691150106).

Your account must meet the following **requirements** to Ban IP addresses in messaging channels:

- For most account types, IP banning is restricted to account administrators and billing administrators. However, Enterprise-level accounts can add IP address banning permission to custom roles.
- To ban IP addresses, or view banned IP addresses, from Agent Workspace, you must be [displaying IP addresses in the Customer Context panel](https://support.zendesk.com/hc/en-us/articles/7041910642074).
- By default, permission to ban IP addresses from messaging channels is not allowed for custom roles.

Currently, the following **limitations** apply to the Ban IP in messaging channels feature:

- Banning messaging channel access by IP address is only available for the Web Widget, iOS SDK, and Android SDK channels. It is not available for social or third-party messaging channels, or the Unity SDK channel.
- You can have up to 5,000 unique banned IP records. A unique ban IP record is an individual IP address or a range of IP addresses.
- It can take a few seconds for an IP ban to take effect. Although uncommon, an end user from a newly banned IP address may be able to initiate a new messaging conversation during that time.

## IP address banning permissions for user roles

If you are on an Enterprise account, you can [give agents permission](https://support.zendesk.com/hc/en-us/articles/4408883763866) to ban IP addresses.

Permission is granted at the role level; all agents assigned a role with permission to ban IP addresses will be able to perform this function.

By default:

- Light agent and contributor system roles have No access, meaning they can’t view, apply, or edit IP bans.
- Admins and Billing admins can add, view, edit, and delete IP bans.
- Agents in [custom roles](https://support.zendesk.com/hc/en-us/articles/4409155971354) can only ban IP addresses if their role allows it.

**To permit agents to ban IP addresses (Enterprise plans only)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Click the role you want to edit, or [create a new custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).
3. Under **People**, find **Ban IP addresses**, select the permission level you want to apply to the role:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/IP_ban_custom_role_settings.png)

   - **No access**: Agents can’t view, apply, or edit IP bans.
   - **View only**: Agents can access the Banned IP page, but can’t edit it or apply IP bans.
   - **View, add, edit, and delete**: Agents can apply and remove IP bans, and can access the Banned IP page.
4. Click **Save**.

## Identifying banned IP addresses

If allowed for your user role, you can view and identify banned IP addresses in several places across Zendesk.

In Admin Center:

- The IP address is added to the [Banned IP addresses page](https://support.zendesk.com/hc/en-us/articles/9435777614874) in Admin Center.
- The banning event appears in your account’s [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434).

In Agent Workspace:

- A label is added to the [device information in the context panel](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_mgz_ljm_3bc).

Note: You must have permission to ban IP addresses, and your account must be configured to [display IP addresses in the Customer Context panel](https://support.zendesk.com/hc/en-us/articles/7041910642074), to view banned IP addresses in Agent Workspace.

## The end-user experience

When an IP address has been banned, any end user from that IP address will be unable to communicate with your agents through the Web Widget or mobile channel.

Note: End users are *not* notified automatically when their IP address is banned. Admins should instruct agents to communicate the ban with an in-channel message or [create a macro](https://support.zendesk.com/hc/en-us/articles/4408844187034) to avoid end-user confusion.

| | Conversation in progress when IP ban applied | New conversation after IP ban applied |
| --- | --- | --- |
| Description of behavior | - Banned user can’t send a message in the   conversation. - Unsent message appears in red. | - Conversation doesn’t load in channel. |
| Web Widget example | | |
| Mobile SDK example | | |
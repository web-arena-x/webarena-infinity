# Adding Facebook Messenger channels

Source: https://support.zendesk.com/hc/en-us/articles/4408835753370-Adding-Facebook-Messenger-channels

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Social Messaging add-on |

Customers without Zendesk Suite must have Support and Chat with the Social Messaging add-on to use this feature.

Location: Admin Center > Channels > Messaging and social >
Messaging

This article describes how you can add Facebook Messenger channels. Facebook Messenger is a popular American messaging app that enables you to send private messages through Facebook.

Facebook Messenger is used for *private messaging* with your customers, and Facebook is used for *public messaging* with your customers. To set up Facebook, see [Setting up your public Facebook channel](https://support.zendesk.com/hc/en-us/articles/4408819897242).

You must be an administrator to add Facebook Messenger channels.

This article includes these sections:

- [Adding a Facebook Messenger channel](#topic_ow1_tbj_smb)
- [Next steps](#topic_e5s_bcj_smb)
- [Limitations](#topic_drz_ybj_smb)
- [No other data shared with Meta/Facebook](#topic_w4b_lf3_ywb)

## Adding a Facebook Messenger channel

You must be an admin to add Facebook Messenger.

The following video gives you an overview of how to add a Facebook Messenger channel:

Automating a Facebook Messenger channel [1:40]

**To add a Facebook Messenger channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Add channel** and select **Facebook Messenger**.
3. From the **Add Facebook Messenger** screen, click **Continue with Facebook**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_facebook_sign_in_initial_v2.png)
4. When prompted, log in to your Facebook account as a user with Admin permissions for all accounts being added, then follow the on-screen instructions to authorize Zendesk to use your Facebook account.
5. Select all the Facebook pages you want to manage in Zendesk, and ensure page permissions are toggled to **Yes**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/fb_messenger_permissions_toggle.png)
6. On the **Add Facebook Messenger** screen, choose a Facebook page from the list and then click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_facebook_choose_page.png)
7. Click **Add channel**.

   When the channel connects successfully, a **Channel added** message appears.
8. Enter a **Channel name**.
9. If your account has [multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), select a **Brand** to associate with the channel.
10. Click **Save settings**.

## Next steps

After you add Facebook Messenger channels, you may need to complete these additional tasks:

- **Set roles for agents** who will participate in social messaging conversations. See [Give agents access to messaging](https://support.zendesk.com/hc/en-us/articles/6073485578010).
- **Adjust your Facebook Messenger business rules and views**, as needed. See [Setting triggers, automations, and views for social messaging](https://support.zendesk.com/hc/en-us/articles/4408824058138#topic_nbm_dsl_2mb).

 When using Facebook Messenger, you need condition statements that read **Channel + Is
 + Facebook Messenger** and **Brand + is + [selected brand]**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_fb_condition_trigger_v3.png)

 Do not use **Facebook Private Message** in your condition statements.
- **Set up auto-responders** for your Facebook channels. See [Sending automatic responses to social messages](https://support.zendesk.com/hc/en-us/articles/4408838007578).
- **Add your Facebook accounts**, if you want to send and receive public messages from Facebook pages. See [Setting up your Facebook channel](https://support.zendesk.com/hc/en-us/articles/4408819897242). When you do, make sure that the setting to capture incoming direct messages as tickets remains disabled.

## Limitations

This section describes some limitations about using Facebook Messenger in Zendesk.

- There's a 2000-character limit for messages sent through Facebook Messenger. Messages longer than that will not be delivered.
- When an agent uses Facebook Messenger to respond to a direct message, the agent's response does not sync to Zendesk. Agents must post messages in Zendesk to see their responses in Zendesk.
- Facebook Messenger allows a business only seven days to respond to the end user before the messaging window closes. To prevent messages from being sent but not delivered, the composer will be blocked once the messaging window is closed. The only way to re-open is if the end user sends a new message.

## No other data shared with Meta/Facebook

Aside from the conversations occurring directly through your Facebook Messenger account within Zendesk, no other data from your Zendesk account, such as ticket metadata, is shared with Meta in connection with the use of the Facebook Messenger integration. Only conversations occurring directly through your Facebook Messenger account will be accessible by Meta.
# Adding LINE social messaging channels

Source: https://support.zendesk.com/hc/en-us/articles/4408844138394-Adding-LINE-social-messaging-channels

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Social Messaging add-on |

Customers without Zendesk Suite must have Support and Chat with the Social Messaging add-on to use this feature.

Location:  Admin Center > Channels > Messaging and social >
Messaging

This article describes how you can add a LINE social messaging channel. LINE is an
all-in-one communications app for free text, voice and video calls, moments, photo sharing,
and games.

This article contains the following sections:

- [Adding a LINE channel](#topic_dlt_xc5_hlb)
- [Copying the Webhook URL to your LINE account](#topic_alp_w2s_xlb)
- [Next steps](#topic_p1z_flp_bmb)

## Adding a LINE channel

To support LINE social messages in the Zendesk Agent Workspace, you can add one
or more LINE channels. You must be an administrator to add LINE channels.

To add a LINE channel, you need the following information from your LINE account:

- **Channel ID** and **Channel secret**: You can get this information from the [LINE Developer
  Center](https://developers.line.biz/). Open the account for editing, then from the **Basic settings** tab,
  copy the values from the **Channel ID** and **Channel secret** fields in LINE to the
  Zendesk **Add channel** page.
- ([Multi-brand](https://support.zendesk.com/hc/en-us/articles/4408829476378) accounts only) **Brand**: The brand to associate
  with the channel.

**To add a LINE channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Add channel** and select **LINE** from the drop-down.
3. Enter the **Channel ID** and **Channel secret**, which can be found in the LINE
   Developer Center.
4. Click **Next**.

   Once your channel details are verified, the **Webhooks**
   settings appear.
5. Copy the **Webhook URL** that appears in the Zendesk **Add channel** page and add
   it to your LINE settings in the LINE Developer Center. For details, see [Copying the Webhook URL to your LINE account](#topic_alp_w2s_xlb).
6. When you've finished copying the Webhook URL to your account in the LINE Developer
   Center, click **Connect channel**.

   When the channel connects successfully, a
   **Channel added** message appears.

## Copying the Webhook URL to your LINE account

When the Webhook URL appears on the Zendesk **Add channel** page, you need to add this
information to your LINE account in the [LINE Developer Center](https://developers.line.biz/). This allows your LINE account
to communicate with your Zendesk account.

**To update the Webhook URL**

1. In the LINE Official Account Manager, under **Response Settings > Toggle
   responses**, turn on
   **Webhooks**.
2. In the LINE Developer Center, click the edit icon for the **Use webhooks**
   setting.
3. Next to **Use webhook**, click the slider to turn it on, then click
   **Update**.
4. Click the edit icon for the **Webhook URL** setting again.
5. Paste the Webhook URL from the Zendesk **Add channel** page, then click
   **Update**.

## Next steps

After you've added your LINE channel, make sure the [Agent Workspace is optimized for your agents](https://support.zendesk.com/hc/en-us/articles/4408824058138) to use it. You can
also [configure automatic responses](https://support.zendesk.com/hc/en-us/articles/4408838007578) to messages your customers send you.
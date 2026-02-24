# Managing phone line settings

Source: https://support.zendesk.com/hc/en-us/articles/4408823877146-Managing-phone-line-settings

---

Admins andagents in custom roles with permissioncan manage phone line settings.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can
manage phone line settings.

This article contains the following topics:

- [Accessing individual line settings](#topic_arg_djv_dhb)
- [Available settings for phone lines](#topic_zhp_hjv_dhb)
- [Changing settings for multiple phone lines](#topic_gbn_qmv_dhb)
- [Deleting and recovering lines](#topic_azv_t51_2hb)

Related articles:

- [Adding phone lines](https://support.zendesk.com/hc/en-us/articles/4408824192026)
- [Managing phone lines](https://support.zendesk.com/hc/en-us/articles/4408881907994-Managing-Zendesk-Talk-numbers)

## Accessing individual line settings

The settings that you can apply to individual phone lines can be found on the lines
properties page.

**To access settings for a phone line**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab.
3. Click the line you want to view or change settings for.
4. Make any changes you want using the [Available settings for phone lines](#topic_zhp_hjv_dhb) list below for help.
5. Once you are finished, click **Save changes**.

If you have many phone lines, you can use the filter to restrict the numbers that are
shown.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_lines_settings_1.png)

## Available settings for phone lines

The following settings are available for phone lines. Settings differ depending on
your plan type and the line type.

| Setting | Description | Line type |
| --- | --- | --- |
| **Nickname** | Enter a nickname for the line that will be displayed when you receive an incoming call. The nickname is required for digital lines. | Phone, digital, SIP-IN |
| **Enable overflow and agent forwarding for this line** | Turn on to support overflow and agent forwarding. On digital or SIP-IN lines, **Overflow** becomes available only when you turn this option on, see [Managing overflow](https://support.zendesk.com/hc/en-us/articles/4408832017690). Turn off to keep the line digital-only. Digital lines that don’t include an outbound number can be used for *browser-to-browser* and *transfer-to-agent-through-browser* calls only. | Digital, SIP-IN |
| **Failover number** (Team, Professional, and Enterprise) | If Zendesk Support is unavailable, failover routes all incoming calls to a designated number so you can keep helping customers with minimal disruption. Failover isn't automated. On the Enterprise plan, if Zendesk Support is available to your end users but you can't access it, [ask Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to initiate failover. Zendesk will manually initiate failover for you once a month.  Important: Failover can be activated for a maximum of 24 hours.  The failover number you choose:  - Must not be a Zendesk phone number. - Must be able to handle your support call volume, as all incoming   calls are routed to it. - Isn't restricted based on the location of your Zendesk phone   number. - Works only for incoming calls; outgoing calls cannot use the   failover number.  Note: Failover numbers must be entered in E.164 format, see [What are the accepted phone number formats?](https://support.zendesk.com/hc/en-us/articles/4408823756570). | Phone lines only |
| **Allow outbound calls?** | Determines whether agents can place outbound calls to customers from this number. By default, this setting is on. Numbers that have this setting off won't appear in the call console as an option when agents try to make an outbound call. | Phone lines only |
| **Forwarding caller ID** | Number displayed to recipients of forwarded calls by IVR or overflow. Restrictions may block forwarded calls depending on the number you select, see [Configuring caller ID](https://support.zendesk.com/hc/en-us/articles/10183620506394). | Phone lines only |
| **Brand** (not available on Suite Team) | If you support [multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), you can add and assign phone numbers for each brand. Calls to and from those numbers will have the associated brand value on the resulting tickets. For more information, see [Setting up phone numbers for multiple brands](https://support.zendesk.com/hc/en-us/articles/4408821946138). | Phone, SIP-IN |
| **Associate outbound phone number with a SIP line** | If selected, from the drop-down, select the phone number that will be used to make outbound calls when overflow, callbacks, agent forwarding, or IVR transfers are used. | SIP-IN lines only |
| **Agent wrap-up after calls?** **Wrap-up time limit** | For each number, you can turn agent wrap-up on or off. When wrap-up is on, agents have time after each call to finish adding details to the ticket. On Professional or Enterprise, you can also limit the amount of time agents have to wrap up calls for each number from 10 seconds to 20 minutes. If you select **No limit**, agents must manually leave wrap-up mode before they are available for another call.  The wrap-up time in the call console shows the wrap up time left for the agent. If you changed the wrap-up time setting to **No limit**, it shows the amount of wrap-up time used by the agent instead. | Phone, digital, SIP-IN |
| **Call offering time limit** (Enterprise only) | Choose the amount of time that each agent gets to answer a call before it's placed back in the queue. The amount of time left to answer the call is displayed in the call console. The time limit is, by default, 30 seconds. You can click the setting to choose a duration between 15 seconds and 2 minutes.  The maximum queue wait time you configure on the Settings page takes precedence over the call offering time limit. | Phone, digital, SIP-IN |
| **Create ticket for abandoned calls?** (Professional and Enterprise) | By default, tickets aren't created for abandoned calls. However, you can choose to activate ticket creation for abandoned calls for each of your individual numbers. When this setting is on, calls that are abandoned in the queue, in voicemail, or in IVR result in a created ticket, as long as a callback number is available. In cases where the caller is identified as "unknown", no ticket is created. Note: This setting isn't available if you’re using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514). With omnichannel routing, while tickets aren't created for calls where the caller is unknown, tickets are always created for abandoned calls. If needed, you can [create a workflow](https://support.zendesk.com/hc/en-us/articles/5027246725786) to automatically close these tickets. | Phone, digital, SIP-IN |
| **Average wait time message?** (Professional and Enterprise) | When this setting is turned on, a message is played when a caller is waiting in the queue informing them of the current average wait time. | Phone, digital, SIP-IN |
| **Wait time message language**  (Professional and Enterprise) | Use the Wait time message language dropdown menu to choose the language in which the message will be played. | Phone lines only |
| **Available agents greeting (voicemail on)** **Available agents greeting (voicemail off)**  **Hold greeting**  **Wait greeting** | Configures various greetings that will be associated with this number. For more information about greetings, see [Managing outgoing greetings](https://support.zendesk.com/hc/en-us/articles/4408821594650). | Phone, digital, SIP-IN |
| **Enable for Text** | If this number is SMS capable, you can activate Zendesk Text. This allows you to provide both message and voice based support from the same phone number. See [Getting started with Text](https://support.zendesk.com/hc/en-us/articles/4408823788314). | Phone lines only |
| **Secure media (TLS/SRTP)** | Turn on to encrypt SIP signaling with TLS and audio with SRTP for this SIP-IN line. When activated, non‑encrypted calls to this line are rejected. With the standard Zendesk Twilio integration, encryption is negotiated automatically; no need for keys or certificates. | SIP-IN lines only |

## Changing settings for multiple phone lines

On the Lines page, you can change some settings for multiple lines
simultaneously.

**To change the settings for multiple lines**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab.
3. For each line you want to select, click the country flag next to the number. A
   check mark is displayed.

   ![Selecting multiple numbers](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_number_settings_1.png)
4. From the "**…**" drop-down list, choose one of the following actions:
   - **Enable outbound calls:** Allow agents to make outbound calls from
     the numbers you select.
   - **Disable outbound calls:** Stops agents from using the numbers you
     select to make outbound calls.
   - **Set as priority number:** With priority numbers you can provide
     differentiated service to your VIP customers and prioritize urgent or
     emergency calls. When you assign a number as a priority number, any
     incoming calls to that number are moved to the head of the queue to be
     answered before other incoming calls.

     Note: If you’re using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) to
     route calls, call tickets from priority phone numbers are given High
     priority instead of going to the head of the queue. Calls to
     non-priority numbers are assigned a Normal
     priority.
   - **Remove priority:** Removes any previously assigned priority from
     the selected numbers.

   ![Performing actions on multiple numbers](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_number_settings_2.png)

## Deleting and recovering lines

You can delete an existing number or digital line if you don't want to use it
anymore. You can't delete your phone number while you're on a suite trial.

**To delete a line**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Next to the number you want to delete, click the gear icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_side_settings_icon.png)), then select **Delete**.
4. On the confirmation page, click **Delete**.

Numbers are removed from your account when your trial expires, your subscription is
canceled, or your account is suspended or deleted. Within 72 hours, you can [contact our customer service team](https://support.zendesk.com/hc/en-us/articles/4408843597850) to reinstate your
number if you have resolved the issue with your account.
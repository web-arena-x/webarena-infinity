# Managing call recording options

Source: https://support.zendesk.com/hc/en-us/articles/4408831738266-Managing-call-recording-options

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

When you enable call recording, all calls are recorded by default and attached to the ticket
associated with the call. You can, however turn off recording for any number or give
callers the ability to opt-in or opt-out of call recording. Use this article to learn
how to set up call recording.

Important: You are responsible for using the recording features in Zendesk in compliance
with all applicable laws. Certain jurisdictions may require end-user and/or agent
consent prior to initiating a recording. By enabling call recording, you agree that
you have received such consent.

This article contains the following topics:

- [Understanding call recording](#topic_aqv_pdy_sjb)
- [Configuring call recording options](#topic_slb_kwv_bkb)
- [Configuring customer access to call recordings](#topic_sfy_x2y_sjb)
- [Deleting call recordings from tickets](#topic_tcq_tsz_mcb)
- [Downloading call recordings](#topic_p1l_bdv_ggb)

## Understanding call recording

Whenever a ticket is created for a phone call and the Always record calls option is
enabled for that number (a Zendesk number or an external number), the call is
recorded.

### What *is* recorded?

- Voicemails
- Calls answered by an agent via the web browser or on an agent forwarding
  number
- Calls transferred to an external phone number by an agent (unless the Stop
  call recording after transfer option is enabled)

### What *is not* recorded?

- The portion of the call while the user is on hold and waiting for an agent
  to become available
- Any consultation, usually before transferring a call to another party (warm
  transfers)
- A call which routes to an IVR phone tree branch that directs the call to an
  external phone number (Professional and Enterprise). Not applicable to
  digital or SIP-IN lines.
- When an agent pauses the call recording (Professional and Enterprise)
- The caller opts-out of the call recording (Professional and Enterprise). Not
  applicable to [digital](https://support.zendesk.com/hc/en-us/articles/4408830696090) or [SIP-IN](https://support.zendesk.com/hc/en-us/articles/8397091234586) lines.

Note: The length of the recording will sometimes be shorter than the 'Length of
phone call' shown in the call details due to the events above not being
recorded.

## Configuring call recording options

You configure call recording settings for each number individually. The available
options will depend on the line type you are configuring.

**To enable call recording and configure options**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the Settings page, click the **Lines** tab.
3. Click the line you want to configure.
4. On the number settings page, click the **Call recording** tab.
5. Configure the following options as required:
   - **Call recording and consent:** Configures call recording opt-in or
     opt-out permissions for callers. This works with both group routing and
     IVR routing.
     - **Always record calls (all):** All inbound and outbound calls
       are recorded.
     - **Caller must opt-in (inbound only):** By default, calls
       (including outbound calls) are not recorded. The caller can
       opt-in to the recording by pressing 3. If you're using a digital
       line, callers can opt-in or opt-out using a checkbox in the Web
       Widget.
     - **Caller must opt-out (inbound only):** By default, calls
       (including outbound calls) are recorded. The caller can opt-out
       of the recording by pressing 3. If you're using a digital line,
       callers can opt-in or opt-out using a checkbox in the Web
       Widget.
     - **Do not record calls (all):** No inbound or outbound calls
       are recorded.

     Regardless of these settings, if the caller chooses to leave a
     voicemail, this is always recorded and a ticket is
     created.

     For more information about call recording opt-in and
     opt-out, see [Understanding call recording
     permissions (opt-in and opt-out)](https://support.zendesk.com/hc/en-us/articles/4408838605210).
   - **Record greeting:** If call recording opt-in or opt-out is enabled,
     choose the greeting that will be played to callers. You can add a custom
     greeting from the Call recording category in the Greetings tab of the
     Settings page. Make sure the greeting informs the caller how they can
     opt-in or opt-out. Not applicable to digital lines.

     Note: This greeting is played when you use group routing. If you are
     using IVR routing, you'll need to record a separate IVR
     greeting. For details, see [Understanding call recording
     opt-in and opt-out](https://support.zendesk.com/hc/en-us/articles/4408838605210).
   - **Allow agents to control call recording:** Enable agents to pause
     and resume call recordings. (for Zendesk numbers or external numbers).
     For details, see [Pausing and resuming call
     recordings with agent recording controls](https://support.zendesk.com/hc/en-us/articles/4408820271002).
   - **Stop call recording after transfer:** When call recording is
     enabled for a number (for Zendesk numbers or external numbers), enable
     this setting if you want call recordings to stop when a call is
     transferred to an external number when using group routing.
   - **Automatic deletion:** From the drop-down list, choose the length of
     time you want to keep call recordings or choose Never to keep them
     indefinitely.
6. Click **Save changes**.

**Zendesk number recording configuration**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_recording_optoutandin.png)

**External number recording configuration**

![External number recording controls](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_recording_external.png)

**Digital line recording configuration**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_digital_recording_1.png)

## Configuring customer access to call recordings

You can allow or block customers from listening to the call recording associated with
their ticket. If you enable this setting, it will apply to calls received from all
of your Zendesk phone numbers.

**To determine whether customers can listed to call recordings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the Settings tab, enable or disable the **New live call recordings are
   public?** option.
3. Click **Save**.

## Deleting call recordings from tickets

If you no longer want a recording to appear on a ticket, you can permanently delete
it. Only admins can delete individual recordings from tickets.

Note: This feature
cannot be disabled.

**To delete a recording from a ticket**

1. In Zendesk Support, open a ticket.
2. In the conversation area of the ticket, locate the call recording, then click
   **delete recording**.

   ![Call recording attached to a ticket](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk-call-recording.png)
3. In the **Confirm** box, click **OK** to confirm you really want to delete
   the recording.

The recording is deleted and replaced by "recording not available".

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/recording_not_available.png)

## Downloading call recordings

If you want to download call recordings and access them offline, use one of the
following methods:

- In a ticket that contains a call recording, right-click the attached voicemail,
  then click **Save as**.
- Use the recording\_URL parameter in the [Zendesk API](https://developer.zendesk.com/api-reference/voice/talk-api/recordings/#json-format) to download the
  recording.
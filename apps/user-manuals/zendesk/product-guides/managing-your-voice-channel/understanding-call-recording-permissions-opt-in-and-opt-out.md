# Understanding call recording permissions (opt-in and opt-out)

Source: https://support.zendesk.com/hc/en-us/articles/4408838605210-Understanding-call-recording-permissions-opt-in-and-opt-out

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

Important: You are responsible for using the recording features in Zendesk Talk in compliance with all applicable laws. Certain jurisdictions may require End-User and/or Agent consent prior to initiating a recording. By enabling call recording, you agree that you have received such consent.

You can configure your call recording options so callers can opt-in or opt-out of call recording by pressing 3. This functionality helps you to remain legally compliant by preventing sensitive and personal end-user data from being stored in call recordings.
Additionally, it gives more flexibility and control over how you manage privacy and data security for your voice channel.

For information about how to set up call recording for phone, digital, and SIP-IN lines, see [Managing call recording options](https://support.zendesk.com/hc/en-us/articles/4408831738266).

This article contains the following topics:

- [Understanding call recording permissions (opt-in or opt-out)](#topic_rpx_yjm_fkb)
- [Using call recording permissions (opt-in or opt-out) with group routing](#topic_rbh_1km_fkb)
- [Using call recording permissions (opt-in or opt-out) with an IVR](#topic_csm_fkm_fkb)
- [Reporting for call recording permissions (opt-in and opt-out)](#topic_p3h_qpm_fkb)

## Understanding call recording permissions (opt-in or opt-out)

You can configure opt-in or opt-out for each of your Zendesk phone numbers.
If you are using a digital or SIP-IN line, some of these settings won't apply.

The settings you can configure are:

- **Always record calls (all):** All inbound and outbound calls are recorded.
- **Caller must opt-in (inbound only):** By default, calls (including outbound calls) are not recorded. The caller can opt-in to the recording by pressing 3.
 Not applicable to [digital lines](https://support.zendesk.com/hc/en-us/articles/4408830696090).
- **Caller must opt-out (inbound only):** By default, calls (including outbound calls) are recorded. The caller can opt-out of the recording by pressing 3.
 Not applicable to [digital lines](https://support.zendesk.com/hc/en-us/articles/4408830696090).
- **Do not record calls (all):** No inbound or outbound calls are recorded.

Regardless of these settings, if the caller chooses to leave a voicemail, this is always recorded and a ticket is created.

To configure call recording options, see [Managing call recording options](https://support.zendesk.com/hc/en-us/articles/4408831738266).

## Using call recording permissions (opt-in or opt-out) with group routing

If you're using group routing and call recording opt-in or opt-out is enabled for a number, the caller hears a default call recording opt-in or opt-out greeting after the Available agents greeting has played. This greeting informs callers that they can press 3 to opt-in or opt-out of call recording.

You can record your own greeting. See [Managing outgoing greetings](https://support.zendesk.com/hc/en-us/articles/4408821594650).

When using a digital line, callers opt-in or opt-out by using a check box in the Web Widget.

## Using call recording permissions (opt-in or opt-out) with an IVR

If you've set up an IVR with the option to direct the call to a group, the default call recording opt-in or opt-out greeting won't be played. However, once a caller is in the queue, that caller can still press 3 to opt-in or opt-out of call recording. Below is an example of how to do this.

**To configure call recording permissions in an IVR**

1. Record a new greeting (or update an existing greeting) in the **IVR** category. Make sure the greeting indicates that the caller can opt-in or opt-out of call recording by pressing 3 (depending on the call recording options you chose). For help recording greetings, see [Managing outgoing greetings](https://support.zendesk.com/hc/en-us/articles/4408821594650).
2. In the IVR route where the action selected is to route to a group, choose your new or updated greeting from the **Greeting** drop-down list.
3. Configure any other IVR options you need, then click **Save**. See the screenshot below for an example.

   ![IVR recording greeting](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_IVR_recording.png)

In the example above, when the caller presses 1 to be routed to the **Support** group, they'll hear the custom greeting you made and be able to press 3 to opt-in or opt-out of the call recording.

## Reporting for call recording permissions (opt-in and opt-out)

You can get details about call recording opt-in and opt-out activity using one of the following methods:

- **From a ticket:** In a ticket generated by a phone call, the Call details section shows whether a caller opted in or out of the call recording.
- **Using Zendesk APIs:** Caller opt-in or opt-out key presses are passed to the incremental API. You can report on caller opt-in or opt-out key presses using the [Incremental Calls Export API](https://developer.zendesk.com/rest_api/docs/voice-api/incremental_export#incremental-calls-export)
 including:
 - Total count of how many times each agent interacts with the recording control button
 - Total time each call was recorded
 - Total time each call was not recorded
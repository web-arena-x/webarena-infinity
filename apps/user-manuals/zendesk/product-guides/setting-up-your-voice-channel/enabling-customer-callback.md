# Enabling customer callback

Source: https://support.zendesk.com/hc/en-us/articles/4408884087706-Enabling-customer-callback

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

Callback enables your customers to choose between waiting on hold in a queue or requesting a
callback. When customers select callback, their places are held in the queue and their call is
automatically returned when an agent is available to talk with them.

For the customer callback feature to work, at least one agent must be logged in and they must
have a status of either Online or Away.

[SIP-IN lines](https://support.zendesk.com/hc/en-us/articles/8397091234586) are compatible with callback.

- If the caller doesn't enter a phone number, the caller number for callbacks is extracted
  from the username contained in the "from" SIP URI.
- Callbacks on SIP lines are dialed from the associated outbound number configured in the
  SIP line settings. If you don't associate a number, callback will be unavailable.

Important: You can't configure callback for [digital lines](https://support.zendesk.com/hc/en-us/articles/4408830696090). Toll-free numbers are supported though some
carriers do not support outbound calling from a toll-free line. Check with your carrier
before you configure callback on a toll-free number.

This article contains the following sections:

- [Understanding the end-user experience](#topic_fy2_tcy_fz)
- [Understanding the agent experience](#topic_rrp_bdy_fz)
- [Reporting on callback activity](#topic_cmt_b24_jz)
- [Enabling callback](#topic_s3m_qcy_fz)

## Understanding the end-user experience

When this feature is enabled on a number, your customers will hear a **Callback**
greeting after the **Available agents** greeting has played. This greeting informs them
that they can press 2 to request a callback. After that, they have the following options:

- Press 1 to request a callback on the number they've called in from
- Press 2 to request a callback to a different number. The alternative number must be in
  E.164 format, i.e. [+ or 00][country code][subscriber number including area code]. If
  it's not in the correct format, the customer will be prompted to enter again.
- Press 3 to return to the queue on hold

Tip: If you've set up an IVR, the callback greeting won't be played.
However, once they are in a queue, customers can still press 2 to request a callback.
Consider adjusting your IVR greeting to advise callers about how to use the callback
functionality.

If the customer requests a callback, they'll also hear a second **Callback
confirmation** greeting confirming their choice. The call will then end while keeping
the customer in the queue.

You can select a language for the callback confirmation greetings when setting up callback
(see [Enabling callback](#topic_s3m_qcy_fz)).

## Understanding the agent experience

Agents click **Call** to call the customer back or **Decline** from the call console
to send the call back to the queue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/callback_console.png)

The callback request is sent to all agents for one hour. If an agent accepts the call or
all agents decline the call, the callback request is cancelled and a ticket with the subject
Callback is created for the agent to action later. If, after 60 minutes, no agents are
available the callback request is cancelled and a ticket is created.

If an agent is in the 'offline' or 'transfers only' state, they are treated as if they
declined the request.

If an agent is in the 'away' state, or is busy on a call, they will receive the request
once they are available. If they are not available after 60 minutes, the callback request is
cancelled and a ticket is created.

A ticket is also created when the agent initiates the callback. If the customer doesn't
pick up, another attempt is made to call them back. An internal comment is automatically
added to the ticket indicating that the callback request was attempted

Note: If omnichannel routing (OCR) isn't enabled, additional callback requests for the same number
are ignored, preventing queue overloading. With OCR enabled, each new callback generates a
ticket stating, "Queue callback request: Ignored, customer already in queue", which can be
automatically closed using triggers.

## Reporting on callback activity

Use the Talk dashboard to analyze your account's callback from queue activity using the
metrics Callbacks in queue, Total callback calls, and Average callback wait time. For more
details, see [Analyzing call activity with the Talk dashboard](https://support.zendesk.com/hc/en-us/articles/4408831823514) and
[Zendesk Talk dashboard metrics reference](https://support.zendesk.com/hc/en-us/articles/4408883025690).

## Enabling callback

Callback is configured for each individual phone number. You can't configure callback for
[digital lines](https://support.zendesk.com/hc/en-us/articles/4408830696090).

Note: You cannot configure callback as a menu option in an IVR. However, if a customer is
waiting to be routed to an agent in the queue, they can request a callback by pressing 2.
Make sure that your IVR greeting informs customers about this capability. For help, see
[Route incoming calls with IVR](https://support.zendesk.com/hc/en-us/articles/4408885628698).

**To enable callback from queue**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Click the number you want to edit.
4. Select the **Callback** tab.
5. Toggle the **Callback** field to enabled.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/callback_enable.png)
6. In the **Language** field, select a language for your callback phone number
   confirmation greeting. This setting affects only the message that plays after customers
   have pressed 2 to request a callback. It doesn't affect the language of the **Callback
   greeting** or **Callback confirmation greeting**.

   Note: If you do not select a
   language, your Zendesk default language is used. If your default language is set to a
   language not included for voice, the greeting will be played in English.
7. In the **Callback greeting** field, select a greeting from the dropdown list. This is
   the greeting that plays informing callers that they can press 2 to request a
   callback.
8. In the **Callback confirmation greeting** field, select a greeting from the dropdown
   list. This is the greeting that plays after callers press 1 to confirm they've selected
   callback.
9. Click **Save changes**.
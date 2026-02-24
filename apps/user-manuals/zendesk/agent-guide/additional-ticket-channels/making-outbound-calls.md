# Making outbound calls

Source: https://support.zendesk.com/hc/en-us/articles/4408836235162-Making-outbound-calls

---

You can make outbound calls from either your browser or your phone, using lines that belong to brands you’re authorized to access. Keep in mind that while you can initiate outbound calls using your own phone, the call will be passed to and made from the call console. You can make outbound calls regardless of whether yourstateis online, offline, away, or transfers only. You must be aTalk agent or team leadto make outbound calls.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

You can make outbound calls from either your browser or your phone, using lines that
belong to brands you’re authorized to access. Keep in mind that while you can initiate
outbound calls using your own phone, the call will be passed to and made from the call
console. You can make outbound calls regardless of whether your [state](https://support.zendesk.com/hc/en-us/articles/4408829114138) is online, offline, away, or transfers only. You must
be a [Talk agent or team lead](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_a54_zlt_qmb) to make outbound
calls.

This article contains the following topics:

- [Considerations for making outbound calls](#topic_xqj_dnh_g3c)
- [Making an outbound call from the call console](#topic_e52_ypm_ltb)
- [Making an outbound call from an existing ticket](#topic_yt4_ypm_ltb)
- [Making an outbound call from a user's profile](#topic_ozw_ypm_ltb)

## Considerations for making outbound calls

Making an outbound call from Talk, forwarding it to another Talk number, and then
sending the caller to voicemail while they wait in a queue isn't supported. Your
admin can [disable voicemail](https://support.zendesk.com/hc/en-us/articles/4408831899930) on numbers used for
outbound calls to prevent end users from leaving voicemails, particularly if you
don't monitor those numbers.

## Making an outbound call from the call console

When you make a call from the call console, the call details are added to a
new ticket. If you use multiple lines, you can filter outbound calls to quickly find
the specific outbound line you want to call from.

**To make an outbound call from the call console**

1. [In Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the Call icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_icon.png)) in the topbar.
2. In the call console, click the dial pad icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_dial_pad_icon.png)) to enter the phone number you want to
   call.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outgoing-calls-2.png)

   The default number that will be used is displayed in the outbound
   call number dropdown (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outbound_call_number_dropdown.png)). The default number is usually the
   last one you used. If your browser cache has been cleared, the outgoing line
   resets to the default number for the default brand.

   Tip: A brand is a customer-facing identity, represented by a
   collection of contact points for your customers. These can include
   email, help center, messaging Web Widget, and social media. See [Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306).
3. Choose a phone line from brands you have access to.

   If you don’t see
   a line you expect, contact your administrator to confirm your brand access
   and the line’s brand assignment.

   You can use the default number
   displayed in the outbound call number dropdown or select another number from
   the dropdown.

   If you call from multiple lines, you can filter the
   options by starting to type in the dropdown and then selecting the line you
   want from the filtered list. You can filter by name, number, or brand.

   Finally, you can enter a phone number on the keypad or in the phone
   number field.
4. When you're ready, click **Call**.

   If you're using your own
   phone, Zendesk will call your number and then dial the requester after you
   pick up.

Tip: Although speed dial numbers aren't supported,
it’s possible to enter the name of the person you wish to call into the dial
pad, rather than type the number manually, if they are a user in your account.
If many numbers or users are displayed, they might obscure the Call button. In
this case, choose one of the numbers or users or narrow your search for
names.

## Making an outbound call from an existing ticket

When you make a call from a ticket, the call details are added to that
ticket. You can initiate an outbound call from any ticket that isn’t closed, even if
it was not created by an incoming call.

**To make an outbound call from an existing ticket**

1. Open the ticket you want to use to call the requester.
2. In the channel switcher menu of the message composer, click **Call
   <number>** or **Call Enter a number**. Select the displayed
   number or select **Enter a number** to manually enter a new number to
   dial.

   The call console opens. You can then edit the outgoing number or
   search for and change the outbound phone line. The country code of the
   number will automatically change to match the number you are calling. When
   you are ready, click **Call** to initiate the phone call.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outgoing-calls-1.png)

Tip: Brands play an important role in which phone line is used for an
outbound call. When making a call from a ticket, a line of the same brand
associated with the ticket is used (if available).

### More information about making outbound calls from a number in a ticket

The following list gives you more information about behavior when you make an
outbound call from a phone number in a ticket:

- Zendesk always uses a line associated with the ticket brand,
  usually the one called by the caller. If the line called by the caller is
  not available or enabled for outbound calls (for example if it has been
  deleted or disabled) or it no longer belongs to the ticket brand, Zendesk
  uses the next available line of the same brand (the first line of the same
  brand in the lines list).

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outgoing-calls-3.png)

  If the brand has no available or enabled lines for outbound
  calls, Zendesk uses the first available line of any brand you have
  access to (the uppermost line in the lines pick-list).

  If you
  disable a line, it will still be shown as available in the call console
  until you refresh your browser window.
- If the brand of the ticket has been updated and it's now different
  from the one called by the user, Zendesk uses the first available line of
  the new brand for the call.

### More information about making a call from a ticket by entering a number

When you choose **Enter a number** from a ticket, the call console
opens where you can configure details about the call. For more information, see
[Making an outbound call from
the call console](#topic_e52_ypm_ltb).

## Making an outbound call from a user's profile

When you make a call from a user's profile, the call details are added to a
new ticket.

**To make an outbound call from a user's profile**

1. Open a user's profile.
2. Click their number in the **Phone** field.
3. In the list, select **Call this number**.

The call console opens and calls the selected number. The default number used is the
last one used by the agent.
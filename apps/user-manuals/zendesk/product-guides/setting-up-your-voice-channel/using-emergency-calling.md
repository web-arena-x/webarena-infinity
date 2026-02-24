# Using emergency calling

Source: https://support.zendesk.com/hc/en-us/articles/4411085317018-Using-emergency-calling

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Location:  Admin Center > Channels > Talk and email > Talk

In certain countries, you can make emergency calls from Zendesk.

This article includes these sections:

- [About emergency calling](#topic_usx_rc5_vrb)
- [Associating an emergency address with a Zendesk phone number (US and Canada numbers only)](#topic_u2w_yzv_hsb)
- [Testing emergency calling (US and Canada numbers only)](#topic_aq2_sd5_vrb)
- [Making an emergency call](#topic_v4l_5d5_vrb)
- [Sending an emergency text](#topic_dj4_vj1_f5b)
- [Contacting the US National Suicide Prevention Lifeline (988)](#topic_wbg_vj1_f5b)

## About emergency calling

Emergency calling is available in some countries (United States, Canada,
the UK, Australia, Ireland, France, Germany, and Austria), enabling outbound calls
to be made to emergency services (for example, 911, 999, and 112). In the event of
an emergency, agents can quickly get in contact with emergency services using the
call console.

In the event that an emergency address is not registered to a US or Canada based
number, 911 calls are routed to a national emergency call center. A trained agent at
the emergency call center asks for the caller’s name, phone number, and location.
Then, they transfer the caller to the appropriate local Public Safety Answering
Point (PSAP) or otherwise determine the best way to provide emergency services. If
you make a 911 call from a US or Canada phone number that does not have an
associated emergency address, Zendesk reserves the right to pass the associated fee
onto you.

In all cases, you should use traditional telephony for making emergency
calls, if possible. Emergency calling in Zendesk is Internet-based and is different
and limited compared to traditional land line or cellular services. For example, it
may be unavailable due to loss of power, Internet connectivity, technical
infeasibility, suspension of services due to billing issues, Zendesk outage, or an
outage within your network, or the network of our underlying provider or their
carriers.

Note: You can only dial emergency services if outbound calling is enabled for your phone
numbers. Emergency calling in Zendesk does not include access to non-emergency help
lines, such as Harmonised Services of Social Value in the EU. It is only technically
feasible for Zendesk to enable emergency calling in countries where Twilio,
Zendesk’s voice services provider, supports it. Therefore, emergency calling is
available only in the supported countries.

## Associating an emergency address with a Zendesk phone number (US and Canada numbers only)

In the US and Canada, Zendesk supports [Enhanced 911](https://www.fcc.gov/general/enhanced-9-1-1-wireless-services) (E911). With E911, an
emergency address can be associated with any US or Canada based phone number. Calls
made from numbers with an associated emergency address are routed directly to the
local Public Safety Answering Point (PSAP) serving the address. The call
automatically includes the caller’s phone number and corresponding address
information for the 911 dispatcher answering the call.

Associating an emergency address with a phone number incurs a monthly fee per phone
number. This monthly fee is charged by the state and/or local government to fund
their emergency response systems and is passed on to you by Zendesk as part of your
usage charges.

**To associate an emergency address to a US or Canada phone number in
Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab, then find the phone line you want to edit
   and open it.

   You can only add an emergency address to a U.S. or Canada phone
   number. Only one emergency address can be associated with a phone number at
   a given time.
3. On the **Settings** tab (of the phone line), scroll down to the
   **Emergency Address** section, and then click the **Add address**
   button.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_emergency_add_address.png)
4. Enter the physical address you want to associate with the phone line
   or, if you have previously entered the address, then select it from the dropdown
   list.

   This address may be used to dispatch police, fire, emergency medical
   and other emergency response resources. The address you enter is passed
   through an emergency address validation system and you may receive a
   suggested address, if a better match is found in the database.

   Note: In
   the US and Canada, the address must be recognized by the Master Street
   Address Guide (MSAG) database. The MSAG address often differs from the
   equivalent US Postal Service address because the MSAG uses the community
   name (township, city, county) from where the closest responding PSAP will
   come.
5. If prompted, confirm that you want to proceed with the suggested
   address.
6. Make sure you click **Save changes** before you leave the page.

   The address moves into the Pending registration state.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_emergency_pending_reg.png)

   Once registration of the emergency address to the phone number is
   complete, the status associated with the emergency address changes to
   Registered. It can take up to five minutes for the status of the emergency
   address to change.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_emergency_registered_address.png)

Note: To remove an emergency address from a phone number,
[contact Zendesk Customer
Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

## Testing emergency calling (US and Canada numbers only)

If you want to check that your account has been properly configured for emergency
calling, you can make a test call by dialing 933. You'll be connected to an
automated system that reads back the phone number that you’re calling from, along
with the address associated with that number.

This must be done sparingly. Some localities require you to schedule emergency test
calls in advance and will charge penalties otherwise. You should check with your
local authorities before placing any unscheduled emergency call tests.

**To place a live emergency test call to 911**

You can place a test call to verify the information that the emergency
responder receives. Call 911 then use the following script.

- "Hello, this is not an emergency call. This is a test. Do you have a
  moment to verify my emergency information or can we schedule a later time to do
  so?"
- "Can you verify the address that you received for my call?" Confirm
  that this matches your intended emergency address.
- "Can you verify the telephone number you received for my call?"
  Confirm that this matches the phone number that you called from.
- "Thank you for your time."

If for any reason the address read back to you is incorrect, [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

## Making an emergency call

Making an emergency call is similar to making any other [outbound call in the call console](../../agent-guide/additional-ticket-channels/making-outbound-calls.md#topic_orv_t31_5hb). The
only important difference is that you do not need to enter the country code (for
example, +1).

**To initiate a US emergency call**

- In the call console, dial **911**, then click **Call**.

You can only dial emergency services in the country associated with your selected
outbound number. For example, if you want to call US emergency services, the
outbound number selected in the call console must be a US based phone number. If,
for example, you had a French based phone number selected as the outbound number, a
call to US emergency services (911) would not connect.

## Sending an emergency text

Agents can send proactive text messages to emergency phone numbers where available.
For help creating proactive text messages, see [Using Text notifications with triggers: Recipes
and tips](https://support.zendesk.com/hc/en-us/articles/4408882005402-Using-Text-notifications-with-triggers-Recipes-and-tips#topic_arl_s33_xhb).

In addition to the steps in the article, you'll need to create an end user with a
short code emergency number (for example 911, 999, or 988). You'll then specify that
user as the requester when you sent a proactive message from a ticket.

Additionally, ensure that the setting **Validate users phone numbers** is
unchecked (in Admin Center under **People** > **Configuration** > **End
users**). If this setting is enabled, the users phone number must be in [E.164 format](https://support.zendesk.com/hc/en-us/articles/4408823756570) meaning that short code numbers such as 911
will not validate and cannot be used.

## Contacting the US National Suicide Prevention Lifeline (988)

In the event of a mental or emotional health emergency, agents can contact the US
National Suicide Prevention Lifeline (988) using the call console. The 988 Suicide
& Crisis Lifeline is a national network of local crisis centers that provides
free and confidential emotional support to people in suicidal crisis or emotional
distress 24 hours a day, seven days a week in the United States. [Find more
information about the 988 Suicide & Crisis Lifeline](https://988lifeline.org/).

The same [restrictions and
recommendations](#topic_usx_rc5_vrb) that apply to calling US emergency services (911) also
apply to calling 988.
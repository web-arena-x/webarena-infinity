# Using emergency calling in Zendesk Sell Voice

Source: https://support.zendesk.com/hc/en-us/articles/4413085281306-Using-emergency-calling-in-Zendesk-Sell-Voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

If you need to, you can use Sell Voice in an emergency to alert nearby emergency response services.

Note: Use the unique phone number assigned to you, as you cannot share the same number with another agent.

This article covers the following topics:

- [About emergency calling in Canada and the US](#topic_hgt_hrh_xrb)
- [Adding an emergency address](#topic_ksf_dyg_xrb)
- [Testing emergency calling (Canadian and US numbers only)](#topic_a44_dyg_xrb)
- [Making an emergency call](#topic_kgy_dyg_xrb)
- [Billing for emergency calling](#topic_apg_2yg_xrb)
- [Removing or changing an emergency address](#topic_z3d_q2h_xrb)

## About emergency calling in Canada and the US

In Canada and the US, Zendesk Sell Voice supports Enhanced 911 (E911). Using E911, you can associate an emergency address with any Canadian or US based phone number. Calls made from numbers with an associated emergency address are routed directly to the local Public Safety Answering Point (PSAP) serving the address. The call automatically includes the caller’s phone number and corresponding address information for the 911 dispatcher answering the call. Associating an emergency address with a phone number incurs a cost of USD $0.75 per phone number per month. This monthly fee is charged by the state/local government to fund their emergency response systems and is passed on by Zendesk as part of your Voice usage charges.

If an emergency address is not registered to a Canadian or US based number, 911 calls are then routed to a national emergency call center. A trained agent at the emergency call center will ask for the caller’s name, phone number, and location. They'll then transfer the caller to the appropriate local PSAP, or determine the best way to provide the emergency service.

Note: If you make a 911 call from a Canadian or US phone number that does not have an associated emergency address, Zendesk reserves the right to pass on a USD $75 fee.

## Adding an emergency address

The address you provide may be used by emergency services when dispatching police, fire, medical, and other emergency response resources. It can take up to five minutes for your emergency address to be registered for use.

**To assign an emergency address to a phone number in Sell Voice**

1. On the Sell sidebar, click **Settings > Communication channels > Voice and text**.
2. In **Emergency address**, click **Assign address**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_voice_emergency_address.png)
3. In the **Add a new emergency address** dialog, enter your company name and the physical address that you want to associate with the phone number. If you've previously entered an emergency address, then you can select it from the drop down menu.

   Note: At this stage admins can also set the default emergency address for the entire account so it will be the suggested address for all non-admin users.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_voice_emergency_calling.png)

   The information you enter for the address is checked against an emergency address validation system, so you may receive a suggested address if a better match is found in their database.

   In Canada and the US, the address must be recognized by the Master Street Address Guide (MSAG) database. The MSAG address often differs from the equivalent US Postal Service address because the MSAG database uses the community name (township, city, county) from where the closest responding PSAP will be deployed.
4. Click **Save** to confirm that you want to proceed with the suggested address.

## Testing emergency calling (Canadian and US numbers only)

If you want to check that your Zendesk Sell Voice account is properly configured for emergency calling, dial **933** to make a test call. An automated system will read back the phone number that you’re calling from, along with the address associated with that number.

You can also dial a live emergency test call to verify the information that the emergency responder receives.

Note: Do this sparingly. Check with your local authorities before placing any unscheduled emergency test calls. Some localities require that you schedule emergency test calls in advance and will charge penalties if you do not. Zendesk is not liable for any unscheduled emergency test calls made by users of your Zendesk account.

**To make a live emergency test call**

When you contact the emergency responder, use the following script to confirm that the address and phone number in their response matches the intended emergency address and phone number that you called from:

*Hello, this is not an emergency call. This is a test. Do you have a moment to verify my emergency information or could we schedule a time to do so later?*

*Can you verify the address that you received for my call?*

*Can you verify the telephone number you received for my call?*

*Thank you for your time.*

If for any reason there is an address mismatch, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

## Making an emergency call

Making an emergency call in Zendesk Sell Voice is similar to any other outbound call. The only important difference is that you do not need to enter the country code. For example, to make an emergency call in the US, just enter **911** and press **Call**, (you do not need to add +1 before the number).

## Billing for emergency calling

Billing differs depending on your location and the phone numbers you use to call emergency services. The charges for using the emergency calling feature in Zendesk Sell Voice are as follows:

**Charges for Canada and the US**

Associating an emergency address with a phone number (Canada and US only) costs USD $0.75 per phone number, per month. This monthly fee is charged by the state/local government to fund their emergency response systems, and is passed on to you by Zendesk as part of your Sell Voice usage charges.

Note: If you make a 911 call from a Canadian or US phone number that does not have an associated emergency address, Zendesk reserves the right to pass on a USD $75 fee.

Calls to 911 are charged at normal rates.

**Charges for all other locations**

Calls to emergency numbers outside of North America, such as 000 or 999 and 112, for example, are charged at normal rates.

## Removing or changing an emergency address

You can change or completely remove your emergency address. However, it can take up to five minutes for the emergency address to be removed.

**To remove an emergency address associated with a phone number in Zendesk Sell Voice**

1. On the Sell sidebar, click **Settings > Communication channels > Voice and text**.
2. In **Emergency address**, click the **Remove address** link.

   After you've removed the emergency address, the address is no longer visible.
3. If you want to enter a new emergency address, click **Assign address** and follow the steps in the section [Adding an emergency address](#topic_ksf_dyg_xrb).
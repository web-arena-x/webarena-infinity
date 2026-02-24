# Porting a number to Sell Voice

Source: https://support.zendesk.com/hc/en-us/articles/4408828587930-Porting-a-number-to-Sell-Voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can port an existing number that you are using to Sell Voice, however we do not
currently support the following:

- Voicemail or call waiting in Sell Voice.
- Hosted numbers (porting the SMS portion of the number only, or voice portion of
  an SMS and voice enabled number).

Note: In Zendesk Sell Voice you can only assign one phone number per user and it is
then permanent to that user, additionally agents cannot share the same number. If
you require a number transfer between agents please contact our support
team.

This article contains the following topics:

- [Before initiating a port request](#topic_vtb_yd4_3qb)
- [When you are ready to port your number](#topic_ovp_yd4_3qb)
- [After you submit](#topic_lkz_yd4_3qb)
- [Porting a number from Sell Voice](#topic_ss4_zd4_3qb)

## Before initiating a port request

There are a number of things to note before you start a port request:

- We can port most US and Canada phone numbers. Outside of those
  countries, porting is handled on a case-by-case basis and is not guaranteed -
  but our team is happy to work with our partner to attempt porting any number
  that Sell Voice currently supports.
- Ports for US and Canada numbers can take between 1-4 weeks. Other
  numbers can take six or more weeks, when you first request porting our Support
  team can check with our provider what the estimated time is, and guide you if
  any additional information is necessary. Please bear in mind that once the
  porting process starts, your number may be unusable until the porting concludes
  and the numbers are configured to use with Sell
- When a porting date is set by our provider Twilio, changing it can be
  difficult and cause potential issues - do not initiate ports until you are ready
  to do so.
- Notify your current carrier that they must not disconnect the number
  until you’ve confirmed it is ok to do so.
- You need to [register for A2P](registering-your-sell-number-to-use-a2p-10dlc-for-text-messaging.md) if you are
  going to use outbound texting with the Sell Voice number you plan to port over a
  US number. This is because US carriers require A2P registration for outbound
  texts to US end users. This process may take up to 6 weeks so it is best to
  apply in advance. Please bear in mind that Sell Voice is not the same product as
  Zendesk Talk and it requires separate registration.

Note: When numbers are being ported to Sell they may be unusable for a period of
time (usually 48-72 hrs), until their status is confirmed and they are correctly
configured and assigned in Sell.

If a user of a ported number has been
deactivated for 3 months or more at a later time after the port, Zendesk cannot
guarantee reassigning the same number to the user if their account is
reactivated. Numbers are automatically released after 3 months from the
deactivation date.

## When you are ready to port your number

When you are ready, send an email to Zendesk Customer Support (see [Contacting Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850)) with the following
information:

- The phone number(s) that you would like to port.
- The carrier(s) for the numbers.
- Does the carrier use Twilio?
- The country for the phone number.
- Your most recent billing statement for the number.
- Your planned go-live date for Sell Voice.
  - We recommend not initiating the port until after your go-live date to
    prevent porting early but we can, at your request, initiate it before
    that. We cannot guarantee any specific porting dates.
- Whether the port should happen only after a specific date.
  - We cannot choose a day and time for the port to happen, but can often
    have a “Do not port until X date set”.
- If you are porting a US-based number, include a [Twilio Letter of Authorization form](https://zendesk.box.com/s/e6a9afdc43d19e3d700b).
  - If you are porting from a different country, our team will contact you
    for any additional forms we may need.
- Your Twilio SID from the current carrier, if you are moving a number from
  another Twilio-based carrier.
- If the number to be ported is a cellphone number, include your account details
  and PIN number in the porting request.
- If you are in [an area where A2P registration is
  required](using-calls-and-text-in-sell-voice.md#:~:text=Registering%20for%20A2P%2010DLC) and you're going to use the requested number for outbound
  text messaging, ensure you submit the necessary information and notify Zendesk
  that you intend to use the number for outbound text messaging.
  - If you already have an approved campaign, you must notify us of your
    plan to use the number for outbound text messaging so we can add the
    number to your registration.

## After you submit

We'll keep you up to date throughout the porting process. We may contact you to
obtain additional documentation or information if specific countries have different
requirements. If you have any questions, let us know.

## Porting a number from Sell Voice

If you want to move your Sell Voice number to another carrier, email Zendesk Customer
Support (see [Contacting Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850)) with the number you
want to move. Porting a number to another carrier can take around 3-4 weeks or more
depending on the country and technical capabilities.
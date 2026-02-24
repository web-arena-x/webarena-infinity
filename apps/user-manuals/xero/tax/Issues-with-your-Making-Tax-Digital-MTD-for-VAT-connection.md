# Troubleshoot MTD VAT issues

Source: https://central.xero.com/s/article/Issues-with-your-Making-Tax-Digital-MTD-for-VAT-connection

---

## Overview

- Resolve issues when you set up Making Tax Digital (MTD) for VAT and filing returns.

###

Can't access outstanding VAT returns from HMRC

If you receive the error **We could not access outstanding VAT returns from HMRC**, you might be using the incorrect Government Gateway ID and password.

If you're a small business, check:

- You're using your MTD Government Gateway ID. Check the ID by signing in to your [HMRC business tax account](https://www.gov.uk/guidance/sign-in-to-your-hmrc-business-tax-account) (HMRC website). Contact HMRC if you need help with your credentials.
- The VAT number in your organisation's [financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK) matches the VAT number in your HMRC business tax account.

If you're an agent trying to connect for a client, check:

- Your client is linked to your Agent Services Account (ASA), and has authorised you to file VAT returns on their behalf. Contact HMRC if you need to check this.
- You’re using the ID and password for your ASA to authorise Xero to connect to HMRC. HMRC advise that agents should link their clients to their ASA, and only use these credentials to approve the connection.
- The VAT number in the organisation's [financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK) matches the VAT number in the client’s HMRC business tax account.

Warning

If you use different credentials to your ASA, the HMRC connection will stop for your ASA linked clients. If you reconnect a client to HMRC using your ASA, all clients linked to that ASA will reconnect.

If none of the above resolves the issue, reset the connection to HMRC:

1. [Remove Xero’s connection permission](https://www.gov.uk/permission-software-tax-information) (HMRC website).
2. [Clear your browser’s cookies and cache](/s/article/Clear-Cookies-and-Cache) and use incognito or private browsing mode to log in to Xero.
3. Use your MTD-enabled Government Gateway ID to [set up MTD for VAT in Xero](Switch-to-our-new-VAT-return-for-MTD.md) again.

###

VAT period doesn’t appear or display correctly in Xero

Once you have connected Xero with HMRC for MTD, Xero pulls the return periods from your HMRC business tax account. These periods are provided by HMRC and displayed in the **Needs Attention** section of your VAT dashboard in Xero.

In some instances, the VAT return periods:

- Don’t appear in the **Needs Attention** section as expected
- Don’t display correctly, for example, they have overlapping dates
- Still show in the **Needs Attention** section after you’ve filed the return

If you have issues with your VAT return periods, check your HMRC business tax account for the VAT periods HMRC are expecting.

If the VAT return periods in your HMRC business tax account match with what is showing in Xero, but these aren’t the periods you’re expecting to see, you need to contact HMRC and ask to speak to an MTD VAT specialist.

If the VAT periods in your HMRC business tax account don’t match what is showing in Xero, check the VAT number in your [financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK) in Xero matches your HMRC business tax account.

If the VAT number in Xero matches your HMRC business tax account and the VAT periods don’t match, please contact Xero support.

###

You need to reauthorise with HMRC

Every 18 months the connection between Xero and HMRC expires. You need to reconnect using your MTD credentials.

Click **Connect to HMRC** to set up your connection to HMRC.

Partners asked to re-connect their organisation to HMRC for MTD VAT

If you’re asked to re-connect your organisation to HMRC for MTD VAT, it could be that the token that allows you to make the connection has expired.

The most common reason for this is that staff members within your practice are using both the practice Agent Services Account (ASA) credentials and client Government Gateway IDs.

If a client's Government Gateway ID is used instead of your practice ASA, this breaks the connection token for your entire practice and all your clients. If this happens, you need to reconnect using the practice ASA; this will re-establish the connection for all your clients. HMRC advises that agents should link all their clients to their ASA and only use these credentials to authorise the software connection.

If reconnecting using your practice ASA doesn't fix the connection, there are other reasons that can cause this issue:

- [The VAT number in the Xero organisation](https://central.xero.com/s/article/Set-up-your-organisation-s-financial-details-UK) is now different to that showing in the customer's Business Tax Account or your practice's ASA.
- Your client is no longer linked to your ASA. You’ll need to [contact HMRC to confirm this](https://www.gov.uk/government/organisations/hm-revenue-customs/contact/vat-enquiries), and if necessary, ask your client to reauthorise you to act on their behalf. They can do this through their Business Tax Account.
- If you’re unable to add a client to your ASA, you’ll need to invite a new user into the client's Xero organisation with an email address that isn't already used by a staff member in your Xero practice. You can then use these login details to authorise Xero to connect to HMRC with the client's Government Gateway ID. This login can be invited into multiple client's Xero organisations but won't be able to be a staff member in your Xero practice.
- There is either a browser issue where stored cookies and cache are causing the connection to be lost, or an error with HMRC’s MTD portal that has caused the connection to be lost. [Please clear the cookies and cache](https://central.xero.com/s/article/Clear-Cookies-and-Cache) on your browser and reconnect using your practice’s ASA.

Business users asked to re-connect their organisation to HMRC for MTD VAT

If you’re asked to re-connect your organisation to HMRC for MTD VAT, it could be that the token that allows you to make the connection has expired.

This could be due to a number of reasons:

- There is a browser issue where stored cookies and cache are causing the connection to be lost. [Please clear the cookies and cache](https://central.xero.com/s/article/Clear-Cookies-and-Cache) on your browser and reconnect using your Government Gateway ID and password.
- [The VAT number in your Xero organisation](https://central.xero.com/s/article/Set-up-your-organisation-s-financial-details-UK) is now different to that showing in your Business Tax Account.
- There is an error with HMRC’s MTD portal that has caused the connection to be lost. Please clear the cookies and cache on your browser and re-connect using your MTD enabled Government Gateway ID and password. It will be the same details your business used to sign up to MTD with HMRC.

​​​You can confirm you’re using your MTD enabled Government Gateway ID and password by logging into your HMRC Business Tax Account, or by [contacting HMRC directly](https://www.gov.uk/government/organisations/hm-revenue-customs/contact/vat-enquiries).

VAT returns “Sorry, you don’t have permission to view this page”

If you’re a multi-practice user and get the “Sorry, you don’t have permission to view this page” error when trying to access VAT in a client organisation, check the following:

- An active client record exists in Xero HQ with the correct organisation linked.
- The client organisation was accessed through the client record in the correct Xero HQ practice.

## What's next?

If you can't fix an MTD for VAT issue, please [contact HMRC](https://www.gov.uk/government/organisations/hm-revenue-customs/contact/vat-enquiries) (HMRC website) for issues in your HMRC business tax account, or Xero support for issues in Xero.
# Troubleshoot MTD for Income Tax issues (BETA)

Source: https://central.xero.com/s/article/Troubleshoot-MTD-for-Income-Tax-issues

---

## Overview

- Resolve issues when you set up Making Tax Digital (MTD) for Income Tax (IT).

Unable to connect to your HMRC account

During setup you’ll be re-directed to HMRC to authorise Xero to interact with HMRC on your behalf and give permission to create a secure connection between Xero and HMRC.

Check that you can log in to HMRC using these details and that you’ve entered them correctly:

- For business owners: this is your Government Gateway username and password.
- For accountants and bookkeepers: this is your Agent Services Account (ASA) username and password.

Invalid National Insurance number

If you see the error page **Invalid National Insurance number**, this means the National Insurance (NI) number entered is not linked to the HMRC account that’s been connected. This can happen if:

- The NI number was entered incorrectly. Check the number and try re-entering it.
- You or your client has not signed up for MTD with HMRC. To check this, verify that you can access MTD for IT services in your HMRC account.
- The wrong HMRC account was connected. This can happen if you entered incorrect login details or were already signed in to a different HMRC account on another browser window when setting up the connection.

Warning

Accountants and Bookkeepers need toconnect their ASA account and not their client’s HMRC account. Check that you can access MTD for IT services in your ASA account for your client.

You can also try reconnecting to HMRC. To do this:

1. At the **Enter your NI number** step, click **Connected the wrong account?**
2. In the popup window, read the instructions and click **Disconnect account.**
3. On the next popup, read the information and click **Disconnect account** again.
4. Once disconnected, you’ll be prompted to begin the onboarding process again. Make sure you are not logged into HMRC on any other browser tab as this can cause HMRC to connect the wrong account.

No businesses were found

When you enter a valid NI number, Xero retrieves a list of businesses from HMRC associated with the number. If you see the error**, 404 (Not Found) MATCHING\_RESOURCE\_NOT\_FOUND**, check with HMRC that the business has been registered.

Tax year set up couldn’t proceed

Check your HMRC account to see if your obligations have been set up for the tax year you selected.

If you get the error, **Tax year set up couldn’t proceed**, click **Back to your selection** and select a different tax year. If the issue persists, you’ll need to contact HMRC.

Can't access MTD for IT pages

If you can’t access MTD for IT or you get an error when you refresh, we can’t get any information from HMRC.

If you see any of the following error messages, the connection to HMRC was lost because either the HMRC connection has expired or the user has revoked Xero’s authority:

- **401 (Unauthorised) MISSING\_CREDENTIALS No OAuth token supplied**
- **401 (Unauthorised) INVALID\_CREDENTIALS Invalid OAuth token, including expired token**
- **401 (Unauthorised) UNAUTHORISED Other issue with authentication**
- **503 (Service Unavailable) SERVER\_ERROR Service is unavailable**

You’ll be prompted to connect to HMRC where you’ll need to complete Step 1 of the onboarding process. You won’t need to complete Steps 2 & 3 as Xero saves the NI number and selected business from the initial onboarding.

Scheduled maintenance

For a **503 (Service Unavailable) SCHEDULED\_MAINTENANCE Scheduled maintenance** error, you can check the [HMRC scheduled maintenance page](https://www.gov.uk/government/publications/use-software-to-send-income-tax-updates-service-availability-and-issues/use-software-to-send-income-tax-updates-service-availability-and-issues) and wait until the maintenance period is over.

If the MTD for IT pages won’t load this is because the HMRC services are unavailable. If it’s not scheduled maintenance, we’ll need to report this to HMRC and you should try again later.

Tax estimate isn’t showing

We don’t display a tax estimate until you’ve sent the first update to HMRC. The **Income** **Tax** **due** will show an empty state until you’ve sent the first update to see the estimate.

If the tax estimate is **Not** **available** this is because there was an error either triggering the calculation or retrieving the calculation from HMRC. This occurs from navigating back to the MTD for IT dashboard after sending an update or after manually updating the tax estimate.

If you see the Updating the tax estimate failed error message, you may need to manually update the tax calculation.

For the error, We can’t get any information from HMRC, refresh the page or try again later.

CIS Amount showing unexpected amount

The CIS amount shown in the Tax deducted section of the tax report comes from the figures your contractor has sent to HMRC through their monthly CIS300 return.

Don't include CIS deduction in the **Tax taken off trading income** box within the Income and Expenditure section. If you enter a figure here, it combines it with the amount that HMRC sends through to Xero, causing an unexpected overall total.

To resolve the issue:

1. Remove the amount in **Tax taken off trading income**.
2. Click **Resend to HMRC** for your quarterly submission.

You should now see an updated calculation showing the correct amount from HMRC.

## What's next?

If you can't fix an MTD for IT issue, please [contact HMRC](https://www.gov.uk/contact-hmrc) (HMRC website) for issues in your HMRC account, or Xero support for issues in Xero.
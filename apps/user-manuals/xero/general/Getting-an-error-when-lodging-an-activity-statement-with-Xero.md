# Resolve errors when lodging an activity statement in Xero

Source: https://central.xero.com/s/article/Getting-an-error-when-lodging-an-activity-statement-with-Xero

---

## Overview

- Find out more about the error messages you might get when using the lodge activity statements with Xero feature, and how you can resolve them.

| Error message(s) | What to do |
| --- | --- |
| CMN.ATO.AS.EM139 – EM139NoAsAccount CMN.ATO.AS.EM024 – Access to the activity statement is not available | The 3 digit ABN branch number (also called a GST branch number) is incorrect. Check the branch you’ve set in [organisation settings](/s/article/Update-your-organisation-s-settings-AU) is correct and update it if you need to. If you didn't enter an ABN branch during setup, Xero uses ‘001’. If you update your branch number in Xero, log out of your organisation and then log back in before you try connecting to the ATO again. You can get your ABN branch number from the ATO online services. For example, if your Number field is '11111111111/002', the branch number is 002 and your ABN is 1111111111. Alternatively, you can contact the ATO directly and ask them what branch you should use. |
| SBR.GEN.AUTH.006 – The software provider has not been nominated to secure your online (cloud) transmissions | The ATO hasn't authorised Xero to send activity statements to the ATO. You’ll need to call the ATO to authorise Xero before you can set up the connection. Once the ATO confirm authorisation, click **Check connection** to [try connecting](Lodge-activity-statements-with-Xero.md) again. |
| SBR.GEN.AUTH.008 – Your nomination with the online (cloud) software provider does not contain the correct Software ID CMN.ATO.AUTH.011 – The client you transmitted is not associated with the agent number you supplied and cannot be authorised | The tax agent isn’t authorised to lodge on behalf of this client. The tax agent needs to add the client to their client list using the client update service or the ATO online services. |
| XERO.AUTAX.SBRCommunicationError – There was a problem communicating with the ATO, contact the support team for a resolution | The ATO's servers are too busy to accept your submission. Wait 30 minutes, then try to submit your activity statement again. If this error persists for more than one day, please contact Xero support. |
| CMN.ATO.AS.EM060 – [Label] was reported as [supplied value] and will be corrected to [tax office value] | The ATO rejects the value(s) supplied in the activity statement, usually it’s the varied PAYGI amount. You can revert the statement to draft and make the required changes. For more information, contact the ATO. |
| XERO.BAS.ERROR or XERO.SBR.ERROR | This error generally occurs when the ATO servers time out due to lodgment congestion. You can relodge your statement. Contact Xero support is the problem persists. |

## What's next?

If you need more help, please contact Xero support below.
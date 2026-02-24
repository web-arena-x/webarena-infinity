# Troubleshoot tax returns in Practice Manager

Source: https://central.xero.com/s/article/Troubleshooting-tax-returns-in-Practice-Manager

---

## Overview

- Understand some common error messages when filing with Inland Revenue (IR).

Warning

We no longer support AIM returns for clients with foreign exchange transactions. AIM returns still support clients without foreign exchange transactions.

Common errors when filing GST and income tax

| | |
| --- | --- |
| **Error Message** | **Action** |
| Error in file version number | Correspondence sent with returns can only contain letters and numbers. If you see this error, remove symbols such as: ?, “, % and try again. If you continue to see the error, contact Xero support below. |
| Field 0: Duplicate Unit | IR views this return as a duplicate and won’t process it. Contact IR to confirm that the return has been received, before marking it as Filed. If IR confirms that it’s a duplicate, follow the instructions below to amend a filed, assessed or archived return. Note: If the **History** section of the return shows a GatewayID number, this might indicate that IR has already received the return. |
| Requesting agent not linked to client | The client and tax agent aren’t linked according to IR’s records. Contact IR to confirm. |
| Sending of return to IR failed with unexpected error | Unlock return and file again. If you continue to see the error, contact IR. |
| The username or password for this tax agent is incorrect | IR doesn't recognise the agent details you've entered. Go to your **Tax Agent** settings and under **Statement Information**, check that you've entered the correct agent information, then click **Save**. |
| Bank account invalid | The bank account details show as invalid. Enter the correct bank account name and number in the fields. See [making payments to Inland Revenue](https://www.ird.govt.nz/managing-my-tax/make-a-payment) (IR website) for more details. |
| Shareholder – IRD number is missing Owner – IRD number is missing Partner – IRD number is missing | The shareholder, owner or partner IRD number is missing. Enter a valid IRD number, or if the IRD number is unavailable enter 000-000-000. |
| We couldn’t get IRD data because a Tax Agent isn’t set up | If you receive this error, it means the client isn’t set up with a tax agent and their **Tax agent** field is set to **No**. The client needs to [set up a tax agent](File-income-tax-and-GST-as-a-tax-agent.md) and [connect to IR’s gateway services](Connect-to-IR-s-gateway-services.md). |

You might also find tax return warnings to show areas that might need a review. These warnings could cover the following:

- Income is between $24,000 and $48,000, taxpayer may be entitled to IETC
- Part year return = ensure date is within current tax year
- Other income has been entered, check if an IR10 needs to be attached
- Dividend imputation credits are greater than 28% of the gross dividends
- The client has not been assigned a tax agent

You can still file a tax return if these warnings are present, but we recommend checking the return first.

If you receive the warning, ‘[**Losses** tab field] in tax return differs to amount received from Inland Revenue, please confirm this is correct’, this means the amount you’ve entered in the **Losses** tab doesn’t match the amount Xero has received from IR. To reload the latest pre-fill at any time, you can select **Import IRD Data**. This overrides any existing data in the return. The fields you might need to update can include:

- Loss brought forward
- Residential rental deductions brought forward
- Research and development tax credits brought forward
- Excess imputation credits brought forward

Common gateway errors for AIM and Income tax returns

| | |
| --- | --- |
| **Error Message** | **Action** |
| (1) Invalid username and password | You need to [reconnect the tax agent to IR](Set-up-your-practice-s-START-connection-with-Inland-Revenue.md). |
| (3) Unauthorised access | The tax agent isn’t linked to this client and doesn’t have permission to file. [Link to a client account](https://www.ird.govt.nz/topics/intermediaries/linking-client-accounts/link-to-a-client-account) (IR website), or contact IR to resolve this message. |
| (4) Unauthorised delegation | This could be due to a number of reasons. Please try the following:   - Check the client is linked to your agency correctly - Check you have the necessary myIR authority to file returns on behalf of your agency - Reset your myIR password   If you're getting this error on the IR526 form, it's likely that the donation tax credit tax type doesn't yet exist for these clients. To resolve this you can either:   - Use the Client registration option under the tax agency **Tax preparer** tab to register them for donation tax credits - Contact IR using secure mail and get a donation tax credit account set up for the client   There might still be a delay after that for this to get processed by IR. If these steps don't fix the issue, contact IR to resolve this error message. |
| (-100) Tax agent has not been set up with gateway services. Go to Tax Agent screen and click Connect to IR | The tax agent’s connection to IR might not be set up. [Enable the agent's connection with IR](File-income-tax-and-GST-as-a-tax-agent.md) before attempting to create the return again. |
| (-101) Unexpected issue connecting to IR, please try again soon | There appears to be a connection issue with IR. If you're filing an AIM or income tax return, you might need to [reconnect a tax agent to GWS](Connect-to-IR-s-gateway-services.md). Try again by moving the AIM or income tax return back to Signed status. If you still need help, contact Xero support below. |
| (-102) Client balance date does not match IR records | The client balance date in Practice Manager doesn't match with IR records. Correct the balance month on the client screen or contact IR to resolve this message. |
| (103) No return found | No return exists for the selected filing period. |
| (104) Invalid filing period | The period end date you've selected doesn't match with IR records. Select the correct period end date or contact IR to resolve this message. |
| (105) No obligation found | The tax return filing frequency is set to **Not required**. Contact IR to resolve this error message. |
| (107) Duplicate Return | Check your myIR for a draft return. If there is one, delete the draft return and resubmit it using Xero Practice Manager. Alternatively, for an AIM return already submitted for this period, you can submit an amendment with **Amended as true**. For income tax or GST returns, you need to make amendments using myIR. |
| (111) Customer is ineligible for AIM Statement of Activity | Please contact IR to find out why your client is ineligible. |
| (112) Entity type not valid for AIM or customer is part of a consolidated group | The entity types supported for AIM are Individual and Company. If your client is set to a different entity type, change their business structure. If you think they should be able to file, please contact IR. |
| (117) A previously expected AIM return has not been filed | A previous return has been missed and needs to be filed first. |
| (118) Duplicate statement of activity | Select **Amend**, then complete the reasons for amendment if a return has been filed for that period already. |
| (120) Ratio return has been filed for this tax year | You're not able to opt into AIM once a ratio return has been filed for the tax year. Contact IR if you need any more help with this. |
| (122) Customer is ineligible for AIM Statement of Activity due to being in a transitional year | You're not able to opt into AIM during a transitional year. Contact IR if you need any more help with this. |
| (123) Income tax account inactive | You're not able to opt into AIM if the income (INC) account is inactive. Contact IR if you need any more help with this. |
| (124) No return has been filed for first period of tax year | Select the mid-year enrolment option if opting into AIM part way through the year. |
| (125) Cannot enter AIM mid-year while on Estimate provisional method | If there isn't an estimate for the current tax year, contact IR to resolve this message. |
| (126) Customer must be up to date with their provisional tax payments | You can receive this error if opting into AIM on a provisional tax due date, and the client already has a provisional assessment for the current year. Contact IR to resolve this message. |
| (127) Cannot opt into AIM mid-year if a previous Statement of Activity has been filed for the year | If this isn't your client's first AIM return for the year, ensure the mid-year enrolment option isn't selected. If you need more help with this, contact Xero support below. |
| (128) Can only amend the most recently filed Statement of Activity | IR only allows the most recently filed AIM return to be amended. If the return is in error, you don't need to click **Amend**. If you need more help with this, contact Xero support below. |
| (129) Mid-year entry missing from amendment submission | If you're amending a return that was used to opt in mid-year, the amended return must also have the box selected for mid-year opt in. |
| (142) Filing obligation not met | The type of form being submitted isn't what's expected. Contact IR to resolve this message. |
| (144) Return being submitted | The return has been submitted and is queued for processing. It might be held by IR for manual intervention. Log in to myIR to confirm the tax payer is active and IR is expecting a tax return to be filed. If you're filing an IR833 return when you experience this error, wait an hour then unlock the return and mark it as signed. IR has a limitation that doesn't allow an IR833 return to be filed at the same time as another main form, such as an IR3 or IR4. |
| (145) Return held for processing | The return can't be retrieved or amended because it's being processed by IR. |
| (146) Return unavailable for viewing | The return can't be viewed. This could be the case for older returns not submitted via Gateway Services. Returns in this state can be amended. |
| (156) Transfer must be greater than 0.00 | 0.00 isn't permitted as a transfer amount. Delete the entry and save the return. |
| (2013) Losses claimed this year error | Loss carried back opt in must be made via myIR, otherwise loss claimed can't be greater than loss brought forward. |
| (2014) Losses cannot be greater than income after expenses | Loss carried back opt in must be made via myIR, otherwise loss claimed can't be greater than income after expenses. |
| (2016) Customer not entitled for early payment discount | Customer doesn't meet Early Payment discount eligibility criteria. Refer to the relevant guide to confirm, or contact IR to resolve this message. |
| (2019) partYearEndDate must be contained within the return period | The part year end date you've entered must fall in the current tax year. |
| (2021) partYearStartDate must be contained within the return period | The part year start date you've entered must fall in the current tax year. |
| (2031) Cannot claim losses claimed this year when a loss was made in this income year | Remove the loss claimed this year from the current year's tax return. |
| (2047) Total dividend credits cannot be greater than total dividends | Total dividend credits are greater than the total dividends on the IR3NR return. To resolve this issue, reduce the amount of dividend credits. |
| (2053) PIE income total tax credits cannot be greater than 28 percent of PIE income and/or PIE income total tax credits cannot be greater than tax on taxable income | Due to rounding changes at IRD, there’s a difference in how they calculate tax on taxable income. To resolve this issue, reduce the PIE tax credit amount by 0.01 (1 cent). |
| (2075) Estate or trust not paying tax on this beneficiary's income | IR6B – If **Trust paying tax** is set to **No**, then only **7K**, **27M**, **27O**, **27Q**, **27U**, **27V**, **27W**, **27X** and **27Y** should be completed. |
| (2153) The period end date may not be more that four years in the past | IR526 – Tax credit claim form. Donation tax credits can only be claimed within a period of four years following the year of the donation. |
| (2228) Unexpected error | You need to make a loss carry-back (LCB) election in myIR before filing the tax return. |
| (2339) Settlor - DOB or commencement date can not be greater than the current tax year end date | You need to update the **Settlor's DOB or commencement date** on the IR6S to a date that's earlier than the end date of the current tax year. |
| (2340) Unexpected error | Check [your IR6S](IR6-Estate-or-Trust-tax-return.md) to make sure that you have a valid country code entered in keypoint SJR in the settlor schedule. You can view the full list of [ISO Alpha-2 country codes](https://www.iso.org/obp/ui/#search/code/) on the International Organisation for Standardisation website. |
| (2341) Settlor IRD number provided is invalid | You need to enter a valid IRD number for the settlor. |
| (2342) Settlor IRD number has not been provided | You need to enter an IRD number for the settlor. |
| (2343) Tax ID number not provided when required | Check that the tax ID number has been provided when it’s required in the IR6S. We recommend that you check if it's missing in the trust settlor details. |
| (2344) No jurisdiction TIN has an invalid value | The settlor’s tax jurisdiction in the IR6S has been entered as **NZ** and **1 TIN not required in jurisdiction** is selected. To resolve this issue, unlock the return, clear the checkbox next to **1 TIN not required in jurisdiction**, then file the return again. |
| (2345) Other field description not provided when previous field has a non-nil value | There’s an issue with the settlor schedule in the trust return. If there’s a non-nil value entered in the **Other** (keypoint 11) field, you'll need to enter something in the description of the **Other** (keypoint 12) field. |
| (2349) Invalid tax jurisdiction value | Enter a tax jurisdiction value for the beneficiary in the IR6B using the [special instructions for tax jurisdiction](IR6-Estate-or-Trust-tax-return.md). |
| (2352) Invalid IRD number entered for beneficiary | Enter a valid IRD number for the beneficiary. If you don't have a valid IRD number and it can't be reasonably obtained (eg beneficiary has passed away), you'll need to select the **TIN not required in jurisdiction** checkbox. |
| (2357) Missing settlor's DOB or commencement date | You need to enter a value in the settlor's DOB or commencement date box in the IR6S or settlor's schedule. |
| (2358) Missing tax jurisdiction value | You need to enter the settlor’s tax jurisdiction in the IR6S. |
| (2359) Settlor - at least one field in the settlement data must be completed | If **No settlement this year** is selected, a value must be entered into at least one keypoint in the IR6S settlement section. To resolve the issue, unlock the return and select one of these checkboxes. Alternatively, enter the correct amount in the IR6S settlement section. |
| (2366) Unexpected error | Check the two-letter country code entered in the Overseas income worksheet. For example the ISO Alpha 2 country code for the United Kingdom of Great Britain and Northern Ireland is GB and not UK. You can view the full list of [ISO Alpha-2 country codes](https://www.iso.org/obp/ui/#search/code/) on the International Organisation for Standardisation website. |
| Internal error | In most cases, this error is caused by an incorrectly formatted IRD number. Check all IRD numbers entered into the return are formatted correctly as XXX-XXX-XXX and the IRD number is valid before trying to file the return again. If you still need help, contact Xero support below. |

For all other errors, contact Xero support below.

## What's next?

Learn how to [amend a filed, assessed or archived return](Amend-a-filed-assessed-or-archived-return.md).
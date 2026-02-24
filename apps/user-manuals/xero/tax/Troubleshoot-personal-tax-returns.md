# Troubleshoot personal and partnership tax returns

Source: https://central.xero.com/s/article/Troubleshoot-personal-tax-returns

---

## Overview

- If you get an error while working on a personal or partnership tax return, check here for a solution before you contact Xero support.

Common error messages

Personal tax Partnership tax

| | |
| --- | --- |
| **Error message** | **Action** |
| Annual investment allowance should not be present for other property if cash basis is being used / The entry in box [PRO32] should not be present as there is no entry in [pro20.2]. Please check. | This will occur if: - You have an entry in **Other UK property** in the **UK property income schedule.** - There's an amount in **Annual investment allowance.** - **Traditional accounting basis used for UK property business** is set to **No** in the **UK property income schedule**.   To fix, either remove the annual investment allowance claim, or set **Traditional accounting basis used for UK property business** to **Yes**. |
| Date of disposal must be within [date] and [date]. | The date of disposal is outside of the tax year. For example, 2023/24 tax returns can only include disposals from 6 April 2023 to 5 April 2024. Review and amend the date in the tax year or remove the date, then submit the return again. |
| [field] must not contain any special characters. | Check that:   - There are no preceding or trailing spaces in the field.   HMRC accept:   - A to Z (upper case) - a to z (lower case) - 0 to 9 (numeric) - space & ‘ ( ) \* , - . / @ £ |
| 1046: Authentication Failure. The supplied user credentials failed validation for the requested service. | Check that:   - The UTR is correct and you're registered as the client’s agent - You’re using the correct government gateway ID - In your HMRC account, you’ve activated the [Self Assessment for Agents service](https://www.gov.uk/guidance/self-assessment-for-agents-online-service#what-you-can-do-in-the-service) (HMRC website) - The password doesn’t contain special characters   HMRC accept:   - A to Z (upper case) - a to z (lower case) - 0 to 9 (numeric) - space & ‘ ( ) \* , - . / @ £ |
| 2021: The supplied IRmark is incorrect | This error is usually caused by invalid characters or additional spaces. Remove any additional spaces, including at the end of sentences or numbers, and check for invalid characters. HMRC accept:   - A to Z (upper case) - a to z (lower case) - 0 to 9 (numeric) - space & ‘ ( ) \* , - . / @ £ |
| 4065: Invalid content found at element [field or box name]. Or 4085: Value [field or box name] doesn't have the correct format. | An error message containing **Invalid content** or **Value doesn't have the correct format** usually means that the return contains invalid characters or that the character limit for that field has been exceeded. HMRC accept:   - A to Z (upper case) - a to z (lower case) - 0 to 9 (numeric) - space & ‘ ( ) \* , - . / @ £   Remove any other characters in the return. The error can also mean a field or box is blank. Make sure the relevant sections have the correct information. |
| 4066: Incomplete content found at element [field or box name]. | This error occurs when something expected by HMRC based on what you’ve already added to the return is missing. The final section of the message indicates which field or box the error relates to.  For example, if the error message is **Incomplete content found at element 'BankAccountDetails'**, it means that **Claim repayment by bank transfer** is selected in the **Other return information** schedule, but the client in HQ doesn’t have any bank repayment details. To resolve this error, choose to claim the refund via cheque, or click **Edit client details** to add bank repayment details to the client in HQ. |
| 5001: The namespace must match the schema being used | This usually occurs when the government gateway server has either been switched off or not yet switched on for the tax year that is being filed. Tax returns will be accepted from the day after the end of the tax year up until the fourth anniversary of the end of the tax year. For example, the 2023/24 tax year is open for original tax return submissions between 6 April 2024 and 5 April 2028. |
| 5015: A submission for the user and tax year has already been successfully made. If amendment(s) are required you will need to make an amended submission. | If you’re filing an original tax return, check that the UTR is correct. If you’re filing an amended tax return, check that you’ve followed the [correct process in Xero Tax](Submit-or-amend-a-personal-tax-return.md). If the above options don’t resolve the error message, contact HMRC. |
| 5017: Failed to match Tax Reference | This error indicates the UTR included in the tax return has been blocked or doesn’t exist with HMRC. A UTR gets blocked if HMRC send a SuRF1 (Suspected Repayment Fraud) letter for identity checks, and it isn’t actioned within 30 days. If HMRC aren’t contacted within 30 days, the Self Assessment record is suspended and the UTR is blocked. Contact HMRC to resolve this error. |
| 5050: The time limit for submitting a return online is 4 years after the end of the year to which it relates. Please check. | An original tax return cannot be filed more than four years after the end of a tax year. For example, for the 2019/20 tax year which ends on 5 April 2020, the tax return must be submitted by 5 April 2024. If this deadline has passed, the tax return will need to be filed by paper, if allowed by HMRC. You’ll need to **Mark as filed** once you have confirmation from HMRC the paper filing has been received. |
| 5090: You have indicated an amended submission but the amendment window has now closed for the year of assessment to which your submission relates. | If you are amending a tax return, the tax return can only be submitted online up to twelve months after the filing deadline. For example, for a 2022/23 tax return, the amended deadline is up to12 months after the filing deadline of 31 January 2024 and so must be filed by 31 January 2025. If this deadline has passed, the tax return will need to be filed by paper, if allowed by HMRC. You’ll need to **Mark as filed** once you have confirmation from HMRC the paper filing has been received. |
| 5093: Authentication error | Although the return might contain a valid UTR, HMRC doesn’t recognise the UTR for the service you’re trying to file under. Check that you have the correct service in the portfolio associated with the login details you’re using. If you can’t resolve this issue, contact HMRC for more information. |
| 6791: There must be an entry in one of [FSE101], [LUN64], [SPS26], [FPS26] or [SSE37] as there is an entry in one of the boxes [FSE76], [LUN52], [SPS20], [FPS20] or [SSE31] and there is an entry in [YPD1], and box [YPD1] date + [66 years] is prior to the beginning of the return year or on 6 April of the return year. | This error occurs when your client is past the state pension age, but in the Class 2 and 4 NIC schedule the Class 4 exempt is set to **No**. The error will only show when you use our test in live tool, or try to move a return from a Draft status. Set the Class 4 exempt back to **Yes** then try again. When you submit a return, Xero Tax calculates the state pension age and automatically sets the Class 4 exempt box to **Yes**. |
| 8253: Line 4 is completed, lines 1, 2 & 3 must also be completed. Please check. | There are missing lines in the address. Check the address is complete and ensure each address line is entered sequentially, for example, add Line 1 first, then Line 2 etc. For foreign addresses, leave the **Postcode** field blank and enter the information on the address lines. |
| 6277: There is an entry in box [CAL14]. Please complete [AOI14] or [LUN28] or [FSE71] or [FSE72] or [FPS11] or [SPS11] | A figure has been entered into box **Increase in tax due to an adjustment in an earlier year** in the **Tax and PAYE coding adjustments schedule**. If you want to include this adjustment, you need to enter one of the following:   - An adjustment for change of accountancy practice on self employment or partnership trade profits - An averaging adjustment on self employment or partnership trade profits - A post cessation or other business receipts in **Other income schedule** If you're not claiming any of the above adjustments, you can remove the figure from PAYE coding and adjustments. If you’re trying to enter tax from an earlier year, including in the PAYE code, enter the figure in the correct box within the PAYE coding section. |

| | |
| --- | --- |
| **Error message** | **Action** |
| [field] must not contain any special characters. | Check that:   - There are no preceding or trailing spaces in the field.   HMRC accept:   - A to Z (upper case) - a to z (lower case) - 0 to 9 (numeric) - space & ‘ ( ) \* , - . / @ £ |
| 5001: The namespace must match the schema being used | This usually occurs when the government gateway server has either been switched off or not yet switched on for the tax year that is being filed. Tax returns will be accepted from the day after the end of the tax year up until the fourth anniversary of the end of the tax year. For example, the 2023/24 tax year is open for original tax return submissions between 6 April 2024 and 5 April 2028. |
| 5015: A submission for the user and tax year has already been successfully made. If amendment(s) are required you will need to make an amended submission. | If you’re filing an original tax return, check that the UTR is correct. If you’re filing an amended tax return, check that you’ve followed the [correct process in Xero Tax](Submit-or-amend-a-personal-tax-return.md). If the above options don’t resolve the error message, contact HMRC. |
| 5017: Failed to match Tax Reference | This error indicates the UTR included in the tax return has been blocked or doesn’t exist with HMRC. A UTR gets blocked if HMRC send a SuRF1 (Suspected Repayment Fraud) letter for identity checks, and it isn’t actioned within 30 days. If HMRC aren’t contacted within 30 days, the Self Assessment record is suspended and the UTR is blocked. Contact HMRC to resolve this error. |
| 5050: The time limit for submitting a return online is 4 years after the end of the year to which it relates. Please check. | An original tax return cannot be filed more than four years after the end of a tax year. For example, for the 2019/20 tax year which ends on 5 April 2020, the tax return must be submitted by 5 April 2024. If this deadline has passed, the tax return will need to be filed by paper, if allowed by HMRC. You’ll need to **Mark as filed** once you have confirmation from HMRC the paper filing has been received. |
| 5090: You have indicated an amended submission but the amendment window has now closed for the year of assessment to which your submission relates. | If you are amending a tax return, the tax return can only be submitted online up to twelve months after the filing deadline. For example, for a 2022/23 tax return, the amended deadline is up to12 months after the filing deadline of 31 January 2024 and so must be filed by 31 January 2025. If this deadline has passed, the tax return will need to be filed by paper, if allowed by HMRC. You’ll need to **Mark as filed** once you have confirmation from HMRC the paper filing has been received. |
| 5093: Authentication error | Although the return might contain a valid UTR, HMRC doesn’t recognise the UTR for the service you’re trying to file under. Check that you have the correct service in the portfolio associated with the login details you’re using. If you can’t resolve this issue, contact HMRC for more information. |
| 8561: If [1.22A] is absent then [1.24] + [1.34] should not exceed [£150,000] | You need to change the accounting basis to **Accrual.** If the property income and balancing charges exceed £150,000, the partnership's accounting basis needs to be **Accrual**. |
| Accounting period and tax year dates are out of sync. Please review to ensure your submission is accurate | The year end of the tax return doesn't align with the tax year. Investment partnerships should follow the tax year. You can update the partnership tax year dates in **Business Details**. |

Understand other error messages

If you receive an HMRC error message that starts with a three letter code, followed by a number, this usually means either:

- There's data missing from a box that HMRC expects you to complete
- Two or more boxes conflict, such as when HMRC requires you to select only one option

The three letter code indicates which section of the form contains the error. The number that follows is the box number.

For example, the error code PRO44 relates to SA105 - UK property and the error is in box 44.

| | | |
| --- | --- | --- |
| **Three letter code** | **HMRC page and section** | **Schedule in Xero** |
| AIL 1-6 | SA101 - Page Ai3 - Other information | - AIL1-2 - Other income - AIL3-6 - Other tax reliefs |
| AIL 7-8 | SA101 - Page Ai4 - Pension Savings Tax Charges | Pension charges |
| AIL 19-20 | SA101 - Page Ai4 - Tax Avoidance Schemes | Tax avoidance schemes |
| AOI | SA101 - Page Ai1 - Other UK income | - AOI1-3 - UK interest - AOI 4-11 - Gains from UK life insurance policies etc - AOI 12-13 - UK dividends and distributions - AOI 14-15 - Other income |
| AOR | SA101 - Page Ai2 - Other tax reliefs | - AOR 1-3 and 10-11 - Investment tax reliefs - AOR 4-9 and 12 - Other tax reliefs |
| ASE | SA101 - Page Ai2 - Share schemes and employment lump sums, compensation and deductions, certain post-employment income and patent royalty payments | Employment and lump sums |
| CAL | SA110 - Tax calculation summary | - CAL1-2 - Calculated tax due figure - CAL3 and 3.1 - Student and postgraduate loans - CAL4 and 4.1 - Class 2 and 4 NIC - CAL5 - Capital gains - CAL6 - Pensions charges - CAL7-9 and 14-16 - Tax and PAYE coding adjustments - CAL10-11 - Payments on account - CAL12-13 - Allowances |
| CBC | SA100 - Page TR5 - High income child benefit | Child benefit charge |
| CGT | SA108 - Capital Gains Tax summary | Capital gains |
| COV | SA100 - Page TR5 - Incorrect claimed coronavirus support | Other income |
| EMP | SA102 - Employment | Employment and lump sums |
| FIN | SA100 - Pages TR 6, 7 or 8 - Finishing your tax return | - FIN1-3 - Tax and PAYE coding adjustments - FIN4-18 and 20-26 - Other return information - FIN19 - Additional notes for tax return |
| FOR | SA106 - Foreign | Foreign income |
| FSE | SA103F - Self-employment (full) | Self employment |
| INC | SA100 - Page TR3 - Income | - INC1-2 - UK interest - INC3, 6-7 - Foreign income - INC4-5 - UK dividends and distributions - INC8-16 - Pensions and state benefits - INC17-21 - Other income |
| MAT | SA100 - Page TR5 - Marriage Allowance | Allowances |
| MCA | SA101 - Page Ai3 - Married Couple’s Allowance | Allowances |
| NRD | SA109 - Residence, remittance basis etc | Residence and domicile |
| PRO | SA105 - UK property | UK property income |
| REL | SA100 - Page TR4 - Tax reliefs | - Pension contributions REL1-4 - Gifts to charities REL5-12 - Allowances REL13-16 |
| SLR | SA100 - Page TR5 - Student Loan and Postgraduate Loan repayments | Student and postgraduate loans |
| SSE | SA103S - Self-employment (short) | Self employment |
| TRU | SA107 - Trusts etc | Trusts and estates |

## What's next?

If you need further help with a return, click the menu icon , then select **Add Xero support**. When you raise a case, please let our support team know which client and return you’ve given us access to.
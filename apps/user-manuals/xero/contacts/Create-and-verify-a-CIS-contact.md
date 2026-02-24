# Create and verify a CIS contact

Source: https://central.xero.com/s/article/Create-and-verify-a-CIS-contact

---

## Overview

- Add CIS information to a new or existing subcontractor’s contact record so Xero can calculate CIS deductions when you pay them.
- Verify CIS subcontractors with HMRC straight from Xero with the CIS Contractor add-on.
- Resolve CIS verification flow issues.

About CIS contacts

### How it works

- A subcontractor must be set up as a CIS contact before you can use CIS account codes on bills or credit notes for them.
- HMRC requires you to verify a subcontractor’s deduction rate before you pay them for the first time. You must also verify a subcontractor if you haven’t included them on a monthly return in the current or last two tax years.
- [You need to enable CIS in your organisation](Enable-CIS-in-your-organisation.md) before you can set up a CIS contact, and you need to [add CIS Contractor to your subscription](/s/article/Changing-pricing-plan-UK) in order to use subcontractor verification in Xero.
- You need the advisor or standard + reports user role to verify a CIS contact.
- Xero doesn't change existing bills when you add CIS information to a contact, but you can edit existing bills to add CIS details if required.
- Once CIS is enabled for a contact, you can edit the CIS rate and other details. However, the contact can't be disabled or merged with another CIS contact. If you merge a non-CIS contact with a CIS contact, you can't restore the non-CIS contact.

### CIS contact fields explained

CIS contacts have the following additional fields in their contact record.

| Field in Xero | Column on import file | Description | Requirements |
| --- | --- | --- | --- |
| **CIS Subcontractor** | CISContact | When importing contacts into Xero, select:   - **Y** – if the contact is a CIS subcontractor - **N** – if the contact isn't a CIS subcontractor | Mandatory for all organisation types. |
| **Registered CIS name** | RegCISName | Xero displays the **Contact** **Name** from the contact record. Enter the contacts registered CIS name, if it's different. | Mandatory for all organisation types. |
| **CIS rate** | CISRate | The **CIS** **Rate** applicable to your contact:   - Gross (0%) - Standard (20%) - Higher (30%) | Mandatory for all organisation types. |
| **Organisation type** | EntityType | The type of organisation applicable to your contact:   - Sole Trader - Limited Company - Partnership - Trust | Mandatory for all organisation types. |
| **National Insurance Number** | NIN | The NIN for the contact. It needs to be in the format XX000000X, be 9 characters long, start with two letters, and end in a letter between A - D or a space. | Sole Trader – Optional. Trust and Partnership – Optional if CRN is entered, otherwise mandatory. |
| **Company registration number** | CRN | The CRN for the contact. It needs to be in the format 00000000 or XX000000. | Limited Company – Mandatory. Trust and Partnership – Optional if NIN is entered, otherwise mandatory. |
| **Unique taxpayer reference** | UTR | The contact's UTR. It needs to be in the format 0000000000, be 10 digits long, and be a valid number recognised by HMRC. | Optional for all organisation types. |
| **Subcontractor verification number** | SVN | The contact's SVN you received from HMRC when you verified the subcontractor. It needs to be in the format V0000000000, V0000000000X or V0000000000XX. | Optional for all organisation types. |

Add CIS information to a contact

### Add or edit a single subcontractor's CIS details

1. In the **Contacts** menu, select **All Contacts**.
2. Either:
   - For an existing contact – Find and open the contact you want to edit, then click **Edit**.
   - For a new contact – Click **New contact**, then enter the [other contact details](Contact-fields.md) as required.
3. Select **CIS** **subcontractor**, then enable **CIS** **deductions** to show the CIS contact fields.
4. Complete the CIS fields. You must complete the **Organisation type**, **Registered CIS name** and **CIS rate** fields before you can save the contact.
5. Click **Save contact and verify CIS details** to verify the subcontractor using Xero’s verification flow.

### Add or edit CIS details for multiple subcontractors

To set up multiple CIS contacts at the same time, [import new contacts](Import-contacts-into-Xero.md) or [edit multiple contacts](/s/article/Update-or-edit-multiple-contacts?userregion=true) as usual and complete the CIS fields as required.

When you’ve imported the new details, verify each subcontractor through Xero’s verification flow or through HMRC.

Tip

See all the contacts you've set up in the [CIS Contractor report](File-a-CIS-Return-with-HMRC.md) on the CIS enabled subcontractors tab.

Verify a CIS subcontractor in Xero

### About subcontractor verification

- [Add CIS Contractor to your subscription](/s/article/Changing-pricing-plan-UK) to use subcontractor verification.
- You need your HMRC credentials and you need the advisor or standard + reports user role in Xero to complete the process.
- Before beginning the verification flow, enter the subcontractor’s UTR and the subcontractor’s expected deduction rate.
- If you don’t enter the subcontractor’s UTR, HMRC can’t verify the subcontractor and applies the default rate of 30%.
- If you leave the CIS rate field empty, Xero applies the highest deduction rate of 30% so the field can be verified as part of the verification flow. Xero updates the field to the correct rate when the verification process is complete.
- You can't verify a subcontractor who is part of a partnership in Xero. Instead, verify them directly with HMRC and add their details into Xero manually.

### Verify a subcontractor

1. In the contact record, complete the CIS fields, then click **Save contact and verify CIS details**. You can also start the verification process from the subcontractor list in the CIS Contractor report.
2. Check the details displayed are correct. If you haven't already entered the subcontractors UTR, add it now. If you don't enter a UTR, the default deduction rate of 30% is applied.
3. Click **Continue**.
4. Enter your HMRC User ID and password, then click **Log in to HMRC**.
5. HMRC verifies the details you've entered in Xero.

If the subcontractor details you've entered match what HMRC have on record, you'll receive confirmation of the subcontractor's deduction rate, SVN and verification date. Xero saves this information in the contact record.

If HMRC's records don't match what your subcontractor told you, click **Back** to return to the contact's details. Check the details in their contact record and update as required, then verify the subcontractor again. You might want to check the details with the subcontractor or their accountant if you still can't verify them.

If the subcontractor isn't registered for CIS, HMRC applies the default rate of 30%.

Troubleshoot issues with the CIS verification flow

### Verification errors

If there’s a problem with something you’ve submitted, you’ll get a verification error.

- **Verification failed** indicates that CIS details in the subcontractor’s record are in the wrong format.

To resolve a verification error, check the format of the fields required for your organisation type.

### System errors

If there's a problem with HMRC or Xero, you'll get a system error.

- **Sorry, something went wrong** usually indicates a temporary issue with the HMRC connection or Xero’s internal systems. It can also be due to concurrency issues if you have more than one browser tab of the contact record open.
- **An error has occurred within Xero** indicates there’s an issue with Xero’s internal system.
- **An error has occurred at HMRC** indicates there’s something wrong with HMRC's system, or it’s too slow to respond. If a response isn’t received after 25 seconds, the connection times out and you receive this error.

To resolve a system error:

1. Click the close icon in the top left hand corner of the error message to close it. Close any other browser tabs with the contact record open.
2. Return to the subcontractor’s contact record and refresh the screen.
3. Start the verification process again from step 2.

If you need further help, please contact Xero support below.

## What's next?

You're all done!
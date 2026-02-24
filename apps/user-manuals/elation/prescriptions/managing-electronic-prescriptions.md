# Prescriptions Guide - Managing electronic prescriptions to and from pharmacies

Source: https://help.elationhealth.com/s/article/managing-electronic-prescriptions

---

# ​​​**Contents**

- [Overview](#overview)
- [Workflow Instructions](#workflows)
 - [Receiving & addressing prescription refill requests from pharmacies](#refill_requests)
 - [Managing electronic prescriptions sent to pharmacies](#electronic_prescriptions)
    - [Receiving fill status notifications from pharmacies](#fill-status)
    - [Receiving prescription change requests from pharmacies](#rx-change-request)
    - [Sending prescription cancelation requests to pharmacies](#request-cancel)
- [Frequently Asked Questions](#faq)

# **Overview**

Elation partners with Surescripts to enable the electronic exchange of prescriptions between your EHR and pharmacies. The following features are available:

- Receive electronic refill requests from pharmacies.
- Send electronic prescriptions to pharmacies.
 - Receive fill status notifications for sent prescriptions.
 - Receive prescription change requests.

# **Workflow Instructions**

## **Receiving & addressing prescription refill requests from pharmacies**

Electronic refill requests are sent from the pharmacy to the patient's chart, where they're assigned to a Provider. The request will appear in the **Requiring Action** section of the patient's chart and in the **Rx Requests** inbox on the Provider's Practice Home page. Requests older than 30 days are automatically archived.

To action on an electronic refill request for **non-controlled substance medications**, follow the steps below. [Click here for instructions on how to address controlled substance medication refill requests](https://help.elationemr.com/s/article/how-to-e-prescribe-controlled-substances#RefillRequest).

| | |
| --- | --- |
| **1** | Go to the **Rx Requests** inbox and click on the patient's name to view the prescription refill request in their chart. |
| **2** | Review the refill request in the **Requiring Action** section of the patient's chart. You will typically see the following detail if applicable:   - Medication name & strength. - Last prescription received by the pharmacy for this medication. - Last dispensed prescription for this medication. - Original prescription for this medication. |
| **3** | Click one of the actions at the bottom of the refill request to address the request. Actions may include:   - **Approve** - Notifies the pharmacy that you approve the prescription refill as requested.    - If the **Approve** button is disabled it means the refill request is missing **Sig** information. Use the **Approve** with modifications option to approve the script after modifying the **Sig**. - **Approve with modifications** - Allows you to update the **Sig** information and then notifies the pharmacy about the approved refill request with modified **Sig**. - **Change Number of Refills** - Allows you to update the number of approved refills and then notifies the pharmacy about the approved refill request with modified refills. - **Deny** - Notifies the pharmacy that you denied the refill request. - **Deny & add reason** - Allows you to add a denial reason and then notifies the pharmacy that you denied the refill request. |
| **4** | Once you respond to the prescription refill request, a record of the script and your actions will be stored in the patient's chart. |

ℹ️   **NOTE** By default, electronic refill requests will be assigned to the Provider Level User whom the pharmacy is requesting a response from. Typically the assigned Provider or their [Rx Delegates](https://help.elationemr.com/s/article/staff-permissions--staff-delegates) would address the electronic refill request. If needed, another Provider Level User (or their own Rx Delegates) can also respond to the assigned Provider's refill request as long as the Provider Level User is not an Rx Delegate for another Provider Level User.

## **Managing electronic prescriptions sent to pharmacies**

Once a prescription is sent to the pharmacy, the following can happen:

1. Pharmacies may notify you of the fill status of the prescription.
2. Pharmacies may send you prescription change requests.
3. You can send a cancellation request to the pharmacy if you no longer want them to fill the prescription.

##

### **Receiving fill status notifications from pharmacies**

Pharmacies can choose to electronically update you on the fill status of a prescription. The type of fill statuses that pharmacies can send include:

- dispensed
- partially dispensed
- not dispensed
- transferred (to another pharmacy)

Pharmacies may also send a note to explain the status (e.g. “not dispensed because the prescription is out of stock”) but are not required to. ​For example, when a pharmacy dispenses a prescription, the fill status will appear as follows:

ℹ️   **CAUTION** Pharmacies are not required to send fill status notifications therefore it is normal if the fill status does not display for some prescriptions.

##

### **Receiving prescription change requests from pharmacies**

Pharmacies can send you prescription change requests electronically. Pharmacies most commonly send prescription change requests:

- if the patient requests a generic substitution at the pharmacy.
- for script clarification.
- in the event that the prescription is out of stock.

Change requests appear in a Provider's **Rx Requests** inbox in the Practice Home page and in the **Requiring Action** section at the top of the patient’s chart. To respond to a prescription change request:

| | |
| --- | --- |
| **1** | Go to the **Rx Requests** inbox and click on the patient's name to view the prescription refill request in their chart. |
| **2** | Review the change request and click one of the actions at the bottom of the refill request to address the request. Actions may include:   - **Approve** - Notifies the pharmacy that you approve the change as requested. - **Approve with modifications** - Allows you to update the script and then notifies the pharmacy about the approved change request along with the modifications. - **Deny & add reason** - Allows you to add a denial reason and then notifies the pharmacy that you denied the refill request.   For controlled substance medication change requests, providers must use their EPCS token to complete the requests due to DEA requirements. |
| **3** | Once you respond to the prescription change request, a record of the script and your actions will be stored in the patient's chart. |

- **Important Note**: Our prescribing partner regularly reviews the response rates to electronic prescription change requests. To preserve the reliability of this feature, our prescribing partner will stop sending electronic prescription change requests to a provider if the provider consistently does not respond to electronic change requests. Once the feature is turned off, pharmacies will instead have to fax change requests to the provider or use other methods to contact the provider.

ℹ️   **CAUTION** Surescripts regularly reviews the response rates to electronic prescription change requests. To preserve the reliability of this feature, Surescripts will stop sending electronic prescription change requests to a provider if the provider consistently does not respond to electronic change requests within a timely manner. Once the feature is turned off, pharmacies will instead have to fax change requests to the provider or use other methods to contact the provider.

We recommend that providers respond to a prescription change request within 48 hours or the pharmacy will call or fax the provider to prevent delays in patient care.

##

### **Sending prescription cancelation requests to pharmacies**

A Provider Level User or ​authorized [Prescription delegate](staff-permissions--staff-delegates.md)​ can request to cancel any prescription sent electronically to a pharmacy by clicking **Actions** -> **Cancel this eRx order**.

For example, when you send a cancellation request, the prescription order status will appear as:

And, once the pharmacy approves the cancellation request, the canceled prescription will appear as:

ℹ️   **NOTE**

- Pharmacies should respond to cancellation requests within 12 hours, but pharmacies are not obligated to keep to this timeframe. If you do not receive a response from the pharmacy to the cancellation request within 24 hours, we recommend directly contacting the pharmacy.
- If you would like to reverse an in-progress cancellation request, you must contact the pharmacy directly to suspend the request.

# **Frequently Asked Questions (FAQ)** **Can staff manage electronic prescriptions on a provider's behalf?**

Yes, Provider Level Users can allow Staff Level Users to execute prescription orders on their behalf by assigning individuals as Authorized Rx Delegates. Authorized Rx Delegates can perform the duties listed below. Learn more about how to assign Authorized Rx Delegates in the [User Accounts Guide- Utilizing authorized staff delegates](staff-permissions--staff-delegates.md) article.

- Transcribe prescription orders in the EMR and send a new prescription electronically to the pharmacy on provider's behalf.
- Transcribe verbal approval or denial of a prescription refill or change request received from a pharmacy and send that approval or denial electronically to the pharmacy on provider's behalf.
- Transcribe provider's order to discontinue a medication in the EMR for documentation purposes
- Transcribe provider's order to cancel a medication sent to a pharmacy

ℹ️   **EXCEPTIONS** Authorized Rx Delegates will not be allowed to ePrescribe controlled substance medications or address controlled substance medication refill requests on a provider's behalf due to DEA regulations.

#### **Pharmacies are faxing change requests to me instead of sending the request electronically. Why is this happening?**

Elation EHR supports [receiving electronic prescription change requests from pharmacies](#rx-change-request). However, our prescribing partner regularly reviews the response rates to electronic prescription change requests. To preserve the reliability of this feature, our prescribing partner will stop sending electronic prescription change requests to a provider if the provider consistently does not respond to electronic change requests. Once the feature is turned off, pharmacies will instead have to fax change requests to the provider or use other methods to contact the provider.

If you wish to receive electronic change requests, contact a member of our Support Team using the **I need help** -> **Contact Elation Support** button at the top of your Elation account and a member of the Support Team will be able to assist you with verifying your ePrescribing configuration.

## **Related Articles**

- [Prescription Form Guide- ePrescribing and ordering medications using a single prescription form](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md)
- [Prescription (Rx) Templates Guide](create-and-use-custom-rx-templates.md)
- [User Accounts Guide- Utilizing authorized staff delegates](staff-permissions--staff-delegates.md)
- [Prescriptions Guide- Frequently Asked Questions](Prescriptions-Guide-Frequently-Asked-Questions.md)
# Billing Guide- Delayed Billing

Source: https://help.elationhealth.com/s/article/How-to-set-up-Delayed-Billing

---

## **Contents**

- [What is Delayed Billing?](#whatisdelayedbilling)
- [Who should use Delayed Billing?](#whoshoulduse)
- [How to turn on Delayed Billing](#howdoyouturnon)
- [How to send bills to your PMS when Delayed Billing is enabled](#howdoyousend)
- [Frequently Asked Questions](#FAQ)

## **What is Delayed Billing?**

For customers using [Elation Billing](Elation-Billing-All-in-One.md) (Elation's all-in-one billing solution) or certain Practice Management System (PMS) integrations with Elation ([see below for which PMS integrations can use this feature](#whoshoulduse)), bills (or claims) are sent to the PMS once a visit note is signed off on. Delayed Billing is a Setting that overrides this default behavior. Instead, upon visit note sign off, the bill will enter a queue in [Billing Home](Billing-Home.md) in Elation for further editing. From there, your practice can make any adjustments to the bill before sending it to your PMS.

This feature is valuable for practices with a coder or designated biller who edits bills after visit note sign off, as it allows the biller to ensure that the bill is comprehensive and accurate prior to submission to the PMS. Without delayed billing in these scenarios, the biller would need to make separate edits in the PMS and Elation to ensure both systems contain accurate billing data.

## **Who should use Delayed Billing?**

While the Delayed Billing setting is available to all practices, we only recommend using this setting if you are using [Elation Billing](Elation-Billing-All-in-One.md) (Elation's all-in-one billing solution) or when you are integrated with one of our Practice Management System (PMS) partners that support Delayed Billing. Today, practices that leverage Elation Billing, AdvancedMD, Candid, ConnxtMD, Kareo, or PracticeSuite can use the Delayed Billing feature.

If you have any questions about your specific PMS vendor, contact Support by clicking "I need help" -> "Contact Elation Support" from your Elation account and a member of the Support Team will be able to provide further guidance.

##

## **How to turn on Delayed Billing**

To turn on Delayed Billing for your practice, navigate to your Settings page and select "Billing Settings". From there, you can scroll to the bottom of the page where you will see a section titled Delayed Billing. Click on the toggle and move it to green to turn on Delayed Billing.

Turning on Delayed Billing will only impact *future* Visit Notes that are signed after you enabled this feature. When a bill does not have a “Billing Reference #” populated in [Billing Home](Billing-Home.md), that indicates that the bill has not been sent over to your PMS.

At any point, you can turn this feature off and all future Visit Notes that are signed will be sent straight to your PMS.

![]()

## **How to send bills to the PMS when Delayed Billing is enabled**

After turning on Delayed Billing, all future bills (or bills without a “Billing Reference #”) will be queued under [Billing Home](Billing-Home.md). You can navigate to Billing Home by clicking on "Reports" in the blue navigation bar and then selecting "Billing Home." From there, you will see all bills pending synchronization to your Practice Management System (PMS).

1. From the queue, you can click on the patient's name to access the visit note and make changes to the bill by click "Actions" >> "Edit Bill".
   - **Note**: Only the provider that signed the visit note or their authorized [billing delegates](staff-permissions--staff-delegates.md) can edit bills.

1. When you are ready to send all bills in the queue to your PMS, click on the Actions Menu ![]() next to the bill and select "Send to PMS" or [use the "Bulk Send"](Billing-Home.md#additional_settings) option

## **Frequently Asked Questions (FAQ)**

#### **Certain bills did not send, what should I do?**

Try the following troubleshooting steps:

1. Look at the bill and see if there is a number in the "Billing Ref #" field. If there is, it means your Practice Management System (PMS) received the bill and returned a corresponding billing reference number or claim number to Elation for reference. Use the search options in your PMS to look for this reference number or claim number to find your bill.
2. If you do not see "Billing Ref #"  and you cannot find the bill in your PMS, click the "Bill didn't send? Click here" button in [Billing Home](Billing-Home.md). You will be shown a list of bills that were not sent and you click "Resend" to try sending the bills again.

If you do not see the bill you are looking for in your PMS after trying the steps above, contact Support by clicking "I need help" -> "Contact Elation Support" from your Elation account and a member of the Support Team will be able to provide further guidance.

#### **Why can't I edit a specific bill?**

Only the provider that signed the visit note or their authorized [billing delegates](staff-permissions--staff-delegates.md) can edit bills.

#### **I turned on Delayed Billing but bills continue to go to the PMS after I sign my visit note. Why?**

While the Delayed Billing setting is available to all practices, we only recommend using this setting when you are using [Elation Billing](Elation-Billing-All-in-One.md) (Elation's all-in-one billing solution) or integrated with one of our Practice Management System (PMS) partners that support Delayed Billing. Today, practices that leverage [Elation Billing](Elation-Billing-All-in-One.md) or any of the following PMS partners can use the Delayed Billing feature:

- AdvancedMD
- Candid
- ConnxtMD
- Kareo
- PracticeSuite

If you have any questions about your specific PMS vendor, [please click here to contact Support](https://help.elationemr.com/s/contactsupport) or click "I need help" -> "Contact Elation Support" from your Elation account and a member of the Support Team will be able to provide further guidance.

## **Related Articles**

- [Billing Home Guide- A dashboard for managing your bills](Billing-Home.md)
- [Billing Guide- Setting up CPT Codes and Place of Service](billing-settings---service-locations--procedure-codes.md)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Billing Guide- Frequently Asked Questions](Billing-Guide-Frequently-Asked-Questions.md)
- [Elation Billing- Using Elation's all-in-one billing solution to manage your claims](Elation-Billing-All-in-One.md)
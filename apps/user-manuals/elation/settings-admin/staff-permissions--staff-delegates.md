# User Accounts Guide- Utilizing authorized staff delegates

Source: https://help.elationhealth.com/s/article/staff-permissions--staff-delegates

---

## ****Contents****

- [What are staff delegates?](#description)
- [Why are staff delegates useful?](#value)
- [Delegates Settings pages](#settings)
- [Provider-level delegates](#provider-level-delegates)
 - [Assigning Prescription delegates in Provider-level Settings](#provider-rx-delegates)
 - [Assigning Orders delegates in Provider-level Settings](#provider-orders-delegates)
 - [Assigning Billing delegates in Provider-level Settings](#provider-billing-delegates)
 - [Assigning Referrals delegates in Provider-level Settings](#provider-referrals-delegates)
 - [Removing delegate permissions in Provider-level Settings](#remove-provider-delegates)
- [Practice-level delegates](#practice-level-delegates)
 - [Assigning Prescription delegates in Practice-level Settings](#practice-rx-delegates)
 - [Assigning Orders delegates in Practice-level Settings](#practice-orders-delegates)
 - [Assigning Billing delegates in Practice-level Settings](#practice-billing-delegates)
 - [Assigning Referrals delegates in Practice-level Settings](#practice-referrals-delegates)
 - [Assigning Office Message delegates in Practice-level Settings](#practice-office-message-delegates)
 - [Removing delegate permissions in Practice-level Settings](#remove-practice-delegates)
- [Delegated actions](#views)
 - [Prescriptions](#rx_view)
 - [Orders](#order_view)
 - [Bills](#bills_view)
 - [Referrals](#referrals_view)
 - [Office Messages](#practice-office-message-delegates)
- [Frequently Asked Questions](#faq)

## ****What are staff delegates?****

In Elation, each [Provider Level User](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) can authorize individual [Staff Level Users](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) to execute prescriptions, orders, referrals, and edit billing information on their behalf. This permission is known as 'authorized staff delegates'.


## **Why are staff delegates useful?**

Staff delegates allow Provider Level Users to delegate permission to their staff members to take certain actions on their behalf to increase administrative efficiency while still complying to legal requirements.

**Important Note**: The 'authorized staff delegates' feature is mainly designed to allow [Staff Level Users](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) to assist [Provider Level Users](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) with completing certain Provider-specific actions in the EHR. If you choose to add another Provider Level User as a delegate, that Provider Level User will not be able to assign their own delegates or sign prescriptions, orders or referrals under their own name.



## **Delegates Settings pages**

There are two Settings for managing staff delegates:

- Provider-level
 - All [Provider Level Users](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) can assign Staff Level Users as delegates in their account-specific Authorized Staff Delegates settings page under the User Settings section. This means only Provider Level Users can adjust their own Provider-level delegate settings. Go to the [Provider-level delegates section](#provider-level-delegates) below to learn more about this Setting.
- Practice-level
 - This is an optional feature for Premium EHR users that can be turned on by Elation. To turn this feature on, have an [Admin Level User](https://help.elationemr.com/s/article/administrative-privileges) send a request to the Elation Support Team using the "I need help" -> "Contact Elation Support" option at the top of their Elation account and a member of the Support Team will assist you with turning this feature on.
 - Once this feature is turned on, a new Settings page will appear for [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) under the Admin Users Only section of the Settings page. Admin Level Users can use this setting to manage staff delegates on behalf of all Provider Level Users in the practice by assigning [User Groups](https://help.elationemr.com/s/article/user-groups) to the different delegate options. Go to the [Practice-level delegates section](#practice-level-delegates) below to learn more about this Setting.

## **Provider-level delegates**

### **Assigning Prescription delegates in Provider-level Settings**

As a Provider Level User, by authorizing individual Staff Level Users as an 'Authorized Rx Delegate'*,* you are allowing them to execute non-controlled substance prescription orders on your behalf in the EHR. These non-controlled substance prescription orders include:

- Transcribe prescription orders in the EMR and send a new non-controlled substance prescriptions electronically to the pharmacy on a provider's behalf.
- Transcribe verbal approval or denial of a non-controlled substance prescription refill or change request received from a pharmacy and send that approval or denial electronically to the pharmacy on provider's behalf.
- Transcribe provider's order to discontinue a non-controlled substance medication in the EHR for documentation purposes.
- Transcribe provider's order to cancel a non-controlled substance medication sent to a pharmacy.

**Important Note**: An 'Authorized Rx Delegate' **is not** allowed to ePrescribe controlled substance medications or address controlled substance medication script requests on a provider's behalf due to DEA regulations.



For Provider Level Users to assign prescription delegates to their own Provider Level User account:

1. Go to "Settings" -> "Provider Managed Delegates" (under User Settings)
2. Go to the Sign Prescriptions section
3. Click in the field that says **Add new rx delegate** under AUTHORIZED RX DELEGATES
4. Search for the name of the desired Staff Level User and click their name to add them as an 'Authorized Rx Delegate'

### **Assigning Orders delegates in Provider-level Settings**

As a Provider Level User, by authorizing individual Staff Level Users as an 'Authorized Orders Delegate'*,* you are allowing them to execute lab, imaging, cardiac, pulmonary and sleep orders on your behalf in the EHR. This permission includes:

- Drafting lab, imaging, cardiac, pulmonary and sleep orders on your behalf.
- Signing lab, imaging, cardiac, pulmonary and sleep orders on your behalf.
- Electronically sending lab orders on your behalf to lab vendors that support this functionality.


For Provider Level Users to assign orders delegates to their own Provider Level User account:

1. Go to "Settings" -> "Provider Managed Delegates" (under User Settings)
2. Go to the Sign Orders section
3. Click in the field that says **Add new order delegate** under AUTHORIZED ORDER DELEGATES
4. Search for the name of the desired Staff Level User and click their name to add them as an 'Authorized Order Delegate'

### **Assigning Billing delegates in Provider-level Settings**

As a Provider Level User, by authorizing individual Staff Level Users as an 'Authorized Billing Delegate'*,* you are allowing them to enter and/or update billing information in visit notes on your behalf in the EHR. This permission includes:

- Entering or editing billing information in visit note drafts.
- Editing billing information in signed visit notes.


For Provider Level Users to assign billing delegates to their own Provider Level User account:

1. Go to "Settings" -> "Provider Managed Delegates" (under User Settings)
2. Go to the Edit Signed Bills section
3. Click in the field that says **Add new bill delegate** under AUTHORIZED BILLING DELEGATES
4. Search for the name of the desired Staff Level User and click their name to add them as an 'Authorized Billing Delegate'

### **Assigning Referrals delegates in Provider-level Settings**

As a Provider Level User, the referrals delegate permissions you set will apply to all Staff Level Users in your practice and cannot be set for individual Staff Level Users. You can allow all Staff Level Users to sign and send referrals (the 'Referral' form in the EHR) on your behalf in the event of an emergency situation when you are not available OR you can block Staff Level Users from signing and sending any referrals.


For Provider Level Users to assign referrals delegates to their own Provider Level User account:

1. Go to "Settings" -> "Provider Managed Delegates" (under User Settings)
2. Go to the Edit and Send Referrals section
3. Select the permission you want all Staff Level Users to have:
   - Allow staff in my practice to execute a verbal order to sign and send referrals on my behalf. In the event of an emergency situation when I am not available, I authorize the staff in my practice to sign and send referrals on my behalf.
   - Allow staff to prepare referrals for me to sign, but do not allow staff to sign and send referrals on my behalf.


​​​​

### **Removing delegate permissions in Provider-level Settings**

Within any list of authorized delegates, click the "Remove" button next to the name of the individual whose delegate privileges you wish to revoke. Those individuals will no longer be able to take the corresponding delegate actions once they are removed from the delegates list.

![]()


​

## **Practice-level delegates**

**Important Notes**:

- Practice-level delegates allow [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) to assign specific User Groups as delegates for ALL Provider Level Users in the practice. Only [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) can adjust Practice-level delegate settings.
- This is an optional feature for Premium EHR users that can be turned on by Elation. To turn this feature on, have an [Admin Level User](https://help.elationemr.com/s/article/administrative-privileges) send a request to the Elation Support Team using the "I need help" -> "Contact Elation Support" option at the top of their Elation account and a member of the Support Team will assist you with turning this feature on.
- The 'authorized staff delegates' feature is mainly designed to allow [Staff Level Users](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) to assist [Provider Level Users](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges) with completing certain Provider-specific actions in the EHR. If you choose to add Provider Level Users as delegates (especially if there are Provider Level Users in the User Group you select), those Provider Level Users will not be able to sign prescriptions, orders or referrals under their own name.

### **Assigning Prescription delegates in Practice-level Settings**

By authorizing specific [User Groups](https://help.elationemr.com/s/article/user-groups) as prescription delegates*,* you are allowing all members of that User Group to execute non-controlled substance prescription orders on behalf of all Provider Level Users in the EHR. These non-controlled substance prescription orders include:

- Transcribe prescription orders in the EMR and send a new non-controlled substance prescriptions electronically to the pharmacy on behalf of all Provider Level Users.
- Transcribe verbal approval or denial of a non-controlled substance prescription refill or change request received from a pharmacy and send that approval or denial electronically to the pharmacy on behalf of all Provider Level Users.
- Transcribe orders to discontinue a non-controlled substance medication in the EHR for documentation purposes on behalf of all Provider Level Users.
- Transcribe orders to cancel a non-controlled substance medication sent to a pharmacy on behalf of all Provider Level Users.

**Important Note**: An 'Authorized Rx Delegate' **is not** allowed to ePrescribe controlled substance medications or address controlled substance medication script requests on a provider's behalf due to DEA regulations.


To assign prescription delegates for all Provider Level User accounts:

1. Admin Level Users would go to "Settings" -> "Admin Managed Delegates" (under Admin User Only)
2. Go to the Sign Prescriptions section
3. Click "+ Add Delegates"
4. Search for the name of the desired [User Group](https://help.elationemr.com/s/article/user-groups) and click their name to add all users in that User Group as prescription delegates

### **Assigning Orders delegates in Practice-level Settings**

By authorizing specific [User Groups](https://help.elationemr.com/s/article/user-groups) as orders delegates*,* you are allowing all members of that User Group to execute lab, imaging, cardiac, pulmonary and sleep orders behalf of all Provider Level Users in the EHR. This permission includes:

- Drafting lab, imaging, cardiac, pulmonary and sleep orders on behalf of all Provider Level Users.
- Signing lab, imaging, cardiac, pulmonary and sleep orders on behalf of all Provider Level Users.
- Electronically sending lab orders on behalf of all Provider Level Users to lab vendors that support this functionality.


To assign orders delegates for all Provider Level User accounts:

1. Admin Level Users would go to "Settings" -> "Admin Managed Delegates" (under Admin User Only)
2. Go to the Sign Orders section
3. Click "+ Add Delegates"
4. Search for the name of the desired [User Group](https://help.elationemr.com/s/article/user-groups) and click their name to add all users in that User Group as orders delegates

### **Assigning Billing delegates in Practice-level Settings**

By authorizing specific [User Groups](https://help.elationemr.com/s/article/user-groups) as billing delegates*,* you are allowing all members of that User Group to enter and/or update billing information in visit notes on behalf of all Provider Level Users in the EHR. This permission includes:

- Entering or editing billing information in visit note drafts on behalf of all Provider Level Users in the EHR.
- Editing billing information in signed visit notes on behalf of all Provider Level Users in the EHR.


To assign billing delegates for all Provider Level User accounts:

1. Admin Level Users would go to "Settings" -> "Admin Managed Delegates" (under Admin User Only)
2. Go to the Edit Signed Bills section
3. Click "+ Add Delegates"
4. Search for the name of the desired [User Group](https://help.elationemr.com/s/article/user-groups) and click their name to add all users in that User Group as billing delegates

### **Assigning Referrals delegates in Practice-level Settings**

By authorizing specific [User Groups](https://help.elationemr.com/s/article/user-groups) as referrals delegates*,* you are allowing all members of that User Group to execute referral orders on behalf of all Provider Level Users in the EHR. This permission includes:

- Drafting referral orders on behalf of all Provider Level Users.
- Signing and/or sending referral orders on behalf of all Provider Level Users.


To assign referrals delegates for all Provider Level User accounts:

1. Admin Level Users would go to "Settings" -> "Admin Managed Delegates" (under Admin User Only)
2. Go to the Sign Referrals section
3. Click "+ Add Delegates"
4. Search for the name of the desired [User Group](https://help.elationemr.com/s/article/user-groups) and click their name to add all users in that User Group as referrals delegates

### **Assigning Office Messages delegates in Practice-level Settings**

By authorizing specific [User Groups](https://help.elationemr.com/s/article/user-groups) as office message delegates*,* you are allowing all members of that User Group to sign Office Messages on behalf of all Provider Level Users in the EHR.

To assign office message delegates for all Provider Level User accounts:

1. Admin Level Users would go to "Settings" -> "Admin Managed Delegates" (under Admin User Only)
2. Go to the Sign Office Messages section
3. Click "+ Add Delegates"
4. Search for the name of the desired [User Group](https://help.elationemr.com/s/article/user-groups) and click their name to add all users in that User Group as office message delegates



​​​​

### **Removing delegate permissions in Practice-level Settings**

Within any list of authorized delegates, click the "X" button next to the name of the User Group you wish to revoke to remove all members of that User Group from being delegates. Members of removed User Groups will no longer be able to take the corresponding delegate actions once they are removed from the delegates list.

- **Important Note**: If a Staff Level User is removed from the [Practice-level delegate](#practice-level-delegates) settings but they are still assigned as a [Provider-level delegate](#provider-level-delegates) then they will still be able to take the delegated action.

## **Delegated actions**

### **Prescriptions**

When prescription delegates draft a prescription, they will see a dropdown at the top of the Prescription Form called "Prescribing on behalf of" that lists the names of all of the Provider Level Users they are delegates for. Once a delegate prescribes on behalf of a Provider Level User, the prescription in the chart will have the following text: *Signed for: [provider's full name] by [delegate's full name]*.

### **Orders**

When orders delegates draft a lab, imaging, cardiac, pulmonary or sleep order, they will see options to "Print on behalf of physician" or "Sign on behalf of physician" at the bottom of the order form. If the individual is a delegate for multiple Provider Level Users, an additional window will appear after they click "Print..." or "Sign..." to select which Provider Level User they want to order on behalf of. The signed order itself will also specify that a delegate signed on behalf of a Provider Level User and will have the following text: *Signed off for [provider's full name] by [delegate's full name]*.

![]()

### **Bills**

Billing delegates will see the "Edit Bills" option when they click the "Actions" button in signed visit notes for any Provider Level Users whom they are a billing delegate for. This option gives billing delegates the ability to edit any billing information for any signed visit note for Provider Level Users whom they are a billing delegates for.


### **Referrals**

When referrals delegates draft a referral, they will see an option called "On Behalf Of" on the Referral form where they can select which Provider Level User they are signing referrals for. The signed referral itself will also specify that a delegate signed on behalf of a Provider Level Users and will have the following text: *Signed off for [provider's full name] by [delegate's full name]*.

![]()

### **Office Messages**

When office message delegates look at office message threads that have Provider Level Users as recipients, they will see a "Sign Off" button that allows office message delegates to sign off office message threads on behalf of Provider Level Users.



## **Frequently Asked Questions (FAQ)**

#### **How do I make myself a delegate for a provider?**

Only Provider Level Users themselves can adjust their own [Provider-level delegate](#provider-level-delegates) settings by logging in to their own Elation EHR account and going to the Authorized Staff Delegates settings page (under User Settings). No one else can adjust a Provider Level User's delegate settings.


#### **I do not see the option to sign a prescription, order or referral for a provider. Why?**

If you do not see the option to sign a prescription, order or referral for a provider, it means the provider has not added you as a delegate for that feature. Have the provider [add you as a delegate](#provider-level-delegates) and then reload the chart you are in and then you will see the sign options.


#### **I do not see the option to edit a bill. Why?**

If you do not see the option to edit a bill, it means the provider has not added you as a [billing delegate](#provider-billing-delegates). Have the provider as you as a billing delegate, reload the chart you are in and then you will the "Edit Bill" option in the "Actions" dropdown for the provider's visit notes.


#### **I do not see a provider's name in the "behalf of..." dropdown. Why?**

If you do not see a provider's name in the "behalf of..." dropdown it means the provider has not added you as a delegate for that feature. Have the provider [add you as a delegate](#provider-level-delegates) and then reload the chart you are in and then you will see their name in the dropdown.


#### **I am a provider but I only see options to sign on behalf of another provider. Why?**

If you are a Provider Level User but you only see the option to sign on behalf of another Provider Level User, this means that Provider Level User added you as a delegate. Please have the other Provider Level User remove your name from their delegate list(s) and then your actions will return to normal once you reload the chart.


#### **I do not see the option to assign Office Message delegates under my Provider Managed Delegates setting. Why?**

Office Message delegates is a setting that is only available for [Practice-level delegates](#practice-level-delegates).

#### **What happens if I set Practice-level delegates for providers who already chose their own Provider-level delegates?**

If you set Practice-level delegates for providers who already chose their own Provider-level delegates then both sets of settings will be applied for those Provider Level Users.

- If a Staff Level User is removed from the [Practice-level delegate](#practice-level-delegates) settings but they are still assigned as a [Provider-level delegate](#provider-level-delegates) then they will still be able to take the delegated action.
- If a Staff Level User is removed from the [Provider-level delegate](#provider-level-delegates) settings but they are still assigned as a [Practice-level delegate](#practice-level-delegates) then they will still be able to take the delegated action.




## **Related Articles**

- [Prescription Form Guide- ePrescribing & Ordering Medications](/s/article/eprescribing-and-ordering-medications-with-the-upgraded-rx-form)
- [Order Forms Introduction- Ordering medical tests for your patients](Order-Forms-Introduction-Ordering-medical-tests-for-your-patients.md)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Letters & Referrals Introduction- Sharing clinical data outside of Elation](letter-and-referral-introduction.md)
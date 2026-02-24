# Salesforce

Create or link to issues from cases. Linear's Salesforce integration is available as an add-on to our Enterprise plan.

![Linear x Salesforce cover image](https://webassets.linear.app/images/ornj730p/production/e54e48e34eec77b4dea1a1d51eda7e1bec5bdfcb-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Salesforce users—whether or not they use Linear—can link cases to existing issues and projects or create new issues using a Linear template.

Real-time updates ensure Salesforce users stay informed of issue/project status and priority changes as they happen, streamlining collaboration between teams.

## Configure

### Contact us

Please reach out to [sales@linear.app](mailto:sales@linear.app) to purchase licenses for this integration. Once purchased, assign them to Salesforce users to enable them to access the integration.

### Configure from Salesforce App Exchange

1. Install the Linear integration from the Salesforce Marketplace
2. Find the **Linear Development** app in the Salesforce **App Launcher**. In order to see this app in the menu launcher, you must have been granted a licence to use this integration. 
3. Click **Login with Linear**
4. Select the Linear workspace you want to connect
5. Confirm the integration between Salesforce and Linear

### Configure from Linear

1. Navigate to **Settings > Integrations > Salesforce**
2. Click **Enable**
3. Copy the URL from any page in your Salesforce installation
4. Paste the URL in the modal in Linear settings

### Enable the Linear component

1. Navigate to a case detail page (commonly in Service Cloud or Support Cloud)
2. Edit the case detail page
3. Find Linear in the list of custom components
4. Place the component in the location of your choice on the page

### Linear x Salesforce integration configuration video

Watch a video overview of how to set up the Salesforce integration.

![Watch on YouTube](https://www.youtube.com/watch?v=hHgd5oY73pU)

---

## Permissions

Three permission sets will become available in Salesforce:

Role | Function
--- | ---
Linear Admin | Has admin permissions in Linear and allows full access and configuration rights
Linear Create Issues | Can create and/or link issues and/or projects
Linear Link Only |  Can only link existing issues. This is useful for large support teams who want more control over issues being created in order to limit noise in Linear.

---

## Settings

### Restrict issue visibility

Once enabled, only Linear issues that were created from or previously linked to Salesforce can be found when searching from the Linear component. This allows teams with privacy concerns to reduce the scope of visible issues in the Salesforce workspace.

### Internal notes

Automatically notify your team in Salesforce when an issue linked to a case has been completed to cancelled. Changes will be added to the _All updates_ section of a case.

### Automatic case reopening

When the linked Linear issue is completed or canceled, you can automate reopening the case to the case status of your choice. This signals your team to follow up with customers.

Case statuses are customizable. If a new case status is added, visiting the Salesforce integration's page in Linear settings will reflect the addition.

### Templates

Once a template has been created in Linear, click the **+** icon to make a template available to Salesforce.

---

### Mapping attributes from Salesforce to Linear

When [Customer Requests](https://linear.app/docs/customer-requests) is enabled, creating issues from a Salesforce case will create new Customers in Linear as needed. The customer request added to the created issue contains the case description.

Customers support attributes you can use to group, order, and filter for data in Linear. For example, filter issues by the tier of the Customer who requested them, order projects by the associated sum of attributed customer revenue, and more. To bring this data into Linear from Salesforce, set the desired mapping between Salesforce account properties and Customer attributes in Linear in **Settings > Customer Requests**. 

You can set mappings with any property you use on Salesforce accounts, as long as the data type is allowable:

Customer attribute | Allowed data type
--- | ---
Owner | String (email address)
Tier | String
Status | String
Revenue | Number
Size | Number

If you're using lookup fields in Salesforce and wish to map to these in Linear, consider using formula fields as described in the FAQ.

## Using the integration

### Create a new issue

1. From a case's details, click **Create issue**
2. Select a template. All issues created by this integration use templates to drive consistency.
3. Include a title
4. Write a new issue description, or turn on the **Include case description** toggle to automatically insert the case description into the Linear issue description. The case description will appear in Linear as the Customer Request attached to the issue.

### Link cases to existing issues or projects

1. Click **Link issue or project** (_depending on permission levels_)
2. Search for the issue or project and confirm

### Link to cases from Linear

You can also link a Linear issue to a case by pasting the case's URL into the Linear issue as a link attachment with `Control `+` L`.

---

## Synced details

### Status and priority

When an issue is linked to a case, a reference to that issue appears in the Salesforce integration. The linked issue's status and priority are always current.

### User account attribution

If a Salesforce user is also a Linear user, their name will be displayed as the issue creator in relevant issue activity sections. If the user does not have a Linear account, the issue creator displays as “User User” (the name of the Salesforce developer account) and the email of the Salesforce user who created or linked the issue.

### Customer information

Linear syncs customer information from the Salesforce workspace. Modify attribute mapping as discussed in _Mapping attributes_ above.

---

## Triage rules

Using the Salesforce integration concurrently with [Triage rules](https://linear.app/docs/triage#triage-routing) offers tools to direct how issues are routed after they're created from Salesforce. You can create rule conditions using properties of the Salesforce Case specifically, along with the normal set of filterable issue data in Linear. Triage rules can set an issue's team, status, assignee, label, project, and priority.

![a triage rule triggered by case origin and priority support](https://webassets.linear.app/images/ornj730p/production/7fee4c6a541d375ee392532d1bb0df893fcd9b49-1788x644.png?q=95&auto=format&dpr=2)



## FAQ

<details>
<summary>What happens when an issue linked to a case is closed as a duplicate in Linear?</summary>
The case will reopen in Salesforce as the linked issue has been canceled. We do not merge Salesforce cases. If desired you may link the reopened case to the canonical issue and re-close the case.
</details>

<details>
<summary>How can Salesforce formula fields make more properties available for mapping? </summary>
Suppose in Salesforce you have a field called "account owner"; an owner ID with a lookup to the user email. This would not work by default in our attribute mapping, as the owner field in Linear requires an email address.

You can work around this by using a formula field. To do so, create a new custom field of type formula. Clicking into "Advanced Formula" will help you build the formula you need. 

![new custom field of type formula in Salesforce](https://webassets.linear.app/images/ornj730p/production/5fbd8928154f911eee5dc3c339f314a85b5c822b-1198x822.png?q=95&auto=format&dpr=2)

In this scenario, a formula field for account.owner returning an email address can be used to map between Linear's Customer owner and the necessary value in Salesforce.
</details>

<details>
<summary>Can I use SOQL to query Linear data?</summary>
Linear data living inside of Salesforce (like which customers have the most issues created from within Salesforce) can be queried directly with SOQL. This can be used to run analyses like returning issues linked to cases, or building custom dashboards within Salesforce.
</details>

<details>
<summary>Can I filter issues by their Salesforce case data in Linear views?</summary>
Yes, you can filter issues in views in Linear under the filter sub-menu _Salesforce case properties._ Salesforce properties are not supported in Insights or Dashboards.
</details>

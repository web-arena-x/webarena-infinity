# Jira

Enable Jira Sync while trialing or transitioning to Linear to keep Jira spaces up to date.

> [!NOTE]
> For pre-existing issues, you can complete a one-time import from Jira to Linear, use the CSV or API credential options in our [importer](https://linear.app/docs/import-issues#jira).   
>   
> Imported issues and projects import as synced only if the Jira integration is [configured](https://linear.app/docs/jira#configure) prior to completing your import. Switching from another tool? [Follow our manual.](https://linear.app/switch)

![Linear and Jira logos](https://webassets.linear.app/images/ornj730p/production/adbef6f35402b94c3522a0f38ac578573dcb6f57-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Some companies choose to [import issues and projects](https://linear.app/docs/import-issues#jira) and switch to Linear immediately; others prefer to trial Linear on a small team first or need some time to make the full transition. For the latter cases, we built Jira Sync. 

This feature allows you to connect Jira spaces to Linear teams, so that new issues and projects created in Jira or Linear are kept current in both places.

## Permissions

The user creating the API token to enable Jira Sync must have the ADMINISTER [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) in Jira. This is necessary for Linear to install the required webhooks. It is possible to remove the global ADMINISTER permission after the setup is complete without impacting this integration. 

If the ADMINISTER holder does not have a Linear seat or does not want this permission stored in Linear, please see the FAQ.

### Jira Cloud

Create an API key for this user by following instructions [here](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/). The default token expiry is one week, please choose to enable for a year instead.

### Jira Server

API keys might not be available. Instead, you need to create a personal access token (or PAT). Instructions can be found [here](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html). The default token expiry is one week, please choose to enable for a year instead.

#### Posting in a synced thread

In order to send a reply to a synced thread, you'll need to link your Atlassian account first.

<details>
<summary>Individual permissions requested in OAuth consent screen</summary>
Permission | What we use it for
--- | ---
User → View → me | We use this to capture the Jira Account ID of each user. This allows us to properly map users between Linear and Jira
User → View → me | This allows us to create issues and comments on behalf of the user. This does not grant access to read issues or comments not created by this user.

Jira Server users will be presented with a simple form to input their own personal access token.

![OAuth consent screen for Jira Sync](https://webassets.linear.app/images/ornj730p/production/f6d920cbe88216b212e34342426a83e1a16dbae7-1196x1270.png?q=95&auto=format&dpr=2)
</details>

## Configure

Enable the integration in Linear from [workspace settings](https://linear.app/settings/integrations) under _Workspace > Integrations > Jira_.

Enter your personal access token (see Permissions > Setup above), email address and installation or cloud hostname and then select which Jira space to link to which Linear team. For the installation or cloud hostname, remember to remove the `http://` and anything after `.net`.

For best performance, users should link their individual Jira accounts in Settings > Integrations > Jira > Connect personal account. This allows better handling of fields in Jira like Assignee and Creator.

## Basics

### Select Jira Spaces

We've set up the integration so that Jira spaces map to teams in Linear.   
  
You can link each Jira space to only a single team in Linear, so the same space cannot create issues in multiple Linear teams. Multiple Jira spaces can be linked to the same Linear team though and issues will be created in Linear from any connected Jira space. 

### Relationship to Jira Imports

Running a Jira import will not automatically import issues as synced _unless_ you've configured the Jira integration prior to the import. You do not need to create the space/team mappings prior to importing. For full instructions about importing issues as synced, please see our [Importer](https://linear.app/docs/import-issues#import-and-sync-with-jira) documentation.

### Synced properties

Once the integration is enabled, any new issue created in a linked Jira space or Linear team will create a synced version of that issue in the other service.

Jira epics automatically sync as Linear projects, maintaining parent-child relationships between issues and their projects/epics.

#### Issues:

Name in Linear | Name in Jira
--- | ---
Title | Title
Description | Description
Assignee*  | Assignee* 
Creator*  | Creator/Reporter* 
Priority | Priority
Status** | Status**
Labels*** | Labels***
Due date | Due date

### Epics/Projects:

Name in Linear | Name in Jira
--- | ---
Project title | Epic title
Project status | Epic status
Project labels*** | Epic labels***
Project priority | Epic priority
Project description | Epic description
Project lead* | Epic assignee*

<details>
<summary>Special cases</summary>
* For these fields to sync successfully, the relevant user must connect their Jira account to Linear in Settings > Integrations > Jira > Connect personal account. If no connection exists, the Assignee field will be unassigned, and/or the creator field will be the user who configured Jira.

** Deleting a synced issue in either Jira or Linear will not delete the issue in the other direction, or otherwise affect status in the synced issue.

If a synced issue in Jira moves to a status not in Linear, The Linear issue's status will not update. The status will update in Linear if the synced issue is moved in Jira to a status that can be mapped properly, or if the status is changed in Linear directly.

*** For labels to sync from Jira to Linear, the label must have already been created in Linear (either through a previous import, or by creating the label manually or through our GraphQL API. When labels sync from Linear to Jira, we'll create a new label in Jira when appropriate.
</details>

### Sync directionality

When configuring the mapping between a Jira space and a Linear team, you have the choice of syncing uni-directionally or bi-directionally.

When syncing uni-directionally, issues created in Jira are also created in Linear. Changes made to that issue from Jira are synced to Linear, but changes made in Linear do not sync back to Jira. 

When syncing bi-directionally, creating an issue in either service will create a synced copy in the other. Updating the synced copy in either service will sync changes back to the other issue.

### Sync banners

Once an issue or project is synced between Jira and Linear, a banner will appear at the top of the issue to make this clear. The banners will display information to show current sync status or will surface any errors with syncing.

![Jira synced issue banner](https://webassets.linear.app/images/ornj730p/production/08bd834bb5c1c5ae41ac68192a284a82363690f7-2874x150.png?q=95&auto=format&dpr=2)

### Limitations

There are a number of features in Jira that Linear has chosen not to pursue as a matter of product philosophy. These discrepancies are worth noting, as they will affect sync. Among these are Issue Type, Constraints, Components, and Required fields. Read more about how these differences are handled by sync below.

<details>
<summary>Required fields</summary>
If a Jira project's workflow demands required fields, we will not create the synced issue or project in Linear. In the case where an issue has been created in Linear before required fields are enforced in Jira, we'll send an error to the Linear issue as a comment to surface the problem.
</details>

<details>
<summary>Issue type</summary>
Issue type is a native required field in Jira. Bug, Story, Epic and Task are common issue types. When you create a new issue in Linear and we create a synced issue in Jira, it will be type _Task_ if we find that type in Jira. 

If this type has been deleted, we'll fallback to the first type on the list. If issues created in Linear are created in Jira as _Story_ for instance, you may wish to create a type _Task_ so that future issues created in Linear will display appropriately.
</details>

<details>
<summary>Constraints</summary>
You may have constraints in Jira that prevent certain updates to a Jira issue   until various conditions are met.

If you update a synced Linear issue in a way that violates Jira constraint, the Linear issue will update but the Jira issue will not.
</details>

<details>
<summary>Components</summary>
In a synced Linear issue or project, components appear as labels - "Component: Engineering" for instance. These labels cannot be grouped or deleted. Removing a component label from an issue in Linear will remove the component in the synced Jira issue.
</details>

<details>
<summary>Hierarchy Limitations</summary>
Linear and Jira have different restrictions for issue and project hierarchy that can lead to discrepancies. If you remove a parent relationship (Project > Issue > Sub-issue) in Linear that would violate Jira's hierarchy constraints (Epic > Story/Bug/Task > Sub-issue), the sync may fail or show discrepancies.
</details>

### Issue filter

By default, Jira Sync will create and sync every issue that’s created in the mapped Jira space. If you wish to filter out some issues, you have the ability to do so by editing the webhook in Jira. 

Please note that any JQL filters you applied to limit the scope of _import_ do not apply for Jira Sync purposes. In order to change what is provided to Linear for Jira Sync, follow the instructions below:

Go to `Settings` → `System` → `Advanced` → `Webhooks`. Select the Linear webhook and click `Edit`.

The `Issue related events` box allows you to provide a custom JQL query to filter out some issues that you do not want to sync with Linear. This works both when the conditions are met at the time of the Jira issue's creation, as well as if the Jira issue is updated to meet the parameters of your filter later.

Here is an example to only sync issues with the label `Bug`:

![image of editing a webhook in Jira to restrict returned results](https://webassets.linear.app/images/ornj730p/production/82c1152a9b627e4b7ebf326122e3dc08a9deea5c-2096x316.png?q=95&auto=format&dpr=2)

### Pre-existing content in Jira

Once configured, Jira Sync will create issues and projects in Linear when issues and epics are created in a synced Jira space. Issues belonging to that synced space from before the sync was configured will not create issues in Linear.

However, when those older issues and epics receive updates in Jira, the updates will prompt those issues to be created and synced in Linear. 

### FAQ

<details>
<summary>Can I sync all tickets in Jira with a Linear team?</summary>
Jira Sync is a forward looking integration -- it will create new issues in Linear or Jira when a new issue is created in a synced context in either service. 

If you'd like to import your Jira issues as synced, please follow the steps [here](https://linear.app/docs/import-issues#import-and-sync-with-jira).
</details>

<details>
<summary>Does Linear become aware of updates to synced Jira space metadata?</summary>
If you change metadata in synced Jira spaces (delete, add, make them unrequired) this may cause the Jira issue and Linear issue to become out of sync. 

Clicking the refresh button on the list of synced Jira spaces in Linear settings will update the list of available spaces, but also update the metadata to Linear's context. This is a fix forward; issues already out of sync because of missing metadata will not update after pressing this. 





![Showing the refresh button in the Jira integration to account for new Jira metadata](https://webassets.linear.app/images/ornj730p/production/028551dbcc69612f31c12505703eedd684a6c3d9-819x469.png?q=95&auto=format&dpr=2)
</details>

<details>
<summary>Will issues created by import from another service sync with Jira?</summary>
No, Issues imported to Linear in general will not create a synced copy in Jira. The specific exception to this is if you set up a synced Jira project in Linear and import from that Jira project to Linear.

Other imports outside of this will not create synced issues in Jira.
</details>

<details>
<summary>Can I send Linear tickets created by Jira to Triage? </summary>
You may wish to triage Linear issues created by Jira instead of syncing their status automatically (for example, you may want the opportunity to decline the issue before admitting it to your backlog).



While this integration is broadly intended to keep Jira and Linear issues in sync, you can workaround this by renaming your first status under type _Started_ something besides To do, to-do or similar variants. When the integration can't determine the right status at issue creation, it falls back to Triage. In other words, if your first started status is called "Started" in Linear and "To do" in Jira, new issues created by Jira in Linear will go to Triage.
</details>

<details>
<summary>Will moving a Jira issue from an unsynced space to a synced space create a Linear issue?</summary>
Yes, a Linear issue will be created when a Jira issue is moved into a synced space.
</details>

<details>
<summary>Will moving a Linear issue from an unsynced team to a bidirectionally synced team create a Linear issue?</summary>
No, a Jira issue will not be created when a Linear issue is moved from one team to another. This will only work when an issue is created directly in the Linear Team.
</details>

<details>
<summary>How can I set up Jira Sync without a Linear admin having ADMINISTER permissions in Jira?</summary>
This integration may also be setup with the webhook option. The actor who configures the webhook must still have ADMINISTER, but this can be done between two people synchronously -- A Jira ADMINISTER holder without a Linear seat, and a Linear admin with BROWSE PROJECTS permissions.



To do this, the Linear actor would choose the "Manual Webhook" option in Linear > Settings > Integrations > Jira

![shows the webhook option when enabling jira sync](https://webassets.linear.app/images/ornj730p/production/bbfe85dd0e58a3f01b7642dc0c3d653fccf8eb16-516x243.png?q=95&auto=format&dpr=2)

Then, the same person can fill this section:

![Picture of the form asking for API token, Jira account email address and jira hostname](https://webassets.linear.app/images/ornj730p/production/b10ac5161fcb397d860c4e6fa15238ed3f0d6c75-487x414.png?q=95&auto=format&dpr=2)

On submission, they'll be presented with this form. They can then share the webhook URL and these instructions with the Jira ADMINISTER holder, who can setup the webhook in Jira directly:  


![jira webhook form in Linear](https://webassets.linear.app/images/ornj730p/production/b2c81982922bb2ccefd750b2fcf17adda6acc7c3-485x584.png?q=95&auto=format&dpr=2)

After the webhook is setup, the Jira actor can securely share the webhook secret (through something like 1Password) to the Linear admin, who can input it where prompted and click Save. Any Linear admin can then manage the integration from within Linear.
</details>

<details>
<summary>My issues are showing a sync or permissions error</summary>
Viewing the sync error will tell you more specific information about the root cause of the sync error. This can typically occur in cases where an issue is missing on Jira or your permissions are not configured correctly.   


For permissions errors, using Jira's permissions helper can shed light on where the error lies. 

![Jira permission helper](https://webassets.linear.app/images/ornj730p/production/1b0faa06c89c3759263aa68f59d4e584de22eba8-633x344.png?q=95&auto=format&dpr=2)

Fill the values to:

* ​**User**​: This should be set to the user who created the Jira Sync integration (you can check this in Linear in Settings > Integrations > Jira > Enabled by)
* ​**Issue**​: Even though we are looking to check permissions to create new issues, the form requires us to pick an issue to check against. Choose any issue.
* **Permission:**​ Choose `Create issues`. Then click submit and look for a status in the blue box, it should tell if that user has access to this permission on this project. If not, the details below should contain some clues about what's missing.
</details>

<details>
<summary>Do Linear Sub-teams work with Jira Sync? </summary>
[Sub-teams](https://linear.app/docs/sub-teams) are not considered when mapping Jira spaces and Linear teams. 

If a parent team is linked to Jira bidirectionally, issues created in that parent team will be created in Jira. Issues created in its sub-teams will not be created in the linked Jira team. 

The sub-teams themselves may be linked individually to Jira spaces however, and this will work independent of the parent team's sync settings.
</details>

<details>
<summary>Do epics that were previously imported or synced as issues automatically sync as projects? </summary>
No. Epics that were previously imported as projects or synced as issues will not retroactively sync as projects. Only newly created epics (after bi-directional sync is enabled) will sync as Linear projects going forward.
</details>

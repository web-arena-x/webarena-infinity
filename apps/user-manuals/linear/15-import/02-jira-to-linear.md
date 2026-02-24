# Importing from Jira

Import Jira projects as Linear teams. 

![Linear and Jira logos](https://webassets.linear.app/images/ornj730p/production/a17831abc8fd10fcaf646b82bb160769fa68e7e2-2880x1620.png?q=95&auto=format&dpr=2)

## Data included in the import

We import data from Jira that matches a concept in Linear, and make some adaptations for other fields specified below:

Jira | Linear
--- | ---
Summary | Title
Description | Converted into markdown and used as issue description
Assignee | Assignee (best effort match)
Creator | Creator (best effort match)
Priority | Priority
Issue Key | Used in backlink, or matched (see article)
Issue type | Label (new label will be created on import if no exact match exists in Linear)
Type | Label (team-level)
Epic | Project
Comments | Comments
Estimate | Estimate
Due date | Due date
Created date | Created date
Parent/Child | Parent/sub-issue
Label | Label
Status | Status (best effort conversion)
Images (inline, in comments, or attached to task) | Image files
Non-image files | Imported as URLs pointing back to original file in Jira
Components | Labels (team-level)

> [!NOTE]
> Please note that data not included above like custom fields will not import to Linear. API credentials must be provided at time of import in order to fetch files.

## What import method should I choose?

Import type | Pros | Cons
--- | --- | ---
API imports | Retains the most data, and permits use of Jira Sync functionality if enabled at the end of the import. | Requires Admin permissions in the source Jira project
CSV imports | Doesn't require high permissions in Jira to initiate, can be used to import many Jira projects at once if you don't need issue ID matching | Jira sync functionality is not supported

**Both options** will automatically label imported issues with "Migrated," are easily deletable within 7 days from Linear's Import/Export settings, and can support matching issue IDs.

You can also import through our CLI tool, but we don't recommend this for Jira as it doesn't import as much data, does not label imported issues and is not easily deletable if you wish to restart.

## Considerations before importing

There are functionalities offered when importing from Jira that you may wish to know about in advance, as they'll affect decisions you make before or during your import

### Syncing changes back to Jira

If your individual team is moving to Linear and your broader organization is still using Jira, Jira sync can help reflect your team's work in Linear back in your Jira instance. 

#### API credential imports

To import issues from Jira as synced, make sure the Jira integration is configured before completing your first import. If you plan to create a new team  for your imported issues during the import (which will also allow matching Jira issue keys in Linear), you don't need to preconfigure team/project mappings in the Jira integration before importing.

During the import, ensure _Sync issues after import_ in selected when prompted.

#### CSV imports

Unfortunately, issues imported from CSV cannot be synced with Jira, and will only appear as static copies of the issues at the time of import. 

A link to the Jira issue will show in Linear so you can click through and check for updates, but changes in Jira or Linear will not be synced with this import type.

API-based import is recommended if you need to maintain a sync after import.

This sync feature will keep most [properties](https://linear.app/docs/jira#synced-properties) aligned between the original issue or epic in Jira, and the imported issue or project in Linear. Optionally, choose to enable bi-directional sync so that issues and epics created in Linear will also sync to Jira (otherwise, only issues and epics created in Jira will sync to Linear.) 

For best performance in syncing fields like assignee and creator, individual Linear users should also connect their personal Jira accounts to Linear in integration [settings](https://linear.app/settings/integrations/jira) prior to import as well. Please see the Mapping Jira users section for more information on this.

> [!NOTE]
> Please see our Jira [documentation](https://linear.app/docs/jira) for more information about Jira Sync

### Mapping Jira users to Linear

The importer will attempt to match existing users in Linear to those you're importing from Jira. The optimal case is for users to already exist in both Jira and Linear with the same email address, and to have linked their Jira accounts in Settings > Integrations > Jira. 

That said, often this is not the case in practice.

1. **If a user is not yet in Linear, but has a valid email address in Jira:** User will be treated as an external user and will be attributed as **author** of issues and comments, but not as the assignee
2. **User's email address is unavailable:** We cannot match these users. But if the user links their Linear and Jira accounts in Settings > Integrations > Jira **and** if the import is re-run, we might have a match.

Regardless of the scenario, re-running the import after users have joined will always help matching more users.

### Matching Jira IDs in Linear

It's possible to have your issue IDs in Jira match in Linear (i.e. ENG-1 in Jira can be ENG-1 in Linear.)

#### API credential imports

During the import process you are offered the choice between importing to an existing team or creating a new team to hold your imported data. The former will will match your IDs. You can also choose to import to an existing team with 0 issues. Importing to an existing team that has issues will not match your IDs.

In both cases, you must also check the boxes to import closed/done/archived issues for proper issue number matching.

#### CSV imports

The CSV file must only contain issues from a single Jira project (otherwise, keys could contain conflicting numbers.) You must also be importing to a new team in Linear or an existing team with no issues.

### Sub-teams

You cannot import from a Jira project to a sub-team directly. If you wish to take this action, import to an existing (or create a new) top-level Linear team first, then [convert it to a sub-team](https://linear.app/docs/sub-teams#update-an-existing-team-to-a-sub-team) afterwards.

### Running the import

When you're ready to import, you can do so by heading to Linear's Import/Export settings. Please note that you must be a Linear Admin to run an import. 

If you run into issues or need further assistance, please let us know at [support@linear.app](mailto:support@linear.app).

#### API credential imports

1. Enter your personal access token (obtained from your [Atlassian settings](https://id.atlassian.com/manage-profile/security/api-tokens)).
2. Enter your project key
3. Enter your email address you use for your Jira account.
4. Enter your installation or cloud hostname. Remember to remove the `http://` and anything following `.net`.
5. Optionally, set a JQL filter to limit the scope of imported data. Please note that this applies only to the import, the filter will not apply to the Jira integration that supports bidirectional sync
6. Select or create a Linear team to receive the imported data
7. Click **Next**

You will then be guided through configuration options during the import process. You will have the option to:

* import into an existing team or a newly created team on your workspace.
* Enable syncing for future created issues via the [Jira](https://linear.app/docs/jira) integration
* Import stale issues (not updated in 6 months) to your archive, or not to import them.
* map each Jira user to an existing Linear user, invite Jira users to your Linear workspace, or take no action for certain Jira users.

#### CSV imports

1. Export a CSV from Jira by searching under advanced issue search in JQL (project=TEST, for instance).
2. Export the data as a CSV and choose the "all fields" option.
3. Attach this file in Linear where prompted and optionally add data in the other requested fields.

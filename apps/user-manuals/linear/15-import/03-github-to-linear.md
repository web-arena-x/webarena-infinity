# Importing from GitHub Issues

This guide explains how to migrate from GitHub Issues to Linear, covering both approaches—starting fresh and importing historical data. We will walk through the preparation, execution, and cleanup phases of migration to ensure a smooth transition.

![Linear and GitHub logos](https://webassets.linear.app/images/ornj730p/production/e97aad772564b992f919dc9a7f2a7860f18ab796-2880x1620.png?q=95&auto=format&dpr=2)

## **Migration Approaches**

**Bringing historical GitHub Issues into Linear** offers several advantages. It preserves valuable context around feature development and bug fixes, maintains all discussions in one place, and provides continuity for in-progress work. Historical data also enables comprehensive reporting and more accurate future estimations based on past performance.

However, **starting fresh in Linear** has its own benefits. It gives teams a clean slate to implement improved workflows without the baggage of outdated processes. The migration process is much simpler with fewer decisions to be made and conflicts to resolve. Teams can establish practices from day one without inheriting messy historical data.

Many teams choose a middle ground—**importing only recent and in-progress issues while keeping the rest in GitHub as a historical archive**. This approach balances maintaining critical context while using the migration as an opportunity to clean up and prioritize the backlog. Your specific needs, the quality of your GitHub data, and how important historical context is to your ongoing work should guide your decision.

---

## Pre-Migration Planning

1. **Set up Linear teams** for each functional group that will be working in Linear. 
Provision users and add them to appropriate teams. Linear supports SCIM Group Push. 
 1. Please note that you cannot import to a sub-team directly. If you plan to use subteams, import to an existing (or create a new) top-level Linear team first, then [convert it to a sub-team](https://linear.app/docs/sub-teams#update-an-existing-team-to-a-sub-team) afterwards.
2. **Align workflows** by creating states in Linear that match what teams use in GitHub. Similar state names will automatically map during import.
3. **Develop a label cleanup strategy** Clean up unused labels in GitHub and plan which labels should be _team-specific_ vs. _workspace-wide_.
4. **Enable key Linear features** like Triage, Estimates, Cycles.
5. **Define use cases for GitHub Sync** either unidirectional or bidirectional. Refer to [GitHub Sync Options](https://linear.app/docs/github-to-linear#github-sync-options).

### Important Considerations

* **Status Mapping**: In GitHub Issues, issues are simply "open" or "closed". If an issue is unstarted or started in Linear, it's considered "open" in GitHub. If completed in Linear, it's considered "closed" in GitHub.
* **User Connections**: For comments and actions to be properly attributed during sync, users need to connect their GitHub accounts in Linear (Preferences > GitHub > Connect Personal Account).
* **Sync Limitations**: The sync doesn't attempt to replicate all features between the systems, focusing instead on core issue tracking functionality.
* **Transition Tool**: Bidirectional sync is generally recommended as a temporary transition tool rather than a permanent solution, due to its limitations and potential for confusion.
* **Multiple Repositories**: You can sync multiple GitHub repositories to a single Linear team, but each Linear team's issues can only sync with a single GitHub repository.

This sync capability allows teams to gradually transition to Linear while maintaining critical GitHub workflows, but it's generally best to eventually consolidate to a single system for clarity and efficiency.

---

## Running the import

### Prerequisites

* You must be a Linear Admin to perform imports
* The first import requires installing the Linear Data importer GitHub app
* GitHub organization admin access or approval may be required

### Import process

#### Setting up an import for the first time

The first time you run an import from a new GitHub organization, you'll need to install the Linear Data importer as a GitHub app. This step may require approval from an Admin in your GitHub organization.

![GitHub Importer first time](https://webassets.linear.app/images/ornj730p/production/42d451f5f7383acbd6e25942c5e3e1b0234688f1-1470x1254.png?q=95&auto=format&dpr=2)

1. Navigate to [Settings > Administration > Import/Export](https://linear.app/settings/import-export)
2. Select GitHub as the source
3. Click `+` next to "Connected organizations" and authenticate into GitHub
4. Choose the organization you wish to import from
5. Select the repositories to give the importer access to
6. Click _Install_
7. You will be redirected back to Linear, and can now select the repos you wish to import

#### Importing once you connected your GitHub organization 

1. Navigate to [Settings > Administration > Import/Export](https://linear.app/settings/import-export)
2. Select GitHub as the source
3. Select a repo or repos to import from
4. Choose the Linear team to import into.
5. Decide whether to import data for closed issues.
6. Review the fetched data
7. Select if you want to import closed issues into your team's archive. 
This archive is accessible from the dropdown menu on the team in your Linear sidebar. Archived issues can be restored at any time.
8. Choose whether to sync changes from Linear back to GitHub Issues.
9. Map your users.
10. Confirm your selections, and select _Finish_ to start the import.

By default, we will import any projects associated with the repos you choose. You will also have the option to choose to import all projects from the organization level. 

> [!NOTE]
> Stale issues are open GitHub issues that have not been updated in over six months. They will be imported into your Linear team's archives.

### Data included in the import

GitHub Issues | Linear --- | --- Title | Title Description | Description Labels | Labels (team-level)
Projects | Projects Comments | Comments Sub-issue | Sub-issue

> [!NOTE]
> Please note that data not included above like custom fields or issue created dates will not import to Linear.

### Syncing issues

![GitHub Issues Importer sync option](https://webassets.linear.app/images/ornj730p/production/788cbb5d30294e9289459d72af1da14df3cd9154-1218x266.png?q=95&auto=format&dpr=2)

The GitHub Issues Importer will sync imported issues bidirectionally.

### Mapping GitHub users to Linear

The importer will attempt to match existing users in Linear to those you're importing from GitHub. The optimal case is for users to already exist in both services with the same email address, and to have linked their GitHub accounts in [Settings > Connected accounts](https://linear.app/settings/account/connections).

That said, often this is not the case in practice.

1. **If a user is not yet in Linear, but has a valid email address in GitHub:** User will be treated as an external user and will be attributed as **author** of issues and comments, but not as the assignee
2. **User's email address is unavailable:** We cannot match these users. But if the user links their Linear and GitHub accounts in Settings > Integrations > GitHub **and** if the import is re-run, we might have a match.

Regardless of the scenario, re-running the import after users have joined will always help matching more users.

---

## Post import clean-up

### Label Organization

Promote common labels to workspace level for universal use:

1. Go to [Settings > Features : Labels](https://linear.app/settings/labels)
2. Create a new label with the exact same name as the team label
3. Re-enter the label name in the field
4. Select **Merge labels**

Consider grouping related labels and removing unused ones. You can refer to the Usage column in the Label settings page.

### Projects Management

GitHub Projects import as Linear Projects. Add appropriate teams to each project by finding it via search, selecting the "Teams" field, and adding teams from the dropdown menu. If a project is not found, it was likely to be imported as archived.

### Status Alignment

If statuses didn't map correctly during import:

1. Open Team settings > Issue statuses & automations
2. Create new statuses in the correct category if needed
3. Use Views to filter issues with incorrect statuses
4. Use `Cmd/Ctrl` `A` to bulk select them and update to the correct status
5. Delete unused or duplicate statuses

### Team Membership Cleanup

Remove team members who were automatically added during import but aren't actually part of the functional team. The importer recognizes all contributors to issues (creators, assignees, commenters) and adds them as members.

### GitHub Sync Options

While the GitHub Issues Importer offers syncing _on imported issues_, the GitHub Issues Sync feature in [Settings > Integrations > GitHub](https://linear.app/settings/integrations/github) allows you to automatically create issues between Linear and GitHub and sync them.

Details | Unidirectional | Bidirectional --- | --- | --- What it does | Creates new issues in Linear when they're created in GitHub | Keeps issues synchronized between both platforms Direction | Issues flow from GitHub → Linear | GitHub ↔ Linear (changes in either system reflect in the other)
Best for | Teams working on open source projects that want private internal discussions while still tracking external GitHub issues | Transition periods or when teams must use GitHub for integration requirements but collaborate with other Linear teams What syncs | * New issue creation
* Issue details (title, description)
* Comments added in GitHub and in Linear
* Attached images
* Open/closed status changes | * Issue creation and deletion
* Issue titles and descriptions
* Comments and responses
* Attached images
* Open/closed status (but not detailed workflow states)

GitHub Issues Sync relies on a mapping you provide in [Settings > Integrations > GitHub](https://linear.app/settings/integrations/github) between a Linear team and a GitHub repository. At this time, you cannot choose to sync only _certain_ Linear issues to GitHub, or select a different repository to sync to except by editing this setting.

> [!NOTE]
> Please see our GitHub integration [documentation](https://linear.app/docs/github#github-issues-sync) for more information about GitHub Sync

---

## **Starting Over**

### Revert an import

* For imports less than 14 days old: Go to Settings > Import/Export. Click the three dots next to the import and select **Delete import**.
* For imports older than 14 days, contact the team at Linear for assistance.

Note that deleting imports will remove all imported issues but not issues created directly in Linear or via GitHub sync.

---

## **Alternative: CLI Import for a flexible import**

For complex migrations involving custom fields:

1. Export GitHub issues to CSV
2. Format the CSV to match Linear's requirements
3. Use the [Linear CLI importer](https://linear.app/docs/import-issues#other)

Be aware that history, links, and integrations won't migrate with this method.

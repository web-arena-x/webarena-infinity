# Importer

Learn best practices for importing to Linear. Select the tool you're importing from in the table of contents for specific instructions.

![Image of migration assistants](https://webassets.linear.app/images/ornj730p/production/d2f61b4eeb982988a066a5416eaa81bb547178b3-2880x1769.png?q=95&auto=format&dpr=2)

## Linear Concepts

A Linear [workspace](https://linear.app/docs/workspaces) is our top level concept, which contains one or many [teams](https://linear.app/docs/teams). We recommend that each company using Linear uses only one workspace.

[Issues](https://linear.app/docs/creating-issues) and [projects](https://linear.app/docs/projects) are the core entities used to manage work in Linear. Each issue belongs to a single team, while projects can belong to one or many teams. Other concepts in Linear can be scoped to a team or a workspace like [Views](https://linear.app/docs/custom-views) (filter based groups of issues or projects), [Initiatives](https://linear.app/docs/initiatives) (hand-picked groups of projects) and more.

When you import from another service to Linear, we'll attempt to match data from the source tool with the closest concept in Linear. If a concept from the source tool does not translate well to Linear, it may not be imported; please see details on your individual service for further details.

## Pre-import best practices

 Consider the below before starting your first import for a smoother experience.

### Which data is worth importing?

 If there is data that is no longer relevant to your organization's day to day work, consider whether it needs to be in Linear at all (perhaps a CSV of exported data from long-resolved issues is sufficient). Some organizations choose to use Linear as a "clean break" from their legacy tool and import only where absolutely necessary so they can start fresh with minimal clutter. Others prefer to maintain as full a historical record as possible in one place.

If you're importing when evaluating Linear instead of transitioning all at once, you may wish to run a pilot by importing just a few teams. We also have a resource for switching tools in our [switch instruction manual. ](https://linear.app/switch)

### Choose an import method

We offer two main methods of importing to Linear; our dedicated import assistants in-product and a CLI import tool. We recommend using the former whenever possible as they retain much more data from the original source, are easier to use, and provide the option to delete an import in bulk if desired.

Use the CLI importer when importing from a service that we don't have a dedicated import assistant for. Import assistants are available for Jira, GitHub Issues, Asana, Shortcut and Linear. More information about the CLI importer can be found [here](https://linear.app/docs/import-issues#trello-or-pivotal-tracker).

### Understand the import process

You'll first need to have an Admin role in Linear in order to access our import tools. You may also need high permissions in the tool you're importing from in order to access the data. In general, the import assistants follow this path:

Step | Detail
--- | ---
Setup  | Provide an access token, or sign in to your source tool from Linear. Choose an existing team to import to, or create a new team. Please note that you cannot import to a sub-team directly -- instead, import to a top-level team and convert it to a sub-team afterwards.
Review | We'll display the issues, projects, labels, users and other data fetched from the information provided. 
Choose what to import | Choose whether to import only open issues, or also to import closed and stale issues to the archive. The archive can be accessed through the overflow menu on each team in your sidebar.
Map users | For each user fetched, choose not to import them, to create a new user from an email address, or to map them to an existing user in your Linear workspace.
Confirm | At this point, all data available to import will be summarized. If it looks as you expect, hit Finish to start the import. 

## How to import

Find instructions on importing from your source tool below:

### Jira

Find instructions [here](https://linear.app/docs/jira-to-linear) 

### GitHub Issues

Find instructions [here](https://linear.app/docs/github-to-linear)

### Asana

1. Navigate to [Settings > Administration > Import/Export](https://linear.app/settings/import-export). You must be an admin in Linear to access this page.
2. Click on the button for Asana.
3. Enter your Asana personal access token. You can obtain your personal access token by navigating to your Asana [developer console](https://app.asana.com/0/my-apps).
4. Enter your Asana team name.
5. Select which Linear team to import issues into.
6. Click **Next** to start importing.

An issue cannot belong to multiple projects in Linear, so one project will be chosen if issues are assigned to multiple Asana projects.

> [!NOTE]
> We currently only support in app importing from Asana organizations. Make sure your Asana workspace is an organization before beginning an import, or [convert your Asana workspace to an organization](https://asana.com/guide/help/workspaces/create#gl-convert-workspace) if it is not. If you do not want to convert your Asana workspace to an organization, use the CLI importer.

We'll map fields in Asana to these fields in Linear: 

Asana | Linear
--- | ---
Priority | Priority
Notes | Issue description (converted to Markdown)
Attached files | Added to description, all files except images and videos are converted to links
Tags | Labels (team-level)
Assignee | Assignee
Projects | Projects
Comments | Comments (markdown respected)
Status | Imported status will be Backlog or Done only
Sub-issue | Sub-issue
Blocked/blocking | Blocked/blocking

### Shortcut

1. Navigate to [Settings > Administration > Import/Export](https://linear.app/settings/import-export). You must be an admin in Linear to access this page.
2. Click on the button for Shortcut.
3. Enter your Shortcut personal access token. 
4. Enter your Shortcut team name.
5. Select which Linear team to import issues into.
6. Click **Next** to start importing.

We'll map fields in Shortcut Issues to these fields in Linear:

Shortcut | Linear
--- | ---
Name | Title
Description | Issue description
Tasks | Appended to the description
External tickets | Appended to the description
State | Mapped to the most similar Linear status
Story type | Added as label (team-level)
Tags | Added as label (team-level)
Owners | First owner added as assignee when possible
Epic | Created as projects
Comments | Comments
Estimate | Estimate
Due date | Due date
Priority | Priority

### Trello, Pivotal Tracker, GitLab Issues

To import issues from these services, use our open source CLI importer_._

For **Trello**, please note that imports must be run from individual board exports, not from the overall workspace. 

While CLI imports can also be used to customize imports for services with an import assistant, we don't recommend this as the CLI importer will not import data supported by the import assistant like comments or projects.

Our [Command Line interface (CLI) tool](https://github.com/linear/linear/tree/master/packages/import) uses CSV exports from the source tool and requires some technical expertise. Access it at the link or from [Settings > Workspace > Import/Export](https://linear.app/settings/import-export). For those unfamiliar with the command line, [this](https://drive.google.com/file/d/1cvjXN1c0oDgmtm0OZQyU1EXylDO2Oz2d/view?usp=sharing) video may help with getting started with a CLI import.

### Linear

To import data from one Linear workspace to another, first ensure that you have an admin account in both workspaces using the same email login credential.

> [!NOTE]
> If there isn't already an admin using the same email credential in both source and destination workspaces, invite an admin from the destination workspace to the source workspace (or vice versa) and have them run the import. For best results, avoid creating multiple accounts on the same workspace under different emails.

1. Navigate to [Settings > Administration > Import/Export](https://linear.app/settings/import-export). You must be an admin in Linear to access this page.
2. Click on the "Linear to Linear import" button.
3. Select the workspace you would like to import. We will only show workspaces under the same email address where you are an admin member.
4. Select the teams you would like to import from this workspace.
5. Choose how to map members from the workspace you are importing from to your current workspace.
6. Review a summary of the import.
7. Click "Start import".

> [!NOTE]
> This import will not carry over all data associated with your source workspace. Please note that the data below will not transfer.
> 
> * Custom views / view preferences / views attached to projects or initiatives
> * Favorites / reminders / drafts / inbox notifications
> * Integrations* / webhooks / OAuth clients / API keys (Integrations will need to be installed on the new workspace and will not resume notifications or automations for imported issues in most cases.)
> * Billing/plans* (please contact support@linear.app for assistance with billing transfers)
> * Workspace URL (you can switch this manually after import)
> * Personal and Workspace settings
> * Roles (current admins will be imported as members, you will initially be the only admin. Guests will carry over with the same permissions.

Linear (old) | Linear (new)
--- | ---
Title | Title
Description | Description
Estimate | Estimate
Labels | Labels
Due date | Due date
Comments | Comments
Workflow state | Workflow state
Sub-issues | Sub-issues
Relationships | Relationships
Projects | Projects
Initiatives | Initiatives
Team templates | Team templates
Dashboards | Dashboards

### Other

If you'd like to import from a tool not listed here, you can still do so using our [CLI importer](https://github.com/linear/linear/tree/master/packages/import) and the CSV file of your exported data.

First, you'll want to generate a Linear export file from [Settings > Administration > Import/Export > Export CSV](https://linear.app/settings/import-export). Remove any exported text but leave the headers of each column. This will give a CSV in the format that the CLI importer expects for a Linear import.

In the fields below, paste data from your source tool's export file, and save the CSV.

* `Title` - Issue title
* `Description` - Issue description
* `Priority` - Issue priority
* `Status` - Issue state (workflow)
* `Assignee` - Issue assignee (user's full name)
* `Created` - Issue created date
* `Completed` - Issue completed timestamp: please note that this will not appear in issue activity log, but will be stored on the issue.
* `Labels` - Added as a label (separate by commas for multiple labels)
* `Estimate` - Issue estimate: please note that these values only appear on the issue after enabling estimates on the imported issue's team.

Once the above data is in the attached format, you can import the CSV using the CLI and selecting the "Linear" CSV option when prompted. 

For those unfamiliar with the command line, [this](https://drive.google.com/file/d/1cvjXN1c0oDgmtm0OZQyU1EXylDO2Oz2d/view?usp=sharing) video may help with getting started with a CLI import.

### Troubleshooting

If something did not import as you expected, please check the section for your specific service to confirm whether we support importing that property. If the property is supported but didn't import as documented, please let us know at [support@linear.app](mailto:support@linear.app).

If you need to delete an import in order to re-import once more, you can do so through Import/Export settings, on the overflow menu on a specific import.  If no overflow menu appears, please contact [Linear support](mailto:support@linear.app) for assistance deleting it. 

Reimporting from the same external source to the same Linear team without deleting the initial import first will skip any already-imported issues.

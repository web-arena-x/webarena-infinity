# Labels

Use labels to categorize issues.

![Linear app showing labels being added to an issue](https://webassets.linear.app/images/ornj730p/production/3a4ffc89117bc3bd582ef96ee1a120607adfa5ad-1688x1325.png?q=95&auto=format&dpr=2)

## Overview

### Labels

Labels allow you to organize issues. Create them scoped to the workspace or a specific team level, so they're available only where relevant. You should create labels that are used by all teams (e.g. "Bug") in the workspace-level, so they will be accessible to all teams.

### Label groups

Label groups create one level of nesting in your workspace and team labels, giving you more options when organizing issues. Each label group is limited to 250 labels.

Please note that labels within groups are _not multi-selectable_, so when applying labels to issues only one label from each group may be applied. 

## Create labels

Create labels in [Settings > Workspace > Labels](https://linear.app/settings/labels) page or _Team settings > Labels_.

### Create a label during add label workflow

You can also create labels in the _Add label_ flow. Take the action to apply a label, then type the name of the label you want to create. The label will be automatically be saved to your team's labels.

If you'd like to create a label or label group directly from the _Add label_ flow, this is available with the syntax `label group`_/`label`_ or `label group:_label_` . For example, using _Type/Bug or Type:Bug_ will create the label group "Type" and the label "Bug".

![Type/Bug syntax being used to create a label in the group "Type" with the label "Bug"](https://webassets.linear.app/images/ornj730p/production/9074377f9a2bda6f688ee1e008ea1c2249581aad-1312x238.png?q=95&auto=format&dpr=2)

## Apply labels

Apply labels to any issue with the shortcut `L`, or by clicking into the label property field in an issue's right sidebar.

## Manage labels

Labels can be edited, merged, and deleted in issue label settings. Label data like SLA and Triage rules the label's used in, when it was last applied, and how many issues have that label appear in settings to guide your choices.

In workspace label settings, optionally select to display both all team and workspace labels on that page for ease of editing. Or, in larger workspaces, search for particular labels to assist in cleanup.

Edit label name or color by clicking on those properties in a label row. Or, right click on the row to see additional options like converting to a group, moving to workspace, or deleting the label.

Take bulk actions by selecting multiple labels (`x` or `Shift `+ click), then right-clicking on any selected label to choose an action. You can move rescope labels to and from the workspace level to a particular team, or change a label's team. If you find duplicates, merge multiple labels into a single label.

### Label descriptions

Add brief label descriptions in label settings. These descriptions appear when you hover over an applied label anywhere in Linear. These descriptions give a consistent understanding of when a label should be applied. [Triage Intelligence](https://linear.app/docs/triage-intelligence) also considers label descriptions to inform whether to suggest a particular label.

### Archive labels

Archiving a label keeps it on any issues where it's been applied, but stops people from using that label moving forward. Views, insights, filters and groups all respect archived labels. Take this option when you no longer need a label actively, but you want to retain historical context. 

Archive labels in label settings, through the overflow menu on a particular label's row.

### Delete labels

If you're sure a label no longer needs to exist, you can also delete it. Deleting labels is not reversible (including by Linear support) and will remove it from issues where it's applied, so please proceed with caution.

Delete labels in label settings, through the overflow menu on a particular label's row.

## Filtering and views

Team-specific labels "act" like workspace labels when filtering all teams or multi-team views. As long as labels in different teams share the same name, filtered results will show all issues across all teams that match the label. This holds true in custom views, my issues, project all team view_s_, and general search (/). It does not extend to the API (you'll have to use the unique identifier for each team's label).

If you only want to see results for a specific team's labels in a multi-team view, add a team filter on top of the label filter. Creating a workspace label with the same name as existing team label(s), will present the option to convert the team label(s) to the workspace level.

Learn more about [Label views](https://linear.app/docs/label-views) and how to [filter](https://linear.app/docs/filters) for labels.

## Reserved label names

We reserve the following label names that are duplicative of existing features to not cause confusion:

"assignee", "cycle", "effort", "estimate", "hours", "priority", "project", "state", "status",

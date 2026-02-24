# Parent and sub-issues

Use sub-issues to break down larger "parent" issues into smaller pieces of work.

![Linear app showing a parent issue with sub-issues](https://webassets.linear.app/images/ornj730p/production/a2c92123d2c244bb53f75e34970a5cb8417bd2c3-2340x1064.png?q=95&auto=format&dpr=2)

## Overview

Consider creating sub-issues when a set of work is too large to be a single issue but too small to be a project. Sub-issues are also ideal for splitting up work shared across teammates. When you add a sub-issue to another issue, the other issue becomes its "parent".

## Create a sub-issue

Create a sub-issue by opening the parent issue and click the `+ Add sub-issues` button below the issue description. This will launch the sub-issue editor. You can also use the shortcut `Command` `Shift` `O` to open the editor.   
  
You can also create sub-issues in the issue creation modal (C) by pressing `Command` `Shift` `O` to open the editor or under the `...` menu and _"Add sub-issue"._ 

When you save a sub-issue, it will automatically launch the editor to create a new one. If you want to create a new one with the same values (labels/assignee etc.) you can press `⌘ Shift` `Enter `or  `Shift`+ click the save button. Press `Esc` to exit the sub-issue editor and continue updating the parent issue.  
  
You can turn a comment under an issue into a sub-issue by hovering over a comment and clicking the `…` menu then _"new sub-issue from comment"._ Selecting a comment's text and pressing  `⌘` `Shift` `O` will also create a sub-issue.  
  
If you have a list (bulleted, numbered or checklist) you can highlight the checklist and hit `⌘` `Shift` `O` to convert to sub-issues or choose the _"Create sub-issues(s) from selection"_ item in the formatting toolbar.  
  
You can add a template using the templates icon when creating a sub-issue or using the command menu under "Create new sub-issue from template" when viewing the parent.

## Copy properties

Sub-issues created in the editor automatically copy issue properties from the parent issue such as the project and cycle _as long as those are set before you create the sub-issue_. 

Team, labels and assignees are not copied over. You can't create sub-issues while editing the parent issue, but the option will come up once you press save.  
  
You can duplicate a parent and its sub-issues from the Parent's `... `menu under _"Duplicate"_ and hit the toggle _"Include sub-issues"._

## Status automation

Optionally, configure the following behaviors at the team level (Settings > Team > Workflow) to automate status relations between parent and sub-issues. Status changes triggered by Git integrations will also respect these automations.

**Parent auto-close**

When all sub-issues are marked as done, the parent issue will also be marked as done automatically.

**Sub-issue auto-close**

When the parent issue is marked as done, all remaining sub-issues will also be marked as done.

## Converting issues

### Turn issues into sub-issues

Turn an existing issue(s) into sub-issues of another issue by selecting one or multiple issues and then taking the action to set the parent issue. This action is accessible from the command menu or by pressing `Cmd` `Shift` `P` and selecting a parent issue.

### Turn issues into parent issues

To make an existing issue a parent issue of another issue, hover over a sub-issue and take the action _"Set Parent"_ in the contextual menu, command menu or `... `menu. 

### Turn sub-issues into issues

You can turn a sub-issue into a regular issue again using the `⌘/ctrl+K` menu option "Remove parent".

### Turn issues into projects

Sometimes an issue grows so large it's more appropriate to turn it into a project instead. To do so, hover over the parent's `...` menu and choose "_Convert to project."_ The project will inherit its details from the original parent issue, and former sub-issues will become standard issues in the project.

## Filter sub-issues

You can usually set the view to show or hide sub-issues in [Display Options.](https://linear.app/docs/display-options) You can also use [Filters](https://linear.app/docs/filters) to show only top-level (parent) issues, issues with sub-issues, or only sub-issues. If you use these filters frequently, consider creating a [custom view.](https://linear.app/docs/custom-views)  
  
You can also hide completed sub-issues by default under the `...` menu and toggling "Always hide completed sub-issues".  
  
You can also sort your sub-issues under an issue from the `…` menu and _"Order by"_ though this only updates it for the current user, not globally.

## Display options

When looking at sub-issues from the context of their parent issue, you can customize the order of the sub-issues and the properties that display.

![sub-issue display options menu](https://webassets.linear.app/images/ornj730p/production/66557cbd02b0b0d4b3dbbdcbcd1a42d1efbc677a-2856x1410.png?q=95&auto=format&dpr=2)

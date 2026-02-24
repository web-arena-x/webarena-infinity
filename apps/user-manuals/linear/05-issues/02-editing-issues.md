# Edit issues

Making changes to an issue.

![issue creation dialogue box](https://webassets.linear.app/images/ornj730p/production/d8f7b8a4591344aa7946960fc408d1fa05044b4c-1256x402.png?q=95&auto=format&dpr=2)

## Overview

All workspace members will be able to edit an issue's title and description, regardless of who is the original creator of an issue. For comments, only the creator of the comment will be able to perform additional edits.

## Edit issue title and description

You can edit an issue title or description by clicking directly on the title or description and editing inline. You can also use the methods below when editing an issue.

## Revert/Restore issue description

If changes have been made to an issue description and you would like to revert to the original issue description or view changes that have been made, open the command menu with `Cmd` `K` and search for `Issue content history… `or choose the "Show version history" option from the `...` menu on an issue.   
The issue description history will be available in this option 10 minutes after a description has been modified.

## Move an issue to another team

When work needs to be passed over to another team, or when you are consolidating teams, issues can be moved to the appropriate Linear team within the same workspace.

For a single issue, simply use `Cmd/Ctrl` `Shift` `M` to move an issue to a new team. To move issues in bulk while retaining as much data as possible, select issues manually or with filters before moving them. Use `Cmd/Ctrl` `A` to select all issues on the list or board.

`Cmd/Ctrl` `Z` will undo moving an issue if you moved it by accident, but it will not undo the removal of issue data.

### Old Issue IDs and URLS

When you move an issue to a new team, we generate a new _issue ID_ and unique URL for the issue. Old URLs will still work and redirect to the new issue URL. Searching for old _issue IDs_ will also bring up the current issue (unfortunately, this doesn't work for old issue titles). Inline references to issues (like #ENG-123) will redirect when clicked, but won't update visually from the original issue ID they're associated with.

### Changes in issue properties

Issue property | Effect | Workaround --- | --- | --- Cycle | Removed | Create a temporary label (e.g. Cycle 1) before moving issues if you'd like to retain the grouping when assigning issues to the new team's cycles Team Labels | Removed | Create a label in the new team with the same name.
Projects | Removed | Add the new team to the current team's project before moving the issue.
Relations | Remain Priority | Remain Issue ID | Changed | A new issue ID will be created in the new team. Old issue URLs will redirect and searches for the old ID will bring up the issue Status | Changed | If the same status name exists, it will be matched. Otherwise, it'll be assigned the first status in the same category.

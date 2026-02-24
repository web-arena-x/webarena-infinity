# Issue relations

Create relationships between issues such as blocking, related, and duplicate.

![Issue relations blocking and relating to other issues](https://webassets.linear.app/images/ornj730p/production/4d5b81c2af018955702e62e2e78d40cc620cc737-946x448.png?q=95&auto=format&dpr=2)

## Overview 

Tag issues with relations and dependencies to help your team identify and remove blockers and work on the most important issues. You can mark issues as blocked, blocking, related, and duplicate.

## Add relationships

The issue and type of relationship will show up in the issue properties sidebar.

From the issue editor, add a relation using keyboard shortcuts or by selecting the overflow menu after saving the issue. From a list or board, use either the keyboard shortcut, command menu or contextual menu. You'll be prompted to find and select the related issue. You can add as many related, blocking, blocked, or duplicate flags as you like but will have to repeat the steps for each one.

## Related issue

When you reference issues in a description or comment, they'll automatically become a related issue. Alternatively, use `M `+ `R `to relate one issue to another. When viewing an issue you can open the command menu (`⌘/CTRL+K`) and type _"Create new issue related to…"._

To remove a related issue, hover over the related issue and click the _X._ You can also select _Remove relation_ from the command menu `⌘/Ctrl` `K`. If you have more than one relation, you'll be prompted to select which relation to remove.

## Blocked / blocking

Mark issues as blocked by other issues with `M` then `B`. If other issues are blocking the current issue, they'll show up in the issue sidebar with an orange flag under _Blocked by_.

Mark issues as blocking other issues with `M` then `X`. If the issue is blocking other work, the blocked issues show up in the issue sidebar with a red flag under _Blocks_.

Once the blocking issue has been resolved, the blocked issue flag turns green and moves under _Related_.

## Duplicate

Merge duplicate issues into the canonical (saved) issue with the shortcut by pressing `M` and `M`. This will mark the issue you are viewing or have selected as a duplicate issue and change the status to canceled. You cannot mark issues the other way around (e.g. view the canonical issue and mark other issues as duplicates of it). If you have more than one canceled status, you can specify which status to apply under _Team Settings > Workflow_.

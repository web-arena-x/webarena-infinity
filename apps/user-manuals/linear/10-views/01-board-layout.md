# Board layout

Nearly all views in Linear can be shown in board layout in addition to list view.

![Linear app showing the board layout](https://webassets.linear.app/images/ornj730p/production/04115ca5eb44c3c6fc38d9998e6a7af068cb8b61-3424x1920.png?q=95&auto=format&dpr=2)

## Configure

You can toggle on board layout with the keyboard shortcut `Cmd/Ctrl` `B`. Alternatively, you can switch between board or list layout using the board and list icons next to `Display options`. 

### Keyboard

`Cmd/Ctrl` `B` to switch to board layout (or back to list)

`X` to select one issue

`Shift` `X` or or `Shift` `Click` to select multiple issues

`Option/Alt` `Shift` `Up` or `Down` to move a selected issue to the top or bottom of the column

`T` to toggle the collapse or expansion of a swimlane

### Mouse

Click on _Board_ icon to the left of _View Options_ and select board layout on most views

Create issue by clicking the _+_ sign at the top of a column to create an issue in that column. 

Hide a column by clicking the more menu (three dots). Unhide a column by scrolling to the right-most column. Filter to show only specific columns or toggle off the View _Option Show empty groups_ to hide empty columns.

### Command menu

`board` to select show in `show in board view`

## Basics

### Feature parity

Functionality and keyboard shortcuts are almost exactly the same on board and list views with a few exceptions.

* Board views and List view cannot be ordered independently. If a List view is ordered by priority for example, Board view will be ordered the same way.
* Board views to default to grouping by Status but you can click into `Display options` and `Grouping` to group by Focus, Status, Project, Priority, Cycle, Label, Label group, or SLA status (if applicable).
* When grouping by status, board views are always ordered with statuses from first to last, whereas some list views have unique ordering for statuses.
* You can hide columns in board views but in list views, you can only temporarily hide the equivalent column/grouping option by using filters. You can then make a custom view if you'd like these filters to be permanent.

The same shortcuts work to select issues in the board view, such as `X` to select specific issues and `Shift` `X` or `Shift` `Click` to select multiple. 

### Hide columns

Hide columns you don't need by selecting _Hide_ from the column menu (three dots). Hidden columns will show up as the last column on your board. Drag issues into hidden columns without having to unhide them.

### Move to top or bottom

To avoid dragging issues up or down long columns, use keyboard shortcuts instead. `Option/Alt` `Shift` `Up` will move issues to the top of a column whereas `Option/Alt` `Shift` `Down` will move it to the bottom. By default, when you move issues to a new column on a board, it will go to the top if you make the change with the keyboard shortcut `S` or command menu and to wherever you placed it if you used the mouse.

### Navigating columns

Board views with multiple columns can be scrolled horizontally by holding `Shift` and scrolling vertically, or using horizontal scroll if your device supports it (like on a trackpad or Magic Mouse). 

Alternatively, click and pull an empty space in the board to scroll horizontally.

### Swimlanes

Board and list views have the option to display an extra dimension for visualising your projects or issues in lanes or rows on a board view, commonly known as swimlanes in project management.   
 
These sub-grouping options are especially useful for a high-level overview of the company's progress or resource allocation. You can sort by columns, group those columns and lay them out as rows for your chosen dimension such as teams, cycles, assignee, lead, initiative or project health to name a few. 
 
These lanes can be collapsed or expanded for further visual clarity in board view.

![Linear interface showing a board view of projects](https://webassets.linear.app/images/ornj730p/production/238e212208818157d687416737b7e922aef7b14f-2560x1440.png?q=95&auto=format&dpr=2)
*Swimlanes showing projects grouped by status and target dates.*

## FAQ

<details>
<summary>Can you set board to be the default layout for the workspace?</summary>
Unfortunately, you can't set board view as a universal default. However, a user can choose board layout in a view and then select `view options` and `set as default` to ensure board layout is the default for that view for anyone who visits that one view.   
This won't prevent other members from changing this and setting a new default afterwards though.
</details>

<details>
<summary>Why is Board layout not showing as an option?</summary>
It is not possible to select board layout in split views like Inbox or Triage.
</details>

<details>
<summary>Can I show descriptions or all issue properties in board layout?</summary>
Descriptions are not shown on cards. If an issue has many properties, not all properties may have space to be display on the card.

Use `Space` while hovering your cursor over a card to peek for more detail, or open the issue to see all properties.
</details>

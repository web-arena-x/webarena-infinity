# Filters

Filters allow you to refine existing views and create custom views to show only the relevant issues.

![Linear interface showing filters applied to the active issues view](https://webassets.linear.app/images/ornj730p/production/26e1e266d76606fad8972baf4b57ed364aa2e4c1-2438x1126.png?q=95&auto=format&dpr=2)

## Overview

Our powerful filtering system lets you refine issue lists down to just the issues you need to work on. You can apply filters to almost every view in Linear and filter by almost any issue property. You can also apply various operators to filters and combine filters to show any or all. 

### Keyboard

`F` to open filter menu, then type to select filter _type_ and _name_ or quick filter by typing the name directly

Press `F` again to add additional filters. To refine operators on existing filters, use the mouse. 

`Backspace/delete` to clear filters if filter panel is focused

`Option/Alt` `V` to save as custom View

### Mouse

* Click the Filter button in the top bar to filter any view
* Click the _X_ on a filter to remove it
* Click the button in the top right next to View Options that appears on filtered views to create a custom View

### Command menu

`filter` then `filter type` then select specific filters. To refine operators on existing filters, use the mouse.

## Basics

### Apply filters

Type `F` to select filters from the command menu or click the Filter button above the board or list. You'll see a menu of filters that you can apply to the current view along with the number of matching issues. Once you've opened the filter menu, you can move through the menu or use free text search to find the exact filter you need.

### Filter categories

You can filter by the following properties in Linear:

Type | Filters --- | --- Issue property | Priority, Cycle, Estimate, Labels, Links Project property | Project Workflow | Status, Auto-closed Issue relations | Blocked, Blocking, Related, Parent, Sub-issue, Duplicate Dates | Completed, Created, Due, Updated User | Assignee, Created by, Subscribers Other | Filter by content

There are a few edge cases with workarounds:

* To filter for **no labels**, you'll have to select all labels and then switch the operator to _does not include_.
* To filter by milestones, filter by project first.
* You cannot filter for **suspended users**. To find issues assigned to or created by suspended users, navigate to their profile page (`linear.app/workspace-name/profiles/username`). If you do not know the username, an admin can find the link by clicking on the user's photo or name on the [Members list](https://linear.app/settings/members).

### Quick search filters

If you know the specific name of the property you want to filter, you can type that directly and the filter will show up as a choice, saving you from having to click through the category to select it. 

Property type | Quick filters --- | --- Team | Team name Status | Status name Assignee | Username Created by | Username Priority | "High", "Low", etc.
Labels | Label or label group name Content | No quick filters available Cycle | Active, Upcoming Project | Project name Subscriber | Username Relations | These are top level filters Date filters | "N days", Month, Quarter, Half-year, Year Links | Front, Zendesk, Intercom, custom link source Milestone | Milestone name

### Filter with AI

Use natural language combined with artificial intelligence to filter your views. For example filter by phrases like "Show me issues assigned to me", "What issues are important?", " what issues are due next week" and so on, to have your views automatically filtered with the most suited parameters.



![Linear interface showing AI filters menu](https://webassets.linear.app/images/ornj730p/production/f2f4e2653379d8211c581e5a946d037b7c4cfd8e-848x405.png?q=95&auto=format&dpr=2)

### Build with operators

Once you add a filter, refine it with operators. The filter type cannot be changed but clicking on any other part of the filter formula will give you options to change it and modify the query. 

For instance, for a filter that says _Assignee is Andreas,_ clicking on _Assignee_ will do nothing, clicking on _is_ will give you the option to change the operator to i_s not_, and clicking on _Andreas_ will show a selectable list to modify the assignee. If you add another assignee, Adrien, then you'll see the is operator change to _is either_ _of_ or _is not_.

We support the following operators in Linear, which will show up depending on the type of filter and selections:

* _is or is not_ when one option is included in the filter
* _is either of or is not_ when multiple options are included in the filter
* _includes any, all, neither, either,_ or _none_ for labels and links
* _before_ or _after_ for date-related filters

### Combined filters

Show results that match _any or all_ filters applied to a view. Once you add at least two filters, the option will appear in the top right sidebar. Click on the _all filters_ or _any filters_ wording to switch it.

### Create Views

Once you've applied at least one filter to a view, you'll see a button in the top right appear that lets you create a View from the custom filters. If you click it (or use the shortcut `Option/Alt` `V`), you'll be taken to the View editor with those filters already applied. Learn more about [Views](https://linear.app/docs/custom-views).

### Filterable views

Almost every view in Linear can be filtered with a few exceptions:

View | Filters --- | --- Search Inbox My issues Reviews Initiatives Projects Customers Teams Members Triage All issues Cycles Archive | Available Views | Apply filters on any view and click to save to create a new custom view. You can also apply temporary filters on top of any existing view.

### Filter with API

For more complex filters or to build queries on the API, see our [developer documentation](https://developers.linear.app/docs/graphql/working-with-the-graphql-api/filtering).

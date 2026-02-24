# Project dependencies

Visualize blocked and blocking relationships amongst projects.

![stylized image of lines connecting projects with dependencies](https://webassets.linear.app/images/ornj730p/production/1e5e2fc2de4cd906689e5bf0751223bc70010e99-3312x1734.png?q=95&auto=format&dpr=2)

## Overview

Project dependencies provide a visual depiction of blocking relationships on timeline views. Currently we only support a end -> start dependency.

## Create a project dependency

You can establish a project dependency from the project's contextual menu by clicking the three dots next to the project name, or using command bar `Cmd/Ctrl` `K`. Select or hover over _Dependencies,_ select or hover over **Blocked by...** or **Blocking...**, then select the related project.

You can also create dependencies from the timeline view. Hover at the end of a project bar to see a circle. Click and drag from that circle to another projects to create a new dependency.

## Working with dependencies on the timeline

* Click on any dependency line to jump to a project, or remove that dependency.
* When dragging a project with dependencies, there are several ergonomics to help you plan quickly:
 * Any projects in the dependency chain that are backlog or planned will be "bumped" with the dragged project. Hold `Cmd/Ctrl` to keep the chain in place.
 * Hold `Shift` to move all projects in the dependency together, regardless of status.

## View project dependencies

When a dependency relationship has been established, the Project Overview and the Project Properties right side panel will display "Blocked by" and "Blocking" fields.

Project dependencies can be seen on the project timeline view. You will see lines connecting the blocked and blocking projects.

### Dependency line color

* The blue line depicts a dependency that has not been violated.
* The red line is a dependency that has been violated.

![blocked and blocking projects visualized in a timeline with lines connecting them](https://webassets.linear.app/images/ornj730p/production/09ba034e341bdc7d30000031f69b7d4760f58f01-1752x482.png?q=95&auto=format&dpr=2)

### Dates used for dependency start/end

* The dependency line will start at either the **target end date** or **predicted end date** (if no target end date is available) of the blocking project.
* The ferry line will link with either the **target start date** or the **target end date** of the blocked project.

## Filtering for project dependencies

There are several filter options related to project dependencies:

* `Project has dependencies`
* `Project has blocking dependency`
* `Project has blocked by dependency`
* `Project has violated dependencies`

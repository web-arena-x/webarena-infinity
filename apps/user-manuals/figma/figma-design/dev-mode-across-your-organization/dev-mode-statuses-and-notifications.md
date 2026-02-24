# Dev Mode statuses and notifications

Source: https://help.figma.com/hc/en-us/articles/26781702258583-Dev-Mode-statuses-and-notifications

---

Before you Start

Who can use this feature

Notifications and the **Ready for dev** status are available on all paid plans

The **Completed** status is available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires a [Full or Dev seat](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor)

Statuses and notifications in Dev Mode help to manage developer handoff. [Statuses](#h_01J96T2MJRVVH4JVPWJSMCGHQX) are used to track when sections, frames, or components are ready for development. [Notifications](#h_01J96T2MJRH0Y3ZAKB13FKS9W1) are based on status changes so developers can react to the state of designs.

## **Statuses**

Dev Mode statuses show the current stage of a design for handoff. Designers can add notes to statuses about updates or changes.

There are two statuses available in Dev Mode for managing handoff:

- ![](https://help.figma.com/hc/article_attachments/29138100363671)**Ready for dev**: Indicates that sections, frames, and components that are ready for a developer to review and implement.
- ![](https://help.figma.com/hc/article_attachments/29138054657047)**Completed** (Organization and Enterprise plans): Indicates that development work for the design is complete.

Both the **Ready for dev** status and the **Completed** status also have a ![](https://help.figma.com/hc/article_attachments/29138054659991)**Changed** state. The **Changed** state is set when a design that’s been marked ready for dev or completed is modified. It cannot be set manually.

When a designer updates a design previously marked ready for dev or completed, they should follow the steps to [update the status for the changed design](#h_01J96T2MJRZVJS24W67375WTPT) to clear the **Changed** state.

When a developer encounters a design that’s changed, they can [compare changes](https://help.figma.com/hc/en-us/articles/15023193382935) to see why the state has changed and the differences from the previous version. The developer should also reach out to their designers to [update the status of the changed design](#h_01J96T2MJRZVJS24W67375WTPT).

A design won't be marked as changed in the following instances:

- If a component instance is updated from a shared library
- If there’s a change in value of a variable that’s already attached to a layer in the design
- If there’s a change in value of a style that’s already attached to a layer in the design
- If the change is temporary, such as when hovering an object over a design that uses auto layout

Statuses, including updating a status that’s changed, can be set while editing designs or in Dev Mode. You can also change and update statuses in Dev Mode [ready for dev view](dev-mode-ready-for-dev-view.md) and [focus view](dev-mode-focus-view.md).

### Mark a design as ready for dev

To mark a design as ready for dev:

1. In Figma Design or Dev Mode, select a section, frame, or component.
2. For sections and frames, next to the label, click  **Mark as ready for dev**. For components, the button is above the upper-right corner. Any users that previously opened the file in Dev Mode are [notified](#h_01J96T2MJRH0Y3ZAKB13FKS9W1) that the design is marked **Ready for dev**.

### Remove the Ready for dev status

To remove the **Ready for dev** status:

1. For the section, frame, or component where you want to clear the status, click  **Ready for dev.**
2. In the drop-down menu, click **Remove status**.

### Mark a design as completed (Organization and Enterprise plans)

To mark a design as completed:

1. For the section, frame, or component that you want to mark completed, Click  **Ready for dev**.
2. In the drop-down menu, click **Mark as completed**. Any users that previously opened the file are notified that the design has been completed.

### Update the status for a changed design (Organization and Enterprise plans)

To update the status for a design that’s changed:

1. For the section, frame, or component that was updated, click ![](https://help.figma.com/hc/article_attachments/29138054659991)**Ready for dev**.
2. Optionally, in the text box that appears, type a reason for the change. The reason is included in the version history for the design and [notifications](#h_01J96T2MJRH0Y3ZAKB13FKS9W1) triggered by the change.
3. Click **Done with changes**. The status is set to **Ready for dev**. Any users that previously opened the file are notified that the design has been updated. If you wrote a reason for the change, that reason is included in the notification.

## Notifications

Dev Mode notifications keep you informed when statuses change in a file. Figma supports email, desktop, and mobile push notifications by default. You can also set up:

- Slack notifications with the [Slack integration for Figma](https://help.figma.com/hc/en-us/articles/360039829154-Get-Figma-notifications-in-Slack)
- Teams notifications with the [Figma app for Microsoft Teams](https://help.figma.com/hc/en-us/articles/7405452518423-Figma-and-Microsoft-Teams)

If you’ve viewed a file in Dev Mode and have either a full or dev seat, you’ll receive notifications when designs are first marked as **Ready for dev**.

If you have an Organization or Enterprise plan, additional notifications are triggered:

- For designs that were previously **Ready for dev** or **Completed**, when the status is [updated following a change](#h_01J96T2MJRZVJS24W67375WTPT) to the design.
- When a design is [marked Completed](#h_01J96T2MJRF777TM3035CYREYJ)

If multiple designs change status within an hour, the notifications are grouped by type. For instance, several **Ready for dev** updates will be combined into a single notification.

Dev Mode notifications include links to the relevant designs:

- The **Inspect in Dev Mode** link goes to the [ready for dev view](dev-mode-ready-for-dev-view.md) for the corresponding Figma file
- The individual cards for designs open the corresponding design in [focus view](dev-mode-focus-view.md)

### Manage Dev Mode notifications

To modify your Dev Mode notification settings for a file:

1. Open a Figma Design file.
2. Click the Dev Mode toggle or use the keyboard shortcut `Shift``D`.
3. Click **Comment** or press `C` to enter comment mode.
4. Click **Settings** at the top of the right sidebar.
5. From the dropdown, select one of the following:
   - **Status changes**: This setting notifies you any time a design in the file is marked **Ready for dev**.
   - **Nothing**: You are sent no Dev Mode notifications.

![Notification settings panel in Figma with options for comment and Dev Mode notifications.](https://help.figma.com/hc/article_attachments/29138100370327)

The settings for Dev Mode notifications can be changed in the Dev Mode interface and when focused on a design.

![Dev Mode notification settings panel showing options for comment notifications and status changes.](https://help.figma.com/hc/article_attachments/29138100371223)
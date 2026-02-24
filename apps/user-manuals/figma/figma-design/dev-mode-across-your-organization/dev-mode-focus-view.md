# Dev Mode focus view

Source: https://help.figma.com/hc/en-us/articles/23919923330455-Dev-Mode-focus-view

---

Before you Start

Who can use this feature

Available on the [Organization and Enterprise plans.](https://help.figma.com/hc/en-us/articles/360040328273)

Users with [Full, Dev, or View](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-is-out-of-beta-what-admins-need-to-know#h_01HKN19J4JJTKGMATHW6BP331A) seats can access the ready for dev view.

Users with [Full or Dev seats](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-is-out-of-beta-what-admins-need-to-know#h_01HKN19J4JJTKGMATHW6BP331A) can change statuses.

Users with [full or dev seats](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-is-out-of-beta-what-admins-need-to-know#h_01HKN19J4JJTKGMATHW6BP331A) can access the focus view.

When you’re using the [ready for dev view in Dev Mode](https://help.figma.com/hc/en-us/articles/23918228264855) to explore sections, frames, and components that are ready for development, you’ll frequently want to inspect specific designs more closely. To get details for designs that are ready for dev, use the Dev Mode focus view. With the focus view, you get:

- All the same tools you normally have available in your Dev Mode toolbar.
- The same **Inspect** and **Plugins** tabs you have access to in Dev Mode’s full experience.
- A version history with descriptions specific to the design you’re viewing that you can use to compare different versions and see changes over time.
- An easy way to expand and explore the layers of a given design that’s ready for dev.
- Interactive inspection controls that let you temporarily resize a design or switch variable modes without disrupting the design file.
- The ability to mark work as completed for a specific design.

To access the focus view in Dev Mode:

1. Open a Figma Design file.
2. Click **Ready for dev** in the left sidebar. The ready for dev view opens, displaying a list of all designs marked with a dev status.
3. Click the design that you want to focus on.

**Note:** You can also open focus view by hovering over or selecting a frame, then clicking **Open in focus view** next to the dev status.

To access the focus view from Design mode:

1. Open a Figma Design file.
2. On the canvas, for the design you want to focus on, click the dev status and select **Show in focus view**.

   ![Context menu showing options: Show in focus view, Copy link to focus view, Mark as completed, Remove status. Cursor hovers over "Show in focus view."](https://help.figma.com/hc/article_attachments/24379953880087)
3. Optionally, click **Copy link to focus view** to get a link to the focused design that you can share with others.

The focus view opens, displaying the following:

- The design you wanted to inspect appears in the center of the focus view. You can use your Dev Mode tools to do things like measure, annotate, and comment on the design.
- [The **Inspect** and **Plugins** tabs](../inspect-designs/guide-to-inspecting.md), where you can do things like generate code, view the properties of the design, export or download various, and run plugins for Dev Mode.
- Interactive inspection controls that let you preview how a design responds to different variable modes and frame sizes without making any changes to the actual design or affecting what others see.
- The **Mark as completed** button, which you use to confirm that the dev work for the design is done.

![Web interface with product thumbnails and prices; right panel shows code settings and version history in focus view.](https://help.figma.com/hc/article_attachments/33544807806487)

## Navigate

In the focus view, Figma provides a few ways to navigate to other areas of Dev Mode.

![UI showing a shopping basket with options to inspect on the page or copy link, and a "Mark as completed" button. Cursor hovers over the "Inspect on page" option.](https://help.figma.com/hc/article_attachments/33544869176343)

To go to the ready for dev view, in the upper-left corner of the focus view, click **See all ready for dev.**

To see the design in the context of the canvas, in the upper-right corner of the focus view, click and then select **Inspect on page**.

To return to the area of the Figma interface you were using before you entered the focus view, in the upper-right corner of the focus view, click . If you entered the focus view from the canvas, you’re returned to the position you were at on the canvas. If you entered from the ready for dev view or using a link, then you are returned to the ready for dev view.

## Explore layers

The focus view provides an easy way to explore the individual layers of a given design. The focus view’s layer panel appears when you select one or more parts of the design.

![Layer panel in Figma's focus view shows hierarchy and text elements to explore specific layers in the design.](https://help.figma.com/hc/article_attachments/24380053112727)

## Inspect and Plugins panels

The **Inspect** and **Plugins** panels are the same as your regular Dev Mode experience, simply limited in scope to the design you’re viewing. To learn how to use the panels, see [Guide to Dev Mode →](../tour-the-interface/guide-to-dev-mode.md)

## Interactive inspection

Focus view includes interactive inspection controls that let you temporarily explore how a design behaves in different scenarios. Use these controls to:

- Resize the top-level frame by typing specific values for width and height, or dragging the horizontal and vertical handles around the frame to adjust the size manually.
- Use the dropdown menu to preview the design in different variable modes (like light and dark themes).

![Canvas displaying an e-commerce design with interactive inspection tools and version history panel for development review.](https://help.figma.com/hc/article_attachments/33544807813143)

Any changes you make with these controls are temporary and only visible to you. They’re helpful for previewing how a design responds to different conditions without affecting the file or what other collaborators see. Changes reset when you leave focus view or click the reset button.

## Version history

Similar to the [version history that’s available for files](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history), the focus view includes an annotated version history that tracks iterations of work on the design.

Normally, the file-wide version history shows you every version in a file, but often there can be a lot of activity and you care most about what’s changed in a specific frame or section that you’re reviewing and implementing. The version history in focus view shows you versions and works the same as the file-wide history, but is scoped to only versions that affect the specific design you have open in focus view.

![Figma focus view showing version history and comments panel for a design, listing who made changes and when on this file.](https://help.figma.com/hc/article_attachments/24380053115031)

As designers and developers iterate on a design, they update the [status](https://help.figma.com/hc/en-us/articles/23918228264855) and add notes to describe the changes. Each time the status updates, an entry in the version history is added. You can also compare different versions in order to identify the changes between each iteration.

![Version history panel in Dev Mode showing options to inspect, compare, or copy link for design versions.](https://help.figma.com/hc/article_attachments/24380063914775)

You can inspect older versions, copy a link to that particular version, or compare it to the latest version currently in your file. [Learn more about comparing in Dev Mode →](../inspect-designs/compare-changes-in-dev-mode.md)

## Mark as completed

To show the dev work for a design is done, use the **Mark as completed** button at the top of the focus view.

![Focus view showing design with 'Mark as completed' button in the upper-right corner.](https://help.figma.com/hc/article_attachments/24380053118615)

When a design is marked completed, a new entry is added to the version history, and the design remains available in the [ready for dev view](https://help.figma.com/hc/en-us/articles/23918228264855) for later iterations.
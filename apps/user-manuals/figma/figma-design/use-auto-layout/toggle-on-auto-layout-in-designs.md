# Toggle on auto layout in designs

Source: https://help.figma.com/hc/en-us/articles/5731482952599-Toggle-on-auto-layout-in-designs

---

Before you start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access can use auto layout

This article covers just one aspect of working auto layout. Check out these other articles to learn more about working with auto layout in Figma Design.

- [Guide to auto layout](https://help.figma.com/hc/articles/360040451373): An overview of auto layout, how it works, key properties, and browse a collection of auto layout resources.
- [Use the horizontal or vertical flows in auto layout](https://help.figma.com/hc/articles/31289464393751): Learn about the properties available to the horizontal and vertical flows in auto layout.
- [Use the grid auto layout flow](https://help.figma.com/hc/articles/31289469907863): Learn how to work with columns, rows, and cells with the grid layout flow.
- [Create multi-dimensional auto layout flows](https://help.figma.com/hc/articles/31441443713047): Combine multiple auto layout flows to build fully responsive components and screens.

## Use auto layout

You can use auto layout on a frame or a selection of objects. This includes:

- New or empty frames
- Frames with existing content
- Components and component sets
- Groups or other selections of layers and/or objects

To use auto layout, select one or more layers and use one of the following methods:

- Use the keyboard shortcut `⇧ Shift` `A`
- In the right panel, click  next to **Auto layout**
- Right-click on a frame or object and select **Add auto layout**

If you have a frame or a main component selected, you can also choose from one of the auto layout flows in the **Layout** section of the right sidebar:

- **Vertical**
- **Horizontal**
- **Grid**

![Mobile design for a blog app using Figma's auto layout, showing layout properties and alignment settings on the right panel.](https://help.figma.com/hc/article_attachments/31937315078679)

Note: Auto layout is only supported on frames. If you have a one or more layers selected, Figma will create an auto layout frame around them.

### Suggest auto layout

When you use **Suggest auto layout**, Figma will try to determine which objects in a frame or component should be placed in an auto layout frame, then adds as many auto layout frames as needed to make the full design responsive. These auto layout frames are created all at once, while attempting to preserve the placement of your designs.

This saves you time so that you don’t have to do the tedious work of adding auto layout frame-by-frame.

Note: Suggest auto layout can handle moderately-complex designs, such as cards, navigation bars, or mobile screens. If you’re working with a large or complex design, such as website, use suggest auto layout in batches.

You can access this option from a few places:

- Use the keyboard shortcut:
  - Mac: `⌃ Control` `⇧ Shift` `A`
  - Windows `⌃ Control` `Alt` `⇧ Shift` `A`
- Right-click the frame or object and go to **More layout options** > **Suggest auto layout**
- Select **Suggest auto layout** from the Actions menu

After you use this action, any nested auto layout frames that were created are indicated with a blue dot in the layers section in the left panel.

![A black mobile-sized frame sits on the canvas containing a design for a schedule app. The Actions menu opens, and the option for suggest auto layout is selected. The layers section of the left shows that multiple auto layout frames has been created for the design.](https://help.figma.com/hc/article_attachments/31727971107991)

Note: Occasionally, you may find an object in a different auto layout frame than you intended; or with a horizontal direction applied when you wanted vertical. Suggest auto layout might not get it right every time, but it is intended to speed up your workflow.

For elements that may be a bit trickier, we recommend framing, grouping, or using auto layout on nested elements before using **Suggest auto layout** on the parent frame.

## Remove auto layout

When you remove auto layout, you will have access to a frame's regular properties.

There are a couple of ways to remove auto layout:

- In the right sidebar, click  **Freeform** or  **Remove auto layout**
- Right-click on the frame and select **Remove auto layout**
- Use keyboard shortcuts:
  - Mac: `⌥ Option``⇧ Shift``A`
  - Windows: `Alt``⇧ Shift``A`

### Remove all auto layout in a selection

To remove auto layout from a frame and all of its nested objects at once, right-click on the frame and go to **More layout options** > **Remove all auto layout**.

**Note:** Auto layout cannot be removed from component instances. You will need to detach the instance from the component to make these edits, or update the main component.
# Create and manage prototype flows

Source: https://help.figma.com/hc/en-us/articles/360039823894-Create-and-manage-prototype-flows

---

Before you start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma)

Requires **can edit** access to a file

When prototyping in Figma, you can create multiple flows to test different parts of a user’s journey.

A **flow** is a collection of connected frames that make up a single prototype experience. For example, you can create a prototype for a shopping app that includes a flow for account creation, another for browsing items, and another for the checkout process–all in one page.

## Create a prototype flow

### Flow starting points

A flow starting point is where the flow begins. Flow starting points are set on [top-level frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma#01H8CWAD9EXJJWFQZYDAG3NYKQ).

When you [add a connection](https://help.figma.com/hc/en-us/articles/360040315773-Create-interactions) between two frames with no existing connections, Figma will create a starting point on the top-level frame where the connection started. Flow starting points are shown on the canvas with a  blue preview icon and the flow name.

A frame can only have one flow starting point.

![A connection is created from one frame to another. A flow starting point is added to the first frame.](https://help.figma.com/hc/article_attachments/31779384389911)

You can also manually create a flow starting point.

1. Select the starting frame.
2. Select the **Prototype** tab from the right sidebar.
3. Click the  plus sign in the **Flow starting point** section.

![Prototype tab showing option to add a flow starting point to Frame B with a plus sign for selecting it.](https://help.figma.com/hc/article_attachments/31779384395159)

To see all flow starting points on the current page:

1. Deselect any objects by clicking an empty part of the canvas.
2. Select the **Prototype** tab from the right sidebar.
3. From the **Flows** section, view a list of all flow starting points.
4. Hover over a flow name and click  **Select frame** to navigate to the frame where the starting point is located.

### Add or remove frames from a flow

Once you have a flow starting point, the rest of the flow consists of any frames that are connected to the starting point with prototyping interactions. This includes frames that are directly connected to the starting point, as well as frames that are connected through other interactions.

For example, all purple frames in the image below are included in **Flow 1**:

![Prototype flow showing connected purple frames in Flow 1; blue frame is part of both Flow 1 and Flow 2.](https://help.figma.com/hc/article_attachments/31779403495959)

To remove a frame from a flow, remove any prototype interactions that connect the frame to other frames in the flow.

Frames can be included in multiple flows. For example, the blue frame in the image below is included in both **Flow 1** and **Flow 2**:  
![Purple frames connected to a blue frame in Figma, showing inclusion in both Flow 1 and Flow 2.](https://help.figma.com/hc/article_attachments/31779384407447)

Once a user navigates to a frame that is included in multiple flows, they can use any interactions on that frame. This opens up the original flow to include any connections from that frame.

## Manage prototype flows

### Edit flow name

Once you've created a flow, Figma will name it **Flow 1** by default, with additional flows being **Flow 2**, **Flow 3**, and so forth. You can rename a flow at any time.

To rename a flow:

1. Select the starting frame.
2. Select the **Prototype** tab from the right sidebar.
3. From the **Flow starting point** section, select the flow name field.
4. Enter in a new flow name.

![Prototype flow with interconnected purple and blue frames and starting flow property being renamed in the sidebar.](https://help.figma.com/hc/article_attachments/31779384412951)

Once renamed, the flow name is displayed in the frame's blue starting point icon and the left sidebar in [presentation view](https://help.figma.com/hc/en-us/articles/360040318013-Preview-designs-and-prototypes-in-Presentation-View).

Tip: You can also rename a flow by double-clicking the flow starting point name directly on the canvas.

### Add flow description

Flow names and descriptions are displayed in the left sidebar when in presentation view. Use descriptions to provide prompts to usability test participants or additional context and documentation for your team. Descriptions can be formatted with bold text, numbered or bulleted lists, and hyperlinks.

To add a flow description:

1. Select the frame with the flow starting point.
2. Select the **Prototype** tab from the right sidebar.
3. From the **Flow starting point** section, click  **Edit description** next to the name of the flow you’d like to edit.
4. Add a rich text description.
5. Click X to exit the **Description** panel and save the description.

Once added, the description is displayed in the left sidebar in presentation view.

### Move flow starting point

By default, Figma uses the first connection you create as the flow starting point. You can move a starting point to another frame.

1. Find the blue starting point icon on the canvas.
2. Click and drag the flow name to a new starting frame.

![The starting point is dragged from one frame to another.](https://help.figma.com/hc/article_attachments/31779384416919)

### Delete flow starting point

To delete a flow starting point:

1. Select the frame with the flow starting point.
2. Select the **Prototype** tab from the right sidebar.
3. From the **Flow starting point** section, click  **Remove starting point**.

Tip: You can also delete a flow starting point by finding the blue starting point icon on the canvas, and clicking and dragging it off the frame to an empty part of the canvas.

## Play and share prototype flows

### Preview flows

You can preview your prototype flows directly in the editor, with an [inline preview](../view-prototypes/play-your-prototypes.md).

1. Deselect any objects by clicking an empty part of the canvas.
2. Select the **Prototype** tab from the right sidebar.
3. From the **Flows** section, view a list of all flows.
4. Hover over a flow name and click  **Preview** to open the inline preview.

From the inline preview, navigate through your flow by triggering each prototype interaction.

Tip: You can also open the inline preview by clicking the  blue preview icon on any flow starting point.

### Copy and share flow links

You can share prototype flows with others in order to get feedback on specific user flows or journeys. When you share a prototype flow, users can play the prototype in presentation view. From presentation view, users can also select any other flow to play.

From the canvas:

1. Select the frame with the flow starting point.
2. Select the **Prototype** tab from the right sidebar.
3. Hover next to the **Flow starting point** heading.
4. Click  **Copy link**.

From presentation view:

1. Select the flow you want to share from the left sidebar.
2. Click **Share prototype** in the toolbar.
3. Click **Copy link**.
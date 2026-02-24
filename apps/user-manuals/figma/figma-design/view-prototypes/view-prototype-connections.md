# View prototype connections

Source: https://help.figma.com/hc/en-us/articles/4411431245335-View-prototype-connections

---

Who can use this feature

Available on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with `can view` or `can edit` access access can view prototype connections and flows.

Anyone with can view or can edit access to the file can view prototype flows and connections. This applies to anyone who views or accesses the file without explicit edit permissions.

People with view access can see interactions between variants in a component set (interactive components). Viewers can only see variant interactions on main components, not instances.

**Note:** There isn't currently a way to share a file with prototype connections turned on by default for viewers.

## View access

Viewers can access all prototype connections on the current page, including any flows and starting points.

To view connections on another page, viewers can select another page in the left sidebar.

### Connections and interactions

1. Use the shortcut `⇧ Shift``E` to toggle the visibility of any prototype connections. Figma will show any connections between frames, as well as the starting points for any flows.
   - Frames can have connections related to multiple flows. To view details of a specific interaction, select the connection and not the frame.
   - If a starting frame has multiple connections, select the starting frame to view all connections and interactions.
2. View the connection details in the **Properties >** **Interactions** section of the right sidebar.
   - Type of interaction that [triggers](../guides/prototype-triggers.md) the flow.
   - [Prototype action](../guides/prototype-actions.md) and the destination.
   - Type of [prototype animation](../guides/prototype-animations.md). If this is an animation that supports a direction, you'll see the origin direction next to the animation name. For example, if the next frame comes from the right and moves left, Figma will show this as **Right**.
   - The [easing curve](https://help.figma.com/hc/en-us/articles/360051748654-Prototype-easing-curves) for the interaction. This can be a preset value, like **Ease out**, or a custom easing curve.
   - Duration of the animation in milliseconds (ms).

![An interaction noodle is selected on the canvas. The interactions panel shows details like 'On click, navigate to Frame 2', animate by 'Move in Right' with an "Ease out" curve lasting "300ms".](https://help.figma.com/hc/article_attachments/26978261634711)

**Tip:** You can also toggle prototype connections from the toolbar. Select [view settings](https://help.figma.com/hc/en-us/articles/360041065034) (current zoom percentage) and toggle **Prototyping** off or on.

### Prototype flows

View prototype flows in the [Properties tab of the right sidebar](../explore/design-prototype-and-explore-layer-properties-in-the-right-sidebar.md#h_01HKASPBBX9V0S5VA9F3XWRM2S).

1. Deselect all objects by clicking on a blank spot on the canvas.
2. Select **Properties** in the right sidebar.
3. View a list of any **Flows** on the current page.
4. Prototype connections are hidden by default for anyone with view access.
   - Select  to toggle visibility on.
   - Select  to toggle visibility off.
5. Hover over the flow to view the actions you can take:

   - Select  **Select frame** to select the starting frame in the canvas. This will also allow you to view details in **Interaction** section of the sidebar
   - Select  **Copy link** to copy link to clipboard
   - Select  **Preview** to open the flow in [inline preview](play-your-prototypes.md)

![](https://help.figma.com/hc/article_attachments/26978254346519)

## Edit access

If you have edit access to the file, you can view and edit any prototype flows and connections. This applies to any flows and starting points, as well as variant interactions on both main components and instances.

Anyone with edit access to the file can access prototyping settings in the right sidebar. The **Prototype** tab allows you to [view, edit, or create interactions and animations](https://help.figma.com/hc/en-us/articles/360040315773).

There are a few ways people with edit access can interact with prototype settings:

- Select **Prototype** tab in the right sidebar to enter prototype mode.
- Use the shortcut `⇧ Shift``E` to open the **Prototype** tab and view any connections.

**Note:** Figma won't display the inherited connections on the canvas by default. Select the instance to view its inherited connections.
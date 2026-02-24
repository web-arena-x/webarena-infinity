# Select layers and objects

Source: https://help.figma.com/hc/en-us/articles/360040449873-Select-layers-and-objects

---

Before you Start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with can view or can edit access to a file can select objects in the canvas or the Layers panel

Anyone with can edit access to a file can can select matching layers

Before you can update any properties associated with an object or layer, you will need to select it. We'll cover all the basics for selecting objects, as well as some lesser-known tips and tricks.

## Select individual layers

You can select layers in the canvas itself, or from the Layers panel. Click on an object in the canvas to select it.

![](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c803ff204286350d088b9d2/file-BqvCdNDvUc.gif)

### Select nested layers

If you're working on more complex designs, you may have objects nested within groups or frames.

We refer to nested objects as **children**, and the frames or groups that they nest within as **parents**. Learn more about [parent, child and sibling relationships](parent-child-and-sibling-relationships.md).

When you click on an object that is part of a group or frame, we'll select the parent by default.

**Double-click** on the object - or press the `enter` key - to select one level of nesting down. Repeat this process until you select the correct child elements.

### Deep select

If there are many levels of nesting, you can use **deep select** to select a nested child layer or the top-level frame. Hold down the modifier key to select the top-level frame or a nested layer or object by clicking it on the canvas.

- Mac: `⌘ Command`
- Windows: `Control`

### Select layer menu

There are a couple of different ways to select nested objects. The **Select Layer menu** allows you to choose which specific layer you'd like to select on the canvas.

1. Right-click to open the context menu.
2. Hover over the **Select layer** option.
3. Select a layer from a list of layers underneath the cursor's location. We show the layer name and icon in the same order as the Layers panel.

![](https://help.figma.com/hc/article_attachments/31672085673751)

**Tip:** Move between nested objects using the keyboard shortcuts:

- Select Child `enter`
- Select Parent `shift` `enter`
- Select Next Sibling `tab`
- Select Previous Sibling `shift` `tab`

### Layers panel

Every object in the canvas has a corresponding layer in the Layers panel.

Click the **Layers** tab in the left sidebar to open the layers panel. Or, use the keyboard shortcut:

- Mac: `Option` `1`
- Windows: `Ctrl` `1`

If you hover over the layer in the panel, a blue box will highlight that layer's location on the canvas.

Click on the layer name in the layers panel to select it.

If there are any frames or groups on the canvas, we will nest the child objects within the parent. Click the arrow next to a frame, group, or component to view any child layers.

**Can't see the layer highlight on hover?** Adjust your preferences in the menu: select **Preferences > Highlight on hover**.

## Select multiple layers

You can also select more than one object or layer at a time.

This is great when you want to:

- Update a property across more than one layer
- Resize layers in bulk
- Move a collection of objects
- Create a group, frame, or component from the selection

**Note:** When you select more than one layer, you can access **Selection Colors** in the right sidebar.

This allows you to update individual Fills, Styles and Strokes in a mixed selection. Learn more in our [View and adjust colors in a mixed selection](https://help.figma.com/hc/en-us/articles/360042553434) article.

### Canvas

1. Select an object in the canvas.
2. Hold `Shift` and click on another object.
3. This will allow you to select as many objects as you like.

![](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c8042572c7d3a0cb93253d5/file-TQrRIcwMNR.gif)

**Tip:** Click an object a second time while holding `Shift` to remove it from from the current selection.

### Selection marquee

The marquee tool allows you to select all objects in a specific area of the canvas.

1. Click and hold on an empty part of the canvas.
2. Drag the cursor across any objects you'd like to select.
3. A blue box will appear around each object are in the selection.
4. To select nested layers, hold down the modifier key and drag the marquee across the objects:
   - Mac: `⌘`
   - Windows: `Ctrl`
5. To remove an object from the selection, hold down the `Shift` key and click on the object.

![](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c8042ec04286350d088ba04/file-tAFIn9Cimd.gif)

**Note:** It's possible to select nested objects without selecting the parent object. This is something to be mindful of, especially when selecting objects to move them!

If you select a top-level frame, only other top-level layers will be selected.

When you select a parent object, this also selects any child objects. This allows you to move everything at once.

### Select multiple layers in the Layers panel

When you select layers in the Layers panel, there are some different rules:

To select **every layer between two layers**:

1. Click on the first layer to select
2. Hold `Shift`.
3. Select the last layer.
4. Figma will select every layer between those two layers in the Layers panel.

To select **individual layers**:

1. Click on the first layer to select
2. Hold down the modifier key
   - Mac: `⌘`
   - Windows: `Ctrl`
3. Select any other layers you want to select

![](https://help.figma.com/hc/article_attachments/31672205983895)

## Select matching objects

Matching objects are identical layers that exist across more than one frame or group.

You can select all matching objects at once to save time when editing or prototyping them. For example, many app designs use a search bar across the top of each frame. You can quickly select them and make edits to them at the same time.

[Learn how to identify matching objects →](https://help.figma.com/hc/en-us/articles/21523793229463/)

To select matching objects:

1. Select an object inside a frame or group. The frame or group should sit at the top-level on the canvas or inside a section.
2. Select matching layers using one of the following:
   - Click **Select matching layers** in the toolbar.
   - Keyboard shortcut:
     - Mac: `⌥ Option` `⌘ Command` `A`
     - Windows: `Alt` `⌃ Control` `A`
   - While pressing `⇧ Shift`, click and hold your cursor on the canvas and drag it over the matching frames to create a selection marquee. Only matching objects are added or removed from the selection.
   - While pressing `⇧ Shift`, click matching objects to add them to the selection. You won't need to double-click objects nested deep inside other groups or frames.

All selected objects are wrapped in a blue bounding box. You can then make edits to them all at once. [Learn how to edit objects in bulk →](https://help.figma.com/hc/en-us/articles/21635177948567/)

Note: Objects with sections can only match with other objects in that section.

## Select all layers

The **Edit** menu lets you select multiple objects based on their properties. This allows you to select all layers in your file that have the same properties.

This is helpful when you want to adjust the properties of all those layers at once.

1. Select a layer or layers in the **Layers panel.**
2. Go to the **File menu** and select **Edit** from the options.
3. Choose to **Select All** other layers that have the same:

   - Properties
   - Fill
   - Stroke
   - Effect
   - Text Properties
   - Font
   - or another Instance

   ![](https://help.figma.com/hc/article_attachments/360056940754)

**Want to select everything on the canvas?**

Use the keyboard shortcut `⌘ Command` / `Ctrl` `A`.

## Collapse all layers

When you expand a layer to reveal its nested layers, **Collapse layers** appears in the top right corner of the Layers panel. Click to collapse all expanded layers.

If you've already selected a layer when you collapse layers, all expanded layers except for your selection will collapse.

## Locked and hidden layers

If you hide a layer we won't show it in the **Select layer** menu. You will need to [toggle visibility on](https://help.figma.com/hc/en-us/articles/360041112614) to select it.

If you lock an object or layer, you can't select it via the normal left-click selection process. However, you can select it via the **Select layer** menu.

We include [locked layers](https://help.figma.com/hc/en-us/articles/360041596573) in the **Select layer** menu with a padlock icon.

**Tip:** [Smart Selection](https://help.figma.com/hc/en-us/articles/360040450233) allows you to select two or more objects in the canvas. From there you can adjust their arrangement, or the spacing between them.

Create a 1D Smart Selection from a list of objects that align on one axis, like a column or row. Or, a 2D Smart Selection of objects in a grid or gallery-like structure.

## Deselect objects or layers

To clear your selection entirely:

- Click anywhere on the canvas
- Use the keyboard shortcut: `Esc`

To remove an object from a selection:

- Hold down the `Shift` key and click on the object again

**Note:** If you click on a parent object, this will deselect the parent and any child objects within it.

To select the inverse of your current selection:

- Use the keyboard shortcut:

 Mac: `⌘` `A` `Shift`

 Windows:  `Ctrl` `A` `Shift`

This removes the current selection, then selects everything on the canvas you didn't select before.

## Select objects in view-only mode

For collaborators with `can view` access, the experience of selecting objects is a bit different.

When you make your selection on the canvas, Figma will:

1. Outline your selection using a solid purple box.
2. Outline the parent of your current selection using a dashed purple box.
3. Show the name of the selected layer(s) at the top of the **Properties** panel in the right sidebar.
4. If applicable, show the **Parent Component** underneath the selected layer in the **Properies** panel. Click the in the **Properties** panel to select the parent component.
5. Show the **properties**, **layout**, and **colors** for the selected layer.
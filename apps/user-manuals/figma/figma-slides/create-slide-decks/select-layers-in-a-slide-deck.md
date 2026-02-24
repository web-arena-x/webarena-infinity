# Select layers in a slide deck

Source: https://help.figma.com/hc/en-us/articles/27330413404567-Select-layers-in-a-slide-deck

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with at least `can view` access to a slide deck can select layers

Anyone with `can edit` access to a slide deck can select matching layers

You must select a layer before you can move it, duplicate it, or update any properties associated with it.

## Select individual layers

The **Move** tool lets you select and move layers on a slide. Select the **Move** tool in the toolbar or press `V` to enable it. Click on an layer on the canvas to select it.

![](https://help.figma.com/hc/article_attachments/27330547524503)

### Select nested layers

Slides with complex designs may have layers nested within groups or frames. We refer to nested layers as **children**, and the frames or groups that they nest within as **parents**. Learn more about [parent, child, and sibling relationships](../../figma-design/work-with-layers/parent-child-and-sibling-relationships.md).

When you select an object that is part of a group or frame, Figma Slides selects the parent layer by default. Double-click on the layer, or press `Enter`, to select one level of nesting down. Repeat this process until you select the correct child elements.

### Deep select

You can also use deep select to select a nested child layer. Hold down the modifier key and select the object by clicking it:

- **Mac:** `⌘ Command`
- **Windows:** `Control`

### From the Layers section

If you have access to [design mode](use-design-mode-in-figma-slides.md), you can view and select layers from the Layers section in the left sidebar. Every layer on a slide has a corresponding layer in the Layers section.

Note: Layers must be inside a slide to view them in the Layers section.

When you hover over a layer in the Layers section, a blue box will highlight that layer’s location on the slide. Click on the layer name to select it. If the layer contains nested layers, click on the arrow to view the child layers.

![](https://help.figma.com/hc/article_attachments/27330834630551)

## Select multiple layers

You can also select more than one layer at a time. This is great for when you want to:

- Update a property across more than one layer
- Resize layers in bulk
- Move several layers
- Create a group or frame from the selection

### From the canvas

1. With the **Move** tool enabled, select an layer on the canvas.
2. Hold down Shift and click on another object. Repeat to select as many objects as you like.
3. To remove a layer from the selection, hold down the Shift key and click on the layer again.

![Animation showing the selection of multiple layers.](https://help.figma.com/hc/article_attachments/27330929198487)

### Selection marquee

The marquee tool allows you to select all objects in a specific area of the canvas.

1. With the **Move** tool enabled, click and drag the cursor across any objects you’d like to select.A blue box will appear around each object are in the selection.
2. To select nested layers, hold down the modifier key and drag the marquee across the objects:
   - Mac: `⌘ Command`
   - Windows: `Control`
3. To remove a layer from the selection, hold down `Shift` and click on the layer.

### From the Layers section

To select a range of layers:

1. Select the first layer.
2. Hold down `Shift`.
3. Select the last layer.

Figma will select every layer between those two layers in the Layers section.

To select multiple individual layers:

1. Select the first layer.
2. Hold down the modifier key:
   - **Mac:** `⌘ Command`
   - **Windows:** `Control`
3. Select any other additional layers.

## Select matching layers

Matching layers are identical layers that exist across more than one slide. You can select all matching layers at once to save time when editing your presentation.

Matching layers are also used for:

- [Smart animate](use-slide-transitions.md#h_01J0VFSNHXH3TKDHTCF18NR8A4): Create advanced transitions between slides
- [Multi-edit text](https://help.figma.com/hc/en-us/articles/27336977187863): Edit text layers in bulk

### Matching layer requirements

**Matching layer names**

For most layer types, the layers must have the same name in order to match. The exception is text layers. Text layers don’t always require identical names. When you create a text layer, the name of the layer will reflect the content of the text itself. You can rename text layers by double-clicking on the layer name in the Layers section.

- If the text layers were explicitly renamed, the layer names must match.
- If the text layers weren’t explicitly renamed, their text styles must match. If there are multiple matching text objects, the best match will be selected based on the location of the text layer in the slide.

**Matching parent frame names**

If the layer is nested inside a parent frame, the parent frames must have matching names.

**Matching layer hierarchy**

If the layer is nested inside a parent frame, it must have the same position in the layer hierarchy across the frames.

### Select matching layers

1. Select a layer inside a slide.
2. Click **Select matching layers** in the right sidebar or se the keyboard shortcut:
   - Mac: `⌥ Option` `⌘ Command` `A`
   - Windows: `Alt` `Control` `A`

All selected layers are wrapped in a blue bounding box. You can then make edits to them in bulk.

## Select all layers

The **Edit** menu lets you select multiple layers based on their properties.

1. Select a layer.
2. Open the **Main menu**, hover over **Edit**, and then hover over **Select all with**.
3. Choose to select all other layers that have the same:
   - Properties
   - Fill
   - Stroke
   - Effect
   - Text properties
   - Font
   - Instance
   - Variant

![](https://help.figma.com/hc/article_attachments/27336734398359)

## Deselect layers

To clear your selection entirely, click on a blank area of the canvas or press `Escape` on your keyboard.

To remove an object from a selection, hold down `Shift` and click on the object.

Note: If you click on a parent object, this will deselect the parent and any child objects within it.

To select the inverse of your current selection, use the keyboard shortcut:

- **Mac:** `⌘ Command` `Shift` `A`
- **Windows:** `Control` `Shift` `A`

This removes your current selection and selects all the other slides in your deck.
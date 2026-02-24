# Frames in Figma Design

Source: https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma-Design

---

Before you start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file can create and edit frames

Frames are layers that act as containers to organize other layers—such as shapes, images, and text—into cohesive designs. You can even nest frames within other frames, allowing you to create more complex designs. Frames allow you to build everything from individual elements like icons or buttons, to entire website layouts and mobile app designs.

Frames that sit directly on the canvas are called **top-level frames**. Frames that contain other layers are called **parent** objects. Any layers or nested frames inside a parent frame are called **child** objects. Learn more about [the parent, child, and sibling relationship](../work-with-layers/parent-child-and-sibling-relationships.md).

Similar to other layer types, you can [adjust the properties of a frame](#h_01J1981B7AHRK7DX39NYD817VQ) including its dimensions and fill.

Frames also give you access to other features including [layout guides](https://help.figma.com/hc/en-us/articles/360040450513), [auto layout](https://help.figma.com/hc/en-us/articles/360040451373), [constraints](https://help.figma.com/hc/en-us/articles/360039957734), and [prototyping](https://help.figma.com/hc/en-us/articles/360040314193).

You can identify frames in the **Layers** panel of the left sidebar by the  frame icon.

![Image showing a frame in the Layers panel with a grid-like icon](https://help.figma.com/hc/article_attachments/26978254616727)

## Select the frame tool

Enable the  Frame tool by selecting it in the toolbar, or by using one of the keyboard shortcuts: `F` or `A`.

![Location of the frame tool as the second option in the Figma toolbar.](https://help.figma.com/hc/article_attachments/24793898578711)

## Create a frame

Once the **Frame** tool is selected, there are several ways to create frames:

- [Click on the canvas](#h_01JH5Y00ZHGVVK1N6P5ZWPGD09)
- [Use a frame preset](#h_01JH5Y0VVZJVB5AXYNYAHJRV3R)
- [Duplicate an existing frame](#h_01JH5Y20QY0BYP980T4GH4H42S)

### Click on the canvas

With the **Frame** tool selected, do one of the following:

- Click on the canvas to create a top-level frame. If this is the first top-level frame you’re creating during your current session in this file, the frame’s dimensions will be set to 100 x 100. Otherwise, the top level-frame will use the same dimensions of the last top-level frame you created.
- Click inside an existing frame to add a 100 x 100 nested frame.
- Click and drag on the canvas or in an existing frame to add a frame with custom dimensions.

**Tip:** You can also create a frame around existing objects using Frame selection. Select one or more layers, then use the frame selection keyboard shortcut:

- **Mac**: `⌥ Option` `⌘ Command` `G`
- **Windows**: `Ctrl` `Alt` `G`

### Use a frame preset

When the **Frame** tool is enabled, a list of frame presets become available in right sidebar. Click the arrow to expand the section and select a preset from the list. You can choose presets for popular device and asset templates:

- Phone
- Tablet
- Desktop
- Presentation
- Watch
- Paper
- Social Media
- Figma Community
- Archive

If you want to change a frame to a different preset, select the frame and use the **Frame** dropdown in the right sidebar to select a different frame preset.

### Duplicate an existing frame

There are two ways to duplicate an existing frame:

- **Quick-add**: With the **Frame** tool enabled, hover over an existing frame and pressing the + **plus** on either side of the frame. This will duplicate the frame and nudge other frames over to accommodate the new frame.![](https://help.figma.com/hc/article_attachments/29097254706455)
- **Duplication shortcut**: Select a frame and use the duplication keyboard shortcut `⌘ Command` `D` (Mac) / `⌃ Control` `D` (Windows). You don’t need to enable the **Frame** tool to use this method. Learn more about [duplicating options](../work-with-layers/copy-and-paste-objects.md#h_01J92HBF9A2T61H5YH99SGW24A).

For both methods, if your frame is in a section, the section will resize to accommodate the new frame.

You can also quickly create a blank frame of the same size by clicking the + **plus** on either side of the frame while holding the keyboard modifier:

- Mac: `⌥ Option`
- Windows: `Alt`

![](https://help.figma.com/hc/article_attachments/29097254713111)

## Frame properties

There are a few properties associated with frames. Frames support the following properties.

- **Corner Radius**: Round the corner of a frame to create softer edges.
- **Clip Content**: Hide any objects within the frame that extend beyond the frame's bounds.
- **Layout Guides**: Create guidelines to help with the visual structure to your designs.
- **Auto Layout:** Create dynamic frames that respond to their contents
- **Fill**: Apply a solid fill, gradient, [images](https://help.figma.com/hc/en-us/articles/360040028034) (PNG, JPEG, GIF, TIFF and WEBP) to a frame.
- **Stroke**: Add strokes to a frame to create a border or outline
- **Effects**: Add a shadow or blurs to a frame

### Extra functionality

Frames allow you to access extra functionality in Figma. You will need to use frames to use the following features or functions:

- **[Layout Guides](https://help.figma.com/hc/en-us/articles/360040450513 "Visual aids that give structure and coherence to your design. They can only be applied to Frames and help to keep objects aligned as you adjust the Frame. They are not visible on the final design or in exports.")**: Apply transparent uniform grids, columns, and/or rows to frames to provide visual structure
- [**Constraints**](https://help.figma.com/hc/en-us/articles/360039957734): Define how child objects respond when you resize a frame. Apply constraints to **objects** within a frame.
- **[Auto Layout](https://help.figma.com/hc/en-us/articles/360040451373)**: Add Auto layout to frames to create dynamic layouts that respond to their contents
- [**Prototyping**](https://help.figma.com/hc/en-us/articles/360040314193): Create interactive prototypes that move between frames in your canvas

A frame is a **parent** object. This means that it can control or influence any **child** objects you place within it.

[Learn more about parent/child relationships in Figma.](https://help.figma.com/hc/en-us/articles/360039959014)

Tip: You can hand off frames for development without reorganizing your file. [Create a section for your frame](https://help.figma.com/hc/en-us/articles/9771500257687), or convert the frame to a section. Then, [mark the section as **Ready for dev**](https://help.figma.com/hc/en-us/articles/9771500257687#h_01HHN2CDAMSCQ3XVSEA2JYSEQJ).

### Adjust properties of the frame

In the past, it was possible to adjust the properties of child objects when you selected the frame. Now, you can adjust the properties of the frame itself.

- Select a child object by using the keyboard shortcut: `Enter` or `Return`.
- Press the `Tab` key to select the next sibling.
- Press `Shift` + `Tab` to select the previous sibling.
- Press `Shift` + `Enter` to select the parent

If you want to adjust the fill and stroke properties of a frame and it's children, you can use **Selection colors** to [view or adjust colors in a mixed selection](https://help.figma.com/hc/en-us/articles/360042553434).

## Nest frames within other frames

In Figma, you can create frames within other frames. We call this process nesting. This allows you to combine frames with different properties to build complex interfaces.

This creates new hierarchies or relationships:

- **Top-level frames:** Any frame that is directly on the canvas. For a frame to be a top-level frame, you can't nest it within another frame, group, or object
- **Nested frame**: Any frame that is placed within another frame. You can place frames within top-level frames, or within other nested frames. Nested frames are both a parent and a child
- **Children:** Any object that is within a frame

[Learn more about parent, child, and sibling relationships.](https://help.figma.com/hc/en-us/articles/360039959014)

### Top-level frames

Figma **bolds** top-level frames in the layers panel and shows the name of any top-level frames on the canvas.

![Image showing a top-level frame in the canvas and layers panel.](https://help.figma.com/hc/article_attachments/26978261914391)

### Nested frames

Nested frames are frames that you place within another frame or object. This makes them both a parent and a child. You can place frames within:

- Top-level frames
- Other nested frames
- In groups

In our example below, each of our elements are in their own frame. We have a status bar at the top and a navigation menu at the bottom. We also have a card that includes the details of our Upcoming Tickets.

Using one of our device presets, we can create a top-level frame for our elements. We can add our elements to the top-level frame to build a single screen in our mobile app.

![Image of an example app design in the canvas, where you can see the individual frames by themselves on the left and then combined into a single frame on the right.](https://help.figma.com/hc/article_attachments/24436758037399)

## Resize frames

You can interact with frames like any other object on the canvas, including change the size or scale of frames. There are a few ways to change the size of a Frame:

### Drag the frame

Drag to resize a frame manually.

1. Select the frame in the canvas, or layers panel in the left sidebar.
2. Click the handle in one of the corners and drag to resize. Or, click one of the edges and drag.

**Tip!**To ignore any [constraints](https://help.figma.com/hc/en-us/articles/360039957734) on child objects, hold down the modifier key:

- Mac: `⌘ Command`
- Windows: `Ctrl`

### Change the frame preset

Select another frame preset to change the frame's size.

1. Select the frame.
2. In the Properties Panel in the right sidebar, select the frame field.
3. Select a preset from the list.
4. Choose presets for popular device and assets templates:
   - Phone
   - Tablet
   - Desktop
   - Presentation
   - Watch
   - Paper
   - Social Media
   - Figma Community
   - Archive
5. Figma will update your frame's dimensions to match the preset.

**Note:** If you have applied [constraints](https://help.figma.com/hc/en-us/articles/360039957734) to any child objects, Figma will resize them to match the new frame preset. Otherwise, objects inside the frame will stay at the original dimensions and position.

### Properties Panel

Update the Frame's **Width** and **Height** using the right sidebar.

Enter a new number in the **W**and **H** fields, or hover over the icon to scrub the field. Drag left to decrease and right to increase.

Select <icon> Lock aspect ratio next to the **W**idth and **H**eight fields to maintain the layer’s proportions while resizing it.![Lock aspect ratio option highlighted in the Layout section of the right sidebar, showing dimensions for width and height.](https://help.figma.com/hc/article_attachments/29799683542679)

**Tip:** You can use the dimension fields to perform calculations. This allows you to quickly scale or resize objects.

- `%` Percentage, such as 50%
- `+` Add, such as +100
- `-`  Subtract, such as -20
- `*`  Multiply, such as \*4
- `/`  Divide, such as /8

It's not possible to **multiply** a width or height by a **percentage**, for example \*50% will result in a value 50x the original, not 50%.

### Resize to fit

You can resize a frame so that it shrinks or grows to fit its child objects. This will redraw the frame around the outermost bounds of the objects within it.

- Use the keyboard shortcut:
  - Mac: `⌥ Option` `Shift` `⌘ Command` `R`
  - Windows: `Alt` `Shift` `Control` `R`
- Click in the **Layout** section of the right sidebar![Image showing the location of the resize to fit icon in the top-right corner of the Design tab in the right sidebar.](https://help.figma.com/hc/article_attachments/24436878068247)

## Ungroup a frame

To ungroup a frame, select the frame and press:

- Mac: `⌘ Command``Shift``G` or `⌘ Command``Delete`
- Windows: `Control``Shift``G` or `Control``Backspace`
# Resize, rotate, and flip objects in FigJam

Source: https://help.figma.com/hc/en-us/articles/1500006206242-Resize-rotate-and-flip-objects-in-FigJam

---

Before you start

- Available on any [team or plan](https://help.figma.com/hc/en-us/articles/360040328273)
- Anyone with `can edit` access in a FigJam file can resize objects
- Check out the [Guide to FigJam →](https://help.figma.com/hc/en-us/articles/1500004362321)

When you create a new object like a sticky note or shape, it's added at a default size to help keep your boards and diagrams looking uniform.

You can resize, scale, rotate, and flip (mirror) objects on your board as needed.

# Resize objects

Need a shape to pop a little more than the rest? Resize objects to make them larger, smaller, wider, shorter, or taller to customize their appearance.

Not all objects can be resized the same way. There are three ways objects can be resized in FigJam.

## Manual resizing

Change the width or height of an object. Manual resizing can change the aspect ratio of an object. To resize an object:

1. Click the object to select it.
2. Click and drag:
   - the right or left edge to change the object's width
   - the top or bottom edge to change the object's height
   - a corner handle resize the object in either direction or press `⇧
     Shift` to resize uniformly

You can resize a shape and truncate the text, then reveal it again in editing mode by clicking the blue arrow at the bottom of the shape.

![Resizing shape to truncate text with option to reveal full text using a blue arrow in FigJam.](https://help.figma.com/hc/article_attachments/4416058096151)

## Scale an object

Scaling changes the width and height at the same time while maintaining the same aspect ratio and scaling its contents proportionally. See [resizing by object type](#h_01F3HEZNFD0NV8QRR0M274W9PA) to see which objects support scaling. To scale an object:

1. Click the object to select it
2. Click and drag anywhere on the bounding box that surrounds it

## Automatic resizing

Some objects will change their size and dimensions as you change the content within them, or content they are connected to. You'll see automatic resizing when you:

- Add content to a sticky note so that it grows taller
- Change the size or weight of text to make it smaller or larger
- Drag a side border to widen a sticky note
- Move two shapes with a connector in-between so the connector will change position and grow to remain connected to those shapes
- Duplicate an object within a group **[Learn more about groups in FigJam →](https://help.figma.com/hc/en-us/articles/1500004414962)**

![A demonstration of a sticky note automatically growing vertically as text becomes too long.](https://help.figma.com/hc/article_attachments/1500011226442)

Scale vs. proportional resize

Scale maintains aspect ratio while the contents within them also scale proportionally in size. Objects that resize without scaling can maintain their aspect ratio by holding the `Shift` modifier key, but their contents won't scale.

# Resizing by object type

|  |  |  |  |
| --- | --- | --- | --- |
| **Type** | **Resizing** | **Scale** | **Automatic** |
| **[Sticky notes](https://help.figma.com/hc/en-us/articles/1500004414322)** | ✓ | ✓ | ✓ |
| **[Shapes with text](https://help.figma.com/hc/en-us/articles/1500004414382)** | ✓ | ✕ | ✕ |
| [**Doodles and highlights**](https://help.figma.com/hc/en-us/articles/1500004414442) | ✕ | ✓ | ✕ |
| **[Stamps](https://help.figma.com/hc/en-us/articles/1500004290981)** | ✕ | ✓ | ✕ |
| **[Connectors and straight lines](https://help.figma.com/hc/en-us/articles/1500004414542)** | ✕ | ✕ | ✕ |
| **[Images](https://help.figma.com/hc/en-us/articles/1500004290881)** | ✕ | ✓ | ✕ |
| **[Text](https://help.figma.com/hc/en-us/articles/1500004291281)** | Width only | ✕ | ✓ |
| **[Stickers and components](https://help.figma.com/hc/en-us/articles/1500004290841)** | ✓ | ✓ | [Yes, if auto layout applied](https://help.figma.com/hc/en-us/articles/360040451373) |
| **[Groups](https://help.figma.com/hc/en-us/articles/1500004414962)** | ✓ | ✕ | ✕ |
| [**Tables**](https://help.figma.com/hc/en-us/articles/12583849250199) | ✓ | ✕ | ✓ |

# Resizing tips

**Anchor points** are the part of the object a transformation action originates from. The anchor point remains in the same position, while the rest of the object transforms outward, away from that point.

FigJam will anchor a resizing action to the opposite edge/corner to the side that you drag. For example: If you click and drag from the top left corner, FigJam will anchor the resizing point to the bottom right corner of the shape. It will grow up and to the left.

- Hold `⇧ Shift` to resize uniformly in all directions
- Hold `⌥ Option` / `Alt` to make the center of the object the resizing anchor point and equally resize two opposing sides at the same time
- Hold both modifier keys `⇧ Shift` `⌥ Option` / `⇧ Shift` `Alt` to resize uniformly from the center

![The effects of resizing modifier keys demonstrated on shapes](https://help.figma.com/hc/article_attachments/1500011223302)

# Rotation

Some objects can be rotated around their center points in increments of 15 degrees. The following objects can be rotated:

- Shapes
- Text
- Images
- Marker tool doodles
- Highlights
- Stamps (slightly rotated by default)
- Components
- Groups

## To rotate an object

1. Click the object to select it
2. Hover your mouse near the object's corner until the  rotation cursor appears
3. Click and drag to rotate your selection

Note

The  rotation cursor won't appear if you select an inner layer of an object, like a text layer inside of a shape.

## Flipping

These objects can be flipped vertically over their X axis and/or horizontally over the Y axis:

- Images
- Marker tool doodles
- Highlights
- Stamps
- Components
- Parallelograms (horizontal only)
- Triangles (vertical only)
- Groups

![Using shortcuts to flip an image of a bird vertically and horizontally](https://help.figma.com/hc/article_attachments/1500011466101)

### Flip an object on the canvas:

1. Click the object to select it.
2. Flip the object using the shortcuts:
   1. `Shift` `V` to flip vertical
   2. `Shift` `H` to flip horizontal

### To flip an object from the menu:

1. Click the object to select it
2. Right-click the object to open its menu
3. Select between **Flip horizontal** or **Flip vertical** from the menu
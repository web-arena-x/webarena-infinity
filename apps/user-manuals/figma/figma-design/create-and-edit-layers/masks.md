# Masks

Source: https://help.figma.com/hc/en-us/articles/360040450253-Masks

---

Before you start

Who can use this feature

 

Anyone on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with edit access to a Figma Design file can use masks

Use masks to show specific areas of objects while concealing the rest.

It's like placing a photograph inside a picture frame with a small opening. You'll see a portion of the photograph peeking through the opening, while the rest is concealed without the need to trim it down to size.

Since no portion of masked layers are modified or deleted in this process, masks are a non-destructive action. This allows you to preserve the concealed areas without the need to trim them down to fit.

## How masks work

Any layer can be used as a mask, including vector shapes, text layers, images with transparency channels, groups, and more.

![](https://help.figma.com/hc/article_attachments/4402389611159)

When you use a layer as a mask, a **mask object** is created, which includes the mask and any layers it is masking. A mask object can be identified in the **Layers** section of the left navigation panel. The mask icon identifies the mask, with an upward-facing arrow along the layers that are being masked.

![Layers panel showing a mask group with masked objects in Figma, identified by an upward arrow and mask icon.](https://help.figma.com/hc/article_attachments/26978254466583)

Masks are positioned below masked layers on the z-axis. The mask applies to all siblings above it until it reaches:

- Another mask or mask object
- The mask's parent frame or group
- A frame or component with clip content on

[Learn more about parent, sibling, and child relationships](https://help.figma.com/hc/en-us/articles/360039959014).

In the example below, the purple ellipse is acting as the mask. If the mask sits below the image of the person on the z-axis, it'll successfully mask that image. If the mask sits above the image, it won't be masked.

![](https://help.figma.com/hc/article_attachments/4405156257815)

## Mask types

### Alpha

All masks in Figma support alpha channels. Alpha channels represent the degree of transparency, or opacity, in a color, image, or object.

When working with alpha masks, masks are applied based on the opacity of the mask. The higher the opacity, the more that is revealed. Zero percent opacity reveals nothing.

This means we can utilize blurs and opacity in our masks:

- Import existing PNGs, GIFs, and WebP files with transparency (alpha channels)
- Use layer blur effects to replicate feathering
- Apply drop and inner shadows to create depth
- Add fills, strokes, and gradients with varying opacity

In the example below, we've used an ellipse with an outside stroke as our mask. The opacity of the ellipse's fill is 100% and the opacity of the stroke is 30%. More is revealed in the center of the image, because the mask's opacity is higher (100%).

![A mask that has an outside stroke with 30 percent opacity](https://help.figma.com/hc/article_attachments/26978261775511)

### Vector

Vector masks, or using shape outlines as masks, ignore the translucency—or opacity value of more than zero percent—of a mask's fill or stroke. If a mask contains any area with an opacity of more than zero percent, then its outlines are used as the mask and the entire mask assumes 100% opacity.

In the example below, an image of a heart with a completely transparent background is being used as a mask. The object on the bottom-left is using an alpha mask, so we see the outline of the heart. The object on the bottom-right is using a vector mask, and uses the outline of the entire image as the mask.

![Heart-shaped image showing alpha mask on left and vector mask on right, illustrating Figma mask types.](https://help.figma.com/hc/article_attachments/26978254472599)

### Luminance

Luminance allows you to use brightness to determine a mask. The brighter the area of a mask, the more that is revealed, or in other words, the higher the opacity of the layers being masked.

The darker the area, the less that is revealed. If a mask has a black fill, or `#000000`, this will reveal nothing and masked layers render at zero percent opacity.

![Masked layer example showing a floral image masked over a purple layer, illustrating the masking effect.](https://help.figma.com/hc/article_attachments/26978254474647)

## Create and edit masks

### Create a mask

1. Choose an object you want to use as your mask, and place it behind all objects that'll be masked on the z-axis.
2. Select all layers that will be a part of the mask object.
3. From the right sidebar, select **More options** > **Use as mask**, or press: 
   - Mac: `⌃ Control` `⌘ Command` `M`
   - Windows: `Ctrl` `Alt` `M`

   Note: If you only have one layer selected, select **Use as mask** directly from the right sidebar.
4. Figma will create a mask group with all selected layers.
5. By default, the mask type is set to **Alpha**. To change it, select the layer being used as a mask and open the dropdown in the Mask section of the right sidebar. Hover over any option to preview it on the canvas. [Learn about mask types](#h_01GWJ59RYMZG5Y3R1HV43PEMXG).

![](https://help.figma.com/hc/article_attachments/26978261782807)

To add layers to an existing mask object, use the Layers panel to click and drag them into the mask object.

[Learn more about reordering layers](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-dimensions-rotation-and-position#Change_layer_order).

### Resize and move

Masks and masked layers move and resize independently from one another. This means that when you move or resize a mask, any masked layers will be unaffected, and vice versa.

![Layer panel showing a mask group with a triangle mask revealing portions of shapes underneath with some areas cut off.](https://help.figma.com/hc/article_attachments/26978254476951)

This is because they are siblings of one another, so masks don’t have any parenting behavior that a frame, group, or component might have.

[Learn more about parent, sibling, and child relationships](https://help.figma.com/hc/en-us/articles/360039959014).

### Remove a mask

To stop using an object as a mask, use any of the following methods to toggle it off:

- Select the mask and click  in the right sidebar
- Right-click the mask and select **Remove mask**
- Select the mask and use the keyboard shortcut:
 - Mac: `⌃ Control` `⌘ Command` `M`
 - Windows: `Ctrl` `Alt` `M`

Any portions hidden by the mask will reappear.

## Reveal mask outlines

By default, Figma does not show the boundaries of a mask. Use mask outlines when working with complex masks or to check for unintended empty spaces.

To toggle mask outlines:

1. Open the Figma menu.
2. Go to **View**> **Mask outlines**.

Once the setting on, masks in your file are outlined in green.

Note: If all layers being masked are hidden or have zero percent opacity, then the object's mask outlines won't appear.
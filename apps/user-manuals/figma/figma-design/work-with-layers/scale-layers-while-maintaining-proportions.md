# Scale layers while maintaining proportions

Source: https://help.figma.com/hc/en-us/articles/360040451453-Scale-layers-while-maintaining-proportions

---

Before you Start

Who can use this feature

 

Users on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Users with `edit access` to a Figma Design file can resize objects with the scale tool

Use the scale tool to proportionally resize layers and objects. This tool preserves aspect ratios and ignores [constraints](https://help.figma.com/hc/en-us/articles/360039957734) of any nested layers in order to scale them proportionally. Any blurs or strokes will scale as well.

Note: To preserve the aspect ratio on a layer without scaling it, you can [lock and unlock aspect ratio](https://help.figma.com/hc/en-us/articles/360039956914#aspect-ratio) on the layer.

You can scale any object, with the exception of [locked layers](https://help.figma.com/hc/en-us/articles/360041596573) and layers nested inside a component instance. Learn more about [instance overrides](https://help.figma.com/hc/en-us/articles/360039150733).

![Cursor using scale tool to proportionally resize an image on the Figma canvas, preserving aspect ratio.](https://help.figma.com/hc/article_attachments/24303550562839)

## Scale

To resize an object using the scale tool:

1. Activate the scale tool by pressing `K`**,** or by clicking in the toolbar and selecting **Scale**.
2. Select an object.
3. Scale the object by doing one of the following:
   - **Click and drag**: Hover over the object’s bounding box to make the cursor appear. Then, click-and-drag to resize.
   - **Scale multiplier**: Use the scale multiplier, in the **Scale** panel of the right sidebar. Open the dropdown to select a multiplier, or type a multiplier in the text field and press `Enter` / `Return` to apply.
   - **Dimensions fields:** Use either the width or height fields, in the **Scale** panel of the right sidebar. Type a number in either field and press `Enter` / `Return` to apply. The other dimension field will automatically update.

     ![Scale panel showing width 400, height 400, scale multiplier dropdown, and anchor point selector centered.](https://help.figma.com/hc/article_attachments/24303550566551)

## Set scale direction

The anchor box in the scale panel allows you to set which direction an object scales when using the scale multiplier or dimension fields.

You use the anchor box to set the object’s anchor point, which tells Figma which side of the object to stay put. Once you scale your object, it scales in the opposite direction of the anchor point.

For example, if the anchor point is set to center, the object’s center stays put and resizes in all directions. If you set the anchor point to the top-left, an object will resize down and to the right.

To change an object’s scale direction:

1. Activate the scale tool `K`.
2. Select the object.
3. Click on one of the anchor points in the anchor box.
4. Use the scale multiplier or dimension fields to scale the object.

![Anchor point for an image within a frame being moved using the anchor selector tool.](https://help.figma.com/hc/article_attachments/24303611959191)
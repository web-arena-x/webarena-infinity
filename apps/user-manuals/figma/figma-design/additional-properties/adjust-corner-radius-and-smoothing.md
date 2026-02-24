# Adjust corner radius and smoothing

Source: https://help.figma.com/hc/en-us/articles/360050986854-Adjust-corner-radius-and-smoothing

---

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file can adjust corner radius and smoothing

In interface design, we see rounded corners on screens, icons, buttons, and cards. It's easier for eyes to follow circles and curves, while sharp edges disrupt our line of sight.

Figma represents corner radius in (density-independent) pixels. You can adjust corner radius for an entire shape, or for each point in a vector object.

Figma has two features for creating rounded corners:

- **Corner radius:** Rounds the corner where two lines meet. Use this to create shapes with rounded corners.
- **Corner smoothing:** Adjusts a rounded corner to create a continuous curve. Use this setting to create "squircles".

Note: Rounded corners may not be available for rectangles you create with the pen tool or rectangles you edit in vector edit mode.

You can apply corner radius and smoothing to:

- Frames
- Rectangles, polygons, and stars
- Vector networks that are closed shapes
- Boolean operations that contain rectangles

Note: It's not possible to apply corner radius to lines, arrows, vector networks with only a single stroke, or boolean operations that only contain ellipses.

## Adjust corner radius for an entire shape

There are a few ways to adjust the corner radius for a vector object or shape.

Tip: Your Small nudge and Big nudge settings apply to corner radius too. Use the `←` and `→` keys to use your small nudge. Hold down `Shift` to use your big nudge settings with the arrow keys.

### Design tab

1. Select the layer.
2. Enter a pixel value in the **Corner radius** field in the right sidebar or hover your cursor over the icon, then click and drag left to reduce or right to increase.

![Rectangle selected on canvas with a corner radius input field in the sidebar set to 0, ready for adjustment.](https://help.figma.com/hc/article_attachments/31779413358487)

### Canvas

You can also adjust the corner radius for rectangles, stars, and polygons on the canvas.

1. Select the shape you want to update.
2. Hover over the corner you want adjust until the radius handle appears.
3. Drag to adjust the radius.

![An example phone layout with on canvas handles that are used to adjust the corner radius of the phone wallpaper. The handles appear as white circles with blue borders within the selection.](https://help.figma.com/hc/article_attachments/31779390027799)

## Adjust the radius of an individual corner

By default, Figma applies corner radius to the entire shape. There are a few ways to adjust the corner radius for individual corners.

Caution: It's not possible to adjust an individual corner's radius in an instance. This is something to think about when setting corner radius for components.

### Independent corners setting (rectangles and frames only)

1. Select the rectangle or frame you want to update.
2. Click **Independent corners** in the right sidebar.
3. In the **Corner radius details** panel, you can:
   - Enter a pixel value for each corner
   - Click **Apply variable** in any of the four corner radius fields to [apply a number variable](https://help.figma.com/hc/en-us/articles/15343107263511)
   - Use the slider to adjust [corner smoothing](adjust-corner-radius-and-smoothing.md#Corner_smoothing_for_squircles)

![Corner radius and smoothing settings in the corner radius details modal for a selected rectangle, showing adjustable values and options.](https://help.figma.com/hc/article_attachments/31779390031383)

### Canvas (rectangles only)

You can also adjust the corner radius for an individual corner in the canvas. This only applies to rectangles.

1. Select the shape you want to update.
2. Hold down the modifier key to adjust a single corner.
   - Mac: `⌥ Option`
   - Windows: `Alt`
3. Hover over the corner you want adjust until the radius handle appears.
4. Drag to adjust the radius.

![The cursor hovers over one of the corner radius handles, a white circle with a blue border, in the upper left corner of an example design.](https://help.figma.com/hc/article_attachments/31779413368343)

### Vector edit mode (shapes only)

1. Select the shape you want to update.
2. Double-click on the shape or press `Enter` or `Return` to enter vector edit mode.
3. Select the individual point on the canvas.
4. Adjust the corner radius using the field in the right sidebar.
5. Enter a pixel value in the **Corner radius** field or hover your cursor over the icon, then click and drag left to reduce and right to increase.

# Corner smoothing for squircles

Designers noticed a difference in the rounded corners of iOS7 app icons. This corner smoothing created a seamless continuous curve that regular rounded corners couldn't.

We refer to shapes that use this particular effect squircles. A shape that's somewhere between a square and a circle. We still see squircles in Apple's later designs, including OS14.

There's quite a bit of mathematics that goes into a squircle. Learn more about [one Figma engineer's search for squircles](https://www.figma.com/blog/desperately-seeking-squircles/).

![Comparison of corner radius with 34 pixels and corner smoothing at 0% versus 100%, showing effect on curve. The 0% example is dark blue. The 100% is orange and overlays the 0% example. The 0% example is partially visible below the 100% example.](https://help.figma.com/hc/article_attachments/31779413370007)

## Adjust corner smoothing

You can apply corner smoothing to any shape you can apply corner radius to. Unlike corner radius, you can only apply corner smoothing to the entire shape.

1. Select the layer you want to update.
2. Open the **Design** panel in the right sidebar.
3. Click the **Independent corners** icon to open the **Corner radius** panel.
4. Use the slider to adjust corner smoothing or click `iOS` to set corner smoothing to 60%, the default for iOS.
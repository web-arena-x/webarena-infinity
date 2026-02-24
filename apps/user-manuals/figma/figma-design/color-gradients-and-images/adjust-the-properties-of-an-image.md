# Adjust the properties of an image

Source: https://help.figma.com/hc/en-us/articles/360041098433-Adjust-the-properties-of-an-image

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

Anyone with `can edit` access to a file can adjust image properties

You can use the image properties to adjust how an image looks in your designs.

## Access the image properties

To access the image properties:

1. Select a layer that uses an image as its fill or stroke.
2. Click the swatch in the **Fill** or **Stroke** section of the right sidebar to open the [color picker](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker).
3. Use the settings to adjust the image properties.

![Selected image fill with adjustment options in right sidebar.](https://help.figma.com/hc/article_attachments/34350348470551)

## Fill mode

The Fill mode determines how Figma will apply the image fill. This takes into account the dimensions of the image and the layer you’re adding it to. Figma retains your Fill mode setting when you scale or manipulate the layer.

There are four Fill modes:

- **Fill:** Positions and scales the image so that it takes up the entire layer it’s applied to. If the image and layer are different shapes, Figma may clip the image to ensure the shape is completely filled.
- **Fit:** Ensures the entire image is visible within the layer. This ensures that no part of the image is hidden, even if you resize the layer. Depending on the shape of the layer, the image may not completely fill the object.
- **Crop:** Allows you to adjust the boundary lines of your image. This lets you control which part of the image you can see. Cropping is a non-destructive action that works similarly to [using a mask](../create-and-edit-layers/masks.md). Learn more about [cropping images](crop-an-image.md).
- **Tile:** Creates a repeated pattern of the original image, filling the entire layer. You can adjust the size of the tile using the percentage value. Figma bases this on a percentage of the image's original dimensions.

![Dropdown menu in Figma image panel showing Fill mode options: Fill, Fit, Crop, Tile, with an image of a bird.](https://help.figma.com/hc/article_attachments/34350300407575)

### Images that scale

Because Figma applies images as fills, it’s not possible to adjust the scale or dimensions of the image itself. However, you can scale the object the image fills. Figma will scale and position the image based on the fill mode you selected.

The example below demonstrates how an image set to **Fill** will scale when the object it’s applied to is resized.

![An example of how an image fill scales when an object is resized](https://help.figma.com/hc/article_attachments/34350300410903)

## Rotation

You can use the  **Rotate 90º** setting to rotate an image fill clockwise in 90º increments. This won’t affect the orientation of the object itself, just the image fill within it.

**Note:** You can use the Crop settings to freely rotate an image fill instead. Learn more about [cropping images](crop-an-image.md).

![An example of how an image fill rotates](https://help.figma.com/hc/article_attachments/34350300416279)

## Image adjustments

You can use the adjustment sliders to modify how an image appears. These work similarly to filters you would see in photo editing software. Drag the handle to the left to apply a negative adjustment, or to the right to apply a positive adjustment.

Adjustments do not permanently alter the image and you can reverse or update these settings at any time.

![Image adjustment panel with sliders for exposure, contrast, and other properties applied to an image of a bird.](https://help.figma.com/hc/article_attachments/34350300419735)

### Exposure

Traditionally, exposure indicates how much light reaches the sensor within a camera. Decrease the exposure to create a darker image, or increase it to add more light.

![Demonstration adjusting exposure using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350300422551)

### Contrast

Contrast refers to the difference between light and dark pixels within an image. Decrease the contrast to narrow the range of colors and create a muted image, or increase it to create a more vivid image with brighter highlights and shadows.

![Demonstration adjusting contrast using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350300426263)

### Saturation

Saturation allows you to adjust the intensity of colors within an image. Decrease the saturation completely to create a black and white image, or increase it to create an image with more intense, saturated colors.

![Demonstration adjusting saturation using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350348489879)

### Temperature

Temperature refers to the tone of an image. Decrease the temperature to create “cooler” images with blue undertones, or increase it to create “warmer” images with amber undertones.

![Demonstration adjusting temperature using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350300429975)

### Tint

Tint allows you to tint the colors within an image. Decrease the tint to make the image appear more green, or increase it to make the image appear more magenta.

**Note:** You can use Temperature and Tint together to adjust the white balance of the image.

![Demonstration adjusting tint using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350300433687)

### Highlights

This allows you to isolate and adjust only the lighter areas of an image. You can use this to create more distinction between an image’s highlights and shadows. Decrease this setting to reduce the amount of light in the highlights, or increase it to create even brighter highlights.

![Demonstration adjusting highlights using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350300436759)

### Shadows

This allows you to isolate and adjust only the darker areas of an image. You can use this to create more distinction between an image’s highlights and shadows. Decrease this setting to reduce the level of light and create deeper shadows, or increase it to add more light and create brighter shadows.

![Demonstration adjusting shadows using the slider to enhance the bird image on the canvas.](https://help.figma.com/hc/article_attachments/34350348507159)
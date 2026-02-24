# About color models

Source: https://help.figma.com/hc/en-us/articles/360043042113-About-color-models

---

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file can use the color picker and select a color model

Figma allows you to see colors across five color models: Hex, HSB, HSL, CSS, and RGB. Switching between color models only affects how Figma describes colors. It doesn't affect how Figma renders them.

**Color profiles** affect how Figma renders colors. You can choose between sRGB or Display P3 as your default color profile, as a design file's color profile, or for exporting assets. Learn more about [color profiles and color management](https://help.figma.com/hc/en-us/articles/360039825114).

![Image showing five color pickers with the same color represented in each color model](https://help.figma.com/hc/article_attachments/360056934834)

## Available color models

By default, Figma represents color values using the **Hex** model. You can also view color notation for other models in the [color picker](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker).

### Hex

Hex is the default color model in Figma and refers to the Hexadecimal color. This is an alphanumeric shorthand representative of the RGB values.

Creators in web or digital design refer to the notation for this color model as hex codes.

Hex values have 8 characters and use the following syntax:

`#RRGGBBAA`

- The RR represents the red component.
- The GG represents the green component.
- The BB represents the blue component.
- The AA represents the alpha component. An alpha value of 00 represents a fully transparent color, and an alpha value of FF represents a fully opaque color.

### RGB

RGB or **R**ed **G**reen **B**lue is the most commonly used color model.

Every color that is rendered on a monitor or screen will be made up of varying amounts of **R**ed, **G**reen, and **B**lue.

RGB values are in the following syntax:

`(red, green, blue, alpha)`

- Red, green, and blue values define the intensity of the color with an integer between 0 and 255
- The alpha value defines the opacity as a number between 0.0 (fully transparent) and 1.0 (fully opaque)

### HSB

**H**ue **S**aturation **B**rightness is an alternative representation of the RGB model.

This is based around how the *human eye* perceives color, versus how a display would (in RGB).

HSB values are in the following syntax:

`(hue, saturation, brightness, alpha)`

- The hue value is measured in degrees, and is represented with an integer from 0 and 360
- The saturation value is represented with an integer from 0 to 100, with 100 being the most saturated
- The brightness value is represented with an integer from 0 to 100, with 100 being the brightest
- The alpha value defines the opacity as a number between 0.0 (fully transparent) and 1.0 (fully opaque)

### HSL

**H**ue **S**aturation **L**uminance is another color model based around how the human eye perceives color.

Like HSB, it is an alternative representation of the RGB model. The main difference between HSB and HSL is how saturation and lightness are treated.

HSL values are in the following syntax:

`(hue, saturation, luminance, alpha)`

- The hue value is measured in degrees, and is represented with an integer from 0 and 360
- The saturation value is represented with an integer from 0 to 100, with 100 being the most saturated
- The luminance value is represented with an integer from 1 to 100, with 100 being the lightest
- The alpha value defines the opacity as a number between 0.0 (fully transparent) and 1.0 (fully opaque)

### CSS

The CSS color model allows you to view or enter RGBa values using CSS syntax.

CSS values are in the following syntax:

`rgba(red, green, blue, alpha)`

- Red, green, and blue values define the intensity of the color with an integer between 0 and 255
- The alpha value defines the opacity as a number between 0.0 (fully transparent) and 1.0 (fully opaque)

**Want to communicate colors to a developer or engineer?** The CSS model lets you copy CSS-friendly notation for the selected color. This lets you paste this directly into a stylesheet, formatting included. Learn more about [developer handoff](https://help.figma.com/hc/en-us/articles/360040521453-Share-designs-with-Developer-Handoff).

## View and adjust color model values

You can view and update colors across different color models using the [color picker](update-fills-using-the-color-picker.md).

1. Select a layer.
2. Click on the swatch in the **Fill** or **Stroke** section of the right sidebar to open the color picker.
3. Use the dropdown below the Hue and Opacity sliders to view the current color model or select a new one.
4. Figma will shows values in the notation you selected.

![View color models from the color picker.](https://help.figma.com/hc/article_attachments/34328552407063)

You can also adjust colors by inputting the values directly in the available fields:

- RGB, HSL, and HSB color models have a separate percentage field for alpha values
- The CSS model must include an alpha value as a number between 0.0 and 1.0
- For Hex, you can either:
  - Input a 6-digit hex code and use the separate percentage field for adjusting the alpha value
  - Input an 8-digit hex code that includes the alpha value as the last two digits
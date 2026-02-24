# Overview of variables, collections, and modes

Source: https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes

---

Before you Start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

The number of modes you can create per collection [depends on your plan](https://help.figma.com/hc/en-us/articles/360040328273)

Looking for more resources on variables? Check out our [guide to variables](https://help.figma.com/hc/en-us/articles/15339657135383).

Variables are raw values—like color, numbers, and strings—that can change in value depending on the context of a design, such as light and dark modes, or mobile and desktop modes.

Like styles and components, variables can also be published to team libraries. When you update the value of a variable, you can update designs across files accordingly. This helps to create consistent designs across projects and makes updating design systems more efficient.

## Types of variables

There are four types of variables. Each one can be applied to specific properties and elements.

|  |  |
| --- | --- |
| **Variable type** | **Defined by** |
| Color | Solid fills |
| Number | Number values |
| String | Text strings |
| Boolean | True, false values |

### Color variable

Color variables use solid color values, such as `#000000` or `#FFCD29`.

They are great for handling theming, such as Dark and Light modes. They can also help you organize your brand's color palette. If you have a complex design system and wish to implement design tokens, you can alias color variables to do so.

Color variables can be applied to:

- [Color styles](https://help.figma.com/hc/en-us/articles/360038746534)
- [Fill colors](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker)
- [Gradient stops](https://help.figma.com/hc/en-us/articles/360041003694)
- [Shadow effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-shadow-or-blur-effects)
- [Stroke colors](../additional-properties/apply-and-adjust-stroke-properties.md#paints)
- Other color variables

### Number variable

Number variables use number values such as `24` or `-8`. You can use whole numbers or any decimal number up to the hundredth place, such as `12.75`.

They are great at handling responsive designs and varying text properties between different languages. You can also number variables inside text styles so that you have reusable pre-defined styles so you don’t have to memorize which property combinations go together.

Certain properties have a smaller range of numbers they support. Check the toggle below for details.

Number variables can be applied to:

- [Corner radius and individual corner radius](../additional-properties/adjust-corner-radius-and-smoothing.md)
- [Dimensions, including minimum and maximum width/height](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-and-position)
- [Font properties](https://help.figma.com/hc/en-us/articles/360039956634)  
  - Font size
  - Font weight (numbers only, e.g. 400, 700)
  - Line height
  - Letter spacing (interpreted as Px, not %)
  - Paragraph indent
  - Paragraph spacing
- Layer opacity (numbers >100 will default to 100)
- [Layout guides](https://help.figma.com/hc/en-us/articles/360040450513-Create-layout-grids-with-grids-columns-and-rows)
  - Uniform grid size
  - Row and column count (whole numbers only)
  - Width, height, margin, offset, and gutter
- [Padding and gap between](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties#h_01HB9Q13716VY5NF7AC5XHK9KD)
- [Shadow and blur effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-shadow-or-blur-effects): X, Y, blur and spread values
- [Stroke weight](../additional-properties/apply-and-adjust-stroke-properties.md): all, top, bottom, left, and right
- Text content
- [Text styles](https://help.figma.com/hc/en-us/articles/360039957034)
- Other number variables

### String variable

String variables use a sequence of characters such as `Inter`, `Hello world!`, or `94102`. They're great for switching languages between different localized designs, combining with other variables to create text styles, and switching component variants in prototyping.

String variables can be applied to:

- [Font properties](https://help.figma.com/hc/en-us/articles/360039956634)  
  - Font family
  - Font style and weight (name only, e.g. regular, bold, black italic)
- [Layer visibility](../work-with-layers/toggle-visibility-to-hide-layers.md), if the string has a value of “true” or “false”
- Text content
- [Text styles](https://help.figma.com/hc/en-us/articles/360039957034)
- [Variant instances in prototyping](../advanced-prototyping/use-variables-in-prototypes.md#h_01H91B3F52N6YVB3RG3RG0GSGS)
- Other string variables

Tip: Be sure to use exact spelling when creating string variables for font family and font style or weight. However, Figma will recognize the value if it includes hyphens (-), underscores (\_), different casings (DM Sans, dm sans), and with or without spaces.

### Boolean variable

Boolean variables use `true` and `false` values. They are great for hiding and showing layers for specific contexts of your designs.

Boolean variables can be applied to:

- [Instances with variant property](../advanced-prototyping/use-variables-in-prototypes.md#h_01H91B3F52N6YVB3RG3RG0GSGS) with true and false values
- [Layer visibility](../work-with-layers/toggle-visibility-to-hide-layers.md)

## Tokens and aliasing

A variable can reference another variable. That is, you can apply a variable to another variable. Also called, "aliasing," this gives you the ability to implement design tokens.

Any variable can reference another variable of the same type. For example, color variables can reference other color variables. Text variables can reference other text variables. Learn how to [alias variables](https://help.figma.com/hc/en-us/articles/15145852043927#alias).

## Collections and groups

Both collections and groups are used to organize variables and make them easier to find.

A collection is a set of variables and modes. Collections can be used to organize related variables together. For example, use one collection to localize text in different languages, and another collection for spatial values.

You can further organize variables by adding them to groups within a collection. For example, use one group for colors used for text, and another for colors used on strokes.

![Example of a collection with groups of color variables nested inside it. ](https://help.figma.com/hc/article_attachments/30211233510039)

Note: You can create up to 5,000 variables per collection.

## Variable modes

A mode is a list of values for a variable in a collection, storing one value per variable. Modes also represent the different contexts of our designs.

If a variable has multiple definitions, each definition is associated with a mode. When the variable is applied to a layer's property, the layer expresses the value based on the mode it's currently in, allowing us to quickly switch our designs between contexts.

![Animation of mode switching where an example product page for an ecommerce site switches from light mode to dark mode and all the colors instantly update](https://help.figma.com/hc/article_attachments/30211233511959)

For example, we might have a color variable storing two color values: a blue color under one mode, and a white color under a different mode. We apply this variable to a text layer, which will either appear as blue or white depending on the mode it’s in.

Here are a few ways you can use modes to switch contexts:

- Different color themes, like light and dark modes
- Different languages to see how copy flows in designs
- Devices sizes to see how elements look with different spacing and padding

Learn how to [switch design contexts with variable modes](https://help.figma.com/hc/en-us/articles/15343816063383).

## Considerations

### Styles and variables

Both variables and styles act as a source of truth and can be reused throughout designs for efficiency and consistency.

When deciding whether to use a variable or style, keep in mind:

- A style is great for creating a composite of values. Also, styles cannot be used in other styles or variables.
- Variables can be used to create multiple modes—such as light and dark modes. Also, variables can be applied to styles and other variables, allowing the ability to implement design tokens.

Learn the difference between [styles and variables](https://help.figma.com/hc/en-us/articles/15871097384471).

Ready to continue your variables journey? Learn how to [create and manage variables.](https://help.figma.com/hc/en-us/articles/15145852043927/)
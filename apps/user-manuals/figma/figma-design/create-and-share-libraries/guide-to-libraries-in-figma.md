# Guide to libraries in Figma

Source: https://help.figma.com/hc/en-us/articles/360041051154-Guide-to-libraries-in-Figma

---

Before you start

Who can use this feature

Available on all [paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

In Figma, a library is a collection of design assets, like components, styles, and variables. These design assets live in a single file, but can be reused across different files or projects.

People often use libraries for sharing common design elements, like buttons, icons, pieces of UI, colors, or values for certain properties. This helps everyone stay consistent and makes it easy to build from existing designs.

When someone changes assets in a library, people can quickly review the changes and automatically update their designs.

#### Example

Here’s an example of how a design team working on the fictional app Habitz might use libraries in Figma:

1. In a file, Kai creates components for different parts of the app, like the nav bar, menu, header, and other UI elements.
2. They publish finalized components as a library from within the file.
3. Working in a different file in the same project, Timothy views the library and adds a few components to the canvas.
4. Some time later, Kai makes an update to one of the components in file where the library was published.
5. In all other files that use the component, people working in the file get notified there's an update available to the component. People can review the component, and accept the update when they’re ready. The update gets applied to any instances of the component they’ve used.

Want to learn more about Kai and the Habitz team? You can follow their journey to launching a design system in Figma’s [Introduction to design systems course →](https://help.figma.com/hc/en-us/articles/14552901442839)

### Create components, styles, or variables to use in a library

The goal of a library is to share reusable design assets with other people you work with. These assets can be components, styles, or variables. Select a tab to learn more about each one.

Components Styles Variables

Components are the building blocks of a design.

They can be individual elements, like icons or buttons, or a collection of elements, like menus and layouts.

When using libraries, the library file contains the **main component**, which defines the properties of the component for everyone to use.

When you access a library in your file, you can add an **instance** of the component to the canvas. This instance will receive any updates made to the main component.

[Learn how to create components in your designs.](https://help.figma.com/hc/en-us/articles/360038663154)

Styles define a collection of properties or settings we want to reuse. For example, you can use styles to:

- Capture specific color values for fills and strokes
- Define text properties like font, line height and letter spacing
- Make presets for shadow and blur effects
- Create shareable scaffolding in the form of rows, columns, and layout guides

[Learn more about creating styles for colors, text, effects and layout guides.](https://help.figma.com/hc/en-us/articles/360038746534-Create-styles-for-colors-text-effects-and-layout-grids)

Variables store reusable values you can apply to all kinds of design properties.

For example, you can:

- Create [design tokens](https://help.figma.com/hc/en-us/articles/18490793776023.html#what-are-tokens) for better efficiency when managing design systems
- Switch a frame between different device sizes and see spacing immediately update according to a defined spatial system
- Preview how different languages affect a design
- Create a fully functional checkout cart design that calculates order total based on which items were added to the cart
- Build a prototype of an interactive quiz that uses conditional logic to show whether a user answers a question correctly or incorrectly

[Learn more about variables.](https://help.figma.com/hc/en-us/articles/15339657135383)

### Publish a library

Before you can access components, styles, or variables in other files, you need to publish them as a library. You can choose which ones to publish, and on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273), who can have access to them.

If you change a published style, component, or variable, Figma will only apply the changes to instances in the current file. If you want those changes to be reflected in your library, you will also need to publish those changes to the library.

- [Publish styles, components, and variables to a library](https://help.figma.com/hc/en-us/articles/360025508373)

### Choose which libraries to use in your files

You can access published libraries in any draft files or team files where you have `can edit` access. Admins can set default libraries for a team or organization, which automatically enables them in every file.

- [Enable access to libraries in your drafts](https://help.figma.com/hc/en-us/articles/360038743434)
- [Enable or disable a library in a design file](https://help.figma.com/hc/en-us/articles/1500008731201-Manage-libraries-in-design-files)

Don't have a library to use? Start building designs with [UI kits](https://help.figma.com/hc/en-us/articles/24037724065943) instead.

### Use library assets in a file

When you’ve found a library you want to use, you can add any components, styles, or variables to your file by following the instructions for each resource:

- [Create an instance of a component](https://help.figma.com/hc/en-us/articles/360039150173)
- [Apply styles to layers and objects](https://help.figma.com/hc/en-us/articles/360040316193-Apply-Styles-to-layers-and-objects)
- [Apply variables to designs](https://help.figma.com/hc/en-us/articles/15343107263511)

### Accept updates to a library in your files

When someone publishes an update to a **main component**, **style,** or **variable** in a library, Figma makes the update available in every file where the component, style, or variable is used.

Anyone with `can edit` access to a file can review and accept or ignore the changes.

- [Accept updates from a library](https://help.figma.com/hc/en-us/articles/360039234193)

### Manage a library

People with `can edit` access to a library file can set permissions to the file, unpublish the library, and move assets between files.

- [Manage libraries in teams](https://help.figma.com/hc/en-us/articles/360039234953)
- [Manage a library for a workspace or organization](https://help.figma.com/hc/en-us/articles/21310245473815)
- [Move published components between files](https://help.figma.com/hc/en-us/articles/4404848314647/)
- [Unpublish a library](https://help.figma.com/hc/en-us/articles/360039236853)

##
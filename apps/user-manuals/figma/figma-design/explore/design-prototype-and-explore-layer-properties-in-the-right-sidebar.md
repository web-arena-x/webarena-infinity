# Design, prototype, and explore layer properties in the right sidebar

Source: https://help.figma.com/hc/en-us/articles/360039832014-Design-prototype-and-explore-layer-properties-in-the-right-sidebar

---

Before you start

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

Requires `can edit` access to a file to adjust layers and prototype from the properties panel

Requires `can view` access to a file to comment, explore file and layer properties, and export layers from the properties panel

In Figma Design, a file has three main interface elements that are detached from the canvas:

- The [navigation panel](https://help.figma.com/hc/en-us/articles/360039831974) on the left side of the screen
- The [toolbar](https://help.figma.com/hc/en-us/articles/360041064174) at the bottom of the screen
- The properties panel on the right side of the screen

In this article, we're going to explore the properties panel.

### How the properties panel changes based on your access to a file

The properties panel has different capabilities depending on your level of access to a file, and your [seat type](https://help.figma.com/hc/en-us/articles/360039960434).

- [Edit access](#h_01J0SSEHX3QKNPT5VJ22JT7Q6M): Edit the design properties of layers, and add prototype flows and interactions
- [View-only access](#h_01J0SST9V85MJE7T08EXXVNG47): View and search comments, inspect layer properties and code output, and export

## Use the properties panel with edit access

![Figma properties panel showing Design and Prototype tabs with options. With the Design tab selected, you can adjust design properties for a layer. With the Prototype tab open, you can choose from prototype settings.](https://help.figma.com/hc/article_attachments/31937313497879)

There are two tabs available in the properties panel when you have edit access to a file: **Design** and **Prototype**.

**Tip**: You can add labels to the properties panel to make it clearer what each property does. To turn on labels, click the  dropdown menu next to the 100% zoom percentage in the properties panel and select **Property labels**.

### **Design**

The **Design** tab lets you view, add, remove or change the properties of objects within your design.

If nothing is selected on the canvas, you'll be able to do the following from the **Design** tab:

- Access styles and variables that are local to the file
- [Update the background color of the canvas](https://help.figma.com/hc/en-us/articles/360041064814)
- Export the entire page

When you select a layer, you can access many different property controls for editing the layer. For example:

- [Alignment, rotation, and position](https://help.figma.com/hc/en-us/articles/360039956814)
- [Frame size and orientation](https://help.figma.com/hc/en-us/articles/360041539473)
- [Corner radius](../additional-properties/adjust-corner-radius-and-smoothing.md)
- [Constraints](https://help.figma.com/hc/en-us/articles/360039957734)
- [Layout guides](https://help.figma.com/hc/en-us/articles/360040450513)
- [Component properties](../components/explore-component-properties.md)
- [Instance](https://help.figma.com/hc/en-us/articles/360039150413)
- [Auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties)
- [Blend Modes](https://help.figma.com/hc/en-us/articles/360040667874)
- [Text](https://help.figma.com/hc/en-us/articles/360039956634)
- [Fill](https://help.figma.com/hc/en-us/articles/360040623954)
- [Stroke](https://help.figma.com/hc/en-us/articles/360041003694)
- [Effects](https://help.figma.com/hc/en-us/articles/360041488473)
- [Export settings](https://help.figma.com/hc/en-us/articles/360040028114)

### **Prototype**

Use the **Prototype** tab to start building prototypes. Select any object to begin, then:

1. Add a [flow starting point](https://help.figma.com/hc/en-us/articles/360039823894#Starting_point): A flow is a path users take through the network of connected frames that make up your prototype. Add a starting point to choose the first frame of the journey.
2. Add an [interaction](https://help.figma.com/hc/en-us/articles/360040315773-Create-connections-and-flows#Create_an_interaction): Open up the **Interaction Details** modal, where you can define the trigger, action, and any animations for the interaction.
3. Define [scroll behavior](../create-prototypes/prototype-scroll-and-overflow-behavior.md): Select how the prototype responds to scrolling.
4. Show [prototype settings](https://help.figma.com/hc/en-us/articles/360039823894-Set-prototype-device-and-starting-point#Prototype_settings): Allows you to adjust the device and background of your prototype.

**Tip**: You can also add interactions directly on the canvas by selecting the **Prototype** tab, then clicking and dragging connections between objects.

[Learn more about prototyping in Figma →](https://help.figma.com/hc/en-us/articles/360040314193)

## Use the properties panel with view-only access

![A side-by-side image showing the two different tab options in the right sidebar: comments and properties. With the Comments tab selected, you can see comments from teammates discussing a design. With the Properties tab selected, you can see specific property attributes of a selected layer.](https://help.figma.com/hc/article_attachments/24303810699543)

People with **can view** access to a file, or who have a View seat on a paid plan, have two tabs in the properties panel: **Comment** and **Properties**.

View-only access is great for people who don't need to edit designs or for developers who need to access designs, but don't need the full suite of Dev Mode features. People with this access to a file can collaborate on designs, view design properties, copy basic code, and export assets.

### **Comment**

Select **Comment** in the right sidebar to add new comments or view existing ones. You can use comments to add or respond to feedback, collaborate, and iterate faster—all from the original design file.

From the **Comment** tab, you can see all the existing comments in a file. Or, find a particular comment or set of comments within a file:

- Type a keyword in the Search field to find a particular comment.
- Use the Filter to view comments by when they were posted or see only the ones you haven’t read yet. Here, you can filter to only view a certain set of comments.

Learn more about [adding comments to a Figma Design file](https://help.figma.com/hc/en-us/articles/360041068574) or [viewing and manage comments.](../comments/view-and-manage-comments.md)

### **Properties**

The **Properties** tab of the right sidebar lets you inspect particular layers on the canvas, as well as export designs.

To begin, select a layer on the canvas. You can do this by either selecting the element on the canvas itself or by selecting it from the **Layers** panel on the left sidebar. You can select any type of layer, such as a shape, text, group, or frame.

Under **Properties**, you’ll see the name of the selected layer and details about it, such as its layout and colors.

Right-click the layer on the canvas to:

- Copy the layer
- Copy/paste as code (CSS, iOS, or Android), SVG, PNG, copy the link, or copy its properties
- Select a different layer within the layer you selected

Looking to measure distances between objects? You can use keyboard shortcuts to quickly access spacing and padding information. [Learn how to add measurement guidelines →](../work-with-layers/measure-distances-between-layers.md)

At the bottom of the **Properties** tab, you can add an export configuration to export designs in a variety of file formats and sizes. Exporting helps you share content with others, move content between tools, and save copies of your designs outside Figma. [Learn how to export content from Figma.](https://help.figma.com/hc/en-us/articles/360040028114-Export-from-Figma)
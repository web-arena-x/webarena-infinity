# Use sections in prototyping

Source: https://help.figma.com/hc/en-us/articles/16194160540567-Use-sections-in-prototyping

---

[Sections](../work-with-layers/organize-your-canvas-with-sections.md) are a great way to visually group frames on the canvas – and they can help reduce the number of connections you need in your prototype, too

When you create a prototype connection to a section, Figma remembers the last-visited frame in the section and automatically returns to it.

Example

In an e-commerce app, you might have two sections:

- A “Browse” section that contains several frames to represent different product types
- A “Checkout” section that contains frames to represent the user checkout flow

On the checkout pages, there is a back button that navigates back to the “Browse” section. When users click the back button, they are automatically returned to the last frame, or product type, they were browsing.

Without using sections, the back button needs a fixed frame to return users to, which may not be the frame they came from. This can result in a prototype that doesn’t accurately reflect the experience users will have.

**Note**: This video explains a feature using Figma's old interface. For examples of the new interface, UI3, see the content in this article.

## Organize frames into sections

To begin, organize frames into sections.

In each section, group together frames that are a part of the same user flow. For example:

- In an e-commerce app, you might create sections for “Browse”, “Cart”, and “Checkout”
- In a social media app, you might create sections for “Feed”, “Settings”, and “Post”
- In a fitness app, you might create sections for “Workouts”, “Goals”, and “Profile”

To create a section:

1. Click  **Section** in the top toolbar, or press `⇧ Shift` + `S`.
2. Click and drag to create the section on the canvas.

Tip: Drag the section over existing frames to automatically put them inside it.

[Learn more about using sections →](../work-with-layers/organize-your-canvas-with-sections.md)

## Add a prototype connection to a section

You can set an entire section as a destination for a prototype connection.

When a connection navigates to a section, Figma remembers the last visited frame of that section and returns to it.

To set a connection destination to a section:

1. Navigate to the **Prototype** tab of the right sidebar, or press `⇧ Shift` + `E`.
2. Select a layer or object for the connection's hotspot, or starting point of the interaction.
3. Click the  plus icon on the side of the object's bounding box and drag it to the destination section.
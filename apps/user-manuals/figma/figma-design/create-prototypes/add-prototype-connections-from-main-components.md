# Add prototype connections from main components

Source: https://help.figma.com/hc/en-us/articles/4404380377367-Add-prototype-connections-from-main-components

---

Before you Start

Who can use this feature

Available on any [plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file or prototype can add prototype connections.

New to Prototyping? Check out our [Getting Started with Prototyping](../guides/guide-to-prototyping-in-figma.md) guide.

When a design reuses a component across multiple screens, you can prototype at the speed of light.

If you [add a prototype connection](https://help.figma.com/hc/en-us/articles/360040315773) from a main component, and use instances of that component in your designs, the prototyping connections of the instances will be inherited from the main component.

Use inherited prototype connections to connect:

- A mobile app tab bar placed at the bottom of multiple screens
- An arrow button to [navigate back](https://help.figma.com/hc/en-us/articles/360040035874#Back) to the previous screen
- A website footer or navigation menu
- Any component used for navigation that appears frequently throughout your design

## Add connections from main components

To prototype with main components:

1. Check that the main component is on the same page as the designs that contain the instances. Components from [team libraries](https://help.figma.com/hc/en-us/articles/360041051154) can't be prototyped this way.
2. Use instance(s) of the component in your designs.
3. Click the **Prototype** tab at the top of the right sidebar.
4. Click and drag from the to create at least one connection from the main component.

In the example below, the mobile app design has a persistent navigation bar at the bottom of each screen. We can connect a tab in the main component to its destination screen, and all instances of the navigation bar inherit the same interaction. Without a main component, we would need to connect each tab of every navigation bar individually.

![Animated demonstration of a mobile app with a persistent navigation bar for prototype connections using main components.](https://help.figma.com/hc/article_attachments/30955963401111)

Note: Figma won't display the inherited connections on the canvas by default. Select the instance to view its inherited connections.
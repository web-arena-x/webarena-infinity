# Create a responsive component that automatically adapts to each breakpoint

Source: https://help.figma.com/hc/en-us/articles/31242826664983-Create-a-responsive-component-that-automatically-adapts-to-each-breakpoint

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

In Figma Sites, you can create responsive components that automatically switch to the correct [variant](https://help.figma.com/hc/en-us/articles/360056440594) when placed in a specific [breakpoint](https://help.figma.com/hc/en-us/articles/31242797809815).

This saves time by reducing manual adjustments when designing for different screen sizes.

### How it works

![Animation of a component set with three variants of different sizes as well as a webpage with desktop, tablet, and mobile. An instance is dragged into the desktop breakpoint and the correctly sized variants appear on the other breakpoints.](https://help.figma.com/hc/article_attachments/31919030874903)

If you create a component set with variants designed for specific breakpoints, Figma will automatically insert the appropriate variant into its corresponding breakpoint when you add an instance to your webpage.

It works by matching the names of your breakpoints with your variant property values. For example, if your breakpoints are named **Desktop**, **Tablet**, and **Mobile**—and your variant properties include these values—Figma will automatically insert the correct variant in the corresponding breakpoint when you add an instance of this component to your webpage.

**Tip:** Learn more about variants and variant properties in the [guide to creating and using variants in Figma Design](https://help.figma.com/hc/en-us/articles/360056440594).

## Create a responsive component

![Responsive button component in Figma showing two "Share" button variants, labeled for Desktop and Mobile sizes, with properties panel on right.](https://help.figma.com/hc/article_attachments/31945095205143)

The following steps assume you’re starting with a single design and are creating variants for a webpage with two breakpoints: **Desktop** and **Mobile**.

1. Select a design and click  **Create component** in the right sidebar to create a component.
2. In the right sidebar, click  **Create property** from underneath the object header and select **Variant property**.
3. For this example, click the property name and change it to **Size.**
4. Click  **Edit property** and change the value from **Default** to **Desktop**.
5. With the new component selected, click  **Add variant**.
6. Change the property value to **Mobile**.
7. For this example, change the height or width of the variant.
8. Click  **Insert** in the left navigation bar and switch to the **Libraries** tab.
9. Click **Created in this file** at the top of the list.
10. Drag an instance of your component into a webpage with multiple breakpoints.
11. The **Desktop** variant should appear in the **Desktop** breakpoint and the **Mobile** variant should appear in the **Mobile** breakpoint.

**Tip**: You can apply this method to more than one property in a component.

**Tip**: If you are using instances from a published library and can’t edit their variant properties without detaching them, follow these steps to quickly turn them into a responsive component:

1. Add instances of the component for each breakpoint to the canvas.
2. Place each instance in an empty frame and rename the frame to match the breakpoint’s name.
3. Select each frame, click the  **dropdown arrow** next to  **Create component** at the top of the right sidebar, then select  **Create component set**.
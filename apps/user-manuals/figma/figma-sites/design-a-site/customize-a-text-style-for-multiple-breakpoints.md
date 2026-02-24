# Customize a text style for multiple breakpoints

Source: https://help.figma.com/hc/en-us/articles/31242838116119-Customize-a-text-style-for-multiple-breakpoints

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

In Figma, a [text style](https://help.figma.com/hc/en-us/articles/360039957034) is a reusable set of typography properties that can be applied to one or more text layers.

Text styles help you stay consistent across your designs by applying the same properties to each text layer. When you update a text style, every text layer using that style automatically updates, saving time and maintaining design consistency.

In Figma Sites, text styles have an additional capability: You can set different text style properties—such as font size, line height, letter spacing, or paragraph spacing—based on a webpage’s breakpoints. This means that you can define how a single style should adapt for different screen sizes or devices.

### **Example**

Suppose you're designing a website with a main hero section that needs to display a heading and a paragraph of text. You want the text to be large and prominent on desktop screens but smaller on mobile devices.

![Three webpage designs show the "Browse everything" display text is the same size on desktop, tablet, and mobile views.](https://help.figma.com/hc/article_attachments/31887814443927)

By default, a text style looks the same across different breakpoints.

![Three webpage designs show the "Browse everything" text is resized on desktop, tablet, and mobile views using responsive text styles.](https://help.figma.com/hc/article_attachments/31887814445463)

By customizing a text style for different breakpoints, you can make sure content looks great on any device.

## Create a new text style with breakpoints

You can create a text style from any text layer that has the properties you want to use.

1. Select a text layer.
2. In the **Typography** section of the right sidebar, click  **Styles**.
3. Click the  **plus icon** to create a new style.
4. Give the style a name.
5. Click  **Add new style breakpoint** in the **Breakpoint** section.
6. Choose an existing breakpoint in your file, or click **Custom** to choose your own breakpoint for this style.
7. Adjust the font size, line height, letter spacing, and paragraph spacing for that breakpoint as needed.
8. Click  **Add new style breakpoint** to add another breakpoint, or click **Create style** when you’re done.

Now, when you use this text style on a webpage with multiple breakpoints, it will automatically adjust based on page’s breakpoint width.

**Tip**: Alternatively, you can create a new responsive text style by first customizing the text layer in each breakpoint on the canvas, then creating the style. Figma will automatically add your customized properties for each breakpoint to the new style.

Simply select the customized text layer in each breakpoint of your webpage, then follow the instructions above. All your text layers’ custom property values will automatically get added to your new style.

## Add breakpoints to an existing text style

You can add breakpoints to text styles created in the file or ones from a library. If you add breakpoints to a text style from a library, these customizations will only be available in the current file—it’s not possible to publish them to a library.

1. Select a text layer with the existing style applied.
2. Click the name of the style in the **Typography** section of the right sidebar.
3. Hover over the name of the style in the list and click  **Edit style.**
4. In the **Breakpoint** section, click  **Add new style**.
5. Choose an existing breakpoint in your file, or click **Custom** to choose your own breakpoint for this style.
6. Adjust the font size, line height, letter spacing, and paragraph spacing for that breakpoint as needed.
7. Click  **Add new style** to add another breakpoint, or click **Create style** when you’re done.

**Tip:** If you want to reuse the text style’s breakpoint values across multiple files, you can [create and use a variable](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables). Since variable collections can be [published in a library](../../figma-design/create-and-share-libraries/publish-a-library.md), this can help you keep the values consistent across multiple files.
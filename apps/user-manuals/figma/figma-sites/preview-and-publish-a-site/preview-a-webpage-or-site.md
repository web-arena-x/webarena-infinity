# Preview a webpage or site

Source: https://help.figma.com/hc/en-us/articles/31242824747287-Preview-a-webpage-or-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires view or edit access to the file

Previewing your site helps you experience it as your users do. It’s a great way to quickly check animations, interactions, and responsiveness—without needing to publish first.

There are two ways to preview a webpage or a site:

1. [Use the inline preview](#h_01JTH6FSSKJZTB5RHXBNYTBQSN)
2. [Use the full-screen preview](#h_01JTH6FSSKXGGZ5QZFAB7JG9DT)

## Access the inline preview

Use the inline preview to view your site directly on the canvas alongside your designs. You can keep the inline preview window open while making design changes, letting you quickly go back and forth to see how your changes look when rendered in a browser environment.

**Tip:** When you click another webpage on the canvas, the preview straight jumps to that webpage.

![](https://help.figma.com/hc/article_attachments/32048553831959)

To open the inline preview, click the  **down arrow** next to the  **Preview** button at the top of the right sidebar, then select **Inline preview**. You can also use the keyboard shortcut: `Shift` `Space`.

![The Earthling website opened in the inline preview with the Figma Sites canvas behind it](https://help.figma.com/hc/article_attachments/31945237491479)

Here are a few ways you can control your previewing experience:

- **Navigation controls:** Click the  **Back** and  **Forward** buttons to mimic the corresponding browser buttons.
- **Automatically resize:** Snap the preview to  desktop,  tablet, or  mobile breakpoints.
- **Manually resize:** Click and drag the edge of the window. Hold `Shift` to scale it proportionally. You can also enter specific width and height values.
- **Change the scale:** Enter a scale percentage to increase or decrease the size of the window. This is a good option when you want to keep the preview window open while freeing up more space to work on the canvas.
- **Reload:** Click  **Reload** to see the most recent changes.
- **Open in full-screen:** Click  **Open full preview** to switch to a full-size preview window.

## Access the full-screen preview

Use the full-screen preview to take over the window and maximize the space you have for testing your site. To open the full-screen preview, click  **Preview** on any webpage, or next to the **Share** button at the top of the right sidebar. You can also use the following keyboard shortcuts:

- Mac: `⌘ Command` `⌥ Option` `Return`
- Windows: `Control` `Alt` `Enter`

Here are a few ways to control the preview:

![](https://help.figma.com/hc/article_attachments/31889241423895)

- **Close the preview**: Click  **Close** to exit the full-screen preview.
- **Switch pages**: Click the webpage slug to jump between pages.
- **Automatically resize**: Snap the preview to  desktop,  tablet, or  mobile breakpoints.
- **Manually resize:** Enter specific width and height values, or drag the handles at the edge of the preview window. Hold `Shift` while dragging to resize the window proportionally.
- **Scale:** Enter a scale percentage to increase or decrease the relative size of the preview.
- **Reload:** Click  **Reload preview** to see the most recent changes.
- **Navigation controls:** Click the  **Back** and  **Forward** buttons to mimic the corresponding browser buttons.
- **Restart preview:** Click  **Restart preview** to return the preview to it’s original state. This is helpful if you’re testing links on a particular page and want to return to the place where you started when you first opened the preview window. **Restart preview** won’t work if you navigate between webpages by clicking the webpage slug.

## Troubleshoot issues when previewing

### The webpage on the canvas isn’t showing the same thing as the preview window

You may notice some inconsistencies between how an object appears on the canvas, in the preview window, and on the published site. The canvas serves as a design workspace, while the preview reflects how the design will function in an actual browser.

Some elements—like animations, [interactions](https://help.figma.com/hc/en-us/articles/31242843431575), [code layers](https://help.figma.com/hc/en-us/articles/31242824165143) or embeds—may not render accurately on the canvas. In the preview window, everything renders as if in a browser, including fonts, flexbox layouts, and embedded content.

While we try and render everything as close to your design as possible, some things may look different due to different browser technologies.

Here are some examples which of where you might find inconsistencies between the canvas and the browser:

- Text decorations like underlines and strikethroughs may appear differently than designed.
- Mixed line heights may show up inconsistently across browsers. To fix, set to a single value.
- Dashes may appear differently than designed.
- Smart animate may not work as expected with vector properties (such as masks, strokes, and fills) or effects.
- Shadows on rotated layers may appear differently than designed.
- Rotations that include groups or objects that change in size can’t use smart animate.

**Tip**: You can check if there are any issues preventing your site from rendering correctly by clicking  **Review issues** at the bottom left corner of the file.

### An interaction or animation isn’t working as expected

- **Review interaction settings**: Check the interaction settings in the **Interaction** panel in the right sidebar. Verify that the settings for your interaction or animation are correctly configured. Make sure triggers and targets are properly assigned, and the values on each interaction property are correct. If an interaction has the  icon, it is not supported in Figma Sites.
- **Check for overlapping elements:** Check the canvas and the **Layers** panel in the left sidebar to see if there are elements on top of your interactive element that are preventing it from working as expected.

### The font size looks too big or too small in the preview window

- **Check for breakpoint-specific text styles:** If the font is appearing too big or too small in a specific breakpoint, it might be the case that you’re using a [font style that is specifically customized for different breakpoints](https://help.figma.com/hc/en-us/articles/31242838116119).
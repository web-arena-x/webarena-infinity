# Add or delete breakpoints in a webpage

Source: https://help.figma.com/hc/en-us/articles/31242797809815-Add-or-delete-breakpoints-in-a-webpage

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

In web design, breakpoints mark specific screen widths where your webpage layout changes to meet the needs of different screen sizes.

Every new webpage in Figma Sites starts with a desktop breakpoint. By adding additional breakpoints, you can fine-tune the look and feel of the webpage and optimize the user experience across devices.

For example, you might use multiple breakpoints to adjust cosmetic elements of the site, like resizing text for different devices. You can also modify functionality—like replacing a hover effect on desktop with a press effect on mobile, since mobile devices don’t support hover interactions.

**Tip**: When you make edits to the [primary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879-Make-changes-across-multiple-layouts-in-a-webpage), they automatically cascade to other breakpoints. [Learn more about editing across breakpoints.](https://help.figma.com/hc/en-us/articles/31242788601879-Make-changes-across-multiple-layouts-in-a-webpage)

### How breakpoints work in Figma Sites

Let’s say you have a desktop breakpoint 1280px wide, a tablet breakpoint 800px wide, and a mobile breakpoint 340px wide.

- A screen width over 1280px will use the desktop layout
- A screen width between 800px and 1280px will use the tablet layout
- A screen width under 800px will use the mobile layout

## Add a new breakpoint

**Tip**: We recommend using [auto layout](https://help.figma.com/hc/en-us/articles/5731482952599) in your designs. Auto layout simplifies the design process by allowing your content to reflow seamlessly across different screen sizes, reducing the need for manual adjustments. [Learn more about working with auto layout.](https://help.figma.com/hc/en-us/articles/360040451373)

![A webpage on the canvas with a plus button and dropdown for selecting breakpoints: Desktop (1280), Tablet (800), Mobile (375), Custom.](https://help.figma.com/hc/article_attachments/31915203653655)

To add a new breakpoint to a webpage:

1. Click the  **plus** button in the webpage header on the canvas.
2. Choose a desktop, tablet, or mobile breakpoint with predefined widths, or enter a custom breakpoint width.

If your designs use auto layout, Figma will automatically adjust the layout so it flows better in the new breakpoint size. For example, Figma will adjust the padding to account for content areas that are too narrow, or convert horizontal layouts to vertical if there is not enough width available.

## Edit breakpoints in a webpage

You can adjust your webpage’s breakpoints simply by changing the width of each one.

When you change the width of a breakpoint, its neighboring breakpoints automatically adjust the range of sizes they cover. To edit the breakpoint width:

1. Select the breakpoint you’d like to change.
2. Enter a new width in the right sidebar.

## Delete a breakpoint

Deleting a breakpoint causes the remaining ones to adjust automatically.

For example, if you delete a tablet breakpoint between a desktop breakpoint and a mobile breakpoint, the mobile breakpoint will then apply at screen widths below the desktop breakpoint.

To delete a breakpoint, select it on the canvas or in the layers panel and press delete.
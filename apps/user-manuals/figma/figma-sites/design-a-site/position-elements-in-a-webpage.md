# Position elements in a webpage

Source: https://help.figma.com/hc/en-us/articles/31242774629655-Position-elements-in-a-webpage

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Figma offers four common CSS positioning properties to help you control the placement of elements in your web design:

1. [Relative](#h_01JTGTRX99MSHQ47BEKESB8K0C): Follows the flow of content in an [auto layout frame](https://help.figma.com/hc/en-us/articles/5731482952599)
2. [Absolute](#h_01JTGTRX992PFSXSR5EWZMWXQE): Allows you to move elements freely within their parent element
3. [Fixed](#h_01JTGTRX99W4J8RE3A6YJPJVF1): Keeps elements visible on the screen
4. [Sticky](#h_01JTGTRX992TGS53RXCRN1B0EH): Lets elements scroll, then stick to the top edge of your screen

You can change an element’s position type from the **Position** section of the right sidebar.

**Tip**: When copying from Figma Design, positioning properties automatically convert to their corresponding types in Figma Sites. [Learn more.](https://help.figma.com/hc/en-us/articles/31414245874455)

![Position dropdown menu the right sidebar, highlighting options for Relative, Absolute, Fixed, Sticky.](https://help.figma.com/hc/article_attachments/32003404358679)

## Apply relative positioning to an object

In Figma Sites, elements automatically use relative positioning when placed inside an [auto layout frame](https://help.figma.com/hc/en-us/articles/5731482952599).

Instead of setting explicit position values, an element’s position determined by the layout rules of its parent auto layout frame.

Adjust the [auto layout properties](https://help.figma.com/hc/en-us/articles/360040451373)—such as direction, alignment, and padding—on the parent frame to define how items within the frame should adapt across desktop, tablet, and mobile devices.

You can’t move elements freely in a webpage when using relative positioning, as they will always follow the layout rules of the parent. To ignore the auto layout flow, switch the element to [absolute positioning](#h_01JTGTRX992PFSXSR5EWZMWXQE).

If you’re familiar with web development, auto layout frames in Figma Sites work similarly to [flexbox](https://www.w3schools.com/css/css3_flexbox.asp).

**When should I use relative positioning?**

Relative positioning is ideal for collections of items where the layout needs to reflow for different screen sizes. For example, if you have a group of elements that appear side-by-side on desktop and should stack vertically on mobile, place them in an auto layout frame.

## Apply absolute positioning to an object

Unlike relative positioning, absolute positioning gives you the flexibility to place elements freely within the parent container.

**Tip:** By default, any element added to a blank webpage is set to absolute positioning. If you add auto layout to the webpage, the element will automatically switch to relative positioning.

**When should I use absolute positioning?**

Use absolute positioning when an element needs to be placed independent of the normal page flow, such as overlays, fixed-position UI components, or graphics that need to remain stable regardless of surrounding content changes.

### Change the object’s position

To change an object’s position, move the element around, or set specific values in the **Constraints** section of the right sidebar to pin the object to the top, bottom, left, or right. You can also use transform or alignment properties to adjust the position.

Learn more about [adjusting alignment, rotation, position, and dimensions](https://help.figma.com/hc/en-us/articles/360039956914).

### Apply constraints

With absolute positioning, you can set [constraints](https://help.figma.com/hc/en-us/articles/360039957734) to anchor an object to one or more sides of the parent layer—or to the webpage if no parent layer exists.

For example, an element positioned at 50px from the left and 100px from the top will always maintain that fixed distance from its parent’s top and left edges.

This gives you more control over how the layer responds when the parent frame is resized.

### Use absolute position in an auto layout frame

An object with absolute positioning inside an auto layout frame is excluded from the auto layout flow. The object and its surrounding siblings ignore each other, even as they resize and move.

## Apply fixed positioning to an object

Fixed positioning is similar to absolute positioning in that it allows you to precisely control an element's placement. However, its behavior is tied to the viewport rather than a containing element.

Layers using fixed positioning move to the top of the layers panel since fixed elements cannot have other layers placed on top of them.

**When should I use fixed positioning?**

Fixed positioning is ideal when you require an element to remain visible regardless of page scrolling. It is best used for navigation menus, headers, footers, or interactive components like chat widgets that must be constantly available.

## Apply sticky positioning to an object

An element with sticky positioning remains in its normal flow until the user scrolls to a specific point, at which time it sticks to a defined position relative to the viewport. It continues to be visible as scrolling progresses, but stops sticking once the bottom edge of its parent container is reached.

**When should I use sticky positioning?**

Sticky positioning is useful for elements that need to remain visible only after they reach a predetermined scroll point. A common example is a table header row that stays visible at the top of the viewport while scrolling through the table.

**Tip**: You can use sticky positioning on an element in an auto layout frame. The element behaves like it has relative positioning until the sticky effect is triggered, then it behaves like it has fixed positioning.

**Caution**: The sticky effect only works if the parent container has enough height for the element with sticky positioning to scroll.
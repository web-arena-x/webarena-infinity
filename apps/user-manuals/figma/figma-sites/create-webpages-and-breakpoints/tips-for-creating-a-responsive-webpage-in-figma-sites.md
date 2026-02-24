# Tips for creating a responsive webpage in Figma Sites

Source: https://help.figma.com/hc/en-us/articles/33257143505175-Tips-for-creating-a-responsive-webpage-in-Figma-Sites

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

[Figma Sites](https://help.figma.com/hc/en-us/articles/31230436657815) lets you design, prototype, and publish high-quality websites—all in one place.

Designing a responsive webpage in Figma Sites means building layouts that adapt seamlessly across screen sizes—without having to recreate them for every breakpoint.

Use the tips below to simplify and speed up the process of designing a responsive website:

1. [Use auto layout to control how the layout adapts to different screen widths](#h_01K05FKJ9D9G9QYKP3BTJ6F13E)
2. [Create top level frames for each section of a webpage](#h_01K05FKJ9DVRR4F430EQ8B3W4Z)
3. [Understand how breakpoints work in Figma Sites](#h_01K05FKJ9D9RSVK3KRSEKZEET3)

## Use auto layout to control how the layout adapts to different screen widths

[Auto layout](https://help.figma.com/hc/en-us/articles/360040451373) is essential for building responsive websites in Figma. It enables layers to respond dynamically when the browser window size changes.

As a first step, we recommend applying auto layout to the webpage itself. Any elements you add will automatically stack vertically down the page, making it easier to structure your site as a series of content blocks.

[](https://help.figma.com/hc/article_attachments/33468477707159)

To apply auto layout to the webpage:

1. Select the primary breakpoint in a webpage by clicking its name—usually **Desktop**.
2. Click **Apply auto layout** in the right sidebar or use the keyboard shortcut `Shift` `A`.
3. If needed, change the auto layout direction to **Vertical**.

**Why is auto layout so important for web design?**

We recommend using auto layout as much as you can on your website.

Elements in an auto layout frame are automatically arranged based on direction, spacing, padding, alignment, and other properties. When the content changes or elements are added, removed, or resized, the layout adjusts without requiring manual repositioning. This makes it much easier to create designs that adapt for different screen sizes.

For example, the ‘project card’ design below uses four auto layout frames. This ensures the content in this card will reflow depending on parent frame’s size—without a designer needing to make changes.

![Project card design containing multiple auto layout frames in a vertical and horizontal orientation](https://help.figma.com/hc/article_attachments/33468817330839)

If you’re new to auto layout, check out these resources:

- Watch and read: [the auto layout module in the Figma Design for Beginners course](https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners)
- Read: [Guide to auto layout](../../figma-design/use-auto-layout/guide-to-auto-layout.md).

## Create top level frames for each section of a webpage

Think of webpage layouts in Figma Sites as a series of vertically stacked frames. Each of these frames represents a ‘block’ or ‘container’ for a specific section of the page.

![Webpage layout showing placeholder top-level frames stacked vertically. The frames are labelled: Navigation, Hero, Features, Testimonials, and Footer](https://help.figma.com/hc/article_attachments/33468817331735)

There are a few benefits to adding this structure to your layout:

- You can nest content and design elements inside each of these parent frames, giving you granular control over the layout of each section as you make adjustments for different screen sizes.
- A structured layout improves both SEO and accessibility, making content easier for search engine and assistive technologies to interpret.
- You can swap, duplicate, or reorder sections just by dragging them around the webpage.

**Tip**: We recommend using frames rather than groups wherever possible in Figma Sites to nest layers. Frames can have properties like fills and auto layout, whereas groups are mainly for grouping layers to perform bulk actions, or using specific features like boolean operations.

### Assemble a site using frames for each section

We recommend designing each section on the canvas, then dropping it into the web page when you’re ready.

[](https://help.figma.com/hc/article_attachments/33468454608023)

1. On the canvas, add design elements to a frame you’d like to use as a content section.
2. Drag that frame into the webpage.
3. Select the frame and set the width to **Fill container**. **Fill container** is only available as an option when nested inside another auto layout frame—in this case, the webpage itself.

**Tip**: Set [accessibility landmarks](../design-a-site/improve-the-accessibility-of-your-site.md)—like `nav`, `main`, and `footer`—on each top-level auto layout frame for better accessibility.

**Why do I need to set each top-level frame to ‘fill container’?**

This setting ensures each section will always span the full width of the parent frame, which is ideal when designing for different screen sizes.

In the animation below, notice how a fixed-width section appears fine on desktop but fails to resize on mobile. Using **Fill container**, it adjusts to the parent width on all breakpoints.

[](https://help.figma.com/hc/article_attachments/33468477705367)

### Let auto layout handle spacing

Auto layout can handle most of your spacing needs for each section. In cases where padding alone doesn’t doesn’t work for your design, you can apply a fixed height to a standalone frame to simulate vertical gaps.

[Learn more about gap between and padding spacing controls in auto layout.](../../figma-design/use-auto-layout/use-the-horizontal-and-vertical-flows-in-auto-layout.md#h_01JT9HNB6TY6SG6BZG1XABVJ1G)

### Set min and max widths where required

Add a min or max width to layers to better control how they change between the defined breakpoints.

You may also want to add a max width to content on your largest breakpoint. If the content uses **Fill container**, it will keep increasing its width, even if displayed on a super wide screen. Set a max width to ensure the content expands to a certain size, but no further.

[](https://help.figma.com/hc/article_attachments/33468335485079)

## Understand how breakpoints work in Figma Sites

Every new webpage starts with a **primary breakpoint**—usually the desktop breakpoint.

- Changes to objects in the **primary** breakpoint cascade to all **secondary** breakpoints.
- Changes in a **secondary** breakpoint apply *only* to that view.

For example, if you drag a hero section into a primary breakpoint, it will immediately appear in all secondary breakpoints. If you add the hero section to a secondary breakpoint, it will only appear on that breakpoint.

This behavior applies to adding, selecting, and editing objects.

[Learn more about working across breakpoints in Figma Sites.](https://help.figma.com/hc/en-us/articles/31242788601879)

### Design mobile-first if you prefer

The desktop breakpoint is set as the primary breakpoint by default, but you can change it to the a tablet or mobile breakpoint if you prefer.

To change the primary breakpoint:

1. Right-click a non-primary breakpoint in a webpage.
2. Select **Set as primary breakpoint**.

Changing the primary breakpoint won’t change the order of the breakpoints in the webpage—you’ll just see the **Primary** label switch to the new breakpoint.
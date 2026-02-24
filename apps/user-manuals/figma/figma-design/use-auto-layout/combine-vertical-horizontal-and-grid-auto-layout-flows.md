# Combine vertical, horizontal, and grid auto layout flows

Source: https://help.figma.com/hc/en-us/articles/31441443713047-Combine-vertical-horizontal-and-grid-auto-layout-flows

---

Before you start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access can use auto layout

This article covers just one aspect of working auto layout. Check out these other articles to learn more about working with auto layout in Figma Design.

- [Guide to auto layout](https://help.figma.com/hc/articles/360040451373): An overview of auto layout, how it works, key properties, and browse a collection of auto layout resources.
- [Toggle auto layout on a design](https://help.figma.com/hc/en-us/articles/5731482952599-Add-auto-layout-to-a-design): Learn how to add auto layout to frames and layers so that you can start making your designs responsive.
- [Use the horizontal or vertical flows in auto layout](https://help.figma.com/hc/articles/31289464393751): Learn about the properties available to the horizontal and vertical flows in auto layout.
- [Use the grid auto layout flow](https://help.figma.com/hc/articles/31289469907863): Learn how to work with columns, rows, and cells with the grid layout flow.

The true power of auto layout's responsiveness emerges when combining resizing behaviors across nested auto layout frame.

Nesting an auto layout frame within another auto layout frame allows you to combine horizontal, vertical, and grid auto layout flows to create intricate components and interfaces. The nested frames will have both parent and child properties, meaning each frame will have its own separate padding and gap between values, which allow for for multi-dimensional layouts with elements that flow in different directions and arrangements.

**Tip**: Nesting refers to the act of placing a layer inside of another layer, such as placing a button inside a component, or a shape inside of a frame.

[Learn more about nesting and parent, child, and sibling relationships.](../work-with-layers/parent-child-and-sibling-relationships.md)

In this article, we’ll go through a couple of examples of nesting auto layout frames, but you can mix and match combinations of auto layout flows to achieve your desired effect.

## Nest vertical and horizontal flows

![Diagram showing nested vertical auto layout frames for author and date, profile as horizontal, posts, and newsfeed.](https://help.figma.com/hc/article_attachments/33916919626263)

In this social media newsfeed example, there are four levels of auto layout. Let’s break them down one by one, starting with the inner-most level:

### Author and date

![Vertical auto layout frame with two text layers flowing top to bottom.](https://help.figma.com/hc/article_attachments/33916919627031)

The author and date are two individual text layers that live together inside an auto layout frame. Because they flow from top to bottom their auto layout frame is set to a **vertical** flow.

Try it out

**Step 1: Create the text layers.**

1. Select the  text tool from the toolbar, or press `T`, then click on the canvas to type a placeholder name.
2. Duplicate the text layer, moving it below the name layer, then update the text to a placeholder date.

**Step 2: Add auto layout.**

1. Select both text layers, then add an auto layout frame around them by pressing `⇧ Shift` `A` or clicking  **Use auto layout** from the **Layout** section of the right sidebar.
2. Set the auto layout flow to  **Vertical**.

![Animation of auto layout in Figma shown with vertical flow for text layers: FirstName LastName and Month DD.](https://help.figma.com/hc/article_attachments/33916919627415)

### Profile

![Auto layout frame with horizontal flow for a profile, containing a circle to represent the avatar and text lines with indicators for content alignment.](https://help.figma.com/hc/article_attachments/33916919627799)

The **Profile** contains an avatar and the author and date frame we just created. Because they flow left-to-right, these elements live in an auto layout frame using the horizontal flow.

Try it out

**Step 1: Create the avatar.**

1. Select the  **Ellipse** tool from the toolbar or press `O`.
2. Click and drag your cursor to create an ellipse. Do this while holding `⇧ Shift` to lock the ellipse to a 1:1 ratio as you create.

**Step 2: Add auto layout for the profile element.**

1. Select both the avatar ellipse and author and date frame.
2. Add an auto layout frame around them by pressing `⇧ Shift` `A` or clicking  **Use auto layout** from the right sidebar.
3. Set the auto layout flow to  **Horizontal**.

![Horizontal auto layout applied to a profile component with avatar and text layers for name and date on a canvas.](https://help.figma.com/hc/article_attachments/33916931905047)

**Step 3: Update auto layout properties.**

To make sure that our elements will reflow properly in our final product, select the name layer and date layer and set their width resizing property to **Fill container**. Then set their parent frame to **Fill container** as well.

![](https://help.figma.com/hc/article_attachments/33916919628439)

### Social media posts

![Diagram of a vertical auto layout in a social media newsfeed.](https://help.figma.com/hc/article_attachments/33916931905943)

Each social media **Post** lives inside it’s own frame, each containing various elements—including the user’s profile, an image, and a description. We want elements in each post to flow from top to bottom, so they are set to a **vertical** auto layout flow.

Try it out

**Step 1: Create the image.**

1. Select the  **Rectangle** tool from the toolbar, or press `R`. Click and drag to draw a rectangle.
2. Click the color swatch from the **Fill** section of the right sidebar to open the color picker.
3. Select  **Image**. You can leave this as a checkerboard placeholder, or insert an image of your own.

**Step 2: Create the description.**

1. Select the text tool, then and click and drag to create a text box.
2. Add some placeholder text.

**Step 3: Add an auto layout frame.**

1. Select the profile element, image, and text description. Then add auto layout.
2. Set the flow to  **Vertical**.

![Vertical auto layout settings in the right sidebar for a social media post, showing profile name, date, and placeholder text.](https://help.figma.com/hc/article_attachments/33916919628951)

**Step 4: Update auto layout properties**.

To make sure our content reflows the way we want them to in our final product, let’s update the resizing properties on a few elements.

- Profile element and post description
  - Set their width resizing to **Fill container** so that it will always fill the width of the container, even if the parent resizes.
  - Set their height resizing to **Hug contents** so that it will grow and shrink to accommodate the layers inside the frame.
- Image
  - Set the width resizing to **Fill container**.
  - Toggle on **Aspect ratio** to maintain the current ratio of the image whenever it resizes.
- Update other auto layout properties as you see fit. Padding and gap between are great places to start.

**Tip**: Add a background color or stroke to the social media post frame so that you can see the bounds of the frame resizing more easily.

### Newsfeed

![Diagram showing a social media newsfeed using nested auto layout frames in a vertical flow.](https://help.figma.com/hc/article_attachments/33916919629719)

The **Newsfeed** lives in a top-level frame and uses a **vertical** auto layout flow so that the social media posts will flow from top to bottom.

Try it out

**Step 1: Add the newsfeed auto layout frame.**

1. Select the social media post and press `⇧ Shift` `A` to add another level of auto layout to it. This will be the newsfeed frame.
2. On the new frame, set the auto layout flow to  **Vertical**.
3. Make sure the height resizing property is set to **Hug contents**.

**Step 2: Update auto layout properties**.

- Select the social media post, and set its width resizing to **Fill container**. Keep the height resizing to **Hug contents**.

  ![Social media post with vertical auto layout, showing an avatar, text layers, and an image placeholder. The width and height boxes in the right sidebar are highlighted.](https://help.figma.com/hc/article_attachments/33916919630231)
- Update the padding and gap between properties as desired for the newsfeed frame.

**Step 3: Duplicate the social media post element.**

Select the social media post again and duplicate it. Notice how the top-level frame resizes to accommodate.

![](https://help.figma.com/hc/article_attachments/33916931907351)

**Finishing up**

Now when you resize the frame or choose a different frame preset, the contents should resize and reflow accordingly.

![](https://help.figma.com/hc/article_attachments/33916919630999)

[Learn more about the vertical and horizontal flows in auto layout.](https://help.figma.com/hc/articles/31289464393751)

## Nest grid flows

🚧 The grid flow for auto layout is currently in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711). Some functions and settings may not yet be available to grid. The feature may change and you may experience bugs or performance issues during the beta period.

![Diagram showing three levels of nested grid auto layout flows for a mobile home screen in Figma, and how the grids can be arranged together.](https://help.figma.com/hc/article_attachments/33916919631639)

In this mobile home screen example, there are three levels of auto layout that all use the grid auto layout flow. This time, let’s start with the outer-most level:

### Apps on the home screen

![Mobile home screen mockup using a 3x6 grid auto layout with placeholder app icons.](https://help.figma.com/hc/article_attachments/33916931908631)

The apps on the home screen live in a top-level auto layout frame that uses the grid option with three columns and six rows (3x6).

Try it out

**Step 1: Create a frame.**

1. Select the  **Frame** tool or press `F`.
2. Choose a mobile [frame preset](../create-and-edit-layers/frames-in-figma-design.md#h_01JH5Y0VVZJVB5AXYNYAHJRV3R) from the right sidebar.

**Step 2: Use grid auto layout flow.**

1. With the frame selected, click the  **Grid** option in the **Layout** section of the right sidebar.
2. Click the grid selector, and set the **Number of columns** to `3` and **Number of rows** to `6`.

![](https://help.figma.com/hc/article_attachments/33916919633815)

**Step 3:** **Add mock app icons.**

1. Select the frame tool again, and click into one of the cells to place a frame.
2. Update any desired properties of the frame (e.g. fill color, stroke, corner radius, and so on).
3. With the frame still selected, press `⌘ Command` / `⌃ Control` `D` to duplicate it. The new frames will fill the subsequent cells.

![](https://help.figma.com/hc/article_attachments/33916931913111)

**Bonus**: Update the mobile frame’s padding and gap between properties to customize the spacing around the apps.

### Folders

![Mobile home screen mockup with a 3x6 grid auto layout, showing placeholders for app icons and larger folder frames.](https://help.figma.com/hc/article_attachments/33916931913751)

The folders are auto layout frames that use the grid option. Each frame spans across four grid cells.

Try it out

**Step 1: Delete any apps you won’t need**

Our folders will occupy multiple cells, so let’s delete the app frames that will be in our way.

![Grid layout with 3 columns and 6 rows, alternating filled blue squares and empty dashed red squares. The dashed red squares represent the app frames we're deleting.](https://help.figma.com/hc/article_attachments/33916919636119)

**Step 2: Span the folder frames.**

Select one of the folder frames and click and drag it to span multiple cells. Change the fill color and any other properties of the folder frame as desired.

![](https://help.figma.com/hc/article_attachments/33916931915159)

### Apps in folders

![Auto layout grid example showing a mobile home screen with nested grid flows: 3x3 and 2x2 grids for app organization.](https://help.figma.com/hc/article_attachments/33916931916439)

Within the folder frames, one uses a 3x3 auto layout grid, and the other uses a 2x2 auto layout grid.

Try it out

**Add grid to the folder frames**

1. Select one of the folder frames and add auto layout to it. Choose grid as the flow option.
2. Click the grid selector and set the **Number of columns** to 3 and **Number of rows** to 3.
3. Copy one of the app frames and paste it multiple times into this folder frame.
4. Update the frame’s padding and gap between values as desired.
5. Repeat the steps above for the 2x2 folder frame.

![Mobile home screen with auto layout grid, showing nested apps in different colored grids (3x6, 3x3, 2x2 configurations).](https://help.figma.com/hc/article_attachments/33916931916823)

[Learn more about the grid auto layout flow.](https://help.figma.com/hc/articles/31289469907863)
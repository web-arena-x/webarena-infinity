# Add interactions to an element

Source: https://help.figma.com/hc/en-us/articles/31242843431575-Add-interactions-to-an-element

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Interactions enhance the user experience of your site by adding animations, transitions, and visual transformations to the content.

Whether it's a subtle hover animation on buttons, adding depth and movement using parallax, or interesting effects triggered by user actions, interactions can help your webpages feel more responsive and vibrant.

**Tip**: This article is about using using Figma’s prebuilt interactions, but you can also [make your own in code](https://help.figma.com/hc/en-us/articles/31242824165143).

## How interactions work

Each interaction has two parts:

- **A trigger**: Defines the event—such as a mouse click or touch gesture— that causes the interaction to start. Some interactions have a built-in trigger, while others let you choose one.
- **An action**: Defines the next step or event that occurs once the interaction is triggered.

## Add an interaction

1. Select a layer or object in a webpage or elsewhere on the canvas.
2. Click the **Interaction** tab in the right sidebar.
3. Click  **Add interaction** in the **Interactions** section.
4. Use the **Interaction details** panel to configure your interaction.

**Tip:** You can add interactions to multiple elements at once. Select one object, then hold down `Shift` while clicking additional objects. When you add an interaction following the steps above, it will apply to all selected objects.

**Note**: Some interactions aren’t available for certain layer types. If an interaction is missing from the list of options, it means that it isn’t supported for your selected layer.

## Select an interaction

Learn more about each of the default interactions in Figma Sites.

### Change to

The **Change to** action lets you switch between variants in a component set. It is only available in the list of **Interactions** when the selected object is a variant in a component set.

For example, if you have a component set for a checkbox icon with a `checked` variant and an `unchecked` variant, the **Change to** action lets you toggle between these states on your site.

### Back

**Back** lets users navigate back to the previous screen. It’s like clicking the back button in a browser.

### Scroll to

**Scroll to** takes you from one frame in a webpage to another. This is the most common action for jumping between items on the same webpage. There are two animations you can use for the scroll effect:

- **Instant**: Users instantly jump straight to the destination element
- **Animate:** The page automatically scrolls to reach the destination element.

### Hover effect

Transform an object when a mouse or pointer hovers over it.

**Tip**: People using your site on a tablet or phone won’t be able to use hover-based interactions. We recommend switching to a different interaction—like a press effect—on mobile breakpoints.

### Press effect

Transform an object for as long as it is pressed, after which it will return to its original state.

### Reveal

Lets elements become visible in a dynamic and visually engaging way. Triggers include:

- **In view**: the reveal starts as the layer scrolls into view
- **Page load**: the transformation starts as soon as the user starts scrolling. This works well for objects in the header or hero that people see after immediately loading the site.
- **Other layer in view**: the transformation starts as a layer you choose scrolls into view

### Scroll parallax

Scroll parallax lets you choose how quickly content moves in response to user scrolling.

This creates an effect where different layers move at varying speeds. For example, you can set background elements to move slower than foreground elements, adding depth and immersion to the design.

**Tip:** If you want to make sure the layer only scrolls as far as the edges of its parent container, make sure the parent frame has **Clip content** turned on in the right sidebar. This lets you crops content that extends past a frame's boundaries.

**Note:** Scroll parallax is deactivated for fixed or sticky elements and their child layers.

### Scroll transform

**Scroll transform** adjusts an element’s properties— such as size, position, opacity, and rotation—as the user scrolls. It can be triggered:

- **On scroll**: The transformation starts as soon as the user starts scrolling and completes when the user has scrolled all the way down the web page.
- **Other layer in view**: The transformation begins as a layer you choose scrolls into view.
- **Layer in view**: The transformation begins when the layer itself is in view.

Choose between these options to fine tune the effect. For example, let’s say you want a layer to fade in from 0% to 100% opacity. If you use **On scroll** or **Other layer in view**, the layer might already be partially visible by the time the user scrolls to it. If you use **Layer in view**, the layer will only start becoming visible when the user has it in view.

### Cursor effect

**Cursor effect** replaces the standard mouse cursor with a design of your choice, like an image, vector object, or frame.

After you’ve selected a design to use for the effect, you can modify the cursor **hotspot.** This defines the exact location of the mouse pointer relative to the the cursor design.

By default, the hotspot is set to **Top left** to mimic a standard mouse, but you can change the location of the pointer by entering your own X and Y values.

**Note:** Any blend modes applied to the cursor element won’t display when the cursor effect renders on the webpage.

**Note: Cursor effect** won’t display when the page is viewed on a mobile device.

### Marquee

**Marquee** creates a scrolling effect where elements move continuously across the screen. You can set the direction, speed in pixels per second, and whether the scrolling is infinite.

You can apply **Marquee** to text layers or frames with [auto layout](https://help.figma.com/hc/en-us/articles/5731482952599) applied. When applied to a frame, marquee animates the child layers of the frame.

The marquee won’t animate beyond the bounds of the layer it is applied to. The exception is when there is overflowing content within the layer. You may need to use [clip content](../../figma-design/create-prototypes/prototype-scroll-and-overflow-behavior.md#h_01HHN5HZP3Y7Z5BTZ6KFXSK76X) on the parent layer if you don’t want the child elements to appear outside of the bounds of the parent layer.

**Tip**: If you’re adding a marquee to a text layer—rather than its parent frame—you may need to add in a few extra spaces to separate the end of the text from its beginning. In an auto layout frame, you can use horizontal padding to separate each instance in the marquee.

### Lightbox

**Lightbox** creates an overlay that brings content into focus. When triggered, the selected element—often an image or gallery item—expands into a full-screen modal with a dimmed background. This immersive display helps to emphasize high-impact visuals or important details, while including an easy way to exit the view.

The **Lightbox** interaction has a dedicated image property that lets you define which image should appear when the lightbox is active.

### Spin

**Spin** rotates an element around its center point.

### Mouse parallax

**Mouse parallax** creates a subtle, depth-enhancing effect by shifting elements in response to the user’s cursor movement. As the pointer moves, the element adjusts its position slightly, creating an interactive layering effect—ideal for backgrounds or decorative elements that benefit from a sense of motion.

### Typewriter

**Typewriter** sequentially reveals text characters as if they were being typed in real time. It’s ideal for headlines, quotes, or storytelling snippets.

### Scramble text

**Scramble text** jumbles the characters of a text element before settling into the final message.

### Draggable

The **Draggable** action lets users drag an element around the screen.

### Conditional

Conditional interactions let you create complex behaviors that only trigger when certain conditions are met. For example, a **Submit** button might only become clickable if a user checks a box agreeing to the terms and conditions.

1. Select **Conditional** as the interaction type.
2. Complete the **If** condition:
   1. In the **If** field, write a [boolean expression](https://help.figma.com/hc/en-us/articles/15253194385943#Boolean_expressions) to represent the condition that must be met.
   2. Select an action from the dropdown menu. This action will be triggered if the **If** statement is met. You can also add extra actions that trigger when the **If** statement is met.
3. Complete the **Else** condition:
   1. Select an action from the dropdown menu. These actions will be triggered if the **If** statement is not met. Alternatively, leave the **Else** action blank.

**Tip:** The **Conditional** interaction works similarly to its counterpart in Figma Design. For more information, we recommend reading the guide to [prototyping with conditionals](../../figma-design/advanced-prototyping/multiple-actions-and-conditionals.md#h_01H91GHXRHGN8K801ZZCPV99FA). You can also check out the [advanced prototyping examples](https://help.figma.com/hc/en-us/articles/17146044893591) for ideas you can bring to your site.

### Set variable

The **Set variable** action allows you to set or modify the value of a variable as a result of an interaction trigger. For example, you can create a light and dark mode toggle, or a form that shows an error if a form is submitted without all required fields completed.

Here’s how to do it:

1. Select **Set variable** as the interaction type.
2. From the **Target** dropdown menu, select the variable you want to set a new value for.
3. In the **Value** field, enter in a new value for the variable. The new value type must match the variable type you’re changing. For example, if you selected a number variable, the new value must also be a number.
   - **String values**: Enter a text string (contained in quotations), or select a string variable from the selection panel.
   - **Number values**: Enter a numeric value, or select a number variable.
   - **Boolean values**: Enter `true` or `false`, or select a boolean variable.
   - **Color values**: Enter a hex code or choose one from the color picker.

Do your variables have multiple modes? [Learn more about setting variable values to specific mode values](https://help.figma.com/hc/en-us/articles/15253268379799).

**Tip:** Setting variables in interactions works similarly to its counterpart in Figma Design. For more information about using variables in interactions, we recommend reading the guide to [using variables](../../figma-design/advanced-prototyping/use-variables-in-prototypes.md)—and [variable modes](../../figma-design/advanced-prototyping/variable-modes-in-prototypes.md)—in prototypes. You can also check out the [advanced prototyping examples](https://help.figma.com/hc/en-us/articles/17146044893591) for ideas you can bring to your site.

## Create an interactive component

When you add an interaction to a main component, any instances of that component used on your site will inherit the interaction.

Use inherited interactions to connect:

- An arrow button to navigate back to the previous screen
- A website footer or navigation menu
- Applying a consistent hover state to all images

**Tip**: You can add additional interactions to instances without detaching them from the main component.

## Troubleshoot interactions between Figma Design and Figma Sites

When copying a Figma Design file with prototype interactions into your site, the interactions should automatically convert to the corresponding interactions in Figma Sites.

In some cases, Figma may not find a matching interaction. To troubleshoot and fix these interactions:

![Review issues modal showing unsupported interactions: "Mouse move inside" trigger and "Smart animate" animation, with options to replace or fix.](https://help.figma.com/hc/article_attachments/31937329768471)

**Check the Review issues modal**

After copy and pasting into a Figma Sites file, check for any unsupported triggers or actions using the **Review issues** modal.

To access this modal, click **Review issues** at the bottom left corner of the file. You can also click **Publish** in the left sidebar, then click **Issues**.

![Figma interface showing an Interaction tab with a selected interaction type, "Mouse move inside," with the unsupported action icon.](https://help.figma.com/hc/article_attachments/31937329770647)

**Update the interaction**

In the **Interaction** tab of the right sidebar, unsupported interactions are represented by the icon.

Click the interaction and choose a different trigger or action to get it working again.
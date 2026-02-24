# Variable modes in prototypes

Source: https://help.figma.com/hc/en-us/articles/15253268379799-Variable-modes-in-prototypes

---

Before you start

Who can use this feature

 

Use variables with prototypes on [any paid plan](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features). The number of variable modes available per collection depends on your plan.

Anyone with `can edit` access to a file can create prototypes.

Anyone with `can view` or `can view prototypes only` access to a file can view prototypes.

Each variable in your collection can have multiple modes. You can select and use the values for specific modes in your prototyping actions and expressions.

There are several ways you can use variable modes to enhance your prototyping experience:

- **Set mode values based on context**: Use multiple mode values of the same variable in your design, and change their values independently in the same interaction
- **Use mode values in expressions**: Use the values of specific mode definitions to build interactions and perform calculations
- **Change variable mode with an interaction**: Use a prototype interaction to change the variable mode of a page

New to variables? Learn more here:

- [Guide to variables →](https://help.figma.com/hc/en-us/articles/15339657135383)
- [Use variables in prototypes →](https://help.figma.com/hc/en-us/articles/14506587589399)

Want to get more hands on practice?

Check out the [advanced prototyping playground file →](https://www.figma.com/community/file/1234939241273272375)

## Set mode values based on context

When a variable has multiple mode definitions, use the **Set variable** action and mode context to change the value of a specific mode definition.

This can be helpful when modifying only one mode definition of a variable. When displaying or using multiple modes of the same variable in a design, adjust their values independently from each other.

For example, take a look at the design below:

![Shopping basket interface showing watermelon and mushrooms with adjustable item counters and subtotal of $22.97.](https://help.figma.com/hc/article_attachments/24299587129751)

Each produce item has a counter to adjust the number of items added to the cart.

If a number variable with only a single mode is used to represent the item count, a unique variable and interaction would be needed for each product listing.

Instead, you can use a number variable with multiple modes—one for each unique produce item.

![Variable collection panel showing product details and modes for watermelon and cherries in a prototyping context.](https://help.figma.com/hc/article_attachments/24299571614999)

By using multiple modes, each item count can be updated separately.

1. [Set the mode](https://help.figma.com/hc/en-us/articles/15343816063383) on the parent layers or objects.

1. Select the layer, group, or object that contains the applied variable. (For example, select the frame that contains the product image and information for the melon.)
2. From the **Appearance** section of the right sidebar, click **Apply variable mode**.
3. Hover over a variable collection and choose a mode. (Select the “melon” mode.)
4. Repeat for any other objects or layers that only apply to a specific mode. (Apply the “shiitakes” mode to the frame that contains the product image and information for the shiitake mushrooms).

2. Change the value of the applied variable with the **Set variable** prototype action. (For example, create a **Set variable** interaction on the + icon for each product counter. Set the `Amount in basket` variable to `Amount in basket + 1`.)

Any variables contained within a layer that has a set mode will only update the value of that specific mode definition.

![Product card interface showing variable mode selection for watermelon in a dropdown menu on the properties panel.](https://help.figma.com/hc/article_attachments/24299715047063)

Tip: Use [components](../components/guide-to-components-in-figma.md) to save even more time while prototyping with modes. With components, you’ll only need to create the interaction once. Then, place multiple instances on the frame, and change the applied mode for each instance.

## Use mode values in expressions

### Select mode definitions in prototype actions

To select specific variable modes in prototypes:

1. Create or click on an existing prototype connection to open the **Interaction** modal.
2. Click on any variable name that you’ve used in the interaction.
3. From the **Modes** dropdown menu, select a specific mode of that variable.

Once you’ve selected a mode, the variable is represented with both the variable name and mode name:

`variableName:modeName`

![An interaction details modal. The user clicks the objectType variable from the to field, and sets it to the objectType:apple mode.](https://help.figma.com/hc/article_attachments/15318964757527)

Tip: You can also use your keyboard to build expressions. To select a specific mode in the expression builder, enter in a variable. Then, press ← to highlight the variable name, and use your ↑ up and ↓ down arrows to select the mode. Press `enter` to confirm.

### Build expressions with mode values

Use expressions with variable modes to calculate values across a single variable.

This can be helpful when writing expressions that use multiple mode definitions of one variable.

For example, consider the same design from above. This time, there are fields to calculate the item subtotal of each produce item, and an overall total to calculate the total price of the entire order.

![My basket screen showing item counters for watermelon and mushrooms with subtotal and schedule pick-up button.](https://help.figma.com/hc/article_attachments/24299587129751)

Tip: In order to apply different modes of the same variable on a the same design, [apply a variable mode to the frame or component layer](https://help.figma.com/hc/en-us/articles/15343816063383).

Now, take a look at the variable collection:

![Figma variables panel showing product data for Watermelon and Cherry, including product name, price, and amount in basket.](https://help.figma.com/hc/article_attachments/24299571614999)

When using expressions, there are times when you’ll need separate values for each variable mode. For example, to calculate the `subtotal` of each produce type, use an expression that multiplies the mode’s `Price` by its `Amount in basket`.

![Prototyping interface shows watermelon product with on-tap interaction to set "Amount in basket" variable for item count adjustment.](https://help.figma.com/hc/article_attachments/24299587143575)

Other times, you’ll need a single variable value to represent the total of different modes. For example, to calculate the order total, create a new variable collection for the `cartTotal` variable with only one mode.

Want to learn more best practices for prototyping with variables? Subscribe to [Figma’s YouTube channel](https://www.youtube.com/channel/UCQsVmhSa4X-G3lHlUtejzLA).

## Change variable mode with an interaction

Use the **Set variable mode** prototype action to change the variable mode of the current page.

For example, if you have a design with a light and dark mode, you can use the **Set variable mode** action to switch between modes while playing a prototype.

![Interactive card layout with a starry sky image, title, description, tags, and a toggle for light/dark mode.](https://help.figma.com/hc/article_attachments/23288995910295)

To use the **Set variable mode** prototype action:

1. Create a [prototype interaction](https://help.figma.com/hc/en-us/articles/360040315773-Create-interactions).
2. For the prototype action, select **Set variable mode** and do the following:
   1. From the first dropdown menu, select a variable collection.
   2. From the second dropdown menu, select a variable mode.

The **Set variable mode** action changes the mode for the current page, and will change the mode for any objects on that page that have their mode set to **Auto**. Any mode explicitly defined on an object will still be used for itself and any nested children, regardless of the page level mode.

[Learn more about setting variable modes on objects →](../variables/modes-for-variables.md#h_01H3ADKDF7JBTRV1Z5P1X1DZVE)
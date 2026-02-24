# Use variables in prototypes

Source: https://help.figma.com/hc/en-us/articles/14506587589399-Use-variables-in-prototypes

---

Before you start

Who can use this feature

 

Available on [any paid plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can create prototypes.

In Figma, variables are stored values that represent design attributes or saved states. They can be string, number, color, or boolean value types.

You can set and modify the values of variables with prototyping actions—allowing you to create immersive prototypes that dynamically change based on user selection, using only a few simple frames and interactions. This means you can use prototype actions to:

- Update text content with string variables
- Change object dimensions, corner radius, or auto layout properties with number variables
- Toggle layer visibility with boolean variables

To begin using variables in prototypes, [set up your variables](#h_01H91B3F513CRWB49MNWXMDAX3), then [use the **Set variable** action](#h_01H91B3F51XXC8CJ8KA55N16JY) to change or modify your variable values.

Once you’ve got the hang of using variables and prototypes together, try some more advanced features to extend their power even further:

- [**Expressions**](https://help.figma.com/hc/en-us/articles/15253194385943): Manipulate variables with basic operations, allowing you to build more advanced prototypes with flexible values
- [**Multiple actions and conditionals**](https://help.figma.com/hc/en-us/articles/15253220891799): Use if/else statements to check if a condition is met before performing actions, and stack an unlimited number of actions on a single trigger

[Learn more about variables in Figma](https://help.figma.com/hc/en-us/articles/15339657135383).

Try it out

Want to get even more practice? Check out the [advanced prototyping playground file](https://www.figma.com/community/file/1234939241273272375).

Looking for more examples of how you can use variables in prototypes? Check out some more [advanced prototyping examples](advanced-prototyping-examples.md).

## Set up your variables

Before you can prototype with variables, you need to:

1. **Create your variables**: [Learn how to create and organize variable collections](https://help.figma.com/hc/en-us/articles/15145852043927/).
2. **Apply variables**: [Learn how to apply variables to text content, object dimensions, layer visibility, and more](https://help.figma.com/hc/en-us/articles/15343107263511).

## Set variable values

Once you’ve created and applied variables throughout your design, you can start using them with prototypes.

Each prototype interaction has a trigger (what causes the prototype to advance forward) and one or more multiple actions (what happens as a result of the trigger).

The **Set variable** action allows you to set or modify the value of a variable as a result of a prototype trigger.

To use the **Set variable** action on a prototype interaction:

1. Create a [prototype interaction](https://help.figma.com/hc/en-us/articles/360040315773-Prototype-interactions-and-animations).
2. Navigate to the **Interaction** modal and select a trigger from the dropdown menu.
3. From the **Action** dropdown menu, select **Set variable**.
4. From the **Target** dropdown menu, select the variable you want to set a new value for.
5. In the **Value** field, enter in a new value for the variable. The new value type must match the variable type you’re changing. For example, if you selected a number variable, the new value must also be a number.
   - **String values**: Enter any text string literal (contained in quotations), or select any string variable from the selection panel
   - **Number values**: Enter any number value, or select any number variable from the selection panel
   - **Boolean values**: Enter `true` or `false`, or select any boolean variable from the selection panel
   - **Color values**: Enter any hex code, or select a hex code from the color picker
6. [Play your prototype](https://help.figma.com/hc/en-us/articles/360040318013-Present-designs-and-prototypes) to test the interaction.

![A design with two frames. A prototype action is set on an image on the first frame. When the image is clicked, the profileName variable will update it's value, and the prototype will navigate to the next frame.](https://help.figma.com/hc/article_attachments/27771812192407)

Note:

Do your variables have multiple modes? [Learn more about setting variable values to specific mode values](https://help.figma.com/hc/en-us/articles/15253268379799).

Tip:

Use [expressions](https://help.figma.com/hc/en-us/articles/15253194385943) to manipulate variables with operations. For example, you can perform basic math on number variables, combine multiple string variables together, or use boolean expressions.

Try it out

Let’s create a collection of variables titled “Shapes”. This collection will include one string variable that represents the name of the shape.

1. Deselect all items on the canvas, then find the **Local variables** section in the right sidebar and click  **Open variables**.
2. Click **Create variable**, and select **String**.
3. In the **Name** column, enter “shapeName”.
4. In the **Value** column, enter “circle”.![The variables modal is open. A string variable with the name shapeName has a value of circle.](https://help.figma.com/hc/article_attachments/27771812195735)

Now, you can apply the `shapeName` variable to your design. For this example, we’ve created a simple design that includes a frame with two shapes (a circle and a square) and two text layers. We want to bind the `shapeName` variable to the bottom text layer so that it changes based on the selected shape.

1. Recreate the design pictured below. Add an ellipse object, a rectangle object, and two text layers to a frame. Enter “You picked:” as the content of the first text layer.
2. Click to select the bottom text layer on your frame.
3. From the **Design** tab in the right sidebar, find the **Text** section and click  **Apply variable**.
4. Select the `shapeName` variable from the variable selection panel to apply it to the text content.![A frame with an ellipse object, a square object, a text layer that says YOU PICKED and a selected text layer that says CIRCLE. With the second text layer selected, the mouse is hovering over the Apply variable icon from the Text section of the right sidebar.](https://help.figma.com/hc/article_attachments/27771782046743)

Now, let’s add an interaction with a **Set variable** action.

1. Select the ellipse object.
2. From the right sidebar, switch to the **Prototype** tab. In in **Interactions** section, click  the plus sign to add a new interaction.
3. In the **Interaction** modal, create an interaction with an **On tap/On click** trigger and the **Set variable** action.
4. Select the `shapeName` variable from the **Target** dropdown menu. In the **Value** field, set the new value to “circle”.
5. Repeat steps 1-4 for the rectangle object. This time, set the `shapeName` variable to “square”.

![A circle object is selected on the frame, with the Interaction modal open. An interaction is set: Trigger is On tap, Action is Set variable, Target is shapeName, and Value is circle.](https://help.figma.com/hc/article_attachments/27771812199959)

Now, you’re ready to [play your prototype](https://help.figma.com/hc/en-us/articles/360040318013-Present-designs-and-prototypes) to test it out. When you click each shape object, the text layer will automatically update based on the new variable value.![The prototype is being played. When the ellipse object is selected, the bottom text layer updates to circle. When the square object is selected, the bottom text layer updates to square.](https://help.figma.com/hc/article_attachments/27771812214551)

## Prototype with variables and components

Once you’ve learned the basics, you can start using variables and components together in your prototypes.

Apply variables to components to automatically update your component when you change the value of a variable in a prototype. Any change in variable value also updates any other elements bound to that same variable.

The value of a variable can be changed by:

- Using the **Set variable** action
- Using the **Change to** action in an interactive component
- Using the **Set variable mode** action

Example

An interactive button component set has a `default` and a `hover` state. The component uses the **Change to** action, so that when you hover over the `default` variant, it switches to the `hover` variant (and vice versa).

A boolean `hoverState` variable is applied to both an instance of the variant and the visibility of a separate, overlay layer.

When you hover over the `default` variant in your prototype:

- The instance updates to the `hover` variant
- The `hoverState` boolean variable updates from false to true
- The image layer is made visible

Want to practice with a similar example? Check out the “Try it out” section below.

The location where you apply the variable determines the scope of changes in the prototype.

|  |  |
| --- | --- |
| **Apply variable to:** | **When prototyping:** |
| Variant properties of component instances | Change the value of the variable to update the variant of the instance. |
| Component properties | Change the value of the variable to update all instances of the component. |

[Learn more about applying variables to component and variant properties](../variables/apply-variables-to-designs.md).

Try it out: Example 1

1. Create an [interactive component set](../components/create-interactive-components-with-variants.md).
   1. Create a button component that has a “clicked” variant property with “true” and “false” values.
   2. Add a prototype interaction on the “false” variant, using the **On click** trigger and the **Change to** action. Now, when the false variant is clicked, it will switch to the true variant.![A component set of a button. One variant is blue, the other variant is grayed out. The component set has a variant property with true and false values.](https://help.figma.com/hc/article_attachments/27771782056983)
2. Place an instance of a variant from the interactive component set in a frame.
   1. Add the false variant to a frame.
3. Assign a variable to the interactive component instance. The value of the variable must match a [variant property value](https://help.figma.com/hc/en-us/articles/360056440594#Variant_properties_and_values).
   1. Create a boolean `circleVisibility` variable with a default false value.
   2. Select the instance of the button.
   3. From the right sidebar, hover over the clicked variant property.
   4. Select  **Apply variable**.
   5. Click to select the `circleVisibility` variable to bind to the property.![An instance of the false button variant is on the frame. The instance is selected, and the user is hovering over the Apply variable button, where they see a list of variables they can apply.](https://help.figma.com/hc/article_attachments/27771782060055)
4. Assign the same variable to another layer in your design.
   1. Add an ellipse object to the frame.
   2. From the **Appearance** section of the right sidebar, right-click the  **Hide** icon.
   3. Select the `circleVisibility` variable to apply the boolean variable to the visibility of the ellipse layer.![An ellipse object is selected on the frame. From the Appearance section of the right sidebar, a mouse is hovering over the Hide icon.](https://help.figma.com/hc/article_attachments/27771782062743)
5. Play your prototype to test the interaction. When the interaction is triggered and the component is changed, the value of the variable also changes. This means that if you have that same variable bound to any other values, those will also update.![A prototype plays. When a button is clicked, the button changes to a grayed out variant, and an ellipse appears.](https://help.figma.com/hc/article_attachments/27771812222231)

Try it out: Example 2

1. Create a component set with at least two variants.
   1. Create a component set that has a “shape” variant property with “circle” and “square” values.![A component set with circle and square variants.](https://help.figma.com/hc/article_attachments/27771812226071)
2. Place an instance of a variant on a frame.
3. Assign a variable to the instance. The value of the variable must match a [variant property value](https://help.figma.com/hc/en-us/articles/360056440594#Variant_properties_and_values).
   1. Create a `shapeType` string variable with a default “circle” value.
   2. Click on the instance to select it.
   3. From the right sidebar, hover to the right of a variant property and click  **Assign variable**.
   4. Select the variable you’d like to bind to the property.![An instance of the circle variant is on a frame. From the right sidebar, in the component section, a mouse hovers over the Apply variable icon.](https://help.figma.com/hc/article_attachments/27771782070039)
4. Create an interaction on any object within the frame that uses the **Set variable** action. Change the value of the variable to match the value of the unused variant property.
   1. Add a prototype interaction on an object, using the **On click/On tap** trigger and the **Set variable** action. Set the `shapeType` variable value to “square”.![A button object that says Square is on the frame. On the button, there is a prototype interaction. The Interaction modal is open, with a On click trigger, a Set variable action, a shapeType target, and a value of square (in quotation marks).](https://help.figma.com/hc/article_attachments/27771812230551)
5. Play your prototype to test the interaction. When the interaction is triggered and the variable is changed, the variant also updates.![A prototype plays. When a button that says square is pressed, the object becomes a square.](https://help.figma.com/hc/article_attachments/27771812232599)
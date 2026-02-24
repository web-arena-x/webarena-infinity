# Advanced prototyping examples

Source: https://help.figma.com/hc/en-us/articles/17146044893591-Advanced-prototyping-examples

---

Advanced prototyping features (such as [variables](use-variables-in-prototypes.md), [conditionals](multiple-actions-and-conditionals.md), and [expressions](use-expressions-in-prototypes.md)) allow you to add a higher level of fidelity to prototypes, while reducing the number of frames and interactions needed to do so.

Use the examples below to inspire you on how you might use advanced prototyping features in your designs.

Create a required checkbox interaction

In this prototype, create a button with a required checkbox interaction.

Features used:

[Variables](../variables/guide-to-variables-in-figma.md), [interactive components](../components/create-interactive-components-with-variants.md), [component properties](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties), [using variables with interactive components](use-variables-in-prototypes.md#Use_variables_with_interactive_components)

![A prototype. When the checkbox is checked off, the continue button becomes activated.](https://help.figma.com/hc/article_attachments/17146056341015)

This interaction is common in online forms. For example, you might be required to agree to a site’s terms and conditions by selecting a checkbox before you can click a **Continue** button.

1. Create an [interactive component](../components/create-interactive-components-with-variants.md) set with two variants to represent a checkbox.
   1. Name the [component property](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties) `isChecked`, with “true” and “false” variants.
   2. Add a **Change to** prototype action between both variants—so when you click on the false variant, it will change to the true variant, and vice versa.![A checkbox component set, with true and false variants. There are interactions created between the true and false variants.](https://help.figma.com/hc/article_attachments/17146028674967)
2. Create another component set for a continue button. One variant should represent an inactive state, and the other should represent an active state.
   1. Name the [component property](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties) `hasAcceptedTerms` with “true” and “false” value names. The “true” variant represents the active button state, and the “false” variant represents the inactive button state.![A continue button component set, with true and false variants.](https://help.figma.com/hc/article_attachments/17146082104471)
3. [Create a boolean variable](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables) named “hasAcceptedTerms”, with a value of false.
4. [Add instances](../use-libraries/create-and-insert-component-instances.md) of your components to your design.
   1. Add an instance of the “false” continue button variant.
   2. Add an instance of the “false” checkbox variant.![A design with the false continue button variant and a false checkbox variant.](https://help.figma.com/hc/article_attachments/17146056356375)
5. Assign the `hasAcceptedTerms` boolean variable to both instances.
   1. Click on the checkbox instance to select it.
   2. From the right sidebar, hover to the right of the variant property and click  **Assign variable**.
   3. Select the `hasAcceptedTerms` variable to bind it to the property.
   4. Repeat steps A through C for the continue button instance.![The checkbox instance is selected. In the right side panel, the mouse is hovering over the Apply variable icon.](https://help.figma.com/hc/article_attachments/17146028685591)

      Tip:

      You can bind a variable to a variant property as long as the values match. Since the boolean variable has `true` and `false` values, and the variant properties have `true` and `false` values, you can bind them together.

      Now, whenever the variable changes to a true value, the instances will also change to their true variant.
6. Return to your continue button component set, and add an action to the active button variant. For example, you can add an **On click** interaction that navigates to the next frame.![A connection between the true variant of the continue button component and a frame.](https://help.figma.com/hc/article_attachments/17146082117271)
7. [Play your prototype](../view-prototypes/play-your-prototypes.md) to test it out.

Add an error message for empty selection states

In this prototype, you can create a form that shows an error if users try to submit it without answering all the questions.

Features used:

[Variables](../variables/guide-to-variables-in-figma.md), [interactive components](../components/create-interactive-components-with-variants.md), [component properties](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties), [using variables with interactive components](use-variables-in-prototypes.md#Use_variables_with_interactive_components), [boolean expressions](use-expressions-in-prototypes.md#Boolean_expressions), [overlays](../create-prototypes/create-overlays-in-your-prototypes.md)

![A prototype. The design has two questions, and when one response is left blank, an error message overlay opens.](https://help.figma.com/hc/article_attachments/17146617169303)

1. In this example, each question has two radio buttons a user can use to select their answer. Let’s create an [interactive component](../components/create-interactive-components-with-variants.md) set to represent each state the answer can be in: nothing selected, choice 1 selected, or choice 2 selected.
   1. Make three variants to represent each state.
   2. Name the [component property](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties) `selectedState`, with “choice1”, “choice2”, and “none” as variants.
   3. Add a **Change to** prototype action between each variant—so whenever you click on the “Choice 1” object, the variant changes to choice1, and whenever you click the “Choice 2” object, the variant changes to choice2.![A radio button component set, with component properties and interactions set between variants.](https://help.figma.com/hc/article_attachments/17146617180055)
2. Since our form will have two questions, let’s [create two string variables](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables). These variables will let us validate whether the form is complete or not when a user submits it.
   1. Name the first string variable “question1response”, with a value of “none”.
   2. Name the second string variable “question2response”, with a value of “none”.
3. Now, let’s assemble our prototype. Add a frame to represent the design of your form. Include two instances of the “none” radio button variant, and a **Submit** button.
4. Assign the variables to the radio button instances.
   1. Click on the first radio button instance to select it.
   2. From the right sidebar, hover to the right of the variant property and click  **Assign variable**.
   3. Select the `question1response` variable to bind it to the property.
   4. Repeat steps A through C for the second radio button instance, this time selecting the `question2response` variable.![An instance of a component is selected on the frame. The mouse is hovering over the Apply variable button in the right sidebar.](https://help.figma.com/hc/article_attachments/17146617181079)
5. Add two more frames: one to represent an error message [overlay](../create-prototypes/create-overlays-in-your-prototypes.md), and one to represent a success message.![Three frames on the canvas: a starting frame, an overlay frame, and a success message frame.](https://help.figma.com/hc/article_attachments/17146617195671)
6. Add a **On tap** prototype interaction to the **Submit** button. Use the **Conditional** action:
   1. If `question1response` == “none” **or** `question2response` == “none”, open the error message frame as an overlay.
   2. Else, **Navigate to** the success message frame.![Interaction details on a Submit button, including a conditional statement.](https://help.figma.com/hc/article_attachments/17146617198359)
7. [Play your prototype](../view-prototypes/play-your-prototypes.md) to test it out.

Display count of selected items

In this prototype, we’ll increase a counter each time a user makes a selection.

Features used:

[Variables](../variables/guide-to-variables-in-figma.md), [interactive components](../components/create-interactive-components-with-variants.md), [component properties](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties), [using variables with interactive components](use-variables-in-prototypes.md#h_01H91B3F52N921482A3051SJEX)

![Interactive prototype on a phone screen showing item selection with counter incrementing from 0 as boxes are clicked.](https://help.figma.com/hc/article_attachments/17148702003351)

This type of interaction has several applications. For example, you might see the total number of items you’ve added to your cart on an e-commerce site, how many photos or messages you’ve selected in a messaging or social media app, or even how many glasses of water you’ve drank in your habit tracking app.

1. Create an [interactive component](../components/create-interactive-components-with-variants.md) set with two variants to represent a selected and unselected state.
   1. Add a **Change to** prototype action between both variants—so when you click on the unselected variant, it will change to the true variant, and vice versa.![count items selected - interactive component set up.png](https://help.figma.com/hc/article_attachments/17148714793879)
2. [Add multiple instances](../use-libraries/create-and-insert-component-instances.md) of the unselected variant to your design.
3. Add a text layer to your design that represents the number of selected items.

   In our design, we’ve added two text layers in a single frame. One text layer states “Items selected:”, and the second text layer states “0”.

   ![item counter - show text frame layers.png](https://help.figma.com/hc/article_attachments/17148702014615)
4. [Create a number variable](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables) named “itemsSelected”, with a value of 0. We’ll use this variable to store a count of how many items have been selected.
5. Assign the `itemsSelected` variable to the text layer.
   1. Click on the “0” text layer to select it.
   2. From the **Text** section of right sidebar, click  **Assign variable**.
   3. Select the `itemsSelected` variable to bind it to the text layer.![display number of selected items - bind variable to text.png](https://help.figma.com/hc/article_attachments/17148714799127)
6. Return to your component set, and add an additional prototype action to each variant that calculates the number of selected items.
   1. On the false variant, add a **Set variable** action that sets the value of the `itemsSelected` variable to `itemsSelected + 1`.
   2. On the true variant, add a **Set variable** action that sets the value of the `itemsSelected` variable to `itemsSelected - 1`.![display number selected -- add expressions.png](https://help.figma.com/hc/article_attachments/17148714805655)
7. [Play your prototype](../view-prototypes/play-your-prototypes.md) to test it out.

Build a click counter

In this prototype, build a click counter. When a user clicks an object or objects the required amount of times, a success interaction initiates.

Features used:

[Variables](../variables/guide-to-variables-in-figma.md), [expressions](use-expressions-in-prototypes.md), [conditionals](multiple-actions-and-conditionals.md)

![The prototype plays. A blue square is clicked 5 times, and then a You Did It success message appears.](https://help.figma.com/hc/article_attachments/17146624784919)

This type of interaction might be seen in the real world when users need to select a specific number of items to continue. For example, users might need to select a certain number of topics that interest them in an onboarding experience to customize their profile, or users might need to select a certain number of toppings to add to their meal in a food delivery app.

1. Add two variables:

- A number variable named `clickCount`, with a starting value of `0`
- A boolean variable named `clickComplete`, with a starting value of `false`

2. Add a rectangle object to a frame.
3. On the rectangle object, add a prototype interaction with an **On click/On tap** trigger. Add two actions, in this order:

1. **Set variable**: `clickCount` to `clickCount + 1`
2. **Conditional**: If `clickCount == 5`, **Set variable** `clickComplete` to `true`![A rectangle object on a frame. The rectangle has an interaction: On tap, set variable clickCount to clickCount + 1. If clickCount == 5, set variable clickComplete to true.](https://help.figma.com/hc/article_attachments/17146637178903)

4. Add two text layers to the frame:

1. The first text layer should list simple instructions (“Press the square 5 times.”)
2. The second text layer should be a success message (“You did it!)

5. Apply the `clickComplete` variable to the layer visibility of the second text layer:

1. Select the text layer.
2. Go to the **Layer** section of the right sidebar and right-click the visibility icon.
3. Click the `clickComplete` variable from the variable selection panel. Now, the layer will only be visible if the `clickComplete` variable value is true.![A text layer beneath the square says You Did It. The text layer is selected, and a mouse is hovering overing the visibility icon from the Layer section of the right sidebar.](https://help.figma.com/hc/article_attachments/17146637180439)

6. [Play your prototype](../view-prototypes/play-your-prototypes.md) to test the interaction.

Build a volume control bar

In this example, we'll use variables to build a volume control bar.

Features used:

[Variables](../variables/guide-to-variables-in-figma.md), [expressions](use-expressions-in-prototypes.md)

![The prototype plays. When the plus sign is clicked, volume level increases in width. When minus button is clicked, volume level decreases in width.](https://help.figma.com/hc/article_attachments/17147402781335)

To begin, set up your frame with a few basic shapes to represent the volume bar and the controls:

- Add one rectangle to represent the volume container—ours has a width of 260 and a height of 100.
- Add a second rectangle to represent the volume level. This rectangle should be placed on top of the first one, and they should be aligned on the left side. The width of the second rectangle should be smaller than the first—ours has a height of 100 and a width of 14 to start.
- Use lines to create objects that represent a plus sign and a minus sign, and place them beneath the volume container.

![A frame with a design of a volume control bar, consisting of two rectangle objects, a plus sign, and a minus sign.](https://help.figma.com/hc/article_attachments/17147402763287)

Next, we need to create a variable. In a new collection, create a number variable. Name it `volumeLevel` and give it an initial value of 14.

Now, let’s bind the `volumeLevel` variable to the width value of the rectangle representing the volume level.

1. Click on the smaller rectangle to select it.
2. From the **Design** tab of the right sidebar, find the width value.
3. Hover over the width value field, then select  **Apply variable**.
4. From the variable selectional panel, select the `volumeLevel` variable. ![With the smaller rectangle selected, navigate to the Width property and click Apply variable.](https://help.figma.com/hc/article_attachments/17147402766871)

Now that our frame and variables are set up, let’s create our prototyping interactions.

1. Click the plus sign object on the frame.
2. From the **Prototype** tab on the right sidebar, click  the plus icon to add a new interaction.
3. Set the trigger to **On tap/On click**, and set the action to **Set variable**. Select the `volumeLevel` variable.
4. Set the new value using an expression. We want the width of the volume level to increase by 5 each time a user presses the plus icon, so we’ll use the following expression:  
   `volumeLevel + 5`
5. Repeat steps 1-4 for the minus icon, this time setting the new variable value with the following expression:  
   `volumeLevel - 5`![The plus sign is selected, and has the following interaction: Set volumeLevel to volumeLevel + 5](https://help.figma.com/hc/article_attachments/17147402774295)

[Play your prototype](https://help.figma.com/hc/en-us/articles/360040318013-Present-designs-and-prototypes) to test the interactions.
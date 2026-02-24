# Create interactive components with variants

Source: https://help.figma.com/hc/en-us/articles/360061175334-Create-interactive-components-with-variants

---

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with can edit access can create interactive components.

Anyone with can edit access to the file can publish components to a library.

New to Prototyping? Check out our **[Guide to prototyping in Figma →](https://help.figma.com/hc/en-us/articles/360040314193)**

Interactive components allow you to create prototype interactions between variants in a component set. Any time you add an instance to your designs, those interactions are set up and ready to go. This saves you time when creating prototypes and prevents unnecessary noodle soup.

- Create interactive elements that automatically switch between variants, like buttons that change from hover to pressed states.
- Set default interactions at a component level and remove the guesswork when it comes to building prototypes.
- Reduce the amount of frames and connections needed to prototype input fields, like a set of checkboxes or toggles.

Note: Interactive components are an extension of variants. If you don't have a component set to work with, you'll need to create one first. **[Learn how to create and use variants →](https://help.figma.com/hc/en-us/articles/360056440594)**

### Before variant interactions

In the example below we've added all the possible connections to prototype a frame with five checkboxes. Without interactive components, we would need to duplicate the same frame 32 times and create 160 connections between them to prototype every possible combination.

![An animation showing a complex network of connections for a frame with multiple check boxes.](https://help.figma.com/hc/article_attachments/4411468633495)

### With variant interactions

With interactive components, we only need to add an instance of the checkbox to our design and its variant interactions are ready to go. When we view the prototype, Figma automatically switches between the checked and unchecked variants.

![](https://help.figma.com/hc/article_attachments/24732453592343)

# Create interactive components

You can only create interactive components using variants from the same component set. If you don't have a component set to work with, you'll need to create one first. **[Learn how to create variants →](https://help.figma.com/hc/en-us/articles/360056440594)**

## Create variant interactions

Interactive components introduces a new [prototype action](https://help.figma.com/hc/en-us/articles/360040035874): **Change to**.

1. Navigate to the **Prototype** tab of the right sidebar.
2. Click the  on the frame's bounding box and drag it to the destination variant. You can also click the  in the **Interactions** section of the **Prototype** panel, set the action to **Change to**, then select the destination variant using the dropdown menu.
3. Once the connection has been made, use the **Interaction** panel to adjust the trigger and action.

![](https://help.figma.com/hc/article_attachments/24732407117463)

You can also use the **Change to** action on a nested instance to change the parent component variant. In the example below, a variant from a component set is nested within another `Expandable` component set. A **Change to** interaction is placed on the nested instance to change the parent component from its `Collapsed` variant to its `Expanded` variant.

![](https://help.figma.com/hc/article_attachments/24732453601687)

Hands-on learner? **[Explore the interactive components playground file →](https://www.figma.com/community/file/1033456279024883078)**

# Use interactive components

Add instances of interactive components to your designs like any other component. The only difference is the instances already have interactions applied for prototyping.

To use interactive components:

1. [Add an instance](https://help.figma.com/hc/en-us/articles/360039150173-Create-an-instance-of-a-component#Component_from_other_files) of an interactive component to a frame in your design.
2. When you're ready to prototype your design, navigate to the **Prototype** tab of the right sidebar.
3. [Build your prototype](https://help.figma.com/hc/en-us/articles/360040314193).
4. [Preview designs and interactions in Presentation view](https://help.figma.com/hc/en-us/articles/360040318013).

Note: Figma will [use the existing rules to preserve any overrides](https://help.figma.com/hc/en-us/articles/360039150733-Apply-overrides-to-instances#Preserve_overrides) you apply to the default variant in a component set. For example: changing the contents of a button label or swapping an icon.

When you add an instance of a component set to the canvas, you also bring along the other variants in that component set. While you can technically still apply overrides to those other variants, Figma won't reflect those overrides in presentation view.

## Add more interactions

When you're building a prototype with interactive components, you can add regular interactions on top of the variant interactions.

In the example below, we have added an interaction with a hover trigger on top of the variant interaction triggered by a click.

![](https://help.figma.com/hc/article_attachments/24732407133463)

The interaction order will depend on whether the triggers you use are the same triggers as the variant interactions. **[Learn more about prototype triggers →](https://help.figma.com/hc/en-us/articles/360040035834)**

### Same triggers

When both interactions use the same trigger, Figma will use the prototype interaction and ignore the variant interaction.

For example:

1. A toggle switch has an `On click` → `Change to` variant interaction between the **On** and **Off** variants in its component set.
2. You add an `On click` → `Navigate to` interaction from the toggle switch to another frame.

Figma will navigate to the next frame when the user clicks on the toggle switch.

### Different triggers

When you add an interaction with a different trigger, Figma will play both the interaction and the variant interactions.

For example:

1. A button has an `On hover` → `Change to` variant interaction between the **default** and **hover** variants.
2. You add an `On click` → `Navigate to` interaction when building your prototype.

Figma will `Change to` the **hover** variant on `hover` , then `Navigate to` the next frame `On click`.

## View interactions

When using interactive components, you will see separate sections for **Interactions** and **Variant interactions** in the **Prototype** tab of the right sidebar.

- Use the **Interactions** section to [create prototype interactions and animations](https://help.figma.com/hc/en-us/articles/360040315773-Prototype-interactions-and-animations)
- Use the **Variant interactions** section view a variant interaction's details

## Edit variant interactions

You can override a variant interaction for an instance in your prototype. If you want to edit a variant interaction for the main component, you'll need to do so from the source file.

To access a component set from an instance and make your edits:

1. In design mode, select the instance.
2. At the top of the right sidebar, click .
3. Select **Go to main component**.
4. Navigate to the **Prototype** tab of the right sidebar.
5. Make your edits to the variant interactions.

## State management across frames

Your prototypes likely involve interactions across multiple frames. By default, Figma uses state management controls to determine how interactive components work across frames.

- **State memorization**: Figma memorizes the last set variant of your interactive component.

  For example, you might have an interactive component for a checkbox. If you set the interactive component to the checked variant, Figma remembers the state of that variant. This means that if you navigate away from that frame and come back to it later, the interactive component will remain in the checked state.
- **State sharing**: Figma shares states between matching interactive components. States are only shared after the component has been initially interacted with.

  For example, you might have an interactive component for a checkbox, with an instance of the component on each of two frames. If you set the interactive component to the checked variant on the first frame, then navigate to the second frame, the matching component on the second frame will also be set to the checked variant.

If you don’t want to maintain states across frames, check off **Reset component state** on the **Interaction details** panel of the prototype interaction.

[Learn more about prototype state management →](https://help.figma.com/hc/en-us/articles/14397859494295)

## Use with variables

Apply [variables](https://help.figma.com/hc/en-us/articles/15339657135383) to interactive components to extend their power even further.

When you click an interactive component with an applied variable:

- The variant updates
- The variable updates, which in turn updates any other elements bound to that same variable

Learn more about [using variables with interactive components →](https://help.figma.com/hc/en-us/articles/14506587589399#Use_variables_with_interactive_components)

## Interactive components with custom fonts

When using custom fonts for text inside interactive components, keep in mind that prototype viewers might not have those custom fonts installed on their devices. In these cases, Figma uses cached information about variants of interactive components to display custom fonts correctly when presenting a prototype, but may replace a font with Inter when we can’t both preserve text overrides and change font settings for an interaction.

For example, let's say a person viewing your prototype doesn't have the custom font being used installed on their device. If an instance of an interactive component has a text overrides:

- Figma may replace the custom font with Inter if the change in variants includes changing a font setting like weight or underline.
- Figma will display the correct font if the change in variant isn't related to a font setting, like a button's background color.

We recommend using [Google fonts](https://fonts.google.com/) for prototypes that are being shared with viewers who may not have access to custom fonts in your designs. If your team is on the [Organization or Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273-Compare-teams-and-plans#Organization_plan), you can make sure prototype viewers have access to custom fonts by [uploading them as shared fonts](https://help.figma.com/hc/en-us/articles/360039956774).
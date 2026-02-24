# Multiple actions and conditionals

Source: https://help.figma.com/hc/en-us/articles/15253220891799-Multiple-actions-and-conditionals

---

Before you start

Who can use this feature

 

Available on [any paid plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can create prototypes.

Anyone with `can view` or `can view prototypes only` access to a file can view prototypes.

As your prototypes increase in depth and complexity, you can use multiple actions and conditionals to handle multiple or different outcomes within the same interaction.

- **Multiple actions**: Stack an unlimited number of actions on the same trigger
- **Conditionals**: Check if a condition is met before performing an action by using an if/else conditional statement

New to variables? Learn more here:

- [Guide to variables →](https://help.figma.com/hc/en-us/articles/15339657135383)
- [Use variables in prototypes →](https://help.figma.com/hc/en-us/articles/14506587589399)

Want to get more hands-on practice?

Check out the [advanced prototyping playground file →](https://www.figma.com/community/file/1234939241273272375)

Looking for more examples of how you can use variables in prototypes? Check out some more [advanced prototyping examples →](advanced-prototyping-examples.md)

Note: This video explains prototyping using Figma's old interface. For examples of the new interface, see the images in this article.

## Multiple actions

Every prototype interaction has a trigger and one or more actions. A trigger is what causes the interaction to begin, and an action is the response.

Multiple actions allow you to add an unlimited number of actions on one trigger.

1. Create a [prototype interaction](https://help.figma.com/hc/en-us/articles/360040315773).
2. To add an additional action, click  **Add action**.
3. From the **Interaction** panel, select any action from the **Action** dropdown menu.

![Figma prototype setup showing interaction panel with multiple trigger actions for navigating and overlay options.](https://help.figma.com/hc/article_attachments/24296415473047)

Tip:  Collapse or expand details of each action by clicking the chevron to the left of the action name.

### Reorder actions

Actions run in the order in which they’re listed, from top to bottom.

To reorder actions:

1. Open an **Interactions** panel.
2. Click to the left of the action and drag to change its order.

![Creating a drag interaction in Figma's prototype panel with scrolling behavior settings displayed.](https://help.figma.com/hc/article_attachments/24296390030999)

Tip:  You can drag and drop any action into a **Conditional** action.

Changing the order of actions can change the outcome of a prototype.

For example, two sample prototype actions are listed below. For this example, the starting value of `numberVar` is `1`.

```
1. Set numberVar to 2  
2. Conditional: if numberVar == 2, Navigate to Frame 2
```

In the first action, the number variable is set to a value of `2`. This means the conditional statement (`if numberVar == 2`) is evaluated to be true, so the action (Navigate to Frame 2) executes.

Now, switch the order of the actions:

```
1. Conditional: if numberVar == 2, Navigate to Frame 2  
2. Set numberVar to 2
```

In the first action, the conditional statement (`if numberVar == 2`) is evaluated to be false, so the action does not execute, and the prototype stays on the current frame. Then, the value of `numberVar` is changed to `2`.

### Animation order

[Prototype animations](../guides/prototype-animations.md) can be used to create smooth transitions between pages and define the behavior for actions like **Navigate to**, **Scroll to**, **Open overlay**, and more.

If you have multiple animations on a trigger, they run sequentially.

![Mobile app prototype showing a course selection flow with linked screens for browsing topics: Chemistry, Physics, and Astronomy.](https://help.figma.com/hc/article_attachments/24296833181719)

![Interactive prototype on a phone showing multiple colored sections with geometric icons, demonstrating trigger-based actions.](https://help.figma.com/hc/article_attachments/24296823765655)

## Conditionals

In prototyping, a conditional is a rule that defines if an action should trigger. Conditionals are written with if/else logic.

For example, consider building a checkout flow. *If* the cart total is higher than a certain amount, the user receives free shipping. If not, or *else*, the user sees the full shipping price.

In Figma, you can use the **Conditional** prototype action to build prototypes with conditional logic.

1. Create a [prototype interaction](https://help.figma.com/hc/en-us/articles/360040315773).
2. From the **Interaction** panel, select any trigger from the dropdown menu.
3. From the **Actions** dropdown menu, select **Conditional**.
4. Complete the **If** condition:

1. In the **If** field, write a [boolean expression](https://help.figma.com/hc/en-us/articles/15253194385943#Boolean_expressions) to represent the condition that must be met.
2. Select an action (or multiple actions) from the dropdown menu. These actions will be triggered if the **If** statement is met.

5. Complete the **Else** condition:

1. Select an action (or multiple actions) from the dropdown menu. These actions will be triggered if the **If** statement is not met. Alternatively, leave the **Else** action blank.

![Product card for watermelon with $3.99/ea and interaction panel showing on-tap conditional logic based on basket amount.](https://help.figma.com/hc/article_attachments/24297142876183)

Only conditionals written with [supported operations and format](https://help.figma.com/hc/en-us/articles/15253194385943#Boolean_expressions) will work. Invalid conditional statements will be outlined in red.

### Evaluate conditional statements

Conditional statements are identical to boolean expressions—the statement is evaluated to have a true or false value. If the value of the statement is true, the **if** action is triggered. If the value of the statement is false, the **else** action is triggered.

Learn more about [how to format and evaluate boolean expressions →](https://help.figma.com/hc/en-us/articles/15253194385943#Boolean_expressions)
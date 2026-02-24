# Variables in Dev Mode

Source: https://help.figma.com/hc/en-us/articles/27882809912471-Variables-in-Dev-Mode

---

As a developer, when you’re reviewing designs in Dev Mode, you’ll encounter color, number, string, and boolean variables. The values of those variables can be dependent on things like the variable mode, which sometimes makes it harder to identify the exact values you want to pull from the design.

Figma provides a few options in Dev Mode to make working with variables easier for developers:

- [Variable details](#h_01JD03NW7F4WS8EXKQHS6E5M1V)
- [Suggested variables](#h_01JD03NW7FA3PYRN5PK9GD2VZ5)
- [Access local variable collections](#h_01JD03NW7FX7SE3KQJQYQTZQ7K)

## Variable details

When you're inspecting a design in Dev Mode, you can view details about variables used in the design. The **Variable details** modal lists information about a variable including:

- The name of the variable
- A link to the file that hosts the variable
- The name of the variable collection that contains the variable
- The variable’s mode
- The variable’s value and, if relevant, the chain of aliases to a raw value
- The scope of the variable (where it can be used)
- A code snippet for using the variable

![](https://help.figma.com/hc/article_attachments/27884524069655)

A useful feature is the ability to follow the a chain of [variable aliases](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables#alias) back to a specific value. For example, in the previous image, the **Background/Positive/Default** variable uses **Green/500** as an alias, which corresponds to the color value **#14AE5C**.

Using the **Variable details** modal, you can also change modes, letting you see the other values the variable can have.

## Open the Variable details modal

There are two ways to open the **Variable details** modal:

For variables that appear in a code snippet, such as design tokens in CSS, click on the variable name in the **Inspect** panel to open the **Variable details** modal.

![](https://help.figma.com/hc/article_attachments/27884524074135)

For other variables, such as those that appear in the **Selection colors** section, click **Variable details** in the **Inspect** panel to open the **Variable details** modal.

![](https://help.figma.com/hc/article_attachments/27884533282839)

## Suggested variables

In Dev Mode, when you’re inspecting a design, you’ll sometimes encounter raw values rather than variables or styles. This can happen for a number of reasons, such as if a designer happened to detach a variable during the design phase. When you encounter a raw value, you may want to see if there’s an existing variable that should be used instead.

To help make identifying corresponding variables easier, Dev Mode can suggest variables.

![](https://help.figma.com/hc/article_attachments/27884524079511)

To suggest a variable, the variable must have:

- Exactly the same value
- The appropriate scope

You can click a suggested variable to copy the name.

## Get suggested variables

To get suggested variables for a value in Dev Mode, in the **Inspect** panel, click the value you want to get a suggestion for. The **Suggested variables** modal appears next to the value you clicked.

![](https://help.figma.com/hc/article_attachments/27884524081047)

## Access local variable collections

In Dev Mode, you can access and view the local variable collections in the file.

![Dev Mode panel displays variable details: names, light and dark mode values for Background, Primary, Secondary, and Accent text.](https://help.figma.com/hc/article_attachments/35622418198039)

The **Variables** modal is a read-only version of the [**Variables** modal provided in Figma Design](../variables/create-and-manage-variables-and-collections.md#01H8044A3JKE9Q769Z1926VE4A). For example, in the previous image, the **Collection 1** variable collection is displayed in the modal.

You can click on individual variables and values to copy them to your clipboard and to view details about the variable.

## Open the Variables modal

When you have no layers selected in Dev Mode, you can open a read-only version of the [**Variables** modal provided in Figma Design](../variables/create-and-manage-variables-and-collections.md#01H8044A3JKE9Q769Z1926VE4A). To open the modal, in the **Variables** section of the inspect panel, click **Open variables table**. The read-only **Variables** modal appears.

![](https://help.figma.com/hc/article_attachments/32233528097687)

## Variables in Dev Mode vs. Design

To best provide properties and values as code in Dev Mode, the way a variable is represented is sometimes adjusted.

**Font Weight**

Font weights in CSS can be represented by either strings or numbers. Similarly, in Figma Design, you can provide string variables as the weight for fonts.

In Dev Mode, string variables for font weight aren't provided. If the value of the string variable matches a valid weight for a given font, then the corresponding font weight is provided as a number in Dev Mode.

For example, suppose you have a text layer that uses Inter as the font:

- In the first scenario, you apply a number variable with the value `100` as the font weight. You name the variable `Thin-100`. In Figma Design, `100` corresponds to a valid font weight (Thin) for Inter. When you inspect the layer properties or view the code in Dev Mode, a reference to the variable is provided: `font-weight: var(--Thin-100, 100);`
- In the second scenario, you apply a string variable with the value `Thin` for the font weight. In Figma Design, `Thin` corresponds to a valid font weight (100). In Dev Mode, when you inspect the layer properties or view the code, a reference to the variable is *not* provided: `font-weight: 100;`

In the second scenario, if the string variable matches a valid font weight for a font, the corresponding number is provided. If there is no corresponding number (that is, the string doesn't match a valid weight for the given font), Dev Mode falls back to `400`: `font-weight: 400;`

**Variable names**

To maintain valid CSS, Dev Mode normalizes variable names in code. For example, suppose you have a variable named `🔵 Blue 0000FF`. When you're viewing code in Dev Mode, the property name is rendered as `--blue-0000FF`.
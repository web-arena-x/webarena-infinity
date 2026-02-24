# Modes for variables

Source: https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables

---

**The entry point to the variables modal is moving!** Currently, the variables modal is not discoverable if you have a layer selected. We're slowly rolling out a new left navigation bar to users in Figma Design, which will include the entry point to the variables modal so you can access your variable collections anytime.

![navigation-bar-variables-entry-point.png](https://help.figma.com/hc/article_attachments/37506151518615)  
The variables modal will also be edge-to-edge in your window by default, called **variables view**, so that you can see more of your variables and modes at once. You can still minimize to a modal view like before.

[Learn more about the new navigation bar.](https://help.figma.com/hc/articles/360039831974)

Before you Start

Who can use this feature

Anyone on
[Education, Professional, Organization, and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)
can create and use modes for variables

The number of modes you can create per variable collection
[depends on your plan](https://help.figma.com/hc/en-us/articles/360040328273)

Looking for more resources on variables?
[Check out our guide to variables](https://help.figma.com/hc/en-us/articles/15339657135383).

Variables allow us to store reusable values that can be applied to various design properties—such as color, spacing values, and dimensions.

**Variable modes** allow us to represent different contexts of our designs without needing to create multiple frames for every context that we need. This is because variables can contain multiple values, organized by way of variable modes, where each mode stores one value per variable.

For example, let's say we need to create light and dark mode versions for a design:

> Without variable modes, we could create designs for light mode (our default), then duplicate those designs and update every color fill necessary for dark mode.
>
> If we use variable modes, we would create a collection of variables with two sets of values—or modes—one for light mode as our default and one for dark mode. We would apply the variables to one set of designs. Then, we could quickly switch designs between light and dark modes.
>
> If we need a third color theme, all we need to do is create a new mode and input values for that theme. We wouldn't need to apply the values to our designs all over again.
>
> ![Animation of mode switching where an example basket page for an ecommerce site switches from light mode to dark mode and all the colors instantly update](https://help.figma.com/hc/article_attachments/26978261813911)

There are many contexts that variable modes can help support. Here are a few ideas to get you started:

- Create accessible color themes, like high contrast mode or different themes for color blindness, using color variables
- Localize UI copy to see how copy flows in designs using string variables
- Account for multiple device sizes, like watch, mobile, and desktop, to see how elements respond to varying spacing and padding sizes using number variables

## Create a mode

1. Deselect all objects by clicking anywhere on the canvas.
2. Open the variables modal by clicking  **Open variables** in the **Local variables** section of the right sidebar.
3. Open the collection you want to create a new mode in.
4. From an existing variable, click **New variable mode** to the right of the column headers. Figma duplicates values from the first column to the new one.

You can also duplicate a mode by right-clicking the mode header and selecting **Duplicate mode.**

## Change the default mode of a collection

In the variables modal, the default mode of a variable collection is the left-most column.

When an object is using a variable or when a page contains objects using variables, the object or page will use the default mode's values until you explicitly set a specific mode to the object or page.

![](https://help.figma.com/hc/article_attachments/15463109119383)

To change the default mode of a collection to a different one:

1. From the **Variables** modal, open the variable collection where the variable mode lives.
2. Find the mode and either:
   - Right-click and select **Set as default**,
   - Or click and drag the variable mode to the left-most column.

If an object's or page's variable mode was set to "Auto" or "Default" instead of a specified mode, they will inherit whatever the new default mode is.

If an object or page was explicitly set to a mode that happened to be the default, they will stay linked to that mode even when it is no longer the default.

**Note:** On the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273), you can set a default mode for the team if the library contains a variable collection with at least two modes.

For example, you might have a variable collection that contains spacing values for different screen sizes. The variable collection might have three modes: desktop, tablet, and mobile.

If your workspace is dedicated to mobile apps, you could set the default mode to mobile. When someone creates a new file in the workspace, the page level default mode is set to mobile and applies to all variables used on the page. People can always switch to another mode if they need to.

[Learn how to set a default mode at the team or workspace level.](https://help.figma.com/hc/en-us/articles/21310245473815-Manage-a-library-for-a-workspace-or-organization#h_01HPJA6RTTT98AAYR5EAAXE1CX)

## Reorder modes

To reorder modes in a variable collection, you can either:

- Right-click and select **Move column right** or **Move column left**
- Or, click and drag the column left or right

If you move a column all the way to the left in a variable collection, this column becomes the default mode.

## Import modes

You can import design tokens directly into Figma Design.

### Format requirements

Design tokens must be in a JSON file and follow the [Design Tokens Community Group (DTCG) format](https://www.designtokens.org/tr/2025.10/format/#design-token).

Example

The following example demonstrates how design tokens should be formatted.

```
{
"red": {
"$type": "color",
"$value": {
"colorSpace": "srgb",
"components": [
0.8886906504631042,
0.15790081024169922,
0.15790081024169922
],
"alpha": 1,
"hex": "#E32828"
}
},
"danger": {
"$type": "color",
"$value": "{red}"
},
"border-radius-default": {
"$type": "number",
"$value": 5
},
"button-text": {
"$type": "string",
"$value": "Click here"
},
"visibility": {
"$type": "number",
"$value": 0,
"$extensions": {
"com.figma.type": "boolean"
}
},
"padding-default": {
"$type": "dimension",
"$value": {
"value": 16,
"unit": "px"
}
},
"heading-font": {
"$type": "fontFamily",
"$value": "Inter"
},
"transition-duration": {
"$type": "duration",
"$value": {
"value": 0.3,
"unit": "s"
}
}
}
```

**Note:** Tokens can contain an optional `$extensions` property where the value is a JSON object with arbitrary key-value pairs. Keys in the `$extensions` object are name-spaced, and any Figma extension keys will be prefixed with `com.figma`. For example, `com.figma.type`

### Supported token types

The following token types are supported for import:

|  |  |  |
| --- | --- | --- |
| **DTCG token type** | **Figma variable type** | **Notes** |
| [Color](https://www.designtokens.org/tr/2025.10/format/#color) | Color | The following color spaces are supported:   - HSL - sRGB |
| [Dimension](https://www.designtokens.org/tr/2025.10/format/#dimension) | Number | The token’s unit value must be set to px. Other values are not supported. |
| [Font family](https://www.designtokens.org/tr/2025.10/format/#font-family) | String | The token’s value must be a string containing a single font name. Tokens with an array value are not supported. |
| [Duration](https://www.designtokens.org/tr/2025.10/format/#duration) | Number | The token’s unit value must be set to s. Other values are not supported. |
| [Number](https://www.designtokens.org/tr/2025.10/format/#number) | Number or boolean | If the token contains com.figma.type: “boolean” in its $extensions value, it is treated as a boolean (where 0 is treated as false and any other number is treated as true). Otherwise, it is treated as a number. |
| - | String | String is not an officially defined DTCG token type, but is accepted on import. |

### Cross-collection references

You can reference variables from other collections using the `com.figma.aliasData` extension with the following properties. If Figma is able to locate a variable in another collection you have access to matching the provided data, the value will be set to an alias referencing that variable.

|  |  |  |
| --- | --- | --- |
| **Property** | **Data** | **Notes** |
| targetVariableID | ID of the target variable | On import, we will first try to link a variable alias to a variable with an ID matching variableID. |
| targetVariableSetID | ID of the target variable’s collection | If no variable with variableId exists, we will look for a variable with a name matching variableName within a variable collection with an ID matching variableSetId. |
| targetVariableSetName | Name of the target variable collection | If no variable set with an ID matching variableSetId exists, we will look for a variable with a name matching variableName in a variable set with a name matching variableSetName. |
| targetVariableName | Name of the target variable | Used to find a target variable when there’s no variable with an ID matching variableId. |

### Token naming

When importing tokens, Figma will normalize the names of tokens in nested groups using forward slashes. For example, `color.accent.light` becomes `color/accent/light`. If two tokens end up with the same normalized name, only the first one encountered will be imported. The duplicate will be ignored.

### Import design tokens into a new collection

1. Open the  Variables modal.
2. Create a new collection, then drag-and-drop one or more eligible file types into the Variables modal.

A new mode will be created for each file you import. Variables will only be created for tokens that meet the following criteria:

- Are present in all imported files
- Have a supported `$type` with a supported value
- Have the same `$type` across all imported files

### Import design tokens to update existing modes

1. Open the  Variables modal.
2. Select an existing collection, then right-click on the mode you want to update and choose **Import mode**.
3. Select the file you want to import, and click **Open**.

Any variables that match the token names and types will be updated.

## Export modes

You can export variable modes to a JSON file.

To export a variable mode:

1. Open the  Variables modal.
2. Do one of the following:
   - **To export a single mode:** Open the collection, then right-click on the mode you want to export and choose **Export mode**.
   - **To export all modes in a collection:** Right-click on the collection and choose **Export modes**.

## Switch between modes

Switch the mode on an object or page so the designs use the variable values you want. You can switch modes on:

- Layers
- Frames
- Components and component sets
- Sections
- Groups
- Pages

Tip: Want to change variable modes while prototyping? [Learn how to use the Set variable mode prototyping action](https://help.figma.com/hc/en-us/articles/15253268379799).

### Switch modes on an object

**For layers:** You can switch their modes if there is at least one variable applied and the variable has multiple modes.

**For groups, frames, components, component sets, and sections:** You can switch their modes if *nested layers* have at least one variable applied and the variable has multiple modes.

To switch the mode on an object:

1. Select the layer, group, or container object.
2. From the **Appearance** section of the right sidebar, click  **Apply variable mode**.
3. Hover over a variable collection and choose a mode.

Once you specify a mode on an object, a tag with the mode icon and mode name will appear next to the layer name in the **Layers** panel of the left sidebar. If there are multiple modes, hover over the tag to see a list of modes.

![](https://help.figma.com/hc/article_attachments/26978254521751)

### Switch modes on a page

You can switch modes on pages if any local collection of variables contains multiple modes.

1. Deselect everything on the canvas.
2. From the **Page** section of the right sidebar, click  **Apply variable mode**.
3. Hover over a variable collection and choose a mode.

### Set to auto mode (objects only)

Objects with variables have their modes set to **Auto** by default. This means they take on the mode of their parent container.

- If their parent container is also set to Auto, objects continue up their layer hierarchy until they reach a container with a specified mode.
- If no parent containers have a mode specified, then the objects fallback to the collection’s [default mode](#h_01HMD3VBSV4SD76PH8BVZY8Z13), shown in parentheses.

![From the right sidebar, the mode selector is opened and Auto is highlighted.](https://help.figma.com/hc/article_attachments/26978254525079)

## Use with variant instances

Boolean, number, and string variables can be assigned to component instances with [variant properties](../components/explore-component-properties.md#h_01G2Q5GF4407ZTN7K8FHM2JREZ).

### String and number variables

String and number variables can be mapped to variant instances so it switches to a different variant when its mode changes. To do this, the variable’s value must match the variant property’s values.

1. Create a string or number variable with multiple values (or modes).
2. Set the variable’s values to match the variant property’s values.
3. Grab a component instance of the variant, and hover over the variant property in the right sidebar.
4. Click  **Assign variable** and choose the variable.

Now, the instance will switch to a different variant whenever the mode switches.

### Boolean variables

Boolean variables can be mapped to variant properties with true and false values.

Note: Currently, boolean variables cannot be applied to [boolean properties](../components/explore-component-properties.md#h_01G2Q5GA6DEB604H2E5H5C5TA4). You’ll need to [add a variant property](https://help.figma.com/hc/en-us/articles/8883756012823) to a component with two values: true and false. Then, add apply the boolean variable to the instance’s variant property.

1. Create a boolean variable with multiple values (or modes).
2. Create two variant instances within the same component set.
3. Set one variant’s value to `True` and the other one to `False`.
4. Grab a component instance of one of the variants, and hover over the variant property in the right sidebar.
5. Click  **Assign variable** and choose the boolean variable.

[Learn how to use variants and variables in prototypes](https://help.figma.com/hc/en-us/articles/14506587589399).

### Nested instances

You can also bind variables to variant properties on nested instances.

1. Create a component with a nested instance of another component.
2. Create a string, number, or boolean variable with multiple values (or modes).
3. Set the variable’s values to match the values of the nested instance component properties.
4. Create a instance of the component.
5. Assign the variable to the nested instance’s variant property.

Now, the nested instance will switch to a different variant whenever the mode switches.

## Mode conflicts

Any modes with conflicts will show an  **information icon** next to it in the mode switcher. Conflicts occur when objects in a file use different versions of the same variable.

If you select a mode with a conflict, the mode is only applied to layers that can render it. The layer must be using a version of the variable that contains that mode.

![The mode selector shows the information icon next to several modes.](https://help.figma.com/hc/article_attachments/26978254526999)

To resolve conflicting modes:

1. Open the file where the main variable lives and [publish it to team libraries](../create-and-share-libraries/publish-a-library.md).
2. Review and accept the [updates from the library modal](../use-libraries/review-and-accept-library-updates.md#h_01HGV42MNBJS02JWFFM1M4SMP8) from the file where the conflicts are happening.

Keep in mind that only those with `can edit` access to a file can make edits, publish, and review and accept library updates to the file.

### Prevent mode conflicts

Mode conflicts can happen if a mode is deleted from or added to the variable, and the updates haven’t made their way to a file or object.

Here are a couple of ways these conflicts can happen and what you can do about them.

Scenario 1

Say you publish a variable collection with two modes—Light and Dark. You use them in a design file called Brand.

Later, a third mode is added to the collection—Superdark. In the file where the variable lives, you set a component to Superdark mode and insert it into the Brand file.

This creates a conflict in the Brand file with the Superdark mode. Even though layers in the Brand file use the same variable, layers using the older version don’t have access to Superdark. Even when you try to apply Superdark to them, they will only be able to render Light and Dark.

As a solution, make sure that updates to the variable are published, and accept the updates from the file containing conflicts.

Scenario 2

In some cases, there's a chain of files with connected assets that are experiencing conflicting modes.

For example, let's say you created a variable in File 1 and publish it to team libraries. In File 2, you use the variable on Main Component A. In File 3, an instance of Component A is inserted into Main Component B. Lastly, an instance of Component B is inserted into File 4. This chain looks like this:

> File 1: Variable (version 1)  
> File 2: Main Component A (uses variable version 1)  
> File 3: Main Component B (uses instance of Component A)  
> File 4: Instance of Component B

One day, someone adds a new mode to the variable in File 1. You grab an asset from File 1 and insert it into File 4. You start seeing an  **information icon**next to one of the modes in the mode switcher. So now, the chain looks like this (changes are **bolded**):

> File 1: Variable (**version 2**)  
> File 2: Main Component A (uses variable version 1)  
> File 3: Main Component B (uses instance of Component A)  
> File 4: Instance of component B (**you spot a conflict**)

![Animation illustrating a chain of mode conflicts across four files. A variable's version updates in file one, which impacts a series of components and nested components in files 2 through 4.](https://help.figma.com/hc/article_attachments/20661411678103)

In this case, reviewing and accepting updates in File 4 will not resolve the issue if Files 2 and 3 haven't received and accepted updates yet.

As a solution, you will need to publish and accept updates to all files involved in the order of the chain.

> File 1: Publish variable  
> File 2: Accept variable update; Then publish Main Component A  
> File 3: Accept updates to variable and Component A; Then publish Component B  
> File 4: Accept updates to variable, Component A, and Component B
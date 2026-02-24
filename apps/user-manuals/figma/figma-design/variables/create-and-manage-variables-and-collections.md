# Create and manage variables and collections

Source: https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections

---

**The entry point to the variables modal is moving!** Currently, the variables modal is not discoverable if you have a layer selected. We're slowly rolling out a new left navigation bar to users in Figma Design, which will include the entry point to the variables modal so you can access your variable collections anytime.

![navigation-bar-variables-entry-point.png](https://help.figma.com/hc/article_attachments/37506151444759) 

The variables modal will also be edge-to-edge in your window by default, called **variables view**, so that you can see more of your variables and modes at once. You can still minimize to a modal view like before.

[Learn more about the new navigation bar.](https://help.figma.com/hc/articles/360039831974)

Before you Start

Who can use this feature

Anyone on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with can edit access to a file can create and edit variables

Looking for more resources on variables? [Check out our guide to variables](https://help.figma.com/hc/en-us/articles/15339657135383).

## Access the Variables modal

Use the **Variables** modal to create and manage:

1. [Variable collections](#01H8044A3JH5079S16V2YHA1RV)
2. [Variables](#01H8044A3J5SZNG4MKAW1PQJDS)
3. [Modes for variables](https://help.figma.com/hc/en-us/articles/15343816063383)
4. [Variable groups](#01H8044A3JN28S65BS0G7Q9E19)

![An overview of the variables modal showing a collection of tokens. It includes annotations A, B, and C at the top; D highlights the sidebar with variable groups like surface and text.](https://help.figma.com/hc/article_attachments/26964398862615)

To access the **Variables** modal:

1. Deselect everything on the canvas by pressing `esc` or clicking the canvas.
2. From the right sidebar, find the **Local variables** section.
3. Click **Open variables.**

You can click **Toggle sidebar** to see additional options in the variables modal.

**Tip**: Expand the size of the variable modal to see more variables and modes at once. You can do this in one of two ways:

- Click and drag the corner or sides of the modal
- Click **Expand** to resize the modal to expand to the full size of your window

## Create a variable

1. From any collection, click **+ Create variable**.
2. Select a [variable type](https://help.figma.com/hc/en-us/articles/14506821864087/) from the dropdown.
3. Give the variable a name in the first column, and a value in the second column.

**Tip**: You can also create a variable using the [eyedropper tool](https://help.figma.com/hc/articles/27643269375767/).

Each collection can have up to 5,000 variables.

To duplicate a variable, select one or more variables and press `⇧ Shift` `Enter`.

To delete a variable, right click the variable and select **Delete variable**.

**Tip**: Those on Education or paid plans can add additional columns to store multiple values in a variable, allowing you to quickly switch between different contexts in designs. Learn how to [create multiple modes for variables](https://help.figma.com/hc/en-us/articles/15343816063383).

## Create an alias

Create an alias for a variable to link its value to an existing variable. This allows you to implement design tokens and makes managing updates to your designs more efficient.

For example, say you have multiple color variables that reference the same color variable. If that color needs updating, you would only need to update the source instead of manually updating every instance of the color.

A variable can reference other variables of the same type.

![An animation of the user clicking a variable in the variable modal and binding it to another variable in the library ](https://help.figma.com/hc/article_attachments/26964398864151)

To create an alias for a variable:

1. Open the **Variables** modal.
2. Right-click a variable’s value and select **Create alias**.
3. From the **Libraries** tab, choose a variable to set an alias. You can use the search bar to find a variable by name or browse through available libraries.

To detach an alias, hover over the value field and click **Detach alias.**

**Want to learn more about how aliasing works?** Check out the [Tokens, variables, and styles](https://help.figma.com/hc/en-us/articles/18490793776023) lesson of Figma's Intro to Design Systems course.

## Copy and paste variables

You can copy and paste variables to any collection, including collections in a different file.

1. Open the desired collection from the variables modal.
2. Select one or more variables.
   - Hold `⌘ Command` for Mac or `⌃ Control` for Windows to select multiple variables.
   - Hold `⇧ Shift` to select a range of variables.
3. Right-click the selection and select **Copy**.
4. From any collection, right-click and select **Paste**.

## Edit a variable

Hover over a variable’s row and click the **Edit variable** icon to open its editing modal.

![Edit variable modal showing fields for name, description, mobile and desktop values, code syntax, and publishing options. Annotations A to F on the side.](https://help.figma.com/hc/article_attachments/26964398869143)

From there, you can:

1. Change the name of the variable.
2. Add a description to explain how the variable should be used.
3. Modify the values of the variable.
4. Add [code syntax](#code_syntax).
5. [Hide the variable from publishing](https://help.figma.com/hc/en-us/articles/360039238193).
6. [Scope a variable](#h_01H32HZB74TE7MJXYBWEBBQWJV) to limit which properties the variable can be applied to.

### Scope a variable

Scope a variable to limit which properties the variable can be applied to. This reduces the guesswork when deciding which variables to use for your designs.

For example, if you scope a number variable to corner radius, the variable can only be applied to corner radius and won't appear as an option for any other supported properties.

Scoping is available for number, color, and string variables.

For number variables, you can scope:

- Auto layout
 - Gap between
 - Padding
- Corner radius
- Font properties
 - Font weight
 - Font size
 - Line height
 - Letter spacing
 - Paragraph spacing
 - Paragraph indent
- Layer opacity
- Effects
- Stroke
- Text content
- Width and height

For color variables, you can scope:

- Effects
- Frame fill
- Shape fill
- Stroke
- Text fill

For string variables, you can scope:

- Font family
- Font weight or style
- Text string

To scope a variable:

1. Right-click on a variable, or multiple variables, and select **Edit variable**. You can also click **Edit variable**, located to the right of any single variable.
2. Open the **Scope** tab.
3. Use the checkboxes to toggle the variable’s availability in that property. Check **Show in all** to make the variable available for all [supported properties](https://help.figma.com/hc/en-us/articles/14506821864087#Types_of_variables).

![The Edit variables menu is open on the Scope tab. The label at the top of this view says Number scope, with over a dozen check boxes and property types. A handful of boxes are checked.](https://help.figma.com/hc/article_attachments/26964398870679)

### Add code syntax

Code syntax allows you to represent variables in code using valid variable names to support a seamless handoff experience. A variable’s code syntax will appear in code snippets in [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247) when inspecting elements using the variable. Currently, code snippets for variables are supported in CSS, SwiftUI, and Compose.

![Two images side by side. On the left is a view of the Edit variable menu. In the code syntax section, there is one code syntax setting for Web, and next to it is an input field with the string var(--extra-small). On the right is a view the right sidebar in Dev Mode. We can see the code syntax for a border-radius of an object.](https://help.figma.com/hc/article_attachments/26964398871319)

You can create one name per platform, including Web, Android, and iOS. This allows for up to three code syntaxes per variable.

To add code syntax to a variable:

1. From the **Code syntax** section of the the **Edit variable** modal, click **Add code syntax**.
2. From the dropdown, choose Web, Android, or iOS.
3. Use the input box to enter a variable name. A preview shows how the variable name appears in code snippets.

Tip: In addition to viewing the code syntax, there are more ways to work with [variables in Dev Mode](https://help.figma.com/hc/en-us/articles/27882809912471). You can see variable details and suggested variables, and view local collections on the variables table.

### Edit variables in bulk

To edit multiple variables at once:

1. Open any collection from the **Variables** modal.
2. Select multiple variables by using keyboard shortcuts:
   - Hold `⌘ Command` / `Control` and click to select individual variables
   - Hold `Shift` and click to select a range of variables
3. Right-click a selected variable and click **Edit variables**.
4. From the **Edit variables** modal, you can:
   - Scope variables, if supported by the variable type
   - Hide variables from publishing

## Search your collections for variables and groups

Use the search bar in the variable modal to search for a specific variable or group in the collection you’re viewing. You can search by variable name, variable value, or group name.

You can also click to filter the list of variables by variable type.

![](https://help.figma.com/hc/article_attachments/33638145403159)

## Create and manage variable collections

A collection is a set of variables and modes. Collections can be used to organize related variables together. For example, use one collection to localize text in different languages, and another collection for spatial values.

### Create a variable collection

To create a variable collection, go to the sidebar of the variables modal and click **More options** > **Create collection.**

![](https://help.figma.com/hc/article_attachments/31448329844887)

If a variable has not been created in a file, you will need to create a variable first in order to create new variable collections. ![](https://help.figma.com/hc/article_attachments/31448329845271)

**Tip**: If your variable collection contains multiple variable modes, you can edit, reorder, and change the default mode my dragging the columns. Learn more about [variable modes](https://help.figma.com/hc/en-us/articles/15343816063383).

### Rename a variable collection

To rename a variable collection:

1. In the sidebar of the variables modal, open the collections dropdown and choose the collection you want to manage.
2. Click **More options** and select **Rename collection**.

### Delete a variable collection

Deleting a variable collection also deletes all of its containing variables. Any properties that were using the variables will no longer be connected to the variable and any existing modes. The variables and collection can only be restored by immediately undo-ing the action or by restoring an earlier version of the file.

To delete a variable collection:

1. In the sidebar of the variables modal, open the collections dropdown and choose the collection you want to manage.
2. Click **More options** and select **Delete collection.**

### Reorder variable collections in a file

Reorder your variable collections to organize and find variables faster when applying them to designs. Changing the order of variable collections will affect the order in which they appear from the variable mode selector and variable selectors.

To reorder variable collections in a file:

1. In the sidebar of the variables modal, click **More options** and select **Reorder collections**.
2. From the **Collections** popup, you can:
   - Click and drag to reorder the collections
   - Or click **Sort A to Z** to order collections in alphanumerical order

## Group a selection of variables

You can further organize variables by adding them to groups within a collection. For example, use one group for colors used for text, and another for colors used on strokes.

To organize variables into a group:

1. From the **Variables** modal, select multiple variables:
   - Hold `⌘ Command` / `Control` to select multiple variables
   - Hold `⇧ Shift` to select a range of variables
2. Right-click the selection and select **New group with selection**.

Click and drag groups in the sidebar of the Variables modal to reorder groups. You can also click and drag groups into other groups to nest them.

### Rename a group

1. In the sidebar of the variables modal, double click the group name.
2. Type a new name for the variable group.

### Manage a group

1. In the sidebar of the variables modal, right-click the group name in the sidebar.
2. From the menu, choose from the following:
   - **Ungroup**
   - **Duplicate group**
   - **Delete group**

Ready to continue your variables journey? Check out the following topics:

- [Publish variables to team libraries](https://help.figma.com/hc/en-us/articles/360025508373-Publish-styles-and-components)
- [Apply variables to designs](https://help.figma.com/hc/en-us/articles/15343107263511)
- [Create modes for variables](https://help.figma.com/hc/en-us/articles/15343816063383)
- [Use variables for advanced prototypes](https://help.figma.com/hc/en-us/articles/14506587589399)
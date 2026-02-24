# Create and use variants

Source: https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants

---

Before you start

Who can use this feature

Supported on all plans. Publishing variants to a library is supported [paid plans](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can create variants and component sets in that file.

Anyone with `can view` access to a file can use components or components sets from that [library](https://help.figma.com/hc/en-us/articles/360025508373).

As you create components and build out your design system, you'll find the need for components that are similar to each other, with only slight differences.

For example: you might have multiple components for buttons, with separate components for various states and sizes, as well as light and dark modes.

Variants allow you to group and organize similar components into a single container. This simplifies your component library and makes it easier for everyone to find what they need.

Customize the properties and values of your variants, to take the guesswork out of your design system and bring your components closer to front-end code.

Note: We don't recommend using variants to group different icons. If you have different sizes of the same icon, then you could combine these as variants instead.

## Variant properties and values

Variant properties and their values allow you to define the attributes of your variants. Variant properties are a type of [component property](https://help.figma.com/hc/en-us/articles/5579474826519/) specific to variants and component sets.

You can add as many properties and values as you need, and customize them to suit your design system. You can even map your properties and values to code components in your design system.

- **Variant properties** are the variable aspects of our component. For example: the properties of a button component could be the `size`, `state`, or `color`.
- **Values** are the different options available for each property. For example: the state property could have `default`, `hover`, `pressed`, and `disabled` values.

All variants within the component set should use the same properties and values, but each variant needs to be a unique combination of them. You don’t need to have a component for every possible combination of properties and values.

## Rename your components

Figma uses the slash naming system to organize components in the assets tab and instance menu. Each `/` in a component's name will create another level of hierarchy.

This makes it easier to navigate your library, or find and swap related components. Learn how to [name and organize components](name-and-organize-components.md).

**Tip:** You can rename layers in bulk using the rename layers modal. Learn more about [renaming layers in bulk](https://help.figma.com/hc/en-us/articles/360039958934).

You can also use this naming system to convert your existing components to variants. To be accurately converted, component names need to follow this structure:

`componentName/property1value/property2value/property3value`

- The text before the first `/` will become the name of the component set.
- Figma will create a new property for every other `/` in the component's name, then add the attribute as a value.
- If you have used suffixes in your naming system, you will need to add these to the component's name, separated by a `/`.

**Caution**: To make sure your values match up with the same property, every component you are combining needs to have the same number of slashes.

A button component with the name `Button/Primary/Large/Default/False` will have the following properties and values:

Component set name: **Button**  
Variant: **Primary**  
Property 2: **Large**  
Property 3: **Default**  
Property 4: **False**

In the image below, we can see how the rest of our component names (on the left) are converted to variant values (on the right). ![An example showing a button component variants organized by properties: type, size, state, and icon, with corresponding values displayed.](https://help.figma.com/hc/article_attachments/360098128293)

## Organize components on the canvas

**Note:** Component sets can only contain components, so it's not possible to add text or annotations, nest frames, or group a subset of variants inside a component set.

When combining components as variants, Figma will apply your existing layout and spacing to variants inside the component set. We recommend organizing your components before converting them, to save you from having to rearrange them after.

If you have a lot of variants for a particular component, you may want to organize your components in rows, columns, or grids. This will help to communicate their multi-dimensional nature to anyone who's using your design system. You can also add text layers beside your component set to annotate the relevant properties and values.

In our example below, we've arranged our button variants in a grid. We've also added text layers to the canvas that correspond to a property's values.![An example showing button a component set organized by type, size, state, and icon presence with property values displayed.](https://help.figma.com/hc/article_attachments/360095834494)

**Tip:** By default, component sets have a dashed-purple stroke and no fill. You can adjust the fill and stroke properties of the component set to better suit your brand or design system.

## Combine as variants

1. Select the components you want to combine. Learn how to [select layers and objects](../work-with-layers/select-layers-and-objects.md).
2. In the right sidebar, click **Combine as variants**.
3. Figma will add all components to a single component set.

![](https://help.figma.com/hc/article_attachments/26976307160215)

## Give properties descriptive names

As part of the conversion process, Figma will create generic properties and add any attributes you added to the component's name as values.

As Figma doesn't know the names of the properties, it will name the first property `Variant`, then number them sequentially: `Property 2`, then `Property 3`, and so on.

You'll need to rename those properties to something more descriptive.

1. Select the component set.
2. Find the **Properties** section in the right sidebar.
3. Hover over a component property name and double-click it.
4. Edit the name and press `Enter` / `Return` to apply the edit.
5. Repeat for the remaining properties.

![](https://help.figma.com/hc/article_attachments/26976307161879)

**Note:** Figma handles component sets the same way as regular components. You can add descriptions and links to documentation to them. You can also drag them into the canvas from the assets tab, and swap between instances of them.

## Create new variants

Note: Figma places variants in a single container called a [component set](https://help.figma.com/hc/en-us/articles/360038663154). Component sets can only contain components. Click **Create component** in the right sidebar, or use the keyboard shortcut to turn your selection into a component:

- Mac: `⌥ Option` `⌘ Command` `K`
- Windows: `Ctrl`  `Alt`  `K`

There are a few ways to create a new variant. Select a main component and:

- Click  from the right sidebar, or
- Right-click the main component > **Main component** > **Add variant**, or
- Click  next to **Add property** from the right sidebar, then select **Variant** from the dropdown. This [creates a new variant property](https://help.figma.com/hc/en-us/articles/5579474826519) and turns the main component into a component set.  
  From there, click  below the component set to add a variant.

![](https://help.figma.com/hc/article_attachments/26976307163415)

Figma will do a few things:

- Make an identical component with the same properties
- Add both components as variants to a component set
- If you used the slash naming convention, the text before the / will become the name of the component set, and the attributes after will be used as values.

You can also create new variants by [combining multiple components](#h_01G2SX8RVSXK0JCQBF8RDWT1MM).

If you have an existing component set, [add more variants](#h_01G2SXVWV94RP15D9QBP1P4PMY) to it at any time.

**Tip:** By default, component sets have a dashed-purple stroke and no fill. You can adjust the fill and stroke properties of the component set to better suit your brand or style guide.

## Add properties and values

Create and apply properties and values to your variants when you first create them, or as your design system evolves. [Learn how to create and apply properties and values](https://help.figma.com/hc/en-us/articles/5579474826519).

Fix conflicted value errors All variants within the component set will use the same properties and values, but each variant needs to be a unique combination of them.

If any variants have the exact same combination of values, Figma will let you know that there is a conflict. You'll see this error even if the variants themselves are visually different.

To resolve this issue, you'll need to add or update the values of the affected variants, so they have a unique combination of values.

## Add more variants to a component set

Continue to add variants to your component set using any of the following methods:

- Select a component set and click  in the right sidebar.
- Select a component set and click  just below the component set.
- Duplicate existing variant using the keyboard shortcut:
  - **Mac**: `⌘ Command``D`
  - **Windows**: `Ctrl``D`
- Drag other components into the component set to add them as variants.

**Tip**: Dragging in other components won't reflow existing variants. You can use smart selection to adjust the layout of your variants. [Learn more about smart selection](https://help.figma.com/hc/en-us/articles/360040450233-Arrange-objects-with-Smart-Selection).

**Caution:** When you add an instance with variants to a file, Figma will import every variant in that component set. Importing large component sets will impact Figma's speed and performance.

## Manage variants

### Organize variants

When you add new variants to a component, Figma's default behavior is to add variants in a single column, with equal spacing between them.

If you have your components in another layout before converting them, Figma will keep the same layout for the component set.

You can override Figma's default behavior and arrange variants in any way you choose.

- Select a variant and move it to new co-ordinates within the component set. Figma will allow you to place variants anywhere within the component set, including over the top of other variants.
- Adjust the dimensions of the component set in the right sidebar, or resize it in the canvas like you would a regular frame.
- With all variants selected: Use the fields in the right sidebar to adjust the  horizontal and  vertical space between variants.

**Note**: Figma will use the variant in the top-left corner as the default variant. This variant will represent the entire component set in the **Assets** tab of the left sidebar.

### Manage properties and values

You can [rename and reorder](https://help.figma.com/hc/en-us/articles/5579474826519/#Manage) properties and values anytime after creation. Remove properties you no longer need.

- If you reorder properties, Figma will adjust the name and syntax of your variants to match.
- If you've converted your existing components to variants, you'll need to rename your properties to make them more descriptive.

Fix corrupted variant errors You will get a corrupted variant error if any of your variants do not follow this syntax. This can happen if you mistype a property or value, or use an invalid naming structure when converting existing components.

To fix this issue, you'll need to rename the properties and values of the variant. While it's possible to rename them using this syntax in the layer name, we recommend renaming properties and values in the right sidebar instead.

**Tip**: Use [multi-edit](https://help.figma.com/hc/en-us/articles/21635177948567) to speed up your workflow when editing component sets. While editing variants in with multi-edit enabled, matching objects also get the same edits without needing you to take extra steps to select them.

## Publish component sets to a library

Users on paid plans can publish component sets to a [library](https://help.figma.com/hc/en-us/articles/360039162653-Publish-a-file-to-a-Team-Library) to share them with collaborators.

Publish component sets alongside your styles and regular components to allow members of your team or organization to use them.

Component sets appear in the assets tab alongside your other components. Figma will use the variant in the top-left corner of the component set as the default variant.

Collaborators can then drag the component set into their files to create an instance. They can then access all the other variants in the component set by configuring the property values in the right sidebar.

Are you a member of a Figma Organization? [Design system analytics](https://help.figma.com/hc/en-us/articles/360039238353-Track-library-and-component-usage) allow you to see how members of your organization are using components and variants.

## Use variants

Component sets appear in the assets tab alongside any regular components. So instead of looking for a specific variant in the assets tab, you only need to select the component set.

Once you have an instance of that component set on the canvas, you can configure the instance's property values to select a variant.

### Select component sets

1. Click on the **Assets** tab in the left sidebar, or use the keyboard shortcut:
   - **Mac**: `⌥ Option` `2`
   - **Windows**: `Alt` `2`
2. Click on a component set and drag it on to the canvas. Figma will create an instance of the default variant of that component set.
3. View the component set's name and properties in the right sidebar.
   - Use the dropdowns next to the property to select your preferred combination of values.
   - Turn specific properties off and on using the toggles.

### Configure variants

Select other variants in a component set by configuring the properties and values in the right sidebar.

1. Select the instance.
2. View the name of the component in the right sidebar. If the component has variants, you'll see fields underneath the component name to configure the properties and values of that component set.
   - Use the dropdowns next to the property to select your preferred combination of values.
   - Turn specific properties off and on using the toggles.
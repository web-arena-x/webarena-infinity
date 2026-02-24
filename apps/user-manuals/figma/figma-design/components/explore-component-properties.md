# Explore component properties

Source: https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties

---

Before you Start

Who can use this feature

 

Users on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with edit access to the Figma Design file can create, manage, and use component props

This article covers how to create and configure component properties. Learn how to [edit instances with component properties](https://help.figma.com/hc/en-us/articles/8883757553943).

Component properties are the changeable aspects of a component. They allow you to communicate which parts of a component can be changed, such as:

- Which layers in a component have the option to be hidden or shown
- Whether an instance can be swapped and set preferred instances to swap to
- Which text strings can be changed

Component properties are created and applied to main components and component sets to define parts of a design system and to make design systems easier to use.

Anyone using a component with component properties can view a single set of consolidated controls in the right panel, so they can understand at a glance what is changeable and make edits in one place.

This reduces time needed to refer to documentation, improves accurate usage of components and design systems, and decreases the need to select and override individual layers.

[Explore the component properties playground file in the Figma Community](https://www.figma.com/community/file/1100581138025393004).

# Types of component properties

Component properties are tied to different design properties. You can create component properties for any [main component](https://help.figma.com/hc/en-us/articles/360038663154) or [variants of a component set](https://help.figma.com/hc/en-us/articles/360056440594), and apply them to nested layers of the component or variant.

Component properties come in different types:

|  |  |
| --- | --- |
| **Component property type** | **Use this to...** |
| [Boolean property](#h_01G2Q5GA6DEB604H2E5H5C5TA4) | Indicate which layers can have their layer visibility turned on/off, such as an icon on a button. |
| [Instance swap property](#h_01G2Q5FYN2ADEDQ3ZSB1KKY8Z0) | Indicate which instances can be swapped; Set preferred instances to swap to. |
| [Text property](#h_01G2Q5G3FV0EQP9RZFZG7GVWEG) | Indicate which text content can be changed. |
| [Variant property](#h_01G2Q5GF4407ZTN7K8FHM2JREZ) | Define the different variations of a component, such as its different states, sizes, or colors. |

Tip: Communicate a component's intended usage by adding descriptions and links to documentation. Documentation helps to guide proper application, variant and state usage, and accessibility and contrast requirements to those who are using your design system. Learn how to [add documentation to design assets](https://help.figma.com/hc/en-us/articles/7938814091287).

# Create and apply component properties

## Boolean property

Use boolean properties to set true/false values, which allow you to toggle an attribute on or off. For example, if a design system contains buttons with and without an icon, instead of creating variants for each state, apply a boolean property to the icon’s layer visibility.

Currently, boolean properties only support layer visibility.

### Create a boolean property

When a boolean property is created for layer visibility, a value set to false means the layer will be hidden. If toggle to true, the layer will be visible.

1. Select a main component or component set.
2. In the right sidebar, click  in the **Properties** section and select **Boolean** from the dropdown.
3. From the **Create component property** modal, use the fields and dropdown menus to configure the property.
   - Give your property a **name** in the text field.
   - Set the default **value** to true or false. You can also click  **Apply variable** to apply an existing boolean variable, if available.
4. Click **Create property**.

![](https://help.figma.com/hc/article_attachments/27771812397079)

### Apply a boolean property to a component

Warning: Before applying boolean properties to components, it’s important to consider any need for [interactive components](https://help.figma.com/hc/en-us/articles/360061175334) or [prototyping connections](https://help.figma.com/hc/en-us/articles/360040315773). Prototyping noodles must connect between two objects. If you connect two components and consolidate them using boolean properties, the prototyping connections will be lost.

For example, you have a boolean property applied to an icon in a button component to represent two states: a button with an icon and one without. It’s not possible to set up an interaction between the two because you’re using a single component. Prototype interactions must be between two individual objects.

1. Select a layer nested within a main component or variant.
2. If you’re working with variants, you can click  to enable multi-edit to edit matching objects and speed up your workflow. Learn how to [multi-edit variants](https://help.figma.com/hc/en-us/articles/21635177948567).
3. In the right sidebar, find the **Appearance** section and click the  **Apply variable/property** icon.
4. Choose a boolean property from the list. When applied, you’ll see a purple pill with the `property name` in the right sidebar.

![](https://help.figma.com/hc/article_attachments/27771782233751)

Tip: You can create and apply a boolean property from any nested layer in a main component or main variant. Select the nested layer and find the **Appearance** section, then click the  **Apply property** icon. Once you create the property, it’ll be applied to the selected layer.

## Instance swap property

The instance swap property allows you to indicate which instances nested in a main component or variant can be swapped.

When creating an instance swap property, you can set a default instance using any component created in the file, or from [libraries added to the file](https://help.figma.com/hc/en-us/articles/1500008731201). You can also set [preferred instances](#preferred) so others know which instances they can swap to. Learn how to [swap components using the instance swap property](https://help.figma.com/hc/en-us/articles/360039150413).

### Create an instance swap property

1. Select a main component or component set.
2. In the right sidebar, click  **Properties** section and select **Instance swap** from the dropdown.
3. From the **Create component property** modal, use the fields and dropdown menus to configure the property.
   - Give your property a **name** using the text field.
   - Set the default **value** by using dropdown to select an instance from any components created in the file, or from any libraries added to the file.
   - If desired, set up any [preferred instances](explore-component-properties.md#preferred) so others know which components they should choose from when swapping the instance.
4. Click **Create property.**

![](https://help.figma.com/hc/article_attachments/27771812403095)

### Apply an instance swap property to a component

1. Select a instance nested within a main component or variant.
2. If you’re working with variants, you can click  to enable multi-edit to edit matching objects and speed up your workflow. Learn how to [multi-edit variants](https://help.figma.com/hc/en-us/articles/21635177948567).
3. At the top of right sidebar, click  **Apply instance swap property**.
4. Choose an instance property from the list. When applied, you’ll see a purple pill with the `property name` in the right sidebar.

![](https://help.figma.com/hc/article_attachments/27771782243735)

Tip: You can create and apply a instance swap property from any instance nested within a main component or main variant. Selected the nested instance and click  **Apply/create instance swap property** at the top of the right sidebar. Once you create the property, it’ll be applied to the selected layer.

### Choose preferred values

Preferred values allow you to create a curated set of components to choose from when swapping instances (via the instance swap property). They reduce guesswork by communicating which specific components can replace an existing one.

> For example, you create an icon button with an instance swap property to indicate that the icon can be swapped. However, your icon library contains over 100 icons, but only 8 of them should be used for this button.  
>   
> To make it easy find these 8 icons and to know which one can be used, you add them as preferred values. Now, whenever designers go to swap the icon, they have a curated list of assets they know they can use.

![](https://help.figma.com/hc/article_attachments/24377633468439)

When using a component with a preferred value, a list of preferred values appear by default when opening the instance swap property menu.

Note: If you don’t want to use a preferred value, click the dropdown or use the search bar above the list to find other components from available.

To add preferred values for an instance:

1. Start by editing its existing instance swap property or creating a new one.
2. From the respective modals, click  in the **Preferred values** section and check the checkboxes next to the instances you want to include as a preferred values.

To remove a preferred value, click  next to the value in the **Preferred** values section of the modal.

## Text property

Use text properties to indicate which text content in a component can be edited. Text content can be edited either from the right panel or on the canvas.

Note: Text component properties currently don't support rich text — such as lists styles, superscript, and other [type settings](https://help.figma.com/hc/en-us/articles/360039956634). You can still apply these settings to the text layer, but their formats won't be reflected in the component properties panel of the right panel.

If the text layer contains a [bulleted or numbered list style](https://help.figma.com/hc/en-us/articles/360040449773), changing the text string from the right panel will remove the list style. To preserve it, update the string from the canvas instead.

### Create a text property

1. Select a main component or component set.
2. Click  **Properties** section of the right sidebar and select **Text** from the dropdown.
3. From the **Create component property** modal, use the fields to configure the property.
   - Give your property a **name** using the text field.
   - Set the default string of text by using the **value** text field. You can also click  **Apply variable** to apply an existing string variable, if available.
4. Click **Create property.**

![](https://help.figma.com/hc/article_attachments/27771782246423)

### Apply a text property to a component

1. Select a text layer nested in a main component or variant.
2. In the **Text** section at the top of the right sidebar, hover over the text field and click  **Apply variable/property**.
3. Choose a text property from the list.

![](https://help.figma.com/hc/article_attachments/27771812416663)

Tip: You can create and apply a text property from any text layer nested within a main component or main variant.

1. With the nested text layer selected, find the text field in the **Text** section of the right sidebar.
2. Hover over the text field and click  **Apply variable/property**.
3. From the menu, click  **Create variable/property**.
4. From the **Create** dropdown, select **Property**. Then give the property a name and a default value.
5. Click **Create property**. Once you create the property, it’ll be applied to the selected layer.

## Variant property

A **variant** is an individual component within a component set.

A **variant property** allows you to define attributes of your variants, such as state, color, or size.

A component set contains multiple variants, and the variants carry attributes that can be defined by variant properties. Variant properties are specific to variants and component sets, and can’t be created or applied to main components.

[Learn how to create variants and component sets](https://help.figma.com/hc/en-us/articles/360056440594).

In the example below, we have a button component set with four variants. It has two variant properties, size and color. The size values include small and large, while color values include green and red.

![](https://help.figma.com/hc/article_attachments/5990492021911)

Note: We recommend reviewing your existing design system before you adopt component properties. That way, you can decide which aspects you can reflect as component properties and which need to be variants.

# Switch to a different component property

If a layer has a component property applied to it, you can switch it to a different one at any time.

1. In the right sidebar, find the corresponding section for the component property you’d like to change.
   - **Instance swap property**: Top of the right sidebar.
   - **Text property**: Top of the right sidebar in the **Text** section.
   - **Boolean property**: The **Appearance** section.
2. Click on the purple pill.
3. Select an existing property of the same type.

# Customize a component property

## Change the default value

Change the default value of a text, boolean, or instance swap property.

1. Select component set or main component.
2. Click  next to the variant property to open the edit property modal.
3. Use the text field or dropdown in the **Value** section to update the default value.

Updating the default value will reflect on canvas if the associated instance layer has no property overrides applied.

Note: The default value of a variant property is determined by the variant in the top left corner of a component set. Learn how to [change the default variant of a component set](https://help.figma.com/hc/en-us/articles/360056440594).

## Expose nested instances

Expose specific nested instances to reveal their component properties alongside those of the top-level instance. This helps design system users discover nested instances and their component properties without deep-selecting layers to find them.

> For example, you create a social media card component with multiple components nested inside — an avatar, name, buttons, and so on. You want to change the icon of the *default button* to a “send” icon, and change its text. You also want to change the *cancel button* state to a *disabled* state.  
>   
> Instead of deep-selecting into each layer to find their component property controls, exposing nested instances allows you to click just the top-level component — in this case, the social media card — and edit your instance from a single place.
>
> ![](https://help.figma.com/hc/article_attachments/24377583365271)

When you select a top-level instance with exposed nested instances, a list of component properties for the top-level and nested instances will appear in the right panel.

When hovering over a property row, a light purple highlight appears around the corresponding object on canvas so you know what you’re editing.

Note: If you have an exposed nested instance with visibility set to hidden on a boolean property, any component properties attached to the instance will be hidden as well.

#### Choose nested instances to expose

With a main component or component set selected, click  in the **Properties** section of right panel and choose **Nested instances** under **Expose properties from**.

![](https://help.figma.com/hc/article_attachments/24377633446807)

Note: The option to expose nested instances is available only if a main component:

- already has an exposed nested instance, or
- contains nested instances with component properties applied to it

If you don’t see the **Nested instances** option, try applying a component property to a nested component first.

From the **Expose nested instances** modal, check the boxes for instances you want to reveal at the top-level.

![](https://help.figma.com/hc/article_attachments/24377583374743)

A list of chosen nested instances will appear in the right panel.

To remove nested instances from being exposed, hover over the instance name on this list and click .

## Simplify instances

Simplifying an instance helps reduce clutter in the layers and properties panel by hiding layers without component properties applied. Figma assumes that a layer with no component property is a layer that should not be edited, and therefore can be hidden.

Note: Simplified instances will hide certain layer names, but anyone with **can edit** permissions to the file can still edit the layers.

To simplify an instance, select a main component or component set, and click  **Component configuration** in the right panel From the pop-up, check the **simplify all instances** checkbox.

When using an instance of a simplified component, excess layers will be collapsed under **See all layers**. Click **See all layers** to expand and see the layers. You can collapse it again by clicking outside the layers panel or selecting a different layer.

# Manage a component property

After creating component properties and their values, you can manage them at any time. Rename, reorder, delete, change default values, and more.

Note: To use new or updated components across different files, be sure to publish them to the team library. This allows you to share them with others or to use them in other files or projects. Learn how to [publish to team library](https://help.figma.com/hc/en-us/articles/360025508373).

## Detach a property

Detach text, instance swap, or boolean properties from a layer.

1. Select a nested layer with a component property applied.
2. Click  in right sidebar panel next to the property you wish to unlink.

This removes the component property from the layer, but the component property won’t be deleted.

Note: It’s not possible to detach a variant property from a nested layer.

## Rename, reorder, or delete

### Properties

To rename, reorder, or delete an existing component property:

1. Select the main component or component set.
2. From the **Properties** section in the right sidebar:
   - **Rename**: Double-click a property name. Type in a new name, then press `return` / `enter` or click outside the field to apply.
   - **Reorder:** Hover over a property to reveal handles. Click and drag to reorder, then release to apply.

     Variant properties always sit above other property types in the right sidebar. They can be reordered with other variant properties, but not with other property types.
   - **Delete**: Right-click a property and click **Delete property**. Or, select a property and press `delete`.

     If your component set or main component only contains one variant property, deleting the property will delete the entire component set or main component.

### Values

To change or reorder values of a variant property:

1. Select component set or main component.
2. Click  next to the variant property to open the edit property modal.
   - **Change:** In the **Values** section, use the text fields to change or update the values.
   - **Reorder:** Hover over a value to reveal handles. Click and drag to reorder.

# Component playground in Dev Mode

When selecting a component or instance in [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247), you’ll see a component preview, a link to the main component, as well as any links to relevant documentation and dev resources.

The component playground appears in the inspect panel when a component instance is selected. Use the playground to experiment with the component’s different properties without changing the actual design. To open the component playground in Dev Mode:

1. Select a component instance on the canvas.
2. Click **Open in playground** in the Inspect panel.

[Learn more about using Dev Mode to inspect designs](https://help.figma.com/hc/en-us/articles/15023124644247).
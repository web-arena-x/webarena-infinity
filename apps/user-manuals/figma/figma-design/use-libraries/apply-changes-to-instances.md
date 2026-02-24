# Apply changes to instances

Source: https://help.figma.com/hc/en-us/articles/360039150733-Apply-changes-to-instances

---

Before you start

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan). Publishing components to a library is supported on paid plans.

Anyone with `can edit` access to a file can create and use variants and component sets in that file.

Component libraries define and outline the ideal implementation of a design system.

These components often contain generic information designers need to change, like the text on a button or the contents of a menu.

- The **main component** defines the properties of the element
- The **instance** is a copy of the component you can reuse in your designs

You can make changes to any instance of a component you add to your file. These changes allow you to customize an instance to suit its new context, or explore iterations of a design.

![Three instances of a button component. Each instance has it's own unique text and icon.](https://help.figma.com/hc/article_attachments/26978261690135)

## Apply changes

To make a change to an instance:

1. Select the instance.
2. Edit or adjust the property you’d like to change. For example, to [change the fill of a layer](%E2%80%9Chttps://help.figma.com/hc/en-us/articles/360040623954-Add-fills-to-text-and-shape-layers%E2%80%9D), edit the **Fill** section of the right sidebar.

### Supported properties

Figma lets you change text, fill, stroke, and effect properties.

You can apply the following changes:

- Change text properties, including font, weight, size, line height, letter spacing, and resizing
- Change the fill or stroke of any layers, including the fill type, value, and opacity
- Add, edit, or remove any shadow or blur effects
- Add, edit, or remove layout guides
- Swap nested instances of other components, like icons
- Add, edit, or remove export settings
- Change the layer name

It’s not possible to make changes to the underlying structure of an instance. You can’t override:

- The order, or z-index, of any layers within the instance
- Position of any layers within the component, including items in an auto layout frame
- Any constraints applied to the layers
- The bounds of any text layers

For changes like reordering layers, you must [detach the instance](%E2%80%9Chttps://help.figma.com/hc/en-us/articles/360038665754-Detach-an-instance-from-the-component%E2%80%9D), or make the changes directly to the main component

### Change preservation

Figma attempts to preserve your changes when you select a different variant or swap between instances.

Figma uses the following criteria to determine whether to preserve a change on an instance:

- The layer names of the current instance and the variant or instance you’re selecting must match. This applies both when swapping instances and selecting variants.
- When selecting variants, Figma also checks if the layer properties you’ve changed originally matched between variants. If so, Figma will preserve your changes.

In our example below, Figma preserves the fill change on Step 3, but not on Step 4. This is because the `default primary` button and `hover primary` button both started with the same fill of `#1BC47D`. Our change was to change the hex code from `#1BC47D` to `#F531B3`.

Figma doesn’t preserve our change in Step 4 as the `hover secondary` variant has a fill of `#FFFFFF`, which is different to the fill we applied our original change to (`#1BC47D`).

![A diagram showing the steps to change the fill of an instance.](https://help.figma.com/hc/article_attachments/26978254394007)

The criteria is less strict for preserving text changes. Figma keeps any changes you’ve made to text layers if the name of the text layer is the same between components. Figma will also check if the text layer’s hierarchy is similar.

## Reset changes

Reset the instance to restore the properties of the main component. You can choose to reset the entire instance, or just a specific property.

![A button instance is selected, and the More Actions menu is open.](https://help.figma.com/hc/article_attachments/26978261704599)

1. Select the instance to view changes for the entire instance, or a specific layer to view changes for that layer only.
2. Click **More actions** next to the component name in the right panel.
3. Figma opens a menu that lets you view any changes for your selection. Figma only lists properties that have changes applied. 
   - Select  **Reset > Reset [property]** to reset a specific property.
   - Select  **Reset > Reset all changes** to reset all properties for that layer.
4. Figma resets the property to match the main component.

## Push changes to main component

You can choose to push your changes back to the main component, which updates any other instances of that component.

You can only push changes if the main component is in the same file as the instance. It’s not possible to push changes to components in another file, including published libraries.

Note: It’s not possible to push changes to a component that’s nested within another component. You need to make those changes to the main component itself.

1. Select the instance with your changes applied to it. You need to select the instance itself, not a specific layer within it.
2. Click **More actions** next to the component name in the right panel.
3. Select **Push changes to main component**.

Note: If you are working in a published library file, you need to [publish your changes](%E2%80%9Chttps://help.figma.com/hc/en-us/articles/360038665934#Publish_changes_to_the_library%E2%80%9D) to allow other instances to receive those updates.
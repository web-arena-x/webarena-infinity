# Create components to reuse in designs

Source: https://help.figma.com/hc/en-us/articles/360038663154-Create-components-to-reuse-in-designs

---

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file can create and edit components

You can create a component out of any collection of objects or layers. Components can be as simple as shapes, buttons or fields, or more complex design like cards and menus.

Tip: Variants allow you to group and organize similar components into a single container. This simplifies your component library and makes it easier for everyone to find what they need. Learn more about [creating variants](https://help.figma.com/hc/en-us/articles/360056440594).

## Create a component

To create a component:

1. Select the layers you’d like to be included in the component.
2. Do one of the following:  
   - Click  **Create component** next to the selection's name in the right sidebar
   - Right-click on your selection and choose **Create component**
   - Use the keyboard shortcut:
     - **Mac**: `Option` `Command` `K`
     - **Windows**: `Ctrl` `Alt` `K`

Figma will nest the layers within a special component frame*.*Identify components in the **Layers** panel using the purple  Component icon. Once created, you can use the [Component configuration settings](../create-and-share-libraries/add-descriptions-to-styles-components-and-variables.md#components) to add a description and documentation link for collaborators.

## Create components in bulk

You can also create components in bulk. This allows you to select multiple layers and create components out of them. Create multiple components from:

- Objects and layers in frames
- Objects and layers in groups
- Single layers, like a path or vector network
- Layers in a boolean operation

Note: If you select more than one layer that isn't on one of the above configurations, Figma will create a component for each individual layer.

1. Select the layers you want to create components from,
2. Click  next to the selection's name in the right sidebar to open the **Create component options** menu.
3. Select  **Create multiple components** from the options.
4. Figma will create a component for each frame, group, boolean operation, or path.

![](https://help.figma.com/hc/article_attachments/26949853048471)

## Delete a component

You can delete components at any time.

Deleting a main component does not remove instances of that component from your files.

1. Select the component you want to delete.
2. Press `Delete`.

## Restore a component

If you have an existing [instance](../use-libraries/create-and-insert-component-instances.md) of a deleted component, you can use that instance to restore the component.

There are a few ways to restore a component from an instance:

### From the right sidebar

1. Select an existing instance of the deleted component.
2. Do one of the following:
   - If you are in the library file that contained the main component, click **Restore Component** in the right sidebar
   - If you are in a file that did not contain the main component, click **Go to main component in library**. Then click the **Restore** button in the dialog window.

![](https://help.figma.com/hc/article_attachments/26949853055255)

### From the right-click menu

1. Right-click on the instance in the canvas.
2. Do one of the following:
   - If you are in the library file that contained the main component, hover over the **Main component** option and click **Restore main component**
   - If you are in a file that did not contain the main component, click **Go to main component**. Then click the **Restore** button in the dialog window

![](https://help.figma.com/hc/article_attachments/24436486532119)
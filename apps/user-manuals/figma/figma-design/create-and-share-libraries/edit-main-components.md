# Edit main components

Source: https://help.figma.com/hc/en-us/articles/360038665934-Edit-main-components

---

Who can use this feature

Components are supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan). You must be on a Professional, Education, or Organization plan to publish components to libraries.

Anyone with edit access to the file can make changes to the main components in that file.

New to components and libraries? **[Guide to style and component libraries →](https://help.figma.com/hc/en-us/articles/360041051154)**

Any instance you create is linked to the main component. When you make changes to the main component, Figma will apply any changes you apply to any linked instances.

If you are using instances within the same file as your main components, Figma applies changes immediately. If the components are published to a library, you need to publish those changes to see those updates in subscribed files.

## Update components

To make sure Figma applies changes to all instances of a component, you will need to edit the main component. You can only edit main components in the original files where they live.

- **Unpublished components**:

 If you're on the Starter plan, or haven't published the components to a library, you can edit your main components like you would any other layers.

 Figma will automatically apply any changes you make to the main component to any instances of the component in your file.
- **Published components:**Figma will immediately apply any changes you make to any instances in that file. If you want those changes to apply to instances in other files, you will need to publish those changes to the library.

**Want to change the location of components?** You can move published components between files and libraries. [Move published components.](https://help.figma.com/hc/en-us/articles/4404848314647/)

### Find main components

If you're working with instances in a separate file, use the **Go to main component** action to open the library file. From there, you can apply any changes you want to the main component.

You can access the **Go to main component** action from one of two places.

Using the keyboard shortcut:

- Mac: `^ Control``⌥ Option``⌘ Command``k`
- Windows: `Control``Alt``Shift``k`

From the Instance menu:

1. Select an instance in the current file.
2. Open the **Design** tab in the right sidebar.
3. Hover over the name of the library file to see **Go to main component in library**. Click to open the library file to the location of the main component.
4. Select the main component and make any changes.

Note: If you accessed the main component from another file, Figma will give you the option to **Return to instance** after making your changes.

## Push overrides to main component

There may be situations where you want changes you've applied to an instance to apply to the main component as well.

You can use the **Push overrides to main component** setting to apply any overrides to the main component. This will also update any other instances of that component.

You can only push overrides if the main component is in the same file as the instance. It's not possible to push overrides to components in another file, including published libraries.

Note: It's not possible to push overrides to a component that's nested within another component. You will need to make those changes to the main component itself.

1. Select the instance with your overrides applied to it. You need to select the parent frame of the instance, not a sublayer.
2. In the right sidebar, click next to the component name.
3. Select **Push overrides to main component** from the options.
4. Figma will apply your overrides to the main component.

## Publish changes to the library

If you make changes to a published style or component, this will only apply those changes to instances in the current file. If you want those changes to be reflected in your library, you will also need to publish those changes to the library. [Learn more about publishing a library.](https://help.figma.com/hc/en-us/articles/360025508373)
# Swap components and instances

Source: https://help.figma.com/hc/en-us/articles/360039150413-Swap-components-and-instances

---

Who can use this feature

Supported on [Education, Professional, and Organization, plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with can edit access to a file can insert components into a file.

New to components and libraries? [Guide to style and component libraries →](https://help.figma.com/hc/en-us/articles/360041051154)

Components let you create and reuse elements of your designs to speed up the process and keep things consistent.

When building interfaces, we often switch between instances of these components for objects like icons, buttons, and cards.

The Instance menu lets you quickly search, preview, and swap one component for another. There are a few ways you replace or swap instances in Figma.

**Want to swap instances in bulk?** Use the **Swap libraries** feature to replace instances in the current file with components from another library. [Swap libraries →](https://help.figma.com/hc/en-us/articles/4404856784663)

Note: Figma will try to preserve any overrides when you select a different variant, or swap between instances in the Instance menu. [Learn more about override preservation →](https://help.figma.com/hc/en-us/articles/360039150733)

## Instance menu

The Instance menu allows you to find component replacements from the current file and any [libraries added to the file](https://help.figma.com/hc/en-us/articles/360039234953-Enable-Libraries-in-the-Assets-Panel-for-a-Team).

When you have a component selected, access the Instance menu in the right sidebar.

![An animation showing how to swap instances using the instance menu in the right sidebar.](https://help.figma.com/hc/article_attachments/24302288548631)

Figma orders components in the Instance menu based on the component's **Name** and **Location**.

- Related components are components that share the same hierarchy. This includes components in the same file, page, and frame.  
    
  For example: you can have a **file** containing your app's UI design system, a **page** for each operating system, and **frames** within each page where your components are grouped by type.
- Figma also groups related components organized using the slash naming structure.  
    
  For example: Figma considers `UI/Button/Active`, `UI/Button/Hover`, and `UI/Button/Inactive` as related components.

![Three panels showing Figma's Instance menu navigation, organized by slash-naming hierarchy: simple design system, inputs, checkbox.](https://help.figma.com/hc/article_attachments/24302858951959)

[Learn how to name and organize components →](https://help.figma.com/hc/en-us/articles/360038663994-Name-and-organize-Components)

To swap an instance using the **Instance** menu:

1. Select the instance you want to replace. Figma will display the name of the component in the right sidebar.
2. Click the name of the component to open the Instance menu.
3. Use the menu to navigate through components:
   1. Select from the group of related components for your selection.
   2. Use the  field to search a component by name.
   3. Click  to switch between [libraries added to the file](https://help.figma.com/hc/en-us/articles/360039234953-Enable-Libraries-in-the-Assets-Panel-for-a-Team).
   4. Click  to navigate to a different group of components.
   5. Use the  and  to switch between grid and list view.
4. Select an instance to replace the current selection.

![](https://help.figma.com/hc/article_attachments/24303196234903)

## Assets panel

The **Assets** panel in the left sidebar allows you to search for components to add to your file. You can find components from any libraries you have access to.

You can drag a component onto the canvas to create an instance of that component. If you use the modifier key while dragging a component from the Assets panel, you can replace the existing component.

1. Open the **Assets** panel and find the component.
2. Hold down the modifier key: If the component **isn't nested** within another frame or component
   - **Mac**: `⌥ Option`
   - **Windows**: `Alt`If the component **is nested** within another Frame or component
   - **Mac**: `⌥ Option` - `⌘ Command`
   - **Windows**: `Alt` + `Control`
3. Drag the component above the instance you want to swap in the canvas.
4. Release the mouse, then release the modifier key. If you release the modifier key first, Figma will only add the new component, not replace.

Note: Figma only preserves text overrides. To keep any changes you've made to text layers, [rename the layers](../work-with-layers/rename-layers.md) so they're unique. If you swap a component with other overrides applied, we won't apply these to the new component. Learn more about [overriding properties of an instance](https://help.figma.com/hc/en-us/articles/360039150733).

## Quick insert

Swap instances of components from your keyboard using quick insert. Quick insert opens the Resources modal where you can find and view components from libraries that have been added to the file. The components found in the Resources modal mirror what you see in the Assets panel.

1. Select the layer or instance you want to swap.
2. Use the shortcut `Shift` `I` to open quick insert.
3. To locate a component, do one of the following:
   - Use the search field to find a specific component. Use your mouse or arrow keys to navigate to the relevant component.
   - Use the  and  icons to switch between grid and list view.
   - Select from a library that's been added to the file. If a library is not displaying, you may need to add it first. [Manage libraries in design files →](https://help.figma.com/hc/en-us/articles/1500008731201)
4. Hold down `⌥ Option` (Mac) or `Ctrl` (Windows).

![](https://help.figma.com/hc/article_attachments/24303315000087)

## Right-click menu

You can also use the right-click menu to switch between related components. This will only allow you to select components in the same frame or hierarchy.

1. Right-click on the instance in the canvas.
2. Hover over the **Swap Instance** option.
3. Select an instance from the list of related components.

![In the right-click context menu on Figma Design's canvas, the cursor hovers over swap instance.](https://help.figma.com/hc/article_attachments/24382659054615)
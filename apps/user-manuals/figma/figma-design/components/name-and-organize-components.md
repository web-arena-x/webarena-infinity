# Name and organize components

Source: https://help.figma.com/hc/en-us/articles/360038663994-Name-and-organize-components

---

Before you Start

Who can use this feature

 

Available on [any plan](https://www.figma.com/pricing/)

Anyone with `can edit` access to a file can rename layers, including components

New to components? Check out our [Guide to components](https://help.figma.com/hc/en-us/articles/360038662654) and [Guide to libraries](https://help.figma.com/hc/en-us/articles/360041051154) articles.

Name and organize your components to ensure consistency across your design system, and make them easier to find in the [assets tab](https://help.figma.com/hc/articles/360039831974#assets) and when [swapping related component instances](https://help.figma.com/hc/en-us/articles/360039150413). We recommend defining and documenting a component naming structure within your team or company.

Tip: Not sure where to start with building a component library? Our [Best practices: components, styles, and shared libraries](https://www.figma.com/blog/component-styles-and-shared-library-best-practices/) article has some great suggestions.

## Component organization in the assets tab

In the assets tab, the organization of components mirrors the file's structure. You will see this general path: `file > page > frame`

You can click on each library file to see its pages. Figma displays pages in alphanumeric order, not the order they are listed in the original file.

Then click on a specific page name to explore the components within. When you click on a component, you'll see a fly-out with more details, such as the component's description and properties.

## Component organization in the swap instance menu

You can view details about a selected instance at the top of the **Design** tab in the right sidebar.

From here, you can click next to the component's name to open the Swap instance window, which displays related components that you can swap the selected instance to.

We determine related components by:

- **How the main component is named**. For example, we will display `UI/Button/Active`, `UI/Button/Hover` and `UI/Button/Inactive` together.
- **How the main component is arranged in the original file**. For example, components within the same frame or section are considered related.

## Organize components by name

To add another layer of organization, you can use naming conventions to categorize your components and add consistency across your files. We recommend you use the slash-separated convention, such as `Component/State` or `Icon/Name`.

This might look like:

- Button/Active
- Button/Hover
- Button/Inactive
- Icon/Alert
- Icon/Profile
- Icon/Close

Tip: Need to rename multiple components at once? [Learn how to rename layers in bulk.](https://help.figma.com/hc/en-us/articles/360039958934)

## Organize components via file structure

To illustrate the importance of component organization, the following example will walk through how you can define your file structure and name its pages and frames to determine the location of your components within.

- In a file named **Figma UI**, we'll create components that make up the Figma UI.
- In the file, we'll create a page called `Icons`, which houses all of our icon components.
- We support two sizes for each icon, 16px and 32px. We'll create two sections for each size, and name them accordingly `16` and `32`, then place the icon components into their corresponding sections.
- To make it easier to differentiate between the icon sizes, we'll make sure to include the icon's size in its name. For example, `icon-16-home` and `icon-32-home`.
- In another file, we've created a dialog window that needs a close  icon. We've already created and published this close icon component in our Figma UI file, so we'll use an instance of that component in our other file.

Note: For this approach, you will need to [publish your library](../create-and-share-libraries/publish-a-library.md) and [add it to the other file](../manage-your-libraries/add-or-remove-a-library-from-a-design-file.md). The ability to publish libraries is only available on our [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features).

- From the other file, we'll go to the assets tab and locate our Figma UI library file. We'll click the file name, open the Icons page, and select either the 16 or 32 section.
- We need the 32px version of that icon, so we'll select that one and then drag that component from the **Assets** tab into the file.
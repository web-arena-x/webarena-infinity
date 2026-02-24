# Create components in Figma Slides

Source: https://help.figma.com/hc/en-us/articles/30630178611991-Create-components-in-Figma-Slides

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a slide deck and a Full seat on paid plans can create components

Anyone with `can edit` access to a slide deck and a Collab, Dev, or Full seat on paid plans can add instances of main components to slides

Components are reusable design elements. They save you from having to recreate the same element multiple times, and make it easy to manage changes across your slide deck.

There are two aspects to a component:

- The **main component** that defines the properties of the design element
- And an **instance** that’s a copy of the component, which you can add to your designs.

Creating and using components in Figma Slides works similarly to how it does in Figma Design. If you’re new to using components, we recommend reading the [guide to components](../../figma-design/components/guide-to-components-in-figma.md) to become familiar with the terms used in this article.

Note: You can also access components by [adding Figma Design libraries](add-figma-design-libraries-to-your-slide-deck.md) to your slide deck.

## Things to keep in mind

There are a few things to be aware of when using components in Figma Slides:

### Publishing slide deck templates

Similar to publishing a library in Figma Design, you can publish components within a [slide deck template](../use-slide-deck-templates/publish-slide-deck-templates-to-a-team-or-organization.md) for your team or organization to use. When the template is used in another deck, any main components that exist inside slides will become instances. These instances are still linked to the main component in the original deck and are eligible to receive updates if the main component changes. You can also add additional instances from the **Assets** menu.

However, if you are publishing slide deck templates to the [Figma Community](https://help.figma.com/hc/en-us/articles/25923960876567-Publish-slide-deck-templates-to-the-Figma-Community), users won’t be able to add new instances from the **Assets** menu or receive updates when the original component changes.

### Ineligible object types

The following objects cannot be turned into main components or be included within a main component:

- Shapes with text
- Code blocks
- Tables
- Live interactions
- Prototypes

## Create a main component

You can only create components while in design mode. Use the toggle in the toolbar to switch to design mode.

To create a main component:

1. Select the objects you want to be included in the component.
2. Click **Create component** in the right sidebar or use the keyboard shortcut:
   - **Mac**: `⌥ Option` `⌘ Command` `K`
   - **Windows**: `Ctrl` `Alt` `K`

Note: You can also create multiple components at once by selecting two or more objects and clicking **Create multiple components** in the Create component options menu.

Once a component is created, you can click **Component Configuration** next to the component name to add a description and documentation link for collaborators. You can also apply component properties to the component. Learn more about [component properties](../../figma-design/components/explore-component-properties.md).

![](https://help.figma.com/hc/article_attachments/30630199221015)

## Delete a main component

You can delete a main component at any time. Deleting a main component will not remove instances of that component from your slide deck. To delete a main component, select it and press `Delete`.

## Restore a main component

If you have existing instances of a deleted main component in your slide deck, you can use that instance to restore the main component.

1. Select an instance of the deleted main component.
2. Click **Restore Component** in the right sidebar.

![](https://help.figma.com/hc/article_attachments/30630178606871)

## Insert instances

Instances are copies of a main component that you can add to your designs. Instances are connected to the main component. This means that changes made to the main component are automatically applied to every instance of that component in the same file, saving you time and making sure your designs stay consistent.

For example, you can create a reusable footer main component and add an instance of it to every slide. When updates are needed, such as modifying the date, changes made to the main component are automatically applied to all instances in the slide deck.

You can insert instances in slides mode or design mode.

To insert an instance:

1. Select **Assets** in the toolbar.
2. Select **Local components** to view all component created in the current slide deck.
3. Click on a component to add an instance to the slide deck.

![](https://help.figma.com/hc/article_attachments/30630199225879)
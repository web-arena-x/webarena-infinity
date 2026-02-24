# Edit instances with component properties

Source: https://help.figma.com/hc/en-us/articles/8883757553943-Edit-instances-with-component-properties

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can create and manage component properties

New to component properties? Learn how component properties works by [exploring the different types](https://help.figma.com/hc/en-us/articles/5579474826519), preferred values, exposed nested instances, and more.

Component properties are the changeable aspects of a component, so you know which parts of a component — like icons or text — can change.

When editing an instance containing component properties, the component properties controls appear in a single section of controls in the right sidebar. This makes it easy to know what is changeable and to make those changes in one place.

![](https://help.figma.com/hc/article_attachments/31413132910615)

This also removes the need to select and override individual layers, reduces time needed to refer to documentation, and removes the guesswork out of design systems!

When editing an instance, you can check any available descriptions or documentation to ensure accurate use of the asset. Component documentation can include a description, a link to external documentation, or both. Learn how to [view component documentation](https://help.figma.com/hc/en-us/articles/7938814091287#view-descriptions).

## Configure properties

When you select an instance containing component properties, the Properties section of the right sidebar will populate with different component property controls. Use the accompanying dropdowns, toggles, or text fields to make changes, and they will be reflected in the instance.

- **Boolean property:** Allows you to set true/false values to turn a specific property on or off. Currently only available for layer visibility. Use the toggles to turn the setting on and off.
- **Instance swap property:** Indicates which instances can be swapped. Dropdowns with a  denote instances that you can swap.
- **Text property:** Indicates which text strings can be edited. Update the text in text fields to directly change the string of text that appears on the canvas.
- **Variant property:** Allows you to define specific values and attributes to your variants, such as state, color, or size. Dropdowns with no icon denote variant states that you can change.

Learnn more about [component property types](https://help.figma.com/hc/en-us/articles/5579474826519).

## Overrides

You can still make overrides to non-component properties of a single instance. Figma records the changes you make to an instance and preserves them, even when you swap between instances or select different variants.

Learn more about [overrides and override preservation](https://help.figma.com/hc/en-us/articles/360039150733-Apply-overrides-to-instances).

Tip: Component properties are supported in Figma's plugin API. Learn more from [Figma's plugin developer docs](https://www.figma.com/plugin-docs/blog/2022/06/23/version-1-update-49/).
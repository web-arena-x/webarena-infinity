# Link Dev resources to layers in Dev Mode

Source: https://help.figma.com/hc/en-us/articles/15023231995927-Link-Dev-resources-to-layers-in-Dev-Mode

---

Before you Start

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires a [Full or Dev seat](https://help.figma.com/hc/en-us/articles/360039960434)

Dev resources are a great way for anyone to add external documentation that can help developers better understand and build a component. Dev resources can be linked to objects in Figma Design and are often related to the documentation or source code. Use Dev resources to:

- Link a GitHub file to a component for quick access to the source code
- Assign a Jira ticket to a specific part of a mockup
- Connect Storybook to view stories in Figma

Note: If an attached dev resource has a related plugin available, clicking the link will automatically launch it in the **Plugins** tab.

# Link to a Dev resource

Dev resources can be added to any layer on the canvas. If a dev resource is added to a component, the link is inherited by all instances of that component. If a dev resource is added to an instance of a component, the link will only appear for that instance.

To link to a dev resource:

1. Copy the URL you want to add.
2. In Dev Mode, select a layer on the canvas.
3. In the inspect panel, click **Layer options**, and then **Add a dev resource link**.
4. In the box that appears in the inspect panel, paste the link.
5. Press `Enter`

![Add a dev resource link to a main component in the inspect panel, ensuring links appear on all instances.](https://help.figma.com/hc/article_attachments/32233541572375)

# Remove a linked Dev resource

1. In the inspect panel**,** click **Additional options** next to the link to the resource.
2. Select **Delete link**.

Note: Dev resources with related plugins may have different ways of detaching a link from a layer. [Learn more about using plugins in Dev Mode.](../tour-the-interface/guide-to-dev-mode.md#01H8CR3K6W4DXEW0G1VP2SE003)

![Inspect panel showing a linked Dev resource with options to copy, edit, or delete the link.](https://help.figma.com/hc/article_attachments/32233527666199)
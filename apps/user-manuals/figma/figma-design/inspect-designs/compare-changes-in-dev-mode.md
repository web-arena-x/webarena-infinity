# Compare changes in Dev Mode

Source: https://help.figma.com/hc/en-us/articles/15023193382935-Compare-changes-in-Dev-Mode

---

Before you Start

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires a [Full or Dev seat](https://help.figma.com/hc/en-us/articles/360039960434)

Dev Mode allows developers to see when a frame or component was last edited and compare changes made at different points in its version history. Since the handoff between design and development can be iterative, being able to compare changes and version history brings clarity to the process. With compare changes, you can always track the latest updates and keep production code accurate.

# Compare changes

If a frame or component has been updated since you last viewed it, you can compare its version history. You can also compare detached components, or instances with design overrides against the base component.

1. Select a top-level frame or component.

   **Tip:** Hold `Shift` and click to select two components on the canvas to compare them with each other.
2. In the Inspect tab of the right sidebar, click **Compare changes**.![Comparing design versions side-by-side with edited layers and code changes panel; includes version history and properties view.](https://help.figma.com/hc/article_attachments/30567573025047)

- A 

  #### Version history

  View a timeline of the file’s history, including saved and autosaved versions. Click on a previous version to compare with the current version. Version history is only shown when comparing a top-level frame over time.
- B 

  #### View edited layers

  Under **Layers**, you can view how an asset’s individual layers have changed over time. Layer changes are labeled as one of the following:

  - **Edited:** The layer was edited between the current and selected versions
  - **Added:** The layer was added between the current and selected versions
  - **Deleted:** The layer was deleted between the current and selected versions

  Clicking on a layer in the list zooms in to the selected layer in the side by side or overlay view.
- C 

  #### Side by side

  A side-by-side view of the selected version and current version of an asset. Adjust the modal’s zoom settings using the  zoom in and  zoom out buttons on the right.
- D 

  #### Overlay

  An overlay view of the current frame version on top of the selected version is helpful for making smaller edits stand out. Use the slider on the right to adjust the current frame’s transparency or click  to toggle its visibility. Adjust the modal’s zoom settings using the  zoom in and  zoom out buttons on the right.
- E 

  #### Compare code

  When you select an edited layer, you can view updated code between the previous version and the current version. This is helpful for making sure your codebase is aligned with the most recent designs.

  Use the dropdown to select your preferred language for the code panel, and click  to select your preferred unit.

  [Learn more about using code snippets in Dev Mode →](../turn-designs-to-code/use-code-snippets-in-dev-mode.md)
- F 

  #### Compare properties

  When you select an edited layer, the updated properties are displayed, along with the assigned values from the previous version and the current version.

# Compare changes in focus view

When focused on a design in Dev Mode, you can take advantage of the version history in the focus view to compare changes. When you compare changes, the interface is the same as detailed in [Compare changes](#01H8F1S0AKZQJMT0J4KNB9F20H).

To compare changes while in focus view:

1. Open a Figma Design file.
2. On the canvas, for the design you want to focus on, click the dev status indicator and select **Show in focus view**.  
   While nothing is selected, the focus view displays the version history on the right side of the view.
3. For the version that you want to compare with the latest, click **…** and select **Compare to latest version**.  
   ![Version timeline with a dropdown menu highlighting "Compare to latest version" for selecting and reviewing design updates.](https://help.figma.com/hc/article_attachments/30567582453399)
4. Optionally, to get a link to the focus view that you can share with others, click **Copy link**.

[Learn more about focus view →](https://help.figma.com/hc/en-us/articles/23919923330455)
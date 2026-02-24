# Edit objects on the canvas in bulk

Source: https://help.figma.com/hc/en-us/articles/21635177948567-Edit-objects-on-the-canvas-in-bulk

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can edit objects on the canvas

Want to get hands-on with editing objects in bulk? Grab a copy of the [multi-edit playground file](https://www.figma.com/community/file/1343991048099728924) to practice while you learn.

Select multiple layers across frames, groups, and sections and apply the same edits to them in bulk. For example:

- Update the string on a text layer, and other selected text layers will update as well
- Create multiple groups of objects across separate sections
- Add auto layout to multiple nested objects across frames
- Insert an object into one variant that repeats across all variants in a component set

## Edit objects in bulk

You can select multiple layers across frames, groups, or sections either via the canvas or the Layers panel. You can also bulk select matching objects. Learn how to [select multiple layers and matching objects →](select-layers-and-objects.md)

Once you’ve selected objects, you can bulk edit them at the same time. This includes rotating, grouping, masking, boolean operations, adding auto layout frames, and more. These actions work even if the selected objects live in different types of containers (frames, groups, and sections).

A couple of things to note:

- **Alignment:** Hold `⇧ Shift` and click one of the alignment buttons in the right sidebar to [align objects](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-and-position) to their respective parent frames.
- **Copy and paste:** Objects copied from and pasted to multiple frames are pasted in the order that they are copied and will repeat if there are additional frames. Learn about [how objects will be pasted →](https://help.figma.com/hc/en-us/articles/4409078832791-Copy-and-paste-objects-in-the-canvas)

## Multi-edit text

You can update the content of multiple text layers at the same time.

1. Select more than one text layer. Learn how to [select multiple layers and objects →](https://help.figma.com/hc/en-us/articles/360040449873)
2. Click  **Multi-edit text** at the top of the right sidebar or press `Enter` / `Return` to edit the contents. All selected text layers will update to match.

## Multi-edit variants

Multi-edit speeds up your workflow when editing [variants and component sets](https://help.figma.com/hc/en-us/articles/360056440594). When you edit a variant while having multi-edit enabled, matching objects will automatically get the same edits.

To enable multi-edit:

1. Select a component set, a variant, or a nested layer inside a variant. If you select:
   - **A component set**: Enabling multi-edit places a dotted rectangle around each variant within the set to indicate the objects you can edit
   - **A variant**: Enabling multi-edit selects other component variants in the set
   - **A nested layer**: Enabling multi-edit selects matching objects across other component variants in the set
2. Click  **Multi-edit variants** at the top of the right sidebar, or press `Q`.
3. To exit multi-edit, click , or press `Q`. You can also double-click anywhere on the canvas outside the component set.

[Check out the entire multi-edit video playlist →](https://youtu.be/XfHSWfCrX58?feature=shared)
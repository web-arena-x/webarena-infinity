# Convert text to vector paths

Source: https://help.figma.com/hc/en-us/articles/360047239073-Convert-text-to-vector-paths

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can convert text layers to vector paths

You can convert any text layer into a vector path. Once converted, you can use [vector edit mode](edit-vector-layers.md) to modify the layer's path. This is useful for:

- Customize aspects of a typeface
- Creating logos or wordmarks
- Preparing assets for printing
- Reducing file or export size
- Combining multiple paths into a single object

There are two ways to turn a text layer into a vector path: flattening the layer or outlining the layer's stroke. Both methods are destructive actions, meaning you'll no longer be able to edit the text contents or any typography properties associated with it. If you convert a text layer by mistake, you can use the file's [version history](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history) to restore a previous version or use the undo shortcut:

- Mac: `Command` `Z`
- Windows: `Control` `Z`

**Note:** Looking for information about typing text on a vector path instead? Check out our [Guide to text](../text-and-typography/guide-to-text-in-figma-design.md#h_01JTH0B6GEA7AVVXVS72X7ANHK).

## Flatten a text layer

When you flatten text layers, Figma will:

- Combine any objects or layers you selected into a single layer
- Convert text layers from editable text to vector paths

To flatten a text layer:

1. 1. Select the text layer you want to flatten.
   2. Right-click on the selection and select **Flatten**or use the keyboard shortcut:
      - **Mac**: `Option` `Shift` `F`
      - **Windows**: `Alt` `Shift` `F`

      Once flattened, the layers will be combined into a single vector layer. Select the layer and press `Enter` to open [vector edit mode](edit-vector-layers.md).

![Text layer flattened to an editable vector path.](https://help.figma.com/hc/article_attachments/32128865055127)

## Outline a layer's stroke

When you use outline stroke, Figma will:

- Convert text layers from editable text to vector paths
- Not combine any objects or layers you selected into a single layer

To apply outline stroke:

1. Select the layer in the canvas.
2. Right-click on the layer and select **Outline stroke**or use the keyboard shortcut:
   - Mac: `Command` `Option` `O`
   - Windows: `Control` `Alt` `O`

When **Outline stroke** is applied, each glyph is converted to its own vector layer, so you can edit each layer individually in [vector edit mode](edit-vector-layers.md).

![Text layer converted to individual vector layers on canvas, each letter is separate for editing.](https://help.figma.com/hc/article_attachments/32128827675927)
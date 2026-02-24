# Convert strokes to vector paths

Source: https://help.figma.com/hc/en-us/articles/33052305733015-Convert-strokes-to-vector-paths

---

Outline stroke allows you to convert strokes into vector paths. This will take each path in the object and turn it into a single editable shape, allowing you to:

- Remove or extend half-dashes
- Create custom shapes and edit them in vector edit mode
- Combine multiple paths into a single object
- Scale vector objects uniformly

Note: Outlining a stroke is a destructive action. Once a stroke is outlined, the stroke properties cannot be changed. If you outline a stroke by mistake, you can use the file’s [version history](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history) to restore a previous version or use the undo shortcut:

- Mac: `Command` `Z`
- Windows: `Control` `Z`

## Outline stroke

To convert a stroke into a vector layer, right-click the layer and select **Outline stroke**, or use keyboard shortcut:

- **Mac:** `Command` `Option` `O`
- **Window:** `Control` `Alt` `O`

Once a stroke is converted, you can use [vector edit mode](edit-vector-layers.md) to edit the vector path.

**Note:** If you prefer to use `Command` / `Control` `Shift` `O` to toggle outline stroke, open the main menu in the top left-corner and go to **Preferences** > **Use old shortcuts for outlines**. This setting will also change the keyboard shortcut for [show outlines](https://help.figma.com/hc/en-us/articles/5724448965527) to `Shift` `O`.

![Image showing how much more complex a shape is when you use outline stroke](https://help.figma.com/hc/article_attachments/33052305731479)

**Tip:** If you have a style applied to the stroke, the color properties of the style will be applied to the vector object as a fill.
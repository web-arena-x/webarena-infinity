# Create bulleted and numbered lists

Source: https://help.figma.com/hc/en-us/articles/360040449773-Create-bulleted-and-numbered-lists

---

Before you start

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with **can edit** access to a file to create and edit text layers.

Lists are a great way to organize and emphasize related information. List items in Figma can either be ordered or unordered in the form of a numbered or bulleted list.

Figma currently supports up to **five** levels of indentation.

![Bulleted and numbered list examples in Figma showing indentation levels with items on cats, dogs, and coding terms.](https://help.figma.com/hc/article_attachments/19783492719895)

# Bulleted lists

You can use bulleted lists to represent unordered sets of information. Figma bullets will keep the same styling at all levels of indentation. At the moment, bullets cannot be customized.

### Create a bulleted list

1. Select the  **Text** tool in the toolbar or by pressing the `T` key.
2. Once in the text layer, there are a few ways to start a bulleted list:
   - Enter one `-` or `*` followed by a `Space`on a Mac or Windows.
   - Enter the keyboard shortcuts:
   - Mac: `⌥ Option``8`
   - Windows: `Alt`+`0`+`1`+`4`+`9`- In the right sidebar, under the Text properties section, you can click  to open the **Type details** panel. From the List style property, select  Bulleted list.

**Tip:** You can use `⌘ Command``Shift``8` to turn an individual text selection or multiple text layers into a bulleted list.

# Numbered lists

Numbered lists can be used to represent groups of ordered or sequential information. In Figma, numbered list counters rotate between numbers, alphabetical characters, and roman numerals with each indentation.

### Create a numbered list

1. Select the  **Text** tool in the toolbar or by pressing the `T` key.
2. From within the text layer, there are a couple of ways to start a numbered list:
   - Enter one of the creation characters below followed by a `Space`:
     - `1``.`
     - `1``)`
   - Click  in the **Text** section of the right sidebar, then select  **Numbered** list.

**Tip:** You can use `⌘ Command``Shift``7` to turn an individual text selection or multiple text layers into a numbered list.

# Format list items

Keep in mind that keyboard shortcuts will activate automatic list styling.

Using `⌘ Command``Z` immediately after a list shortcut removes the default styling.

## Indentation

Figma bulleted and numbered lists currently support **five** levels of indentation. To change a list item's indentation:

### Increase indentation

- Use `Tab``⌘ Command``]` or `Control` + `]` to increase the indentation of a line.
- Pressing `Tab` will increase the indent again.

### Decrease indentation

- Use `Backspace` or `Delete` at the beginning of a list item to delete the counter, but keep the same level of indentation.
- Each line's indentation can be decreased individually.
- Use `Return` or `Enter` while on an empty list item to decrease indentation.

## Spacing

### List

**List spacing** lets you control the distance between each line item in a bulleted or numbered list. By default, list spacing is set to `0` when creating a new list and for any existing text styles. Figma represents list spacing in pixels (px).

To adjust list item spacing:

1. Select text in a list or a text layer with only list text.
2. Use the  field to enter a px value in the list spacing field. Or hover above the icon and drag to **decrease (left)** or **increase (right)** the value.

You can also adjust list spacing from the **Type details** panel by clicking  in the **Text** section of the right sidebar.

### Paragraph

Paragraph spacing lets you control the distance between paragraphs. This can increase or reduce the whitespace around text in your design. White space can help to focus the viewer's attention, as well as increase legibility and readability.

Figma represents paragraph in **pixels (px)**. Enter a px value in the paragraph spacing field. Or hover above the icon and drag to **decrease (left)** or **increase (right)** the value.

Note: Figma will create a new paragraph when you use the `Enter` or `Return` keys. This is something to bear in mind if your [text resizing](explore-text-properties.md#basic) is set to **Auto Width**.

[Learn more about text properties →](https://help.figma.com/hc/en-us/articles/360039956634)

### Hanging quotes

Toggle hanging quotes to move a text layer's opening quotation marks outside of the bounding box.

![Comparison of text bounding box with hanging quotes toggle off and on, showing effect on text alignment.](https://help.figma.com/hc/article_attachments/19761009274903)

### Hanging lists

Toggle hanging lists to move bullet points or numbers of each list item outside of the bounding box. This aligns text content with the bounding box.

![Type settings panel displaying text with bullets in a list, showing options to adjust hanging lists and paragraph indent.](https://help.figma.com/hc/article_attachments/19761009281047)

[Learn more about formatting text →](https://help.figma.com/hc/en-us/articles/360039956634)

## List styling

### Text color

- The first character of the first item in the list sets the color for the bullets in the list
- Following list items will take on the text color of the item preceding it

![Color-coded bulleted list in Figma showing CSS color names with their corresponding hex values and 100% opacity.](https://help.figma.com/hc/article_attachments/1500007596962)

### Stroke

- Stroke properties are applied to the entire selected text layer.
- Changes to the weight of your text will apply to the bullet associated with it.

### Effects

- Effects will be applied to the entire selected text layer. This includes any bullets and counters.

Tip! Selecting the  No list property from the Type panel removes any current list styling from a text selection.
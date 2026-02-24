# Rename Layers

Source: https://help.figma.com/hc/en-us/articles/360039958934-Rename-Layers

---

Before you Start

Who can use this feature

 

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with can edit access to a file can rename layers

Establishing a clear naming structure or hierarchy makes managing layers in your files much easier. The **Rename layers** function will allow you to quickly rename multiple layers at once.

Tip: [Use Figma AI to quickly rename layers in bulk](https://help.figma.com/hc/en-us/articles/24004711129879). You can then customize layers as needed.

![Figma layers panel showing layers being selected in bulk, right-clicked-, then renamed using the bulk renaming modal.](https://help.figma.com/hc/article_attachments/30801508424215)

## Rename layers modal

You can access the **Rename layers****modal** a number of different ways.

1. Select the layers you want to rename from the canvas, or in the layers panel.
2. To toggle the **Rename Layers Modal** you can then do one of the following: 
   1. Right-click on the layers in the panel and choose **Rename**.
   2. Use the keyboard shortcuts:
      - Mac: `Command ⌘` - `R`
      - Windows: `Ctrl` + `R`
3. The **Rename Layers Modal** will open above the canvas:![Rename layers modal showing fields for "Match" and "Rename to," with options for current name, ascending, descending numbering, and preview list.](https://help.figma.com/hc/article_attachments/30801508429463)

Tip! You can rename a single [frame](https://help.figma.com/hc/en-us/articles/360041539473) or [flow starting point](https://help.figma.com/hc/en-us/articles/360039823894) right from the canvas by double-clicking its current name.

## Rename layers in bulk

If you're wanting to simply update the selected layers to the same name, you can add the desired name to the **Rename to** field and click **Rename**.

However, it's more likely that you will want to update each layer to have a slightly different name, allowing you to better distinguish objects in the Layers panel.

Below the *Rename to* field you will see some buttons. When clicked, these buttons will add a special code to the *Rename to* field that allows you to generate slightly different names for each layer.

- The **Current name** button represents the layer's current name.
- The **Number** `↑` button inserts a number into each layer's name, in an ascending order.
- The **Number** `↓` button inserts a number into each layer's name, in an descending order.

To better explain how this works, we'll show you some examples.

#### Example 1: Rename every layer to the exact same name

If you want to update all of your selected layers to have the same name (for example, *Icon*):

1. Select the layers you want to update.
2. Use the keyboard shortcuts to open the *Rename Layer Modal*
   - Mac: `Command ⌘` - `R`
   - Windows: `Ctrl` + `R`
3. Enter the new name into the *Rename to* field.
4. Click the **Rename** button to apply.
5. The selected layers will be updated to that name.

#### Example 2: Rename each layer with a numerical suffix

If you have a bunch of similar layers that you want to have the same name, but still be distinguishable, you can add a number to the end (or beginning) of the layer's name (for example, *Icon\_1*).

1. Select the layers you want to rename.
2. Right-click on the layers and select **Rename layers**.
3. Enter the name you want to call the layers in the *Rename to* field.
4. Click the **Number** `↑` or **Number** `↓` button. This adds a code to the name, that tells Figma to add a different number to the end of each layer's name.
5. If you like, you can set the **Start ascending from** / **Stop descending at** field.
6. You will see a *Preview* of the updated names on the left. Click the **Rename** button to apply.
7. The selected layers will be updated to the new name, with a unique number at the end.

#### Example 3: Add a prefix to every layer

If you already have a unique name for each layer, but would like to group them for faster editing, you can add a prefix to the existing name (for example, *Icon\_Home*).

1. Select the layers you want to rename.
2. Right-click on the layers in the layers panel and select **Rename layers**.
3. Enter the prefix you'd like to add to the layer name.
4. Click the **Current Name** button to add the current layer name after the prefix.
5. You will see a *Preview* of the updated names on the left. Click the **Rename** button to apply.
6. The selected layers will be updated to start with the prefix, followed by the original name:

## Rename part of a layer's name

While you were using the modal, you may have noticed a " **Match**" field. This allows you to identify which part of the layer's name you want to update. 
 
By leaving this blank you can update the entire name, but you can also use this field to remove or update part of the layer's name (for example, change the " *Icon/*" part in the name "*Icon/Home*" to "*Image/*").

1. Select the layers you want to rename.
2. In the **Match** field, enter the part of the name you'd like to update.
3. Enter what you'd like to replace that part of the name with. This will only replace the part of the layer's name identified in the *Match* field.
4. You will see a *Preview* of the updated names on the left. Click the **Rename** button to apply.

## Use Regular Expressions (Advanced)

If you're familiar with, or confident using regular expressions, then you can also use these in the Rename Layers Modal. This is particularly handy if you want to change the syntax of the name (for example, change "Icon\_003" to  "003\_Icon").

1. Select the layers you want to rename.
2. Use the keyboard shortcuts to open the Rename Layer Modal:
   - Mac: `Command ⌘` + `R`
   - Windows: `Ctrl` + `R`
3. Type `([a-zA-Z]+)_(\d+)` in the **Match** field.
4. Type `$2_$1` in the **Replace** field.
5. You will see a preview of the updated names on the left.
6. Click the **Rename button** to apply.

**New to Regular Expressions or need a refresh?** Mozilla have a [handy reference guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace) on their website.

Some common patterns to get you started are:

- **$1, $2, etc** – the first, second, etc., match marked by parentheses.
- **$&** – the entire thing that was matched.
- **$`** – everything before the thing that was matched.
- **$’** – everything after the thing that was matched.
- **$n** – an increasing counter. (nonstandard).
- **$nnn** – an increasing counter with three digits. (nonstandard)
- **$NNN** –  a decreasing counter with three digits. (nonstandard)

If you want to test your regular expressions before entering them you can try them out here <https://regexr.com/>
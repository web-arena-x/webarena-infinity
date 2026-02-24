# Add right-to-left text

Source: https://help.figma.com/hc/en-us/articles/4972283635863-Add-right-to-left-text

---

Before you start

Who can use this feature

 

Supported on  [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Available in Figma Design and FigJam files

Users with **can edit** access to a file can use RTL and bidirectional text controls

RTL languages and bidirectional text are supported in Figma Design and FigJam files. Control the direction of bidirectional text on text layers, stickies, arrows, and more.

- **RTL** (right-to-left) refers to scripts, or writing systems, that start on the right and continue to the left. This includes Arabic, Hebrew, Farsi, Urdu, and more.
- **Bidirectional** (bidi) text refers to text containing both RTL and LTR (left-to-right) scripts, or writing systems.

By default, Figma automatically handles text direction based on language detection. However, you can override [**text direction with controls ↓**](#direction) in Figma Design and FigJam files.

RTL fonts are available by default in Figma Design. If a character isn’t supported by the font you’re using, Figma will [**fall back ↓**](#fallback) to a Noto font.

Note: If any RTL plugins were previously used on text layers in files, the text will be preserved. However, you can [**upgrade these text ↓**](#rtl-plugins) layers to use Figma’s RTL and bidi features.

# RTL text

## Align text

In Figma Design files, text layers default to **left alignment**. That is, the blocks of text align to the left side of the layer’s bounding box. However, Figma will remember the alignment setting of the previous edited text layer until the file tab refreshes or closes.

Note: Each text layer can have one text alignment. If you need different text alignment, create a new text layer.

In [FigJam](https://help.figma.com/hc/en-us/articles/1500004291281), text will automatically right-align on new stickies if you’re typing in an RTL script.

## Navigate text

Mixing RTL and LTR scripts in the same text layer affects how highlighting and cursor movements work.

When using the left and right arrow keys to navigate through your text, think of their directions as “forward” and “backward” based on the [**direction setting ↓**](#direction) of the text.![forward cursor direction when pressing left arrow key for right to left script](https://help.figma.com/hc/article_attachments/5083953188887)

When clicking and holding your mouse to highlight bits of text, the highlight moves in the direction of the selected language.

# Direction controls

Figma supports bidirectional text, so you can write in both LTR and RTL scripts in the same paragraph. By default, Figma automatically handles text direction based on language detection. However, controls are available to override text direction per paragraph in Figma Design and FigJam files.

If an RTL script is detected in your text layer, a  will appear in the text section of the right sidebar, allowing you to control the text direction.

## Figma Design

Change the direction of RTL text in a Figma Design file from the right sidebar, quick actions menu, or main menu.

**Right sidebar:**

1. Select text layer(s) containing RTL script.
2. Click or to toggle between RTL and LTR directions.

**Quick actions:**

1. Select text layer(s) containing RTL script.
2. Open the [quick actions](https://help.figma.com/hc/en-us/articles/360040328653) menu.
   - Mac: `⌘ Command``/`
   - Windows: `Control``/`
3. Use **right to left text direction** or **left to right text direction**.![text direction from quick actions menu in Figma Design](https://help.figma.com/hc/article_attachments/5084072607639)

**Main menu:**

1. Select text layer(s) containing RTL script.
2. Click  to open the main menu.
3. Go to **Text** > **Text direction**.
4. Select **Left to right** or **Right to left**.

## FigJam

Change the direction of RTL text in a FigJam file from the quick actions menu or the main menu.

**Quick actions:**

1. Select text layer(s) containing RTL script.
2. Open the [quick actions](https://help.figma.com/hc/en-us/articles/360040328653) menu.
   - Mac: `⌘ Command``/`
   - Windows: `Control``/`
3. Use **right to left text direction** or **left to right text direction**.

**Main menu:**

1. Select text containing RTL script.
2. Open the main menu in the top left corner.
3. Go to **Text** > **Text direction**.
4. Select **Left to right** or **Right to left**.

# Supported fonts

If you are using the [Figma desktop app](https://help.figma.com/hc/en-us/articles/360039823654), you can use any fonts already on your computer. If you're using Figma in the browser, you can [install the Figma Font Helper](https://help.figma.com/hc/en-us/articles/360039956894#Install_Figma_Font_Helper) to access your installed fonts.

Figma’s default font list includes RTL fonts.

If the font you’re using does not support the RTL scripts you’re typing, Figma will **[fall back to a different font ↓](#fallback).**

Tip! Figma supports most Google fonts. Go to [fonts.google.com](http://fonts.google.com) and use the **Languages** filter to find fonts that support the script you want to use.

## Font fallback

Font fallback allows you to use characters and icons that aren't specifically supported by that font.

If a font doesn't support a character you input, Figma will render that specific character in a Noto font. No more empty spaces or missing character icons.

# Text using RTL plugins

Any RTL plugins previously used on text layers in Figma Design or text in FigJam will be preserved. However, you can upgrade the text to use Figma’s RTL and bidirectional control features.

Before you upgrade: Check the RTL plugin for a way to reset the text to its original state before the plugin was used. This ensures your text will flow as expected when you upgrade to using Figma’s RTL and bidirectional features.

If the plugin doesn’t provide a way to reset the text, you can still upgrade it to use Figma’s RTL and bidi features, but you will need to create a new text layer and rewrite your copy.

## Figma Design

Upgrade specific text layers using RTL plugins in Figma Design files to use Figma's RTL and bidirectional text features.

**Right sidebar:**

1. Select text layer(s) that previously used an RTL plugin.
2. From the right sidebar, click  in the **Text** section to open the [Type details](https://help.figma.com/hc/en-us/articles/360039956634) panel.
3. At the bottom of the Type details panel, click **Upgrade**.

**Quick actions:**

1. Select text layer(s) that previously used an RTL plugin.
2. Open the [quick actions](https://help.figma.com/hc/en-us/articles/360040328653) menu.
   - Mac: `⌘ Command``/`
   - Windows: `Control``/`
3. Use **update to support bidirectional text**.

## FigJam

Upgrade specific text using RTL plugins in FigJam files to use Figma's RTL and bidirectional text features.

1. Select text that previously used an RTL plugin.
2. Open the [quick actions](https://help.figma.com/hc/en-us/articles/360040328653) menu.
   - Mac: `⌘ Command``/`
   - Windows: `Control``/`
3. Use **update to support bidirectional text (RTL)**.
# Use variable fonts

Source: https://help.figma.com/hc/en-us/articles/5579502031511-Use-variable-fonts

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can use variable fonts

Variable fonts are different from variables. Looking to apply variables to font properties? Check out our [guide to variables](https://help.figma.com/hc/en-us/articles/15339657135383).

A variable font provides a range of dynamic font variations for a typeface in a single file. While static fonts can only contain one font per file, a variable font can contain many.

> For example, if a [typeface](https://www.figma.com/dictionary/#typeface) contains five font styles — italic, thin, regular, bold, and black — using the typeface’s static font files would require five font files. In contrast, using the typeface’s variable font version would combine all five styles into one file.

![An example of a variable font.gif](https://help.figma.com/hc/article_attachments/31412926597527)

Variable fonts also contain **axes** (*singular noun* axis), which provide a range of property customizations. Standard axes include weight, width, optical size, and slant, but font authors can also provide alternative axes for more style options.

> For example, instead of providing a few predefined properties (such as font weights of 300, 500, and 700), font authors can set a range so that users can apply granular values (so, font weights of 143 or 629 in a range from 100-800).

In this article, we’ll talk about how to replace static fonts with the variable font version, how to change axes, access previous axis settings, and developer handoff.

Check out our [variable fonts page](https://www.figma.com/typography/variable-fonts/) to learn more about axes and how they’re used, and for additional resources.

Note: If you are using the [Figma desktop app](https://help.figma.com/hc/en-us/articles/360039823654), you can use any fonts already on your computer. If you're using Figma in the browser, you can [install the Figma Font Helper](https://help.figma.com/hc/en-us/articles/360039956894#Install_Figma_Font_Helper) to access your installed fonts.

## Replace static fonts with variable fonts

If the font you’re using contains a variable font version, you can replace the static font that you, your team, or your organization has been using with the font’s variable font file.

Keep in mind that when editing in Figma Design, Figma pulls fonts from three different sources: shared fonts, installed fonts, and web fonts (Google fonts) provided by Figma.

If the same font is available from more than one source, Figma will serve fonts in this order of priority:

1. [Shared font uploaded to the organization →](https://help.figma.com/hc/en-us/articles/360039956774)
2. [Fonts installed on your device →](https://help.figma.com/hc/en-us/articles/360039956894)
3. [Default web fonts provided by Figma →](https://help.figma.com/hc/en-us/articles/360039956634)

### Shared fonts (Organization and enterprise plans only)

If the new variable font contains the font families of your previous static font files, then Figma will ask if you want to replace the static font with the variable font.

![Replacing fonts modal.png](https://help.figma.com/hc/article_attachments/31412931098007)

Once you click replace, Figma deletes the old static font from the shared fonts list and uses the variable version. Learn more about [shared fonts](https://help.figma.com/hc/en-us/articles/360039956774-Upload-custom-fonts-to-an-organization).

Note: A font’s variable version might not have the same font styles available as its static versions.

For example, say you want to replace your organization’s static fonts (which include light, regular, bold, and black styles) with the variable font version. However, the variable version includes all styles except bold. In this case, Figma keeps the static font file for bold so it can be used. The rest are replaced by the variable font version.

### Installed fonts

To replace your static fonts with a variable version, be sure to install the variable version to your device. Learn how to [access installed fonts](add-a-font-to-figma-design.md).

If the variable font version contains all the families of your old static fonts, then there are no further steps to take. Figma will automatically prioritize using the variable font over the static ones.

However, if the variable font version is missing any families, you’ll see a missing font dialogue and will need to [choose a replacement style](https://help.figma.com/hc/en-us/articles/360039956994-Manage-missing-fonts).

### Default fonts provided by Figma

If you’ve been using any default fonts, like [Google fonts](http://fonts.google.com), transitioning to the variable font version depends on the font’s latest variable version.

If the variable font version contains all old static styles, then the replacement will be seamless.

However, if the variable font version is missing any families, you’ll see a missing font dialogue and will need to [choose a replacement style](https://help.figma.com/hc/en-us/articles/360039956994-Manage-missing-fonts).

## Use variable fonts

Customize text using variable fonts by changing various axes. The most common options are weight, width, optical size, italic, and slant. The axes of a variable font depend on the author of the font.

You customize your variable font text from the type settings panel.

To access the type settings panel:

1. Select a text layer that is using a variable font.
2. Click  from the right sidebar to open the type settings panel.
3. Click the **Variable** tab.

![Access font variables from the variable tab.png](https://help.figma.com/hc/article_attachments/31412926600343)

From the **Variable** tab you can use the sliders and input boxes to change the values of each axis.

Tip: Hover over an axis in the type settings panel to preview what the property looks like.

### Access frequently used axis settings

Quickly access previous variable font settings you’ve applied to text. These settings are explicit to individual fonts, and Figma lists the most frequently used axis settings.

1. Select one or more text layers using a variable font.
2. Click the  to open the font style drop-down menu.
3. Options are listed just below the font families. Click a setting to apply it to the text.

## View variable font properties in Dev Mode

If you have `can view` access to a file, use the **Properties** tab in the right sidebar to view a text layer's variable font properties.

If you're in Dev Mode, use the **Inspect** tab in the right sidebar to view a text layer's variable font properties and grab its code snippets. Learn more about [inspecting layers](https://help.figma.com/hc/en-us/articles/15023124644247).
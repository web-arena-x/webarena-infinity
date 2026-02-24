# Add a font to Figma Design

Source: https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma-Design

---

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone can add a font to Figma Design

By default, Figma includes [Google fonts](https://fonts.google.com/) and [Apple fonts](https://developer.apple.com/fonts/) in Figma Design files. To use a different font, you can install it on your computer and access it in your Figma Design files.

**Caution**: If you use your own font in a Figma Design file, anyone you share the file with can preview the font. To edit text layers using that font, they will need to install it on their computer. They may see errors related to [managing missing fonts](https://help.figma.com/hc/en-us/articles/360039956994).

Follow the steps below to use your own font in Figma Design:

![Flowchart illustrating steps to use custom fonts in Figma: download, install to font manager, install font helper, and use in Figma.](https://help.figma.com/hc/article_attachments/19825105682327)

1. [Prepare and download the font files](#h_01HHJPRGW7H4ADNAZZM8S2JM0H)
2. [Install the font on your computer](#h_01HHJPRGW7RDGSW1T6FCFYZP29)
3. [Install the Figma font helper (browser only)](#h_01HHJPRGW7HM4KP1G53T9K1G95)
4. [Use your font in a design file](#h_01HHJPRGW7RW3T8X7VP553Y760)

## 1. Prepare and download the font files

Fonts are typically collections of OpenType (.OTF) or TrueType (.TTF) files. Each font can have several styles, and each style has its own file.

For example, using Inter Regular, Inter Bold, and Inter Extra Light requires three font files.

**Tip:** If you're using a font that other people use too, make sure you have the same styles. If someone uses a font style in a file but you don't have that style on your computer, you'll get [a missing font error](https://help.figma.com/hc/en-us/articles/360039956994).

**Note**: Figma only supports .TTF and .OTF font files.

## 2. Install the font on your computer

To use a font, it must be installed in your computer’s font manager.

- On Mac, the font manager is called Font Book. Apple provides guidelines for [installing and validating fonts in Font Book on Mac.](https://support.apple.com/guide/font-book/install-and-validate-fonts-fntbk1000/mac) As a general rule, if you can see your font in Font Book, it’s installed on your computer.
- On Windows, you can install fonts by adding font files to the **Fonts** folder. [Add a font →](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1)

**Note**: Figma doesn't support fonts for devices running ChromeOS or Linux. Chromebook and Linux users can only use Google fonts and available Apple fonts (SF Pro and SF Compact), which are the default fonts in Figma.

## 3. Install the Figma font helper

**Note**: If you're using the desktop app, you can skip this step. The desktop app includes the Figma font helper.

If you use Figma in your web browser, you need to install the Figma installer, otherwise known as the font helper, before you can add your own font to Figma Design files.

[Download the Figma font installer](https://www.figma.com/downloads/)

After installation, **reload any open files in your browser** to start using your font.

**Note**: The Figma font installer, FigmaAgent, runs an HTTP and HTTPS server on [localhost](https://en.wikipedia.org/wiki/Localhost). It only allows connections from `figma.com` and isn't exposed to the public internet.

You may see events related to the FigmaAgent in your console log or when monitoring activity on your computer. The loopback address for localhost resolves to `127.0.0.1`.

You can always [uninstall the font helper](https://help.figma.com/hc/en-us/articles/19764441960599) if you need to.

## 4. Use your font in a design file

![Font selector dropdown showing "Installed by you" filter with "Inter" highlighted in Figma's typography panel.](https://help.figma.com/hc/article_attachments/26982310211479)

To find and use your font:

1. From a Figma Design file, select or create a text layer.
2. Open the font selector in the right sidebar.
3. Open the filter dropdown and choose **Installed by you**.

**Tip**: Learn more about [browsing and applying fonts in your files](https://help.figma.com/hc/en-us/articles/360041308034)

**Note**: Got stuck? Check out our guide to [troubleshooting font issues →](https://help.figma.com/hc/en-us/sections/19818416478487)
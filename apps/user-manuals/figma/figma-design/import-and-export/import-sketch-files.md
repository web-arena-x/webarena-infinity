# Import Sketch files

Source: https://help.figma.com/hc/en-us/articles/360040514273-Import-Sketch-files

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone can import Sketch files to their drafts

Anyone with `can edit` access to a team can import Sketch files to that team

You can import Sketch files (.sketch) into Figma. When you import a file, it is converted to a Figma Design file and any further changes made to the original file in Sketch will not be reflected in Figma.

**Note** If you’re using a beta version of Sketch, there may be discrepancies with how assets are imported into Figma. We recommend saving files using the latest version of Sketch before importing them to Figma.

If you only want to import individual assets from Sketch, you can also copy and paste the asset into a design file. Learn more about [copying assets between design tools →](https://help.figma.com/hc/en-us/articles/360040030374)

## How Sketch features are converted in Figma

After importing a Sketch file, you’ll notice that existing Sketch features will have been converted to Figma features.

**New to using Figma?** Learn more about what to [expect when moving from Sketch to Figma →](https://www.figma.com/best-practices/what-to-expect-when-moving-from-sketch-to-figma/#sketch-import)

### Artboards

Any artboards in the Sketch file will be converted to frames in Figma. Like artboards, frames are used to contain content but include some additional functionality. Learn more about [working with frames →](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma)

### Pages

Like Sketch, Figma supports having multiple pages within a single design file. Any page that exists in your Sketch file will be imported as a separate page within the design file.

You can navigate between pages using the Layers panel in the left sidebar. Learn more about [using the Layers panel →](https://help.figma.com/hc/en-us/articles/360039831974)

### Symbols and libraries

When you import a Sketch file into Figma, any symbols included in the original file are converted to components in Figma. The Symbols page in the Sketch file will be imported into Figma as a page named “Symbols” that contains your main components. Learn more about [working with components →](../components/guide-to-components-in-figma.md)

When you import a symbol library from Sketch, it is imported as a design file, not a library. If you’re on a paid plan, you can publish the components to a library after importing. This allows you to use the components across multiple design files. Learn more about [publishing libraries →](../create-and-share-libraries/publish-a-library.md)

Note: If you a import Sketch file that includes symbol instances, you’ll need to reconnect those instances to the main component after publishing the symbols to a library. You can do this either by [swapping individual components](360039150413-Swap-components-and-instances) or by [performing a library swap](../use-libraries/swap-style-and-component-libraries.md).

### Fonts

If your Sketch file uses fonts stored on your computer, you will need to make those fonts available in Figma. If you’re using the [Figma desktop app](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app), these fonts are accessible by default. If you’re using Figma in the browser, you’ll need to download the [Figma font installer](https://www.figma.com/downloads/) to access them. Learn more about [accessing fonts on your computer →](https://help.figma.com/hc/en-us/articles/360039956894)

If you receive a “Missing fonts” error message after importing a Sketch file, you’ll be prompted to update any affected text layers. Learn more about [managing missing fonts →](https://help.figma.com/hc/en-us/articles/360039956994)

Note: Figma does not support fonts installed on devices running ChromeOS or Linux. Organization admins can upload custom fonts for members of the organization to use. Learn more about [uploading custom fonts to an organization →](https://help.figma.com/hc/en-us/articles/360039956774-Upload-custom-fonts-to-an-organization)

### Styles

Styles are not retained during the import process. You will need to recreate any styles you used in Sketch after the file has been imported. Learn more about [creating styles →](https://help.figma.com/hc/en-us/articles/360038746534)

## Import a Sketch file

You can import a Sketch file using the file browser or the editor.

Note: Attempting to import very large Sketch files may result in a failed import. To prevent this, consider splitting up the Sketch file into smaller files before importing.

### Import a Sketch file using the file browser

![Dropdown menu in Figma file browser highlighting Import option under Create new for importing Sketch files.](https://help.figma.com/hc/article_attachments/31411207657495)

1. From the [file browser](https://help.figma.com/hc/en-us/articles/14381406380183), click **Create** > **Import** at the top-right of the page.
2. Click **From your computer**.
3. Select the Sketch file you want to import and click **Open**. Depending on the file size, the import process may take a few moments.
4. Click **Done**.

Note: You can also drag and drop files from your computer to import them to the file browser.

### Import a Sketch file from a Figma Design file

1. Click  **Main menu**.
2. Select **File** > **New from Sketch file**.
3. Select a .sketch file and click **Open**.
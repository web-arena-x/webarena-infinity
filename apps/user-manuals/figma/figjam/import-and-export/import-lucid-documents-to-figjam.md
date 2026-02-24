# Import Lucid documents to FigJam

Source: https://help.figma.com/hc/en-us/articles/24170628689047-Import-Lucid-documents-to-FigJam

---

Who can use this feature

- Available on any [team or plan](https://help.figma.com/hc/en-us/articles/360040328273)
- Anyone with **can edit** access in a FigJam file can import a Lucid document.
- Anyone can export documents from a Lucid document.
- Check out the [FigJam migration guide →](https://www.figma.com/community/file/1199813514105456242/figjam-migration-guide)

You can import the contents of a Lucid document into FigJam. After importing, you’ll be able to edit text as well as move and resize objects.

Tip:

There isn't a way to export boards in bulk from Lucid. To find the most relevant boards to export, sort and filter boards in your Lucid dashboard by date created, viewed, or updated.

## Export from Lucid

To export all or part of a board from Lucid:

1. Open the Lucidchart or Lucidspark document you want to export.
2. [Follow Lucid's steps for exporting content as an image →](https://help.lucid.co/hc/en-us/articles/16324571257492-Export-or-print-a-Lucid-document#export-as-jpg-svg-png-pdf)
3. From the File format menu, choose PDF
4. Select the content you want to export. If the document contains multiple pages, you can select any/all pages to be exported together. Multi-page documents will all be imported into the same FigJam document.
5. Click Download. Your image will save to your computer as a PDF file.

Note

Lucid also allows you to select objects in the document, right click, and **Export selection**. FigJam **does not support** PDF content exported using this process.

**[Learn more about exporting Lucid documents as images →](https://help.lucid.co/hc/en-us/articles/16324571257492-Export-or-print-a-Lucid-document#export-as-jpg-svg-png-pdf)**

## Import Lucid content to FigJam

After exporting content from Lucid, you can:

- [Create a new FigJam file from the Lucid PDF](#h_01G6K0ZXY108AQJ78DMHX8CVY4)
- [Import the content into an existing FigJam file](#h_01G6K108HYD53K5JJC1G8YWVAE)

### Create a new FigJam file

1. Open the Figma file browser.
2. From Recents, Drafts, or a project, click Import at the top right of the page.
3. Click Import from computer.
4. Select one or more Lucid PDF files to import.
5. Select Lucid on the Where are your files from? screen and click Confirm.
6. Click Done once the import is complete.

**Tip:** You can also drag and drop one or more Lucid PDF files into the Figma file browser. Figma will create a new FigJam file for each PDF.

### Import into an existing FigJam file

1. Open a FigJam file.
2. Click the Figma icon at the top left of the file.
3. Navigate to **File > Import.**
4. Select Lucid on the Where are your files from? screen and click Confirm.
5. Select one or more Lucid PDF files.

**Tip:** You can also drag and drop one or more Lucid PDF files straight into the FigJam canvas. Each Lucid PDF will get imported into the open FigJam file.

## How Lucid objects map to FigJam

The following table explains how a Lucid object gets imported into FigJam.

| | |
| --- | --- |
| Lucid object | FigJam |
| Sticky note | Shape with text |
| Text | Text |
| Mind map | Shapes, connectors, and text |
| Shape | Shape |
| Image | Image |
| Table | Text and shapes |
| Frames and Containers | Shapes and text |
| iframe object (embedded URLs and videos) | Hyperlinked text with the source URL |
| GIF | Images |
| Icon | Shapes and images |
| Comment | Not supported |
| Line | Connectors |
| Pen, highlighter | Lines and shapes |
| Card | Shapes and text |
| Voting | Not supported |
| Uploaded files (Videos, PDFs, documents, etc.) | Not supported |
| Visual activity | Not supported |
| Quick tools | Not supported |

**Note**: FigJam currently does not support importing:

- Connectors with text are migrated as images and text
- Right-to-left text is not supported
- Text with italics is not supported, and will be migrated as regular text
- Bulleted lists in stickies are not supported
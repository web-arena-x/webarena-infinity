# How can I improve the accuracy of OCR on my drawings? - Procore

Source: https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-ocr-on-my-drawings

---

When you upload new drawings to a project, Procore can automatically populate the Title, Number, and Discipline fields using Optical Character Recognition (OCR) technology to help expedite the upload and review process. See [Which fields can Procore automatically populate when uploading drawings?](https://support.procore.com/faq/which-fields-can-procore-automatically-populate-when-uploading-drawings "Which fields can Procore automatically populate when uploading drawings?")

In order to improve the accuracy of this character recognition technology, we recommend you configure your drawings based on the following guidelines. 
*Note:* Click a link below to view guidelines for that topic.

- [Drawing Format](#Drawing_Format "How can I improve the accuracy of OCR on my drawings?")
- [Drawing Block Location](#Drawing_Block_Location "How can I improve the accuracy of OCR on my drawings?")
- [Drawing Block Text](#Drawing_Block_Text "How can I improve the accuracy of OCR on my drawings?")
- [Drawing Callouts](#Drawing_Callouts "How can I improve the accuracy of OCR on my drawings?")

#### Drawing Format

- Drawings must be in PDF format.
- PDFs should contain all vector format.
- Drawings should be in landscape orientation.
- Important notes for AutoCAD users:
 - In order to create selectable and searchable text in a PDF from AutoCAD:
    - Use a TrueType font.
    - Do not alter the text from the original font, such as changing width (must be 1.0) or other style options.
    - Make sure the Z coordinate value of the text is zero.
 - AutoCAD users should turn off the "text as comments" feature before publishing a PDF for use in Procore. Exporting your drawings as a PDF with this feature enabled could impact Procore Drawings tool OCR. 
    *Note*: To turn off the feature, navigate to the command line in AutoCAD. Enter **EPDFSHX** and change the value to zero (**0**). See [Drawing text appears as comments in a PDF created by AutoCAD](http://knowledge.autodesk.com/support/autocad/troubleshooting/caas/sfdcarticles/sfdcarticles/Drawing-text-appears-as-Comments-in-a-PDF-created-by-AutoCAD.html "http://knowledge.autodesk.com/support/autocad/troubleshooting/caas/sfdcarticles/sfdcarticles/Drawing-text-appears-as-Comments-in-a-PDF-created-by-AutoCAD.html").

#### Drawing Block Location

- Make sure the drawing number is located in the bottom right corner with the title nearby.

![ideal drawing block location.png](https://support.procore.com/@api/deki/files/6703/ideal_drawing_block_location.png?revision=1&size=bestfit&width=450&height=378)

#### Drawing Block Text

- **Format:**
 - Use labels for the drawing title and drawing number (e.g. 'Sheet Title:' and 'Sheet Number:')
 - The drawing number and title should be larger than other text in the title block.
 - Use a simple Sans-Serif font, such as Arial or Helvetica (or any UTF8 font).
 - Text is best horizontal. However, the title can be vertical.
 - It is recommended to embed fonts in your PDF files while saving them so that they display as expected when opened in other programs.
- **Title:**
 - Try to have the title as one line when possible.
 - Titles should be less than 255 characters.
 - OCR only recognizes words from English, Spanish, French, and German dictionaries.
- **Number:**
 - Place the drawing number in the bottom right with the title nearby.
 - Do not use spelled out words in the Number. (e.g. 'Drawing Number One')

![ideal drawing block text.png](https://support.procore.com/@api/deki/files/6702/ideal_drawing_block_text.png?revision=1&size=bestfit&width=304&height=280)

#### Drawing Callouts

- See [Why are automatic drawing sheet links missing?](https://support.procore.com/faq/why-are-automatic-drawing-sheet-links-missing "faq/why-are-automatic-drawing-sheet-links-missing")

## See Also

- [Which fields can Procore automatically populate when uploading drawings?](https://support.procore.com/faq/which-fields-can-procore-automatically-populate-when-uploading-drawings "Which fields can Procore automatically populate when uploading drawings?")
- [How can I improve the accuracy of Specification Section Identification?](https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-specification-section-identification "How can I improve the accuracy of Specification Section Identification?")
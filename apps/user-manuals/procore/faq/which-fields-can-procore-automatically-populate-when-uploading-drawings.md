# Which fields can Procore automatically populate when uploading drawings? - Procore

Source: https://support.procore.com/faq/which-fields-can-procore-automatically-populate-when-uploading-drawings

---

## Answer

When you upload new drawings to a project, Procore can automatically populate the following fields using [Optical Character Recognition (OCR)](http://en.wikipedia.org/wiki/Optical_character_recognition) technology to help expedite the upload and review process:

- **Drawing Number**: Pulls directly from the number listed on drawing sheet.
- **Drawing Title**: Pulls directly from title block on drawing sheet.  
  *Note:* If you are uploading a drawing revision, Procore will populate the drawing title based off the information entered on the previous drawing revision.
- **Drawing Discipline**: Populates based on the drawing number's letter prefix.  
  *Note:* You can set which letters designate which disciplines. See [Configure Default Drawing Disciplines](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/configure-default-drawing-disciplines "Configure Default Drawing Disciplines").

![drawings-auto-populate.png](https://support.procore.com/@api/deki/files/88188/drawings-auto-populate.png?revision=2)

For example, if you upload a PDF with 'A123' as its drawing number and "SECOND FLOOR - REFLECTED CEILING PLAN" as the title, Procore will automatically recognize each of those fields, fill the number in the number field, the title in the Title field, and use the prefix of the number to populate the Discipline field with "Architecture".

*Note:* If you correct an auto-filled value, you will be prompted to have the system reevaluate the remaining drawings where it will dynamically re-adjust its auto-detection algorithm accordingly (see image below).

![readjust-numbers.png](https://support.procore.com/@api/deki/files/88189/readjust-numbers.png?revision=1)

## See Also

- [How can I improve the accuracy of OCR on my drawings?](https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-ocr-on-my-drawings "How can I improve the accuracy of OCR on my drawings?")
- [How can I improve the accuracy of Specification Section Identification?](https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-specification-section-identification "How can I improve the accuracy of Specification Section Identification?")
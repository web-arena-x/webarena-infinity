# Automatic Drawing Sheet Linking - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/automatic-drawing-sheet-linking

---

## Overview

![drawing sheet linking2.png](https://support.procore.com/@api/deki/files/6447/drawing_sheet_linking2.png?revision=1&size=bestfit&width=395&height=342)﻿Drawing sheet links make it easier for users to quickly navigate between related drawing sheets.  
  
Procore leverages [Optical Character Recognition﻿ (OCR)](http://en.wikipedia.org/wiki/Optical_character_recognition "http://en.wikipedia.org/wiki/Optical_character_recognition") technology to intelligently scan a drawing for shapes and characters that are most likely callouts that reference section cuts, other drawings, or even of the drawing itself. Procore will attempt to decipher the drawing sheet number of a callout and create a link to the related drawing if an existing drawing can be found with the same drawing number, which is why it's important to use drawing sheet numbers that match the detailed callouts as much as possible.

Procore always recommends that you upload drawings with vector callouts that are unflattened and not scanned because accuracy in identifying callouts is increased in vector-based files.

See [What is the difference between raster and vector content in PDFs?](https://support.procore.com/faq/what-is-the-difference-between-raster-and-vector-content-in-pdfs "What is the difference between raster and vector content in PDFs?") Procore handles vector and raster-based files differently.

#####

### Vector PDFs

- Procore can reliably find drawing numbers as long as it is vector text, inside, or outside of a circle callout symbol. Procore also attempts to partially match drawing numbers.   
  *Note:* Procore will hyperlink alphanumerics, but not one or two digit numbers. For example, a drawing number of A-1 would be linked, while a drawing number of 55 would not.
- Procore will not ignore spaces, dots or dashes when matching for hyperlinks. For example, a drawing number of A-100 would not get a hyperlink on a callout that said A100, A 100, A - 100, A.100, or A   100.
- If a drawing is recognized as vector, then Procore will be able to read the vector text easily. For example, Procore might confuse an ’S’ for a ‘5’ in a raster file.
- If the callout is recognized as vector, Procore will draw a turquoise **rectangle** around the drawing number.

### Raster PDFs

- In raster PDFs, Procore will only recognize a callout if the drawing number appears in a circle callout symbol.
- Raster PDFs are harder to read, and accuracy is reduced by visual noise and interference, or low quality pdfs or unusual fonts. See [Why are automatic drawing sheet links missing?](https://support.procore.com/faq/why-are-automatic-drawing-sheet-links-missing "Why are automatic drawing sheet links missing?") for common troubleshooting solutions for raster files.
- Procore will ignore spaces, dots, and dashes when matching for hyperlinks on raster drawings. For example, a drawing number of A-100 would get a hyperlink on a callout that said A100, A 100, A - 100, A-100, A.100, and A   100.
- If a drawing is recognized as raster or flattened, Procore will draw a **circle** around the callout to try to match the exact size of the circle symbol around it.

### Three Types of Callouts that Procore Automatically Links To:

1. **Detail Callouts**: Detail callouts reference a closer view of a smaller aspect of a project.  
   ![detailcallout.png](https://support.procore.com/@api/deki/files/9074/detailcallout.png?revision=1&size=bestfit&width=58&height=53)
2. **Section Cut Callouts**: Section callouts are usually shown on a floor plan and reference a vertical 2-D view of a building, from the perspective of where the callout is located.   
   ![sectioncut.png](https://support.procore.com/@api/deki/files/9075/sectioncut.png?revision=1&size=bestfit&width=87&height=83)
3. **Elevation Callouts**: Elevation callouts reference a 2-D view of the building, and can show either the interior or exterior view.   
   ![elevationcallout.png](https://support.procore.com/@api/deki/files/9076/elevationcallout.png?revision=1&size=bestfit&width=73&height=63)

## Things to Consider

- There is no guarantee that every callout will automatically ﻿be converted into a drawing sheet link when you upload new drawings.
- Drawing sheet links will typically appear within a few minutes after you have finished reviewing and publishing the uploaded drawings. However, processing time can vary depending on how many drawing sheets are currently being uploaded to Procore. During peak upload times, it may take over 45 minutes for drawings to be fully processed.
- Currently, there is no way to determine whether or not a drawing sheet was fully processed. If you view a drawing and do not see any drawing sheet links, Procore's servers might still be processing your drawing or perhaps it might have already been processed.
- It's recommended that you perform a small test of your drawings to see if the image processing application is able to properly identify and add sheet links to your drawings. Upload a few sample drawings before uploading entire drawing sets.
- There may be several reasons why the image processing application is unable to create sheet links on your drawings. Please see, [Why are Automatic Drawing Sheet Links Missing?](https://support.procore.com/faq/why-are-automatic-drawing-sheet-links-missing "Why are automatic drawing sheet links missing?")
- Once files are uploaded, you can still use the [**Markup Toolbar**](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/mark-up-a-drawing "Mark Up a Drawing") to add links manually.
- Automatic drawing sheet links will not be applied to drawings that were uploaded prior to Oct. 14, 2014.
- Y﻿ou do not have to upload all related drawings at the same time in order for automatic sheet linking to occur. In fact, if you upload related drawings at a later time, drawing sheet links will automatically be added to link to the current version of that drawing. This does not work in reverse; no drawing sheet links will be added from the older drawings to the newly uploaded drawing.

### Tips for Getting Automatic Sheet Linking to Work as Expected on Raster Drawings

There are several best practices that you can follow that will increase the likelihood that automatic drawing sheet links are applied to your uploaded drawings.

- When you review and publish your drawings, name the "Drawing #" so that it matches the exact drawing number in the drawing's section callouts. For example, if the section cut says "A1500" you should name the drawing appropriately with matching upper/lower case characters.
- Make sure section callouts use standard sans-serif fonts (e.g. Arial) to prevent character confusion﻿; it's difficult to decipher serif fonts (e.g. Times New Roman)

For tips as to why your drawing sheet links might not be working, see [Why are automatic drawing sheet links missing?](https://support.procore.com/faq/why-are-automatic-drawing-sheet-links-missing "Why are automatic drawing sheet links missing?")

## See Also

- [Add a Link to a Drawing](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/add-a-link-to-a-drawing "Add a Link to a Drawing")
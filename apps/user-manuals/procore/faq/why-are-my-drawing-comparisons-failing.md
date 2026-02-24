# Why are my drawing comparisons failing? - Procore

Source: https://support.procore.com/faq/why-are-my-drawing-comparisons-failing

---

## Background

| | |
| --- | --- |
| A powerful feature in Procore is the ability to compare different drawing revisions to view any changes. Any additions to a drawing are highlighted in green while deletions are highlighted in red (as shown in the screenshot to the right). | drawing-comparison-example.png |

| | |
| --- | --- |
| drawing-comparison-example-failed.png | There are a few things to consider before you upload a drawing revision to ensure that the comparison tool can accurately diagnose and highlight changes to your drawings. Please follow these recommended best practices:   1. Make sure the drawing is the same size as its previously uploaded revision. 2. Make sure the architect didn't accidentally shift the whole drawing a few pixels, which would cause the entire drawing to be highlighted as a change (as shown in the screenshot to the left). |

## Answer

Your drawing revision comparison may fail if any of the following factors are true.

1. **The drawings are different sizes**
   - Example: If a drawing is downloaded from Procore, edited in a third party PDF editor (that's different than what was used to create the original PDF), and then uploaded back into Procore, it's likely that the size/scale of the new PDF is different than the previously uploaded revision. In such cases, the comparison tool might highlight the entire drawing as a modification.
   - Solution: If possible, always use the same software to generate drawing revisions. In some cases, you may need to ask the architect to create all drawing revisions in order to preserve the same drawing size/scale across all revisions. If  the same software cannot be used to create drawing revisions, you may need to delete and replace the original drawing with one from the sofware application that will be used to generate all future drawing revisions.
2. **The drawing was slightly shifted or offset in some direction**
   - Example: If you or the design team edited the PDF and shifted any part of the drawing (even if it's only been shifted just a few pixels), the comparison tool might highlight the entire drawing as a change.
   - Solution: Always be careful when editing drawings. Be sure to check the dimensions and placement of the drawing when you save changes and create a new PDF.
3. **Poor Resolution or Image Quality**
   - Example: The original source (PDF) file cannot be found or you scan a drawing because it has markups directly on the printed version that you want to preserve. Scanned versions will typically have lower quality or resolution than the original files. As a result, the comparison tool might have a hard time distinguishing unchanged elements because of degraded image quality.
   - Solution: Transfer the on-print markups in Procore using the Drawing's markup tool.

## See Also

- [Compare Drawing Revisions](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/compare-drawing-revisions "Compare Drawing Revisions")

## 

If you would like to learn more about Procore's construction drawings software and how it can help your business, please visit our [construction drawing management software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/drawings "https://www.procore.com/project-management/drawings").
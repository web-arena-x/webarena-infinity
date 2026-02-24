# What is the difference between raster and vector content in PDFs? - Procore

Source: https://support.procore.com/faq/what-is-the-difference-between-raster-and-vector-content-in-pdfs

---

## Answer

There are two types of PDF content: raster, and vector. Vector content is preferred for use with Procore.

### Vector (Preferred)

Vector content is based on a mathematical model that creates connections between a series of points, and then displays the connections between those points on your screen.

Procore's OCR and text parsing technology was built for this kind of content, and can easily identify text and shapes in a vector-based PDF. Vector content leads to the most accurate and complete results when using tools like Drawings, Specifications, or Search.

It's a good idea to ask anyone who's responsible for creating PDF files that will be uploaded to Procore to make sure those files are saved as vector PDFs.

### Raster

Raster files are kind of like image files. They consist of a series of pixels that are a static grid of colored squares, not actual lines or letters. Procore's OCR and text parsing technology might attempt to read this type of content, but often won't be successful.

If you've received a raster-based PDF, contact the creator of the file and ask them to save the original content as a vector-based PDF.

### How do I know if a PDF file is raster-based or Vector-based?

- Open the file and try to highlight text with your mouse.

 - If you can NOT highlight the text, the content is raster.
 - If you CAN highlight the text, the content is vector.
 - If you can't highlight only some of the text, the content might be a mix of raster and vector.
- Zoom in on the PDF.

 - If the image or text gets blurry or pixilated, it is a raster file.
 - If the image and text remain sharp, it is a vector file.
- Was the file scanned to your computer?

 - Scanned files are always raster files.

## See Also

- [How can I improve the accuracy of OCR on my drawings?](https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-ocr-on-my-drawings "How can I improve the accuracy of OCR on my drawings?")
- [How can I improve the accuracy of Specification Section Identification?](https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-specification-section-identification "How can I improve the accuracy of Specification Section Identification?")
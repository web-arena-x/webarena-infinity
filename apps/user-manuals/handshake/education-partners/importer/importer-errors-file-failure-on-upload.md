# Importer Errors: File Failure on Upload

Source: https://support.joinhandshake.com/hc/en-us/articles/227601827-Importer-Errors-File-Failure-on-Upload

---

**If you see the following analysis error after submitting your file to the Importer:**

     A system error occurred while running this static analysis.

![](https://support.joinhandshake.com/hc/article_attachments/25995122332567)

**What does this error mean?**

This could be due to:

- **Additional columns/commas in the file that have no entries**

- The easiest way to check this is by right-clicking the file and opening it in a text editor

- *An example of what you may see:*![](https://support.joinhandshake.com/hc/article_attachments/25995103724695)
- Note that if there are trailing commas [creating additional columns] this is generally affected throughout the file and must be corrected

- If it's occurring for your automated sync, you may have to contact your IT department to have it corrected
- If it's occurring in a one-off file (that is not sent through AWS), a quick way to resolve this is by going into excel and highlighting the "empty columns" to the right - remove them by right-clicking and delete

- **The file is not a true .CSV**

- **See:** [CSV Rules and Requirements](https://support.joinhandshake.com/hc/en-us/articles/226346508-CSV-Rules-and-File-Requirements)
- You can check this by typing in your command line prompt:

- $file filenamehere.csv
- use a file viewer

- **File contains line breaks or new lines that are causing an issue (CRLF terminators)**

**Once you have addressed this error and made any necessary file formatting adjustments, you can resubmit your file for processing!**
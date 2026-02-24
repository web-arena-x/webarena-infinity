# Importer App: CSV Rules and File Requirements

Source: https://support.joinhandshake.com/hc/en-us/articles/226346508-Importer-App-CSV-Rules-and-File-Requirements

---

To successfully upload a file via the Importer, the file must follow a strict set of requirements. These requirments include:

- A file size *less* than 50MB. If larger, you'll need to split it into separate files of 50MB or smaller.
- All headers consisting of down-cased text, as the Importer is case-sensitive.
- All preset values for each field being case-sensitive; casing will vary by each type of upload.
- File *must be* exported in a true .CSV format.
- File *may not* be another file type with a .CSV extension added to it.
- File *must be* exported in Unicode (UTF-8).
- *All dates must be in yyyy-mm-dd format, unless otherwise specified in the UI***.**
  - For more information, refer to [Importer: Date Formatting](https://support.joinhandshake.com/hc/en-us/articles/231942648).

**Important**: if you don't use UTF-8 format, it can cause bad encoding issues, which can lead to poorly translated records or failure to sync/import correctly.

### Possible Errors

- "*There are characters we could not recogonize. Please fix these characters manually or convert your file to UTF-8 and re-upload to try again"* indicates the file contains invalid characters that aren't in UTF-8 format - You'll need to convert your file to a UTF-8 to upload.

![UTF8_errors.png](https://support.joinhandshake.com/hc/article_attachments/8591499688343)

- "*File name is invalid, File is invalid, File content typse is invalid*" indicates the file wasn't saved as a .CSV - You'll need to convert your file to a .CSV to upload.

![File_not_saved_in_correct_format.png](https://support.joinhandshake.com/hc/article_attachments/8591631804311)

- "A system error occured while running this static analysis. Invalid byte sequence in UTF-8" indicates a non UTF-8 CSV file formating issue - You'll need to ensure all fomatting requirements are correct to upload.

![Other_format_error.png](https://support.joinhandshake.com/hc/article_attachments/8591697287447)

### Converting an Excel File to UTF-8

If you are using Excel, you can choose "CSV UTF-8" to ensure you have the proper formatting. Follow these steps to convert your file:

- Click **File**, then **Save as** from the menu.
- In the 'Save as type' dropdown > select 'CSV UTF-8 (Comma delimited) (.csv)'
- Select 'Web Options' in the 'Tools...' dropdown at the bottom of the dialog box.
- Select the 'Encoding' tab.
- In the ‘Save this document as:’ dropdown, select ‘US-ASCII’

![](/attachments/token/wg6J6H88alDvmoHLcDBy9ngOE/?name=inline466209979.png)

![](/attachments/token/R8PHNEeao7x65suQ1IAbZGTWu/?name=inline-1587694321.png)

For more information on how to export a file to a UTF-8, refer to this external document: <https://docs.moodle.org/24/en/Converting_files_to_UTF-8>

#### 

### Tips

- If you're unsure of the details in your file, you may use your command prompt to return some detail: $*file filename.ext* (e.g. $*file users.csv*)
- Additionally, you may either view the file in a text editor or use a tool like the 'File Viewer'.
- If you are still having issues, please reach out to contact us.
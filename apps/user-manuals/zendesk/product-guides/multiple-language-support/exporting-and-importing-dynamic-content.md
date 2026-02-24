# Exporting and importing dynamic content

Source: https://support.zendesk.com/hc/en-us/articles/4408894053530-Exporting-and-importing-dynamic-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

To streamline the translation of your dynamic content, you can easily export the
content as CSV (comma separated values) files that you can send off to a
translation agency and then import the translated files back into your
Zendesk. You can do this when first creating the dynamic content and any
time you need to update the content thereafter.

An excellent way to manage your dynamic content translation is to first create
all the dynamic content in your default language and then export the files.
The export creates separate files for each of the languages you support in
your Zendesk. Your translation agency can add all the translated content
into the files and when you import the files back into your Zendesk the
language variants will be created automatically for you. In other words,
there's no need to manually create language variants in your Zendesk if
you're sending the export files out for translation.

Note: Before exporting and importing your files, you must first create
dynamic content items in your Zendesk account. For information on
creating dynamic content items see, [Providing multiple language support with
dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content-Professional-and-Enterprise-#topic_qcy_eci_je).

## Exporting dynamic content for translation

You can quickly export all of your dynamic content into CSV files that you can send out for
translation and then import back into your Zendesk when the translations are complete.

The export process creates separate CSV files for every language that you support. For
example, if your default language is English and you also support French and German, the
export generates the following three files:

- en-US.csv
- fr.csv
- de.csv

The CSV files are contained in a zip file.

**To export your dynamic content**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. In the **Import & Export** section, select **Export content**.
3. Click **Export**. When the export is complete, you'll receive an email containing a
   link from which you can download the zip file.

   Note: You can export your dynamic content
   once in a 15 minute period. Additional requests to export the content within that
   period return results for the first request you made. After 15 minutes, the export
   will reflect any changes you made to the content since the first export
   request.

Each file contains all of your dynamic content in the default language in which you created
them (in this example, English). Here's an example of the French CSV (fr.csv) file.

```
"Title","Default language","Default text","fr text","Variant status"
"Agent signature","English","The MondoCam Support Team","",""
"Welcome message","English","Welcome to MondoCam Customer Service!","",""
```

The first row of the CSV file is the header row, which contains the names of the data
contained in the file: title, the default language, the default text of the dynamic content,
the variant's language, and the status.

The CSV file can be opened in a text editor, a spreadsheet application such as Microsoft
Excel or OpenOffice.org Calc, or imported into some other translation system so that the
French translations can be added. The translators add the text in the 'fr text' column and
then send the CSV file back so that you can import it into your Zendesk.

Note: The CSV files are exported in the UTF-8 format, and you must import the files back into your
Zendesk in the same format. If you're importing CSV files to
Microsoft Excel, make sure to use Excel's **Get Data**
command. If you try to open the CSV in Excel as normal, the
import fails.

```
"Title","Default language","Default text","fr text","Variant status"
"Agent signature","English","The MondoCam Support Team","Toute l'équipe du Support MondoCam",""
"Welcome message","English","Welcome to MondoCam Customer Service!","Bienvenue au support de MondoCam",""
```

The identifier for each dynamic content item is its title. When you import the file, the
title is matched to the existing dynamic content item and the translations are added as
language variants.

## Importing the translated CSV files

After your CSV files have been translated, you can import them back into your Zendesk.

**To import dynamic content**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. In the **Import & Export** selection, select **Import content**.
3. You can either choose the CSV file you want to import or paste the CSV data in
   directly.
   - To import a CSV file, select **Choose File**.
   - To paste in the CSV data, select **Let me paste in data instead**.
4. Click **Import**. You'll receive an email when the import is complete.

If your CSV file is properly formatted and is in the UTF-8 format, your import will be
successful. If the import fails, you'll receive an email describing the errors that
occurred.

While importing a CSV file is a straightforward process, there are some details about
importing this content that you'll want to be aware of.

- Even though the CSV file contains the status, you cannot set the status via the
  import. If you manually change the status in the import CSV file, your changes will be
  ignored.
- If you import content for a variant that does not exist (but the language is supported
  in your Zendesk), the variant will automatically be added and its status set to Active.
- The only data that is required (in fact, the only data that is imported from the CSV
  file) is the title and the language text. Therefore, you can import variant translations
  using a CSV file in this
  format:

  ```
  "Title","fr text"
  "Agent signature","Toute l'équipe du Support MondoCam"
  "Welcome message","Bienvenue au support de MondoCam"
  ```
- If the language text in a variant is blank or is just spaces (in other words, no valid
  text) then the variant content is not added. However, all other valid entries in the
  file will be added.
- If an error occurs during the import, the import will fail and you'll receive an email
  message with the error details.
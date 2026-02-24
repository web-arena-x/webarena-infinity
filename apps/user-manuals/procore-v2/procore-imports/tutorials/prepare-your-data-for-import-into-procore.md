# Prepare Your Data for Import into Procore

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-your-data-for-import-into-procore

---

***IMPORTANT!*** In order to protect the integrity of your companyâs data, Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. This restriction applies to all data modifications, including correcting typographical errors. If Procore determines that errors are present in any Procore Import Template that you submit to Procore, it will be returned to you for correction. **Please note that the import process may take up to 72 hours to process.**

## Background

You can import a wide variety of data into Procore, which lets you control how your data will be populated in various tools. Each tool has different data requirements. Typically, most tools require your data to be properly formatted as a Microsoft Excel Open XML (XLSX) or Comma Separated Values CSV file.

### General Import Considerations

Before starting the import process, its important to take a few preliminary steps to make sure your XLSX or CSV file is properly formatted. This ensures that the import process is completed successfully.

- **Considerations for Row Data:**

  - Each row in the table corresponds to an individual record. There is no limit to the number of rows you can import. However, rows must not be blank.
  - Each row must include the information specified in the import template for each column header.
  - Remove all special/hidden characters and text from the file. If you used a cut-and-paste operation to move data between Microsoft Word and Excel, you may have inadvertently pasted hidden characters and text into your file. This can interfere with the import process and often leads to import errors.\* **'** (single quote)\* **"** (double quote)\* 1/2 (forward slash)\* **-** (dash)\* **,** (comma)
  - To avoid import errors, clean your file before submitting it to Procore. To clean your file, first copy-and-paste your spreadsheet data into Notepad. Next, copy the text in Notepad and then paste it into the XLSX or CSV template. Ensure that data is pasted into the appropriate column order.
- **Considerations for Column Data**:

  - See [Procore Import Templates](/reference-procore-import-templates) for the appropriate template and tutorial steps for each tool.
- **If the import must be performed by Procore:**

  - You must submit a completed import template to Procore in XLSX or CSV format. See [Procore Import Templates](/reference-procore-import-templates) for details.
  - Before an import is performed, Procore ensures that your template is converted to the required CSV (UTF-8) format.
  - You must input your user data using the column headers and column order defined in the template. To avoid import errors, do NOT add blank columns and do NOT add new data columns.

##### Â Note

If you are importing line items to the Client Contracts, Commitments, Direct Costs, Funding, or Prime Contracts tools, Procore users have the option to choose the character used as a delimiter. A *delimiter* is a character used to separate values or text strings. It marks both the beginning and end of a unit of data. This supports Procore clients who work in regions where a comma (,) is used to represent a decimal symbol and the list separator is generally set to a semicolon (;). To learn more see one of these tutorials:

- [Import Commitment SOV Line Items from a CSV File](/product-manuals/commitments-project/tutorials/import-commitment-sov-line-items-from-a-csv-file)
- [Import Direct Costs](/product-manuals/direct-costs-project/tutorials/import-direct-costs)
- [Import a Prime Contract SOV from a CSV File](/product-manuals/prime-contracts-project/tutorials/import-a-prime-contract-sov-from-a-csv-file)
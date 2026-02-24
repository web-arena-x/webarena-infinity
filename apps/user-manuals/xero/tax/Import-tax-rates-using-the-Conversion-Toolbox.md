# Import tax rates using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-tax-rates-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import tax rates that aren’t available in Xero by default.

What you need to know

### How it works

Import a comma-separated values (CSV) tax rates file from your client’s previous accounting system to create new tax rates in Xero.

A tax rate can have between one and six tax components. If a tax rate has more than one component, they're linked together as a composite rate.

If you only need a few tax rates, it might be easier to [add them manually](Add-or-edit-tax-rates.md).

### Before you start

If you plan to import your client’s chart of accounts, do this first. You can use the [Conversion Toolbox chart of accounts import tool](Import-a-chart-of-accounts-using-the-Conversion-Toolbox.md) or [import your own](Import-a-chart-of-accounts.md).

To import tax rates into your client’s Xero organisation, you need the data file saved as a CSV file. If your client’s previous accounting system can’t export data as a CSV, either:

- [Use the Toolbox to convert the file](Convert-data-to-Xero-using-the-Conversion-Toolbox.md)
- Manually create an import file

Create the import file

If you can’t export your client's tax rates from their previous accounting system in comma-separated values (CSV) format, you need to create the file manually. To do this:

1. Open your client’s exported tax rates file in a spreadsheet program.
2. Adjust the formatting and data as needed.
3. Save the file in CSV format.

The import file needs the following information:

| Column name | Content |
| --- | --- |
| Name | The Tax rate display name. Enter the name as you want it to show in Xero. Use the same name on each line if the tax rate has separate components. |
| Component Name | The Tax component name. If it's a compound rate, add a separate line and name for each component, making up the overall tax rate. You can have up to six components per tax rate. |
| Component Rate | Enter a tax rate percentage for each component. |
| Is Compound | If there are two or more component rates, one can be a compound rate. Enter **Yes** if a rate is a compound rate, or **No** if it's not. A compound tax rate is applied to the transaction subtotal after the tax calculated from the other components has been added. |

Import the file

Once the file is in CSV format, import it into the toolbox:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client's organisation.
3. Click **Import Tax Rates**.
4. Click **Select CSV File to Upload,**select the import file, then click **Start Conversion**.
5. In the **Field** column, select the Xero field to map to each column in the import file, then click **Next Step**.
6. Preview the tax rates to import. Click **Show Details** to expand the list. Click **Previous step** to make changes in the toolbox. If you need to make changes to the import file, go back to step 4 and select the file again.
7. Once you’ve resolved any issues, click **Next Step**, then click **Finish**.

## What's next?

Check the [tax rates have imported](Add-or-edit-tax-rates.md) correctly.
# Configure Project Currency Settings

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/configure-project-currency-settings

---

## Background

Project currency settings allow you to set a default project currency, and configure exchange rates between currencies. You can also add currencies and default exchange rates that can be used on your contracts and direct costs as well as associated change orders, invoices and RFQs.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool.

## Steps

1. Navigate to the project's **Admin** tool.
2. Click **Currency Settings**.

### Project Currency and Exchange Rate Settings

**Project Currency**

This currency is used for Project level management and reporting. Available currencies are managed in the Company Admin tool. See [Configure Company Currency Settings](/product-manuals/admin-company/tutorials/configure-company-currency-settings).

- **Currency Display**

Choose whether currencies in Procore to be displayed as a symbol or ISO code.

- **Project to Company Exchange Rate**

This setting controls the exchange rate between the Project currency and the Company currency.

- **Synced with current company rate.** Selecting this option will keep the exchange rate for the project currency synced with the Company level configuration.
- **Fixed Rate**. 
   Selecting this option will allow you to set the exchange rate for the project currency. The project currency exchange rate will not stay in sync with the company-level exchange rate if this option is selected. You can update this rate at any time.

### Multi Currency for Financial Objects

**Enable Financial Object Multi Currency Settings**

Check this box to activate multi currency settings on financial objects. This will introduce the option to add currencies and default exchange rates that can be used on your contracts and direct costs as well as associated change orders, invoices, and RFQs.

**Activate Currencies for use on Financial Objects**

Click the **checkbox** in the 'Active?' column in the for currencies to make them available to select on contracts and direct costs.

**Set Project Specific Exhange Rates for Financial Objects**

If the 'Fixed Rate' option is selected, then you can edit the default exchange rate for new financial objects.
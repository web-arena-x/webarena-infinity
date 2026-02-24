# Bill Settings

Source: https://help.clio.com/hc/en-us/articles/14078692470427-Bill-Settings

---

## Change bill invoice PDF page size

This setting allows you to choose the page size format for bills that you download from Clio Manage. You can choose letter, A4, or legal.

1. Go **Settings** > **Billing** > **Bill Settings**.
2. Under **PDF Page Size**, select the appropriate page size format.
3. Scroll to the bottom and click **Save changes**.

## Bill sending options

#### Set default bill attachment options

In your bill settings, you can choose the default setting for how bills are attached when you send bills by email. You can choose to send bills as a secure PDF link or as an attached PDF as your default option.

1. Go **Settings** > **Billing** > **Bill Settings**.
2. Under **Default Bill Attachment Options**, select your default option.
3. Scroll to the bottom and click **Save changes**.

#### Default send by text message

In your bill settings, you can choose whether to allow [sending bills](https://help.clio.com/hc/articles/9285343645595-Send-Bills-for-Billing-in-Clio#h_01HBC5VHWDF3V78PNQMFXMWEFJ) by text message as being on or off by default. By default, the setting to send by text message is **On**. You can change this in your firm's bill settings.

1. Go **Settings** > **Billing** > **Bill Settings**.
2. Under **Default send by text message**, select your default option.
3. Scroll to the bottom and click **Save changes**.

**Note:** At the time that you [send a bill](https://help.clio.com/hc/en-us/articles/9285343645595-Send-Bills-for-Billing-in-Clio#h_01HBC5VHWDF3V78PNQMFXMWEFJ), you can still update your options for that particular bill.

## Enable bill cover page

By default, your bill invoices will not be preceded by a bill cover page. You can choose to turn this setting on, which means that bills you send to clients and bills that you download will have a cover page that shows the bill invoice number and total amount due before the rest of the bill invoice details. The bill cover page cannot be customized.

1. Go **Settings** > **Billing** > **Bill Settings**.
2. Under **Bill Cover Page**, check or uncheck the box for **Generate cover page for bills**.
3. Scroll to the bottom and click **Save changes**.

## Manage one or multiple currencies

Clio Manage supports working with multiple currencies for creating activities, billing, reporting, recording bank transactions, and more. To get started with multi-currency features, simply have to add a second currency in Clio Manage.

**Important:** At present, you should not use multiple currencies when you also use Clio Accounting.

**Note:** Administrators can manage the default currency and add, edit, and delete currencies to Clio Manage.

#### Change the default currency

When you set the default currency and use only one currency, any future change to this default currency changes the currency symbol in Clio Manage, but the change will not apply to any activities or expenses that were already billed, nor any previously recorded payments.

To change the default currency for your user account:

1. Go to **Settings** > **Billing** > **Bill Settings**.
2. Scroll down to **Default currency** and select a new currency.
3. At the bottom of the screen, click **Save changes**.

**Note:** You cannot change the default currency once you add additional currencies to Clio Manage.

#### Add a currency

**Important:** Before adding a currency, make sure that you have set your default currency. Once you add a currency, you cannot change the default currency.

Clio allows you to create activities, record expenses, and send bills in multiple currencies. When you opt in to use the multi-currency features in Clio Manage by adding a currency, all previous currency values entered are assumed to be the default currency.

**Note:** If your firm previously [edited bills](https://help.clio.com/hc/articles/9285222010395) for certain matters to change the currency symbol on the bills itself, adding a currency will cause a mismatch between your recorded activities/expenses and the payments of those bills for those activities/expenses. This happens because editing the currency on a bill does not change the currency of the activity or expense recorded in Clio Manage (which will continue to be in your default currency). When you add a currency, you will no longer be able to continue [editing the currency on bills](https://help.clio.com/hc/articles/9285222010395) as you did before. You will also not be able to change the currency for these matters due to the fact that their expenses and activities have already been recorded in the original currency used by your firm.

If you choose to start using the multiple currencies feature, you can handle this scenario in the following way:

- Create a new matter for your client and set the currency of the matter to your client’s preference. This leaves your previous historical data intact while allows your firm to take full advantage of Clio’s multiple currency feature.

To enable multiple currencies for your firm:

1. Go to **Settings** > **Billing** > **Bill Settings**.
2. Scroll to the **Currencies** section, then click **+ Add currency**.
3. Read the notification and confirm that you understand the effects of adding a currency.
4. Select a currency.
5. Choose how to use the currency when recording time entries.
   - **When it's a [your selected currency] matter billing preference, also record time in [your selected currency]:** When you choose this option, any time entry created for a [matter where the billing preference is set to your selected currency](../activities/rates-and-rate-hierarchies.md#h_01HEQZK3WR299D2JG523261DRW) will create the time entry in the same selected currency.
   - **When it's a [your selected currency] matter billing preference, record time in the default billing currency:** When you choose this option, any time entry created for a [matter where the billing preference is set to your selected currency](../activities/rates-and-rate-hierarchies.md#h_01HEQZK3WR299D2JG523261DRW) will have the time entry be created in the [default currency](#h_01KBGQ4G7D3EPWQ97NM88SMP47).

     You will have to also select how the conversion should be done.

     Example

     If your firm is in the US and you use a default currency of USD, but you have a client in Canada, you may set the client’s matter’s billing preference to CAD. If you choose this option, any time entry that you create for your client (in CAD) will be converted to your firm’s default currency of USD.
6. Choose how to use the currency when recording expense entries.
   - **Bill [your selected currency] expenses in [your selected currency] without converting to the matter billing currency:** When you choose this option, any expense entry created for a matter will remain in that currency.
   - **Bill [your selected currency] expenses by converting them to the matter billing currency:** When you choose this option, any expense entry created for a will be converted to the billing currency set for the matter.

     You will have to also select how the conversion should be done.
7. Once you have made all your selections, click **Add**.
8. At the bottom of the screen, click **Save changes**.

**Note:** If you have an integration with a third-party accounting software, make sure that your sync settings are correctly configured to handle multiple currencies.

- For QuickBooks Online or Xero, make sure that currency features are turned on.
- For other 3rd party providers, check to see if they support the integration before enabling multi-currency in your Clio account.

#### Edit a currency’s options

You can modify any currency you previously added.

1. Go to **Settings** > **Billing** > **Bill Settings**.
2. Scroll to the **Currencies** section, and in the **Other currencies** table, click the pencil (edit) icon for the currency that you want to modify.

**Note:** Certain changes to the currency’s settings may overwrite matter billing preferences. When such a scenario occurs when you are editing a currency, you will be notified.

For example, when you choose to convert time entries on a matter that has a particular currency specified in its billing preferences (i.e., you select the **When it's a [your selected currency] matter billing preference, record time in the default billing currency** radio button), any custom rate previously added to that matter will be overwritten by this conversion. You will be notified that any matter with custom rates in the currency you are editing will be cleared. When you later visit a matter to which this applied, a notification banner will also show that you may need to review the matter’s billing preference and update the custom billing rate.

#### Remove a currency

If you previously added other currencies, you can remove them from your firm’s account as long as the currencies have not been used to create any records (time entries, bank accounts, etc). Deleting created records in added currencies will not enable you to delete a currency from **Bill settings**.

1. Go to **Settings** > **Billing** > **Bill Settings**.
2. Scroll to the list of other currencies.
3. For the currency you want to remove, click the trash can (delete) icon.

   **Note:** If the icon is not clickable, the currency has been used for billing or accounting activities and cannot be deleted.

## Change time and decimal rounding settings

Clio Manage has two options for time rounding when creating time entries and generating bills to suit your firm’s needs.

Decimal rounding :   This option rounds all time entries to the nearest two decimal places. For example, if you create a time entry for 0.248 hours, the time entry will appear as 0.25 hours in the **Activities** table and on the bill.

Time rounding :   This option rounds all time entries up to the nearest minute increment of your choice. For example, if you set your minute increment to 5 and create a time entry for 22 minutes, the time entry will be rounded up to the nearest interval of 5 minutes, which is 25 minutes. If you set your time entry in hours, such as 1.20 hours, the time entry is calculated as 72 minutes and then gets rounded to the nearest 5 minute increment, which is 75 minutes or 1.25 hours.

**Important:** When you change time and decimal rounding settings, *all* time entries are affected for *all* users at the firm. This includes activities that have already been created and activities that have already been generated on bills.

To change your time and decimal rounding settings:

1. Go to **Settings** > **Billing** > **Bill settings**.
2. Scroll down to **Time rounding**.
3. Check or uncheck the boxes for **Enable decimal rounding** and **Enable time rounding**.
4. Click **Save changes**.
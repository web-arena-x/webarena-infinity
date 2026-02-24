# Set up and manage client relationships in Practice Manager

Source: https://central.xero.com/s/article/Set-up-client-relationships

---

## Overview

- Set up a relationship between clients individually, or import multiple client relationships using an import file.

How it works

- Client relationships help you prepare tax returns more efficiently.
- Xero automatically adds the relevant schedule to a tax return based on the relationship you select.
- Import data from other returns you've created for one member of the relationship.
- Set up a relationship between two clients.
- When you add or update a relationship in Practice Manager, the change appears automatically in Xero HQ as well.

Add a relationship

Before you can add a relationship, you must [select a business structure](Set-up-custom-business-structures-in-Practice-Manager.md) for your client. The available relationship types depend on the business structure of the client.

To set up a relationship between two clients:

1. Select **Clients**, then click one of the clients you want to add to the relationship.
2. Next to **Relationships**, click **Add**.
3. Select the **Relationship type** and search for and select the **Related client**.
   Depending on the client’s business structure and the type of relationship you select, you might need to enter additional information. For example, if you select **Shareholder Of**, enter **Shares held**.
4. (Optional) Enter a start date, end date or both to show when the relationship began or ended.
5. Click **Create relationship**.

You'll see the relationship in the client records of both members of the relationship.

Import client relationships

### Prepare the client relationships import file

If you want to add multiple client relationships at the same time, you can import the details from another source, such as a spreadsheet. Before you can start the import, you need to [prepare the import file](Import-data-into-Practice-Manager.md) from an exported file, a blank file, or the example file we provide, [Client Relationships-NZ](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/3m000000DrGz/sn1.7_NqfLWmSwRueZbWG5nmnkUr4K20_sHwMZYN8Zc) (CSV, 80 bytes).

### Client relationships import fields explained

Most client relationships import fields are straightforward, but some have special requirements for formatting or acceptable values.

Required fields for importing client relationships are:

- Name
- Related Name
- Relationship

These details must be complete for both members of the relationship.

| **Field** | **Description** |
| --- | --- |
| **Name** | Enter the name of the client you are importing the relationship against. |
| **Related Name** | Enter the name of the related client. The value must match the name of an existing client in Practice Manager. |
| **Relationship** | The value must be one of: Director, Shareholder, Trustee, Beneficiary, Partner, Settlor, Secretary, Public Officer, Husband, Wife, Spouse, Parent Of, Child Of, Appointer, Member, Auditor, Owner. The valid values depend on the business structure of the client. |
| **Number of Shares** | Enter the total number of shares held by each related entity. Recommended for some relationship types, such as Shareholder and Owner. |
| **Percentage** | Enter the percentage holding of each related partner. Recommended for Partner type relationships. |
| **Start date** | The values can be in either d-m-yyyy or d/m/yyyy format. Dates cannot be further in the future than 2030. |
| **End Date** | The values can be in either d-m-yyyy or d/m/yyyy format. Dates cannot be further in the future than 2030. |

### Import the data

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Client Relationship**.
4. Select the format of your import file then click **Next**.
5. Click **Choose File** and select your import file.
6. Click **Import**.

The number of rows imported and any errors are displayed at the bottom of the screen. We recommend you check the relationship between a small number of clients to ensure the import worked as expected.

Edit or delete a relationship

Tip

When you delete a relationship, Practice Manager removes all details of the relationship. If you want to keep a record of when a relationship ended, enter an end date and save the change instead.

To edit or delete a relationship:

1. Select **Clients**, then click the name of one of the clients in the relationship.
2. Under **Relationships**, next to the relationship you want to change, click the menu icon , then select:
   - **Edit**, update the details of the relationship, then click **Edit relationship**.
   - **Remove this** **relationship**, then click **Remove** to confirm.

Any changes you make to the relationship, including deleting it, are automatically applied to both clients in the relationship.

## What's next?

You're all done. With a client relationship in place, information is shared when you create a tax return for related clients.
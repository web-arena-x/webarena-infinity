# Set Up the Import Sage 300 CREÂ® Tax Groups Feature

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/set-up-the-imoprt-sage-300-cre-tax-groups-feature

---

## Background

In Sage 300 CREÂ®, a *tax group* is used to calculate the tax rates on both purchase and sales transactions. They can also be imported into Procore. After importing them into Procore, Sage 300 CREÂ® tax groups are called *tax codes.* You and your project team members can then begin adding tax codes to a variety of different line items in Procore's financial tools, such as:

- Commitments (i.e., Purchase Orders and Subcontracts)
- Change Orders (i.e., Purchase Order and Subcontract Change Orders)

To learn more about how tax codes can be used with Procore's financial tools, see â[How can I use tax codes on a project?](/faq-how-can-i-use-tax-codes-on-a-procore-project)

##### Â Important

During your company's Procore + Sage 300 CREÂ® implementation process, a Integration Implementation Specialist will work with your 

A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

ProcoreÂ Administrator to configure the tax group and tax rate configuration settings in the hh2 synchronization client. See [Set Up the hh2 Synchronization client for Importing Sage 300 CREÂ® Tax Groups](/product-manuals/sage-300-cre/tutorials/set-up-the-hh2-synchronization-client-to-import-sage-300-cre-tax-groups).

## Things to Consider

- **Required User Permissions**:

  - 'Admin' on the Company Directory.
- **Prerequisites:**

  - Create one (1) or more tax group(s) in Sage 300 CREÂ®. A tax group can contain multiple tax rates.
- **Procore +** **Sage 300 CREÂ®** **Information:**

  - Always create your tax groups in Sage 300 CREÂ®.
  - Sage 300 CREÂ® tax groups can contain multiple rates.
  - When applying a tax group with multiple rates to a line item, the tax code in Procore will be calculated on as a cumulative sum of all of that group's rates.
  - The steps for adding a tax code to a commitment or Commitment Change Order (CCO) line item is the same for both ERP-integrated and non-integrated Procore companies.
  - When exporting a PDF Invoice from Procore, the system will calculate and display the Tax Type subtotal in the same manner for both integrated and non-integrated Procore companies.

## Steps

##### Â Important

Before you use the steps below, ensure that you have created the desired tax groups in Sage 300 CREÂ® and confirm that your Integration Implementation Specialist has completed the required tax configuration steps and turned the feature ON in the Procore + Sage 300 CREÂ® microservice.

After completing the tasks in the Important note above, do the following:

- Enable the Tax Code Settings in Procore
- Activate the Tax Codes Feature on a Procore Project

#### Enable the Tax Code Settings in Procore

1. Navigate to the company's **Admin** tool.
2. Under **Project Settings**, click **Tax Codes**.
3. Place a mark in the **Use Tax Code Settings** checkbox.
4. Click **Save**.   
   *Note*: Your Integration Implementation Specialist will also need to enable an export setting in the Sage 300 CREÂ® microservice.

#### Set the Tax Type

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings**, click **Tax Codes**.
3. Under **Tax Type**, click **Add a New Type** and enter the following information:

   - **Name**. Enter the name of the tax type. For example, enter GST (for Goods & Services Tax) or VAT (for Value-Added Tax). After you click Save, the name you enter here is updated on the [Tax Type] in the **Tax Codes** section of this page.
   - **Description**. Enter a descriptive name for the tax type. Typically, the name of the tax type will be abbreviated, so the description field lets you provide more information about the tax type. For example, enter `Goods & Services Tax` or `Value-Added Tax`.
4. Click **Add a New Type**.
5. If you want to delete the tax type, click the delete icon next to the tax type line item.

#### Activate the Tax Codes Feature on a Procore Project

1. Navigate to the project's **Admin** tool.
2. Click **General**.
3. Under **Advanced Project Settings**, place a mark in the **Use Tax Codes** check box.
4. Select the desired code from the **Default Tax Code** box.
5. Click **Update**.
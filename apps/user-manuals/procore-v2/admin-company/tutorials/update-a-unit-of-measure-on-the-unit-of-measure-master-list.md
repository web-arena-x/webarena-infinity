# Update a Unit of Measure on the Unit of Measure Master List

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list

---

## Background

The Company Admin tool stores Procore's Unit of Measure Master list. The system's default list contains 19 units of measure. See [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) Although you cannot remove the default selections from the list, you can add new units of measure using the Steps below.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company Admin tool.
- **Additional Information**:

 - To add a new unit of measure to the list, contact your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator).
 - You cannot modify or delete the default units of measure on Procore's master list, but you can add an unlimited number of new measures to it.
- For companies using the ERP Integrations tool: **Show/Hide**

 Each [integrated ERP system](/glossary-of-terms) imposes its own maximum character limits on 'Unit Name' entries. While Procore does NOT enforce these system's limits on 'Unit Name' entries, a reminder message (pictured below) appears when you attempt to save a longer entry:

 Below are each system's maximum character limits:

 - ViewpointÂ® SpectrumÂ®**:** ViewpointÂ® SpectrumÂ®. Six (6) characters maximum.
 - Integration by Procore**:** VistaÂ®. Three (3) characters maximum.
 - QuickBooksÂ® Desktop. Six (6) characters maximum.
 - Sage 100 ContractorÂ®. Six (6) characters maximum.
 - Sage 300 CREÂ®. Six (6) characters maximum.

##### Â Warnings

For the units of measure that you add to your company's Procore account:

- You can edit a unit of measure (for example, change 'gal' to 'gallon'). However, the change will only affect new line items. Changes do NOT affect existing line items, which may be undesirable behavior if your team is using Procore's reporting capabilities.
- You can delete a unit of measure that you added to the list (for example, delete 'gal' from the UOM drop-down menu on the line item experience). However, you cannot delete the standard measures on Procore's Master List.
- Keep in mind that deleting measures will only remove the unit of measure from the drop-down list in Procore's line item experience. It will not change existing measures that have been applied to existing line items.

## Steps

1. Navigate to the Company **Admin** tool.
2. Under 'Company Settings', click **Unit of Measure Master List**.
3. Click **Add Unit of Measure**.
4. Add a new unit of measure as follows:

   1. In the **Display Name** field, type the desired abbreviation. For example, enter an abbreviation for 'Gallon' as follows: gal

      ##### Â Important

      When entering a 'Unit Name' that includes an exponent (for example, square meters (m2) or cubic meters (m3)), always insert a caret (^) symbol between the unit of measurement and exponent. Do NOT type (or use a cut-and-paste operation) to enter the exponent into the cell. Procore will use this notation to convert the character into a superscript entry.

      Below are common examples showing the correct notation format to use when entering exponents in the 'Unit of Measure' cells on an import template:

      - **Square kilometers (km2) MUST be entered as:** km^2
      - **Square meters (m2) MUST be entered as**: m^2
      - **Cubic meters (m3) MUST be entered as**: m^3

      Currently, when adding custom units of measure, you do NOT have the ability to add entries in the **Description** field.

- From the **Category** list, select the measurement type from the following choices:

 - Time
 - Amount
 - Length
 - Area
 - Volume
 - Mass
 - Other
- Click **Save**.
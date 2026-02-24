# Creating and configuring assets in Admin Center (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/9817310808090-Creating-and-configuring-assets-in-Admin-Center-EAP

---

Verified AI summary ◀▼

Create and configure IT asset types and custom fields to manage hardware and software assets. Use hierarchical structures for efficient field inheritance. Track asset locations and bulk import asset data using a CSV file. This setup allows agents to interact with asset records in the Agent Workspace, streamlining asset management and enhancing your support operations.

All Suites | Growth, Professional, Enterprise, or Enterprise Plus

IT assets are things, such as hardware and software, that IT teams need to procure, allocate, refresh, and retire over time. Admins can create and configure asset types and then bulk import existing asset data into Zendesk. This data is then available to agents to interact with in the Agent Workspace.

This article contains the following topics:

- [Understanding assets and how they work](#topic_fgd_z2c_bhc)
- [Creating asset types](#topic_u1d_vcf_bhc)
- [Creating custom asset fields and adding them to asset types](#topic_vkv_jdf_bhc)
- [Creating and using asset locations](#topic_lrl_ldf_bhc)
- [Bulk importing asset data](#topic_sd2_mdf_bhc)

**Related articles**:

- [Turning on IT asset management in Zendesk (EAP)](https://support.zendesk.com/hc/en-us/articles/9817293579674)
- [Using assets in ticket workflows (EAP)](https://support.zendesk.com/hc/en-us/articles/9817279885466)

## Understanding assets and how they work

An *asset* is a physical or digital thing that you procure, allocate, maintain, and retire. For IT teams, assets are often hardware, such as laptops and monitors, and software licenses.

When managing assets in Zendesk, an admin must first define the *asset type*, which becomes an object in Zendesk. The asset type definition consists of standard and [custom fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) that describe the data you need to store for this type of asset. This could be anything from text and drop-down fields to [lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770), which define how the asset type is related to other objects in your Zendesk account.

To save you the effort of recreating the same fields for many asset types, they're created with a hierarchical structure that makes it possible for child asset types to inherit the parent asset type's fields. For example, Zendesk predefines a Hardware asset type with three predefined children asset types: Mobile, Desktop, and Laptop. The children asset types' records automatically have all of the Hardware fields.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_asset_type_hierarchy.png)

After an asset type is created and configured with fields, admins can use the data importer to [bulk import](#topic_sd2_mdf_bhc) their asset data, and agents can view and manage the asset records in Zendesk Support.

## Creating asset types

Admins can use the Types page to create and manage asset types. You can have a total of 50 asset types.

**To create an asset type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png)
   **IT Assets** in the sidebar, then select **Assets > Types**.
2. Click **Create type**.
3. Enter a unique **Name** for the asset type.
4. If applicable, select the **Parent type**.

   Asset types can only be nested three layers deep. You can't select an asset type as the parent if it would result in more than three layers.

   Note: The new asset type will automatically inherit the parent type's fields and be nested under the parent asset type on the Asset types page.
5. Click **Create**.

## Creating custom asset fields and adding them to asset types

Asset fields are the schema for each asset type, defined by [standard](#topic_odv_v2f_bhc) and [custom](https://support.zendesk.com/hc/en-us/articles/4408838961562) asset fields. These fields represent properties of the asset type that you want to store and are used by agents when creating and managing assets.

An asset record consists of the [global asset fields](#topic_cjf_ywq_bhc), [asset type custom fields](#topic_rgb_bxq_bhc), and asset type custom fields inherited from parent asset types.

### Understanding the standard asset fields

The following common asset fields are pre-defined by Zendesk. These fields apply to all assets and can't be edited or deleted.

| Field name | Field type |
| --- | --- |
| Asset tag | Text |
| Asset type | Lookup relationship |
| Location | Lookup relationship |
| Manufacturer | Text |
| Model | Text |
| Notes | Multi-line |
| Organization | Lookup relationship |
| Purchase cost | Decimal |
| Purchase date | Date |
| Serial number | Text |
| Status | Lookup relationship (Valid values: available, in use, missing, pending, retired, under repair) |
| User | Lookup relationship |
| Vendor | Text |
| Warranty expiration | Date |

### Creating custom asset fields

To finish creating an asset type, you must configure it with custom asset fields. There are two ways to create custom asset fields:

- [Global asset fields](#topic_cjf_ywq_bhc): Asset fields created and managed on the Asset fields page in Admin Center, including all standard asset fields. These apply to all asset types.
- [Asset type custom fields](#topic_rgb_bxq_bhc): Asset fields added on an asset type's Field tab.
 These apply exclusively to the individual asset type and aren't available to be reused by other asset types.

You can have up to 100 asset fields, including standard and custom fields.

#### Creating global custom asset fields

Use the Asset fields page to create custom asset fields that will apply to all asset types.

**To create global custom asset fields**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png)
   **IT Assets** in the sidebar, then select **Assets > Fields**.

   Alternatively, you can create and add fields from the Fields tab of an asset type. Fields created this way are still available to all asset types.
2. Click **Create field**.
3. Select the [field type](https://support.zendesk.com/hc/en-us/articles/4408838961562) and enter a unique **Display name**.
4. Verify that the **Field key** is the value you want it to be.

   The field key makes it possible for the API to reference the field. When you enter a name for the field, the field key is automatically populated. If you want the name and key to be different, you must edit the field key.

   Note: You can't change the field key after you create the custom object field.
5. Set other properties for your field.

   Options vary by field type.
6. Click **Save**.

#### Adding custom fields to an asset type

Use the Fields tab of an asset type to create custom asset fields that apply only to that individual asset type. These are the only fields that are listed on the asset type’s Fields tab. However, records with the asset type will include all global and inherited asset fields as well.

**To add custom fields to an asset type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png)
   **IT Assets** in the sidebar, then select **Assets > Types**.
2. Click the name of the asset type you want to add fields to.
3. Click the **Fields** tab, and then click **Add field**.
4. Select the [field type](https://support.zendesk.com/hc/en-us/articles/4408838961562) and enter a unique **Display name**.
5. Verify that the **Field key** is the value you want it to be.

   The field key makes it possible for the API to reference the field. When you enter a name for the field, the field key is automatically populated. If you want the name and key to be different, you must edit the field key.

   Note: You can't change the field key after you create the asset field.
6. Set other properties for your field.

   Options vary by field type.
7. Click **Save**.

## Creating and using asset locations

Tracking the location of physical assets is important. Locations are referenced as asset lookup relationship fields, so you can see and manage an asset’s location in the asset record.

You can create up to 10,000 locations.

**To create a location**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png)
   **IT Assets** in the sidebar, then select **Assets > Locations**.
2. Click **Create location**.
3. Enter a unique **Location name**.
4. Click **Create**.

## Bulk importing asset data

Rather than adding your assets one by one, you can import your asset data in bulk after you create the asset types and add fields to it. To do this, upload a CSV (comma-separated value) file. You must be an admin to import assets.

**To bulk import asset data**

1. Create a CSV file that adheres to the [required formatting](#topic_tc4_t1h_bhc).
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tools > Data importer**.
3. Click **Import**.
4. Under **Target destination**, select **Assets**.
5. Under **Import type**, choose one of the following:
   - **Create only**: Only new asset records are created. Any data in the CSV file pertaining to existing records is ignored.
   - **Update only**: Replace data for the existing asset records listed in your CSV file. Any data pertaining to new records is ignored.
   - **Create and update**: Create new asset records and update data for the existing asset records listed in your CSV file.
6. Under **File upload**, drag and drop your file or **click to upload** and select your CSV file from the file browser.

   If you need to change the file you've selected, click the delete icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) next to the file name.
7. Click **Next**.
8. Review the **Field mapping** list.
   - If the field mapping is correct, click **Next**.
   - If the field mapping isn't correct, click **Back**. Edit your CSV file to adhere to the format requirements, and then re-upload the file.
9. Review the summary of import details in the confirmation dialog and then click **Start import**.

   After the import starts, the imported changes can't be reverted. To check the status of an import, check your [import history](https://support.zendesk.com/hc/en-us/articles/5789034291738).

### Formatting your CSV file

When creating your CSV file to import asset data, keep the following in mind:

- The file must be properly formatted CSV and saved using UTF-8 character encoding.
- The first row of the CSV file is the header row.
- The header row must contain the following columns: **name**, **asset type**, and **status**. Optionally, if you wish to bulk update the records in the future, you must also include an **external\_id** column. All other field names in the header row must be exact matches to the field keys in your asset types.
- Each row must contain valid values for all of the asset type's required fields. Otherwise, the asset record can't be created.

 Note: The asset type, status, and location values are case-sensitive. Inconsistent capitalization between your CSV file and the asset type, status, and location names in Zendesk can result in a failure to create or update asset records.

 Unrecognized location values, including variations in capitalization, result in the creation of new locations of that name.
- The import CSV file can't exceed 1 GB in size or 10,000 rows of data.
 Furthermore, each row can't exceed 32 KB in size.
- The import CSV file can contain a maximum of 100 columns.
- Don't include the same record more than once within a CSV file. Doing so can cause your import to fail.
- There's no guarantee that asset records are created or updated in the order they appear in the CSV file.
- To import values for dropdown fields, use the custom dropdown field's **field\_key** as the column heading and specify the options **tag**, not the user-friendly value.
- To import values for lookup relationship fields, use the custom lookup relationship field's **field\_key** as the column heading and provide either the record's **id** or **external id**. If you use the record's **ID**, provide the value. If you use the **External ID**, use the format **external\_id:*value***, where *value* is replaced with the related record's external ID value.

 Note: To assign an asset to a user during an import, you can provide the user's **email** in place of the user's **id** or **external id**.
- If you are not importing data for a field, do not list it in the header row.
- Add line breaks to notes or multiline custom fields by pressing ALT+ENTER on Windows or CTRL+OPTION+RETURN on macOS.
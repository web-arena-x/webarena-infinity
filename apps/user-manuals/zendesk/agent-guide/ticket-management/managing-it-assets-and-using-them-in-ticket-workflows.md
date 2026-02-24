# Managing IT assets and using them in ticket workflows

Source: https://support.zendesk.com/hc/en-us/articles/9817279885466-Managing-IT-assets-and-using-them-in-ticket-workflows

---

All Suites | Growth, Professional, Enterprise, or Enterprise Plus

IT assets are things, such as hardware and software, that IT teams need to procure, allocate, refresh, and retire over time. Within Zendesk *assets* are the records for each asset. The information captured varies by asset type and is defined by admins.

Within Zendesk Support, individual assets can be assigned and viewed by agents.
Additionally, admins can create new asset records and modify details of existing assets.

This article contains the following topics:

- [Assigning IT assets in tickets](#topic_vv4_2cr_bhc)
- [Viewing an asset's details from a ticket](#topic_qpk_32r_bhc)
- [Viewing and managing assets](#topic_ngw_dcr_bhc)

Related articles:

- [Turning on IT asset management in Zendesk](https://support.zendesk.com/hc/en-us/articles/9817293579674)
- [Creating and configuring asset types in Admin Center](https://support.zendesk.com/hc/en-us/articles/9817310808090)

## Assigning IT assets in tickets

When a support or service request is related to an asset, agents can use the context panel to assign an asset to the ticket requester.

**To assign an asset from the context panel in a ticket**

1. In Zendesk Support, open a ticket requesting an asset.
2. In the ticket, click the IT asset management icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the right sidebar.
3. In the Assets panel, click **Assign asset**.
4. Click **All assets** or the name of a specific asset type.
5. Select an available asset and click **Select**.
6. Select the asset's **Status**.
7. Click **Assign**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_asset_assigning.png)

## Viewing an asset's details from a ticket

Agents can see a summary of key information about assets assigned to the ticket requester in the IT asset management view in the context panel. From there, they can open an asset's details directly if they need to learn more about an asset already assigned to a ticket requester or assets they are considering assigning to the requester.

The data tracked for each asset is defined by admins through a combination of the [global asset fields](https://support.zendesk.com/hc/en-us/articles/9817310808090#topic_cjf_ywq_bhc)
(including the [standard asset fields](https://support.zendesk.com/hc/en-us/articles/9817310808090#topic_odv_v2f_bhc)), asset type custom fields, and asset type custom fields inherited from parent asset types.
The fields within an asset record are organized based on their origin.

**To open an asset's details from a ticket**

1. In a ticket, click the **Asset Management** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the right sidebar to open the context panel.
2. Beneath the asset you want to view more information about, click **View record**.

   This opens the asset record's details in a new tab. The asset details are read-only for agents.

## Viewing and managing assets

The Asset Management page in Support provides a comprehensive list of asset records.
From this page, admins can search for assets, view asset details, and create and modify asset records as needed. Agents can view details for individual assets, accessed from a ticket, but can't view a list of assets or create and manage asset records.

On the Asset Management page, users with permission can:

- [Access the asset list](#topic_bkw_h2r_bhc)
- [Create an asset record](#topic_onz_32r_bhc)
- [Edit an asset record](#topic_sdg_k2r_bhc)
- [Delete asset records](#topic_cf4_trr_bhc)

### Accessing the asset list

Admins can view a complete list of assets. In addition to filtering the list by asset type, you can also search for assets by name.

**To access the asset list**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Asset Management** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the sidebar.
2. Under **IT Asset Types**, select the asset type.

   A list of all assets of that type is displayed.
3. (Optional) Use the search bar at the top of the page to search for a specific asset record.

   When searching for an asset, keep the following in mind:
   - Search queries check against all text-based fields within the records. That means queries can match against the Name field value and values in fields of the following types:
     Text, Regex, or Multi-line.
   - Search queries match on the beginning of words only. In multi-word values, queries can match against the beginning of any word in the value.

### Creating an asset record

Admins can create asset records individually from the Asset Management page or [in bulk](https://support.zendesk.com/hc/en-us/articles/9817310808090#topic_sd2_mdf_bhc)
from Admin Center.

**To create an asset record**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Asset Management** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the sidebar.
2. Click **Create record**.
3. Under **Standard fields**, enter the required information, such as the asset's **Name** and **Status**.
4. Click the **Asset fields** tab to enter information into the asset type's custom fields.

   If the asset type inherited any asset type fields from parent asset types, those are grouped together by the parent type.
5. Click **Add**.

### Editing an asset record

Admins can modify asset records as needed.

**To edit an asset record**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Asset Management** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the sidebar.
2. Under **IT Asset Types**, select the asset type.
3. Click the name of the asset you want to edit.
4. Click **Edit** next to the collection of fields you need to update:
   - **Standard fields**
   - **Asset fields** tab, next to the groupings of fields by asset type (parent types and this asset's type)

   Note: If you change the asset type, any data that is no longer applicable to the new type is preserved in a read-only state at the bottom of the asset record, labeled as *transferred fields*.
5. Click **Save**.

### Deleting asset records

Assets that are no longer needed can be deleted individually or in bulk. Deleting an asset is permanent and can't be undone.

**To delete a single asset record**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Asset Management** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the sidebar.
2. Under **IT Asset Types**, select the asset type.
3. Select the asset you want to delete.
4. Click **Delete** at the bottom of the page.
5. In the confirmation dialog, click **Delete record**.

#### Deleting asset records in bulk

Deleting multiple assets simultaneously can save you time.

**To delete a multiple asset records**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Asset Management** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/itam_icon.png))
   in the sidebar.
2. Under **IT Asset Types**, select the asset type.
3. Select the assets you want to delete.
4. Click **Delete** at the bottom of the page.
5. In the confirmation dialog, click **Delete record**.
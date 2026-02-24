# Add, edit or delete a fixed asset type

Source: https://central.xero.com/s/article/Add-edit-or-delete-a-fixed-asset-type

---

## Overview

- Create a new asset type, edit the fields of an existing asset type or delete an asset type.
- The default settings of the asset type will be applied to any new assets assigned to it.

About fixed asset types

You need the advisor user role to add, edit or delete asset types.

Every fixed asset you add to the register needs to be assigned a fixed asset type. You can have a maximum of 25 fixed assets types in Xero.

An asset type has the following settings:

- Asset account
- Accumulated depreciation account
- Depreciation expense account
- Depreciation method
- Averaging method
- Depreciation rate or effective life

All fields are mandatory. You need to choose one of either depreciation rate or effective life.

When you create a fixed asset and select the asset type, all the default settings of the asset type are applied to the asset.

You can edit the depreciation settings for a particular asset, but you can't change the accounts. To change the account codes for a particular asset, you need to change the asset type assigned to the asset.

Add a fixed asset type

Before you create an asset type, make sure your chart of accounts contains the fixed asset, accumulated depreciation and depreciation expense accounts you want to assign. When you create the fixed asset type, the asset account and accumulated depreciation accounts need to be fixed asset type accounts. You can [add accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md) to the chart of accounts if needed.

To add a fixed asset type:

1. In the **Accounting** menu, select **Accounting settings**, then click **Fixed assets settings**.
2. Click **New asset type**.
3. Under **Asset type**, enter a name. This must be unique.
4. Under **Asset account,** select the fixed asset account that you want to assign to your new asset type.
5. Select the **Accumulated depreciation account** and **Depreciation expense account**.
6. Select the **Depreciation method** and the **Averaging method**.
7. Select either **Rate** or **Effective life**, then enter the specific rate or number of years accordingly.
8. Click **Save**.

Edit a fixed asset type

The details you can change depend on whether the asset type is locked or not.

If you run depreciation on assets assigned to an asset type, Xero locks the asset type in **Fixed assets settings**.

If an asset type is locked, you can only update the name of the asset type and the depreciation settings (method, rate or effective life).

If you need to edit any other fields of a locked asset type, you need to [roll back depreciation](Run-or-roll-back-depreciation.md) so that no assets assigned to that type have any depreciation posted. Make your changes, then re-run depreciation.

The number next to an asset type is the number of assets applied to that asset type.

If you edit an asset type, all future assets that are assigned that type will have the updated settings applied. The fixed assets currently assigned to that asset type will show the updated name of the asset type, but their depreciation settings remain as they were.

To edit an asset type:

1. In the **Accounting** menu, select **Accounting settings**, then click **Fixed assets settings**.
2. In the **Asset types** tab, select the name of the asset type you want to edit.
3. Make your changes, then click **Save**.

Delete a fixed asset type

You can delete a fixed asset type which has draft fixed assets assigned to it, or no assets assigned to it. If you delete an asset type that has draft assets assigned to it, the asset type is deleted from each draft asset.

You can't delete a fixed asset type that has registered or disposed fixed assets assigned to it. You can see how many registered and disposed fixed assets a fixed asset type has when you click on the asset type.

You can't delete a locked fixed asset type.

When you delete an asset type, it can't be restored. If you delete an asset type in error, you need to recreate it.

To delete a fixed asset type:

1. In the **Accounting** menu, select **Accounting settings**, then click **Fixed assets settings**.
2. On the **Asset types** tab, click the fixed asset type you want to delete.
3. Click **Delete**, then click **Delete**again to confirm.

## What's next?

Once you've added a fixed asset type, you can assign assets to it when you [add fixed assets to your register](Add-fixed-assets.md).
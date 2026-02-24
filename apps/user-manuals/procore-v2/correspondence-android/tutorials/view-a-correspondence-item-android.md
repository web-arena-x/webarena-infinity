# View a Correspondence Item (Android)

Source: https://v2.support.procore.com/product-manuals/correspondence-android/tutorials/view-a-correspondence-item-android

---

## Things to Consider

- **Required User Permissions:**

 - *To view a correspondence item not marked as 'Private':*

    - 'Read Only' level permissions or higher on the correspondence type.

      ##### Â Tip

      Users may require specific roles on a correspondence item (or granular permissions) to view the item depending on the item's status and privacy settings.

      **What user roles can view which types of correspondence items?** **Show/Hide**

      In the table below, the icon indicates which user roles can view a correspondence item based on its status and privacy settings, and the icon indicates which user roles cannot view a correspondence item based on its status and privacy settings.

      | | | | | | | | | | |
      | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
      | User Role | Correspondence Item Settings | | | | | | | | |
      | Draft | Draft and 'Private' | Draft and 'Super Private' | Open | Open 'Private' | Open and 'Super Private' | Closed | Closed and 'Private' | Closed and 'Super Private' | |
      | Creator | | | | | | | | | |
      | Assignee | | | | | | | | | |
      | Distribution List Member | | | | | | | | | |
      | Received From | | | | | | | | | |
      | No Role | | | | | 1 | 1 | | 1 | 1 |
      | Correspondence Type Admin | | | | | | 2 | | | 2 |

      1 Users with the ['View Private Items Accessible to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can view 'Open' or 'Closed' correspondence item marked 'Private' or 'Super Private' if another user in their company (including them) is the correspondence item's creator, an Assignee, a Distribution List member, or added in the Received From field on the item.

      2 Users with 'Admin' level permissions on the correspondence type can view 'Super Private' correspondence items ('Open' or 'Closed') if they are (or another user in their company is) the correspondence item's creator, an Assignee, a Distribution List member, or added in the Received From field on the item.

## Steps

1. Navigate to the project's **Correspondence** tool.
2. *Optional:* [Search and Filter Correspondences (Android)](/product-manuals/correspondence-android/tutorials/search-and-filter-correspondences-android)
3. Tap the correspondence item to view its summary.
4. *Optional:* The 'Attachments' section shows the documents attached to the item. Tap **See All** to view all the item's attachments in a list format and search by file name, format, or when a file was last modified.
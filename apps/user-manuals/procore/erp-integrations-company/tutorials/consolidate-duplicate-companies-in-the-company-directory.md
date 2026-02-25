# Consolidate Duplicate Companies in the Company Directory

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/consolidate-duplicate-companies-in-the-company-directory

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When your Procore company is integrated with an ERP system, you will typically link the company records in your ERP system with their corresponding company records in Procore's Company level Directory tool.

However, before you create that link between the systems, it is strongly recommended that you use the steps below to remove any duplicate company records that might exist in the Company level Directory to make sure linking is valid and all records maintain integrity.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the company's Directory tool.
- **Recommendations**:

 - If you only have a few duplicate company records in the Company Directory, use the steps below. 
     OR
 - If you have many duplicate records, use the steps in [Merge Companies](/product-manuals/directory-company/tutorials/merge-companies) instead.

## Steps

### 1. Move the Company's Users

1. Navigate to the Company level **Directory** tool.
2. Click the **Companies** tab.
3. Locate the duplicate company records in the list.
4. Do the following:

   - **Identify the 'primary' company record that you want to keep**. You do not need to take action on the users listed under the record you want to keep.   
      AND
   - **Identify the 'duplicate' company record that you want to remove**. You will remove all of the users from this record and reassign them to the correct record.
5. Next to the 'duplicate' company (the one you want to remove), click **Edit**.
6. Click the **General** subtab.
7. In the **Name** field, add an 'X-' in front of the company name (e.g., *X-ABC Plumbing*) so you can easily recognize it later as the company you DON'T want to keep.
8. Click **Save**.
9. In the same ('duplicate') company record, click the **Users** subtab.
10. Do the following for EVERY user listed under the company that you won't keep:

- Click the **Edit** button next to the user's name.
- Clear 'duplicate' company from the **Company Name** selection.
- Select the correct 'primary' company (the one you will keep), from the drop-down list.
- Click **Save**. 
 *Note: You must remove ALL of the existing users from the 'duplicate' company before you can remove it. If there are too many users to perform this action manually with the steps described above, you can choose to* [Merge Companies](/product-manuals/directory-company/tutorials/merge-companies) *instead.*

Once all users have been moved to the company record you need to keep, you can then deactivate the duplicate company record.

### 2. Deactivate the Company

1. Navigate to the company's Directory tool.
2. Locate the company record that you want to remove (e.g., X-ABC Plumbing).
3. Click **Edit**.
4. Click **Deactivate Company**.

   - If this button is grayed-out and unavailable, click the **Users** subtab and make sure the list is empty.
   - If the duplicate company record is listed on a commitment, you cannot deactivate it. Instead, see [Merge Companies](/product-manuals/directory-company/tutorials/merge-companies).

A banner appears at the top of the page to confirm that the company record is deactivated.

## Next Steps

- [Link an ERP Company to a Procore Company](/product-manuals/erp-integrations-company/tutorials/link-erp-companies-to-procore-companies)
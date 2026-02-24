# Add Conditional Logic to a Company Level Inspection Template

Source: https://v2.support.procore.com/product-manuals/inspections-company/tutorials/add-conditional-logic-to-company-level-inspection-template

---

## Things to Consider

- [Required User Permissions](/product-manuals/inspections-company/permissions)

## Steps

The rule for inspection conditions is as follows: **When** 'Parent item' **Is** 'Display Condition', **Then show** 'Child Item(s)'.

1. Locate the Company level inspection template and click **Edit**.
2. Under **Inspection Items,** find a 'Parent Item' you want to begin your conditions with and click the **Add Conditions** icon.
3. Select your 'Display Condition'.
4. Select your [Child Item(s)]. Items not selected will become a 'Hidden Item' when the 'Display Condition' is selected by the inspector.
5. If you want to add another condition within the same parent inspection item, click + **Add** **Condition**.
6. Click **Save**.
7. **Repeat** Steps 1 - 6 to add additional 'Parent Items'.
8. If applicable, use the **up arrow** icon and the **down arrow** icon to move inspection items up or down.
9. When you are done adding all of your conditional logic items, click **Update**.

##### Â Note

- All inspection line items must already be contained within the same inspection section as the 'Parent Item' to add them as 'Child Item'.
- You can have up to four maximum conditions nested within one 'Parent Item'.
- **Number**, **Text**, **Signature**, and **Date** response types can't have conditional logic added to them.
- You can see change histories for any added or removed conditional logic items.
- Conditional Logic can only be added to Company Level Inspection line items at the Company Level.
- Conditional Logic can only be added to Project Level inspection line items at the Project Level.
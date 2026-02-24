# Send a Change Order to the Change Events Tool

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/send-a-change-order-to-the-change-events-tool

---

## Background

After you have created a change order in the Estimating tool, you can use the 'Create a New Change Event' or 'Update Existing Change Event' options to copy and export line items from that change order into the project's Change Events tool. The cost codes and amounts on the estimate will also be updated on the project's budget.

## Things to Consider

- [Required User Permissions](/product-manuals/estimating-project/permissions)
- Your company must be licensed for Procore's Project Financials tools.
- The Change Events tool must be turned ON in your project.

## Steps

##### Â Note

The segments and items that you can select on your Procore project are unique to your project's specific WBS. Contact your company's Procore Administrator if you require assistance with creating a budget code for your environment.

1. Navigate to the project's **Estimating** tool.
2. Click the **Estimating** tab.
3. Select the **change order**.
4. Click the **Actions** menu and select one of the following options:

   1. **Create Change Event**

      - Enter a title and description for the new change event.
      - Update any settings as needed.

        - **Send Costs Only**: In this case only costs will be sent and your Cost ROM and Revenue ROM will be the same.
        - **Send the entire estimate including additional adjustments:** In this case, costs and adjustments are sent to the Change Events tool. Your Cost ROM and Revenue ROM may differ as Revenue ROM includes costs with adjustments.

          - **Profit, Overhead, Discount, Taxes, Others**: Select spread across estimate items or summarize into specific budget code. See [How do budget codes in an estimate create line items in a budget?](/faq-how-do-budget-codes-in-an-estimate-create-line-items-in-a-budget)

            - If summarizing into a specific budget code, click **Select** or the **current selection** to configure the cost code and cost type for each. Then click **Save Changes**.
      - *Optional*: Select '**Manage'** to make changes to the WBS segments and budget code structure.
   2. **Update Existing Change Event**

      - Select the existing change event you are updating from the **Change Event** dropdown menu.
      - Update any settings as needed.

        - **Send** **Costs Only**: In this case only costs will be sent and your Cost ROM and Revenue ROM will be the same.
        - **Send the entire estimate including additional adjustments:** In this case, costs and adjustments are sent to the Change Events tool. Your Cost ROM and Revenue ROM may differ as Revenue ROM includes costs with adjustments.

          - **Profit, Overhead, Discount, Taxes, Others**: Select spread across estimate items or summarize into specific budget code. See [How do budget codes in an estimate create line items in a budget?](/faq-how-do-budget-codes-in-an-estimate-create-line-items-in-a-budget)

            - If summarizing into a specific budget code, click **Select** or the **current selection** to configure the cost code and cost type for each. Then click **Save Changes**.
      - *Optional*: Select '**Manage'** to make changes to the WBS segments and budget code structure.
5. Click **Send to Change Event**.
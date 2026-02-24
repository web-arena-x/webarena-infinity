# Create a Commitment Potential Change Order from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-a-commitment-potential-change-order-from-a-change-event

---

## Background

Your project's change order tier configuration settings determines if you need to create a potential change order for a commitment:

- **1-Tier Change Orders**. You don't need to create a potential change order and can skip the Steps below. Instead, you simply create a commitment change order.
- **2-Tier Change Orders**. First, create a Change Event. Then, use the Steps below to create a potential change order for your commitment from the change event.

##### Â Note

If your project is using the optional Request for Quote (RFQ) feature in the Change Events tool, you can create the potential change order either before or after the RFQ has a response. However, if you wait until the RFQ has been reviewed and placed into the *Pending Final Approval* status, Procore will automatically populate the potential change order's Schedule of Values (SOV) with the RFQ amount.

## Things to Consider

- **Required User Permissions:**

 - You need one of the following:

    - 'Admin' level permissions on the project's Commitments tool.
    - 'Standard' level permissions on the project's Commitments tool and added to the 'Private' drop-down list and the 'Allow Standard Level Users to Create PCOs' configuration must be selected.
- **Requirements:**

 - The Change Events tool must be enabled on the project.
 - The Commitments tool must be configured for two-tier change orders.
- **Additional Information:**

 - After you create a change event, you have the option to create a RFQ.
 - On commitments, potential change orders can be transitioned into change orders.

## Prerequisites

1. Complete the steps in [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event).
2. *Optional:* Complete the steps in [Create RFQs from a Change Event](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event).

## Steps

1. Navigate to the project's **Change Events** tool.
2. Click the **Detail** tab.
3. Place a checkmark next to the change event line items to add to the potential change order.

   ##### Â Notes

   - To show only line items for a specific vendor, click **Add Filter** and then choose **Vendor** from the drop-down list.
   - You can select multiple line items from multiple change events.

- Click **Bulk Actions** and choose one of these options:

 - **Create a Commitment PCO** > **Contracts with Matching Cost Codes**If there are contracts with cost codes that match the change event line items you select, they will appear here for your selection.
 - **Create a Commitment PCO** > **Contracts**All other approved contracts will appear here for your selection.   
    *Note*: If an option is grayed out and dimmed, hover your mouse cursor over the tooltip to learn why.
- Under **General Information** in the New Potential Change Order page, enter the following information:

 - **Number**Procore automatically assigns the next available number to the potential change order. By default numbers are assigned as 001, 002, 002, and so on.

    ##### Â Tip

    - You can manually override this by typing over the number if desired. For example, you might want your numbering scheme to use three (3) leading zeros instead of two (2): 0001
    - If you override the default number, Procore automatically increments the numbering using your new entry and format.
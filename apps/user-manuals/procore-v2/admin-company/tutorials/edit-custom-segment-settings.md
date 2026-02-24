# Edit Custom Segment Settings

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/edit-custom-segment-settings

---

## Background

After you add a custom segment, you can edit its 'Segment Name' and its 'Project Level Actions' settings at any time. However, you are NOT permitted to modify its 'Segment Structure' setting. For example, you can change a segment named 'Phase' to 'Stage' and you can turn ON/OFF the Project level settings, but you cannot change a tiered segment to a flat segment (or vice versa).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - You cannot edit the 'Segment Structure' after a segment is created. For example, you cannot change a tiered segment to a flat segment or vice versa.
 - You can edit these settings for a 

    In Procore, a *custom segment* is a discrete category created for a company or project to breakdown your work into management components. Custom segments can be created in Procore's Work Breakdown Structure. Examples of custom segments your company or project team might want to create include:*Area*, *Location*, *Phase*, and so on.

    Custom Segment: 'Segment Name' and the checkboxes under 'Project Level Actions'.
 - You cannot edit the settings for a 

    In Procore, a segment is a discrete category that an organization uses to break down its work into manageable components. A default segment is one that is automatically provided for use with your Procore company account. Procore's WBS has two required default segments: cost code and cost type. It also has an optional default segment: sub job.

    Default Segment at any time.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)

## Steps

1. Navigate to the company's **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the 'Segment' that you want to work with.
4. Click the **Configure Settings** icon.
5. Edit the segment settings as follows:

   ##### Â Notes

   - You can only edit segment settings for custom segments. You cannot edit settings for a default segment. See [What is the difference between a default and custom segment in Procore's WBS?](/faq-what-is-the-difference-between-a-default-and-custom-segment-in-procores-wbs)
   - When editing a custom segment:

     - You can only update the 'Segment Name' and its settings under 'Project Level Actions'.
     - You are NOT permitted to edit its 'Segment Structure'.

- *Optional:* **Segment Name**. Type over the existing name with a new one. This is a required field.

- Click **Save**. The 'Segments' list is updated with your changes.
- Repeat the steps above for all of your company's segments with settings to edit. 
   You can continue by configuring the budget code structure for your company's Procore account.
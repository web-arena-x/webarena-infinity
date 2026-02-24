# Configure Settings: Company Level Work Breakdown Structure

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/configure-settings-company-level-work-breakdown-structure

---

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions to the company's Admin tool.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Click **Work Breakdown Structure**.
3. Click the **Configure Settings** icon.
4. Configure one or more of the following settings:

   - **Sub Jobs**. Make sub jobs an option on any projects within your Company.

     ##### Â Note

     Once sub jobs are in use on at least one project's budget code structure, this setting cannot be turned off.

- **Budget Code Structure Edits at Project Level**. This setting allows users to change the order of segments in the budget code structure at the Project level.
- **Custom Budget Code Descriptions**. This setting allows users to create custom budget code descriptions for all projects within your company.

 ##### Â Note

 Once this setting is enabled at the Company level, the budget code descriptions setting must be enabled on an individual project's Work Breakdown Structure configuration settings.

- **Copy Over WBS Sub Job and Cost Code Details When Project Templates Are Used**. When this setting is ON and you create a new project from a template, it will inherit **both** the company-level standard cost codes **and** any custom cost codes added specifically to that project template. It will also inherit sub-jobs (if enabled). To learn more, see [How do my project-specific 'Cost Code' segment items get carried over from a project template to a new project?](/faq-how-do-my-project-specific-cost-code-segment-items-get-carried-over-to-a-new-project-from-a-project-template) *Note*: Yardi VoyagerÂ® and MRI Platform XÂ® users creating a Procore project with this setting enabled must ensure that all cost codes in the project template also exist in the corresponding ERP project (Yardi VoyagerÂ® or MRI Platform XÂ®) before applying the template to the Procore project. See [Things to know about the Project Financials + Yardi VoyagerÂ® Connector](/product-manuals/yardi-voyager/things-to-know) or [Things to Know about the Project Financials + MRI Platform XÂ® Connector](/product-manuals/mri-project-financials/things-to-know).
- Click **Save**.
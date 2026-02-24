# What fieldset configurations are recommended for configurable fieldsets? - Procore

Source: https://support.procore.com/faq/what-fieldset-configurations-are-recommended-for-configurable-fieldsets

---

## Background

A Procore account user who has 'Admin' level permissions on the company's Admin tool can configure certain configurable fieldsets for supported tools.

With configurable fieldsets, you can control which fields are required, optional, or hidden. This simplifies the user interface and allows you to customize forms according to your company-specific requirements. For example, if you want to make sure everyone fills out the 'Contributing Behavior' field for an incident report, you can use configurable fieldsets to mark the field as 'Required'. These fieldset configurations will be reflected in your custom reports, allowing you to improve your analytics based on what's important to your company.

##### Note

If you apply a new configuration to a fieldset that is being used by an existing project, the new configuration will be applied when creating a form or updating its information. For example, if you change the 'Contributing Behavior' fieldset to be 'Required' for an observation, a user will be prompted to update the field when editing the observation.

By configuring tool fieldsets, you can create a company standard according to your business process to ensure consistency and prevent data entry errors. When you configure a fieldset, the fieldset will apply to all new projects with the option to apply it to existing projects. This makes it easier for users to adopt each tool. The answer below provides Procore's recommendations for default fieldset configurations, which are optimized for companies managing around $20M in annual construction volume.

For more information about configurable fieldsets, see [What are configurable fieldsets and which Procore tools support them?](https://support.procore.com/faq/what-are-configurable-fieldsets-and-which-procore-tools-support-them "What are configurable fieldsets and which Procore tools support them?")

For instructions on creating new configurable fieldsets, see [Create New Configurable Fieldsets](/products/online/user-guide/company-level/admin/tutorials/create-new-configurable-fieldsets "Create New Configurable Fieldsets") OR **click here to view the steps.**

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click the tool you want to create configurable fieldsets for.
3. Click the **Fieldsets** tab. 
   ![admin-fieldsets-tab.png](https://support.procore.com/@api/deki/files/121033/admin-fieldsets-tab.png?revision=2) 
   *Note:* Tools without other settings in the Company level Admin tool will open to this page automatically.
4. Click **Create Fieldset** and if required, select the fieldset type.
5. Enter a name for the fieldset, then click **Create**.
6. On the 'Edit Fieldset' page, each field name has the following options:
   - Click the toggle to the ON**![](/)**![icon-toggle-on.png](https://support.procore.com/@api/deki/files/93011/icon-toggle-on.png?revision=1&size=bestfit&width=25&height=25) position to make the field visible in the section. 
     OR Click the toggle to the OFF ![icon-toggle-off.png](https://support.procore.com/@api/deki/files/93010/icon-toggle-off.png?revision=1&size=bestfit&width=25&height=25) position to hide the field in the section.
     *Note:* A ![icon-toggle-on2.png](https://support.procore.com/@api/deki/files/243454/icon-toggle-on2.png?revision=1&size=bestfit&width=25&height=25) icon indicates that the field is visible by default and cannot be changed to hidden.
   - Mark the 'Required' checkbox to designate the field as required. 
     OR Clear the 'Required' checkbox to designate the field as optional.
     *Notes:*
     - Fields without a checkbox are optional by default and cannot be changed to required.
     - A gray marked checkbox ![icon-checkbox-marked-grayed-out.png](https://support.procore.com/@api/deki/files/243455/icon-checkbox-marked-grayed-out.png?revision=1&size=bestfit&width=17&height=17) indicates that the field is required by default and cannot be changed to optional.
7. *Optional:* If available, click **Create Section** to create a new section. See [Create Custom Sections](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-sections "Create Custom Sections").
8. Click **Save**.
9. In the 'Apply changes to [#] project(s)?' window, click **Assign Projects** to add the fieldset to projects.
   - In the 'Assign Projects' window, mark the checkbox next to each project you want to apply the fieldset to and click **Update**.
   - In the 'Apply changes to [#] project(s)?' window, click **Confirm**.
10. *Optional:* To set a fieldset as the default for new projects, click the ![icon-ellipsis-options-menu.png](https://support.procore.com/@api/deki/files/90868/icon-ellipsis-options-menu.png?revision=1&size=bestfit&width=4&height=15) icon at the end of its row on the 'Fieldsets' tab and select **Set as New Project Default**.

    ##### Note

    Projects created from a project template that includes fieldsets will inherit the fieldsets from the project template instead of your company's default fieldsets. See [Configure a Project Template](https://support.procore.com/products/online/user-guide/company-level/portfolio/tutorials/configure-a-project-template "Configure a Project Template").

---

## Answer

The tables below provide the recommended default fieldset configurations for providing a more simplified user interface with fewer required fields.

Note that a field name in GRAY italics indicates the field cannot be configured from its default setting.

##### Note

These fieldset configurations may be more appropriate for companies managing less than $20M (USD) in annual construction volume.

- [Project Admin](#Project_Admin "What fieldset configurations are recommended for configurable fieldsets?")
- [Directory](#Directory "What fieldset configurations are recommended for configurable fieldsets?")
- [Drawings](#Drawings "What fieldset configurations are recommended for configurable fieldsets?")
- [Incidents](#Incidents "What fieldset configurations are recommended for configurable fieldsets?")
- [Observations](#Observations "What fieldset configurations are recommended for configurable fieldsets?")
- [RFIs](#RFIs "What fieldset configurations are recommended for configurable fieldsets?")
- [Submittals](#Submittals "What fieldset configurations are recommended for configurable fieldsets?")
- [T&M Tickets](#T.26M_Tickets "What fieldset configurations are recommended for configurable fieldsets?")

### Project Admin

#### General Project Settings Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| Accounting Project ID/Number | Hidden |
| *Active* | *Required* |
| Actual Start Date | Hidden |
| Address | Required |
| Bid Type | Hidden |
| City | Required |
| *Country* | *Required* |
| County | Optional |
| Demo | Required |
| Departments | Hidden |
| Description | Optional |
| Designated Market Area | Hidden |
| Fax | Hidden |
| *Latitude* | *Optional* |
| Logo | Optional |
| *Longitude* | *Optional* |
| Office | Optional or Required |
| Owner Type | Hidden |
| Parent Project | Hidden |
| Phone | Required |
| Photo | Optional |
| Program | Hidden |
| Project Name | Required |
| Project # | Optional |
| Project Template | Optional |
| Projected finish date | Hidden |
| Region | Optional |
| Square Feet | Hidden |
| Stage | Optional |
| *State Code* | *Optional* |
| Store | Hidden |
| *Timezone* | *Required* |
| Type | Optional |
| Warranty End Date | Hidden |
| Warranty Start Date | Hidden |
| Zip Code | Required |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

---

### Directory

#### Person Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Active* | *Required* |
| Address | Required |
| Attachments | Hidden |
| Business Fax | Hidden |
| Business Phone | Hidden |
| Cell Phone | Required |
| City | Required |
| Company | Required |
| Country/State | Required |
| *Email* | *Required* |
| First Name | Required |
| Initials | Hidden |
| Is Employee Of | Optional |
| Job Title | Required |
| *Last Name* | *Required* |
| Send This User Messages | Hidden |
| Tags/Keywords | Hidden |
| Zip | Required |

#### Company Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| Abbreviated Name | Hidden |
| Address | Required |
| Attachments | Hidden |
| Business Phone | Required |
| City | Required |
| Contract Signer | Hidden |
| Country/State | Required |
| DBA | Hidden |
| Email address | Required |
| Entity Type | Hidden |
| Fax | Hidden |
| Invoice Contacts | Optional |
| Labor Union | Hidden |
| License Number | Required |
| *Name* | *Required* |
| Primary Contact | Optional |
| Tags/Keywords | Hidden |
| Website | Hidden |
| Zip | Required |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

---

### Drawings

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Drawing Number* | *Required* |
| Drawing Title | Required |
| Drawing Date | Optional |
| Drawing Received Date | Optional |
| *Drawing Set* | *Required* |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

---

### Incidents

#### Incident Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| Attachments | Optional |
| Contributing Behavior | Optional |
| Contributing Condition | Optional |
| Description | Required |
| Distribution | Optional |
| *Event Date/Time* | *Required* |
| Hazard | Required |
| Location | Optional |
| Private | Required |
| *Status* | *Required* |
| *Time Unknown* | *Required* |
| *Title* | *Required* |

#### Injury/Illness Record Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| Date Returned to Work | Required |
| Date of Death | Hidden |
| Filing Type | Required |
| Hospitalized Overnight | Required |
| *Injury/Illness* | *Required* |
| *Body Part Affected* | *Required* |
| Treated in ER | Optional |
| Treatment Facility | Optional |
| Treatment Facility Address | Optional |
| Treatment Provider | Optional |
| Workdays Absent | Required |
| Workdays Restricted | Required |
| Workdays Transferred | Optional |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

---

### Observations

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Assignee* | *Required* |
| Attachments | Optional |
| Contributing Behavior | Hidden |
| Contributing Condition | Hidden |
| Description | Required |
| Distribution | Optional |
| Due Date | Required |
| Hazard | Optional |
| Location | Optional |
| *Number* | *Required* |
| Priority | Optional |
| Private | Required |
| *Status* | *Required* |
| *Title* | *Required* |
| Trade | Hidden |
| *Type* | *Required* |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

### RFIs

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Assignees* | *Required* |
| Cost Code | Optional |
| Cost Impact | Optional |
| Distribution | Optional |
| Drawing # | Optional |
| *Due Date* | *Required* |
| Location | Optional |
| *Private* | *Required* |
| Project Stage | Optional |
| *RFI #* | *Required* |
| *RFI Manager* | *Required* |
| Received From | Optional |
| Reference | Hidden |
| Responsible Contractor | Optional |
| Schedule Impact | Optional |
| Spec Section | Optional |
| *Subject* | *Required* |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

---

### Submittals

| **Configurable Field** | **Recommendation** |
| --- | --- |
| Actual Delivery Date | Hidden |
| Attachments | Required |
| Confirmed Delivery Date | Hidden |
| Cost Code | Optional |
| Description | Required |
| Distribution | Optional |
| Final Due Date | Hidden |
| Issue Date | Hidden |
| Location | Optional |
| Number | Required |
| Private | Required |
| Received Date | Hidden |
| Received From | Required |
| Responsible Contractor | Required |
| Schedule Task | Hidden |
| Spec Section | Required |
| Status | Required |
| Sub Job | Hidden |
| Submittal Manager | Required |
| Submittal Package | Optional |
| Title | Required |
| Type | Optional |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

---

### T&M Tickets

#### General Information Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Description* | *Required* |
| *Performed On* | *Required* |
| *Status* | *Required* |
| Location | Optional |
| Ordered By | Optional |
| Reference # | Optional |
| Company Signee | Optional |
| Customer Signee | Optional |
| Notes | Optional |

#### Labor Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Employee* | *Required* |
| Classification | Optional |
| Time Type | Optional |
| *Hours* | *Required* |

#### Material Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Material Name* | *Required* |
| Material Description | Optional |
| *Unit* | *Required* |
| *Quantity* | *Required* |

#### Equipment Fieldsets

| **Configurable Field** | **Recommendation** |
| --- | --- |
| *Equipment Name* | *Required* |
| Equipment Description | Optional |
| *Unit* | *Required* |
| *Quantity* | *Required* |

[Back to Top](#Answer "What fieldset configurations are recommended for configurable fieldsets?")

## See Also

- [Create New Configurable Fieldsets](/products/online/user-guide/company-level/admin/tutorials/create-new-configurable-fieldsets "Create New Configurable Fieldsets")
- [Apply Configurable Fieldsets to Projects](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/apply-configurable-fieldsets-to-projects "Apply Configurable Fieldsets to Projects")
- [Edit Configurable Fieldsets](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/edit-configurable-fieldsets "Edit Configurable Fieldsets")
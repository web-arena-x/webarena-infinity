# Set Up your Payroll Export for use with Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/set-up-your-payroll-export-for-use-with-sage-300-cre

---

## Background

You can export data from the Company level Timesheets tool in Procore and import it directly into Payroll in Sage 300 CREÂ®. This allows self-performing contractors to spend less time formatting data, decreases duplicate data entry between time collection and payroll, and ensures a more accurate data flow.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- The following fields will need to match exactly between Procore and Sage 300 CREÂ®:

  - Employee & Employee ID
  - Classification (Certified or Union Class)
  - Pay ID & Time Type
  - Job & Project
  - JC extra & Sub Job
  - JC Cost Code & Cost Code
- **For companies using the ERP Integrations tool:**

  - The Project, Sub Job, and Cost Code fields sync automatically.

## Prerequisites

- You must have a license for the Company level Timesheets tool.

## Steps

1. Set Up a Time Entry View in Sage 300 CRE
2. Configure the Timesheets Tool in Procore

### Set Up a Time Entry View in Sage 300 CREÂ®

1. Log in to Sage 300 CREÂ®.
2. Select **Applications**.
3. Select **Payroll** from the list.
4. Select **Tools**.
5. Select **Customize Time Entry**.
6. Create a new time entry view.  
   *Note*: You must add a name and description for the time entry view, such as "Procore Time Import," before you can select the columns in the next step.
7. Double-click on the time entry column items in the same order that appears on the company's Timesheets tool in Procore.

   ##### Â Important

   - To successfully perform the import, the time entry view for Sage 300 CREÂ® must be configured to exactly match the format in Procore's Timesheets tool. In the table below, the asterisk (\*) indicates a required field.

   | **Column Name in Sage 300 CRE** | **Equivalent Column Name in Procore** |
   | --- | --- |
   | Date | Date |
   | Employee \* | Employee ID \* |
   | Job | Project |
   | JC Extra | Sub Job |
   | JC Cost Code | Cost Code |
   | Certified/Union class | Classification |
   | Pay ID \* | Time Type \* |
   | Units \* | Total Time \* |

   - To see cost type in Sage 300 CREÂ®, ensure that 'Pay ID' is associated with the correct JC Category (cost type) in Sage 300 CREÂ®. When imported, data in Procore's 'Time Type' is applied to the 'Pay ID' in Sage 300 CREÂ®. Time entries then populate the cost type that is assigned to the 'Pay ID'.
   - If you include **Union Class** column, you must also include these columns to the time entry view:

     - Union ID
     - Union local
     - Union class
   - To successfully import the **Union** columns into Sage 300 CREÂ®, the default *Union*, *Union local*, and *Union class* items must be assigned to each employee in the Employee Setup in Sage 300 CREÂ®.

- Click **Close**.

### Configure the Timesheets Tool in Procore

1. Navigate to the company's **Timesheets** tool.
2. Click **Configure Settings** .
3. In the **Settings** page, click the **Payroll** tab.
4. Scroll down to the **Payroll Export Settings** section.
5. In the **Payroll Software** drop-down list, select *Sage 300 CREÂ®*.
6. In the 'Columns in Sage 300 CREÂ®' list, check the boxes for the columns you want to include in your time entry view.

   ##### Â Notes

   - If you select the 'Classification' column, you must also select 'Certified Class' or 'Union Class'.
   - If you use custom fields in the Timesheets or My Time tools, select the checkboxes to include them in your export or clear them to exclude them.

- Click **Update**.
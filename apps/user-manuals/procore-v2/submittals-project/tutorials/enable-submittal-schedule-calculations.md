# Enable Submittal Schedule Calculations

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/enable-submittal-schedule-calculations

---

## Background

*Submittal Schedule Calculations* is an optional configuration feature that can be enabled for use with the Project level Submittals tool. When enabled on a Procore project, this option analyzes these key dates, which are entered by the creator under Submittal Schedule Information in a submittal package or a submittal item:

- Required On-Site Date
- Lead Time
- Design Team Review Time
- Internal Review Time

After analyzing the date entries, Procore automatically populates the calculated date values for the end user in the following fields:

- Planned Return Date
- Planned Internal Review Completed Date
- Planned Submit By Date

Based on the calculated date values above, Procore also suggests dates for the following fields:

- Submitter Due Date
- Approver Due Date

This helps the submittal creator ensure that submittal packages and items submitted to the review team are approved on schedule.

##### Example

When the 'Submittal Schedule Calculations' option is turned ON, you first enter a date in the 'Required On-Site Date' field. Next, enter a number of days in the 'Lead Time' box (e.g., enter â10â days) and note how the system will automatically enter a 'Planned Return Date' by subtracting the â10â day lead time from the 'Required On-Site Date'. The same is true for the 'Design Team Review Time' box (e.g., enter â7â days), which subtracts â7â days from the 'Planned Return Date' to calculate the automatic entry for the 'Planned Internal Review Completed Date'. Finally, enter a number of days in the 'Internal Review Time' box (e.g., enter â5â days) and Procore will subtract '5' days from the 'Internal Review Time' date to automatically calculate the 'Planned Submit By Date.'

## Things to Consider

- **Required User Permissions**:

  - 'Admin' level permission to the project's Submittals tool.
- **Requirements**:

  - The Submittals tool must be active on the project. See [Add and Remove Tools on a Project](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Demo

## Steps

1. Navigate to the Project level **Submittals** tool.  
    This reveals the Submittals page.
2. Click **Configure Settings** .   
    This reveals the Submittal Settings page.
3. Scroll down the page.
4. Place a checkmark in the **Enable Submittal Schedule Calculations** checkbox.
5. Specify a number of days in the boxes that appear. The default number of days is 14.

   - **Default Internal Review Time**
   - **Default Design Team Review Time**
6. Click **Update**.   
    The system saves your settings
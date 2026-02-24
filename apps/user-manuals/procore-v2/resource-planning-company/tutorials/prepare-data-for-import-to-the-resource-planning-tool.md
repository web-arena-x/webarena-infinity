# Prepare Data for Import to the Resource Planning Tool

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/prepare-data-for-import-to-the-resource-planning-tool

---

## Background

The Resource Planning tool at the Company level is Procoreâs construction resource management solution that provides real-time insight into your job assignments and availability.

To set up your Resource Planning tool, Procore offers data import to set up your projects, employees, and more. While only certain fields are required, it's recommended to fill out as much information as accurately as possible for the most complete setup.

## Things to Consider

- Customers can use this process one (1) time to set up their Resource Planning Tool.
- No special characters `` (~`!@#$%^&*()_{[}]|:;ââ<,>.?/) ``

##### Â Tip

- Fill out as much information as possible for the most complete setup.
- Review the spreadsheet for accuracy before submitting it.

## Steps

1. Navigate to the Company level **Resource Planning** tool.
2. Click the **Configure Settings**  icon.
3. Click **Data Upload**.
4. Click the **Excel Template** to open the Google Sheet.
5. Click **File** and select **Make a Copy**.
6. Fill out the following information in the template:

   - Groups **Show/Hide Fields**

     - **Required Fields**

       - **Group Name**. The title of Resource Planning group. Hyphens (-) are accepted. Example: Kansas City
       - **Group ID**. The abbreviated group identifier. Example: KS
       - **Time Zone**. The time zone of the group location.

         - America/Chicago
         - America/Los\_Angeles
         - America/New\_York
         - America/Denver
         - Australia/Brisbane
         - Australia/Sydney
         - Australia/Adelaide
         - Australia/Darwin
         - Australia/Perth
         - Pacific/Auckland
     - **Optional Fields**

       - **Address 1**. The address of the group location. Example: 1234 Main St
       - **Address 2**. The address of the group location. Example: Suite 320
       - **City/Town.** The city of the group location. Example: Kansas City
       - **State/Province**. The state abbreviation code of group location, formatted with all uppercase letters. Example: MO
       - **Postal Code.** The postal code of the group location (for US Customers). Example: 62113
       - **Country**. The country of the group location, formatted as a standard country code. Example: US
       - **Contact Name**. The name of the point of contact for the group. Example: John Smith
       - **Contact Phone Number**. The phone number for the group's point of contact.

         - The format is +[country code]XXXXXXXXXX.
         - Examples: +19135558225, or +6421345687.
       - **Contact Email**. The email address for the group's point of contact. Example: [test@test.com](mailto:test@test.com)
   - Job Titles **Show/Hide Fields**

     - **Required Fields**

       - **Job Title Name**. The name of the job title. Hyphens (-) are accepted. Example: Apprentice
       - **Job Title ID**. The abbreviated job title identifier. Example: APP
       - **Group ID(s)**. The group(s) the job titles are a part of. The ID must match Group ID in the 'Group' tab exactly. Example: KS

         - If there are more than one group, each group must be separated by a pipe (|) with no spaces. Example: KC|LA
         - If the job title belongs to all groups, type 'All'. Example: All
     - **Optional Fields**

       - **Job Title Color**. The HEX value associated with the Job Title. Example: #FFA500
   - Tags **Show/Hide Fields**

     - **Required Fields**

       - **Tag Name**. The name of certification/training/badging tag. Hyphens (-) are accepted. Example: OSHA 30
       - **5-Digit (Character) Identifier**. The abbreviated name of tag that can be easily identified on the Boards and List views. This field can support up to five characters. Example: OSH30
       - **Group IDs**. The groups the tags are a part of. The ID must match Group ID in the 'Group' tab exactly. Example: KS

         - If there is more than one group, each group must be separated by a pipe (|) with no spaces. Example: KC|LA
         - If the job title belongs to all groups, type 'All'. Example: All
       - **Does this Tag Expire? (Y/N).** Whether or not the tag can expire, like a certification. Example: Y
     - **Optional Fields**

       - **Tag Color (HEX value)**. The HEX value associated with the tag. Example: #FFA500
       - **# of Days Warning**. If this tag expires, a warning period (in days) can be set to notify users about expiring tags. Example: 60
       - **Categories**. The name of the tag category the tag belongs to. Example: Safety.

         - If there is more than one group, each group must be separated by a pipe (|) with no spaces. Example: Safety|Badging
   - Tag Categories **Show/Hide Fields**

     - **Required Fields**

       - **Category Name**. The category names that are used to organize tags. Example: Safety
   - People**Show/Hide Fields**

     - **Required fields**

       - **First Name**. The first name of employee. Hyphens (-) and apostrophes (') are accepted. Example: John
       - **Last Name**. The last name of the employee. Example: Smith
       - **Group ID(s) Available To**. Which groups the employees should be visible.

         - The ID must match Group ID in the 'Group' tab exactly. Example: KS
         - If there is more than one group, each group must be separated by a pipe (|) with no spaces. Example: KC|LA
         - If the job title belongs to all groups, type 'All'. Example: All
       - **Status (active/inactive)**. The current status of the employee. Example: active
       - **Assignable (Y)**. All employees must be added as assignable in the data upload. After the data upload is complete, you can update this in the Resource Planning tool. Example: Y
       - **Employee ID**. The employee's ID number. Example: B18283
     - **Optional Fields**

       - **Job Title ID**. The job title ID of the employee. The ID must match the Job Title ID exactly. Example: APP
       - **Date of Hire (MM/DD/YYYY)**. The date the employee was hired. Example: 01/26/2016
       - **Hourly Wage (XX or XX.XX)**. The employee's hourly rate. Example: 25.50
       - **Mobile Phone**. The employee's mobile number.

         - The format is +[country code]XXXXXXXXXX.
         - Examples: +19135558225, or +6421345687.

           ##### Â Note

           The same phone number can not be uploaded for different employees. Please remove any duplicate phone numbers.

     - **Can Receive SMS (Y/N)**. Whether the employee should receive alerts and messages via SMS. Example: Y
     - **Email**. The employee's email address. Example: [test@test.com](mailto:test@test.com)

       ##### Â Note

       - If possible, this should be their work email address as this will be their log in to Procore, and receive notifications from Resource Planning.
       - The same email address can not be uploaded for different employees. Please remove any duplicate email addresses.
   - **Can Receive Email (Y/N)**. Whether the employee should receive alerts and messages via email. Example: Y
   - **Address 1**. The employee's address. This is required for the employee to appear on the Resource Planning map. Example: 1234 Main St
   - **Address 2**. The employee's address. Example: Suite 320
   - **City/Town**. The employee's city. This is required for the employee to appear on the Resource Planning map. Example: Kansas City
   - **State/Province**. The employee's state abbreviation code, formatted with all uppercase letters. This is required for the employee to appear on the Resource Planning map. Example: MO
   - **Postal Code**. The employee's postal code (for US Customers). This is required for the employee to appear on the Resource Planning map. Example: 62113
   - **Country**. The employee's country, formatted as a standard country code. Example: US
   - **Date of Birth (MM/DD/YYYY)**. The employee's date of birth. Example: 01/26/1980
   - **Gender (M/F)**. The employee's gender. Example: M
   - **Emergency Contact Name**. The name of the employee's emergency contact. Example: Jane Smith
   - **Emergency Contact Relationship**. The relationship between the employee and their emergency contact. Example: Spouse
   - **Emergency Contact Phone Number**. The phone number of the employee's emergency contact.

     - The format is +[country code]XXXXXXXXXX.
     - Examples: +19135558225, or +6421345687.
   - **Emergency Contact Email**. The email address for the employee's emergency contact. Example: [test@test.com](mailto:test@test.com)
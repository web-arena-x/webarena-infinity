# Prepare Equipment Records for Import to the Company Equipment Tool

Source: https://v2.support.procore.com/product-manuals/equipment-company/tutorials/prepare-equipment-records-for-import-to-the-company-equipment-tool

---

## Background

Procore's Equipment tool ensures all machines are optimally used and effectively managed from arrival to departure. The company's Equipment tool is a registry of your company's owned or rented equipment for your job sites. When equipment is assigned to projects, it is added to the Project's Equipment tool where it can be used in Inspections, Timesheets, Daily Log, T&M Tickets, and your Budget.

You can import your equipment into the Equipment tool instead of creating the records manually.

## Things to Consider

- [Required User Permissions](/product-manuals/equipment-company/permissions)
- Imported equipment categories, types, makes, models, and custom statuses are added to the tool's configuration settings.
- The fields Equipment ID, Status Type, Status, Category, Type and Ownership are required.
- If using the following custom statuses, the must have the following status types:

 - 'Available' needs an 'Available' status type.
 - 'Active' needs an 'In Use' status type.
 - 'Inactive' needs an 'Unavailable' status type.
- The document must be in .xlsx format.

## Steps

1. Navigate to the company's **Equipment** tool.
2. Click **Import**.
3. Click **Download Excel Template** to download the template.
4. Enter your equipment information into the spreadsheet:

   - **Equipment ID**. The unique ID for the piece of equipment.
   - **Name**. The name of the equipment.
   - **Status Type**. The category for the custom status:\* Available\* In Use\* Unavailable
   - **Status**. The custom status name. See [Configure Custom Statuses for Equipment](/product-manuals/equipment-company/tutorials/configure-custom-statuses-for-equipment).
   - **Category**. The category of equipment. Example: Earthmoving Equipment, Lifting Equipment, etc.
   - **Type**. The type of equipment. Example: Cement Mixer, Skid Steer, etc.
   - **Make**. The equipment's make.
   - **Model**. The equipment's model.
   - **Year**. The year the equipment was made. The year must be between 1970-Present.
   - **Serial #**. The equipment's serial number.
   - **Notes**. Any notes about the equipment.
   - **Ownership**. Who owns the equipment:\* Owned\* Rented\* Subcontracted
   - **Rate/Hr**. The equipment's rate per hour in decimal format.
5. Save the file.

## Next Step

- [Import Equipment Records](/product-manuals/equipment-company/tutorials/import-equipment-records-in-the-company-equipment-tool)
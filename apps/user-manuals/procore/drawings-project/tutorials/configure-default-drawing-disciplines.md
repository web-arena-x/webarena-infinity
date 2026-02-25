# Configure Default Drawing Disciplines

Source: https://v2.support.procore.com/product-manuals/drawings-project/tutorials/configure-default-drawing-disciplines

---

## Background

When you upload drawings into Procore, the Discipline field should automatically populate based off information on the drawing. By default, there are several abbreviations that are mapped to the most common industry standard disciplines, such as Architectural, Civil, and Electrical. However, you can change the default abbreviation mappings or add custom ones for the project as needed.

If the discipline for the drawing is not populated or does not appear on the drawing, you can also choose to enter a new discipline manually while reviewing and confirming drawings. See [Review and Confirm Drawings](/process-guides/user-guide-bidding-and-estimating-integration/review-and-confirm-drawings). After confirming the drawing, the new discipline will be added to the Discipline Abbreviation Setup list for the project and can be selected for other drawings.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' on the project's Drawings tool.
- **Additional Information:**

 - Abbreviation mappings are project-specific settings and can be changed at any time, which will affect any newly uploaded drawings. Changes will not affect previously uploaded drawings.
 - Abbreviation mappings are not case sensitive.
 - Abbreviation mappings will only affect new drawings that uploaded into a project. If a drawing is a revision of a previously uploaded drawing, it will inherit the previous version's discipline.
 - An abbreviation can only be mapped to a single drawing discipline.
 - Add additional abbreviation mappings, as necessary. For example, if you want to use 'H' for "Hazardous Materials" instead of "HVAC" you can change the default abbreviation mapping from 'H' to 'HV' and then create a new discipline mapping for 'H' that maps to the "Hazardous Materials" discipline.

#### Default Drawing Discipline Abbreviation Mappings

- A - Architectural
- C - Civil
- E - Electrical
- F - Fire Protection
- G - General
- GA - Garage Architectural
- GE - Garage Electrical
- GM - Garage Mechanical
- GP - Garage Plumbing
- GS - Garage Structural
- H - HVAC
- I - Interior
- L - Landscape
- M - Mechanical
- P - Plumbing
- Q - Equipment
- R - Resource
- S - Structural
- T - Telecommunications
- X - Other
- Z - Contractor / Shop Drawings

## Steps

1. Navigate to your project's **Drawings** tool.
2. Click the **Configure Settings** icon.
3. Click **Discipline Abbreviation Setup** to navigate to the drawing discipline abbreviation setup page.
4. Click on the discipline name or abbreviation to modify an existing entry. 
   *Note*: Click out of the field to save changes.
5. To add a new abbreviation, enter an abbreviation and discipline name, then click +**Add**. 
   *Note*: Changes are automatically saved after this step.
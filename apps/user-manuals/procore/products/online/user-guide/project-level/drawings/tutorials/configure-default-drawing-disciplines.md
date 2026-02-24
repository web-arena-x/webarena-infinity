# Configure Default Drawing Disciplines - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/configure-default-drawing-disciplines

---

## Objective

To set up the abbreviation mappings that are used to auto-fill drawing disciplines when uploading new drawings.

## Background

When you upload drawings into Procore, the Discipline field should automatically populate based off information on the drawing. By default, there are several abbreviations that are mapped to the most common industry standard disciplines, such as Architectural, Civil, and Electrical. However, you can change the default abbreviation mappings or add custom ones for the project as needed.

If the discipline for the drawing is not populated or does not appear on the drawing, you can also choose to enter a new discipline manually while reviewing and confirming drawings. See [Review and Confirm Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/review-and-confirm-drawings "Review and Confirm Drawings"). After confirming the drawing, the new discipline will be added to the Discipline Abbreviation Setup list for the project and can be selected for other drawings.

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

1. Navigate to your project's **Drawings** tool.
2. Click the **Configure Settings** ****![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)**** icon.
3. Click **Discipline Abbreviation Setup** to navigate to the drawing discipline abbreviation setup page.
4. Click on the discipline name or abbreviation to modify an existing entry.  
   *Note*: Click out of the field to save changes.
5. To add a new abbreviation, enter an abbreviation and discipline name, then click +**Add**.  
   *Note*: Changes are automatically saved after this step.  
     
   ![default drawing discipline set up.png](https://support.procore.com/@api/deki/files/1277/default_drawing_discipline_set_up.png?revision=1&size=bestfit&width=700&height=121)

## See Also

- [Configure Advanced Settings: Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/configure-advanced-settings-drawings "Configure Advanced Settings: Drawings")
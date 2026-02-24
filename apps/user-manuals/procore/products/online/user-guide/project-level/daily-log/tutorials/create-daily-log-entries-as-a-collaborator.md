# Create Daily Log Entries as a Collaborator - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-daily-log-entries-as-a-collaborator

---

## Objective

To create a daily log entry as an external collaborator in a project's Daily Log tool.

## Background

If you are an external collaborator working in another account's Daily Log tool in Procore, you can create log entries if you have the appropriate permissions. An Admin user on the project's Daily Log tool will need to approve your entry before it can be finalized on the log.

## Things to Consider

- **Required User Permissions:**
  - 'Read Only' or 'Standard' on the project's Daily Log tool with the ['Collaborator Entry Only' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Daily_Log "Grant Granular Permissions in a Permission Template") enabled on your permissions template.
    - The granular permission for 'Collaborator Entry Only' has to be on a global permission template OR a project permission template before the option is available in the Daily Log configuration settings.
    - The additional granular permission 'View entries associated to users within the same company' gives users access to view collaborator entries made by other users at their company.
- **Additional Information:**
  - If you are a collaborator for the project, the following conditions apply:
    - You can only see the logs that the project has enabled Collaborator Entry for.   
      *Note: Not all log types support Collaborator Entry.*
    - You can only select your own company or users from your company in the drop-down menus.
    - You can edit or delete your entries until they have been approved.
    - If you only have the 'Collaborator Entry Only' granular permission, you can only see the entries that you have submitted. If you also have the granular permission to 'View entries associated to users within the same company,' you can view other collaborator entries made by users at your same company.

## Steps

1. Navigate to the **Daily Log** tool.
2. Select the date you want to add entries to.
3. Scroll to the applicable log.  
   OR  
   Click the 'Create' button at the top of the Daily Log page and select the log type you want to create. The page then navigates you to the appropriate section of the log.
4. Fill out the appropriate information for each entry.  
   *Note:* Visit Daily Log for Web, iOS, or Android to view lists of articles that provide instructions for each log type.

## Next Step

- A Daily Log 'Admin' user will need to [Approve Daily Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/approve-or-reject-daily-log-entries "Approve Collaborator-submitted Daily Log Entries").

## See Also

- [Grant Granular Permissions in a Permission Template](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template "Grant Granular Permissions in a Permission Template")
- [Configure Advanced Settings: Daily Log](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/configure-advanced-settings-daily-log "Configure Advanced Settings: Daily Log")
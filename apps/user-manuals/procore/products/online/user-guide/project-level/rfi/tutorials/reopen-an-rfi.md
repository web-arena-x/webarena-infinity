# Reopen an RFI - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/reopen-an-rfi

---

## Objective

To reopen an RFI that has been previously closed.

## Background

After an RFI has gone through its workflow and all responses have been logged in Procore, users with the appropriate permissions can change its open status to 'Closed.' In Procore, a closed RFI indicates that the question has been resolved and requires no further action. If a closed RFI needs additional action, best practice is to [issue a revision](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/revise-an-rfi "Revise an RFI (Beta)"). If small corrections are needed on a closed RFI, follow the steps below to reopen the RFI.

## Things to Consider

- **Required User Permission**:
  - 'Admin' level permission on the project's RFIs tool.  
    OR
  - 'Read Only' or 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on your permission template AND be the RFI's creator ('Standard' only) or RFI Manager.
- **Prerequisites**:
  - [Close an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/close-an-rfi "Close an RFI")
- **Additional Information**:
  - When you reopen an RFI, it returns to the status it was in when it was closed. For example, if you close a 'Draft' RFI, it returns to the 'Draft' status when reopened. If you close an 'Open' RFI, it returns to the 'Open' status when reopened.

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. In the **Add Filters** drop-down list, select *Status*. Then choose *Closed* from the secondary drop-down list.   
   This narrows the list to show only RFIs in the 'Closed' status.
4. Click **View** next to the RFI you want to reopen.

   ##### Tip

   Before you reopen the RFI, you can edit the **Distribution List** to add one or more users from the company in the **Responsible Contractor** field. See [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI"). If the RFI email settings for the project are configured to send emails to users on an RFI's **Distribution List** when an RFI is reopened, adding those users to the **Distribution List** will ensure they receive an email notification when the RFI is reopened. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")
5. Click **Reopen RFI**.  
     
   The system reopens the RFI and places it into the status it was in prior to being closed.   
   Emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")

## See Also

- [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")
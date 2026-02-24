# How do I control which emails are sent by Procore during the RFI process? - Procore

Source: https://support.procore.com/faq/how-do-i-control-which-emails-are-sent-by-procore-during-the-rfi-process

---

## Answer

The project's RFIs tool sends out various automatic email notifications when certain tasks are completed for an RFI. These tasks are referred to as **Email Events** in the **RFI Emails** table in the **RFI Settings** page. The table below shows the default email notification settings, but users with the appropriate permissions can modify these settings. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs").

| **Email Event** | **Enable Email** | **Creator** | **RFI Manager** | **Assignees** | **Distribution  Group** |
| --- | --- | --- | --- | --- | --- |
| Ball In Court Shift 1 | icon-green-checkmark.png | icon-x-red.png | icon-x-red.png | icon-x-red.png | icon-x-red.png |
| Closed | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png |
| Created | icon-green-checkmark.png | icon-x-red.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png |
| Draft Created | icon-green-checkmark.png | icon-x-red.png | icon-green-checkmark.png | icon-x-red.png | icon-x-red.png |
| Due Date Changed | icon-green-checkmark.png | icon-x-red.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-x-red.png |
| Reassigned | icon-green-checkmark.png | icon-x-red.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png |
| Reopened | icon-green-checkmark.png | icon-x-red.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png |
| Response Added 2, 3 | icon-green-checkmark.png | icon-x-red.png | icon-green-checkmark.png | icon-green-checkmark.png | icon-green-checkmark.png |

1When 'Ball In Court Shift' emails are enabled and the Ball In Court responsibility for an RFI is shifted manually (see [Shift the Ball In Court on an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/shift-the-ball-in-court-on-an-rfi "Shift the Ball In Court on an RFI")), Procore sends an automatic email notification to the user who the Ball In Court responsibility shifted to (the item's RFI Manager or Assignee), even if no user checkboxes are marked in the **RFI Emails** table.

2 When 'Response Added' emails are enabled and the **Only Show Official Response to Standard and Read Only Users** checkbox is marked (see [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs")), an RFI's creator who has 'Standard' level permissions on the tool will not receive an email when a response is added to the RFI, even if the 'Creator' checkbox is marked in the **RFI Emails** table.

3 When 'Response Added' emails are enabled and the **Only Show Official Response to Standard and Read Only Users** checkbox is marked (see [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs")), an RFI's creator who has 'Standard' level permissions on the tool will receive an email when a response on the RFI is marked 'Official' if the 'Creator' checkbox is marked in the **RFI Emails** table. *Note:* Other users with roles on the RFI will not receive an email when a response on the RFI is marked 'Official', even if checkboxes for their roles are marked in the **RFI Emails** table.

## Examples

[When does the RFIs tool send email notifications?](#s29112)

## See Also

- [Configure Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Settings: RFIs")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").
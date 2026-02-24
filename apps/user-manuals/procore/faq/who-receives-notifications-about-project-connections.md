# Who receives notifications about project connections? - Procore

Source: https://support.procore.com/faq/who-receives-notifications-about-project-connections

---

## Background

[Overview-Connection Manager](#s214925)

## Answer

By default, anyone who is a full company Admin and is added to that project's Directory will receive a notification. If you want different users to be notified, you can configure the email notification distribution list in each project's Connection Manager settings. See [Connection Manager: Configure Advanced Settings](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager").

The following matrix describes notification behavior and configuration options:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Notification Event | Which company receives a notification? | Which users receive a notification? | Where are the settings for this notification configured? | How can this notification be configured? |
| **Connection Requested** | Upstream | Users with full Company Admin permissions.    *\*Note: Excludes Company Admin users unless they are members of the Project Directory.* | Connection Manager > Configuration Settings | Can be limited to only selected Connection Manager Admin users. Company Admins can be added. |
| **Connection Request Rejected** | Downstream | Users with full Company Admin permissions.    *\*Note: Excludes Company Admin users unless they are members of the Project Directory.* | Connection Manager > Configuration Settings | Can be limited to only selected Connection Manager Admin users. Company Admins can be added. |
| **Connection Created** | Both Upstream and Downstream | Users with full Company Admin permissions.    *\*Note: Excludes Company Admin users unless they are members of the Project Directory.* | Connection Manager > Configuration Settings | Can be limited to only selected Connection Manager Admin users. Company Admins can be added. |
| **Initial Sync Complete** | Downstream | All users with Admin level permissions on the project's Drawings tool. | Drawings Tool > Configuration Settings | Can be limited to only selected Drawings Tool Admin users. |
| **New Drawings Published in Upstream Account** | Downstream | All users with Admin level permissions on the project's Drawings tool. | Drawings Tool > Configuration Settings | Can be limited to only selected Drawings Tool Admin users. |
| **Drawings Deleted in Upstream Account** | Downstream | All users with Admin level permissions on the project's Drawings tool. | Drawings Tool > Configuration Settings | Can be limited to only selected Drawings Tool Admin users. |
| **Connection Disabled** | Both Upstream and Downstream | Users with full Company Admin permissions.    *\*Note: Excludes Company Admin users unless they are members of the Project Directory.* | Connection Manager > Configuration Settings | Can be limited to only selected Connection Manager Admin users. Company Admins can be added. |

## See Also

- [About Connectability](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/about-procore-connect "About Connectability")
- [Connection Manager: Configure Advanced Settings](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager")
# Configure Alerts and Severity for Incidents

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/configure-alerts-and-severity-for-incidents

---

## Background

Configuring severity and alerts for the Incidents tool allows users to automatically notify key stakeholders about incident records based on the filing type of the incident record. While these settings are configured at the Company level, a user's ability to view incident and incident record details are based on their permissions to the Incidents tool in each Procore project.

## Things to Consider

- **Required User Permissions**:

 - *To configure Severity, remove Alert Recipients, and manage Alert Types*:

    - 'Admin' level permissions on the Company level Admin tool.
 - *To add Alert Recipients, you need both of the following*:

    - 'Admin' on the Company level Admin tool
    - 'Read Only' level permissions or higher on the Company level Directory tool.

## Steps

We recommend that you start with Configure Severity before you Configure Alerts. If your company has already configured severity settings for the Incidents tool, continue to Configure Alerts.

#### Configure Severity

##### General

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Incidents**.
3. Click the **Severity** tab.
4. Under 'General', complete the following:

   - **Number of Severity Levels**: Choose between '4' and '5'.
   - **Severity Level Labels**: Enter a name for each color-coded level.
   - **Order of Severity Levels**: Choose between 'Ascending' (1 representing the lowest level and 5 representing the highest level) and 'Descending' (1 representing the highest level and 5 representing the lowest level).
5. Click **Update**.

##### Injury/Illness

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Incidents**.
3. Click the **Severity** tab.
4. Under 'Injury/Illness', select a severity level for each filing type.
5. Click **Update**.

#### Configure Alerts

##### Alert Recipients

##### Â Note

Any user can be added to an 'Alert Recipient' list to receive alert push notifications and emails for the projects they are added to, but they need 'Read Only' level permissions or higher on a project's Incidents tool in order to view the record associated with the alert.

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Incidents**.
3. Click the **Alerts** tab.
4. In the 'Alert Recipients' column, do one of the following:

   - Click **+Add Recipients** next to the severity level you want to configure alerts for.
   - Click **(#)** **Recipients** if the severity level already has one or more alert recipients.
5. Click the triangle icon in the 'Edit Alert Recipients' window to open the search bar.
6. Enter the user's name you want to send alerts to and select their name. You can search by their first name or last name and suggested users display as you type.
7. Continue adding as many users as needed.
8. Click the X next to a user's name to remove them from the alert recipients list.
9. Press ESC on your keyboard to close the drop-down menu.
10. Click **Update**.

##### Alert Types

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Incidents**.
3. Click the **Alerts** tab.
4. In the 'Alert Types' column next to the severity level you want to configure alerts for, select 'Email', 'Push (iOS and Android)', or both options. *Note:* Users can choose whether to enable push notifications from Procore on their devices. See [Manage Project Settings (iOS)](/process-guides/getting-started-procore-app-ios/manage-project-settings) and [Manage Project Settings (Android)](/process-guides/getting-started-procore-app-android/manage-project-settings).

## Next Steps

[Add an Injury/Illness Record to an Incident](/product-manuals/incidents-project/tutorials/add-an-injury-illness-record-to-an-incident)
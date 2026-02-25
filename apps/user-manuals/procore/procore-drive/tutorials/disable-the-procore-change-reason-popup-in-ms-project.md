# Disable the Procore Change Reason Pop-up in MS Project

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/disable-the-procore-change-reason-popup-in-ms-project

---

## Background

When you sync a MS Project schedule to Procore Drive, any changes you make in MS Project will automatically be synced to Procore Drive and Procore upon clicking **Save**. By default, Procore will ask you for a change reason when changes are made so you and your team can keep track of why changes to the schedule were made, by whom, and when. If you would like to disable this prompting by Procore, you can disable the Add-in in MS Project. However, the changes to the schedule will still be synced.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Schedule tool; access to the project's MS Project schedule that is synced to Procore.
- **Additional Information:**

  - ***Important!*** Keep the Procore add-in online to view schedule changes in the Schedule Changes report in the Reports tool. The report will not gather data unless a user enters information into this pop-up.
  - Uninstalling the Procore add-in from MS Project will require a full uninstall and reinstall of Procore Drive if you want to reinstall the add-in.

## Steps

You can either disable it temporarily, or uninstall it permanently.

- [To disable the add-in temporarily](#steps)
- [To uninstall the add-in](#steps)

##### To disable the Add-in temporarily

1. Open MS Project on your computer.
2. If it is available, click the **Add-ins** tab.  
   *Note*: If this feature is not available, skip to [here](#steps).
3. Click the **Online** button above the word "Procore".  
   *Note*: This will disable the comment popup add-in until you enable it again by turning it to online again.

##### To uninstall the Add-in

##### Â Important

If you want to re-install the add-in, you will need to uninstall Procore Drive, re-install Procore Drive, then launch a MS Project file from the Schedules tab in Procore Drive.

1. Open MS Project on your computer.
2. Click **File**.
3. Click **Options**.
4. Click the **Add-ins** tab to the left of the options menu.
5. To the right of the word "Manage", select "COM Add-ins" from the drop-down menu.
6. Click **Go...**
7. Select the Procore Add-in.  
   *Note*: You may see two Procore Add-ins. If so, disable both.
8. Click **Remove**.  
   *Note*: This will uninstall the comment request popup permanently unless you reinstall it.
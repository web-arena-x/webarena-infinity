# Configure Advanced Settings: Photos

Source: https://v2.support.procore.com/product-manuals/photos-project/tutorials/configure-advanced-settings-photos

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Photos tool.  
    *Note:* Some features explained here require 'Admin' permissions on the project's Directory tool.

## Steps

1. Navigate to your project's **Photos** tool.
2. Click the **Configure Settings**  icon.
3. Set your preferences for the following:

   - Photo Settings
   - Inbound Email Options
   - Photos from Other Tools
   - Permissions Table

#### Photo Settings

1. Click on the **Photo Settings** page.
2. Set your preferences for the following:

   - **Project Photos Subscribers**: Select team members from this drop-down menu to have Procore automatically send them an email when new photos are added to the project.
   - **When new albums are created, add them:** (to the beginning of the list / to the end of the list): Click the button next to the option you prefer.
   - **âMake photos uploaded to the Photos tool private by default**: Mark the checkbox to have photos uploaded to the Photos tool private by default so only Admin users can view them.

##### Inbound Email Options

The inbound email address for the Photos tool is listed under Inbound Address.

Depending on the inbound email setting selected below, photos can be added directly to the Photos tool by sending an email containing photos to the inbound email address (shown above). Configure who can send emails to the Photos tool by selecting one of the following:

- **Allow anyone to send inbound emails to the Photos tool**: Select this option if you do *not* want to restrict who can send inbound emails to the Photos tool. While this is selected, anyone who knows the inbound email address listed in the Photos tool's configure settings can send an email containing photos (which will be added to the Photos tool).
- **Only allow Photos tool Admins to send inbound emails to the Photos tool**: Select this option if you want to allow photos from an inbound email to be added to the Photos tool, but only those sent by users with 'Admin' permissions to the Photos tool.
- **Disable all inbound emails to the Photos tool**: Select this option if you do not want any photos to be added from an inbound email. While this is selected, any emails sent to the Photos tool's inbound email address will be blocked.

See [Who can send emails and files into Procore?](/faq-who-can-send-emails-and-files-into-procore) for more information on inbound emails and the settings that are available.

#### Photos from Other Tools

***Important!*** The following options can only be configured by users with 'Admin' permissions to the project's Photos tool AND Directory tool:

- **Default album for emailed photos:** Select an album for photos that have been added through an inbound email to the Photos tool. See Inbound Email Options above.
- **Import photos from Drawings to the Photos tool**: Enable or disable photo aggregation from the Drawings tool. See [Add Photos to a Drawing](/product-manuals/drawings-project/tutorials/add-photos-to-a-drawing).

  - **Default album for Drawing photos**: By default, Procore will make a new album automatically called "Photos from Drawings" to which all photos added to drawings will be uploaded. From the drop-down menu, select a different destination album if desired.  
    *Note*: To configure the privacy settings for the album you select, see [Mark an Album as Private](/product-manuals/photos-project/tutorials/mark-an-album-as-private).
  - **Make Drawings photos private by default**: This setting configures the privacy settings of individual photos imported from the drawings tool. By default, photos added to drawings and then aggregated into the Photos tool will be viewable by all users who have access to the Photos tool. If you want to hide these photos from anyone but 'Admin' users on the Photos tool, mark the checkbox.  
    *Note*: The privacy settings for the album that photos from the Drawings tool are imported into are respected.
- **Import photos from Daily Log to the Photos tool**: Enable or disable photo aggregation from the Daily Log tool. See [Add a Photo to a Daily Log Entry](/product-manuals/daily-log-project/tutorials/add-a-photo-to-a-daily-log-entry).   
  *Note*: Disabling this setting will only prevent photos that are added as attachments to daily log entries from being uploaded to the Photos tool. If photos are uploaded directly to the Photos log in the Daily Log tool, they will still be added to the Photos tool.

  - **Default album for Daily Log photos**: By default, Procore will make a new album automatically called "Photos from Daily Log" to which all photos added to daily log entries will be uploaded. From the drop-down menu, select a different destination album if desired.  
    *Note*: To configure the privacy settings for the album you select, see [Mark an Album as Private](/product-manuals/photos-project/tutorials/mark-an-album-as-private).
  - **Make Daily Log photos private by default**: By default, photos added to daily log entries and then aggregated into the Photos tool will only be viewable by 'Admin' users on the Photos tool. If you want to expose these photos to all users who have access to the Photos tool, unmark the checkbox.  
    *Note*: The privacy settings for the album that photos from the Daily Log tool are imported into are respected.
- **Import photos from Punch List to the Photos tool**: Enable or disable photo aggregation from the Punch List tool.   
  See [Add a Photo to a Punch List Item](/product-manuals/punch-list-project/tutorials/add-photos-to-a-punch-list-item-so-that-it-populates-in-the-photos-tool).

  - **Default album for Punch List photos**: By default, Procore will make a new album automatically called "Photos from Punch List" to which all photos added to punch list items will be uploaded. From the drop-down menu, select a different destination album if desired.  
    *Note*: To configure the privacy settings for the album you select, see [Mark an Album as Private](/product-manuals/photos-project/tutorials/mark-an-album-as-private).
  - **Make Punch List photos private by default**: By default, photos added to punch list items and then aggregated into the Photos tool will only be viewable by 'Admin' users on the Photos tool. If you want to expose these photos to all users who have access to the Photos tool, unmark the checkbox.  
    *Note*: The privacy settings for the album that photos from the Punch List tool are imported into are respected.
  - **Include photos from private Punch List:** Select this checkbox to include photos from punch lists marked as 'Private.'
- **Import photos from observations to the Photos tool**: Enable or disable photo aggregation from the Observations tool.   
  See [Add a Photo to an Observation](/product-manuals/observations-project/tutorials/add-a-photo-to-an-observation-so-that-it-populates-in-the-photos-tool).

  - **Default album for observation photos**: By default, Procore will make a new album automatically called "Photos from Observations" to which all photos added to observations will be uploaded. From the drop-down menu, select a different destination album if desired.  
    *Note*: To configure the privacy settings for the album you select, see [Mark an Album as Private](/product-manuals/photos-project/tutorials/mark-an-album-as-private).
  - **Make observation photos private by default**: By default, photos added to observations and then aggregated into the Photos tool will marked as private and therefore only be viewable by 'Admin' users on the Photos tool. If you want to expose these photos to all users who have access to the Photos tool, unmark the checkbox.  
    *Note*: The privacy settings for the album that photos from the Observations tool are imported into are respected.
  - **Include photos from private Observations:** Select this checkbox to include photos from Observations marked as 'Private.'
- **Import photos from inspections to the Photos tool**: Enable or disable photo aggregation from the Inspections tool.   
  See [Add a Photo to an Inspection](/product-manuals/inspections-project/tutorials/add-a-photo-to-an-inspection-so-that-it-populates-in-the-photos-tool).

  - **Default album for inspections photos**: By default, Procore will make a new album automatically called "Photos from Inspections" to which all photos added to inspections will be uploaded. From the drop-down menu, select a different destination album if desired.  
    *Note*: To configure the privacy settings for the album you select, see [Mark an Album as Private](/product-manuals/photos-project/tutorials/mark-an-album-as-private).
  - **Make inspection photos private by default**: By default, photos added to inspections and then aggregated into the Photos tool will marked as private and therefore only be viewable by 'Admin' users on the Photos tool. If you want to expose these photos to all users who have access to the Photos tool, unmark the checkbox.  
    *Note*: The privacy settings for the album that photos from the Inspections tool are imported into are respected.
  - **Include photos from private Inspections:** Select this checkbox to include photos from Inspections marked as 'Private.'

#### Permissions Table

1. Click the **Permissions Table** page.
2. Set each user's permission for the Photos tool according to your preferences.

   - Access
   - No Access
3. For a list of what actions users can perform at each permission level in Photos, see the [Permissions Matrix](/product-manuals/photos-project/permissions).
4. In the example screenshot below, the users have 'None' and 'Read Only' permissions, respectively.
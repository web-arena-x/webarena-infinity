# Integrate an Asta Powerproject Schedule Using Procore Drive

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/integrate-an-asta-powerproject-schedule-using-procore-drive

---

## Background

The Procore + Asta Powerproject integration allows users to upload one (1) Asta Powerproject schedule per Procore project. The files must be in a supported file format.

#### Supported File Formats

*Note*: An asterisk (\*) denotes that the file format uses the Powerproject (.PP) file name extension.

- Easyplan 6\*
- Easyplan 5\*
- Easyplan 4\*
- Easyplan 3\*
- Easyplan 2\*
- Powerproject 8 and above\*

## Things to Consider

- **Required User Permissions**:

  - *To upload a* *schedule*, 'Admin' level permissions on the project's Schedule tool.
  - *To view an uploaded* *schedule*, 'Read Only' permissions on the project's Schedule tool.
- **Limitations**:

  - You can upload one (1) Asta Powerproject schedule per Procore project.
  - Asta Powerproject schedules cannot be updated in Procore. All schedule modifications must first be updated in Asta Powerproject. Then an updated file must be uploaded to Procore.
- **Prerequisites**:

  - Ensure that the most current version of Procore Drive is installed on your computer. See [Procore Drive: Setup Guide](/product-manuals/procore-drive/tutorials/procore-drive-setup-guide).

## Steps

### Configure the Project Level Schedule Tool

Before you can upload a schedule using Procore Drive, you need to configure the Project level Schedule tool in Procore for the file type you're going to integrate with.

1. Log in to Procore with an account that has 'Admin' level permissions to the **Schedule** tool.
2. Navigate to the project's **Schedule** tool.
3. In the right pane, click the **Configure** **Schedule** **Settings** link.
4. Click the **Schedule** **Settings** subtab.
5. From the Upload Project Schedule Files drop-down list, select 'File upload via Procore Drive.'
6. At the bottom of the page, click **Update**.

### Upload an Asta Powerproject Schedule

1. Launch Procore Drive (i.e., Start > Programs > Procore Drive).
2. Select your company and project from the drop-down menus.
3. Navigate to the **Schedule** tool.
4. Click **Upload PP or MDB**.  
   *Note*: If the project scheduling preference is current set to "Primavera Integration," click the **Change to Asta Powerproject** button.
5. Browse your local file system and select the appropriate PP or MDB file.
6. Click **Open**.
7. Log in to Procore and verify that you can see your schedule and all of its data under your projectâs Schedule tool. Use the various 'View By' options to change how the information is displayed.
# Upload Photos to the Daily Log from the Photos Tool

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/upload-photos-to-the-daily-log-from-the-photos-tool

---

## Background

When uploading photos to the Photos tool, you have an option to add the photos to the Daily Log tool. Photos added this way will appear in the relevant day's Photos section of the Daily Log tool.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' on the the project's Photos tool. 
    AND 'Standard' or 'Admin' on the project's Daily Log tool.
- **Additional Information:**

 - Only Public photos can be added to the Photos section of the Daily Log tool.

    - If the project's Photos tool is configured to have photos set to private by default, you will not be able to upload photos to the Photos section of the Daily Log. 
      ***Important!*** The following settings in the [Configure Advanced Settings page for the Photos tool](/product-manuals/photos-project/tutorials/configure-advanced-settings-photos) must be disabled in order for photos to be added to the Daily Log tool using this method:

      1. Clear the checkbox next to 'Make Daily Log photos private by default'.
      2. Clear the checkbox next to 'Make photos upload to the Photos tool private by default'. 
         *Note:* These settings can be managed by any user with 'Admin' permissions to the project's Photos tool.
    - The photo album selected for the upload cannot be marked as Private.
    - If you need to upload Private photos to a daily log, you can add them to entries from other sections of the Daily Log tool, such as the Notes log.
 - Photos will be added to the daily log that corresponds with the date that the photos were taken.
 - If capture data is not found on the image, any image added to the Photos tool will be added to the Daily Log based on the day the photo was uploaded.
 - ***Tip!*** You can also upload photos to a daily log directly from the Photos section of the Daily Log tool.

## Steps

1. Navigate to your project's **Photos** tool.
2. Drag-and-drop the photos that you want to upload, or click **Attach File(s)** to select photos manually.
3. Fill out the fields in the upload modal as necessary.

   - **Date**: This field will automatically populate with the dates that the photos were taken. If capture information was not recorded when the photo was taken, the photos will default to today's date.
   - **Location**: Select a location associated with the photo(s).
   - **Album**: Select an album for the photo(s).
   - **Trade**: Select the trade associated with the photo(s).
   - **Private:** Do NOT mark the checkbox next to 'Private' when adding photos to the Daily Log, as only public photos can be added to the Photos section of the Daily Log tool. 
     *Note:* If you need to upload Private photos to a daily log, you can add them to entries from other sections of the Daily Log tool, such as the Notes log.
4. Mark the checkbox next to **Add to Daily Log**.
5. Click **Upload Photos**. 
   *Note:* All photos will be uploaded to the Photos Log in the Daily Log tool on the day that corresponds to the taken date. If capture data is not found on the image, any image added to the Photos tool will be added to the Daily Log based on the day the photo was uploaded.
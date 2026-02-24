# Create an Observation with Quick Capture (iOS)

Source: https://v2.support.procore.com/product-manuals/observations-ios/tutorials/create-an-observation-with-quick-capture-ios

---

## Things to Consider

- [Required User Permissions](/product-manuals/observations-project/permissions)
- **Additional Information:**

  - Your iOS device must be configured to allow the Procore app to access the device's 'Camera', 'Microphone', and 'Speech Recognition' features. When you open Quick Capture for the first time, the Procore app will automatically prompt you to allow it to access these features. If you denied the Procore app's access to these features, see Apple's [Control Access to Hardware Features on iPhone](https://support.apple.com/guide/iphone/control-access-to-hardware-features-iph168c4bbd5/ios)  for more information about manually configuring these features.
  - Your iOS device must have the 'Dictation' feature enabled. See Apple's [Dictate Text on iPhone](https://support.apple.com/guide/iphone/dictate-text-iph2c0651d2/ios) .
  - When you create an observation, you will receive email notifications any time another user comments or changes the status of an Observation.
  - Quick Capture does not require an internet connection when you are recording the Quick Capture. You will only need a cellular or WiFi network connection in order to create the observation.
  - While recording a video, you can verbally describe what you are seeing and the audio will be transcribed to automatically populate the observationâs Title, Description, and Type fields.
  - Each recording can be a maximum of 60 seconds long.
  - On supported devices, tap the **flashlight**  icon to turn on your device's flashlight for the duration of your recording.
  - Templates are not available when using Quick Capture on iOS.
  - You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).

## Steps

1. Open the **Procore** app on an iOS mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Quick Capture: Observation**.  
    OR  
    Tap the **Observations** tool. Tap the **create**  icon, then tap **Quick Capture**.

   ##### Â Tip

   The in-app user guide will load automatically the first time you use Quick Capture. After this, tap the information  icon to review the in-app user guide again as needed.

- *Optional:* Tap the **Location**  icon for the observation you want to create with Quick Capture, and then tap **Save**. You can change this selection later if necessary when reviewing the observation.  
  *Note:* Location and Drawing selections persist for all Quick Capture Observations in the session. You can update the Location and Drawing at any time. After you close Quick Capture, Location and Drawing settings reset.
- Tap the **record observation**  button to begin recording the observation.  
  *Note:* Each recording can be a maximum of 60 seconds long.
- While recording, describe the observation out loud.
- Tap the **record observation**  button again to stop recording.
- Repeat steps 3-7 for each observation you want to create using Quick Capture.
- When you are done recording observations, tap **Review [#]**.
- In the **Quick Capture Items** menu, tap the observation items you want to create.
- Select a **Type** for the observation.  
  *Notes:*

  - The type is automatically populated if it's detected in the audio recording.
  - The type will help you filter and report based on the type of observation. It will not have any affect on which fields will appear when creating an observation. See [What are the default Observation types used for?](/faq-what-are-the-default-observation-types-used-for)
- Tap into the fields to enter the relevant information.
- Tap **Create**.  
  *Note:* Notifications are not automatically sent to the assignee and distribution list members.
- When you are ready to notify users about the observation, navigate back to the **Observations** tool.
- Tap the **Send**  icon.  
  *Notes:* This will send a notification to members on the observation's distribution list and assignees for all of the observations that have yet to be sent. The 'Date Notified' in this message will be set to the date the notification was sent.

  - When sending out notifications of observations, keep the following permissions in mind:

    - *If you have 'Admin' level permissions,* an email digest for ALL observations will be sent.
    - *If you have 'Standard' level permissions*, an email digest for only the observations you created will be sent.
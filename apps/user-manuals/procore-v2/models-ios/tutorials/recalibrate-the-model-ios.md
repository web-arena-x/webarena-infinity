# Recalibrate the Model (iOS)

Source: https://v2.support.procore.com/product-manuals/models-ios/tutorials/recalibrate-the-model-ios

---

## Background

To maintain accuracy in augmented reality, digital models must be periodically recalibrated to prevent **"******model drift******"**âa gradual misalignment with the physical environment. Calibration involves adjusting the model's position (its x and y coordinates) and rotation.

The system includes several built-in prompts to ensure user safety and model accuracy:

- **12-Foot Safety Lock**: For your safety, the screen automatically locks after you move 12 feet from your starting point. It displays a prompt encouraging you to check your surroundings before unlocking the screen at your destination.
- **30-Foot Recalibration**: To correct for natural drift, the system requires you to recalibrate the model's alignment after you have moved 30 feet.
- **Device Orientation**: If your hand covers the camera lens or you hold your device upside down, a prompt will appear asking you to correct the orientation.

## Things to Consider

- **Required User Permissions**:

  - âRead Onlyâ or âAdminâ permissions to the Models tool.

## Prerequisites

- At least one model must have been published to the Procore project. See [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore).

## Steps

1. Navigate to the **Models** tool on the Procore app using an iOS mobile device.
2. Tap the **Augmented Reality** icon. A safety message appears when you first enter augmented reality, warning that this is an immersive experience and users can easily get lost when looking at your device within augmented reality. It emphasizes that staring at your screen on a job site is not advisable.
3. To recalibrate the model, do one of the following:

   - Tap **Recalibrate** on the 30-foot recalibration prompt.
   - From the menu, tab **Recalibrate.**
4. To align the model along the X, Y, and Z axes:

   1. Use the joysticks to move the model along the X and Y axes.
   2. Rotate the model using the rotate control.
   3. Adjust the Z elevation using the Z-bump.
5. Tap **Done**. This action restarts the prompts in the safety cycle.
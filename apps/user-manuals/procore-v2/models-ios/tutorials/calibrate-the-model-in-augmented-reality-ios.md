# Calibrate the Model in Augmented Reality (iOS)

Source: https://v2.support.procore.com/product-manuals/models-ios/tutorials/calibrate-the-model-in-augmented-reality-ios

---

## Background

Construction professionals can improve collaboration and decision-making by experiencing models in a real-world environment. Procoreâs augmented reality provides an immersive experience to promote intuitive understanding of project designs, while highlighting safety with built-in guards.

Revit grids can help with calibration in augmented reality, if the grids are available for the model.

## Things to Consider

- Required User Permissions:

  - âRead Onlyâ or âAdminâ permissions to the Models tool.
- Additional information:

  - Procoreâs augmented reality includes safety and recalibration prompts to ensure user awareness and prevent accidents.

    - 12-foot lock: When you walk 12 feet from your starting point, the screen locks and prompts you to check your surroundings. You can unlock the screen after you arrive at your destination.
    - 30-foot recalibration: When you continue to walk 30 feet, you are prompted to check your surroundings and recalibrate the model. Recalibration is required as models will drift.
- If your hand covers the camera lens or you hold your iOS mobile device upside down, the system prompts you to flip the device over to the correct orientation.

## Prerequisites

- At least one model must have been published to the Procore project. See [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore).

## Steps

1. Navigate to the **Models** tool on the Procore app using an iOS mobile device.
2. Tap the **Augmented Reality** icon. A safety message appears when you first enter augmented reality, warning that this is an immersive experience and users can easily get lost when looking at your device within augmented reality. It emphasizes that staring at your screen on a job site is not advisable.
3. Tap **Acknowledge**. The sheet mapped to the model appears. *Note:* Users are often taken to a home view where they are on the job site but not yet in augmented reality.
4. Touch your device at the location on the sheet to find your position on the project.
5. Adjust your location or orientation as needed.
6. Tap **Confirm**. The model adjusts to your position.
7. Point the iOS mobile device at the ground to detect the Z elevation of the floor you are standing on. *Note:* The ground can be dirt, a metal deck, or finished concrete.
8. Tap the same object in the model that is at that elevation. *Note:* You can hide entire models in the object tree to access the correct object.
9. Tap **Next**.
10. To align the model along the X, Y, and Z axis:

    ##### Example

    If the iOS mobile device detects a metal deck elevation but the model's concrete slab needs to align with the metal deck, you can bump the model up to the accurate measurement.

- Use the joysticks to move the model along the X and Y axes.
- Rotate the model using the rotate control.
- Adjust the Z elevation using the Z-bump.

  ##### Â Tip

  **Do you want to verify that the model is aligned?** Switch between different rendering modes. The default mode for calibration is **Shape**. Other options include **Hidden Line** and **Wireframe**.

1. Ensure alignment by walking around to view different angles (e.g., along columns).
2. Tap **Done**.
3. To validate the work, fade the model and camera back and forth.
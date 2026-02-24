# Measure Distances on a Model (iOS)

Source: https://v2.support.procore.com/product-manuals/models-ios/tutorials/measure-distances-on-a-model-ios

---

Also available on

## Background

The Measure Mode in the Models tool allows you to automatically calculate distances between objects or points and examine them in the context of the model. This is beneficial if you need to measure and validate work, or determine how much clearance exists between objects.

## Things to Consider

- **Required User Permissions**:

  - 'Read Only' or 'Admin' permissions to the Models tool.
- **Additional Information**:

  - You can select from different units of measurements in the Measurement section of the tool's settings. See [Settings: Models (iOS)](/product-manuals/models-ios/tutorials/settings-models-ios).
  - If you are measuring complex objects, the calculation can take some time.

## Prerequisites

- At least one model must have been published to the Procore project. See [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore).

## Steps

- If you want to measure distances on a model, follow the steps for Measure Distances on a Model.
- If you want to measure objects while in 2D Views, follow the steps for Measure Distances in 2D Views.

### Measure Distances on a Model

1. Navigate to the **Models** tool on the Procore app using an iOS mobile device.
2. Tap the model you want to open.  
   *Note:* If you have not downloaded the model to your device yet, tap **Download**. See [Download or Remove Models from a Device (iOS)](/product-manuals/models-ios/tutorials/download-or-remove-models-from-a-mobile-device-ios).
3. Tap **Measure**.
4. Select the type of measurement that you want to make:

   - **Object to Object**
   - **Point to Point**

#### Object to Object

1. After selecting **Object to Object**, tap the two objects you want to measure between.  
    Procore automatically calculates the shortest distance between objects.
2. *Optional:* To view the measurements and objects from different perspectives, drag your finger on the screen to orbit around.
3. If you want to measure other objects, tap **Restart**.
4. When you are done measuring objects, tap **Done**.

#### Point to Point

1. After selecting **Point to Point**, find the area of the model that you want to measure.
2. Drag the **finger pad**  to a point that you want to measure from and release your finger to set the first point.   
   *Note:* As you move the pointer to select a point, Procore highlights areas it can "snap" to so that you can select precise points and get accurate measurements:

   - **Endpoint**: Allows you to precisely select the endpoint of a line segment or the vertex (corner) of a polyline.
   - **Surface**: Allows you to accurately select any visible points on the surface of an object or plane.
   - **Edge**: Allows you to automatically select the nearest point along a line or edge.
   - **Midpoint**: Allows you to quickly identify and select the midpoint of any line segment or edge.
   - **Intersection**: Allows you to select the exact point where two objects intersect.
3. Drag the **finger pad**  towards the second point and release your finger when the **pointer**  aligns with the point.   
    Procore automatically calculates the distance between the two points.
4. *Optional:* To view the measurements and objects from different perspectives, drag your finger on the screen to orbit around.
5. If you want to start over or measure other points, tap **Restart**.
6. When you are done measuring points, tap **Done**.

##### Point to Point Demo

### Measure Distances in 2D Views

While in the 2D View mode for an object, you can tap an object to measure off grids, as well as zoom in for more detailed measurements.*Note:* The Tape Measure feature is only available on iPads. In addition, it will only show for models that have had grids exported from the Procore plugin in RevitÂ®. See [Getting Started Guide for 2D Views in the Models Tool](/product-manuals/models-project/tutorials/getting-started-guide-2d-views-in-the-models-tool).

1. To measure a distance, tap a starting point and drag the line to the end point. The measurement is automatically shown.   
   *Note:* While you are in Tape Measure mode, any click and drag motion will create a measurement. If you need to move around the drawing, use two fingers to pan.
2. Continue making measurements as necessary.

   ##### Â Caution

   Only click 'Done' when you are ready to exit the Tape Measure mode. Clicking Done clears all current measurements.

- *Optional:* If you want to delete measurements:

  - Select a measurement and tap **Delete**.   
     OR
  - Click **Delete All** to clear all measurements.
- Measurements cannot be exported from Procore at this time, but you can take a screenshot on your iPad to save a reference of the measurements. To see how to take a screenshot on your iPad, refer to the support article on Apple's support site [here](https://support.apple.com/en-us/HT210781).
- When you are finished taking measurements and want to exit the Tape Measure mode, click **Done**.
# Trimble Setup for iOS Devices

Source: https://v2.support.procore.com/product-manuals/unearth/tutorials/Trimble_Setup_for_iOS_Devices

---

Unearth OnePlace integrates with Trimble R2 and DA2 devices, providing highly accurate data via a wireless Bluetooth connection. As of iOS **Version 4.7.3** on the App Store, integrating with the Trimble R2 and DA2 is supported on both phone & tablet. Any other Trimble Devices are not supported.

**You will need the Trimble Mobile Manager (TMM) app installed on your iOS device, as well as TMM login credentials in order to connect the Trimble R2 or DA2.**

#### **Configure and Connect Trimble Mobile Manager**

The first time you connect a Trimble device, you will need to configure your device and connect to the Trimble Mobile Manager.

---

|  |
| --- |
| - Ensure you have the Trimble Mobile Manager app installed on your phone and that you are logged in on the TMM app. - Open the Unearth App and select a project that youâd like to add properties in via Trimble. - Open the side menu by clicking the "U" in the top left corner. - Tap on âConnect GPS Deviceâ |
| - Tap on âTrimble GPS." |
| - A pop up will show âConfigure Trimble Mobile Manager.â - Tap on "Continue." |
| - Tap on âOn My iPhone" to choose a location. |
| - Tap on âMobile Managerâ - Then, tap on âDoneâ at the top right of the screen to close the configuration window. - TMM is now connected. |

#### **Pair Trimble Device**

Once TMM has been connect, you can pair to the Trimble Device.

---

|  |
| --- |
| - Select âPair Another Device." Make sure your bluetooth is enabled and the Trimble R2 or DA2 is turned on. |
| - A popup saying âSelect an Accessoryâ will appear. After waiting some time (may take several minutes), the Trimble R2 or DA2 will appear in the list. Select the Trimble from the list. |
| - The "Select an Accessory" window will close. - Select the R2 or DA2 from the list under âSelect from Paired Devices.â |
| - You will now see the âGPS Accuracyâ header with the Trimble icon and another header showing âFinding Your Location.â - The âFinding Your Locationâ step can take some time (around 1 min - 5min), and it works best to be outside so the satellites can be found easier. |
| - After Unearth finds your location based off the Trimble R2 or DA2, the header will show an accuracy based solely off the Trimble. - Tapping on the GPS Accuracy details header will show details from the Trimble R2 or DA2 that are being sent to the device and displayed to the user. |

#### **Adding Properties**

Now that the Trimble R2 or DA2 is connected to Unearth, you can begin adding properties.

---

|  |
| --- |
| - Click the "+" button. - Select the tool you'd like to add. |
| - Click the location arrow to center on location (see center screenshot below).   Since Trimble is based on where you are physically located on the map, you must tap the "Center on Location" button AFTER selecting a tool and BEFORE adding the point to the map to enable the point as a Trimble point. The order of steps is important when adding points from the Trimble's location. |
| - Click "Add Point" in the bottom right-hand corner. |
| - Confirm your point was added with Trimble accuracy. - The added point should be marked as having been added via Trimble inside the âGeometryâ tab on the property panel. You can determine if a point was added from Trimble if the following are present:    - Tab states â1/1 points connected with high-accuracy GPS."   - Trimble icon is located to the left of the point #.   - An âAccuracyâ field is attached to each point. |

If you run into any issues or have any questions, please reach out to us at [unearthsupport@procore.com](mailto:unearthsupport@procore.com).
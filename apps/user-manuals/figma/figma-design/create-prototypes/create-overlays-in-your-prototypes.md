# Create overlays in your prototypes

Source: https://help.figma.com/hc/en-us/articles/360039818254-Create-overlays-in-your-prototypes

---

Before you start

Who can use this feature

Anyone on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with can edit access to the file can create and edit prototype connections.

**New to Prototyping in Figma?** Check out our [Getting Started with Prototyping](https://help.figma.com/hc/en-us/articles/360040314193) and [Build Prototypes with Interactions and Animations](https://help.figma.com/hc/en-us/articles/360040315773) articles.

Prototypes often require transitions between screens in a design. For some interactions, you may want to keep the user on the same screen, but show additional information.

Overlays allow you to show new content or information above the current screen in a prototype. Use overlays to prototype:

- Alerts or confirmations
- Interactive hamburger menus
- Tooltips and additional information
- On-screen keyboards

# Overlay actions

In a prototype connection, an action usually takes the user from **A** to **B**. When the action is an overlay, Figma shows the overlay above the current screen.

Figma usually applies interaction settings to just that the connection. When you create an overlay, Figma applies those settings to the overlay itself, not the connection.

This allows you to apply those settings once and reuse that overlay across your prototype.

**Tip!** You can create interactions between overlays using the **Swap overlay** action. Learn more in the [Swap between overlays](#h_c996af75-4270-4f95-844b-643d9dd1d10f) section.

# Create an overlay

You create an overlay when you define the interaction of a connection. Overlays can be triggered from any object, layer, group or frame. The overlay must be inside a frame.

1. Click the **Prototype** tab in the right sidebar.
2. Hover over the object you want to start the overlay from. Click on the prototype node and drag a connection to the frame you want to become the overlay.![Image showing three frames in the canvas with a connection between the main screen and the overlay](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c7f9f1c2c7d3a0cb932495c/file-rcBPJuHdOA.png)
3. Now you can customize the interaction. There are three aspects of the interaction, the trigger, action and destination.
   1. Select what kind of interaction will trigger the animation.
   2. Select **Open overlay** from the actions.
   3. Figma determines the **Destination** based on where the connection ends. For this interaction, you want this to be the overlay frame. 
      ![Interaction details panel showing settings for a drag-triggered navigation to "Profile/Photos" destination.](https://help.figma.com/hc/article_attachments/360084140933)

There are a few aspects of an overlay that you can customize:

1. **Position:** The location of the overlay relative to the original frame. Choose from seven default options or set a position manually.
2. **Close when clicking outside**: Check this setting to dismiss the overlay when a user clicks outside the overlay's dimensions.
3. **Add background behind overlay:** Check this setting to add a background color behind the overlay and in front of the current frame. Set both the color and the opacity. 
   ![Overlay section of Interaction details menu](https://help.figma.com/hc/article_attachments/360084141453)
4. In the Animation section, customize how the overlay will appear. Select the (1) transition and any additional settings, including (2) direction, (3) easing, and (4) duration. Learn how to [build prototypes with interactions and animations](https://help.figma.com/hc/en-us/articles/360040315773). 
   ![Annotated view of Interaction Details and Animations panel](https://help.figma.com/hc/article_attachments/360083115954)

**Tip!** Add GIFs to your overlays to simulate more advanced animations. GIFs show up as static images in the Editor, but playback as GIFs in [Presentation View](https://help.figma.com/hc/en-us/articles/360040318013).

# Swap between overlays

When working with overlays, you can choose the **Swap overlay** action. This allows you to keep the existing settings while you swap one overlay for another.

In the following example, we used **Swap overlay** to show a user interacting with our in-app help menu.

1. The user clicks on the help icon, which opens the first overlay (`Help menu`).
2. They select the `Get Help` option from the menu.
3. We replace the `Help menu` overlay with a `Chat window` overlay.

![Animated gif showing the overlay swapping from the help menu to the chat window](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5bffbb8004286304a71cc7e5/file-uXyoXeWEXM.gif)

Note: Figma doesn't record **Swap overlay** actions in a prototype's history. When you create a **Back** action from a **Swap overlay** transition, Figma will take you back to the previous screen, not the previous overlay.

## Use Swap Overlay

1. Select the first overlay in the canvas.
2. Open the **Prototype** tab in the right sidebar.
3. In the **Trigger** field, choose the type of interaction you want to use as the trigger.
4. In the **Action** field, select **Swap overlay**.
5. In the **Destination** field, select the overlay you'd want to swap to.
6. Customize the **Animation** with transition, direction, easing, and duration settings.
7. Preview your overlay in [Presentation view](https://help.figma.com/hc/en-us/articles/360040318013).

Note: You can't set a different position for the new overlay. Figma places the new overlay in the same position as the original overlay.

# Edit or delete an overlay

Unlike other actions, overlay settings are applied to the overlay and not the connection. This means you can update the overlay's settings in one place.

You can only edit or remove an overlay in **Prototype** mode.

## Edit overlay

1. Identify an overlay using the blue icon. This will appear next to the frame in the canvas.
2. Click the icon to view overlay's settings in the right sidebar.
3. Make any changes to the overlay, as required.

Tip! You can also access the overlay settings by clicking on a hotspot, or on an arrow from one of the connections.

## Delete Overlay

There are a few ways to delete an overlay:

- Click on the connection arrow and drag it to an empty part of the canvas.
- Click the icon to select the overlay, then press the `Delete` key.
- Remove all connections on the current page. Right-click on a connection and select **Remove all interactions**.
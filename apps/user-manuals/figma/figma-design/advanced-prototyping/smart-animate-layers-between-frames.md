# Smart animate layers between frames

Source: https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames

---

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Users with can edit access to a file can create and edit prototypes.

Users with can view access to a file or prototype can view prototypes.

Smart animate looks for matching layers, recognizes differences, and animates layers between frames in a prototype.

You can select **Smart animate** from the list of transitions, when building a prototype. You can also apply **Smart animate** with other transitions to create seamless animations.

Smart animate allows you to quickly create advanced animations. Use **Smart animate** to replicate:

- Loading sequences
- Parallax scrolling
- Touch gestures, for example Drag, Swipe, Long-Press
- Sliders, Toggles and Switches
- Expanding content (Show more / Show Less)
- Pull to refresh

![Animated image showing Smart animate in action](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d95307404286364bc8fe2d5/file-u0w1O0jCDW.gif)

Learn more about how we built smart animate in our Blog post: [Announcing smart animate](https://www.figma.com/blog/announcing-smart-animate-and-advanced-transitions).

# Supported properties

Smart animate looks for matching layers that exist across multiple frames. Figma takes into account both the **layer's name** and where it sits within the **hierarchy**.

For layers that match between frames, Figma recognizes what's changed and applies transition to animate between them.

You can apply smart animate to entire objects or Components, as well as individual layers within a Component or group.

It's likely that more than one of an object's properties will change between Frames. We've isolated each of the properties we support below, so you know what to expect.

## Scale

If an object changes in size between frames, Figma will animate it shrinking or growing.![Animated image showing an object with a different scale across two frames and the resulting smart animation](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950a782c7d3a7e9ae1f78f/file-TxYtpSEfl0.gif)

## Position

Figma recognizes if an object's location, the x and y co-ordinates, have changed. It will then animate the object moving from its current position, to its position in the destination frame.![Animated image showing an object with a different position across two frames and the resulting smart animation](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950a8b04286364bc8fe143/file-muIQMZMadV.gif)

## Opacity

Smart animate can also recognize a layer or object's opacity. You can adjust opacity to make an object to appear or disappear between frames.

Set the opacity of the layer to 0%, instead of toggling the layer visibility. Figma will apply a dissolve transition to animate the layer's opacity.

You can adjust opacity through a layer's Fill properties, as well as through the **Layer** property. Smart animate will apply to both.

We recommend adjusting the entire layer's opacity. Adjust the opacity **Layer** setting in the **Design** tab of the right sidebar.![Animated image showing an object with a different opacity across two frames and the resulting smart animation](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950a9904286364bc8fe144/file-LdnSGNfOjR.gif)

## Rotation

Smart animate also takes the layer's rotation and orientation into account.

You can [rotate an object](https://help.figma.com/hc/en-us/articles/360039956914#Rotating_objects) using the  rotation field in the right sidebar or in the canvas itself. Hover over the corner bounds of an object until the rotation cursor  appears.

Rotate a single layer at once, or rotate a group of them around a single anchor point.![Animated image showing an object with a different rotation across two frames and the resulting smart animation](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950aa32c7d3a7e9ae1f793/file-OOGxIrV1Il.gif)

## Fill

Figma will smart animate any changes to an object's fill. This allows you to animate changes between solid colors, gradients and even image fills.![Transitioning bar chart demonstrating Figma's smart animate feature with color change and position shift between frames.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950ab02c7d3a7e9ae1f794/file-ATNtix86xk.gif)

**Things to note**

- Figma supports smart animate for layers with texture, noise, background blur, or layer blur [effects](https://help.figma.com/hc/en-us/articles/360041488473) applied. Because texture and noise effects are randomly generated, we recommend duplicating the frame to ensure smart animate works as expected. If the frames are not identical, Figma will apply a default dissolve transition.
- Figma does not support smart animate for layers with drop shadow and inner shadow [effects](https://help.figma.com/hc/en-us/articles/360041488473), or for moving between [shapes](https://help.figma.com/hc/en-us/articles/360040450133). If a frame includes an unsupported property, Figma will apply a default dissolve transition.
- Figma doesn't support smart animate for [overlay actions](https://help.figma.com/hc/en-us/articles/360039818254). This is because Figma treats overlays as new frames. You can use smart animate when [swapping between overlays](https://help.figma.com/hc/en-us/articles/360039818254), if those overlays have matching layers.
- If you introduce a new layer in the destination frame, smart animate will dissolve the layer into view.
- If a layer's properties stay the same between two frames, Figma won't animate that layer at all. This is great for status bars and menus, and interactions when you don't want to move to a different UI.
- If you check the **Fix Position when Scrolling checkbox** for any layers, Figma will add them to the list of **Fixed** layers. Smart animate handles layers differently when you [combine **Smart animate** with other transitions](#h_90607300-1bb6-4f5b-987b-be36a8fc7ad9).

# Apply smart animate

There are two ways you can use smart animate in your prototypes. As a stand alone transition, or by using **Smart animate matching layers** with another animation.

## Smart animate

Select **Smart animate** in the transition field to animate between two frames.

1. Open the **Prototype** tab in the right sidebar.
2. Select layer, group, or frame in the canvas. A connection node will appear on the right-edge.
3. Click on the node and drag it to the next frame to create a connection.
4. Define the **Interaction** in the right sidebar by choosing a trigger and action. Figma will set the second frame as the destination.
5. In the **Animation** section, select **Smart animate** from the transition field.
6. Apply **Easing** to the transition, or change the **Duration** (optional).
7. Repeat for any other frames you want to smart animate.
8. Click the  in the toolbar to [open the prototype in Presentation View.](https://help.figma.com/hc/en-us/articles/360040318013)

In our example below, we have three frames with some matching layers. We want smart animate to animate removing the Abel Tasman Coast Track from our list of favorites. ![Image showing the three separate frames in our prototype](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950ace2c7d3a7e9ae1f796/file-H7Ayz3WHDi.png)

Smart animate now moves us smoothly between each frame in our prototype!![Animated image showing a smart animate transition](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950af02c7d3a7e9ae1f79d/file-YwCcOT43HD.gif)

## Smart animate matching layers

If you want to smart animate some layers in your prototype while using another main transition, you can check a box to **Smart animate matching layers**.

Figma treats fixed layers differently when using smart animate with other transitions.

- **Layers that don't match:** Figma will use the main **transition** you select.
- **Layers that do match:** Figma will **Smart animate** any differences for supported properties.
- **Fixed layers that do match**: Figma won't apply any transition.
- **Fixed layers that don't match**: Figma will apply a dissolve transition instead of the transition you select.

To use **Smart animate matching layers**, check the box in the right sidebar when adjust the animation:

![Interaction details panel showing animation settings with "Push" transition and "Smart Animate Matching Layers" checked.](https://help.figma.com/hc/article_attachments/32404312938519)

In our example below, we have a status bar and navigation that exist across all three frames. We want these to stay in place when we switch between tabs.  
![Image showing the three frames in our prtotype](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b0f2c7d3a7e9ae1f7a1/file-5gZ13AZyie.png)

We've selected a **Push** Transition to move between Frames. We choose not to check the box next to **Smart animate matching layers**.

When we view our Prototype, we can see that everything in our destination frame uses the **Push** transition. This makes it pretty obvious that we're moving between separate screens in a prototype.

![Animated image showing our push transition in our prototype](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b2504286364bc8fe14b/file-3BKeoV8zLU.gif)

If we check the box next to **Smart animate matching layers**, our status bar and navigation stay in place, while the other content uses **Push**.![Animated image showing the push transition with Smart animate matching layers applied](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b322c7d3a7e9ae1f7a2/file-aI3r9NOwPe.gif)

# Tips for Smart Animation

Before smart animate, Figma didn't place much importance on layer names. As Smart Animate is reliant on **Layer name** and **hierarchy**, this may require you to use a different approach.

Learn more about creating [matching objects with layer name and hierarchy →](https://help.figma.com/hc/en-us/articles/21523793229463/)

We've outlined a few ways to troubleshoot unexpected smart animate results below.

Tip: We recommend increasing the duration while building your prototype. This lets you see what's happening and make any adjustments.

## Layer names

One quick way to create frames for smart animate is to **duplicate** them. This keeps the naming consistent between each frame. You can then add and remove layers to each frame, as needed.

Figma names frames and layers based on the way you duplicate or copy and paste them.

- **Within a frame:** Figma numbers layers them sequentially. For example: Frame 1, Frame 2 etc.
- **Between frames**: Figma uses the same name. For example: If you copy `Rectangle 1` from one frame, Figma will paste it as `Rectangle 1` in the next frame.

You may have objects or layer that exist across frames, but have different names in each. Or, you may have the opposite problem - layers that all have the same name, which you don't want to match.

You can view and update your layer names using the [Layers panel](https://help.figma.com/hc/en-us/articles/360039831974) in the left sidebar. Learn how to [rename layers in bulk](https://help.figma.com/hc/en-us/articles/360039958934).

## View matching layers

Figma has also made it easier to identify layers or objects that exist - or match - between frames. This applies to all layers, groups, frames, and Components.

1. Open the Prototype tab in the right sidebar.
2. Hover over an object or layer in the canvas.
3. Figma will highlight that layer in any other frames it exists in.

![Image showing the navigation menu frame selected in all three frames in our prototype](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b582c7d3a7e9ae1f7a4/file-RLsj3fqAtd.png)

## Layer order and hierarchy

**Smart animate** and **Smart animate matching layers** take into account the layer order, or hierarchy of your layers.

Normally, **Move in** or **Slide in** will transition the entire destination frame above the original frame. With smart animate matching layers, Figma will move or slide in layers based on their hierarchy, which can cause some confusing or unexpected results.

In our screenshot below, we have two matching objects between our frames ( `Explorer 1` and `Explorer 2`). These are the **Status Bar** and the **Navigation**.

If we have layers above any matching layers, Figma will animate them above the destination frame. In our screenshot below, we can see layers from `Explorer 1` appear above the destination frame.![Image showing how our layers are ordered in the layers panel and the resulting transition](https://help.figma.com/hc/article_attachments/32404312940439)

By moving our matching layers to the top of the hierarchy instead, we can make sure the entire destination frames slide above the original frame.![Image showing how our layers are ordered in the layers panel and the resulting transition](https://help.figma.com/hc/article_attachments/32404267897879)

## Group layers

To be more precise in deciding what to smart animate, Figma matches layers based on their **name** and **hierarchy**. This also lets you quickly un-match layers between frames.

Let's say that we have five rectangles in each of our frames. These rectangles contain different content between each frame. We labeled them as `Trip 1` to `Trip 5` across all three frames.

![Image showing the layout of the three screens in our prototype](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b6e2c7d3a7e9ae1f7a8/file-w6ZuaK5IZJ.png)

When we try apply a **Push** transition, smart animate recognizes them as matching layers. Instead of treating these rectangles as new content, Figma smart animates the change to their position.![Animated image showing how smart animates reorders the rectangles instead of treating them as different content](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b8e2c7d3a7e9ae1f7ac/file-XbwpEthQlW.gif)

To change this behavior, we can group the rectangle trips in each frame and give them a unique name.

When we preview our transition, smart animate no longer recognizes these as matching layers. Our content will **Push** in together, making our Prototype look much more realistic.

![Animated image showing a slide transition between each frame](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b9c04286364bc8fe151/file-L3LZGQot04.gif)

## Smart animate with Slide in and Move in

There are a few things to consider when using **Smart animate matching layers** with Slide or Move transitions.

When selected, Figma will animate any matching layers between frames. This means Figma can't animate the entire destination Frame (B) over the initial Frame (A), like it normally would.

Figma also doesn't include a frame's fill as part of the animation. This can cause layers to overlap, making the transition look messy.

![Animated image showing how layers are overlapping in our transition](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950bae04286364bc8fe155/file-uk4otwmIZP.gif)

To prevent this, we can add a rectangle with a solid fill behind our other layers. Now, when we view our prototype, the content in each frame slides in together.![Animated image showing how our layer now smoothly transition](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950bc604286364bc8fe158/file-ytA85lem0C.gif)
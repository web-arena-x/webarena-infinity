# Use videos in prototypes

Source: https://help.figma.com/hc/en-us/articles/8878274530455-Use-videos-in-prototypes

---

Before you start

Who can use this feature

 

Supported for files in [Education, Professional, Organization, and Enterprise teams](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone part of a paid team can add video to files.

Anyone with can edit access can edit videos in files.

New to Prototyping? Check out our **[Guide to prototyping →](guide-to-prototyping-in-figma.md)**

Add video to your prototypes to replicate the experience your users would have in a site or app with video playback or previews.

Video in prototypes:

- Can be in .mp4 or .mov format using H.264 encoding.
- Can be in .webm format using VP8 encoding.
- Can be up to 100MB in size
- Are [shape fills](https://help.figma.com/hc/en-us/articles/360040623954-Add-fills-to-text-and-shape-layers) and behave as such
- Are not currently supported in the [Figma mobile app](https://help.figma.com/hc/en-us/articles/1500007537281)

Note: Video can only be added to files in a paid Education, Professional, and Organization team. Collaborators on free Starter teams can edit existing video in a file but not upload video to it.

Once you add video(s) to your design file, you can edit or adjust basic video qualities. Then, you can add interactions to your videos to start building your prototypes.

## Add video to files

Figma doesn't have a specific layer type for video, instead, videos are a type of fill. Since videos are fills, you can add them to any vector or shape.

![Capybara video fill selected in Figma, showing playback controls and video properties in the Fill panel.](https://help.figma.com/hc/article_attachments/31619782909847)

There are a number of ways you can add video to design files:

- A Drag and drop video file from your computer onto the canvas.
- B Use the video importer from the fill color picker. **[Learn more about how to upload fills →](https://help.figma.com/hc/en-us/articles/360041090073)**
- C Use the Place image/video tool to add videos in bulk. **[Learn more about the Place image/video tool →](https://help.figma.com/hc/en-us/articles/360041089973-Add-images-in-bulk-with-Place-image)**
- C Copy a video from another layer in the current file, or from another file.
- D Paste any video from your clipboard into the canvas.

Note: You can also add animated GIFs to your prototypes. GIFs only playback when viewing designs and prototypes in presentation view. [Add animated GIFs to prototypes →](https://help.figma.com/hc/en-us/articles/360041486873)

If you add a video straight to the canvas, Figma creates an object on the canvas with the dimensions of the original file. If you add a video as a fill to an existing object, Figma uses the name and dimensions of the original object.

View and update video fills in the **Fill** section of the right sidebar. From the **Fill** section, you can play and preview your video fill, jump to a specific timestamp, or scrub through the video.

![Video of capybaras in a Figma canvas, displaying video fill options with preview and scrubber in the sidebar.](https://help.figma.com/hc/article_attachments/31619751191447)

You can also identify layers with video fills in the Layers panel in the left sidebar. Objects with video fills are represented on the layers panel with the icon.

## Edit video

Once you’ve added a video to your file, you can edit the video in the following ways:

- [Scale, rotate and adjust the dimensions of any layers with video](https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-and-position)
- [Crop and re-position video applied to layers](../color-gradients-and-images/crop-an-image.md)
- Adjust the video options including the Fill mode, rotation and [blend modes](https://help.figma.com/hc/en-us/articles/360040667874-Create-unique-effects-with-Blend-modes)
- [Apply masks](../create-and-edit-layers/masks.md) to only show a part of the video

## Prototype with video

Once you add video to a frame, switch over to the **Prototype** of the right sidebar. From here, you can create interactions between frames with video.

[Learn more about prototyping →](guide-to-prototyping-in-figma.md)

### Video properties

![Video editing panel showing autoplay options and a selected wildlife video on the canvas.](https://help.figma.com/hc/article_attachments/31619751194519)

When you select a video, there is a **Video** section available on the Prototype tab. This section lets you set a video’s behavior when navigating to its frame in a prototype.

- Check the box to **autoplay** video
- Click the **Loop** icon to loop video
- Click the **Sound** icon to turn the video’s default sound setting on or off

### Video interactions

When you create any prototyping connection, there is a **trigger** that determines what causes the interaction to begin, and an **action** that defines the response from the triggered event.

The following interaction triggers are available for videos:

- **When video hits** - Trigger set action when the video hits a specific timestamp.
- **When video ends** - Trigger set action when the video completes playing.

The following interaction actions are available for videos:

- **Play/pause video** - Select either **Play video**, **Pause video**, or **Toggle play/pause**.
- **Mute/unmute video** - Select either **Mute video**, **Unmute video**, **Toggle mute/unmute**.
- **Set to specific time** - Set a timestamp to jump to in the video.
- **Jump forward/backward in time** - Select either **Jump forward** or **Jump backward**, then set the number of seconds to jump forward/backward in the video.

When you create an interaction between two frames that have the same video, there is a **Reset video state** toggle in the **Interaction details** panel. When toggled on, the video will restart from its beginning between frames. [Learn more about video state management →](https://help.figma.com/hc/en-us/articles/14397859494295)

![Figma Prototype tab displaying video interaction settings including "On click" trigger, "Navigate to" action, and "Reset video state".](https://help.figma.com/hc/article_attachments/31619782929431)

### Video interactions within the same frame

You can interact and prototype with videos based on triggers made within the same frame. This can be helpful when trying to build an interactive video player experience.

1. Create a connection from your starting object to the video file.
2. Set your desired starting action (for example, **On click**).
3. Set your desired action for the video (for example, **Mute/unmute video**).

![Figma prototype with selected frame for video interaction setup, showing capybara image as a placeholder.](https://help.figma.com/hc/article_attachments/31619751198103)

### Video and smart animate

You can [use smart animate](https://help.figma.com/hc/en-us/articles/360039818874) to preserve a video’s progress when navigating between frames. Let’s say you want to create a prototype where entering a frame begins playback, then clicking on the video navigates to a new frame with a larger view.

![Two frames in a Figma prototype with a video, demonstrating video interactions and smart animate.](https://help.figma.com/hc/article_attachments/31619782933911)

1. Create a connection between the two frames with the same video name. Make sure the video layer names match as well.
2. Set the animation setting to **Smart animate**.
3. In the **Interaction details** panel, uncheck **Reset video states.**

### Video and interactive components

Use interactive components to prototype video interactions in a single frame, like previewing playback on hover.

![Two video layers in Figma prototype showing default and hover states for interaction.](https://help.figma.com/hc/article_attachments/31619782934679)

1. [Create a component with variants](https://help.figma.com/hc/en-us/articles/360061175334) for a default and hover state.
2. The default state should have autoplay off, and the hover state should be set to autoplay.
3. Create a connection from the default variant to **change to** the hover variant and uncheck **Reset video states.**
4. Create a frame with a couple instances of the component and replace video to reuse the component.

[**Try out more ways to prototype with video using the playground file →**](https://www.figma.com/community/file/1155152691809198766)
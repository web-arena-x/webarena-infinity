# Add images and video to a site

Source: https://help.figma.com/hc/en-us/articles/33666207487767-Add-images-and-video-to-a-site

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

You can enhance your site with photos, graphics, videos, and GIFs . Figma Sites supports the following formats:

- **Image:** JPG, PNG, HEIC, WebP, SVG, GIF, TIFF (only available on Safari)
- **Video:** MP4, MOV, WebM

**Note**: Figma Sites supports uploads up to 100MB per video file, and up to 1GB of video per site. For larger files, we recommend using platforms like YouTube or Vimeo. These services are optimized to balance video quality and internet speed during playback.

## Add an image or video to a site

Drag and drop files from your computer onto the canvas, or use the media picker to select the files you want to add. You can import multiple files at once.

1. Click  **Image/video** in the toolbar or use the keyboard shortcut:
   - **Mac:** `Shift` `Command` `K`
   - **Windows:** `Shift` `Ctrl` `K`
2. Select one or more files to upload.
3. Your cursor will show a thumbnail of the first file. If you selected multiple files, a badge displays the number of files you have left to place.
4. Place your file by doing one of the following:
   - Click to add it at its original size.
   - Click and drag to define custom dimensions.
   - Hover your cursor over an object with a fill, such as a frame, and click to replace the fill with your file.

**Note:** Videos and animated GIFs appear as static images on the canvas. To play them, place them in a webpage and then [open the preview](https://help.figma.com/hc/en-us/articles/31242824747287).

### Adjust video properties

Video layers show a  icon in the **Layers** panel of the left sidebar.

Since images and videos are treated as fills, you can adjust the design properties of the parent object as you would any other element.

There are also video-specific properties available at the top of the right sidebar:

- **Loop**: Play the video in a continuous loop.
- **Mute**: Check the box to mute audio when the video loads. Users can unmute and listen to the audio if playback controls are enabled.
- **Autoplay**: Play video automatically when it loads. Autoplay won’t work for users with reduced motion settings enabled on their computer.
- **Show playback controls**: Allow users to access play, pause, timeline, and audio controls.

### Embed a video from a third party platform

You can also embed videos from hosting platforms like YouTube or Vimeo on your site. Video embeds are a special type of element in Figma Sites, and can’t be used as an object fill.

1. Click  **Insert** in the left navigation bar.
2. On the **Blocks** tab, click **Embeds.**
3. Click and drag the relevant embed block into a webpage or onto the canvas. Use the **URL or HTML** embed if your video platform isn’t listed.

## Frequently asked questions

### Should I upload a video file to Figma or use a video embed from a third party platform?

There are a few things to consider when choosing where to host your video:

|  | Video upload | Embed |
| --- | --- | --- |
| **File size** | Less than 10MB | More than 10MB |
| **Accessibility** | Decorative only | Supports captions |
| **Length** | Shorter videos | Longer videos |
| **Video player** | Uses browser’s video player | Custom to each video platform |

### My video is more than 10MB. How do I make it smaller?

Here are two ways you can adjust your video to make it smaller:

- **Reduce the resolution**: Use **720p or 1080p**. Higher resolutions like 4K may not render smoothly and typically aren’t necessary for background use.
- **Reduce the bitrate**: Use compression tools to stay under **2–3 Mbps**.
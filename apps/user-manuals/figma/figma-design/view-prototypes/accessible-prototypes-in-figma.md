# Accessible prototypes in Figma

Source: https://help.figma.com/hc/en-us/articles/7810391964695-Accessible-prototypes-in-Figma

---

Accessible prototypes in Figma allow you to navigate through content using a screen reader. To use accessibility mode in a prototype, you’ll first need to install a supported screen reader.

Accessible prototypes are only available in the desktop browser and on the Figma desktop app. Accessibility mode does not work for mobile or mobile web prototypes. [View a list of supported browsers →](https://help.figma.com/hc/en-us/articles/360039827194-Figma-browser-requirements)

## Supported screen readers

### Mac

- VoiceOver: [View the VoiceOver user guide for macOS](https://support.apple.com/guide/voiceover/welcome/mac) [→](https://help.figma.com/hc/en-us/articles/360039827194-Figma-browser-requirements)

### Windows

- JAWS (Job Access With Speech): [View Freedom Scientific's JAWS documentation](https://support.freedomscientific.com/products/blindness/jawsdocumentation) [→](https://help.figma.com/hc/en-us/articles/360039827194-Figma-browser-requirements)
- NVDA (NonVisual Desktop Access): [View the NV Access NVDA user guide](https://www.nvaccess.org/files/nvda/documentation/userGuide.html) [→](https://help.figma.com/hc/en-us/articles/360039827194-Figma-browser-requirements)

## Activate accessibility mode

After a screen reader is installed and enabled, you can activate accessibility mode in a Figma prototype a few different ways:

### Keyboard controls

1. Press `Tab` to focus on the hidden **Skip to content** button. This button is the first interactive item on the page.
2. Press `Enter` to turn on accessibility mode for the current prototyping session.

A self-dismissing message that reads “Now adapting content for screen readers” displays at the bottom of the page. If enabled, your screen reader will also verbalize this message.

**Note:** The **Skip to content** button is also available in screen reader menus, such as VoiceOver’s Form Controls rotor.

### Accessibility settings

1. Select **Options** > **Accessibility settings** in the toolbar.
2. Toggle **Adapt content for screen readers** to turn accessibility mode off.

## Deactivate accessibility mode

To deactivate accessibility mode:

1. Select **Options** > **Accessibility settings** in the toolbar.
2. Select **Adapt content for screen readers** to turn accessibility mode off.

## Figma Design to HTML mapping

While in accessibility mode, Figma Design elements are translated to HTML or HyperText Markup Language. Screen readers interpret HTML tags to understand the content and sections of a document, as well as which elements are available for a user to interact with on a page. Semantic HTML tags also allow a screen reader to communicate content that may be highlighted visually to a user.

When considering how your Figma Design elements translate to HTML:

- The prototype actions **Navigate to** and **Open link** are seen by screen readers as links; all other actions are seen by screen readers as buttons
- Any element in a prototype with an **On click** interaction is seen by the screen reader as an accessible button or link, depending on its triggered action
- The screen reader navigates through links and lists within design text
 - Ordered and unordered lists are read as structured and nested lists
 - Inline links are seen by screen readers as accessible links
- Any shapes with an image fill appear as an image and have their alt text populated with the layer’s name
- Top-level frames, components, and component instances become labelled sections using layer names as the accessible label

Using `Tab` to navigate follows the layer order of your prototype. If your content isn't read in the order you expect, open the Figma Design file and [change the layer order in the left sidebar](https://help.figma.com/hc/en-us/articles/360039956914#Change_layer_order). For frames with auto layout, navigation follows the order of the layout—either top to bottom or left to right.

To learn more about accessible prototypes in Figma, check out [this playground file](https://www.figma.com/community/file/1167124335986833540) and try it out yourself!
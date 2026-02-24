# Add links to a site

Source: https://help.figma.com/hc/en-us/articles/31242823085207-Add-links-to-a-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Adding links to your site lets users quickly navigate to the most relevant information. You can add several types of links in Figma Sites:

- **Page link:** Links to another page on your site or to an external site.
- **Back link:** Works like a browser back button, returning visitors to the previous page.
- **Anchor link:** Links to a specific section of the same page. With anchor links, you can set:
 - **Destination**: The section you want the link to scroll to.
 - **Offset**: An optional vertical adjustment in pixels to fine-tune where the scroll lands.

## Add a link to an element

To add a link:

1. Select a layer or object to link. If your webpage has multiple breakpoints, select the object in the [primary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879) to automatically select the matching object in the other breakpoints.
2. Click **Create link** in the **Link** section of the right sidebar.
3. Open the dropdown menu and select a link type, or enter a URL to link to an external site.

**Tip**: External sites open in a new tab by default. Uncheck **Open in a new tab** to keep users in the same tab. You can add URL parameters like UTMs on URLs to external sites.

**Note**: Links associated with a CMS item include a trailing `/slug` to indicate that the link is dynamically generated. [Learn more about CMS in Figma Sites](https://help.figma.com/hc/en-us/articles/35995403973783).

Figma Sites also supports both `tel:` and `mailto:` link protocols.

![An animation showing two webpages with a user dragging a link noodle from an element on one webpage to the other webpage.](https://help.figma.com/hc/article_attachments/31919171021207)

**Tip**: After switching to the **Interaction** tab, you can create also create links by selecting one or more objects and dragging a connection to a destination webpage or an element on the same page. In this example, [selecting an object in the primary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879) also selected the corresponding objects in the other breakpoints.

## Remove a link from an element

From the canvas From the right sidebar

1. Navigate to the **Interaction** tab if the right sidebar.
2. Click anywhere on the canvas to reveal the link connection arrows.
3. Click and drag to select one or more link connection arrows, then press the **Delete** key.

1. Select one or more layers with a link you’d like to remove. For webpages with multiple breakpoints, select the object in the primary breakpoint to automatically select the corresponding objects in the other breakpoints.
2. In the the right sidebar, click the **minus** icon in the **Link** section.
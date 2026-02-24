# Copy and paste between Figma Sites and Figma Design

Source: https://help.figma.com/hc/en-us/articles/31414245874455-Copy-and-paste-between-Figma-Sites-and-Figma-Design

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access in the destination file

You can freely copy and paste objects between Figma Design and Figma Sites—although there are several features that work differently in each product.

**Tip:** Curious about the differences between these products? [Learn more about which tools and properties are available in Figma Sites and Figma Design.](https://help.figma.com/hc/en-us/articles/31242787286935)

## Copy from Figma Design to Figma Sites

You can copy and paste any design assets between Figma Design and Figma Sites using the standard copy and paste keyboard shortcuts:

- **Copy**: `Ctrl` or `Cmd` `C`
- **Paste**: `Ctrl` or `Cmd` `V`

If your design’s width is between 1200px and 1600px—and you are the file creator—you can also send it straight to a new Figma Sites file:

1. Open the Figma Design file containing your design.
2. Right-click the frame you want to add as a webpage to Figma Sites.
3. Select **Copy to Figma Sites**.

Figma will open a new site file with your design added to the **Home** page.

![Animation of right-clicking a design in Figma and selecting 'copy to figma sites'. The design is sent to a new sites file and added to the home page.](https://help.figma.com/hc/article_attachments/31909926980759)

### Things to keep in mind

Here are a few things to be aware of when moving from Figma Design to Figma Sites:

| Feature | Behavior |
| --- | --- |
| [Annotations](https://help.figma.com/hc/en-us/articles/20774752502935) | Annotations do not render in a site file, but they reappear if you copy and paste the design back into Figma Design later. |
| [Positioning](https://help.figma.com/hc/en-us/articles/31242774629655) | The positioning of each element is based on the properties set in Figma Design:   - Auto layout frames use relative positioning (with auto layout applied) - Objects without auto layout—or with auto layout ignored—use absolute positioning - Objects set to **Sticky** or **Fixed** as [scroll behaviors in a prototype](https://help.figma.com/hc/en-us/articles/360039818734) will maintain the corresponding positioning |
| [Prototypes](https://help.figma.com/hc/en-us/articles/360040314193) | Most prototype connections automatically convert to the corresponding interactions in Figma Sites. [Learn how to troubleshoot any unsupported interactions.](https://help.figma.com/hc/en-us/articles/31242843431575) |

**Tip**: To get the most out of your design, check out these [tips for creating a responsive webpage in Figma Sites](https://help.figma.com/hc/en-us/articles/33257143505175).

## Copy from Figma Sites to Figma Design

You can manually copy and paste design assets from Figma Sites to Figma Design using the same standard copy and paste keyboard shortcuts mentioned above.

**Tip**: There are lots of ways you can[modify how content is pasted into Figma Design](../../figma-design/work-with-layers/copy-and-paste-objects.md#h_01J92HBF9AD0R0NRKPMHT8NJ06), like paste to replace, paste over selection—and more.

### Things to keep in mind

Here are a few things to be aware of when moving from Figma Sites to Figma Design:

| Feature | Behavior |
| --- | --- |
| [Accessibility properties](https://help.figma.com/hc/en-us/articles/31242789265431) | Accessibility properties do not render in a design file, but they reappear if you copy and paste the design back into Figma Sites later. |
| [Code layers](https://help.figma.com/hc/en-us/articles/31242824165143) | Code layers are not supported in Figma Design and appear as a static image snapshot on the canvas. |
| [Embeds](https://help.figma.com/hc/en-us/articles/31242773374615) | Embeds are not supported in Figma Design and appear as static images on the canvas. |
| [Interactions](https://help.figma.com/hc/en-us/articles/31242843431575) | If available, interactions will automatically convert to the corresponding prototype connections—but many interactions are not supported in Figma Design. |
| [Links](https://help.figma.com/hc/en-us/articles/31242823085207) | Links to external websites will automatically convert to an **Open link** prototype action in Figma Design. Internal links to other webpages within a site won’t copy across to Figma Design. |
| [Positioning](https://help.figma.com/hc/en-us/articles/31242774629655) | The positioning of each element is based on the properties set in Figma Sites:   - Auto layout frames continue to use auto layout - Objects with absolute positioning inside an auto layout frame use ‘ignore auto layout’ - Objects set to **Sticky** or **Fixed** positioning use the corresponding [scroll behavior](https://help.figma.com/hc/en-us/articles/360039818734) |
| [Webpages](https://help.figma.com/hc/en-us/articles/31242763080983) | Each webpage is converted into a section with frames for each breakpoint. |
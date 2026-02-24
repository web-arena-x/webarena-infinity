# Insert blocks, embeds, webpages, and design libraries into a site

Source: https://help.figma.com/hc/en-us/articles/31242773374615-Insert-blocks-embeds-webpages-and-design-libraries-into-a-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Add prebuilt elements from the **Insert** menu to start building your site faster. The **Insert** menu contains:

- **Blocks:** Ready-made design components you can drag and drop into to your website to quickly assemble a layout. This also includes embeds—components that let you interact with external content, such as videos or maps—as well as [CMS lists and pages](https://help.figma.com/hc/en-us/articles/35995403973783).
- **Libraries:** Design libraries provide access your team’s components, variables, and styles. Using these assets ensures your sites are always in sync with your company's colors, fonts, and logos.

![Cursor clicks the "Insert" icon in Figma Sites, opening a menu with options like blocks, libraries, and embeds for web design.](https://help.figma.com/hc/article_attachments/31880156111127)

To access the **Insert** menu, click the  icon in the left navigation bar of a site file.

**Tip**: You can also work from a template if you prefer. To use a template:

1. Create a new sites file and use the template picker
2. Make a copy of any site file available from Figma Community

## Add an insert to your site

There are two ways to add blocks, embeds or library assets to your site:

**Drag an item onto the canvas**

Drag an insert into a webpage or directly onto the canvas.

- If you drag an insert into a [webpage’s primary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879), it is automatically added to all other breakpoints.
- If you drag an insert into a non-primary breakpoint, it appears only in that breakpoint.

**Click an item in the Insert menu**

What happens when you click an insert depends on what’s selected on the canvas.

- If nothing is selected, the insert is added to the canvas.
- If a webpage or [primary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879) is selected, the insert is added to all breakpoints in the webpage.
- If a non-primary breakpoint is selected, the insert is added only to that breakpoint.

**Tip:** Add any block to an empty webpage to automatically activate auto layout for that webpage. This makes it easier to quickly snap together a page from different blocks.

## Configure an embed

Embeds are site elements that let you interact with external content, such as forms, videos hosted on other websites or maps.

Each embed has editable properties in the right sidebar. For example, the Google Maps embed includes **Location settings** to set the map’s pin location.

Here are a few things to keep in mind when using embeds:

- Embeds only render in the preview or published site—not on the canvas.
- An embed might not work if the third-party website prevents its content from being shown in an `<iframe>` for security reasons.

**Tip**: You can also insert custom code elements in the `<head>` or `<body>` of your site from [website settings](https://help.figma.com/hc/en-us/articles/31242875661591). This is a good option if you have a `<script>` tag you want to insert into your site.

## Use design libraries in your site

The **Libraries** tab lists all libraries available in the file. You can add additional libraries as needed:

1. Click the  **Libraries** icon to open the **Libraries** modal.
2. Locate the library you want to add. Use the search bar to search your library by name, or—if available—use the sections under **Browse libraries** to find relevant libraries across your team or organization.
3. Click the library to view its assets. Click **Add to file** to add the library to your file, or click **Open file** to view the library’s source file.

**Tip:** Too many libraries in your sidebar? Right-click on any library and select **Remove library from file**. You can always add it back later.

### Access styles, components, and variables in a site file

When you add a library to a site file, everyone in the file can use its assets.

Styles Components Variables

Select an element, then use the  **Style and variables** picker on the relevant property in the right sidebar. Applying a style in Figma Sites [works the same way as in Figma Design](https://help.figma.com/hc/en-us/articles/360040316193).

In the **Insert** tab, click a library to view its components, then drag the ones you want to use onto the canvas. Using components in Figma Sites is very similar to [using them in Figma Design](https://help.figma.com/hc/en-us/articles/360039150173).

Variables can be applied to various properties in the right sidebar. Learn how to [apply variables to designs in Figma Design](https://help.figma.com/hc/en-us/articles/15343107263511), which works the same way in Figma Sites.
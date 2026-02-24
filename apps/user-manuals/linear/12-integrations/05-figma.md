# Figma

We use Figma at Linear and our integrated tools make it easy for you to collaborate on design.

![Linear and Figma logos](https://webassets.linear.app/images/ornj730p/production/715e73405ea73596781be7d43896081207e38598-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

There are two ways to connect Figma to Linear to streamline your design and development workflows. The Linear plugin for Figma allows you to create and link issues directly from Figma. A separate integration enables you to embed designs into Linear descriptions, comments and documents. 

### Keyboard

`G` then `S` to go to Settings

Paste the link to embed file

Click on files to open in Figma (no shortcuts)

To update the preview, use `E` to go into issue edit mode or select the more menu (three dots) to edit a comment, then hover to bring up the refresh button

### Mouse

* Paste the link to embed file
* Click on the link to open in Figma
* To update the preview, go into issue or comment edit mode, then hover to bring up the refresh button

### Command menu

No command menu options available

## Configure

#### Embed Figma previews in Linear

Connect to Figma under _[Settings > Features > Integrations > Figma](https://linear.app/settings/integrations/figma)._ We recommend that you do this in a browser and not the desktop client. Once connected, the integration will work across your full workspace.

#### Linear plugin for Figma

To create or link issues from Figma, select a frame, section or link and run the Linear plugin from Resources > Plugins > Linear or run directly from the Figma community [here](https://www.figma.com/community/plugin/1221187540287746170).

## Embed Figma Previews

#### Preview designs

Simply copy a link to specific frames or files and paste it into a Linear issue description or comment. We automatically convert the link into a design preview. Even if the file changes, the snapshot in Linear remains as it appeared when the comment or description was created. 

#### Open files

Click to preview the embedded file without having to leave Linear. We currently support interactive in-app preview of publicly shared Figma files only. We're considering building support for private files in the future. We built this as a custom integration using Figma's API with their OAuth2 authentication instead of using their standard embed to create a faster experience.

#### Refresh files

By default, we do not refresh the Figma preview so that you maintain the context of related comments and issue descriptions. To update the preview, go into Edit mode in the issue or comment, then hover over the Figma file. You'll see a Refresh button appear, which you can click to pull the latest version. This action cannot be undone.

## Linear Plugin for Figma

Run the plugin to see all Linear issues linked to your designs. From the plugin, select issues or the linked elements below the issue description to be taken to the inked frame, section, or page.

![Video](https://webassets.linear.app/files/ornj730p/production/07a275c0f4339777fabf3443dd1589736bec60ef.mp4)

## Create issues

When using the [Linear plugin](https://www.figma.com/community/plugin/1221187540287746170/Linear) from within Figma, select the `+` button to create issues that link pages, frames, and sections of your Figma design. You'll be able to create issues in any teams that you've joined. 

#### Link issues

Link designs to existing issues by searching for the ID, title, or description. From the Linear side, you can link designs to issues by attaching Figma links for the page, section, or frame using `Ctrl` `L`. You can link multiple issues to the same design and multiple frames, sections, or pages to a single Linear issue. 

#### Update issues

Update properties such as team, status, assignee, and project directly from Figma. You'll be able to update these at any point during your design process. Any changes made in Linear are immediately synced to the Figma plugin.

#### Filter and sort

Filter your issues that appear in the plugin window to hide completed or cancelled issues, show only assigned or created by you, and to sort by status, priority, nam, or created date. By default, the plugin will hide canceled issues.

## Figma Plugin 

### Privacy Policy

1. **Terms of Service** By authenticating the plugin, you agree to Linear's [Terms of Service](https://linear.app/terms). Plugin authentication grants you access to Linear's features and functionality.
2. **Figma File Key Transmission** When the plugin is opened within Figma, Linear will receive the file key for the current Figma file. When connecting a frame in Figma to a Linear issue, Linear will receive and securely store the file key associated with the respective Figma file. This storage of file keys allows Linear to establish the necessary connection and enable bi-directional linking between Figma and Linear.
3. **Figma File Key Access** Any user with access to a Linear issue will also have access to the associated file key for any linked Figma frames.
4. **Data Removal** Users have the authority to remove Figma data stored by Linear at any time. This can be achieved by either disconnecting the frame from the Linear issue or deleting the associated team or workspace. To permanently delete your data from Linear’s storage contact security@linear.app
5. **Data Processing** All data, including Figma file keys, is processed by Linear in accordance with Linear’s Data Processing Agreement ([DPA](https://linear.app/dpa)). The DPA outlines the measures taken by Linear to ensure the privacy and security of customer data. For more details on our data processing practices, please refer to our [DPA](https://linear.app/dpa).

## FAQ

<details>
<summary>My Figma integration stopped working. How do I fix it?</summary>
First, check that the Figma integration is connected in [settings](https://linear.app/settings/integrations/figma). We'll disable integrations if we notice they're not working anymore (admins should receive an email if we do) and it's also possible that someone on your team removed the integration, intentionally or not. 

If the Figma integration is enabled and it's still not working, try removing and then reconnecting the integration. 

1. Open Linear in the browser and remove the integration.
2. Go to linear.app/reset 
3. Reconnect to Figma via the browser. 

Reach out to us in support if you still have trouble after taking those steps.
</details>

<details>
<summary>Can I collapse or hide the Figma embed?</summary>
By default, any Figma links added to Linear will embed and there is no way to hide it. The workaround is to hyperlink text in a comment or description instead of pasting the full link.
</details>

<details>
<summary>I keep getting prompted to login to Figma yet cannot view the preview. Help?</summary>
We've noticed this issue specifically for If your Brave shield is up you must manually allow "cross-site cookies" to be able to view authenticated Figma embeds.

![Brave browser settings](https://webassets.linear.app/images/ornj730p/production/aad6a15aa033a4d4ccd01d6c4e866d75fd218f3d-834x1164.png?q=95&auto=format&dpr=2)
</details>

<details>
<summary>I'm seeing the error message "unable to embed from Figma" when linking a Figma file.</summary>
This error message typically also references "Insufficient permissions to access the file". While you yourself may have access to the file, it's important that the installer of the Figma integration in Linear also has access to the file. If they don't this error message will appear. The solution here is to share the file with the team member who installed the Figma integration.
</details>

<details>
<summary>Figma is not working on desktop</summary>
Connect the integration using Linear in a web browser. If the integration doesn’t work on the macOS app, open Linear in a browser and disconnect the integration. Then open the macOS app and clear application data (found under Linear in the application menu bar). Open Linear in the browser again and reconnect to Figma. If that doesn’t work, reach out to us at [support@linear.app](mailto:support@linear.app).
</details>

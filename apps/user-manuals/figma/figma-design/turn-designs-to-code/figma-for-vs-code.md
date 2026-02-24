# Figma for VS Code

Source: https://help.figma.com/hc/en-us/articles/15023121296151-Figma-for-VS-Code

---

Before you Start

Who can use this feature

Available on all paid plans

Requires a [Full or Dev seat](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor)

The Figma for VS Code extension provides an easy way for developers to access and inspect designs right from VS Code. You can navigate and inspect design files, collaborate with designers, track changes, and speed up design implementation—all without leaving your development environment.

Use the Figma for VS Code extension to:

- See and respond to comments and activity in real time
- Get code suggestions based on designs
- Link code files to design components

You can install the [Figma for VS Code extension](https://marketplace.visualstudio.com/items?itemName=figma.figma-vscode-extension) from Visual Studio’s Marketplace. You’ll be prompted to sign in to your Figma account when you first open the extension in VS Code.

# Open Figma designs in VS Code

There are a couple of ways to open a design file through the VS Code extension:

**From Dev Mode**

1. Set CSS as your preferred language in **Code** **settings** or the **Code** section of the Inspect panel.
2. Click on a top-level frame.
3. In the Inspect panel, click **Options** next to the layer name.
4. Select **Open in VS Code**.

**From VS Code**

1. Open VS Code.
2. Click Figma in the activity bar, or find Figma for VS Code from your list of extensions.
3. In the primary sidebar under Files, click on the design you want to open.

# Inspect Figma designs in VS Code

![VS Code showing the Figma extension in the sidebar with an HTML file open, illustrating integration for inspecting designs.](https://help.figma.com/hc/article_attachments/20999160449815)

## Explore a design file in VS Code

Figma for VS Code extends the functionality of Dev Mode’s inspection features and brings design files right to your text editor. When you select a design file in VS Code, you’ll see frames in the file grouped by section, status (e.g ready for development) and page. If a frame doesn’t have a parent section, or an assigned status, those won’t be visible.

## Inspect a frame

Select from a grid of frames and see them individually with focus view. Search for frames and filter through results to quickly find what you’re looking for.

## See which designs are ready for development

Click Layers in the toolbar to view sections marked as Ready for development.

## View code snippets

View code snippets and relevant information like modes and styles in the **Code** tab.

Choose your preferred language and unit for code snippets in the top-right of the Inspect toolbar.

## Access Dev resources

Access relevant development links in the **Dev resources** tab. Click **Add Dev resources** to add a link to a code file or dev resource.

If a link has a matching implementation in your current codebase, it opens the file in VS Code instead of the browser.

[Link Dev resources to layers in Dev Mode →](https://help.figma.com/hc/en-us/articles/15023231995927)

## View component properties

If you have a component selected, you can view its properties in the Component tab.

## Export assets

Download and export assets for a selected layer in the **Assets** tab.

[Learn more about exporting selections from Figma →](https://help.figma.com/hc/en-us/articles/360040028114-Export-from-Figma)

## Auto-complete code suggestions

The Figma for VS Code extension provides auto-complete suggestions based on the selected layer. This is helpful if you’re building components that don’t have an existing implementation in your codebase.

## View comment notifications

You can view comment notifications in real time under **Notifications** in the primary sidebar. Click on a notification to view and add a comment to the design through VS Code.

[Guide to comments in Figma →](../comments/guide-to-comments-in-figma.md)

## Run plugins in VS Code

Leverage third party tools and customized code without leaving your code editor.  [Check out our docs to learn how to make your private plugin work in VS Code →](https://www.figma.com/plugin-docs/working-in-dev-mode/#how-to-get-started)

## Log out of Figma for VS Code

1. While in VS Code, Press `Shift` `Command` `P` to **Show and Run Commands**.
2. Select **Figma: Log out** from the list of options in the search bar.
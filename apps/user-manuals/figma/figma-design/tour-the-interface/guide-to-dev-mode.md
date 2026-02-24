# Guide to Dev Mode

Source: https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode

---

Before you Start

Who can use this feature

Available on all paid plans

Requires a [Full](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor) or a [Dev seat](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-GA-for-admins#h_01HKN19J4JJTKGMATHW6BP331A)

Dev Mode in Figma gives you everything you need to navigate design files and transform designs into code. With Dev Mode, designers and developers can stay on the same page, making sure important details aren’t lost in the handoff process.

Developers use Dev Mode to:

- Access advanced inspection capabilities and more codegen languages
- Make sure they’re building with the latest specs by easily comparing frame versions
- Quickly review designs that are ready for development with statuses and annotations
- Streamline workflows with developer-focused integrations, like JIRA, Storybook and GitHub
- Explore all variants in a component set without editing the file
- Link designs to tickets, documentation, and code components
- Inspect designs and write code side-by-side using the Figma for VS Code extension

## Enter Dev Mode

Dev Mode is a developer-focused interface for inspecting and navigating designs. You can access Dev Mode in any Figma Design file. To toggle between Design Mode and Dev Mode:

1. Open a Figma Design file.
2. Click the Dev Mode toggle or use the keyboard shortcut `ShiftD`.

![Dev Mode interface with navigation, canvas showing design variants, and inspect panel displaying component details.](https://help.figma.com/hc/article_attachments/26975850870551)

Note: You are automatically dropped into Dev Mode when you open a Figma Design file with a Dev Mode link.

## Navigate

In Dev Mode, the left sidebar provides an easy way to move between designs marked as ready for development.

![Dev Mode panel showing designs marked ready for development, with edit dates and layer structure for easy navigation.](https://help.figma.com/hc/article_attachments/26975834817175)

- A 

 #### View which assets are ready for development

 The Dev Mode icon indicates which pages contain frames, components, instances, and sections marked ready for dev. Objects on the canvas marked as ready appear under **Ready for development** in the Dev Mode layers panel.

 To mark an asset as ready for dev:

 1. While in Dev Mode, select a frame, component, instance, or section.
 2. Click **Mark as ready for dev** in the toolbar.

 Additionally, if you have a full, dev, or viewer seat in an org or enterprise, Dev Mode provides a [view](#h_01J04M14T5XBGDZ8S4A0NHM713) of designs that are marked ready for dev. The ready for dev view appears only when one or more designs in the file have a dev status.
- B 

 #### Know when a frame was last edited

 You can see when a frame was last edited under the frame’s name in the navigation panel.
- C 

 #### Navigate frames and layers

 In Design Mode, anyone can group related content into sections and mark sections as ready for development. Dev Mode will prioritize content in a section. Any content outside of a section is still visible in the left sidebar, but is collapsed by default.

 Click a frame in the left sidebar to center it on the canvas. Select the frame on the canvas to view the layers nested inside it. Selecting a frame changes the navigation panel to a layers panel and only shows the layers for the currently selected top-level frame.

 [Navigate frames and layers in Dev Mode ->](https://help.figma.com/hc/en-us/articles/15023152204951)

**Note:** You can [access version history](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history#View_a_version) from the file name menu while in Dev Mode to view and inspect any version of a design file.

## Inspect

The inspect panel displays design specs and relevant component information needed to understand a design and transform it into code.

![Inspect panel showing notification component details, layout properties, interactions, assets, and export options.](https://help.figma.com/hc/article_attachments/32233541075479)

- A 

 #### View layer names and types

 The selected layer's name is displayed at the top of the inspect panel, along with its layer type (component, instance, frame, text, etc.). You can also see when the layer was last updated.
- B 

 #### Compare design changes

 If changes have been made to a design, **Compare changes** will appear below the layer information in the inspect panel. Click the link to open the frame history modal where you can compare current version to previous versions of the design.

 In the case of component instances, **Compare with main component** appears below the layer information in the inspect panel. You can also compare a [detached component](../use-libraries/detach-an-instance-from-the-component.md) to previous versions, and to the main component it was once linked to. You can clear its detachment history to avoid seeing information about its original main component.

 [Compare changes in Dev Mode](https://help.figma.com/hc/en-us/articles/15023193382935)
- C 

 #### Add external links and resources for developers

 Both designers and developers can add links to external resources that may help with the implementation of a component. This can include GitHub, Jira, and Storybook links, as well as VS Code links that can be used with the [Figma for VS Code extension](https://help.figma.com/hc/en-us/articles/15023121296151). Dev resources added to components propagate to all the instances of that component.

 [Add resource links to layers in Dev Mode](https://help.figma.com/hc/en-us/articles/15023231995927)
- D 

 #### View component information

 When you select a component, the inspect panel displays information and metadata about the component, including keywords, the layout of the main component, variant information, and component properties.
- E 

 #### Try component variations in the component playground

 When you select a component or instance, **Explore component behavior** appears below the component information. Click **Explore component behavior** to open the component playground. Use the playground to experiment with the component's different properties and variable modes without changing the actual design.
- F 

 #### Get recommended code with Code Connect

 Code Connect is a tool for design systems and engineering teams to bring component code into Dev Mode. When inspecting a component with connected code snippets, developers will see design system code from their libraries instead of auto-generated code. Use Code Connect to:

 - Make custom component code easily available to drive design system adoption
 - Map out variants and properties of a design component in code for consistency across product teams
 - Create examples for specific component use cases to help developers understand its correct usage

 Custom code snippets build on the Figma API and are fully customizable to support multiple design systems, products, and languages.

 [Check out the Code Connect overview to learn how to connect custom code snippets to components.](https://help.figma.com/hc/en-us/articles/23920389749655)

 **Note:** Code Connect is available on Organization and Enterprise plans.
- G 

 #### View layer properties

 The layer properties section of the inspect panel contains detailed information about the layer you've selected. The information includes the layout and spacing of the layer, layer properties represented either as a list or as code, colors used in the layer, and any prototype interactions that have been applied to the layer. Use the toggle in the layer properties section to swap between **Code** (default) and **List**.

 **Customizable code snippets**

 ![Code snippet in Dev Mode showing layout and style properties for a component, illustrating customizable code output.](https://help.figma.com/hc/article_attachments/32233527183255)

 When you toggle to **Code,** the inspect panel displays autogenerated code snippets for the layer.

 You can select the language and units to view in the canvas and generated code, as well as extend the functionality of code snippets with codegen plugins. To change the language or select a codegen plugin:

 1. In the top-right of the **Code** section, select a language or plugin from the dropdown.
 2. For settings specific to that language, such as changing the unit of measure for CSS, scroll to the bottom of the dropdown and select the settings you want.

 [Learn how to use code snippets in Dev Mode](https://help.figma.com/hc/en-us/articles/15023202277399)

 **List properties and values**

 ![Panel showing layer properties in Figma Dev Mode, with layout and spacing details in list format.](https://help.figma.com/hc/article_attachments/32233527185047)

 When you toggle to **List**, the inspect panel displays a list of properties that are set for the layer and the corresponding values for those properties. You can click on the values to copy them to your clipboard.
- H 

 #### View applied styles

 View styles and variables applied to the selected layer. Additionally, you can [view details about variables](../inspect-designs/variables-in-dev-mode.md#h_01JD03NW7F4WS8EXKQHS6E5M1V), and get [suggested variables](../inspect-designs/variables-in-dev-mode.md#h_01JD03NW7FA3PYRN5PK9GD2VZ5).
- I 

 #### Download assets

 Dev Mode can automatically detect icons and present them as downloadable assets for developers. If you want to inspect an individual vector layer contained in an icon, you can turn off automatic icon detection:

 1. Click **Main menu** in the toolbar
 2. Hover over **View** in the dropdown
 3. Deselect **Automatically detect icons**

 The **Assets** section will also allow you to download GIF image and MP4 video nodes, and the [source file of an image](https://help.figma.com/hc/en-us/articles/22012921621015/live_preview/01JWYCA764WR2KENRF7Q5DA6KH#h_01JWYBRK4VGF5BAPSN9XMQ6GDZ) at its full resolution.
- J 

 #### Export

 You can apply export settings to layers to define the format and any other export settings. Figma supports the following export formats: PNG, JPG, SVG, and PDF. [Learn more about exports in Figma.](https://help.figma.com/hc/en-us/articles/360040028114)

**Note:** You can access [layout guides](https://help.figma.com/hc/en-us/articles/360040450513-Create-layout-grids-with-grids-columns-and-rows#h_fa39b302-65b2-4cb7-9153-25ddcf76929f), [rulers](../file-utilities/add-guides-to-the-canvas-or-frames.md#Toggle_rulers), and [layer outlines](https://help.figma.com/hc/en-us/articles/5724448965527-View-layer-outlines-in-Figma-design) in Dev Mode.

## Annotate

![Cursor clicking in Figma's Dev Mode interface, illustrating annotation and measurement capabilities for developers.](https://help.figma.com/hc/article_attachments/24163086307095)

Designers can use annotations to markup designs with additional context, specs, and measurements. This makes it easy for developers to make sure they don’t miss any crucial callouts during handoff. Use annotations and measurements in Dev Mode to:

- Surface important properties so developers can't miss them
- Help developers quickly visualize spacing and sizing
- Add additional context with text notes connected directly to the designs

[Learn how to add measurements and annotate designs in Dev Mode →](https://help.figma.com/hc/en-us/articles/20774752502935)

## Manage dev handoff

When you have sections, frames, and components that are [marked ready for dev](#h_01JA8Z1DAZSGZ1M4AV2RK05C65), you can take advantage of Dev Mode’s ready for dev and focus views to help manage your developer handoff process:

- Ready for dev view provides an easy way to explore all designs in a file that are marked ready for dev. You can filter and see all your designs that are marked ready for dev. [Learn more about ready for dev view and the handoff process →](https://help.figma.com/hc/en-us/articles/23918228264855) 
 ![Design file in Dev Mode showing order completion frames marked "Ready for dev" with recent changes noted.](https://help.figma.com/hc/article_attachments/24382888515351)
- Focus view shows only one design that’s ready for dev at a time. You can use all of your usual Dev Mode tools, explore the layers of the design, and find important info like an annotated version history. [Learn more about focus view →](https://help.figma.com/hc/en-us/articles/23919923330455) 
 ![Design file in Dev Mode showing bakery product images with annotations and an inspect panel displaying variation details.](https://help.figma.com/hc/article_attachments/24382888520855)

## Dev Mode statuses and notifications

Statuses and notifications in Dev Mode help to manage developer handoff. [Statuses](https://help.figma.com/hc/en-us/articles/26781702258583#h_01J96T2MJRVVH4JVPWJSMCGHQX) are used to track when sections, frames, or components are ready for development. [Notifications](https://help.figma.com/hc/en-us/articles/26781702258583#h_01J96T2MJRH0Y3ZAKB13FKS9W1) are based on status changes so developers can react to the state of designs.

### Statuses

All plans that provide Dev Mode include the **Ready for dev** status. You can set the **Ready for dev** status on components, frames, and sections, to indicate that the design is ready for development. An additional status, **Completed**, is available if you're on an Organization or Enterprise plan.

For more information, such as how to use statuses, see [Dev Mode statuses and notifications](https://help.figma.com/hc/en-us/articles/26781702258583#h_01J96T2MJRVVH4JVPWJSMCGHQX).

### Notifications

If you’ve viewed a file in Dev Mode and have either a Full or Dev seat, you’ll be notified each time a design is marked ready for dev in that file. This includes the first time a design marked ready for dev, as well as when the ready for dev status is removed and then set again.

For more information, including how to turn Dev Mode notifications on and off, see [Dev Mode statuses and notifications](https://help.figma.com/hc/en-us/articles/26781702258583#h_01J96T2MJRH0Y3ZAKB13FKS9W1).

## Use Dev Mode plugins

Dev Mode plugins help you automate tasks and connect other tools for documentation and communication. For example:

- Stay on track with development tasks by syncing with Jira across Figma, FigJam and Dev Mode
- Connect your Figma Design system and design system in code with Storybook
- Link designs to code, so they always stay in sync, by bringing Github into Figma.
- Customize code output (for Tailwind or React) or for your own code components

The **Plugins** tab in Dev Mode shows your recently used plugins, as well as recommended plugins from the Figma Community.

[Learn how to use plugins in files →](https://help.figma.com/hc/en-us/articles/360042532714-Use-plugins-in-files)

Check out the [Plugins for Dev Mode playground file](https://www.figma.com/community/file/1286813780866360645/plugins-for-dev-mode-playground) to learn about Dev Mode plugins hands-on.

### Figma for VS Code

Figma for VS Code lets you navigate and inspect design files, collaborate with designers, track design changes, and speed up design implementation - all without leaving your text editor. Improve developer productivity by eliminating the context switching and busy work needed to turn designs into code.

- See and respond to comments and activity in real time
- Get code suggestions based on designs
- Link code files to design components

[Learn more about the Figma for VS Code extension →](https://help.figma.com/hc/en-us/articles/15023121296151)
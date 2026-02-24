# Edit a code layer

Source: https://help.figma.com/hc/en-us/articles/32596943880599-Edit-a-code-layer

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

[AI features must be enabled](https://help.figma.com/hc/en-us/articles/17725942479127-Control-AI-features-and-content-training-settings) to chat with AI

![](https://help.figma.com/hc/article_attachments/32699158258967)

[Code layers](https://help.figma.com/hc/en-us/articles/31242824165143) add custom functionality to your site, enabling you to explore ideas, experiment, and enhance your designs using the power of code.

To edit a code layer, double-click it on the canvas. You can also select the layer and click **Edit code layer** in the right sidebar.

Editing a code layer opens the composer window. From this window you can chat with AI, write your own code, preview the code layer, and adjust any [custom properties](#h_01JXB7CV7YTXE0Z8A4GJJNQ746).

**Tip**: To open the composer window in a full screen view—and preview all the code components and code layers in the file—click **More** at the top right of the window, then **Open in Make view**.

There are a few details to keep in mind as you work with code layers:

- Child elements of a code layer are represented in code rather than layers that can be directly manipulated on the canvas. It’s not possible to nest design layers within code layers.
- Code layers have fewer properties available than other layer types. For example, they don’t have fill, stroke, or effect properties—but you can manage these directly in the code and even [surface them as editable properties](#h_01JXB7CV7YTXE0Z8A4GJJNQ746).
- It’s not possible to publish code layers to a library yet.

## Chat with AI

**Note**: Chatting with AI requires your team or organization to [enable AI features](https://help.figma.com/hc/en-us/articles/17725942479127-Control-AI-features-and-content-training-settings).

In the chat interface, describe what you’d like to build. After you send your prompt, Figma starts writing the code for your code layer. Depending on the complexity of the request, it may take a few minutes for Figma to finish.

For advice on crafting effective prompts, check out the [guide to writing great prompts](https://www.figma.com/code-docs/how-to-write-great-prompts/) in our developer documentation.

The chat history stays attached to the code layer, even if you duplicate the layer or move it to another file.

**Tip**: You don’t need to keep the composer window open while it’s working. Close it and come back later when it’s finished. You can use this method to work on multiple code layers simultaneously.

### Restore a previous version

As you chat back and forth, Figma will add a checkpoint to the chat window for each revision to the code layer. To roll back to a previous version, scroll up in the chat window and click **Restore this version** on a checkpoint.

## Write your own code

Code layers use React, Typescript, and Tailwind CSS. You can copy and paste code directly into the code editor, or start writing from scratch. When writing your own code, you can do things like:

- Use external libraries
- Add motion using animation libraries
- Fetch data from external APIs

**Tip**: To learn more about writing code for code layers, check out the [guide to working with React in Figma](https://www.figma.com/code-docs/working-with-react) in our developer documentation.

## Use the edit tool to manipulate specific elements

![](https://help.figma.com/hc/article_attachments/32699158259863)

When previewing a code layer in the composer window, you can use the edit tool to point to specific elements of the preview.

Depending on the type of element and how it was generated, you can modify properties such as colors, padding, margins, text styling, and more. You can also prompt the model to make changes directly to that element.

To use the edit tool:

1. At the top of the preview, click **Edit**.
2. Select the element you want to modify.
3. Click **Edit properties** to make changes using the toolbar, or **Edit with prompt** to describe the changes you’d like to make. You can also select **Go to source** to jump straight to the relevant spot in the code.

Note: The exact set of properties you can edit depends on the type of element you’ve selected.

## Create and edit custom code layer properties

![](https://help.figma.com/hc/article_attachments/32699158260631)

Code layers can have customizable properties that control their behavior and appearance. These properties appear in the properties panel and enable people to modify the code layer without needing to edit its underlying code.

**Tip**: When editing a code layer, click to open the inline properties panel and console.

There are several property types available, with more coming soon:

| Type | Usage |
| --- | --- |
| String | String properties allow users to input text values into your code layer. They're perfect for configurable labels, headings, descriptions, or any text-based content. String properties can be controlled by a dropdown rather than an open input field, which is useful when you want your code layer to only accept a specific set of inputs. |
| Number | Number properties allow users to input numeric values into your code layer. They're ideal for dimensions, quantities, or for setting values like opacity levels. Number properties can be controlled by a slider or a dropdown for predefined options. |
| Boolean | Boolean properties allow users to toggle functionality or visibility for elements in your code layer. |
| Component reference | Component reference properties allow your code layer to incorporate instances of components from the current file or any available libraries. |

When chatting with AI, Figma will create custom properties based on your prompt. You can also request specific properties if needed.

You can code the properties yourself using the `defineProperties` function. [Learn more about using this function in the developer documentation.](https://www.figma.com/code-docs/define-properties/)

**Note**: When editing custom code layer properties in a webpage with multiple breakpoints, changes made to the properties on the [primary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879) won’t cascade to other breakpoints. This is different from other layers types, where edits do cascade.

## Adjust the responsiveness of a code layer

Code layers always use [auto layout](https://help.figma.com/hc/en-us/articles/360040451373), which helps the content reflow automatically as you resize the layer. You can prompt the AI or edit the code to make the content more or less responsive according to your needs.

When editing a code layer in a webpage with multiple breakpoints, it doesn’t matter whether you edit the code layer in the [primary or secondary breakpoint](https://help.figma.com/hc/en-us/articles/31242788601879) as any changes you make to the underlying code will apply to all breakpoints. To customize the code layer for each breakpoint you can:

- [Create custom properties](#h_01JXB7CV7YTXE0Z8A4GJJNQ746) and configure them for each breakpoint.
- Use the `useBreakpoint` hook, which detects the current breakpoint and can be used to adjust elements accordingly. [Learn more about using this hook in the developer documentation.](https://www.figma.com/code-docs/use-active-breakpoint/)

## Frequently asked questions

Can I reference elements of my design system, like components, styles and variables in a code layer?

Yes, you can work with components and variables in code layers:

- **Components**: Use a [component reference property](#h_01JXB7CV7YTXE0Z8A4GJJNQ746) to incorporate component instances in your code layer. This keeps the instances connected to their main components.
- **Styles**: It's currently not possible to reference styles in a code layer.
- **Variables:** You can bind any custom properties in the code layer to variables by hovering over the property name or value and clicking **Apply variable to property**.

Can code layers share information between them?

Not yet, but we're actively working to make this functionality available.

What should I do if the preview of my code layer is larger than the code layers itself?

If the content of the code layer extends beyond its bounds on the canvas, consider the following approaches:

- Prompt the AI with a phrase like: "The content is larger than its container. Can you make sure it is responsive to its container size?"
- Edit the relevant portions of the code.
- Check **clip content** in the right sidebar to hide any content that extends beyond the bounds of the code layer.

How do I work with fonts in code layers?

You can write CSS to change the font. For example, `<p className="font-['Roboto_Mono:Medium',_sans-serif] text-xl text-black">`

What happens if a design uses styles, components or variables, and then I convert it to a code layer? Will it still receive updates from my design system?

When you [convert a design to a code layer](https://help.figma.com/hc/en-us/articles/32641332638999), any instances, styles, or variables used in the design become detached from your design system.

## More resources

See how Lauren, a Figma Advocate, brings a florist’s website to life using code layers.
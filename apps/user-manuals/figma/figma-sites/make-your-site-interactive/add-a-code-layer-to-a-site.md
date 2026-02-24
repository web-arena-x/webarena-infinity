# Add a code layer to a site

Source: https://help.figma.com/hc/en-us/articles/32641332638999-Add-a-code-layer-to-a-site

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

[AI features must be enabled](https://help.figma.com/hc/en-us/articles/17725942479127-Control-AI-features-and-content-training-settings) to chat with AI

[Code layers](https://help.figma.com/hc/en-us/articles/31242824165143) are a powerful way to add interactivity to your site, whether you’re building collaboratively with AI, or writing code yourself.

There are three different ways to create a code layer, depending on what you’re looking to make:

| **Method** | **Benefit** |
| --- | --- |
| [Add a code layer using the Make tool](#h_01JXB6EF9G0Z3B6Z8C57EQR3V8) | Bring any idea to life by describing what you’d like to make, or writing the code yourself. Create carousels, mini-games, text effects—whatever feels right. |
| [Make a code layer from an existing design](#h_01JXB6EF9GGZA5X45YTX4DQQ3A) | Use an existing design as the foundation for the code layer. This is useful when you have a specific design and want to explore ways to add interactivity. |
| [Create a new component in **Make**](#h_01JXB6EF9GTS8YVQ4AXH4NV81J) | Create reusable code components whose instances can be placed throughout your site. When you update the component, all instances update automatically. |

## Add a code layer using the Make tool

![](https://help.figma.com/hc/article_attachments/32698706447127)

Use the **Make** tool in the toolbar—or use the keyboard shortcut `E`—to draw a code layer on the canvas or in a webpage. You can place the code layer anywhere, including inside an existing design or a webpage.

**Tip:** When creating a code layer directly in a webpage with multiple breakpoints, check which breakpoint you're adding it to:

- If you create it in the **primary** breakpoint, it is automatically added to all secondary breakpoints.
- When you create a code layer in a **secondary** breakpoint, it is visible only on that specific breakpoint and hidden in the others.

[Learn more about working across breakpoints.](https://help.figma.com/hc/en-us/articles/31242788601879)

## Make a code layer from an existing design

![](https://help.figma.com/hc/article_attachments/32698703084823)

You can turn any design into a code layer when you want to add interactivity to it. This action converts all the layers in the design to their corresponding code representations, making it easier to build out your idea.

You can also copy out or restore the original design in place if you need.

**Note:** Once a design is converted to a code layer, you won’t be able to access its child layers in the layers panel any more.

1. Select a design on the canvas. It can have as many child layers as you like.
2. In the right sidebar, click **Make code from design**.

**Note**: It’s not possible to create a code layer from a main component, a component set, or a variant within a component set.

### Copy out or restore the original design

If you still need to access the original design, select the code layer and click the **More** menu in the right sidebar.

1. **Copy out original design:** Keep the code layer and create a copy of the original design with all its layers to the side.
2. **Restore design:** Restore the original design in place. This option is useful if the design is already positioned in a webpage and you don’t want to reposition it.

## Create a code component in Make

![](https://help.figma.com/hc/article_attachments/32698729589655)

If you want to build for reusability from the start, create a code component in the **Make** view. You can then place instances of the component directly on the canvas wherever you want to use it in your designs.

1. Click **Make** in the left navigation bar.
2. Click **Add new code component**.

When you’re component is ready for use, click **Add to canvas** to place an instance on the canvas or in a webpage.

**Why create a code component first?**

Here’s an example of when a code component might be useful: Let’s say you want certain sections on your website to have a subtle gradient animation as a background—and you want the animation to look consistent wherever it is used.

By creating a component, you can dial in your animation timing and color scheme so its consistent everywhere you use it. You can then use instances of this component all over your site.

If you decide to change the component later, the changes will automatically apply to all instances on the canvas.

**Tip**: You can also turn a code layer into a component from the canvas by selecting it and clicking **Create component**.

## More resources

Watch Niko, a product manager at Figma, demo both code layers and instances of code components.
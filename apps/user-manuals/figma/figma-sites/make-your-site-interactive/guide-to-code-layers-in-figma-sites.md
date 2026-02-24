# Guide to code layers in Figma Sites

Source: https://help.figma.com/hc/en-us/articles/31242824165143-Guide-to-code-layers-in-Figma-Sites

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

[AI features must be enabled](https://help.figma.com/hc/en-us/articles/17725942479127-Control-AI-features-and-content-training-settings) to chat with AI

Code layers add custom functionality to your site, enabling you to explore ideas, experiment, and enhance your designs using the power of code.

Like frames and shapes, code layers are another type of layer you can add to the canvas in Figma Sites. What makes code layers unique is how you edit content inside the layer. When you [edit a code layer](https://help.figma.com/hc/en-us/articles/32596943880599), you can either describe what you’d like to create with AI, or write React code yourself. Or both!

People use code layers to:

![Colorful abstract shader with interactive ripple effects responding to cursor movement](https://help.figma.com/hc/article_attachments/32742619150359)

**Create new site elements entirely in code**

![Dot grid with proximity-based scaling interaction where dots expand near the cursor](https://help.figma.com/hc/article_attachments/32742619153687)

**Create custom interactions**

![Gallery grid displaying artwork from the Art Institute of Chicago API](https://help.figma.com/hc/article_attachments/32742619154711)

**Connect real data sources to your designs**

![Interactive image carousel with rotating slides](https://help.figma.com/hc/article_attachments/32742619159703)

**Add motion or animations to an existing design**

## Key features

### **Chat with AI, or write your own code**

In the code composer, you can describe what you want to make, refine it, or even roll back to previous versions. If you’d prefer to work with the code directly, use React, Typescript, and Tailwind CSS to bring your idea to life.

[Learn more about working with code in Figma’s developer documentation](https://www.figma.com/code-docs/working-with-react).

Caution: For your security, API keys should never be added to code layers. Adding API keys will put them at risk of being discoverable and usable by other people, and may result in additional issues such as incurring additional costs from the API tool.

### **Use existing designs or start from scratch**

You can convert an existing design to a code layer to add interactivity and expressiveness to it. Or, you can create a new code layer on the canvas and start describing your vision without any reference designs.

[Learn more about creating code layers from existing designs.](https://help.figma.com/hc/en-us/articles/32641332638999)

### **Turn code layers into components and instances**

Like other layers, code layers can be turned into reusable components. You can then insert instances of the same component on the canvas.

For example, imagine you want to show live stock prices for different companies on your website. You want each of them to look the same, have the same functionality, but for different stocks.

You can create one stock ticker component, then place many instances of that component in your site.

### What’s the difference between code layers and Figma Make?

[Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make) is an AI-driven, prompt-to-app tool that lets you bring ideas and existing Figma designs to life as functional prototypes, web apps, and interactive UI.

With code layers, you’re accessing the power of Figma Make inside of Figma Sites. Here is some advice for picking which tool to use:

Use Figma Make if:

- You want to start purely from a prompt and get all the way to a functional app
- You don’t need a canvas or don’t want to do a lot of precise designing

Use code layers in Figma Sites if:

- You’d rather start designing on the canvas and want to add custom interactivity and/or motion
- You’re adding interactivity to a website design

Ready to dive in? Get started by [creating your first code layer](https://help.figma.com/hc/en-us/articles/32641332638999).
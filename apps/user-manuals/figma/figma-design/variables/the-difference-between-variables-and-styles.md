# The difference between variables and styles

Source: https://help.figma.com/hc/en-us/articles/15871097384471-The-difference-between-variables-and-styles

---

As Figma extends its feature set with variables, you might be wondering: What is the difference between variables and styles? When should I choose one over the other? Are styles becoming obsolete?

After all, they seem to function similarly on the surface:

- Both act as sources of truths.
- Both can be published to team libraries and reused throughout designs.
- Both support efficient design system management because updates to a variable or style will prompt updates for all designs using them.

Styles and variables have key differences that make them valuable in different situations.

In this article, we’ll highlight their differences and help you decide whether to use on, or both, in your designs.

## Foundational differences

There are a couple of key differences between styles and variables: the types of values they use, their appearance on canvas, and the use of modes.

**Styles** can store a variety of properties:

- A property with a single raw value, like a solid fill `#FFFFFF`
- A property with multiple raw values, like a color gradient
- Other formats like blend modes, images, GIFs, videos

Styles are built to hold a combination of values, where all values get expressed all at once. For example, you can store font family, font size, and font weight properties in one text style simultaneously. When you apply the text style on a text layer, all properties will be used on the text layer at the same time.

In another example, let's take a look at color styles which can be a combination of different fill types and variables, and are organized in a top-to-bottom stack. A color style is like looking at a “stack” of cards from above, where each card is a fill. If the color at the top is transparent enough, you can see the color below it. You can also manually rearrange the fill to change what you see from the top.![Animation of the Edit color style modal with a cursor reordering stack of color fills](https://help.figma.com/hc/article_attachments/16007056182551)

**Variables** can store single, raw values. For example, raw values can include solid fills like `#FFFFFF`, numbers like `16` or `-32.75`, and boolean values `true` and `false`.

Variables are built to hold one or more single, reusable values, but only one value can be expressed at a time. Each value corresponds to a different [variable mode](https://help.figma.com/hc/en-us/articles/15343816063383). This is true of all variable types. Unlike styles, a variable is like set of cards with where you can view only one card, and what card you get to see depends on its context.

For example, let’s say we have a collection of variables with light and dark modes. We apply them to various layers in a frame, and set the frame to dark mode. All layers with the variables will express the values from dark mode. If we switch the frame to light mode, the variables will switch their expressed values to light mode. ![Animation of mode switching where an example product page for an ecommerce site switches from light mode to dark mode and all the colors instantly update](https://help.figma.com/hc/article_attachments/16007126603799)

Even though modes are built for variables, Figma allows us to apply them to styles.

> Say we have a number variable for a default font size. The variable has two single, raw values: `16` for a mobile mode and `18` for a desktop mode. We apply this variable to a text style’s font family property, as well as other variables and values to other properties.  
>   
> Now, we can switch the mode on any text layer using this text style, because it uses a variable with multiple modes.

[Learn how to back styles with variables.](https://youtu.be/vCnB8bAEFl4)

Takeaways

- A variable stores raw, reusable values. Styles stores a composite of different values.
- If a variable has multiple values (i.e. modes), it can only express one value at a time. A style’s composite of values are expressed all at once.
- If you want to create different contexts for your design elements (such as light and dark modes) you will need to use variables and variable modes.

## Scalability and management

One of the most powerful ways of managing and scaling a design system is through aliasing tokens.

- A **design token** is an industry term to refer to reusable values, meant to help design and code stay in sync.
- **Aliasing** is a method of organizing a design system by allowing any design token to inherit the value of another design token.

Variables allows you to do exactly this.

For example, let’s say the variable "brand-400" (which is one of our design tokens) has a value of `#EAEA00`. We want the variable "icon-default" (another design token) to be an alias of brand-400, meaning it will inherit whatever value brand-400 has.

![Design token aliasing example: "brand-400" with green color #EAEA00, "icon-default" inherits the same color as an alias.](https://help.figma.com/hc/article_attachments/22826592601751)

If the value of brand-400 ever changes, then icon-default will follow suit, as long as it’s still bound to brand-400’s definition.

![Color token aliasing in Figma, with "ICON-DEFAULT" inheriting value from "BRAND-400" shown as pink swatches.](https://help.figma.com/hc/article_attachments/22826623803799)

Styles don't support aliasing. In other words, they cannot be applied to variables and other styles. Variables can be applied to both.

Because variables support aliasing, it offers more robust support for complex, scalable token structures. They allow you to define primitive values that can flow through other tokens and elements of your design system. It also makes updating and managing design systems more efficient.

For example, let’s say we create a variable that acts as a global token, and we use it to define other variables at varying levels. If the global token changes, then everything downstream changes.

![Animation showing cascading changes when the cursor changes global token from pink to coral and all tokens downstream change](https://help.figma.com/hc/article_attachments/16012830510743)

If we only want *some* tokens to change, this structure allows us to choose the correct token upstream and change it without having to manually rework everything downstream.

![Animation showing creation of new global token and only certain downstream tokens are affected](https://help.figma.com/hc/article_attachments/16012830513175)

Aliasing is supported for all variable types. Learn how to [alias variables](https://help.figma.com/hc/en-us/articles/15145852043927#alias).

Takeaways:

- Variables can be applied to styles and other variables, but styles cannot be applied to either
- Variables help scale a growing design system and make managing a design system more efficient

## Supporting features

### Scope variables

Scoping is fully supported for number variables but will be expanded to other variable types in the future.

Scope variables to limit which properties a variable can be applied to.

For example, you can limit a color variable to only stroke fills, so you wouldn’t be able to apply the variable to any other fill properties. This gives you better control over where it can be used and cuts out the guesswork when designing.

[Learn how to scope variables.](https://help.figma.com/hc/en-us/articles/15145852043927#h_01H32HZB74TE7MJXYBWEBBQWJV)

Takeaways:

- Since scoping is available to variables but not styles, use variables if you want to take advantage of scoping capabilities
- Scoping is currently available for number variables and will expand to other types in the future

### Prototype with variables

In prototyping, variables are used to store object states or properties. Prototype interactions are used to modify variable values, which can change the appearance, content, or visibility of objects in a design—all in a few simple frames.

[Learn how to use variables in advanced prototypes.](https://help.figma.com/hc/en-us/articles/14506587589399)

### Code syntax with variables

Code syntax is currently in development and will be available soon.

When you open a variable’s editing modal, you’ll see a section titled **Code syntax**. Code syntax represents variables in code using valid variable names. This information will appear in [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247) and will help designers and developers create a seamless handoff experience.

[Learn more about code syntax.](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables#code_syntax)

Takeaway: If you're looking to improve your handoff experience, you can take variables and code syntax into consideration

## Final thoughts

Whether you choose to use variables or styles depends largely on your goals. You might focus solely on variables to take advantage of design token scalability. Or you might find that sticking to styles is suitable for your projects. Or you might end up using some combination of both!

Styles will remain ‌a key feature in Figma Design. Despite their similarities, variables are not a replacement for styles. Rather, they are additive to Figma’s core feature set.
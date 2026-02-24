# Guide to variables in Figma

Source: https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma

---

Before you Start

Who can use this feature

 

Variables in prototypes and publishing variables to team libraries are available on the [education plan and any paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with can edit access to a file can create and manage variables

Anyone with access to a file can use variables from that file in their designs

Variables in Figma Design store reusable values that can be applied to all kinds of design properties and prototyping actions. They help save time and effort when building designs, managing design systems, and creating complex prototyping flows.

For example, you can:

- Create design tokens for better efficiency when managing design systems
- Switch a frame between different device sizes and have spacing immediately update, according to a defined spatial system
- Preview how text flows in different languages by switching copy on a frame
- Create a fully functional checkout cart design that calculates order total based on which items were added to the cart
- Build a prototype of an interactive quiz that uses conditional logic to show whether a user answers a questions correctly or incorrectly

There are three main ways to use variables in Figma:

1. [Designs and design systems ↓](#h_01H3AECYSXVMKV6H60WJ9SF84F)
2. [Advanced prototyping ↓](#h_01H3AED6XW5K1DKGXJWEMSF303)
3. [Figma APIs ↓](#h_01H4S62F4ERWJQ6B4DZ7NBCJWC)

## Variables for designs and design systems

Use variables and modes to implement design tokens for your design system, switch designs between different contexts—such as light/dark themes. With variables, you can design more efficiently and build a more powerful design system.

- **Figma tutorial: Intro to variables**

 This video tutorial covers the foundations of variables, how to use them to represent design tokens, and how to use color and number variables to account for different modes and themes.
- **Figma tutorial: Variables for typography**

 In this video tutorial, learn how to use variables on font properties, adopt variables into an existing type system, and how to use them to power a responsive design.
- **Article: [Overview of variables, collections, and modes →](https://help.figma.com/hc/en-us/articles/14506821864087)**

 Start your variables journey here! Learn about the different types of variables and what variable collections and modes are.
- **Article: [Create and manage variables and collections →](https://help.figma.com/hc/en-us/articles/15145852043927)**

 Learn how to create variables and collections, reference other variable definitions, and scope which variables can be used in designs.
- **Article: [Apply variables to designs →](https://help.figma.com/hc/en-us/articles/15343107263511)**

 Learn how to apply existing variables to design properties.
- **Article: [Modes for variables →](https://help.figma.com/hc/en-us/articles/15343816063383)**

 Learn how to create multiple definitions for a variable, each one associated with a mode. Also, learn how to use them to quickly switch the contexts of designs.
- **Article: [Extend a variable collection →](https://help.figma.com/hc/en-us/articles/36346281624471)**Learn how extending your variable collections can help you manage multi-brand design systems.
- **Article:**[**The difference between variables and styles →**](https://help.figma.com/hc/en-us/articles/15871097384471) 

 As Figma extends its feature set with variables, you might be wondering: What is the difference between variables and styles? When should I choose one over the other?
- **Article:**[**Variables in Dev Mode →**](https://help.figma.com/hc/en-us/articles/27882809912471) 

 Learn more about accessing variables in Dev Mode while inspecting designs, including getting variable details and suggested variables, and viewing local collections using the variables table.
- **Community file: [Variables playground →](https://www.figma.com/community/file/1234936397107899445)**

 Want to get hands-on experience with variables? Grab a copy of the variables playground file to practice while you learn.

## Variables for advanced prototyping

With variables, you can build high-fidelity prototypes using fewer frames. Use variables with other advanced features like expressions and conditionals to take your prototypes to the next level.

In prototyping, variables are used to store object states or properties. Use prototype interactions to modify variable values, which can change the appearance, content, or visibility of objects in a design—all in a few simple frames.

- **Video tutorial: Prototype with variables**

 Watch and learn how to use variables in prototypes by following along with a realistic example. You’ll review how to modify variable values, how to build simple expressions, and how to use multiple actions and if/else logic to evaluate conditional checks.
- **Article: [Use variables in prototypes →](https://help.figma.com/hc/en-us/articles/14506587589399)**

 Learn the basics of how to prototype with variables in Figma—including how to configure your variables, use the **Set variable** action to change variable values, and use variables with component variants and interactive components.
- **Article: [Use expressions in prototypes →](https://help.figma.com/hc/en-us/articles/15253194385943)**

 Learn how to use expressions and variables in prototypes to generate dynamic string values, perform basic math operations with number values, or even evaluate boolean expressions.
- **Article: [Multiple actions and conditionals →](https://help.figma.com/hc/en-us/articles/15253220891799)**

 Learn how to use multiple actions to stack an unlimited number of actions on the same trigger, or use conditionals to check if a condition is met before performing an action by using if/else logic.
- **Article: [Variable modes in prototypes →](https://help.figma.com/hc/en-us/articles/15253268379799)**

 Learn how to use variable modes in your prototypes. You can set the values of specific modes based on context, or use specific mode values in your expressions.
- **Community file: [Advanced prototyping playground →](https://www.figma.com/community/file/1234939241273272375)**

 Make a copy of our advanced prototyping playground file to get some more hands-on practice with variables in prototyping.

## Variables using APIs

Variables are now supported in Figma’s Plugin API—for building plugins and widgets—and in the REST API.

- **Developer docs: [For the REST API →](https://www.figma.com/developers/api#variables)**

 Support for variables in the REST API includes endpoints for querying, creating, updating, and deleting variables.
- **Developer docs: [For the plugin API →](https://www.figma.com/plugin-docs/working-with-variables)**

 Support for variables in the plugin API includes creating and reading variables, and binding variables to components. For example, a plugin can be built to [import or export variables](https://github.com/figma/plugin-samples/tree/master/variables-import-export) or to [convert styles to variables](https://github.com/figma/plugin-samples/tree/master/styles-to-variables).
- **Developer docs: [For the widget API →](https://www.figma.com/widget-docs/working-with-variables)**

 Widgets can access variables using the Plugin API. Widgets can create and read variables, but widget properties cannot be bound to variables.
- **Figma tutorial: Sync variable to GitHub**

 In this video tutorial, learn how to sync your variables with your codebase. We'll cover how to use our Variables GitHub Action example repo to sync your Figma variables and your codebase.
- **Community file: [Syncing design systems using Variables REST API →](https://www.figma.com/community/file/1270821372236564565)**

 Learn how you can use Figma's variables REST API to set up automated workflows to sync changes between design files and your codebase.
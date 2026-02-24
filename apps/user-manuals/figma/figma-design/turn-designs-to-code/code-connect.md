# Code Connect

Source: https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect

---

Who can use this feature

Available on the **[Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)**

Requires a [Full or Dev seat](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor)

Code Connect is a bridge between your codebase and Figma's Dev Mode, connecting components in your repositories directly to components in your design files. When implemented, these connections enhance the [Figma MCP server](https://developers.figma.com/docs/figma-mcp-server)'s ability to guide AI agents with more precise implementation details by giving them direct references to your actual code.

**Note:** This is a general overview for approaching Code Connect as an organization. For implementation details and code samples, see the [Code Connect developer documentation](https://developers.figma.com/docs/code-connect).

## Two ways to use Code Connect

There are two ways to connect your code repositories to Figma: **Code Connect UI** and **Code Connect CLI**. Both contribute to the same MCP infrastructure, but differ in how they integrate into your workflow.

- **Code Connect UI** runs entirely inside Figma. It’s quick to set up, language-agnostic, and ideal for teams who want a simple, visual way to link design components to code. You can connect directly to a GitHub repository, or manually provide component paths and names if you use another version control system.

 - Best for design and engineering teams who want an accessible, collaborative setup.
 - Connects to your repository through Figma or via manual links.
 - When connected, it provides component paths, component names, and enhanced AI-generated code examples for richer context.

 [See the Code Connect UI developer documentation →](https://developers.figma.com/docs/code-connect/code-connect-ui-setup/)
- **Code Connect CLI** runs locally in your repository and provides developers with more precision and flexibility. It supports property mappings and dynamic code examples, allowing for deeper integration and accuracy.

 - Best for developers who want precision and flexibility in how design and code are connected.
 - Runs from the terminal within your local codebase and publishes connections to Figma.
 - Provides property mappings and dynamic code examples that reflect your actual production components.

 [See the Code Connect CLI developer documentation →](https://developers.figma.com/docs/code-connect/quickstart-guide/)

**Note:** You can only use one connection type per component, but both the UI and CLI can coexist within the same design system. Many teams use a mix of both approaches depending on their workflow and technical setup.

### How Code Connect works with MCP

Both Code Connect UI and CLI feed into Figma’s MCP Server, which makes your connected components accessible to AI-enabled tools and code editors. This ensures your design system context is reflected accurately wherever it’s referenced, from Dev Mode to external AI integrations.

## Code Connect UI

The Code Connect UI helps you link design components in your Figma libraries to the corresponding code components in your codebase. It runs entirely inside Figma and connects directly to GitHub for repository access and mapping context. These connections enhance the MCP server’s ability to guide AI agents with more precise implementation details by giving them direct references to your actual code.

![Code Connect UI displaying options for mapping design components to code repositories, including a connect button.](https://help.figma.com/hc/article_attachments/35139962417047)

### Connection types

**Connect to a GitHub repository (optional)**

Authorize Figma to access your GitHub repository and select components directly. Connecting to GitHub is optional. You can map your design system components to code paths manually without a GitHub connection.

**Note:** You must be the owner of the file you want to connect to GitHub or an organization admin.

**Manual mapping**

Link components manually by pasting the relevant file path or URL and the component name.

Once mapped, this information is shared with the [Figma MCP server.](https://developers.figma.com/docs/figma-mcp-server) Anytime this design component is used, the linked code info is included in the design context sent to AI agents.

[See our developer documentation to learn more about getting started with Code Connect UI ->](https://developers.figma.com/docs/code-connect/code-connect-ui-setup)

### Enhanced MCP codegen with previews

Code Connect UI now includes enhanced MCP codegen, which surfaces example code previews based on your actual connected source files. In Dev Mode, you’ll see AI-generated snippets showing how the component might appear in your codebase, helping you understand implementation details before handing off.

![code-connect-ui.png](https://help.figma.com/hc/article_attachments/36452798260759)

You can also:

- Add custom notes or usage instructions per mapping, which Figma includes in the MCP server output to guide AI-assisted tools.
- Use the built-in component playground to see how different configuration options affect your code connections in real time.

[Learn more about enhanced MCP codegen in Code Connect UI ->](https://developers.figma.com/docs/code-connect/code-connect-ui-setup/#add-custom-instructions-for-ai-code-generation)

## Code Connect CLI

When using Code Connect CLI, Dev Mode displays real world code snippets defined by your design system instead of the autogenerated code snippets that Dev Mode provides by default. In addition to connecting component definitions, Code Connect CLI can also map properties from code to Figma, enabling dynamic and correct snippets.

Code Connect CLI is especially useful when you have an existing design system and want to drive consistent and correct adoption of that design system across design and engineering.

### Overview

The exact steps you take to set up Code Connect CLI depend on the architecture of your design system and codebase. For example, if you use SwiftUI, you'll plan your approach to use the SwiftUI resources we provide.

Generally, your organization will follow these steps to get started:

1. **Plan the implementation.** Usually this includes:
   - Identifying the requirements of your front-end developers, such as whether you need support for React or SwiftUI.
   - Identifying the components in your codebase that you want to integrate with Dev Mode.
   - Planning the configuration of Code Connect CLI and the mappings of your components.
2. **Get the Code Connect repository.** Code Connect supports:
   - React (or React Native)
   - HTML (Web Components, Angular, Vue, etc.)
   - SwiftUI
   - Jetpack Compose
3. **Implement the component mappings.** The exact way you build the mappings will depend on your codebase and design system, but broadly the process involves mapping properties from your design system components to properties in Figma. This allows Code Connect CLI to generate snippets of code that map the values in Figma to the architecture of your components, and then surface those snippets inside Dev Mode.
4. **Review in Dev Mode.** In Dev Mode, review the Code Connect CLI output with your developers and designers to ensure the practical usability of the component examples and that the representations are accurate.

To take full advantage of Code Connect CLI, the developers responsible for your design system components should work with your designers to implement the mappings from your production codebase to Figma.

### What's available?

To get started with Code Connect CLI, check out the detailed steps we provide in the [Code Connect CLI developer documentation](https://www.figma.com/code-connect-docs/quickstart-guide/).

Code Connect CLI supports:

- [React (or React Native)](https://www.figma.com/code-connect-docs/react/)
- [HTML (Web Components, Angular, Vue, etc.)](https://www.figma.com/code-connect-docs/html/)
- [SwiftUI](https://www.figma.com/code-connect-docs/swiftui/)
- [Jetpack Compose](https://www.figma.com/code-connect-docs/compose/)

Additionally, Code Connect CLI provides some advanced features:

- [Integration with Storybook](https://www.figma.com/code-connect-docs/storybook/)
- [Custom parsers](https://www.figma.com/code-connect-docs/custom-parsers/)
- [Template API](https://www.figma.com/code-connect-docs/template-api/)

The [Code Connect CLI repository](https://github.com/figma/code-connect) is available on GitHub.

### Privacy and Code Connect CLI

Figma only collects the minimum data needed to enable Code Connect CLI in the interface. When you run `figma connect` using Code Connect CLI, Figma gets the following data:

- The paths for components that are added
- The repository URL where the Code Connect components are implemented
- The properties and code in the .figma files

Figma logs only basic events for understanding Code Connect CLI usage: when components are published or unpublished, and calls to get Figma data when using the command-line interface.

For more information about Figma's approach to privacy, see Figma's [Privacy Policy](https://www.figma.com/legal/privacy/).
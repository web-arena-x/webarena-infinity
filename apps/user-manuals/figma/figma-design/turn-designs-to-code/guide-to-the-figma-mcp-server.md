# Guide to the Figma MCP server

Source: https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server

---

Before you start

Who can use this feature

The remote server is available on [all seats and plans.](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

The desktop server is available on a [Dev or Full seat](https://help.figma.com/hc/en-us/articles/27468498501527-Updates-to-Figma-s-pricing-seats-and-billing-experience#h_01JCPBM8X2MBEXTABDM92HWZG4) for [all paid plans.](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

You must use a code editor or application that supports MCP servers (i.e. VS Code, Cursor, Windsurf, Claude Code, Codex). [See our MCP catalog for a full list of supported clients ->](https://figma.com/mcp-catalog)

---

For information about usage and rate limits, see [Plans, access, and permissions](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/) in the Figma developer documentation.

The Figma MCP server helps developers implement designs quickly and accurately by providing important context to AI agents that generate code from Figma design, FigJam and Make files. The tools within Figma’s MCP server bring additional context from Figma into your workflow, so your code doesn't just match your existing systems, but your design, too.

MCP servers are part of a standardized interface for AI agents to interact with data sources using the [Model Context Protocol](https://modelcontextprotocol.io/introduction).

[See our Figma MCP Collection to learn more about the MCP server and bringing Figma into your workflow →](https://help.figma.com/hc/en-us/sections/35280374295831-Figma-MCP-collection)

**Note:** This page is a general overview of the Figma MCP server. For detailed instructions and code samples, see the [Figma MCP server developer documentation](https://developers.figma.com/docs/figma-mcp-server).

With the server enabled, you can:

- **Send live UI to Figma Design files with Claude Code to Figma**

  Turn live UI from your browser (production, staging, or localhost) into editable Figma frames. Send screens or whole flows as design layers to Figma for exploration, alignment, and refinement.

  This feature is continuously being improved. If you encounter issues, you can report the issues using [Fig, our support chatbot](https://help.figma.com/hc/en-us/articles/360041057214-Explore-Figma-s-help-and-support-resources#h_01KBJZP4HEVHZSHXBV6PFQBPH0), or by [emailing support (paid plans)](https://help.figma.com/hc/en-us/articles/360041057214-Explore-Figma-s-help-and-support-resources#h_01KBJZP4JHXDEZM922NWPF3P9D).

  [Learn more about Claude Code to Figma](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/#generate_figma_design)
- **Generate code from selected frames**

  Select a Figma frame and turn it into code. Great for product teams building new flows or iterating on app features.
- **Extract design context**

  Pull in variables, components, and layout data directly into your IDE. This is especially useful for design systems and component-based workflows.
- **Retrieve FigJam resources**

  Access content from your FigJam diagrams and use it in your code generation workflow. Incorporate early-stage ideas, flows, or architecture maps directly into development.
- **Retrieve Make resources**

  [Gather code resources from Make files](https://developers.figma.com/docs/figma-mcp-server/bringing-make-context-to-your-agent/) and provide them to the LLM as context. This can help as you move from prototype to production application.
- **Keep your design system components consistent with Code Connect**

  Boost output quality by reusing your actual components. Code Connect keeps your generated code consistent with your codebase.

  [Learn more about Code Connect](code-connect.md)

## Set up the MCP server

You can connect the Figma MCP server in two ways:

- [**Desktop MCP server**](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/): Runs locally through the [Figma desktop app.](https://www.figma.com/downloads)
- [**Remote MCP server**](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Connects directly to Figma’s hosted endpoint at `https://mcp.figma.com/mcp`.

### Enable the desktop MCP server

1. Open the [Figma desktop app](https://www.figma.com/downloads/) and make sure you've [updated to the latest version](https://help.figma.com/hc/en-us/articles/5601429983767-Guide-to-the-Figma-desktop-app#h_01HE5QD60DG6FEEDTZVJYM82QW).
2. Create or open a Figma Design file.
3. In the toolbar at the bottom, toggle to [Dev Mode](../tour-the-interface/guide-to-dev-mode.md) or use the keyboard shortcut `Shift`⁠`D`.
4. In the **MCP server** section of the inspect panel, click **Enable desktop MCP server**.

A confirmation message appears at the bottom of the window once the server is running.

The server runs locally at `http://127.0.0.1:3845/mcp`. Keep this address handy for your configuration file in the next step.

### Connect the MCP server to your editor

Follow instructions for your specific editor to connect to the Figma MCP server, either locally or remotely. Some clients also support [Skills](#h_01KG5HNM2M3Y6RGBRK84FH1Z1E), which add agent-level instructions that help AI tools work more effectively with Figma designs:

|  |  |  |  |
| --- | --- | --- | --- |
| **Client** | **Desktop server support** | **Remote server support** | **Skills support** |
| [Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/qdev-mcp.html) | ✓ |  |  |
| [Android Studio](https://developer.android.com/studio/gemini/add-mcp-server) | ✓ | ✓ |  |
| [Claude Code](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/#claude-code) | ✓ | ✓ | [Claude Skills](https://claude.com/connectors/figma) |
| [Codex by OpenAI](https://developers.openai.com/codex/mcp#connect-codex-to-a-mcp-server) | ✓ | ✓ | [Codex Skills](https://github.com/openai/skills/blob/main/skills/.curated/figma-implement-design/SKILL.md) |
| [Cursor](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/#cursor) | ✓ | ✓ |  |
| [Gemini CLI](https://github.com/figma/figma-gemini-cli-extension) | ✓ | ✓ |  |
| [Kiro](https://kiro.dev/docs/mcp/servers/#remote-mcp-servers) | ✓ | ✓ | [Kiro Powers](https://kiro.dev/powers/) |
| [Openhands](https://docs.all-hands.dev/usage/mcp) | ✓ |  |  |
| [Replit](https://blog.replit.com/everything-you-need-to-know-about-mcp) |  | ✓ |  |
| [VS Code](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/#vs-code) | ✓ | ✓ |  |
| [Warp](https://docs.warp.dev/knowledge-and-collaboration/mcp#adding-an-mcp-server) | ✓ | ✓ |  |

### About Skills

Skills provide guidance for how an agent should complete specific tasks, using a combination of MCP tool calls and detailed instructions.

While the Figma MCP server exposes individual tools, Skills help agents understand which tools to use, how to sequence them, and how to apply the results when working with Figma designs.

Skills can guide agents through workflows like:

- Connect Figma design components to code components using Code Connect
- Generate design system rules aligned to your codebase
- Translate designs into production-ready code

Skills don’t replace MCP connections or add new MCP capabilities. They reduce setup and guesswork by packaging recommended workflows into reusable instructions.

**Tip:** For the latest list of supported editors and clients, check out our [MCP Catalog](https://www.figma.com/mcp-catalog).

## Prompt your MCP client

The Figma MCP server introduces a set of tools that help LLMs translate designs in Figma. Once connected, you can prompt your MCP client to access a specific design node.

There are two ways to provide Figma design context to your AI client:

### Selection-based (desktop server only)

1. Select a frame or layer inside Figma using the desktop app.
2. Prompt your client to help you implement your current selection.

### Link-based

1. Copy the link to a frame or layer in Figma.
2. Prompt your client to help you implement the design at the selected URL.

**Note:** Your client won’t be able to navigate to the selected URL, but it will extract the node-id that is required for the MCP server to identify which object to return information about.

### Tools and usage suggestions

The Figma MCP server includes several tools that help your AI assistant generate, adapt, and align code with your designs. Each tool supports different workflows, from producing code to mapping components or retrieving design tokens. To learn more about available tools and usage suggestions, see the [Figma MCP server developer documentation.](https://developers.figma.com/docs/figma-mcp-server)
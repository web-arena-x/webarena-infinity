# AI at Linear

AI has made engineers faster at writing code and given product teams better access to insights. But this progress has been scattered across different tools and chat interfaces.

At Linear, we’re bringing it all together. We see potential to use AI to improve the entire software development lifecycle. From planning and code generation, to QA and incident response.

In this guide, we'll touch on the ways we're doing it.

---

At a conceptual level, there’s three core areas where AI can improve how teams build products:

1. Making sense of all your information and surfacing what matters
2. Taking action on those insights systematically
3. Connecting your existing tools so data flows seamlessly

Linear addresses each of these through our embedded AI workflows, agent platform, and our MCP server,

---

## Product Intelligence: Managing information

Teams accumulate huge backlogs of ideas, issues, and requests that become hard to navigate. While figuring out which team a bug or piece of customer feedback should go to becomes increasingly difficult as you scale.

Linear's **Product Intelligence** tackles both problems. When new work comes in, Product Intelligence automatically suggests the right team, finds related issues, and flags potential duplicates.

This turns your backlog from noise into actionable context, and eliminates the manual work of routing and organizing information.

 
_[space for product intelligence demo - tbd]_

### FAQs

<details>
<summary>What happens to existing backlogs when we turn this on?</summary>
All of those issues you’ve accumulated become useful. Linear will now automatically reach into the backlog, find related work, surface duplicates, and highlight anything that’s conceptually connected. Which makes the question of whether you should import a backlog into Linear a definite “yes”.
</details>

<details>
<summary>Does Product Intelligence act autonomously?</summary>
Right now, no. We want to maintain a human in the loop while we train the model. In time, as confidence grows, our intention is to enable teams to decide for themselves whether they want Product Intelligence to make decisions autonomously.
</details>

<details>
<summary>How accurate are the suggestions?</summary>
Quite accurate. Each suggestion you approve or disapprove will refine the overall quality of the suggestions. We expect these suggestions to continuously improve with usage.
</details>

<details>
<summary>What plans is Product Intelligence available on?</summary>
Product Intelligence is live on all Linear Plans as a technology preview.
</details>

---

## Pulse: Managing information

As companies grow, answering the simple question “What’s happening right now?” becomes increasingly hard. Information is spread across tools, projects, and teams, making it difficult to get a clear, high-level view.

**Pulse** is a new way to stay in sync with your product organization through a personalized AI-generated real-time feed of updates and discussions. Delivered as a daily or weekly update you can read or listen to.



![Watch on YouTube](https://www.youtube.com/watch?v=mcWS9yiGzog)

### FAQs

<details>
<summary>What plans is Pulse available on?</summary>
All Linear plans.
</details>

<details>
<summary>Can we control what goes into the feed?</summary>
Not directly. You control the feed indirectly through the activity that happens within Linear.
</details>

---

## Agents: Taking action on information

Agents are here, and Linear is where you orchestrate both human teams and AI agents around product development.

You can build your own, or choose from a variety of agents crafted specifically for Linear workflows by Cursor, Codegen, Sentry, and others.

Agents operate within Linear just like human teammates. Start delegating work, from code generation to other technical tasks. This turns every team member into a manager with their own AI workforce, giving you the leverage to scale output without scaling headcount.



> [!NOTE]
> Here’s our Head of Product, Nan, giving a demo of the Codegen agent in Linear:

![Watch on YouTube](https://www.youtube.com/watch?v=e_T8Sn8s46M)

### FAQs

<details>
<summary>What specific tasks can agents actually do?</summary>
tbd
</details>

<details>
<summary>How do I add agents to my Linear workspace?</summary>
tbd
</details>

<details>
<summary>How do I control what agents can and can't access?</summary>
tbd
</details>

<details>
<summary>Can I build my own agent?</summary>
tbd
</details>

<details>
<summary>How much do agents cost?</summary>
Adding an agent to your org will not require paying for an additional seat.

While there will be no charges on our side, developers would have to pay for LLM usage to the provider they choose to build their agent with. And it's also likely that, for any third-party agents used, the company building that agent will charge something for its use.
</details>

---

## Linear MCP: Connecting information

Through our official **MCP**, you can connect Linear directly to the AI tools you already use - Cursor, Claude Code, ChatGPT, and more. 

Pull Linear context into your AI tools or push information back to Linear, without switching apps.



> [!NOTE]
> Here’s a demo from Tom, our Head of Engineering, showing how our MCP server works with Claude:

![Video](https://webassets.linear.app/files/ornj730p/production/45f706efb0229daf6e43db7ff203ded1d7496ac5.mp4)

### FAQs

<details>
<summary>Which AI tools does Linear's MCP support?</summary>
Claude, ChatGPT, Cursor, Windsurf, and any tool that supports the MCP standard. Further details on setting up these connections can be found [here](https://linear.app/docs/mcp).
</details>

<details>
<summary>Is this secure? What data gets shared between tools?</summary>
We're following the authenticated remote [MCP spec](https://modelcontextprotocol.io/specification/2025-03-26). Security and safety guidelines outlined [here](https://modelcontextprotocol.io/specification/2025-03-26#security-and-trust-%26-safety). Further details about our Linear MCP configuration can be found here.
</details>

<details>
<summary>Is MCP only available on certain Linear plans?</summary>
MCP is available on all Linear plans. However, be mindful that if you’re connecting Linear with tools like Claude and ChatGPT, there are restrictions on their side based on plan type.
</details>

<details>
<summary>What are the use-cases?</summary>
MCP is a relatively new concept, and so, we’re still figuring out the breadth of possibilities. Today, you could:

* Ask Claude "what's on my plate today" and get your Linear assignments with full context.
* Research complex bugs in ChatGPT, then automatically create detailed Linear issues with your findings.
* Pull project context from Linear directly into Cursor while coding. Push code decisions and technical notes back to Linear without leaving your development environment.
* And many others.
</details>

---

## Roadmap

We're building Linear into the command center for AI-assisted product development. This means creating a unified environment where AI and agents work alongside human teams across your entire product organization.



_[Add chart/table/timeline of roadmap?]_

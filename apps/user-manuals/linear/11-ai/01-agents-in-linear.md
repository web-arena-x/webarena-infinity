# AI Agents

Build and deploy AI agents that work alongside your team

![list of agents in assignee menu, Charlie and ChatPRD are visible](https://webassets.linear.app/images/ornj730p/production/68c955d01e0e45b23747e8cd7362b018b06a6655-2880x1768.png?q=95&auto=format&dpr=2)

## Overview

Agents, also known as "app users", behave similar to other users in a workspace. They can be @-mentioned, delegated issues through assignment, create and reply to comments, collaborate on projects and documents, etc. App users are installed and managed by workspace admins.

Agents are not traditional assignees. Assigning an issue to an agent triggers delegation—the agent acts on the issue, but the human teammate remains responsible for its completion.

## Adding Agents

> [!NOTE]
> Workspace admins can install agents by following the setup instructions provided by the agent developer. Find available agents in the [Integrations Directory](https://linear.app/integrations/agents).

During installation, you’ll be prompted to choose which teams the agent has access to.

<details>
<summary>Example</summary>
![Installing the codegen agent into Linear permissions modal](https://webassets.linear.app/images/ornj730p/production/9a11b2deb2fd1f6b5649f00ebaa928124f061099-1292x1019.png?q=95&auto=format&dpr=2)
*Example of installing an agent into Linear*
</details>

Once installed, any user with access to the selected teams can interact with the agent.

Agents can be uninstalled or managed by admins from **Settings > Applications** or suspended from **Settings > Administration > Members**.

## Using Agents in Linear

Agents are designed to work seamlessly alongside human teammates:

* **Delegate issues to them** by assigning the issue to the agent. This triggers the agent to take action based on its programmed behavior.
 * The human assignee remains responsible for the issue, even after delegation to an agent.
* **@mention them** in comments or descriptions to trigger their functions.

If you're not sure how to interact or what they're able to help with, you can try @mentioning the agent to ask for help.

## Guiding Agents

Agent guidance lets you provide instructions that agents will automatically receive when they work on issues in your workspace. 

![Screenshot of the Additional guidance panel showing repository instructions for agents](https://webassets.linear.app/images/ornj730p/production/d9cb1836286c78822dddee0e6e9ec3c67a1c10a9-1570x788.png?q=95&auto=format&dpr=2)

Agent guidance provides instructions that help agents work within your team’s conventions. Guidance can specify which repository to use for certain code changes, how to reference issues in commits or pull requests, and what review process to follow, so agents align with your existing workflows.

> [!NOTE]
> **Note:** All guidance is passed to the agent, but how it is interpreted or applied depends on the specific agent integration. If an agent doesn’t appear to follow the guidance, please share feedback with the team responsible for that agent directly.

Workspace guidance applies across the entire organization, while team-specific guidance can be used to include additional instructions unique to that team. When both exist, team guidance takes priority. 

Guidance is authored in a markdown editor with full history, so instructions can be formatted clearly and reviewed or updated over time.

To edit your workspace-level agent guidance, navigate to [_Settings_ > _Agents_ > _Additional guidance_](https://linear.app/settings/agents). For team-level guidance, navigate into your parent or sub-team's settings > _Agents_ > _Additional guidance_. Both workspace and team level guidance may not exist in all agent contexts.

## Viewing Agent Activity

You can track what an agent has done in the same ways you track other teammates:

* **Agent** [**user pages**](https://linear.app/docs/user-views) show issue activity and contributions.
* In the **My issues** view, issues that you’ve delegated to agents will still appear—so you maintain visibility and control over the work in progress.
* **Custom views** filtered by **Delegate** to monitor agent involvement on specific types of issues or workflows.
* Use **Insights** sliced or segmented by **Delegate** to measure how much work is being directed to and handled by agents.

## Building Your Own Agent

Developers can build custom agents using Linear’s developer platform. Documentation on agent APIs, authentication, and behavior can be found in our [Developer Docs](https://linear.app/developers/agents).

## FAQs

<details>
<summary>Are agents billable seats? </summary>
Agents are not counted as billable seats in Linear. The services that provide the agent may have their own pricing structure, and you should refer to their documentation before installing.
</details>

<details>
<summary>How does Linear use data from agents?</summary>
Linear does not train on customer's data. We use models from common model providers, a complete list is available in our [DPA](https://linear.app/dpa).

Agents themselves would be 3rd party integrations approved by your workspace, in which case we can't speak to how the agent provider operates and you'd have to refer to the agent service provider.
</details>

<details>
<summary>What are the limitations in agents interacting with Linear?</summary>
Agents cannot sign in to the app, access admin functionality or manage users.
</details>

<details>
<summary>What happens if I install an agent but the name is already taken?</summary>
In the event that you have a member on your workspace with the same name as an Agent, the Agent's username will simply append a number at the end to keep it unique.

For example, Charlie would become Charlie1.
</details>

##

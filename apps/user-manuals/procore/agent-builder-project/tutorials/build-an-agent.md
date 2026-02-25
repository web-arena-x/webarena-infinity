# Build an Agent

Source: https://v2.support.procore.com/product-manuals/agent-builder-project/tutorials/build-an-agent

---

## Background

Procore's Agent Builder helps users create AI Agents to automate routine tasks and gain predictive insights from project data. You can easily tailor the Agent to meet your specific project requirements and business needs by selecting the actions it should take and the data it should access. After creating the Agent, you can run it directly from [Assist](/product-manuals/assist-project/), Procore's in-app AI service.

## Things to Consider

- Agent Builder is currently in Open Beta. See [About Agent Builder](/product-manuals/agent-builder-project/tutorials/about-agent-builder) for more information.
- **Required User Permissions:** Any user can create an Agent, but the user who runs the Agent (via Assist), needs appropriate permissions in all the tools involved in executing the tasks. See [About Agent Builder](/product-manuals/agent-builder-project/tutorials/about-agent-builder) for more information.

## Steps

1. Navigate to your project in Procore.
2. Open the Agent Builder tool.
3. Choose if you want to create a new Agent, copy an existing Agent, or import an Agent.

   - **Create a new Agent:** Click the **+Create Agent** button.
   - **Copy an existing Agent:** Click on the existing Agent's

     **more** menu and select **Make a Copy.**

     The copied Agent opens so you can edit it, and it's automatically added to your project's list of Agents, with the name, "Copy of [copied Agent name]" until you edit that.
   - **Import an Agent:** Click the **arrow** on the **Create Agent** button and then choose **Import Procore Agent**. Select an .md file from your device. This is a Markdown text file with a short block of setup information at the top, called âfront matterâ.
4. Customize your Agent by selecting and writing the desired inputs in each of the areas below.

   - Agent Basics
   - Agent Building Blocks
   - Agent Instructions
5. When finished, click the **Save & Close** button, or the **Save & Test** button if you'd like to [use your Agent](/product-manuals/assist-project/tutorials/run-an-agent-in-assist) in Procore Assist. Your Agent is now live in Assist but only for you.
6. Publish your Agent if you want other project users to have access to it: From **Agent Home**, click your Agent's **more** menu and select **Publish.**

#### Agent Basics

When members of your project view the available Agents in Procore Assist, they can see each Agent's title, description, and author.

1. Type a name for your Agent.
2. Type a brief description for your Agent. 
   The description lets other users know what the Agent can do without having to read the Agent's instructions.

#### Agent Building Blocks

Choose what documents and actions power this Agent.

##### Procore Documents

Attach documents from the Procore Documents tool that you want the Agent to reference when executing its tasks.   
*Note:* Documents must be .pdf and 50 pages or less.

1. Click the **Add** button.
2. Find and click the document you'd like to attach to the Agent.
3. Click the **Attach** button.

##### Actions

The Agent can perform certain actions for you within Procore like creating an observation, sending a task to someone, or accessing data.

1. Click on the category you're interested in adding an action for. 
   *Note:* This brings up a list of all available actions for that tool or category. Or, you can reference a [complete list of all the available actions](/faq-what-actions-are-available-in-agent-builder) Procore Agents can take.
2. Click an action to add it to the list of "Selected Actions" for your Agent. You can select multiple actions across multiple categories.

#### Agent Instructions

Write the instructions the same way you would when requesting something from a coworker. Tell the Agent what information or task you'd like to achieve and how to use any attached documents. Include as much information and detail as you can and use complete sentences. When someone runs your Agent, these are the instructions the Agent will follow.

Review the following best practices for writing Agent instructions:

1. **Start with the most important points.** Begin by stating your main goal or question, and then give any critical constraints (example 1, example 2, etc.).

2. **Keep it simple**

- Short sentences or bullet points work well.
- Avoid filler words or vague language if you can.
- The clearer your wording, the easier it is for the AI to follow.

3. **List out specific steps or details**. If the task requires multiple steps or details, grouping them in a short list can help.

For example:

`Step 1   
 - Detail 1   
 - Detail 2   
 - Detail 3 
   
Step 2 
- Detail 1 
- Detail 2 
- Detail 3`

4. **Use examples** ***(if helpful)****.* Quick examples act like mini templates for your instructions (e.g., "Here's a sample answer style that I like...").

5. **Mention format requirements**. If you need the output in a specific format, mention that explicitly. For example, say "Provide your answer as bullet points."

6. **Be brief, but complete**. Too much text can be confusing. But if it's too short, the AI may not know exactly what you mean. Aim for a sweet spot--just enough detail to cover your request without burying it in extra text.

7. **Add notes for other users.** To include comments (information for yourself or teammates, not for the Agent to read or execute), begin the line or paragraph with two forward slashes. Example: // This Agent consolidates morning activities into one efficient interactive briefing for daily field operations.
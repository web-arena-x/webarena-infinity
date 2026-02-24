# View Agent Activity

Source: https://v2.support.procore.com/product-manuals/agent-builder-project/tutorials/view-agent-activity

---

## Background

After creating an Agent in Procore's [Agent Builder](/product-manuals/agent-builder-project/) and running it in [Assist](/product-manuals/assist-project/), you can view that Agent's metrics and analytics on its 'Agent Activity' page.

This tutorial helps you discover usage data for *one* agent at a time. If you have access to Procore's Company 360 Reporting tool, you can also view usage and performance data across all agents if Agent Builder is enabled at the *company* level. See [Create a Company 360 Report](/product-manuals/reports-company/tutorials/create-a-company-360-report) to help you make use of the [Agent Adoption dataset](/process-guides/enhanced-reporting-data-guide/agent-adoption).

## Things to Consider

- To access Agent information, you need the Procore Agent Builder tool. See [About Agent Builder](/product-manuals/agent-builder-project/tutorials/about-agent-builder) for more information.
- **Required User Permissions:**

 - Unpublished Agents: Only the Agent's author can view the activity of unpublished Agents.
 - Published Agents: Anyone can view the activity of a published Agent.

## Steps

1. Navigate to your project in Procore.
2. Open the **Agent Builder** tool.
3. Click on the Agent you want to view analytics for.
4. Click the **Agent Activity** tab under the Agent's name.
5. Select the time period from the drop-down menu. The default is the last 7 days, but you can select another increment such as 'Today', 'Last 90 days', or 'All Time'.
6. View the following metrics and analytics about that Agent:

   - **Total Invocations** - Total inputs sent by users to this agent
   - **Invocations over time** - Number of inputs sent by users to this agent during the selected time period.
   - **Unique Users** - Unique users who chatted with this agent.
   - **Unique Users over time** - Number of unique users who chatted with this agent during the selected time period.
   - **Credits** - Credits consumed to process conversations.
   - **Credit Consumption** - Number of credits consumed by this agent to process conversations during the selected time period.

##### What are credits?

Credits are a unit for measuring the computational resources an AI interaction consumes. While there are no predefined usage limits during Agent Builder's beta program, Procore may notify users or Admins if usage becomes exceptionally high. We plan to introduce automatic usage limits once the product is generally available.
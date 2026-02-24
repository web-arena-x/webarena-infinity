# Determining agent availability when escalating from advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8920466700698-Determining-agent-availability-when-escalating-from-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The availability check described in this article should be used only with CRM integrations other than Zendesk. To check Zendesk agent availability, see [Checking operating hours and agent availability during conversations with advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749686554) instead.

When using an advanced AI agent for customer support, it’s helpful to know when a human agent is available to step in. The Agent Availability API helps with this by allowing your AI agent to check the availability of specific agents or groups of agents based on certain criteria.

The API provides detailed information about each agent’s status, including whether they’re online, away, or offline for different channels like messaging. It also shows their overall availability across all channels, the tasks they’re currently handling, and their workload limits for specific channels.

By using the Agent Availability API, you can make your AI agent smarter when it comes to handing off conversations, routing customer queries to the right agent, or tracking agent availability or estimated wait times.

In this article, we’ll show you how to set it up so your AI agent and support team can work together more efficiently, giving customers faster and more precise help.

This article contains the following topics:

- [Prerequisites for setting up the Agent Availability API in the integration builder](#h_01JMFX76J31ANNM16JVPP7MJ84)
- [Creating a token to access the API](#h_01JMFX7FHJVSD81JJFWDP3AT12)
- [Creating the integration in the integration builder](#h_01JMFX8KN5FJX16RDYDT6CW8V0)

## Prerequisites for setting up the Agent Availability API in the integration builder

To set up the Agent Availability API in the integration builder, you'll need to gather the following key information:

- **The Zendesk subdomain.** This is the name of your company within your Zendesk instance. This is needed for the URL to make the call to the API using the integration builder.
- **Auth token and an admin email.** Created in Admin Center, this token will authorize your AI agent to make the request for the Agent Availability data.
- **Any group ID (if applicable).** If you want to filter for online agents belonging to a specific group, you can do so with a URL query.

## Creating a token to access the API

To access the Zendesk API, you'll need to create a token in Admin Center.

**To create an API token**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click **Apps and integrations** in the sidebar, then select **APIs** > **Zendesk API**.
2. Click **Add API token**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_agent_avail_1.png)
3. Give the token a descriptive name, such as **Agent Availability**.
4. Copy the token somewhere safe, as you'll need this for setting up the integration in the integration builder.

## Creating the integration in the integration builder

1. Create an integration in the integration builder.
2. Go to the **Environment** tab and select your chosen environment (for example, Production, or you could change this to something more descriptive such as getAgents).
3. Set up the endpoint using the following format, replacing *[your-subdomain]* with your subdomain: 
   *https://[your-subdomain].zendesk.com/api/v2/agent\_availabilities*
4. (Optional) Further customize the query URL by filtering. 
   - Example 1: If you want to check how many agents are online now in the messaging channel: 
     *https://[your-subdomain].zendesk.com/api/v2/agent\_availabilities?filter[channel\_status]=messaging:online*
   - If you want to check for agents available online and in a specific service group: 
     *https://[your-subdomain].zendesk.com/api/v2/agent\_availabilities?filter[channel\_status]=messaging:online&filter[group\_id]={{groupId}}* For more information, see [Agent Availability API](https://developer.zendesk.com/api-reference/agent-availability/agent-availability-api/introduction/).
5. On the **Authorization** tab, set the **Authorization type** to **Basic Auth**. 
   - **Username**: Your admin email address with ‘/token’ appended (for example, admin@yourcompany.com/token).
   - **Password**: Paste the API key you generated earlier in Admin Center.
6. On the **Headers** tab, click **Add Header.**
7. In the **Key** field, enter **Authorization**.
8. In the **Value** field, enter **Basic {{apiToken}}**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_agent_avail_2.png)
9. (Optional) If you're checking for a particular groupId, then you can either add it statically to the URL query or you can create a dynamic link by creating a parameter in **Request parameters** with a key such as **groupId** and adding **&filter[group\_id]={{groupId}}** to the URL (as demonstrated in step 4). 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_agent_avail_3.png)

With that all set up, you should be able to successfully test your integration to view the response.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_agent_avail_4.png)

For the success scenario, you can now add your session parameters. Here are three commonly useful example parameters:

- **agentCheck**: Provides an array of relevant available agents. 
 - In the dialogue builder, use a conditional block with Includes.
- **availableAgent**: Provides number of relevant available agents. 
 - In the dialogue builder, use a conditional block with Greater/Less Than.
- **estimatedWait**: Divides number of open work items by active agents, multiplied by average handling time. This value is in minutes. 
 - In the dialogue builder, use a conditional block with Greater/Less Than. 
    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_agent_avail_5.png)

These parameters are now available for use in the dialogue builder with an API node that calls the Agent Availability integration you built in the integration builder.
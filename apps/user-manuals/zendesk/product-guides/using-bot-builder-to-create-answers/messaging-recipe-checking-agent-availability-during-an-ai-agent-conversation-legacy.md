# Messaging recipe: Checking agent availability during an AI agent conversation (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5706660392602-Messaging-recipe-Checking-agent-availability-during-an-AI-agent-conversation-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

This article describes
functionality available only to customers who had a drafted or published AI agent as
of February 2, 2025. For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Building dialogues for AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

The
bot builder's **Add business hours condition** step lets you branch an AI agent's
answers based on your business hours. However, it can't branch a conversation based on
agent availability.

In this recipe, you’ll use the bot builder's [Make API call](https://support.zendesk.com/hc/en-us/articles/4572971586586) and [Branch by condition](https://support.zendesk.com/hc/en-us/articles/5280598023450) steps to branch an existing AI agent answer based on the
number of online agents at the time of the conversation. The **Make API call** step
gets a count of the current online agents by calling the Zendesk Real Time Chat REST
API's [Get Agent Status Count](https://developer.zendesk.com/api-reference/live-chat/real-time-chat-api/rest/#get-agent-status-count) endpoint. The **Branch by
condition** step then uses the count to branch the answer's flow.

Note: If your account was created after November 11, 2021, you
can't use the use the [Get Agent Status Count](https://developer.zendesk.com/api-reference/live-chat/real-time-chat-api/rest/#get-agent-status-count) endpoint. Instead, use the Agent
Availability API's [Get agent availabilities](https://developer.zendesk.com/api-reference/agent-availability/agent-availability-api/agent_availabilities/#get-agent-availabilities) endpoint.

You can use this setup to send customized AI agent messages before creating a ticket using the
**Transfer to agent** step. These messages can help set better customer
expectations around wait or response times.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/no-agent-recipe-example.gif)

The recipe involves the following tasks:

- [Task 1: Checking your setup](#topic_en5_x3r_kxb)
- [Task 2: Creating an API connection](#topic_s1l_pkr_kxb)
- [Task 3: Retrieving agent availability](#topic_r1r_zlr_kxb)
- [Task 4: Branching based on agent availability](#topic_gm3_14r_kxb)
- [Task 5: Publishing your updated AI agent](#id_elm_lqr_kxb)
- [Task 6: Testing your changes](#id_ad5_nqr_kxb)

## Task 1: Checking your setup

To complete this recipe, you'll need the following:

- A Zendesk account with a published AI agent. If you are on a Suite Enterprise or Enterprise Plus
  plan, you can use a [sandbox testing environment](https://support.zendesk.com/hc/en-us/articles/4408844075930) to
  test the AI agent before using it in production.

  To set up an AI agent on
  a web and mobile messaging channel, see [Creating an AI agent for your web and mobile
  channels](https://support.zendesk.com/hc/en-us/articles/4408824263578).
- An OAuth access token for the Zendesk Chat API. To create this token, see
  [Chat API tutorial: Generating an OAuth
  token](https://support.zendesk.com/hc/en-us/articles/4408828740762).

## Task 2: Creating an API connection

To start, create an API connection to store your OAuth access token for the Chat API. Your AI
agent can use this connection to authenticate calls to the API.

**To create the connection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Connections >
   Connections**.
2. Click
   **Create connection**.
3. Select the
   **Bearer token**
   authentication type.
4. For
   **Connection name**, enter "zendesk\_chat\_api\_oauth\_token".
5. For **Token**, enter your OAuth access token (see [Task 1: Checking your setup](#topic_en5_x3r_kxb)).
6. For
   **Allowed domain**, enter "rtm.zopim.com".
7. Click
   **Save**
   to create the connection.

## Task 3: Retrieving agent availability

Next, add a **Make API call** step to an existing answer in your AI agent. This step gets a
current count of online agents from the Real Time Chat API's [Get Agent Status Count](https://developer.zendesk.com/api-reference/live-chat/real-time-chat-api/rest/#get-agent-status-count) endpoint.

**To add the Make API call step**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to update, then click the answer you want to
   update.
3. In bot builder, add a step to the desired location in the answer's
   flow.
4. Under **Choose step**, select **Make API Call**.
5. Enter **Get agent availability** as the **Name**.
6. Under **API details,** enter
   `https://rtm.zopim.com/stream/agents/agents_online` as the
   **Endpoint URL.**
7. In **Authentication**, select the **zendesk\_chat\_api\_oauth\_token**
   connection.
8. To test the API request, click **Make API call**.
9. Under **Test Data**, enter **Melbourne, AU** as the **Location**.
10. Click **Make API call**.
11. Save the following variable using its default name:
    - **content** > **data** > **agents\_online**
12. (Optional) Add a step under the **Get agent availability** step’s **API call
    failed** branch. This step runs if the Get Agent Status Count request
    fails.

## Task 4: Branching based on agent availability

Next, add a
**Branch by condition**
step to branch the answer's flow based on the
value of the
**agents\_online**
variable.

**To add the Branch by condition step**

1. In the bot builder, add a step in the
   **Get agent availability**
   step's
   **API call successful**
   branch.
2. Under
   **Choose step**, select
   **Branch by condition**.
3. Enter
   **Check agent availability**
   as the
   **Name**.
4. In the
   **If this**
   branch, enter
   **Agents are online**
   as the
   **Name**.
5. In the
   **If this**
   branch, click
   **Add condition**. Configure the
   condition as follows:
   - **Variable**: agents\_online
   - **Operator**: Is not
   - **Value**: 0
6. Click
   **Add**.
7. Add any desired steps under the
   **Agents are online**
   and
   **Else**
   branches. Steps under the
   **Agents are online**
   branch run when the
   [Get Agent Status Count](https://developer.zendesk.com/api-reference/live-chat/real-time-chat-api/rest/#get-agent-status-count)
   request
   indicates one or more agents are online. Steps under the
   **Else**
   branch run
   when the request indicates no agents are online.

## Task 5: Publishing your updated AI agent

When you're done editing the answer, you can publish the updated AI agent.

**To publish the AI agent**

1. Click **Done** in the upper right corner of the bot builder.
2. On the AI agent page, click **Publish AI agent**.
3. Click **Publish**.

## Task 6: Testing your changes

After you publish your changes, you can test the updated answer by using one of its training
phrases in a conversation with the updated AI agent. For more information about
testing AI agents, see [Testing the end user's messaging experience](https://support.zendesk.com/hc/en-us/articles/4408835784602).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/no-agent-recipe-example.gif)
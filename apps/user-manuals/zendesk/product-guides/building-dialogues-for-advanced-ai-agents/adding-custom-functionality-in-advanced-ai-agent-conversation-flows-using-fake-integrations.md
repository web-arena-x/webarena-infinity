# Adding custom functionality in advanced AI agent conversation flows using fake integrations

Source: https://support.zendesk.com/hc/en-us/articles/8357749820570-Adding-custom-functionality-in-advanced-AI-agent-conversation-flows-using-fake-integrations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

A fake integration allows for custom functionality to be added to dialogues using data already present in the conversation, without making actual API calls or retrieving external data. This allows you to implement logic using JSONata for data manipulation, comparisons, or other tasks within the dialogue flow.

This type of integration is useful for handling tasks that don’t require real-time external data, acting as a “helper” integration to extend an AI agent’s capabilities beyond standard features.

This article contains the following topics:

- [About fake integrations](#1-about-fake-integrations)
- [Building a fake integration](#2-building-a-fake-integration)
- [Adding a fake integration within a dialogue](#3-adding-a-fake-integration-within-a-dialogue)

## About fake integrations

A fake integration is useful when you want to process or manipulate data already available within the conversation. For example, you can accomplish the following tasks using a fake integration:

- Transform your data to a more appropriate format.
- Format and filter complex CRM or API data.
- Compare dates to find the most recent one.
- Retrieve the current day and time.
- Check whether a date is within a certain time frame.
- Check whether a URL contains specific words.
- Check for and replace any null values.
- Replace letters or symbols in your data.
- Use a case-insensitive filter to go through data and return the first matching value or provide a fallback response if there are no matches

If you can define logic using [JSONata](https://jsonata.org), then you can enhance your conversations with these helpful integrations.

## Building a fake integration

Tip: Before building a fake integration, we suggest that you familiarize yourself with using JSONata with the integration builder. See [Using JSONata with advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756877466).

To build a fake integration, you create an API Integration as usual. However, no request for data is ever made.

**To build a fake integration**

1. In the main menu, click **API Integrations**.
2. In the top right, click **Add Integration**.
3. In the **Add Integration** window:
   1. In the **Integration name** field, give your integration a descriptive name.
   2. (Optional) In the **Description** field, enter a description of the integration that helps you remember what it’s for.
   3. Click **Save**.
4. In the left sidebar, under Environments, select an environment (such as Production).
5. Set **Method type** to **GET**.
6. In the **URL** field, enter a dummy URL (for example, <https://dummyjson.com/http/200)>. ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_fake_integrations_1.png)
   - #### **Note:** Because fake integrations are hosted within the integration framework, they must point to a valid URL. The example above uses https://dummyjson.com/http/200, but its availability can’t be guaranteed. You can use whatever dummy URL makes sense for you. While an API call will be made to the specified URL, no data from the response will be processed in the fake integration.
7. Make sure **Authorization type** is set to **No Authorization**.
8. (Optional) In the left sidebar, under **Scenarios**, hover over **Failure**, select the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)), and select **Delete**. You don’t need a failure scenario for a fake integration.
9. In the left sidebar, under **Scenarios**, select **Success**.
10. Depending on your scenario, do one of the following:
    - If you have a simple query, enter it in the **Scenario Query** field. For example, if you just need a boolean response, then having the query here is all you need.
    - If you need to define logic based on request parameters (coming from the conversation):
      1. Enter **requestParameters** in the **Scenario Query** field.
      2. Under **Session Parameters**, enter the parameters for your fake integration. The screenshot below includes example parameters and JSONata expressions for returning the day of the week and the current time. 
         ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_fake_integrations_2.png)
11. Click **Save**.

## Adding a fake integration within a dialogue

In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), you can add an API integration block and select your fake integration.

**To add a fake integration within a dialogue**

1. In the top-right corner, use the AI agent drop-down field to select the AI agent you want to update the dialogue for.
2. In the main menu on the left, select **Content** > **Intents**.
3. Select the intent you want to update the dialogue for.
4. Select the **Replies** tab.
5. Select the reply you want to update the dialogue for, and then click **Edit Dialogue**.
6. Click the plus icon (+) at the appropriate point in the dialogue and add an **API integration** block. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_fake_integrations_3.png)
7. Select the fake integration you created above. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_fake_integrations_4.png)

Now, when the fake integration branch is hit in the conversation, your fake API integration is called and the session parameters you defined in your success scenario will be available to the dialogue. The example below shows a fake integration feeding into a conditional block using day-of-week-based parameters returned by the fake integration. 
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_fake_integrations_5.png)
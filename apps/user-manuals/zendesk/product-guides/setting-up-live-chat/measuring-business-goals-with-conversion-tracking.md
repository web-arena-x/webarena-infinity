# Measuring business goals with conversion tracking

Source: https://support.zendesk.com/hc/en-us/articles/4408886086042-Measuring-business-goals-with-conversion-tracking

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

Note: The information in this article applies to accounts using Zendesk Chat. If you are using
messaging, see [Tracking customer actions with messaging
goals](https://support.zendesk.com/hc/en-us/articles/9435878261402).

Use conversion tracking to set a business goal that tracks which chats influenced the
customer to make a purchase. This article will instruct you on how to set up conversion
tracking.

This article contains the following sections:

- [Creating a URL goal](#topic_swp_fwn_xz)
- [Viewing conversions in chats](#topic_jff_nyn_xz)
- [Measuring conversions in Analytics](#topic_ngp_wyn_xz)

## Creating a URL goal

To start tracking conversions on your website, you'll need to first set up a URL goal. You
can create up to 5 URL goals.

**To create a URL goal**

1. On the dashboard, select **Settings** > **Goals** and select **Add Goal**.
2. Enter a name and description for your goal.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/url_goals.png)
3. Select an attribution method. The attribution method determines which chat and agent
   gets credit for the conversion. For example, the **Last Touch** option assigns 100% of
   the credit to the last chat and agent the customer speaks to that immediately precede
   sales or conversions. In contrast, the **First Touch** option assigns 100% credit to
   the first chat and agent that the customer talks to, regardless of how many they speak to
   after the first one.
4. Enter an attribution period. The attribution period is the number of days within which
   agent interactions will be considered for attribution.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/attribution.png)
5. Set the Goal URL field to the page your customer ends on after they've taken the action
   you're trying to track (in this example, making a purchase). The goal URL page needs to be
   one the Chat widget is embedded on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/goal_url.png)
6. Click **Create Goal**.

## Viewing conversions in chats

Now that you have your conversion goals set up, you'll want to keep an eye out for when a
customer completes a goal.

The following notification appears in a chat every time a customer completes the goal.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/goal_chat_event.png)

You can view conversions associated with past chats by selecting the chat in the History
tab.

**To view past chats with conversions**

1. Click the arrow next to the field to enter advanced search criteria.
2. Next to **Goal completed**, select a goal from the drop-down list.
3. Select a chat, then click the **Conversions** tab.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Chat_conversion_history.png)

You can then see the goal name, agent, and time since the chat was closed. See [Browsing past chats in History](https://support.zendesk.com/hc/en-us/articles/4408893866778-Browsing-past-chats-in-History) for more information
on the History tab.

## Measuring conversions in Analytics

To keep track of all your conversions, view the overall conversions in Analytics under
**Chat Reports**. For example, the following shows that there were roughly 1,200 chats
and 2,300 conversions on May 3rd.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_analytics_conversions.png)

Drill down further to see which chats influenced those conversions under **Agent
Reports**. The dates on the report represent when the conversion occurred, not the chat
date. The following example shows that 78 of the 2300 conversions were influenced by a
chat.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conversions_agent_reports.png)

To get even more detailed, view the Home tab to see the total number of visitors on May
3rd.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conversion_analytics_home.png)

You can then calculate the conversion rate as follows:

- **Total conversions**: 2300
- **Total conversions attributed to chat:** 78
- **Total visitors:** 100,0000
- **Conversion rate (2300/100,000):** 2.3%
- **Chat conversion rate (78/2300):** 3.39%
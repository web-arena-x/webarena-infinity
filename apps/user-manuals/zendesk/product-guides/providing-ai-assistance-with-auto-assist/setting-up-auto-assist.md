# Setting up auto assist

Source: https://support.zendesk.com/hc/en-us/articles/8984493142810-Setting-up-auto-assist

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Auto assist is an AI tool that helps agents by suggesting replies and actions for tickets. To set it up, identify repetitive issues, enable the feature, write procedures, tag relevant tickets, and test the setup. This process ensures that agents receive helpful suggestions, improving response times and accuracy. Each suggestion requires agent approval, allowing safe real-world testing.

[Auto assist](https://support.zendesk.com/hc/en-us/articles/9945148867866) is an AI-powered assistant for
your agents. Using large language model (LLM) technology, auto assist understands the
contents of submitted tickets and makes suggestions to your agents on how to solve
them.

These suggestions can be replies that the agent should send
to the customer, or actions that the agent should take. Auto assist suggestions appear
in tickets in the Agent Workspace in place of the composer.

Watch the demo video below to see auto assist in
action:

*Agent copilot featuring auto assist (4:43)*

To help you get the most out of Zendesk’s AI Copilot features, this
article provides an overview on how admins can get started with auto assist.

This article contains the following topics:

- [Step 1: Identify a
  problem where auto assist can help](#topic_ipg_tk2_r2c)
- [Step 2: Turn on auto
  assist and define who has access](#topic_lgk_jm2_r2c)
- [Step 3: Write a
  procedure for the problem](#topic_b35_pn2_r2c)
- [Step 4:Add a tag to
  tickets for which you created a procedure](#topic_iqd_l42_r2c)
- [Step 5: Test your
  procedure](#topic_yhc_lp2_r2c)

Related articles:

- [Turning on and configuring auto
  assist](https://support.zendesk.com/hc/en-us/articles/8013454025114)
- [Creating and managing procedures for auto
  assist](https://support.zendesk.com/hc/en-us/articles/7924047699738)
- [Creating and managing actions for auto
  assist](https://support.zendesk.com/hc/en-us/articles/8013439366810)

## Step 1: Identify a problem where auto assist can help

To identify a specific problem where you would like auto assist to suggest replies,
think of scenarios where your agents receive a lot of tickets that require
repetitive back and forth. For example:

- Advising a user on buying a product or service sold by your
  company
- Explaining a business policy
- Helping troubleshoot a problem

Tip: For inspiration, identify patterns by reviewing
your most popular [intents](https://support.zendesk.com/hc/en-us/articles/7934147095066#topic_mvx_bms_rcc), [macros](https://support.zendesk.com/hc/en-us/articles/4408835645466), or [ticket views](https://support.zendesk.com/hc/en-us/articles/4408829483930) and checking your [intelligent triage dashboard](https://support.zendesk.com/hc/en-us/articles/7934127855002). To best identify a problem
where auto assist can help, you’ll want to find tickets where a lot of messages were
exchanged between agents and end users.

## Step 2: Turn on auto assist and define who has access

After you’ve identified a problem, turn on auto assist and define which groups of
agents have access.

If you want to test auto assist yourself first, then select or
[create a group](https://support.zendesk.com/hc/en-us/articles/4408894175130) that only you’re in.

**To turn on and configure access to auto assist**

1. In Admin Center, click **AI** in the sidebar, then select **Agent copilot >
   Auto assist**.
2. Select **Show auto assist replies and actions in the agent composer**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ai_auto_assist_setting.png)
3. In the **Who has access** field, search for and select the groups that should
   be able to use the suggested replies feature. By default, all groups have
   access.
4. Click **Save**.

   See [Turning on and configuring auto
   assist](https://support.zendesk.com/hc/en-us/articles/8013454025114) for more information.

## Step 3: Write a procedure for the problem

Write a procedure that describes how the problem you identified should be handled.
Procedures are the instructions that auto assist should follow when suggesting
replies or actions to an agent in a ticket.

When writing a procedure, think of the way you would tell an
agent how to proceed with solving the problem you identified.

Tip: Review the [best practices for creating effective
procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738#topic_o3y_l44_xcc) before getting started.

**To write a procedure for the problem you’ve identified**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Manage articles**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Select **Procedures**, then click **Create procedure**.
3. In the **Name** field, enter a descriptive name for the procedure.
4. To associate the procedure with specific brands, open the right-hand Settings
   panel, click **Selected brands**, then choose the brands you want to
   associate the procedure with.
5. Click below the name field and enter the content for your procedure.

   To add
   specific actions to your procedure, click the **Insert action** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_add.png)) button in the
   toolbar.
6. To publish your procedure, click the drop-down arrow next to Save draft and
   select **Publish**.
7. In the window that appears, click **Publish**.

   Published procedures are
   automatically available for auto assist to use.

   See [Creating procedures for auto
   assist](https://support.zendesk.com/hc/en-us/articles/7924047699738) for more information.

## Step 4: Add a tag to tickets for which you created a procedure

Each ticket needs to have an “agent\_copilot\_enabled” tag. A good practice is to add
this tag for tickets with a specific intent, after writing a procedure on how to
handle those.

The tag should only be added to tickets for which you have
created a procedure. Otherwise, auto assist will suggest replies to tickets without
procedures, which leads to suggestions that aren’t applicable to your business.

**To create a trigger that adds the auto assist tag to
tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. On the Triggers page, click the Ticket tab, then click **Create
   trigger**.
3. Enter a **Name**, **Description**, and **Category** for your trigger.
   See [Creating ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) for
   details.
4. In the **Conditions** pane, under **Meet ALL of the following
   conditions**, add the following conditions:
   - **Ticket
     status | **Is** | **New****
   - **Tags** | **Contains none of the following** |
     **agent\_copilot\_enabled**
5. Under **Meet ANY of the following conditions**, add the following
   conditions:
   - (Optional) **Channel** | **Is** | <select the channel
     you want the trigger to work on>
   - (Optional) **Intent** | **Is** | <select an intent you have
     created a procedure for>
6. In the **Actions** pane, add the following action:
   - **Add tags | agent\_copilot\_enabled**
7. Click **Create**.

   See [Configuring auto assist on messaging or
   email channels using tags on answers](https://support.zendesk.com/hc/en-us/articles/8013454025114#topic_wx3_rww_xcc) for more
   information.

## Step 5: Test your procedure

Test your procedure before letting auto assist suggest replies or actions in a
real-world setting.

If the suggestions aren’t accurate, review the [procedure best practices](https://support.zendesk.com/hc/en-us/articles/7924047699738#topic_o3y_l44_xcc) and [edit your procedure](https://support.zendesk.com/hc/en-us/articles/9012170900890#topic_pd3_k44_xcc). Creating an effective
procedure is an iterative process that usually takes a few tweaks to get right.

**To test a procedure**

1. Make sure you’ve [limited the agents who can interact with auto
   assist](https://support.zendesk.com/hc/en-us/articles/8013454025114) to only the groups or agents who are performing the
   testing.
2. Create a messaging or email ticket with the agent\_copilot\_enabled tag.

   Email
   tickets must be created from an email that's not associated with any agents
   in your Zendesk account, because auto assist doesn't respond to agent
   comments.
3. [Try to solve the ticket](https://support.zendesk.com/hc/en-us/articles/7051314237466) with auto
   assist’s help.
4. Iterate the procedure until you get accurate and helpful suggestions.

   See [Testing a procedure](https://support.zendesk.com/hc/en-us/articles/7924047699738#topic_y2w_j44_xcc) for more
   information.

When you’re satisfied with auto assist’s suggestions for your procedure, invite your
agents to test it live with customers.

Each suggestion must be approved by the agent before it is sent
so there’s little risk in trying this live.
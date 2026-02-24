# Allowing customers to continue their conversation over email

Source: https://support.zendesk.com/hc/en-us/articles/4408829095706-Allowing-customers-to-continue-their-conversation-over-email

---

The continuous conversations feature allows you to automatically send an email notification to customers who abandon a conversation conducted through a messaging Web Widget, encouraging them to re-engage with your agents through their preferred channel.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

The continuous conversations feature lets you keep customer interactions going by sending an email when they leave a messaging conversation. Customers can resume the conversation via email or the website. Activate this feature to enhance user experience, especially during high wait times or offline hours.

The continuous conversations feature allows you to automatically send an email notification to customers who abandon a conversation conducted through a messaging Web Widget, encouraging them to re-engage with your agents through their preferred channel.

This article includes the following topics:

- [About continuous conversations](#topic_i1x_vxj_p4b)
- [Activating continuous conversations](#topic_lbl_bvj_p4b)
- [Deactivating continuous conversations](#topic_v2s_rrq_p4b)

## About continuous conversations

The continuous conversations feature allows both end users and agents to leave (but not end) a messaging conversation at any time and pick it up where they left off, without the end user losing track of the conversation.

End users may choose to leave a conversation when the expected wait time is high, when your business is offline, or there is a long queue, for example.

With continuous conversations activated, an email is sent to the end user informing them when an agent has left them a message in the conversation (see [The end user experience](#topic_urm_yxj_p4b)).
The continuous conversation email template is localized and translated based on the user's profile language in Support. See [How does Zendesk set a language for a user in Support?](https://support.zendesk.com/hc/en-us/articles/4408893879322)

To use continuous conversations, your account must meet the following requirements:

- Zendesk Suite OR Support + Chat (Team plan or higher).
- Agent Workspace activated. See [Activating and deactivating the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866).
- At least one agent with Chat access. See [About Staff roles in Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4408882929946).
- A [support email address](https://support.zendesk.com/hc/en-us/articles/4408842868506).

Consider the following when activating and using continuous conversations:

- The continuous conversations feature is only available when using messaging through a Web Widget, and is not available on mobile devices.
- Continuous conversation emails are based on your [email notification template](https://support.zendesk.com/hc/en-us/articles/4408886168090), and can't be edited by the agent conducting the conversation.
- Email notifications are sent when a conversation is [deemed inactive](https://support.zendesk.com/hc/en-us/articles/7043034053658)
 with unread messages from the agent, even if the associated ticket's status is Solved.
 However, they will not be sent if the associated ticket's status is Closed.

### The end-user experience

With continuous conversations activated, an end user who leaves an ongoing conversation from a website receives an email when an agent responds, allowing them to easily find and continue the conversation when they're ready. The end user can continue the conversation by responding to the email, or they can return to the website conversation.

The example below describes the default experience when you activate continuous conversations.
Here, an end user starts a conversation with a company that is currently offline. If the end user has provided an email, they will receive an acknowledgement informing them that email will be sent when the agent responds.
If the end user has not previously provided an email, they will be prompted to provide one. End user email addresses cannot contain accented characters.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/continuous_conversations_info_request.png)

Note: The "We're offline" message from the AI agent is fixed and cannot be customized.

Later, an agent responds to the original conversation request.
If the message from the agent remains unread until the [conversation is considered inactive](https://support.zendesk.com/hc/en-us/articles/7043034053658), an email is sent to the end user with the unread agent’s response.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/continuous_conversations_email_received.png)

The email includes the number of unread agent messages, a snippet of the conversation, and instructions for continuing the conversation.

The end user can choose to continue the conversation by responding to the email, or return to the website to do so.

Note: The example above uses the default [Support account email notification](https://support.zendesk.com/hc/en-us/articles/4408883361946)
format. If you are using a customized email template, the continuous conversations email sent to end users may look different.

### The agent experience

For agents, the entire conversation takes place in the Zendesk Agent Workspace. Continuing with the example above, when an agent returns to work, they are notified that a conversation is waiting for them in their queue, and they can respond to the conversation as usual.

If the agent leaves a message for the end user in the conversation, and the message remains unread by the end user, an email is automatically triggered.
When the end user responds, their response is included in the conversation, indicating whether it was sent via email or messaging:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/continuous_conversations_agent_view.png)

### Working with other triggers

If you are using the [out-of-office message](https://support.zendesk.com/hc/en-us/articles/4408842866074)
trigger, you may want to deactivate it when using continuous conversations to prevent sending duplicate messages to the end user.

## Activating continuous conversations

You can activate continuous conversations on the Ticket Settings page in Admin Center.

**To activate continuous conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Continuous conversations** to expand it.
3. Under the Settings tab, select **Switch messaging conversations to email**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/continuous_conversations_setting_2.png)

   This activates continuous conversations and creates an active, editable trigger, *Request email for continuous conversations*, that sends a request for the end user's email address after the conversation is idle for 5 seconds. You can find the trigger on the [Messaging triggers page](https://support.zendesk.com/hc/en-us/articles/5973077601562).

   Note: If you do not want to send an email request to end users – for example, if you are already collecting their email address at the beginning of the conversation – you can deactivate this trigger, or update the trigger's actions.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/continuous_conversations_trigger.png)

## Deactivating continuous conversations

If you choose to stop using continuous conversations, you’ll need to deactivate both the tickets setting and the trigger created when you activated the feature.

**To deactivate continuous conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Continuous conversations** to expand it.
3. Deselect **Switch messaging conversations to email**, then click **Save** at the bottom of the page.
4. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)
   , click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)**Objects and rules** in the sidebar, then select **Business rules > Messaging triggers** and open the trigger **Request email for continuous conversation**.
5. Deselect **Activate this trigger**, then click **Save**.
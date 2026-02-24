# Using the Answer Bot for Slack integration

Source: https://support.zendesk.com/hc/en-us/articles/4408827411098-Using-the-Answer-Bot-for-Slack-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

The [Slack for Zendesk integration](https://support.zendesk.com/hc/en-us/articles/4408833756698)
includes the Answer Bot for Slack integration.

The integration implements the [autoreplies with articles](https://support.zendesk.com/hc/en-us/articles/4408820349850) capability in Slack, so your end users can get help without waiting for someone to reply. It listens on selected Slack channels and resolves questions by providing article suggestions from your knowledge base.

Answer Bot for Slack is a free feature available in the Slack for Zendesk integration.

This article includes the following topics:

- [About the Answer Bot for Slack integration](#topic_nsp_mry_shb)
- [Adding the integration to a Slack channel](#topic_tx3_4ry_shb)
- [Removing the integration from a Slack channel](#section_adv_z5s_shb)
- [Editing autoreply settings for a Slack channel](#topic_mq2_xvw_dvb)
- [Asking a question in Slack](#topic_tr1_pry_shb)

For more information about Answer Bot and the Slack for Zendesk integration, see the following articles:

- [Understanding everywhere you can use Zendesk bots](https://support.zendesk.com/hc/en-us/articles/4408821281818)
- [Using the Slack for Zendesk integration](https://support.zendesk.com/hc/en-us/articles/4408843621530)

## About the Answer Bot for Slack integration

This integration is built on top of the Slack for Zendesk integration. It is automatically available when you install the Slack for Zendesk integration. After Answer Bot for Slack is installed, Zendesk admins can use Admin Center to add it to Slack channels.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_answer_bot_convo_new.png)

Note: The Answer Bot for Slack integration works only for [languages supported by essential AI agents](https://support.zendesk.com/hc/en-us/articles/4408821324826#01K20M7T89DW513X9KM1QPYAM6). However, Answer Bot cannot provide article suggestions in Slack when questions are asked in Chinese, Korean, Japanese, or Thai.

## Adding the integration to a Slack channel

Zendesk administrators can add autoreplies with articles to specific Slack channels in Admin Center. The feature can be added to public and private channels. You must have access to the private channels to add this feature to them.

You first need to install the [Slack for Zendesk integration](https://support.zendesk.com/hc/en-us/articles/4408833756698) and [activate autoreplies](https://support.zendesk.com/hc/en-us/articles/4408820349850) for this feature to be available.

**To add Answer Bot to a specific channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Configure** under the name of the Slack workspace you want to configure.
4. Click the **Answer Bot** tab.
5. Click **Add Answer Bot**.

   The Add Answer Bot page appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_answer_bot_add.png)
6. In the **Slack Channel** field, select the channel where you want to add Answer Bot.

   The drop-down list displays public and private channels (that you have access to) where [Zendesk is invited](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb) and Answer Bot for Slack is not already set up.

   The Slack channel list includes private channels that you are a member of. If the app is a member of a private channel that you're not a member of, you won't see it here until you are also invited to that channel.

   If you don't see your private channels in Zendesk (and you do see them in Slack), make sure you added the Zendesk app to these channels. Also, ensure that your default email in Zendesk matches your Slack email address.
7. In the **Brand** field, select the [brand](https://support.zendesk.com/hc/en-us/articles/4408829476378)
   to associate with this Answer Bot.
8. In the **Segments** field, select [user segments](https://support.zendesk.com/hc/en-us/articles/4408827797274)
   to refine article recommendations by user segment.
9. Click **Save**.

Answer Bot is added to the channel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_answer_bot_saved.png)

## Removing the integration from a Slack channel

To remove Answer Bot from a channel, you need to delete the integration from that channel. You can’t recover it after you delete it.

**To delete Answer Bot for Slack from a single channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Configure** under the name of the Slack workspace you want to configure.
4. Click the **Answer Bot** tab.
5. Hover over the channel, click the options menu that appears (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), then click **Delete**.
6. Click **Delete configuration**.

## Editing autoreply settings for a Slack channel

After you’ve added Answer Bot for Slack to a channel, you can update the settings.
The changes take effect within the Slack channel immediately after you save them.

**To edit autoreply settings for a Slack channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Configure** under the name of the Slack workspace you want to configure.
4. Click the **Answer Bot** tab.
5. Hover over the channel, click the options menu that appears (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), then click **Edit**.
6. Update the Answer Bot settings as needed.
7. Click **Save**.

## Asking a question in Slack

Answer Bot for Slack listens on configured Slack channels and offers article suggestions when a question is posted. The integration only listens on Slack channels and does not interact with direct messages in Slack.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_answer_bot_convo_new.png)

If your company uses multiple Zendesk accounts and has them configured in the same channel, you'll receive article suggestions from all help centers tied to the Slack workspace. The article suggestions aren't combined into one response; you will see multiple Answer Bot responses.

**To ask a question using autoreplies with articles in Slack**

1. Post a question in the Slack channel containing at least five words ending with a question mark. The bot responds to the question by starting a thread.

   If the bot doesn't respond, no articles were found related to your question. Try rephrasing your question.
2. Click **Yes** or **No** to indicate whether your question is answered.

   Clicking **No** gives you options to give feedback and **Submit a Request** to create a ticket.
3. If more than one article is found, click **More suggestions** to see additional articles.
4. Click the article number button if it answers your question, or **None of the above** if a suitable answer is not provided.

Your response to article suggestions is visible as a green tick or red cross emoji reaction after the question. This is particularly useful in a busy Slack channel. It indicates to other members of the channel whether the question was successfully resolved or whether it needs someone to respond.

If the suggestion doesn’t answer your question, you can create a ticket directly from Slack by clicking **Submit a Request**. For more information on submitting and viewing tickets created in Slack, see [Using the Slack for Zendesk integration](https://support.zendesk.com/hc/en-us/articles/4408843621530-Using-the-Slack-for-Zendesk-integration) .
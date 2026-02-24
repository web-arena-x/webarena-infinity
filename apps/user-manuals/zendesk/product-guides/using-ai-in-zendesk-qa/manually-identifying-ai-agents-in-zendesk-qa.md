# Manually identifying AI agents in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/8071540887450-Manually-identifying-AI-agents-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Manually identify AI agents to ensure they are reviewed with the right resources. Add third-party bots as users, ensuring each has a unique email. Mark users as bots, but note that only certain roles can be marked. If needed, revert a bot to a user without data loss. Exclude bots from reviews if context is lacking, using the reviewable option.

Besides [Zendesk QA’s automatically detected AI agents](https://support.zendesk.com/hc/en-us/articles/7418648293018), you can manually mark other users as AI agents, so they can be reviewed using the correct resources.

Admins and account managers can mark users as bots. Users with [admin roles](https://support.zendesk.com/hc/en-us/articles/7043760141978) cannot be marked as bots.

Before third-party bots can be marked as bots in Zendesk QA, they must first be added as users. You can add third-party bots via Zendesk Admin Center. See [Managing third-party bots in Admin Center.](https://support.zendesk.com/hc/en-us/articles/5064149334426)

Important: Each bot must use a unique email address which cannot be used in more than one Zendesk account, such as a production and [sandbox account](https://support.zendesk.com/hc/en-us/articles/4408824434586). For example, FIN typically has a unique identifier in the format: *operator+{FIN-ID}@intercom.io*.

**Marking users as bots**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. Select **Users**.

   Your list of users is displayed.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) next to the user.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_mark_as_bot.png)
4. Select **Mark as bot**.

Your marked user-bot is now listed in the Bots section.

If you accidentally set a real user as a bot, they won’t be able to log in anymore. However, you can revert this action by selecting **Mark as user**. No data will be lost.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ZendesQA_mark_as_user.png)

You can exclude bots from reviews by selecting Yes or No using the checkbox in the Reviewable column. This can be useful when you don’t have enough context to review a bot. See [Configuring which AI agents are evaluated](https://support.zendesk.com/hc/en-us/articles/7418648293018#topic_wrh_gzs_rdc).
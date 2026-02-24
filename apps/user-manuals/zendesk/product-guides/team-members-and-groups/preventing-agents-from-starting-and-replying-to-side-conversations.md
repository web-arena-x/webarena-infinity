# Preventing agents from starting and replying to side conversations

Source: https://support.zendesk.com/hc/en-us/articles/4408832432922-Preventing-agents-from-starting-and-replying-to-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

To prevent [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents-Enterprise-) from starting and replying to [side conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962), you must disable the permission to do so.
Otherwise, all agents are able to start and reply to side conversations.

You may want to do this if, for example, you have multiple tiers of agents, and only the more advanced agents need to be able to reach out to external partners as part of the escalation process. Creating a custom role for lower-level agents that doesn't include side conversation permissions prevents them from sending emails to anyone outside of the tickets they're working on. This helps them stay focused on their tasks by not presenting a new tool to work with. Note that disabling this setting doesn't change an agent's ability to see all of the side conversations on a ticket. There is no setting that restricts the visibility of side conversations to certain agents.

**To disable side conversation permissions for custom agents**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Locate the role you want to edit and click **Edit**.
3. Scroll down to the the **Agent workflow** section, and then disable **Contribute to side conversations**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_custom_role_permission2.png)
4. Click **Save**.
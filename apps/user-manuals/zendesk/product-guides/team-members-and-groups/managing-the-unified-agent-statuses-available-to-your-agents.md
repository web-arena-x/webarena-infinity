# Managing the unified agent statuses available to your agents

Source: https://support.zendesk.com/hc/en-us/articles/5133588225690-Managing-the-unified-agent-statuses-available-to-your-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Manage unified agent statuses to control availability across email, voice, and messaging. You can view default statuses and edit or delete custom ones. Custom statuses let you tailor availability settings, while idle timeout rules can automatically set agents to away or offline. Use APIs to manage agent and group availability for more control over your team's status management.

Location: Admin Center > Objects and rules > Omnichannel routing > Agent statuses

[Unified agent status](https://support.zendesk.com/hc/en-us/articles/5133523363226) is part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) and provides a way for agents to control availability for email, voice, and messaging from a single menu. The default agent statuses are view-only, but [custom unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594) can be edited or deleted.
Admins can also [enable and configure an idle timeout](https://support.zendesk.com/hc/en-us/articles/5286614817562) rule to automatically set idle agents to *away* or *offline*.

This article contains the following topics:

- [Viewing unified agent statuses](#topic_og3_1ms_bvb)
- [Editing a custom unified agent status](#topic_pwr_xc1_4vb)
- [Deleting a custom unified agent status](#topic_bqk_2g1_4vb)

If necessary, admins can use the [Unified Agent Status API](https://developer.zendesk.com/api-reference/agent-availability/unified-agent-status-api/introduction/) to view and set an agent's unified status or the [Group Availability API](https://developer.zendesk.com/api-reference/agent-availability/account-groups-availability/account_groups_availability/) to view availability and capacity data at the group level.

## Viewing unified agent statuses

When you enable omnichannel routing, native unified agent statuses automatically become available for agents to use across channels. They cannot be edited, but you may review their configuration. If you [add custom unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594) (Professional and Enterprise plans), they are also available for all agents to use.

**To review unified agent statuses**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent statuses**.
2. To view how a default status is set up, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), and then select **View details**.
3. Review the configuration and click **Close** to return to the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_native_agent_statuses.png)

## Editing a custom unified agent status

Native unified agent statuses can't be edited. If you [created](https://support.zendesk.com/hc/en-us/articles/4410525357594) custom unified statuses, you can modify them at any time. However, editing a custom unified status won't change the status of any agent using that status at the time. The updated status name and definition won't be applied to that agent until the next time they set that status. For this reason, consider deploying updates outside of business hours if possible, or when fewer agents are online.

**To edit a custom unified status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent statuses**.
2. Find the custom status in the list, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), and select **Edit**.
3. Make your changes and then click **Save**.

   You might need to refresh the Agent Workspace to see your changes.

## Deleting a custom unified agent status

When a custom unified status is deleted, any agents using the status at the time are notified, set to offline, and encouraged to set a new status.

Note: If you've configured idle timeouts or disconnection statuses for the custom unified agent status you're deleting, the following changes occur for agents upon the deletion of their current status:

- If the agent goes idle, they will remain in the current status. This is true regardless of whether a different idle status was configured for the deleted custom status.
- If the agent experiences a disconnection event, their status is set to *Offline*.

**To delete a custom unified status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent statuses**.
2. Find the custom status in the list, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), and select **Delete**.
3. In the confirmation dialog, click **Delete**.
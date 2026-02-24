# Managing skills

Source: https://support.zendesk.com/hc/en-us/articles/5833516958362-Managing-skills

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Objects and rules > Business rules >
Skills

With skills-based routing, you can set up *skills* and associate each one with individual agents. For each skill, you also define a set of ticket conditions that require the skills. Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can edit and delete skills and skill types.

This article contains the following topics:

- [Understanding the effects of modifying skills and skill types](#topic_wnj_gsl_5xb)
- [Managing skills](#topic_epv_zrl_5xb)
- [Managing skill types](#topic_ohk_1sl_5xb)

For more information about creating skills and managing skills assigned to agents, see [Adding agent skills to use for routing](https://support.zendesk.com/hc/en-us/articles/4408838892826).

## Understanding the effects of modifying skills and skill types

Before updating your skills, it's important to understand the impacts of that change.

- When you change the name of a skill, it is automatically updated on tickets and agent profiles.
- Within a skill type, skill names must be unique. We recommend that you avoid repeating skill names between skill types, too. When using skills in triggers, you only see the list of skill names without the context of their skill types.
- When you delete a skill, it is automatically removed from the tickets and agents it was assigned to.
- When you delete a skill type, you also delete all skills it contains.

## Managing skills

Skills can be viewed, edited, or deleted after they've been created. They can be manually viewed and modified by admins or [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_y53_s3t_mfb) on a ticket-by-ticket basis.

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can assign skills to agents.

### Renaming a skill

If a skill is renamed, the updated skill name is reflected on the ticket, agent profiles, and in business rules.

**To rename a skill**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Hover your cursor over the skill you want to edit, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Rename**.
3. Enter the new name.
4. To save your change, press **Enter** or click away from the field.

### Deleting a skill

Skills can be deleted from the Skills admin page. When you delete a skill, it is permanently removed from tickets and agent profiles.

**To delete a skill**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Hover your cursor over the skill you want to edit, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Delete**.
3. In the confirmation dialog, click **Delete skill**.

## Managing skill types

Because skill types only exist on the Skills page to help organize skills, there are fewer options for managing them. You can either rename them or delete them. You can't move skills between skill types. Instead, they must be recreated in the skill type you want it to be in.

### Renaming a skill type

Renaming a skill type can help you manage skills contained within skill types, but won't affect tickets or agents.

**To rename a skill type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Hover your cursor over the skill type you want to edit, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Rename**.
3. Enter the new name.
4. To save your change, press **Enter** or click away from the field.

### Deleting a skill type

When you delete a skill type, you also delete any skills within it. This can't be undone.

**To delete a skill**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Hover your cursor over the skill type you want to edit, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Delete**.
3. In the confirmation dialog, click **Delete skill type**.
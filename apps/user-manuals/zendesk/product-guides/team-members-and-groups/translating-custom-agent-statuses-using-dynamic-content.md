# Translating custom agent statuses using dynamic content

Source: https://support.zendesk.com/hc/en-us/articles/5360039903898-Translating-custom-agent-statuses-using-dynamic-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

[Unified agent status](https://support.zendesk.com/hc/en-us/articles/5133523363226) is part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) that enables agents to set a single unified status for email, voice, and messaging. If you support multiple languages, you can translate, or localize, your custom agent statuses. That way, when an agent needs to set their status, they can do so in their primary language.

Unified agent statuses are automatically available to accounts that meet certain [requirements](https://support.zendesk.com/hc/en-us/articles/5133523363226-About-unified-agent-status#topic_zvv_bjt_nvb) and enable omnichannel routing.
To learn more about unified agent statuses, see [Creating custom unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594). To learn more about how dynamic content works, see [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066).

This article contains the following topics:

- [Creating and using dynamic content for custom agent statuses](#topic_shh_ffv_f5b)
- [Viewing and testing your localized agent statuses](#topic_cnr_3fv_f5b)

## Creating and using dynamic content for custom agent statuses

To localize the names of custom agent statuses, you’ll create dynamic content, which includes a default language along with additional variants for the other languages you want the status to be available in. Then you'll use the dynamic content placeholder as the name for the custom agent status.

Tip: Before you get started, make sure you’ve already [created the custom status](https://support.zendesk.com/hc/en-us/articles/4410525357594) you want to localize. Also, make sure you [have the translations](https://support.zendesk.com/hc/en-us/articles/4408886903450) of the statuses in your supported languages.

**To create dynamic content for a custom agent status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. Click **Add item**.
3. Under **Dynamic content item title**, enter a descriptive title for your new piece of dynamic content. To make it easier to find and manage your localized agent statuses, Zendesk recommends naming the dynamic content the same as the custom status name in your account's default language (for example, "Agent status - <Status name> ".
4. Select the **Default language** for your dynamic content. This field shows all of the [languages that you have enabled](https://support.zendesk.com/hc/en-us/articles/4408888770714) for Zendesk Support.
5. In the **Content** field, enter the name of the status you want to see for the default language.

   Tip: Remove any trailing spaces or line breaks before saving your text, as this might cause issues when used within other Zendesk products.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_agent_status_dynamic_content_create.png)
6. Click **Create**. You're redirected to a screen where you can add variants for the languages you want your status to be available in.
7. Click **Add variant** and fill out the following fields:
   1. **Language**: Select a language you want the status to be available in.
   2. **Status**: Select **Active**.
   3. **Default**: Leave this checkbox blank. Select it only if you want to change the status's default language from the one you created earlier to this one.
   4. **Content**: Enter the name of the status in the language you just selected. In other words, this is the translation of the status name you entered in your initial piece of dynamic content.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_agent_status_dynamic_content_variant.png)
8. Click **Create**. You’re redirected to the variants page.
9. (Optional) Repeat steps 7-9 for any additional languages you want the custom agent status to be available in.
10. Near the top of the variants page, copy the **Placeholder** text for your dynamic content. You'll need this for the next step.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_agent_status_dynamic_content_placeholder.png)
11. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
    **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent statuses**.
12. Find the custom agent status you want to localize, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), and select **Edit**.
13. Paste your dynamic content placeholder into the agent status's **Name** field.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_agent_status_dynamic_content_use.png)
14. Click **Save**.

## Viewing and testing your localized agent statuses

You can view and manage your localized agent statuses on the Agent statuses administration page.

**To view and manage your localized agent statuses**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
 **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent statuses**.

When viewed here, localized custom statuses show the placeholder name in the **Status** column.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_agent_status_dynamic_content_view_list.png)

For more on managing agent statuses, see [Managing unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133588225690).

**To test that your agent status is localized**

1. In the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), click your profile icon in the upper-right corner of the page header and view the available statuses.
2. In your [user profile](https://support.zendesk.com/hc/en-us/articles/4408835022490), change your **Language** to one of the status variants you created.
3. Refresh the page.
4. Click your profile icon in the upper-right corner of the page header and check that you now see the localized agent status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_agent_status_dynamic_content_select.png)

For more on setting unified agent statuses, see [Setting your agent status with omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4410545721114).
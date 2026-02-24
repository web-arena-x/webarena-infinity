# Configuring the knowledge section in the context panel

Source: https://support.zendesk.com/hc/en-us/articles/7263163614874-Configuring-the-knowledge-section-in-the-context-panel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Enable the knowledge section in the context panel to let agents search your help center for articles, view suggestions, and provide feedback. Configure content sources like knowledge articles, community posts, and external content. Set default search filters to streamline agent searches. These settings enhance your team's ability to find and use relevant information quickly.

Location: Admin Center > Workspaces > Agent tools > Context panel

In the [knowledge section of the context panel](https://support.zendesk.com/hc/en-us/articles/5581313653530), your agents can search for content in your help center that might help your customers solve issues, view suggestions for articles based on ticket content, or add feedback to flag existing articles.

Admins can activate the knowledge section in the context panel, set knowledge sources that are included, and configure default search filters.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/GenSearch-SearchResult.png)

This article includes these sections:

- [Enabling or disabling knowledge in the context panel](#topic_qpq_dqk_qpb)
- [Configuring content sources for knowledge in the context panel](#topic_eqk_2cw_fpb)
- [Configuring default search filters for knowledge in the context panel](#topic_gwh_mr3_k5b)

## Enabling or disabling knowledge in the context panel

The knowledge section is enabled by default in the context panel.

**To enable or disable knowledge in the context panel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Context panel**.

   The configuration settings for the context panel appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cross-prod-turn-on-knowledge.png)
2. In the **Knowledge** section:
   - Select **Turn on Knowledge** to turn on Knowledge in the context panel.

     When you turn on Knowledge, you can configure which knowledge sources are searched. See [Configuring content sources for knowledge in the context panel](#topic_eqk_2cw_fpb).
   - Deselect **Turn on Knowledge** to turn off Knowledge in the context panel.

     When you turn off Knowledge, the Knowledge icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_knowledge.png)) is removed from the context panel and your knowledge sources aren't searched.
3. Click **Save**.

## Configuring content sources for knowledge in the context panel

You can configure which content sources are searched to determine the answers that appear in the context panel and you can specify whether agents can use existing templates to create articles.

**To configure content sources**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Context panel**.

   The configuration settings for the context panel appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cross-prod-know-context-pnl.png)
2. Ensure **Turn on Knowledge** is selected.
3. When Knowledge is turned on, select the content sources you want to include in Knowledge searches:
   - **Knowledge articles**: [Articles](https://support.zendesk.com/hc/en-us/articles/4408839258778) included in your help center.
   - **Community posts**: Information posted in your help center [community](https://support.zendesk.com/hc/en-us/articles/4408882689306), including questions, answers, and shared ideas.
   - **External content**: Content that is external to your help center, but that can be configured to appear in your help center's search results. This option appears only if [federated search is configured](https://support.zendesk.com/hc/en-us/articles/4593564000410).
4. If you want to restrict Agents and Admins to only create articles from existing templates (and not create new blank articles), then **Under Configure knowledge**, select the **Require articles templates** checkbox.

   Note: You must be an Admin to [create a template](https://support.zendesk.com/hc/en-us/articles/4408828223898). If no templates have been created, then this option will not appear in Knowledge.
5. If you want to provide AI-generated answers to the searches that agents perform within the knowledge section of the context panel, select [Show a quick answer before search results](https://support.zendesk.com/hc/en-us/articles/8079579364250).
6. When you’ve finished selecting content sources, click **Save**.

## Configuring default search filters for knowledge in the context panel

You can configure the default search filters that are available for agents searching for content in Knowledge in the context panel.

Note: You can also configure default filters for the [knowledge section of contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408833498906) (Enterprise plans). When default filters are configured in a contextual workspace, those filter settings override default filters configured in the Context panel.

Default search filters are automatically applied to agent search queries unless they are manually changed or removed by agents. Configuring the filters that agents use the most reduces the time they spend customizing default search filters before searching for content.

**To configure default search filters**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Context panel**.

   The configuration settings for the context panel appear.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ContextPanelSearch-default-filters.png)
2. In the **Default filters** section, configure the default filters that you want to use. If you want to:
   - Remove the selected filters, click **X** to remove the filters displayed in the Default filters list.
   - Add new filters, use the dropdown menu to select the filters that you want to add. You can click the **>** icon to display the filters grouped under a filter type (for example, Brand or Language). Select up to five filters within each filter type that you want to use as default search filters.

     ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-context-panel-filter-ddown.png)
3. When you’ve finished selecting filters, **Save** your changes.
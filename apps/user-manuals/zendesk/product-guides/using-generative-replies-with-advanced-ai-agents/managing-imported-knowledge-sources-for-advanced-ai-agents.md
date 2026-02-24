# Managing imported knowledge sources for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9962106058906-Managing-imported-knowledge-sources-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Knowledge sources are the information your advanced AI agent uses to create AI-generated answers to questions from your customers. After you [import a knowledge source](https://support.zendesk.com/hc/en-us/articles/8357749301658), you can manage it from the Knowledge sources page.

This article contains the following topics:

- [Viewing all imported knowledge sources for an advanced AI agent](#topic_bhz_wp5_3hc)
- [Reimporting a knowledge source manually](#topic_mxn_4n5_3hc)
- [Editing an imported knowledge source](#topic_dhj_qn5_3hc)
- [Deleting a knowledge source](#topic_uwd_rn5_3hc)
- [Viewing the import summary for a web crawler import](#topic_jxx_rn5_3hc)

Related article:

- [Configuring search rules for knowledge sources for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9185497386394)

## Viewing all imported knowledge sources for an advanced AI agent

On the Knowledge sources page, you can view all the knowledge sources currently connected to an advanced AI agent. The AI agent uses these sources to generate answers to customer questions.

**To view all imported knowledge sources**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.

   The Knowledge sources page shows a list of all knowledge sources that have been imported for the AI agent. The list includes the following columns:

   - **Type**: The type of imported knowledge source.
   - **Name**: The name of the knowledge source.
   - **Source**: The URL or file name of the knowledge source.
   - **Status**: The status of the import.
   - **Import frequency**: How often the knowledge source is reimported.
   - **Last updated**: When the knowledge source was last updated.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_sources_list.png)

## Reimporting a knowledge source manually

If you want to reimport a knowledge source outside the frequency you specified in its configuration, you can perform a manual reimport.

**To reimport a knowledge source manually**

1. [In the list of knowledge sources](#topic_bhz_wp5_3hc), find the knowledge source you want to reimport.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Reimport**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_sources_reimport.png)

## Editing an imported knowledge source

You can edit an imported knowledge source's settings at any time.

**To edit an imported knowledge source**

1. [In the list of knowledge sources](#topic_bhz_wp5_3hc), find the knowledge source you want to edit.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Edit**.

   The Edit source panel opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_sources_edit_panel.png)
3. Edit the settings as needed.

   For help with any of the fields, see [Importing a knowledge source](https://support.zendesk.com/hc/en-us/articles/8357749301658#topic_kpz_13w_cfc).
4. Click **Save**.

## Deleting a knowledge source

You can disconnect a knowledge source from an AI agent to prevent it from using the information in that source when generating answers to customer questions.

**To delete a knowledge source**

1. [In the list of knowledge sources](#topic_bhz_wp5_3hc), find the knowledge source you want to delete.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Delete**.

   A confirmation window opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_sources_delete.png)
3. Click **Delete**.

## Viewing the import summary for a web crawler import

When you [import content using a web crawler](https://support.zendesk.com/hc/en-us/articles/8357749301658#topic_amk_g3w_cfc), you can view a summary that shows the details of the import, including the specific content that was imported. This information can be especially useful when [troubleshooting issues with web crawler imports](https://support.zendesk.com/hc/en-us/articles/9961828111258).

Note: Import summaries are available only for web crawler imports, not other import types.

**To view the import summary for a web crawler import**

1. [In the list of knowledge sources](#topic_bhz_wp5_3hc), find the web crawler knowledge source you want to view an import summary for.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Import summary**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_sources_import_summary_menu.png)

   A new browser tab opens, showing the Import summary page. The summary includes the following information:

   - **Source name**: The name of the web crawler import.
   - **Results**: How many pages were imported.
   - **Total duration**: How long the import took.
   - **Imported on**: The date and time the content was imported.
   - **Import frequency**: How often the import is scheduled to run.
   - **Overview**:
     - **Webpage URL**: The URL of the imported page.
     - **Extracted text**: The actual text the crawler imported.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_sources_import_summary_page.png)
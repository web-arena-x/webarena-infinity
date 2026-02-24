# Importing ticket data from Zendesk Support into an advanced AI agent

Source: https://support.zendesk.com/hc/en-us/articles/8357758714906-Importing-ticket-data-from-Zendesk-Support-into-an-advanced-AI-agent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

After you [create an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749415066) and [connect it to email](https://support.zendesk.com/hc/en-us/articles/8357750858010), you can import ticket data from Zendesk Support. This populates the AI agent’s [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) with historical data from Zendesk Support.

**To import ticket data from Zendesk Support into an advanced AI agent**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. On the Overview tab, click **Import conversations**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_import_conversations_button.png)

   The Import conversations from Zendesk Support panel opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_import_conversations_zendesk_support.png)
4. In **Time frame**, select the window of time you want to import tickets from.
5. (Optional) In **Maximum messages**, enter the maximum number of tickets you want to import.
6. (Optional) In **Tag**, enter the specific tags that a ticket must have in order to be imported.
7. In **Channel**, select one or more channels that a ticket must have originated from in order to be imported.
8. In **Depth**, enter the number of responses within a ticket that should be imported.

   The default is 2.
9. (Optional) Select **Import tags** to import any [tags on the ticket in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408835059482)
   as [labels on the conversation in AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357749583130).
10. In **Group**, enter the ID of one or more groups that a ticket must have been assigned to in order to be imported.

    Separate multiple group IDs with commas.
    For help finding a group ID, see [How can I retrieve the group ID in Support?](https://support.zendesk.com/hc/en-us/articles/4408837673114)
11. In **Benchmark model**, select **Import only**.
12. Click **Import**.

    Depending on how much ticket data you’re importing, the import can take 10–20 minutes to complete. Afterward, you can see the imported data in the AI agent’s [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186).
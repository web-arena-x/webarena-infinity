# Adding and managing supported languages for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749666714-Adding-and-managing-supported-languages-for-advanced-AI-agents

---

If your customer base speaks multiple languages, you can add languages to your advanced AI agent so that it responds to your customers in the right language. You must add and activate a language to your AI agent before it can begin responding to customers in that language.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

If your customer base speaks multiple languages, you can add languages to your advanced AI agent so that it responds to your customers in the right language. You must add and activate a language to your AI agent before it can begin responding to customers in that language.

This article contains the following topics:

- [Adding a supported language to an advanced AI agent](#topic_rmc_kzx_jgc)
- [Activating an added language](#topic_etz_kzx_jgc)
- [Setting an AI agent’s default language](#topic_fhd_mzx_jgc)
- [Editing an added language](#topic_x5t_mzx_jgc)

Related articles:

- [Best practices for expanding language support for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357751833498)
- [Translating replies for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756745882)

## Adding a supported language to an advanced AI agent

Adding a supported language to an advanced AI agent means it can use that language (once [activated](#topic_etz_kzx_jgc)) to respond to customers during conversations. For dialogue-based responses, an [active reply](https://support.zendesk.com/hc/en-us/articles/9624068102682#topic_jyw_4zx_jgc) must also exist for that language.

**To add a new language**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to add a language to.
2. In the left sidebar, select **Settings** > **AI agent settings**.
3. Select the **Languages** tab.
4. Click **Add language**.
5. In **Languages**, select the language you want to add.
6. In **Icon**, select the icon for the new language.
7. If the AI agent already has well-built replies in another language that can be translated and reused in the language you’re adding:
   1. Select **Duplicate replies from another language (recommended)**.

      For AI agents that don’t have reusable replies, such as brand-new AI agents, keep this option deselected.
   2. Select the language you want to copy replies from.
8. In **Locale info (optional)**, enter the same locale information you maintain in your CRM (for example, de\_DE, germany, or DE).

   You can add multiple values separated by commas.

   Note: Locale values are case sensitive, so make sure at least one of the values you enter matches the locale value from your CRM exactly.
9. Click **Add**.

   A "New language added" dialog appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_new_language_added.png)
10. If you opted to duplicate replies earlier in these steps, click **Export** to [get a file for translation](https://support.zendesk.com/hc/en-us/articles/8357756745882).

    If you didn’t, click **Skip for now**.

Your language is added. You can continue to add more languages, or else begin [building dialogues](https://support.zendesk.com/hc/en-us/articles/8357749494810) for the new language.

## Activating an added language

An [added language](#topic_rmc_kzx_jgc) must be activated before an AI agent can use that language to respond to customers.
Activating a language publishes all [active replies](https://support.zendesk.com/hc/en-us/articles/9624068102682#topic_jyw_4zx_jgc) for that language, so make sure those replies are ready to be seen by customers before you do this.

**To activate a language**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to activate a language for.
2. In the left sidebar, select **Settings** > **AI agent settings**.
3. Select the **Languages** tab.
4. Find the language you want to activate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Edit**.
5. Select **Activate**.
6. (Optional) Select **Activate all inactive replies in this language** if you want to activate any reply that’s currently marked as inactive.
7. (Optional) Select **Set as default** if you want to set this language as the [AI agent’s default language](#topic_fhd_mzx_jgc).
8. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_activating_added_language.png)

## Setting an AI agent’s default language

An AI agent’s default language is used when the customer’s [locale is unknown](https://support.zendesk.com/hc/en-us/articles/8357756692890#topic_urt_nxx_jgc). A language must first be [active](#topic_etz_kzx_jgc) before it can be set as the default. An AI agent can have only one default language at a time.

**To set a default language**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to set a default language for.
2. In the left sidebar, select **Settings** > **AI agent settings**.
3. Select the **Languages** tab.
4. Find the language you want to activate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Edit**.
5. Select **Set as default**.
6. Click **Save**.

## Editing an added language

At any time, you can edit a language you added to an AI agent.

**To edit a language**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to edit a language for.
2. In the left sidebar, select **Settings** > **AI agent settings**.
3. Select the **Languages** tab.
4. Find the language you want to activate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Edit**.
5. Make changes as needed.

   See [Adding a supported language to an advanced AI agent](#topic_rmc_kzx_jgc) for help.
6. Click **Save**.
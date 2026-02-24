# Managing languages and translation support in AI agents

Source: https://support.zendesk.com/hc/en-us/articles/4408842754202-Managing-languages-and-translation-support-in-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

After you [create an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578), you can specify its default language and configure either automatic or custom translations for an improved customer experience. Using these settings, you can select a language for a single-language AI agent or create a multilingual AI agent.

You must be an admin to manage languages and translations for an AI agent.

This article contains the following topics:

- [Understanding language support in AI agents](#topic_x2q_3ff_3fc)
- [Configuring a default language for an AI agent](#topic_rzn_3cj_bpb)
- [Activating automatic translation for an AI agent](#topic_ddp_kcj_bpb)
- [Creating custom translations for AI agent messages](#topic_trh_sjg_5bc)

Related articles:

- [Best practices for supporting multiple languages in an AI agent](https://support.zendesk.com/hc/en-us/articles/9466418506010)
- [Viewing and configuring settings for AI agents](https://support.zendesk.com/hc/en-us/articles/6447052708762)

## Understanding language support in AI agents

Which language an AI agent uses to respond to a customer depends on the channel.

### Language support on messaging channels

For [standard responses](https://support.zendesk.com/hc/en-us/articles/8774095741466) and messages sent as part of an [answer flow](https://support.zendesk.com/hc/en-us/articles/4422584657434) (which is legacy functionality), the AI agent uses the language [set in the Language section of the Settings tab](#topic_rzn_3cj_bpb). By default, this is the same as your [account’s default language](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_rtc_42j_1y). This language can be any of the languages [listed here](https://support.zendesk.com/hc/en-us/articles/4408821324826#01K20M7T89DW513X9KM1QPYAM6).

For AI-generated replies, the language the AI agent uses depends on the language the customer types their initial message in:

- If the customer’s language is [supported by the AI model](../multiple-language-support/zendesk-language-support-by-product.md#01K20M7T89DW513X9KM1QPYAM6:~:text=Languages%20supported%20in%20generative%20replies), the AI agent replies in that language.
- If the customer’s language isn't supported by the AI model, the AI agent replies in the account’s default language.

If the customer's first message is too short to perform language detection, the AI agent continues in the language indicated by the customer’s browser or mobile app until they send a message long enough to perform language detection.

### Language support on email, API, and web form channels

The AI agent generates a response using relevant help center content in the same language as the [language set in the requester's profile](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_tmu_gno_ze). If no relevant content exists in the requester's language, the AI agent uses content in either of the following languages, evaluated in order:

- The parent language of the requester's language. For example, if the requester's language is British English (en-gb), but no help center content exists in that language, the AI agent uses English (en).
- The AI agent's default language.

## Configuring a default language for an AI agent

By default, your AI agent language is set to your [account's default language](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_rtc_42j_1y), but you can change it if necessary.

For consistency and ease of comprehension, the AI agent’s default language should match the language used in its [standard responses](https://support.zendesk.com/hc/en-us/articles/8774095741466).

**To configure a default language for an AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to configure a default language for.
3. Click the **Settings** tab.
4. Click the **Language** section to expand it.
5. Use the drop-down menu to select your language.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_default_language_set.png)

Your changes are automatically saved, but updates to the AI agent’s default language won’t be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Activating automatic translation for an AI agent

You can configure your AI agent to automatically translate its messages. This includes its [standard responses](https://support.zendesk.com/hc/en-us/articles/4422584657434#topic_slx_n4p_qtb) and, if you had a draft or published AI agent as of February 2, 2025, the text elements in any [answer steps](https://support.zendesk.com/hc/en-us/articles/4408836323738), including AI agent messages, options, button text and links, carousel card titles, image descriptions, and variables.

The AI agent’s [default language](#topic_rzn_3cj_bpb) is used as the source language when translating text.
The language the AI agent translates messages into depends on where the Web Widget is embedded. If the Web Widget is embedded in:

- **A Zendesk help center**, the AI agent uses the [language provided by the help center itself](https://support.zendesk.com/hc/en-us/articles/4408822162330#topic_pw2_w3z_5pb).
- **A website**, the AI agent uses the end user’s browser language.

In either case, you need to add the language as a supported language when activating automatic translation, as described below.

Activating automatic translation in an AI agent does not impact text elements managed outside of the AI agent settings, such as help center articles. You can, however, use dynamic content to translate some of these elements in Zendesk Support. See [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066).

**To activate automatic translation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to activate automatic translation for.
3. Click the **Settings** tab.
4. Click the **Language** section to expand it.
5. Select **Translate messages**.
6. Click **Select languages for translation** and select the languages you want to include in the automatic translation process.

   To filter the options, you can begin typing a language name.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_activate_automatic_translation.png)

Your changes are automatically saved, but updates to the AI agent’s automatic translation process won’t be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Creating custom translations for AI agent messages

Note: This section applies only if you're on Support Professional and above or Suite Growth and above.

If you find that the automatic translations for some AI agent messages don’t meet your standards—for example, by translating product and brand names, using incorrect pronouns, or using inaccurate phrasing—you can replace them with custom translations.

Custom message translations are manually written versions of the text in the message fields of an AI agent’s [standard responses](https://support.zendesk.com/hc/en-us/articles/4422584657434#topic_slx_n4p_qtb)
and, if you had a draft or published AI agent as of February 2, 2025, AI agent messages in [answer steps](https://support.zendesk.com/hc/en-us/articles/4408836323738). Custom translations aren’t available for other automatically translated text elements (such as option or button text).

To customize a message in a particular language, that language must be:

- Included in the [automatic translation settings](#topic_ddp_kcj_bpb)
- Added to the list of [available languages in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_aom_yxz_ye)

Custom-translated AI agent messages are sent to end users based on their [detected language](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_tmu_gno_ze).
If a message field does not have a customized translation in the end user’s detected language and that language is included in the automatic translation settings, it will be autotranslated.

This section contains the following topics:

- [Creating custom translations for AI agent standard responses](#topic_ewt_fbm_dgc)
- [Creating custom translations for AI agent messages in answer steps (Legacy)](#topic_l51_lzj_f2c)

### Creating custom translations for AI agent standard responses

You can create custom translations for the text in an AI agent’s standard responses.

**To create a custom translation for a standard AI agent response**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to create custom translations for.
3. Click the **Messaging behavior** tab.
4. Click the standard response you want to create a custom translation for.
5. Under the message text, click **Manage translations**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_translations_behavior.png)
6. Click the pencil icon for the language you want to customize, then enter the custom text.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_translations-customizing_ex.png)

   Repeat this step for additional languages if needed.
7. Click **Done**.

Your changes are automatically saved, but updates to the AI agent’s custom translations won’t be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

### Creating custom translations for AI agent messages in answer steps (Legacy)

Note: This section applies only if you had a draft or published AI agent as of February 2, 2025.

You can create custom translations for the AI agent messages in an answer step.

**To create a custom translation for an answer**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to create custom translations for.
3. Click the **Answers** tab.
4. Select the answer you want to create a custom translation for.

   The bot builder opens.
5. Click the AI agent message you want to create a custom translation for.

   You can’t create custom translations for other text elements, such as option or button text.
6. Under the AI agent message, click **Manage translations**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_translations_bot_builder.png)
7. Click the pencil icon for the language you want to customize, then enter the custom text.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_translations-customizing_ex.png)

   Repeat this step for additional languages if needed.
8. Click **Done**.

Your changes are automatically saved, but updates to the AI agent’s custom translations won’t be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).
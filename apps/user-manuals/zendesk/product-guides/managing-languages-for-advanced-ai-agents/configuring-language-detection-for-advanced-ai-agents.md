# Configuring language detection for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756692890-Configuring-language-detection-for-advanced-AI-agents

---

Language detection is the task of automatically identifying the language the customer is using during a conversation with an AI agent so that the AI agent can respond in the same language.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Language detection is the task of automatically identifying the language the customer is
using during a conversation with an AI agent so that the AI agent can respond in the
same language.

This article contains the following topics:

- [About language detection in advanced AI agents](#topic_urt_nxx_jgc)
- [Detecting the customer’s language](#topic_wwm_4xx_jgc)
- [Resetting the detected language](#topic_nzh_pxx_jgc)
- [Preventing the unsupported language reply from triggering](#topic_axl_qxx_jgc)

Related articles:

- [Languages supported by advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749663130)
- [Managing languages for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749666714)
- [Translating and building replies for advanced AI
  agents](https://support.zendesk.com/hc/en-us/articles/8357756745882)

## About language detection in advanced AI agents

For an advanced AI agent to reply in a customer’s preferred language, it must first
be able to detect the language. For dialogue-based responses, there must also be an
[active reply](https://support.zendesk.com/hc/en-us/articles/9624068102682#topic_jyw_4zx_jgc) created in that language. For
both dialogue-based and generative AI responses, the detected language must be [activated](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_etz_kzx_jgc) and be one of the [supported languages](https://support.zendesk.com/hc/en-us/articles/8357749663130#h_01JJZBMRA1W2EH2K4JQHR5FQ0S).

The customer’s language is set and stored in a [session parameter](https://support.zendesk.com/hc/en-us/articles/9522180655386#topic_lf5_pzp_xfc) called
*active\_language*. Language detection is triggered every time the
*active\_language* parameter is empty. This happens in the following
scenarios:

- On the first message
- If the language hasn’t been saved
- If the language has been reset

The AI agent can determine the customer’s language based on one of the following
methods:

- The content of the customer’s first message (default)
- An integration with your CRM
- The customer’s language selection in the welcome message (if configured)

The following table outlines how the AI agent responds based on the active or
inactive status of the detected language and the reply associated with the predicted
use case. The language status always takes precedence over the reply status.

|  |  |  |
| --- | --- | --- |
| **Language active or inactive?** | **Reply active or inactive?** | **AI agent responds with the…** |
| Active | Active | Dialogue associated with the reply for the detected language |
| Active | Inactive | “Default reply” [system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882#topic_edj_gnp_xfc) |
| Inactive | Active | “Unsupported language reply” system reply |
| Inactive | Inactive | “Unsupported language reply” system reply |

## Detecting the customer’s language

There are three different methods you can use to detect a customer’s language during
a conversation with an advanced AI agent:

- [Detecting language based on the customer’s first message](#topic_n1b_ydy_jgc)
- [Detecting language based on a CRM integration](#topic_qxk_xdy_jgc)
- [Detecting language based on selection in welcome message](#topic_vcv_12y_jgc)

Based on this information, you can then [use a conditional block](https://support.zendesk.com/hc/en-us/articles/8357733406234) to divert users to the correct
reply.

### Detecting language based on the customer’s first message

Detecting the language based on the customer’s first message leverages natural
language processing (NLP) technology. This type of language detection works by
default and is used if the language isn’t set manually. Additionally, this works
best on messages longer than five words. Using this method, the AI agent can
produce a:

- **High-confidence identification of an active language.** In this case,
  the AI agent responds to the customer in this language.
- **High-confidence prediction of an inactive or unsupported language.** In
  this case, the AI agent sends the “Unsupported language reply” system reply.
- **Low-confidence prediction of any language.** In this case, the AI agent
  falls back to its [default language](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_fhd_mzx_jgc) instead.

It’s important to note that using the customer’s first message to detect their
language may not be the right method in the following types of scenarios:

- **Your customers are likely to begin with short messages or use multiple
  languages in the same message.** For this, it’s worth [reviewing your AI agent’s conversation
  logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) to see what first messages customers typically send. Are
  they shorter than five words? Do they mix languages?
- **Your customer base speaks multiple closely related languages.** Another
  consideration is that closely related languages—such as Spanish and Catalan,
  or Serbian and Croatian—may have more overlap, making some sentences hard to
  predict with a high confidence.

In cases like these, it’s not recommended to use the customer’s first message to
detect their language, as there’s a higher chance of the AI agent setting an
incorrect language or sending the “Unsupported language reply” system reply.

### Detecting language based on a CRM integration

To detect a customer’s language based on your CRM integration, you must perform
the following tasks:

- [Setting the locale info in the language](#topic_zwr_sfy_jgc)
- [Creating an action to obtain user locale](#topic_gvj_5fy_jgc)
- [Detecting language based on selection in welcome message](#topic_vcv_12y_jgc)

#### Setting the locale info in the language

First, make sure the locale info is configured in the appropriate language.
If you didn’t already configure this when you [added the language](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_rmc_kzx_jgc), you can [edit the language](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_x5t_mzx_jgc) to update the
locale info.

Note: Locale values are case sensitive.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_language_set_locale.png)

#### Creating an action to obtain user locale

Next, you must create an action to obtain the customer’s locale.

**To create an action to obtain user locale**

1. In AI agents - Advanced, in the top-right corner, use the AI agent
   drop-down field to select the AI agent you want to create the action
   for.
2. In the left sidebar, select **Content** > **Actions**.
3. Click **Create action**.
4. In **Name**, give the action a descriptive name.
5. In **Target**, select your CRM.
6. In **Task**, select the following option associated with your
   CRM:
   - **Sunshine Conversations**: [Get user](https://support.zendesk.com/hc/en-us/articles/8357734565402)
   - **Zendesk Chat**: [Get tag](https://support.zendesk.com/hc/en-us/articles/8357750804250)
7. In **Field to retrieve**, select **locale**.
8. In **Save as parameter**, enter **active\_language**.
9. Click **Create**.

#### Adding the action at the AI agent level

Finally, you must add the action at the AI agent level. As part of this,
you’ll configure it to run at the beginning of every conversation.

**To add the action at the AI agent level**

1. In AI agents - Advanced, in the top-right corner, use the AI agent
   drop-down field to select the AI agent you want to add the action to.
2. In the left sidebar, select **Settings** > **AI agent settings**.
3. Select the **Events and actions** tab.
4. Click **Add action**.
5. Select **Conversation started**.
6. Select the action you created above.

### Detecting language based on selection in welcome message

At the beginning of the conversation, you can configure your conversation flow to
ask the user their language preference. To do this, [use a conditional block](https://support.zendesk.com/hc/en-us/articles/8357733406234) that includes
a fallback option with selectable supported languages. When a customer selects a
language, they’re directed to the rest of the conversation flow in that
language. See the image below for an example.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7293772757650.png)

## Resetting the detected language

Because many people work and travel in locations that aren’t aligned with the
language they’re most comfortable with, it’s a good idea to allow customers to reset
their language so they can communicate with you in their preferred language.

You can ask the customer to reset their language by creating a “Change language” use
case. Or, you could even repurpose the “Unsupported language reply” system reply. In
either case, you can then build a dialogue capable of resetting the
*active\_language* parameter.

**To reset the detected language**

1. [Create a new use case](https://support.zendesk.com/hc/en-us/articles/9041901679130) called
   **Change language** or [open the Unsupported language reply
   system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882#topic_jhb_k4p_xfc) for editing.
2. [Create a dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) for the use case
   in which you:
   1. [Add a conditional block](https://support.zendesk.com/hc/en-us/articles/8357733406234) to
      check the *active\_language* parameter to give options for
      languages.
   2. Add buttons that correspond to the languages the AI agent supports.
   3. [Add actions](https://support.zendesk.com/hc/en-us/articles/8357756623770) to set the
      language based on the conversation data.

      See the image below for
      an example.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_8751022282642.png)

## Preventing the unsupported language reply from triggering

The “Unsupported language reply” system reply checks the *active\_language*
session parameter to determine whether the customer’s language is detected and, if
so, supported. This system reply is automatically triggered during a conversation in
the following scenarios:

- The *active\_language* parameter is not set, and language detection
  identifies an unsupported language.
- The *active\_language* parameter is set, but the customer breaks away from a
  dialogue and begins using an unsupported language.

If you support a limited number of languages but still want to allow customers to
communicate in any language, you can prevent the system reply from triggering when
the *active\_language* parameter is already set (the second bullet point above).

In this scenario, the *active\_language* value isn’t changed and the “Unsupported
language reply” system reply isn’t triggered. Instead, the AI agent sends its next
reply based on the following priority: relevant use case > “Generative replies”
system reply > default reply.

**To prevent the unsupported language reply from triggering**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down
   field to select the AI agent you want to update.
2. In the left sidebar, select **Content** > **Use cases**.
3. Select **Unsupported language reply**.
4. Select the **Settings** tab.
5. Select **Prevent triggering the 'Unsupported language reply' when
   *active\_language* is set**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_unsupported_language_prevent_setting.png)
6. Click **Save**.
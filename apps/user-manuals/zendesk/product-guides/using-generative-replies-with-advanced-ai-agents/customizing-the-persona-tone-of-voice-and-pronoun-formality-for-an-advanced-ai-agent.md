# Customizing the persona, tone of voice, and pronoun formality for an advanced AI agent

Source: https://support.zendesk.com/hc/en-us/articles/8357758773658-Customizing-the-persona-tone-of-voice-and-pronoun-formality-for-an-advanced-AI-agent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

For each AI agent you create, you can define its individual persona, tone of voice, and
pronoun formality:

- **Persona** refers to the identity of an AI agent, or how it presents itself to
  your users. For example, does it interact with your users as a friendly peer, or
  more like a professional guide?
- **Tone of voice** refers to the type of language the AI agent uses when
  responding to users. For example, does it elaborate in its answers to users, or keep
  its responses short and to the point?
- **Pronoun formality** refers to whether your AI agent uses formal or informal
  pronouns when talking to a user. This applies only in languages that distinguish
  between formal and informal pronouns, such as German.

Note: Before you get started, see [Building an AI agent persona and tone of voice](https://support.zendesk.com/hc/en-us/articles/8357758777626) for
guidance on creating an AI agent that gives your users the best experience with your
brand.

This article contains the following topics:

- [Customizing an AI agent's persona](#topic_hps_snf_52c)
- [Customizing an AI agent's tone of voice](#topic_kzp_tnf_52c)
- [Customizing an AI agent's pronoun formality](#topic_qt2_5nf_52c)

Related articles:

- [Best practices for using instructions and custom
  tone of voice to influence advanced AI agent responses](https://support.zendesk.com/hc/en-us/articles/8719119396506)
- [Using instructions to influence advanced AI agent
  responses](https://support.zendesk.com/hc/en-us/articles/8357749291290)

## Customizing an AI agent's persona

You can customize an AI agent's persona to control its identity, or how it presents
itself to your users.

**To customize an AI agent’s persona**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Personalization**.
3. On the Identity tab, in **AI agent name**, enter the same name that you
   used when you created the AI agent.

   This name is shown to your users in
   the widget.
4. In **Company name**, enter the name of your company.

   This is how the AI
   agent knows what company it works for, if a user asks it.
5. In **Business profile**, enter one or two short, factual sentences in
   English that describe what your company does.

   This information gives the
   AI agent context so that it can give the most appropriate responses.
   Keep this description focused on simple text about your company's
   business domain, rather than marketing-focused material that could
   potentially influence your AI agent's behavior.

   Note: Make sure not to add instructions for the AI
   agent to the business profile, which might lead to unexpected
   errors.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_personalization_identity_tab.png)
6. Click **Test** to open a test window on the right, where you can get an
   idea of how these options affect the AI agent’s responses before proceeding.
7. Click **Save**.

## Customizing an AI agent's tone of voice

You can customize an AI agent's tone of voice to control the AI agent’s style of
communication.

**To customize an AI agent's tone of voice**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Personalization**.
3. Select the **Tone of voice** tab.
4. Select a tone:
   - **Professional**: (Default) A patient and informative tone.
   - **Informal**: A casual and friendly tone.
   - **Enthusiastic**: An enthusiastic and conversational tone.
   - **Custom**: A custom tone created from scratch or an edited
     version of one of the tones above.

     If you select this option,
     write a short **Tone description** that tells the AI agent
     how to speak to users. For example, “You maintain a polite,
     approachable, and conversational tone throughout the
     conversation.”
5. In **Answer length**, select one of the following options to configure
   the approximate length of each of the AI agent’s responses when it consults
   a [knowledge source](https://support.zendesk.com/hc/en-us/articles/8357749301658):
   - | For messaging AI agents | For email AI agents |
     | - **Short (30–60 words)** - **Medium (60–90 words)** - **Long (90–120 words)** - **Very Long (120–150 words)** | - **Short (150 words)** - **Medium (300 words)** - **Long (600 words)** - **Very Long (Unlimited word count)** |

     Note: These options affect only responses
     where the AI agent consulted a knowledge source. The appropriate
     lengths of conversational responses are left up to the AI agent.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_personalization_tone_of_voice_tab.png)
6. Click **Test** to open a test window on the right, where you can get an
   idea of how these options affect the AI agent’s responses before proceeding.
7. Click **Save**.

## Customizing an AI agent's pronoun formality

You can customize an AI agent's pronoun formality to control whether your AI agent
uses formal or informal pronouns when talking to a user.

**To customize an AI agent's pronoun formality**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Personalization**.
3. Select the **Pronoun formality** tab.
4. For each [supported language you’ve added](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_rmc_kzx_jgc),
   select either of the following options:
   - **Use formal pronouns**: Selected by default. AI agents use
     formal pronouns, conveying respect, when communicating with users in
     the specified language.
   - **Use informal pronouns**: AI agents use informal pronouns,
     conveying familiarity, when communicating with users in the
     specified language.

     For languages that don’t distinguish between
     formal and informal pronouns (for example, English), neither
     option is selectable.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_personalization_pronoun_formality_tab.png)
5. Click **Test** to open a test window on the right, where you can get an
   idea of how these options affect the AI agent’s responses before proceeding.
6. Click **Save**.
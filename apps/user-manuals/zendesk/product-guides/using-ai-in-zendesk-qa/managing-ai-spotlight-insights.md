# Managing AI spotlight insights

Source: https://support.zendesk.com/hc/en-us/articles/9483275885466-Managing-AI-spotlight-insights

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

AI spotlight insights help you manage conversation quality by highlighting key events for review. Customize predefined insights like "Dead air" and "Recording disclosure missing" to fit your needs. You can edit, activate, deactivate, or delete these insights to control which conversations are analyzed. This feature supports better quality assurance by focusing on important conversation aspects.

Location:  Zendesk QA > Settings > AI

In Zendesk QA, spotlight provides insights into the quality of your conversations
and helps you handpick critical conversations for manual review. It automatically surfaces
newly synced closed conversations with various [out-of-the-box insights](https://support.zendesk.com/hc/en-us/articles/7043759586074) to help you identify specific events or
signals for further analysis.

Admins and account managers can customize spotlight’s predefined voice insights and
edit the insights they have created.

This article contains the following topics:

- [Customizing predefined spotlight
  insights](#topic_hvj_hvh_xdc)
- [Editing custom spotlight
  insights](#topic_yq5_st4_q2c)
- [Activating a spotlight](#topic_ycy_vrm_nfc)
- [Deactivating a spotlight](#topic_hm4_fcn_nfc)
- [Deleting a spotlight](#topic_tyq_fcn_nfc)

Related articles

- [Understanding spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074)
- [Creating AI prompt-based spotlight insights](https://support.zendesk.com/hc/en-us/articles/9327313916570)

## Customizing predefined spotlight insights

You can customize the following predefined spotlight insights:

- **[Dead
  air](#topic_hvj_hvh_xdc__dead_air_customize)**: Analyzes moments of dead air in voice conversations that last longer
  than the set threshold. The default industry threshold is 30 seconds, but it can be
  adjusted to any duration.
- **[Recording disclosure missing](#topic_hvj_hvh_xdc__recording_disclosure_customize)**: Automatically identifies voice
  calls lacking the mandatory disclosure statement, such as 'This call will be recorded.' It
  uses a large language model (LLM) to dynamically understand context, eliminating the need
  for preset phrases. [LLM-based AutoQA](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) must be enabled for the Recording
  disclosure missing spotlight to function.

**To customize the Dead air spotlight insight**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Under **Usage** select **Spotlight** to display a list of all your
   spotlights.
5. Click the **Dead air** spotlight insight to open it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_AI_spotlight_edit.png)
6. Select whether the rule applies to **All conversations** or **Specific
   conversations**.

   If you select specific conversations, you must select which of the
   following conversations the insight applies to:

   - Call direction: [inbound](https://support.zendesk.com/hc/en-us/articles/4408821359002) or [outbound](https://support.zendesk.com/hc/en-us/articles/4408836235162)
   - [Conversation brand](https://support.zendesk.com/hc/en-us/articles/4408829476378)
   - [Conversation channel](https://support.zendesk.com/hc/en-us/articles/4408824097050)
   - [Escalation](https://support.zendesk.com/hc/en-us/articles/7043759586074-Using-Zendesk-QA-Spotlight-insights-to-filter-conversations#topic_gst_d1g_zdc)
   - [Help desk tag](https://support.zendesk.com/hc/en-us/articles/4408881573658)
   - [Language](https://support.zendesk.com/hc/en-us/articles/7043759449114-Finding-conversations-to-review-using-custom-filters#h_4e27ce74b3)
   - [Sentiment](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_u4j_rth_xdc)
   - [Source type](https://support.zendesk.com/hc/en-us/articles/7043759449114#h_4e27ce74b3)
7. Define the maximum **Dead air** threshold for your calls in seconds.
8. Click **Save changes**.

**To customize the Recording disclosure
missing spotlight insight**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Under **Usage** select **Spotlight** to display a list of all your
   spotlights.
5. Click the **Recording disclosure missing** spotlight insight to open it.
6. Select whether the rule applies to **All conversations** or **Specific
   conversations**.

   If you select specific conversations, you must select which of the
   following conversations the insight applies to:

   - Call direction: [inbound](https://support.zendesk.com/hc/en-us/articles/4408821359002) or [outbound](https://support.zendesk.com/hc/en-us/articles/4408836235162)
   - [Conversation brand](https://support.zendesk.com/hc/en-us/articles/4408829476378)
   - [Conversation channel](https://support.zendesk.com/hc/en-us/articles/4408824097050)
   - [Escalation](https://support.zendesk.com/hc/en-us/articles/7043759586074-Using-Zendesk-QA-Spotlight-insights-to-filter-conversations#topic_gst_d1g_zdc)
   - [Help desk tag](https://support.zendesk.com/hc/en-us/articles/4408881573658)
   - [Language](https://support.zendesk.com/hc/en-us/articles/7043759449114-Finding-conversations-to-review-using-custom-filters#h_4e27ce74b3)
   - [Sentiment](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_u4j_rth_xdc)
   - [Source type](https://support.zendesk.com/hc/en-us/articles/7043759449114#h_4e27ce74b3)
7. Click **Save changes**.

## Editing custom spotlight insights

You can also edit the [spotlight insights you have created](https://support.zendesk.com/hc/en-us/articles/9327313916570).

**To edit your spotlight insights**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Under **Usage** select **Spotlight** to display a list of all your
   spotlights.
5. Click the name of the spotlight insight you want to edit.
6. Select whether the rule applies to **All conversations** or **Specific
   conversations**.

   If you select specific conversations, you must select which of the
   following conversations the insight applies to:

   - Call direction: [inbound](https://support.zendesk.com/hc/en-us/articles/4408821359002) or [outbound](https://support.zendesk.com/hc/en-us/articles/4408836235162)
   - [Conversation brand](https://support.zendesk.com/hc/en-us/articles/4408829476378)
   - [Conversation channel](https://support.zendesk.com/hc/en-us/articles/4408824097050)
   - [Escalation](https://support.zendesk.com/hc/en-us/articles/7043759586074-Using-Zendesk-QA-Spotlight-insights-to-filter-conversations#topic_gst_d1g_zdc)
   - [Help desk tag](https://support.zendesk.com/hc/en-us/articles/4408881573658)
   - [Language](https://support.zendesk.com/hc/en-us/articles/7043759449114-Finding-conversations-to-review-using-custom-filters#h_4e27ce74b3)
   - [Sentiment](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_u4j_rth_xdc)
   - [Source type](https://support.zendesk.com/hc/en-us/articles/7043759449114#h_4e27ce74b3)
7. Click **Save changes**.

## Activating a spotlight

A spotlight marked as inactive is not surfacing newly synced closed
conversations. To allow it to automatically analyze conversations, it must be marked as
active.

**To mark a spotlight as active**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Under **Usage** select **Spotlight** to display a list of all your
   spotlights.
5. Next to the spotlight you want to activate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_horizontal.png)) and select **Mark as active**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_spotlight_mark_active.png)

## Deactivating a spotlight

A spotlight marked as active currently surfaces newly synced closed
conversations. Marking a spotlight as inactive stops it from automatically analyzing
conversations. However, inactive spotlights remain available for reporting and
filtering.

**To mark a spotlight as inactive**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Under **Usage** select **Spotlight** to display a list of all your
   spotlights.
5. Next to the spotlight you want to deactivate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_horizontal.png)) and select **Mark as inactive**.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_spotlight_mark_inactive.png)

## Deleting a spotlight

Deleting spotlights is permanent and erases all spotlight data from reporting.
Once deleted you can't restore the spotlight or its data.

**To delete a spotlight**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Under **Usage** select **Spotlight** to display a list of all your
   spotlights.
5. Next to the spotlight you want to delete, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_horizontal.png)) and select **Delete**.
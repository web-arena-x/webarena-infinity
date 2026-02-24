# Turning on suggested macros

Source: https://support.zendesk.com/hc/en-us/articles/4408824813722-Turning-on-suggested-macros

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

Suggested macros use AI to recommend relevant macros based on past ticket data, helping you quickly resolve customer requests. You can enable this feature if your account has sufficient macro usage data.

Location:  Admin Center > Workspaces > Agent tools > Macros

Suggested macros are AI-powered suggestions that help agents find the right macros to apply to the tickets they’re currently working on. These suggestions are based on macros that were applied to similar tickets in the past, and are intended to help agents resolve the customer’s request more quickly.

This article contains the following topics:

- [About suggested macros](#id_mkx_hk3_xcc)
- [Turning suggested macros on or off](#topic_ktj_hlv_hrb)

Related articles:

- [Applying suggested macros to tickets](https://support.zendesk.com/hc/en-us/articles/4408826078362)
- [Organizing and managing macros](https://support.zendesk.com/hc/en-us/articles/4408884166554)
- [Macros resources](https://support.zendesk.com/hc/en-us/articles/4408824631578)

## About suggested macros

Suggested macros are shared macros that have been identified through an AI-powered analysis of your macro usage data. Using machine learning, an algorithm analyzes the text in the ticket's subject and comments. It then compares them to those used in tickets that were created in the last nine months, where a macro was applied.

The ticket must be from an email, webform, Web Widget, API, Mobile SDK, or [Channel framework](https://developer.zendesk.com/documentation/channel_framework/) channel. Only [shared](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_zh2_4nw_4y) macros that an agent has access to are suggested; [personal](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_zdw_nnw_4y) macros are never suggested.

Up to three suggested macros appear at the top of the macros list in the ticket interface.

For more information about the agent workflow, see [Applying suggested macros to tickets](https://support.zendesk.com/hc/en-us/articles/4408826078362).

## Turning suggested macros on or off

Suggested macros are off by default. You can turn on suggested macros only when the account includes enough data about past macro usage. Your account must include at least 100 tickets that were created within the last nine months in a [supported channel](#id_mkx_hk3_xcc) and had a shared macro applied. In addition, at least three of the shared macros in the account need to have been used at least once on tickets that were created in the last nine months.

If the account doesn’t include enough macro usage data, you will need to create and use more [shared](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_zh2_4nw_4y) macros, more frequently, and over a period of time, before you can turn on suggested macros. When you create a new macro, it takes two weeks to be included in the suggested macros machine learning model for analysis.

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can turn suggested macros on or off. You can find information about [supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01K20K8XP6BTZP9ZMCW3CRZCJN) for suggested macros in the Zendesk language support article.

**To turn suggested macros on or off**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. On the **Macros** page, click **Actions** > **Manage settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_consolidated_settings_manage.png)
3. On the **Manage settings** page, select or deselect the **Display suggested macros** option to turn it on or off.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/macros_consolidated_settings_suggested.png)

   This is an account-wide setting, not individual. Turning the option on or off will affect all admins and agents on the account.
4. Click **Save**.
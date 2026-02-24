# Editing and managing intents

Source: https://support.zendesk.com/hc/en-us/articles/9488233422746-Editing-and-managing-intents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

As part of [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_ebn_l4g_htb), your account includes a
prebuilt list of default intents specific to your industry that predict what a ticket is
about. To address your specific business needs, you might also [create custom intents](https://support.zendesk.com/hc/en-us/articles/8718789695002) or [accept suggestions for new intents](https://support.zendesk.com/hc/en-us/articles/9484697389210) that intelligent triage
provides based on your ticket data.

You can edit and manage default intents, suggested intents, and any custom intents you
create by editing names and descriptions. Intents can also be deactivated and activated
as needed.

To manage any duplicate or overlapping intents, see [Resolving intent conflicts](https://support.zendesk.com/hc/en-us/articles/9484697389210#topic_kwc_gtn_yhc).

This article contains the following topics:

- [Editing intent names and
  descriptions](#topic_qbn_ln3_fzb)
- [Restoring an intent name to its
  default value](#topic_tnb_lqp_zfc)
- [Deactivating or activating
  intents](#topic_oq2_hc4_32c)

Related articles:

- [Accessing and viewing intelligent triage
  intents](https://support.zendesk.com/hc/en-us/articles/9488234915610)
- [Automatically detecting customer intent,
  language, and sentiment](https://support.zendesk.com/hc/en-us/articles/4550640560538)

## Editing intent names and descriptions

You can edit an intent’s name or description in any supported language to better
reflect the terminology preferred by your organization.

Intelligent triage continues to detect tickets based on the original intent, even
after its been edited. Because of this, you should only edit intent names to make
small adjustments to an intent’s terminology, not updates that completely change the
meaning of an intent.

Keep in mind that when you edit an intent name, the edit intent's name isn't updated
in any of your existing [ticket triggers](https://support.zendesk.com/hc/en-us/articles/440889354588https://support.zendesk.com/hc/en-us/articles/4408893545882) that use the
"Ticket>Intent" condition.

**To edit an intent name or description**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. (Optional) Change the language by clicking **Actions** > **View language**
   and select the language you want to edit intents for.
3. Browse, search, or filter the list to [find the intent](https://support.zendesk.com/hc/en-us/articles/9488234915610#topic_l3b_hn3_fzb) you want to edit.
4. Hover your mouse over the intent, click the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) icon, and select **Edit intent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ai_hub_intents_manage.png)
5. Update the **Name** or **Description** of the intent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ai_hub_intents_manage_edit.png)
6. Click **Save changes**.

   The intent is automatically marked with an Edited
   label to let you know that it has been changed from its original
   name.

## Restoring an intent name to its default value

If needed, you can also restore an edited intent's name to its default name.

**To restore an intent name to its default value**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. Browse, search, or filter to [find the intent](https://support.zendesk.com/hc/en-us/articles/9488234915610#topic_l3b_hn3_fzb) you want to
   restore.
3. Click the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) icon, and select **Restore default
   name**.

## Deactivating or activating an intent

You can deactivate both default and [custom intents](https://support.zendesk.com/hc/en-us/articles/8718789695002#topic_b1s_pyn_32c) that aren’t useful for your
account anymore.

Zendesk may deactivate intent values if the intent is no longer available
or relevant to your account. Intent values may also be reactivated by Zendesk if
they become relevant again.

You can reactivate intents values as needed but can’t reactivate intents
that were deactivated by Zendesk.

When you deactivate an intent or Zendesk deactivates an intent, the intent
will no longer be detected in new tickets. If you have any business rules, such as
triggers, view or automations, that are based on the deactivated intent, they will
stop working. Deactivated intents still appear in Explore reports.

At least one default intent must remain active.

**To deactivate or activate an intent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. Browse or search to find the intent you want to deactivate or activate.
3. Hover your mouse over the intent, click the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) icon, and select **Activate** or
   **Deactivate**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ai_hub_intents_manage.png)
4. Confirm your selection by clicking either **Activate intent** or
   **Deactivate intent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intents_deactivate_confirmation.png)

   The intent’s status is
   updated in the intent list. Deactivated intents are labeled “Inactive”. If
   you’ve activated an intent, the “Inactive” label is removed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intents_list_system_inactive.png)
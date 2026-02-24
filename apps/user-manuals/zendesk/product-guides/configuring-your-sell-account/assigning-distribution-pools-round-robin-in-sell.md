# Assigning distribution pools (round robin) in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408823875354-Assigning-distribution-pools-round-robin-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Suite Professional plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_suite_pee.png)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

You can assign a [distribution pool](https://support.zendesk.com/hc/en-us/articles/4408839201178) anywhere in Sell that you assign an owner for a lead, contact, or deal.

This article covers the following topics:

- [Assigning a distribution pool to a single lead, contact, or deal](#topic-1__topic_ncq_djx_vjb)
- [Assigning a distribution pool for imported leads, contacts, or deals](#topic-1__section_on3_3m4_xjb)
- [Assigning a distribution pool in the Lead Capture Form](#topic-1__section_pc5_q34_xjb)
- [Assigning a distribution pool during lead conversion](#topic-1__section_m3g_pw4_xjb)
- [Assigning a distribution pool using a Smart List](#topic-1__section_ocp_y4v_zjb)
- [Assigning a distribution pool for integrations](#topic-1__section_mzp_wmv_zjb)

## Assigning a distribution pool to a single lead, contact, or deal

If you have rights to reassign objects, you can edit a specific lead, contact, or deal to assign them to a user in the distribution pool.

**To allocate a distribution pool to a single lead, contact, or deal**

1. On the sidebar, click the **Lead**, **Contact**, or **Deal** icon.
2. Click **Edit** for an existing lead, contact, or deal, or **Add** for a new lead, contact, or deal.
3. In the **Owner** field, click the distribution pool name (instead of a user name).
4. Click **Save**.

   Note: You'll only see a distribution list is if relates to the correct record type. For example, a leads distribution pool is visible only in the leads page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_dist_assign_single.png)

   The lead, contact, or deal is assigned to the next user in the distribution pool.

## Assigning a distribution pool for imported leads, contacts, or deals

When you import leads, contacts, or deals using a CSV file, you can specify a distribution pool as the owner. This ensures all imported records are distributed evenly in a team.

**To assign a distribution pool when importing leads, contacts, or deals**

1. On the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Data > Import](https://app.futuresimple.com/settings/imports)**.
2. Import your CSV file (see [Importing leads, contacts, or deals](https://support.zendesk.com/hc/en-us/articles/4408845638298)).
3. In the **Owner** field, ensure you specify the distribution pool name as the Sell lead, contact, or deal owner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_dist_assign_import.png)

   When the import has been processed, each imported lead, contact, or deal is assigned, in order, to the users in the distribution pool.

## Assigning a distribution pool in the Lead Capture Form

You can specify a distribution pool in the [Lead Capture Form](https://support.zendesk.com/hc/en-us/articles/4408832077338), so that any leads contacting you using a web-based form are assigned using the round-robin method.

**To assign a distribution pool in the Lead Capture Form**

1. On the Sell sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Tools > Lead Capture Form](https://app.futuresimple.com/settings/lead_capture_form)**.
2. Click **Assign leads to**.
3. Click the lead distribution pool name (instead of a user name).
4. Click **Save**.

   When each new lead is captured, it is assigned, in order, to the users in the distribution pool.

## Assigning a distribution pool during lead conversion

You can specify a contact distribution pool when you convert a lead.

Alternatively, if there is an associated deal, you can use either a contact or deal distribution pool. Both the contact and the deal are assigned to the same user in the distribution pool.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_dist_assign_convert.png)

**To assign a distribution pool during lead conversion (contact only)**

1. On the Sell sidebar, click the **Leads** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)), then select the lead page that you want to convert.
2. Click **Convert**.
3. In the **Owner** field, select the contact distribution pool name. Deselect **Create a deal for this converted lead**.
4. Click **Convert**.

   The lead is converted and the new contact is assigned to the next user in the distribution pool.

**To assign a distribution pool during lead conversion (contact and deal)**

1. On the Sell sidebar, click the **Leads** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)), then select the lead page that you want to convert.
2. Click **Convert**.
3. In the **Owner** field, select the contact or deal distribution pool name. Ensure that **Create a deal for this converted lead** is selected.
4. Enter a deal name and optionally a pipeline. The default setting is to use the lead's name as the deal name.
5. Click **Convert**.

   The lead is converted and the new contact and associated deal are assigned together to the next user in the distribution pool.

## Assigning a distribution pool using a Smart List

You can specify a distribution pool as the owner for all the records in any Smart List that you have created. This provides a powerful way to reassign ownership for a large, customized group of records.

**To assign a distribution pool using a Smart List**

1. On the Sell sidebar, click the **Lead**, **Contact**, or **Deal** page that contains the Smart List you want to work with.
2. Click the **Working Center** view and click your Smart List. If you need to set up a new Smart List, see [Using Smart Lists](https://support.zendesk.com/hc/en-us/articles/4408827735066).
3. Select the Smart List (click the check box in the toolbar).
4. Click **Reassign Owner**.
5. The Reassign Owner window appears. Select the distribution pool to reassign ownership for the records in the Smart List.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_distribution_smartlist.png)
6. Click **Reassign**.

   Each record in the Smart List is assigned, in order, to the users in the distribution pool.

## Assigning a distribution pool for integrations

For any integrations that you have enabled for your account, for example, Hubspot, Zapier, Zendesk Chat, or Zendesk Support, you can specify a distribution pool as the owner. For example, in Zendesk Support, this would be the owner of a new lead that is created by a Support agent, and assigned in Sell.

**To assign a distribution pool for integrations**

1. On the Sell sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. For the enabled integration, click **Settings**.

   Note: If the integration is disabled, you won't see the Settings button.
3. If there is the possibility to assign an owner for that integration, you can specify the distribution pool as the assigned owner.

   For example, in an enabled Zendesk Support integration, you can set assign owner to a chosen distribution pool:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_distribution_integration.png)

   When each new lead is captured, it is assigned, in order, to the users in the distribution pool.
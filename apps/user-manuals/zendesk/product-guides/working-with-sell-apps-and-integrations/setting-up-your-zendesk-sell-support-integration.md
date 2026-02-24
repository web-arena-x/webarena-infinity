# Setting up your Zendesk Sell-Support integration

Source: https://support.zendesk.com/hc/en-us/articles/4408828146586-Setting-up-your-Zendesk-Sell-Support-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

![Available on all Support plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_all.png)

You can configure the Sell-Support integration to access support tickets in Sell, and to see Sell data from your Support interface. To learn more about the features of having a Sell-Support integration, see [About integrating Sell and Support for an overview of customer communication in your company](https://support.zendesk.com/hc/en-us/articles/4408833438746).

This article covers the following topics:

- [Prerequisites](#topic_q2d_n3w_2nb)
- [Setting up the Sell-Support integration](#topic_npt_n3w_2nb)
- [Further configurations](#topic_rlm_bgv_w4b)

Related articles:

- [Customizing the data fields displayed by the Zendesk for Support app](https://support.zendesk.com/hc/en-us/articles/4408821766938)
- [Working with the Zendesk Sell app in Support](https://support.zendesk.com/hc/en-us/articles/4408831980314)
- [Setting up the Zendesk Sell-Chat integration](https://support.zendesk.com/hc/en-us/articles/4408831757210)

## Prerequisites

Ensure the following is set up prior to your integration:

- You have a Sell account that is a Zendesk account (see [Connecting your legacy Sell account to the Zendesk platform](https://support.zendesk.com/hc/en-us/articles/4408835851162-Migrating-your-Sell-account-to-Zendesk)).
- Your Sell and Support accounts are on the same Zendesk subdomain.
- You have Support admin rights to install the Sell app in Support and grant Sell users permission to tickets. Anyone with admin rights in Support can set up your Zendesk Sell-Support integration.
- You have Sell admin rights, so you can: enable tickets in Sell, set up access to Sell information in Support, and carry our any further configurations.

## Setting up the Sell-Support integration

If you have met the prerequisites, then you can start configuring your integration between Sell and Support so you can view Support tickets in Sell and display Sell data in Support. You also need to grant permission to your Sales team and add them to groups so they can access tickets.

**To enable the Sell-Support integration and add users to groups**

1. In Sell, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. Select the **Zendesk Support** integration, and click **Enable**.
3. To right of **View Support tickets in Sell**, click **Enable**, then in the **Support tickets in Sell** dialog, click **Enable**..
4. (Optional) Click **Add users to groups**. This will take you to Support where you can enable users to access tickets (see [Understanding ticket permissions for Sell users](https://support.zendesk.com/hc/en-us/articles/4408833438746#topic_j2k_hw3_2nb)).
5. (Optional) To drag the **Tickets in Support** widget to a more prominent position on your Lead, Contact, and Deal cards, go to **Layouts** and click **Change location**.

**To install the Sell app in Support**

1. Go to **View Sell information in Support**, and click **Learn more**, or go [directly to Zendesk Marketplace](https://www.zendesk.com/apps/support/zendesk-sell/) to install the **Zendesk Sell** app for Support:
   1. Click **Install**, then confirm or fill in your Support subdomain and click **Install**.
   2. Check if the app and installation details are correct, then click **Install**.
2. Click the **Zendesk products tray** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/product_tray_icon.png)) in the top bar, and click the **Sell** icon to return to Sell.
3. To allow Support Agents to see the leads, contacts, and deals data in Support, and to ensure the Sales team can see leads that have been created in Support, continue on to further configuring the app.

Congratulations, you have now set up the integration between the [Zendesk Sell app and Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408831980314).

## Further configurations

To configure additional settings, go to **Integrations** > [**Zendesk Support Integration** > **Sell app in Zendesk Support - Installed**](https://app.futuresimple.com/settings/integrations/support). There you can configure additional settings. Any changes you make are automatically saved.

**To configure a Support agent's access to Sell data**

- Under **Access to Sell information in Support**, specify who can access leads, contacts, and deals in Support. Choose from:
- - **Only Sell users have access** - this means that only Support agents who have access to Sell will see Sell information in Support. Specifically, they can only see Sell data in Support that they have access to in Sell.
 - **All agents have access** - this means all Support agents (regardless of whether they have access to Sell), will see the data for Sell leads, contacts, and deals in the Sell app in Support.

![Agent access to Sell data](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_agent_access_to_sell_data.png)

**To configure how Agents create leads**

- In **Assign Status**, you can set the status of the lead that is assigned to a lead through the Sell app in Support. You can make changes to the default statuses under the [Lead Status](https://app.futuresimple.com/settings/leads/lead-status) tab.
- In **Assign Source**, if you have [lead sources](https://app.futuresimple.com/settings/leads/lead-sources) set up for your account, you can select the lead source that is set when you create a lead from a Support ticket. You can also create a new lead source by entering the source name into input field of the dropdown menu.
- In **Assign Owner**, you can select the Sell users, or distribution pools (if available). Agents can choose these in the Sell app while creating leads.
 - You can allocate a lead to any owner in your organization. You can also specify multiple owners, distributions, or a combination of both. During lead creation agent are asked to choose who the lead should be assigned to.

    ![Sell-Support assign suggested](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_assign_suggested.png)

    Note: If you have several sales teams, you want to ensure leads are assigned to the right people so the reps can act on them immediately. You also want to avoid time-consuming triage. To do this, [create several lead distributions](https://support.zendesk.com/hc/en-us/articles/4408839201178) with names that are easy to understand by your Support agents, then assign people to those distributions and specify those distributions as possible lead owners in the integration settings.
 - If you want agents to have full control over assigning leads in the Support app, select the **Allow agents to assign any owner** check box. This means that in the app, the agent will have a list of all available Sell users and distributions that they can assign the lead to.
 - If you leave the **Owner** field empty, then the lead ownership will rely on how you’ve configured the Support agents to access Sell data until the checkbox **Allow agents to assign any owner** is selected, for example:
    - If you selected **Only Sell users have access**, the lead will be assigned to the user who created the lead.
    - If you selected **All agents have access**, the lead will be assigned to the topmost manager, (the person name displayed in the settings).![Sell-Support owner field with distribution](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_owner_field_with_distributions.png)

 Note: If only one owner (a Sell user or distribution) is selected in the Assign Owner field, then you won't see a dropdown menu here. Instead, leads will be automatically assigned to the owner selected in Sell settings.

 **To configure data that the Sell app displays in Support**

 - Click **Field Configuration** at the bottom of the page (see [Customizing the data fields displayed by the Zendesk Sell for Support app](https://support.zendesk.com/hc/en-us/articles/4408821766938)).
# Customizing your Sell-Support integration

Source: https://support.zendesk.com/hc/en-us/articles/4408819763866-Customizing-your-Sell-Support-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You must have Sell and Support to use this integration.

With your Sell-Support integration, there are a couple of things you can customize. You can change the position of the widget for tickets in Sell and you can adjust your workflows in Support to ensure tickets created from Sell end up in the right place.

This article covers the following topics:

- [Configuring the widget panel](#sell_Customizing_your_sell_support_integration__h_01EPCJ6H69ZN4R95NV945686AQ)
- [Customizing your workflow for Support tickets created from Sell](#sell_Customizing_your_sell_support_integration__h_01EPCM00ZFSR9CMP6R25S6NK40)

## Configuring the widget panel

To configure the widget panel, you must first check the group permissions for contributors.

### Checking contributer permissions

Improve the workflow for your contributors by ensuring they are assigned to the right groups and can view all of the tickets assigned to them from those groups.

**To check if a contributor is assigned to the right groups**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Groups**.

You also want to ensure that all new tickets end up in the proper group so your agents can see them.

### Customizing the layout of your widget panel

After integrating Sell and Support, you can customize the position of the widget on the lead, contact, or deal (object) card. It is useful to add the widget panel to the top of the object card, so your sales reps can easily access their Support tickets from the Sell interface.

**To customize the widget position on your object card**

1. In Sell, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to [**Customize > Layouts**](https://app.futuresimple.com/settings/layout).
2. Choose the layout you want to modify by clicking on the tab, for example **Leads**.

   For this example, we are modifying the widget panel for Leads. It is exactly the same procedure to change the widget panel for People, Companies, and Deals.
3. In the **Widget panel** section, drag and drop the **Tickets in Support widget**.

   On the widget panel, you can drag and drop each widget up and down into an order that works best for your workflow.
4. To the right of **Widget panel**, click **Save**.

Now you can view your Support tickets in Sell.

## Customizing your workflow for Support tickets created from Sell

The Sell-Support integration allows you to create tickets in Support and view them in Sell. To optimize this for your workflow, you must configure the groups to ensure they are being sent the appropriate tickets, and configure the notifications to the requestor so they can keep up to date on the progress of the ticket.

**To ensure the tickets are available in proper groups**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click **Create trigger**.
3. Enter a name for the trigger.
4. In **Conditions**, enter the following conditions:
   - **Status** | **Is** | **New**
   - **Tags** | **Contains at least one of the following** | **ticket\_from\_sell**

   ![Sell trigger conditions.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_Trigger_conditions.png)
5. In **Actions**, choose the appropriate conditions from the drop-down menus.

   ![Sell trigger actions.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_Trigger_actions.png)
6. Click **Create**.

   By default the requester of a ticket (your customer), does not get notifications about the ticket. So if you want to enable email notifications for the requester, you will need to create a trigger for that.

   Note: Before creating a new trigger, check that no other trigger has been set up for the conditions you are defining.

**To create a trigger to enable notifications for the requester**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click **Create trigger**.
3. Enter a name for the trigger.
4. In **Conditions**, enter the following conditions.
   - **Status** | **Is** | **New**
   - **Tags** | **Contains at least one of the following** | **ticket\_from\_sell**

   ![Sell trigger conditions.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_Trigger_conditions.png)
5. In **Actions**, choose the appropriate email user and requester from the drop-down menus, and enter the subject and content of your email.

   ![Sell trigger actions for the requester.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_Trigger_requester_actions.png)
6. Click **Create**.
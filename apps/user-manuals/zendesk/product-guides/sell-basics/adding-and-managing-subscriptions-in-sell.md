# Adding and managing subscriptions in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4413953731354-Adding-and-managing-subscriptions-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Note: You must be an admin to activate this feature.

In Sell, you can use the subscriptions feature to have greater visibility over your subscriptions. For example, you can see whether a subscription has expanded or contracted since the customer's last subscription period and see the subscription end date for the current and upcoming monthly recurring revenue (MRR) of a subscriber. Subscriptions also provides greater insight into total MRR for sales reps.

This article covers the following topics:

- [Adding a new subscription record](#topic_inx_v3n_zrb)
- [Changing and editing an existing subscription](#topic_omw_5sw_prb)
- [Creating a subscriptions smart list](#topic_qgv_z3w_prb)
- [Understanding subscriptions tags](#topic_esf_4d4_rsb)
- [Removing a subscription record](#topic_ewb_lw5_rrb)

Related article:

- [Activating and deactivating subscriptions in Sell](https://support.zendesk.com/hc/en-us/articles/4413961610266)

## Adding a new subscription record

Before you can add a new subscription record, you must first [activate the subscriptions feature](https://support.zendesk.com/hc/en-us/articles/4413961610266), then you can get started with Sell subscriptions by adding a new subscription record to an existing contact.

**To add a new MRR record**

1. On the sidebar, click **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), then open the contact you want to add a subscription to.
2. On the right side, in the **Subscription** widget, click **Add** (**+**) to add a subscription for your customer.

   ![Sell add new subscription](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_create.png)
3. In **Add subscription**, enter the details of the customer's subscription, including the currency and monthly billing amount, when you want the subscription period to begin and end and a description of what type of subscription it is (for example a yearly renewable or ongoing subscription).

   ![Sell add subscription](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_add.png)

   The subscription details are immediately visible on the contact's record.

## Changing and editing an existing subscription

After you've created a subscriptions smart list of your contacts, it's good practice to check the subscription widget on a contact page to ensure the subscription details are correct. You can always change the MRR of a subscription to update its monetary value for the next subscription period, or edit the details of the current subscription in the subscription widget.

**To change the upcoming MRR of a subscription**

1. On the sidebar, click **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), then open the contact whose subscription you want to renew or edit.
2. On the **Contact** page, in the **Subscription** widget, you can see the current MRR for that customer, click **Change**.

   ![Sell change or update subscription](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_updated.png)
3. In **Add subscription**, update the relevant details of the subscription in the following fields:
   - **Monthly value** - click the drop down menu and choose the currency you want the subscription to be in, then enter the amount of the monthly subscription.
   - **Effective date** - below this field you can see the end date of the previous subscription, click the **Calendar** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)) icon to choose the date you want the subscription to begin.
   - **End date** - select the radial button for when you want the subscription to finish:
     - **After a number of months** - enter the number of months the subscription is valid for.
     - **On a specific date** - click the Calendar icon to choose the date that you want the subscription to end.
     - **Never** - select this option if it is a long term or on-going subscription.
   - **Description** - enter any relevant information about the type of subscription it is, product type, MRR change type (for example, expansion or contraction).
4. Click **Save**.

   You can now see the updated MRR in the subscription widget on the contact's page, showing the start and end dates of the subscription as well as an expansion or contraction tag for the period that the change will occur.

**To edit the details of a subscription**

You can edit the subscription details in two ways:

1. On the **Contact** page, in the **Subscription** widget,
   1. Hover over the current MRR for that customer, and click the **Pencil** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_pencil.png)) icon.
   2. Or click the **Current MRR** value.

   ![Sell edit subscription details](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_edit.png)
2. In **Edit subscription**, you can update the value of the current monthly subscription, the begin and end dates for the subscription period, and add to the description of the current subscription. To delete the current subscription, click **Delete subscription period**.

   ![Sell edit current MRR](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/edit_subscription.png)

## Creating a subscriptions smart list

After you've activated the subscriptions feature, it's good practice to create a smart list of your subscribers so you can see in good time when their subscriptions are about to end, and if their subscription is increasing or decreasing.

**To create a smart list for your subscriptions**

1. On the sidebar, click **Contacts**.
2. On the **Contacts** page, click **+ Field**.
3. Scroll through the list and click to add the following columns:

   - **Current MRR**
   - **Upcoming MRR**
   - **Subscription end date**
4. At the top left of the page, click **Save as Smart List**.

   Note: If there is no upcoming MRR value added to the subscription information in the subscription widget, you will not see an upcoming MRR value on your smart list.

Now that you've created a smart list for the subscriptions of your customers, you can see the date when a customer's subscription ends. You can also export subscriptions smart lists, which is helpful for

- Seeing what the MRR is for a specific customer, so you know how much they're paying every month.
- Forecasting the total MRR in the current pipeline of a sales rep.
- Seeing how much a customer will still need to pay for the rest of their subscription (for example, as of today).
- Seeing the total MRR already accrued over a given period (see [Exporting a smart list](https://support.zendesk.com/hc/en-us/articles/4408832080666)), for example, you can see how much a specific customer has paid in total since their subscription begin date.

![Sell smart list subscription end date](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_smart_list_end_date.png)

## Understanding subscriptions tags

Subscriptions uses tags to make it easy for sales reps and managers to see at a glance the status of a subscription. The information that you enter into the details of each subscription is reflected in the tag that is automatically assigned to it.

- **New business** — tells you this is a new subscription.
- **Expansion** — the updated information added to the subscription shows that the MRR is increasing in value.
- **Contraction** — the updated information added to the subscription shows that the MRR is decreasing in value.
- **Renewal** — the updated information added to the subscription shows that the MRR is being renewed at the same value as the current subscription.
- **Reactivation** — this tag means that the MRR is a previously canceled subscription that is being reactivated.

You can see the status tags on the subscription widget.

![Sell subscriptions tags](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_tags.png)

## Removing a subscription record

As a sales rep, you can remove a subscription record from the subscription widget, so it's no longer visible on a Contact card.

**To remove a subscription record**

1. On the sidebar, click **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), then open the relevant contact.
2. On the **Contact** page, in the **Subscription** widget, you can see the records listed for that customer, click the click the **Trashcan** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) icon.
3. In the **Delete subscription period** dialog, click **Delete subscription period** to confirm that you want to delete it.

   ![Sell delete subscription](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_subscriptions_delete.png)
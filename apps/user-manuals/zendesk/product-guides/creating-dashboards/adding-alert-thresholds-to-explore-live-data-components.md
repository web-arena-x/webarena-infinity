# Adding alert thresholds to Explore live data components

Source: https://support.zendesk.com/hc/en-us/articles/4408823170842-Adding-alert-thresholds-to-Explore-live-data-components

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Enterprise |

With Explore, you can add live data to your dashboards using live data components. This lets you see information about your business in near-real-time. Additionally, you can use *threshold alerts* to change the color of your component when certain conditions are met, for example:

- Has the number of open tickets risen above 100?
- Are there more than five chats in the queue?
- Are more than ten callbacks awaiting a response?

In this article, you'll learn how to configure alert thresholds for your live data components. For more information about the available live data components, see [Live data components for Explore dashboards](https://support.zendesk.com/hc/en-us/articles/4408843357210).

## Configuring alert thresholds

In this section, you'll configure an alert threshold that changes the color of the **Chats in queue** live data component if the number of chats in the queue is more than one. You can substitute any live data component for this one.

**To configure the alert threshold**

1. In an Explore Enterprise dashboard, add the **Chats in queue** live data component. For help adding live data components, see [Adding live data and live filter components to dashboards](https://support.zendesk.com/hc/en-us/articles/4408846742042).
2. Click the **Chats in queue** component and then, from the options panel, select **Alerts** > **Add alert**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_updates_d10.png)
3. From the **Chart configuration** menu, choose **Alerts**.
4. On the **Alerts** menu, click **Add alert**.
5. Configure the **Alert level** to match your needs. In this example, you'll configure the operator **More than** and a value of **0** meaning if the number of chats is more than zero, the alert will change the color of the **Chats in queue** widget.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_updates_d11.png)

   The other available operators are **Less than** and **Equals**.
6. If required, click the **Background color** icon to change the alert threshold color.
7. Click back into the dashboard to close the menus. Now, whenever the alert threshold is triggered, the **Chats in queue** component changes color.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_alert_threshold_3.png)
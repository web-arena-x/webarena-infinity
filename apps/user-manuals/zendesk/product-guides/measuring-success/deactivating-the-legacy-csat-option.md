# Deactivating the legacy CSAT option

Source: https://support.zendesk.com/hc/en-us/articles/4408822875034-Deactivating-the-legacy-CSAT-option

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

You can disable legacy CSAT if you want to stop sending CSAT surveys or if you want to start using the [updated CSAT option](https://support.zendesk.com/hc/en-us/articles/7689997846554).
You must disable legacy CSAT before you can use the updated CSAT option. You can have only one CSAT option activated at any given time.

Deactivating the legacy survey also deactivates any default automations and triggers associated with legacy CSAT. If you have custom CSAT automations and triggers, you must manually deactivate those.

**To deactivate legacy CSAT**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. Click the **Satisfaction** tab, then deselect **Allow customers to rate tickets**.
3. Click **Save tab**.
4. If you have any custom automations and triggers that use the placeholders
   {{satisfaction.rating\_section}} or {{satisfaction.rating.url}} or that use the "Request messaging rating" action, you'll need to manually find and update or deactivate those.
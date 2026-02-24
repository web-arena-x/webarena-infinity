# Configuring agent statuses for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9791029724186-Configuring-agent-statuses-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Configure agent statuses to streamline status updates between systems. Although status changes in one system don't sync automatically with the other, you can set up and map agent statuses in both systems. This mapping allows you to manage your availability more effectively, ensuring that your status is consistent across platforms like Amazon Connect and the admin center.

Zendesk and Amazon Connect allow agents to change their status (from available to
offline, for example), however, updates made in Zendesk do not automatically sync with
Amazon Connect. Agents must manually update their status in both systems.

To streamline this process, you can configure agent statuses in Amazon Connect and
configure agent statuses in Zendesk, then map Zendesk statuses to the corresponding
Amazon Connect statuses.

**To configure and map agent statuses**

1. In Amazon Connect, select **Users > Agent status > Manage agent
   statuses**.
2. Set up agent statuses in Amazon Connect.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cont_cent_status_4.png)
3. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent
   statuses**.
4. Set up agent statuses in Admin Center (see [Creating custom unified agent
   statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cont_cent_status_3.png)
5. Map the Zendesk agent statuses to the Amazon Connect agent statuses.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cont_cent_status_2.png)
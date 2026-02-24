# Managing Zendesk phone lines

Source: https://support.zendesk.com/hc/en-us/articles/4408881907994-Managing-Zendesk-phone-lines

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

This article describes how to manage general settings for phone lines.

For details about managing line-specific settings, see [Managing individual line settings](https://support.zendesk.com/hc/en-us/articles/4408823877146).

For details about adding new lines, see [Adding Zendesk phone lines](https://support.zendesk.com/hc/en-us/articles/4408824192026).

This article contains the following sections:

- [Deleting a line](#topic_zrg_2dd_yt)
- [Recovering a number](#topic_sj2_kdd_yt)
- [Adding a failover number](#topic_fkr_j2d_yt)
- [Setting number priority (Professional and Enterprise)](#topic_nhq_4wy_11b)

## Deleting a line

You can delete an existing line if you don't want to use it anymore.

Note: You can't delete lines while you're on a trial.

**To delete a line**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Next to the line you want to delete, click the menu icon, then select **Delete**.
4. Click **Ok** to confirm that you want to delete the line.

## Recovering a number

Your Zendesk phone number is removed from your account when your trial expires, when your subscription is canceled, or when your account is suspended or deleted.

Within 72 hours, you can [contact Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to reinstate your number if you have resolved the issue with your account.

## Adding a failover number

In the event that service is unavailable, the failover feature can route all incoming calls to a pre-designated number so you can help your customers with minimal disruption.

With the Enterprise plan, if Zendesk is available to your end users but you are unable to access it (for example if you’re experiencing a localized internet outage), you can request to have failover manually initiated by [contacting Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850). Zendesk will manually initiate failover for you once a month.

Important: Failover can be enabled for a maximum of 24 Hours.

The failover number you choose:

- Must not be a Zendesk phone number.
- Must be able to handle your support call volume, as all incoming calls are routed to it.
- Is not restricted based on the location of your Zendesk phone number.
- Works only for incoming calls; outgoing calls do not have the ability to use the failover number.

Note: You must contact Zendesk to initiate failover. Failover cannot be initiated automatically.

**To add a failover number**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Next to the number you want to add a failover number for, click the menu icon, then select **Edit**.
4. Enter the number in the **Failover number** field on the **Settings** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_failover.png)

   Note: Failover numbers must be entered in e.164 format. For more information, see [What are the accepted phone number formats for Zendesk](https://support.zendesk.com/hc/en-us/articles/4408823756570-What-are-the-accepted-phone-number-formats-for-Talk-).
5. Click **Save changes**.

## Setting number priority (Professional and Enterprise)

On Professional and Enterprise plans, you can set certain phone numbers to be priority numbers, meaning calls received at these numbers will be sent to the front of the queue of available agents. For example, you might want to prioritize calls from actively subscribed customers over calls from trial users.

The list of phone numbers is sorted into priority numbers and all other numbers. You can also filter this list to show only priority numbers or other numbers.

**To filter the list of numbers**

- Click the drop-down list next to **All phone numbers** at the top of the list.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_filter_numbers.png)

 Select **Priority numbers** or **All other numbers** to filter the list accordingly.

**To set number priority**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Hover over the number you want to edit and select the check box that appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_priority_select_number.png)
4. Click **Set number priority** at the top of the list of numbers. Select either **Set as priority number** or **Remove priority**, depending on the change you're making.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_number_set_priority.png)

   The list of numbers automatically refreshes with your changes.
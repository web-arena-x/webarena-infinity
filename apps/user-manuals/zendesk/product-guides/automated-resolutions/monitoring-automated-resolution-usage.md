# Monitoring automated resolution usage

Source: https://support.zendesk.com/hc/en-us/articles/8922391373978-Monitoring-automated-resolution-usage

---

You can track yourautomated resolutionusage, which can help you determine whether your plan-based automated resolution baseline meets your needs. When you are near your automated resolution limit, you'll be alerted in Admin Center and your billing admin will receive an email notification.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can track your [automated resolution](https://support.zendesk.com/hc/en-us/articles/5352026794010) usage, which can help you
determine whether your plan-based automated resolution baseline meets your needs. When
you are near your automated resolution limit, you'll be alerted in Admin Center and your
billing admin will receive an email notification.

This article contains the following topics:

- [Viewing the Automated resolutions dashboard](#topic_s32_rww_k2c)
- [Monitoring automated resolutions at the ticket level](#topic_skx_tdh_g3c)
- [Monitoring automated resolutions at the conversation level (AI agents - Advanced)](#topic_uyw_rww_k2c)
- [Monitoring automated resolutions at the account level (AI agents - Advanced)](#topic_qgd_sww_k2c)
- [Viewing automated resolution usage banners](#topic_dfj_sww_k2c)

Related articles:

- [Explore recipe: Reporting on automated
  resolutions for email and web form channels](https://support.zendesk.com/hc/en-us/articles/9285975382298)
- [Managing your automated resolutions](https://support.zendesk.com/hc/en-us/articles/6958358659226)
- [Turning off automated resolution
  features](https://support.zendesk.com/hc/en-us/articles/7460877856026)

## Viewing the Automated resolutions dashboard

The Automated resolutions dashboard provides a look into how many automated
resolutions you use. The dashboard can help you determine how well your AI agents
deflect customer support requests and whether you should change your current
configurations. This information can also help you forecast your future automated
resolution needs.

**To view the Automated resolutions usage dashboard**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
  **Account** in the sidebar, then select **Usage > Automated resolutions**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ar_dashboard-viewonly.png)

The dashboard includes basic information about your automated resolution usage.

- **Overview**
  - **Allowance usage** displays the percentage of automated resolutions
    used in the current billing period.
  - **Automated resolutions** displays the number of automated
    resolutions used in the current billing period.
- **Usage details** displays a chart tracking the number of automated
  resolutions used per day for the selected time period. Use the drop-down menus
  to change the time span covered in the breakdown, as defined in [Understanding how automated resolutions are
  measured](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_m1n_sq4_jwb), and to display usage by type of automated resolution used,
  or to group types together.
- **Show cumulative** toggles on or off the aggregate of usage for the
  subscription term.

The dashboard only displays data on [confirmed automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_m1n_sq4_jwb).

From the dashboard, you can access the page to [manage your automated resolution overage setting](https://support.zendesk.com/hc/en-us/articles/6958358659226) and
[add automated resolutions to your
account](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_g2n_q3x_4wb).

## Monitoring automated resolutions at the ticket level

Tickets include helpful indicators when an automated resolution is consumed:

- The Resolution type field lists Automated as the value.
- In the [events view](https://support.zendesk.com/hc/en-us/articles/4408829602970), a system entry notes the
  date and time the automated resolution occurred.
- The Resolution type field can be used when [creating custom reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aia_resolution_type_ticket_field.png)

Note: Deleting a ticket with a Resolution type value of
Automated doesn’t undo the consumption of an automated resolution.

## Monitoring automated resolutions at the conversation level (AI agents - Advanced)

At the conversation level, automated resolutions are indicated in the [Conversation Logs](https://support.zendesk.com/hc/en-us/articles/8357749580186).

In the Conversation Logs, an automated resolution icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_ARs_icon.png)) is added to any conversation
that [consumes an automated resolution.](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_m1n_sq4_jwb)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_ARs_in_convo_log.png)

Additionally, you can drill into a specific conversation to see an explanation of the
automated resolution verification.

**To view a conversation’s automated resolution verification details**

1. In the main menu, select **Conversation Logs**.
2. From the list, select a conversation with the automated resolution icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_ARs_icon.png)).
3. Click **Details**.

   In the **Conversation Overview** panel that opens
   on the right, the **Automated resolution** section includes an
   explanation of why the conversation is considered to be
   verified.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_ARs_in_convo_overview.png)

## Monitoring automated resolutions at the account level (AI agents - Advanced)

At the account level, automated resolutions are reported in the Reporting
dashboard. This dashboard includes automated resolutions reporting that shows
your automated resolutions usage at the account level. For details, see [Analyzing advanced AI agent performance with
the reporting dashboard](https://support.zendesk.com/hc/en-us/articles/9510024609178).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_analytics_dashboard_performance.png)

## Viewing automated resolution usage banners

On AI agent pages in Admin Center, overage warning banners notify you when you’ve
used 80% of your automated resolutions, and will be updated when you’ve used 100%.
Banners will include basic information about what happens when you reach your limit
based on your [automated resolution overage setting](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_awx_qp1_ccc).

You can't dismiss these banners and they will remain visible until
automated resolutions are again available for your account when your billing cycle
resets or you purchase additional automated resolutions.

Overage warning banners appear on related Admin Center pages,
including:

- The parent AI agents page, as well as the following child
  pages:

  - AI agents for messaging
  - AI agents for email and web form
- The Web Widget (Classic) page
- The Automated resolution dashboard

Overage warning banners also appear on every page in the AI agents -
Advanced add-on.

If you choose to [pause AI agent functionality](https://support.zendesk.com/hc/en-us/articles/6958358659226#topic_iw3_b2h_bdc) when you
reach your automated resolution limit, notifications will appear on the admin pages
for each of the paused capabilities.

Additionally, your account owner and billing admin will receive an email notification
when you've used 80% of your automated resolutions, and again when you've used 100%.
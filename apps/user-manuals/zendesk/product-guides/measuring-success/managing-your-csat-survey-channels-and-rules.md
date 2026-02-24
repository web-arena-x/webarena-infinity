# Managing your CSAT survey, channels, and rules

Source: https://support.zendesk.com/hc/en-us/articles/8054625864602-Managing-your-CSAT-survey-channels-and-rules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

If you have [activated the CSAT survey](https://support.zendesk.com/hc/en-us/articles/7689997846554) for customers, you
can make changes for CSAT as needed. You can edit the CSAT survey, activate or
deactivate channels for the survey, and view and update the standard CSAT business
rules.

Note: Using satisfaction rating placeholders outside of
business rules can result in users other than the requester submitting satisfaction
scores.

You must be an administrator to manage CSAT.

This article includes the following topics:

- [Editing the CSAT
  survey](#topic_uqr_clr_w1c__ul_e3l_bmr_w1c)
- [Activating or deactivating the
  CSAT survey for a channel](#topic_pzy_h2d_5cc)
- [Viewing and updating the standard CSAT business rules](#topic_h5b_j2d_5cc)

## Editing the CSAT survey

You can make changes to the rating scale and follow-up questions for your CSAT survey
as needed.

**To set up and send the CSAT survey**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Customer
   satisfaction**.
2. Make changes to the **Rating scale** and **Follow-up questions**
   sections as needed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-customize-survey00509.png)
3. Click **Save**, then click **Back** to return to the Customer
   satisfaction page.

## Activating or deactivating the CSAT survey for a channel

Activating a channel turns on the associated business rule to start sending the CSAT
survey to users in that channel.

Deactivating a channel removes the channel and the accompanying business rules that
send the survey, but leaves the CSAT survey itself intact.

If you want to completely deactivate and removed the CSAT survey, see [Turning off the CSAT survey](https://support.zendesk.com/hc/en-us/articles/7689997846554#topic_nwn_32d_5cc).

**To activate or deactivate a CSAT channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Customer
   satisfaction**.
2. In the Channels section, click the channel actions icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-channel-select-icon.0509.png)) for the channel, then
   select **Activate** or **Deactivate**.

   To send a CSAT survey for
   messaging, you must have [set up messaging](https://support.zendesk.com/hc/en-us/articles/4409103246874).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Deactivate+channel+with+messaging.png)
3. Click **Activate rule** or **Deactivate rule**.

   The channel is
   either activated or deactivated and the channel status is updated to
   either Active or Inactive on the Customer satisfaction
   page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Channels+with+inactive+displayed+2.png)

## Viewing and updating the standard CSAT business rules

You can view and update the standard business rules associated with your active CSAT
channels to change the behavior as needed. Custom CSAT automations and triggers are
not displayed in the channels section of the Customer satisfaction page.

**To view the rule for an active CSAT channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Customer
   satisfaction**.
2. In the Channels section, click the channel actions icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-channel-select-icon.0509.png)) for the channel you want
   to view, then select **View rule**.

   The business rule opens in a new
   tab for you to view or edit.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging+view+rule.png)

### About the email automation for CSAT

The Request customer satisfaction rating automation for email sends the CSAT survey 24 hours after the ticket is solved, and the user has 28 days to respond. You can update this
automation rule or you can configure your own using the {{satisfaction.survey\_section}}
and {{satisfaction.survey\_url}} placeholders.

The Request customer satisfaction rating automation for email sends the CSAT
survey 24 hours after the ticket is set to solved.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/EmailAutomationPg_Jan325.png)

### About the messaging trigger for CSAT

The Request customer satisfaction rating trigger for messaging presents the CSAT
survey when a ticket created through the Web Widget, mobile SDK, or social
channel is set to solved.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT_view-rules_Messaging.png)
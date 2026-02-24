# Sending a CSAT survey to your customers

Source: https://support.zendesk.com/hc/en-us/articles/7689997846554-Sending-a-CSAT-survey-to-your-customers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

A [customer satisfaction (CSAT) survey](https://support.zendesk.com/hc/en-us/articles/4408886173338) encourages your
customers to provide feedback about their support experience by rating their solved
tickets. The survey is designed to maximize the response rate by being quick and simple,
while also gathering the essential data. You can customize the CSAT survey as
follows:

- **Tailor the CSAT question** to your needs
- **Select a rating scale** with 1-2, 1-3, or 1-5 ranges
- **Edit the label text** for each rating
- **Set the rating type** as numerical, emoji, or custom text
- **Show follow-up questions** for users who submit negative ratings

You can send a CSAT survey for email and messaging tickets, but not for legacy live chat.
For email tickets, the CSAT survey is sent in email one day after the ticket is set to
solved. For web, mobile, and social messaging, the survey is presented in the messaging
interface immediately after the ticket is set to solved.

You must be an administrator to set up and send a CSAT survey.

This article contains the following topics:

- [Setting up the CSAT survey](#topic_drb_cqq_1bc)
- [Turning off the
  CSAT survey](#topic_uqr_clr_w1c__ul_e3l_bmr_w1c)

## Setting up the CSAT survey

By default, the CSAT survey is not active. You can tailor the survey with your
CSAT question, rating scale, and rating labels, then choose the channels you'd like
to send the survey. You must be an admin to set up and send the CSAT survey.

Important: If you're using legacy CSAT, you must [deactivate legacy CSAT and any custom CSAT
business rules](https://support.zendesk.com/hc/en-us/articles/4408822875034) before you can activate this updated CSAT option. The
updated CSAT uses a [different placeholder](https://support.zendesk.com/hc/en-us/articles/4408886858138#topic_nnz_opl_rc) than the legacy
CSAT.

**To set up and send the CSAT survey**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Customer
   satisfaction**.
2. Click **Get started**.

   The page does not appear if you or another admin
   has already taken this step. If a banner at the top warns that you have
   legacy CSAT activated, click **Go to end-user admin** to deactivate
   legacy CSAT in the Satisfaction tab before continuing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-new-activation-landing.png)
3. Click **Edit survey**.
4. In the **Rating scale** section, configure the following:
   - **Headline**: Text users see when asked to respond to
     the survey.
   - **Scale range**: Rating scale options that you want
     users to select from:
     - 1-2 rating scale, where 1 is bad and 2 is good (Use this
       scale if you want to send a simple survey with a good or
       bad rating.)
     - 1-3 rating scale, where 1-2 is bad and 3 is good
     - 1-5 rating scale, where 1-3 is bad and 4-5 is good
   - **Scale type**: Response indicators that users will
     select when rating their experience, either numerical, emoji, or
     custom text.
   - **Scale**: Rating responses specific to the scale type. If your
     scale type is:
     - **Numerical**: The column displays numbers within the
       scale range.
     - **Emoji**: You can select the emoji that corresponds to
       the rating.
     - **Custom text**: You can type the text you want to
       display as the rating.
   - **Label**: For numerical or emoji scale types, this is the text
     that identifies the rating.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-rating-scale-0512.png)
5. (Optional) If you want to send an open-ended question to users who submit a
   negative rating, click to expand the **Open-ended question** section,
   then type the question in the **Headline** field.

   To remove this
   question from the survey, click **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-delete-survey-section00509.png)
6. (Optional) If you want to send a drop-down question to users who submit a
   negative rating, click to expand the **Drop down question** section, then
   configure your drop-down question:
   - **Headline**: Text presented above the drop-down question that
     asks users to select an option.
   - **Drop down options**: Possible reasons why users might submit a
     negative rating.
     - Click the **delete** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-trash-icon-0510.png)**)**
       to remove an option.
     - Use the **drag-and-drop** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-dropdown-recorder-0510.png)) to move
       an option up or down in the list.
     - Click **Add option** to add a new option.

     To remove this question from the survey, click
     **Delete**.
   - ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-dropdown.png)
7. Click **Save**, then click **Back** to return to the Customer
   satisfaction page to activate a channel for your CSAT survey.

   The CSAT
   survey will not be sent to users until you activate at least one channel
   for it.
8. In the **Channels** section, click the channel actions icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-channel-select-icon.0509.png)) for the channel you want
   to activate, then select **Activate**.

   Activating a channel turns on
   the associated business rule to start sending the CSAT survey to users
   in that channel. To send a CSAT survey for messaging, you must have
   [set up messaging](https://support.zendesk.com/hc/en-us/articles/4409103246874).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Activate+channels+with+messaging.png)
9. Click **Activate rule**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-activation-activate-rule00509.png)

   Once you activate the rule, the channel Status will show as
   **Active** on the Customer satisfaction page. To view CSAT
   results, see [Viewing your CSAT score and
   ratings](https://support.zendesk.com/hc/en-us/articles/4408846011546).

## Turning off the CSAT survey

Turning off a CSAT survey removes the CSAT survey and deactivates all channels. If
you want to turn off the survey for a specific channel only, see [Deactivating a CSAT channel](https://support.zendesk.com/hc/en-us/articles/8054625864602#topic_pzy_h2d_5cc).

**To turn off the CSAT survey and deactivate all channels**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Customer
   satisfaction**.
2. In the upper-right corner of the page, click **Actions**, then select
   **Turn off customer satisfaction**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/csat_turn_off.png)
3. Click **Turn off**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-turn-off-conf-0531.png)

   The CSAT survey is removed and no longer sent to
   users.
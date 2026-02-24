# Recipe: Sending a CSAT survey when a messaging session ends

Source: https://support.zendesk.com/hc/en-us/articles/8082415949210-Recipe-Sending-a-CSAT-survey-when-a-messaging-session-ends

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Note: To update the trigger as described in this article, your account must have the
[customizable CSAT survey](https://support.zendesk.com/hc/en-us/articles/7689997846554) feature.

When an agent [ends a messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042), the messaging
channel is essentially turned off for that customer interaction. This means that when
the related ticket status is later updated to Solved, it happens in the Support channel
rather than the messaging channel, and the conditions in the default messaging CSAT
trigger aren't met.

You can address this issue by updating the default trigger, *Request customer
satisfaction rating (messaging)*.

By default, the *Request customer satisfaction rating (messaging)* trigger fires
when the status of a ticket created via a messaging channel is updated to Solved and a
CSAT survey has not been sent to the customer.

To make sure the survey is sent for all messaging tickets when the session ends *or*
the ticket is updated to Solved, you must update the trigger's conditions so it fires
when either condition is met.

**To send a CSAT survey when a a messaging session ends**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Customer
   satisfaction**.
2. Click the *Request customer satisfaction rating (messaging)* trigger.
3. Under **Meet ALL of the following conditions**, remove the following
   condition:

   - **Ticket > Status category | Changed to | Solved**
4. Under **Meet ANY of the following conditions**, click **Add condition**.
5. Add the following conditions:

   - **Ticket > Status category | Changed to | Solved**
   - **Ticket > Messaging session ended reason | Changed to | Ended
     by agent**
6. Click **Save**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/send_survey_end_session_trigger.png)
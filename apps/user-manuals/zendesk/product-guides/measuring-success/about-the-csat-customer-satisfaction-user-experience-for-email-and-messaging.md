# About the CSAT (Customer Satisfaction) user experience for email and messaging

Source: https://support.zendesk.com/hc/en-us/articles/4408886173338-About-the-CSAT-Customer-Satisfaction-user-experience-for-email-and-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

Enable CSAT ratings to gather customer feedback on solved tickets via email, messaging, or the customer portal. Customers can rate their experience and add comments, helping you understand their satisfaction levels. Customize survey questions and response options to fit your needs. Note that CSAT surveys are optional in messaging but mandatory for each solved ticket in email.

Your customers can provide feedback about their support experience by rating their solved
tickets. When you [enable CSAT](https://support.zendesk.com/hc/en-us/articles/7689997846554) (customer
satisfaction) ratings, end users and agents who submit ticket requests
receive a notification after the ticket has been solved that asks them to
briefly evaluate their experience. They can also submit CSAT feedback in the
customer portal of your help center.

The survey is designed to maximize the response rate by being quick and simple
while also gathering the essential data: a positive or negative rating and
optional comment. You can customize the CSAT question, rating scale, and
rating labels.

This article contains the following sections:

- [Email channel CSAT end-user experience](#topic_xxm_imn_gc)
- [Messaging channel CSAT end-user experience](#topic_zcl_lsd_fc)
- [Request page CSAT end-user experience](#topic_dnq_fw1_l2c)

Related articles:

- [Viewing your CSAT
  ratings and score](https://support.zendesk.com/hc/en-us/articles/4408846011546)

## Email channel CSAT end-user experience

When you turn on CSAT ratings for email, end users and agents who
submitted an email request receive a notification after the ticket
is set to solved, asking them to briefly evaluate their experience.
They have 28 days, by default, to respond to this request. Users can
respond to the CSAT survey as long as the link hasn't expired,
regardless of whether the ticket is in a solved or closed state. You
can customize the default CSAT automation to modify the end-user
experience, including the number of hours after a ticket is solved
that users receive the CSAT notification.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Email_new_Scale-0512.png)

The survey is designed to maximize the response rate by being
quick and simple while also asking users to rate their satisfaction
with the support they received. Users can select the option that
best reflects their experience from the ratings listed.

When users select a rating, they are brought to a landing page
where they can provide their feedback and add an optional comment.
The elements end users see depends on how the CSAT is configured.
For example, if CSAT is configured to include the CSAT ratings and
no additional questions, end users will only see the ratings area.
For the configuration options, see [Sending a CSAT survey to your customers](https://support.zendesk.com/hc/en-us/articles/7689997846554).

**Example**

In this example, a CSAT survey is configured with the following:

- CSAT question with ratings
- Drop-down reasons for users who submit a negative
  rating
- Open-ended question

When CSAT is configured this way, end users responding to the survey will
see one of the following views, depending on whether they submit a
positive or a negative rating.

- **Positive rating**: End users can add
  comments

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT-Positive-1108.png)
- **Negative rating**: End users can add comments and
  select a reason for their experience from the
  drop-down menu.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT+negative+1108-NEW.jpg)

The following rules apply to end users when using CSAT:

- End users can't opt out of receiving survey
  requests.
- Satisfaction ratings are per ticket, not per customer.
  End users receive a survey request for each of their
  tickets that are solved.
- Once a ticket is set to Closed status, the temporary URL
  is available for 28 days after the CSAT is
  sent.

## Messaging channel CSAT end-user experience

When you turn on CSAT ratings for messaging, a simple survey is added to
your messaging workflow, allowing your end users and agents who
submit ticket requests to provide feedback about their support
experience. These surveys are completely optional for your
customers. After an end user receives assistance through a messaging
channel, they are sent a message asking them to evaluate their
experience. They have 28 days, by default, to respond to this
request.

Note: To enable agents to rate
their own tickets (where they are requesters), [turn on help center
authentication](https://support.zendesk.com/hc/en-us/articles/9495852479770) in the Web Widget.

CSAT functionality in messaging has the following limitations:

- Agents cannot manually launch a CSAT survey. It can only be sent
  when a ticket is marked as *Solved*, or if the default
  trigger is altered.
- CSAT collection is represented by the bot avatar in messaging.
  This cannot be configured, but is presented by the system
  avatar in the new CSAT.

You can customize the default trigger to modify the end-user
experience.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT-Messaging-chat-window-1.png)

By default, the survey is presented in the messaging channels (for example,
web and mobile). The survey is designed to maximize the response
rate by being quick and simple, while also gathering the essential
data: a positive or negative rating and optional comments. You can customize the CSAT question, rating scale, and rating labels.

When users click to submit a customer satisfaction rating, they begin a messaging
conversation that guides them through questions where they can
provide their feedback and add comments. This flow may vary based on
the messaging channel and configuration. In general, the elements
end users can respond to in the message depends on how CSAT is
configured. For example, if CSAT is configured to include the
CSAT ratings and no additional questions, end users would see only
the ratings question. For the configuration
options, see [Sending a CSAT survey to your
customers](https://support.zendesk.com/hc/en-us/articles/7689997846554).

In this example, a CSAT survey is configured with the following:

- CSAT question with ratings
- Drop-down reasons for users who submit a negative
  rating
- Open-ended question

When CSAT is configured this way, end users responding to the survey
with a negative rating will see the following flow.

- **Rating**: User rates the support as 2, which is a
  negative rating.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT-Messaging-Rating-2.png)
- **Reason**: User selects a reason for their
  experience from the drop-down menu.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT-Messaging-Reason-3.png)
- **Comments and submit**: User finishes the survey by
  typing additional comments and submitting the
  feedback.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/CSAT-Messaging-Comment-4.png)

## Request page CSAT end-user experience

You can collect CSAT feedback from end users on the request page in the
Customer Portal. To do this, your theme must include the new
satisfaction\_response property in the Copenhagen request\_page.hbs
(see [Enable CSAT for solved
tickets on the Customer Portal](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_nl4_tnx_ycc)).

Once the ticket is solved, end users can use the Requests page to find
and open their request and submit CSAT feedback. See [Submitting CSAT for your
ticket](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_rpc_ygy_ycc).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Add+Feedback.png)
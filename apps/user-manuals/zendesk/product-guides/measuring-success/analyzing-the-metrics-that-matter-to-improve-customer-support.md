# Analyzing the metrics that matter to improve customer support

Source: https://support.zendesk.com/hc/en-us/articles/4408832234394-Analyzing-the-metrics-that-matter-to-improve-customer-support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

Using Explore, you can analyze your customer service experience to identify areas where you're exceeding expectations and areas that might need improvement. You can then use this information to improve the effectiveness of your team and your customer support.

Learn which metrics are important to monitor, how to report on them in Explore, what trends to look for, and how to take action on this information.

This article contains the following topics:

- [How many tickets are we solving?](#topic_twv_f1q_k5b)
- [What are the most common ticket areas?](#topic_bnf_31q_k5b)
- [How much work do we have?](#topic_gvj_j1q_k5b)
- [How long do customers wait for a first reply?](#topic_byc_k1q_k5b)
- [How long do tickets take to resolve?](#topic_a11_l1q_k5b)
- [How often are solved tickets reopened?](#topic_fqt_l1q_k5b)
- [How satisfied are customers?](#topic_mzr_m1q_k5b)
- [More resources](#topic_kdx_n1q_k5b)
- [Join the conversation!](#topic_c5m_41q_k5b)

## How many tickets are we solving?

The number of tickets solved gives you a quick indication of how your team is doing.
It's most useful for examining overall trends, as some tickets are quickly solved while others take longer. Monitoring this metric over time helps you evaluate your team's performance and decide your resourcing needs.

### Viewing prebuilt reports (Lite and Professional)

The [Tickets tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_hlj_xbj_z3b) gives you an at-a-glance view of your solved, unsolved, created, and reopened tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_metrics_matter_tickets_tab.png)

Additionally, the **Assignee activity** report on the [Assignee activity tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_dpf_ybj_z3b) shows your top ticket solvers, along with a wealth of other information.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_assignee_activity_report.png)

### Creating your own reports (Professional)

The [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y) contains the metrics and attributes you need to create your own reports about solved tickets.

The following Explore recipes give you some great starting points for creating your reports:

- [Reporting on created and solved tickets](https://support.zendesk.com/hc/en-us/articles/4408825110682)
- [Daily ticket activity in the last 30 days](https://support.zendesk.com/hc/en-us/articles/4408838648602)
- [Solved tickets this year compared to last year](https://support.zendesk.com/hc/en-us/articles/4408819446298)

For a full list of recipes, see [Explore recipes reference](https://support.zendesk.com/hc/en-us/articles/4409149172890).

### What to look for

As you look at your reports, focus on the following information:

- The **Solved tickets** metric for both the whole team and individual agents.
- The average values over a period of time (for example, a month). Some days, agents will be over or under the target.
- The number of solved tickets compared with the number of open tickets. This shows how well the team is keeping up with the ticket queue.

### How to use the results

The following table gives some examples of how you can use solved ticket reports to help improve your team's efficiency:

| If you see this | Do this |
| --- | --- |
| Ticket volumes are consistently high. | - Consider hiring more agents. Look for patterns of   particularly busy or quiet times and staff   accordingly. - Consider more training for your agents. - Look for common problem areas in tickets. Meet with   product managers to see if the product could be   improved. Consider setting up an About field (see [What are the   most common ticket areas?](#topic_bnf_31q_k5b)). - Consider [setting up a   knowledge base](https://support.zendesk.com/hc/en-us/articles/4408846795674) to enable customers to serve   themselves. A great knowledge base means that many of   your customers will find the answer to their problem   without ever opening a ticket. |
| Ticket volumes are consistently low. | - You might be able to reduce your number of agents. |
| Some agents have low solve rates. | - Check which tickets the agent has been working on. They   could be particularly time-consuming problems. - If an agent has a consistently low solve rate, they   might require more product training. |

## What are the most common ticket areas?

Feedback from customers can help you improve your products and your customers' experiences. Take advantage of this feedback by categorizing your support requests into product areas. Then, you can easily see which product areas generate the most support issues.

To categorize your support requests, [add a custom field to your tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794). This field can contain as many values as you want, and you can call the field whatever you want. In this example, the field is called Product and contains three values.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/improving_support_1.png)

To see how Zendesk categorizes tickets, see [The 'About' Field](https://support.zendesk.com/hc/en-us/articles/4409155792026).

### Viewing prebuilt reports (Lite and Professional)

Explore doesn't include custom fields on prebuilt dashboards. However, you can report on custom ticket fields by creating your own reports.

### Creating your own reports (Professional)

The [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y) includes each of your custom fields as an attribute. For more information, see [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538).

**To create a report showing areas with the most tickets**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) using the **Support - Tickets** dataset.
2. In the **Metrics** panel, select **Tickets** > **Tickets**.
3. In the **Rows** panel, select **Ticket custom fields** >
   ***customfieldname***.

   ***customfieldname*** is the name of the custom field you created to categorize your tickets.

The following Explore recipes give you some great starting points for creating your reports:

- [Reporting on custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4660627546010)
- [Reporting on nested drop-down fields](https://support.zendesk.com/hc/en-us/articles/4408846701082)

### What to look for

As you look at your reports, focus on the following information:

- The number of tickets in each area compared to the overall ticket volume.
- The average time it takes to solve a ticket in each area.
- The average CSAT rating for tickets in each area.

### How to use the results

The following table gives some examples of how the category can help improve your customer support:

| If you see this | Do this |
| --- | --- |
| One category generates significantly more tickets than others. | - Work with product teams to identify whether the product   area could be improved. - [Create a knowledge   base](https://support.zendesk.com/hc/en-us/articles/4408846795674) with information to help customers use   that area of the product. |
| Many tickets are not assigned to a category. | - Train your agents to categorize tickets by selecting   from the list of predefined categories. - Make the category field mandatory, meaning a category   must be chosen before you can proceed. - [Add the field to your   support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794#topic_ubz_ynk_xj) so your customers can   choose the relevant category when they submit a support   request. |

## How much work do we have?

Your ticket backlog provides a general pulse on the health of your support team.
Ticket backlog is defined as all tickets currently in a new, open, pending, or on-hold state. In other words, it's your unsolved tickets that need work done on them.

This is an important metric to watch because it provides insight into your incoming ticket volume and how well you keep up, given your resources.

### Viewing prebuilt reports (Lite and Professional)

The [Backlog tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_wyg_ybj_z3b) includes prebuilt reports that measure your daily and weekly ticket backlog.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_metrics_matter_ticket_backlog.png)

### Creating your own reports (Professional)

The [Backlog history dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_dfb_ydg_ndb) contains the metrics and attributes you need to create your own reports about your ticket backlog.

The following Explore recipes give you some great starting points for creating your reports:

- [Backlog tickets by month](https://support.zendesk.com/hc/en-us/articles/4408827158426)
- [Top problem tickets by unsolved incidents](https://support.zendesk.com/hc/en-us/articles/4408833663514-Explore-Recipe-Top-problem-tickets-by-unsolved-incidents)

### What to look for

As you look at your reports, focus on the following information:

- Ticket backlog volume cross-referenced with ticket age and first reply time. A large backlog isn't necessarily a bad thing if your team is capable of a high throughput.
- Ticket priority cross-referenced with ticket status. A large backlog may or may not be bad, but one with many high-priority tickets probably is.
- Historical backlog trends. For example, what are your busiest months?
 Which of your agents are performing the best?
- Whether there are multiple support requests from the same customer, or in the same categories.

Remember that speed is important, but not at the expense of quality. Sometimes, support issues take longer to solve than the customer expects or longer than the performance targets you’ve set for your team. However, the longer it takes to solve a customer’s issue, the more likely customer satisfaction will suffer.

### How to use the results

The following table gives some examples of how examining your ticket backlog can help improve your customer support:

| If you see this | Do this |
| --- | --- |
| Your backlog is too big. | - This means that customers are waiting longer for help.   Your team can help by keeping the customer informed   about the status and progress of their request. - Are a lot of tickets in a pending state waiting for a   customer response? Consider creating an automation to   remind the customer of the pending status of their   issue. If they don’t respond after a set number of days,   you can automatically resolve the ticket to remove it   from the backlog. For an example, see [Zendesk on Zendesk:   Bump Bump Solve](https://support.zendesk.com/hc/en-us/community/posts/204143947). - A backlog consists of both unassigned tickets and   assigned tickets that have not yet been solved. The two   combined equals your total ticket backlog. Try to ensure   that tickets are assigned to someone as quickly as   possible. |
| You have a lot of high-priority tickets in your backlog. | - Consider creating a trigger that escalates high-priority   tickets to make them visible more quickly. See [Creating triggers for   automatic ticket updates and   notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466). - Triage incoming tickets from customers to ensure they've   set the priority field appropriately. - Make sure your agents aren't setting the priority field   incorrectly. If so, they might need further training in   how to categorize requests. |
| You see multiple support requests from the same customer in the same category. | - Engage directly with the customer to find out what's   wrong. |
| You get multiple support requests from different customers for the same problem. | - Consider [writing a knowledge   base article](https://support.zendesk.com/hc/en-us/articles/4408839258778) about the problem. - [Engage with the   community](https://www.zendesk.com/blog/cultivate-community-customer-experience) in your knowledge base. - Talk to your product development team. Could a product   redesign help to stop problems? |

## How long do customers wait for a first reply?

First reply time (FRT) is the amount of time from when a ticket is created to when an agent makes the first reply to the customer. In other words, it measures how long it takes a real human, not an automated reply, to contact the customer. First reply time is a good indicator of the efficiency of your team and how well they hold up in handling fluctuating incoming ticket volumes.

Your performance target for this metric should align with your industry and customer expectations for first reply times. For example, you might use:

- 24 hours for support requests submitted using email and online forms
- 60 minutes for requests submitted using social media

Of course, exceeding these expectations is even better from the customer’s perspective.

### Viewing prebuilt reports (Lite and Professional)

The [Efficiency tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_zd3_ybj_z3b) includes prebuilt reports that measure your first reply time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_metrics_matter_ticket_backlog.png)

### Creating your own reports (Professional)

The [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y) contains the metrics and attributes you need to create your own reports about first reply time and efficiency.

The following Explore recipes give you some great starting points for creating your reports:

- [Reporting on first reply time](https://support.zendesk.com/hc/en-us/articles/4408820652058)
- [First reply time heatmap](https://support.zendesk.com/hc/en-us/articles/4408823587738-Explore-recipe-First-reply-time-heatmap)
- [Displaying tickets with a higher than average first reply time](https://support.zendesk.com/hc/en-us/articles/4408819310746)
- [Creating a ticket first reply date attribute](https://support.zendesk.com/hc/en-us/articles/4408846756506)
- [Getting resolution times (first reply, first resolution, and full resolution) based on tags](https://support.zendesk.com/hc/en-us/articles/4408827196954)

### What to look for

As you look at your reports, focus on the following information:

- Look at your ticket volume whenever your first reply time changes. A change might correspond with a temporary change in ticket volume. Start by looking at the [Tickets](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_hlj_xbj_z3b) and [Efficiency](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_zd3_ybj_z3b) tabs in the Zendesk Support dashboard. If you had a temporary surge from a new product launch or a major service incident, then this might not be a worrying trend. If you can predict these surges, that's a great time to bring a bit of extra help onboard.
- If your first reply time is 24 hours on email-submitted requests and your median number of agent interactions is eight per ticket, then your average reply time median should be 4 hours or less. Looking at tickets with an average reply time greater than 4 hours should highlight opportunities for improving agent performance (such as training or adding self-service documentation to your knowledge base).
- What are your customers telling you about your reply time? Look at your CSAT ratings and comments.
- Monitor first reply time for each of your support channels to ensure that expectations are being met.
- Monitor first reply time by product area if you're using a custom field as described earlier in this article (see [What are the most common ticket areas?](#topic_bnf_31q_k5b)).
- Monitor average reply time. This is the average amount of time for all replies to the customer when solving a support request.

### How to use the results

The following table gives some examples of how examining your first response times can help improve your customer support:

| If you see this | Do this |
| --- | --- |
| First reply times are high. | - Look at when you get most of your tickets. An Explore   report using the **Tickets** metric and the **Ticket   created - Hour** attribute is a quick way to help   make sure you have support online when your customers   are. - However quickly your team solves emailed tickets,   sometimes live channels can be a faster way for   customers to get help and for you to solve tickets. - When something goes wrong, it's critical to find and   address the issue as quickly as possible. Letting   customers know you're aware and working on a problem is   key to turning a bad situation into a good interaction   with your company. - If your customers serve themselves, then you don't need   to worry about first reply times! [Set up a knowledge   base](https://support.zendesk.com/hc/en-us/articles/4408846795674) and write articles that address your top   customer pain points. Stay present in your knowledge   base and always answer questions from customers. |

## How long do tickets take to resolve?

Resolution time is important not just to you and your team. Customers also want their problems solved quickly. There are several key metrics that indicate how long it takes for agents to resolve issues:

- **Resolution time:** The time it takes for a support issue to be solved. A ticket might get solved more than once because it can be reopened before it’s closed. The time it took to solve the issue the first time is called first resolution time.
- **Full resolution time:** The time it took to finally solve the ticket.
- **Agent replies:** The number of replies it takes for your agents to solve the ticket. The faster you can solve a ticket, the happier the customer will be.
- **One-touch resolution:** Support issues that were resolved in a single interaction such as a call, ticket reply, or live chat. This has a positive impact on customer satisfaction and helps reduce support costs.

### Viewing prebuilt reports (Lite and Professional)

The [Efficiency tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_zd3_ybj_z3b) includes prebuilt reports that measure how long your tickets take to solve.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_improve_metrics_4.png)

### Creating your own reports (Professional)

The [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y) contains the metrics and attributes you need to create your own reports about first reply time and efficiency.

The following Explore recipes give you some great starting points for creating your reports:

- [First assignment to first resolution time](https://support.zendesk.com/hc/en-us/articles/4408845671706)
- [Reporting on full resolution time](https://support.zendesk.com/hc/en-us/articles/4408846254234)
- [Average ticket resolution time without pending or on-hold time](https://support.zendesk.com/hc/en-us/articles/4408830883610)
- [Getting resolution times (first reply, first resolution, and full resolution) based on tags](https://support.zendesk.com/hc/en-us/articles/4408827196954-Explore-recipe-Getting-resolution-times-first-reply-first-resolution-and-full-resolution-based-on-tags)
- [Time Tracking app: metrics you need to be measuring](https://support.zendesk.com/hc/en-us/articles/4408825230490)

### What to look for

Metrics that can help you understand the time and effort that went into solving a ticket include:

- **Handle time:** The time that an agent spends working on a single support interaction. In Support, handle time is captured using the [Time Tracking app](https://support.zendesk.com/hc/en-us/articles/4408828227098). Explore can report on this data using the custom fields Total time spent, Avg time spent per ticket, and Avg time spent per update. For details, see [Time Tracking app: metrics you need to be measuring](https://support.zendesk.com/hc/en-us/articles/4408825230490).
- **Agent touches:** An update that an agent makes to a ticket. This includes changes of ticket status, adding comments, and others. With Explore, you can report on agent touches using the **Agent replies** metric and **Agent replies brackets** attribute.
- **Requester wait time:** The time a customer waits for their issue to be resolved. This is the time that a ticket spends in the New, Open, and On-hold statuses. During these periods, it’s the support team’s responsibility to resolve the issue. It's a good indicator of the customer’s experience of the support interaction.

### How to use the results

The following table gives some examples of how examining your full resolution times can help improve your customer support:

| If you see this | Do this |
| --- | --- |
| Tickets are taking too long to resolve. | - This has a direct effect on customer satisfaction:   People don’t want to wait a long time to have their   problems resolved. However, focusing solely on   resolution time isn’t necessarily a good idea. Speed   doesn’t always equal quality. (For more, see [How often   are solved tickets reopened?](#topic_fqt_l1q_k5b)) - In addition to resolution time, finding the actual time   that the agent spent resolving the issue is important.   Total resolution time doesn’t do that because it   includes stages in the ticket lifecycle when the agent   isn’t working on it. For example, when it’s sent back to   the customer for information and put in a Pending   status. |
| You have a high proportion of one-touch resolution tickets. | - This might indicate that you have lots of low-complexity   support issues that could be better handled with   self-service. Agents should work on more complex issues,   not those that a customer can easily solve on their own   by reading FAQs. |
| Tickets have a high proportion of agent touches. | - This might indicate that the agent needs more training   because it takes them more touches than the team average   to solve tickets. |

## How often are solved tickets reopened?

A reopen occurs when a ticket's status is changed from Solved back to Open.

When tickets are reopened, this might indicate that agents aren’t fully solving the customer’s support issues. This might be because agents are concentrating on first-touch resolutions and speed over quality. It’s good practice to routinely monitor your team’s ticket reopens.

### Viewing prebuilt reports (Lite and Professional)

The [Tickets tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_hlj_xbj_z3b) contains information about reopened tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_improve_metrics_5.png)

### Creating your own reports (Professional)

The [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y) contains the metrics and attributes you need to create your own reports about reopened tickets.

### What to look for

- The total number of reopens
- The percentage of tickets with reopens

### How to use the results

The following table gives some examples of how examining your ticket reopens can help improve your customer support:

| If you see this | Do this |
| --- | --- |
| The percentage of tickets being reopened is high. | - Is this an escalated issue? Ticket reopens are more   likely when agents deal with more complex support   issues, so reopens might be higher for escalated   tickets. - Are your agents sufficiently trained? They might not   have sufficient knowledge to solve more complex   problems. - Was there missing information in the ticket that caused   the agent to misdiagnose the issue? Consider collecting   more information in the customer ticket form if this is   the case. |

## How satisfied are customers?

Every time you interact with a customer, consider [measuring their satisfaction with a Customer Satisfaction Survey (CSAT)](https://support.zendesk.com/hc/en-us/articles/4408822875034), a short survey sent to the customer after their problem is solved.

Tracking CSAT helps you spot trends that might be affecting customer satisfaction.
Satisfaction ratings are also key performance indicators for your agents because each rating received is associated with the agent who solved the customer’s problem.
These can be averaged to give each agent an overall CSAT score.

At Zendesk, we simply ask if the interaction was good or bad. If customers want to give more feedback, they can add a comment.

Examples of metrics you can track include:

- A customer’s CSAT rating over time
- CSAT ratings by channel, product, or service
- Average CSAT ratings for agents and teams

### Viewing prebuilt reports (Lite and Professional)

The [Satisfaction tab of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_ijh_ybj_z3b) includes reports that help you analyze your customer satisfaction scores.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_improve_metrics_6.png)

### Creating your own reports (Professional)

The [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y) contains the metrics and attributes you need to create your own reports about customer satisfaction.

The following Explore recipes give you some great starting points for creating your reports:

- [Reporting on customer satisfaction by agent](https://support.zendesk.com/hc/en-us/articles/4408845694234)
- [Determining satsifaction scores for your agents](https://support.zendesk.com/hc/en-us/articles/4408822875930)
- [Determine ticket assignee when satisfaction rating is given](https://support.zendesk.com/hc/en-us/articles/4408843401370)
- [Display all customer satisfaction comments](https://support.zendesk.com/hc/en-us/articles/4408825376282)
- [Bad ratings with comments](https://support.zendesk.com/hc/en-us/articles/4408838658074-Explore-Recipe-Bad-ratings-with-comments)
- [Reporting on CSAT and one-touch tickets](https://support.zendesk.com/hc/en-us/articles/4408845685146)
- [Percentage satisfaction score based on agent replies](https://support.zendesk.com/hc/en-us/articles/4408820380314-Explore-Recipe-Percentage-satisfaction-score-based-on-agent-replies)
- [Satisfaction trending year-over-year](https://support.zendesk.com/hc/en-us/articles/4408837820442-Explore-recipe-Satisfaction-trending-year-over-year)

### What to look for

- Compare ticket stats on tickets rated bad to those rated good.
- Look for satisfaction ratings with comments.

### How to use the results

The following table gives some examples of how examining your customer satisfaction can help improve your customer support:

| If you see this | Do this |
| --- | --- |
| You get one or more bad ratings. | - Notify managers when you get feedback. You can automate   this using a trigger to notify a manager or group of   managers when a ticket receives a bad rating. Use the   following two [trigger   conditions](https://support.zendesk.com/hc/en-us/articles/4408886797466):   - **Ticket: Satisfaction** > **Changed to**     > **Bad**   - **Ticket: Satisfaction** > **Changed to**     > **Bad with comment** - Give your agents more information about your customers.   Tickets with more touches often have a lower CSAT   rating. Making more customer information available to   your support teams with CRM integrations or custom user   and organization fields can help your team know more   about customers up front. If you can eliminate initial   questions on tickets, that leads to faster resolution   times and more one-touch ticket solves. - Did your agent provide inaccurate information? Was there   an issue with resolution time? Consider categorizing   badly rated tickets based on the reasons why the ticket   was rated the way it was. If it's purely about ticket   handling, resolution time, or workflow issues, then   those are some great projects to work on going   forward. |

## More resources

By focusing on the metrics that matter, both your organization and your customers will benefit. All of the reports you've learned about in this article can be used to help you avoid ongoing issues.

If you're new to Explore and want to learn the basics, read [Getting started with Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618).

For some great ideas to help you get started with reporting, check out [Explore recipes reference](https://support.zendesk.com/hc/en-us/articles/4409149172890).

Finally, to see all of the Explore documentation, start with [Zendesk Explore resources](https://support.zendesk.com/hc/en-us/articles/4408846357018).

## Join the conversation!

What tools do you use to help measure the success of your support organization? How have you managed to improve these metrics? Let us know in the comments below.
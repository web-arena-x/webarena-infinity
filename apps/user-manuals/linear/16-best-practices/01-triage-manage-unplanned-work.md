# How to manage unplanned work

![Icons for Front, Zapier, Intercom, Slack, and Zendesk connecting to Linear's Triage icon.](https://webassets.linear.app/images/ornj730p/production/d1c6a325cb0083436a3aafd62930f6c1cb9755af-2400x1352.jpg?q=95&auto=format&dpr=2)

One of the biggest pain points for product teams is how to manage work that arises unexpectedly, like bug reports from customers and requests from other teams. These issues vary in scope, priority, and importance, which makes them harder to process and fit into a team's planned work or cycle. Another challenge is that they often come from different, disconnected places. This makes it hard to understand the context of the issue and communicate with the issue creator. 

Some common examples of these issues include:

* Bug reports from customers
* Requests from sales, marketing, or other departments 
* Issues filed by colleagues outside of your team, who don't have context to assign or prioritize them

Without a clear process, unplanned work can become a real toll on your team. Issues get lost (or don't get filed in the first place), active work queues clutter up, and teams get distracted from higher priority work.

The best strategy for managing unplanned work is to create a clear process that centralizes all incoming requests and routes them to the correct team. We call this process Triage.

---

## Build a Triage process

![Data flowing from many places, including Slack, Intercom, and Zendesk through Linear Triage and into an appropriate location.](https://webassets.linear.app/images/ornj730p/production/9f04052f066aa603a30f2f4431490d39c0b2bd4b-2400x1352.jpg?q=95&auto=format&dpr=2)

Follow these best practices to build an effective triaging process for your team. Linear's Triage feature is designed around these best practices and works seamless with any integrations you use to create issues. 

### 1. Lower the friction to file

A good triage process makes it easy for anyone to file new issues. You shouldn't have to ask how to file an issue to a team, or follow a different process for different teams. It's even better if you can build the issue creation flow into team members's current workflows and most used tools.

With Triage enabled, there is no special process to follow when filing issues to another team. Simply create an issue; if you aren't a member of the assigned team, the issue will go to that team's Triage inbox automatically. 

Seamless[ integrations](https://linear.app/integrations) let your frontline team create issues from the tools that they use most.

Team | Sent to Triage from
--- | ---
Customer Support | Intercom, Zendesk, Front
Sales & Operations | Slack
DevOps | Sentry, Bugsnag
Anyone | Custom tooling with API, Zapier

![Video](https://webassets.linear.app/files/ornj730p/production/d11fec2ba120061ac3b457c6d1c814e1559e87b4.mp4)

### 2. Route issues to one place

For the teams receiving new issues, it helps to keep unreviewed work separate from any active or prioritized work queues. This makes it easier for the team to understand priorities since they can trust that issues in the backlog or active views are ready to be picked up. It also avoids scope creep and distractions that can happen if anyone can put new issues into a team's workflow.

In Linear, new issues are assigned a Triage workflow status and all go to the shared team Triage inbox. These issues do not show up in the backlog or active issue lists, though you can update view options to include them in issue views. 

![Video](https://webassets.linear.app/files/ornj730p/production/68d8deeccaacf52795168d9ee1fa8043be686bfc.mp4)

### 3. Choose Triage captains

Someone should have the explicit responsibility to review new issues to make sure they're seen and prioritized. It's common to set up a rotation (e.g., weekly) or for the team lead to own this task. The most important thing is to make a clear owner to ensure new issues get reviewed in a timely way.

The Triage captain can monitor the team's inbox by looking at the count of issues in the sidebar. They can also configure notifications so they're notified of new issues in Triage and get a notification in their personal inbox as well as the Triage inbox.

![Video](https://webassets.linear.app/files/ornj730p/production/5223b45ee9c53d9f2e212ccee46afe1145a157c9.mp4)

> [!NOTE]
> **How we work at Linear**  
> We send all customer issues, internal work requests, and Sentry alerts to a single team in Linear which is managed by a rotating Triage captain. Every engineer on the team participates. The rotation is managed in PagerDuty and captains often enable Triage notifications temporarily during their tour of duty.

### 4. Review issues regularly

Teams should establish their own standards for how to review and prioritize issues. It is helpful if these standards are communicated to others so they know what to expect. The process will be faster if Triage captains feel they have the authority and knowledge to make decisions such as canceling issues and assigning them to the appropriate teammates.

Triage has built-in features that make it quick to review issues and easy to communicate with team members. Quick actions allow you to accept, reject, merge, or snooze issues. Built-in details encourage you to add a note when canceling issues or to leave comments when you need more clarity. When merging issues, the links and key details are carried over for you.

![Video](https://webassets.linear.app/files/ornj730p/production/48f9ff27aac5526617006ad4e617af7dd54c53cb.mp4)

---

## Optimize your workflow

Move faster and personalize your triage workflow with these features and customizations:

* [**Inbox notifications**](https://linear.app/docs/triage#notifications): send Triage notifications to your personal inbox
* [**Snooze notifications**](https://linear.app/docs/triage#snooze): snooze issues until they're ready for review
* [**Favorite**](https://linear.app/docs/favorites): favorite your Triage inbox for easy access in the sidebar
* [**Prioritize**](https://linear.app/docs/triage#collapsible-6554f37d047c): require priority as an issue field when accepting issues
* [**Sentry alerts**](https://linear.app/docs/sentry#automations): automatically create issues from Sentry alerts
* [**View options**](https://linear.app/docs/triage#collapsible-11bbc5452305): show or hide triage issues from views

---

## Level up

Get more out of Triage by using these additional features:

### Prioritize time-sensitive issues with SLAs

Enable SLAs in your workspace so that they are automatically applied to issues when they match certain parameters. This can help signal important issues in the Triage queue and ensure that time-sensitive issues are prioritized. [Learn more](https://linear.app/docs/sla)

Example SLAs | 
--- | ---
When priority is urgent | Apply 24 hour SLA
When priority is high and the label includes bug | Apply 1 week SLA
When priority is low and the label includes bug | Apply 2 week SLA

![Video](https://webassets.linear.app/files/ornj730p/production/4d7b0c21f90ef17991a7e096f77edaab71954080.mp4)

### Enable support automations

If you use [Zendesk](https://linear.app/integrations/zendesk), [Intercom](https://linear.app/integrations/intercom), [Front](https://linear.app/integrations/front), or [Plain](https://linear.app/integrations/plain), we recommend checking out the integration and using it in combination with Triage.

Any issues created by your customer support team through the integration will go to Triage, where they can trust someone from the engineering team will review the issue. The integrations make it easy for the support team to track progress on top customer issues and communicate with the engineering team when questions arise. Engineers debugging issues can view the initial conversation from Linear or follow the linked conversation to learn more or directly reach out to the customer. It's easy to close the feedback loop with customers, too, since conversations re-open when Linear issues are closed. Learn more

![Video](https://webassets.linear.app/files/ornj730p/production/282302b610cae47e45208dfb3a582b3d2bdf1f22.mp4)

# Troubleshooting: Experience Approvals Running Out of Order

Source: https://support.joinhandshake.com/hc/en-us/articles/115015970728-Troubleshooting-Experience-Approvals-Running-Out-of-Order

---

If you manage the approval process for experiences, and notice that the approval process is running out of order, it could seem like a bug. This article will walk you through the troubleshooting steps!

If the approvals look like they are being sent out of order, it most likely a result of how the approval offset timelines are configured.

Note: for more information on approval offset timelines, check out [this article on Offset Days](definition-offset-days.md)

If an experience approver's deadline is LESS THAN 3 days, it's entirely possible these are approved out of order because we are sending two reminder emails to each approver:

- One notification sent 3 days before their deadline.
- One notification sent 24 hours before their deadline

Essentially, if that deadline is less than 3 days, we will send the "3 day" notification immediately. This means that a secondary approver who would regularly have to wait for the initial contact to approve, will technically have a chance to approve before the initial contact does.

We don't typically recommend assigning a deadline of less than 3 days to an approver, since that can be a quick turnaround. However, if you need to have a shorter timeframe for your workflow, you'll want to be aware of the chance that these could be approved out of order.
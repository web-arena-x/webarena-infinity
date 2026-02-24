# Lesson 3: Solving tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408882997530-Lesson-3-Solving-tickets

---

- [Introduction: Getting started with Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408884056346)
- [Lesson 1: Ticket Basics](https://support.zendesk.com/hc/en-us/articles/4408881925786)
- [Lesson 2: Viewing and Organizing](https://support.zendesk.com/hc/en-us/articles/4408883609370)
- [Lesson 3: Solving Tickets](https://support.zendesk.com/hc/en-us/articles/4408882997530)
- [Lesson 4: Business Rules](https://support.zendesk.com/hc/en-us/articles/4408885959066)
- [Where to go next](https://support.zendesk.com/hc/en-us/articles/4408883043226)

Topics covered in this lesson:

[Lesson overview](#overview) [Ticket update notifications to the customer](#notifications) [Ticket type and priority](#type-priority) [Responding to recurring questions](#recurring-questions) [Reviewing a ticket's history](#review-history) [Sharing tickets with colleagues and other Zendesk instances](#sharing-tickets)

## Lesson overview

In this lesson, we'll focus on how agents solve tickets.

Solving a ticket typically involves any or all of the following tasks:

- Telling the customer that you received their request
- Troubleshooting a problem with the customer
- Troubleshooting a problem with another agent
- Reviewing the history of a ticket
- Solving a ticket
- Solving recurring problems

The test ticket you created in the first lesson should still be open in Support. If not, you can find it by clicking the Views icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar. The ticket should be in your list of unsolved tickets. The ticket should look like this, ready for your response:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_ticket.png)

We'll explore the ticket life cycle in more detail in the following sections of this lesson.

## Ticket update notifications to the customer

As an agent, the first order of business is to reply to the customer to acknowledge that you received the support request.

But with Zendesk Support there's no need, we already took care of it for you. When a ticket is created, an email is sent to the customer acknowledging that the ticket was received. We refer to these as *email notifications* and these are automatically sent to the customer after certain types of ticket updates.

When a new support request is received, an email notification is sent to the user to acknowledge that request. A link to the ticket that was created by that support request is included so that customer can track and update the ticket if needed. Alternatively, the end user can also reply back to the notification to update the ticket. Each email reply adds a new comment to the ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_request_received.png)

Many Zendesk customers only interact with their customers via email and don't provide other channels for customers to contact them. You can easily do the same thing and modify your email notification template to omit the link back to the ticket. You can also customize your template and change the visual design to match your branding.

### Introducing triggers

The request received email is an example of a Zendesk *trigger* at work. A trigger consists of one or more actions performed immediately after a ticket is created or updated. A trigger fires when specific conditions are met—in this case, a ticket was created.

There are a number of pre-defined standard  ticket triggers. You can modify them or define your own. We'll cover triggers in more detail in an upcoming lesson.

## Ticket type and priority

You know now that a ticket's status changes as it goes from new to solved. These changes in status are essential for monitoring where each ticket is on its journey to being resolved. There are two optional (but very helpful) ticket properties that are used for sorting and managing your ticket queue. They both can convey how urgently a ticket needs to be addressed.

### Type

The first property is the ticket type and there are four pre-defined choices: Question, Problem, Incident, and Task. The ticket type is optional and selected manually by an agent when triaging a new ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_type_select.png)

**Question** is used to indicate that the requester's issue is a question rather than a problem that needs to be solved.

**Problem** is used to indicate that the requester is having an issue with your product or service that is likely to be experienced by other customers.

**Incident** is used for occurrences of a problem that affects more than one person. Incident tickets are linked to a problem ticket and when the problem ticket is solved all the incidents of that problem are solved automatically at the same time.

**Task** is used when you want to assign the ticket as a task to a specific agent. When you select Task, you also set the Task Due Date.

### Priority

The ticket priority helps you to convey the level of urgency for each ticket and can be used in the rules you set up in Zendesk Support to manage tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_priority_select.png)

There are four values for priority: Low, Normal, High, and Urgent. How you weight the priority of your tickets is up to you. For example, you might assign a ticket to Urgent based on the customer who submitted the request or based on how many hours have passed since the ticket was created.

### A problem and incidents example

To demonstrate how problem and incidents tickets work, imagine that you provide support for a large corporation and suddenly no one has access to the internal wiki and can't get to their documents. Support requests start pouring in. Rather than handle each one individually, you create a new ticket that summarizes the problem. You then link all the individual support requests to that problem ticket. When the problem is resolved, you solve the problem ticket you created and all the incident tickets are automatically solved as well.

## Responding to recurring questions

Some support issues that affect more than one customer aren't the result of something working incorrectly. Sometimes you just have issues or recurring questions that you need a standard reply for. For example, many customers are asking about a feature you don't provide yet or they need to reset their password. To handle these types of recurring requests, you use *macros*.

Macros are pre-defined responses that you can easily apply to any ticket. An example of where a macro is useful is replying to customers' requests to reset a password. Rather than having your agents respond to each of these inquiries by creating separate responses, you create one response that all agents can use.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_macro2.png)

Like views, you can create global macros that all agents can use, restricted macros that only agents in a specific group can use, and personal macros.

Macros can be created from scratch or by saving one of your responses to a ticket.

Macros are a big productivity enhancer and Zendesk includes macros for some common situations to get you started.

Another way to handle recurring questions is to create a knowledge base that your customers can access in your help center so that they can search for and find answers themselves.

### Personalizing your macros with placeholders

It's always best to personalize your communication with customers so that they feel you are speaking directly to them rather than sending them an automated response. With macros, and other notifications to customers, you also need to include customer specific data (for example their name and a link to the ticket). You do this by adding *placeholders*.

Placeholders are references to ticket and user data that you can add into messages to customers. For example, if you want to start your macro with the customer's first name, you add the {{ticket.requester.first\_name}} placeholder. Then, when the macro is processed and the ticket is updated, the customer receives a message that starts "Hello Caitlin!" rather than a generic greeting like "Dear customer".

Try it yourself: Create and apply a macro

### Create and apply a macro

Let's demonstrate how macros work by creating a macro and then applying it to a ticket in Zendesk Support.

First, create the macro, following these steps:

1. Click the **Admin** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_icon.png)) in the sidebar and then click **Go to Admin Center**.
2. Click (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)) **Workspaces** in the sidebar, then select **Agent tools > Macros**
3. Click **Add macro**.

   For this example, we'll create a macro that asks the customer for more information. We'll change the ticket status to Pending (because we need information from the customer and can't proceed until we receive that information) and add a message explaining what we need.
4. Enter a **name** (for example, *Need more information*).
5. Macros contain actions that update the ticket and can generate notifications to the customer. Click **Add action**, then select **Ticket: Status** and **Pending**.
6. Next, add the email notification message by adding another action. Click **Add action** and then select **Ticket: Comment/description**.  
     
   A text box appears.
7. Add this message or something similar:

   Thanks for contacting us {{ticket.requester.first\_name}}. To help you fix this problem we'll need a little more information from you. We need your model number and the serial number (you can find this on the bottom edge of your device).
8. Specify who can use the macro on your team. Select **Available for all agents**.
9. Click **Create**.

Now that you've created a macro, you can apply it to a ticket.

1. Look at your test ticket again.
2. At the bottom of the ticket window, click **Apply Macro**. You'll see the pre-defined macros and also the macro you just created.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_macro.png)
3. Select your macro from the list.  
   The ticket is updated with the actions contained in the macro.
4. Click **Submit** to save the updates and generate the email notification to the customer.

## Reviewing a ticket's history

As mentioned earlier, when a customer replies to an email notification a new comment is added to the ticket. As an agent works to resolve a problem, there may be many messages back and forth between the agent and the customer. We refer to this as the *ticket conversation*. Along the way, a ticket may be updated by macros and other automation tools like triggers that alter a ticket's properties and content.

There are two views of the ticket data: the one we've shown you so far (the ticket properties and comments) and also a ticket's events and notification history.

To see this, look at your test ticket and above the first ticket comment, click the events icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_events_icon.png)) to toggle between ticket conversations and events.

- **Conversations** displays only communication between the agent and the customer, or the agent and other agents.
- **Events** displays all replies, status changes, and so on, applied to the ticket by an agent or a business rule.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/allevents1.png)

We mentioned triggers earlier in this lesson and you know that they're used to automatically update tickets based on some ticket criteria. This events view of the ticket shows you when a trigger updated the ticket. You'll also see when another agent was CC'd on the ticket and so on.

### Merging users and tickets

When users are allowed to self-register in your Zendesk account, they may sometimes create more than one user account. They might also create more than one request for the same support issue. Both of theses situations are easily handled in Zendesk by merging a user's duplicate accounts and by merging multiple support requests for the same issue into a single ticket.

These merge actions are also included in the ticket's event history.

## Sharing tickets with colleagues and other Zendesk instances

The agent assigned to a ticket isn't necessarily the only person who will work on a ticket. In the journey from new ticket to solved ticket any number of agents may be assigned to a ticket. You can also CC other people on a ticket. This includes both agents and end-users. Being able to CC other people allows you to easily collaborate with others who might have the information you need to solve a ticket. Other agents who are CC'd on a ticket can add both public and private comments, while end-users can only add public comments.

Zendesk doesn't limit collaboration on resolving tickets to just the users of your own Zendesk account. If you work with other companies or teams within your own company who use a separate instance of Zendesk Support, you can easily share tickets to those other companies or teams. This feature is called *ticket sharing*.

Ticket sharing allows you to assign tickets to affiliated Zendesk Support accounts and their agents either provide information toward resolving the issue or solve the issue themselves. The ticket status and comments can stay synced between the tickets in each account.

## Formatting your ticket comments

Agents can add headings, bullet lists, and other useful text formatting in comments using *rich content* or they can use a simple text markup called *markdown*. Agents can switch between rich content formatting and markdown [formatting](https://support.zendesk.com/hc/en-us/articles/4408884153242#topic_qgg_xqm_hpb) within the same editor.
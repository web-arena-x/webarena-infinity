# Routing options for queue management in Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4409148772506-Routing-options-for-queue-management-in-Zendesk-Support

---

This article describes some routing options for managing your ticket queues. In general, the approach you use to manage the queue often depends on the number of agents you have and your company's products.

## Managing smaller-to-medium ticket queues

For a support team with small-to-medium number of products or agents, one method of managing the queue is to separate the types of tickets you receive.

For a company with just a few types of products, it's a good idea to separate the tickets based upon which product is associated with the customer request. Separating the tickets can be done a couple of different ways.

### Option 1: Custom drop-down field to your ticket form

Add a custom drop-down field to your ticket submission form in help center so customers can easily select which product they are asking about. See [Adding custom fields to your tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794 "Adding and using custom ticket fields") .

This is the drop-down setup:

![](http://i.imgur.com/IdKfj5r.png?1)

This is the default form without the drop-down:

![](http://i.imgur.com/ztQWK3H.png?1)

This is the form with an example drop-down field added to the default form:

![](http://i.imgur.com/b76P8rb.png?1)

When you set up each field option you can also specify a unique tag to assign to each product type (for example, bear). We'll explain later how these tags are used. 

### Option 2: Support email address

Instead of using a custom ticket field, another way to separate tickets is by using different, product-specific email addresses. For example:

- If a customer has a question about the Bear product, direct them to email your support team at   *bear@YOURCOMPANY.zendesk.com*  or **bear@YOURCOMPANY.com.**
- If a customer has a question about the Lion product, direct them to email your support team at lion*@YOURCOMPANY.zendesk.com*  or **lion@**YOURCOMPANY**.com.**

Then, set up triggers that tag incoming tickets based on which email they have been received at. For example:

![](http://i.imgur.com/tmbV96r.png?1)

For more detail on triggers, see [Creating triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).

### Creating views to organize your tickets

Once tickets are coming in and getting tagged based on your pre-defined drop-down options, you can set up custom views based on these tags. For example, you can create a view that displays all tickets created with the tag for "bear."

When your triggers assign tags based on a product-related email address, you may notice that as soon as a tag is added in tickets, the custom field is also set to the appropriate field option. In other words, emails sent to bear@YOURCOMPANY.com will have a "bear" tag added and the custom field is automatically set to "bear." See  [Using views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570).

Now, create views so that you only see tickets belonging to each product. You can build views with a condition based on the custom field that you created earlier.

Select your custom field from the condition drop-down menu. See example below.

![](http://i.imgur.com/vsSFAFG.png?1)

Here's an example of what the active views will look like with these new views based on a selection from the custom field:

![](http://i.imgur.com/uOZ7VvI.png?1)

Now that your tickets are organized by view, you can create and assign separate groups of agents, one for each view.

## Managing larger ticket queues

If your support team has a lot of agents, one approach is to dedicate an agent to a queue manager (QM) function. Queue managers can perform the following actions:

- Handle the main queue and assign tickets to groups or agents (for example, based on their speciality).
- Quickly scan for trends or potential issues that are happening to many customers at once. See [Streamline support using problem and incident tickets](http://www.zendesk.com/blog/tip-of-the-week-streamline-support-using-problem-and-incident-tickets-2).
- Send tickets requiring a higher-level of specialization or requiring different tools to another team (for example, Engineering, Order Processing, and so on).
- Make sure the difficulty of tickets being assigned are going to the right agent. For example, give new agents the easiest tickets and give seasoned agents the most-difficult tickets.

Beyond the queue manager, it's a good idea to have predefined roles for your agents and groups based on products or ticket channels.

Here are some examples of how to manage larger ticket queues.

### Example: The call center

In this example, you have a large volume of calls coming in covering all aspects of your products. This type of queue is best managed by having a large number of agents and is more likely to be managed by each agent after calls are finished. Once the queue manager assigns tickets to this group (usually simpler tickets that don't require a lot of time) the agents themselves can use the Play button to zap through ticket after ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Y6MtzCH.png)

### Example: The online store

Many online stores leverage email and possibly the help center as the main methods of ticket submission. It is common, however, to direct your customers to a Q & A forum to answer most questions without requiring a ticket submission. Agents who are taking calls can also reply to questions in the community Q&A forums. The benefit is that an agent answering one question on the forum is likely addressing many future questions from future customers who visit that forum. See [Best practices for driving traffic to your knowledge base and community](https://support.zendesk.com/hc/en-us/articles/4408828362522)

### Example: Email only

If you only use email as the channel to submit requests, then in addition to the tips above to aid the agents in organizing and streamlining tickets, it can help to modify ticket properties via email exclusively. For example, you can add a tag using **#tag: bear** to set the product field to **bear**. See  [Updating ticket properties from your inbox](https://support.zendesk.com/hc/en-us/articles/4408839419034-updating-ticket-properties-from-your-inbox)  .

### Example: The all-purpose

This scenario includes using separate agent groups to handle most, if not all, channels of ticket submission and may even use the [Zendesk API](http://www.zendesk.com/support/api). Your groups might look something like this:

- Social messaging group
- Phone group
- Chat group
- Forum moderators
- High priority tickets group
- Email tickets group
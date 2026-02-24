# Lesson 2: Organizing tickets and users

Source: https://support.zendesk.com/hc/en-us/articles/4408883609370-Lesson-2-Organizing-tickets-and-users

---

- [Introduction: Getting started with Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408884056346)
- [Lesson 1: Ticket Basics](https://support.zendesk.com/hc/en-us/articles/4408881925786)
- [Lesson 2: Viewing and Organizing](https://support.zendesk.com/hc/en-us/articles/4408883609370)
- [Lesson 3: Solving Tickets](https://support.zendesk.com/hc/en-us/articles/4408882997530)
- [Lesson 4: Business Rules](https://support.zendesk.com/hc/en-us/articles/4408885959066)
- [Where to go next](https://support.zendesk.com/hc/en-us/articles/4408883043226)

Topics covered in this lesson:

[Ticket views](#views) [Segmenting agents and their tickets with groups](#h_01HS1KV1FX0J4C4W0PK15P82RZ) [Organizing customers](#h_01HS1KV1FXTF03TSW7Z17Y5KK1) [User roles](#h_01HS1KV1FXW9WMJ5JCAD7W5PQY)

## Ticket views

In the previous lesson, we introduced *views*. Views are used to organize your tickets at all stages in the ticket life cycle. In this lesson, we'll take a more in-depth look at how views can be used to organize your tickets. We'll also look at the tools you have available for organizing users. Your users include both your customers and your support staff.

Let's begin with views.

Views are essential for managing the ticket workflow because they enable you to create meaningful groupings of tickets as they progress through the ticket lifecycle.

Zendesk provides some pre-defined, editable views. These views were created for the essential day-to-day running of Zendesk Support and are based on customer service best practices.

Click the Views icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar to see the list of views. Every Zendesk account contains these views to get you started:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_unassigned_tickets_new_thumb.png)

Since views organize tickets based on a ticket's properties, a ticket can appear in more than one view. For example, a new ticket can appear in the Unassigned tickets, All unsolved tickets, and New tickets in your groups views. This is because a new ticket meets all the criteria for how these views were defined.

You can create new views or modify the existing views to suit your needs.

### Shared and personal views

The pre-defined views provided in your Zendesk account are available to all of your agents. These are *shared views.* You can edit these views or create your own views and define who has access to them.

Admins can also create views that only a specific group of agents can see. These are referred to as *restricted views*.

Lastly, all agents can create *personal views* that no one else has access to.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_view_available_for.png)

Try it yourself: Create personal views

### Create personal views

In this video, you can see how to create a personal view for your solved tickets:

Creating a View (1:29)

## Try it yourself

Let's quickly create a new view for the tickets assigned to you, solved or not. Since you created a test ticket in the previous lesson, you'll have one ticket for your view.

1. Click the **Views** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.
2. At the bottom of the list of views, click **Manage views** to open the Views page in Admin Center.
3. Click **Add View**.
4. Enter a title for your new view (for example, *My tickets*).
5. Conditions are used to define what tickets are shown in a view. You can think of conditions as a simple formula for selecting data in tickets. In this example, we're trying to create a view of the tickets that are assigned to you. To do that, click the drop-down list below the label **Meet all of the following conditions**. Select **Ticket: Assignee**. Two more drop-down lists will appear. The first should already be set to **Is**. Now click the next drop-down list and select **(current user)** or your name (either will work) from the list of agents. You've just defined a condition.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_assignee.png)
6. If you want to immediately see the results of the condition you defined, click **Preview**. Your ticket will be displayed in a table.
7. When defining a view you can also define the formatting and who has access to it. For now, accept the default formatting. From the **Who has access** menu select **Only you**.
8. Click **Save**. Congratulations, you've just created your first personal view.

Your new view is listed in **Your views** under the list of pre-defined views in Zendesk Support.

## Segmenting agents and their tickets with groups

You may have noticed that several of the pre-defined views refer to *groups*. In Zendesk Support you organize your agents into groups. When you assign a ticket to an agent you're also assigning it to a group that the agent belongs to (agents can belong to more than one group).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_assignee_groups.png)

You can also assign a ticket to just a group and not a specific agent within the group. Doing this allows the agents within that group to determine who should be assigned to the ticket.

You can create groups of agents for any reason. Typically, groups are used to organize agents by specialty or expertise (product support vs advanced support for example) or by location or language.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_group_new.png)

You can create views that list all the tickets assigned to each of your groups.

It's up to you to think about how you want to organize your tickets and the views your team needs. For example, if you only have a few agents, you might just need an "Unassigned" view where agents can pick tickets to work on. If you have a larger team, it might be a good idea to set up views for each group and have tickets routed accordingly.

Think about how you want to manage your ticket queue and then create the views and groups you need to support that workflow.

### The default group

In Zendesk Support, you'll see a group called Support. This is the default group that you and any agents you add are automatically added to. You can create new groups and add or remove agents from any of the Zendesk Support groups. The default Support group is there because a group is required to assign and solve a ticket.

Try it yourself: Create a group

### Create a group

You can create as many groups as you need to support your unique ticket workflow. In this example, you'll create a new group for your advanced support group. To see how to create a group, take a look at this video:

Creating a Group (0:57)

If you'd like to try creating a group, follow these steps:

1. Click the **Admin** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_icon.png)) in the sidebar, then select **Go to Admin Center**.
2. In Admin Center, click (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) **People** in the sidebar, then select **Team > Groups**.
3. Click **Create Group**.
4. Enter a name for your new group (for example, *Advanced support*).
5. Select your name the list of all Zendesk Support agents.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Create_Group_Get_Started.png)
6. Click **Create group**.

You now have two groups: the default *Support* group and the *Advanced support* group you just added. We'll show you how to use this group shortly.

## Organizing customers

To help manage your support workflow, you can add each of your customers to one or more *organizations*. You can then provide different types of support for each organization.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_org_list_new.png)

The default organization a user belongs to is associated with every ticket they create and can be used to automate how incoming tickets are handled.

Common uses of organizations include supporting a service level agreement you have with customers, tracking and managing tickets by company names or email domain, and by location or language.

You can also use organizations as a way to control access to Zendesk Support tickets. You can allow specific users to see all the other tickets in their organization, which gives them visibility into Zendesk Support issues that affect the entire organization. Doing this may prevent additional tickets from being created for a support issue that affects an entire organization (for example, an essential application being temporarily unavailable to everyone).

You can also add agents to organizations. You might do this to restrict an agent's access to only tickets from a specific organization (Note: you can also restrict an agent's access to the tickets in a specific group). And you can automatically assign tickets from an organization to a specific group.

## User and organization tags

Both the user profile and organization profile can contain additional information that can be used to customize your Zendesk Support workflow. You can add *tags* to both and use these tags to automatically assign or track tickets.

For example, if you add a tag called premium\_support to a user or an organization, that tag is automatically added to every ticket from that user or users within that organization. You can then, for example, use the tag to define a new view that tracks your premium support tickets.

Try it yourself: Create an organization

### Create an organization

Zendesk Support doesn't contain any default organizations. If you choose to use organizations, you will need to create them. To see how to create organizations, take a look at this video:

Creating an Organization (1:01)

If you'd like to try creating an organization, follow these steps:

1. Open a new support ticket as you did before. Ensure that the ticket has a requester name that you haven't already added to an organization. You could create a new user for testing purposes.  

   You'll see that there are three tabs within the ticket. The first is the **Organization** tab, the second is the **User** tab, and the third is the **Ticket** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_org.png)
2. To create a new organization, click **Organization (create)**.
3. You'll be prompted to enter an organization name. Enter a name. For example, you might just call this organization *Customers*.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Create_Org_Get_Started.png)

   You can additionally add one or more email domains, which will automatically add every other new user with the same email domain into this organization. You'd probably do that if you're providing support to specific companies and want to segment them into organizations. For example, every user from @somecompany.com could be added to an organization called Some Company. You can skip this for now and add it later if you need to.
4. Click **Add**and the new organization is created and added to the user's profile as associated with the ticket.

## User roles

So far we've talked about agents and customers. These are the two primary user roles involved in Zendesk Support transactions. Customers have issues that need to be fixed and agents fix them. However, there are several other user roles that you should be aware of.

First, be aware that the term *customer* is often used interchangeably with *end user*. Both refer to the people who use Zendesk Support to request assistance.

Now let's look at the Zendesk Support staff roles. You know about the *agent* role. Agents primarily solve tickets. However, you can assign specific permissions to agents to control their access to the different parts of your Zendesk. For example, you can allow just a few agents to manage and moderate your Help Center.

In addition to agents, there is the *administrator* role. You can have one or many administrators in your Zendesk account. You can think of this role as the manager of your Zendesk account. They set up your account with the channels you want to support, define new shared views, manage users, and so on.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_user_roles.png)

If you originally created your Zendesk account, you are the *account owner*. This role is the super administrator role and can do everything that's possible to do in Zendesk.

## Custom agent roles

On Enterprise plans, you can create custom agent roles. In other words, you can craft a role specifically designed to support your workflow from a list of permissions. We've defined some common roles that you can use as is or customize.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gsg_roles_enterprise.png)

Try it yourself: Add a new agent and assign them to a group and organization

### Add a new agent and assign them to a group and organization

Now that you have an understanding of the Zendesk Support user roles, let's add a support agent. To do this, you'll need to use an email address that hasn't already been used in your Zendesk account. In other words, you can't use the email address you used to create your Zendesk account.

This video shows you how to add an agent to Zendesk Support:

Adding an Agent (1:15)

1. In Support, position your mouse over the **Add** tab in the top toolbar, then click **User**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_user_add.png)
2. Enter the name and email address of your new agent.
3. Select **Staff member** as the user type.
4. Click the **Role** drop-down list and select **Agent**. Then, click **Add**.

   This new user's profile is displayed. Here you can add your new agent to other groups, define their access to tickets and other parts of your Zendesk account, and add any other user profile information you want.
5. Click the **Groups** field.  
   You're prompted to add the agent to another group. Select the *Advanced support* group you created earlier.
6. Now set the agent's access permissions. Click the **Access** field and select **Tickets in agent's org**.
7. To complete the agent's access restriction, click the **Org.** field and select *Customers*.

That's it, you're done. Zendesk automatically saves the changes you make to a user's profile. You've just added an agent, added them to a group, and restricted their access to only tickets within the *Customer's* organization.
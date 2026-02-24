# Prompting guidelines and examples for App Builder

Source: https://support.zendesk.com/hc/en-us/articles/9037913973146-Prompting-guidelines-and-examples-for-App-Builder

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

The App Builder leverages natural language processing (NLP) to interpret user prompts and
transform them into actionable app components. To maximize the effectiveness of this
tool, it's important to provide clear and precise prompts. This article outlines key
guidelines for crafting effective prompts for communicating your needs effectively to
the App Builder. It also includes some examples of how to use the App Builder prompt
framework to help you narrow in on what you’re working towards.

By following these guidelines and framework example, you can ensure that the LLM
understands your requests accurately, resulting in a smoother app development process
and better outcomes.

This article includes these sections:

- [Best practices for effective prompting](#topic_e12_qbx_zgc)
- [Guidelines for App Builder prompts](#topic_gzx_xgj_4fc)
- [Framework for App Builder prompts](#topic_mzb_23j_4fc)
- [Prompt examples, using MAPS principles](#topic_oyq_11l_4fc)
- [Customer-built app examples](#topic_bkw_d1l_4fc)

## **Best practices for effective prompting**

Following these best practices will help you minimize the number of prompts needed
while generating more accurate and efficient results from App Builder.

- **Focus prompts on building your app**: App Builder is optimized to help you
  design and refine your apps, connect APIs, and set up integrations. It provides
  high-level assistance for app construction but is not a replacement for
  step-by-step setup instructions. For specific tasks like finding API credentials
  or connecting third-party systems via API Key or OAuth, use official
  documentation or trusted resources such as Google Search or ChatGPT. This frees
  up your App Builder prompts for the actual app logic and feature building.
- **Know when to seek additional help**: If you’ve tried troubleshooting the
  same error several times (for example, after three or four prompt attempts) and
  are still unable to move forward, [contact Zendesk Customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850) with
  your error details.
- **Clearly describe errors and expectations**: When your app encounters an
  error during testing, explain exactly what went wrong and what you expected to
  happen. Detailed feedback helps the AI address the issue more efficiently.
- **Share debugging details for unresolved issues**: If repeated fixes are
  unsuccessful, clearly state this in your prompt. Ask the AI to generate
  extensive debugging information in the console, then reproduce the error and
  paste the output back into the conversation.
- **Batch cosmetic and simple changes**: To optimize prompt usage, group minor
  adjustments (such as layout tweaks, button styles, or tab order) into a single
  prompt instead of sending multiple separate requests.
- **Customize test mode with ticket search**: Use the ticket search in Agent
  Workspace to change tickets while testing your app. This enables quick scenario
  validation without extra prompts.
- **Provide examples for private or unknown APIs**: If you’re using an API that
  App Builder doesn’t recognize, include both a sample API request and the
  expected response. This improves the AI’s accuracy and reduces wasted
  iterations.
- **Test in both light and dark mode**: If any agents use [dark mode](https://support.zendesk.com/hc/en-us/articles/9011095783322), be sure to test your app in
  both themes to catch and resolve visual issues early.
- **Save your blueprint before deleting conversations**: Before deleting a
  conversation, save the `blueprint.md` file from the Code tab. It
  contains your app’s design summary and is important for future revisions.
- **Adjust app name and icon via Settings**: Update your app’s name and icon
  directly in the Settings tab rather than through prompts.
- **Apps run inside Agent Workspace**: App Builder apps operate within the
  Agent Workspace environment and run only while that workspace is open. If you
  need background or persistent workflows, use Action Builder, ZIS, or external
  tools like Workato, Zapier, AWS Lambda, or Heroku.
- **Plan requirements before building**: Outline your app’s goal, workflow,
  data requirements, and preferences before you start. This helps the AI deliver a
  strong first version and often results in a faster build than filing a support
  ticket.

## **Guidelines for App Builder prompts**

Best practices for writing prompts when using the Zendesk App Builder, include:

- **Use clear and simple language** 
  - Write prompts in natural, straightforward sentences as if
    explaining your needs to a colleague.
  - Avoid technical jargon or programming terms that you do not
    explain or that users wouldn’t know.
  - Be direct about what the app should do.

- **Be specific about desired functionality** 
  - Clearly state what data sources the app should use (for
    example, Google, Jira, internal database).
  - Specify the core features or actions the app should have (such as
    display order status, submit escalation form).
  - Include any critical data points or outputs you want
    visible.

- **Include the user context or role** 

  This helps the App Builder
  tailor the interface and functionality accordingly.

  - Mention the primary users of the app (for example, agents,
    supervisors).
  - Describe the context in which they will use the app (for
    example, while handling support tickets).
- **Break down complex requests** 

  This reduces errors and helps you better understand each feature.

  - If the app needs multiple functions, try splitting requests
    into smaller parts and build iteratively.
  - Start with a basic app prompt, then refine by adding features
    or details step-by-step.
- **Use examples and visual expectations** 
  - If possible, describe how you want the app’s output to look
    (list, button, graph).
  - Referencing tangible elements helps the builder create
    intuitive interfaces.

- **Request iterative improvements** 

  An iterative cycle allows you
  to test and improve the app one feature at a time instead of all at once,
  leading to better final apps without coding.

  - After the first version is generated, review and provide
    feedback: what works, what doesn’t.
  - Use natural language to specify changes (for example, “Add a
    button to refresh data” or “Show only open tickets”).

- **Focus on practical benefits**

  This keeps the app focused on
  delivering value, which ensures relevance and usability.

  - Frame prompts around the problems to solve or tasks to
    simplify for agents.

- **Avoid ambiguity** 
  - Don’t leave vague terms like “show relevant info” without
    explaining what “relevant” means.
  - Ambiguity can lead to apps that don’t meet your
    expectations.

By following these best practices, users without coding experience can
write effective prompts to create useful, custom support apps.

## **Framework for App Builder prompts**

When writing a prompt, you’re giving the App Builder instructions in a way that’s
similar to giving instructions to a developer to create an app for you.
It’s helpful to have a plan for what you want to accomplish. The following framework
lets you and the App Builder know what you’re expecting, which helps you focus on
what you’re working towards more effectively.

Without this type of direction, App Builder will build an app, but it may not meet
your needs. App Builder will try, even if your prompt is *Build an app*.
However, if you need a particular app, the more you guide the App Builder, the more
likely you’ll be to get what you need.

When writing prompts, consider these MAPS principles: Mission, Action,
Parts, Scope

- **Mission**: What the app is meant to do. Consider the current need
  and context.
- **Action**: What the AI should generate. Consider core
  functionality and workflows.
- **Parts**: What the UI or structural parts are. Consider the look
  and feel components.
- **Scope**: Who or what it’s for. Consider constraints and audience.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_maps.png)

By using MAPS principles, if you’re not sure or don’t like something, you
can change the action, scope, or parts without changing the other sections.

## Prompt examples, using MAPS principles

Here are some prompt examples using MAPS principles:

**Example 1**: My Recent Satisfaction Comments app

- **Mission**: This app is built for agent satisfaction and
  allows a feedback loop for agents so that they have insight into the
  customer's satisfaction history to guide interactions and improve service
  quality.
- **Action**: Create a side panel app that retrieves and displays
  the five most recent ticket satisfaction comments and trends covering the
  last six months.
- **Parts**: Don’t display the date and satisfaction score.
  Display the five most recent ticket satisfaction comments in a table and
  6-month trends in a compact line chart. Include tabs to switch between
  individual ticket satisfaction comments and trends. Make the comment column
  the full width of the app. Give the background of each container a slight,
  faded shade of green if the satisfaction rating was good, and a slight,
  faded shade of red if the satisfaction rating was bad.
- **Scope**: This app is for agents viewing support tickets.
  Display ticket satisfaction comments for only the current requester and only
  tickets with the same brand or organization.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_customer_satisfaction_insights.png)

**Example 2**: Customer 360 app

- **Mission**: This app is designed to boost agent efficiency by
  displaying key customer information directly within the ticket view, giving
  agents quick access to the details they need to resolve issues without
  navigating away.
- **Action**: Create an app that retrieves and displays the
  customer information, purchase history, and customer loyalty information
  from our internal CRM database.
- **Parts**: Display customer information, purchase history, and
  customer loyalty information in 3 separate tabs. Visually indicate the tab
  that is currently viewed. Highlight information in yellow if the customer
  loyalty is low. Add a button to refresh the displayed data to reflect the
  latest changes.
- **Scope**: This app is for agents viewing support tickets.
  Display this information for only the current requester and only tickets
  with the same brand or organization.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_customer_360.png)

## **Customer-built app examples**

Here are some examples of apps created by Zendesk customers:

**Assignee Change Tracket app**: An app that captures all the ticket assignment
changes in a table and shows the total number of ticket assignments that happened.
This is available for admins and team leads to use. It took an admin less than 30
minutes to build this app.

**Prompts**

- Create an app that tracks changes on an assignee on a given
  ticket. Make sure to display assignee names of previous assignees and new
  assignees. Also display the total number of changes in assignment of the
  ticket.
- Add a button to refresh the displayed data to reflect the latest
  changes. Add another button to export data to excel. Make both buttons small
  and next to each other.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_assignee_change_tracker.png)

**My Recent Satisfaction Comments app**: An app that displays the five most recent
CSAT comments on a ticket. They are intending to use this app as a replacement for
the CSAT comments that used to be displayed at the top of the ticket, which was
removed from the conversation log when they updated to the newer version of
Zendesk’s built-in CSAT tool. It took an admin one hour to build this app and deploy
it to production. This app is built for agent satisfaction and allows a feedback
loop for agents so that they know how customers are feeling after each
interaction.

**Prompts**

- Create an app that shows the five most recent ticket satisfaction
  comments.
- Update the app to only show ticket satisfaction comments for the
  current user.
- The app is still showing the five most recent ticket satisfaction
  comments across all users rather than just the current user.
- Remove the date and score columns. And make the comment column the
  full with of the app.
- Give the background of each container a slight, faded shade of
  green if the satisfaction rating was good, and a slight, faded shade of red
  if the satisfaction rating was bad.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_my_recent_satisfaction_comments.png)

**User Data app**: An app that displays the requester’s ticket data, full ticket
history, and ticket attachments.

**Prompts**

- Create a Knowledge or Explore report of the user’s ticket data
  where created date, closed date, and ticket ID are provided. The button for
  the report should create the report first, then set it as downloadable.
- See the customer’s ticket history where all ticket statuses are
  shown in the order of New>Open>Pending>Solved>Closed.
- Download all files sent as attachments in the ticket.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_user_data.png)

**My Insight app**: An app that allows agent visibility into the top five ticket
topics or categories they’ve solved within the last six months.

**Prompts**

- Create an app for an agent to see their top five topics or
  categories they’ve solved tickets in within the last six months, based on
  the number of tickets within the last six months as well as based on the number of tickets by
  ticket forms and what the CSAT is for each. Make the category names reflect
  a B2C retail and ecommerce use case and just make up mock data. There should
  be no N/A% or 100% CSAT scores. Add a column for AHT and Average Full
  Resolution Time.
- Add a filter that allows the agent to slice and dice the data by
  period and also add an agent assignee count to each category.
- Reassignments must be average, not total number, within each
  category. Also, add a column of how the Avg. Resolution time compares
  to the team benchmark using the green, yellow, and red traffic light system
  tag.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_my_insights.png)

**User & Org Details app**: An app that displays user and org details
including custom user fields and custom organization fields with collapsible
sections.

**Prompts**

- Create an app that shows user and org details including all the
  custom user fields and all the custom org fields.
- Thanks. Would you please get the name of custom user and org
  fields rather than the key? Also, let’s rename the app User & Org
  details.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_user_org_details.png)

**Ticket Pulse app**: An app that displays the requester’s recent activity,
specifically the five most recent tickets with their associated information.

**Prompts**

- Create an app that displays the latest five tickets for the
  current ticket requester. I want to display the number of the ticket and
  subject and link that can be redirected to open it in new tab.
- Can ticket be opened in a new tab inside Zendesk?
- Can you make the UI more user friendly?
- Give it another cooler name.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_ticket_pulse.png)

**Salesforce Account Details app**: An app that displays the Salesforce account
details for the ticket requester.

**Prompts**

- Use the Zendesk API to reach out to the Salesforce API and
  retrieve the Salesforce account details for the ticket requester.
- Now, for testing purposes to show how the app would look, have the
  app return mock test values for each of the Salesforce fields without
  actually reaching out to the Salesforce API.

**Resulting app**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_builder_salesforce_account_details.png)
# Viewing and using the automation potential report to create or enhance AI agents (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/9877546283930-Viewing-and-using-the-automation-potential-report-to-create-or-enhance-AI-agents-EAP

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

The automation potential report is
currently in an early access program (EAP). You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLScdW2g4QEYw7nGh_OaVp3EpTZscZzLs7SJcD6DrswMAFWboOw/viewform).

The automation potential report is a powerful tool that shows you how to leverage AI
agents to automatically answer customer questions. The report analyzes your last 30 days
of ticket data and provides insights on how you can increase your ticket automation
rates.

Specifically, the automation potential report shows you areas where you:

- Already have help center content that could be leveraged by a new AI agent to
  automatically answer customer questions.
- Need to create help center content to allow an existing AI agent to answer customer
  questions.

In addition, every insight in the report is tied to projected cost and time savings,
allowing you to prioritize automations with the biggest business impact. From the
report, you can quickly jump to creating a new AI agent or enhancing an existing one,
guiding you through the automations step by step.

You must be an admin to view the automation potential report.

This article contains the following topics:

- [Viewing the automation potential report](#topic_ncg_l2y_4hc)
- [Viewing customer questions that could be answered by an AI agent](#topic_w1c_m2y_4hc)
- [Automatically generating help center articles to close knowledge gaps](#topic_tk5_m2y_4hc)

## Viewing the automation potential report

You can view the automation potential report in Admin Center. The report’s results
are segmented by brand, as you can have only one AI agent per brand. Within each
brand's report, you can see the predicted automation potential, including cost and
time savings, calculated based on a subset of tickets in your account.

To be included in the subset used for calculation, tickets must meet all of the
following criteria:

- One-touch tickets (solved with only one agent reply)
- On one of the following channels: Web form, Email, Web service (API), or Web
  Widget
- In a Closed or Solved status
- Have had only one assignee
- Ticket is public (no private tickets)
- In a public group
- Solved in the last 30 days

**To view the automation potential report**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **View automation insights**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_automation_potential_view.png)

   The automation potential
   report appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_automation_potential_report.png)
3. (Optional) Use the brand selector to the right of the report name to select
   the brand you want to view information for.
4. Review the report’s information:
   - The following high-level metrics estimate the time and money you
     could save by implementing the suggestions in the report:
     - **Estimated automated resolution rate**: The percentage
       of tickets that could be automatically resolved using
       knowledge content and AI agent capabilities. This percentage
       is calculated by comparing the number of one-touch tickets
       to the total tickets with that same topic.
     - **Estimated cost savings**: The estimated amount of money
       your organization could save by applying the suggestions in
       the automation potential report. This amount is calculated
       by multiplying the number of potentially automated tickets
       by the average cost per ticket (benchmarked at $3.50 USD).
     - **Estimated agent time savings**: The estimated number of
       hours your agents could save if you apply the suggestions in
       the automation potential report. This number is calculated
       by multiplying the number of tickets that could be automated
       by average ticket handle time (benchmarked at 10 minutes per
       ticket).
   - The Conversation insights section includes the following tabs that
     explore the topics your customers are submitting tickets about and
     whether you can handle these automatically:
     - **Ready to automate**: Shows the topics that customers
       are asking about that can be automated right away based on
       information you already have in your help center. See [Viewing customer questions that could be answered by an AI agent](#topic_w1c_m2y_4hc).
     - **Knowledge gaps**: Shows the topics that customers are
       asking about that can’t currently be answered based on
       information in your help center. See [Automatically generating help center articles to close knowledge gaps](#topic_tk5_m2y_4hc).

## Viewing customer questions that could be answered by an AI agent

In the automation potential report, the Ready to automate tab shows topics, grouped
into similar categories, where you already have articles in your help center that an
AI agent could use to automatically answer your customers’ questions. From this tab,
you can quickly create a new AI agent that can answer customer questions on these
topics, increasing your automation rates.

**To view customer questions that could be answered by an AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **View automation insights**.
3. Select the **Ready to automate** tab.
4. Click a category to expand it and review its information.

   Tip: Categories are marked as high,
   medium, or low impact based on their estimated automation rate, cost
   savings, and time savings. For the biggest benefit, prioritize
   high-impact categories.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_automation_potential_ready_to_automate.png)

   Here, you can see how many
   tickets your customers submitted that matched this category. You can also
   see the estimated automation rate, cost savings, and time savings for this
   category specifically.

   Within the category, you can see individual topics
   that you already have help center articles about, which could be used by
   an AI agent to answer customer questions about these topics. You can
   also see example tickets related to this category, which you can open to
   confirm that the topic and the conversation in the ticket
   match.
5. Hover over a topic within the category and click **View sample
   response**.

   A panel on the right appears, showing how an AI agent
   could use your existing help center content to answer a hypothetical
   question from a customer about this topic.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_automation_potential_sample_response.png)
6. Repeat the step above for as many topics as you want to view sample
   responses for.
7. Click **Create AI agent** to [create a new AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578).

After the AI agent is [published](https://support.zendesk.com/hc/en-us/articles/7232810932250), your new AI agent can use your existing help
center content to generate answers to customer questions about any of the topics,
across all categories, identified in the automation potential report.

## Automatically generating help center articles to close knowledge gaps

In the automation potential report, the Knowledge gaps tab shows topics, grouped into
similar categories, where you don’t currently have any help center articles that the
AI agent can use to answer customer questions about the topic. From this tab, you
can quickly create articles using generative AI to fill these gaps and automate
future tickets on these topics.

**To automatically generate an article to close a knowledge gap**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **View automation insights**.
3. Select the **Knowledge gaps** tab.
4. Click a category to expand it and review its information.

   Tip: Categories are marked as high,
   medium, or low impact based on their estimated automation rate, cost
   savings, and time savings. For the biggest benefit, prioritize
   high-impact categories.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_automation_potential_knowledge_gaps.png)

   Here, you can see how many
   tickets your customers submitted that matched this category. You can also
   see the estimated automation rate, cost savings, and time savings for this
   category specifically.

   Within the category, you can see individual topics
   that would benefit from a help center article. You can also see example
   tickets related to this category, which you can open to confirm that the
   topic and the conversation in the ticket match.
5. Hover over a topic you want to create a help center article for and click
   **Generate article draft**.

   You’re taken to the article editor in
   Knowledge, where the draft of an article is automatically generated for
   you based on your ticket data from the last 30 days.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_automation_potential_generated_article.png)
6. Review the content of the article and [edit it](https://support.zendesk.com/hc/en-us/articles/9185667124506#topic_ixw_bww_cfc) as necessary.
7. [Configure the article’s settings](https://support.zendesk.com/hc/en-us/articles/4408839258778#topic_bpt_tdq_cy),
   including its viewer permissions and placement within your help center.

   Note: If you restrict the article’s viewer
   permissions, see [Using restricted help center
   content in AI agent responses](https://support.zendesk.com/hc/en-us/articles/8087943201306) for information on how the
   AI agent can use its content in responses to customers.
8. [Save and publish](https://support.zendesk.com/hc/en-us/articles/4408839258778#topic_ngr_25x_cfc) the article.

After the article is published, your AI agent can begin using it to generate answers
to customer questions after it has been reindexed by your help center, which usually
takes a matter of minutes.
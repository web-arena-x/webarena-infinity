# Reviewing and implementing AI recommendations to automate tasks

Source: https://support.zendesk.com/hc/en-us/articles/9598690362010-Reviewing-and-implementing-AI-recommendations-to-automate-tasks

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Explore AI-powered recommendations to automate tasks and optimize ticket workflows. Review suggestions for triggers, autoreplies, and unused business rules based on ticket intent, sentiment, language, and entities. Improve auto assist setups and review AI-generated procedure drafts. Take action or dismiss recommendations, and track changes in the recommendations archive. Enhance efficiency by reducing manual tasks and improving response times.

As you begin to use Copilot in your account, a list of AI-powered recommendations are provided and updated weekly on the Recommendations page in Admin Center, in [Admin Center Home](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_whk_vpj_fcc), and contextually on relevant Admin Center pages.

These recommendations provide actionable guidance on how you can automate tasks and optimize your ticket workflows by creating triggers and autoreplies based on tickets’ intent, sentiment, language, and detected entities, as well as guidance for reviewing unused business rules and macros. Recommendations also provide guidance on improving your auto assist set up and alert you to when there are new AI-generated procedure drafts to review and publish.

This article includes these sections:

- [Understanding Copilot recommendations](#topic_dr3_qqy_hgc)
- [Taking action on recommendations](#topic_fj4_s4f_p2c)
- [Viewing the recommendations archive](#topic_zbz_pm2_fhc)
- [Examples of recommendations](#topic_bs3_xqy_hgc)

Related articles:

- [Monitoring and optimizing effective AI setup in your account](https://support.zendesk.com/hc/en-us/articles/8997125297946)

## Understanding Copilot recommendations

Copilot recommendations proactively identify opportunities to automate repetitive tasks, improve ticketing workflows, clean up unused business rules, and tailor Zendesk AI to your needs.

Depending on your ticket data, your personalized recommendations may include:

- Suggestions for new or updated triggers and autoreplies based on tickets’ intent, sentiment, language, and detected entities.
 [Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)
 must be turned on and configured in your account to see these recommendations.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_recommendation_autoreply_example.png)

 See [Examples of recommendations](#topic_bs3_xqy_hgc)
 below for more information.
- Suggestions to review unused triggers, automations, and macros.

 These recommendations help you manage your business rules and macros that build up over time.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_recommendation_stale_trigger.png)
- Guidance for improving your auto assist setup, including recommendations for reviewing procedures with a high takeover rate.

 For example, say you have a procedure where agents took over in 42% of interactions. Copilot may make a recommendation to review the procedure.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_recommendations_procedure.png)
- Procedure recommendations to help improve auto assist quality and reduce the time you spend writing procedures. Each recommendation may contain up to three [AI-generated procedure drafts](https://support.zendesk.com/hc/en-us/articles/10140109521178#topic_efr_gbc_xhc)
 per brand.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_recommendations_procedures_auto_gen.png)

 Procedure recommendations are based on your top ticket intents or common customer support issues, existing relevant solved tickets, and existing knowledge articles.

Before implementing a recommendation, you can view information and supporting insights, including:

- What actions the recommendation will perform.

 Recommended triggers can include actions for routing to an agent or group, or updating the ticket type, priority, form, or status. Recommended autoreplies include actions for sending automatic responses.
- How your resolution time could improve, how you can reduce time spent on certain tickets, or how the recommendation will help agents.
- How many tickets in a certain period of time had the detected intent, sentiment, or entity, what percentage of those tickets had a certain action taken, and how much time was spent manually performing this action on average.
- When a business rule or macro was last used.

If you want to take action on a recommendation, click the link to navigate to the relevant page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_hub_new_recommendations.png)

If you choose not to act on a recommendation, you can provide feedback about why you dismissed it so that your future recommendations are more accurate and useful over time. You might want to dismiss recommendations that aren’t relevant, are already automated, or that need different logic.

As an admin, you always have full control over what recommendations are implemented in your account. Any decisions and actions about recommendations require your approval. You can view all accepted and dismissed recommendations from the recommendations archive.

## Taking action on recommendations

Relevant recommendations are updated weekly. All Copilot customers will be able to see the Recommendations page, but you might not have recommendations.

See [Examples of recommendations](#topic_bs3_xqy_hgc)
to view examples of the types of recommendations you may see in your account.

**To take action on a recommendation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Admin copilot > Recommendations**.
2. To quickly find a recommendation type, click **Filter**.
3. In the **Feature** menu, select one or more options, then click **Apply filters**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_recommendations_filter.png)
4. To learn more and take action, click a recommendation to expand it.

   Depending on your ticket data, the options available to you will differ:

   - To create a recommended trigger or autoreply, click **Review trigger**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_hub_recommendation_new1.png)

     The Create ticket trigger page opens with prefilled trigger information.

     Review the prefilled information and enter a **Trigger name** and **Trigger category**.
     Click **Create trigger**.
   - To review an unused business rule or macro, click the button to navigate to the relevant page.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_recommendation_stale_trigger.png)

     Review the unused trigger, automation, or macro and delete it if necessary.
   - To improve an auto assist procedure, click **Edit procedure**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_recommendations_procedure.png)

     [Edit the procedure](https://support.zendesk.com/hc/en-us/articles/9012170900890#topic_pd3_k44_xcc)
     as needed and click **Publish**.
   - To review an AI-generated procedure draft, click the name of one of the procedures in the recommendation to open it in Knowledge admin.

     Alternatively, click **Review procedures** to open your list of procedures in Knowledge admin.
   - ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_recommendations_procedures_auto_gen.png)

     You can review and edit the procedure draft and must publish it before it's available to auto assist. See [Reviewing and publishing AI-generated procedures for auto assist](https://support.zendesk.com/hc/en-us/articles/10140109521178).

   When you're done, return to the recommendation.
5. Open the **Actions** menu at the bottom of the recommendation and select **Mark as done** to remove it from the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_hub_recommendation_mark_done.png)

   If you don’t want to take action on a recommendation, select **Dismiss** to remove the recommendation from the list.

   You can optionally give feedback about a recommendation you dismiss.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_hub_recommendation_feedback.png)

   It's important to share your feedback to help improve the accuracy and relevance of future recommendations.

## Viewing the recommendations archive

Recommendations that are marked as done or are dismissed are added to your recommendations archive for you to review as needed.

**Viewing your recommendations archive**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Admin copilot > Recommendations**.
2. Click **View archive**.

   Your Recommendations archive opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_recommendations_archive2.png)
3. Click an archived recommendation to learn more.

## Examples of recommendations

The examples in this section describe the different types of recommendations you may see in your account.

### Intent-based trigger recommendation example

| | |
| --- | --- |
| **Recommended action** | Route specific tickets to group: Support |
| **Expected improvement** | Resolution time could improve by 1h |
| **Description and rationale** | Tickets with some intents tend to be routed to the same agent group. Automate this action to reduce manual triage and help improve resolution time. |
| **Supporting insights** | - 167 tickets (88%) had the intent: Graduation ceremony date. - Most of these tickets (16.7%) were   routed to the same group:   Support. - On average, it took 1h to manually   route each ticket. This could be   reduced through automation. |

### Intent-based autoreply recommendation example

| | |
| --- | --- |
| **Recommended action** | Send an autoreply to tickets with intent: Transaction failed (+4 more) |
| **Expected improvement** | Resolution time could improve by 1h |
| **Description and rationale** | Tickets with some intents tend to be answered with the same reply. Automate this action to reduce manual work and help improve resolution time. |
| **Supporting insights** | - 167 tickets (88%) had the intent:   Transaction failed, Battery   charging issue, Rate lock request   accepted, How to enroll in employee   benefits, Sending late arrival form. - Most of these tickets (16.7%) were   answered with the same   reply. - On average, it took 1h to manually   route each ticket. This could   be   reduced through automation. |

### Sentiment-based recommendation example

| | |
| --- | --- |
| **Recommended action** | Automatically set ticket priority to High or Urgent for tickets with negative sentiment |
| **Expected improvement** | Improve agent response times and reduce escalation risk |
| **Description and rationale** | Negative-sentiment tickets are usually urgent. By increasing ticket priority automatically, these cases can be addressed right away. It’s a way to improve customer satisfaction and prevent churn. |
| **Supporting insights** | - In the last 30 days, 23 tickets (12%)   were assigned negative   sentiment. - 28% of escalations came from delayed   responses to these   tickets. - On average, it took 6 hours per   ticket to update priority manually.   This   could be reduced through automation. |

### Entity-based recommendation example

| | |
| --- | --- |
| **Recommended action** | Change ticket type for entity: Account error |
| **Expected improvement** | Resolution time could improve by 1h. |
| **Description and rationale** | Tickets with some entities tend to have their ticket type changed to the same one. Automate this action to reduce manual triage and help improve resolution time. |
| **Supporting insights** | - 167 tickets (88%) had one of these entities: Account error - Most of these tickets (16.7%) had   their ticket type changed to:   Problem - On average, it took 1h to manually   triage each ticket. This could   be   reduced through automation. |

### Language-based recommendation example

| | |
| --- | --- |
| **Recommended action** | Route specific language tickets to group: Iberia support team |
| **Expected improvement** | Resolution time could improve by 54min. |
| **Description and rationale** | Specific language tickets tend to be routed to the same group. Automate this action to reduce manual triage and help improve resolution time. |
| **Supporting insights** | - 4370 tickets (10%) were assigned this language: Spanish - Most of these tickets (98%) were   routed to the same group:   Iberia support team - On average, it took 54min to   manually route each ticket. This   could be   reduced through automation. |
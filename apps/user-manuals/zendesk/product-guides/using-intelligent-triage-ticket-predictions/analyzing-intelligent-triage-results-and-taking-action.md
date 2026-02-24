# Analyzing intelligent triage results and taking action

Source: https://support.zendesk.com/hc/en-us/articles/5201262314266-Analyzing-intelligent-triage-results-and-taking-action

---

Intelligent triage is an AI-powered feature that automatically detects what a ticket is about (its intent), what language it's written in, and whether the customer's message is positive or negative (its sentiment). You can use this information to route tickets to the right groups automatically, create views to group similar types of requests, and report on trends in the types of tickets your customers are submitting.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Intelligent triage uses AI to detect ticket intent, language, and sentiment, helping you streamline workflows. Start by understanding how it works, enabling it, and building reports to analyze trends. Identify prevalent intents and languages, group similar ones, and address negative sentiments. Focus on key metrics like CSAT and first response time, and iteratively refine workflows based on agent feedback.

Intelligent triage is an AI-powered feature that automatically detects what a ticket is
about (its intent), what language it's written in, and whether the customer's message is
positive or negative (its sentiment). You can use this information to route tickets to
the right groups automatically, create views to group similar types of requests, and
report on trends in the types of tickets your customers are submitting.

Because intelligent triage can affect different areas of your ticket workflows, you might
not know exactly where to start at first. This article discusses some best practices for
gathering, analyzing, and acting on intelligent triage information.

For more information about intelligent triage, see [Intelligent triage resources](https://support.zendesk.com/hc/en-us/articles/4471123173402).

This article contains the following topics:

- [Gathering intelligent triage data](#topic_vdx_fxp_rvb)
- [Analyzing and fine-tuning the results](#topic_mth_3xp_rvb)

Related articles:

- [Using intelligent triage to identify and act on
  ticket escalations](https://support.zendesk.com/hc/en-us/articles/6353620565530)

Note: When creating reports in Explore, intelligent triage
prediction values are available only in English. However, intelligent triage is
capable of evaluating content in the languages listed [here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

## Gathering intelligent triage data

Intelligent triage can have a powerful effect on your agents' workflows, saving them
anywhere from 30 to 60 seconds per ticket by automatically identifying and routing a
ticket based on its intent, language, or sentiment.

However, before you make any changes to your triage or routing workflows, it's
helpful to understand exactly how intelligent triage categorizes the tickets in your
account. Getting to know the specific intent values and trends in your account will
help you decide which workflow changes will best improve the agent and customer
experience.

In general, we recommend getting started with these four steps:

1. **[Understand how intelligent triage
   works](https://support.zendesk.com/hc/en-us/articles/4964463770650#topic_nkh_cst_x5b)** from ticket submission to resolution. You should also
   understand how the system [populates intent, language, and sentiment
   values on tickets](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_ebn_l4g_htb).
2. **[Enable intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_gpp_p4g_htb)** to
   start allowing tickets in your account to be categorized with an intent,
   language, sentiment, or all three.
3. **[Build reports to analyze intelligent
   triage results](https://support.zendesk.com/hc/en-us/articles/4550620559258)** to see trends in your tickets. As you get
   started, consider building separate reports for intent, language, and sentiment
   to allow you to focus on one prediction type at a time.
4. **Wait for approximately two weeks** to allow for a sufficient sample size of
   tickets to be enriched by intelligent triage.

## Analyzing and fine-tuning the results

After a couple of weeks, intelligent triage should have enriched enough tickets for
you to be able to decide which actions to take. The following sections present some
additional points to consider as you perform this analysis.

### Identify trends in the predicted intents, languages, and sentiments

First, take a look at the reports you built above and review the High and Medium
confidence tickets. Look for trends, and decide whether you want to take action
to improve them.

| Trend | Actions to consider |
| --- | --- |
| What are the most prevalent intents and languages? | - Make sure your agents are trained to handle the most common   types of requests. - Create knowledge base articles and other self-serve   resources to deal with easy requests (like password resets),   and automate responses to these types of tickets using   macros. - Make sure you have agents who speak the same languages as   your customers. |
| Are there any intents that would make sense for you to group together? | - [Create views that group   similar intents together](https://support.zendesk.com/hc/en-us/articles/4662504732954#topic_hfh_cz3_5tb), and [route them to the agents   who are best suited](https://support.zendesk.com/hc/en-us/articles/4973607684506) to deal with them. |
| Are the predicted intents and languages consistent with the initial message on each ticket? | - If not, [give feedback to   Zendesk](https://support.zendesk.com/hc/en-us/community/posts/4409898234138) so we can improve the prediction   model. - You can also [report on tickets where   the intent was manually changed by an agent](https://support.zendesk.com/hc/en-us/articles/4550629802650),   signaling that the initial prediction didn't hit the   mark. |
| What trends are there in customer sentiment? Are negative-sentiment tickets especially prevalent for a specific product or category? | - If you receive many negative-sentiment tickets,   it might be worth giving agents additional training on   diffusing tough situations. - If a specific product or category receives many   negative-sentiment tickets, investigate whether there   are improvements to the product that need to be   made. |

### Decide which metrics you want to improve

Next, decide which metrics matter the most to your team. Do you want to raise
CSAT ratings, meet SLAs more consistently, improve first response time, reduce
group assignments, or something else?

Start by targeting one or two metrics, or perhaps a subset of intents, and
consider how workflow changes can improve the overall experience. Target those
areas first to get the maximum impact from intelligent triage.

| Trend | Action to consider |
| --- | --- |
| Low first reply times on urgent issues | - [Create a trigger](https://support.zendesk.com/hc/en-us/articles/4766535251610)   that raises the priority for tickets with certain intents so   that agents get to the ticket faster. |
| CSAT is low for tickets in a particular language | - [Route tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506) of a   particular language directly to the agents who are fluent in   that language. |
| Tickets about a certain topic always require more information from an agent before they can be solved | - Exclude these tickets from the normal “Ticket is created”   trigger and instead [create a trigger](https://support.zendesk.com/hc/en-us/articles/4766535251610)   that sends the customer a message which prompts them to   provide the needed information. - Consider [updating your ticket   forms](https://support.zendesk.com/hc/en-us/articles/4408846520858#topic_h4l_mkp_knb) to collect the required information as part   of the original ticket. |

### Design, implement, and report in an iterative process

Regardless of the changes you decide to make, remember that this is an iterative
process. You will identify trends, make changes accordingly, track the success
of those changes, and repeat.

Here are some questions to consider as you design, implement, and report on your
workflow changes:

- What is the highest level of confidence needed for the workflow to be
  effective? For example, is it acceptable to send *all* tickets with a
  certain intent to a designated group and ask that they manually reroute if
  the intent was wrong, or should only tickets with a High confidence level be
  routed to that group?
- Should the workflow apply a tag or update some other ticket attribute to
  allow for easier reporting in the future?

### Establish two-way communication with your agents

Inform your agents of any changes you make so that they’re equipped to provide
feedback on them, both good and bad.

For example, consider [setting up a macro](https://support.zendesk.com/hc/en-us/articles/4408844187034) to tag tickets
where the agent has feedback, and include an internal note where they can record
their feedback about the workflow.

Ask your agents about particular pain points they have with tickets. If there is
a particular group of intents where they see complications, brainstorm ways to
adapt your workflows to improve the agent and customer experience.
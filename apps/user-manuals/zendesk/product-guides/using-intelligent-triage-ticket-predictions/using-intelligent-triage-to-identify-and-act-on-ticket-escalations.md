# Using intelligent triage to identify and act on ticket escalations

Source: https://support.zendesk.com/hc/en-us/articles/6353620565530-Using-intelligent-triage-to-identify-and-act-on-ticket-escalations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Ticket escalations can take many forms. A customer interaction might need to be raised to a manager, or perhaps a ticket needs to be sent to an agent with special expertise.

Using intelligent triage, you can design workflows to help identify potential escalation situations and act accordingly. This article provides some examples of how to put this into practice.

A well-designed escalation process can improve resolution times, get customers the help they need faster, or just get the right eyes on an emergent situation. This improves the customer experience, enhances their loyalty, and potentially increases the value of their relationship.

This article contains the following topics:

- [Step 1: Turn on intelligent triage and wait for data](#topic_hr2_n4g_jzb)
- [Step 2: Consider known escalation paths and indicators](#topic_ftg_44g_jzb)
- [Step 3: Build a report](#topic_fh3_p4g_jzb)
- [Step 4: Take action](#topic_ng1_q4g_jzb)

Note: When creating reports in Explore, intelligent triage prediction values are available only in English. However, intelligent triage is capable of evaluating content in the languages listed [here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

## Step 1: Turn on intelligent triage and wait for data

The first step in this process is [turning on intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_gpp_p4g_htb). After it’s turned on, it will start enriching tickets on your selected channels with predictions about customer intent, language, and sentiment. These enrichments will be the foundation for identifying potential escalations.

It's important to allow enough time to gather sufficient data before moving on to the next step. Depending on the frequency of escalations in your account, this time can vary. Typically, two weeks is a sufficient amount of time.

## Step 2: Consider known escalation paths and indicators

The next step is to consider known escalation paths or indicators. These are patterns or attributes that suggest a ticket might need to be escalated.

Two common indicators include:

- **Group transfers**: This is when a ticket is transferred from one group to another. Frequent transfers of a specific subset of tickets could indicate a pattern where there is a complex issue that requires escalation. These could be tickets that are transferred from a frontline group to a specialist group, or from a support group to a group of team leads or managers.
- **Tags and fields**: Certain tags or fields in a ticket could signify an escalation. Perhaps you have a specific macro that applies a tag or tracks escalations in a designated ticket field.

## Step 3: Build a report

After identifying potential escalation indicators, the next step is to build a report. This report should include:

- **Metrics or attributes specific to the escalation(s)**: These could be the old and new groups for transferred tickets, tickets with the applicable tag or field value identified in step 2 above, or something else.
- **Intent/language/sentiment**: Including these attributes in your report helps you to see whether intelligent triage insights can help you proactively identify potential escalations. Example insights you might find include:
 - Tickets with a specific intent are frequently escalated if there has been more than a certain number of agent replies.
 - Negative sentiment tickets assigned to a collections group are likely to be escalated.

Using reports in these situations can help you anticipate future escalations and take proactive measures.

### Create a metric to track the escalation

After observing escalations from frontline support agents to team leads or managers, you can configure a metric in Explore to track tickets taking this path.

For example, you can [create a standard calculated metric](https://support.zendesk.com/hc/en-us/articles/4408824243738#topic_g2g_hdb_hv)
called **Manager escalations** with a formula like the one provided below.
Replace the placeholder values with each group’s ID. For help, see [How can I retrieve the group ID in Support?](https://support.zendesk.com/hc/en-us/articles/4408837673114)

```
If([Changes - Field name]="group_id"
AND IN([Changes - Previous value], 
ARRAY(
/* Tier 1 Group */ "XXXXXXX",
/* Tier 2 Group */ "YYYYYYY"))

AND IN([Changes - New value],
ARRAY(
/* Manager Group */
"AAAAAAA",
/*Team Lead Group */
"BBBBBBB",)))

THEN [Ticket ID]
ENDIF
```

### Create a report to track tickets following this escalation path

1. In Explore, click the reports (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, click **Support** > **Updates History**, then click **Start report**. The report builder opens.
4. In the **Metrics** panel, click **Add**.
5. From the list, select the metric you created above (in the example, this was **Manager escalations**) and click **Apply**.
6. In the **Rows** panel, click **Add**.
7. From the list, select the following attributes and click **Apply**. These are just example attributes. You could use at least one of these values and their associated confidence levels, along with other known attributes in your account.
   - **Intent**
   - **Language**
   - **Sentiment**
   - (Optional) **About**, **Issue type**, **Reason code** (Or any common custom ticket field you might use to have your customers or agents track what the request is about. This value paired with the intelligent triage values can amplify the effectiveness of your report. See also [Explore recipe: Comparing intelligent triage intent predictions with a custom About field](https://support.zendesk.com/hc/en-us/articles/5429030095258).)
8. To filter your report to show only tickets where the Intent, Language, or Sentiment field was populated by intelligent triage:
   1. Click the **Intent**, **Language**, or **Sentiment** attribute on the left.
   2. Click the **Excluded** tab.
   3. Select **NULL**.
   4. Click **Apply**.

      Tip: As an alternative to this step, you can create a standard calculated attribute that acts as a filter to identify tickets enriched by intelligent triage. The benefit to the calculated attribute is that you can quickly reuse it in other reports, and it can find tickets where an intent, language, or sentiment prediction has been made. For instructions, see [Creating an optional filter](https://support.zendesk.com/hc/en-us/articles/4550620559258#h_01GNWSPEKSVQATW95TMP58DYHH).
9. Click the default **Update - Date** and select the time frame that’s most helpful to you. This could be the period of time since you enabled intelligent triage, made a specific workflow update, or an arbitrary time frame like the past 30 days.

## Step 4: Take action

The final step in the intelligent triage escalation process is taking action based on your findings. There are several possible paths to take, and multiple paths can be applied depending on the situation:

- **Automatically escalate the ticket**: If you find a very high percentage of tickets with a certain intent or subject matter, it may make sense to route the ticket to the appropriate agents right away. You can update your business rules or routing to incorporate the applicable values and add an internal note to indicate the reason for escalation. For more information about routing tickets using intelligent triage, see [Choosing a routing method for automatically triaged tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506).
- **Add an internal note**: Using the Internal note trigger action, you can warn agents about special handling requirements. You might decide to trigger this after a certain number of agent replies, and you could provide helpful agent resources, such as instructions, knowledge base articles, or other external links). See [Adding an internal note to a ticket using a trigger](https://support.zendesk.com/hc/en-us/articles/6191477770906#topic_kvx_rwg_xyb) for instructions. For example, you could create a trigger with the following conditions and actions:
 - **Meet ALL of the following conditions**:
    - **Intent** | **Is** | **Software error**
    - **Agent replies** | **Is** | **5**
    - **Status** | **Is** | **Open**
    - **Ticket tags** | **Contains none of the following** | **agent\_esc\_notified**
 - **Actions**:
    - **Add tags** | **agent\_esc\_notified**
    - **Internal note** | Add a message to encourage your agent to ask for help, suggest documentation that might help them, or advise them they may need to escalate. This is a good time for them to be retrospective and decide whether they’re stuck on the current issue or have a plan of action that can continue until the matter is resolved.
- **Add a Service Level Agreement (SLA)**: If the issue is often urgent, a trigger can update the ticket’s priority to meet SLA requirements to be prioritized by the team. For more information about setting up SLAs, see [Defining SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866).

The automated and consistent categorization of tickets allows you to build predictable workflows without having to manually handle and assign every ticket, saving your agents time and improving customer satisfaction.
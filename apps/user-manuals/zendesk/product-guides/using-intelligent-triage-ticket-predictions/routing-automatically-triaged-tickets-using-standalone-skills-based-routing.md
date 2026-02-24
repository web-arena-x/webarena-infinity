# Routing automatically triaged tickets using standalone skills-based routing

Source: https://support.zendesk.com/hc/en-us/articles/6191493148186-Routing-automatically-triaged-tickets-using-standalone-skills-based-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

You must have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330) to use the features described in this
article.

You can incorporate [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) information into your [standalone skills-based routing](https://support.zendesk.com/hc/en-us/articles/4408883700122) setup.

Intelligent triage automatically determines a ticket's intent, the language it's written
in, and the customer sentiment (positive or negative). Standalone skills-based routing
allows you to route tickets to the agents who have the right expertise to handle
them.

Pairing these two features lets you automatically route tickets to the agents who have
the right knowledge to resolve a specific issue, such as speaking the same language as
the requester.

This article gives you examples of skill routing rules you can create based on
intelligent triage information. Because these examples are starting points, customize
the details however makes sense for your business.

This article contains the following topics:

- [Creating a skill routing rule based on intent](#topic_rq2_w5g_xyb)
- [Creating a skill routing rule based on language](#topic_gxm_x5g_xyb)
- [Creating a skill routing rule based on intent and language](#topic_kvn_y5g_xyb)
- [Creating a skill routing rule based on sentiment](#topic_k2c_1vg_xyb)

Related articles:

- [Choosing a routing method for automatically
  triaged tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506)
- [Routing automatically triaged tickets using
  omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4766535251610)

Note: When creating skill routing rules in Admin Center,
intelligent triage prediction values are available only in English. However,
intelligent triage is capable of evaluating content in the languages listed [here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

## Creating a skill routing rule based on intent

In the example below, a skill routing rule sends refund request tickets to your
agents who specialize in handling refunds.

**To create a skill routing rule based on intent**

1. [Create a skill type](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_sx3_hqt_cs) called
   **Specialty area** that [contains a skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ug2_j4y_hdb) named **Refunds**,
   and [assign the skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb) to at least one
   agent.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
3. Click the **Specialty area** skill type, then click **Refunds**.
4. In the **Tickets** section, click **Add condition** under **Meet Any of
   the following conditions**.
5. Set the following conditions:
   - **Intent** | **Is** | **Billing::Refund::Refund request**
   - **Intent** | **Is** | **Billing::Refund::Refund amount is
     wrong**
   - **Intent** | **Is** | **Billing::Refund via a specific
     channel**
6. Click **Save**.
7. [Create a skills-based view](https://support.zendesk.com/hc/en-us/articles/4408883700122#topic_ifc_vwf_2nb) for agents
   to see the routed tickets.

## Creating a skill routing rule based on language

In the example below, you'll build a skill routing rule that sends tickets written in
Spanish to your Spanish-speaking agents.

**To create a skill routing rule based on language**

1. [Create a skill type](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_sx3_hqt_cs) called
   **Language** that [contains a skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ug2_j4y_hdb) named **Spanish**,
   and [assign the skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb) to at least one
   agent.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
3. Click the **Language** skill type, then click **Spanish**.
4. In the **Tickets** section, click **Add condition** under **Meet All of
   the following conditions**.
5. Set the following condition: **Language** | **Is** | **Spanish**
6. Click **Save**.
7. [Create a skills-based view](https://support.zendesk.com/hc/en-us/articles/4408883700122#topic_ifc_vwf_2nb) for agents
   to see the routed tickets.

## Creating a skill routing rule based on intent and language

In the example below, a skill routing rule sends refund request tickets written in
Spanish to your Spanish-speaking agents who specialize in handling refunds.

**To create a skill routing rule based on intent and language**

1. [Create a skill type](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_sx3_hqt_cs) called
   **Language-specific specialty area** that [contains a skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ug2_j4y_hdb) named **Spanish -
   Refunds**, and [assign the skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb) to at least one
   agent.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
3. Click the **Language-specific specialty area** skill type, then click
   **Spanish - Refunds**.
4. In the **Tickets** section, click **Add condition** under **Meet All of
   the following conditions**.
5. Set the following condition: **Language** | **Is** | **Spanish**
6. Click **Add condition** under **Meet Any of the following conditions**.
7. Set the following conditions:
   - **Intent** | **Is** | **Billing::Refund::Refund request**
   - **Intent** | **Is** | **Billing::Refund::Refund amount is
     wrong**
   - **Intent** | **Is** | **Billing::Refund via a specific
     channel**
8. Click **Save**.
9. [Create a skills-based view](https://support.zendesk.com/hc/en-us/articles/4408883700122#topic_ifc_vwf_2nb) for agents
   to see the routed tickets.

## Creating a skill routing rule based on sentiment

In the example below, a skill routing rule sends tickets with a negative sentiment to
a group specially trained to handle these kinds of situations.

**To create a skill routing rule based on sentiment**

1. [Create a skill type](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_sx3_hqt_cs) called **Customer
   service** that [contains a skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ug2_j4y_hdb) named **Negative
   sentiment**, and [assign the skill](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb) to at least one
   agent.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
3. Click the **Customer service** skill type, then click **Negative
   sentiment**.
4. In the **Tickets** section, click **Add condition** under **Meet Any of
   the following conditions**.
5. Set the following conditions:
   - **Sentiment** | **Is** | **Negative**
   - **Sentiment** | **Is** | **Very negative**
6. Click **Save**.
7. [Create a skills-based view](https://support.zendesk.com/hc/en-us/articles/4408883700122#topic_ifc_vwf_2nb) for agents
   to see the routed tickets.
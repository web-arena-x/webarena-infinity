# Enhanced Disaster Recovery 

Source: https://support.zendesk.com/hc/en-us/articles/4408826350234-Enhanced-Disaster-Recovery

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise Plus |

This article describes Enhanced Disaster Recovery for Zendesk.

Note: Enhanced Disaster Recovery covers Guide accounts and Help Center Functionality.

This article includes the following sections:

- [About Enhanced Disaster Recovery](#h_e08a7d7a-6eba-4ef3-81af-400834daa0a6)
- [Key features of Enhanced Disaster Recovery](#h_4355256e-07bf-4ac4-934a-fa88bd4fcc81)
- [Exceptions to Enhanced Disaster Recovery](#h_01EHWVZS634KG0W67H957FRG00)

## About Enhanced Disaster Recovery

Enhanced Disaster Recovery enhances the protection of your Zendesk data and provides for faster recovery in the event of a disaster that interrupts your Zendesk service. With this feature, your Zendesk data is replicated in real-time, and you’ll receive priority cloud resiliency.

## Key features of Enhanced Disaster Recovery

Key features of Enhanced Disaster Recovery include:

- **Real-time data replication**: **Zendesk will replicate your data in real-time within and across Amazon Web Service (AWS) Availability Zones, ensuring extra redundancy and lessening the chance of data loss in the event of a significant disaster. This replication occurs within the same region as your Zendesk service data.**
- **Availability Zone** **Redundancy**: Zendesk infrastructure within each region is spread across two, and sometimes three, physically diverse Availability Zones to provide increased redundancy. In the event of a significant issue impacting an Availability Zone, this structure allows Zendesk to recover within the surviving Availability Zone(s). The secondary Availability Zones, along with AWS elastic scaling capabilities, provide for quicker recovery of service, or in some cases, continuous operation.
- **Traffic** **Prioritization**: Enhanced disaster recovery combines AWS Availability Zone redundancy with our Cloudflare edge network capability to prioritize Enhanced Disaster Recovery Subscriber traffic while additional capacity is restored for other subscribers.
- **Priority Recovery Planning**: Zendesk maintains a program of test activities and events to validate that our plans for priority recovery of the Services are effective. The scenarios for these exercises vary and test different elements of Zendesk’s business continuity and disaster recovery plans to validate the overall strength of the plan.

**In the event of a disaster, the following objectives apply:**

- **4 hour Recovery Time Objective (RTO)**: Zendesk will aim to restore normal operations for your Zendesk Support account within four hours from the time a disaster is declared, unless a disaster, or multiple disasters, impacts all of the Availability Zones used on an account.
- **Under 1 hour Recovery Point Objective (RPO)**: Zendesk will target one hour or less of data loss for your account. This is calculated from the point of the disruption, not from Zendesk’s disaster declaration.
- **Service and traffic prioritization**: Recovery for your Zendesk account will be prioritized over the accounts of other subscribers who have not purchased Enhanced Disaster Recovery commitments. Additionally, your account’s traffic will be prioritized over other accounts within the Zendesk Content Delivery Network (CDN).

## Exceptions to Enhanced Disaster Recovery

Enhanced Disaster Recovery and the practices described in this article do not apply to the functionality within Zendesk Suite, Support and Chat integrations with third-party messaging providers, or to Zendesk Sunshine Conversations, Zendesk Sell, Zendesk WFM (Tymeshift), Zendesk QA (Klaus), Zendesk Sunshine, Custom Objects, Custom Events, and Unified Profiles whether such functionality is available standalone or is available in Zendesk Suite and Support. If you purchase a Zendesk Suite, Zendesk Support Suite, or Sales Suite service plan that includes Enhanced Disaster Recovery, Enhanced Disaster Recovery will only apply to the underlying services that are covered by the feature.
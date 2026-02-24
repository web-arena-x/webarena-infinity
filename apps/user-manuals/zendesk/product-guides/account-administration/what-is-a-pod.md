# What is a Pod?

Source: https://support.zendesk.com/hc/en-us/articles/4408829092506-What-is-a-Pod

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

**Zendesk has data centers throughout the globe to meet the performance and data needs of our customers. Each of these data centers contains one or more [Pods](https://en.wikipedia.org/wiki/Point_of_delivery_(networking)) (points of delivery). Your Zendesk account shares common network and system resources with other Zendesk customers in a given Pod.**

**This article includes the following sections:**

- [About Pods](#h_01EE928YQH2X90G4QN2GJ20XAD)
- [How do I learn what Pod I am on?](#h_01EE9296PRDQFBW472BBDEJT1Z)
- [Can I specify the Pod my Zendesk account is hosted on?](#h_01EE929E2GB0T1B65XWT6AB5FM)
- [How do I learn the geographical location of my Pod?](#h_01EE929TEFF6YJMAVK0JR4YKPE)

## About Pods

You can think of a Pod as a high-rise office building with one Zendesk account occupying each floor. Just as the high-rise provides shared infrastructure like security, electricity, plumbing, and air conditioning for each floor of the building, a Pod provides the security, network, application, and database services shared by multiple Zendesk accounts on that Pod.

**This Pod architecture provides maximum performance and stability (service incidents affecting one Pod will not affect customers in other Pods) with the added benefits of faster account provisioning and improved scalability.  You can learn more details about Zendesk's technical architecture and Pods in the Help Center article [Zendesk scalability and performance: Technical architecture](https://support.zendesk.com/hc/en-us/articles/4408832509338).**

## How do I learn what Pod I am on?

You can confirm your Zendesk account's Pod by [opening Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb). Your Pod is displayed at the bottom of Admin Center Home.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_home_pod.png)

You can also visit the [Zendesk Status site](https://status.zendesk.com/), where you can enter your subdomain name to find out which pod you are on.

## Can I specify the Pod my Zendesk account is hosted on?

In most cases, the Pod you are hosted in is located in the data center physically closest to your location at signup. However, we do occasionally need to "load balance" certain accounts to other Pods to improve performance, as needed. If you do wish to ensure that your data stays in a certain location, consider our [Data Center Location feature](https://www.zendesk.com/company/policies-procedures/regional-data-hosting-policy/). Select from United States (US)-only and European Economic Area (EEA)-only for the storage of your data.

## How do I learn the geographical location of my Pod?

Along with your pod number, the data center location is displayed at the bottom of Admin Center Home. If you have questions, contact [Zendesk Customer Support.](https://support.zendesk.com/hc/en-us/articles/4408843597850)
# Using the sample data for employee services

Source: https://support.zendesk.com/hc/en-us/articles/9012803758362-Using-the-sample-data-for-employee-services

---

The Customer Support Suite and Employee Service Suite plans both provide full-service, cross-channel experiences for your users with the ticketing system, help center, messaging and live chat, and voice all working together. They also provide the basic components and configurations required to get you up and running quickly.

However, while the Customer Support Suite is designed for generic customer service, the Employee Service Suite is designed with common HR and IT use cases in mind. Therefore, Zendesk is able to provide more sample data and configurations that work out of the box for employee services.

This article describes what sample data and configurations are provided for Employee Service Suite plans and how to use them.

This article includes the following topics:

- [Understanding the additional sample data and configurations for employee services](#topic_dkn_ldl_q2c)
- [Using the employee service sample data and configurations](#topic_bcx_v2l_q2c)

## Understanding the additional sample data and configurations for employee services

In addition to all of the standard content and configurations for the Customer Support Suite plans, Employee Service Suite plans come with the following additional sample data designed specifically for HR and IT use cases:

- [Ticket forms](https://support.zendesk.com/hc/en-us/articles/4408888481178)
- [Ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098#topic_djc_ky3_q2c)
- [Macros](https://support.zendesk.com/hc/en-us/articles/4408887656602#topic_ef1_nsk_q2c)
- [Views](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_mdh_mlg_p2c)
- [Brands](https://support.zendesk.com/hc/en-us/articles/4408829476378)
- [Groups](https://support.zendesk.com/hc/en-us/articles/4408886146842#topic_k1c_11l_q2c)
- [Help center articles](https://support.zendesk.com/hc/en-us/articles/8988883304090)
- Sample tickets

## Using the employee service sample data and configurations

You have the following options when working with the sample data and configurations provided for Employee Service Suite plans:

- Use it as-is.
- Make adjustments, customizing it to better meet your needs.
- Deactivate or delete any of the sample data and configurations you don't intend to use.

To make it easy for admins to identify the sample data and configurations, all of their names begin with *[SAMPLE]*. This preface isn't displayed to requesters in tickets cases where the name is visible to both agents and requesters. However, it's a good idea to remove this preface from the names of any sample data and configurations you decide to use in your workflows.

It's also important to understand that all of the sample data and configurations for employee services are active by default. That means, unlike Customer Service Suite and Support plans, Employee Service Suite plans have multiple groups, brands, and ticket forms from the start. This changes some expected behaviors, so it's important to identify which of these are applicable to your use case, and deactivate everything else.

For example, new Employee Service Suite plans have multiple brands and omnichannel routing on by default. However, omnichannel routing doesn't recognize which brands agents belong to and tickets are associated with, which can lead to issues. See [Using brands (department spaces) with omnichannel routing](https://support.zendesk.com/hc/en-us/articles/8125262923802).

**To get started with a new Employee Service Suite account**

1. [Review the employee service sample data and configurations](#topic_dkn_ldl_q2c).
2. Deactivate the sample content you don't intend to use.
3. Configure the sample content you do intend to use. For example, you may want to:
   - Restrict [views](https://support.zendesk.com/hc/en-us/articles/4408838983322) or [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408822414490#topic_nhh_gys_5wb) by brand to control agent access to tickets.
   - Configure groups that will handle sensitive information in tickets to be [private ticket groups](https://support.zendesk.com/hc/en-us/articles/4767122732058).
   - Decide whether you'll use [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962) or [other routing options](https://support.zendesk.com/hc/en-us/articles/4408831658650). If you decide not to use omnichannel routing, you must [turn it off](https://support.zendesk.com/hc/en-us/articles/5095079121690).
   - Create [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466), [custom omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858), or other business rules to assign incoming tickets to groups. This is necessary as soon as you start adding agents.
4. [Add agents and admins individually](https://support.zendesk.com/hc/en-us/articles/4408886939930) or [in bulk](https://support.zendesk.com/hc/en-us/articles/4408893496218).
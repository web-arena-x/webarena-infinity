# Multiple Contact Centers on a Single Zendesk Instance (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731475270298-Multiple-Contact-Centers-on-a-Single-Zendesk-Instance-Engage-Legacy

---

Zendesk for Contact Center can support multiple Contact Center applications. In order for this to work correctly, a number of conditions must be met. This document describes the exact conditions for this to operate.

# Technical Requirements

1. All Contact Center instances must be authenticated independently. This requires each contact center instance to have unique instances of all the below:   
   1. Enterprise Application at the IdP for each Connect and Cognito instance
   2. Cognito User Pool and ID Pool
2. Each Contact Center instance must be fully provisioned with their own Cloudformation Stack
3. In order for the Agent status feature to work, ensure that a Zendesk Webhook exists for each Contact Center Application instance attached to the Zendesk instance
4. Ensure that each Zendesk Agent is only provisioned to work with a single Contact Center Application instance. Agents can not be shared or duplicated across Amazon Connect instances
5. During operation, ensure all agents are only running a single instance of Contact Center. Ensure that there are no more than one (1) instance of Contact Center running in a browser tab or window at a time.
6. Test instances should mirror Agent Configurations (as specified in points 1 - 5)

‍
# Multibrand: Restricting agents to specific brands

Source: https://support.zendesk.com/hc/en-us/articles/4408829471898-Multibrand-Restricting-agents-to-specific-brands

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

The [Multibrand feature](https://support.zendesk.com/hc/en-us/articles/4408829476378) in Support is configured by default to allow all agents to access tickets for all brands. This allows your support team to seamlessly move between requests from all of your brands and provide faster support. However, some teams might want to restrict the agents that are able to access tickets for specific brands.

This article describes how to effectively restrict agent access to tickets for specific brands by following the steps below:

- [Step 1: Create groups](#h_01H1W402BRYZS0057FGJ0G9PSD)
- [Step 2: Limit agents to groups](#h_01H1W40E5M1AS3Q0NFEMTMBKJH)
- [Step 3: Set up triggers](#h_01H1W40PMD25H7QC1XAJ9HCYVR)
- [Optional: Add group-limited views](#h_01H1W40XTM7DAERJY3CW1B10GK)

## Step 1: Create groups

After you've [set up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), create groups. You may want to create just one group per brand or maybe many per brand, depending on how granular you want restrictions to be. For example:

- Simple: BrandA, BrandB, BrandC, etc
- Complex: Support\_BrandA, Returns\_BrandA, Support\_BrandB, Returns\_BrandB, Support\_BrandC, Returns\_BrandC, etc

When creating these groups, add the agents whose access to specific brands you want to restrict.

See [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130) and [Adding team members to groups](https://support.zendesk.com/hc/en-us/articles/4408821536794).

## Step 2: Limit agents to groups

Next, limit agent access to only tickets within their groups.

(Enterprise only) Custom roles can be set to restrict agents to only access tickets within their groups. Create or edit an existing custom role, then in the **Tickets they can access** section, select **Within their groups**. See [Creating custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) and [Editing custom roles](https://support.zendesk.com/hc/en-us/articles/4408832292506#topic_w4w_wyy_qpb).  
  
(Suite Growth and Professional) You can limit agent access to tickets in their groups from their profiles in Support. Learn more about [setting up agent access restrictions](https://support.zendesk.com/hc/en-us/articles/4408831313050).

## Step 3: Set up triggers

You can now set up triggers to route new tickets to a group for the right brand. It might be beneficial to first route tickets to a triage group, which will then assign them to the appropriate group based on the type of request. See [Creating triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466).

Set the condition of the trigger to be when a ticket is created for a certain brand:

![](https://support.zendesk.com/hc/article_attachments/7856364392986)

Then the action assigns it to the correct group:

![](https://support.zendesk.com/hc/article_attachments/7856364392730)

You can add any notification messages or other ticket updates as well.

For existing tickets for a certain brand, you must manually assign them to the correct group. See [Bulk updating tickets](../../agent-guide/ticket-management/managing-tickets-in-bulk.md#topic_oth_lkp_gk).

Note that agents are able to edit the brand of tickets. Agents can still access tickets that they change the brand of as long as it is still assigned to their group.  
To further restrict your agents' access to specific brands, you can set up a trigger that reassigns the ticket when the brand is changed. For example:

![trigger_brand_restriction.png](https://support.zendesk.com/hc/article_attachments/7856386829722)

## Optional: Add group-limited views

In addition to the group and trigger workflow, you can also restrict your views to a specific group. This way, you can have a view of BrandA's tickets and only allow a specific group of agents to see that view:  
![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/views_limit_access_group.png)

For more information, see  [Using views to sort branded tickets](https://support.zendesk.com/hc/en-us/articles/4408838983322).

Note:  If you use brand-specific views, and your agents are restricted to working only in their groups, it might be harder for your agents to assign tickets and collaborate across groups. You can have managers or administrators with access to every group's tickets facilitate handoffs if necessary in this case.
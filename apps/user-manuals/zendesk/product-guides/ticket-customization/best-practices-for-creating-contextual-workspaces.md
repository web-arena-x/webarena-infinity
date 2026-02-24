# Best practices for creating contextual workspaces

Source: https://support.zendesk.com/hc/en-us/articles/4408828930202-Best-practices-for-creating-contextual-workspaces

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Workspaces > Agent tools >
Contextual workspaces

To effectively complete their tasks, agents need access to the right tools at the right time.
Contextual workspaces allow administrators to select the right tools for agents to see when they first open a ticket. To help your agents cut through the noise, it's important to create workspaces that are specific. This article provides some examples and advice to help you plan your workspace strategy.

This article contains the following topics:

- [When to create a workspace](#topic_fyp_pyb_vfb)
- [How to create a focused workspace](#topic_s5b_ryb_vfb)
- [Avoid adding too many macros and forms](#topic_hzq_syb_vfb)

Administrators and advisors can create and manage contextual workspaces. To create a new workspace, see [Setting up a contextual workspace](https://support.zendesk.com/hc/en-us/articles/4408833498906-Setting-up-contextual-workspaces-Enterprise-). To manage workspaces, see [Managing contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408822138522-Managing-contextual-workspaces-Enterprise-).

## When to create a workspace

The following are some typical scenarios where agents can benefit from the highlighted set of tools that a workspace provides.

### Scenario 1: Reduce training for frequent request types

In a given season, company A has 60% of their overall requests about one specific topic.
They tend to hire seasonal employees to help with the extra load. The set of actions and information needed are fairly limited, but the cost of re-training every season is extremely high. Also, there's no opportunity to deflect these tickets automatically with [autorepliest](https://support.zendesk.com/hc/en-us/articles/4408821295898) because agents need to perform an action before the request can be finished.

Creating workspaces that tackle common request types can have a large impact on agent efficiency. A tailored set of ticket fields, macros, expanded apps, and a custom layout can reduce the amount of training agents need to complete the request.

### Scenario 2: Improve macro selection and quality

Company B has requests where they need to reply with links to time-sensitive, promotional codes. Because these promotional codes change often, agents don't know which macros to use and which links to send. Customers often receive expired links with out-of-date codes.

Creating workspaces for promotional code requests will ensure that agents immediately see the correct macros to use, and customers will receive active links with up-to-date promotional codes.

### Scenario 3: Manage international process differences

Company C is a global company and adheres to different international laws. In some countries, returns need X information, while in other countries they need Y information.
Currently, agents don't know which ticket fields are needed for their region or which macro folder to open for the right macro.

Creating different workspaces for each type of return will highlight the right ticket fields and macros for each region.

### Scenario 4: Focus agent attention for faster ticket resolution

Company D is a large, high-speed delivery company with agents that process hundreds of tickets a day. Their agents need to create and fill out tickets as quickly as possible. Any slowdown in ticket processing has a direct impact on the bottom line.

Creating workspaces with custom layouts can direct agent workflow by showing them only the relevant information and apps they need for the task at hand. Custom layouts will help agents focus their efforts and complete tickets quickly.

### Scenario 5: Reduce the time agents spend searching for Knowledge content

Company E is a large company that handles many returns, especially during the busy holiday season. To help agents quickly process returns and damaged items, you can create a workspace where the Knowledge section uses default filters to show articles in the Return and Damage sections of your help center. If necessary, agents can manually remove these filters to access a broader range of articles.

Creating a workspace with default filters helps agents use the Knowledge section to quickly and easily find the articles they need to complete their tasks.

Note: To change knowledge section settings that are not part of this workspace, see [Configuring the knowledge section in the context panel](https://support.zendesk.com/hc/en-us/articles/7263163614874).

## How to create a focused workspace

Don't create a workspace that is too generic. Generic workspaces can present agents with a set of tools that is still overwhelming, and they can spend too much time digging for the right tools. Use the following approach to discover scenarios that work well with workspaces. You are limited to 500 active workspaces with no more than 10 conditions per workspace, so planning is important. Each workspace can have one custom layout associated with it.

1. Write down the relevant areas of your organization. Ask yourself which departments, locales, teams, tiers, products, and specialties exist.
2. Map out each of these areas. Include how specific teams interact within each area.
3. Think about which ticket forms you currently use. These forms tend to showcase the general request types for your organization.
4. Ask yourself about one type of request that would benefit from a workspace.
5. Open an existing ticket from that request. What does an agent need to see when they are working on this ticket?
   - Make a note of the ticket forms and macros the agent needs to see.
   - What apps should you emphasize?
   - How can a streamlined layout help the agent’s workflow?
6. Continue to work through each area.

This process should help you arrive at the specific request type for a workspace, the feature set tied to this workspace, and the set of conditions that would apply to the workspace. The order and elements of how you get to your specific task will vary depending on your industry and company organization. See example below.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual-workspaces-example2.png)

- **Request type**: In this example, the teams are heavily influenced by the region that they work in. Their processes differ based on region. The specific workspace they want to create is for damaged video products sold in North America.
- **Feature set**: After you focus on the request type, open a ticket within that request type. Then, map out which apps, ticket fields, macros, and layout are important for this request type.
- **Workspace conditions**: Equipped with your specific request type and a set of ticket features, figure out when this workspace would apply. Similar to triggers, you can set workspace conditions. For example, you could define a workspace that applies when the **Organization** is **North America**, the Brand is **Video Products**, and the **Subject text** contains **damage** or **broken**. To learn more, see [Setting workspace conditions](https://support.zendesk.com/hc/en-us/articles/4408833498906-Setting-up-contextual-workspaces-Enterprise-#topic_xcq_sgt_w2b).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cw_layout3.png)

## Avoid adding too many macros and forms

Agents still have access to all of their ticket fields, macros and apps. So, avoid adding too many macros or ticket fields to a workspace. You don't need to include them all. Focus on the common one or two macros that agents need to complete the request. Also, think about the amount of vertical space on their screen and choose the appropriate amount of ticket fields to provide. These will be highlighted on the ticket.
# About Agent Builder

Source: https://v2.support.procore.com/product-manuals/agent-builder-project/tutorials/about-agent-builder

---

##### Agent Builder Transition

Agent Builder is **no longer available for new activations via Procore Explore** as we transition to our next generation of Procore AI. We are currently developing powerful new agentic capabilities via our Datagrid integrationâstay tuned for updates.

Procore's Agent Builder helps users create AI Agents that automate routine tasks and gain predictive insights from project data. You can easily tailor an Agent to your specific project requirements and business needs. Simply select the actions it should take and the documents it should reference.

You can run the Agent directly from [Assist](/product-manuals/assist-project/), Procore's in-app AI service. Get powerful automation as you work. 
 
Example Agent functions:

- **Draft submittals** from existing project specifications.
- **Analyze photos** to identify potential safety observations.
- **Create draft daily logs** using schedules and photos.
- **Create tasks** to notify teams about potential delays.
- **Consolidate cross-tool data** into a weekly summary, highlighting overdue tasks or issues.

## Availability

Agent Builder is currently in **Open Beta**. Usage is free during this period. You can [self-enroll](/product-manuals/assist-project/tutorials/enable-assist) via Procore Explore, provided you meet the prerequisites and understand the permissions, guidelines, and limits outlined below. Once the product is generally available, some features may incur a cost. For more information, contact your Procore point of contact.

### Prerequisites for Access

- To access Agent Builder, you must have **Assist in tool side panels.** While some accounts have access to Procore Assist via global search, enrollment in the beta program for [Assist in tool side panels](/product-manuals/assist-project/tutorials/enable-assist) is a prerequisite to getting Agent Builder.
- Decide on the scope for enabling Agent Builder: company-wide, per project, or for individual users.

### Permissions

Procore AI and Agent Builder strictly adhere to your existing Procore permissions.

- **Who can use Agent Builder and create an Agent?** Company admin can enable Agent Builder for everyone in a company, specific projects, or specific users.
- **Who can run an Agent?** Any user with Agent Builder access can create and run an Agent in Assist. However, to get the expected results, the user running the Agent must have the necessary permissions in all tools involved in the Agentâs tasks. For example, if you lack permission to view an RFI, the Agent will not provide information about that RFI, even if you created the Agent.

### Guidelines and Limits

- **For Procore AI products:**

 - Procore's AI can create new items and notify users about existing items, but it

    *cannot* modify or delete items. Learn more about our [AI parameters](/faq-how-are-data-security-and-validation-handled-with-procore-ai-products).
 - The AI asks for confirmation from the user before creating or sending an item.
 - Procore AI user interfaces are in English and use United States construction terminology. However, you can create Agents in most languages, and Assist can respond in that language.
- **For users:**

 - Agent Builder does not have predefined usage limits during the beta program. However, Procore may notify users or Admins if agent usage becomes exceptionally high.
 - It's important to validate all results and use AI tools appropriately. Review guidelines in

    [How are data security and validation handled with Procore AI products?](/faq-how-are-data-security-and-validation-handled-with-procore-ai-products)

## Features at a Glance

Any user can [build an Agent](/product-manuals/agent-builder-project/tutorials/build-an-agent) by giving it a name, choosing from a list of predefined [actions](/faq-what-actions-are-available-in-agent-builder), and writing instructions for its behavior. Or copy one our [Starter Agents](/faq-what-are-the-procore-starter-agents).
# Analyzing your business rules

Source: https://support.zendesk.com/hc/en-us/articles/4408889285530-Analyzing-your-business-rules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Tip: Check out [this video](https://support.zendesk.com/hc/en-us/articles/4408894141850) from our Customer Success team about rule analysis.

You can analyze your business rules with Rules analysis. For example, suppose that you'd like to understand how a particular group or agent is being assigned tickets or you want to optimize how tags are used across Zendesk Support so you'd like to see how they're currently being used. Rather than manually inspecting each business rule to assess their downstream effects on the workflow, Zendesk provides you with a tool for inspecting what can be a complex web of interactions.

You might use business rules analysis for the following situations:

- To locate the business rules that assign tickets to a specific agent. This can be helpful when an agent leaves for example.
- To find out why a specific agent or group is being assigned an unusual amount of tickets.
- To evaluate what business rules will be affected if you make changes to your custom fields.
- To update your business rules to reflect organizational changes you've made. Perhaps you've restructured and added or removed groups and responsibility for specific areas of support have changed.
- To track and make changes to how tags are being used throughout Zendesk Support.

Business rules analysis begins by summarizing how the following ticket properties are used in business rules:

- Group assignment
- Agent assignment
- Organization
- Channel
- Request received at email
- Macro reference
- Email user
- Email group
- Notify target
- Tag

**To access rule analysis**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Rule analysis**.

   The Rule analysis page appears. Only those ticket properties that are actively being used in business rules are displayed. Tags that appear in bold are in use by custom fields.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rules_analyze_initial_edit.png)
2. Click the arrows beside any ticket property to view the detail for that property value and analyze how it is being used in triggers, automations, macros, and views.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rules_analyze_details.png)

   In this example, triggers that reference (as a condition) or set (as an action) the Level 1 support group are displayed. You can select to show active (which is the default) or inactive business rules.
3. Click **Edit** to modify any business rule or hover your mouse over the business rule if you want to click **Clone** or **Deactivate**.
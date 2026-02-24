# Discovering light agents and contributors that also take up paid agent seats

Source: https://support.zendesk.com/hc/en-us/articles/4844001120410-Discovering-light-agents-and-contributors-that-also-take-up-paid-agent-seats

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > People > Team > Team members

Even though users with roles like Light agent and Contributor don’t take up an
agent seat in Support, granting these users permissions in other Zendesk products can increase
your seat usage. For example, a light agent doesn’t take up a Support seat, but a light agent
with Knowledge admin permission, requires a Support seat.

This issue arises most often in Suite accounts, where a user who is listed as a light agent
or contributor in Support has agent or admin access to other Suite products like Chat,
Explore, Guide, or Talk. A Zendesk Suite account is a bundle where seat assignment is
interdependent and the same agent uses a seat across all the core products.

## Filtering for seat usage

If your account uses more agent seats than you expected, you can use filters on
the Team members page to search for these types of users. This search technique is useful
for finding light agents with elevated permissions in other Zendesk products. You can use a
similar technique for contributors.

**To filter for seat usage**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.

   The [Team members page](https://support.zendesk.com/hc/en-us/articles/4408843830938) appears.
2. Click **Filters** and select **Support > Light agent** from the **Product and
   role** drop-down.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/role_filter_light_agent.png)
3. Click **Apply filters**.

   A list of light agents in your account appears.

   At this point, you could open the individual profiles for each light
   agent to see if they have expanded permissions, but this can be time consuming. Instead,
   you can narrow your results by including another role in the filter that requires an
   agent seat.
4. For example, click **Filters** and add **Guide > Admin** from the **Product and
   role** drop-down.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/role_filter_refine.png)
5. Click **Apply filters**.

   A list of light agents that also have a Guide
   admin role appears. This shows you which light agents are taking up an agent seat in
   your account.

   You can repeat these steps by filtering your light agents for other
   product roles until you discover all the light agents who are taking up seats in other
   products. See [Managing agent seats for Support](https://support.zendesk.com/hc/en-us/articles/4408834934554) and [About team member product roles and access](https://support.zendesk.com/hc/en-us/articles/4408832171034).
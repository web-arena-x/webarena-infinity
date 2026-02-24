# Changing an agent's role

Source: https://support.zendesk.com/hc/en-us/articles/4409155967258-Changing-an-agent-s-role

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Administrators can change an agent's Support role, for example, by promoting an agent's role to administrator or downgrading it to end user. Before proceeding, we recommend reading [Downgrading and removing an agent](https://support.zendesk.com/hc/en-us/articles/4408888690842), which contains suggestions to avoid some of the common pitfalls in this process.

This article covers the following topics:

- [Upgrading the agent to an administrator role](#topic_m51_vq5_w2b)
- [Upgrading a light agent’s role](#topic_qsp_w45_5zb)
- [Downgrading the agent to an end-user role](#topic_n1j_vq5_w2b)
- [Removing a user from your account](#topic_f4n_bq5_w2b)
- [Understanding role changes in the audit log](#topic_ixk_cjh_4xb)

## Upgrading an agent's role to administrator

Administrators can promote agents to the administrator role.

**To promote an agent to the administrator role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. From the list, click the agent you want to upgrade.
3. On the **Roles and access** tab of the agent's page, select **Admin** from the **Role** drop-down list for Support.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_promote_agent_admin.png)
4. When you're finished, click **Save**.

   An email is sent to all administrators notifying them that the agent has been added as an administrator.

The agent's existing group assignments remain; you can add or remove them from groups as needed.

## Upgrading a light agent’s role

Admins can promote a light agent to an agent (or an admin). You need an available agent seat to change the role.

**To promote a light agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. From the list, click the light agent you want to upgrade.
3. On the **Roles and access** tab of the agent's page, open the **Role** drop-down list for Support and change **Light agent** to **Agent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_light_agents_promote2.png)
4. When you're finished, click **Save**.

   An email is sent to all administrators notifying them that the light agent’s role has changed.

## Downgrading an agent's role

Administrators can downgrade an agent's role to end user.

**To downgrade an agent's role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. From the list, click the agent you want to downgrade.
3. In the upper-right, click **Manage in Support**.

   Alternatively, you can click **Go to user profile** under the list.
4. On the agent's profile, set the **User type** to **End user**.

   You'll see a warning screen that informs you of the privileges that will be lost by this user if you continue with the downgrade. Verify that this is what you want by selecting **Yes, downgrade this user** . Once you select this, your agent is no longer an agent and will no longer count towards your agent limit.

Note: Downgrading the agent does not change your agent seat count. You will be charged for the same number of agents unless you change your subscription (see [Changing plan subscriptions)](https://support.zendesk.com/hc/en-us/articles/4408834640666#topic_xtw_3kw_zgb).

Explore users might experience issues with some reports when they downgrade an agent.
Potential issues include:

- Reports that slice via user role can be affected, as the downgraded agent is now an end user.
- Report tabs with user filtering enabled will no longer show the downgraded agent in the drop-down.

If your Zendesk plan includes light agents, you may want to downgrade an agent to a light agent, then suspend them, to mitigate the impact on their Explore reports.

## Removing a user from your account

After downgrading the agent to an end user, you can suspend them from the account. This removes them from your Support instance.

**To suspend a user from your account**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click the **Customers** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.
2. Locate the agent who was downgraded to an end user and click **Edit**.
3. Click the drop-down icon at the top-right of the profile and select **Suspend access**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-suspend-updated.png)

## Understanding role changes in the audit log

When an admin changes an agent's Support role, the change to the Support role will be attributed to the admin as the actor in the audit log. Any associated changes, such as roles in other products or ticket restrictions, will be attributed to the system user.

For example, when an admin changes an agent's custom role and the new custom role includes editor access to Explore, you'll see two changes in the audit logs:

- The change to the Support role (the admin is attributed)
- The change to the Explore role (the system user is attributed)
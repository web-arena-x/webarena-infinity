# Using @mentions

Source: https://support.zendesk.com/hc/en-us/articles/4928739064986-Using-mentions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Use @mentions to add agents to tickets by typing "@" followed by their name in comments. This feature is available in public and private comments, adding agents as CCs or followers based on your settings. Note that light agents and contributors can't use @mentions. Ensure custom roles have "View user profile lists" enabled to access and use @mentions effectively.

Agents and admins can add other agents to the tickets using @mentions. End users can't be @mentioned.

Light agents and [contributors](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_pzw_3bs_qmb) can't use the @mentions feature (see [Understanding and setting light agent permissions](../../product-guides/team-members-and-groups/understanding-and-setting-light-agent-permissions.md)).

This article includes :

- [About @mentions](#topic_rvk_rh5_nvb)
- [Adding an agent with @mentions](#topic_b1n_qkx_vy)

Related articles:

- [CCs and followers resources](https://support.zendesk.com/hc/en-us/articles/4408836035866)

## About @mentions

The following table describes how @mentions work and what to expect when you @mention another agent. Your results may vary depending on what settings are enabled in your Support account and whether you @mention someone in a public or private comment.

| | In public comments (public reply) | In private comments (internal note) |
| --- | --- | --- |
| If CCs and followers are enabled, and **Automatically make an agent CC a follower** is enabled. | @mentioned agents are added as CCs and followers. | @mentioned agents are added as followers. |
| If CCs and followers are enabled, and **Automatically make an agent CC a follower** is disabled. | @mentions are added as CCs. @mentions are not added as followers. | @mentioned agents are added as followers. |
| If CCs are enabled, and followers are disabled. | @mentions are added as CCs. There’s no **Followers** field, so @mentions are not added as followers. | @mentions are not added as CCs or followers. |

## Adding an agent with @mentions

If you're an agent or admin, you can @mention other agents in tickets.

**To add an agent with an @mention**

1. Begin writing a comment (either Public reply or Internal note).

   Note: @mentions can’t be used in tickets created from the Facebook or X (formerly Twitter) channels because these types of tickets, and their comments, are plain text only.
2. In the body of the comment, type "@" followed by the beginning of the agent's name.

   For instance, if you want to include agent Jane Doe, type "@Jan".
3. Select the agent you want to add from the autocomplete menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/atmention_example.png)
4. Finish composing your message, and click **Submit**.

The agent mentioned is automatically CC'd on the ticket, and will receive all normal [CC email notifications](#topic_h5l_1yb_chb) for that ticket. If they are logged in, the added agent sees a notification in the upper-right corner of the Zendesk Support interface informing them that they were mentioned on the ticket. This notification disappears after one minute.

Important: If you're using Support Enterprise with custom roles, ensure that the setting **View user profile lists** is enabled in the custom role. Users need that setting enabled to access the list of agents and use @mentions.
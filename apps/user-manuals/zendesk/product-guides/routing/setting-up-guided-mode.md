# Setting up Guided mode

Source: https://support.zendesk.com/hc/en-us/articles/4408825479066-Setting-up-Guided-mode

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Guided mode helps you manage ticket order by restricting agents to using the Play button to navigate through tickets. Agents can access views and work on tickets one at a time. Agents can skip tickets and provide reasons, which you can review.

Location: Admin Center > People > Team > Roles

Ensure tickets are addressed in the appropriate order with Guided mode, a custom role option that requires agents to work through tickets in a view using the Play button.

Tip: You can more effectively determine which tickets agents work on by using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) to assign tickets directly to agents.

This article contains these sections:

- [Understanding the agent experience in Guided mode](#topic_mrz_tfw_tv)
- [Setting team member access to Guided mode](#topic_l2s_ty2_p5)
- [Viewing skipped tickets](#topic_d1v_31f_p5)

## About Guided mode

In Guided mode, agents can access views using the Play button. For more details, see [Using Play mode](https://support.zendesk.com/hc/en-us/articles/9186492658714). When agents click the Play button, the system automatically opens the first ticket in the view. After addressing the ticket, the agent submits the update and automatically moves to the next ticket.

In Guided mode, when an agent clicks the **Views** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, they can do either of the following:

- See and open all tickets assigned to them in the system Your assigned tickets view.
- Click on any other view to open its available ticket and start Play mode. They won't be able to see a list of the tickets in the view.

When you set up Guided mode, keep in mind that:

- Agents in Guided mode will still be able to view and open tickets they have access to from end-user or organization profiles and through search.
- Tickets in Guided mode aren't automatically assigned to the agent who is working on them unless you use one of the [routing and automation options](https://support.zendesk.com/hc/en-us/articles/4408831658650) to assign tickets.
- Guided mode may show an agent another agent's assigned tickets. This can happen if the tickets meet all view conditions, agent permission settings, and are not being viewed by another agent.

## Setting team member access to Guided mode

You'll need to create or edit a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) and assign it to the team members who should have Guided mode access.

**To assign Guided mode to a custom role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Roles**.
2. Next to the role you want to modify, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)), then select **edit**.
3. In the **Agent workflow** section, under **View permissions**, click **Play views only**.
4. Click **Save**.

## Viewing skipped tickets

In Guided mode, team members can choose to skip a ticket. After they click **Skip**, a window appears prompting them to enter a reason.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/playonly_skip_reason.png)

Guided mode team members can still click **Skip** in the above window without entering a reason. If you're looking for specific information from team members when they skip tickets, you should communicate expectations on entering reasons and how you'll be using the responses.

Review skipped tickets and reasons in a Guided mode team member's user profile. Looking through skipped tickets can help you identify specific knowledge areas and processes that team members are struggling with.

Admins can view skipped tickets for any agent in Guided mode. Guided mode agents can view their own skipped tickets only.

**To view a Guided mode team member's skipped tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Team members**.
2. Locate the agent you want to review.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)), then select **Manage in Support** to open the user's profile.
4. Click **Play only**.

   A list of tickets the agent has skipped, along with each reason entered, appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/play_only_profile_skipped.png)
5. Click a ticket to open it and view additional details.
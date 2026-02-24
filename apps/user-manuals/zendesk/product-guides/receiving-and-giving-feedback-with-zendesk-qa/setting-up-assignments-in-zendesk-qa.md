# Setting up assignments in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043747327770-Setting-up-assignments-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Assignments in QA help you manage and review support interactions by setting up recurring tasks for reviewers. You can create assignments, configure reviewers and reviewees, set conditions, and define goals. This feature allows you to tailor the review process to your needs, ensuring quality assurance and performance tracking. You can also convert conversation views into assignments for streamlined management.

Assignments in Zendesk Quality Assurance (QA) can help you manage and review customer support interactions. These recurring tasks consist of sets of conversations assigned to reviewers for evaluation based on specific criteria and predefined goals.

This article contains the following topics:

- [Creating assignments](#topic_kcp_yv1_cbc)
- [Creating an assignment based on a conversation view filter](#topic_ihh_dcl_rgc)

Related articles

- [Editing and updating workspace assignment status in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/8533419670298)
- [Viewing and managing your assigned conversations in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7317000589466)
- [Accessing and viewing the Assignments dashboard in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/8207770590490)

## Creating assignments

Admins, workspace managers, and leads can set up assignments. See [Understanding roles and permissions in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043760141978).

**To add a QA assignment**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. Choose your workspace, then click **Assignments**.
3. Click **Create assignment**.
4. On the **General** tab, enter an **Assignment name**.
5. Under Cycle settings, select how frequently the assignment cycle **Repeats**:
   **Never**, **Daily**, **Weekly**, **Bi-weekly**, or **Monthly**.

   Note: When the new cycle begins, Zendesk QA fetches all applicable conversations and then doesn't fetch or refresh the conversations again until the next cycle.
6. Select a custom **Start** date and time. For monthly assignments, also specify whether you want it to start on the same day every month or on specific dates (for example, the first day of the month or every fourth Thursday).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043668470426_1.png)
7. Select the **Timezone**.
8. Configure the assignment's [reviewers and reviewees](#topic_g5y_dw1_cbc).
9. Configure the assignment's [conditions](#topic_tx1_mdl_rgc).
10. Configure the assignment's [goal](#topic_pgh_jdl_rgc).
11. Click **Create assignment**.

Tip: If you need to update an assignment mid-cycle, you can do so without losing the cycle's progress. All given reviews will still count towards the goal of the assignment.

### Configuring assignment reviewers and reviewees

Use the Reviewers and reviewees tab to select the reviewers and reviewees for the assignment. When selecting who will review conversations, you can select all workspace users (except agents), a group or selection of groups, a user, or a selection of users.

You can also exclude users from reviewing conversations.

**To configure an assignment's reviewers and reviewees**

1. [Create a new assignment](#topic_kcp_yv1_cbc) or [edit an existing assignment](https://support.zendesk.com/hc/en-us/articles/8533419670298#topic_yvn_4wq_jhc).
2. Click the **Reviewers and reviewees** tab.
3. Under **Reviewers**, select one of the following options:
   - **Most active agent**: (Default) The user who sent the most public messages.
   - **Participant**: A user who left either a public reply or an internal note in a conversation.
   - **Assignee**: The owner of the help desk ticket.
4. (Optional) If necessary, under **Excluded reviewers**, select users who shouldn't be reviewers for the assignment.
5. Under **Reviewees**, select who is being reviewed: **Bots** or **Agents**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ZendeskQA_reviewees_bots_users.png)
6. Under **Who will be reviewed**, select which users or bots should be reviewed.
7. (Optional) If necessary, under **Exclude reviewees**, select users who shouldn't be reviewed for the assignment.
8. If reviewing users, under **Which types of users should be selected as reviewees**, select **Workspace default**, **Most active agent** (default), **Participant**, or **Assignee**.

### Configuring the conditions for the assignment

An assignment's conditions describe characteristics a conversation must have to be assigned to a reviewer by the assignment. For example, the conversations you want reviewed under the terms of an assignment might be summarized as "conversations with more than three replies from the previous 30 days."

Assignment conditions in Zendesk QA are the same as the [conversation filter types](https://support.zendesk.com/hc/en-us/articles/7043759449114-Finding-conversations-to-review-using-custom-filters#h_01HYBGTNNH3EK3E7S5S0RCGD4B).

Tip: To prevent previously reviewed tickets from being offered for review again, add the following assignment condition: **Review status | is | not reviewed**.

**To configure the assignment's conditions**

1. [Create a new assignment](#topic_kcp_yv1_cbc) or [edit an existing assignment](https://support.zendesk.com/hc/en-us/articles/8533419670298#topic_yvn_4wq_jhc).
2. Click the **Conditions** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043668470426_3.png)
3. Under **Date**, **Conversation**, or **Help desk**, click the add icon to add at least one condition to the assignment.

   For Conversation conditions, you can search for conditions by name or click the **Show all conditions** toggle to the on position.

### Configuring the assignment goal

The assignment goal is highly configurable. If you already have a QA approach, you can reflect the current process in these settings.

**To configure the assignment goal**

1. [Create a new assignment](#topic_kcp_yv1_cbc) or [edit an existing assignment](https://support.zendesk.com/hc/en-us/articles/8533419670298#topic_yvn_4wq_jhc).
2. Click the **Goal** tab.
3. Under **Assignment approach**, select **Reviewers can choose conversations from the shared pool** or **Reviewers are assigned conversations from the shared pool**.
4. Under **Review goal**, select one of the three options:
   - **Reviewers must collectively review a set number of conversations**: Set an exact number or a percentage of conversations reviewers need to cover.
   - **Each reviewer must do a set number of reviews**: Specify the individual goal for each reviewer.
   - **Each reviewee must have a minimum number of their total conversations reviewed**: Define the reviewee-based objective by setting a specific number or percentage of conversations that must be rated for each reviewee.
5. (Optional) Under **Advanced settings**, you can configure the following settings by clicking the toggles to the on position:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_assignment_goal.png)

   - **Specify minimum reviews for each reviewee**: Turn this option on to ensure that a minimum number of reviews per reviewee are covered.
   - **Allow reviewers to be assigned their own conversations for review**: Turn this option on to allow your reviewers to do self-reviews.

     Note: The agent role does not have access to assignments.
   - **Allow replacing conversations (Reviewer and above)**: In some cases, reviewers might want to skip a conversation in an assignment. Turn this option on if you want reviewers to be able to [choose a different conversation to review](https://support.zendesk.com/hc/en-us/articles/7317000589466#topic_ywc_pzp_jhc)
     instead of the one provided from the list.

## Creating an assignment based on a conversation view filter

Another way to create an assignment is from a [conversation filter](https://support.zendesk.com/hc/en-us/articles/7043759449114).

**To turn a conversation view into an assignment**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Conversations**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_conversations_icon.png) in the sidebar.
2. Click **Public filters** or **Private filters** to display a list of your public or private filters.
3. Next to the filter you want to turn into an assignment, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_horizontal.png)) and select **Edit**.
4. At the bottom of the page, click **Turn into an assignment**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043668470426_10.png)
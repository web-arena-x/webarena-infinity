# Managing workspace general settings in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043668704026-Managing-workspace-general-settings-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Admins and workspace managers can customize workspace settings by editing names, colors, and general settings. You can enable unbiased grading to hide other reviewers’ feedback, allow agents to review their own conversations, and set a default reviewee to direct feedback. Remember, deleting a workspace removes all data and cannot be undone.

Location:  Zendesk QA > Dashboard > Users, bots, and workspaces

Admins and workspace managers can set up and edit the workspace’s name and representative
color. They can also configure other workspace’s general settings, including activating
unbiased grading to hide other reviewers’ feedback, allowing agents to review their own
conversations, setting a default reviewee for direct feedback, and [deleting a workspace](https://support.zendesk.com/hc/en-us/articles/7043759641242).

**To manage a workspace’s general settings**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner, then select **Users, bots, and workspaces**.
2. Under **Workspaces**, click the name of the workspace you want to edit, then
   click **General**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_workspace_general.png)
3. Configure the following workspace settings:
   - **Unbiased grading**. When this option is selected, users with
     the [reviewer role](https://support.zendesk.com/hc/en-us/articles/7043760141978#topic_dzc_fgq_q2c) can't see reviews
     left by other reviewers, including AutoQA, in both the [Activity](https://support.zendesk.com/hc/en-us/articles/7043760283546#understanding-received-reviews) and the [Conversations view](https://support.zendesk.com/hc/en-us/articles/7043661945370). Otherwise,
     AutoQA is visible under Activity.
   - **Self-reviews**. When this option is selected, agents can
     [review their own conversations](https://support.zendesk.com/hc/en-us/articles/7043669307418).
     Reviewers, leads, and workspace managers can also use assignments to perform
     self-reviews. Agents can see the AutoQA scores for their own tickets. AutoQA
     remains visible to reviewers in the Conversations view when submitting
     self-reviews, even if the Unbiased grading option is selected. When the
     Self-reviews option isn't selected, AutoQA is not visible in the
     Conversations view.
   - **Default reviewee**. Selecting a default reviewee ensures
     feedback is directed to the most appropriate agent. Options include:
     - **Most active agent**: The agent who sent the most
       replies in a conversation.
     - **Assignee**: The agent assigned to the
       conversation.
4. Click **Save changes**.
# Getting started with Zendesk QA: Admin guide

Source: https://support.zendesk.com/hc/en-us/articles/10093676975898-Getting-started-with-Zendesk-QA-Admin-guide

---

Zendesk Quality assurance (QA) leverages AI to automate 100% of ticket reviews. By analyzing every interaction, you can quickly uncover trends and identify areas for improvement, which boosts efficiency, enhances agent performance, and ultimately leads to better customer experiences.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Leverage AI-powered quality assurance to automate ticket reviews, uncover trends, and improve customer experiences. Set up a structured QA process, define quality standards, and use AI to flag critical interactions for review. Manage users and workspaces, create rating categories and scorecards, and monitor performance through dashboards. Enhance service quality with targeted coaching sessions, quizzes, and calibration to ensure consistent feedback.

Zendesk Quality assurance (QA) leverages AI to automate 100% of ticket reviews.
By analyzing every interaction, you can quickly uncover trends and identify areas for improvement, which boosts efficiency, enhances agent performance, and ultimately leads to better customer experiences.

This guide is recommended for anyone responsible for quality assurance planning and implementation, as well as the initial configuration and organizational setup of Zendesk QA.

Tip: You can quickly start leveraging AI to detect predefined QA concerns in live ticket conversations by using Real-time QA insights in Agent Workspace. See [Real-time QA insights (EAP)](https://support.zendesk.com/hc/en-us/articles/9745122485914).

This article includes the following topics:

- [Understanding quality assurance](#topic_cfy_hv5_zfc)
- [Planning your implementation](#topic_cnq_gqn_shc)
- [Accessing Zendesk QA](#topic_hxv_n41_c3c)
- [Reviewing your help desk connection](#topic_cmg_lq1_c3c)
- [Granting users access to Zendesk QA](#topic_bqv_vqn_shc)
- [Planning and creating workspaces](#topic_kjg_lq1_c3c)
- [Setting up scorecards and using AI-powered tools to review and evaluate customer conversations](#topic_qh4_fsn_shc)
- [Ensuring service quality with monitoring and coaching](#topic_rpf_jsn_shc)
- [More resources and next steps](#topic_uhc_4sn_shc)

## Understanding quality assurance

[Quality assurance (QA)](https://www.zendesk.com/blog/quality-assurance/) is a systematic approach that ensures products and services consistently meet customer expectations, achieve service targets, and adhere to industry standards.

Support teams are the eyes and ears of the company. While automated metrics like first response time indicate the team's speed, they don't capture whether an agent goes the extra mile to provide excellent service or if the agent is rude, gives incorrect technical advice, or misses a major security step. Monitoring QA allows you to spot patterns that metrics alone miss.

In customer support, QA is rarely the responsibility of just one person.
Instead, it’s typically distributed across several roles, depending on the size of the company.

Common roles responsible for QA include:

- **Peer reviewers** who are typically experienced senior agents who spend a few hours a week reviewing tickets from newer peers.
- **QA specialists or analysts** typically perform ticket audits by reviewing transcripts and call recordings. They usually score interactions based on accuracy, empathy, brand voice, and technical resolution.
- **Support team leads and supervisors** typically review a subset of their own team's tickets to ensure their direct reports are following protocol, and use QA results to have 1-on-1 development conversations with agents.
- **QA managers and heads of quality** typically design the quality framework by deciding which metrics matter (for example, CSAT vs. IQS), deciding which tools to use, and ensuring the QA process itself is fair and consistent, by performing calibrations.

Monitoring ticket conversations with Zendesk QA helps you understand customer issues and assess customer interactions.

AI-powered QA tools automatically scan tickets for sentiment, grammar, tone, or any other issues you consider valuable. They flag problematic tickets for human review, so QA peer reviewers, specialists, analysts, team leads, supervisors,managers, or heads of quality don't have to search for them manually.

Agents feel more supported when they receive fair, transparent feedback rather than being judged solely on a single angry customer rating (CSAT). With Zendesk QA you can review every single ticket conversation and gain instant insight into your support teams’ performance.

You can monitor and compare general metrics, such as your Internal Quality Score (IQS) against your CSAT (Customer Satisfaction). You can then examine specific conversations to understand the causes of any issues, allowing you to continuously train your teams and improve your service.

Zendesk QA also helps you evaluate how well your [AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690) perform in conversations with your customers.
You can then analyze the results and use this information to update your AI agents and customer service workflows as needed.

## Planning your implementation

Effective quality assurance requires a well-defined structure and strategy.
Here are some key steps to perform QA effectively:

- **Define your quality standards**: Set measurable criteria that reflect your brand and regulatory requirements. See [Understanding the quality indicators on the Reviews dashboard cards](https://support.zendesk.com/hc/en-us/articles/7043724913690#topic_cwx_3qw_42c).
- **Plan your QA process**: Decide who will conduct reviews, how often, and what tools or QA scorecards you’ll use to evaluate performance. See [Methods for reviewing customer support conversations](https://support.zendesk.com/hc/en-us/articles/7043760307482).
- **Train your team**: Ensure everyone understands the QA standards and receives ongoing training to stay aligned. See [More resources and next steps](#topic_uhc_4sn_shc).
- **Use AI as your first line of defense**: Leverage AI-powered tools to automatically detect the most critical interactions that need human review.
 See [About AI insights in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/9224552305946).
- **Automatically assign tickets for human review**: Use AI to route flagged interactions to the appropriate reviewers, ensuring timely attention.
 See [Setting up assignments in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043747327770).
- **Monitor performance and provide coaching**: Use quality monitoring to track agent performance and identify coaching opportunities. See [Ensuring service quality with monitoring and coaching](https://docs.google.com/document/d/1OwxT9VsVANF7wTM9R7vzryG27So2Pzm04jYHm9A5IJg/edit?tab=t.0#heading=h.gbar2ldtw7tt).
- **Calibrate regularly and perform Reviewer QA**: Align reviewer standards and evaluate the reviewers to maintain consistency. See [Ensuring service quality with monitoring and coaching](https://docs.google.com/document/d/1OwxT9VsVANF7wTM9R7vzryG27So2Pzm04jYHm9A5IJg/edit?tab=t.0#heading=h.5dp9zpw0k0g3).

It’s important to note that QA works best as an ongoing cycle. A consistent and evolving QA process helps you identify issues early and strengthen team performance. Over time, this leads to more reliable service and stronger customer relationships.

## Accessing Zendesk QA

By default, the Zendesk account owner is the only user with access to the add-on and has a role of Admin in Zendesk QA.

To get started setting it up, you can access Zendesk QA from anywhere in Zendesk.

**To access Zendesk QA**

- Click the **Zendesk products** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/products_icon2.png)) in the top bar, then select **Quality assurance**.

The Conversations view is the primary area where you land.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_review_conversation.png)

Here, agents access the conversations they've worked on, and admins, managers, and reviewers evaluate those conversations. See [Using the Conversations view](https://support.zendesk.com/hc/en-us/articles/7043661945370).

Reviewers can leave scores and provide feedback to agents, helping improve customer support quality and overall agent performance. See [Using Zendesk QA as a reviewer](https://support.zendesk.com/hc/en-us/articles/7043669307418).

## Reviewing your help desk connection

All support requests, from all channels, become tickets in [Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408881925786). Tickets capture your customer's initial request for support and all the conversations your agents have with the customer along the way to solving their support issue. When you [buy the Zendesk QA add-on](https://support.zendesk.com/hc/en-us/articles/6851584037146), all your Zendesk ticket conversation-data automatically imports into Zendesk QA. Ticket conversations from your Support help desk sync with Zendesk QA every four to six hours.

Tip: Call recordings must be imported into Zendesk QA before they can be analyzed. To do this, [activate Voice QA](https://support.zendesk.com/hc/en-us/articles/8536077648538).

You can review your connection to Support, and configure it as needed. For example, you may want to protect the privacy of your customers and support agents by filtering out selected content, ensuring it's not visible to reviewers or stored by Zendesk QA. Or you might select a retention period, so conversations that remain inactive for the specified time are automatically deleted. See [Managing help desk connections in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043712839450).

## Granting users access to Zendesk QA

By default, the Zendesk account owner is the only user with access to the add-on and the account owner has a role of Admin in Zendesk QA.

Grant access to each user who will manage settings, participate in reviews, or be reviewed in conversations. Access to the Quality assurance add-on is controlled in Admin Center.

The following table shows the Zendesk QA roles available in Admin Center.

| | |
| --- | --- |
| **Role** | **Description** |
| Admin | Can see everything and manage all settings. |
| Agent | Can view their own conversations, reply to feedback, and view their customer reviews. They have workspace-specific permissions and can view and edit data within their assigned workspaces only. They also have access to their own dashboard and can perform self-reviews, if enabled. |
| Reviewer | Can view all reviews but cannot edit workspace settings. Can perform peer reviews. |
| Workspace lead | Can view everything in the workspace and manage quizzes, assignments, groups, disputes, and calibration sessions. Cannot edit other workspace settings or scorecards. |
| Workspace manager | Can view all reviews and manage all workspace settings. |
| Connected user | Connected users don't have access to Zendesk QA. Their conversations are available for review, but these agents are unaware that they're being reviewed. |

**To give a user access to Quality assurance**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. On the **Team members** page, scroll through the list or use the search option to find the user you want to grant access to, then click to open their profile.
3. Click the **Roles and access** tab.
4. Beside Quality assurance, click the **Access** checkbox.
5. Use the **Role** dropdown next to Quality assurance to select a role for the user.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_admin_user_role.png)
6. Click **Save**.

You can review users in the Users page to confirm that the right people are present and have the correct permissions for QA workspaces.

**To access the Users page in Zendesk QA**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. In the side menu, click **Users**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_users.png)

To learn more see [Understanding roles and permissions in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043760141978).

## Planning and creating workspaces

A workspace allows reviewers to review conversations using one set of criteria. All accounts have one default workspace. Once given access to Zendesk QA, all new users are automatically assigned to the account’s default workspace called Zendesk.

You cannot remove users from the account’s default workspace. However, you can create additional workspaces, and change the default workspace, if needed.

There are good reasons to configure Zendesk QA to use a single workspace or multiple workspaces. Understanding the benefits of each option helps you optimize your team's workflow and review processes. At a high level:

- Sharing a **consolidated workspace** works well for teams that measure performance in the same way, such as small teams, teams with a flat hierarchy, and teams where everyone works across the same range of conversations.
- Creating **multiple workspaces** allows you to segment users and define different review criteria for each workspace.

**To create a new workspace**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. In the navigation panel, click the create workspace icon (+) next to **Workspaces** to create a new workspace.
3. Enter a unique name for the workspace.
4. Click **Create workspace**.

   Within each workspace, you can configure the following settings:

   - **Members**: Add or remove users from the workspace and change their permissions for that workspace. See [Managing workspace members](https://support.zendesk.com/hc/en-us/articles/9203020826266).
   - **General**: Set or edit the workspace name and representative color, turn unbiased grading and self-reviews on or off, and select the default reviewee. See [Managing workspace’s general settings](https://support.zendesk.com/hc/en-us/articles/7043668704026).
   - **Hashtags**: Manage custom hashtags and track their usage.
     See [Adding custom hashtags to Zendesk QA comments](https://support.zendesk.com/hc/en-us/articles/7043700996762).
   - **Threshold**: Set the overall QA goal for the workspace.
     Scores below the threshold appear in red, while scores above it appear in green. See [Setting a performance reporting threshold in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043700991514).
   - **Assignments**: Set up automatic assignment of conversations based on specific conditions. See [Setting up assignments in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043747327770).
   - **Calibration**: Ensure consistent feedback by having reviewers rate the same conversations and comparing their evaluations.
     See [Setting up calibration in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043724530842).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_workspace_members_remove.png)

In General settings, set your default workspace. You can also configure key account settings and adjust other global options that apply to all workspaces, such as notification preferences, AI and automation, privacy, and review workflows. To learn more, see [Viewing and updating Zendesk QA account settings](https://support.zendesk.com/hc/en-us/articles/7043669430426).

**To change the account’s default workspace**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **General**.
4. Use the Default workspace drop-down to select your preferred default workspace for all users.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_account_settings.png)
5. Click **Save changes**.

## Setting up scorecards and using AI-powered tools to review and evaluate customer conversations

Quality assurance encompasses a variety of methods to review and evaluate performance and improve quality across customer interactions and operational workflows.

**A scorecard** defines how conversations are evaluated. You can customize or create new scorecards to evaluate agent performance, identify improvement areas, and ensure your team meets organizational goals. You can add categories, set rating scales, and define weights to highlight important aspects of customer interactions. Use conditional scorecards to streamline reviews based on specific criteria, and add root causes for detailed feedback. Once set up, publish your scorecard to start assessing your team's quality assurance process. See [Creating scorecards](https://support.zendesk.com/hc/en-us/articles/7043760215194).

**Spotlight insights** enhance your QA process by automatically highlighting key interactions for review, using predefined insights like outliers, churn risk, and exceptional service. This tool helps you identify improvement opportunities by analyzing conversations and tagging them with performance indicators. Access insights through the Feedback section in conversations to quickly assess and address customer interactions. See [Understanding spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074).

**Autoscoring** evaluates and scores all customer interactions automatically, helping you maintain consistent quality assessments and save time. By activating autoscoring categories you can identify training needs across categories like empathy, tone, and comprehension. See [Understanding autoscoring categories](https://support.zendesk.com/hc/en-us/articles/7043747123354).

**Prompt-based AI insights** leverage the latest AI models, allowing you to customize AI-powered prompts using natural language for quality autoscoring and risk detection. By using AI prompt-based categories, you can ask targeted questions about conversations using natural language and automatically score them based on your criteria. See [About AI insights in Zendesk QA.](https://support.zendesk.com/hc/en-us/articles/9224552305946)

## Ensuring service quality with monitoring and coaching

To ensure consistent monitoring, you can automate the process of getting the right tickets in front of the right reviewers.

Create assignments for managers or peer reviewers and set review goals.
These recurring tasks consist of sets of conversations assigned to reviewers for evaluation based on specific criteria and predefined goals. For example, to review five technical tickets per week for each agent.

**To create an assignment**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. Choose your workspace, then click **Assignments**.
3. Click **Create assignment**.
4. On the **General** tab, enter an **Assignment name**.
5. Under **Cycle settings**, select how frequently the assignment cycle **Repeats**: Never, Daily, Weekly, Bi-weekly, or Monthly.
6. Select a custom **Start date and time**. For monthly assignments, also specify whether you want it to start on the same day every month or on specific dates (for example, the first day of the month or every fourth Thursday).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043668470426_1.png)
7. Select the **Timezone**.
8. Configure the assignment's [reviewers and reviewees](../../product-guides/receiving-and-giving-feedback-with-zendesk-qa/setting-up-assignments-in-zendesk-qa.md#topic_g5y_dw1_cbc).
9. Configure the assignment's [conditions](../../product-guides/receiving-and-giving-feedback-with-zendesk-qa/setting-up-assignments-in-zendesk-qa.md#topic_tx1_mdl_rgc).
10. Configure the assignment's [goal](../../product-guides/receiving-and-giving-feedback-with-zendesk-qa/setting-up-assignments-in-zendesk-qa.md#topic_pgh_jdl_rgc).
11. Click **Create assignment**.

Use Zendesk QA to run calibration cycles. Calibration aligns reviewers by having them rate the same conversations and compare evaluations, ensuring consistent feedback for agents. Have multiple reviewers score the same ticket to ensure everyone is aligned on what "good" looks like, reducing bias and ensuring fair coaching. See [Setting up calibration in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043724530842).

Once you've identified gaps, create coaching sessions. You can bundle specific conversations and pinned notes into a formal coaching session. You can also track when coaching sessions occurred and whether agents have reviewed the feedback they received. See [Understanding coaching sessions](https://support.zendesk.com/hc/en-us/articles/7043747156506).

Analytics and dashboards offer a real-time overview and highlight trends in service quality across human and AI agents, teams, and channels. You can create custom views to select which cards to display or hide, and download reports that give you an overview of your Zendesk QA data. Use dashboard filters to efficiently locate the data necessary for assessing and enhancing your team's performance. See [About dashboards in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043701144858).

## More resources and next steps

Depending on their role in setting up or using Zendesk QA, make sure your team members review the following:

- [Using Zendesk QA as a reviewer](https://support.zendesk.com/hc/en-us/articles/7043669307418)
- [Using Zendesk QA as an agent](https://support.zendesk.com/hc/en-us/articles/7043760283546)
- [Zendesk QA video webinar tutorials and tips](https://www.youtube.com/playlist?list=PLb00xo9zloI5eXpazvz_VnmHjb4a_gsKG)
- [Online course: Setting up a perfect customer service review program](https://training.zendesk.com/setting-up-the-perfect-customer-service-review-program)

When you’re ready to learn more, you may find the following resources helpful:

- [Setting up Zendesk QA](https://support.zendesk.com/hc/en-us/sections/7162431070618)
- [Receiving and giving feedback with Zendesk QA](https://support.zendesk.com/hc/en-us/sections/7162462801562)
- [Working with users and workspaces in Zendesk QA](https://support.zendesk.com/hc/en-us/sections/7162447218330)
- [Using Zendesk QA for coaching](https://support.zendesk.com/hc/en-us/sections/7162479059098)
- [Working with the dashboard in Zendesk QA](https://support.zendesk.com/hc/en-us/sections/7162457497114)
- [Working with conversations in Zendesk QA](https://support.zendesk.com/hc/en-us/sections/7162471604890)
- [Integrating Zendesk QA](https://support.zendesk.com/hc/en-us/sections/7162489443354)
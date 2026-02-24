# Setting up calibration in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043724530842-Setting-up-calibration-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Calibration aligns reviewers by having them rate the same conversations and compare evaluations, ensuring consistent feedback for agents. You can set up and conduct calibration sessions without affecting the Internal Quality Score. Use the Calibration dashboard to view results, but note that no notifications are sent, and reviews remain separate from the main dashboard.

Calibration is the practice of having all your reviewers rate the same batch of conversations and compare their scores and comments. This ensures that your reviewers are aligned in their evaluations, providing consistent feedback to agents regardless of who conducts the review.

[Admins, workspace leads, and managers](https://support.zendesk.com/hc/en-us/articles/7043760141978) can perform calibrations.

This article contains the following topics:

- [Understanding calibration](#topic_typ_bhj_vhc)
- [Setting up calibration](#topic_yvn_4wq_jhc)
- [Conducting calibration](#topic_ows_lv2_p2c)
- [Viewing calibration results](#topic_zwd_xfr_jhc)

## Understanding calibration

Calibration ensures that reviewers provide consistent feedback by having them rate the same conversations and compare their evaluations. Regular calibration helps maintain uniformity in reviews, ensuring that agents receive similar feedback regardless of the reviewer.

Agents do not see any conversation-related information in calibration.

No notifications are sent to reviewers, so it's up to the workspace manager or lead to inform reviewers about the calibration session and its due date.

## Setting up calibration

Calibration can be done within the existing workspace, and the calibration scores don't affect the existing [Internal Quality Score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_sws_4ww_42c).

**To set up calibration**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. Choose your [workspace](https://support.zendesk.com/hc/en-us/articles/9202963091866).
3. Click **Calibration**.
4. Click the **Calibration** toggle to the on position.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_calibration.png)
5. Select the visibility of previously given reviews:

   - **Not visible**: Previously given reviews are not displayed when a conversation is added to the session.
   - **Visible**: Previously given reviews are regarded as calibration reviews. Only one conversation review per reviewer will be added to the session. Message-specific reviews are not displayed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_calibration.png)
6. Select the visibility of calibration reviews for:
   - **Reviewers**: You can choose to allow workspace reviewers to see only their own reviews, or to see their peers' reviews after submitting their calibration review.
   - **Lead**: You can choose to allow workspace leads to see evaluations given by other reviewers during a calibration session only after submitting a review or to always see all reviews.
   - **Manager**: You can choose to allow workspace managers to see evaluations given by other reviewers during a calibration session only after submitting a review or to always see all reviews.
7. Click **Save changes**.

## Conducting calibration

Calibration can be conducted within the same workspace where you perform regular reviews.

**To conduct calibration**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Tasks** ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_tasks_icon.png) in the sidebar.
2. Click the plus sign (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_plus_sign.png)) next to Tasks, then select **Create calibration session**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_create_assigment_calibration.png)

   You can also view the list of previous Calibration sessions here.
3. Enter a name for the calibration session.
4. Set a due date for the calibration session. Deadlines can be extended if needed.
5. Click **Create session**.
6. When you find a [conversation](https://support.zendesk.com/hc/en-us/articles/7043661945370) that you want to add to the calibration session, use the **Add to/remove from calibration session** button at the top.

   Once reviews are submitted, you can mark one review as the baseline for others by clicking the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) next to it. This makes it easier to compare scores against it. The baseline is marked with the label 'Baseline review'.

   Workspace managers can add and remove baseline reviews.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_add_to_calibration_baseline.png)

## Viewing calibration result

The [IQS](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_sws_4ww_42c) of the selected workspace remains unaffected by calibration reviews.

You can view the list of conversations and their associated reviews in the [Calibration dashboard](https://support.zendesk.com/hc/en-us/articles/7043701144858).

No notifications are triggered, and calibration reviews, comments, and scores do not appear on the main dashboard; they are exclusively available in the Calibration dashboard.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_dashboard_baseline.png)
# Creating and managing unassigned shifts (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/8847380904346-Creating-and-managing-unassigned-shifts-EAP

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Note: The new unassigned shifts feature, available in the Week view for schedules, is currently in an early access program (EAP). You can sign up for the EAP [here](https://forms.gle/DTTsM3Eq5fJsimrF7).

Admins can create shifts that they intentionally don’t assign to agents. These shifts become available for agents to request, or can be manually assigned by an admin at a later time.

This article contains the following topics:

- [Understanding how unassigned shifts work](#topic_spv_fsl_g2c)
- [Creating unassigned shifts](#topic_cs5_tkb_j2c)
- [Sharing unassigned shifts](#topic_d3d_cvm_g2c)
- [Approving unassigned shift requests](#topic_wx2_rvd_k2c)
- [Editing unassigned shifts](#topic_ww2_rvd_k2c)
- [Deleting unassigned shifts](#topic_p11_d12_k2c)

Related articles

- [About the WFM schedule page](https://support.zendesk.com/hc/en-us/articles/6443348256794)
- [Viewing and managing your schedule as an agent](https://support.zendesk.com/hc/en-us/articles/6443374353434)
- [Requesting to take unassigned shifts (EAP)](https://support.zendesk.com/hc/en-us/articles/8847379712794)

## Understanding how unassigned shifts work

By allowing the creation of unassigned shifts, managers can ensure optimal coverage without focusing on specific individuals. Additionally, it helps distribute the extra work among the agents who are willing to take on additional shifts and allows agents to select their preferred shifts.

Unassigned shifts are visible only in the Week view. They are highlighted in yellow under the Unassigned shifts row in the schedule. Once these shifts are [shared with agents](#topic_d3d_cvm_g2c), they will change to gray.

From the schedule, you can click on an unassigned shift to view its details, such as the number of available shift slots and the agents eligible to take them, in a panel on the right.

Shifts that remain unassigned are deleted 24 hours after the unassigned shift’s time. This helps prevent skewing the staffing panel results.

Agents can view and request available shifts. These requests are sent to their manager for approval.

## Creating unassigned shifts

Admins can create new unassigned shifts from the Zendesk Workforce management (WFM) Schedule page.

**To create an unassigned shift**

1. In [Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/4408838272410), hover over the schedule icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)) in the navigation bar, then select **Schedule**.
2. Click the **View** menu next to the date picker and select **Week**.

   The **Unassigned shifts** menu will appear at the top of the search and filtering panel on the left.
3. Hover over **Unassigned shifts** and click the **Add** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_add_unassigned_shifts+.png)

   Alternatively, you can also click the **Add** icon (![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdBHmCGQB5CduDGOFHU0Waal6OOsOO0GfX2xmFfImmmABB_AITEGx5NVCoAWg5XluI-t2Io-kKytRyQp47DOj69nbYXlFL9bHGOFohi2SLJ8e8d5Xwpz8xiq6cChx4sRiuXXSC77Q?key=6KyC-wGVLUmzOQrx634lNIhF)) by hovering over the applicable day of the week on the Unassigned shifts row.
4. Select the [shift or intraday](https://support.zendesk.com/hc/en-us/articles/6443345205402) that you want to use.

   Automatic shifts can’t be selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_add_unassigned_shifts_shift.png)
5. For **Shift distribution**, select one of the following options:
   - **Identical shifts**: Use the exact same shift and intraday schedule for the shifts. This means that the same shift can be taken by multiple agents.
   - **Optimized shifts**: Creates identical replicas of the shift. Each shift has a unique intraday schedule optimized for daily coverage. This option can help prevent coverage gaps.
6. Select the **Workstreams** you want your agents to work on during this shift.
7. Select the **Date range** for the unassigned shifts you want to create.
8. For each day in the date range, specify the **number of unassigned shifts**.

   If you’re using identical shift distribution, the number of unassigned shifts each day defines the number of agents who can take the same shift. However, if you’re using optimized shift distribution, this value determines the number of similar, but separate shifts that are created; each of the separate shifts can be taken by a single agent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_add_unassigned_shift.png)
9. Click the **Agent access** tab and select who can view and request this shift from the shift pool.
10. Click **Submit**.
11. Share the unassigned shifts with agents so they can request them.

## Sharing unassigned shifts

After creating unassigned shifts, you must share them before agents can access and request them in their [My Schedule view](https://support.zendesk.com/hc/en-us/articles/6443374353434).

**To Share an unassigned shift**

1. In [Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/4408838272410), hover over the schedule icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)) in the navigation bar, then select **Schedule**.
2. Click the **Share unassigned shifts button**.
3. Select a date range for the shifts that you want to share. .

   You may want to share only unassigned shifts created within a specific date range, which may not include all unassigned shifts you have created.
4. Click **Share**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_share_unassigned_shifts.png)

Shared unassigned shifts appear in gray. Agents can now request these shifts, which must be approved by their managers.

## Approving agent requests for unassigned shifts

Agents can request unassigned shifts, but these shifts do not officially become part of their schedule until their manager approves the requests.

Unassigned shifts remain available for request in the shifts pool by any agent listed in the unassigned shift's Agent access list until a manager makes a decision or the shift is deleted. It's up to the manager to identify overlapping requests and make a final decision.

Approving a request for an unassigned shift automatically rejects all other requests for that shift.

After an unassigned shift request is approved, it replaces any previously scheduled shift for that agent on that day.

**To approve or deny agents' unassigned shift requests:**

To approve or deny agents’ unassigned shift requests:

1. In [Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/4408838272410), hover over the schedule icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)) in the navigation bar, then select **Unassigned shift management**
2. Click **Pending** in the top right.

   A list of unassigned shifts requests from the agents you manage is displayed.
3. Hover over each request and select **Deny** or **Approve**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_unassigned_shifts_mgmt_approve.png)

You can view a list of all your denied, approved, and expired requests by clicking Closed in the top right.

When a request is approved, the schedule is updated to display the agent’s new shift.

## Editing an unassigned shift

**To edit an unassigned shift**

1. In [Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/4408838272410), hover over the schedule icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)) in the navigation bar, then select **Schedule**.
2. Click the **View** menu next to the date picker and select **Week**.

   The **Unassigned shifts** menu will appear at the top of the search and filtering panel on the left. If necessary, click the arrow to expand the section
3. Click any unassigned shift to display its details on the right side.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/wfm_unassigned_shifts_row_edit.png)
4. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) next to the shift date and select **Edit**.
5. Edit any of the unassigned shift details.
6. Click **Save**.

## Deleting an unassigned shift

Deleting a shift permanently removes it from the schedule and the shift pool. Any existing requests for that shift will be automatically denied.

**To delete an unassigned shift**

1. In [Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/4408838272410), hover over the schedule icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)) in the navigation bar, then select **Schedule**.
2. Click the **View** menu next to the date picker and select **Week**.

   The **Unassigned shifts** menu will appear at the top of the search and filtering panel on the left. If necessary, click the arrow to expand the section
3. Click any unassigned shift to display its details on the right side.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/wfm_unassigned_shifts_row_edit.png)
4. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) next to the shift date and select **Delete**.
5. Click  **Delete shift**.
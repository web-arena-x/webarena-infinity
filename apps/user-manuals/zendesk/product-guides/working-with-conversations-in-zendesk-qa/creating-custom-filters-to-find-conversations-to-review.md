# Creating custom filters to find conversations to review

Source: https://support.zendesk.com/hc/en-us/articles/7043669455130-Creating-custom-filters-to-find-conversations-to-review

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Create custom filters to quickly find specific conversations for review based on your criteria. Customize filters by setting visibility, date range, and conditions like review status and churn risk. Add, edit, or delete filters to streamline your process and focus on important conversations. Use the "Turn into assignment" option to convert filters into tasks for efficient management.

Location: Zendesk QA > Conversations

Your Zendesk QA account comes with a set of [predefined filters](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) to help you navigate through your conversations. However, you can also create custom filters to meet your specific needs.

Custom filters in Zendesk QA allow you to quickly locate specific conversations for review based on your chosen criteria. By setting up these filters, you streamline your review process and ensure that you focus on the conversations that matter most.

You can add as many filters as needed. You can also [edit, delete, clone, and rearrange your filters to customize the order](https://support.zendesk.com/hc/en-us/articles/9147011738650). For a comprehensive list of filters and their functions see [Understanding conversation filter types in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043759449114).

**To create a new custom filter**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_conversations_icon.png)
   **Conversations** in the sidebar.
2. Next to **Public filters** or **Private filters**, click the plus icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)) to create a new filter.
3. Enter a **Filter name**, for example “*Incorrect solution*”.
4. Choose whether the filter should be accessible to everyone in your account or only to you by setting its visibility to either **Public** or **Private**.

   Public filters are visible to all users, except [Workspace agents](https://support.zendesk.com/hc/en-us/articles/7043760141978).
5. (Optional) Select a **Date**. For new filters, the default condition is set to display conversations that were initially created within the last 30 days.
6. Turn on **Show all conditions** to display all available filters. You can either use the search box to find the filter type you want to create or scroll through the list until you locate it. For example, look for the “Solution offered” category. Under Conversation, click the Solution offered filter and select the negative scoring option.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_create_filter.png)
7. Click **Apply filter**.
8. (Optional) Add additional filter conditions to display only the conversations you want to review. For example, set "Review status" to "not reviewed" and "Churn risk" to "detected."

   Note: Only conversations that match all the conditions you set will display as a result of your filter.

   For each filter type, use the dropdown menus and checkboxes to set the filter criteria, then click **Apply Filter**. You can see how many conversations were found after applying each filter next to **Conversations found** in the bottom left corner of the dialog box.
9. Click **Create filter**.

   **Tip:** Click **Turn into assignment** instead of **Create filter** to [create a new assignment](https://support.zendesk.com/hc/en-us/articles/7043747327770). The assignment is automatically added to your Tasks list.

   Your new “Incorrect solution” filter is added to the **Filters** section displaying all conversations created in the last 30 days that have not yet been reviewed, where a negative score was assigned in the [Solution offered category](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories__solution), and where the [Churn risk spotlight](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc__churn_risk) insight was detected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_filter_example.png)
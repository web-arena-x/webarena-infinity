# Exporting a view of tickets to a CSV file

Source: https://support.zendesk.com/hc/en-us/articles/5521220496154-Exporting-a-view-of-tickets-to-a-CSV-file

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Export your ticket views to a CSV file to keep track of customer inquiries and related details. You can export once every 10 minutes, and you'll receive an email with the download link. If the export option isn't visible, ensure no filters are applied or check your role permissions. For larger views, consider modifying the view or using the Views API.

Location: 
Admin Center > Workspaces > Agent tools > Views

You can export a view to a comma-separated values (CSV) file. The CSV file will contain an entry for each ticket and all its associated ticket information from the view. Each ticket's requested date is displayed in your account's [time zone](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_dil_hnc_xe).

Because of the processing required to generate a CSV file, you can export a view only once every 10 minutes. You will receive an error message if there is less than 10 minutes between requests.

Tip: Check out this [suggestion for exporting views](https://support.zendesk.com/hc/en-us/community/posts/4968023028250) in our Community from Serge.

**To export a view to a CSV file**

1. In In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.
2. Click on the name of the view in the left sidebar to open it.
3. Depending on the view, click **Export CSV** in the upper right, or click **Actions** > **Export as CSV**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/view-actions-export.png)

   If you don't see the export option:
   - Check whether any filters are applied, and clear them. Views must be unfiltered to export them.
   - On Enterprise plans, the ability to export views to a CSV file is controlled by a custom role permission. If your role doesn't have permission, you won't see this option.
4. Check your email. You’ll receive an email with a download link to your CSV file. The email is sent to your primary email account in your user profile.

Larger views might fail to export, even though they display correctly in the Support console. If you don't receive an email with the download link, consider [modifying the view](https://support.zendesk.com/hc/en-us/articles/4408832792986#topic_fzx_qyj_5b) to return less information or using the [Views API](https://developer.zendesk.com/api-reference/ticketing/business-rules/views/) to retrieve the information you need.
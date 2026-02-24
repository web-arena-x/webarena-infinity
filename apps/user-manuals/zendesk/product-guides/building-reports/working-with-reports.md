# Working with reports

Source: https://support.zendesk.com/hc/en-us/articles/4408829048602-Working-with-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you'll learn how to perform various operations with existing Explore reports like saving, exporting, and cloning. If you are looking for information about how to create reports, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-queries). The operations you can perform on reports can be accessed from two places: the Reports library and the report itself.

This article contains the following topics:

- [Working with reports in the Reports library](#topic_kfn_gbv_klb)
- [Working with reports from within a report](#topic_s3r_hbv_klb)
- [Organizing your reports with tags](#topic_i1m_52h_r4b)

## Working with reports in the Reports library

The Reports library contains tools to help you manage and sort your reports. You open the Reports library by clicking the (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon on the left sidebar. The Reports library navigation bar shows the following options.

- **All reports:** Displays all reports in your Explore instance.
- **Favorites:** Displays the reports you've marked as a favorite. To mark a report as a favorite, click the star icon next to a report name. Clear the star if you don't want the report to be a favorite any more.

 ![Explore report favorites](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_new_queries_1.png)
- **My reports:** Displays only the reports that you created.
- **Recently updated:** Displays only the most recently created reports.

From the Reports library, you can click the pull-down list next to any report to display the following options:

![Explore report library options](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_working_with_queries_1.png)

- **Edit:** Opens the selected report in the report builder.
- **Clone:** Creates an editable copy of the report. You can choose the dataset to which the report will be copied and give the copy a new name. Bear in mind that if the dataset you copy to doesn't support the metrics and attributes in your report, it won't work.
- **Rename:** Enables you to enter a new name for the report in the **Name** column of report builder. Alternatively, while you are in a report, you can give it a new name in the **Report name** text box above the **Filters** panel and then click **Save**.
- **Delete:** Deletes the report from the Reports library. This option will not be selectable if you don't have permissions to access the report. For more details about permissions, see [Setting editor and admin permissions](https://support.zendesk.com/hc/en-us/articles/4408831563802-Setting-editor-and-admin-permissions). If you want to delete multiple reports, see [Deleting multiple reports](#topic_rxj_ygv_klb)
 below.

### Deleting multiple reports

In addition to deleting single reports, you can also delete multiple reports by using the procedure below.

Note: Deleted reports cannot be recovered.

**To delete multiple reports**

1. In the report builder, enable the checkbox next to each report you want to delete.
2. Below the list of reports, click **Delete**.

   ![Bulk delete reports example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_new_queries_2.png)
3. In the **Delete report** warning, click **Yes, delete** or **No, cancel**.

The selected reports are deleted.

## Working with reports from within a report

In the report builder, with a report open, click **Save**. From here, you can save, add the report to a new or existing dashboard, clone it, or export it.

![Report saving options.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_save_query.png)

- **Save:** Saves the current report. When you create or edit a report in Explore, the changes you make do *not* automatically save. You must save the report yourself.

 Note: By default, your report will be named **New report**. Before you save it, you'll need to give it a new name in the **Report name** text box above the **Filters** panel.
- **Add to dashboard:** Adds your report to a new or existing dashboard. Your report will also be saved to the Reports library. For more help, see [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418-Creating-dashboards) and [Adding reports to dashboards](https://support.zendesk.com/hc/en-us/articles/4408827904794-Adding-queries-to-dashboards).
- **Save as new:** Creates an editable copy of the report. You can choose the dataset to which the report will be copied and give the copy a new name. Bear in mind that if the dataset you copy to doesn't support the metrics and attributes in your report, it won't work.
- **Export:** Creates a CSV, image, PDF, or Excel file of your report. Exporting your report will not save it to the Reports library. When you export a report as CSV, only the data from the report is exported. Any formatting you've applied to the report is not exported. When you export a report in Excel format, the report formatting is maintained.

You can also reload the report by clicking the **Reload report** button.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Explore_reload_query.png)

Reloading the report resubmits all of the report's calculations behind the scenes, which can be useful when you’re manipulating especially complex or custom metrics. Additionally, reloading the report this way is faster than reloading the entire webpage and prevents you from losing any work that you haven’t yet saved.

## Organizing your reports with tags

When your organization has used Explore for a while, it's likely you'll accumulate a lot of reports. While you can mark your favorite reports, and see your own or recently updated reports, Explore also enables you to *tag* reports to make them easier to find in the Reports library. For example, you could create tags like:

- *Tickets*: For any reports relating to tickets
- *Articles*: For any reports relating to article views
- *Managers*: For any reports created by the management team

This section contains the following topics:

- [Creating report tags](#topic_fpf_pfh_r4b)
- [Adding tags to your reports](#topic_vg2_mfh_r4b)
- [Pinning report tags](#topic_wz3_hmy_nxb)
- [Viewing reports by tag](#topic_wfg_pfh_r4b)

### Creating report tags

You must be an Explore admin to create tags.

**To create tags**

1. In the **Tags** section of the Report library, click **Manage**.
2. In the **Manage tags** panel, click **New tag**.
3. Type a name for the tag and click **Save**.
4. Repeat steps 2 and 3 to continue entering as many tag names as you want.
5. When you're finished, click **Done**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_add_query_tag_updated.png)

To delete or rename any of your report tags, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) next to the report tag you want to change.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_manage_query_tag_1.png)

Important: If you rename or delete a tag, the action applies to all Explore users, not just you.

### Adding tags to your reports

Any Explore user with the Editor or Admin role can add tags to reports in the report builder. If you change your mind, you can always go back and edit them later.

**To add tags to a report**

1. While editing a report, click the tags icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_manage_query_tag_2.png)
2. In the **Manage tags** panel, select any tags you want to apply to the report.
3. When you're finished, click **Done**.

### Pinning report tags

You can control which tags appear in the Reports library by pinning the ones you want.

**To pin tags**

1. In the **Manage tags** panel, click the pin icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_manage_query_tag_pin.png)) next to any report tag you want to pin.
2. When you're finished, click **Done**.

The tags you pinned will now always be visible in the Reports library.

Note: Your pinned tags are visible only to you. Each Explore user can create their own pinned tags to suit their requirements.

### Viewing reports by tag

You can filter your list of reports in the library to show only the ones you want.

**To filter your reports by tag**

- In the **Tags** section of the Reports library, click any tag.

Explore displays only the reports that contain the tag you chose.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_manage_query_tag_9.png)
# Working with datasets

Source: https://support.zendesk.com/hc/en-us/articles/4408846513050-Working-with-datasets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In Explore, datasets give you access to your Zendesk product data. Each dataset contains
metrics and attributes that you use to create reports.

Typically, you'll select one of the default datasets that contains data for the product you
want to report on. However, you can also create copies of these datasets for testing (for
example, if you want to test custom metrics or apply specific security permissions).

This article contains the following sections:

- [Choosing a dataset](#topic_ig1_whf_5y)
- [Creating a copy of a dataset](#topic_hdd_2bc_v2b)
- [Managing datasets](#topic_rqh_p4h_3jb)

Related articles:

- [Understanding datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842)
- [Setting dataset permissions](https://support.zendesk.com/hc/en-us/articles/4408831563802)

## Choosing a dataset

You can choose the dataset you want to use before you create reports, or while you create a
report.

Tip: For an overview of all default datasets, see [Understanding the available default
datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842#topic_hr1_tfk_jkb).

### Choosing a dataset before you create a report

To get a jump start on creating reports, you can decide which dataset to use before
creating a report by going to the Datasets library.

**To choose a dataset from the Datasets library**

1. In Explore, click the **Datasets** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dataset_icon.png)).
2. On the **Datasets** library page, select the product dataset you want to use. The
   prebuilt, original dataset names display the status **Default**, and should be used
   whenever possible.

   If a dataset displays the status **Out of date**, it's a legacy
   dataset that is no longer being updated by Zendesk. Some of the metrics and attributes
   in that dataset might not function correctly. Unless you are maintaining reports that
   use this dataset, you should delete it.

   ![Explore dataset selection layout](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dataset_new_1.png)

The page for the dataset you chose opens. From here, you can select an existing report or
create a new report.

### Choosing a dataset when you create a report

When creating a report, the first step is always selecting a dataset.

**To choose a dataset while you create a report**

1. In Explore, click the **Reports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)).
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, select the Zendesk product you want to create
   reports for.

   ![Explore new dataset layout](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_select_a_dataset.png)
4. Select a specific dataset within that Zendesk product. For example, Zendesk Support
   contains different datasets for tickets, updates, SLAs, and backlog history.

   When you
   select a dataset, the **Dataset** panel appears on the right. This panel allows you
   to select the **Dataset version**: either the default version of the dataset (most
   common) or a custom version. You can also see which metrics the dataset includes,
   which helps you determine that you're selecting the right dataset before you start
   creating your report.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_select_a_dataset_panel.png)
5. Click **Start report**.

The report builder opens using the dataset you chose. You can now begin to [create your report](https://support.zendesk.com/hc/en-us/articles/4408821589530).

## Creating a copy of a dataset

In some circumstances, you might want to create your own copy of one of the default
datasets. For example, you might want to experiment with the data structure, or practice
working with custom metrics and attributes without worrying about cluttering a shared
default dataset.

Note: Remember, if you create your own dataset, formulas and reports
from the original dataset will not be available. For most purposes, use one of the default
datasets instead.

**To create a copy of a default dataset**

1. In Explore, click the **Datasets** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dataset_icon.png)).
2. In the **Datasets** library, click **New dataset**.
3. On the **Select a source** page, choose the product you want to create reports
   for.
4. In the **Display name** field, enter a name for your new dataset.
5. Under **Select a dataset**, select the default dataset that you want to make a copy
   of.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_creating_a_new_dataset.png)
6. Click **Done**.

The report builder opens using the dataset you just created. You can now begin to [create your report](https://support.zendesk.com/hc/en-us/articles/4408821589530).

## Managing datasets

Explore offers further options for managing your datasets. The available options depend on
the level of permission you have to the dataset. For example, you can't delete
or edit
the default datasets.

**To access the dataset operations**

1. In Explore, click the **Datasets** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dataset_icon.png)).
2. In the **Datasets** library, hover the mouse over the dataset you want to manage and
   click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)).

   ![Dataset options menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dataset_new_3.png)
3. From the options menu, select one of the following:
   - **New report from this**: Opens a new report using the selected dataset.
   - **Edit**: Opens the dataset configuration page, where you can change the name of
     the dataset and review the product it uses.
   - **Rename**: Allows you to change the name of the dataset.
   - **Clone**: Creates a copy of the selected dataset.
   - **Delete**: Deletes the selected dataset.
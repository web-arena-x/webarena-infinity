# Generating sandbox creation reports

Source: https://support.zendesk.com/hc/en-us/articles/7502268225690-Generating-sandbox-creation-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Account > Sandbox > Sandboxes

When you create a sandbox, a lot of your production data is replicated in the sandbox.
However, sometimes problems arise and the sandbox might not contain all of the elements
you expected to be replicated. This can happen for a variety of reasons. Admins can
download a sandbox creation report to help them understand what was replicated and
understand why some elements might be missing.

This article contains the following sections:

- [About the sandbox creation report](#topic_hg1_yx2_wbc)
- [Downloading a creation report](#topic_epz_yx2_wbc)

Related articles:

- [About Zendesk sandbox
  environments](https://support.zendesk.com/hc/en-us/articles/6150628316058)
- [Creating a sandbox environment to test
  changes](https://support.zendesk.com/hc/en-us/articles/4408822049818)

## About the sandbox creation report

The sandbox creation report contains information about most elements of the
production instance that Zendesk attempted to replicate in the sandbox and indicates
whether that replication was successful. If a sandbox element wasn't successfully
recplicated, the report includes an explanation of why that occurred.

The report is downloaded as a comma-seperated values (CSV) file and contains the
following headings:

- **Name**: The name of the sandbox element.
- **Source\_config\_id**: The element's ID in production.
- **Target\_config\_id**: The element's ID in the sandbox.
- **Config\_type**: The configuration type. This matches the API names
  for configuration types. For example, "custom status."
- **Timestamp**: The timestamp of the element's
  creation.
- **Copied**: Indicates whether the element was successfully
  replicated during the sandbox creation. Valid values: Yes, No
- **Message**: An explanation of why an element wasn't replicated.
  Empty for elements that were replicated.

### Requirements and limitations

Consider the following requirements and limitations before generating a sandbox
creation report:

- You must be an admin to create sandboxes and download sandbox creation
  reports.
- A sandbox creation report can be downloaded for up to 30 days after the
  sandbox is created. After 30 days, the report is deleted and can't be
  accessed again.
- When a sandbox is deleted, its associated creation report is also
  deleted.
- Users, organizations, and ticket creation events aren't
  included in the report because of the high number of records for each of
  those objects. Other objects, configurations, and events [that can be replicated](https://support.zendesk.com/hc/en-us/articles/7137127340442#topic_eyb_2pd_5yb) are
  captured in the report.

## Downloading a creation report

Creation reports are downloaded from the Sandboxes page in Admin Center.

**To download a sandbox creation report**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Sandboxes**.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to one of your sandboxes, then select
   **Download creation report (.csv)**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sandbox-download-report.png)

   You'll find the report in the
   Downloads directory on your computer.
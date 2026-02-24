# Viewing your import history

Source: https://support.zendesk.com/hc/en-us/articles/5789034291738-Viewing-your-import-history

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Tools > Data importer

Import history is logged for data importer events only. The data
importer is currently in an open beta.

Rather than adding users, organizations, and custom object records one at a time, admins
can add them in bulk by importing a comma-separated values (CSV) file. The import
history shows logs of all attempted imports through the Data importer.

This article contains the following topics:

- [Monitoring active imports](#topic_dpb_bln_sxb)
- [Viewing the import history](#topic_dxm_1km_sxb)

## Monitoring active imports

Imports take time. While data is being imported, an Import in progress section is
displayed at the top of the Data importer page. In this section, you can see the
file name, target destination (the object for which you're uploading data), number
of records, errors, and information about how the import is progressing. Admins
receive email notifications when an import is complete.

When there are no imports in progress, this section isn't displayed.

**To monitor the import in progress**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tools > Data importer**.
2. View details about the import's progress under **Import in
   progress**.
3. (Optional) Click the refresh icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/import_progress_reload_icon.png)) to refresh the progress information
   for the import.

## Viewing the import history

The import history provides a record of every attempted import via the data importer.
Each log entry captures the import date and time, the CSV file name, the status of
the import, the target destination (the object for which you're uploading data), the
number of errors, and the name of the person who performed the import.

**To view your import history**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tools > Data importer**.
2. View details about past imports under **Import history**.
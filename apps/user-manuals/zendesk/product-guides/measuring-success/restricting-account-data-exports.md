# Restricting account data exports

Source: https://support.zendesk.com/hc/en-us/articles/5388932900250-Restricting-account-data-exports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Account > Tools > Reports

If the ability to export account data has been enabled in your account by Zendesk, you can [export ticket, user, or organization data from your account](https://support.zendesk.com/hc/en-us/articles/4408886165402) from Admin Center.

To protect your account data, you can restrict who can export the data based on their email domain. You can also contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to deactivate the ability to export account data.

This article contains the following sections:

- [Restricting data exports to certain admins](#topic_bkl_nkw_jwb)

This article doesn' apply to API data exports.

## Restricting data exports to certain admins

When Zendesk enables data exports in your account, only administrators with email addresses that have a specific allow-listed email domain can export data from your account. The account owner's email domain is the approved email domain by default but the account owner can change it if necessary.

Note: Admins with secondary email addresses with an email domain that isn't on the allowlist can't access the Reports page in Admin Center.

**To change the approved email domain for exporting data**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Tools > Reports**.

   If necessary, click the **Export** tab to display data export options. Some legacy versions of Zendesk show the export options on a separate tab.

   You won't see the export option unless you contacted Zendesk Customer Support to enable data exports. See [Exporting ticket, user, or organization data from your account](https://support.zendesk.com/hc/en-us/articles/4408886165402).
2. Replace the domain in **Approved email domain**

   For example, *mycompany.com*.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/data_export_email_domain.png)

   If you leave the field blank, the ability to export data won't be limited to admins in a specific domain. In that case, any admin will be able to export data, regardless of their email domain. If you enter a value, admins must sign in using the approved email domain to use the data export option.
3. Click **Save**.
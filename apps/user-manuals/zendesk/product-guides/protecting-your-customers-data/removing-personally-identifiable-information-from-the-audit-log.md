# Removing personally identifiable information from the audit log

Source: https://support.zendesk.com/hc/en-us/articles/4418433154074-Removing-personally-identifiable-information-from-the-audit-log

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Account > Audit log > Audit log

Admins have the ability to permanently delete users, which removes the user from the system. This might be necessary because of General Data Protection Regulation (GDPR) or similar regulations, which grant individuals from certain regions the *right to erasure* or the right to be [forgotten or deleted](https://support.zendesk.com/hc/en-us/articles/4408845703194). When permanently deleting users and removing personally identifiable information (PII) from Zendesk products, you must consider whether the data captured in the audit log contains personal information that also needs to be removed.

This may be necessary, but it is important to understand that altering the audit log in this way can make it harder to accurately track your history.

**To delete PII from the audit log**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Audit log > Audit log**.
2. Click **Manage settings**.
3. Select **Automatically delete PII** and click **Save**.

   When this setting is enabled, personal information in the actor, IP address, and item columns of the audit log is deleted automatically when a user is permanently deleted. Names are replaced with user IDs.
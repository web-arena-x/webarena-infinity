# Comparing snapshots of environment configurations

Source: https://support.zendesk.com/hc/en-us/articles/8913001178778-Comparing-snapshots-of-environment-configurations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

As an admin, you can compare snapshots of environment configurations to identify changes. This feature lets you view what was added, modified, or deleted between two snapshots. Changes are highlighted, with old configurations in red and new ones in green. Ensure you're an admin in both environments and match the locale settings for accurate comparisons.

Location:  Admin Center > Account > Sandbox > Compare
snapshots

A [snapshot](https://support.zendesk.com/hc/en-us/articles/8915863870362) is a read-only version of an environment's
configurations at a given time. When necessary, admins can compare two snapshots of the
same environment or snapshots of two different environments.

Note:

- You must be an admin in both environments you're comparing.
- Comparisons are language sensitive. For best results, the user's locale
  should match the environments' locale. Otherwise, configurations may appear
  as new or deleted because the configuration's name differs between
  locales.

**To compare saved snapshots of an environment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Compare snapshots**.
2. Under **Compare**, select the first saved snapshot you want to compare.
3. Under **To**, select the second saved snapshot you want to compare.

   As soon
   as values are selected in both fields, the read-only comparison is
   generated.
4. View the comparison and drill down into each configuration, as needed, to see
   what was added, modified, or deleted.

   Within the comparison, old versions of a
   configuration are highlighted in red and new versions of a configuration are
   highlighted in green. Additionally, each change item is labeled as:

   - **Modified**: The configuration item exists in both snapshots, but
     has some differences.
   - **New**: The configuration item exists only in the *To*
     snapshot.
   - **Deleted**: The configuration item exists only in the *Compare*
     snapshot.
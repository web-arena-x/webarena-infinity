# Syncing products and add-ons to sandboxes

Source: https://support.zendesk.com/hc/en-us/articles/7414296161818-Syncing-products-and-add-ons-to-sandboxes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Premium Sandbox add-on |

Location:  Admin Center > Account > Sandbox > Environments

For sandboxes to serve their purpose, it's important that they provide a good likeness of
the production environment. To that end, all sandboxes provide some level of data
replication during the sandbox creation process. However, that's an accurate snapshot of
your production environment only at that moment in time. You can use the sandbox
synchronization feature to update existing sandboxes to reflect subscription-level
changes to your account, including purchased products, agent seats, add-ons, and
cancelations.

This article contains the following topics:

- [About updating product and add-ons in your sandbox](#topic_uwz_4zh_hcc)
- [Syncing products and add-ons to your sandbox](#topic_gq5_pzh_hcc)

## About updating product and add-ons in your sandbox

Syncing your product, add-ons, and cancelations to your sandbox account is a powerful
way to ensure your sandbox accurately reflects your production account.

The following data is updated when you sync a sandbox:

- Newly purchased add-ons and products are added to the sandbox.
- Canceled add-ons and products are removed from the sandbox.
- Agent seats in the sandbox will be updated to reflect the number of seats in
  the production account.

  Note: If you've reduced the number of agent seats in
  your production environment, synching your products and add ons can
  result in changes to the roles of agents in your sandbox.

The following data isn't updated when a sandbox syncs:

- No [replicated data](https://support.zendesk.com/hc/en-us/articles/6150628316058) other than
  add-ons, products, and agent seat counts are updated. If you want to update
  other data, you must [replace your sandbox](https://support.zendesk.com/hc/en-us/articles/4408824434586#topic_omh_zl1_57).
- Even if the number of agent seats is increased in your sandbox account, the
  user data associated with agents in those seats isn't updated during a
  sync.
- The [High Volume API add-on](https://support.zendesk.com/hc/en-us/articles/4408836402074#topic_vwh_wz4_jyb) isn't
  copied to sandboxes.

## Syncing products and add-ons to your sandbox

Syncing your production subscription data to a sandbox is done from the production
account.

**To sync your product and add-on data with a sandbox**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Environments**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the sandbox you want to update and
   select **Sync products and add-ons**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/sandbox_sync_subscription_data.png)
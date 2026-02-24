# Using and managing sandboxes

Source: https://support.zendesk.com/hc/en-us/articles/4408824434586-Using-and-managing-sandboxes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Account > Sandbox > Sandboxes

This article describes how to use, maintain, and manage [sandboxes](https://support.zendesk.com/hc/en-us/articles/6150628316058).

This article contains the following topics:

- [Accessing a sandbox](#topic_o4y_cs1_53)
- [Updating a sandbox](#topic_ryx_hgj_tgc)
- [Deleting a sandbox](#topic_omh_zl1_57)

## Accessing a sandbox

After you [create](https://support.zendesk.com/hc/en-us/articles/4408822049818) a sandbox and it's active, you can start working in it.

**To switch to a sandbox from the production instance of Zendesk Support**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Sandboxes**.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to one of your sandboxes, then select **Open Sandbox** to launch the sandbox instance in a new browser tab.

   You can also bookmark the sandbox URL and access it directly.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_sandbox_open.png)
3. Log in to the sandbox with your normal administrator credentials.

Make changes, test, and fine tune as needed. Sandbox changes are not copied to the production instance. You can manually recreate changes to your sandbox environment in your production instance.

## Updating a sandbox

After a sandbox is created, you can update some details, such as [account changes](#topic_bnt_2jl_tgc) and [configurations](#topic_d4d_gjl_tgc).

However, the only way to update other data, such as tickets and user information, is to re-create it manually. When this is required, it is often best to [delete](#topic_omh_zl1_57) the sandbox and [create](https://support.zendesk.com/hc/en-us/articles/4408822049818) a new one based on the current settings and data in your production instance of Zendesk Support.

### Managing sandboxes through account changes

When you change your production account's subscription, including plans, seats, and add-ons, your sandbox environment remains unchanged until you sync the sandbox. After syncing a sandbox, the sandbox environment reflects the account changes.

For example, if downgrading from a Zendesk Suite plan to a lower Suite plan or standalone Support plan without access to sandboxes, after you delete any existing sandboxes you have, you won't be able to create a new one.

See [Syncing product and add-on data to sandboxes](https://support.zendesk.com/hc/en-us/articles/7414296161818).

### Deploying production configuration updates to sandboxes

You can use the [Configuration Management EAP](https://support.zendesk.com/hc/en-us/articles/8712690572442) to reflect configuration changes to your production account in a sandbox environment.

## Deleting a sandbox

After you're done with a round of testing and updates, it's a good idea to delete the existing sandbox.

When you're ready to start testing something new, you can then create a new sandbox based on the current settings and data in your production instance of Zendesk Support. Creating a new sandbox is also useful if you mess up and want to start from scratch. However, when you replace a sandbox, coordinate with your internal development teams and consider the following effects of creating a new sandbox:

- The sandbox URL changes
- All object IDs in the sandbox change, for example, ticket field IDs will be different
- Any custom help center themes are lost, but they can be [exported](https://support.zendesk.com/hc/en-us/articles/4408828976538) before you delete the old sandbox
- All apps are removed
- Any sharing agreements are removed

**To delete your sandbox**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Sandboxes**.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then select **Delete Sandbox**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_sandbox_work_1.png)
3. When you're ready to replace the deleted sandbox, [create a new sandbox](https://support.zendesk.com/hc/en-us/articles/4408822049818).
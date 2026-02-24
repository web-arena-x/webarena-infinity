# Managing configuration deployments between Zendesk environments

Source: https://support.zendesk.com/hc/en-us/articles/9805528582298-Managing-configuration-deployments-between-Zendesk-environments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Account > Configuration management > Deployments

Deploying your account configurations is currently part of an early
access program (EAP). You can sign up for the [Configuration Management EAP here](https://support.zendesk.com/hc/en-us/community/topics/8521230663578).

After you [deploy configurations](https://support.zendesk.com/hc/en-us/articles/9474556880922) from one Zendesk
environment to another in your account, you might need to revert, rename, or otherwise
manage the deployment.

This article contains the following topics:

- [Viewing a deployment's details, source, or destination](#topic_yr1_tg3_xgc)
- [Reverting a deployment](#topic_wp2_jw5_wgc)
- [Renaming a deployment](#topic_cjj_ty5_wgc)
- [Redeploying a reverted deployment](#topic_bvy_jw5_wgc)
- [Deleting a deployment](#topic_dyz_sy5_wgc)

## Viewing a deployment's details, source, or destination

After you create a deployment, you can view it's details, the source snapshot, and
the destination environment.

**To view a deployment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Configuration
   management > Deployments**.
2. Find the deployment you want more information about, click the options menu
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select one of the following:
   - **View**
   - **View source**
   - **View destination**

## Reverting a deployment

If you need to roll back changes you deployed, you can revert the deployment.

**To revert a deployment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Configuration
   management > Deployments**.
2. Find the deployment you want to revert, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select **Revert**.

   This creates a
   new deployment with the source and destination environments
   pre-selected. It's also automatically named *Revert: [deployment
   name]*, where *[deployment name]* is replaced with the name
   of the deployment you're reverting.
3. Review the changes that would be made to the production environment.
4. (Optional) Click **Refresh** under the *Destination* to ensure the
   latest updates in the destination environment are reflected in the
   comparison.
5. Click **Test deploy**.

   This can take up to several minutes. When the
   test is complete, you will either see that it passed or be notified of
   missing dependencies.

   - If the test fails with missing dependencies, click **Auto-select
     dependencies**.
   - Alternatively, you can click **Cancel** to manually resolve the
     dependency issue or click **Ignore** to proceed without resolving
     the missing dependency.

   Note: After the test passes, no changes can be made to the
   configurations selected in the deployment.
6. Click **Deploy**.

   When a deployment begins, Zendesk saves a version of
   the destination environment before making any changes. This ensures you
   can revert a deploy if necessary.

## Renaming a deployment

Sometimes it's necessary to rename a deployment.

**To rename a deployment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Configuration
   management > Deployments**.
2. Find the deployment you want to rename, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select **Rename**.
3. In the Rename deployment dialog, enter a new **Name**.
4. Click **Rename**.

## Redeploying a reverted deployment

There are times when you need to revert and then redeploy a deployment.

**To redeploy a deployment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Configuration
   management > Deployments**.
2. Find the deployment you want to redeploy, click the options menu icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select **Redeploy**.

   This creates a
   new deployment with the source and destination environments
   pre-selected. It's also automatically named *Redeploy: [deployment
   name]*, where *[deployment name]* is replaced with the name
   of the deployment you're redeploying.
3. Review the changes that would be made to the production environment.
4. (Optional) Click **Refresh** under the *Destination* to ensure the
   latest updates in the destination environment are reflected in the
   comparison.
5. Click **Test deploy**.

   This can take up to several minutes. When the
   test is complete, you will either see that it passed or be notified of
   missing dependencies.

   - If the test fails with missing dependencies, click **Auto-select
     dependencies**.
   - Alternatively, you can click **Cancel** to manually resolve the
     dependency issue or click **Ignore** to proceed without resolving
     the missing dependency.

   Note: After the test passes, no changes can be made to the
   configurations selected in the deployment.
6. Click **Deploy**.

   When a deployment begins, Zendesk saves a version of
   the destination environment before making any changes. This ensures you
   can revert a deploy if necessary.

## Deleting a deployment

Deleting a deployment is permanent and affects only the record of the deployment. The
changes that were deployed are unaffected. For Enterprise plans and above,
deployment events are also recorded in the audit log and will be preserved even if a
deployment is deleted from the Deployments page.

**To delete a deployment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Configuration
   management > Deployments**.
2. Find the deployment you want to delete, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select **Delete**.
3. In the confirmation dialog, click **Delete deployment**.
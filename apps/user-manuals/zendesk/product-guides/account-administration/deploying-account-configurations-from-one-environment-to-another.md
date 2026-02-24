# Deploying account configurations from one environment to another

Source: https://support.zendesk.com/hc/en-us/articles/9474556880922-Deploying-account-configurations-from-one-environment-to-another

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

Deploy account configurations from one environment to another to reduce risks of manual recreation. Use snapshots to save, create, and deploy configurations, ensuring consistency across environments. Monitor deployment status and manage deployments directly from your account. Note that private apps require separate installation in each environment, and you need at least one sandbox in addition to your production environment.

Location:  Admin Center > Account > Sandbox > Deployments

Admins can create, update, and test account configurations in one environment and then
implement them identically in another environment without the inherent risks of manually
recreating them. It also provides a way to update sandbox environments to reflect
changes to your production environment rather than having to delete the sandbox and
recreate it.

Private apps can't be deployed from one environment to another. Instead, they must be
installed and configured in each environment separately.

Note: Deployments occur between
environments in your account. Therefore, to use this functionality, you must have at
least one sandbox in addition to your production environment.

This article contains the following topics:

- [Deploying configurations from a snapshot](#topic_dtn_np2_yfc)
- [Monitoring the status of deployments](#topic_rbj_4p2_yfc)
- [Managing deployments](#topic_efv_djl_yfc)

## Deploying configurations from a snapshot

Deployments are based on [snapshots](https://support.zendesk.com/hc/en-us/articles/8915863870362), which you can think of as read-only versions
of an environment's configurations at a given time. When you deploy configurations,
you select the snapshot you want to deploy, which of the configurations from that
snapshot to deploy, and the target environment it will be deployed to.

Deploying configurations consists of three primary steps:

1. [Save a snapshot](https://support.zendesk.com/hc/en-us/articles/8915863870362) of the environment
   with the configuration you want to deploy.
2. Create the deployment.
3. Select the configuration items and deploy them.

Note: To deploy configurations, you must be an admin in both
environments.

### Creating a deployment

After you save a snapshot of the environment with the configuration you want to
deploy, you must create the deployment itself. This defines the environment and
snapshot you'll be deploying a configuration items from and the destination
environment you're deploying the configurations to. This preliminary information
allows for the comparisons necessary to identify and resolve any dependencies or
conflicts between the snapshot and destination prior to deploying the
configuration items.

**To create a deployment**

1. In your production account, open [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Deployment**.
2. Click **Create deployment**.
3. In the Create new deployment dialog, do the following:
   - **Name**: Enter a unique name for the deployment.
   - **Source**: Select the [saved snapshot](https://support.zendesk.com/hc/en-us/articles/8915863870362) of the
     configurations you want to deploy.
   - **Destination**: Select the environment to which you want to
     deploy the configuration.
4. Click **Create**.

### Deploying a configuration

After the deployment is created, you must specify which configuration items you
want to deploy. Zendesk automatically compares the selected configuration to the
destination, including any dependencies or conflicts that must be resolved prior
to performing the deploy.

Note: Deploying a renaming of a ticket, user, or
organization custom field results in the deletion of the original custom
field and data associated with it and creation of a new custom field with
the updated name.

**To deploy a configuration**

1. In your production account, open [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Deployment**.
2. Click the name of the deployment.
3. In the **Source** column of the page, select at least one
   **Configuration** you want to deploy along with any dependencies
   it has that also need to be deployed with it.
4. Review the changes that would be made to the production environment.
   Optionally, you can click **Refresh** under the *Destination* to
   ensure the latest updates in the destination environment are reflected
   in the comparison.
5. (Optional) Click **Save**.

   This saves the selected configurations
   and dependencies, but still allows you to make changes to the
   deployment.
6. Click **Test deploy**.

   This can take up to several minutes. When
   the test is complete, you will either see that it passed or be
   notified of missing dependencies or conflicts. If missing
   dependencies are found, click **Cancel** to select the dependency
   and resolve them or click **Ignore** to proceed without resolving
   the missing dependency.

   Note:
   - After the test passes, no changes can be made to the
     configurations selected in the deployment.
   - If the user's locale differs from the locale of the
     snapshot's environment or the destination environment,
     configuration names may differ and cause them to appear
     erroneously as new or deleted.
7. Click **Deploy**.

   When a deploy begins, Zendesk saves a snapshot of
   the destination environment before making any changes. This ensures
   you can revert a deploy if necessary.

## Monitoring the status of deployments

From the Deployments page, you can view your deployment history. The list includes
each deployment, along with its source, destination, status, and last updated
date.

**To monitor the status of deployments**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Sandbox >
   Deployments**.
2. View the status beside the deployment you want to monitor.

   The following
   statuses are possible:
   - **Draft**: The deployment has been created, but not deployed.
     This includes testing the deployment.
   - **Deploying**: The deployment has been initiated and is in
     progress.
   - **Deployed**: The deployment succeeded.
   - **Failed**: The deployment failed.

## Managing deployments

After you create a deployment, it's visible in the list on the Deployments page.

**To manage a deployment**

1. In your production account, open [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Deployment**.
2. Next to the deployment you want to manage, click the menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) and select one of the available options.

   The
   options available for each deployment depends on its status.
   - Deployments with a status of **Draft** have the options
     to:
     - View
     - Rename
     - View source
     - View destination
     - Delete
   - Deployments with a status of **Deploying** have the options
     to:
     - View
     - Rename
     - View source
     - View destination
   - Deployments that **Deployed** or **Failed** have the
     options to:
     - View
     - Rename
     - View source
     - View destination
     - Revert
     - Redeploy
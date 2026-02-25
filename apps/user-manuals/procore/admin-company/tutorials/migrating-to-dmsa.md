# Migrating Data Connection Apps to Use Developer Managed Service Accounts

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/migrating-to-dmsa

---

*All Traditional Service Accounts will sunset on March 18,* *2025.*

Traditional Service Accounts were deprecated on December 9, 2021. Beginning January 21, 2025, we will no longer allow the creation of new Traditional Service Accounts. Existing Traditional Service Accounts will continue to function until March 18, 2025.

In accordance with this timeline, developers of data connection applications that currently use Traditional Service Accounts are required to update their applications to use [Developer Managed Service Accounts](/faq-what-is-developer-managed-service-account), and customers will be required to install these updated applications before the sunset date. All data connection applications not migrated by the sunset date will cease to function. Any application listed on the Procore App Marketplace that is not using a supported method for accessing the Procore API will be removed by the sunset date. See for additional information.

## Background

With the deprecation of traditional service accounts and the release of [Developer Managed Service Accounts (DMSA)](/faq-what-is-developer-managed-service-account), customers currently using data connection applications that rely on traditional service accounts must plan to switch over to using applications that use DMSAs prior to the sunset date. Third-party developers and integrators will be updating their applications to use DMSAs and make new versions available to Procore customers over time. This tutorial provides some suggestions for preparing a migration plan and outlines the procedures for working through a migration.

### About the Procore Developer Portal

The [Procore Developer Portal](https://developers.procore.com/) is a comprehensive resource designed for developers to enhance their understanding and usage of Procore's APIs and other development tools. The portal provides in-depth documentation, guides, and resources to encourage developers to build applications that integrate with Procore's platform. It facilitates seamless interaction with Procore's construction management software, allowing developers to create customized solutions that extend Procore's functionalities.

### Signing Up, Registering, and Building an Application on the Portal

Procore customers interested in building their own applications that integrate with the Procore platform can follow these steps to begin their development journey:

- **Sign Up**: [Create an account](https://developers.procore.com/documentation/new-account) on the Procore Developer Portal.
- **Register**: Register and [create a new application](https://developers.procore.com/documentation/building-apps-create-new) within the portal.
- **Build**: Use Procore's APIs and [API documentation](https://developers.procore.com/reference/rest/v1/docs/rest-api-overview) to develop and integrate your application with Procore's platform.

See [Building Procore Data Connection Applications with DMSA](https://developers.procore.com/documentation/building-data-connection-apps) for more information.

## Things to Consider

- **Required User Permissions**:

 - Company Admin

## Migration Preparation

Understanding your existing traditional service accounts can help you plan effectively for a successful application migration. Before migrating to a DMSA application you will need to review the settings for each of your existing service accounts to verify the information is accurate, and to update any service accounts where the settings may be missing or incorrect.

Service accounts are categorized into two application types - `Marketplace` and `Custom`.

- **Marketplace** - for service accounts that are mapped to applications installed from or listed on the Procore App Marketplace. Applications are selectable from a dropdown list.
- **Custom** - for custom applications that were developed internally or by third-party integrators specifically for your company.

Note that some service accounts in your company may not have a defined application type. You will need to update these service accounts with the correct application type before migrating to DMSAs. It is also a good opportunity to review and verify the existing application type settings to ensure your service accounts are mapped properly.

### Step 1 - Set Application Type for Undefined Service Accounts

Use the following steps to update your existing service accounts where the application type is not defined.

1. Navigate to the company's **Admin** tool.
2. Under 'Company Settings', click **Service Accounts**. The Service Accounts page shows a list of the existing service accounts in your company.

   1. Upon examining your service accounts you may see one or more accounts with no value in the App Name column, as shown in the first account in the example above. This indicates that the application type for that service account is undefined. You will need to update those accounts before migrating to DMSA.
3. Locate a service account where the App Name column value is missing and click **Edit**.
4. For the App Type setting, choose one of the following options:

   1. **Marketplace** - choose this setting if the service account is mapped to an application on the Procore App Marketplace. Use the dropdown menu to select the application. Verify that the application you select matches the application you have in production.
   2. **Custom** - choose this setting if the service account is used by an application you have developed internally, or by an application built by a third-party integrator specifically for your company. Enter a description for the account as well as the developer name and email address.
5. Click **Update**.
6. Repeat Steps 3-5 above for all existing service accounts in your company where the App Name column value is missing.

### Step 2 - Review and Verify Existing Service Account Mappings

Now that you have set the application type for all your existing service accounts, take a few minutes to review each account and verify that the application type mapping is correct, and that all required fields and are filled in as needed.

**Review Custom Service Accounts**

- Be sure that all service accounts marked as `Custom` are actually used by custom integrations rather than by Marketplace applications. If you find a Custom service account that should be changed to a Marketplace account, update the App Type setting as described in the previous section.
- Verify that all Custom service accounts in your company are actively being used. Remove any inactive accounts.
- Verify that all Custom service accounts in your company have the **Description**, **Company/Developer Name** and **Company/Developer Email** fields filled in accurately. (see above)

**Review Marketplace Service Accounts**

- Be sure that all service accounts marked as âMarketplaceâ are actually used by applications from the Procore App Marketplace that you have currently running in production. If you find a âMarketplaceâ service account that should be changed to âCustomâ, update the App Type setting as described in the previous section.
- Verify that all Marketplace service accounts have the correct **Marketplace App** selected in the dropdown. (see above)

## Migrate Applications to DMSA

The steps for migrating an application from traditional service account to DMSA varies depending on the application type.

### Marketplace Applications

- Reach out to the developers of your existing service account based Marketplace applications to understand when they expect to have DMSA-enabled versions available for their customers. Locate the application listing on [marketplace.procore.com](https://marketplace.procore.com/) and use the developer email or support information to contact the developer.
- Formulate an internal communication plan based on the release dates provided by the developer, so that your end users are informed about any pending application migrations. Include timelines for moving all users onto new applications and for retiring the old versions.
- Once the DMSA-enabled version of the application is available, follow the steps outlined in [Install a Data Connection App from the Marketplace](/product-manuals/admin-company/tutorials/Install-data-connection-app). If you are unclear about how to install the new DMSA-enabled version of a particular application, contact the developer for additional information.
- After successfully installing the new Marketplace application, instruct your end users to begin using the new application instead of the older version.
- After all users have been successfully moved over to using the new application, you can remove the old service account as described in [Delete a Service Account](/product-manuals/admin-company/tutorials/delete-service-account) and [uninstall](/product-manuals/admin-company/tutorials/uninstall-app) the old version of the application.

### Custom Applications

- If a custom application was developed and maintained internally by your company, you will need to develop a new DMSA-enabled version of the application as described in the [Service Account Deprecation](https://developers.procore.com/documentation/service-account-deprecation) announcement. See [Developer Managed Service Accounts](https://developers.procore.com/documentation/developer-managed-service-accounts) for details. Reach out to [apisupport@procore.com](mailto:apisupport@procore.com) if you need additional guidance.
- If a custom application was built by a third-party developer specifically for your company, reach out to them to understand when a new DMSA-enabled version of the application will be available, and make sure they fill out the custom application information on the Service Account user interface.
- Once the DMSA-enabled version of the custom application is available, follow the steps outlined in [Install a Custom App](/product-manuals/admin-company/tutorials/install-a-custom-app). If you are unclear about how to install the new DMSA-enabled version of a particular application, contact the developer for additional information.
- After successfully installing the new custom application, instruct your end users to begin using the new application instead of the older version.
- After all users have been successfully moved over to using the new application, you can remove the old service account as described in [Delete a Service Account](/product-manuals/admin-company/tutorials/delete-service-account) and [uninstall](/product-manuals/admin-company/tutorials/uninstall-app) the old version of the application.
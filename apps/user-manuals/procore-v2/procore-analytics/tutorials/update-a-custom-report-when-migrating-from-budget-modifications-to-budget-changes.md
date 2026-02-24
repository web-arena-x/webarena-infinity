# Update a Custom Report When Migrating from Budget Modifications to Budget Changes

Source: https://v2.support.procore.com/product-manuals/procore-analytics/tutorials/update-a-custom-report-when-migrating-from-budget-modifications-to-budget-changes

---

##### Â Important

This tutorial is written for users who are familiar with updating custom reports in Microsoft's Power BI Desktop. For the most up-to-date-information available, visit [Microsoft's Power BI website](https://learn.microsoft.com/en-us/power-bi/).

## Background

In October 2022, Procore released a new Budget Changes feature that replaced the existing budget modifications feature in the Project level Budget Tool. See [Migrating to Budget Changes from Budget Modifications](/product-manuals/budget-project/tutorials/migrating-to-budget-changes-from-budget-modifications). The Budget tool only supports the new budget changes feature. However, the API endpoints for Procore's legacy budget modifications feature will continue to be available until October 2023.

- In Procore Analytics, your legacy budget modification dashboards are still visible. However, we've added new budget changes dashboards that include both budget changes data and historical budget modifications data. This update was released on October 27, 2022.
- For Procore Analytics users who have built custom reports using Data Extract/SQL endpoints budget modifications, please be aware of the following:

  - In October 2022, Procore announced that it expects to sunset the legacy endpoints in October 2023.
  - The legacy API endpoints have also been marked deprecated in the [Reference](https://developers.procore.com/reference/rest/v1/docs/rest-api-overview) documentation on [developers.procore.com](https://developers.procore.com/) .

##### Â Important

If you built any custom reports in Procore Analytics using the legacy budget modifications data, you must complete these steps in this order:

1. **Perform the Migration to Budget Changes**. To learn about the migration process for the Procore web application, see [Migrating to Budget Changes from Budget Modifications](/product-manuals/budget-project/tutorials/migrating-to-budget-changes-from-budget-modifications).
2. **Update Your Custom Reports in Procore Analytics**. To learn how to update your custom reports in Procore Analytics, see the [Steps](#steps) below.

If you have any questions about these changes, please send an email message to: [analyticssupport@procore.com](mailto:analyticssupport@procore.com)
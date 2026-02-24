# Migrating to Budget Changes from Budget Modifications

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/migrating-to-budget-changes-from-budget-modifications

---

##### Â Phased Release

The [new Budget Changes feature](/process-guides/about-budget-changes/) is designed to replace the existing budget modifications feature. Once you migrate to Budget Changes, you will no longer have access to the budget modifications feature. If you have any questions before your company starts the migration, contact your Procore point of contact. To learn more about the timeline for migration, see: [Common Questions](/process-guides/about-budget-changes/common-questions).

## Background

The new Budget Changes feature is replacing the existing budget modifications feature. Starting in October 2022, Procore will be working with Procore customers to migrate from budget modifications to the Budget Changes feature by a date that has yet to be determined. Once you migrate, you will no longer have access to the budget modifications feature. If you have any questions before your company starts the migration, contact your Procore point of contact.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information**:

 - The migration to the budget changes feature is permanent. Once completed, Procore cannot restore the budget modifications function.
 - All numbers in Procore will remain unchanged.
 - Once migration is complete, All labels and references to 'budget modifications' in Procore's user interface are updated to 'budget changes'.

##### Â Important

A new Budget tool configure setting is available after migrating your company to Budget Changes, 'Require net zero Budget Change Amounts'. When the setting is turned OFF, users can create Budget Changes that do not require adjustments to be balanced. When the setting is turned ON, adjustments are required to equal a net-zero total change. See [Configure Settings: Budget](/product-manuals/budget-project/tutorials/configure-settings-budget).

'Require net zero Budget Change Amounts' is turned OFF by default. However, the setting will be copied to new projects if a project template is used. See [What gets copied over to a new project when applying a project template?](/faq-what-gets-copied-over-to-a-new-project-when-applying-a-project-template)

When migrating from Budget Modifications to Budget Changes, Procore will turn the setting ON or OFF based on the following project settings:

1. If âAllow Budget Modifications Which Modify Grand Totalâ is turned OFF, âRequire net zero Budget Change Amountsâ will be turned ON.
2. If âAllow Budget Modifications Which Modify Grand Totalâ is turned ON, âRequire net zero Budget Change Amountsâ will be turned OFF.

For companies using the ERP Integrations tool: **Show/Hide**

- In order to send the budget change to the ERP Integrations tool to be accepted for export by an [accounting approver](/glossary-of-terms):
- Only âApprovedâ Budget Changes can be sent to an ERP integration.
- Budget Changes can be retrieved from an ERP integration if they have not yet been synced.
- Budget Changes cannot be edited or deleted once synced with an ERP integration.
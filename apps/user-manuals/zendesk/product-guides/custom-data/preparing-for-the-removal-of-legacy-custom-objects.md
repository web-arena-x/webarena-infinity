# Preparing for the removal of legacy custom objects

Source: https://support.zendesk.com/hc/en-us/articles/9418212259098-Preparing-for-the-removal-of-legacy-custom-objects

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Zendesk is [removing legacy custom objects](https://support.zendesk.com/hc/en-us/articles/9156194392730) in 2026. As an admin,
it’s important to understand the impact on your operations, if any, assess your current
environment, and coordinate a smooth transition to the new custom objects platform to
avoid interruptions.

This guide outlines the key steps admins need to take to prepare, plan, and
execute this migration.

Note: Migrating legacy custom objects to the new custom objects is not
an automated process. It requires a well-structured plan and the [involvement of developers](https://developer.zendesk.com/documentation/custom-data/).

This article contains the following topics:

- [Essential facts about the removal of legacy custom objects](#topic_pjk_551_5fc)
- [Planning and coordinating the transition from legacy custom objects to new custom objects](#topic_fwb_bv1_5fc)

## Essential facts about the removal of legacy custom objects

Legacy custom objects are being removed in two phases. See [Announcing the removal of legacy custom objects](https://support.zendesk.com/hc/en-us/articles/9156194392730) for more
details.

- **Phase 1 - No new objects or relationships**: After this date, creating new
  legacy custom objects or relationships will be disabled. However, existing
  legacy custom objects will continue to function, and new records can still be
  created on these existing objects until the final removal date.
- **Phase 2 - Full removal**: Zendesk will completely remove the legacy custom
  objects experience. Legacy APIs, the admin interface, and all legacy object
  records will no longer be accessible or supported. You must use the new custom
  objects platform.

## Planning and coordinating the transition from legacy custom objects to new custom objects

New custom objects are a low-code feature, so admins can create and manage them
independently. However, legacy custom objects were API-based. In preparation for the
removal of legacy custom objects, admins should do the following to ensure your team
resolves any dependencies on legacy custom objects.

**To prepare for the removal of legacy custom objects**

1. Check if you are using legacy custom objects. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb),
   click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules > Custom Objects** and check for "Legacy objects" in the
   sidebar.
   - If you don't see the Legacy objects page in the navigation panel, no
     further action is needed and you can disregard this article.
   - If you do see the Legacy objects page, proceed to step 2 to determin
     whether they are actively used.
2. Evaluate the scope of your use and dependencies on legacy custom objects. For
   example, you might want to:
   - Ask your development team to use the legacy custom objects [Limits API](https://developer.zendesk.com/api-reference/custom-data/custom-objects-api/limits/) to count existing
     legacy records and determine the scope of usage.
   - Identify any installed apps or integration that rely on your legacy
     objects.
   - Contact the developers of the apps with dependencies to understand their
     migration plan.

     Note: If legacy custom objects are present but
     not actively used, no further action is needed and you can
     disregard this article.
3. Inform and coordinate with stakeholders. This might include:
   - Notifying your development teams about the upcoming removal of legacy
     custom objects and sharing the [migrating examples](https://developer.zendesk.com/documentation/custom-data/custom-objects/migrating/introduction/) in our
     developer documentation.
   - Contacting your third-party app vendors to confirm whether their
     applications use legacy custom objects and inquire about their migration
     status and timelines.
   - If available, coordinating with Zendesk Customer Success Managers or
     Technical Account Managers to get tailored support throughout your
     migration process.
4. Plan and execute your migration. Typically, this might require you to:
   - Establish a migration project and assign responsible team members.
   - Develop a timeline aligned with Zendesk's removal schedule for legacy
     custom objects.
   - Begin migrating data and updating integrations to the new custom
     objects.
5. Test the migrated data and new custom objects.
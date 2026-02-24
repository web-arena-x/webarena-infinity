# Merging organizations

Source: https://support.zendesk.com/hc/en-us/articles/6216929727898-Merging-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

[Organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842#topic_npu_dkx_ac) are a way to manage users and your ticket handling workflow. They’re primarily a collection of your end users, but can also include team members.

At times, you may need to merge two organizations into one. For example, company acquisitions, restructuring, or general maintenance could all require organization merges.
Merging organizations save admins time and effort by automating the updates to the organizations themselves as well as the associated tickets and users.

This article contains the following sections:

- [About merging organizations](#topic_wfs_kzh_hzb)
- [Merging organizations](#topic_vt2_xzh_hzb)
- [Understanding how organization data is merged](#topic_jq3_v13_hzb)

Related articles

- [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842)
- [About the organizations page](https://support.zendesk.com/hc/en-us/articles/4408821417114)

## About merging organizations

Admins can merge one organization into another. The organization being merged into another is referred to as the *merging organization*. The target of the merge is referred to as the *receiving organization*.

When organizations are merged, all users, tickets, and domains are merged into one organization - the receiving organization. The merging organization is deleted after the merge completes. All changes related to an organization merge are recorded in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434). Additionally, tickets that are part of the merge show the change in their [ticket events log](https://support.zendesk.com/hc/en-us/articles/4408829602970).

### Essential facts

Before you begin an organization merge, make sure you understand the following essential facts:

- Organization merges are permanent and can’t be undone. If an organization merge is already in progress, then it can’t be undone, updated, or resubmitted.
- The organization that’s being merged into another organization (the *merging organization*) is deleted upon completion.
- Only admins can merge organizations.
- The merging organization can’t be edited or deleted during an in progress merge. With the exception of the domains, the receiving organization can be edited during a merge.
- Business rules that check or set the organization value can break when you merge organizations. Review your triggers, automations, macros, views, and SLAs.
- [Lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) that point to organizations can also break when you merge organizations. References to the merging organization aren’t updated to the receiving organization during the merge.

### Considerations and limitations

Consider the following before deciding to merge organizations. Learn more about [how data is merged](#topic_jq3_v13_hzb).

- To be eligible for merging, the merging organization must have 10,000 or fewer tickets and 10,000 or fewer users. Otherwise, the merge will be blocked.
- Group assignments aren’t updated on tickets that are merged to the receiving organization. However, the group mapping of the receiving organization applies the next time a ticket is updated and to all new tickets. This may result in tickets being assigned to an unexpected group.
- Users may [belong to multiple organizations](https://support.zendesk.com/hc/en-us/articles/4408838140314) but can have only one default organization. If a user’s default organization is merged into another, then their default organization is updated. If the merging organization isn’t their default organization, then their default remains unchanged and only the membership is updated.
- End users won’t see the merging organization in their profile if they submit a new request, update a request, or look at open requests. However, if end users were part of an organization that was merged into another, they will see the details of the receiving organization when they log into their Guide profile.
- Notifications don’t appear when an organization merge is in progress, completes successfully, or fails. Instead, you can check the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434) for details.

## Merging organizations

You must be an admin to merge organizations.

Important: A merge can’t be undone after it begins. Be careful to select the correct organizations.

**To merge one organization into another**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click the **Organizations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want to merge and click its name.
3. Click the drop-down icon at the top-right of the page and select **Merge into another organization**.
4. Begin typing the name of the receiving organization and select it from the list. Click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organization_merge.png)
5. If you select two organizations with different [group mappings](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_cfj_gfn_bc) or [sharing permissions](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nat_vgn_bc), you'll see a warning. Click **Continue merge** to proceed.
6. Review the organization merge summary to ensure it’s correct, then click **Confirm merge**.

   Note: If an organization has different ticket access permissions, a warning appears in the confirmation message. If you proceed, tickets could be exposed to unintended end users.

   This can't be undone.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organization_merge_confirm.png)

   When the merge completes, all changes are recorded in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434). Additionally, tickets that are part of the merge show the change in their [ticket events log](https://support.zendesk.com/hc/en-us/articles/4408829602970).

## Understanding how organization data is merged

When two organizations are merged, the merging organization loses all data except for open tickets, users, and domains. The following table provides more detail about how an organization’s data and settings are handled as a result of the merge.

| Organization data | Merge results |
| --- | --- |
| Tickets | All of the merging organization’s tickets, including archived and closed tickets, are merged into the receiving organization. Tickets that are part of the merge, including archived and closed tickets, show that their organizations are updated in their [ticket events log](https://support.zendesk.com/hc/en-us/articles/4408829602970). |
| Users | All of the merging organization’s users are merged into the receiving organization. |
| Domains | The merging organization’s domains are appended to the receiving organization. |
| Tags | Merging organization’s tags are lost. |
| Notes | Merging organization’s notes are lost. |
| Details | Merging organization’s details are lost. |
| Custom organization fields | Merging organization’s custom fields are lost. |
| External ID | Merging organization’s external ID is lost. |
| Group mapping | The merging organization’s group mapping is lost. |
| Shared organization setting | The merging organization’s shared organization setting is lost. |
| Related records | The merging organization’s related records are lost. |
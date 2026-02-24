# Adding tags to users and organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408881573658-Adding-tags-to-users-and-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Tags can be added to users and organizations and these tags can then be used in business rules to manage the ticket workflow and to restrict access to Help Center content.

This article contains the following sections:

- [About user and organization tagging](#topic_olv_kmn_dsb)
- [Enabling user and organization tagging](#topic_czm_tew_qc)
- [Adding tags to users and organizations](#topic_hjy_afw_qc)
- [Managing user and organization tags](#topic_bdp_thw_qc)
- [User and organization tags in business rules](#topic_lry_ifw_qc)
- [User and organization tag placeholders](#topic_tkd_ehd_rc)
- [Searching for user and organization tags](#topic_alr_gfw_qc)

## About user and organization tagging

Tagging users and organizations provides you with a way to add more data about each and then act on that data. For example, you can tag an organization or a user and then add the tag to a trigger to escalate the ticket to a specific support group.

A user's tags, and the tags of the organization to which they belong, are added to their tickets. In other words, if a user is tagged with *manager* and belongs to an organization tagged with *premium*, all the user's tickets will contain both of those tags. If a user belongs to multiple organizations, only the organization tags that are associated with the organization set on the ticket are added, not all the tags from all the user's organizations.

You can add tags manually when adding or editing users and organizations, during a bulk import, via the Zendesk API, and via enterprise single sign-on (JWT and SAML). Agents can add tags to end user profiles.
Administrators can add tags to agent and end user profiles and to organizations. On Enterprise, agents who have a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) with the correct permissions can also add tags to organizations.

User and organization tags can be used in business rules and they can be referenced as placeholders and as data in Liquid markup code.

Tags can also be used to restrict access to Help Center content (see [Restricting access to knowledge base content](https://support.zendesk.com/hc/en-us/articles/4408824005914) and [Restricting access to community content](https://support.zendesk.com/hc/en-us/articles/4408845814170)).

## Enabling user and organization tagging

An administrator can enable user and organization tagging.

**To enable user and organization tagging**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar, then select **Configuration > End users**.
2. In the **Tags on users and organizations** section, click **Enabled**.
3. Click **Save Tab**.

Note: If you want to add tags during a bulk import or via the Zendesk API, Remote Authentication, or SAML, you also must first enable this setting.

## Adding tags to users and organizations

Tags can be added when manually adding or editing users and organizations, when bulk importing user and organization data, and via the Zendesk API, Remote Authentication, and SAML.

Note: If you've added a custom user field that lets a user specify a tag, then you can also add a tag to a user by creating a trigger with the `Requester: [custom field]` action.
For more information, see [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866) and [Building trigger action statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb).

In Zendesk Support, you add tags in the user's profile page and in the organization settings page. After signing in, users can view all tags associated with their profile by accessing the Help Center source code.

Only administrators can add tags to agent profiles. Agents cannot add tags to other agents' profiles.

The user and organization tags are added to new tickets submitted after this feature has been enabled, not retroactively to a user's existing tickets. Also, these tags are only added when tickets are created, not when they're updated.

The exception to this is when you update a ticket to change the requester or organization. If you change a ticket's requester to another user, the original requester's tags are removed and the new requester's tags are added. If you only change the organization, without changing the requester, the original organization's tags are removed and the new organization's tags are added.

For information about adding tags during bulk imports, see [Bulk importing users and organizations](https://support.zendesk.com/hc/en-us/articles/4408893496218).

For information about working with user and organization tags via the Zendesk API, see [REST API: Users](https://developer.zendesk.com/api-reference/ticketing/users/users) and [REST API: Organizations](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/).

## Managing user and organization tags

In Admin Center, you can view all of your user and organization tags, along with the details of how the tags are being used and how many times they've been added. You can also remove tags from all the users and organizations to which they have been added.

**To view user and organization tags**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar, then select **Configuration >
 Tags**.

 Note: Alternatively, you can view tags added to users and organizations from the [Customers page](https://support.zendesk.com/hc/en-us/articles/4408828129946) and [Organizations page](https://support.zendesk.com/hc/en-us/articles/4408821417114). If more than 30 tags are added to an end user or organization, you can click **See more** to access the end user’s or organization’s profile page.

**To remove tags from users and organizations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar, then select **Configuration > Tags**.
2. Locate the tag you want to remove and then click **Remove**.
3. Confirm that you want to remove the tag and then click **OK**.

Note: Removing user and organization tags does not remove them from the tickets they have been added to. You can delete the tags from those tickets manually or just manage them out of your Zendesk Support as the tickets are closed.

## User and organization tags in business rules

Since a user's tags (including their organization's tags) are added to their tickets, you can use these tags in business rules to automatically make changes to the ticket. For example, based on a user or organization tag, you can automatically assign tickets to a specific group, as in the following example.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/usertag_trigger.png)

These tags can be used in any business rules (automations, macros, triggers, and views) as well as reports.

If an end user uses organization tags and any of those tags overlap with tags associated with drop-down custom organization field selections, this can cause problems, such as business rules firing unexpectedly.
For example, consider the following situation:

- An organization has the tag "test", and there's also a custom drop-down organization field with a value in the pick-list with a tag value of "test" and another of "other."
- There's a trigger set to assign a created ticket to a group when a custom field selection is "other" but the requester is in the organization with the "test" tag.

The trigger won't fire because the organization tag "test" will be applied instead of "other", as only a single tag associated with a drop-down field can be present on a ticket at any given time.

For general information about custom organization fields, see [Adding custom fields to organizations](adding-custom-fields-to-organizations.md).

## User and organization tag placeholders

User and organization tags are available as placeholders. They are properties of the User and Organization data objects and can therefore be referenced as user properties. For example:

```
{{ticket.requester.organization.tags}}
```

```
{{ticket.assignee.tags}}
```

For more information, see [Zendesk Support placeholders reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

## Searching for user and organization tags

You can always search for tags using the *tags* keyword. For example, the following search returns the tag 'premium' wherever it's been used, including in ticket details and in the forums:

```
tags:premium
```

Using the *type* keyword, you can narrow your search results to tickets that contain the tag.

```
type:ticket tags:premium
```

A search like this returns all tags (not just user or organization tags).
There's currently no way to search for user and organization tags within a ticket separate from other tags that have been added to the ticket (via custom fields, auto tagging, business rules, or manually by an agent). You can of course create a user and organization tag naming scheme (for example, user\_*tag* and org\_*tag*) and then search for those.

However, since *tags* is also a property of both the User and Organization data objects, you can narrow your search results to just those objects by using the *type* keyword.

To search for organization tags, you can use a search statement like this:

```
type:organization tags:premium
```

To search for user tags, you can do this:

```
type:user tags:beta_user
```
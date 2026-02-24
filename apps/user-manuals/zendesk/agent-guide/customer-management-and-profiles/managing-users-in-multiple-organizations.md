# Managing users in multiple organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

If [multiple organizations is enabled](https://support.zendesk.com/hc/en-us/articles/4408838140314), you can add users to multiple organizations. A user can belong to as many as 300 separate organizations. On Team plans, users can belong to only one organization.

This article contains the following sections:

- [Adding and removing multiple organizations for users](#topic_spj_srp_dp)
- [Changing the default organization for a user](#topic_cjl_trp_dp)
- [Understanding the end-user experience for multiple organizations](#topic_hyp_5rp_dp)

## Adding and removing multiple organizations for users

You can add a user to up to 300 separate organizations. You can remove a user from any of their organizations as needed.

When you add a user to an additional organization, that user's already-existing tickets are not affected. However, agents will need to manually select an organization for that user moving forward.

When you remove a user from an organization, if the organization was the user's default organization, a new default organization is selected from the user's remaining organizations. Removing users from organizations affects tickets these ways:

- Any of the user's tickets associated with the organization, that aren't in the closed state or archived, are moved to the user's default organization.
- Any closed tickets remain associated with the organization that was set on the ticket when it was closed.

Note: Administrators can add users to multiple organizations through bulk user import (see [Importing users into multiple organizations](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-and-organizations#topic_xbb_wkp_mr)).

If one of the organizations a user belongs to is deleted, any non-closed tickets associated with the deleted organization are updated to have no organization. If the organization that was deleted was the user's default organization, one of the user's other organizations is promoted to be the default organization.

**To add a user to multiple organizations**

1. Open the profile for the user you want to add to multiple organizations.
2. Click **Add organization**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_add_org_to_user2.png)
3. Start typing the name of the organization, then select the organization.

   A list of matching organizations appears as you type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_add_multi_org_to_user2.png)
4. Click **Add organization** to add another organization, and repeat as needed.

   Your update is saved automatically, so when you are finished you can simply navigate away.

**To remove an organization from a user who belongs to multiple organizations**

1. Open the user's profile.
2. Click the name of the organization you want to remove, then select **Remove**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_remove_multi_org.png)
3. Click **Yes, remove it** in the confirmation box.

## Changing the default organization for a user

When you add a user to multiple organizations, the first organization that you added to the user becomes the user's default organization.
If the default organization for a user is deleted, and the user belongs to multiple organizations, one of the other organizations the user belongs to becomes the default organization.

When an organization is deleted, any non-closed tickets associated with the deleted organization are updated to the default organization. If the organization that was deleted was the requester's default organization, one of the requester's other organizations is promoted to be the default organization.

The default organization is also used in Explore for reporting. You can report on users according to their default organization only.

You can change the default organization for a user at any time.

**To change the default organization for a user who belongs to multiple organizations**

- In the user's profile, click the name of the organization you want to make the default, then select **Make default**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/org_make_default_on_user.png)

## Understanding the end-user experience for multiple organizations

When users belong to multiple organizations, they can choose the organization for any support request they submit in your Help Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/org_multi_hc_submit_request.png)

Users who belong to multiple organizations can change the organization for any of their support requests in your Help Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/org_multi_hc_check_request.png)
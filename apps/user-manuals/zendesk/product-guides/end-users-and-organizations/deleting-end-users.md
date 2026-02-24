# Deleting end users

Source: https://support.zendesk.com/hc/en-us/articles/4408821737498-Deleting-end-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can delete end users one at a time or in bulk from the Customers page in
Support. Agents must have [access to all tickets](https://support.zendesk.com/hc/en-us/articles/4408886939930#topic_3zw_yl2_yg) to
delete end users. On Enterprise plans, this permission is set by an agent’s
[custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882). Only admins can
delete end users in bulk.

When you delete end users, they’re soft deleted and queued for permanent deletion
after 30 days.

Admins can [permanently delete end
users](#topic_vcv_yjh_xcc) before 30 days. Permanently deleting end users ensures
compliance with global data privacy laws such as the General Data Protection
Regulation (GDPR) and the California Privacy Rights Act (CPRA). For more
information about GDPR, see [Complying with privacy and data
protection law](https://support.zendesk.com/hc/en-us/sections/4405298848154) and [Forgetting a user in
Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845703194).

This article covers the following topics:

- [Considerations
  for end-user deletion](#topic_arx_sry_vcc)
- [Deleting an end
  user](#topic_dr4_r14_x1b)
- [Deleting end
  users in bulk](#topic_lhv_gvy_vcc)
- [Permanently deleting an end
  user](#topic_vcv_yjh_xcc)

## Considerations for end-user deletion

Make sure you understand the following before you delete end users from
your account:

- You can't delete these types of users:
  - An end user who’s the requester on a
    ticket that isn’t closed.
  - Placeholder users created during
    [ticket
    sharing](https://support.zendesk.com/hc/en-us/articles/4408893967514#topic_pxh_wkz_sq).
  - Users created through legacy
    Chat.
- No help center content is lost when you delete
  an end user.
- Deleting end users from your account soft
  deletes them, which means the users are still in the
  Zendesk database for 30 days before they’re queued
  for permanent deletion.
- Deleting an end user's account can’t be
  undone. Make sure you select the correct user when
  deleting end users.

## Deleting an end user

Admins and agents with access to all tickets can delete an end user.
Admins can also [delete
multiple end users](#topic_lhv_gvy_vcc) at the same time.

Deleted end users appear on the Deleted users page for 30 days before
they’re queued for permanent deletion by an automated process.

Important: Deleted end users can’t be restored.

You can’t delete an end user with tickets that aren’t closed. It’s
recommended to locate the user’s unclosed tickets beforehand and
edit the tickets to [change the requester](https://support.zendesk.com/hc/en-us/articles/4408886900506#topic_jwd_bnr_wt)
or [create a trigger to close
them](https://support.zendesk.com/hc/en-us/articles/4408827596570).

**To delete an end user**

1. Open the user's profile by doing one of the following:
   - In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Customers** icon
     (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar. Locate the user and
     click their name.
   - In a ticket, click the user's profile name or picture.
2. In the user's profile, click the user options arrow in the upper right, then select
   **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-top-right.png)
3. When prompted, click **OK** to confirm the deletion.

   The end user is
   deleted.

   If the end user has unclosed tickets, they aren’t deleted and an
   error appears.

## Deleting end users in bulk

Admins can delete up to 100 end users at a time.

**To delete users in bulk**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Customers**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.

   By default, users are sorted by their creation
   date, from most recent to oldest. Change the sort
   order by clicking a column header.
2. (Optional) Click the **Suspended Users** list if you want to
   delete only suspended users.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customers_suspended_users_list_new.png)
3. Select the checkbox for each user you want to delete. You can
   select users across multiple pages.

   Alternatively, select
   an entire page of end users by clicking the check
   box at the top of the table.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customers_delete_bulk_new.png)
4. At the bottom of the list, click **Delete**.
5. Click **Delete customers** in the dialog to confirm the
   deletion.
   - The selected users are deleted if they don’t
     have any unclosed tickets. This might take a few
     minutes.
   - The selected users aren’t deleted if they have
     tickets that aren’t closed. A message appears that
     shows which users are requesters on unclosed
     tickets.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customers_delete_bulk_new_error.png)

     Click a user’s name to view their
     unclosed tickets. You can edit the tickets to
     [change the
     requester](https://support.zendesk.com/hc/en-us/articles/4408886900506#topic_jwd_bnr_wt) or [create a trigger to
     close the tickets](https://support.zendesk.com/hc/en-us/articles/4408827596570), then attempt to delete
     the end user again.

## Permanently deleting an end user

After deleting a user, they’re queued for permanent deletion after 30
days. Admins can permanently delete end users before those 30 days
if needed.

**To permanently delete an end user**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Deleted users > Deleted users**.
2. Click the user you want to delete permanently from the list.

   A
   screen appears with the user's name and their
   associated tickets.
3. Click **Delete User**.
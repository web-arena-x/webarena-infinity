# Viewing an end user's profile in Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408822762650-Viewing-an-end-user-s-profile-in-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Accessing an end user's profile lets you view and edit their details, manage tickets, and perform actions like merging or deleting users. You can also create new tickets and view user activities such as comments and subscriptions. The profile includes default fields like role, access, email, and organization, which help in managing user interactions and support tasks effectively.

You can view an end user's profile in either Zendesk Support or in the help center. This
article describes how to view an end user's profile in Support and the default fields
contained in their profile.

The following topics are covered in this article:

- [Viewing an end user's profile](#topic_g1d_wxt_bwb)
- [Default user fields](#awg_fk2_4qb)

**Related articles**

- [Viewing your Zendesk Support user profile](https://support.zendesk.com/hc/en-us/articles/4408835022490)
- [Viewing user profiles from Help Center](../../agent-guide/additional-ticket-channels/viewing-user-profiles-from-help-center.md)

## Viewing an end user's profile

When you open an end user's profile in Support, you can view their profile and activity
information, edit certain fields, and open a ticket on their behalf. You can also perform
other actions, such as merging or deleting the user.

**To view an end user's profile**

1. Open an end user's profile using one of the following methods in Support:
   - Click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the sidebar and then search for the end
     user you want to view.
   - Click the tab for the ticket requester's profile in a ticket.
   - Click the end user's name on the [Customers page](https://support.zendesk.com/hc/en-us/articles/4408828129946).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/edit_user_profile_rel.png)
2. Click through the different tabs on the main window to view the following
   information:
   - **Tickets**: View a user's [requested or CC'd tickets](https://support.zendesk.com/hc/en-us/articles/4408829574810). The tickets list returns only
     the first 1,000 results even if there are more results.
   - **Help Center**: View a user's comments, posts, votes, and subscriptions.
   - **Related**: View a user’s lookup relationships with tickets, organizations,
     and other users. See [Using lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770).
   - **Security Settings**: Reset a user's password. See [Resetting users passwords](https://support.zendesk.com/hc/en-us/articles/4408831970202).
3. Click the **+ New Ticket** button next to the end user's name at the top right of
   the profile to create a new ticket on their behalf or the down arrow to perform actions
   such as merging, suspending, deleting, or assuming the identity of the user.

   Tip: When you create a new ticket, it might take a few minutes before it appears on the
   user's Requested tickets page.
4. View and edit user details on the left side of the profile.

   Below are the default
   user fields. If you created custom fields, they're included in the user details panel
   (see [Adding custom fields to
   users](adding-custom-fields-to-users.md)).

## Default user fields

| User data | Description |
| --- | --- |
| Role | Defines the user's function and access level. There are three user types: End user, Agent, and Administrator. By default, all new users are set to end users. Agents can only add end users. Only administrators can change a user's role. |
| Access | Important: There are organization access settings in the user profile and in the organization itself. If the settings are in conflict, the more permissive setting overrides the less permissive setting. Enable the end user to do one of the following:  - **View and edit own tickets only**, meaning users can only see and comment   on tickets where they are the requester. Note: If you chose this setting, but the org setting gives users in the org   access to all tickets, this user setting *will be overridden* by the   org setting. - **Can view tickets from user's org**, meaning user can see (but not comment   on) all tickets in their organization. Note: If you chose this setting, and the org setting restricts access for   users in the org to their own tickets only, this user setting *will   override* the org setting. |
| Email | This is the email address you added for the end user. The email address must be unique to the end user. You cannot use a duplicate email address. |
| Contacts | You can also add additional contact information for users using the **Add contacts** link. See [Adding user contact information](managing-end-users.md#topic_zb2_22c_ppb). |
| Tags | List of tags you want automatically added to new tickets created by the end user. Separate tags with a space. Tags are added to new tickets only, not updated tickets. This is an optional feature and you might not have enabled user tagging. See [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| Organization | If you use organizations, and you want to add this end user to one, click **Add organization**, then enter the name of the organization. Click **Add organization** again if you'd like to add this user to multiple organizations (see [Enabling multiple organizations for users](https://support.zendesk.com/hc/en-us/articles/4408838140314)). On the Team plan, users can belong to only one organization. On Professional and Enterprise, users can belong to multiple organizations, up to 300. A user does not have to belong to any organization, however.  If your administrator has set up user mapping, which automatically adds new users to an organization based on their email domain, you can leave this blank. |
| Language | Language the user will view your instance of Zendesk Support in. This setting affects this user only. The language can be set to any [supported language](https://support.zendesk.com/hc/en-us/articles/4408888770714) on your account. The end-user's help center will appear in the selected language and some system messages and email notifications may also be in the selected language. *Not available on Team plans* |
| Time zone | The end-user's local time zone; used to time stamp tickets submitted by this user. This setting affects this user only. *Not available on Team plans* |
| Details | Additional details about the end user. Address, for example. Details are visible to agents only, not end users. |
| Notes | Any notes about the end user. Notes are visible to agents only, not end users. |
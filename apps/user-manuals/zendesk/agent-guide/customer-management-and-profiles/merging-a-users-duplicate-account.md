# Merging a user's duplicate account

Source: https://support.zendesk.com/hc/en-us/articles/4408887695898-Merging-a-user-s-duplicate-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Duplicate accounts for a single user can make it challenging to provide great customer support. To avoid this, you can add multiple email addresses and social media handles to a user's profile. This enables you to properly identify the user regardless of the email address or social media channel they submit requests through without generating duplicate accounts. However, any time a user submits a request from an email or social media account that isn't in their user profile, a duplicate end user account might be created. This article describes how to merge duplicate accounts when this happens.

This article contains the following topics:

- [Requirements and considerations for merging end user accounts](#topic_klp_3sy_fzb)
- [Merging duplicate end user accounts](#topic_yjv_cty_fzb)
- [Understanding how user data is merged](#topic_l3l_dnr_l3)

## Requirements and considerations for merging end user accounts

If you do end up with multiple accounts for a single end user, you can merge one of the accounts into the other, as long as the following is true:

- Both accounts are for end users, not admins or agents.
- If the end user's account is unverified, they must have one or both of the following: an email address or an X (formerly Twitter) account.
- Each of the accounts to be merged have 10,000 tickets or less.

Before attempting to merge end user accounts, consider the following:

- If your account uses single sign-on and handles user authentication with JWT or SAML, you can merge end user accounts only if there are no external IDs associated with either of the end user accounts.
- Merging end user accounts can't be undone. Make sure to select the correct user accounts.
- After merging accounts, any tickets created by the duplicate (now merged) account are updated with the primary user account. These ticket updates appear in the ticket event log as a requester change, but do not cause triggers to fire.

## Merging duplicate end user accounts

Merging duplicate accounts enables your agents to provide better customer support to your end users. However, a merge can't be undone. Be careful when selecting the accounts to merge.

**To merge a user's duplicate account**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Customers** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.
2. In the **Search** bar, enter the name of the user you want to merge in the search box and click the user's name when it appears.

   Alternatively, you can open a user's profile from one of their tickets.
3. Click the User options menu in the upper right, then select **Merge into another user**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/merge_user_command_new.png)
4. Enter the user's name and all users that match what you entered are displayed. Select the correct user and then click **Merge**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/merge_user_new.png)
5. When prompted, click **Confirm and Merge** to confirm the merge. If you want to cancel the merge, close the window without clicking **Confirm and Merge**.

## Understanding how user data is merged

When you merge one user account into another, the tickets owned by the user account being merged become the tickets of the user that account was merged into and the data in each user profile is combined. The following table describes how user profile data is handled as a result of a merge. The user being merged is referred to as the *merging user* and the target of the merge is referred to as the *receiving user*. In general, the merging user will lose all data, except for tickets and email identities. The merging user's account is also [queued for permanent deletion](https://support.zendesk.com/hc/en-us/articles/4408821737498#topic_vcv_yjh_xcc)
following the merge.

| User ticket and profile data | Merge results |
| --- | --- |
| Tickets | All of the merging user's requested tickets are now requested by the receiving user. CCs are treated similarly for non-archived tickets. Tickets that are part of the merge, including archived and closed tickets, show the update in their [ticket events log](https://support.zendesk.com/hc/en-us/articles/4408829602970). |
| Phone number | Merging user's number is added as a second number in the receiving user's profile |
| Direct Line | Receiving user's value is not affected by merge. |
| Primary email | Receiving user's value is not affected by merge. |
| Secondary email | All secondary email addresses are maintained, merging user's email is added as an additional secondary email address. |
| Language | Receiving user's value is not affected by merge. |
| Time Zone | Receiving user's value is not affected by merge. |
| Organization | Receiving user's value is not affected by merge. If multiple organizations are enabled in the receiving account, all organizations will be merged. If multiple organizations are not enabled and there is no original organization only one will be merged. Tickets aren't automatically updated and may maintain old organization values. |
| Tags | Merging user's tags are lost. |
| Details | Merging user's details are lost. |
| Notes | Merging user's notes are lost. |
| Picture | Receiving user's value is not affected by merge. |
| User fields | Receiving user's fields remain intact. Merging user's fields are lost. |
| External IDs | Merging user's external IDs are lost. |
| Help Center contributions | Votes, subscriptions, community posts, and comments on articles and posts in Help Center still exist and are visible, but they are lost (they don't become associated with the target user). |
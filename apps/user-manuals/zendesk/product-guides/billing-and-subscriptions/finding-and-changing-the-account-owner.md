# Finding and changing the account owner

Source: https://support.zendesk.com/hc/en-us/articles/4408822084634-Finding-and-changing-the-account-owner

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Account > Billing > Contacts

Account ownership is managed in [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408839227290--Draft-Using-Zendesk-Admin-Center). You must be the current account owner to change account ownership. There can be only one account owner at a time. If you aren't the account owner, you can [find the account owner](#topic_xkh_3lm_ygb) and request they make the change.

Note: Zendesk can't change the account owner for you. If the current account owner is no longer available, work with your IT administrators to access their email address and initiate a password reset. If you can’t resolve this, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to initiate a security review.

This article includes the following topics:

- [Finding the account owner](#topic_xkh_3lm_ygb)
- [Transferring account ownership](#topic_ubp_zq5_w2b)
- [Finding and changing the account owner (legacy Chat)](#topic_mln_s5h_jcc)

Note: Most of the instructions in this article are for Support and Zendesk Suite accounts. If you have a legacy, Chat only account, see [Finding and changing the account owner (legacy Chat)](#topic_mln_s5h_jcc) at the end of this article.

## Finding the account owner

If you don't know the owner of your account you can view the roles assigned to your users to find out. Admins can quickly find the account owner on the account Contacts page. Both agents and admins can find the account owner on the Team members page.

**To find the account owner (admin)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Billing > Contacts**.

   The Contacts page appears with a list of account contacts. The account owner appears at the top of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_billing_account_contacts_top_of_list.png)

**To find the acounts owner (agent)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Team > Team members**.
2. Search through the list of team members.

   The team member who is the account owner will have an **Administrator (Owner)** role.

## Transferring account ownership

Only the current account owner can transfer ownership to another user. When the current owner is still available, transferring ownership is simple. The current account owner can give another billing admin the account owner role.

To transfer ownership to a different user the new owner must be a billing admin on the account. If you need to add the new account owner, see [Adding agents and administrators](https://support.zendesk.com/hc/en-us/articles/4408886939930). If you add a new user to Zendesk to become the account owner, make sure they have a verified email address. They can verify the email address themselves. A verification link is sent automatically when you add them to the account. Alternatively, you can [verify](https://support.zendesk.com/hc/en-us/articles/4408886752410#topic_ryz_p4g_b2b) the email address for them.

When you change the account owner, the previous account owner loses access to all subscription-related pages such as **Invoices** and **Payment**. Also, when you change the owner of your account, integrations that were set up by the previous account owner may break. The new account owner might need to reauthorize integrations.

**To transfer ownership to a current billing admin**

1. Make sure the new owner you want to change to has a verified email address.
2. Make sure the new owner you want to change to is a *billing admin*. See [About billing admins](https://support.zendesk.com/hc/en-us/articles/4408838125082#topic_db4_zcc_wnb). You can’t change ownership to a non-billing admin.
3. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Billing > Contacts**.

   A list of account contacts appears, including all billing admins for the account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_billing_account_contacts_page_owner.png)
4. Locate the billing admin you want to make the new account owner.
5. Click the options menu icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the billing admin and select **Make account owner** from the drop-down menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_billing_account_owner_menu.png)
6. When the confirmation message appears, click **Change owner.**

   After confirmation, a success message appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_billing_account_owner_success.png)

**To transfer ownership to a new billing admin when no agent seats are available**

If you need to add the new owner to the account, and no agent seats are available, the current owner can edit their own user profile to make the transfer.

1. In Zendesk Support click the current owner's profile icon in the upper-right corner of the page header and then select **View profile page**.
2. In the profile's email field click **add contact** and enter the new owner's email address.

   The current owner will receive an email that this new address has been added. Make sure the current owner verifies this new email address.
3. After the current owner receives and verifies the email, return to the current owner's profile in Support.
4. Click the drop-down icon on the new email address and select **Make primary contact**.
5. Delete the old owner's email address from the account.

   The account and profile now belong to the new owner.
6. Reset the account's password and update the other account information as needed.

   Note: If you don't want to change the email address of the current owner profile, you can submit a request to [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to see if it's possible to add a temporary agent seat to your account to create a new user profile.

## Finding and changing the account owner (legacy Chat)

If you have a legacy, Chat only account, there isn't a Contacts page in Admin Center and there aren't billing admins. Instead, follow these instructions to find and change the account owner.

**To find and change the account owner**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) Account in the sidebar, then select **Billing > Account owner**.

   A page appears with a list of team members in the Chat only account. The account owner appears at the top of the list.
2. To change the account owner, find the team member you want to make the new account owner.
3. Click the options menu icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the team member and select **Make account owner** from the drop-down menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_billing_account_owner_chat_only.png)
4. When the confirmation message appears, click **Change owner.**
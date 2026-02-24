# Adding end users

Source: https://support.zendesk.com/hc/en-us/articles/4408893585178-Adding-end-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

End users, also known as customers, are the people who request support by interacting with Zendesk and submitting tickets. Regardless of the channel your end users use to request support, each must have an account. An end user's account contains both required and optional information.

There are several ways to add end users:

- End users can add themselves by submitting a support request.
- Agents can add them by [creating a ticket on their behalf](https://support.zendesk.com/hc/en-us/articles/4408882462618) or by including the user’s email address in a side conversation.
- Agents can add them manually in Support.
- Admins can add several users at once by [bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-) or [importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/support/users).

This article covers how to [add individual end users](#topic_tkx_mdu_kf) by creating new user accounts in Zendesk Support.

Note: Agents must have [access to all tickets](https://support.zendesk.com/hc/en-us/articles/4408886939930#topic_3zw_yl2_yg) to create or edit end users. On Enterprise plans, this permission is set by an agent’s [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).

This article includes the following topics:

- [Adding end users](#topic_tkx_mdu_kf)
- [Understanding the security concerns of using non-existing email addresses](#topic_a33_vhw_52c)

Related articles:

- [Managing end user settings](../../product-guides/account-access/managing-end-user-settings.md)
- [Deleting end users](https://support.zendesk.com/hc/en-us/articles/4408821737498)

## Adding end users

You can add individual end users by manually creating new user accounts in Zendesk Support. Both agents and administrators can perform this action. You might use this if, for example, you're on the telephone with a customer who has never before requested support and doesn't have an account. By creating a user account, you can then follow up with an email.

There are additional user registration settings you can set after you add an end user, such as access to your Help Center, email verification, and support request settings.

**To add an end user**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Customers** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.
2. Click **Add customer**. Alternatively, hover over the **+Add** tab in the top toolbar and select **User**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_buttons_support_2.png)

   If you have the Customer Lists add-on, navigate to Customer Lists, click “**All customers**” and then click **Add customer**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customers_lists_all_lists.png)
3. Enter the user's **Name** and **Email**.

   For security reasons, avoid using [non-existing email addresses](#topic_a33_vhw_52c).
4. Click **Add**.
5. When the user's profile opens, enter additional information for the user.

   See [Viewing a user’s profile in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408822762650) for information about default user fields.

## Understanding the security concerns of using non-existing email addresses

Avoid adding end users to your Zendesk account with non-functional or non-existing email addresses. This poses potential security risks. If a non-existing domain is subsequently registered, an unauthorized individual could start receiving emails sent to that address, which may contain private or personal data.

If your workflow requires a non-existing email address, use **@example.com**, because this domain is universally undeliverable and will not cause issues.
# Setting your allowlist and blocklist to control email support requests

Source: https://support.zendesk.com/hc/en-us/articles/4408886840986-Setting-your-allowlist-and-blocklist-to-control-email-support-requests

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > People > Configuration > End users

Typically, when an end user submits a support request by email, the email becomes a new ticket. However, you can control what happens to email support requests by using the allowlist or blocklist.

For example, you can block specific users from creating tickets or suspend their tickets so you can review them first. Or, you can only allow users from a particular email domain to create tickets. See [Understanding the allowlist and blocklist](https://support.zendesk.com/hc/en-us/articles/6136740916250) for usage examples, limitations, and considerations.

You must be an administrator to set the allowlist and blocklist.

This article covers the following topics:

- [Setting your blocklist and allowlist](#topic_jqt_4b4_xz)
- [Rules for setting your blocklist and allowlist](#topic_arr_xny_txb)

## Setting your blocklist and allowlist

Zendesk reads email headers of incoming support requests to determine whether an email should become a ticket or be suspended or rejected based on the [rules](#topic_arr_xny_txb) you’ve configured.

Note: Check the email headers of the emails you want to block or allow. If both FROM and REPLY-TO are present, use the FROM value because this is used to identify the user.

**To edit your blocklist and allowlist**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Configuration > End users**.
2. Enter your **Allowlist** and **Blocklist** settings. See [Rules for setting your blocklist and allowlist](#topic_arr_xny_txb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bwlist_settings2.png)

   You can enter up to 10,000 characters in the allowlist and blocklist fields. If you are adding multiple email addresses or domains, separate them with a space.
3. Click **Save tab**.

## Rules for setting your blocklist and allowlist

Consider the following rules and guidelines before setting your blocklist and allowlist:

- Leave the allowlist blank to allow all users to submit tickets to your Zendesk account, except those added to the blocklist.
- Use keywords or symbols with a blocklist or allowlist entry to make the restrictions broader or more specific:

  - To block or allow an entire email domain, do not include the "@" symbol. An email domain with "@" will not be successfully added to the allowlist or blocklist.
  - When using keywords, type the keyword followed by a colon with no space after the colon (for example, **`reject:megaspam.com`**). Separate multiple entries with a space, and add the keyword before each entry (for example, `reject:randomspammer@gmail.com reject:megaspam.com
    reject:spammerspace.com`). See [Allowlist and blocklist usage examples](https://support.zendesk.com/hc/en-us/articles/6136740916250#topic_hyf_mfs_kd).
  - To send support requests from specific users to the suspended tickets queue, enter the keyword **`suspend:`** in front of an email address or domain list in the blocklist.
  - To completely block support requests from specific users, enter the keyword **`reject:`** in front of an email address or domain list in the blocklist. Tickets will not be added to the suspended tickets queue, and there will be no record of the ticket in your Zendesk account.
  - The keywords **`reject:`** and **`suspend:`** apply only to support requests and don't prevent users from creating an account. See [Limitations when using the allowlist and blocklist with other Zendesk channels](https://support.zendesk.com/hc/en-us/articles/6136740916250#topic_kkv_4gm_nyb).
- Add a wildcard (**\***) in your blocklist to suspend ticket submissions from all new users except those added to the allowlist. This sends tickets from every user not added to the allowlist into the suspended tickets queue, preventing new users from creating accounts.
  - A wildcard in the blocklist won't prevent tickets from being created by users who already have profiles; however, blocklisting a domain or email address will. To prevent traffic from a specific user with a profile, suspend or delete the user.
  - Use the keywords **`suspend:`** and **`reject:`** when using wildcards to suspend most users but reject others. This applies to individual users only and not domains. If you add a full email address with either the **`suspend:`** or **`reject:`** keyword, the user is suspended or rejected accordingly (unless the user already has a user profile).
- If an address or domain conflict exists between **`suspend:`** and **`reject:`**, then Zendesk defaults to suspension. For example, entering **\* reject:gmail.com** in your blocklist causes a suspension rather than a rejection because the wildcard (**\***) applies to all addresses and domains, which conflicts with the gmail.com reject entry.
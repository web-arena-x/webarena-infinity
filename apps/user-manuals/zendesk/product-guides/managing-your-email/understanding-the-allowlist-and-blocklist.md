# Understanding the allowlist and blocklist

Source: https://support.zendesk.com/hc/en-us/articles/6136740916250-Understanding-the-allowlist-and-blocklist

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Use the allowlist and blocklist to control email support requests by accepting, suspending, or rejecting emails based on configured rules. The allowlist lets you accept emails from specific domains or addresses, while the blocklist suspends or rejects others. Note that these lists primarily affect email channels, with limitations on other channels like help center and API requests.

Location: Admin Center > People > Configuration > End users

As described in [Setting your allowlist and blocklist to control email support requests](https://support.zendesk.com/hc/en-us/articles/4408886840986), Zendesk administrators can use the allowlist and blocklist to accept, suspend, or reject emails.

This article covers the following topics:

- [About the blocklist and allowlist](#topic_f2v_rff_zz)
- [Allowlist and blocklist usage examples](#topic_hyf_mfs_kd)
- [Limitations when using the allowlist and blocklist with other Zendesk channels](#topic_kkv_4gm_nyb)
- [Considerations](#topic_prd_zf5_j5b)

## About the blocklist and allowlist

Zendesk reads email headers of incoming support requests to determine whether an email should become a ticket based on the [rules](https://support.zendesk.com/hc/en-us/articles/4408886840986#topic_arr_xny_txb) you’ve configured in your allowlist and blocklist.

If an incoming support request originates from an email address or domain on the blocklist, it becomes a [suspended ticket](https://support.zendesk.com/hc/en-us/articles/4408889141146#topic_vpr_1sp_nj) with the suspension cause: **Email is from a blocklisted sender or domain**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_blocklist.png)

You can also create rules to completely block users so there’s no record of the ticket in your Zendesk account.

Use the allowlist to accept emails from specific domains or email addresses. For example, you can use the allowlist with your blocklist to allow all emails from the gmail.com domain but block specific email addresses within that domain.

Adding a domain to the allowlist or blocklist also allows or blocks the related subdomains.

Your allowlist overrides your blocklist. For example, if you add a specific domain to the blocklist but allow a user with that email domain, they will be given access.

## Allowlist and blocklist usage examples

You can use a combination of the [blocklist and allowlist rules](https://support.zendesk.com/hc/en-us/articles/4408886840986#topic_arr_xny_txb) to ensure you are permitting access or blocking the correct users. This section contains some usage examples you can replicate for your own Zendesk account.

### Approve a domain, suspend all other users

You can allow specific domains access to your Zendesk account by adding the domain to the allowlist and suspend all users with a different email domain by adding a wildcard (**\***) to the blocklist. In the following example, only email from the domain mondocampcorp.com will be permitted access.

```
allowlist: mondocamcorp.com
blocklist: *
```

Enter multiple domains separated by a space to allow more than one domain access.
In the following example, email from the domains mondocamcorp, comdocam, and mondostore are permitted, and all other users will be suspended.

```
allowlist: mondocamcorp.com mondocam.com mondostore.com
blocklist: *
```

### Approve a domain, but suspend specific email addresses with the domain

Using the **`suspend`** keyword, you can prevent a specific email address with an allowed domain from accessing your Zendesk account.

In the following example, only email from gmail.com is given access, except for the email address randomspammer@gmail.com.

```
allowlist: gmail.com
blocklist: * suspend:randomspammer@gmail.com
```

### Approve a domain, but reject specific email addresses and domains within it

Similar to the previous example, you can block specific email addresses from using an allowed domain by entering their email address in the blocklist. Use the **`reject`** keyword to prevent a user's tickets from being added to your Zendesk account.

In the following example, only email from gmail.com is accepted. All tickets from other email domains are sent to the suspended tickets queue except for the email address randomspammer@gmail.com. Email from randomspammer@gmail.com will be rejected completely, and the ticket will not be recorded in your Zendesk account.

```
allowlist: gmail.com
blocklist: * reject:randomspammer@gmail.com
```

Note: If you are still getting requests from blocked domains or email addresses, we recommend contacting [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) so we can help you diagnose the problem. This can be the result of email spoofing.

### Approve all, but reject specific email addresses and domains

You can also allow all users to register except for specific email addresses and domains. To allow all users to register, leave the allowlist blank, then enter any blocked users.

In the following example, everyone can access your Zendesk account except for randomspammer@gmail.com and users sending email from the megaspam.com and spammerspace.com domains. Because the **`reject:`** keyword is used, all emails from those accounts are blocked completely, and the tickets aren't recorded in your Zendesk account.

```
allowlist: 
blocklist: reject:randomspammer@gmail.com reject:megaspam.com reject:spammerspace.com
```

### Suspend support request tickets from specific email addresses or domains

Adding an email address or domain to your blocklist suspends tickets from those users, but only if those tickets are submitted through the email channel.

```
allowlist: 
blocklist: suspend:randomspammer@gmail.com suspend:megaspam.com
```

When using the **`suspend`** keyword to suspend all support requests from a specific domain, all tickets from that domain are suspended, even if individual email addresses with that domain are in the allowlist.

For email support requests only: To suspend all tickets from a domain but allow specific users, add the domain to the blocklist (without the "@" symbol or the **`suspend`** keyword) and add the allowed email addresses to the allowlist. This procedure does not work for channels outside of email because only email respects the allowlist for support requests.

## Limitations when using the allowlist and blocklist with other Zendesk channels

If you’d like to use the allowlist and blocklist for channels outside of email, for example, to customize who can create support requests and register on your help center, it works differently than it does for email.

### Limitations for support requests submitted through other channels

- Only the email channel uses the allowlist for support requests. All other channels, such as the help center support request form, the Zendesk API, or Web Widget, ignore the allowlist for support requests.
 Therefore, email addresses or domains you add to the allowlist will only be respected for support requests you receive by email.
- You can use the blocklist to block specific email addresses or domains from submitting support requests from other channels. To do this, you *must* use the **`suspend:`** and **`reject:`** keywords.
- A wildcard (\*) is ignored for all channels outside email for support requests. See the example: [Approve all, but reject specific email addresses and domains](#topic_kmx_xec_ae).

### Limitations for account registration through your help center

- If you’ve added a wildcard (\*) to the blocklist, only users with domains in your allowlist can create accounts, but users with blocked domains can still submit support requests through the help center request form.
- When **`suspend:domain.com`** or **`reject:domain.com`** are used in the blocklist, users with these domains can't submit support requests through the help center request form but can still create accounts with blocked domains.

## Considerations

Consider the following when setting up your blocklist and allowlist:

- The allowlist doesn’t prevent tickets from being suspended. Tickets can be suspended for several reasons, as described in [Causes for ticket suspension](https://support.zendesk.com/hc/en-us/articles/4408828416282).
- The allowlist doesn't provide access for suspended users. Suspension takes priority over a user's email in the allowlist.
- If you set up [user mapping](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nxl_vdt_bc):
 - Email domains saved in the organization's **Domains** list are automatically allowed. You don't have to add these domains to the allowlist manually.
 - If a user's domain or email address is in the blocklist, but their full email address is present in an organization's **Domains** field, the address is still allowed.
- If an email subject includes the text “Out of office” or the ticket originates from an email with a “do not reply” address, the ticket will be suspended, even if the email address is on the allowlist.
- Email addresses on the blocklist still receive notifications if the user is the requester or added as a CC on a ticket. To prevent notifications, [suspend the user](https://support.zendesk.com/hc/en-us/articles/4408889293978#topic_h4v_hsh_15b).
- If an email includes a blocked email address in the CC field that isn't associated with an existing user, then a new user record is not created. If a user profile exists for the email address, the blocklist has no effect.
- If you blocklist a user that is a CC on a ticket, they won’t be removed from existing tickets.
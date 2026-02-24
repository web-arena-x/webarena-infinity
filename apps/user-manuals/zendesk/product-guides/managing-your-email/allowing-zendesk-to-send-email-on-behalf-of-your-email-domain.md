# Allowing Zendesk to send email on behalf of your email domain

Source: https://support.zendesk.com/hc/en-us/articles/4408832543770-Allowing-Zendesk-to-send-email-on-behalf-of-your-email-domain

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

By allowing email to be sent on behalf of your domain, you maintain your brand identity in customer communications. Set up an SPF record in your DNS settings to authorize sending emails from your domain. This prevents emails from being flagged as spam and removes the "via" statement in messages.

If you want to use your own email address to receive support requests, and you've [added your email address as a support address](https://support.zendesk.com/hc/en-us/articles/4408886828698#topic_wtd_1jl_nwb) in Zendesk, then you can set up your custom email domain to verify that Zendesk can send email on behalf of your email server.

For example, if you receive email from your customers at *help@acme.com*, and you've set up an automatic redirect to forward all email received there to Support, you can authorize Zendesk to send out notifications as if it originated from your own email address (for example: *help@acme.com*). That way you can preserve your branding throughout the entire process.

You don’t have to configure your email domain this way, but it’s recommended if you use your own custom email domain and have [set up forwarding to an external email address](https://support.zendesk.com/hc/en-us/articles/4408886828698-Forwarding-incoming-email-to-Zendesk-Support). If you use a non-custom domain, such as addresses ending in @gmail.com or @yahoo.com, you can't use this feature, as you won't have access to the account DNS settings.

Note: If you use the Zendesk Connector for Gmail to send emails, it's recommended, but not required that you set up an SPF record to allow Zendesk to send email on your behalf (see [Enabling automatic ticket creation for your Gmail inbox](https://support.zendesk.com/hc/en-us/articles/4408835030426)).

This article includes these topics:

- [The advantages of this configuration](#topic_g5q_s42_vp)
- [Setting up records for your domain](#topic_1h2_2v2_vp)
- [Verifying your domain](#topic_ryh_djh_sfb)
- [Understanding SPF checks](#topic_oct_kvr_42b)

## The advantages of this configuration

Note: To use this configuration, you must [add your email address as a support address](https://support.zendesk.com/hc/en-us/articles/4408886828698#topic_wtd_1jl_nwb) in Zendesk before proceeding.

So, do you have to allow Zendesk to send email on behalf of your email domain? The short answer is: *No.* The slightly longer answer is: *Only if you really don't want your customers to see the Zendesk name on their messages.*

When Zendesk sends an email message using your email address (which is what happens if you've [set up a support address with forwarding](https://support.zendesk.com/hc/en-us/articles/4408886828698-Forwarding-incoming-email-to-Zendesk-Support)) the message identifies the sender as *zendesk.com* to avoid getting rejected. However, if you allow Zendesk to send email on behalf of your email domain, Zendesk stops sending messages from *zendesk.com*, and sends them from your domain, completely preserving your branding.

If you *don't* complete the tasks described in this article, your customers might see something like this:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_via_zendesk.png)

The following warning will also appear in the agent interface next to your external support addresses:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/spf_warning_v2.png)

However, if you complete the tasks described in this article, the **via** statement and warning don’t appear.

## Setting up records for your domain

Note: Setting up records for your domain can be confusing because it's something most of us rarely do. Consult your system administrator, if you have one, before proceeding.

The process of setting up an SPF record is different for different domain registrars. For example, here are the instructions for [GoDaddy](http://help.godaddy.com/article/680#spfrecs), [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317), [1&1](https://help.1and1.com/domains-c36931/manage-domains-c79822/dns-c37586/add-or-remove-txt-records-a792509.html), [Network Solutions](http://www.networksolutions.com/support/how-to-manage-advanced-dns-records/), and [Google Domains](https://support.google.com/a/answer/178723?hl=en).

**To create or edit an SPF record to reference Zendesk**

- Edit your domain's DNS settings to add a TXT record. The steps vary depending on your domain registrar. A TXT record is required for your SPF record to be validated. Zendesk attempts to verify this record when you [add a support address](https://support.zendesk.com/hc/en-us/articles/4408886828698#topic_wtd_1jl_nwb).

Zendesk recommends using the following SPF record:

```
v=spf1 include:mail.zendesk.com -all
```

Note the following:

- If you use `include:mail.zendesk.com`, then it must be in the first-layer lookup
- SPF macros are supported
- `redirect:` syntax is supported
- Record flattening services will work, though this practice may be less stable than `include:`, `redirect:`, or macro syntax.

Note: While the SPF mechanism you choose is up to your domain admin, we recommend employing a hardfail SPF mechanism (`-all`), which offers the greatest security against email spoofing. An invalid SPF record can cause verification to fail. Seek support from your domain provider, as Zendesk cannot help you administer your DNS or security records and policies.

If you've already set up an SPF record for another purpose, add a reference to Zendesk to it. The SPF specification requires that you only have one SPF record on your domain. If you have multiple records, it may cause issues, and cause rejections of your email.

For example, instead of having two separate records, such as `v=spf1 include:_spf.google.com -all` and `v=spf1 include:mail.zendesk.com -all`, combine them into one, like this:

```
v=spf1 include:_spf.google.com include:mail.zendesk.com -all
```

In the past, Zendesk suggested alternate formulations for SPF records, including `include:smtp.zendesk.com` and `include:support.zendesk.com`. These are both outdated SPF records. While they might still work, they're not the best option. If you're still using them, you'll see a warning flag indicating you've set up an outdated record.

Tip: Consider making an additional update to digitally sign outbound email from Zendesk to prevent your customers' email clients from blocking email. Digitally signing email proves that an email actually came from your organization and not someone pretending to be your organization. For instructions, see [Digitally signing your email with DKIM](https://support.zendesk.com/hc/en-us/articles/4408822303386-Digitally-signing-your-email-with-DKIM-or-DMARC).

## Verifying your domain

Zendesk auto-verifies this record when you [add a support address](https://support.zendesk.com/hc/en-us/articles/4408886828698#topic_wtd_1jl_nwb). It currently does not have a verification function but we may require the value be added to your domain's DNS record in the future.

## Understanding SPF checks

Sender Policy Framework (SPF) is a domain level email authorization protocol that allows you to declare which IP addresses are allowed to send email as if it originated from your domain.

This is accomplished by adding Domain Name System (DNS) TXT record. Think of DNS as a publicly accessible record for the internet. This record enables you to state publicly that Zendesk is an authorized sender for your domain.

When an email client receives a message, it performs an SPF check on the sending domain to verify that the email came from who it says it did. If this check fails, or there isn't a DNS record that says that Zendesk is a permitted sender, some receivers might consider that email spam or a phishing attempt, and flag it as untrustworthy or not display it to your customers at all.

Zendesk avoids this by sending email using our own domain when we're not authorized to use your domain, and by using your domain only when you authorize Zendesk with a proper SPF record. Generally, this helps to prevent emails from your Zendesk account to your customers from being incorrectly marked as spam. However, if you are having this problem, see [How can I stop my emails from going into my customer's spam folder?](https://support.zendesk.com/hc/en-us/articles/4408836031002)

If you're curious, you can read more about SPF at [www.openspf.org](http://www.openspf.org). If you're having trouble verifying your SPF record, see [Why is my SPF record not validating?](https://support.zendesk.com/hc/en-us/articles/4408820922650)
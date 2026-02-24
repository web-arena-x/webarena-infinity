# Accepting wildcard email addresses for support requests

Source: https://support.zendesk.com/hc/en-us/articles/5318946039578-Accepting-wildcard-email-addresses-for-support-requests

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enable wildcard email addresses to ensure customer emails reach you even if they misspell your support address. This feature allows any variation before the @ symbol to create a ticket, using your default support address as the Reply From. It's a helpful way to capture all customer inquiries without needing to specify every possible email variation.

As an alternative to, or in addition to, using [support addresses](https://support.zendesk.com/hc/en-us/articles/5279521301914), you can allow end users to send email to any variation of the name that precedes the @ symbol of your Zendesk address, regardless of whether it's a known support address. If a customer misspelled your support email address (for example, biling@*yoursubdomain*.zendesk.com), the email can be accepted and a ticket created. These types of variations are referred to as *wildcards*.

For example, you don't need to explicitly declare any of these email variations in your Zendesk account:

- support@myaccount.zendesk.com
- help@myaccount.zendesk.com
- sales@myaccount.zendesk.com
- billing@myaccount.zendesk.com

A wildcard address can have anything preceding the @ symbol, but the subdomain that follows the @ symbol (*yoursubdomain*.zendesk.com) must remain the same.

Wildcard email addresses use your [default support address](https://support.zendesk.com/hc/en-us/articles/5279521301914#topic_btc_h1f_bwb) as the Reply From address. Any email sent to a variation of your Zendesk Support email address that is not a known support address will use your default support address as the Reply From. If you have multiple brands, the default support address for your default brand will be used as the Reply From.

**To turn on wildcard email addresses**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. In the Email settings section, select **Accept wildcard emails**.
3. Click **Save**.
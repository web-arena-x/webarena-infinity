# Using an allowlist to manage where the Web Widget appears

Source: https://support.zendesk.com/hc/en-us/articles/10212540848538-Using-an-allowlist-to-manage-where-the-Web-Widget-appears

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Use an allowlist to control where your Web Widget appears by specifying approved domains. This feature ensures the widget functions only on listed domains, blocking it elsewhere. You can easily add or remove domains from the allowlist or disable it entirely to make the widget active on all sites with the code snippet.

Admins can create an allowlist of website domains to specify where their Web Widget can be shown to end users. When you create an allowlist:

- The widget can be embedded and accessed on any web pages within the domains (or subdomains) added to the list.
- The widget cannot be accessed on any web pages from domains *not* included in the list.
- Admins can quickly block the Web Widget from appearing on a domain or subdomain by removing it from the widget’s allowlist.

It’s important to note that the allowlist does *not* prevent your Web Widget code snippet from being added to a website’s code. Rather, it stops the code snippet from functioning, blocking the widget on any sites in the domains not included in the list.

This article includes the following topics:

- [Creating an allowlist for the Web Widget](#topic_edv_xd5_2tb)
- [Removing a domain from the allowlist](#topic_tml_h25_2tb)
- [Turning off the allowlist](#topic_gyt_h25_2tb)

## Creating an allowlist for the Web Widget

You can create an allowlist of website domains to specify where their Web Widget *can* be shown to end users.

**To create an allowlist for a widget**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the widget you want to edit.
3. Scroll down, then click **Installation** to expand it.
4. Click the checkbox to **Only allow Web Widget to be installed on these domains**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ww_allowlist_install_tab.png)
5. Add the domains or subdomains where the widget *can* be installed. To add all subdomains from a single domain, add an asterisk before the domain name (for example, `*.yourdomain.com`).

   Only alphabetical characters are allowed after the final dot (.)
   in the subdomain. For example, `my-awesome-restaurant.pizza` is valid, but `my-awesome-restaurant.pizza-chain` is not.
6. Click **Save**.

Note: As soon as you save, Web Widget appears only on web pages in the specified domains. If you enable the allowlist for a widget that has already been embedded in a website, and that website’s domain or subdomain is not included in the allowlist, it will be blocked on that website.

## Removing a domain from the allowlist

If you no longer wish to allow your Web Widget on a domain or subdomain, you can remove that domain from the allowlist, which immediately blocks it from the removed website.

**To remove a domain from the allowlist**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the widget you want to edit.
3. Scroll down, then click **Installation** to expand it.
4. Under **Only allow Web Widget to be installed on these domains**, remove the domains or subdomains where the widget should be blocked
5. Click **Save**.

## Turning off the allowlist

If you choose to no longer restrict your Web Widget by domain, you can turn off the allowlist on that widget. When you turn off the allowlist, the Web Widget becomes active on all websites that have added the Web Widget code snippet to their page code.

**To turn off the allowlist**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the widget you want to edit.
3. Scroll down, then click **Installation** to expand it.
4. Deselect the checkbox to **Only allow Web Widget to be installed on these domains**.
5. Click **Save**.
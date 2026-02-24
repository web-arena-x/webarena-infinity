# Restricting the Chat widget by country or domain

Source: https://support.zendesk.com/hc/en-us/articles/4408887520282-Restricting-the-Chat-widget-by-country-or-domain

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Using the Widget Security settings in the dashboard, you can restrict what countries and domains can load the chat widget.

Note: If you use Web Widget (Classic) with Zendesk Support, keep in mind that the blocked countries and allowed domains settings below impact only chat availability and will not affect the Help Center or contact form experience.

## Adding countries to the Blocked Countries list

Prevent the widget from loading in certain countries by adding them to the Blocked Countries list, or "blocklist." You might want to use this setting if you live in a locale where there are legal restrictions against doing business with certain other countries. If you don't enable this setting, the widget will load for all visitors regardless of the country they're located in.

**To add or remove countries from the Blocked Countries**

1. From the Chat dashboard, go to **Settings**> **Widget**> **Widget Security** tab.
2. Next to **Blocked Countries**, select **On**.
3. To add a country to the blocklist, select it from the dropdown menu.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_block_menu.png)
4. To remove a country from the blocklist, click on its tile. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_unblock_country.png)
5. Click **Save Changes**.

## Adding domains to the Allowed Domains list

Specify the trusted domains you want the widget to load on by adding them to the Allowed Domains list, or "allowlist." Enabling this feature prevents others from taking your widget code snippet and putting it on their own websites.

You can enter an unlimited number of URL paths. It will do an exact match with what was entered.Entering *subdomain.domain.com* will mean the widget will only load for that specific subdomain, and not all of *domain.com*. If you want to support all subdomains, you can use a wildcard (for example, \**.domain.com*).

**To add domains to the Allowed Domains list**

1. From the dashboard, go to **Settings**> **Widget**> **Widget Security** tab.
2. Next to **Allowed Domains**, select **On**.
3. Enter the domains you want to allow in the field. To add additional domains, click the **+**button. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_allow_domain.png)
4. Click **Save Changes**.
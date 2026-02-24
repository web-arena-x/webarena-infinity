# Accessing Zendesk with a reverse proxy

Source: https://support.zendesk.com/hc/en-us/articles/4728116057626-Accessing-Zendesk-with-a-reverse-proxy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Zendesk has a sophisticated set of abuse protection systems that protect all Zendesk instances and the overall stability of the platform. Most Zendesk customers and their customers (end users) access Zendesk directly over the internet. Zendesk assumes this standard setup. Customers deviating from this standard may experience issues when connecting to Zendesk.

For example, an organization may want their agents and end users to access Zendesk from a single point of access or their own CDN by setting up a reverse proxy. The reverse proxy intercepts requests from web clients trying to access Zendesk and forwards them to Zendesk. The web clients never communicate directly with Zendesk. Only the proxy communicates directly with Zendesk.

Zendesk can't prevent customers from configuring their access in this way. However, this is a non-standard use case and may result in undesired behavior, including the following:

- Bot management challenges (CAPTCHA) - If all requests come through a single IP or ASN, they're more likely to be identified as bots even if they're legitimate users. This is even more likely if the proxy or CDN alters HTTP headers in some way.
- Rejection of search engine crawlers and other “good” bots - Cloudflare identifies good bots in part through request IPs and ASNs. For example, if a request with a Googlebot User Agent has a request IP that's different from Google’s registered IPs, it will be rejected by Cloudflare.
- Indexing wrong pages - If not rejected by Cloudflare, search crawlers will likely try to use the canonical URL as provided by Zendesk site metadata tags. As a result, if a search engine actually crawls a proxied site, it will index pages with non-proxied URLs.
- Rate limiting - Rate limits are applied based on the request IP. If all customer requests travel through a single or a small set of IP addresses, rate limits are more likely to be applied.
- Cache issues - If your proxy or CDN setup has custom caching logic, Zendesk can't guarantee the integrity of this cache. For example, deleted articles might be visible for longer in the proxy than they are in the help center. Changes to permissions might also be delayed.

Before using a reverse proxy, consider whether it's really necessary. If you need to change the URL of your help center, you can use host mapping instead. See [Host mapping - Changing the URL of your help center](../setting-up-your-help-center/host-mapping-changing-the-url-of-your-help-center.md).

## Guidelines

If using a reverse proxy for accessing Zendesk is unavoidable, bear in mind the following guidelines:

- All traffic via the proxy must use multiple IPs for egress to avoid rate limiting and appearing like a bot
- Reverse proxies must be transparent and not manipulate headers in any way, such as overwriting the User Agent

Even so, traffic might still be categorized as bot traffic by Zendesk systems. If you follow these guidelines and are still encountering issues, contact your IT department for help.
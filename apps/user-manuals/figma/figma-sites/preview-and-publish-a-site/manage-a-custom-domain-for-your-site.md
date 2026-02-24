# Manage a custom domain for your site

Source: https://help.figma.com/hc/en-us/articles/31414274019863-Manage-a-custom-domain-for-your-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

By default, Figma hosts published sites on a randomly generated `figma.site` subdomain. After publishing, you can connect your website to a custom domain you own.

### How many custom domains can you have during the beta?

Custom domains are free of charge through 2025. Organization and Enterprise plans can connect as many custom domains needed, and Professional plans can connect up to 10 custom domains. These limits are subject to change after 2025.

| **Plan** | **Number of custom domains** |
| --- | --- |
| Professional | 10 |
| Organization | Unlimited |
| Enterprise | Unlimited |

## Connect a custom domain to your site

![The Domains tab in site settigns showing a connected domain "earthling.com" with status "Connected" and base domain details.](https://help.figma.com/hc/article_attachments/31915849641111)

Before adding a custom domain to Figma Sites, you’ll need to purchase one from a domain registrar and update its settings.

Here’s the process:

1. [Publish your site](https://help.figma.com/hc/en-us/articles/31242845959703).
2. From a sites file, click  **Settings** in the left navigation bar.
3. In the **Site** section, click  **Domains.**
4. Click **Add connected domain**and enter your domain.
5. If using an apex domain or `www` subdomain, choose whether to redirect the subdomain to the apex domain or vice versa. Use the toggle to disable the redirect if needed. This option won’t appear if you’re using any other subdomain. See the note below if you need help choosing.
6. Sign in to your domain registrar.
7. Locate the DNS settings, often found under **Domain management** or **Advanced settings**.
8. Add the TXT and CNAME record provided by Figma to your DNS settings.
9. Return to the **Domains** page in Figma and click  **Refresh.**

**Understanding apex domain and** `www` **subdomain redirects**

Figma supports connecting both apex domains and subdomains like `www`. An apex domain—also called a root or naked domain—is the highest-level domain without any subdomain prefix.

For example, `example.com` is the apex domain, while `www.example.com` is the `www` subdomain

If you use an apex domain or a `www` subdomain, Figma will ask whether you want to redirect users from the subdomain to the apex domain, or vice versa.

If you're not sure which option to choose, we recommend redirecting the apex domain to the `www` subdomain. However, this is more about preference than anything else. Modern browsers and SEO tools treat both versions equally, as long as one redirects cleanly to the other. If you don’t redirect from one to the other, this can split your traffic and impact SEO.

The option to add a redirect won’t appear if you’re using any other subdomain.

### Troubleshoot the domain connection

If you encounter issues connecting your domain, there may be a few reasons why:

- **Cloudflare domains:** If Cloudflare is your custom domain provider, you need to [set the proxy status for the domain](https://developers.cloudflare.com/dns/proxy-status/) to **DNS only**. This configuration is required to successfully verify the domain.
- **DNS propagation delays**: DNS changes can take time to update across the internet. If you think this might be the problem, we recommend waiting a while and checking back later.
- **Incorrect record types or values**: Ensure the provided values exactly match what’s required. Even a small typo can interrupt the process. Figma will display an  error icon if one or both of the records can’t be verified.
- **Conflicting DNS settings**: Check for duplicate or conflicting entries in your DNS settings—for instance, multiple CNAME records for the same subdomain.
- **Conflicting AAAA record on apex domain**: If you're connecting an apex domain—like `example.com`—using an A record, check whether there’s an existing AAAA (IPv6) record on the same host (`@`). Having both can prevent your domain from connecting properly. Remove the AAAA record from your DNS settings and try again.
- **Awaiting SSL certificates**: Figma automatically provisions SSL certificates for custom domains, which ensures secure HTTPS access. This process typically takes up to 15 minutes, but can sometimes require additional time. If you're still waiting after 30 minutes, we recommend checking if you have any CAA (Certificate Authority Authorization) DNS records configured for your domain. If so, make sure they allow certificates from Google Trust Services, Let's Encrypt, and SSL.com.

## Add or remove a redirect between your apex domain and www subdomain

You can only add or remove a redirect only if you're using an apex domain or a `www` subdomain.

Add a redirect
Remove a redirect

If you didn’t set up a redirect when adding your custom domain—or if your
`www` subdomain was added before Figma supported apex domains—you
can still add one:

1. From a site file, click 
   **Settings** in the left navigation bar.
2. In the **Site** section, click
   **Domains**.
3. Click  **More**
   next to your custom domain and choose
   **Add redirect from apex domain**.
4. A new DNS record will appear. Add this to your domain provider’s DNS
   records.
5. Return to the **Domains** page in Figma and click
    **Refresh**.

You can remove an existing redirect between your apex domain and
`www` subdomain. Once removed, users won’t be able to access your
site at the domain that was being redirected.

1. From a site file, click 
   **Settings** in the left navigation bar.
2. In the **Site** section, click
   **Domains**.
3. Click the 
   **More** next to your custom domain and choose
   **Remove redirect**.

## Disconnect a custom domain from your site

You can disconnect your custom domain at any time. Your site will remain accessible on the public web at the auto-generated `figma.site` subdomain.

1. From a sites file, click  **Settings** in the left navigation bar.
2. In the **Site** section, click **Domains.**
3. Click the  **More** menu.
4. Select **Remove connected domain**.

**Tip**: To completely remove your site from the web, you’ll need to [unpublish it](https://help.figma.com/hc/en-us/articles/31242845959703).

## Frequently asked questions

**Can a site have more than one custom domain?**

Today, a site can only use one custom domain at a time.

**Does Figma support wildcard domains?**

A wildcard domain uses an asterisk (\*) to match any subdomain of a given domain. For example, \*.example.com will cover requests for [blog.example.com](http://blog.example.com), [shop.example.com](http://shop.example.com), or any other subdomain. Figma doesn’t currently support wildcard domains; each site file can only be tied to a single subdomain.

**Can I use a domain path to point to my Figma site?**

Figma currently only supports the root of the domain or subdomain you configure. Specifying a domain path—like [www.example.com/about](https://www.example.com/about)—isn't supported.
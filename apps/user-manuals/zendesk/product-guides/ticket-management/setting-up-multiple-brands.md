# Setting up multiple brands

Source: https://support.zendesk.com/hc/en-us/articles/4408829476378-Setting-up-multiple-brands

---

Brand is also a ticket value added to all your tickets. Agents can manually change the brand associated with a ticket, and they search for tickets by brand. Agents can view, search, and access tickets within their brands only, defined by theirbrand membership. Admins have access to all tickets for all brands.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Account > Brand management > Brands

Note: This feature has the following plan restrictions:

- Suite Growth and Professional includes up to five brands.
- Suite Enterprise and Enterprise Plus includes up to 300 brands.
- Support Enterprise includes up to five brands.

Brand is a customer facing identity, represented by a collection of contact points for your customers. These contact points can include email support addresses, help center, voice, messaging Web Widget or Web Widget (Classic), X (formerly Twitter), and Facebook.

Brand is also a ticket value added to all your tickets. Agents can manually change the brand associated with a ticket, and they search for tickets by brand. Agents can view, search, and access tickets within their brands only, defined by their [brand membership](https://support.zendesk.com/hc/en-us/articles/7584022494874). Admins have access to all tickets for all brands.

You can also use brands in business rules, including macros, views, triggers, and automations, as well as in Explore and Insights reporting.

All Zendesk Suite and Support plans have one brand by default, which is created when you set up your Zendesk account. This is also true for Employee Service Suite Team plans. However, [Employee Service Suite Growth plans and above](https://support.zendesk.com/hc/en-us/articles/9012803758362) have three brands by default: one that represents the company as a whole (Support), one for HR, and one for IT. Depending on your plan type, you might be able to create additional brands.

You must be an administrator to add and manage brands.

This article contains the following sections:

- [Understanding how Multibrand works in your account](#topic_hyq_l1v_cr)
- [Adding multiple brands](#topic_bp3_gby_wp)
- [Generating an SSL certificate for host-mapped brands](#topic_m2b_fgq_ft)
- [Excluding your branded help centers from system generated account emails](#topic_4bt_fgq_ft)
- [Next step after you add a brand: Configure your channels to support multiple brands](#topic_gmf_z23_dr)

For a list of resources, see [Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306).

## Understanding how Multibrand works in your account

When your account is created, one brand is created for you by default.
So, before you add any brands, you have a single *account subdomain* and one *brand subdomain* that match. When you add brands, you still have a single account subdomain, but you have *multiple brand subdomains*, including your original brand that matches your account subdomain.

When you have multiple brands, one is always assigned as the *default brand*. This is the brand associated with your default help center, and is applied in any situation where another specific brand is not indicated. The default brand cannot be deleted or deactivated until another brand is made the default. The default brand is identified as (Default) on your brands list.

You can also define an *agent brand*, or *agent route*, which is essentially the default brand for agents. Meaning, the agent brand is the brand that agents are routed to when they sign in to Zendesk. The agent brand cannot be deleted or deactivated until another brand is made the agent route. It is identified as (Agent)
on your brands list. The agent brand is also the brand retained if you downgrade to a single-brand plan. For more information, see [Changing your agent brand](https://support.zendesk.com/hc/en-us/articles/4408826557082-Editing-brands#topic_bqs_lns_x4b).

Note: Currently, you cannot change the subdomain of your original brand without also changing your account subdomain.

Brand is a ticket value. Every ticket has a brand. Agents can view, search, and access tickets within their brands only, defined by their [brand membership](https://support.zendesk.com/hc/en-us/articles/7584022494874).
Admins have access to all tickets for all brands. End users and organizations do not have a brand value. They belong to the account, not a brand. You cannot segment end users or orgs by brand. End users can access their requests in each brand's help center.
Depending on the account [configuration](https://support.zendesk.com/hc/en-us/articles/9319604460826), the list of an end user's requests is either restricted to the help center's brand or reflects all of their requests for all brands.

Most channels have a brand value, so that you can configure specific channels for specific brands. This includes help center, voice, messaging Web Widget, Web Widget (Classic), X (formerly Twitter), and Facebook.

## Creating multiple brands

You have one brand for your account by default, but you can set up a number of brands, depending on your plan type:

- Suite Growth and Professional includes up to five brands.
- Suite Enterprise and Enterprise Plus includes up to 300 brands.
- Support Enterprise includes up to five brands.

Brands are created and managed on the Brands page in Admin Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_brands_page_general.png)

**To add a brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click **Create brand**.

   If this is the first time you are adding a brand, click **Get started** instead.
3. Enter a brand **Name**.

   Brand name is required and must be a unique name, not used by any of your other brands. This name will be customer-facing.
4. Enter a **Subdomain** for this brand's help center.

   This subdomain will be the address (URL) for this brand's help center:
   *yoursubdomain*.zendesk.com/hc. It will also be the default support address for this brand:
   support@*yoursubdomain*.zendesk.com.

   Subdomain is required; each brand has its own subdomain. It can include only letters A-Z, numbers 0-9, and dashes (-).
   When you enter a subdomain you'll see an indication of whether that subdomain is available or already taken.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multibrand_enter_subdomain.png)
5. (Optional) Add a **Logo** by dragging your file to or clicking within the designated logo area.

   Your logo should be 2 MB or less and must be a PNG, JPG, JPEG, or GIF file. For best results, your logo should be square. Otherwise, your logo will be stretched or compressed to fit.
6. (Optional) Enter a brand signature to append your agent's personal email signature when they are representing that brand. For information on agent signatures, see [Adding an agent signature to ticket email notifications](https://support.zendesk.com/hc/en-us/articles/4408822471322#multibrands).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/brand_signature.png)
7. (Optional) Enter an alternative support site URL in **Host mapping** to map one of your own domain names to the help center for this brand. For example, you might use support.*yoursubdomain*.com/hc instead of *yoursubdomain*.zendesk.com/hc.

   When you enter your host mapped URL it is automatically tested, and you'll see notification that your host mapping is either working or not working.

   Note: There are multiple steps required to set up host mapping for a brand, including generating an updated SSL certificate every time you add one or more brands. For more information, see [Generating an SSL certificate for host-mapped brands](#topic_m2b_fgq_ft).

   After you add multiple brands, host mapping is managed in **Manage > Brands** instead of **Settings > Account**.
8. Click **Save**.

   Your new brand is created.
9. Under **Who has access**, click **Manage brand membership** to [add team members to the brand](https://support.zendesk.com/hc/en-us/articles/7584022494874#topic_p4k_grx_xbc).

   All admins are added to the brand, can access all tickets within the brand, and cannot be removed from the brand. Team members cannot view, search, or access tickets with the new brand until you add them to the brand.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_brands_who_has_access.png)

Your new brand will not be available to end users until you add a help center or associate it with another channel (see [Configuring your channels to support multiple brands](https://support.zendesk.com/hc/en-us/articles/4408836507162)).

To manage your brands, see [Managing multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829486362). To start using and supporting your new brand, see the next section [Next steps after you add a new brand](#topic_gmf_z23_dr).

## Generating an SSL certificate for host-mapped brands

When you add a host mapped brand, you need to regenerate your SSL certificate. If you do not regenerate your certificate, host mapping will work, but the brand will not be protected.

Note: If you did not previously have host mapping set up, skip this section and go through the entire host mapping process. See [Changing the address of your help center subdomain (host mapping)](https://support.zendesk.com/hc/en-us/articles/4408838571930).

You need to regenerate your SSL certificate every time you add *one or more* host mapped brands, but you do not need to regenerate your certificate for *every* host mapped brand. For example, if you add three new brands, you need to regenerate your certificate only once. If you later add two more brands, you need to regenerate your certificate again.

Your certificate request should be formatted as a SAN (SubjectAltName)
cert. This type of certificate is used to manage multiple SSL-protected host mapped domains. Each brand subdomain is listed in the certificate as a SAN.

To regenerate your SSL certificate when you add one or more host mapped brands, see [Setting up a hosted SSL](https://support.zendesk.com/hc/en-us/articles/4408838571930#topic_dyr_bqk_j4b).

## Excluding your branded help centers from system generated account emails

By default, when you have multiple brands with active help centers, a list of all your active branded help centers are included in account emails. Account emails are system-generated emails that notify agents and end users about their profile, including welcome emails, account verification emails, and password reset emails.

If you do not want to include a list of your active branded help centers in account emails, you can exclude it.

**To exclude the list of active branded help centers from account emails to agents and end users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. Beside **Account emails**, deselect **Include a list of active help centers in account emails**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multibrand_HCs_in_account_emails.png)
3. Click **Save tab**.

## Next step after you add a brand: Configure your channels to support multiple brands

When you add multiple brands, you must add a help center or associate another channel with each brand before your customers can open requests with a specific brand.

**Resources to help you configure your channels to support multiple brands**

You can support your brands in any of these channels: email, help center, voice, messaging Web Widget, and Web Widget (Classic). See the following resources:

- [Adding email support addresses for multiple brands](https://support.zendesk.com/hc/en-us/articles/4408836507162)
- [Creating a help center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408828794778)
- [Adding Web Widgets (Classic) for multiple brands](https://support.zendesk.com/hc/en-us/articles/4408828483738)
- [Setting up Zendesk phone numbers for multiple brands](https://support.zendesk.com/hc/en-us/articles/4408821946138)

Social and third-party messaging channels (such as Facebook, Instagram, WeChat, and Slack) also support multiple brands. See our [Third-party and social messaging channels](https://support.zendesk.com/hc/en-us/sections/4405298883482) page for helpful resources.

**Other possible next steps after you add a brand and configure your channels**

- [Restricting agent ticket access by brand](https://support.zendesk.com/hc/en-us/articles/7584022494874)
- [Using the email template with multiple brands](https://support.zendesk.com/hc/en-us/articles/4408832356762)
- [Setting up business rules for multiple brands](https://support.zendesk.com/hc/en-us/articles/4408842973338)
- [Setting up views to sort your branded tickets](https://support.zendesk.com/hc/en-us/articles/4408838983322)
- [Configuring the visibility of service requests across brands](https://support.zendesk.com/hc/en-us/articles/9319604460826)

For a list of resources, see [Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306).
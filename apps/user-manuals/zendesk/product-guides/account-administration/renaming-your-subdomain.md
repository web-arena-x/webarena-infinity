# Renaming your subdomain

Source: https://support.zendesk.com/hc/en-us/articles/4408845973914-Renaming-your-subdomain

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

To rename your subdomain, ensure you're the account owner. Consider alternatives like host mapping before proceeding. Renaming affects URLs, email addresses, and integrations like Jira and Salesforce. Update email forwarding, CNAME, SSL, and integrations before and after the change. Be aware of potential service disruptions and update all related configurations to maintain functionality.

You must be the account owner to rename a [subdomain](https://support.zendesk.com/hc/en-us/articles/4408883411354#topic_swn_h2f_3xb). If you aren't the account owner,
you can [find the account owner](https://support.zendesk.com/hc/en-us/articles/4408822084634#topic_xkh_3lm_ygb) and request they make
the change. You cannot rename the subdomain of a sandbox account.

Zendesk can't change your account's subdomain for you. If you can't find the account
owner, work with your IT administrators. If you can’t resolve this, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to initiate a security review.

Renaming your subdomain takes effect immediately. Your Zendesk account will no longer be
at your old URL, and Zendesk cannot set up a redirect on your behalf. Consider your
entire workflow before making this change.

Warning: Renaming your subdomain (*mycompany.*zendesk.com) actually
changes the address of your account. Be sure you read and understand the [Important considerations before renaming
your subdomain](#topic_vcg_jvs_nvb).

This article covers the following considerations and updates you will need to make:

- [Important considerations before
  renaming your subdomain](#topic_vcg_jvs_nvb)
- [Step 1: Tasks before renaming your
  subdomain](#topic_ahm_lws_nvb)
- [Step 2: Rename your
  subdomain](#topic_m5k_pzs_nvb)
- [Step 3: Tasks after renaming your
  subdomain](#topic_gwv_qpt_nvb)

## Important considerations before renaming your subdomain

Before you rename your subdomain, consider simply changing your [account name](https://support.zendesk.com/hc/en-us/articles/4408842817434#topic_j34_xj2_4nb) or setting up [host mapping](https://support.zendesk.com/hc/en-us/articles/4408838571930) as alternatives instead.

Host mapping (purchasing another domain that points to your Zendesk) is highly
recommended as an alternative to renaming your subdomain. This enables you to change
the URL that your customers see when accessing your help center without having to
change the actual address of your agent interface or Zendesk account. See [Changing the URL of your help center](https://support.zendesk.com/hc/en-us/articles/4408838571930).

If you want to proceed with renaming your subdomain, make sure you understand the
following important considerations:

- Renaming your subdomain takes effect immediately, so it’s recommended to
  make the change during low-volume hours or after your business hours because
  some functionality is affected.
- Renaming your subdomain changes the URL of your help center (for example,
  *myoldsubdomain.*zendesk.com/hc to
  *mynewsubdomain.*zendesk.com/hc). You may need to update links or
  bookmarks referencing the old help center URL to ensure users can access the
  correct site. Additionally, you should communicate this change to your
  customers to avoid confusion.
- If you rename your Zendesk subdomain, any Zendesk support email addresses
  that are based on your old subdomain will automatically update to reflect
  your new subdomain. For example, if your previous subdomain was
  *myoldsubdomain* and you renamed it to *mynewsubdomain*, any
  support addresses like support@*myoldsubdomain*.zendesk.com would
  change to support@*mynewsubdomain*.zendesk.com.
- There may be a delay of several hours before you can add new native support
  addresses. When [adding a support address](https://support.zendesk.com/hc/en-us/articles/4408842868506#topic_wg1_1zk_zm), check
  that the new subdomain appears on the "Create a new support address" form.
  If the old subdomain appears, check back again in a few hours.
- Chat may be inaccessible for up to 2 hours after changing your subdomain. We
  highly recommend you change your subdomain after hours.
- If you use Sunshine Conversations through the Agent Workspace and want to
  change your subdomain, you must delete and then recreate your Sunshine
  Conversations integrations. We recommend using [host-mapped domains](https://support.zendesk.com/hc/en-us/articles/4408838571930) instead of
  changing a subdomain. Note that changing your subdomain will halt all
  Zendesk bot and autoreply activity. If you want to continue your Zendesk bot
  activity, don't change your subdomain.
- Customers using the [Authenticated SMTP Connector](https://support.zendesk.com/hc/en-us/articles/7189260823194) will
  need to deprecate their usage before renaming their subdomain, then re-add
  their configuration once the subdomain change is complete, as this feature
  is subdomain-specific and will not automatically
  update.
- Access to many early access programs (EAPs) is controlled by the account
  subdomain. If you change your subdomain, you will lose access to any EAPs
  controlled in this manner. You must sign up again for those EAPs with your
  new subdomain.
- After you change your domain, you cannot copy and paste comments (internal
  or public) or images from a ticket created in the old domain. Doing so
  results in broken images and incomplete comments. You must recreate comments
  or re-upload the image attachments directly into the ticket in the new
  domain.

## Step 1: Tasks before renaming your subdomain

Before renaming your subdomain, you should update the following items:

- [Email forwarding from external
  addresses](#topic_plc_2cw_c1c)
- [CNAME, host maps, and
  SSL](#topic_vfx_sws_nvb)
- [Jira integration](#topic_u1m_cxs_nvb)
- [Salesforce integration](#topic_t3q_nwz_c3c)

### Email forwarding from external addresses

You need to update any [email forwarding](https://support.zendesk.com/hc/en-us/articles/4408886828698-Using-an-external-email-domain) to point to your new
support address and URL in sync with renaming your subdomain to avoid missing
any incoming tickets. This includes the wildcard email option (see [Accepting wildcard email addresses for
support requests](https://support.zendesk.com/hc/en-us/articles/5318946039578)). You should "flip the switch" during a slow period
to be sure you have time to get everything in order.

Things to consider:

- You are responsible for migrating external addresses. Zendesk cannot migrate
  external addresses automatically.
- Ensure all your external addresses route to the new subdomain, and remove
  all routing rules for the old subdomain.
- If you forward email from multiple external addresses to multiple Zendesk
  addresses, you must temporarily consolidate email traffic under your default
  support address (support@*new\_subdomain*.zendesk.com) or enable
  wildcards. Although it may take several hours before you can add new native
  support addresses using the new domain, the default
  support@*new\_subdomain*.zendesk.com address is available right
  away.

### CNAME, host maps, and SSL

Update any [host mapping](https://support.zendesk.com/hc/en-us/articles/4408838571930-Changing-the-address-of-your-support-website-on-Zendesk-host-mapping-) to point to your new
support address and URL. Ensure that any CNAME changes and certificate updates
are done with your customer service team before changing your subdomain. You
must add a new CNAME for your new Zendesk subdomain with a new hostmap URL.
Additionally, you'll need to set up a redirect from your old hostmap to your new
one. This can take time to set up.

You can obtain a new SSL certificate by grabbing a Certificate Signing Request
and then uploading the new certificate to Zendesk Support. You must install a
new SSL certificate that covers the changed host mapped URL. For more
information, see [Replacing a
certificate](4408845973914).

### Jira integration

If you've connected the [Jira integration](https://support.zendesk.com/hc/en-us/articles/4408837969946), update your Jira
settings before changing your subdomain.

**To update Jira with a new subdomain**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Channel
   apps**.
2. Disable the Jira app.
3. Rename your subdomain.
4. Enable the connector again in Jira.
5. Select the **Configure** option in the connector setup.
6. On the next screen, click on **Complete set-up** to install the
   App.
7. Follow the on-screen instructions.
8. Go back to Zendesk Support and check to see if the Jira app loads
   properly.

Your linked tickets/issues with Zendesk Support and Jira will not be lost in this
process; we're just re-authorizing the Zendesk app.

You might have to update your other apps as well if you used OAuth credentials
tied to your old subdomain.

### Salesforce integration

[Disconnect the Salesforce integration](https://support.zendesk.com/hc/en-us/articles/4408821555482#topic_rmq_jkt_sjb)
before renaming your subdomain.

## Step 2: Rename your subdomain

You must be the account owner to rename a subdomain. If you aren't the account owner,
you can [find the account owner](https://support.zendesk.com/hc/en-us/articles/4408822084634#topic_xkh_3lm_ygb) and request that
they make the change.

Zendesk can't change your account's subdomain for you. If you can't find the account
owner, work with your IT administrators. If you can’t resolve this, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to initiate a security
review.

Not everything changes when you update your subdomain. All your existing users,
tickets, organizations, and groups will automatically exist at your new URL.
Additionally, your triggers and automations will be all set. While your users will
need to sign in again to your new Zendesk location, their profiles and ticket
histories will still be intact.

Be sure to complete the tasks in [Step 3: Tasks after renaming your subdomain](#topic_gwv_qpt_nvb)
after you change your subdomain.

Note: When you rename your subdomain, you must choose a name that contains between 3 and
63 characters. You can't use underscores (\_) or other special characters as part of
the name. It can include only letters A-Z, numbers 0-9, and dashes (-).

**To rename a subdomain**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Appearance > Branding**.
2. In the Subdomain section, click **Brands menu**.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the brand with the subdomain you'd like to
   rename, then click **Edit**.
4. In the Subdomain field, type the new subdomain.
5. Click **Save**.
6. Review the consequences of changing your subdomain, then click **Yes, change
   subdomain**.

## Step 3: Tasks after renaming your subdomain

After renaming your subdomain, you should update the following items:

- [Ticket sharing
  agreements](#topic_d5b_cvt_nvb)
- [CSAT representation/ Web Widget
  (Classic)](#topic_cnb_jvt_nvb)
- [Ticket replies](#topic_htt_vwt_nvb)
- [Mobile SDK](#topic_jbs_kxt_nvb)
- [Voice](#topic_xvy_sxt_nvb)
- [API tokens/credentials](#topic_wc4_vxt_nvb)
- [Single sign-on](#topic_qjq_1yt_nvb)
- [Messaging](#topic_o2x_ksl_k1c)
- [Chat](#topic_kpb_2yt_nvb)
- [Workforce manangement](#topic_mcb_xjq_1cc)
- [Status notifications](#topic_k5l_3yt_nvb)
- [Reporting](#topic_tdq_kyt_nvb)
- [Salesforce integration](#topic_abz_vwz_c3c)

### Ticket sharing agreements

If you have any active [ticket sharing agreements](https://support.zendesk.com/hc/en-us/articles/4408893967514-Sharing-tickets-with-other-Zendesk-accounts), you'll need
to deactivate and recreate them after changing your subdomain. This includes any
receiving ticket sharing agreements, which means that you'll also need the
admins of those Zendesk accounts to recreate your sharing agreements to update
the location of your Zendesk account.

Sharing on individual tickets will also no longer work. After you rename your
subdomain and update your sharing agreements, you'll have to manually update all
shared tickets to reflect the new sharing agreement.

### CSAT representation/ Web Widget (Classic)

If you are using one or more instances of [Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408836216218), you must update
them after changing your subdomain. You will also need to update your jQuery if
you have made modifications to your CSAT representation. For more information on
updating your satisfaction ratings in JSON format, see [Displaying your last 100 satisfaction
ratings](https://support.zendesk.com/hc/en-us/articles/4408894103706).

You must update your widgets for your help center and website individually after
you have changed your subdomain name.

**To update Web Widget (Classic):**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Setup tab**, if it is not already selected.
3. Under the code box, click **Copy to clipboard**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_admin_copy_to_clipboard.png)
4. To edit your widget on your website, go to the web page where you want
   to add the widget, then paste the updated code before closing HTML
   </HEAD> tag. You need to add the code to every webpage where you
   want to update the widget.

**To update your help center widget:**

1. In help center, click **Customize design** in the tools panel, then
   click **edit them**.
2. Select the **Header** template from the drop-down.
3. Delete any existing help center widget code you have.
4. Paste the updated code before the </HEADER> ; tag.
5. Click **save**, then click **Publish changes**.

For more information on updating your widgets see, [Using Web Widget (Classic) to embed customer
service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218#topic_pp3_pgd_bq).

### Ticket replies

If you use email notifications, customer replies to ticket notifications sent
prior to the subdomain change will not be received in your account or added as
updates to those tickets. All ticket URLs sent in email notifications prior to
the subdomain change will now also be invalid. To correct this, update all of
these with a public comment after changing your subdomain.

Start by creating a view of all the unsolved tickets in your instance of Zendesk
Support. If you haven't done too much customization, you might already have this
native view active in your account.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/subdomain1.png)

From this view, you can mass edit all your tickets with whatever comment you
like. The new reply to email address will now be valid, and if you use the
{{ticket.URL}} placeholder, it will populate with the updated ticket URL.

Note: You cannot open attachments or view inline images in tickets that existed
before the subdomain rename. Contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to have
inline images fixed. Image links copied and pasted from other sources cannot be
fixed. Attachments cannot be retrieved.

### Mobile SDK

You will need to update the code on your Mobile SDK, so it will point to the
correct Zendesk URL after you've updated your subdomain.

**To update your Mobile SDK:**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Mobile SDK**.
2. Locate the code snippet with your subdomain in your Android and iOS
   code.
3. Give your developer the updated code snippets.

### Voice

If you experience issues with voice support talk after changing your subdomain,
contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

### API authentication

If you are using [Zendesk API](https://developer.zendesk.com/rest_api/docs/core/introduction) to fetch or send data in
your account, make sure to update the subdomain you are pointing to so the API
call doesn’t fail.

Example:

```
https://{OLDsubdomain}.zendesk.com/api/v2/tickets.json \ -v -u {email_address}:{password}
https://{NEWsubdomain}.zendesk.com/api/v2/tickets.json \ -v -u {email_address}:{password}
```

Also, if your email address or your agents' email addresses changed, you might
need to update your API tokens or credentials. For more information, see [Managing access to the Zendesk
API](https://support.zendesk.com/hc/en-us/articles/4408889192858).

### Single sign-on

Both SAML and JWT pass the SSO request to Zendesk Access Consumer URL, which
references your account subdomain. You cannot sign in via SSO until you update
the subdomain.

For information on setting up SSO, see [Using SAML for single sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690) and
[Setting up single sign-on with JWT (JSON Web
Token)](https://support.zendesk.com/hc/en-us/articles/4408845838874-Setting-up-single-sign-on-with-JWT-JSON-Web-Token-).

### Messaging

When you change your subdomain, a new messaging Web Widget script is generated.
You must update all pages of your site/application to use the new script.
See [Installing the Web Widget on a
website](https://support.zendesk.com/hc/en-us/articles/4500748175258#topic_fqh_qtc_3rb).

### Chat

If you originally purchased Chat separately then later linked your Chat account
with your Support account, your Chat account will fail to create tickets. You
will need to contact our customer service team to make changes.

If you purchased Zendesk Chat and Zendesk Support together, updates occur
automatically, and no action is required.

### Workforce management (WFM)

When you rename your Zendesk subdomain, rename your subdomain on Zendesk WFM to
ensure the accounts match and your historical data and settings are intact.

Warning: If you have renamed the subdomain on the Zendesk side, and you
have not updated it on Zendesk WFM yet, the app on the top right of Zendesk
displays a Complete installation message. Do not continue with the new
installation, as it will create a new Zendesk WFM account.

**To rename your Zendesk WFM subdomain**

1. Once you have renamed your Zendesk subdomain, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) with your
   previous Zendesk subdomain and your new renamed subdomain.
2. Zendesk will update your subdomain and invite you to reauthorize the
   account.

### Status notifications

If you [subscribed](https://support.zendesk.com/hc/en-us/articles/4408821424666) to Zendesk status
notifications, update your subscription with your new subdomain.

### Reporting

You may see some delayed (or missed) [scheduled dashboard deliveries](https://support.zendesk.com/hc/en-us/articles/4408843602714) while
your account re-synchronizes with Explore.

### Salesforce integration

Reconnect the Salesforce integration. See [Connecting Salesforce to Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821555482#topic_vmn_vkc_rlb).
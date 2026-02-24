# Sharing Explore dashboards outside Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408826905626-Sharing-Explore-dashboards-outside-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Enterprise |

Note: Customers on the Explore Legacy plan can also share external
links to dashboards. See [About the Explore Legacy plan](https://support.zendesk.com/hc/en-us/articles/4408823356186#topic_pf2_35r_smb).

You can share a link to a dashboard with external users who do not have a Zendesk
account. The link can also be used to display the dashboard on a television or monitor.
Users will have view-only access to the dashboard with the following security
measures:

- Interaction options are disabled when you share dashboards externally. For details
  about interaction options, see [Interacting with dashboards](https://support.zendesk.com/hc/en-us/articles/4408834682778) and [Interacting with reports](https://support.zendesk.com/hc/en-us/articles/4408829009818).
- Any IP restrictions configured in your Zendesk instance will be enforced and links
  will only be accessible from that IP range. For details about IP restrictions, see
  [Restricting access to Zendesk Support and your
  Help Center using IP restrictions](https://support.zendesk.com/hc/en-us/articles/4408894156186).
- When sharing a dashboard outside Zendesk, all data returned by the dashboard is
  available to viewers. [Dashboard restrictions](https://support.zendesk.com/hc/en-us/articles/5282695803290) still apply, but users with [Limited viewer and Limited editor permissions](https://support.zendesk.com/hc/en-us/articles/4408836002970) will be
  able to see data outside of their permissions.

Important: Public links can be accessed by anyone on the internet,
regardless of whether they have a Zendesk account. Always consider protecting your
dashboards with a strong password. Record the password and store it securely in
accordance with your organization's security policies. Additionally, always review
the content of any dashboards you share externally to ensure that sensitive data is
not leaked.

This article contains the following topics:

- [Turning on external link sharing](#topic_j5z_fvx_5mb)
- [Sharing an external link to a dashboard](#topic_f4w_gvx_5mb)
- [Disabling external link sharing](#topic_i1x_tm3_f1c)

## Turning on external link sharing

Before you can start sharing external links, an admin must turn this on from the
Explore admin menu.

**To turn on external link sharing**

1. In Explore, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) in the left sidebar.
2. Select the **Sharing** tab.
3. Turn on the **Public links to dashboards** setting.
4. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_sharing_public_links_to_dashboards_setting.png)

You can now create public links to dashboards.

## Sharing an external link to a dashboard

Now that you've enabled sharing dashboard sharing, you can start creating and sharing
links.

Note: Currently, you cannot share the [prebuilt live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546) as an external
link to users outside of your Zendesk account.

**To share a dashboard externally**

1. From an open dashboard or a dashboard in preview mode, click **Share**, then
   select \*\*Get link\*\*.

   ![Explore sharing menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_sharing_554.png)

   The Get link page opens.
2. Click **Create link**.
3. On the Create link page, configure the following:
   - **Access type:** Select any [dashboard restrictions](https://support.zendesk.com/hc/en-us/articles/5282695803290) that
     will apply to the shared dashboard.
   - **Protect with password:** (Recommended) Enter a password that end
     users must enter to access the dashboard. The password must have at
     least:
     - 10 characters
     - 1 uppercase character
     - 1 lowercase character
     - 1 number
     - 1 symbol

     Important: Make sure to save the password. Once you've
     created the link, you'll no longer be able to access it.

     If you don't want to password-protect the dashboard, deselect the
     **Protect with password** checkbox (not recommended).
   - Click **Create link**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_getlink_1.png)

   The Get link page opens,
   showing your new link. From here, you can reset or remove the password, or
   delete the link.
4. Inform the required users of the link to the dashboard and the password.

   Important: If a user attempts to access a
   password-protected dashboard and enters an incorrect password five
   times, the dashboard becomes inaccessible for all users for five
   minutes.

## Disabling external link sharing

You can turn off external link sharing at any time. This is especially useful in
situations where you suspect that one or more dashboards with sensitive data have
been inappropriately shared externally.

When you turn off external link sharing, any existing shared links are disabled. If
you decide to [re-enable external link sharing](https://support.zendesk.com/hc/en-us/articles/4408826905626#topic_j5z_fvx_5mb), you will
need to [create new external links](https://support.zendesk.com/hc/en-us/articles/4408826905626#topic_f4w_gvx_5mb) for any
dashboards you want to share.

**To disable external link sharing**

1. In Explore, open the **Admin** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) in the left panel, then select **Dashboard
   sharing permissions** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ent_dash_share_1.png)).
2. On the **Dashboard sharing permissions** page, deselect **Enable creating
   public links to dashboards**.
3. Click **Save**.
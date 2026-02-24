# Managing your support addresses

Source: https://support.zendesk.com/hc/en-us/articles/5279521301914-Managing-your-support-addresses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Manage your support addresses to streamline customer interactions. Set a default email for notifications, remove unnecessary addresses, or edit names and brands. Remember, the default system address can’t be deleted, and changes require verification. If you have over 3000 addresses, use the API for management. Keep your support channels organized and responsive to enhance customer service.

As described in [Understanding the default email setup in
Zendesk](https://support.zendesk.com/hc/en-us/articles/5612728377754), one support email address is initially set up for users to submit
tickets: support@*yoursubdomain*.zendesk.com. This is the default email address for
submitting tickets and can’t be removed.

If you [created additional support email addresses](https://support.zendesk.com/hc/en-us/articles/4408842868506),
you can manage your email addresses if necessary. For example, you might need to change
the default address, remove an address that’s no longer needed, or edit the name of an
address.

Note: Support addresses are not visible in Admin
Center > Email > Manage support addresses if you have a very large number of
support addresses (3000+). If you see a message that support addresses are hidden,
you must manage them using the [Zendesk API](https://developer.zendesk.com/api-reference/ticketing/account-configuration/support_addresses/).

This article covers the following topics:

- [Setting a default support
  address](#topic_btc_h1f_bwb)
- [Removing a support
  address](#topic_hl1_5z2_bwb)
- [Editing the name and brand of a support address](#topic_ahs_l1f_bwb)

Related articles:

- [Understanding the support address end-user
  experience](https://support.zendesk.com/hc/en-us/articles/5000599601050)
- [Adding support email addresses for users to
  submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506)

## Setting a default support address

When you created your Zendesk account, one email address was set up for you:
support@*yoursubdomain*.zendesk.com. This system support address is used as
your default support address, unless you change the default.

Your default support address is used as the sending address for notifications when a
ticket is created manually, when a ticket is sent directly to your default support
address, or when a ticket is created through a channel other than email.

Additionally, the default support address is used as the Reply From address in
replies to users when you [have the wildcard emails option enabled](https://support.zendesk.com/hc/en-us/articles/5318946039578),
and an end user sends email to an address that is *not* a known support
address.

You can change the default support address at any time. The option to make a support
address the default will only appear if the address has been verified (see [Adding support
addresses](https://support.zendesk.com/hc/en-us/articles/4408842868506#topic_wg1_1zk_zm)).

**To change your default support address**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the support address you want to make
   the default, then click **Make default**.

   The **Default** label
   appears beside your new default address, and that address moves up under
   your system support address in your support addresses list.

## Removing a support address

You can remove any support address except the original system support address
(support@*yoursubdomain*.zendesk.com) or your current default support
address. If you selected another support address as your default (other than your
system support address), you can delete that support address if you make another
support address the default first.

If you connect to Gmail, you can disconnect from a Gmail account anytime to stop
importing emails from that inbox. See [Managing Gmail connections](https://support.zendesk.com/hc/en-us/articles/4408835030426#topic_oww_k1h_v5).

When you delete a support address, outgoing email notifications will no longer be
sent from that address. Any tickets using the deleted support address will be given
to the default address.

**To delete a support address**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the support address you want to
   delete, then click **Delete**.
4. In the confirmation window, click **Delete support address**.

   The
   support address is removed from your list.

## Editing the name and brand of a support address

You can edit the name of an existing support address, but you cannot edit the email
address for an existing support address. If you need to edit the email address
itself, delete the support address and add it again.

If you're editing an external support address, you can also update the brand
associated with the address.

**To edit a support address name**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the support address you want to
   rename, then click **Edit**.
4. In the Name field, add, change, or remove the support address name.
5. (External support addresses only) In the Brand field, change the brand
   associated with the address if needed by selecting a different brand from
   the drop-down list.
6. Click **Save**.

   The updates to your address appear in the support
   addresses list.
# Editing brand settings

Source: https://support.zendesk.com/hc/en-us/articles/4408826557082-Editing-brand-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Edit brand settings to manage multiple brands effectively. Change default and agent brands to control help center associations and agent routing. Require agents to select a brand before saving tickets to ensure proper ticket management. On Enterprise plans, manage brand memberships to control team members' access to tickets. Adjust settings for new team members to assign brand access appropriately.

If you have [created multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), your brands appear
alphabetically on the Brands page, except for the default brand, which always appears last.
You cannot reorder your brands on this page.

You can edit your existing brands and brand settings as needed. You can also change your
default brand and your agent brand if necessary.

The *default brand* is associated with your default help center and is applied when a
specific brand is not indicated. The *agent brand* is the brand that agents are routed to
when they sign in to Zendesk. The default and agent brands are typically the same but can be
different.

Note: If you see a warning icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multibrand_ssl_warning_icon.png)) beside one of your brands, SSL is not working for that brand. To
fix it, click the icon, then click **Edit SSL settings**.

For information about deactivating and deleting brands, see [Deactivating and deleting brands](https://support.zendesk.com/hc/en-us/articles/4408829486362). For a list of other resources, see
[Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306).

This article contains the following sections:

- [Editing a brand](#topic_awp_xms_x4b)
- [Changing your default brand](#topic_vnh_yms_x4b)
- [Changing your agent brand](#topic_bqs_lns_x4b)
- [Requiring agents to select a brand before saving tickets](#topic_vrf_w1v_sgc)
- [Editing brand membership settings (Enterprise plans only)](#topic_hmj_245_ngc)

## Editing a brand

You can edit your existing brands, including brand settings. Customers on Enterprise plans
and above can also edit brand memberships.

Adding or removing team members from a brand impacts their access to tickets. For more
information, see [Restricting agent ticket access by brand](https://support.zendesk.com/hc/en-us/articles/7584022494874).

**To edit a brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click the menu icon beside the brand that you want to edit, then select
   **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multibrand_edit_brand.png)

   The brand
   expands to show all of the settings for that brand.
3. Make changes to the fields as needed.
4. Click **Save changes**.

**To edit brand members (Enterprise plans and above)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click the brand name in the list.

   The Who has access page displays.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_brands_who_has_access.png)
3. Click **Manage brand membership**.
4. Select the team members to add or remove from the brand, then click the **Manage brand
   membership** link at the bottom of the page.
5. Select the brands from which to add or remove team members, then click **Save**.

## Changing your default brand

The *default brand* is the brand associated with your default help center and is
applied when a specific brand is not indicated.

The default brand is identified as (Default) on your brands list. You must be an admin to
change the default brand. The default brand cannot be deleted or deactivated unless it is
replaced as the default brand.

The default brand is retained if you downgrade to a single-brand plan, unless the agent
brand differs from the default brand. In that case the agent brand is retained.

**To change your default brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click the menu icon beside the brand, then select **Set as default**.

   The brand
   moves to the top of your list of brands and is labeled as the default.

   The
   default brand is applied to any tickets where brand is not selected. This includes
   tickets that come in via the API, shared tickets, and Chat tickets.

## Changing your agent brand

The *agent brand* is the brand to which agents are routed when they sign in to
Zendesk. This is also known as the *agent route*. The agent brand is the same as the
default brand unless you change it.

When agents sign in to Zendesk, they are routed to the agent brand, regardless of their
brand membership.

The agent brand is identified as *Agent route* on your brands list if it differs from
your default brand. Otherwise, the agent brand is the same as your default brand. The agent
brand is the brand retained if you downgrade to a single-brand plan.

Only the account owner can change the agent brand. The agent brand cannot be deleted or
deactivated unless it is no longer associated with any agents.

**To change your agent brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Appearance > Branding**.
2. In the **Subdomain** section, use the **Brands menu** drop-down to select your
   agent brand.

   The drop-down menu is only visible to the account owner.
3. Click **Save**.

## Requiring agents to select a brand before saving tickets

Agents can select a brand when creating or editing a ticket, but are not required to do so
by default. Admins can require agents to select a brand to prevent tickets from being saved
without a brand. Requiring a brand is recommended if you [restrict agent access to tickets by brand](https://support.zendesk.com/hc/en-us/articles/7584022494874), as agents can only
access tickets within their assigned brands.

**To require agents to select a brand before saving tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click **Manage settings**.
3. Select **Require brand selection before saving tickets**.
4. Click **Save**.

## Editing brand membership settings (Enterprise plans only)

Customers on Enterprise plans and above with multiple brands can manage brand settings for
new and upgraded team members.

By default, all brands are selected when adding a new team member, giving them access to
tickets within those brands. If you want to [restrict agent ticket access by brand](https://support.zendesk.com/hc/en-us/articles/7584022494874), you can change this setting
to have no brands selected, requiring manual brand assignments when adding team members.

Note: Team members can only view, search, and access tickets with their
assigned brands. It's important to [understand brand membership](https://support.zendesk.com/hc/en-us/articles/7584022494874#topic_eqt_crx_xbc) before changing this
setting.

**To edit brand membership settings for new team members**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click **Manage settings**.
3. Select options for **Choose how new team members get assigned to brands** and
   **Choose how end users are assigned to brands when upgraded to team member**.

   See
   [Configuring brand membership settings for new team
   members](https://support.zendesk.com/hc/en-us/articles/7584022494874#topic_yb2_whp_ngc) for details.
4. Click **Save**.
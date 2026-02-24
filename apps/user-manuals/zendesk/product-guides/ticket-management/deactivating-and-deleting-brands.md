# Deactivating and deleting brands

Source: https://support.zendesk.com/hc/en-us/articles/4408829486362-Deactivating-and-deleting-brands

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Learn how to deactivate or delete brands to manage your support operations effectively. Deactivating a brand stops new tickets and help center access but retains existing ticket visibility. Deleting a brand is permanent, removing all tickets and support addresses. Ensure to update macros, business rules, and communicate changes to customers before deletion to avoid errors and disruptions.

Location:  Admin Center > Account > Brand management > Brands

This article describes how to deactivate and delete brands. For information about editing
your brands, see [Editing brands](https://support.zendesk.com/hc/en-us/articles/4408826557082). For a list of other resources, see
[Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306).

This article contains the following sections:

- [Deactivating brands](#topic_b12_nhz_t4b)
- [Deleting brands](#topic_ipz_qhz_t4b)

## Deactivating brands

When you deactivate a brand, consider the following consequences and best practices:

- End users can't submit tickets to that brand or visit the help center for that
  brand.
- You will continue to see the brand on existing tickets.
- New channels can't be created for the brand.
- Emails sent to the brand's support address will create tickets for your default
  brand.
- Agents can still visit the help center for the deactivated brand.
- Admins can continue to add team members to the brand.
- Inactive brands with [host-mapped addresses](https://support.zendesk.com/hc/en-us/articles/4408838571930) turned on still require a valid SSL
  certificate. Therefore, if an inactive brand no longer requires host mapping, we recommend
  removing it.
- The brand's [Web Widget](https://support.zendesk.com/hc/en-us/articles/4409103246874) disappears from the Messaging page in
  Admin Center after you deactivate the brand, but reappears after you reactivate it.

**To deactivate a brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click the menu icon beside the brand, then select **Deactivate**.

   The brand moves
   to the bottom of your list of brands. You can activate the brand again at any
   time.

## Deleting brands

When you delete a brand, it cannot be recovered, and end users and agents can't submit
tickets to that brand or visit its help center.

Before you delete a brand, consider the following consequences and best practices:

- If the brand you want to delete is the default brand, you must first [set a new default brand](https://support.zendesk.com/hc/en-us/articles/4408826557082#topic_vnh_yms_x4b). If the brand is the agent
  brand (the brand agents are routed to when they sign in to Zendesk), you must [change the agent brand](https://support.zendesk.com/hc/en-us/articles/4408826557082#topic_bqs_lns_x4b) before deleting it.
- No new tickets will be created with the deleted brand.
- All unclosed tickets will be reassigned to your default brand.
- Team members assigned to the brand as their only brand membership will be added to the
  default brand.
- No new contacts can be created for this brand.
- If a macro is applied that references a deleted brand, it will cause an error, and the
  ticket update will not be saved. To prevent this, check macros and business rules for
  references to the brand you are removing and edit or deactivate these as needed.
- All support addresses in the domain will be deleted. Therefore, it might be necessary to
  remove the email forwarding for any external support addresses so that they no longer
  point to Zendesk. However, if you still plan to use these support addresses going forward,
  you'll want to add them again and associate them with a new brand.
- Any emails sent to Zendesk support addresses (ending in .zendesk.com) associated with
  the deleted brand will be rejected. Therefore, we recommend communicating this change to
  your customers before you delete the brand if they use those support addresses.
- Depending on your workflow, we recommend [bulk updating tickets](../../agent-guide/ticket-management/managing-tickets-in-bulk.md) associated with this brand
  to assign them to a new brand. When a brand is removed, any tickets associated with the
  brand that are not in a closed status will be automatically updated to reflect your
  default brand.
- If there's a help center associated with this brand, it will be removed when the brand
  is deleted. If you've created knowledge base articles in that help center and want to save
  that information, you can only do that before deleting the brand.
- You will continue to see the deleted brand on existing tickets.

**To delete a brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click the menu icon beside the brand, then select **Delete**.

   The brand is
   removed from your list of brands.
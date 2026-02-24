# Creating and applying branded ticket forms

Source: https://support.zendesk.com/hc/en-us/articles/4408822414490-Creating-and-applying-branded-ticket-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Tickets > Forms

If you have [set up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), you can restrict
access to specific [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858) by brand. This allows you to control the ticket
forms available to end users and agents based on the brand of the Help Center or ticket
they're viewing. You can assign brands to new ticket forms or add them to existing
forms.

Note: When viewing a ticket, if an agent changes the brand, the selected form
won't change even if the currently-selected form isn't available to the new brand.
This is to prevent loss of data in the ticket fields.

This article includes the following topics:

- [Creating a new branded ticket form](#topic_ql4_kjr_5wb)
- [Assigning brands to an existing ticket form](#topic_nhh_gys_5wb)

## Creating a new branded ticket form

When you create a new ticket form, you can apply it to all brands or assign specific
brands.

**To create a new branded ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click **Add form**.
3. Follow the steps in [Creating multiple ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858), with
   the following modifications:
   1. Deselect **Apply to all brands**.
   2. Click the **Associated brands** text box and select the brand(s) that
      should use this form.
4. Click **Save**.

## Assigning brands to an existing ticket form

After you create a ticket form, you can edit the form to assign specific brands.

Note: Zendesk recommends keeping the default ticket form for your account assigned to
all brands. Otherwise, if a brand can't access the default ticket form, the first
ticket form availble to the brand that is [listed](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_xrp_1bc_cdb) on the Ticket forms page in Admin
Center will be used as the default.

### Adding brands to a ticket form

**To add brands restrictions to a ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click the name of the form you want to update.
3. Deselect **Apply to all brands**.
4. Click the **Associated brands** text box and select the brands that
   should use this form.
5. Click **Save**.

### Changing the brands assigned to a ticket form

**To change the brand restrictions on a ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click the **Associated brands** box to display the current brands
   assigned to the ticket form.
3. Change the brands as needed.
   - To add brands, select the brand name from the drop-down list.
   - To remove brands, click the **x** next to the brand name.
4. Click **Save**.
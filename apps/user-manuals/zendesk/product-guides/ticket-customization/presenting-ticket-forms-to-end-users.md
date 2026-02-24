# Presenting ticket forms to end users

Source: https://support.zendesk.com/hc/en-us/articles/4408842873498-Presenting-ticket-forms-to-end-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Tickets > Forms

A ticket form is a set of predefined ticket fields for a specific type of support request.
When you have [multiple
ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858) available to end users, you can customize the instructions that
direct end users to select the appropriate support request form or provide a link to the
appropriate ticket form directly in your help center.

This article contains the following topics:

- [Customizing the presentation of ticket forms to end users](#topic_zzx_ync_fdc)
- [Changing the instructions for selecting a ticket form](#topic_dtr_52d_fdc)
- [Linking directly to a ticket form](#topic_uqq_z2d_fdc)

## Customizing the presentation of ticket forms to end users

Without customization, when multiple ticket forms exist, users are presented with a
drop-down list of forms to select from when submitting a request.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticketforms_end_user.png)

However, the following options are available to help ensure users submit requests based on
the correct form:

- You can [change the order](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_ksw_lrb_lk) of the forms in the drop-down list.
- You can link directly to a ticket form in your help center to present a group of end
  users with a specific request form instead of asking them to select the appropriate
  form. If you require sign-in to submit tickets, the user will have to sign in to see the
  form.
- If you want to streamline the whole process for your users and agents, you can
  create automatically filled fields of the form for them. See [Creating pre-filled ticket forms](https://support.zendesk.com/hc/en-us/articles/4408839114522).

## Changing the instructions for selecting a ticket form

Instead of using the standard instructions, you can customize the instructions provided to
end users when submitting a request to help them select the appropriate ticket form.

**To change the instructions that end users see for multiple ticket forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Enter text in the **End user instructions** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_end_user_instructions_v3.png)

   You can use dynamic
   content in your end-user instructions. For more information see [Creating dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066#topic_qcy_eci_je).
3. Click **Save**.

## Linking directly to a ticket form

In some cases, you can skip the step of users selecting their ticket form and provide them
a direct link to a specific form.

**To link directly to a ticket form in your help center**

1. Get the URL for the ticket form you want to link to by doing **one** of the
   following:
   - Go to your support request form on your site, select a form from the drop-down
     list, then copy the URL.
   - Go to the **Ticket Forms** admin page and click the ticket form to open it for
     editing. The edit page for the ticket form opens. Look at the URL in the your
     internet browser. The number at the end of the URL is the ID of the ticket
     form.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ticket_forms_1.png)

     Replace
     the ticket form ID (8613) in the example URL below with your ticket form
     ID:

     https://**mycompany**.zendesk.com/hc/en-us/requests/new?ticket\_form\_id=**8613**.
2. Present the link to customers so that they can open a specific request form in your
   help center.

   Note: If you're on a Support Enterprise plan, you must also have at least a
   [Guide Lite Legacy](https://support.zendesk.com/hc/en-us/articles/4408823905434#topic_u2d_nww_tvb) plan to be able to route
   users to the form.

   If you require sign-in to submit tickets, the user will
   have to sign in to see the form.
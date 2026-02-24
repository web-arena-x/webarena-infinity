# Using custom ticket fields and ticket forms with the Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408834218522-Using-custom-ticket-fields-and-ticket-forms-with-the-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The Web Widget (Classic) allows you to customize the information displayed in your contact form in a number of ways. In this article, we'll discuss the following customizations:

- Adding custom ticket fields to the Web Widget (Classic) default contact form
- Removing the name field in the default contact form and ticket forms
- Making the name field in the default contact form and ticket forms a required field
- Using different ticket forms with the Web Widget (Classic)

This article includes the following topics:

- [Adding custom ticket fields to the default contact form](#topic_j4t_ppp_jz)
- [Enabling multiple ticket forms in the Web Widget (Classic)](#topic_bpg_wrp_jz)
- [Customizing field descriptions in the Web Widget (Classic)](#topic_ndd_qpp_jz)
- [Advanced customization: Contextual ticket forms](#topic_qxn_ppp_jz)
- [Advanced customization: Pre-populating contact form text fields](#topic_pny_ppp_jz)

Related article:

- [Configuring components in the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258)

## Adding custom ticket fields to the default contact form

Customers on any Support plan can choose to display one, two, or all visible, editable custom ticket fields to the Web Widget (Classic) contact form. On some usage plans, you can choose any number of custom ticket fields to display in the default contact form. For information on custom ticket fields, see [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794).

[System ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098), such as the **Priority** field, are not supported in the Web Widget (Classic). They appear in the default contact form (and any other ticket form), when accessed from the help center, but do not appear in the Web Widget (Classic). Reordering fields is supported in the Web Widget (Classic)
using the ticket forms, but not in the contact form.

Regular expression (Regex), Date, and [Multi-select](https://support.zendesk.com/hc/en-us/articles/4408883152794) custom fields cannot be used in the Web Widget (Classic).

**To display custom ticket fields in the default contact form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. In the **Basics** tab, select the **Contact form** checkbox and click the **Custom ticket fields** drop-down.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_custom_tkt_fields-2.png)
3. Select the custom ticket fields you want to display in the contact form, or select **Select all**.
4. Click **Save**.

## Enabling multiple ticket forms in the Web Widget (Classic)

If you're on a Zendesk Suite or Support Enterprise or Enterprise Plus plan, you can use multiple ticket forms in the Web Widget (Classic). For a list, and for general information about how ticket forms work, see [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858).

Ticket forms allow you to customize the fields displayed in your contact form based on the type of request a customer makes. In order for this feature to work, you must have more than one ticket form created.

**To enable ticket forms in your Web Widget (Classic)**

1. CIn [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. In the **Basics** tab, select the **Contact form** checkbox and then select the **Ticket forms** checkbox.
3. Click **Save**.

With ticket forms are toggled on, when a customer clicks the Leave us a message button, they're asked to select a form that matches their needs, from a list of all of your [active ticket forms](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_jnd_krb_lk):

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_tkt_form_ex.png)

When they make a selection, the contact form displays fields specific to that ticket form.

## Customizing field descriptions in Web Widget (Classic)

You can add [custom ticket fields and their descriptions to the default contact form in the Web Widget (Classic)](#topic_j4t_ppp_jz). To make these appear, you must select the field from the **Custom ticket fields** option in the Web Widget (Classic) admin settings.

However, keep in mind that [system fields](https://support.zendesk.com/hc/en-us/articles/4408886739098), such as the **Priority** field, are not supported in the Web Widget (Classic). This is regardless of plan type. They appear in the default contact form, and any other ticket form, when accessed from the help center, but do not appear in the Web Widget (Classic).

Ticket forms are not available on all usage plans. If available on your plan, you can also include custom fields and their descriptions in ticket forms. To make custom ticket fields and their descriptions appear, you must enable the **Ticket forms** option in the Web Widget (Classic) settings.

Note: If the **Ticket forms** toggle is off, the default contact form does not include custom fields and their descriptions in the default contact form. The default contact form will include description that states **How can we help you?** instead.

You can create and edit ticket field descriptions from the **Ticket Fields** admin page.
For more information about ticket fields, see [About ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098).

**To add a field description**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Click the name of the field that needs a description.
3. In the **For end users** section, click **Editable**.
4. Enter a description for the field, then click **Update field**.

## Advanced customization: Contextual ticket forms

You can craft more customized experiences for your users by limiting the forms the end user sees based on the web page they're currently viewing, by modifying the zESettings object in the Web Widget (Classic) JavaScript API. For information on working with the API, see [Advanced customization of Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562).

In the code for the web page you want to modify, update the zESettings object to include the ID number of the ticket form(s) you want to surface. Your Ticket Forms ID is listed in the URL in the Ticket Forms admin page.

**To locate a ticket form ID number**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click the name of the form you want to hide, or to use as your standalone form.
3. Take note of the form ID in the address bar:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_tkt_form_ID.png)

Use the following examples to modify your website code.

**To display a single ticket form:**

```
<script type="text/javascript">
window.zESettings = {
 webWidget: {
    contactForm: {
      ticketForms: [
        { id: ###### }
      ]
    }
 }
};
</script>
```

**To display two ticket forms:**

```
<script type="text/javascript">
window.zESettings = {
 webWidget: {
    contactForm: {
      ticketForms: [
        { id: ###### }, 
        { id: ###### }
      ]
    }
 }
};
</script>
```

Add additional IDs to the zESettings object as needed.

## Advanced customization: Pre-populating text fields

You can use new settings to pre-fill certain fields. You can use different strings for different locales, or use one string for all locales by using an asterisk (\*) for the locale. This is similar to other customizable text strings like Contact Form title.

Note: This section discusses how to pre-populate system fields. For information on pre-filling user names and email addresses, see [Web Widget API zE.identify](https://developer.zendesk.com/embeddables/docs/widget/api#ze.identify).

To pre-fill a system field like 'subject' and/or 'description' , update the zESettings object as shown below.

**Example: Prefilled description text**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_tkt_form_prefill_ex.png)

Use the following code:

```
<script type="text/javascript">
zESettings = {
 webWidget: {
    contactForm: {
      fields: [
        { id: 'description', prefill: { '*': 'This is prefilled description text' } }
      ]
    }
 }
};
</script>
```

**Example: Prefilled custom field:**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_cust_field_prefill_ex.png)

Use the following code:

```
<script type="text/javascript">
zESettings = {
 webWidget: {
    contactForm: {
      fields: [
        { id: #####, prefill: { '*': 'Desired text' } }
      ]
    }
 }
};
</script>
```

In this code block, `id: #####` is the custom field identifier.

You can elect to always prefill a particular field in all of your forms, or prefill it separately in specific forms.

**Code example: Different text for the same field in different forms:**

```
<script type="text/javascript">
window.zESettings = {
 webWidget: {
    contactForm: {
      ticketForms: [
       { 
         id: ###TicketFormID###, 
         fields: [
           {
              id: 'description',
              prefill: {
                '*': description
              }
            }
          ]
        },
        {
          id: ###TicketFormID###, 
          fields: [
            {
              id: 'description',
              prefill: {
                '*': 'different description'
              }
            }
          ]
        }
      ]
    }
 }
};
</script>
```
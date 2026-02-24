# Creating pre-filled ticket forms

Source: https://support.zendesk.com/hc/en-us/articles/4408839114522-Creating-pre-filled-ticket-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can set up a ticket form that has pre-filled values in specific fields (such as the Subject or Description fields). This can save time for your end users and get them closer to a resolution. It also benefits your support agents by ensuring they have accurate and specific input from customers.

For example, if an article in your help center explains how to troubleshoot a coffee maker, you can create a link at the end of that article that opens a ticket form pre-populated with the coffee maker model and issue. Users who click this link will have much less information to fill out when submitting their ticket.

Note: This feature requires that your theme uses Templating API version 2 or higher. To check your version see [About help center templating versions](https://support.zendesk.com/hc/en-us/articles/4408820214554).

Pre-fill ticket forms (2:03)

This article includes the following sections:

- [Configuring a pre-filled ticket form](#topic_qvy_gnj_x4b)
- [Parameter keys and values](#topic_s54_vcq_gpb)

Related articles:

- [Customizing and creating support request forms](https://support.zendesk.com/hc/en-us/articles/4408882448922-Using-Zendesk-Support-and-Zendesk-Guide-together#topic_p22_sw2_2db)
- [Creating conditional ticket fields](https://support.zendesk.com/hc/en-us/articles/4408834799770)
- [Creating multiple ticket forms to support different request types](https://support.zendesk.com/hc/en-us/articles/4408846520858)
- [Enabling agents to access request forms](https://support.zendesk.com/hc/en-us/articles/4408828251930)
- [Using pre-filled ticket forms with SSO authentication](#topic_tws_yjw_mxb)

## Configuring a pre-filled ticket form

When you create pre-filled ticket forms, you add parameters for the fields that you want to pre-fill to the URL of the form. If you have multiple ticket forms, you’ll also include the specific ticket form ID in the URL.

**To configure pre-filled fields in a form**

1. Copy the URL for the ticket form that end users see when they click **Submit a request** and paste it into a text editor file.

   It should resemble this, where *mycompany* is your subdomain:
   *https://mycompany.zendesk.com/hc/en-us/requests/new?* 

   Note: If you have host mapping, your URL will look different from the previous example (see [Host mapping - changing the URL of your help center](../setting-up-your-help-center/host-mapping-changing-the-url-of-your-help-center.md)).
2. (Multiple ticket forms only) In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets >
   Forms**. Select the ticket form you want to pre-fill, then copy the form ID from the URL in Support and paste the ID to the end of the URL in your text editor.
3. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets >
   Fields**. Copy the field values you want to pre-fill and paste them along with values to the end of the URL in your text editor.

   For *system* values, copy the title of the field (for example "Subject"). Use the following format to paste the title at the end of the URL that you are building, along with the value that you want to assign to the field:

   `&tf_{title}={value}`

   For *custom* values, copy the Field ID of the field (for example, “12345”). Use the following format to paste the Field ID at the end of the URL that you are building, along with the value that you want to assign to the field:

   `&tf_[fieldID}={value}`

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_pre-filled_custom_system_fields.png)
4. Continue adding fields and values to the end of the URL in your text editor as needed.

   The parameters should be similar to the following example:
   `&tf_subject=Faulty charger 999 recall&tf_12345=USA`
5. Copy the URL from the text editor and paste it wherever you want to link end users to the pre-filled form. Your final URL should resemble one of the following examples:
   - Single ticket form:

     `https://www.example.zendesk.com/hc/en-us/requests/new?tf_subject=Faulty charger 999 recall&tf_12345=USA`
   - Multiple ticket form:

     `https://www.example.zendesk.com/hc/en-us/requests/new?ticket_form_id=1500000300222&tf_subject=Faulty charger 999 recall&tf_12345=USA`

## Parameter keys and values

The URL parameter keys and values differ based on what type of field you want to pre-fill. There are two different field types that are used in a request ticket form:

- **System fields** - are the default fields in a ticket and have a unique name.
- **Custom fields** - are fields that you can create to supplement the information that is already being gathered from the existing system fields.

### System fields

The URL parameter of system fields uses the prefix `tf_` followed by the field name. For example `tf_subject`. For more information, see [System ticket fields](../ticket-management/about-ticket-fields.md#topic_drw_ft1_3nb). Use the following parameters for the Zendesk system fields:

- **Email**: `tf_anonymous_requester_email`
- **Priority**: Include the value type (low, norm, high, urgent), after the field name, for example `tf_priority=high`
- **Type**: Include the value type after the field name, for example `tf_type=incident`
- **Description**: `tf_description`
- **Subject**: `tf_subject`
- **Due date**: (Used when Type=task) Use the canonical date format YYYY-MM-DD, for example `tf_due_at`
- **Cc**: (Used when a user is logged in). Separate the emails with a comma, not a space, for example `tf_collaborators=name1@example.com,name2@example.com`
- **Organization ID**: Include the value type after the field name, for example`tf_organization_id=123456789`

### Custom fields

The URL parameter of custom fields uses the prefix `tf_` followed by the field ID. For example `tf_40630945`. For more information, see [About custom field types](https://support.zendesk.com/hc/en-us/articles/4408838961562). With custom objects, you can create the following custom fields:

- **Multi-select**: Use field tags as the values and separate them with a comma, not a space, for example blue,green,red.
- **Drop-down menu**: Use the tag associated with the value. For example `tf_40630945=dog_beagle`.
- **Checkbox**: Use the value true/false
- **Decimal**: Use integers and non-integers (for example, -8.012345679). Do not use commas.
- **Date**: Use the canonical date format: YYYY-MM-DD
- **Lookup relationship**: Use the value or custom object record ID.
 For example:
 `tf_40630945=HVAC02345`

## Using pre-filled ticket forms with SSO authentication

When you use pre-filled ticket forms in environments with single sign on (SSO)
authentication, end users must be logged in before they can submit a ticket. This means that if an end user accesses the pre-filled ticket form from another source (for example, website or QR code), they must be logged in to see the initial values in the pre-filled ticket form. If they are not logged in, they will be prompted to log in before being directed to the ticket form. Because users are accessing the form from the login page rather than from the original link or QR code, the pre-filled ticket values no longer appear. Users can still fill out the form and submit the ticket, but they will not see any pre-filled values.

To ensure that users can access pre-filled ticket forms at all times, you can choose to not require user authentication prior to access the ticket form. Alternatively if your environment requires user authenticaion in all cases, you can include content for users wherever they access the link, instructing them to return to this link after they log in to the environment. Once they are logged in, they can click the link or use the QR code to access the pre-filled ticket forms.
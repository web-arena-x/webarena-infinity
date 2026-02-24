# Creating and managing structured message templates for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357757976474-Creating-and-managing-structured-message-templates-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

This article applies only to advanced AI agents [connected to a messaging channel](https://support.zendesk.com/hc/en-us/articles/8357720504858).

You can create structured message templates and insert them in conversation flows for advanced AI agents. There are three types of structured message templates, which can be used to do the following:

- **Forms**: Collect a predefined set of information from a customer.
- **Webviews**: Present an external website to the customer within the Web Widget.
- **Custom**: Templates that are designed to meet your business needs.

This article contains the following topics:

- [Creating a structured message template](#topic_lfw_hcj_jhc)
- [Adding a structured message template in a dialogue](#topic_mgl_3cj_jhc)
- [Viewing all structured message templates](#topic_ahy_3cj_jhc)
- [Editing a structured message template](#topic_c54_jcj_jhc)
- [Deleting a structured message template](#topic_i2j_kcj_jhc)

Related article:

- [Using templates to create conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756562330)

## Creating a structured message template

You can create three types of structured message templates:

- [Form templates](#topic_gzn_zdj_jhc)
- [Webview templates](#topic_rnb_12j_jhc)
- [Custom (JSON)
 templates](#topic_c2p_12j_jhc)

### Creating a form template

Form templates are useful for presenting a customer with a set of predefined fields that you want them to fill out, such as their contact information.

**To create a form template**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Templates** tab.
4. Click **Create your first template** or, if you’ve created a template before, **Create template**.
5. Select **Forms**.

   The form template configuration page appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_form_template.png)
6. In **Template name**, enter a name for the template.

   The name can't have spaces or any special characters other than hyphens (-) and underscores (\_). This name appears in the list of structured message templates and is the shorthand you’ll use to [add the template in a dialogue](#topic_mgl_3cj_jhc).
7. (Optional) In **Description**, enter a brief description of the template, such as its intended purpose.
8. Select **Block messaging input** if you want to prevent the customer from continuing the conversation until they’ve filled out the form.
9. Under Input Field, in **Message type**, select the type of information you want to collect from the user: **Email**, **Text**, or **Select** (which allows customers to select from options you define).

   All fields in this section are limited to 130 characters.
10. In **Name**, enter the name of the variable that will be created based on this input field.
11. In **Label**, enter the name of the field that will be shown to the customer in the widget.
12. If you selected a message type of Select, click **Add option** and fill out the following fields:
    - **Option name**: Enter the name of the variable that will be created based on this option selection.
    - **Option label**: Enter the name of the option that will be shown to the customer in the form. Repeat this step for any additional options you want to present to the customer.
13. (Optional) Click **Add field** to add additional fields to the form.

    For the best user experience, keep the number of fields to five or fewer.
14. Click **Create**.

### Creating a webview template

Webview templates are useful for presenting an external website to the customer within the Web Widget so that they don’t have to leave the conversation.

Note: Webview templates can be used to direct customers to a single website, with one fallback website available. To create a dynamic webview where the website the customer is directed to is based on collected parameters, use the [Add a webview](https://support.zendesk.com/hc/en-us/articles/8357734565402#h_01GWKHG1ZJ40C0D3HW289PY990) CRM action instead.

**To create a webview template**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Templates** tab.
4. Click **Create your first template** or, if you’ve created a template before, **Create template**.
5. Select **Webview**.

   The webview template configuration page appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_webview_template.png)
6. In **Template name**, enter a name for the template.

   The name cannot have spaces or any special characters other than hyphens (-)
   and underscores (\_). This name appears in the list of structured message templates and is the shorthand you’ll use to [add the template in a dialogue](#topic_mgl_3cj_jhc).
7. (Optional) In **Description**, enter a brief description of the template, such as its intended purpose.
8. In **Message text**, enter the message your advanced AI agent will show above the button.

   For example, if you're creating a webview to present product information to the customer from your website, the message text might say, "You can check out our product page to learn more about this camera model."
9. In **Button text**, enter the text that appears as the label on the button.

   For example: "View product details"
10. In **URL**, enter the URL that opens when the customer clicks the button.

    This URL must allow loading in an iframe.
11. In **Fallback URL**, enter a backup URL.

    Channels that don’t support webviews open the fallback URL instead.
12. (Optional) Click **Optional fields** to show the following additional configuration options:
    - **Size**: Select the size of the displayed webpage within the Web Widget. Available options are **Compact**, **Tall**, or **Full**.
    - **Default**: Select this toggle to make this the default action.
    - **Automatically open webview**: Select this toggle to automatically open the webview when this template is triggered.
    - **Add field**: Click to add field to capture metadata based on this template. Fill out the **Metadata** and **Value** fields. Repeat as needed to add additional fields.
13. Click **Create**.

### Creating a custom (JSON) template

Custom templates are useful for presenting carousels, lists of content, NPS ratings, or location-based messages.

**To create a custom (JSON) template**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Templates** tab.
4. Click **Create your first template** or, if you’ve created a template before, **Create template**.
5. Select **Custom (JSON)**.

   The custom template configuration page appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_custom_template.png)
6. In **Template name**, enter a name for the template.

   The name cannot have spaces or any special characters other than hyphens (-)
   and underscores (\_). This name appears in the list of structured message templates and is the shorthand you’ll use to [add the template in a dialogue](#topic_mgl_3cj_jhc).
7. (Optional) In **Description**, enter a brief description of the template, such as its intended purpose.
8. In the code field, enter the JSON for the custom template you want to create.

   For help, see [Template messages](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/template-messages/).
9. Click **Create**.

## Adding a structured message template in a dialogue

After you [create a structured message template](#topic_lfw_hcj_jhc), you have to add it in a dialogue so that it’s presented to a customer at the appropriate time during a conversation with an advanced AI agent.

**To add a structured message template in a dialogue**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Templates** tab.
4. Find the template you want to add and click the entry in the Shorthand column.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_shorthand.png)

   The template shorthand is copied to your clipboard.
5. [Open the dialogue](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c) you want to add the template to.
6. Select the AI agent message block where you want the AI agent to present the template to the customer.
7. Paste the template shorthand you copied earlier.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_add_in_dialogue.png)

## Viewing all structured message templates

You can view a list of all structured message templates you’ve created.

**To view all structured message templates**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Templates** tab.

   The Templates page opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_templates_page.png)

   From this page, you can see a list of all structured message templates, with information shown in the following columns:
   - **Details**: The name of the template.
   - **Shorthand**: Click to copy the text you should enter when you [add the template in a dialogue](#topic_mgl_3cj_jhc).
   - **Type**: The type of structured message template (form, webview, or custom).
   - **Created by**: The user who created the template.
   - **Last modified by**: The date the template was last updated.

## Editing a structured message template

After you create a structured message template, you can edit it at any time.

**To edit a structured message template**

1. [In the list of structured message templates](#topic_ahy_3cj_jhc), find the template you want to edit.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **View information**.

   The template configuration page opens.
3. Edit the template as needed.

   For help, see [Creating a structured message template](#topic_lfw_hcj_jhc).
4. Click Save.

## Deleting a structured message template

If you no longer need a structured message template, you can delete it.

**To delete a structured message template**

1. [In the list of structured message templates](#topic_ahy_3cj_jhc), find the template you want to delete.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Delete**.

   A confirmation dialog appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_rich_messaging_delete.png)
3. Click **Delete**.
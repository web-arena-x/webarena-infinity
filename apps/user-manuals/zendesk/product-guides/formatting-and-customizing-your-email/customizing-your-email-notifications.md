# Customizing your email notifications

Source: https://support.zendesk.com/hc/en-us/articles/4408886168090-Customizing-your-email-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Customize your email notifications by editing HTML and plain text templates to match your brand. Add logos, change colors, or include specific messages. Use triggers and automations for dynamic content, and manage multiple brands with a single template. Note that side conversation emails don't use these templates, and editing might require contacting support.

Location: Admin Center > Channels > Talk and email > Email

Your account sends regular email notifications to end users when events such as ticket or help center updates occur. The content and format of almost all these emails are controlled by two templates in Admin Center: an HTML template and a plain text template. Both formats are included in each email sent. The version end users see depends on their email application settings.

You can use both templates as they come or edit them to better suit your needs. Unlike the plain text template, the HTML template also lets you customize the look and feel of the email sent from your account. For example, you can add your company logo or a call-to-action banner to match your brand identity or to more closely match the look of your help center.

This article contains the following topics:

- [Limitations](#topic_y1j_bhk_12c)
- [Anatomy of the email templates](#topic_x2z_thk_12c)
- [Customizing your HTML email](#topic_myq_hb2_tdc)
- [Customizing your plain text email](#topic_adc_1c2_tdc)
- [Customizing your email in triggers and automations](#topic_uzz_vq2_tdc)
- [Customizing your email for multiple brands](#topic_u4q_xss_tdc)
- [Placeholder reference for the HTML email template](#topic_mqn_hpd_x3)

## Limitations

- Editing email templates isn't allowed by default for trials and might not be allowed for some accounts. To enable editing, [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850-Contacting-Zendesk-Customer-Support?source=search) with your subdomain, a link to your company website, and a brief description of the changes you want to make.
- [Side conversation](https://support.zendesk.com/hc/en-us/articles/4408844206746) email notifications don't use the email templates.

## Anatomy of the email templates

Understanding the anatomy of the HTML and plain text templates is useful when customizing them.

### Anatomy of the HTML template

The standard HTML notification email sent from your Zendesk account looks as follows:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_anatomy.png)

The side numbers in the screenshot correspond to the following components in the email templates:

| **email body** | The email body is represented by the `{{content}}` placeholder in the HTML email template in Admin Center (red highlight box):    Before sending out the email, the system replaces the `{{content}}` placeholder in the template with additional HTML to display the email body. The email body itself is defined in a trigger. In the following trigger action, the email body is highlighted in red:    In the example, the email body consists of two elements:   - A notification message: "Your request ({{ticket.id}}) has been updated. To add   additional comments, reply to this email." - Ticket comments represented by the   `{{ticket.comments_formatted}}` placeholder   See [Customizing your email in triggers and automations](#topic_uzz_vq2_tdc). |
| **standard footer** | The standard footer consists of the following two placeholders:   - `{{footer}}`: Renders "This email is a service from   Mondocam." - `{{footer_link}}`: Renders "Delivered by [Zendesk](https://www.zendesk.com/support)"   Both placeholders are optional. You can delete one or both from the template. |

### Anatomy of the plain text template

The plain text email template is used when the user elects not to read email messages in HTML format. The template consists of two system placeholders:

```
{{content}}

{{footer}}
```

The `{{content}}` placeholder inserts the text generated from business rules (triggers, automations, or macros), and the ticket comments. The `{{footer}}` placeholder is optional. You can remove it if you want. For more information, see [Understanding the system placeholders](#topic_mqn_hpd_x3).

If you'd like to add a line to your plain text emails, add it to the template.

```
Thanks for contacting Mondocam Support!

{{content}}

{{footer}}
```

## Customizing your HTML email

You can customize the look and feel of the HTML email notifications sent to your customers.
This section covers the following topics:

- [Editing the HTML email template](#topic_ucy_3vc_x3)
- [Example: Changing the color of the footer text](#topic_x5r_hnd_x3)
- [Example: Adding your logo](#topic_kfp_cgr_tdc)

For guidelines and recipes, see the [Zendesk email design cookbook](https://support.zendesk.com/hc/en-us/articles/8414886738970).

### Editing the HTML email template

You can change the appearance of HTML emails by editing the HTML email template in Admin Center. Editing the HTML template requires a certain level of familiarity with HTML and CSS. For recipes, see the [Zendesk email design cookbook](https://support.zendesk.com/hc/en-us/articles/8414886738970). For design guidelines, see [HTML guidelines for email](https://support.zendesk.com/hc/en-us/articles/8414886738970--DRAFT-Email-template-cookbook#topic_tt1_3c1_ldc).

The changes are applied to your outgoing email immediately after saving them. Therefore, you should [preview and test your changes](https://support.zendesk.com/hc/en-us/articles/8414886738970#topic_q3g_4mj_ldc) before applying them to the template. If you're on an Enterprise plan, you can also [test email changes in a sandbox](https://support.zendesk.com/hc/en-us/articles/4408828617370) before deploying them publicly.

**To edit the HTML template**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Edit email templates**.
3. In the HTML template section, modify the HTML of the template as needed.

   See the [Zendesk email design cookbook](https://support.zendesk.com/hc/en-us/articles/8414886738970).
4. If you want to start over with the default version, click **Revert to default** above the template.
5. If you want to show user photos in emails, select **Show user profile photos in emails**.

   When selected, profile photos are displayed in emails when the email client supports it. Not all email clients display images by default.
6. Click **Save**.

#### Example: Changing the color of the footer text

This example shows how to change the font color of the footer to teal, which has a hex color code of #009966. For more ideas for a footer, see the following recipes in the Zendesk email design cookbook:

- [Recipe: Add a footer](https://support.zendesk.com/hc/en-us/articles/8414886738970--DRAFT-Email-template-cookbook#topic_phy_3mx_ldc)
- [Recipe: Add social media links to the footer](https://support.zendesk.com/hc/en-us/articles/8414886738970--DRAFT-Email-template-cookbook#topic_zvk_dvq_qdc)

Suppose the footer in your template consists of the `{{footer}}` and `{{footer_link}}` placeholders. If your company name is Mondocam, the placeholders render the following line in the email sent: "This email is a service from Mondocam. Delivered by [Zendesk](https://www.zendesk.com/support)".

**To change the color of the footer text**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Edit email templates**.
3. In the HTML template section, locate the two footer placeholders and their parent `<div>` tag:

   ```
   ...
     <div style="padding: 10px;
                 line-height: 1.5; 
                 font-family: 'Lucida Grande',Verdana,Arial,sans-serif; 
                 font-size: 12px; 
                 color: #aaaaaa; 
                 margin: 10px 0 14px 0; 
                 padding-top: 10px; 
                 border-top: 1px solid #eeeeee;">
       {{footer}} {{footer_link}}
     </div>
   ...
   ```
4. Change the value of **`color`** to **#009966**, which is the hex code for a shade of teal.
5. Click **Save**.

Note: The color of links can't be customized. Links are styled with CSS pseudo classes such as `:hover`. Example: `a:hover {color:#FF00FF;}`. Unfortunately, CSS pseudo classes are not supported in inline CSS, and major email clients like Gmail strip out any CSS that is not inline.

When changing text color, use sufficient color contrast for accessibility. Follow the [Web Content Accessibility Guidelines (WCAG)
recommendations](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) and use tools like [WebAIM color contrast checker](https://webaim.org/resources/contrastchecker/) to check the contrast ratio between the text and the background.

#### Example: Adding your logo

You can add your company logo to the top of your email notifications, but keep in mind that some email clients don't display images by default.

**To add your company logo to your email notifications**

1. Insert an `<img>` tag (`<img src="">`) after the `<body>` tag but before the content `<div>` tag.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_cookbook_location-logo.png)
2. Specify the URL of the logo image as the value of the `src` attribute. Example:

   ```
   <img src="https://mondocam.com/assets/logo.png"/>
   ```
3. If you want to add a hyperlink to the logo, enclose the `<img>` tag in an anchor tag, as in this example:

   ```
   <a href="https://mondocam.com/home"><img src="https://mondocam.com/assets/logo.png"></a>
   ```

To customize your logo in more detail, see [Recipe: Add your company logo](https://support.zendesk.com/hc/en-us/articles/8414886738970#topic_ont_qmb_ldc) in the Zendesk email design cookbook.

## Customizing your plain text email

Because you can't use HTML, you can't customize the look and feel of the plain text email notifications sent to your customers. However, you can add information to your emails.

**To customize the plain text template**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Edit email templates**.
3. Modify the **text template** as needed.
4. If you want to start over with the default version, click **Revert to default** above the template.
5. Click **Save**.

## Customizing your email in triggers and automations

Triggers and automations can have actions that send email to your users. You can add HTML and Liquid markup to trigger or automation actions rather than to the email template to customize the email body. Example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_cookbook_trigger_text.png)

See the following articles for details:

- [Editing and cloning ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722-Managing-triggers#topic_dwq_zoy_tb)
- [Add or remove ticket links](https://support.zendesk.com/hc/en-us/articles/4408846446234)
- [Using Liquid markup to customize the formatting and placement of text in comments and email notifications](https://support.zendesk.com/hc/en-us/articles/4408832790042)

Tip: [Read this Zendesk blog post](https://www.zendesk.com/blog/use-customer-service-email-templates-save-time/) to learn how to save time with common customer service messages for the email body of email notifications.

## Customizing your email for multiple brands

To customize email notifications for multiple brands, you have to customize the email body in the actions of triggers and automations, but keep the email template as generic as possible because you only have one. In other words, you use a single template for all brands but customize different actions for each brand. For more information, see the following resources:

- [Using the email template with multiple brands](https://support.zendesk.com/hc/en-us/articles/4408832356762)
- [How to structure your email template to use custom HTML layouts for each of your multiple brands](https://support.zendesk.com/hc/en-us/community/posts/360033000374), a tip contributed by Andrew Soderberg

## Placeholder reference for the HTML email template

Most of the content in notification emails is generated dynamically by the Zendesk system.
The generated content is represented by placeholders in the email templates. The placeholders are enclosed in double curly quotes, such as `{{footer}}`.

The placeholders insert the email contents and footer text.

`{{content}}` :   Displays the email content, which can include ticket comments and user profile photos.
    The content is defined in the trigger, automation, or anything else that sends email from your account. See [Creating and managing triggers for ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).

`{{quoted_content}}` :   Optional. Displays the message history. The quoted content is usually collapsed in the user's email application, but the user can expand it. In Gmail, for example, the user clicks the ellipsis (…). See [Understanding simplified email threading](https://support.zendesk.com/hc/en-us/articles/4565992897562).
:   Quoted content may not include attachments, depending on how the ticket was created:

    - Attachments are *not* included in the quoted content if the ticket was created by email.
    - Attachments *are* included in the quoted content if the ticket is created by web form (or another non-email channel).

`{{footer}}` :   Optional. Displays the line "This email is a service from *YourZendeskName*." It also displays ticket properties, such as status and requester, in emails sent to agents.
    The properties are not displayed in emails sent to end users.

`{{footer_link}}` :   Optional. Displays the line "Delivered by Zendesk." The word Zendesk is a link to https://www.zendesk.com.

`{{delimiter}}` :   Displays the line "##- Please type your reply above this line -##". The delimiter is used by the system to separate old content from new. When a person replies to an email, the new content in the reply is added to the ticket as a comment. This placeholder is required in the HTML template if you are using the email delimiter. See [Customizing the delimiter text in emails](https://support.zendesk.com/hc/en-us/articles/4408821456922).

`{{styles}}` :   Optional. For future use. Currently, the system uses this placeholder to inject styles when it detects that the locale is a Right-To-Left locale.

`{{attributes}}` :   Optional. For future use. Currently, the system uses this placeholder to inject attributes when it detects that the locale is Right-To-Left.
# Enabling customers to opt out of emails in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408827014042-Enabling-customers-to-opt-out-of-emails-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

If you connect your email address into Sell, you may want to provide a method for your customers to opt out of future email campaigns, or to request that a lead, for example, is not contacted. This article provides guidance on how you can provide a mechanism for customers to opt out, and then track those customers that do not want to be part of future email campaigns.

Note: You are responsible for using the email features in Zendesk Sell in compliance with all applicable laws. Many jurisdictions require sales emails to follow prescribed behaviors, such as including an option for the recipient to unsubscribe. By using these features, you agree that you comply with any such applicable laws. See [Complying with Privacy and Data Protection Law in Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408883081242) for more information.

This article covers the following topics:

- [Providing an opt-out mechanism in an email or email template](#topic_rl4_bss_rlb)
- [Actioning email opt-out requests](#topic_wks_gss_rlb)

Related articles: [Using Mailchimp in Sell](https://support.zendesk.com/hc/en-us/articles/4408832300442) and [About using email in Sell](https://support.zendesk.com/hc/en-us/articles/4408838786586).

## Providing an opt-out mechanism in an email or email template

You can add information to your email or email template to allow customers to opt-out or unsubscribe from future contact or email campaigns.

**To provide an opt-out option in an email or email template**

1. From a lead, contact, or deal card, select the **Send an Email** tab.
2. Compose your email message.

   If you are going to create an email template, you should include merge tags (see [Using merge tags in your email messages](https://support.zendesk.com/hc/en-us/articles/4408828807066-Merge-Tags)), to insert data that is specific to the recipients (for example, their first name), when the message is sent.
3. If you want to add text to your standard email signature, see [Customizing your email signature](https://support.zendesk.com/hc/en-us/articles/4408832176666).
4. In the email or your signature, include a note saying that if you don’t want to receive more emails from us, please reply to this email with “unsubscribe”.

   For example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_unsubscribe_example.png)
5. Click the **Email templates** button if you want to save the email as a template, (see [Creating email templates](https://support.zendesk.com/hc/en-us/articles/4408821812890)).
6. Click **Send Email**.

   Your email is sent, and if the customer replies with unsubscribe, mark them as Opt out in Sell, (see [Actioning email opt-out requests](#topic_wks_gss_rlb)).

   Note: If you’re [sending an email sequence to a lead](https://support.zendesk.com/hc/en-us/articles/4408844143130) and a lead replies with a wish to unsubscribe, the sequence will automatically stop and no further scheduled emails will be sent from this sequence.

## Actioning email opt-out requests

If a customer contacts you to opt out of a campaign, you can use a custom field to flag that they are not to be included in future emails.

You can then use smart lists to view or exclude groups of customers that have requested to opt-out of certain campaigns.

**To add an opted-out customer to a group**

1. Set up a checkbox custom field to add to a customer's record, (see [Creating and managing custom fields](https://support.zendesk.com/hc/en-us/articles/4408838289562)).

   For example, set up a Leads Checkbox custom field called **Opt out**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_optout_checkbox_custom_field.png)

   Tip: Alternatively, you could set up a date custom field called **Unsubscribed at**, if you want to record when a customer unsubscribed.
2. When the customer contacts you, in their record, click the **Opt out** custom field to add a checkmark to the checkbox (to specify that they would like to opt out).
3. In your Working List, filter by your custom field, (see [Filtering your working list and smart lists](https://support.zendesk.com/hc/en-us/articles/4408843786266-Filtering-working-and-smart-lists)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_optout_view.png)
4. To create your campaign list, select only the customers that have the **Opt out** field set to **No**.

   If you created an **Unsubscribed at** custom field, you could **Display > Without Value** to exclude opted-out customers:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_custom_display_without.png)
5. Save your view as a smart list for future use, (see [Creating and using smart lists](https://support.zendesk.com/hc/en-us/articles/4408827735066)).
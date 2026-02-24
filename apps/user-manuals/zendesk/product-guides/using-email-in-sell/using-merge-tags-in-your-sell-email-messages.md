# Using merge tags in your Sell email messages

Source: https://support.zendesk.com/hc/en-us/articles/4408828807066-Using-merge-tags-in-your-Sell-email-messages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

You can dynamically insert personalized data into your email messages using merge tags. For example, you can use a merge tag to insert each recipient’s first name into a bulk email message.

Sell provides standard merge tags that include profile data such as name, phone number, job title, and so on. The custom fields that you create for your leads and contacts are also available as merge tags. Deal custom fields are not available as merge tags. For more information about custom fields, see [Creating and managing custom fields](https://support.zendesk.com/hc/en-us/articles/4408838289562).

**To use merge tags in your email messages**

1. In Sell on the sidebar, click the **Leads**, **Contacts**, or **Deals** icon.
2. Choose the person you want to send an email to, then click the **Send an Email** tab.
3. You can select merge tags for the Subject line by clicking the **Add merge tag** icon (**{ }**) next to the Templates dropdown menu.
4. You can select merge tags for the email body by clicking the **Add merge tag** icon (**{ }**) in the format toolbar or typing {{ and then the name of the merge tag.

   ![Sell email add merge tag](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_merge_tag_add.png)
5. Select a merge tag from the list. If you created any custom fields, they will also be listed and available to insert into your email message.

   When you send the email message, the merge tag will be populated with the corresponding data.![Screenshot_2021-10-13_at_12.23.44.png](https://support.zendesk.com/hc/article_attachments/4408859747098)

   In the example message above, the second merge tag is a custom field. If the custom field has not been populated with data in the lead or contact’s profile, Sell will warn you of that (shown here as an orange tag) and prompt you to remove it from your message.

   If you use a custom field merge tag in a bulk message and some of the recipients do not have data in that custom field, the email message will not be sent to those recipients. You will see a notification informing you that some of the recipients were not included in the email message and a link to create a new email message for those recipients.
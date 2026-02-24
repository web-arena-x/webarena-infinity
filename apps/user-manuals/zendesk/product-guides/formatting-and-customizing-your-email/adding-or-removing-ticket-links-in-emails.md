# Adding or removing ticket links in emails

Source: https://support.zendesk.com/hc/en-us/articles/4408846446234-Adding-or-removing-ticket-links-in-emails

---

Your email notifications can provide a link back to the ticket being discussed:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_ticket_link.png)

This type of link is defined in a trigger or automation, not in the template itself. For example, most of the default triggers have an action that sends an email notification with a link to a ticket. If you provide email-only support, you don't want customers to see a link to a ticket that would prompt them to log in. In this case, you must edit your triggers or any other business rules that generate email notifications.

**To add or remove a ticket link in a notification trigger or automation**

1. Do one of the following, depending on whether you want to modify a trigger or an automation:
   1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Triggers**.
   2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Automations**.
2. Locate the notification trigger or automation and select **Edit**.
3. Modify the action or actions as needed.

   The following placeholders insert ticket links in the email body: `{{ticket.link}}` or `{{ticket.id}}`. For information on working with placeholders, see [Using placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330).
4. Click **Update**.

For more information on editing triggers to remove ticket links, see [Removing tickets links from your notifications](https://support.zendesk.com/hc/en-us/articles/4408888722842#topic_nha_nls_yb).

If you provide support through email only, see [Setting up to provide email-only support](https://support.zendesk.com/hc/en-us/articles/4408888722842). The article describes how to remove links back to your Help Center that would prompt your end-users to attempt to sign in.
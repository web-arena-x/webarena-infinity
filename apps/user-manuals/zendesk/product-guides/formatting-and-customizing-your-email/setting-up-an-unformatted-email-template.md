# Setting up an unformatted email template

Source: https://support.zendesk.com/hc/en-us/articles/4408883361946-Setting-up-an-unformatted-email-template

---

The default formatting for Zendesk Support emails is nice if you're setup as a ticketing system. But what if you want your replies to look like a response from a normal person who writes plainly without formatting? Removing the extra formatting can be a hurdle. We hope to simplify this process for you today!

Changing a formatted email to an unformatted one is as easy as making a few changes in your Zendesk Support settings. For example, you can take an email that looks like this:  
![TotW_-_Email_w_default_formatting1.png](https://support.zendesk.com/hc/article_attachments/7856552871066)

and change it to something like this:

![TotW_-_Email_w_no_formatting.png](https://support.zendesk.com/hc/article_attachments/7856552871834)![](/attachments/token/9podPR5MWdY7YNxRmP0szmKJ4/?name=TotW+-+Email+w+no+formatting.png)

## Step 1: Update your triggers

By default, your triggers send out all the comments made in a ticket, separated by formatting. We'll work through deactivating unwanted notifications and removing the extra formatting.

### Deactivate the "Notify Requester and CCs of Received Request" trigger

An email interaction starts when a user first sends an email. A default trigger in Zendesk Support sends a response telling the customer that the system has received their request. You probably want to disable this trigger if you want your email responses to look personal.

**To deactivate the trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Triggers**.
2. Hover your mouse over the "Notify Requester and CCs of Received Request" trigger to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)).
3. Move your mouse over the options menu icon and select **Deactivate**, then confirm the deactivation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deactivate_trigger_with_callouts.png)

### Remove the formatting from the rest of your triggers

With the "Notify Requester and CCs of Received Request" trigger deactivated, you should have one or two remaining triggers that send email to your end-users. One is  "Notify requester and CCs of comment update.  *"*  If you have an older account, the other one is "Notify requester of solved request." If you added other custom notification triggers that send email to requesters, you'll want to modify them too to get rid of the formatting.

**To remove the formatting from outgoing emails from your remaining triggers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Triggers**.
2. Locate one of the remaining notification triggers and open the options menu as described above, then select **Edit**.
3. In the email template in the  **Perform these Actions**  section, clear the  **Email Subject**  field and enter {{ticket.title}} instead. The {{ticket.title}} placeholder adds the subject of the original email to your response. If you like, you can preface it with "Re: ".
4. Next, delete the email body and replace it with the following Liquid Markup syntax:  
     

   ```
   {% for comment in ticket.comments limit:1 offset:0 %}  
   {{comment.value_rich}}  
   {% for attachment in comment.attachments %}  
   {{attachment.filename}}  
   {{attachment.url}}   
   {% endfor %}  
   {% endfor %}
   ```

   This code takes the text of the last comment added to the ticket without any extra formatting. Be sure to add this to the top line of the trigger email body or the extra space will show up in your outgoing emails.
5. Review your work. Your trigger action should look something like the following:  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_action_remove_formatting_ex.png)
6. If everything looks good, click **Save**.

## Step 2: Update your follower notifications

If you have ticket followers enabled, followers receive notifications that are formatted in a way that's very similar to how triggers were set up originally. You'll need to edit this as well.

**To change the follower notification template**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Tickets > Settings**.
2. In the  **CCs and followers**section, find the **Follower email template**. If followers are not enabled for your tickets, you will not see this field.
3. Paste the same Liquid Markup code that you added to your triggers:  

   ```
   {% for comment in ticket.comments limit:1 offset:0 %}  
   {{comment.value_rich}}  
   {% for attachment in comment.attachments %}  
   {{attachment.filename}}  
   {{attachment.url}}   
   {% endfor %}  
   {% endfor %}
   ```
4. Click **Save tab**.

## Step 3: Update your email template

There's one other place that affects the formatting of your outgoing emails: your overall email template. This template is applied to all outgoing emails from your Zendesk account.

**To remove the formatting from the email template**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Channels** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)) in the sidebar, then select **Talk and email > Email**.
2. Click **Edit email templates**.
3. If you still have the default template, it should look as follows. If you have customized the template, you can click  **Revert to default**  to get it back.
4. Remove the following elements:  
   - the {{footer}} placeholder
   - the {{footer\_link}} placeholder
   - any extra text or links left in the box.
   - the email delimiter

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/delimiter_and_footer_elements_email_callouts.png)  
   (Open image in new tab to enlarge)

   Leave the {{content}} placeholder in the template. It populates the email with the comments you add.
5. Remove the entire line immediately below and above the {{footer}} placeholder. This <div style...> code adds a line break to the email.

For more information on what each of these placeholders do and how to customize the template, see  [Customizing your templates for email notifications.](https://support.zendesk.com/hc/en-us/articles/4408886168090-Customizing-your-email-templates "Customizing your email templates")

## Step 4: Change the "From" field

Finally, if you want to change the sender specified in the "From" line, you can to go back to  **Admin > Channels > Email > Edit email templates**. There are two places where you can change this.

First, you may want to set up a support address to customize what email address your end-users use to send requests. Otherwise you'll be communicating with your customers with a "@[subdomain].zendesk.com" address. To set up your own email to forward emails into Zendesk Support and then send emails out at that same address, you'll need to configure your external email address appropriately. For instructions, see [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698) .

After setting up the email you want to use, you'll want to take a look at your support addresses. Make sure they're configured like you want them. You can remove any mention of the company after the agent's name by removing it in your Support Address options. For more information, see  [Adding support email addresses for users to submit tickets.](https://support.zendesk.com/hc/en-us/articles/4408842868506)

Next, you'll want to check out the [Personalized email replies](https://support.zendesk.com/hc/en-us/articles/4408887209498) option. When enabled, the "From" field includes the name of the agent making the comment on the ticket. This replaces your company name in your responses.

Congratulations! You removed all formatting from your ticket email notifications. You can now have smooth email conversations without your customers knowing that you're using Zendesk Support.
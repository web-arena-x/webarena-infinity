# Enrolling Sell leads and contacts in sequences

Source: https://support.zendesk.com/hc/en-us/articles/4408844143130-Enrolling-Sell-leads-and-contacts-in-sequences

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

Note: Each Sell user that enrolls a lead or contact in a sequence that contains an email must have already integrated their email account into Sell (see [Integrating email with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821242266)).

In Sell, you can engage leads (prospects) or contacts by automatically sending them emails at intervals using an email sequence.

A sequence is a series of actions that specify how and when sales reps contact new leads. In other words, it is a series of contact attempts and the spacing of time between them. For example, you might send an introductory email on day one, a follow up email on day three, and an extra promotional email on day five. As soon as a lead or contacts answers one of the emails, or the lead is converted to a contact, the sequence ends and no further emails are sent.

After your Sell admin has set up a sequence in Sell, you can start enrolling leads or contacts into a sequence (see [Setting up email and task sequences in Sell](https://support.zendesk.com/hc/en-us/articles/4408842857370)).

Before you add a lead or contact to a sequence, ensure that your leads and contacts have their full contact information recorded on their Leads or Contacts page, as this ensures the sequence can proceed using accurate information. You can [use Sales Engagement Tools (Reach) to enrich your existing leads](https://support.zendesk.com/hc/en-us/articles/4408830786202).

You need update permissions in Sell to add or remove a lead or contact from a sequence.

Note: You also have the option of managing lead and contact sequences via the Sequence Enrollments API, and through Zapier (see [Managing leads and contacts in sequences via the API and Zapier](https://support.zendesk.com/hc/en-us/articles/4408819642138)).

This article covers the following topics:

- [Starting a sequence for a lead or contact](#topic_l2v_4kt_fqb)
- [Bulk starting a sequence for leads or contacts](#topic_c5f_pkt_fqb)
- [Viewing a sequence for a lead or contact](#topic_tf4_pkt_fqb)
- [Viewing sequences and scheduled emails in a leads or contacts smart list](#topic_vty_pkt_fqb)
- [Identifying emails sent to a lead or contact using a sequence](#topic_khj_qkt_fqb)
- [Stopping a sequence for a lead or contact](#topic_k4t_qkt_fqb)

Related articles:

- [Setting up email sequences in Sell](https://support.zendesk.com/hc/en-us/articles/4408842857370)
- [Managing leads and contacts in sequences via the Zendesk API and Zapier](https://support.zendesk.com/hc/en-us/articles/4408819642138)
- [Best practices for preventing your Sell email messages from being flagged as spam](https://support.zendesk.com/hc/en-us/articles/4408830566298)

## Starting a sequence for a lead or contact

You can select a sequence from the list, and add the current lead or contact to that sequence.

**To add a lead or contact to a sequence**

1. On the sidebar in Sell, click **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)) or **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), and choose a specific lead or contact.
2. On the **Sequences** widget, click **Add** (**+**).

   If there are no sequences available, this means that your admin has not set up a sequence yet (see [Setting up email and task sequences in Sell](https://support.zendesk.com/hc/en-us/articles/4408842857370)).

   Tip: Sell admins can customize visible widgets and their order in **Settings > Customize > Layouts**.
3. Click to select one of the available sequences, or use the search to find the name of the sequence you want.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_select_sequence.png)

   As you select a sequence, you'll see information about when the first task is created or automated email is due to be sent to the lead or contact.

   If a lead or contact with the same email address is already active in this sequence, you'll see a notification, and will not be able to add the lead or contact again.
4. Click **Next** to preview steps in the selected sequence.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_selected_sequence.png)
5. Click **Start sequence**. The lead or contact is now active in the sequence, and will receive emails or tasks according to that sequence. All emails to the lead or contact will be sent from you (the rep who added the lead to the sequence).

   Note: If your lead or contact does not have the information required by the email template merge tags, you'll see it in the email preview. Make sure all of the contact information for the lead or contact is recorded on their Leads or Contacts page. This ensures the sequence proceeds using accurate information. If you don't add this information, your leads and contacts won't get emails from the sequence (see [Using merge tags in your email messages](https://support.zendesk.com/hc/en-us/articles/4408828807066)).

   As soon as a lead or contact responds to an email, or a lead is converted to a contact, the sequence ends.

## Bulk starting a sequence for leads or contacts

You can start a sequence for multiple leads or contact at once.

**To add multiple leads or contact to a sequence at the same time**

1. On the sidebar, click **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)) or **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)).
2. Using either the **Index** or **Table** views on the **Leads** or **Contacts** page, select the checkbox next to the name of the lead or contact. If you want to select all items in a view, select the **Select All** checkbox at the top of the list.
3. When you’ve selected all the leads or contacts you want to add to a sequence, click **Sequence**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequence_bulk.png)

   If there are no sequences available, this means that your admin has not yet set up a sequence (see [Setting up email and task sequences in Sell](https://support.zendesk.com/hc/en-us/articles/4408842857370)).
4. Select one of the available sequences, or use the search to find the name of the sequence you want.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_select_sequence.png)

   As you select a sequence, you'll see information about when the first task will be created or automated email is due to be sent to the lead or contact.
5. Click **Start sequence**. The selected leads or contacts are now active in the sequence, and will receive emails or have tasks created according to that sequence. All emails to the lead or contact will be sent from you (the rep who added the lead or contact to the email sequence).

   Note: If your lead or contact does not have information required by the email template merge tags, you'll see it in the email preview. Make sure that your leads and contacts have full contact information recorded on their Leads or Contacts page, as this ensures the sequence can proceed using accurate information. If you don't add this information, your lead or contact won't get any emails from the sequence (see [Using merge tags in your email sequences](https://support.zendesk.com/hc/en-us/articles/4408828807066)).

   As soon as a lead or contact responds to an email, or a lead is converted to a contact, the sequence ends.

## Viewing a sequence for a lead or contact

You can view the sequences for each lead or contact from the **Sequences** widget. This allows you to understand if a lead or contact is, or was, enrolled in a sequence, and the sequence progress for an active sequence.

**To view a sequence for a lead or contact**

1. On the sidebar, click **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)) or **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), and choose a specific lead or contact.
2. On the **Sequences** widget, click **Add** (**+**).

   You'll see a summary of the number of active, blocked, and completed sequences for that lead or contact, and a list of all the sequences.

   If there are more than five sequences available, you can scroll to see more sequences.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequences.png)

   Each sequence provides the following information:
   - The sequence name.
   - The sequence state (active, blocked, or completed).
     - If the sequence is **active**: it will show the step that was last completed for the lead or contact, and when the next scheduled email will be sent.
     - If the sequence is **blocked**: it shows the number of steps, and the reason the sequence is blocked. A sequence might be blocked if the email couldn't be delivered, because your email quota has been reached, or because there is a problem with your email settings.
     - If the sequence is **completed**: it shows the date the sequence was completed for that lead or contact, and the number of steps that were completed

For active and blocked sequences, you can view which emails and tasks are still scheduled for the future by clicking on the sequence name in the widget.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_active_sequence_preview.png)

In the sequence preview, you can retry steps that could not be completed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequence_first_step.png)

## Viewing sequences and scheduled emails in a leads or contacts smart list

You can view the sequences for multiple leads or contacts.

1. In the Leads or Contacts smart list, refer to the **Ongoing Sequences** and **Completed Sequences** columns.

   This shows you the leads or contact that are, or were, enrolled in a sequence, as well as the leads or contacts that have not been added to any sequence.
2. (Alternatively) You can use the **Next Email** column to view the next scheduled email for any lead or contact in your Leads or Contacts smart list (see [Creating and using smart lists](https://support.zendesk.com/hc/en-us/articles/4408827735066)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequences_smart_lists.png)

## Identifying emails sent to a lead or contact using a sequence

When an email is sent to a lead or contact using a sequence, you can see this correspondence type in the activity feed of the lead or contact.

**To view an email sent using a sequence**

1. On the sidebar, click **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)) or **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), and choose a specific lead.
2. Go the **Activity feed** section.

   Any emails sent using a sequence are identified with a **Sequence** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_send.png)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequences_in_feed.png)
3. Click the email to see the content of the email that was sent to the lead or contact.

## Stopping a sequence for a lead or contact

You can stop a sequence for a lead or contact using the **Sequences** widget if, for example, they've contacted you and asked to be removed from one or more sequences.

All sequences are automatically stopped for a lead or contact if any of the following events occur:

- The lead or contact emails you in response to an email sent by the sequence
- The lead is converted to a contact in Sell
- The lead or contact is deleted in Sell

**To stop a sequence for a lead or contact**

1. On the sidebar, click **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_leads.png)) or **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)), and choose a specific lead or contact.
2. On the **Sequences** widget, hover over the sequence that you want to stop. If there are more than five sequences available, you can scroll to see more sequences.
3. Click **X** to stop the sequence.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_Stop_sequence.png)

   The sequence is stopped immediately, and the lead or contact will not receive any scheduled or future emails from the email sequence, and any subsequent tasks in the sequence will not be created.
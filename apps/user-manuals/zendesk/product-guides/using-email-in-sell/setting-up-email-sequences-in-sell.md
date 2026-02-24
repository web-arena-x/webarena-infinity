# Setting up email sequences in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408842857370-Setting-up-email-sequences-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

Note: Each Sell user that enrolls a lead or contact in a sequence that contains an email must have already integrated their email account into Sell (see [Integrating email with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821242266)). See [Sales engagement automation limits (Reach)](https://support.zendesk.com/hc/en-us/articles/4408827866266) for the maximum limits for sales engagement automation.

You can set up an email sequence to engage leads (prospects) and contacts by automatically sending them emails at intervals. A sequence is a series of actions that specify how and when sales reps contact new leads and contacts.

Sequence emails are created using a template. This mean you need to specify a number of suitable email templates to send to leads or contacts before setting up an email sequence.

To set up email sequences in Sell, you need admin rights.

This article covers the following topics:

- [Creating a sequence](#topic_d13_ctp_2qb)
- [Monitoring a sequence](#topic_xxn_dtp_2qb)
- [Changing a sequence](#topic_ycy_ctp_2qb)
- [Deleting a sequence](#topic_c1f_2tp_2qb)

Related articles:

- [Sending an email and task sequence to leads and contacts in Sell](https://support.zendesk.com/hc/en-us/articles/4408844143130)
- [Managing leads and contacts in sequences via the Zendesk API and Zapier](https://support.zendesk.com/hc/en-us/articles/4408819642138)
- [Best practices for preventing your Sell email messages from being flagged as spam](https://support.zendesk.com/hc/en-us/articles/4408830566298)

## **Creating a sequence**

To use a sequence, you need to specify the frequency of contact and the steps involved, including the type of correspondence (for example automated email or steps in a task). You can also name each task in the steps of the sequence. It could be something specific (for example: *Call Contact*, *Send Follow Up Email,* or *Connect on LinkedIn*) or it could be something as generic as *Research Lead*.

For the steps that have tasks, the sequence automatically progresses to the next step when the task for the previous step has been marked as completed.

**To set up a sequence**

1. On the sidebar in Sell, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click **[Business Rules > Sequences](https://app.futuresimple.com/settings/sequences/leads)**.

   You'll see all of your existing sequences that you have configured.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequences_reach_leads_contacts.png)
2. Click **Add sequence**.
3. Give your new lead or contact sequence a name.

   Note: Use a meaningful name as this will be used by sales reps to find the correct sequence, when they add leads and contacts.
4. Read the preset rules for sending out emails in the sequence:

   - Any user can enroll leads and contacts into a sequence.
   - Emails are sent to leads and contacts on behalf of the user who enrolled them.
   - Emails are sent on weekdays (Monday, Tuesday, Wednesday, Thursday, Friday), and weekends (Saturday and Sunday) are ignored.
   - When a lead or contact replies to an email, or a lead is converted to a contact, the sequence stops and the lead or contact does not receive any more emails.
5. Click **Add step**.

   Your automated emails will be sent in the order that you define them in your steps (although you can reorder the steps before you save the sequence).
6. Choose the email template that you want to use for this step, or [create a new template](https://support.zendesk.com/hc/en-us/articles/4408821812890).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lead_sequence_select_template.png)
7. Specify when you want the email to be delivered.

   For the first step, you may want to send the email immediately, so the email is sent as soon as a lead or contact is enrolled in the sequence. If this is a follow-up step, specify a wait time.

   The first step doesn't have to happen immediately upon enrollment as it depends on the sequence. The first action starts immediately, when the lead or contact is enrolled in a sequence, then the next step goes out precisely at the cadence that you've set it to. For example, if it is set to go out one day after, then the second step will go out 24 hours after the first one.

   Note: The wait time for a task is specified in weekdays (Monday to Friday), because weekends (Saturday and Sunday) are ignored when calculating the wait time. You can also set the time, in hours, for tasks in a step to be completed, or to send an email.
8. (Optional add an unsubscribe link to emails) To avoid your email being labelled as spam, it's good practice to include an unsubscribe link in any automated communication, such as email sequences. Including an unsubscribe link is also required by law in some jurisdictions. To include an unsubscribe link:

   - Select the checkbox for **Add an unsubscribe link to all emails in this sequence**.
   - Click the **Unsubscribe link language** dropdown menu and choose the language you want to use for the unsubscribe message.

     The unsubscribe link will be added, in the selected language, to the bottom of each email sent in a sequence.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_unsubscribe_language.png)

   Note: It's good practice to only allow your users to click the unsubscribe link in an email, otherwise it may lead to unsubscribing your leads or contacts.

   When an email recipient clicks Unsubscribe, they'll see an unsubscribe confirmation and will be excluded from any ongoing and future sequences. To avoid sending unwanted email messages, if you accidentally add the recipient to a sequence or try to send them an email, you'll be notified that the recipient has unsubscribed. You can check when a given recipient unsubscribed by hovering your cursor over the unsubscribe icon next to the recipient's email.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_unsubscribed.png)
9. To ensure all information is correct, preview the email template that will be sent in a step.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sequence_step_configuration.png)

   Note: Shared email templates are available for everyone in your team to use, also for one-off emails. You can [share a template](https://support.zendesk.com/hc/en-us/articles/4408821812890-Creating-and-using-email-message-templates#topic_o2c_t24_5lb__section_axt_kf4_5lb) by editing it (see [Setting up a shared email template in Sell](https://support.zendesk.com/hc/en-us/articles/4408825504026)).
10. Click **Add step** to include another step, and repeat the process for each step in your sequence. For follow-up steps, you can choose if you want the email to be sent as a reply to the previous step or to start a new email thread.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequence_step_configuration_reply.png)

    You can also add a task as a step at any point and define when the task is due (for example, after the previous step has been completed). To change the sequence order, drag and drop the steps.
11. Click **Save sequence** to save your sequence.

    You'll see your new sequence on the **Reach - sequences** page, including information about the number of steps in the sequence, any enrolled leads or contacts, and the creator of the sequence.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_Sequence_task.png)

    After you've created an email sequence, any Sell user in your account can use it to engage with their leads or contacts (see [Sending an email sequence to leads and contacts in Sell](https://support.zendesk.com/hc/en-us/articles/4408844143130)).

## **Monitoring sequence usage**

To get the most out of sequence workflows, you can view usage and performance statistics for each sequence.

**To view sequence statistics**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click **[Business Rules > Sequences](https://app.futuresimple.com/settings/sequences/leads)**.

   On the **Reach - sequences page**, you'll see all of the existing lead and contact sequences you've configured.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequences_reach_leads_contacts.png)
2. Click the name of the sequence you want to edit to open it.

   You can see usage statistics for that sequence:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_sequence_stats.png)

   - **Active**: How many leads or contacts are currently active in the sequence.
   - **Completed**: How many leads or contacts have already completed the sequence.
   - **Reply rate**: What percentage of leads or contacts, who completed the sequence, replied to any of the sequence emails. To see the exact sum of the leads or contacts who replied, hover your cursor over the reply rate.

## Changing a sequence

You can edit an existing sequence if you need to change some of the details.

**To edit or change a sequence**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Business Rules > Sequences](https://app.futuresimple.com/settings/sequences/leads)**.

   The **Reach - sequences** page, lists all of the existing lead and contact sequences that you've configured.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/reach_lead_sequences_change.png)
2. Click the name of the sequence you want to edit to open it.

   If the sequence is in use (it has active leads or contacts enrolled in the sequence) then you'll receive a warning specifying the number of leads that'll be affected if you edit the sequence. As a Sell admin, if you don't want existing leads or contacts to be affected by changes in a sequence, you must create a new sequence. When you edit the sequence, any enrolled leads or contacts will follow the changes from after the next step (the step after the one that is scheduled).
3. From the lead sequence editing page you can:
   - **Change the sequence name**: Click the sequence name to change it. This doesn't affect the sequenced leads and contacts.
   - **Reorder the email sequence steps**: Drag and drop the steps to change their order.
   - **Add a step**: Click **Add step** to add a new step to the sequence, specify an email template, and time delay for the step.
   - **Change a step**: Click **Edit** on a specific step to open the dialog to change the email template and time delay for the step.
   - **Remove a step**: Click **Edit** on a specific step and click **Delete** to remove the step.

   Any new leads or contacts that start the sequence after your changes have been applied will follow the new email sequence. All active leads and contacts that had started the sequence before your edits were applied, will continue the existing sequence without your changes being applied to them.

   Note: Changes you make to email template content are immediately applied to all sequences in which the edited template is used.
4. Click **Save** to keep your edited email sequence.

   You'll see your edited sequence on the Reach - sequences page, including information about the number of steps, and the creator of the sequence.

## Deleting a sequence

You can delete a sequence from the Reach - sequences page. When you delete a sequence, it is permanently removed.

**To delete a sequence**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Business Rules > Sequences](https://app.futuresimple.com/settings/sequences/leads)**.

   On the **Reach - sequences** page, you'll see all of the existing lead and contact sequences that you have configured.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/reach_lead_sequences_change.png)
2. Click **Trashcan** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) to delete the sequence.

   If the sequence is currently in use (that is, it has active leads or contacts enrolled in the sequence), you'll see a warning specifying the number of leads or contacts that will be affected if you proceed to delete the sequence. If you delete the sequence, it is deleted immediately and the enrolled leads or contacts will not receive any new emails as part of that sequence.
3. Click **Delete** to confirm.

   Your sequence is permanently deleted and no longer appears on the Reach - sequences page.
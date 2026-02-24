# Complying with Privacy and Data Protection Law in Zendesk Talk

Source: https://support.zendesk.com/hc/en-us/articles/4408821829402-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-Talk

---

This guide describes how certain features and functionality in Zendesk Talk can
assist with your with your obligations under privacy law. Users in Zendesk
Talk are managed in Zendesk Support.

To learn more about meeting your obligations in other Zendesk products,
see [Complying with Privacy and Data
Protection Law in Zendesk products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

In this guide, *users* can be End-Users or Agents as the terms are defined
in the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

Topics covered in this guide:

- [Meeting an access obligation](#topic_qdm_yhk_gs)
- [Meeting a correction obligation](#topic_ezm_pcv_4v)
- [Meeting an erasure obligation](#topic_p3p_zhk_gs)
- [Meeting a data portability obligation](#topic_ekz_13k_gs)
- [Meeting an objection obligation](#topic_gcn_swl_ycb)
- [Disclaimer](#topic_hxw_bzf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you may
have an obligation to inform an end user or agent where their personal data is being
held and for what purposes.

If an end user requests their personal data, you can export the data from
Zendesk as described in [Meeting the data portability
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ekz_13k_gs) in the article for Zendesk
Support.

## Meeting a correction obligation

Individuals from certain regions have a *right to rectification*, or the right to have
inaccuracies in their personal data corrected. On request, you may have an
obligation to provide the individual with their personal data and fix inaccuracies
or add missing information.

See [Meeting the correction
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ezm_pcv_4v) in the article for Zendesk
Support.

## Meeting an erasure obligation

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or
deleted. On request, you may have an obligation to delete the personal data of an
individual.

The workflow for deleting the personal data of an end user or agent is as
follows:

1. Delete personal data from any Talk tickets.
2. Delete the end user or agent from Zendesk Support.

The order of operations is important because user data might be required
to find the tickets containing personal data.

**To delete personal data from tickets**

Personal data may be contained in Talk tickets in Zendesk Support. To
delete personal data in tickets, see [Meeting the erasure
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_p3p_zhk_gs) in the article for Zendesk Support.

Personal data may also be contained in the call recordings of Talk
tickets. See the following topics in this guide:

- [Deleting call recordings](#topic_lbr_pfj_1db)
- [Getting an audit log of deleted call recordings](#topic_p1s_x5g_ddb)

**To delete the end user or agent**

After deleting personal data from any tickets, you can delete the end
user or agent as described in [Meeting the erasure
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_p3p_zhk_gs) in the article for Zendesk Support.

When an end user is deleted in Zendesk Support, the user's phone number
is scrubbed from the Call History page, the Text History page, the
Call History csv file, and the Call Monitoring csv file. Recordings
and personal data are also scrubbed from Zendesk Talk’s service
provider, Twilio.

The end user's associated personal data is also removed from Insights.
Phone numbers still exist in Insights in the following two
scenarios:

- Calls routed to an external number through an IVR menu
  option
- Calls transferred to an external number

In both scenarios, the phone numbers are not associated to an end-user
profile.

Not all personal data is scrubbed if an end user is on a call when you
delete the end user. Make sure the user has ended any call before
deleting them.

### Deleting call recordings

An administrator can manually delete call recordings from
tickets. You can also configure Zendesk Talk to
automatically delete live call recordings or voicemails
after a certain amount of time. A third option is to delete
the tickets containing the call recordings.

**To manually delete a call recording from a ticket**

1. In Zendesk Support, select the ticket with the recording.
2. Next to the recording, click **delete recording**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_delete_recording.png)

   Important: Once deleted, the recording will be permanently removed from the ticket and cannot be recovered. The deletion will not be noted in the ticket events log.
3. Click **OK**.

**To automatically delete call recordings after an
interval**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Click the line you want to automatically delete recordings for.
4. In the **Call recording** tab, select a timeframe for live call recordings in the
   **Automatic deletion** field.
5. Click **Save changes**.

**To delete tickets containing the call recordings**

Permanently delete the ticket as described in [Meeting the erasure
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_p3p_zhk_gs) in the article for
Zendesk Support.

When you permanently delete a ticket in Zendesk Support, any call
recording is also deleted. The recording is soft deleted at
first, then hard deleted automatically 7 days later. The
call recordings are also deleted from Zendesk Talk’s service
provider, Twilio.

### Getting an audit log of deleted call recordings

**Viewing who deleted a call recording**

Note: The audit log is only available with Enterprise and Enterprise Plus plans.

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
  **Account** in the sidebar, then select **Logs > Audit log**.

A deleted call recording appears as a separate entry with the
name of the admin who deleted the recording and the ID of
the ticket to which the recording was associated.

The audit log looks as follows when a call recording was deleted
as part of the ticket being deleted:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/audit_log_deleted_call.png)

## Meeting a data portability obligation

Individuals from certain regions have a *right to data portability*. On request, you may
have an obligation to provide an individual with their personal data or to transmit
the data to another organization.

To export an agent's or end user's personal data, see [Meeting the data portability
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ekz_13k_gs)[Meeting the data portability
obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ekz_13k_gs) in the article for Zendesk
Support.

You can also export the account's call history or monitoring history
(Professional and above) as a CSV file. See the following topics in
this guide:

- [Exporting the call history](#topic_jn3_gqg_ddb)
- [Exporting the monitoring history](#topic_ald_rrg_ddb)

### Exporting the call history

Note: If you delete an end user or agent, the personal data
associated with that user won't be available in the exported
call history. Only the record of the call will
remain.

**To export the call history**

1. Sign in to Zendesk Support as an
   admin.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
3. Select the **History** tab.
4. Specify a date range. The current
   month is chosen by default.
5. Click **Export CSV**.
6. Check your email for a link to
   download the CSV file.

### Exporting the monitoring history

Note: If you delete an end user or agent, the personal data
associated with that user won't be available in the exported
monitoring history. Only the record of the call will
remain.

This feature is only available on Professional and above.

**To export the monitoring history**

1. Sign in to Zendesk Support as an admin.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
3. Select the **History** tab.
4. Specify a date range.
5. Click **Export Monitoring CSV**.
6. Check your email for a link to download the
   CSV file.

## Meeting an objection obligation

Individuals from certain regions have a *right of objection*, or the right to object to
direct marketing. You may have an obligation to stop processing personal data for
direct marketing purposes when you receive an objection from an individual.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.
# Forwarding an email message to your support address

Source: https://support.zendesk.com/hc/en-us/articles/4408836514202-Forwarding-an-email-message-to-your-support-address

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

If your customers occasionally send support requests to your email address instead of your
support address, you can forward the email to the support address. By forwarding the email, a
ticket is created with the original sender set as the requester. It also creates a new account
if the user isn't registered.

When you forward the email, the sender becomes you, not the original sender. Normally, the
process creates a ticket listing you as the requester. However, you can use one of the
following solutions to set the correct requester on the ticket:

- [Enabling the forwarding option for agents in Zendesk Support](#topic_ipd_hvd_55b)
- [Specifying the requester in the forwarded email](#topic_hqg_3vd_55b)

Use this article if you want to handle the occasional email yourself. If you want to forward
all emails sent to an email address (not just the occasional one), see [Forwarding incoming email from your existing email address to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698).

Note: [Light agents](https://support.zendesk.com/hc/en-us/articles/4408846501402) can use agent email forwarding to forward an email to
your support address, which creates a ticket with a private comment. They cannot use agent
email forwarding to create a ticket with a public comment.

Tip: To troubleshoot email forwarding and customer ticket
replies not displaying in Zendesk, see [Customer emails don't show up in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408833552282-Customer-emails-don-t-show-up-in-Zendesk).

## Enabling the forwarding option for agents in Zendesk Support

Your administrator can enable an option that lets you forward an email in your inbox to
your support address to create a ticket on behalf of the original sender.

Forwarding works for ticket creation, not ticket updates. Once a ticket has been created,
users should reply directly from their email notifications.

Forwarding is only configured to look at the From field in the body of the forwarded
message. When an agent forwards an email and forwarding is enabled in the account, the
forwarded email will not contain the original list of CCs (copied users) that may have been
included on the ticket notifications.

When a non-restricted agent creates a ticket using agent forwarding, the ticket is
unassigned. When a restricted agent creates a ticket using agent forwarding, the ticket will
initially be assigned to their default group. Any group routing that would normally occur as
a result of the requester's organization is ignored.

Note: Your email address must be registered in your user profile. This
feature is supported for email clients in western European languages, Hebrew, and
Chinese.

**To enable the forwarding option**

1. Log in as an administrator.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
3. Scroll down to the **Email forwarding** section and then select **Enable email
   forwarding**.
4. Click **Save**.

Agents can add public comments to the ticket by replying to the email. To add private
comments, agents can type the comment above the **Forwarded message** line.

Note: The
inclusion of a comment or internal note when forwarding a ticket suppresses the
*Autoreply with articles*, *Autoreply*, and *Internal note* trigger
actions when the ticket triggers run as a result of that ticket update.

## Specifying the requester in the forwarded email

This solution works for all email clients. It involves inserting a simple instruction in
the email body that specifies the requester. When creating the ticket, Zendesk Support reads
the instruction and sets the requester you specified.

The solution works only if you're an agent and your email address is registered in your
account. The command is ignored if the email is forwarded by an end-user. For more
information, see [Updating ticket properties from your inbox](https://support.zendesk.com/hc/en-us/articles/4408839419034).

1. Select the email in your inbox and click **Forward**.
2. Enter the following instruction at the top of the email body:

   ```
   #requester {requester_email}
   ```

   where
   `{requester_email}` is the requester's email address.
   Example:

   ```
   #requester gerry5@yahoo.com
   ```

   **Tip**:
   You can copy the requester's address from the Forwarded Message section in the
   body.
3. Clean up the email. For example, remove the FWD prefix in the subject line and the
   Forwarded Message header in the body.

   The requester instruction will be stripped from
   the ticket automatically.
4. Enter your support address in the To field and click **Send**.
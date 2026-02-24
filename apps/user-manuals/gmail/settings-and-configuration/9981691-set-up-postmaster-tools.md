# Set up Postmaster Tools

Source: https://support.google.com/mail/answer/9981691

---

Monitor outgoing email to Gmail accounts

Use Postmaster Tools to monitor information about outgoing email that you send to personal Gmail accounts, and about the domains and IP addresses you use to send email. The information in Postmaster Tools helps you meet Gmail’s requirements for sending email to personal Gmail accounts, described in our [Email sender guidelines](/a/answer/81126) and [Email sender guidelines FAQ](/a/answer/14229414).

Postmaster Tools dashboards have detailed information about spam rate, reputation, message authentication, and delivery errors. For details about each dashboard, visit [Postmaster Tools dashboards](/a/answer/14668346).

To use Postmaster Tools, you must have a [Google Account](/accounts/answer/27441) or a [Google Workspace account](/a/answer/6365252).  Data in Postmaster Tools only applies to messages sent to personal Gmail accounts. A personal Gmail account is an account that ends in @gmail.com or @googlemail.com.

## Set up Postmaster Tools

Follow these steps to set up Postmaster Tools for your domains. Keep in mind:

- To see dashboards for subdomains independently from the primary domain, add the subdomains to Postmaster Tools in the same way you add a primary domain. We recommend you add subdomains after adding and verifying the primary domain. If the primary domain is verified, you don’t need to verify its subdomains.
- To set up Postmaster Tools access for multiple accounts for a domain, set up separate DNS verification records for each account.

### Step 1: Add your sending domain to Postmaster Tools

Add either the DKIM (d=) domain or the SPF (Return-Path) domain. If the DKIM and SPF domains are the same, Postmaster Tools will use messages signed by SPF, DKIM, or both, for dashboard data.

1. Sign in to [Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. In the bottom right, click Add ![Add](//lh3.googleusercontent.com/ki2XH4GrUtraIQUMATZ9-8qDgRw6mAKajvRn9qZWYCR1ThUfZhGOJ56wIkfYP6BGc0c=w36-h36).
3. In the **Getting starte**d window, enter the domain used to authenticate outgoing email with SPF, or DKIM, or both.
4. Click **Next** to open the **Verify your domain** window.

### Step 2: Verify your sending domains

You can skip this step and continue setup without verifying your domain, but Postmaster Tools won’t display information about your email until your domain is verified. To skip this step, click **Not now**.

You’ll log into your domain provider’s management console in this step, so you may want to open it in another browser tab. [Get help with domain verification](/a/answer/60216)

1. In the **Verify your domain** window, copy the text in the **TXT record** field.
2. Log into your domain provider and add the copied text to your domain’s DNS records. For detailed steps, visit [Verify your domain (host-specific steps)](/a/topic/1409901).
3. Return to the **Verify your domain** window and click **Verify**.  
   Typically domains are verified right away but it might take up to 10 minutes before your domain’s verification status is updated.

After you click **Verify** or **Not now**, the domain appears on the Postmaster Tools domains page.

### Step 3: Give others access to your Postmaster Tools dashboards (optional)

To let other people access Postmaster Tools dashboards for your domains, add them to the domain in Postmaster Tools. You can add users to verified domains only, and they must have a Google or Google Workspace account.

1. From the **Manage Domains** page, to the right of the domain name, click **More** > **Manage**
2. On the bottom right, click **Add**.
3. In the window, enter the Google email address of the person you’re adding to the domain.

People aren’t notified when you give them access to your domain, so we recommend you let them know. When they log in to Postmaster Tools, they’ll see the domains they have access to on the Manage Domains page.

People who don't have domain access get this message when they try to open a dashboard:

*You are not authorized to view data for this domain. Please ensure you have verified yourself as an owner, or an owner has granted you read access.*

Now you're ready to monitor your outgoing email with the [Postmaster Tools dashboards](/a/answer/14668346).

## Troubleshoot Postmaster Tools setup

Here are recommended actions for issues that might occur during Postmaster Tools setup.

| Issue | Possible causes | Recommended actions |
| --- | --- | --- |
| I can’t verify a domain. | Postmaster Tools couldn’t connect to the DNS server for the domain.  The verification DNS CNAME record was not found for your domain. | Wait a few minutes to let Google get your changes to the CNAME records.  Check that the domain verification string is correct in the DNS records for the domain.  Try to verify the domain again, with a new string. |
| I can’t give people access to my domain. | The person doesn’t have a Google account. | Make sure the person you’re trying to add has a Google account and you’re using the email address associated with that account. |
| I don’t see the expected data for my domain in one or more dashboards. | Data might be missing if the total number of messages for a given day is too low. This is to protect users' privacy. | Check the dashboards again when your email sending volume increases enough to populate the dashboards.  Follow these best practices for sending email:   - Send email only to recipients who want to get messages from you. - Make sure recipients opt in to get messages from you. - Confirm each recipient's email address before subscribing them. - Periodically send messages to confirm that recipients want to stay subscribed. - Consider unsubscribing recipients who don’t open or read your messages. - Make it easy to unsubscribe. - Use the feedback ID to identify the types of message that are most often marked as spam by recipients. |

## Was this helpful?

How can we improve it?

YesNo

Submit
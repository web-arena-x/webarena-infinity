# Guidelines for reviewing suspended tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408832102042-Guidelines-for-reviewing-suspended-tickets

---

Review your queue of suspended tickets on a regular basis. Follow review guidelines like the ones suggested below. The guidelines vary depending on how your instance of Zendesk Support is set up.

You can review suspended emails one-by-one or in bulk. The choice depends on your policy and the volume of suspended emails to be recovered or deleted. When reviewing emails in bulk, recovering them creates a batch of tickets. When reviewing emails one by one, you have the option of recovering each email automatically or manually. The automatic recovery option creates the ticket immediately. The manual recovery option lets you edit the ticket properties before it's created. For step-by-step instructions, see [Viewing, recovering, and deleting suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408893392922)

Tip: The export feature is helpful when reviewing a large number of suspended tickets and following the guidelines in this article. See [Using export to analyze suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408893392922#topic_v5w_wgd_s5b) for more information.

This article contains the following topics:

- [Review guidelines for an open Zendesk Support instance](#topic_j3v_kn3_h1b)
- [Review guidelines for a closed or restricted Zendesk Support instance](#topic_p3v_kn3_h1b)

Related articles:

- [Understanding and managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146)
- [Setting up suspended ticket notifications](https://support.zendesk.com/hc/en-us/articles/4408834669082)
- [Authenticating incoming email using DMARC](https://support.zendesk.com/hc/en-us/articles/4408821985818)

## Review guidelines for an open Zendesk Support instance

Anybody can submit tickets when using open support. You may or may not require them to register first. If they have to register, the first ticket is suspended while a welcome email is sent to the new user requiring them to register before the ticket can be submitted.

**Guidelines if you don't require users to register**

1. Recover emails that should be tickets. In particular, look for the following cases:
   - Ticket notification replies with the encoded ID stripped out (cause of suspension in the **Suspended Tickets** view: "User does not have authority to update the ticket")
   - Spam emails that aren't spam (cause of suspension: "Detected as spam")
   - Emails that did not pass Zendesk's DMARC authentication (cause of suspension:
     "Failed email authentication")
2. Bulk delete any remaining emails.

**Guidelines if you require users to register**

1. Recover tickets from users who haven't registered yet. Recovering the ticket also registers the user. To identify the emails, look for the following cause of suspension in the **Suspended Tickets** view: "User must sign up to submit email, user notified." Note that the user's email remains unverified until the user responds to the welcome email sent to them.
2. Recover other emails that should be tickets. In particular, look for the following cases:
   - tickets that registered users submitted through the web form while logged out (cause of suspension: "Submitted by registered user while logged out")
   - ticket notification replies by registered users from unverified addresses (cause of suspension: "Submitted by unverified user")
   - ticket notification replies by registered users with the email token stripped out (cause of suspension: "Permission denied due to unauthenticated email update")
   - spam emails that aren't spam (cause of suspension: "Detected as spam")
   - Emails that did not pass Zendesk's DMARC authentication (cause of suspension:
     "Failed email authentication")
3. Bulk delete any remaining emails.

## Review guidelines for a closed or restricted Zendesk Support instance

Only designated persons can submit tickets directly in closed or restricted support. You may have a suspended ticket workflow in place to let anonymous users submit tickets indirectly. When a support request from an anonymous user is received and suspended, an agent reviews the email and either recovers or deletes it.

**Guidelines**

1. If you accept tickets from anonymous users, review and recover them one by one, either manually or automatically. To identify them, look for the following causes of suspension in the **Suspended Tickets** view: "Permission denied for unknown email submitter" for a closed or "Sender domain not on allowlist" for a restricted.
2. If you are requiring approved users to register, recover tickets from approved users who haven't registered yet. Recovering the ticket also registers the user. To identify the emails, look for the following cause of suspension: "User must sign up to submit email, user notified." Note that the user's email remains unverified until the user responds to the welcome email sent to them.
3. Recover other emails that should be tickets. In particular, look for the following cases:
   - tickets that registered users submitted through the web form while logged out (cause of suspension: "Submitted by registered user while logged out")
   - ticket notification replies by registered users from unverified addresses (cause of suspension: "Submitted by unverified user")
   - ticket notification replies by registered users with the email token stripped out (cause of suspension: "Permission denied due to unauthenticated email update")
   - spam emails that aren't spam (cause of suspension: "Detected as spam")
   - Emails that did not pass Zendesk's DMARC authentication (cause of suspension:
     "Failed email authentication")
4. Bulk delete the remaining emails.
# Zendesk Suite Product Controls and Recommendations Guide

Source: https://support.zendesk.com/hc/en-us/articles/5418528821146-Zendesk-Suite-Product-Controls-and-Recommendations-Guide

---

This article provides a baseline product-level reference for successfully securing and managing your Zendesk Suite instance. Zendesk strongly recommends that you consider implementing these product controls and recommendations at the onset of adoption and regularly review your settings and company best practices to ensure that they are both appropriate for your specific use case and correctly adhered to by your employees. Training agents and administrators on how to apply these product controls will help minimize risk exposure—in keeping with our [Shared Responsibility Model](https://support.zendesk.com/hc/en-us/articles/360050371513-The-Zendesk-Shared-Responsibility-Model).

For a high-level overview of our recommended security practices, see the [General Security Best Practices](general-security-best-practices.md) document.

This article contains the following sections on Zendesk Suite Product Controls:

- [Support](##h_01GEFQMXMHVDJZHGABW1EK9M7J)
- [Guide](#h_01GEFR0YC8MMS9V47FDDR3FBCG)
- [Chat](##h_01GEFRA590YZ600SSNRMQEHCDB)
- [Talk](##h_01GEFREM2FD4XEMX3TB1MXFKA3)
- [Explore](####h_01GEFRZG6ZFA5PCFCD1RP4699Q)
- [Messaging](##h_01GEFRTPKMBCWBBAJZ3Z7QGY4G)

**Security Best Practices: Zendesk Suite Product Controls**

#### **Support**

- **Custom password configurations**. Customize your own password security level to align with internal policies. Zendesk provides the following levels of password security: Recommended, High, Medium, and Low. See [Setting the password security level](https://support.zendesk.com/hc/en-us/articles/4408822149018) for implementation steps. Note: When Zendesk authentication is enabled, you can set session expiration/inactivity timeout restrictions and/or password expiration at the agent/Admin level.
- **Two-factor authentication** (‘2FA’) Implement a second authentication security layer. Available [natively in the product](https://support.zendesk.com/hc/en-us/articles/4408826974874) via SMS message or from a 2-factor authentication app installed on the user’s mobile device, or your 2FA solution to be used should you couple it with Single Sign On within your environment.
- **Single Sign On** (‘SSO’) (for business and social end-user accounts). Reduce the number of attack surfaces by having users login in once, with a single set of credentials.
- **Restrict IP addresses**. [Limit the agent interface](https://support.zendesk.com/hc/en-us/articles/4408894156186-Restricting-access-to-Zendesk-Support-and-your-Help-Center-using-IP-restrictions)) to only those users from coming from a specific range of approved IP addresses.
- **Secure Attachment Access**. Require users to login to their account before accessing attachments by [activating private attachments](https://support.zendesk.com/hc/en-us/articles/4408832757146).
- **Malware Scanning.** Admins should follow company guidelines on how to manage attachments that have been flagged by our [Malware Scanning](managing-malicious-attachments.md).
- **Email**  
  - - [Disable rich content](https://support.zendesk.com/hc/en-us/articles/4408828563866-Disabling-and-enabling-rich-content-in-incoming-emails) in emails (i.e., non-plain text/HTML).
    - Decommission unused support email addresses.
    - Disable wildcard email address when not needed.
    - Enable email authentication with SPF, DKIM and DMARC to reduce email spoofing and Business Email Compromise.
    - Use DKIM for outbound email to verify the origin of emails (e.g., from within your organization)
- **Device Tracking**. [Manage user devices](checking-devices-and-applications-that-accessed-your-account.md) and remove those no longer in use (with Agent/Admin access).
- **Sandbox.** We recommend using a sandbox environment for testing and launching code before it goes into your production environment. Please note that this is only available with Enterprise plans.
- **Support Mobile app.** Decide if you want to allow access for Agents via the Support Mobile app, and if not, remove the Mobile App access in Admin Center under “More Security Settings”. Please note that Password Access to the API needs to be allowed for Mobile Apps to work.
- **Log Management.**
  - - **Audit logs.** Manage your audit logs to keep track of changes in your account. Export reports via the API or as CSV. Only available with Enterprise plans.
    - **Ticket interaction/event logs**. [See all actions and notifications that have occurred in your account](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-all-events-of-a-ticket).
    - **Integration logs.** Track data syncing between your Support instance and your integration via this tool in the Admin Center**.**
- **End user verification**. Require [end users](https://support.zendesk.com/hc/en-us/articles/4408887573274-Configuring-end-user-access-and-sign-in) to register and verify their email address.
- **Least privilege.** Restrict user access to ensure that users only have access to task dependent products. [Learn more about Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866).
- **Custom Roles.** [Delegate access](../team-members-and-groups/creating-custom-roles-and-assigning-agents.md) by role/job description. Please note that this feature is only available for Enterprise plans.
- **Allowlisting.** Define who has [access](https://support.zendesk.com/hc/en-us/articles/4408886840986-Using-the-allowlist-and-blocklist-to-control-access-to-Zendesk-Support-) to your instance to reduce the exposure of sensitive data and unauthorized system access.
- **Blocklisting.** Suspend, reject or prevent users from accessing your instance if/when you perceive a threat to your security.
- **Remove accounts/users.** Regularly review the users on your account and [suspend/demote users](https://support.zendesk.com/hc/en-us/articles/4408888690842-Best-practices-for-removing-agents) who no longer need access to your system.
- **Custom Roles.** Delegate access by role/job description. Please note that this feature is only available for Enterprise.
- **CC and Follower Blocklisting**. Prevent others from [being tagged on tickets](https://support.zendesk.com/hc/en-us/articles/4408843795482-Configuring-CC-and-follower-permissions) and notified of customer conversations to limit access to sensitive customer information and vulnerability to a data breach.
- **Limit Team Member and End-User Inactive Session Length**. Helps limit the [window of time that a session can be utilized](https://support.zendesk.com/hc/en-us/articles/4408832533274-Understanding-your-Zendesk-session-time#:~:text=By%20default%2C%20when%20you%20sign,after%208%20hours%20of%20inactivity.), before sign-in must occur again to reduce unauthorized access to systems and data.
- **Turn off unnecessary [social sign-in methods](https://support.zendesk.com/hc/en-us/articles/4408885847962) for end users.**
- **Disable Ability for Admins to Set Passwords for Users**. Enforce least privilege and remove the ability to set a password without having a user apply 2FA and verify their email address through the normal password reset process. See [this document](https://support.zendesk.com/hc/en-us/articles/4408822149018-Setting-the-password-security-level-for-your-Zendesk#topic_phk_dm5_k) for more information about setting password security levels.
- **Webhooks.** Use TLS/HTTPS to securely [connect](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [to](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [th](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks)[ird](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [party](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [endpoints](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [s](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks)[uch](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [as](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [applic](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks)[ations](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [or](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks) [websites.](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks)
- **API Access**
  - - Disable password access to your API to limit the exposure of protected information.
    - **API Tokens**. Have your Admin set up least privilege access to reduce the number of people who have access to your API and sensitive customer data (e.g., PII, PHI etc.). Please see the [Security Configuration Requirements for HIPAA or HDS Enabled Accounts](https://support.zendesk.com/hc/en-us/articles/4408828395802) for related information about API token management.
- **OAuth** clients. Secure access to your API (and related data). Choose the right flow type for your use case and prefer Authorization Code Grant or Implicit Grant over Password Grant if possible. Visit [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) for a detailed list of industry best practices.

#### **Guide**

- **Moderate Content.** Review Guide content to ensure that [SPAM](../setting-up-your-help-center/using-the-spam-filter-to-prevent-spam-in-your-help-center.md) isn’t being posted to your Help Center.
- **API.** Disable password access to your API to minimize the exposure of sensitive data.
- **API Tokens**. Have your Admin set up least privilege access to reduce the number of people who have access to your API and opportunities for data compromise.
- [Restrict Help Center Access](../setting-up-your-help-center/restricting-help-center-access-to-signed-in-end-users.md)**.** Apply IP address restrictions to [limit](https://support.zendesk.com/hc/en-us/articles/4408894156186-Restricting-access-to-Zendesk-Support-and-your-Help-Center-using-IP-restrictions) user access based on authentication and segmentation.
- **Article Interaction/event Logs**. [See all actions taken by agents on an article](https://support.zendesk.com/hc/en-us/articles/4408820188442-Viewing-article-events-in-History) to ensure adherence to company best practices.
- **Agent/Alias Display Name**. Allow agents to personalize their signatures, increasing trust between agents and customers, as well as, the online safety of your agents.
- **Unsafe Content.** Prevent [unsafe content](https://support.zendesk.com/hc/en-us/articles/4408824584602-Allowing-unsafe-HTML-in-help-center-articles) from being displayed in your Help Center.

#### **Chat**

- **Chat API.** Have your Admin set up least privilege access to reduce the number of people who have access to sensitive data. Be sure to acknowledge the following [restrictions](https://developer.zendesk.com/documentation/live-chat/getting-started/restrictions/).
- **Native File Attachment Allow Listing**. Restrict [file sharing](../live-chat-agent-guide/sending-files-in-a-chat.md) to only those extensions needed for specific job tasks.
- **Gating via Support**. Apply cascading security configurations across products (only applicable for Suite plans).
- **Visitor Authentication**. [Enable visitor authentication](https://support.zendesk.com/hc/en-us/articles/4408838925082-Enabling-authenticated-visitors-in-Web-Widget-Classic-) via token or shared secret to ensure that only authorized users have access.
- **Authentication controls**. Send [private chat attachments](https://support.zendesk.com/hc/en-us/articles/4408842669594-Enabling-secure-chat-attachments-in-the-Zendesk-Agent-Workspace) with authentication controls (only available with the Agent Workspace).
- [Restrict Chat Widget by location](https://support.zendesk.com/hc/en-us/articles/4408887520282#blocked) (e.g., country or domain) to reduce your exposure to bad actors and or malicious nation state actors.
- **Custom Roles.** Delegate access to Chat by role/job description. Please note that this feature is only available with Enterprise plans.

#### **Talk**

- **Call Recording.** [Opt-in or opt-out of call recording](https://support.zendesk.com/hc/en-us/articles/4408831738266-Managing-call-recording-options-in-Talk) based on the number, caller or end user.
- **Delete Recordings.** Automatic deletion of recordings—enable automatic deletion of talk recordings.
- **Talk API Delete Recording Feature**. [Use this endpoint feature](https://developer.zendesk.com/documentation/voice/talk-api/getting-started/) to programmatically delete recordings from tickets, where applicable. Manual deletion can also be applied for [erasure obligation, right to be forgotten as well as industry privacy and compliance requirements](../complying-with-privacy-and-data-protection-law/complying-with-privacy-and-data-protection-law-in-zendesk-talk.md). Note: Automatic Redaction is a separate feature that can’t currently be used to redact credit card information from Voicemail transcripts.

#### **Explore**

- **Manage Explore Permissions.** Enable [Explore access](https://support.zendesk.com/hc/en-us/articles/4408836002970) based on least privilege access (with Admin access).
- **Set up Dataset Permissions.** Set [dataset permissions](https://support.zendesk.com/hc/en-us/articles/4408831563802-Setting-Explore-dataset-permissions) using least privilege access (with Admin access).

#### **Messaging** **(Native)**

- **End User Authentication.** [Enable end user authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746) for Web Widget and Mobile SDK.
- **Allowlisting**. Only allow the Web Widget to be loaded [on specific domains](https://support.zendesk.com/hc/en-us/articles/4500748175258-Installing-the-Web-Widget).
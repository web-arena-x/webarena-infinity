# General security best practices

Source: https://support.zendesk.com/hc/en-us/articles/4408888782618-General-security-best-practices

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enhance security by reviewing your account's security posture, increasing password security, and using two-factor authentication. Limit admin access, use single sign-on for remote authentication, and monitor audit logs. Avoid sharing sensitive information and follow secure coding practices if using the REST API. Provide an email for security notifications to stay informed about potential incidents.

Zendesk provides a range of security options that you can use to ensure that private information is protected and secure. This article covers general security best practices to help you get started. We strongly recommend you train your agents and administrators to follow the best practices to ensure a secure environment.

See the [Zendesk Suite Product Controls and Recommendations Guide](https://support.zendesk.com/hc/en-us/articles/5418528821146) for a detailed list of security best practices we recommend implementing in your instance.

This article covers the following topics:

- [Review the security posture of your Zendesk account](#topic_mvy_kty_vgc)
- [Increase password security for your agents](#topic_spf_cnf_ie)
- [Never give out user names, email addresses, or passwords](#topic_ogq_fnf_ie)
- [Limit the number of agents with administrator access](#topic_dkx_nnf_ie)
- [Remotely authenticate users with single sign-on](#topic_ndv_qnf_ie)
- [Monitor account audit logs](#topic_3zl_yht_hj)
- [Limit access or follow secure coding practices if using the REST API](#topic_3ms_bkr_zk)
- [Provide an email address for security notifications](#topic_xth_pfm_swb)

If you have questions about the security of your Zendesk instance, contact Zendesk directly. In case of a suspected security breach, submit a ticket with the subject “Security” along with the details. Alternatively, you can send an email to [security@zendesk.com](mailto:security@zendesk.com).

## Review the security posture of your Zendesk account

The Security overview page in Admin Center serves as a centralized dashboard for managing your account's security-related settings and provides insight into which features are enabled in your account. The dashboard helps to identify risks associated with your existing configurations and provides recommendations for mitigating these risks. Review the dashboard to determine which security settings need updates. See [Analyzing and improving the security posture of your Zendesk account.](https://support.zendesk.com/hc/en-us/articles/9774890665370)

## Increase password security for your agents

Zendesk provides four [password security levels](https://support.zendesk.com/hc/en-us/articles/4408822149018): Recommended, High, Medium, and Low. You can also specify a custom security level. An administrator can set one password security level for end users and another for agents and admins.

Zendesk strongly suggests setting the Recommended password security level for both team members and end users to safeguard your account. This security level is configured with strict password requirements, checks against known breached passwords, and is based on security best practices and industry standards.

Increase the password requirements for agents to help prevent unauthorized users from guessing your agents' passwords. You should also require administrators and agents to select unique passwords for their Zendesk accounts and avoid reusing passwords for external systems.

Encourage agents to monitor their own accounts. Zendesk will send agents an email notification when their password is changed. Also, agents can conveniently monitor their accounts by [enabling email alerts](https://support.zendesk.com/hc/en-us/articles/4408834578074) for logins from new devices. If you see a new login from a suspicious device, remove the device to end the user's session, then choose a new password.

Require [two-factor authentication](https://support.zendesk.com/hc/en-us/articles/4408826974874) for agents and admins for another layer of security. We recommend sending a message to your support team with a link to the [Using two-factor authentication](https://support.zendesk.com/hc/en-us/articles/4408829277466) article.

Consider using a password manager such as [1Password](https://1password.com/) or [LastPass](https://www.lastpass.com/). Password managers help you generate a single strong password that can be used for all of your other sites.

## Never give out user names, email addresses, or passwords

Zendesk agents and administrators should never give out user names, email addresses, or passwords.

If you're using standard Zendesk sign-in authentication, the only secure way to reset a password is for the user to click the **Forgot my password** link on the Zendesk sign-in screen. This prompts the user to enter a valid email address (one already verified as a legitimate user in your account). After submitting it, they will receive an email containing a link to reset their password.

If you're using a third-party single sign-on authentication system such as Active Directory, Open Directory, LDAP or SAML, passwords can be reset similarly through those services.

Hackers sometimes use social engineering techniques to pressure people into giving them a password for an account. Some hackers use tools that spoof email addresses to impersonate users from legitimate email domains. As a result, what appears to be a legitimate email request from a user may not be from that actual address.

If someone who claims to be a user or administrator contacts you, note the IP address (shown in the [events view](https://support.zendesk.com/hc/en-us/articles/4408829602970) in tickets) and independently verify their identity (for example, by calling the phone number in their user profile). If in doubt, never provide sensitive information or make account changes on someone else's behalf. Legitimate users can change their own account settings.

Educate your agents about these types of security risks. Also, create a security policy that everyone knows and can refer to when these incidents occur.

## Limit the number of agents with administrator access

Administrators can access parts of your Zendesk account that regular agents do not. You can reduce your security risk by limiting the number of agents who have administrator access. The agent role provides access that typical agents need to manage and solve tickets.

You can select predefined agent roles that grant additional permissions to agents. On Enterprise plans, you can also create your own [custom agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) and decide what parts of Zendesk the agent role can access and manage. These permissions are limited. Only account owners and administrators have access, for example, to security settings.

If you're concerned about your agents accessing information about your end users, you can create a role that does not allow them to edit end-user profiles or view the list of all your end users.

## Limit access to private information in tickets

On Enterprise plans, administrators can designate a group as private. This generally restricts access to agents within the group, although admins and team leaders have access by default, and agents can be granted [permission to view private tickets](https://support.zendesk.com/hc/en-us/articles/4988173561370#topic_l21_rbj_dvb). Agents working private tickets are prevented from [@mentioning](https://support.zendesk.com/hc/en-us/articles/4408822451482) or opening [side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746) with team members outside the private group. Using private ticket groups can significantly reduce visibility into the content of tickets.

If you're concerned about agents accessing sensitive information in tickets, you can create private groups and assign appropriate agents to the group to handle those tickets.

## Remotely authenticate users with single sign-on

In addition to the user authentication provided by Zendesk, you can also use single sign-on, which authenticates your users outside of Zendesk. There are two [SSO options](https://support.zendesk.com/hc/en-us/articles/4408883587226): social media single sign-on and enterprise single sign-on.

Social media single sign-on allows your customers to sign in with either their Zendesk account or one of their social media accounts, such as Google or Microsoft. While these options are convenient, we recommend inactivating unnecessary social logins.

Enterprise single sign-on bypasses Zendesk and authenticates your users externally. When users navigate to your Zendesk sign-in page or click a link to access your Zendesk account, they can authenticate by signing into a corporate server or a third-party identity provider, such as OneLogin or Okta.

When providing either enterprise or social media single sign-on, we recommend taking advantage of the two-factor authentication (also known as multi-factor authentication) these services provide. This adds another layer of protection by requiring additional proof of identity. If you're using [JWT](https://support.zendesk.com/hc/en-us/articles/4408845838874) or [SAML](https://support.zendesk.com/hc/en-us/articles/4408887505690), you'll need to set this up for your Zendesk account. For social media single sign-on, your users will need to set this up themselves. All of these services provide the necessary documentation to set it up.

Agents and end users can have different ways to authenticate themselves. You can secure Zendesk Support by creating a stricter authentication policy for agents while providing easy access to your customers and end users.

## Monitor account audit logs

Note: The audit log is available on Enterprise plans and above.

The [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434) tracks important changes to your account. Using the audit log, you can monitor various security events such as user suspensions, password policy changes, exports of customer data, changes to custom role definitions, and many more.

## Limit access or follow secure coding practices if using the REST API

You can use the [Zendesk REST API](https://developer.zendesk.com/api-reference/) and the [Zendesk Apps framework](https://developer.zendesk.com/documentation/apps/) to extend the functionality of your Zendesk Support instance.

If you want to extend your Zendesk instance, we strongly recommend following secure coding best practices. A good reference for this is the Open Web Application Security Project (OWASP), which you can find [here](https://www.owasp.org/index.php/Main_Page).

## Provide an email address for security notifications

If a security incident impacts your Service Data, it is Zendesk's top priority and legal obligation to notify our customers within the required time period. Add the email address of your organization's security contact or group who should receive security incident notifications. See [Designating an email address to receive required security notifications](https://support.zendesk.com/hc/en-us/articles/5436977203610).
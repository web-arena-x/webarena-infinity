# Access log use cases and workflows (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/9972142485530-Access-log-use-cases-and-workflows-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

Use the access log to monitor agent activity, ensuring data privacy and security. Identify unauthorized access, track changes to user data, and prevent potential security risks by filtering access events. Secure API credentials, control access, and detect suspicious activities to maintain compliance and safeguard sensitive information. Leverage both the Admin Center and API workflows for comprehensive oversight.

Location: Admin Center > Account > Logs > Access log

As described in [Using the access log to monitor agent activity](https://support.zendesk.com/hc/en-us/articles/6066010357530), the access log enables monitoring of access events in your account related to tickets, user profiles, and searches. By providing detailed, filtered views of access events, admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can identify unauthorized activities and help ensure compliance with data privacy regulations.

This article covers the following topics:

- [Common use cases](#topic_nxr_yxr_jhc)
- [Example Admin Center workflows](#topic_zgr_tzr_jhc)
- [Example API workflows](#topic_r3v_xzr_jhc)

## Common use cases

This section includes example use cases to help you better understand how the access log can aid in detecting potential security risks. These use cases apply to both the Admin Center user interface and the API.

Each use case includes categories and summaries to filter the access log and find related access events. For example, in the use case *Monitor changes to contact numbers to prevent abuse or fraud*, filter by the **Phone numbers** Category and the recommended Summary items (such as **Create Phone Number** and **Delete Phone Number**) to surface the related access events.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/access_log_filter_example.png)

For more information on filtering the access log, see the following topics:

- [Filtering access log data to refine search results](https://support.zendesk.com/hc/en-us/articles/6066010357530#topic_mdl_fy5_3hc)
- [Zendesk API Reference: Access Logs](https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/)

Expand the sections below to learn more about common use cases.

**Monitor user data access and assess privacy risks**

| Use case | Category filter | Summary filters |
| --- | --- | --- |
| Monitor user profile views to detect unauthorized or excessive profile data access | Users | - Show user - List users |
| Profiles API | - Get profile by identifier - Get profile by profile ID - Get profiles by user ID |
| Monitor critical security settings and account configuration changes | Account settings | - Update account settings |
| Staff | - Fetch staff users - Update staff user - Change password - Update email identity - Fetch 2FA recovery code - Delete 2FA configuration - Set password |
| Track changes to authentication vectors indicating possible account compromise | User identities | - List identities - Delete identity - Show identity - Make identity primary - Update identity - Create identity |
| Current account | - Returns remote authentications for the account - Delete a remote authentication by ID - Get a remote authentication by ID |
| Remote authentication | - Update a remote authentication - Creates a new remote authentication |
| Monitor changes to contact numbers to prevent abuse or fraud | Phone numbers | - List phone numbers - Delete phone number - Show phone number - Update phone number - Create phone number |
| Monitor custom object data and workflow rules to prevent data breaches | Custom objects | - List custom objects - Delete custom object - Show custom object - Update custom object |
| Custom object fields | - List custom object fields - Delete custom object field - Show custom object field - Update custom object field - Create custom object field |

**Secure API credentials and tokens**

| Use case | Category filter | Summary filters |
| --- | --- | --- |
| Secure API credentials and tokens to prevent unauthorized API access | OAuth tokens | - List tokens - Revoke token - Show token - Create token |
| OAuth clients | - Show OAuth clients - Delete OAuth client - Show OAuth client - Update OAuth client - Create OAuth client - List clients - Delete client - Show client - Update client - Create client |
| OAuth connections | - Delete connection - Show OAuth connection - Update connection - Create connection - Import connection - Exchange verification code - OAuth callback - Show OAuth flow - Start OAuth flow - Start OAuth redirect - OAuth token - Refresh OAuth token - Show OAuth connections |
| Monitor API keys and basic authentication credentials management for abuse prevention | API key connections | - Delete API key connection - Update API key connection - Create API key connection |
| Basic authentication connections | - Delete basic authentication connection - Update basic authentication connection - Create basic authentication connection |

**Assess security risks for apps, integrations, and automations**

| Use case | Category filter | Summary filters |
| --- | --- | --- |
| Monitor app and integration lifecycle changes to help prevent security risks | Apps | - Delete app - Get app public key - Update app - Update app installation - Install app - Create app - Upload app package |
| Installations | - Update installed integration - Create an installation |
| Integrations | - Create integration |
| Prevent webhook management abuse, such as data exfiltration or automation-based attacks | Webhooks | - Delete webhook - List webhook invocations - List webhook invocation attempts - Patch webhook - Update webhook - Show webhook signing secret - Reset webhook signing secret - Create or clone webhook |
| Detect automation misuse to prevent privilege escalation or data leaks | Automations | - Bulk delete automations - Delete automation - Update automation - Create automation - Update many automations |
| Macros | - Create unassociated macro attachment - Bulk delete macros - Create macro attachment - Delete macro - Update macro - Create macro - Update many macros |
| Object triggers | - Delete many object triggers - Delete object trigger - Update object trigger - Create object trigger - Update many object triggers |
| Triggers | - Bulk delete ticket triggers - Delete ticket trigger - Update ticket trigger - Create trigger - Update many ticket triggers |

**Control access and prevent privilege escalation**

| Use case | Category filter | Summary filters |
| --- | --- | --- |
| Prevent unauthorized privilege escalation by tracking group and role changes | Group memberships | - Bulk create memberships - Bulk delete memberships - Delete membership - Create membership |
| Custom roles | - Delete custom role - Update custom role - Create custom role |

**Detect bulk actions that could signify malicious activity**

| Use case | Category filter | Summary filter |
| --- | --- | --- |
| Detect other high-impact mass operations that could signify malicious activity | Organization memberships | Bulk delete memberships |
| Organizations | Bulk delete organizations |
| Sessions | Bulk delete sessions |
| Tickets | Bulk delete tickets |
| Users | Bulk delete users |
| Views | Bulk delete views |
| Workspaces | Bulk delete workspaces |

## Example Admin Center workflows

### Monitor user profile views to detect unauthorized or excessive access

**Scenario**: As an admin, you want to ensure agents can only view customer profiles within their groups.

**How to use the access log to filter these access events:**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Logs > Access log**.
2. Click **Filter**.
3. Apply either of the following activity filter combinations:
   - **Category**: Users, **Summary**: Show user, List users
   - **Category**: Profiles API, **Summary**: Get profile by identifier, Get profile by profile ID, Get profiles by user ID
4. Click **Apply filters**.
5. Review the list of events for unauthorized profile views.

### Monitor critical security settings and account configuration changes

**Scenario:** As an admin, you want to monitor when other Zendesk admins change critical security and account settings to ensure your account remains secure and compliant.

**How to use the access log to filter these access events:**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Logs > Access log**.
2. Click **Filter**.
3. Apply either of the following activity filter combinations:
   - **Category**: Account settings, **Summary**: Update account settings
   - **Category**: Staff, **Summary**: Fetch staff users, Update staff user, Change password, Update email identity, Fetch 2FA recovery code, Delete 2FA configuration, Set password
4. Click **Apply filters**.
5. Review the list for security settings or account configuration updates that put your account at risk.

## Example API workflows

### Identify trends to help refine permissions

**Scenario**: Your company has a new customer service team, and you want to ensure its agents are viewing the correct data to comply with data privacy regulations. Your goal is to refine permissions for this group so agents have access only to the data they are permitted to see.

**How to use the Access Log API to address the scenario:**

1. Identify an agent of the new team to use their activity as a reference point.
2. Make an API call filtered by the agent's user ID, which reveals all of the agent's events, including a record of the tickets viewed and searches, at what time, and from which IP address.

   For example, user\_id 1213456789 viewed ticket number 937.

   ```
   timestamp: "2023-02-16T19:00:00Z",
   user_id: 1213456789,
   ip_address: "00.00.000.00",
   url: ""/api/v2/tickets/937?[...]
   method: "GET",
   status: 200
   ```

   Also, user\_id 1213456789 opened the profile belonging to user\_id 9878654.

   ```
   timestamp: “2023-02-16T19:00:00Z”,
   user_id: 1213456789,
   ip_address: “00.00.000.00”,
   url: “/api/v2/users/9878654?[...]
   method: “GET”,
   status: 304
   ```
3. Use the data to determine whether the agent is accessing tickets assigned to other agent groups or viewing profiles of customers assigned to other agents.

   You now have more data to help you set up the proper permissions for agents in the group.

### Investigate suspicious activity

**Scenario**: You are notified that an agent is searching for customer credit card numbers. You'd like a complete record of the agent's activity so you can take the appropriate steps to investigate the issue.

**How to use the Access Log API to address the scenario:**

1. Make an API call filtered by the agent's user ID.
2. Evaluate the search records in the access log to identify repeated searches for sensitive information.

   For example, this agent is searching for "credit card."

   ```
   timestamp: “2023-02-16T19:00:00Z”,
   user_id: 1213456789,
   ip_address: “00.00.000.00”,
   url: “/hc/api/v2/articles/search.json?[...]query=credit%20card”,
   method: “GET”,
   status: 200
   ```
3. If applicable, use the access log to help trace which customers have been affected.
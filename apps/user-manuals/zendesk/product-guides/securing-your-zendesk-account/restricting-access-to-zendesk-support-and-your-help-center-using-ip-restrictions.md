# Restricting access to Zendesk Support and your help center using IP restrictions

Source: https://support.zendesk.com/hc/en-us/articles/4408894156186-Restricting-access-to-Zendesk-Support-and-your-help-center-using-IP-restrictions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Use IP restrictions to control access to your support and help center by allowing only specific IP ranges. This feature enhances security by preventing unauthorized access to API calls and sign-ins. You can allow customers to bypass these restrictions, but not agents or admins. Be aware of undocumented endpoints that remain accessible and consider potential impacts on third-party integrations.

Location:  Admin Center > Account > Security >
Advanced

If Zendesk authentication is turned on, you can restrict access to Zendesk to users
within a specific range of IP addresses. This means that any attempt to make API calls,
sign in, or access pages in any Zendesk product will fail from outside your approved
range. For example, to restrict access to users in your company, only allow access from
your company's IP addresses.

You can also allow customers (but not agents and administrators) to bypass IP
restrictions. IP restrictions you manage in Admin Center apply to all Zendesk products
and Zendesk mobile applications. The restrictions may also affect how other products,
such as Gmail attachments, work.

You can specify ranges of IP addresses, separating each range with a space. Two methods
are available to specify a range. The first is to use asterisk (\*) wildcards. An IP
address consists of four numbers separated by periods, such as **192.168.0.1**. You
can substitute a single asterisk character (\*) for any number group to let Zendesk know
that it should accept any value in that space. For example, **192.\*.\*.\*** allows any
IP address whose first number is 192.

The second way to specify an IP range is to use [IP
subnet mask syntax](https://mxtoolbox.com/subnetcalculator.aspx). For example, **192.168.1.0/25** specifies all the IP
addresses between 192.168.1.0 and 192.168.1.127.

You cannot specify IP ranges where the CIDR (Classless Inter-Domain Routing) value is 0.
For example, if you specify  **10.0.0.0/0**, the **/0** is invalid.

**To set IP restrictions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. On the **IP Restrictions** tab, select **Enable IP restrictions**, then
   enter the **Allowed IP Ranges** you want to restrict.

   Note: Enabling IP-based access restrictions can break third-party
   integrations. Be sure to include all external IPs that need access to
   your account via the Zendesk API.
3. (Optional) Select the **Allow customers to bypass IP restrictions** check
   box.

   This option ensures that your customers can access your help center
   and messaging channels regardless of their IP address, even if their IP
   address is not in the range of allowed IP addresses.

   Agents and
   administrators cannot bypass IP address restrictions.
4. (Optional) If your implementation involves any third-party services, such as
   external bots, make sure their IPs are included in your allowlist.
5. Click **Save**.

## Undocumented endpoints

Certain [undocumented endpoints](https://developer.zendesk.com/api-reference/introduction/undocumented_apis) are not in-scope
for IP restrictions, and may be accessible from any network location, regardless of
the IP restrictions in place. Review these endpoints carefully and consider any
related security implications before using.

Note:

These endpoints are considered unsupported. Zendesk is not responsible for any
issues or losses arising from their use. See [Undocumented APIs](https://developer.zendesk.com/api-reference/introduction/undocumented_apis/).

| Endpoint | Reason for exemption |
| --- | --- |
| /api/v2/pcm/campaign\_analytics | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /api/v2/pcm/campaign\_list | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /api/v2/pcm/campaign/{campaign-id} | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable\_blip | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/accounts/sunco\_app | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/admin/brand\_config\_sets.json | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/admin/brand\_config\_sets/default.json | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/admin/brands | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/admin/brands.json | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/admin/integrations/{integrations-id} | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/brands.json | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/config\_sets | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/internal/config\_sets.json | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/sdk\_channels | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/sdk\_channels/{sdk\_channels-id} | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/api/sdk\_channels/lookup/sunco/{sunco-id} | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/campaigns/{campaigns-id} | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/config | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/messaging/custom\_ticket\_fields | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /embeddable/preview/config | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /frontendevents/dl | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /frontendevents/pca | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /frontendevents/pv | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /mobile\_sdk\_api/settings/{settings-id}.json | Public access to this messaging analytics endpoint is required for data collection and reporting by external systems. |
| /chat/static/css/style\_language.less | This endpoint delivers a globally shared static asset required by all accounts. IP restrictions is not feasible without significant redesign. |
| /chat/static/css/style\_simulatev2.less | This endpoint delivers a globally shared static asset required by all accounts. IP restrictions is not feasible without significant redesign. |
| /chat/static/css/style\_variables.less | This endpoint delivers a globally shared static asset required by all accounts. IP restrictions is not feasible without significant redesign. |
| /voice/calls/ivr\_keypress/{ivr\_keypress-id} | This endpoint must be accessible to Twilio’s infrastructure to support core call flows. Applying IP restrictions would interfere with integration functionality. |
| /voice/calls/ivr\_menu/{ivr\_menu-id} | This endpoint must be accessible to Twilio’s infrastructure to support core call flows. Applying IP restrictions would interfere with integration functionality. |
| /voice/failover/v3/on\_exception | This endpoint must be accessible to Twilio’s infrastructure to support core call flows. Applying IP restrictions would interfere with integration functionality. |
| /voice/verifications/status/{status-id} | This endpoint must be accessible to Twilio’s infrastructure to support core call flows. Applying IP restrictions would interfere with integration functionality. |
| /flow\_composer/assets/bot-avatar/{bot-avatar-id} | This endpoint provides avatar images for bots. Centralized asset delivery must remain openly accessible to ensure compatibility across multiple Zendesk products and clients. |
| /ips | The endpoint provides necessary ingress and egress IP information for customer firewall setup. It must be externally accessible to enable customer operations and integrations. |
| /api/v2/rapid\_resolve/fetch | This helper endpoint requires both an authentication token and an article id for access, ensuring unauthorized use is not possible. Open invocation is necessary to support technical workflows such as feedback widgets. |
| /theming/api/internal/s3\_upload\_tracking | This endpoint receives notifications from Amazon Simple Notification Service (AWS SNS) regarding theme upload events and uses SNS signature authentication. Public accessibility is required to enable integration with AWS services. |
| /integrations/outlook/finish | This endpoint is necessary to complete the Outlook authentication process with Microsoft’s cloud service. Public accessibility is required to support SSO and redirect functionality. |
| /api/services/talk\_recordings/recordings/{recordings-id} | This endpoint supports legacy recording integration during the migration to the Voice product. It will remain open throughout the transition period. |
| /api/v2/zorgtest/zorgheaders | This endpoint is used for integration testing. Applying access restrictions would prevent automated validation. |
| /api/v2/zorgtest | This endpoint is used exclusively for internal integration testing and system health checks. Implementing IP restrictions would prevent automation and engineering teams from accessing the endpoint. |
| /flow\_director/smooch/v2/webhook | Public access to the webhook endpoint is necessary for integration with external messaging services. Authentication is handled through the use of unique webhook keys. |
| All logout endpoints | Logout endpoints must remain publicly accessible so users can securely end their sessions from any network location. |
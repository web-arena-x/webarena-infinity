# Configuring your firewall for use with Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408842860186-Configuring-your-firewall-for-use-with-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Zendesk occasionally updates its public-facing IP addresses to ensure continued reliability and stability for its customers. This article guides IT administrators on configuring your organization’s firewall for use with Zendesk, ensuring service availability during these updates.

This article includes the following topics:

- [About Zendesk's IP addresses](#h_01JK9QS5NJ1J1MFR8FT7DP32BY)
- [Customizing your IP address configurations](#01JK9RF2TRC7G1AZW0MWNAS5DA)
- [Getting IP addresses for additional Zendesk products](#h_01JK9QSD1S41227ND68WP9SMGJ)

## About Zendesk's IP addresses

Zendesk has removed some AWS IP addresses from use and consolidated those public IPs to a single address range (216.198.0.0/18) that Zendesk exclusively owns.

This transition enhances network efficiency and streamlines firewall configuration for our customers by ensuring any IPs rotated in the Zendesk infrastructure are never repurposed by another entity besides Zendesk. It also ensures any necessary IP changes to protect our customers from internet outages or other service-impacting incidents wouldn't require customers to make subsequent changes to their firewall ACLs.

## Customizing your IP address configurations

- Use the [Zendesk IP API](https://developer.zendesk.com/api-reference/ticketing/account-configuration/public_ips/) to retrieve your Zendesk subdomain’s inbound and outbound IP addresses: <https://{your-subdomain}.zendesk.com/ips>.
- Update your allowlists to include the supplied ranges.
- If your agents use any of the Zendesk products listed in [Getting IP addresses for additional Zendesk products](#h_01JK9QSD1S41227ND68WP9SMGJ), add those IP addresses to your allowlists as well. You can find the products included in your organization’s Zendesk plan [here](https://www.zendesk.com/pricing/featured/#compare-plans).
- The addresses listed on <https://{your-subdomain}.zendesk.com/ips> do not include the IP ranges for emails sent by Zendesk's mail servers.  
  To discover the additional IPs, open any popular [Domain Information Grouper (DIG) tool](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm) and enter the following command:  
  dig txt mail.zendesk.com +short  
  The IP addresses returned by the DIG tool do not apply to messages sent via the Gmail Connector or Exchange Connector.

### Important notes

- The [Zendesk IP API](https://developer.zendesk.com/api-reference/ticketing/account-configuration/public_ips/) doesn't return retired AWS IP addresses or product-specific IP addresses.  Refer to [Getting IP addresses for additional Zendesk products](#h_01JK9QSD1S41227ND68WP9SMGJ) to retrieve the complete list of Zendesk IPs required for your firewall configuration.
- Zendesk supports FQDN-based allowlists on a very limited basis. [Contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) if this is a required configuration.

## Getting IP addresses for additional Zendesk products

Some Zendesk products and features require additional IP addresses in addition to Zendesk’s public IP range. Please refer to the following articles relevant to your use case.

- [Zendesk Talk](https://support.zendesk.com/hc/en-us/articles/4408831417498-Talk-network-requirements)
- [Zendesk Chat](../chat-basics/zendesk-chat-system-requirements.md)
- [Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408835459738)
- Zendesk Guide: Add **uploaded-assets-\*.s3.\*.amazonaws.com**.
- [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756859546)
- [Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/6443151510170)
- Zendesk QA: 34.159.180.83, 34.141.81.127, 34.40.37.64, 34.107.48.207, 35.246.215.216, 35.246.44.146
- [Data importer](https://support.zendesk.com/hc/en-us/articles/6280564143514): Add **\*-data-importer\*.s3.\*.amazonaws.com**.
- [Advanced Data Privacy and Protection (ADPP) add-on](../protecting-your-customers-data/about-the-advanced-data-privacy-and-protection-adpp-add-on.md): Add the IP addresses from this URL: <https://www.cloudflare.com/ips/>
- Zendesk Marketplace or other pages located on [www.zendesk.com](http://www.zendesk.com) - [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).
- [Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408831676442)

Note: Zendesk is continuously monitoring the adoption of IPv6 support across our customer base. At this juncture, IPv6 is not supported on our ingress or egress traffic due to the prevalence of IPv4-only or dual stack environments. We will continue to monitor these changes to ensure compatibility.
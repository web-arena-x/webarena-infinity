# Understanding network requirements for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9790998022042-Understanding-network-requirements-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

To access Contact Center through your network, allow specific IP addresses for both Contact Center and third-party services. Follow AWS Amazon Connect requirements and update your network settings to include necessary domains and IP ranges. This ensures smooth operation and access to features like analytics, user metrics, and beta toggling. Check AWS documentation for detailed IP ranges and configurations.

To make Contact Center accessible through your network, there are several IP addresses
you need to allow for Contact Center and for third-party services.

You should also follow the AWS Amazon Connect networking requirements. See [Set up your network to use the Amazon Connect Contact
Control Panel (CCP)](https://docs.aws.amazon.com/connect/latest/adminguide/ccp-networking.html) in the AWS documentation.

This article contains the following topics:

- [Allowing IP addresses for Contact
  Center](#topic_l1t_lfn_wgc)
- [Allowing IP addresses for third-party
  services](#topic_fdh_bgn_wgc)

## Allowing IP addresses for Contact Center

The following domains must be allowed for Contact Center to be accessible in your
network.

‍**Domain allow
list**

| Domain/URL allow list | Purpose | IP Ranges | Ports | Direction | Traffic |
| --- | --- | --- | --- | --- | --- |
| engage..localmeasure.com | Engage Agent desktop and corresponding back end. Replace with one of the following: uk, us, syd, ca | Cloudfront <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html> | 443 (TCP) | Outbound | Send/Receive |
| ..localmeasure.com | Engage Agent desktop and corresponding back end. Replace with one of the following: uk, us, syd, ca | Cloudfront <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html> | 443 (TCP) | Outbound | Send/Receive |
| Customer-Deployed | This is deployed into the customer’s AWS account each time a Cloudformation update is run. The URL changes each time and needs to be updated after every upgrade. You can find this URL in your Contact Center settings panel under “General Settings → Main Configuration → Local Measure Connection → API Gateway URL” | API Gateway <https://ip-ranges.amazonaws.com/ip-ranges.json> | 443 (TCP) | Outbound | Send/Receive |
| app.launchdarkly.com | Enable this if you wish to get access to Beta features | <https://docs.launchdarkly.com/home/infrastructure/ip-list> | 443 (TCP) | Outbound | Send/Receive |
| clientstream.launchdarkly.com | Enable this if you wish to get access to Beta features | <https://docs.launchdarkly.com/home/infrastructure/ip-list> | 443 (TCP) | Outbound | Send/Receive |
| events.launchdarkly.com | Enable this if you wish to get access to Beta features | <https://docs.launchdarkly.com/home/infrastructure/ip-list> | 443 (TCP) | Outbound | Send/Receive |
| <https://logs.browser-intake-datadoghq.com/> | error logs for application monitoring | <https://docs.datadoghq.com/api/latest/ip-ranges/> | 443 (TCP) | Outbound | Send/Receive |
| [www.facebook.com](http://www.facebook.com/) | Enable this only if Facebook chat is required | N/A | 443 (TCP) | Outbound | Send/Receive |
| connect.facebook.net | Enable this only if Facebook chat is required | N/A | 443 (TCP) | Outbound | Send/Receive |
| cdn.segment.com | Application analytics |  | 443 (TCP) | Outbound | Send/Receive |

## Allowing IP addresses for third-party services

There are several services that should be allowed so that they are accessible in your
network.

- **Contact Center services**: Contact Center leverages AWS Cloudfront to
  host and serve Contact Center. To reach the Contact Center SaaS-hosted
  services, your network must be able to reach the IPs listed in the
  documented IP Range list provided by AWS. See [Locations and IP address ranges of
  CloudFront edge servers - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html).
- **Customer-deployed services**: Contact Center leverages AWS API Gateway
  as part of the Cloudformation Stack deployed and hosted in your AWS
  Environment as a customer. The API Gateway service leverages an EDGE type
  API Gateway and can be accessed by using the ip-ranges.json
  file.
- **Additional third-party services**: Zendesk leverages a number of
  third-party services for extended functionality, including analytics,
  user-metrics, and beta feature toggling. To ensure you have access to full
  Contact Center functionality, you should allow the domains and IP addresses
  of these services
  listed.
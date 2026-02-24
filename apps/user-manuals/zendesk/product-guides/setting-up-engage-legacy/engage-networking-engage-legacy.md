# Engage Networking (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731437990810-Engage-Networking-Engage-Legacy

---

This document outlines the domains that must be accessible through your network when deploying Engage. Additionally, all AWS Amazon Connect networking requirements must be followed. Please refer to Amazon Connect network setup guide first for all Connect domains required:<https://docs.aws.amazon.com/connect/latest/adminguide/ccp-networking.html>

‍

## Domain Allow List

In order for an Engage deployment to be accessible in your network, the following domains must be allowed:

| Domain/URL allow list | Purpose | IP Ranges | Ports | Direction | Traffic |
| --- | --- | --- | --- | --- | --- |
| engage…localmeasure.com | Engage Agent desktop and corresponding back end. Replace with one of the following: uk, us, syd, ca | Cloudfront https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html | 443 (TCP) | Outbound | Send/Receive |
| …localmeasure.com | Engage Agent desktop and corresponding back end. Replace with one of the following: uk, us, syd, ca | Cloudfront https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html | 443 (TCP) | Outbound | Send/Receive |
| Customer-Deployed | This is deployed into the customer’s AWS account each time a Cloudformation update is run. The URL changes each time and needs to be updated after every upgrade. You can find this URL in your Engage settings panel under “General Settings → Main Configuration → Local Measure Connection → API Gateway URL” | API Gateway https://ip-ranges.amazonaws.com/ip-ranges.json | 443 (TCP) | Outbound | Send/Receive |
| app.launchdarkly.com | Enable this if you wish to get access to Beta features | https://docs.launchdarkly.com/home/infrastructure/ip-list | 443 (TCP) | Outbound | Send/Receive |
| clientstream.launchdarkly.com | Enable this if you wish to get access to Beta features | https://docs.launchdarkly.com/home/infrastructure/ip-list | 443 (TCP) | Outbound | Send/Receive |
| events.launchdarkly.com | Enable this if you wish to get access to Beta features | https://docs.launchdarkly.com/home/infrastructure/ip-list | 443 (TCP) | Outbound | Send/Receive |
| https://logs.browser-intake-datadoghq.com/ | error logs for application monitoring | https://docs.datadoghq.com/api/latest/ip-ranges/ | 443 (TCP) | Outbound | Send/Receive |
| www.facebook.com | Enable this only if Facebook chat is required | N/A | 443 (TCP) | Outbound | Send/Receive |
| connect.facebook.net | Enable this only if Facebook chat is required | N/A | 443 (TCP) | Outbound | Send/Receive |
| cdn.segment.com | Application analytics | | 443 (TCP) | Outbound | Send/Receive |

## IP Address Ranges

### Local Measure Services

Local Measure leverages AWS Cloudfront to host and serve Engage. In order to reach the Engage SaaS-hosted services, your network must be able to reach the IP’s listed in the documented IP Range list provided by AWS. Please see here for the full list:

[Locations and IP address ranges of CloudFront edge servers - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html)

### Customer-Deployed Services

Engage also leverages AWS API Gateway as part of the Cloudformation Stack deployed and hosted in your AWS Environment as a customer. The API Gateway service leverages an EDGE type API Gateway and can be accessed by using the ip-ranges.json file.

### Additional 3rd Party Services

Additionally, Local Measure leverages a number of 3rd party services for extended functionality such as analytics, user-metrics and beta feature toggling. For access to full Local Measure functionality and support, we highly recommend whitelisting the domains and/or IP addresses of these services listed.

‍
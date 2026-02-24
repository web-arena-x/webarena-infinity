# Allowing network IP addresses for Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408835459738-Allowing-network-IP-addresses-for-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

Explore uses Amazon Web Services (AWS) to provide some services. To allow Explore to work properly, you must ensure that you allow the network traffic from these services on your network. In this article, you'll learn how to find the IP ranges you'll need to allow for Explore to work correctly.

Tip: You might need to ask your network administrator to change allowed IP ranges on your network.

**To download and filter the full list of IP ranges**

1. Use the [instructions on the Amazon web site](https://aws.amazon.com/premiumsupport/knowledge-center/s3-find-ip-address-ranges/) to download the JSON file that contains all AWS S3 IP ranges.
2. Use these [instructions from Amazon](https://aws.amazon.com/premiumsupport/knowledge-center/s3-find-ip-address-ranges/) to filter the list of IP address ranges for your specific AWS region:
   - For AMER (North, Central and South America) and APAC (Asia Pacific), filter for **us-east-1**
   - For EMEA (Europe, Middle-East, and Africa), filter for **eu-west-1**

Now, you can work with your network administrator to make sure the required IP ranges are freed.

For more information about using Zendesk behind a firewall, see [Configuring your firewall for use with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408842860186).
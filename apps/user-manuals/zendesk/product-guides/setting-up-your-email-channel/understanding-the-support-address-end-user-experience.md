# Understanding the support address end-user experience

Source: https://support.zendesk.com/hc/en-us/articles/5000599601050-Understanding-the-support-address-end-user-experience

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When a customer sends an email to your support email address, a ticket is created in Zendesk Support. The support address is set as the recipient address on the ticket and will be used to send replies. For example, tickets sent to help@acme.zendesk.com will reply from help@acme.zendesk.com.

When you add a support address, a preview pane shows you exactly what end users will see in their email inboxes so you understand the end-user experience. What end users see as the from address depends on whether you are using a Zendesk address or an external email address to receive support requests. Also, using personalized replies changes the way the Reply From looks to end users.

This article covers the following topics:

- [Using Zendesk email addresses as support addresses](#topic_sb3_wfp_3n)
- [Using external email addresses as support addresses](#topic_fyf_vfp_3n)
- [Using personalized replies with support addresses](#topic_fg1_1yb_bn)

Related articles:

- [Understanding the default email setup in Zendesk](https://support.zendesk.com/hc/en-us/articles/5612728377754)
- [Adding support email addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506)
- [Which support address are email replies sent from?](https://support.zendesk.com/hc/en-us/articles/4408884042138)

## Using Zendesk email addresses as support addresses

If you are using Zendesk email addresses, the following table shows what the Sent To and Reply From addresses might look like when users email one of your known support addresses.

Table 1. Examples using Zendesk email addresses

| Sent to (address the user sends email to) | Reply from (address the user sees in the reply email) | Example |
| --- | --- | --- |
| support@*yoursubdomain*.zendesk.com | Support address name <support@*yoursubdomain*.zendesk.com> | Acme Support <support@acme.zendesk.com> Note: If the support address does not have a name, the Reply From looks like this: <support@acme.zendesk.com> |
| help@*yoursubdomain*.zendesk.com | Support address name <help@*yoursubdomain*.zendesk.com> | Acme Help <help@acme.zendesk.com> |
| sales@*yoursubdomain*.zendesk.com | Support address name <sales@*yoursubdomain*.zendesk.com> | Acme Sales <sales@acme.zendesk.com> |

## Using external email addresses as support addresses

If you are using external email addresses, the following table shows what the Sent To and Reply From addresses might look like when users email one of your known support addresses.

Note: For information about using an external email address, see [Forwarding incoming email from your existing email address to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698).

Table 2. Examples using external email addresses

| Sent to (address the user sends email to) | Reply from (address the user sees in the reply email) | Example |
| --- | --- | --- |
| support@mycompany.com | Support address name <support@mycompany.com> | Acme Support <support@acme.com> Note: If the support address does not have a name, the Reply From looks like this: <support@acme.com> |
| help@mycompany.com | Support address name <help@mycompany.com> | Acme Support <help@acme.com> |
| sales@mycompany.com | Support address name <sales@mycompany.com> | Acme Support <sales@acme.com> |

## Using personalized replies with support addresses

When personalized replies is enabled, the Reply From address will match the support address it was sent to and it will also include the replying agent or end user's name.

For information about using personalized replies, see [Enabling personalized email replies](https://support.zendesk.com/hc/en-us/articles/4408887209498).

The following table shows what the Sent To and Reply From addresses might look like when you have personalized replies enabled, and users email one of your known support addresses.

Table 3. Examples using personalized replies

| Sent to (address the user sends email to) | Reply from (address the user sees in the reply email) | Example |
| --- | --- | --- |
| support@*yoursubdomain*.zendesk.com | User Name (Support address name) <support@*yoursubdomain*.zendesk.com> | Claire Grenier (Acme Support) <support@acme.zendesk.com> Note: If the support address does not have a name, the Reply From looks like this: Claire Grenier <support@acme.zendesk.com> |
| sales@*yoursubdomain*.zendesk.com | User Name (Support address name) <sales@*yoursubdomain*.zendesk.com> | Ben Gunther (Acme Sales) <sales@acme.zendesk.com> |
| support@mycompany.com | User Name(Support address name) <support@mycompany.com> | Claire Grenier (Acme Support) <support@acme.com> |
| sales@mycompany.com | User Name (Support address name) <sales@mycompany.com> | Ben Gunther (Acme Sales) <sales@acme.com> |
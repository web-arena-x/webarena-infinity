# Using Microsoft Exchange Online with the authenticated SMTP connector

Source: https://support.zendesk.com/hc/en-us/articles/8130298032538-Using-Microsoft-Exchange-Online-with-the-authenticated-SMTP-connector

---

**Note:**Due to Microsoft Exchange Online [retiring Basic authentication for SMTP](https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-retire-basic-auth-for-client-submission-smtp-auth/4114750) at the end of December, 2026, the solution described in this article will be deprecated at that time. Customers using Microsoft Exchange should use the [Exchange connector](https://support.zendesk.com/hc/en-us/articles/8979947090586) instead of the SMTP connector. See the [announcement](https://support.zendesk.com/hc/en-us/articles/10203154603546) for details.

This is a setup recommendation article for the [authenticated SMTP connector](https://support.zendesk.com/hc/en-us/articles/8043218178842) (outbound version) for use with Microsoft cloud-based email services. If these do not work for you, you may need to open a ticket with Microsoft for more specific recommendations. 

What we refer to as the “outbound” portion SMTP Relay is compatible with Microsoft Exchange Online. However, Microsoft email services do not appear to allow the addition of SMTP AUTH credentials with what we’d consider to be the “inbound” half of the SMTP Relay. 

Accounts wishing to use Microsoft cloud-based email services should employ the version of the feature described in this [setup article](https://support.zendesk.com/hc/en-us/articles/8043218178842-Connecting-your-Outbound-Email-Server-to-Zendesk-using-the-Authenticated-SMTP-Connector-EAP), which allows for standard auto-forwarding into Zendesk (see last paragraph) but can create an authenticated connection for outbound sending. 

Prior to setup in Zendesk, you’ll need to enable SMTP AUTH for the address in Outlook. See [Enable SMTP AUTH for specific mailboxes](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission#enable-smtp-auth-for-specific-mailboxes) for more info. This is likely a missing step for many customers, and you may need to work with your Office 365 admins to enable the setting.

The following example details come from [How to set up SMTP AUTH client submission](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365#how-to-set-up-smtp-auth-client-submission):

| | |
| --- | --- |
| **Device or Application setting** | **Value** |
| Server/smart host | [smtp.office365.com](http://smtp.office365.com/) |
| Port | Port 587 (recommended) or port 25 |
| Username/email address and password | Enter the sign-in credentials of the hosted mailbox being used |

Another consideration is an administrative page in Microsoft cloud-based email services that should be examined. It is called "Block access for unknown or unsupported device platform." Even though you may have enabled SMTP AUTH, that alone might not automatically allow you to use this integration. You may want to ensure that Linux is not excluded from access as a device platform:

![Block Access.png](https://support.zendesk.com/hc/article_attachments/8214069728282)

In addition to enabling the feature for outbound sending from Zendesk, you must set up auto-forwarding into Zendesk so that both the initial support requests and ticket updates can be forwarded to Zendesk for the purpose of creating and updating tickets.

Setting up only the outbound portion of an existing address is not possible. You must delete the existing address and follow the [setup process](https://support.zendesk.com/hc/en-us/articles/8043218178842-Connecting-your-Outbound-Email-Server-to-Zendesk-using-the-Authenticated-SMTP-Connector-EAP) to establish the outbound connection. This [Microsoft article](https://support.microsoft.com/en-us/office/turn-on-automatic-forwarding-in-outlook-7f2670a1-7fff-4475-8a3c-5822d63b0c8e) describes that process, though we have received feedback that Microsoft might also require the enabling of an outbound spam policy rule before auto-forwarding will function correctly.  If we are able to obtain more specific information about that spam policy we will post it here.
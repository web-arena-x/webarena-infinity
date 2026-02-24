# Decommissioning email support addresses

Source: https://support.zendesk.com/hc/en-us/articles/4408833416474-Decommissioning-email-support-addresses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Sometimes, an organization needs to discontinue the use of an external or native support email address without responses to existing tickets being lost. This article explains how to manage this workflow for both types of addresses.

This article contains the following sections:

- [Decommissioning an external Support Address](#h_01ERZ4XXQM7YQ0GCRNDK3992BE)
- [Decommissioning a native Zendesk support address](#h_01ERZ4YQ96XTCRV7QWYMVBCEA9)

## Decommissioning an external Support Address

Depending on your organization's specific needs you might need to vary this workflow.

**To decommission an external Support address**

1. Create a unique native Zendesk Support address as part of the same brand that the previous address belonged to (if you are using brands, otherwise just add the address to your account, which is your only brand). [Here is an article](https://support.zendesk.com/hc/en-us/articles/4408842868506-Adding-support-addresses-for-users-to-submit-tickets) that describes the support address creation process. This assumes that the external address that is doing the forwarding is still a fully functioning address with SPF (and/or DKIM) enabled, so that your response email notifications will continue to be sent from the address that will be decommissioned. This allows for the temporary continuance of conversation threading, as needed.   
   Replace decommissioning@*yoursubdomain*.zendesk.com) with your own subdomain: 
   ![](https://support.zendesk.com/hc/article_attachments/7856391182746)
2. Create a new trigger and place it towards the top of your list of triggers. This trigger's purpose will be to set any newly created tickets (not responses to existing tickets) to the solved state and provide you with the opportunity to respond to your customers, letting them know which new address they should be using to open support tickets, if that suits your organization's needs. Depending on those variable needs, the trigger would look something like this example. The address "decommissioning@" would be the address you no longer wish to use: 
   ![](https://support.zendesk.com/hc/article_attachments/7856391182362) 
   The response email is optional. The tag (*decommissioned*) should be used as a prohibitive condition in all of your other triggers that are designed to respond to new ticket creation events ("Notify requester of received request"). This is to prevent more than one trigger from firing upon ticket creation, like this: 
   ![](https://support.zendesk.com/hc/article_attachments/7856391182618) 
   The tag does not need to be called "*decommissioned*". You can also use "*do\_not\_reply*" as a general prohibitive tag that can be applied via agent update or through the use of a [Macro](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets), when you have a specific need to make sure that no email notifications are sent from all of the Triggers to which it is applied. It is entirely up to you, as is the title of the newly created support address: *anything*@*yoursubdomain*.zendesk.com.
3. After these steps have been done you can have your domain admin direct the forwarding rule from the previous native support address (*decommissioned*@*yourdomain*.zendesk.com) to the new support address (*anythingnew*@*yourdomain*.zendesk.com). This will allow existing tickets to continue to be updated (as it does not strictly matter which support address an emailed response arrives at, the ticket will still be updated, though different triggers might act differently upon the newly arriving email from previous behavior), while newly created tickets to that old address will be closed and an advisory email will be sent in response.
4. (Optional). To better assist your customers in adopting your new workflow you may want to consider creating new "Notify requester of comment update" triggers to advise them on your new process as well. This can be helpful in migrating all traffic over to the new address more quickly. The same prohibitive conditions (**Tags** > **Contains none of the following** > **decommissioned**) should be added to your other triggers to prevent two email notifications from going out for each update.

In time your customers will adopt the new support address and the existing tickets can be solved out, then the support address, triggers, and forwarding rule from your external domain can be deleted or freed up for other purposes.

## Decommissioning a native Zendesk support address

One method that can help your customers adopt your new support address quickly is to set up a trigger that lets your customers know that you are taking this address out of use.

**To set up a notification trigger**

1. Configure a trigger with the following conditions and actions:![](https://support.zendesk.com/hc/article_attachments/7856435724442)
2. If you're concerned about losing traffic even after you are not seeing many new requests or responses coming to this support address then you can [enable wildcard addresses](https://support.zendesk.com/hc/en-us/articles/4408842868506-Adding-support-addresses-for-users-to-submit-tickets#topic_o1c_53r_l3b). This will allow your account to accept email that arrives at *anything*@*subdomain*.zendesk.com (which includes your decommissioned address). This method does not allow for routing rules through triggers, as rules can only be created around existing support addresses. However, it does ensure that any late arriving traffic to that previous support address will not be lost.

In this article, you've learned about the process of removing a legacy support address. If you have any questions then please [contact us](https://support.zendesk.com/hc/en-us/articles/4408843597850) or post your question in the comments section (without providing any private addresses or account data) and we'll do our best to assist.
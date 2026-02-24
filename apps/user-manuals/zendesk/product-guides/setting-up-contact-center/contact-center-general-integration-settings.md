# Contact Center general integration settings

Source: https://support.zendesk.com/hc/en-us/articles/9611882665754-Contact-Center-general-integration-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Access the Contact Center integration settings to customize ticket creation and call handling. Adjust ticket assignment, force ticket creation, and decide if customer details pop up before calls. Configure outbound call ticket creation and manage call recordings and transcripts, choosing between redacted or unredacted options. Tailor these settings to streamline your support processes and improve call management.

Once your CloudFormation stack is updated to integrate with Zendesk, you can access the Zendesk settings page from the left-side navigation bar of Contact Center. From here, there are various settings you can customize.

This article contains the following topics:

- [Standard settings](#topic_ggr_pkc_jgc)
- [Call details settings](#topic_n1s_1vb_jgc)

## Standard settings

In this section you can review and edit details of the Zendesk integration or click **Go to Zendesk** to open your linked Zendesk account.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_fri_1.png)

This page contains the following settings:

- **Ticket assignment behavior**

 | UI value | Contact attribute value | Behavior |
 | --- | --- | --- |
 | True | None | A new ticket will be created after the Agent accepts the call. The ticket will be ‘popped’ to the Agent. |
 | True | ticket\_assignment = true | A new ticket will be created after the Agent accepts the call. The ticket will be ‘popped’ to the agent. |
 | True | ticket\_assignment = false | A new ticket will not be created after the Agent accepts the call. No ticket will be ‘popped’ to the Agent. |
 | False | None | A new ticket will not be created after the Agent accepts the call. No ticket will be ‘popped’ to the Agent. |
 | False | ticket\_assignment = true | A new ticket will be created after the Agent accepts the call. The ticket will be ‘popped’ to the Agent. |
 | False | ticket\_assignment = false | A new ticket will not be created after the Agent accepts the call. No ticket will be ‘popped’ to the Agent. |
- **Force ticket creation**

 | UI value | Contact attribute value | Behavior |
 | --- | --- | --- |
 | True | None | If a ticket isn’t created by default (see Ticket assignment behaviour) the Agent will be made to create a new ticket or link the call to an existing ticket before they are able to close the call. |
 | True | force\_ticket\_creation = true | If a ticket isn’t created by default (see Ticket assignment behaviour) the Agent will be made to create a new ticket or link the call to an existing ticket before they are able to close the call. |
 | True | force\_ticket\_creation = false | An Agent can end a call irrespective of whether or not a ticket has been associated to the call. |
 | False | None | An Agent can end a call irrespective of whether or not a ticket has been associated to the call. |
 | False | force\_ticket\_creation = true | If a ticket isn’t created by default (see Ticket assignment behaviour) the Agent will be made to create a new ticket or link the call to an existing ticket before they are able to close the call. |
 | False | force\_ticket\_creation = false | An Agent can end a call irrespective of whether or not a ticket has been associated to the call. |
- **Pop customer or ticket details before accepting the call**

 | UI value | Contact attribute value | Behavior |
 | --- | --- | --- |
 | True | None | A ticket or the customer profile will be displayed to the Agent prior to them answering/accepting the call. The zendesk\_ticket\_id attribute must be set on the ticket for this to work. |
 | True | pop\_incoming = true | A ticket or the customer profile will be displayed to the Agent prior to them answering/accepting the call. The zendesk\_ticket\_id attribute must be set on the ticket for this to work. |
 | True | pop\_incoming = false | A ticket or user profile will not be displayed to the Agent prior to them accepting the call. A ticket or user profile may be displayed after the Agent has accepted the call, depending on other settings. |
 | False | None | A ticket or user profile will not be displayed to the Agent prior to them accepting the call. A ticket or user profile may be displayed after the Agent has accepted the call, depending on other settings. |
 | False | pop\_incoming = true | A ticket or the customer profile will be displayed to the Agent prior to them answering/accepting the call. The zendesk\_ticket\_id attribute must be set on the ticket for this to work. |
 | False | pop\_incoming = false | A ticket or user profile will not be displayed to the Agent prior to them accepting the call. A ticket or user profile may be displayed after the Agent has accepted the call, depending on other settings. |
- **Create a ticket on every outbound call**

 | UI value | Contact attribute value | Behavior |
 | --- | --- | --- |
 | True | None | A new ticket will be created and associated to the call every time an outbound call is placed. |
 | True | all\_outbound = true | A new ticket will be created and associated to the call every time an outbound call is placed. |
 | True | all\_outbound = false | When placing an outbound call, a ticket will not be created automatically. |
 | False | None | When placing an outbound call, a ticket will not be created automatically. |
 | False | all\_outbound = true | A new ticket will be created and associated to the call every time an outbound call is placed. |
 | False | all\_outbound = false | When placing an outbound call, a ticket will not be created automatically. |

## Call details settings

This section defines the behavior of Call Transcripts and Recordings in Zendesk from the Contact Center app and contains the following settings:

- **Provide a link to download the call recording:** Select how call recordings cabn be downloaded:
 - **Redacted call recording:** Important information, such as credit card numbers, is redacted from the call recording.
 - **Unredacted call recording:** The entire call recording can be downloaded with no redactions.
 - **No call recording:** The call transcript is not available to download.
- **Call transcript:** Select how call transcripts are downloaded:
 - **Redacted call transcript:** Important information, such as credit card numbers, is redacted from the call transcript.
 - **Unredacted call transcript:** The entire call transcript can be downloaded with no redactions.
 - **No call transcript:** The call transcript is not available to download.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_fri_5.png)
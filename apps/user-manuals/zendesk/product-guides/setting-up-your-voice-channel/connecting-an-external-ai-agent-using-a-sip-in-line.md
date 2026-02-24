# Connecting an external AI agent using a SIP-IN line

Source: https://support.zendesk.com/hc/en-us/articles/8397061704474-Connecting-an-external-AI-agent-using-a-SIP-IN-line

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

SIP (Session Initiation Protocol) technology allows voice calls and other communication services to be carried over the internet.

SIP-IN, for receiving calls from the internet, is supported. SIP-OUT, for making outbound calls on the internet, is currently not supported.

A common use case for a SIP-IN line is to connect an external AI agent to Zendesk. For example, you might want your AI agent to field the call first. If it can’t help, you’ll then be transferred to a Zendesk agent.

Once you’ve [added a SIP-IN line](https://support.zendesk.com/hc/en-us/articles/8397091234586), you can configure call transfer to your AI agent when a human agent or voicemail is unavailable.

This article contains the following topics:

- [Understanding the call escalation process](#topic_ulw_2fc_qdc)
- [Step 1: Understanding the requirements for SIP-IN lines](#topic_y5h_rmt_kdc)
- [Step 2: Connecting an incoming call to an external AI agent](#topic_wt5_rmt_kdc)
- [Step 3: Interacting with the AI agent](#topic_zmv_rmt_kdc)
- [Step 4: Completing the call](#topic_dcw_rmt_kdc)

## Understanding the call escalation process

Here’s a high-level overview of how the process works:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_sipin_27.png)

1. An end user calls your phone number using a Public Switched Telephone Network (PSTN) phone line.
2. If no agent is available and voicemail is off, the call is transferred to the external AI agent using [call overflow](https://support.zendesk.com/hc/en-us/articles/4408832017690) or [IVR keypress](https://support.zendesk.com/hc/en-us/articles/4408885628698) to an external number hosted with the AI agent provider.
3. The AI agent addresses the caller’s query, or, if it cannot address it, escalates the call to a Zendesk live agent using your SIP-IN line.
4. During escalation, context collected by the AI agent can be passed to Zendesk in a ticket.
5. At the end of the overflowed call to the external number, a ticket is created with the tag "call\_overflow".

## Step 1: Understanding the requirements for SIP-IN lines

Before you start, ensure that you've read and understood the requirements for using SIP-IN lines. See [Adding a SIP-IN line](https://support.zendesk.com/hc/en-us/articles/8397091234586).

A ticket (containing all relevant call information) can be created by the AI agent partner before the call, and the ticket ID is passed to Zendesk to be associated with the SIP call. Agents will be shown the linked call tickets containing caller and SIP details when handling SIP-IN calls, ensuring a seamless conversation. You must configure your AI agent to create a ticket. You can use the [Zendesk API](https://developer.zendesk.com/documentation) and your AI agent's documentation to learn how to do this. Creating a ticket has the following requirements:

- The SIP header format must be: X-Zendesk-Ticket-Id=<*ticket number*>.
- When creating the ticket, use the via\_id 34 as detailed [here](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/#:~:text=34,Phone%20call%20(incoming)). This will identify it as an incoming voice call ticket in Zendesk.
- Our provider supports G.711 μ-law (PCMU) and A-law (PCMA) codecs for media.
- Twilio voice media IPs use a single global range: 168.86.128.0/18, with a UDP port range 10000-60000.

## Step 2: Connecting an incoming call to an external AI agent

Once you’ve met the necessary requirements, you can configure connecting incoming calls to your AI agent.

Note: Multiple schedules can be created on Suite Enterprise plan to overflow the call at specific times.

**To connect a call to your AI agent**

1. Configure your AI agent with the URI you created for your SIP-IN line.
   See [Adding a SIP-IN line](https://support.zendesk.com/hc/en-us/articles/8397091234586).
2. Ensure that [call overflow](https://support.zendesk.com/hc/en-us/articles/4408832017690) is configured to dial your AI agent when a call can’t be taken by agents or answered by voicemail. You can [create multiple schedules](https://support.zendesk.com/hc/en-us/articles/4408842938522) on the Suite Enterprise plan to overflow calls at specific times. A ticket number is not passed to the AI agent.

When an incoming call is received on your standard (Public Switched Telephone Network or PSTN) Zendesk phone number and no agent or voicemail is available, the call overflows to the AI agent using a PSTN line. The call is shown in the [real-time dashboard](https://support.zendesk.com/hc/en-us/articles/4408831823514).

## Step 3: Interacting with the AI agent

In this step, the caller interacts with the external AI agent.

The AI agent authenticates the caller and creates a ticket to log the conversation. If the caller is a new end user, the external AI agent can create a new profile and link this profile to the ticket.

Agents will be shown the linked call tickets containing caller and SIP details when handling SIP-IN calls.

The ticket generated by the AI agent must:

- Set the SIP header format to X-Zendesk-Ticket-Id=<*ticket number*>, to pass the ticket number.
- Use the via\_id 34 (details [here](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/#:~:text=34,Phone%20call%20(incoming))). This will help identify it as an incoming voice call ticket in Zendesk.

Tip: Separate from the AI agent’s ticket, an [overflow ticket is created](https://support.zendesk.com/hc/en-us/articles/4408821302810) when the overflowed call to the external number ends. If you don’t need this ticket, you can use [a trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) to automatically close it.
You can identify overflow tickets by the ticket tag, “call\_overflow”.

## Step 4: Completing the call

After the AI agent takes the call, one of two things will happen:

- The external AI agent resolves the caller’s question, ends the call, and updates the ticket. The information updated in the ticket can be used for reporting. [Omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) can work using parameters from this ticket.
- The AI agent cannot resolve the caller’s query and escalates the call using the SIP-IN line. The available agents greeting plays, and the call is offered to agents. The business hours setting on the SIP-IN line, voicemail, and overflow settings are respected. The hold music plays while the call is routed.

 After the call ends, the ticket passed by the external AI agent is displayed to the agent. The ticket contains the caller and SIP details.

**To configure call escalation**

1. Configure your AI agent to forward calls to the SIP-IN line URI you created in Admin Center.
2. Configure your AI agent to pass a ticket to support using the SIP line you created. This process might differ depending on the AI agent you are using.
   Refer to your AI agent documentation for help. The AI agent can use the Zendesk API to create a ticket in Support for the conversation. Additionally, the AI agent can create a Zendesk user profile if necessary. [See the API documentation](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/) for help.

Important: When you create a ticket using the API, make sure to use via\_id 34 to create the ticket.

During escalation, context collected by the AI agent can be passed to Zendesk in the form of a Zendesk ticket. If a ticket is not passed, the overflow ticket created when the overflowed call ends, with tag "call\_overflow", serves as the record of the call.

Zendesk authenticates incoming requests on the SIP-IN line by matching the IP address of the request with the IP ranges defined in the SIP-IN Line settings.
The ticket ID contained in the SIP header is used by Zendesk to link the relevant ticket to the phone call. This ticket is displayed to the agent who answers the call and is also used for reporting purposes.

You can find other connection requirements for forwarding the call over SIP [in this article](https://support.zendesk.com/hc/en-us/articles/8397091234586-Adding-a-Talk-SIP-IN-line#topic_idv_2dt_kdc).
# Troubleshooting advanced AI agents with Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357757857050-Troubleshooting-advanced-AI-agents-with-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

Here are some common issues and suggested fixes:

- [AI agent goes online then offline again](#h_01FPJ95DX666H51DDDMNSJQMGZ)
- [AI agent shows offline in Zendesk Chat](#h_01FPJ95DX666H51DDDMNSJQMGZ)
- [AI agent doesn’t join the conversation](#h_01FPJ8WPBAZS36AJWDMJFCJS8Q)
- [Widget missing from my website](#h_01FPJ8XG73EQM68GW42PF81YKB)
- [AI agent keeps throwing EOS errors when turned on](#h_01FPJ8XA77Z3C68E0ZF4BQCAVC)

## **Error** - The AI agent goes online then offline again

This is because somebody is logged in to Zendesk as the AI agent.
When someone logs in to the AI agent's account, this overwrites the integration of the AI agents - Advanced Dashboard and changes the status.

To fix the issue:

1. Switch the Automation Engine toggle off in **Settings > CRM integration.**
2. Ask the person to log out as the AI agent.
3. Switch the Automation Engine back on.

## **Error** - The AI agent shows offline in Zendesk Chat

Make sure nobody is logged in as the AI agent in Zendesk. When someone logs in to the AI agent's account, this overwrites the integration of the AI agents - Advanced Dashboard and changes the status.

To fix the issue:

1. Restart the AI agent by switching the Automation Engine toggle off in **CRM integration**.
2. Check that nobody is logged in as the AI agent. If yes, they need to log out.
3. Switch the Automation Engine back on.

## **Error** - The AI agent doesn't join the conversation

Make sure nobody is logged in as the AI agent in Zendesk. When your AI agent doesn’t join the chat, there are a few things to do and check. Follow the steps below and always restart the AI agent after each change to see if it’s working.

### Reauthorize the connection between AI agents - Advanced and Zendesk

Only Client Admins are able to reauthorize the connection.

To do this:

1. Sign in to Zendesk as the AI agent
2. Sign in to the AI agents - Advanced Dashboard in a separate tab
3. Toggle the Automation Engine off 
   ![mceclip1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip1_w8XAx.png)
4. Navigate to Settings > CRM Integration and click **Unauthorize Zendesk Chat**![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_Eb43p.png)
5. On the same page, go to Integration Parameters and make sure the correct departments are selected
6. Click **Authorize Zendesk Chat 
   ![mceclip2.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip2_PEBeb.png)**
7. Once authorization is completed, log OUT as the AI agent in Zendesk.
8. Toggle the Automation Engine back on.

### Department selection

Chats are routed using departments/groups. If you have prechat form enabled in Zendesk Chat, make sure [the hide department snippet](https://support.zendesk.com/hc/en-us/articles/8357757747354#Step-3.--Add-hide-department-snippet-to-configure-the-chat-widget)
is implemented correctly with the exact names of the departments/groups. 

### Sign out from Zendesk

The AI agent in our Dashboard can’t join the chat if there’s someone logged in using the AI agent account in zendesk. To solve this:

1. Sign out from Zendesk
2. Restart the AI agent by switching the toggle next to automation engine in **CRM Integration** on and off

## Restart the AI agent

1. Restart the AI agent by switching the Automation Engine toggle off in **CRM integration**.
2. Give it a second before switching it back on again.

### Reconnect the AI agent

It is important to login as the AI agent in Zendesk before authorizing. Try to reconnect by following the steps below:

1. Unauthorize in Dashboard
2. Log out of all Zendesk products
3. Sign in as the AI agent account in Zendesk Chat
4. Repeat [the connecting steps](https://support.zendesk.com/hc/en-us/articles/8357757747354 "https://ultimateai.atlassian.net/wiki/spaces/CS/pages/2108949264/Scenario+A+Zendesk+Chat+Widget+Already+Live+Help+Center#4.-Connect-the-bot-by-turning-the-Automation-Engine-on-in-ultimate.ai%E2%80%99s-Dashboard")

### Check settings in Zendesk Chat

### Settings > Agents

1. Is the AI agent there?
2. Is it enabled?
3. Is it online?

![mceclip5.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip5.png)

Settings > Departments

- Is there a department for the AI agent?
- Is the AI agent the only agent in there?
- Is it enabled?

Settings > Widget > Forms

- Pre-chat form should be on
- Required department should be enabled

![mceclip6.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip6.png)

### Settings > Account > Operating hours

- Is it switched **On** or **Off**?

 - If you want the AI agent to be online only during certain hours, make sure to set it up here.
- If it’s switched on, are the hours correct?

![mceclip7.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip7.png)

### Settings > Routing

- Escalation might fail when there are no agents available. Agent availability can be affected by **Chat routing** and **Chat limit**.
- There are two options here: 
 ![mceclip8.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip8.png)

1. **Broadcast** is preferred if the client doesn’t have “Skills-based routing” on.
2. **Assigned**  is used when the client has “Skills-based routing” on. This can be checked by going to the **Skills** tab in the top left corner.
   ![mceclip9.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip9.png)

- **Chat limit** can also be found on **Settings > Routing**

**![mceclip10.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip10.png)**

---

## In Zendesk Support

### Check if the AI agent account has access to Zendesk Chat

1. Go to Zendesk Support > Settings > People
2. Locate the AI agent by searching for its name![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_G0TDm.png)
3. Then enable Zendesk Chat by toggling the switch on ![mceclip1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip1_tgkIw.png)
   - You might see "Manage in Admin Center" instead of the toggle depending on your Zendesk version
     ![mceclip2.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip2_C5l7S.png)
   - If that's the case follow this screenshot instead:![mceclip3.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip3.png)

## In Dashboard

### Make sure there’s nothing under Zendesk Tags in Integration parameters

This is only used IF the client uses Zendesk Skill routing. The “tag” here refers to “skill tag” and is NOT the same as chat tags that we use in dialogues.
[Read more about skill routing in this Zendesk guide.](https://support.zendesk.com/hc/en-us/articles/360022365513-Routing-chats-based-on-agent-skills#topic_exc_rqx_q1b "https://support.zendesk.com/hc/en-us/articles/360022365513-Routing-chats-based-on-agent-skills#topic_exc_rqx_q1b")

The screenshot below is an opposite example. If this is what you see, click the trash can icon to remove it.

![mceclip4.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip4.png)

## If you use Google Tag Manager

- Does the widget look like the new one or legacy one? ![mceclip11.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip11.png)

- If it looks like the old one, then check the following:
 - Is the correct container / version being published?
 - In Tags, see if the old one is still enabled. If the client sees one that could be the old one, try to “pause” it and see if it changes anything - they should know how to do this.
 - Another way to see if it’s the legacy one spooking us, go to the website where the current chat widget is, right click to inspect the code.

---

## **Error** - The AI agent sends an EOS error when turned on

Check if the client has IP Restrictions set up on their account:

- Login to your zendesk

 - go to "zendesk chat"
 - click on "settings " --> "account"
 - click on the tab "security"
 - If the IP restriction is enabled, please add the following:

    - 34.140.214.64
    - 34.140.222.34
    - 35.233.19.208
    - 34.79.189.15
    - 34.78.252.6
    - 34.34.185.160

---

## **Error** - The widget is missing from the website

# If you don't see the widget on your website, please follow the Zendesk article below:

<https://support.zendesk.com/hc/en-us/articles/225523927-Troubleshooting-Guide-The-widget-is-missing-from-my-website>
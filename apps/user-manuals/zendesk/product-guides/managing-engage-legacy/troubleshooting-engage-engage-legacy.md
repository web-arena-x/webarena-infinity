# Troubleshooting Engage (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731439518618-Troubleshooting-Engage-Engage-Legacy

---

The following article is to provide guidance on initial troubleshooting steps that can be taken in the event you experience any issues with the Engage platform.

For Amazon Connect Troubleshooting documentation, please see the following: <https://docs.aws.amazon.com/connect/latest/adminguide/troubleshooting.html>

For steps on how to submit an AWS Support Ticket, please see the following: <https://docs.aws.amazon.com/awssupport/latest/user/case-management.html>

# General Questions

The following is important information to have on hand when troubleshooting an issue in Engage.

- How many users are affected?
- Clear steps to follow to reproduce the issue.
- When (time & date) was the issue first experienced by the user(s)?
- Have the affected user(s) tried refreshing their browsers, closed and opened their browser, or tried using different browsers?
- What part of the product/platform is the issue happening on; Dashboards, Message text editor, Utility widget etc.
- Is there a workaround for the issue?
- Is the issue reproducible in the [Amazon Connect CCP](https://docs.aws.amazon.com/connect/latest/adminguide/launch-ccp.html)?
- Have any changes been made to Contact Flows, Queues or Routing Profiles in Amazon Connect?
- Are the affected Agents using Softphone or Desk Phone settings?
- Do you see any Error messages in the Browser Console log or Network Log at the time the issue occurs?

# SSO login

Typically issues could be due to the connection or web browser and internal security policies which could be blocking access.

‍

Try testing the following with the user:

1. Checking network connection and VPN.
2. Make sure the browser is up to date, particularly after a system update.
3. Restart your browser, use a different browser.
4. Clear browser cache.
5. If using VPC or VPC with PrivateLink, make sure you have adequate permission to access in this manner.
6. You can also try authenticating in a private window of your browser to avoid any cached credentials.

‍

If the issue persists, please log an AWS Support Case from your Amazon Console. AWS will ask you to upload a HAR file attached to the support case. Please note to export the HAR file while replicating the issue and also check the preserve logs button while working on it.

How to create a HAR file from a browser for an AWS Support Case: https://aws.amazon.com/premiumsupport/knowledge-center/support-case-browser-har-file/

# Call or Network Quality

In the event that call quality is impaired or an agent is experiencing latency in the Engage desktop, we recommend that the customer follow the steps below for debugging purposes:

‍

**AWS Technical Support Ticket:** When a networking issue has been reported, we recommend that a ticket is submitted to AWS Support simultaneously. The ticket should include a full description of the issue experienced by agents, the time of occurrence and the output logs of an Endpoint Test and Agent CCP logs (run by the agent who has experienced the issue).

‍

Other recommended questions:

1. Contact your ISP to see if there are any stability issues or latency problems.
2. Check to make sure that the WAN isn't congested.
3. If there is a QoS mechanism on your routers, try to prioritize Amazon Connect voice traffic.

‍

**Amazon Connect Endpoint Test:** Ask agents to run the Amazon Connect Endpoint Test using the connectivity tool: <https://tools.connect.aws/endpoint-test/>

The results are available for download as a JSON file. You can load the results file into the tool by selecting the **Load previous results** option. This option displays the contents of the file visually and makes analysis easier. You can also download a bookmark specifically for the provided instance to make future tests easier to run.

‍

**CCP Log Parser:** Downloaded Agent Logs can be reviewed in the CCP Log Parser tool for any errors. The CCP Log Parser is an AWS tool for analyzing the agent logs and overall latency. The output logs assist in troubleshooting any CCP related issues.

<https://tools.connect.aws/ccp-log-parser/>

‍

# Amazon Connect CCP

If an issue is reproducible in the Amazon Connect CCP or Agent Workspace, then we strongly recommend you log an AWS Technical Support Ticket and work with the AWS Support team to troubleshoot the issue in the Amazon Connect CCP or Workspace while Engage is not open. Once the issue is resolved in the CCP or Workspace, but you are still experiencing it in Engage after a hard refresh, then we advise reaching out to the Local Measure Support team at [engage-support@getlocalmeasure.com](mailto:engage-support@getlocalmeasure.com) for further assistance.

‍

# Flow Specific Diagnosis

If changes have been made to Contact Flows, this could be the root cause for various issues.

Review the related Contact Flows’ change history to confirm if recent changes have been made, and by who.

Review the CloudWatch logs in Amazon Console for additional information.

‍

# UI Issues

- A hard refresh should resolve most UI related issues.
- If the button to Accept calls is not working, check that the agent doesn’t have Desk Phone enabled in their Agent settings, as this causes the call to be forwarded to another phone number and they can’t accept the call from the desktop.
- Desktop shows the agent is logged in, but they do not receive calls.   
 - Refresh the page and re-authenticate to log back into Amazon Connect.
 - If the user did not log out at the end of their shift, and just closed the browser, the desktop won’t know their session has expired until they interact with the page or refresh it.

‍
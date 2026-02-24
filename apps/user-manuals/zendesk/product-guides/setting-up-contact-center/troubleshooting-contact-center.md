# Troubleshooting Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696137463066-Troubleshooting-Contact-Center

---

This article provides guidance on troubleshooting steps you can take if you experience any issues with Zendesk Contact Center.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

This article guides you through troubleshooting issues in the Contact Center, covering topics like SSO, call quality, and UI problems. It emphasizes gathering key information, checking network and browser settings, and using AWS tools like the Amazon Connect Endpoint Test and CCP Log Parser. For persistent issues, it suggests logging an AWS support ticket and reviewing contact flow changes and CloudWatch logs.

This article provides guidance on troubleshooting steps you can take if you experience
any issues with Zendesk Contact Center.

Also, you can refer to [Amazon Connect troubleshooting](https://docs.aws.amazon.com/connect/latest/adminguide/troubleshooting.html)
documentation.

This article contains the following topics:

- [General troubleshooting](#topic_k4p_stm_pgc)
- [CloudFormation deployment issues](#topic_r5t_stm_pgc)
- [Single sign-on (SSO) issues](#topic_r5w_stm_pgc)
- [Call or network quality issues](#topic_utx_stm_pgc)
- [Amazon Connect CCP issues](#topic_fmy_stm_pgc)
- [Flow specific diagnosis](#topic_bdz_stm_pgc)
- [UI Issues](#topic_etz_stm_pgc)

## General troubleshooting

The following is important information to have on hand when troubleshooting issues in
Contact Center.

- How many users are affected
- Clear steps to follow to reproduce the issue
- When was the issue first experienced
- Have the affected users tried refreshing their browsers, closed and opened their
  browser, or tried using a different browser
- What part of the product or platform is the issue happening on, for example,
  dashboards, the message text editor, the utility widget, or similar
- Is there a workaround for the issue
- Is the issue reproducible in the [Amazon Connect Contact Control Panel
  (CCP)](https://docs.aws.amazon.com/connect/latest/adminguide/launch-ccp.html)
- Have any changes been made to contact flows, queues, or routing profiles in
  Amazon Connect
- Are the affected agents using softphone or desk phone settings
- Do you see any error messages in the browser console log or network log at the
  time the issue occurs

## CloudFormation deployment issues

When a CloudFormation stack fails to create, AWS automatically rolls back any partial
changes. To diagnose, open the stack in the AWS CloudFormation console and review
the Events tab to find the first failed resource and error message.

Common causes and checks:

- **Prerequisites not enabled in Amazon Connect.** If you see errors like
  “Subscribe CTR (Contact Trace Records) Data Stream,” ensure Contact Trace
  Records streaming is turned on and an Amazon Kinesis Data Stream is configured
  in your Connect instance before deploying.
- **Incorrect parameters.** Verify values such as the Connect instance ARN/ID
  and any region‑specific inputs.
- **Insufficient permissions.** The deploying role must be able to
  create/update IAM, Lambda, EventBridge, API Gateway, Cognito, and related
  resources. Lack of IAM permissions commonly causes failures.
- **Review the failed resource details.** In the Events tab, select the failed
  logical resource to see the full AWS error for targeted remediation.

After resolving the issue, re‑run the deployment using the same quick‑create
link.

Sign‑in note for Cognito deployments: if a user was created with a temporary
password, the first login must allow password change. If needed, set a permanent
password for the user in the Cognito console before testing, or use your SSO
provider.

## Single sign-on (SSO) issues

Typically, issues could be due to the connection or web browser and internal security
policies which could be blocking access.

Try testing the following with the user:

- Checking network connection and VPN.
- Make sure the browser is up to date, particularly after a system update.
- Restart your browser, use a different browser.
- Clear the browser cache.
- If using VPC or VPC with PrivateLink, make sure you have adequate permission to
  access in this manner.
- You can also try authenticating in a private window of your browser to avoid any
  cached credentials.

If the issue persists, log an AWS Support Case from your Amazon Console. AWS will ask
you to upload a HAR file attached to the support case. Export the HAR file while
replicating the issue and check the preserve logs button while working on it.

For more information, see [How to create a HAR file from a browser for an
AWS Support Case](https://aws.amazon.com/premiumsupport/knowledge-center/support-case-browser-har-file/).

## Call or network quality issues

In the event that call quality is impaired or an agent is experiencing latency in the
Contact Center desktop, follow the steps below for debugging purposes:

- **AWS technical support ticket:** When a networking issue has been
  reported, we recommend that a ticket is submitted to AWS support
  simultaneously. The ticket should include a full description of the issue
  experienced by agents, the time of occurrence and the output logs of an
  endpoint test and agent CCP logs (run by the agent who has experienced the
  issue).
- **Amazon Connect Endpoint Test:** Ask agents to run the [Amazon Connect Endpoint Test](https://tools.connect.aws/endpoint-test/) using the
  connectivity tool.

  The results are available for download as a JSON file.
  You can load the results file into the tool by selecting the **Load
  previous results** option. This option displays the contents of
  the file visually and makes analysis easier. You can also download a
  bookmark specifically for the provided instance to make future tests
  easier to run.
- **CCP Log Parser:** Downloaded agent logs can be reviewed in the [CCP log parser tool](https://tools.connect.aws/ccp-log-parser/) for any errors. The CCP log
  parser is an AWS tool for analyzing the agent logs and overall latency. The
  output logs assist in troubleshooting any CCP related issues.

Other recommended troubleshooting:

- Contact your Internet Service Provider to see if there are any stability issues
  or latency problems.
- Check to make sure that the WAN isn't congested.
- If there is a QoS mechanism on your routers, try prioritizing Amazon Connect
  voice traffic.

## Amazon Connect CCP issues

If an issue is reproducible in the Amazon Connect CCP or agent workspace, you can
[submit an AWS support ticket](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) and work with
the AWS Support team to troubleshoot the issue in the Amazon Connect CCP or
workspace. ‍

## Flow specific diagnosis

If changes have been made to contact flows, this could be the root cause for various
issues. Try the following:

- Review the related contact flows’ change history to confirm if recent
  changes have been made, and by who.
- Review the CloudWatch logs in Amazon Console for additional
  information.

## UI Issues

Consider the following options for UI issues:

- A hard browser refresh should resolve most UI related issues.
- If the button to accept calls is not working, check that the agent doesn’t have
  desk phone enabled in their agent settings, as this causes the call to be
  forwarded to another phone number and they can’t accept the call from the
  desktop.
- Desktop shows the agent is logged in, but they do not receive calls.
  - Refresh the page and re-authenticate to log back into Amazon
    Connect.
  - If the user did not log out at the end of their shift, and just closed
    the browser, the desktop won’t know their session has expired until they
    interact with the page or refresh it.
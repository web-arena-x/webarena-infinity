# Testing Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9832930064026-Testing-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

After setting up Contact Center, test it by signing into the agent interface to ensure everything is functioning. Use SSO or Amazon Cognito credentials to access the Contact Center interface. Verify integration by checking if the Connect softphone and agent status controls load. If issues arise, consult the troubleshooting guide. This process helps confirm that your setup is ready for customer interactions.

Once you've finished setting up Contact Center as described in [Getting started with Contact Center](https://support.zendesk.com/hc/en-us/articles/9824150119450), you can test it to make
sure everything is working.

**To test Contact Center**

1. Sign out of the Contact Center admin console and navigate to the Contact
   Center agent login page, https://${Zendesk Instance Name}/agent.
2. Sign in with SSO or the user credentials you set up in Amazon Cognito
   (username and password).

   You'll now be in the Contact Center interface. This app
   links to Connect in the background (using the allowed origin you set and the
   integration configuration you deployed). If your Connect instance is new, there
   might not be much to see yet (until you set up a phone number or chat). However,
   you can verify connectivity by seeing if the Connect softphone and agent status
   controls load in Contact Center.

   For example, you might see your Connect
   agent status indicator in Contact Center and be able to change status or make a
   test outbound call if you've claimed a number. This indicates the integration is
   working.

If you're having problems, see [Troubleshooting Contact Center](https://support.zendesk.com/hc/en-us/articles/9696137463066).
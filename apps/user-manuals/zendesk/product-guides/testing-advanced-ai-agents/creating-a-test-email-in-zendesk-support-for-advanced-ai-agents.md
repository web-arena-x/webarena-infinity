# Creating a test email in Zendesk Support for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357751811610-Creating-a-test-email-in-Zendesk-Support-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

During the testing phase, you may wish to have a safe environment to test the AI agent without having it live for customers and impacting the day-to-day work of your human agents. The way to do this is to create a test email for your testers to email to send their inquiries to, so only those requests that are sent to that test email are responded to.

### Pre-requisites

[AI agent Group Created](https://support.zendesk.com/hc/en-us/articles/8357765429274)

[CRM Integration completed in AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357750858010)

## Creating an Email for Zendesk

To create a [new email address](../setting-up-your-email-channel/adding-support-email-addresses-for-users-to-submit-tickets.md) for your Zendesk Support account you will need to do the following:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Talk and email > Email**.
2. In the Support addresses section, click **Add address**, then select **Create new Zendesk address**.

   ![add_address_-_Zendesk.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7942203111314.png)
3. Enter an address you'd like to use for receiving support requests.
4. Click **Create now**.

## Create a Test View

To add a view in Zendesk, there is a tutorial [here](https://support.zendesk.com/hc/en-us/articles/4408888828570-Creating-views-to-manage-ticket-workflow)

You will want it to have the conditions of when sent to the newly created test email address, assign it to the AI agent group.

## Create a Trigger

Add a Trigger to ensure that only this email address goes to the AI agent and other agents aren't notified. 

This should say that when a ticket is created for the test email and is on the channels of email or webform. Ensure that the checkbox for notifying all agents is unchecked to avoid spamming the full support team.

Once you have completed the test, you can just change the email back to the normal email address you would use.
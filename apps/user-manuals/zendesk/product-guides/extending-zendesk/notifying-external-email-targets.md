# Notifying external email targets

Source: https://support.zendesk.com/hc/en-us/articles/4408883282458-Notifying-external-email-targets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can notify email targets when a ticket is created or updated. Email targets can be used in automation and trigger actions. First you configure a target and then you specify the target using the *Notify by > Target* action.

This article contains the following topics:

- [Setting up a target](#topic_hvf_eoa_vb)
- [Using targets in automations and triggers](#topic_cjz_eqa_vb)
- [Avoiding timeout errors](#topic_y12_xl5_rjb)

## Adding an email target

Note:

- Trial accounts are limited to a maximum of ten targets.
- When two-factor authentication is enabled for agents or admins, you can only use an API token to authenticate your targets, using "[email@example.com](mailto:email@example.com)*/token*" and your token as a password.

You can use ticket triggers or automations to send emails to a specific address. The sending address is the default address associated with your brand.

Email notifications sent to an external Support address on another Support account with whom you have ticket sharing agreements are rejected by the target email address. A ticket will not be created.
This prevents an email loop. If you need to share support requests with another Support account, use the [ticket sharing feature](https://support.zendesk.com/hc/en-us/articles/4408886265370)
instead.

Also, to prevent an email loop, you can't notify your own account's support addresses.

**To add a target**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Targets > Targets**.
2. Select **Add target**.
3. Select **Create target** from the drop-down list at the bottom of the page. If you want to test the target before adding it, select **Test target**.
4. Click **Submit**.

Once you've set up targets, you can edit, delete, and deactivate and reactivate them. See [Managing external targets](https://support.zendesk.com/hc/en-us/articles/4408835069978).

## Using email targets in automations and triggers

Once you've set up email targets, you can use them in automations and triggers. You can enter up to 8192 characters in the body of *Notify by > Target* actions.

Since you're interacting with external targets, there may be a delay between when a trigger or automation runs and when you'll see the results in the external target .

Here's an example of a trigger that notifies a target email address when an urgent ticket is created:

- Meet all of the following conditions
 - **Ticket > Ticket** | **Is** | **Created**
 - **Ticket > Priority** | **Is** | **Urgent**
- Actions
 - **Notify by > Target** | **My Email Target**

## Avoiding timeout errors

If a timeout error is received within 10 seconds of a request being made, Zendesk retries the request. After 21 consecutive failed attempts to retry the request, Zendesk deactivates the target. You'll need to reactivate the target before you can use it again.

Zendesk admins receive a notification when a target is automatically deactivated. They don't receive a notification when a target is manually deleted or deactivated.

The following are the most common causes of timeout errors:

- The message body in the trigger or target page is blank.
- There's a problem with the receiving server.
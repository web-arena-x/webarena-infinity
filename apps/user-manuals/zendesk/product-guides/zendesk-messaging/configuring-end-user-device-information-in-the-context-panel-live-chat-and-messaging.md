# Configuring end-user device information in the context panel (live chat and messaging)

Source: https://support.zendesk.com/hc/en-us/articles/7041910642074-Configuring-end-user-device-information-in-the-context-panel-live-chat-and-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

End-user metadata is captured whenever an end user interacts with Zendesk. Agents can use this information to troubleshoot and address customer inquiries in a timely manner in live chat and messaging tickets.

Note: Device information is displayed only on tickets received via live chat, and web and mobile messaging channels. It is not available for tickets from social and other third-party channels.

This article describes the admin tasks for configuring the displayed information. For information on how agents can view device information, see [Viewing customer context for user, history, and device information](https://support.zendesk.com/hc/en-us/articles/4408829170458).

Not all captured metadata is displayed in the customer context. See [Default Data Types Captured by Zendesk Services](https://support.zendesk.com/hc/en-us/articles/4408837672346) for a complete list of captured metadata in messaging and other Zendesk capabilities and products.

## Configuring displayed device information

By default, device information is displayed in the Agent Workspace [context panel](https://support.zendesk.com/hc/en-us/articles/4408829170458). It appears in its own section, **Device information**, as part of the customer context. Keep in mind that light agents, contributors, and agents in a Chat-only role can't view end user device information.

Displayed device information includes:

- **Location** (optional): City and country associated with the device IP address. Location information is hidden by default.
- **IP address**(optional): The unique number assigned to the device currently being used. Note that this information may not reflect the end user’s originating IP address. IP address is hidden by default.

  Note: You must select this option to display the [Ban IP button and the Banned flag](https://support.zendesk.com/hc/en-us/articles/9418700382618) in Device information.
- **Device type**: End user’s device type and model (if applicable)
- **OS**: The operating system and version being used.
- **Browser**: The browser and version being used.

This information is collected and updated on every user visit.

**To configure device information visibility in the Agent Workspace**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Context panel**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/device_information-ac.png)
2. On the Context panel admin page, select **Show customer’s device information** to show the section in the customer context; deselect this option to hide the section.
3. Under **Limit access to personal information**, choose the visibility settings for the following information.

   - Deselect **Hide IP address** to display the end user’s IP address in the Device information section; select this option to hide the IP address.
   - Deselect **Hide location** to display the end user’s location in the Device information section; select this option to hide the location.
4. Click **Save**. The settings are applied to pre-existing tickets, and to new tickets moving forward.
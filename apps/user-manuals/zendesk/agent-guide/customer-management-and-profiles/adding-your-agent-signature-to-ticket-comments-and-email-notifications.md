# Adding your agent signature to ticket comments and email notifications

Source: https://support.zendesk.com/hc/en-us/articles/8713325400986-Adding-your-agent-signature-to-ticket-comments-and-email-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

As an agent, you can add a personal signature to all the public ticket comments and outgoing
email notifications you send from the agent interface. Your signature can include any text
such as your name and position, your group, contact information, and so on. Use Markdown for
advanced customization (see [Formatting text with Markdown](https://support.zendesk.com/hc/en-us/articles/4408846544922)).

Note: An admin must include the `{{agent.signature}}` placeholder in either the
[common agent signature](#topic_1kj_sbj_2g) or a [branded agent signature](#topic_c51_jkt_nyb) to allow
agents to add personal agent signatures.

**To add a personal agent signature**

1. In Zendesk Support, click your user icon in the upper-right corner and select **View
   profile**.
2. In the **Signature** text box in the left sidebar, enter the signature text and any placeholders.

   ```
   Regards,

   Jane Tolland
   Customer Care Associate
   {{agent.email}}
   ```

Any text that your admin has configured in the common signature or a branded signature is
included with your customized personal signature.
# Adding an agent signature to ticket email notifications

Source: https://support.zendesk.com/hc/en-us/articles/4408822471322-Adding-an-agent-signature-to-ticket-email-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can specify an agent signature in all public ticket comments and outgoing messages when an agent responds using the agent interface. This signature doesn't appear if the agent responds to a ticket by email or in email notifications sent automatically through triggers or automations.

Admins can add a common signature for all agents on the account. If you're using multiple brands, an administrator can also add brand information to the signature. If allowed by admins, agents can personalize their signature. If you're using side conversations (Suite Professional and above), personal agent signatures are included on email side conversations.

This article includes the following topics:

- [Using placeholders in agent signatures](#topic_rck_qry_kzb)
- [Adding a common agent signature](#topic_1kj_sbj_2g)
- [Adding a branded agent signature](#topic_c51_jkt_nyb)

## Using placeholders in agent signatures

Placeholders are references to agent and other data stored in Zendesk. For example:
`{{agent.email}}`. The following classes of placeholders are supported in signatures : "agent", "current\_user", "account", and when used as HTML, "dc" (for dynamic content). The "ticket" placeholder class (such as `{{ticket.assignee.name}}`)
is not supported.

Not all placeholders are supported in signatures. For a list of placeholders allowed in agent signatures, see [Placeholders reference for business rules: Agent data](https://support.zendesk.com/hc/en-us/articles/4408886858138#topic_hmx_zzw_4v).
For general information on placeholders, see [Using placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330).

## Adding a common agent signature

An administrator can add a common signature for all agents on the account. For example, you can include your company name and tagline in the signature.

Agent signatures are added to outgoing messages when an agent responds with a public comment from the agent interface.

**To add a common agent signature**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
2. In the **Signature** text box, enter the signature text and any [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138#topic_hmx_zzw_4v).

   ```
   {{agent.signature}}
   Love your Zendesk
   ```

   The `{{agent.signature}}` placeholder is included by default and allows agents to customize their [personal signature](#topic_uxd_slm_hj). Remove the placeholder if you don't want agents to customize their signatures.

Tip: You can use Liquid markup to set different signatures for different agents. See [Using Liquid markup to set agent signatures](https://support.zendesk.com/hc/en-us/articles/4408881941914).

## Adding a branded agent signature (Suite Growth and above or Support Enterprise)

If you're using multiple brands, you can create a custom signature for each brand. Creating a signature for each brand allows you to add brand-specific information to the agent signature.

Branded agent signatures are included when an agent responds to a ticket with a public comment from the agent interface. Agent signatures, and any brand-specific information you add to them, aren't included in email notifications sent automatically through triggers or automations.

If you want to include other brand-specific information in outgoing emails to customers, make sure you've [updated your email template for multiple brands](https://support.zendesk.com/hc/en-us/articles/4408832356762).

**To add branded agent signatures (Support Enterprise or Suite Growth and above )**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Depending on how your brands and department spaces are configured, you'll see one of the following options:
   - If you have one brand, the Agent signature text box displays.
   - If you have multiple brands, the Branded signature text box displays.

   If you have one brand, click the brand name you want to add a signature to. If you have [department spaces](https://support.zendesk.com/hc/en-us/articles/7584022494874) turned on, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the brand you want to update, then click **Edit**.
3. In the **Branded signature** or **Agent signature** text box, enter the information you want to include in the selected brand's signature. You can enter the information above or below the agent signature placeholder:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/brand_signature.png)
4. Click **Save**.
5. Repeat as needed for your other brands.

## Adding a personal agent signature

As an agent, you can add a personal signature to all your public ticket comments and outgoing email notifications you send from the agent interface. Your signature can include any text such as your name and position, your group, contact information, and so on. Use Markdown for advanced customization (see [Formatting text with Markdown](https://support.zendesk.com/hc/en-us/articles/4408846544922)).

Note: To allow agents to add personal agent signatures, an admin must include the `{{agent.signature}}` placeholder in either the [common agent signature](#topic_1kj_sbj_2g) or a [branded agent signature](#topic_c51_jkt_nyb).

**To add a personal agent signature**

1. In Zendesk Support, click your user icon in the upper-right corner and select **View profile**.
2. In the **Signature** text box in the left sidebar, enter the signature text and any placeholders.

   ```
   Regards,

   Jane Tolland
   Customer Care Associate
   {{agent.email}}
   ```

Any text that your admin has configured in the common signature or a branded signature is included with your customized personal signature.
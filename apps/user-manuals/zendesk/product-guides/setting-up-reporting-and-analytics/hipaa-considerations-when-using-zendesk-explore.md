# HIPAA considerations when using Zendesk Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408831157914-HIPAA-considerations-when-using-Zendesk-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

The Health Insurance Portability and Accountability Act (HIPAA) is a set of rules and
regulations designed to protect the privacy and security of individuals’ personal health
information (PHI).

Zendesk Explore can be configured to be compliant with the HIPAA rules and regulations
pertaining to Business Associates. To ensure the security of you and your customers’
information, you must take the following actions in Zendesk Explore and Zendesk
Support:

- [Review access for your existing agents](#topic_odj_2r4_zgb)
- [Additional considerations](#topic_vmr_2r4_zgb)

## **Review access for your existing agents**

For each agent who currently accesses Zendesk Support Professional or
Enterprise, review their access to Explore using the following sections:

- [Configuring access with Zendesk Support Professional](#topic_y5g_gcs_vkb)
- [Configuring access with Zendesk Support Enterprise](#topic_owj_hcs_vkb)

### Configuring access with Zendesk Support Professional

If you're using Support Professional, you configure agent access to Explore as
follows:

- Configure the default Explore role from the Explore admin menu
- Configure Explore permissions from Zendesk Admin Center

You must be a Support admin to configure access. The available access levels
depend on the version of Explore you are using.

For detailed instructions, see [Giving agents access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970).

### Configuring access with Zendesk Support Enterprise

If you're using Support Enterprise, you configure access to Explore using [custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882). In your custom role settings, you'll
find the option **What can this agent do in Explore?**. The following
settings are available:

- **Create reports and manage permissions:** Gives full admin permission to
  Explore
- **Create reports:** Agents can create, edit and share reports
- **View reports:** Agents can view dashboards only, but cannot edit their
  underlying reports
- **No access:** Agents cannot view or access Explore

Ensure that you review any roles you have assigned to agents to make sure they
have the required level of access to Explore.

For detailed instructions, see [Giving agents access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970-Adding-users-to-Explore).

## **Additional considerations**

In addition to steps you can take above, keep in mind the following
considerations:

- Don’t grant agents more access than they need to view reports. For
  example, if the agent doesn’t need to create reports, grant that agent
  “viewer” access.
- When you export reports from Explore, it’s your responsibility to
  ensure the security of the information in that report. For example, don’t
  send an exported report containing sensitive patient information over an
  unencrypted email system.
- When you create or access Explore reports, sensitive electronic
  patient health information might be displayed on the device you are using.
  It’s your responsibility to ensure that this information can’t be seen or
  accessed by unauthorized people.
- If you share public links to dashboards using Explore Enterprise, remember
  that these can be accessed by anyone on the internet, regardless of whether
  they have a Zendesk account. Always consider protecting your dashboards with
  a strong password. Record the password and store it securely in accordance
  with your organization's security policies. Additionally, always review the
  content of any dashboards you share externally to ensure that sensitive data
  is not leaked.

For more information about HIPAA compliance and Zendesk products, see [Advanced Security: Data at Rest Encryption, Enhanced
Disaster Recovery, and HIPAA Compliance (Enterprise Add-on)](https://support.zendesk.com/hc/en-us/articles/4408836302618) and
[Security Configuration Requirements for HIPAA
Enabled Accounts on Zendesk](https://support.zendesk.com/hc/en-us/articles/4408828395802-Security-Configuration-Requirements-for-HIPAA-Enabled-Accounts-on-Zendesk).

If you have any questions, or need any help, please [contact us](https://support.zendesk.com/hc/en-us/articles/4408843597850).
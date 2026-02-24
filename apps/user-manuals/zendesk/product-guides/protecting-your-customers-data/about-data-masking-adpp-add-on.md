# About data masking (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/7713908123674-About-data-masking-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

The data masking feature in the Advanced Data Privacy and Protection add-on helps protect sensitive information by hiding personally identifiable information (PII) from agents in custom and light agent roles. It limits data exposure, supports GDPR compliance, and allows you to control which user data is visible. Note that data masking doesn't alter database information and has some limitations, such as restricted agent actions.

The data masking feature, part of the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), allows you to hide personally identifiable information (PII) from agents in custom and light agent roles.

Data masking helps reduce unnecessary exposure to sensitive information by limiting the data that agents can view. For example, a company collaborating with high-profile clients may restrict access so that agents only see user data when it's required for their role. This practice also supports compliance with regulations such as the General Data Protection Regulation (GDPR), which emphasizes data minimization and controlled access.

This article includes the following topics:

- [Understanding data masking](#topic_kll_qrj_1fc)
- [Data masking limitations](#topic_d1c_vgm_tfc)
- [Understanding the differences between data redaction and data masking](#topic_pv5_5lv_bfc)

Related article:

- [Turning on and configuring data masking](https://support.zendesk.com/hc/en-us/articles/9368104312602)

## Understanding data masking

Data masking allows admins to create and assign agents to custom and light agent roles to determine which data is masked from agents.

When a role is configured with data masking, agents see only the PII required for their responsibilities, reducing the risk of unauthorized access. Masking is applied at the presentation layer only, so PII in the database remains unchanged. Agents in roles without masking continue to see all PII. When a role with masking settings is saved, Zendesk automatically updates permissions to hide restricted PII. Agents assigned to the masked role will see a lock icon next to any PII fields they are not permitted to view.

Data masking supports masking the following system fields in the Support and Guide areas of Zendesk:

- Name
- Email
- Phone

The system fields listed above will be masked in the following areas of Zendesk Support:

- End-user profile
- End-user fields in the context of a ticket (requester, CCs, followers)
- Email notifications
- Ticket views
- Support search
- Triggers and automations (business rules)
- Side conversations

For Knowledge, PII is masked from agents with permission to [manage Guide](../team-members-and-groups/creating-custom-roles-and-assigning-agents.md#:~:text=help%20center%20permissions.-,Manage%20Guide,-%3A%20Access%20the%20help). This applies to:

- User segments
- User content
- Spam
- Community moderation views

Note that end-user data that has been made public will be visible to agents, even with data masking in place. For example, if moderation is turned on and an end user posts a public comment, their name won't be masked because it can be seen in the help center.

## Data masking limitations

Data masking may restrict certain agent actions that require access to PII. Features such as managing end-user profiles will be unavailable to agents in roles with masking, and some tasks, such as managing suspended tickets, may be limited. Core workflows for solving tickets remain unaffected.

**General limitations**

- Any functionality outside the scope described in [Understanding data masking](#topic_kll_qrj_1fc), including QA, WFM, Talk, and Explore, is not supported with masking.
- Zendesk recommends testing data masking in a [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058).

**Support limitations**

- Managing end-user profiles, merging tickets, and masking of PII in ticket comments are not yet supported.
- Managing organizations, managing suspended tickets, placeholders, legacy CCs, print ticket, and View original email functionality is unavailable for masked agents.
- [AI-generated ticket summaries](https://support.zendesk.com/hc/en-us/articles/8037565521946) may expose PII if turned on.

## Understanding the differences between data redaction and data masking

Data redaction and data masking are both techniques used to protect sensitive information, but they serve different purposes.

Data redaction allows admins or [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to permanently remove sensitive information from tickets, ensuring that deleted data can't be retrieved or viewed by any agents. Agents can [redact ticket content manually](https://support.zendesk.com/hc/en-us/articles/4408846470170), or with the Advanced Data Privacy and Protection add-on, admins can create triggers to [automatically redact ticket data](https://support.zendesk.com/hc/en-us/articles/9248330321050).

Data masking offers an alternative approach to protecting sensitive information. It allows certain roles to have end-user names, email addresses, and phone numbers obscured based on role settings. This means that while the original data remains intact, it's hidden from view for agents without permission. This capability allows customers to maintain data integrity while safeguarding user privacy.

While data redaction permanently removes sensitive information, data masking provides a way to obscure it based on user permissions.
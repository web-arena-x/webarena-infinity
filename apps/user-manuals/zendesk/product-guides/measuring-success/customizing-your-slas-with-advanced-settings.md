# Customizing your SLAs with advanced settings

Source: https://support.zendesk.com/hc/en-us/articles/7412192349466-Customizing-your-SLAs-with-advanced-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Business rules > Service level agreements

A service level agreement, or SLA, is a policy you define that specifies and measures the response and resolution times that your support team delivers to your customers.
There are [seven metrics](https://support.zendesk.com/hc/en-us/articles/4408829459866#topic_gpr_ppv_tr) you can use to define SLA policies.

Advanced settings are available for the First reply time, Next reply time, and Periodic update metrics. They change the logic for when an SLA metric is activated or fulfilled on an individual policy basis. You can define advanced settings for both new and existing SLA policies.

Defining advanced settings for these metrics allows you to customize your SLAs so that they apply in more situations and measure what’s most relevant to your business. This leads to a more efficient support process and an improved experience for agents and end users.

For example, you can define advanced settings for an SLA policy so that it measures periodic updates through internal notes instead of just public replies. This ensures that a ticket is continually being worked on or monitored, even if there’s no update to give to the customer yet.

This article contains the following sections:

- [Defining advanced SLA settings](#topic_vng_wgn_sbc)
- [Understanding advanced settings for SLA metrics](#topic_a1f_mhn_sbc)

Related articles

- [About SLA policies and how they work](https://support.zendesk.com/hc/en-us/articles/5600997516058)
- [Defining SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866)

## Defining advanced SLA settings

Advanced settings for SLAs are available for the First reply time, Next reply time, and Periodic update metrics. You can define advanced settings for both new and existing SLA policies.

When you define advanced settings for an existing policy, your reporting may change as SLA achievements or breaches would be measured differently than before. To compare reporting changes before and after you make changes, note the date when you update your policies.

Alternatively, create a new SLA policy with a different name, using the same criteria as before, but with the new advanced settings applied. If you choose to create a new policy, make sure you [reorder your policies](https://support.zendesk.com/hc/en-us/articles/5610005534618) so that the old SLA policy doesn’t apply.

**To define advanced SLA settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Service level agreements**.
2. Define a [new SLA policy](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies#topic_tsz_1yv_rr) or [edit an existing policy](https://support.zendesk.com/hc/en-us/articles/5610005959962#topic_qpn_fzq_kxb).

   Ensure that the policy you’re editing or creating has a First reply time, Next reply time, or Periodic update metric defined.
3. Click **Advanced settings**.
4. Select the check boxes for the settings you want to apply to the policy.

   See [Understanding advanced settings](#topic_a1f_mhn_sbc)
   to learn more.
5. Click **Add**, then **Save policy**.

   The advanced settings you applied to the metrics take effect the next time a ticket that matches the policy’s criteria is created or updated. If you edited an existing policy, note that SLA policy changes only apply when tickets are subsequently created or updated. They are never retroactively applied.

## Understanding advanced settings for SLA metrics

This section outlines the advanced settings available for the [First reply time](#topic_bhk_c3n_sbc), Next reply time, and Periodic update metrics. In the metric’s advanced settings, the dimmed check boxes describe the standard criteria for how the metric is activated and fulfilled. The standard criteria can’t be edited and always apply to how the metric is activated or fulfilled.

Any advanced settings that you select are applied in addition to the metric’s standard criteria.
For example, if you create a policy, define the first reply time metric, and select the advanced setting for When any ticket is created for an end user with an internal note, first reply time will still be activated on tickets when an end user submits a request with a public comment.

### First reply time

The [First reply time metric](https://support.zendesk.com/hc/en-us/articles/4408829459866#topic_crn_1yk_kxb) is used to measure the time between ticket creation (activating the target) and the first reply from an agent (fulfilling the target).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sla_advanced_firstreplytime.png)

#### Activating the target

The First reply start settings determine which actions activate the target.

Standard settings are *always* selected, and activate the target with the following actions:

- **When an end user submits a request with a public comment**.
- **When an agent forwards an email from an end user to create a ticket**.
- **When an agent creates a side conversation child ticket**.

Advanced settings allow you to activate the target with the following actions:

- **When any ticket is created for an end user with a public comment**. The ticket requester must be an [end user](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles#topic_hlt_cbp_cc) (or customer). This also applies to voicemail tickets.

 For voicemail tickets to activate the First reply time SLA, you must enable the New live call recordings are public option. See [Configuring customer access to call recordings](https://support.zendesk.com/hc/en-us/articles/4408831738266#topic_sfy_x2y_sjb).
- **When any ticket is created for an end user with an internal note**. The ticket submitter must be a [team member](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles#topic_nqx_cbp_cc), but can’t be a [light agent](https://support.zendesk.com/hc/en-us/articles/4408846501402). The requester must be an [end user](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles#topic_hlt_cbp_cc).
- **When a light agent forwards an email from an end user to create a ticket**.
- **When an agent creates a ticket for themselves as the requester**. The ticket submitter *and* requester must be a [team member](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles#topic_nqx_cbp_cc). This can be helpful when an agent reaches out to an internal department for help. Note that the agent creating the ticket can’t fulfill the target.

#### Fulfilling the target

The standard settings for first reply time mark the target as fulfilled when an agent adds the first public reply. With advanced settings, the target can also be fulfilled when an agent or light agent adds an internal note to a ticket.

### Next reply time

The Next reply time metric measures the time between the oldest unanswered customer comment and the next reply from an agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sla_advanced_nextreplytime.png)

Note: You must activate the First reply time metric to use the Next reply time metric.

#### Activating the target

The standard setting is *always* selected, and activates the next reply time target with the following action:

- **When an end user requester adds a new comment**.

Advanced settings allow you to activate the target with the following actions:

- **When any end user replies to a ticket and that reply is added as an internal note**. The replying end user does not need to be the ticket requester. This can be helpful when there are other end users who reply to a ticket that they’re CCed on.
- **When an agent is the requester on the ticket and leaves a new comment**. The new comment can be either a public comment or an internal note.
- **When a light agent requester adds an internal note**. To activate this target, you must select the “When an agent creates a ticket for themselves as the requester” setting and the “When an agent adds an internal note to a ticket” advanced fulfillment option for the First reply time metric.

#### Fulfilling the target

The standard settings for next reply time mark the target as fulfilled when an agent, who is not the requester, adds the next public reply. With advanced settings, the target can also be fulfilled when an agent, who is not the requester, adds an internal note.

### Periodic update time

The Periodic update metric measures the time between each comment from agents.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sla_advanced_periodicupdate.png)

#### Activating the target

The standard setting is *always* selected, and activates the next reply time target with the following action:

- **When an agent adds a public reply**. This can be a standard or custom agent, or a light agent.

Advanced settings allow you to activate the target with the following actions:

- **When an agent adds an internal note**. This can be a standard or custom agent, or a light agent.
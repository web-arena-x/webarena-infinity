# Configuring idle timeout and disconnection settings for unified agent statuses

Source: https://support.zendesk.com/hc/en-us/articles/5286614817562-Configuring-idle-timeout-and-disconnection-settings-for-unified-agent-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Configure idle timeout and disconnection settings to manage agent availability across channels. Set idle timeout to update agent status after inactivity, and adjust disconnection status for network or session disruptions. Customize statuses to suit your team's workflow, ensuring agents are marked as away or offline when needed. This helps maintain accurate agent presence and improves response management.

Location:  Admin Center > Objects and rules > Omnichannel routing
> Status timeouts

[Unified agent status](https://support.zendesk.com/hc/en-us/articles/5133523363226) is part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) and provides a way for agents to control
their availability for email, voice, and messaging from a single menu. However, there
are situations in which Zendesk can infer and automatically update an agent's status,
such as lengthy periods of inactivity or a detected disconnection. Admins can use the
Status timeouts page in Admin Center to configure the desired idle timeout and status as
well as the disconnection status for each unified agent status.

This article contains the following topics:

- [Considerations for configuring idle timeouts and disconnection behavior](#topic_qzr_5hq_rgc)
- [Configuring a status's idle timeout behavior](#topic_wwb_5l1_cwb)
- [Configuring a status's disconnection behavior](#topic_zh3_gh3_jgc)

## Considerations for configuring idle timeouts and disconnection behavior

Consider the following when modifying a status's idle timeout and disconnection
behaviors:

- Updates made to a idle timeout behavior won't be reflected for agents
  currently working in the Agent Workspace until they refresh the page.
- In the event that a disconnection event occurs while an agent is in an idle
  status, the disconnection status overwrites the idle status.
- If an agent is removed from a group while using a custom unified agent
  status that is restricted to that group, when they become idle or
  disconnected, their status changes to Offline.

## Configuring a status's idle timeout behavior

The idle timeout and disconnection settings can be configured individually for each
unified agent status. Idle timeout is turned off by default and must be selected if
you want Zendesk to infer agent status based on session activity. For the purposes
of idle timeout, *inactivity* is defined as no mouse or keyboard interactions
within the Zendesk tab of a browser. However, even if
an agent is idle by this definition, updates to an agent's status by the API cause
the idle timer to reset.

In most cases, the default idle status is *Keep current status* and no idle
timeout value, but, if you turned on idle timeouts prior to September 8, 2025, your
unified agent statuses inherit a default idle status of *Away* or
*Offline* and an idle timeout of *10 minutes*.

### Configuring an idle timeout for a status

To turn on and configure an idle timeout for a status, you must change the
unified agent status's idle status to anything other than *Keep current
status*.

**To configure idle timeout for a status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, select **Omnichannel routing > Status
   timeouts**.
2. In the table of unified agent statuses, find the status you want to
   configure an idle timeout for.
3. Select the preferred **Idle status**. This could be one of the
   standard unified agent statuses (*away* or *transfers only*)
   or a custom unified agent status.

   Selecting *Keep current status*
   turns off idle timeout for the status.
4. Under **Idle timer**, enter a value between 5 and 1440 minutes, after
   which an agent is deemed inactive and their status should be updated to
   the configured idle status.
5. Click **Save**.

### Turning off a status's idle timeout

Admins can turn off idle timeout for each unified agent status individually.

Make sure you inform agents if you disable the fallback status for idle agents.
They will need to manually set themselves to *away* or *offline* when
they are unavailable to receive work.

**To disable idle status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, select **Omnichannel routing > Status
   timeouts**.
2. In the table of unified agent statuses, find the status for which you
   want to turn off idle timeout.
3. Change the **Idle status** to **Keep current status**.
4. Click **Save**.

## Configuring a status's disconnection behavior

In addition to idle timeout, Zendesk can also infer session connectivity based on the
following disconnection events:

- An agent closes the Agent Workspace without signing out (by
  closing down their computer or browser window or putting their computer to
  sleep)
- An agent’s connection is lost due to a network outage

Note: A disconnection event is different from a Zendesk session [expiring](https://support.zendesk.com/hc/en-us/articles/4408832533274).

### Configuring a disconnection status

To turn on and configure a disconnection status, you must set the unified agent
status's disconnection status to anything other than *Keep current
status*.

**To configure a status's disconnection status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, select **Omnichannel routing > Status
   timeouts**.
2. In the table of unified agent statuses, find the status you want to
   configure an idle timeout for.
3. Select the preferred **Disconnection status**. This could be one of
   the standard unified agent statuses (*away*, *transfer only*,
   or *offline*) or a custom unified agent status.

   Selecting *Keep
   current status* turns off the disconnection status.
4. Click **Save**.

### Turning off a status's disconnection status

Admins can turn off the disconnection status behavior for each unified agent
status individually.

**To disable a status's disconnection status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, select **Omnichannel routing > Status
   timeouts**.
2. In the table of unified agent statuses, find the status for which you
   want to turn disconnection status.
3. Change the **Disconnection status** to **Keep current
   status**.
4. Click **Save**.
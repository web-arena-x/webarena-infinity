# Configuring caller ID on calls forwarded by IVR or overflow

Source: https://support.zendesk.com/hc/en-us/articles/10183620506394-Configuring-caller-ID-on-calls-forwarded-by-IVR-or-overflow

---

Admins andagents in custom roles with permissioncan set the phone number shown to recipients when Zendesk forwards a call as part of anIVRoroverflowworkflow. The phone number shown is referred to as the forwarding caller ID.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can set
the phone number shown to recipients when Zendesk forwards a call as part of an [IVR](https://support.zendesk.com/hc/en-us/articles/4408885628698) or [overflow](https://support.zendesk.com/hc/en-us/articles/4408832017690#id_4408832017690__topic_zgz_mpf_dfb) workflow. The phone number shown is
referred to as the forwarding caller ID.

In some countries, telecom rules restrict which caller ID can be shown on forwarded
calls. If the caller ID isn’t permitted, the forwarded call might not complete. These
restrictions are intended to reduce unwanted calls and caller ID spoofing, where callers
falsify their number to disguise their identity.

This article explains how forwarding caller ID works and which option to select based on
local regulations.

This article contains the following topics:

- [About local restrictions](#topic_uqg_q2r_c3c)
- [Configuring forwarding caller ID](#topic_yqg_q2r_c3c)

Related articles:

- [Managing phone line settings](https://support.zendesk.com/hc/en-us/articles/4408823877146)
- [Zendesk voice and text number regulatory
  requirements](https://support.zendesk.com/hc/en-us/articles/4408824253978)

## About local restrictions

Some countries and carriers limit which caller IDs can be shown to call recipients on
forwarded calls, to reduce caller ID spoofing.

Because a forwarded call is treated like a new outbound call, carriers might reject
calls that display a caller ID the forwarding party doesn’t control, such as the
original caller’s number or an anonymous caller ID. If the caller ID you select
isn’t permitted, the forwarded call might not complete. For example, the destination
number might not ring. The behavior can vary by country, carrier, and call scenario
and could change over time.

### Country restrictions

The following countries have known restrictions that can affect call forwarding
based on the caller ID option you select. For a definition of the options, see
[Configuring forwarding caller
ID](#topic_yqg_q2r_c3c).

If your destination country isn’t listed, start with the Caller’s
number option.

|  |  |  |
| --- | --- | --- |
| **Country** | **What you might see** | **Recommended option** |
| Australia | Forwarded calls might fail when the original caller is anonymous. | Use either the:   - Talk number - Talk number for anonymous calls only |
| Austria | Enforcement is tightening, and forwarded calls might fail depending on the caller ID shown. | Talk number |
| Italy | Enforcement is tightening, and forwarded calls might fail depending on the caller ID shown. | Talk number |
| Spain | Enforcement is tightening, and forwarded calls might fail depending on the caller ID shown. | Talk number |

## Configuring forwarding caller ID

When Zendesk forwards a call to an external phone number, it places a new call to
that destination. The caller ID shown to recipients on an IVR or overflow-forwarded
call depends on the option you select in **Forwarding caller ID**. This setting
doesn’t apply to calls forwarded to agents or transferred to external numbers.

**To configure forwarding caller ID**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab.
3. Click the line you want to change settings for.
4. Under **Forwarding caller ID**, select one of the following options:
   - **Caller’s number**: The forwarded call displays the original
     caller’s phone number. This is the default value.
   - **Talk number**: The forwarded call displays your Zendesk Talk
     number.
   - **Talk number for anonymous calls only**: The forwarded call
     displays the caller’s number when available, but uses your Talk
     number when the original caller ID is anonymous.
5. Click **Save changes**.
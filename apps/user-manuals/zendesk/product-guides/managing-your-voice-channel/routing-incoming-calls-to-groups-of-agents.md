# Routing incoming calls to groups of agents

Source: https://support.zendesk.com/hc/en-us/articles/4408885952922-Routing-incoming-calls-to-groups-of-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

For each of your phone lines, you can choose to route incoming calls to only the agent groups you choose.

If your plan includes it, you can route calls using IVR instead of group routing. For details, see [Routing incoming calls with IVR](https://support.zendesk.com/hc/en-us/articles/4408885628698).

If you’re using the Agent Workspace, you can route calls using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514). With the standard omnichannel routing configuration, calls can only be routed to a single group. If you need to route calls to multiple groups at a time, you can [create custom omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858).

**To route calls to specific groups**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab.
3. Click the number you want to edit.
4. Click the **Routing** tab.
5. In the **Group Routing** section, select one or more groups to route calls to. If you don't enable a group, calls are routed to all available agents.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_grouprouting1.png)
6. If you chose more than one group, also choose a default group from the drop-down menu next to **Default group**. Calls are routed to the default group first if agents in that group are available. If no agents from any of the selected groups are available, resulting voicemails are also assigned to the default group.

   When three or more groups are selected, there is no hierarchy to the non-default groups. All voice channel agents in those groups are put into a single assignment pool. Call routing is determined by an agent's online status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_defaultgroup.png)
7. When you are finished, click **Save changes**.

Note: If [call recording is enabled](https://support.zendesk.com/hc/en-us/articles/4408831738266#topic_zwp_syc_yt), recording continues after you transfer a call internally (to another agent or group) or externally (to an end-user or external number).
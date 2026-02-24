# Managing overflow calls and after-hours call routing

Source: https://support.zendesk.com/hc/en-us/articles/4408832017690-Managing-overflow-calls-and-after-hours-call-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

An *overflow* call is a call that cannot currently be taken by any agents or answered by voicemail. This can happen for the following reasons:

- All agents are offline.
- All agents decline an incoming call.
- All agents miss an incoming call.
- The maximum queue wait time is exceeded.
- The maximum queue size is reached.

This article describes options for managing overflow and after-hours calls, including the following topics:

- [Handling overflow calls with omnichannel routing](#id_4408832017690__section_flm_yfd_wbc)
- [About adding an overflow number to a Zendesk number](#id_4408832017690__section_zgz_mpf_dfb)
- [Adding an overflow number (for phone lines)](#id_4408832017690__section_q45_qpf_dfb)
- [Adding an overflow number (for digital and SIP-IN lines)](#id_4408832017690__section_ics_krn_nrb)
- [Adding an overflow number when business hours are configured (for phone lines)](#id_4408832017690__section_bhk_rpf_dfb)
- [Adding an overflow number when business hours are configured (for digital lines)](#id_4408832017690__section_bks_qrn_nrb)

Note: Outbound calls cannot be made from toll-free numbers. Therefore, these numbers can't be used as an overflow number.

## Handling overflow calls with omnichannel routing

When you [turn on](https://support.zendesk.com/hc/en-us/articles/5866925319962)
[omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), you can configure an overflow behavior by [creating custom queues](https://support.zendesk.com/hc/en-us/articles/6716530152858). Within each custom queue, admins can define primary and secondary groups. Omnichannel routing will route calls to the primary groups first, treating them as a single collective pool of agents, and "overflow" to the pool of secondary groups only when necessary. Although you can still overflow to alternative numbers, when using omnichannel routing queues, it isn't necessary because the overflow behavior happens between the primary and secondary groups of agents configured for the queues.

For more information, see [Understanding how omnichannel routing uses queues to route work to agents](https://support.zendesk.com/hc/en-us/articles/6712096584090) and [Creating custom omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858).

## About overflow phone numbers for Zendesk lines

When you aren't using omnichannel routing, you can provide a better experience for callers by adding an overflow phone number to each phone line you've added.

When a call is not answered by an agent, and voicemail is off, the call will be sent to the overflow number. This could be the number of an external support organization, or an on-call agent that you use outside of your normal business-hours, or during holidays.

Things to consider when you set up an overflow number include:

- When a call is sent to an overflow number that is not a Zendesk number, a ticket is created with the tag, **call\_overflow**.
- When a call is sent to an overflow number that is a Zendesk number, a regular ticket with no tag is created.
- If recording is enabled for that number, any tickets created include a recording of the overflow call.
- Overflow calls are charged as normal calls, including recordings, when enabled.
- When a call is sent to an overflow number, the caller ID sent to the overflow number will be that of the original caller.

When voicemail is turned off, no overflow number is configured, and no agents are available to take a call, your configured voicemail-off greeting plays, and then the call is disconnected.

If you want to always send calls to the overflow number when they cannot be answered, see [Adding an overflow number](https://support.zendesk.com/hc/en-us/articles/4408832017690#zug_talk_overflow__section_q45_qpf_dfb).

If you want to send calls to the overflow number depending on the business hours you have configured, see [Adding an overflow number when business hours are configured](https://support.zendesk.com/hc/en-us/articles/4408832017690#zug_talk_overflow__section_bhk_rpf_dfb).

Tip: If voicemail is turned on, you cannot enable the **Overflow calls** option.

## Adding an overflow number (for phone lines)

If you don't have business hours configured, follow these steps to add an overflow number to Zendesk lines that are phone lines (not digital or SIP-IN lines).

**To add an overflow number (for phone lines)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the **Lines** tab, open a phone line for editing.
3. On the **Routing** tab (of the phone line), make sure that the **Schedule** drop-down list is set to **Always route calls**.
4. On the **Overflow** tab, turn on the **Overflow calls** toggle, and then enter a valid phone number that calls will overflow to.

   ![Overflow page 1](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_overflow_page.png)
5. When you are finished, click **Save changes**.

   Now, when calls are not answered by an agent, and voicemail is off, calls will be diverted to the overflow number you entered.

## Adding an overflow number (for digital and SIP-IN lines)

If you don't have business hours configured, follow these steps to add an overflow

**To add an overflow number (for digital or SIP-IN lines)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the **Lines** tab. open a digital or SIP-IN line for editing.
3. On the **Settings** tab of the line), make sure that the [Enable overflow and agent forwarding for this line](https://support.zendesk.com/hc/en-us/articles/4408823877146#topic_zhp_hjv_dhb) check box is selected and that, in the drop-down list, an outbound number is selected.

   Note: When working with a digital or SIP-IN line, the **Overflow** tab only displays when this check box is selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_outbound_number_enabled.png)
4. On the **Routing** tab, make sure that the **Schedule** drop-down list is set to **Always route calls**.
5. On the **Overflow** tab, select the **Overflow calls** check box, and then enter a valid phone number that calls will overflow to.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_overflow_disabled.png)
6. When you are finished, click **Save changes**.

   Now, when calls are not answered by an agent, and voicemail is off, calls will be diverted to the overflow number you entered.

## Adding an overflow number when business hours are configured (for phone lines)

If you have business hours configured, follow these steps to add an overflow number to Zendesk lines that are phone lines (not digital or SIP-IN lines).

**To add an overflow number when business-hours are configured (for phone lines)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the **Lines** tab, open a phone line for editing.
3. On the **Routing** tab (of the phone line), make sure that the **Schedule** drop-down list is set to **Business Hours**.
4. On the **Overflow** tab, specify overflow options for calls received to your phone line during certain business hours (specified on the **Routing tab**).

   For example:

   - In the **Inside schedule** section, turn on the **Overflow calls** toggle, and then enter a phone number that calls will outflow to when placed inside of your scheduled business hours.
   - In the **Outside schedule** section, turn on the **Overflow calls** toggle, and then enter a phone number that calls will overflow to when placed outside of your scheduled business hours.

   ![Overflow page 2](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_overflow_page2.png)
5. When you are finished, click **Save changes**.

   Now, when calls are not answered by an agent, and voicemail is off, calls will be diverted to the overflow numbers you entered, according to the schedule options you configured.

## Adding an overflow number when business hours are configured (for digital or SIP-IN lines)

If you have business hours configured, follow these steps to add an overflow number to digital or SIP-IN lines (not phone lines).

**To add an overflow number when business-hours are configured (for digital or SIP-IN lines)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the **Lines** tab, open a digital or SIP-IN line for editing.
3. On the **Settings** tab of the line), make sure that the [Enable overflow and agent forwarding for this line](https://support.zendesk.com/hc/en-us/articles/4408823877146#topic_zhp_hjv_dhb) check box is selected and that, in the drop-down list, an outbound number is selected.

   Note: When working with a digital or SIP-IN line, the **Overflow** tab only displays when this check box is selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_outbound_number_enabled.png)
4. On the **Routing** tab, make sure that the **Schedule** drop-down list is set to **Business Hours**.
5. On the **Overflow** tab, specify overflow options for calls received to your digital or SIP-IN line during certain business hours (specified on the **Routing tab**).

   For example:

   - In the **Inside schedule** section, select the **Overflow calls** check box, and then enter a phone number that calls will outflow to when placed inside of your scheduled business hours.
   - In the **Outside schedule** section, select the **Overflow calls** check box, and then enter a phone number that calls will overflow to when placed outside of your scheduled business hours.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_overflow_enabled_with_business_hrs.png)
6. When you are finished, click **Save changes**.

   Now, when calls are not answered by an agent, and voicemail is off, calls will be diverted to the overflow numbers you entered, according to the schedule options you configured.
# About native Call time duration metrics

Source: https://support.zendesk.com/hc/en-us/articles/8202998599066-About-native-Call-time-duration-metrics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you'll learn more about some of the metrics that help you measure the duration between two events.

This article covers only the native call metrics. Support and SLA metrics might have identical names but their behavior is different. See [About native Support time duration metrics](about-native-support-time-duration-metrics.md#:~:text=The%20native%20duration%20metrics%20are,the%20specific%20events%20take%20place.) and [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies#topic_gpr_ppv_tr).

The leg time metrics have a similar definition to the full call time metrics, but they specifically pertain to individual segment events within a call. For more details, refer to the section on [Reporting on calls with Explore](../reporting-on-your-voice-channel/reporting-on-calls-with-explore.md#topic_utw_qd5_yjb).

For more information about the voice metrics and attributes you can use with Explore, see [Metrics and attributes for Zendesk Voice](https://support.zendesk.com/hc/en-us/articles/4409156145434-Metrics-and-attributes-for-Zendesk-Talk).

This article contains the following topics:

- [Call answer time](#topic_qgr_fhb_ldc)
- [Call wait time](#topic_vvy_fhb_ldc)
- [Call IVR time](#topic_elz_fhb_ldc)
- [Call talk time](#topic_dzz_fhb_ldc)
- [Call consultation time](#topic_edf_ghb_ldc)
- [Call on-hold time](#topic_gmf_ghb_ldc)
- [Call wrap-up time](#topic_lwf_ghb_ldc)
- [Call duration](#topic_m2g_ghb_ldc)

Related articles:

- [Reporting on calls with Explore](https://support.zendesk.com/hc/en-us/articles/4408885612314)
- [About native Support time duration metrics](https://support.zendesk.com/hc/en-us/articles/4408834848154)

## Call answer time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met1.png)

- **Definition**: The duration between the customer first connecting to the system and the first conference with an agent. Repetition, such as waiting after a transfer occurs, is not included. Voicemails are also excluded from this number.
- **First timestamp**: End user called the support number.
- **Second timestamp**: End user connected to an agent.

## Call wait time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met2.png)

- **Definition**: The duration the end user waits in the queue to talk to an agent.
- **First timestamp**: End user entered in the queue after finishing IVR.
- **Second timestamp**: End user connected to an agent.

## Call IVR time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met3.png)

- **Definition**: The duration that an end user spent in an interactive voice response (IVR) system.
- **First timestamp**: End user started interacting with IVR.
- **Second timestamp**: End user finished interacting with the IVR.

## Call talk time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met4.png)

- **Definition**: The duration spent talking from the customer’s perspective or the time spent in a conference with an agent. If the call was transferred this will include all agent conferences with the customer.
- **First timestamp**: End user started talking with the agent.
- **Second timestamp**: End user finished talking with the agent.

## Call consultation time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met5.png)

- **Definition**: The duration of consultation time. Sums the value of any number of agent-to-agent consultations.
- **First timestamp**: Agent started consulting with another agent.
- **Second timestamp**: Agent ended consulting with another agent.

## Call on-hold time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met6.png)

- **Definition**: The duration a call was on-hold from the customer’s perspective.
- **First timestamp**: End user set to on-hold.
- **Second timestamp**: End user took off from on-hold.

## Call wrap-up time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met7.png)

- **Definition**: The duration that an agent spent in the wrap-up stage after a call.
- **First timestamp**: Agent started wrap-up stage.
- **Second timestamp**: Agent finished wrap-up stage.

## Call duration

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met8.png)

- **Definition**: The total call duration for an end user from when the call is connected until it is disconnected.
- **First timestamp**: End user connected.
- **Second timestamp**: End user disconnected.
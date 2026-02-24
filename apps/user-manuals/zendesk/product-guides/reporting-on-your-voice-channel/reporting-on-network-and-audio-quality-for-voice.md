# Reporting on network and audio quality for voice

Source: https://support.zendesk.com/hc/en-us/articles/4408833546522-Reporting-on-network-and-audio-quality-for-voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

When your call audio or network quality drops, you'll see a notification in the
call console.

These days, more agents are working remotely which presents challenges helping
to diagnose call quality issues. In this article you'll learn how agents are notified
when call quality issues occur, and how admins can report on these issues and configure
computers and the network to improve things.

This article contains the following sections:

- [Headset audio level notifications](#topic_sym_qc5_hlb)
- [Call connection issue notifications](#topic_orl_rc5_hlb)
- [Reporting on call quality issues](#topic_akd_jd5_hlb)

## Headset audio level notifications

If the call audio quality drops, you'll see a warning icon in the call console.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_problem_2.png)

If you see this warning, check your headset is plugged in and the microphone input
levels are high enough. Also, make sure you haven't muted the microphone. Finally,
try a different headset to ensure the one you are using isn't faulty.

For more information about getting the best audio quality, see [Preparing to offer voice support](https://support.zendesk.com/hc/en-us/articles/4408827987482).

## Call connection issue notifications

If network conditions affect the call quality, you'll see a warning icon in the
console. Click the icon to see more details about the problem.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_problem_1.png)

The [network requirements](https://support.zendesk.com/hc/en-us/articles/4408831417498) article contains a
wealth of information to help you avoid and troubleshoot issues. Note that an
administrator will need to configure some of the network settings you might need to
change.

## Reporting on call quality issues

There are a number of issues that might happen on a call leg including:

- **high\_jitter**: Two conditions can result in calls being tagged with high
  jitter, average jitter of 5ms and max jitter of 30ms, or more than 1% of packets
  delayed by 200ms or more.
- **high\_latency**: The Twilio-internal RTP traversal time exceeded 150ms.
- **high\_packet\_loss**: Packet loss was larger than five percent.
- **high\_pdd**: Post-dial delay (PDD) is the number of seconds elapsed between
  dialing the last digit of the phone number and the start of ringing. The
  percentage of total calls are represented with high PDD compared against the
  99th percentile of all calls to the destination country.
- **pstn\_short\_duration:** Identifies short outbound calls, when the duration
  of the outbound call is less than 10 seconds to PSTN destinations.

  Note: Frequent
  short outbound calls (under 10 seconds) can cause carriers to tag your
  numbers as low trust. Your calls can then be marked as spam or blocked.
  Monitor this metric and adjust your outbound calling to reduce
  short‑duration calls.
- **silence**: Silence was detected on the call. This could be due to a missing
  audio stream or a completely silent stream received. See [What does the silent tag
  mean?](https://support.zendesk.com/hc/en-us/articles/9211159721498)

The information in the [network requirements](https://support.zendesk.com/hc/en-us/articles/4408831417498) article can help you troubleshoot
many of these issues. You can use one of the following two methods to report on call
quality issues:

- [Reporting on call quality with Explore](#topic_ly2_wp5_mmb)
- [Reporting on call quality with the Incremental Exports API](#topic_mgl_wp5_mmb)

### Reporting on call quality with Explore

Zendesk Explore gives you comprehensive call quality reporting capabilities. For
example, you can report on good quality calls, bad quality calls, or dig-in to
find detailed call quality information.

The pre-built dashboard contains several reports to help you monitor
call quality. For more information, see [Analyzing your Talk activity](https://support.zendesk.com/hc/en-us/articles/4408836253338).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_2020_dashboard_4.png)

On Professional plans and above, you can build your own reports and dashboards
using Explore's metrics and attributes. For help creating reports, see [Creating queries](https://support.zendesk.com/hc/en-us/articles/4408821589530). To see the available
metrics and attributes, read [Metrics and attributes for Zendesk
Talk](https://support.zendesk.com/hc/en-us/articles/4409156145434).

### Reporting on call quality with the Incremental Exports API

You can use the Incremental Exports API to collect data to report on call quality
issues. You can access information about call leg quality (Agent Leg and
Customer leg) information from the [Incremental Exports API](https://developer.zendesk.com/api-reference/voice/talk-api/incremental_exports/) soon after the
call ends.
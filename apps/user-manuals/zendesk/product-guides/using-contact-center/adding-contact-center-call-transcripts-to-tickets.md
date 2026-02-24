# Adding Contact Center call transcripts to tickets

Source: https://support.zendesk.com/hc/en-us/articles/9459081200538-Adding-Contact-Center-call-transcripts-to-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

To add call transcripts to tickets, configure your Amazon Connect contact flow and set up post-call triggers in the Amazon console. Enable speech analytics and redact sensitive data in Amazon Connect. Then, activate the necessary triggers in the Amazon console for your post-call lambda. This setup ensures call transcripts are captured and associated with the relevant tickets.

Before you can add Zendesk for Contact Center call transcripts to your tickets, you need
to configure the post-call lambda in your Amazon console. A *lambda* is a small
piece of code that runs when triggered by an event. You need to enable two triggers in
the Amazon console that allow your call transcripts to be captured within the Zendesk
ticket associated with the call.

This article contains the following topics:

- [Configuring Amazon Connect](#topic_hll_g4v_zfc)
- [Configuring your triggers](#topic_t4n_ncw_zfc)

## Configuring Amazon Connect

Before you start capturing call transcripts, you must configure your Amazon Connect
contact flow.

**To configure Amazon Connect**

1. In your Amazon Connect contact flow, include the **Set recording and analytics
   behavior** block in the flow.

   ‍![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_36.png)
2. In the Set recording and analytics behavior block, in Contact Lens speech
   analytics, enable speech analytics, then select **Real-time and post-call
   analytics**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_37.png)
3. Under Redaction, select **Redact sensitive data**, then customize the
   redaction settings to fit your requirements.

   Note: The data redaction is strict and might redact non-sensitive data. Only
   select critical sensitive data to be redacted.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_38.png)

### Configuring your triggers

Once you've configured Amazon Connect, you can configure the triggers for your
post-call lambda in the Amazon console.

**To configure your triggers**

1. In the Amazon console, navigate to Lambdas.
2. In the **Functions** section, search for "post."

   This returns a
   function with a name containing "VoicePostCa."
3. Open this function, then on the Function overview page, select
   **Configuration** > **Triggers**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_39.png)
4. Click **Kinesis**, then click **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_40.png)
5. On the Edit trigger page, click **Activate trigger**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_41.png)
6. Click **Save**.
7. Beside **EventBridge**, click the link in the name.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_42.png)
8. In the **EventBridge** rule details page, click **Enable**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_43.png)

   Note: If a dual stack upgrade is performed, then these triggers must be
   disabled on the old lambda before you enable them on the new
   lambda.

Now, your call transcripts will be shown in Contact Center.
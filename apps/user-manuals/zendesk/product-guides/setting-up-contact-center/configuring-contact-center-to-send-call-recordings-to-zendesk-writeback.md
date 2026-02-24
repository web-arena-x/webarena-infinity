# Configuring Contact Center to send call recordings to Zendesk (writeback)

Source: https://support.zendesk.com/hc/en-us/articles/9696142065306-Configuring-Contact-Center-to-send-call-recordings-to-Zendesk-writeback

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Enable call recording writeback by activating AWS Lambda functions. This setup sends call transcripts to tickets after a voice call. Start by turning on the voice post-call Lambda, and repeat for ContactLensEventsLambda and CTRIngestLambda. Remember to disable triggers on old Lambdas before enabling them on new ones if a dual-stack upgrade is performed. Refer to Amazon's documentation for the latest Lambda usage details.

To configure Contact Center to send call recordings back to Zendesk following a
call (known as *writeback*), turn on the voice post-call Lambda in AWS.

Tip: **AWS Lambda** is a service that lets you run code without setting
up or managing servers. It's useful for tasks that only need to happen once in a
while, like responding to a user clicking a button or a file being uploaded.

**To turn on writeback**

Important: For the latest information about using Lambdas in the Amazon
Console, see [Amazon's product documentation](https://docs.aws.amazon.com/lambda/).

1. In your AWS console, go to the Lambda page.
2. In the Functions section of the page, search for "post". This will return a function
   called "VoicePostCa".
3. Click the function to open it and, on the function overview page, click
   **Configuration** > **Triggers**.
4. From the list of triggers, select the checkbox for **Kinesis**, then click
   **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_16.png)
5. On the Edit trigger page, click **Activate trigger**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_17.png)
6. Click **Save**.
7. From the list of triggers, click the hyperlink next to the EventBridge
   trigger.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_18.png)
8. On the EventBridge rule details page, click **Enable**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_19.png)
9. Repeat the above steps for the following Lambda functions:
   - ContactLensEventsLambda: Process Contact Lens analytics and rules
     events to add to tickets.
   - CTRIngestLambda: Ingest and parse Contact Trace Records (CTR) to
     add call metadata to tickets.

     Note: These lambdas are only available if your
     setup is on the Zendesk infrastructure. Access the non-Zendesk
     infrastructure instructions [here](https://support.zendesk.com/hc/en-us/articles/9907359706650#final_cc_writeback:~:text=to%20be%20redacted.-,Turning%20on%20writeback,-Next%2C%20configure%20your).

Now, after a Contact Center voice call, the call transcript will be added to
the Zendesk ticket.

Note: If a [dual-stack
upgrade](https://support.zendesk.com/hc/en-us/articles/9829206009242#topic_uzp_34z_hgc) is performed, then these triggers must be turned off on the old
Lambda and only then turned on for the new Lambda.
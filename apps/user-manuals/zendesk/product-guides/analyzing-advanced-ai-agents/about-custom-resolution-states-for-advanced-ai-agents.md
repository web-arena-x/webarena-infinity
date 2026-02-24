# About custom resolution states for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756466586-About-custom-resolution-states-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Note: Custom resolutions will be removed on February 28, 2026. For more information, see [Announcing end of life for custom resolutions in AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/9747676998682).

Custom resolution states unlock a greater analytic potential to have granular and actionable insights to track the performance of the AI agent more accurately and in a transparent manner.

You may be wondering how many conversations end in an escalation. How many didn't receive a resolution and just dropped off? Was the customer informed of the self-service guidance or instructions but didn’t finish the flow?

By having the answers to these questions you are empowered to make changes to the conversation flow to provide the best experience, as you will have better visibility on which conversations are problematic or include insights.

This article contains the following topics:

- [About resolutions](#h_01GHTMQJWCNAM5NQBSMAXZGFFS)
- [Setting custom resolution states](#h_01GHTMQXN0Q4SVXW86HA7273H0)
- [Recommendations](#h_01GNY5V2G4HNW5Y997A92HSTZX)
 - [Structuring your resolutions](#h_01GNY5VGR67YG5A464R6VPSHSB)
 - [Using the informed state](#h_01GNVCDV9VQ7GXME85YPNE9KXJ)
 - [How to use the unresolved state](#h_01GNY5W2SGCE137T9KE8CZN0BY)
- [Resolutions in analytics](#h_01GHTMR3M6FYATX6CBQCD665G8)
- [Resolutions in conversations logs](#h_01GHTMRKRV96DG1E8K3CFWJ6R9)
- [FAQ](#h_01GHTMRXMA7926CCXWAZ0BFK04)

## About resolutions

The table below describes the available custom resolution states.

| | |
| --- | --- |
| **Custom resolution state** | **Definition** |
| Undefined | AI agent conversations that ended without a custom resolution state, often due to drop-off or use cases missing a custom resolution state. |
| Informed | AI agent conversations where the AI agent provided guidance to the customer. For more information, see [Using the informed state](#h_01GNVCDV9VQ7GXME85YPNE9KXJ). |
| Resolved | AI agent conversations that ended with a meaningful resolution and no further questions from the customer. |
| Unresolved | AI agent conversations where the issue was not answered or resolved. |
| Escalated to agent | AI agent conversations that were escalated to a human agent. This state is automatically set when the conversation flow reaches an Escalation block in a dialogue with the “Forward to an agent” or “Custom escalation” option set. |
| Escalated via email | AI agent conversations that were converted into an email ticket. This state is automatically set when the conversation flow reaches an Escalation block in a dialogue with the “Send an email” option set. |

## Setting custom resolution states

From the dialogue builder, you can add the applicable states to any message block to highlight whether a user was informed, or if the query was resolved/unresolved or escalated. The final resolution of a conversation can be reviewed in the conversation logs afterward.

**To set a custom resolution state**

1. Navigate to an Intent or Template Reply 
   ![DLB_Intent_1.gif](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_8524316429202.png)
2. Select the block you would like to apply the state to 
   ![DLB_note_2.gif](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_8524316434834.png)
3. On the details tab, scroll to Resolutions and select the appropriate state from the drop-down 
     
   ![DLB_resolutions.gif](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_8513921437714.png)
4. Press **Save Draft** or **Publish**to save your changes.

An important thing to note is that each block can only have one custom resolution state associated with it as when a user passes that block that custom resolution state will be applied. The resolution of a conversation will stay the same after passing the selected block until a new resolution is set. Therefore there is no need to cover all the following blocks with the same resolution type. 
Recommendations

### Structuring your resolutions

Use the [conversation funnel model](https://support.zendesk.com/hc/en-us/articles/8357758797338) from your onboarding as inspiration as you will likely be following a linear path of informing the user of information, checking as to whether this resolves their issue and can apply the resolved / not resolved state based on the response, then the escalation status based on the escalation type from the non-resolved or process-based escalation.

![image__31_.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9418358370194.png)

### Using the Informed state

The informed state should be used when a message is sent that gives the customer information that enables them to handle the situation themselves. Alternatively, where the AI agent is providing the customer with information that they must then come back to that furthers the conversation, for example, please send me a picture of the defect or the invoice number. This way if they drop off the chat, perhaps to go retrieve that information and come back later, then it still counts as the AI agent giving them key information that helps the process along for next time.

### When not to use the Informed state

Don't use informed when changing the language as there hasn't been a "real" Intent handled.

Depending on the solution, you might not want to use the informed state to say that there is no solution available unless it would be the same as what a human agent would do.

### How to use the Unresolved state

Use this as part of the resolution check or feedback flows to indicate whether the user is satisfied or received an answer that didn't help. This then helps with identifying those who drop off before escalation or where conversations can be improved. This makes reviewing conversations within the conversation logs faster.

We would recommend not using this as the first custom resolution state as then this will include everyone who drops off the chat early making it very manual to differentiate truly unresolved/dissatisfied users and those who just drop off.

## Resolutions in analytics

For information on reporting on custom resolutions, see [Analyzing advanced AI agent performance with the Reporting dashboard](https://support.zendesk.com/hc/en-us/articles/9510024609178).

## Resolutions in conversations logs

Within the conversation logs, you have the ability to review the different states associated with a conversation by using the toggle at the bottom of the table to switch between the original states of AI agent-handled or escalated. Using the status filter toggle at the bottom of the conversations table.

![CL_switch_2.gif](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_8557709970834.png)

To review conversations associated with a particular state you have the ability to do this by clicking Add Filter, navigating to Resolutions, and then selecting the specific state(s) you would like to filter by.

![CL_filter_3.gif](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_8557709974930.png)

## FAQ

### Can I create my own status?

In time - we would like feedback to know which states you would like added if these are common and can be added for everyone and if we find everything is super specific per group and necessary we will introduce custom resolutions for people to set.

If there is a particular state you would like please let your CSM know.

### Can I have a setting that removes the last set state?

No, the last set state always remains so we recommend that you include states in all your conversation so that it gets a new state based on the flow it is going down.

### Can I see all the states a conversation goes through?

Currently, you cannot see a progress bar of a conversations states, only the last most state is displayed in the analytics and conversation logs, however, we plan to add this in the future to show how conversations flow - which will be especially impactful for longer or multi-intent conversations.

### Can I use custom resolution states in conditional logic?

Yes, there is a system parameter called  `lastResolution` which enables you to separate based on the values: `Undefined` , `Informed` , `Resolved` , `Not Resolved` , `Escalated To Agent` , `Escalated via Email`
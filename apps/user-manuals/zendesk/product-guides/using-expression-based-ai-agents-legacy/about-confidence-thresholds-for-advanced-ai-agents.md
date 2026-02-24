# About confidence thresholds for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749625498-About-confidence-thresholds-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

This article applies only to [expression](https://support.zendesk.com/hc/en-us/articles/8357751704474)-based AI agents.

The confidence determines how certain the AI agent is that the expression received matches to an Intent.

You can see this in your [Conversation Logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) when you click on any message as to what it was recognized as and the percentage of confidence it had that it was that Intent.

| | |
| --- | --- |
| Screenshot_2022-10-05_at_08.45.06.png | Screenshot_2022-10-05_at_08.46.19.png |

You have the possibility to choose what you would like the confidence threshold to be - how sure does the AI agent need to be in order to send an Intent reply?

We set the confidence threshold for the AI agent to 60, and we find that most of our users have the threshold set somewhere between 50% and 70% as the sweet spot that provides the most value when training the AI agent. But you might be asking yourself... How do you know what is the best confidence threshold for you? 
In order to decide this, you need to know what happens when you lower or higher the threshold. What happens when the AI agent receives an expression on either side of the threshold?

In this article we will cover:

- [Setting the Confidence Threshold](#h_01GPB6Z8X2YA09Z6TBM0MY06BR)
- [Confidence Scenarios](#h_01GEHM5W1YPM4FKJTS538AKRAW)
- [Considerations](#h_01GEHM7S14479T8DQ3EZN50AWB)

## Setting the Confidence Threshold

### In the Beginning

One approach we can recommend is that at the beginning, start with a higher confidence threshold, once you feel confident in your Intent Replies, you have added more expressions and training to your AI agent, and have factored in the feedback from your users, you can experiment by lowering it and see if it impacts other metrics. 

### Setting the Confidence Threshold

The confidence threshold of your AI agent can be found in Settings > General > **Confidence Threshold**

**Note -**based on the confidence of an [expression](https://support.zendesk.com/hc/en-us/articles/8357751704474), you can send different replies using [conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234) with the confidence\_score parameter.

## Confidence Scenarios

When a message comes in the AI kicks into gear and will compare the content of the message against all of the Intents you have created and its understanding of them, to see whether it can find a match. Based on this analysis it will do some quick maths to determine what level of confidence it feels it belongs to one of those Intents, as to how closely it matches this representation the AI has built. Thresholds are from 0-100 and if you have the confidence threshold at the default of 60, everything at 60 and above will trigger the Intent it was matched to along with it's subsequent actions and replies.

- If it is above the threshold, that Intent is triggered which could be correct or incorrect - the lower you make the threshold, there is a higher likelihood that a wrong intent is triggered.
- If it is below the threshold a Default Reply will be sent.
- For ticket automation, if it's below the threshold - no reply is sent unless you have configured it otherwise. 
 For chat automation it could be that then the customer is escalated, depending on how you have designed your default reply.

The higher the confidence threshold, the more accurate the AI agent would be, but then more default replies would be sent. Therefore you need to consider 5 things:

- The benefits you are looking to achieve with the AI agent?
- What does the AI agent being wrong cost you as a business and your customers?
- What does the AI agent sending the Default Reply cost you as a business and your customers?
- What does doing nothing or escalating cost you as a business and your customers?
- [The Conversation Design](https://support.zendesk.com/hc/en-us/articles/8357758797338) on your Default Reply

## Considerations

To determine the confidence threshold, you can run a full analysis, however, if you are looking for how to you can do this in a simple way we can ask you an either-or question.

| | |
| --- | --- |
| In 100 messages, which is better? | |
| 50 potentially incorrect answers + 50 correct answers | 100 Default Replies / No action taken |
| 40 potentially incorrect answers + 60 correct answers | 100 Default Replies / No action taken |
| 30 potentially incorrect answers + 70 correct answers | 100 Default Replies / No action taken |
| 20 potentially incorrect answers + 80 correct answers | 100 Default Replies / No action taken |

Now, the answer will depend on how you have built your Intent Replies.

### Are the conversations designed flexibly?

Do they have the option, especially on similar intents such as Return Process vs Refund Inquiry? They share a lot of common words around returns, so the likelihood for confusion is higher, but if on the first message you can get them back on track the wrong intent being triggered has a lower negative impact.

### How good is the training?

Do you have a lot of confusion between Intents? By analyzing the [Confusion Matrix](https://support.zendesk.com/hc/en-us/articles/8357756496922) you can try to reduce confusion which will impact the confidence positively.
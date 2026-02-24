# Using Message Training for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749400602-Using-Message-Training-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Message Training is a revamped version of the previous Training page. Not only does it include all the features from before, but also more sophisticated filters. In addition, we've taken the search feature to the next level. When searching for keywords, it searches for typos as well as other forms of the word. For example, if you type "cancel", you will see messages that contain "cancelling", "canceling" "cancelled", and "canceled".

This article covers:

- [When to use it?](#h_01FB9826X8NBAD81BV98DPQ7C8)
- [How to use it?](#h_01FB982CKR292DBVHZ66MTD2Z0)
- [Search features](#h_01FB982HSHBQ289N6PW70YCR0R)
- [Advanced Filters](#h_01FB982NAC85SWFB5ZGAFQ7P05)

## When to use it?

As Message Training gives you a quick and easy overview of all the messages without scrolling through Conversation Logs, it's perfect for any time you want to perform a targeted keyword search, such as:

- When you notice that there are topics that your customers ask about but don't see them in the impact report
- When you want to cover different synonyms
- When you discover topics during [content coverage analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322)

For example, if you want to add expressions to the intent “Password reset”, you would start with [Intent Training](https://support.zendesk.com/hc/en-us/articles/8357756486042). After that, you can cover the blind spots by searching for "sign in" and "log in" in Message Training to find messages that are not as obvious to the AI model and therefore not seen in Intent Training.

## How to use it?

1. Select the timeframe in the top right corner to make sure you get the most recent user messages
2. Search for the keyword(s) you have in mind
3. Select the messages that can be trained to the appropriate intents
   - Use Advanced Filters to screen out noise.

## Search operators

You can use the operators below to enhance your search results:

|  |  |  |  |
| --- | --- | --- | --- |
| Operators | Description | Examples | Results |
| \* | Match any word | `*ould` | Any message that contains "should", "would", or "could" |
| OR | X OR Y | `package OR parcel` | Any message that contains "package" or "parcel" |
| AND | X AND Y | `tracking AND email` | Any message that contains "tracking" and  "email" |
| NOT | Exclude X | `* NOT address` | Any message that does NOT contain "address" |

## Advanced Filters

Advanced Filters:

- **Count of Characters** - Limits the message you see based on length. Space counts as one character
- **Confidence Threshold** - This shows how confident the AI model is about its intent prediction
- **Message Quality** - Calculated by the AI model. The higher the quality, the more similar a message is to the trained expressions, semantically speaking
- **Similar to Intent** - By selecting this you will see the messages that match the intent the AI model has the most confidence with
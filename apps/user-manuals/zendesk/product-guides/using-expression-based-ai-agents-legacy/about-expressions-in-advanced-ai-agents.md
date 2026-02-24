# About expressions in advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357751704474-About-expressions-in-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

![Expressions.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Expressions_fWx5E.png)

An expression is a customer message that has been trained to a specific intent. By assigning a message to an intent through training, the message becomes an expression under that intent.

A good expression is a message that represents the [intent topic(s)](https://support.zendesk.com/hc/en-us/articles/8357751694362#h_01FE36FTHBD0E17E66EZGVR8K3) well. Expressions can be short and concise, long and detailed or anything in between. An intent should be trained with a mixture of expressions that reflect the data and customer behavior. 

The same expression or similar expressions should never be trained to different intents. This will cause considerable confusion for [the AI model](https://support.zendesk.com/hc/en-us/articles/8357749611802), and for an intent to be incorrectly triggered and trigger other intents incorrectly.

## How many should you have?

For the initial launch, 50 expressions per intent is a good baseline. However, it’s essential that the number of expressions reflect the frequency of the intent. This is because the more expressions an intent has, the more weight it will have in the AI model.

More complex intents like those that include subtopics or multi-topics will require more expressions.

For example: “Update Account” may require expressions to cover a range of topics like update email, password, address, username etc. Some examples of expressions needed to support an intent like “Update Account”:

- *Hey I want to update my email*
- *Need to change my address*
- *Can I change my username*
- *Hello, I want to change my phone number*
- *my last name is wrong*

## Recommended expression count weighting of meaningful intents at launch:

- Most frequent: 150 expressions
- Mid-frequent: 100 expressions
- Least frequent: 50 expressions

If you do not have data on the frequency of customer queries, performing [Content Coverage Analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322-Content-Coverage-Analysis-explained) will help you identify the most frequent intents.

The number of expressions trained to structural intents may vary more as their function is specific.

**For an advanced AI model,** the impact and benefits of adding expressions diminishes as the expression count increases. Increasing an expression count from 100 to 200 will add some additional benefits, but will not be as impactful as strengthening from 50 to 100. Anything above 200 will have minimal impact.
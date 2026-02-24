# About intent training for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756486042-About-intent-training-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Note: This article describes how intents are used in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/8725042447002) only. For information about how intents are used in the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), see [Automatically detecting customer intent, sentiment, and language](https://support.zendesk.com/hc/en-us/articles/4550640560538).

## Why use Intent Training?

A good intent structure entails a good AI model that understands the most frequent intents and ensures your AI agent takes the automation potential to the fullest. But what is a good intent structure? A good intent structure should reflect the reality of your support query frequency. Meaning the most frequent intents should have the most expressions.

## When to use it?

Before launching the AI agent, aim for 50 expressions per intent as the baseline and 150-200 for the most frequent ones.

In addition, before or after launching the AI agent, if you notice that your most frequent intents have fewer expressions than the other less frequent ones.

## Training Expressions to an Intent

To train the intents that need to be strengthened:

1. Navigate to **Training** Center and click**Intent Training**
2. Select the intent you want to add more expressions to
   - Use the search bar if you've got a long list of intents
3. You'll see two tabs on the right:
   - [Current Expressions](#h_01GEHKWNQ4YGT9BRE86NVG60ZG) - Shows you the expressions that have been trained to the intent to give you an idea of what to look for
   - [AI Suggested Messages](#h_01GEHKWXFXMBY0838GGAVDTRPJ)- Shows the expressions suggested by AI that could be added to the intent
4. Take a brief look at **Current Expressions** to get an idea of what expressions you should be looking for in AI Suggested Messages. Then, go to **AI Suggested Messages.**
5. In AI Suggested Messages, select the messages that should be trained to the intent, and click **Train**.

### Current Expressions

This view shows the expressions suggested by the AI model that could be added to the intent. All these actions can be done in bulk or one by one.

### Add Expressions

To add expressions, simply type the expressions you'd like to add in the bar on top then hit enter or click **Add Expression.**

### Move expressions to another intent

If you spot any expression that should be trained to another intent, you can do so by clicking the forwarding arrow of an expression, or selecting multiple ones and clicking the forwarding arrow on top.

### Untrain Expressions

If you spot any expression that shouldn't have been trained to this intent, you can untrain it by clicking the X icon of an expression, or selecting multiple ones and clicking the x at the top.

The untrained expressions will be returned to where they are from originally - meaning if it was trained from another intent, it will go back to that intent. If it was untrained previously, it will remain as an untrained expression.

### AI Suggested Messages

This view shows the expressions suggested by the AI model that could be added to the intent. The untrained expressions you see here can be adjusted using the [Confidence Range](https://support.ultimate.ai/hc/en-us/articles/4403736597650-AI-Suggested-Messages#h_01FAJCDSWCKQTPDBDJJNMR62TT) slider.

This article covers:

- [Confidence Range](https://support.ultimate.ai/hc/en-us/articles/4403736597650-AI-Suggested-Messages#h_01FAJCDSWCKQTPDBDJJNMR62TT)
- [Train to another intent](https://support.ultimate.ai/hc/en-us/articles/4403736597650-AI-Suggested-Messages#h_01FAZ5E6W14VJ40DDJBJZ79EM2)
- [Train to a new intent](https://support.ultimate.ai/hc/en-us/articles/4403736597650-AI-Suggested-Messages#h_01FAZ5EBNK6WEFBX18NXHR01ND)

### Confidence Range

The default is set to between 50% and 70% as this is usually the sweet spot that provides the most value when training the AI agent. We suggest setting the maximum to right below the confidence threshold of your AI agent to get the best performance. The confidence threshold of your AI agent can be found in Settings > General > **Confidence Threshold for default messages**.

### Train to another Intent

If you spot any expressions that should go to another intent in this view, you can also train them to the suitable intent by clicking the triangle next to Train and then selecting **Train to another intent**.

### Train to a new Intent

If you can't find a suitable Intent for an untrained expression, you can create a new Intent and train the expression there simultaneously. To do so, click the triangle next to Train then select **Train to a new intent**.
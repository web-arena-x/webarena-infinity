# About AI models for expression-based AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749601050-About-AI-models-for-expression-based-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

An AI (artificial intelligence) model is a program that has been trained on a set of data to recognize certain types of patterns.

We develop [our own AI model architecture in-house](https://support.zendesk.com/hc/en-us/articles/8357749611802). Instead of relying on third-party APIs, our AI researchers use the latest advancements to train and optimize industry-leading models specifically for enterprise customer support. 

We’ve built a language-agnostic AI model, allowing you to quickly scale your support in any language.

We use Natural Language Processing (NLP) technology that can “learn” with ample examples and adapt to different sentence structures and spellings, such as synonyms and typos. This is particularly important in customer service as people pay less attention to correct capitalization and punctuation than in other forms of text.

## How does it learn?

The AI model learns through training. Training is when you assign a customer message, or expression, to a specific customer query, or intent.

Through training, the AI model learns patterns in the data so that it can distinguish individual intents from one another. As you train, the AI model learns and makes adjustments, so that its predictions are more accurate.

In the Dashboard, under [AI > Models](https://support.zendesk.com/hc/en-us/articles/8357749611802), you will see that the AI automatically makes adjustments every evening and creates a new model, if any changes have been made to the training data that day. If you have added new intents or have trained an intent with new expressions and you need the AI model to learn immediately, select “Train Model”.

An evaluation model is also automatically created once a week, whether training has taken place or not. This will generate an updated Confusion Matrix available under Training Center > [Confusion Matrix](https://support.zendesk.com/hc/en-us/articles/8357756496922).

## What makes a good AI model?

A good AI model is one that recognizes 80%+ of user messages and predicts them to the correct Intent. This is best achieved by a sensible Intent structure, where intents are well-defined and do not overlap, and the number of expressions is representative of the frequency of intents. 

When building a model, remember to: 

- **Trust the data**The Intent structure must consider the AI model and your customer's behavior, not what makes sense from a reply or process perspective.
- **Prioritize the most frequent Intents**The aim is to cover the most frequent queries and ensure the AI agent handles these. [It is ineffective to build an AI model that recognizes all customer queries](https://support.zendesk.com/hc/en-us/articles/8357751694362), as certain more complex queries will be better handled by your agents.
- **Focus on training**Build a solid foundation by [weighting your intents](https://support.zendesk.com/hc/en-us/articles/8357751694362) using customers’ real data. Strengthen further after launch with regular training as you learn how customers interact with the AI agent. Note, it is better for the model to not train than to train poorly.

The [Automation Report](https://support.zendesk.com/hc/en-us/articles/8357749403418) and Training Center guide you to build the best model based on your customer's unique behavior.
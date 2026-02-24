# About intents in advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357751694362-About-intents-in-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Note: This article describes how intents are used in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/8725042447002) only. For information about how intents are used in the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), see [Automatically detecting customer intent, sentiment, and language](https://support.zendesk.com/hc/en-us/articles/4550640560538).

![intent.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_intent_eqQkK.png)

This article covers all that you need to know to get started with Intents. The following topics are covered:

- [What is an Intent?](#h_01FE35CVBYHJJ54AAF18KZD1F1)
- [Types of Intents](#h_01FE35JES8DXM2NS3B3QRC4SYC)
- [Intent topics](#h_01FE36FTHBD0E17E66EZGVR8K3)  
  - [Examples of single- and multi-topic intents](#h_01FE34TECWP82PC6C65ZZAXX0Q)
- [Intent Training Best Practices](#h_01GDX97H4RR4Y4P39NAG1DEBVC)
  - [How do you build Intents?](#h_01GDX97QEE5ECA7XVASMGV5XHZ)
  - [How many Intents should you have?](#h_01GDXA3KF37C0DRRBE5921R2QN)
  - [Should you add Intents for every situation?](#h_01GDXA4AATS2M3HP1PGH1XJM0Y)
  - [When to merge or delete an Intent](#h_01GDXA4KM7JKT9J2N25MZSK19D)

## What is an Intent?

An intent is a grouping of semantically-similar messages, or [expressions](https://support.zendesk.com/hc/en-us/articles/8357751704474), to be precise, that represent a customer query. 

When it comes to building your Intents, we will ask you to think about the Intent structure.   
An intent structure refers to the complete list of all the meaningful and structural intents in your AI agent (we will cover what these are in just a minute), and the "weight" of each intent, namely the number of expressions each intent has. 

A good intent structure is the foundation of a strong AI model. And a good intent structure reflects reality. This means intents are based on real customer data, are clearly defined, and the expressions trained to them do not overlap with one another. 

## Types of Intents

Well-functioning AI agents have two types of intents: Meaningful intents and structural intents.

**Meaningful intents** represent the most frequent customer queries identified in your data using the [Impact Report](https://support.zendesk.com/hc/en-us/articles/8357749403418-Impact-Report-explained) or through [Content Coverage Analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322-Content-Coverage-Analysis-explained) if no historical data is available.

**Structural intents** are intents that support the conversation flow and are not AI agent or industry-specific. Below you will find some of the most common structural intents, however, it is important to verify from conversations with the AI agent which structural intents are the most important, as these can vary depending on language, culture or user behavior. 

|  |  |  |  |
| --- | --- | --- | --- |
| Greeting | How are you? | Appreciation | Goodbye |
| Affirmative | Negative | I want to speak to a human | I have a problem/I need help |
| I haven’t heard back from you | Chat got cut off | That’s not what I asked | That didn’t work |
| Negative feedback | It’s already been x days | Positive Feedback | I don't know |

#### For English, Finnish, and German these are available pre-trained with expressions in the Content Marketplace.

## Intent Topics

Whether it's a meaningful intent or structural intent, an intent typically covers a single topic (see [single-topic example](#h_01FE34TECWP82PC6C65ZZAXX0Q) below). However, if less data is available for training, an intent may include semantically-similar messages that cover more than one topic or an intent may be broader and include several subtopics (see [multi-topic examples](#h_01FE34VE9P65XBCRF4FRXV3RX4) below).

When creating an intent, the intent name should identify the customer query or queries. Intent description can be used to define in more detail what query or queries the intent covers. The intent category is used to group intents together by a broader subject.

Here are some examples:

### Single-topic Examples

- Intent name: Order status
- Category: Order
- Description: Customer inquiries about order status, tracking of order, says they have not received an order
- Intent name: Account verification
- Category: Account
- Description: The customer asks how to verify their account, what documents are needed to verify, and info on verifying process

### Multi-topic Examples

- Intent name: Order cancellation
- Category: Order
- Description: Customer asks to cancel their order, why was their order canceled
- Intent name: Account query
- Category: Account
- Description: Customer has a query related to creating/deleting their account, account log-in & password, payments attached to an account, account tiers etc.

## Intent Training FAQ's

### How do you build Intents?

The best way to build Intents during onboarding is with the [content coverage analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322) process. This way you are using real customer conversations to add expressions and determine which topics arise most frequently, and thus have the greatest automation potential.

### How many Intents should you have?

For an **initial AI model**, an AI agent typically launches with between 30 and 40 intents, including [structural intents](https://support.zendesk.com/hc/en-us/articles/8357751694362). 

**An advanced model** will have between 60 and 80 intents. In the weeks and months post-launch, you will identify new intents as your customers interact with the solution, increasing the count gradually from 30 to 40 to 60 to 80. However, the optimal number will depend on the breadth and complexity of your customer support operation. An AI agent with an intent count below 30 or over 100 would be very rare.

Technically, there is no limit to the number of intents you can have.

### Should you add Intents for every situation?

From the AI model's perspective, it is not wise or possible to have the AI model recognize all of the customers queries - this is because anytime a message comes in it will hold it against all your intents and see which it has the best fit for. The more specific of an intent you have, the fewer expressions you will have for it, and the harder and more confused the AI will be. The benefit of adding new intents decreases rapidly after the top intents have been accounted for. The aim, instead, is to cover the most frequent requests. 

[Content Coverage Analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322) is used to identify frequent queries that are not yet covered by an intent. As a general guide, a query is frequent if it makes up anything from 2% or above of the content using CCA.

One thing to consider when making Intents is does this message have the exact same flow as something else. You should bear in mind that a customer’s query may be better answered by adding a new branch to an existing reply or by creating a reply variation/conditional flow to an existing intent.

Allow us to illustrate this with an example.

Should you create a unique Intent for the following scenarios

- Change Last Name
- Change Gender
- Change Email
- Change Address
- Change Payment Method
- Change Marketing Preferences

We would suggest no. These may all be handled differently, but having a catch-all Intent around changing account information is more likely to produce a robust Intent with many expressions, whereas one of those topics alone will be harder. This doesn't mean that when it comes to formulating your replies that you can't personalize them and have specific flows based on each criterion - you will have the option to design the conversation experience based on the Intents and Expressions you add - which is why Intent descriptions are very helpful to share what exactly the Intent includes or doesn't.

### When to merge or delete an Intent

In the beginning, you can have a lot of Intents if you think you can find more expressions, however, when it comes to building the dialogues, you should prioritize and activate the replies for those that have the most expressions.

You can then assess whether you can merge them with a similar intent and then handle different use cases from a conversational design perspective. You can use the confusion matrix to identify if maybe there are overlapping Intents that can be merged.

You should consider deleting an Intent when intent health is low or messages are incorrectly triggering an Intent, then the overall Intent performance should be investigated.

### What is Intent Health?

Intent Health is the average confidence of messages being recognized to the intent and how well the expressions reflect how the customer communicates with the AI agent.

If intent health is low, it may mean:

- There are not enough expressions trained to an intent for a customer query to be recognized reliably to an intent.
- The intent is rarely triggered. This can happen if there is an intent linked to a service or product that is no longer offered, or an intent that was added without sufficient data to justify its addition.

### What is Intent Overlap?

Intent overlap is when two or more intents contain similar expressions. This will cause the AI to confuse the intents with each other.

More details on how to identify and fix intent overlap in [How to keep the AI agent smart using the Confusion Matrix](https://support.zendesk.com/hc/en-us/articles/8357758882330).
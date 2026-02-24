# About conversation design for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357758797338-About-conversation-design-for-advanced-AI-agents

---

Structuring your replies is one of the most important tasks that you can undertake and it requires thinking about conversation design best practices.

Be sure to review the [best practices](https://support.ultimate.ai/hc/en-us/articles/4402041984146) based on working with all of our customers.

This article contains the following sections:

- [Communication Theory](#h_01GE46Y5QHECTKPHDGH1W57Q51)
- [Structuring Replies](#h_01GE474HNEA2P9EZ4E75PE07S0)

## Communication theory

### Human<->Human Communication

Humans are not always great at impactful communication. Most of us talk, then wait for the next moment in which we can speak rather than giving listening 100% of our attention. Life has so many distractions and we want to take the path of least resistance. We may also think what we say is perfectly clear as we have 100% of the picture from our side, but the words that are said encode perhaps 50-60% of this.

There as some unspoken rules when it comes to communicating between humans that a large majority of people *just*know.

For example, based on who you speak to you may tailor your communication to suit them. The way I might explain a concept such as digital security protocols to a child vs a developer vs my grandma is something I know I must do as they have very different understandings of the world, technology, and consequences. This provides clarity to the situation for the recipient.

For the most part, we as humans are also able to read nuances in tone, structure, and inferences.

Where is the emphasis, is there an inflection, is it sincere, based on the situation did the colleague actually just crash and burn? All of these things and more can turn "Great job!" from a compliment into a sarcastic or snide remark very quickly and humans typically know the difference.

There is, of course, a barrier when we look at different forms of communication from voice, text, and actions, however, typically if you look hard enough as a provider or receiver of information you will find a way to decide these factors - rightly or wrongly as the case may be.

This is why it is important to communicate with the right energy, to convey the way to infer through your message.

Finally, as humans, we understand that people have lives, hopes, and fears as well as a myriad of other things. With humans, it can be that the actual content of the message doesn't matter that much, as the interpretation the recipient has is all they will focus on and can have a drastic impact on how they navigate the conversation going forward. Therefore, we should try to communicate with empathy - and maybe not be lazy with our communication.

### Human<->AI agent Communication

Now that we know how humans communicate and the complexities it unearths, let's add in an additional factor - an AI agent.

An AI agent is able to handle multiple conversations at the same time, on the same or different topics simultaneously, which humans would really struggle to do past a certain number so AI agents can significantly reduce the repetitive load for humans - which is amazing.

You will never speak to an AI agent that woke up on the wrong side of the bed, had a partner that just dumped them, or has the flu - so you will receive a consistent experience no matter who you are or how many questions you ask.

However, unlike humans, AI agents have some differences.

They don't have a body and therefore physical language is out of the question for communication. The reason why people have typically an aversion to talking to AI agents, is they reply to the message received and don't have the human ability to read sub-text or infer sentiment as humans can. But the biggest consideration is that AI agents work in a very structured way and the communication is turn-based, and it is expecting a certain output in return.

I speak -> You give me an answer I am expecting

An example: If I ask you how many pets you have and you say "a cat, a dog, and a fish" a human understands this as 3 pets. An AI agent, however, will likely be expecting a number as a result, so either you get into a conversation loop or you ask it another way to provide clarity on the expected answer structure. This will is something to consider later when we get into building your replies - ways of understanding responses.

So how do we fight the preconceptions and structure a reply that is impactful?

## Structuring replies

### Conversation funnel

As an overall flow, you want to work on a funnel approach: Start broad and get more granular based  
on the information a customer provides. For example:

1. Confirm that the AI agent understood the intent correctly / does the customer need to rephrase
2. Define all possible scenarios and include an escape route / false positive catch
3. Share general information, FAQs, and self-guided instructions based on each scenario
4. Validate whether this helped by doing a resolution check / providing a call to action where  
   applicable
5. Perform a resolution check:
   - If it helped - ask whether they have further requests
   - If it didn't help offer further assistance if available or escalate to a human  
     agent.

Here's an example of updating account details.

[View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conversation_funnel.png) ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conversation_funnel.png)

With the conversation funnel, decide based on your processes if this is something the AI agent can fully automate for you or if it is something you need to escalate to a human agent. But before you do, is there anything the AI agent can do for you to speed up their investigation or do you have an authentication flow that they should conduct? This can help reduce their workload and speed up average handling time.

### Conversation chunking

Conversation chunking is a pretty advanced method of conversation design but can make a massive impact on the experience of the user.

This is something we do as humans, based on experience and knowledge we adjust what we say so it makes sense to the person who is listening. An example - when someone asks where you come from, you might ask them how familiar they are with your country, and based on their understanding you will adjust your response. If I am from a small village in a country I might start with how far from the capital it is, then go in the cardinal direction of the country, maybe the state/county name or what the area is famous for. However, if someone is very familiar I would instead go likely to the closest large city then down to the town name.

You may have some customers who have been with you a long time, usually handle everything they need, and don't need to contact support. If they end up in a situation that is outside the norm, they likely don't want to be taken down the same path as newer or less brand-savvy users. This is when you can ask them questions to fast-track them to either more specific answers or get them to an agent faster.

You can do this based on customer information, such as loyalty/VIP status, or by building it into the conversation flow.

For example, returning a product is a fairly common use case for a lot of industries. If someone has ordered with you a lot, they likely know where to get a return label - let's say in this case it is *always* in the box, where to go to return it, and how long it takes. If someone has returned with you before, but they have a new order where the return label isn't included they may say something like this: "I need a return label". Depending on how you built your flow you might say, "You can find your return label within the box, affix it to the top and remove all other labels, then you can find drop-off locations here, or schedule a pick-up here. Once it has been collected it can take up to 14 days for the return and refund to be processed". This doesn't help the customer, and they might then get frustrated. You could start with a question like, "have you returned with us before?" or check whether they are a first-time purchaser with API integration to personalize the response accordingly. Then the text can be adjusted to meet their experience level. You could also check based on the URL of the chat, which is on the FAQ page. They have likely read those guidances and now need specific help.

We hope you enjoyed this introduction to Chat Conversational Design. Check out the exercise to start working with your team to start forming your replies, which you can get from your CSM.
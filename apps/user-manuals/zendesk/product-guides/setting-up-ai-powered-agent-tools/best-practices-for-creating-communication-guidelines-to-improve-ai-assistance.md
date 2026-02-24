# Best practices for creating communication guidelines to improve AI assistance

Source: https://support.zendesk.com/hc/en-us/articles/9182110974746-Best-practices-for-creating-communication-guidelines-to-improve-AI-assistance

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Communication guidelines allow [auto assist](../providing-ai-assistance-with-auto-assist/turning-on-and-configuring-auto-assist.md) and the [rewrite in your tone tool](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_fn1_bkp_22c) to adapt suggestions and responses based on the tone, topic, urgency, language, writing style, and context of an ongoing ticket conversation.

To further refine the suggestions and responses that Copilot AI tools make to agents, you can create your own communication guidelines that are specific to your business.
Creating your own guidelines helps cover a wider range of writing rules, such as general communication principles, formatting, length, formality, structure, greetings, closings, wording, and more.

This article contains best practices that help you write more effective communication guidelines.

This article contains the following topics:

- [Best practices for defining communication guidelines](#topic_ks3_vp3_zfc)
- [Communications guideline example](#topic_irb_yq3_zfc)

Related articles:

- [Using communication guidelines to improve AI assistance for agent comments](https://support.zendesk.com/hc/en-us/articles/8761641980698)

## Best practices for defining communication guidelines

When [creating new communication guidelines](#topic_arb_r43_zfc), keep the following in mind:

- Your guidelines should be kept separate from procedures. Guidelines define how to say something, while procedures define what to do.
- Guidelines are treated as signals rather than strict rules. This means that instructions you include in your guidelines might not be followed perfectly, especially in complex or emotional conversations. Customer empathy is always prioritized. For example, if you include a “happy tone” guideline, the system might not follow this instruction if the user is upset.
- A guideline can be associated with multiple brands, but a brand can be associated with one guideline only.
- Communication guidelines apply only when the entire message text is selected for rewriting, not just a part of it.
- There is a 10,000 character limit. This generally corresponds to four to five pages of text in a standard document using 12 point font with single spacing.

Adhering to the following best practices helps you write more effective communication guideline:

- [Use clear, specific language](#topic_k5q_dq3_zfc)
- [Focus on the tone and writing style](#topic_dkn_hq3_zfc)
- [Add examples and short explanations](#topic_g5t_pfq_zfc)
- [Group related rules](#topic_avz_2gq_zfc)
- [Avoid vague conditional instructions](#topic_ufr_sgq_zfc)
- [Avoid ambiguous or conflicting rules](#topic_f14_chq_zfc)
- [Consider how agent signatures are added](#topic_j24_hhq_zfc)
- [Clearly define channel names](#topic_pbv_lhq_zfc)
- [Test, iterate, and update regularly](#topic_wlz_ngx_zfc)
- [Try new versions](#topic_fnk_xhx_zfc)

### Use clear, specific language

Write each rule using simple, direct words. Avoid vague terms, jargon, and complex sentences to ensure the AI interprets your rules correctly. When creating guidelines, write as if you’re talking to an agent.

- **Good**: Always greet the customer with: 'Hello!' or 'Hi'. At the end of each message, apply ‘Kind Regards’.
- **Bad**: Greetings: Use 'Hello!' or 'Hi [Name],' Signature: 'Kind regards etc.

### Focus on the tone and writing style

Your guidelines should focus on how the response is written rather than what to do. Guidelines aren’t for defining which steps the AI should take.

[Procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738) define what to do, while guidelines define how to say it. You can review your procedures and move tone or writing-related instructions into communication guidelines.

- **Good**: Be apologetic and professional when discussing refunds.
- **Bad**: Always escalate refund requests

### Add examples and short explanations

It’s helpful to add examples and short explanations to your rules so that the AI understands what you have in mind.

- **Good**:

 Empathy and Personalization: If the customer seems confused, respond kindly and supportively. Personalize your message and reassure them you’re here to help.

 Example: I understand this can be confusing and I’m here to help.
- **Bad**: Empathy & directness

### Group related rules

Your guidelines should group your related rules together logically to help prevent confusion.

- **Good**:

 Greetings and Closures:

 -Always greet the customer with: “Hello!”.

 - At the end of each message, apply “Kind
 Regards”.

 Formatting:

 - Every time a reference to an order
 ID is mentioned, include a # symbol before the ID.

 - For
 currencies, always include information about the smallest currency unit (e.g., cents)
- **Bad**: Always greet the customer with: “Hello!”. Every time a reference to an order ID is mentioned, make sure to include a # symbol before the ID.
 At the end of each message apply “Kind Regards”. For currencies, always include information about the smallest currency unit (e.g., cents).

### Avoid vague conditional instructions

Avoid specifying rules for the "first message" versus "subsequent messages," especially when distinguishing between the agent’s first reply and later replies when other messages (such as customer messages) appear.

It’s also important to use names consistently so that situations are clearly defined.

- **Good**:

 For the first agent's reply: Greet the customer and offer help.

 For later replies: Skip the greeting and get straight to the point.

 Note: In this example, using the word reply in both cases makes it clear that the condition refers specifically to the agent’s messages.
- **Bad**:

 Initial contact: Greet the customer and offer help.

 Subsequent messages: Skip the greeting and get straight to the point.

 Initial contact: Greet the customer and offer help.

 If not the first message: Skip the greeting and get straight to the point.

 For the first agent's reply: Greet the customer and offer help. When replying to an ongoing conversation:
 Skip the greeting and get straight to the point.

 Note: In this example, the AI may confuse subsequent messages and incorrectly apply the second rule to the agent’s first reply if the customer message is treated as the first message.

### Avoid ambiguous or conflicting rules

Avoid rules that the AI might interpret as ambiguous. For example, if you use “always”, don’t introduce an exception afterwards. Your rules should also not contradict each other.

- **Good**: Confirm that you understand the customer's concerns without repeating excessive details. Briefly paraphrase the key points to demonstrate attentiveness.
- **Bad**: Always confirm customer concerns are understood, but avoid repeating information already provided.

### Consider how agent signatures are added

If personal agent signatures are automatically added by the system, your guidelines should instruct the AI not to add any additional signatures in rewritten messages. Since agent signatures are appended after the message is rewritten, preventing the AI from adding signatures during rewriting avoids duplicates.

Without this instruction, the AI may copy an existing signature from the ticket conversation context, causing duplicate signatures in the final message.

For example:

Do not sign messages.

Exclude signatures from rewritten messages.

Do not add the agent's signature in the rewritten message.

### Clearly define channel names

When writing channel-specific guideline rules, use the exact channel names as they appear in the "Ticket created by" field. See the [Zendesk developer documentation](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/) for a full list of the channel names that appear in this field.

Note: Currently, the only supported field is Ticket created by.

- **Good**:

 If message is from chat, whatsapp, facebook, sms channels:

 - Use emojis.

 - Write with casual
 language.

 - Keep messages short, easy, and personable.

 If message is from mail, web forms, side conversation channels:

 - Use
 a highly formal and polite tone.

 - Do not use emojis in any
 communication
- **Bad**: Messaging channel: Use a lot of emojis. Write with casual language. Keep messages short, easy, and personable. Non-messaging channel:
 Use a highly formal and polite tone. Do not use emojis in any communication.

### Test, iterate, and update regularly

Continuously test your guidelines with real interactions to evaluate their effectiveness. Revise the rules as based on what works best over time.

- **Good**: Review communication guidelines monthly and adjust rules as needed.
- **Bad**: Write once and never revise.

### Try new versions

You can experiment with different approaches and explore the communication guidelines feature to find what works best for your brand and use case. An LLM can also offer suggestions to improve your prompt. For example:

"This is a prompt for communication guidelines in a customer service tool. Please suggest improvements based on these guidelines (link).”

Using an LLM alongside hands-on experimentation can help accelerate your optimization process. However, your own testing and adjustments are essential for success.

## Communication guideline example

The following example is what a clear and effective communication guideline might look like. This example is effective because it’s direct, specific, and structured by category, which makes it ideal for helping the AI consistently adapt to your company’s writing style and tone.

**Example of an effective communication guideline**

### Greeting and closures

- Do not add signatures to the rewritten message.
- For the first agent’s reply:

 Always begin by greeting the customer by name and include a brief summary of their issue to show empathy and engagement.

 Example:

 “Hello Emily! I understand you are experiencing issues with your payment. I am here to assist you.”
- For later agent’s replies:Start with a polite thank you and move directly to addressing the customer’s ongoing concern.

 Example:

 “Thank you for getting back to us. I’m working on your payment concern.”

### Tone and style

- Use an active voice at all times.
- Address the customer directly using “you” and “your.”
- For negative feedback:
 - Slightly negative sentiment: acknowledge the concern and offer help.
 - Strongly negative sentiment: express explicit empathy
 - Always add an introductory sentence confirming understanding of the issue.
- When conveying multiple points or ideas, use bullets or line breaks for clarity.

### Restrictions and words to avoid

- Do not use "unfortunately"; always use "currently" instead.
- Never include:
 - The agent’s last name.
 - Metaphors, idioms, or clichés (e.g., “game-changer”, “navigate”, “in a world where”, “groundbreaking”, etc.).
 - Setup phrases (e.g., “In conclusion”, “To summarize”).

### Channel-specific rules

- For messages coming from messaging channels (chat, whatsapp, facebook message, sms):
 - Use casual, personable language.
 - Include emojis to convey tone and friendliness.
 - Keep messages short, simple, and easy to understand.
 - Always address customers by their first name.
- For messages from non-messaging channels (e.g., email, web forms, ticket portals):
 - Use a highly formal and polite tone.
 - Do not use emojis.
 - Write in full sentences with organized paragraphs.
 - Address customers formally using their full name and proper title where possible.
 - Maintain a respectful, businesslike style

### Formatting and numerical standards

- Every time you reference an order ID, make sure to include the “#” symbol before it.

 Example:

 Instead of “order 123456”, write “#123456”

 “Hello sir,

 For #123456 we can file a discount code that will net you 20% savings!

 Thank you.”
- When specifying large quantities, format numbers according to SI/ISO/Scientific standards with spaces separating thousands.

 Example:

 Instead of “1234567”, write “1 234 567”.

 For currencies, always include cents in your amount.

 Example:

 Instead of “$12”, write “$12.00”.
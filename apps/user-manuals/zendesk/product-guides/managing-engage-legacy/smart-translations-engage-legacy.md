# Smart Translations (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731439401242-Smart-Translations-Engage-Legacy

---

Many businesses have a need to support their customers in a range of languages.

Smart Translations removes the need to have Agents trained in a broad range of languages by automatically detecting whether a customer is speaking in a different language to the Agent, and translating everything for both parties, so that the Agent sees their language of choice, and the customer does too.

### How Does Smart Translations Work

Smart Translations work on all social, chat and email channels. Smart Translations are not available on voice.

- Automatically detects the language sent by the customer (e.g. French)
- Translates the customer’s message into the Agents set language (e.g. English)
- Translates the Agent’s response into French
- The agent can edit any translations before sending
- We double check the translation before the Agent has the option to send it to your Customer
- Both parties see the Contact in their own language
- The agent will be able to see the original and translated messages within an ongoing contact

The Agent's language is set in their Agent Settings. [Click here to see how](https://support.zendesk.com/hc/en-us/articles/9696157744922).

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731439433626)

### Pricing

As with all Smart Tools, Smart Translations will use your LLM, and as such there will be a cost incurred with your chosen AI service provider

Smart Translations will also incur Local Measure unit consumption. Each contact that utilises Smart Translations will have an 2 units associated to it, on top of any other unit consumption related to that Contact.

‍

### Prerequisites

Before settings up Smart Notes in Engage, you will need the following:

1. CloudFormation Stack is on v5.79.3 (20240514) +
2. Access to models within an AI Service (e.g. Amazon Bedrock)
3. The AI Service configured as an Smart Tools integration in Engage

[Click here](https://support.zendesk.com/hc/en-us/articles/9731462361882) for more information on steps 2 & 3 above.

‍

### How to Configure Smart Translations

1. Navigate to **Settings** -> **Workflows**
2. On the required Workflow click the **Edit workflow** button
3. Scroll down to the **Smart Tools** section
4. Select the relevant option to enable Smart Translations

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731450871450)

‍

### How to Use Smart Translations as an Agent

1. When a Contact comes through on a Workflow that has Smart Translations enabled, Smart Translations will automatically run, the Agent does not need to enable Smart Translations
2. As messages are received, the Customer's language will automatically be detected, and messages will be translated
3. When an Agent crafts a message, click the **Translate** button to begin translating the outgoing message
4. Engage will translate the message and then perform a secondary check on the translation
5. If no problems are detected, the Agent can click the **Send translation** button

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731467450394)

Smart Translations - Send Translation

1. If a problem is detected, Engage will prompt the Agent by displaying a **Problems detected** message.
   1. Hover over the message to see the specific problem
   2. Click the **Fix problems** button to perform another translation
2. Click the **Send translation** button to send the message to the Customer

‍

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731463803162)

Smart Translations - Problem Detected

‍

### How to Control the Language Used

There are numerous ways to control the language a contact is bring translated to/from:

1. **Automatic language detection** - this is the default process for selecting the language. Engage will use the messages from the customer and review the language in which they are sent. Agents can re-run the automatic detection at any time by clicking the refresh icon on the translation banner.
2. **Manual Agent override** - If the detected language seems incorrect, Agents have the option to manually select a language. They can do this by clicking on the language displayed in the translation banner and typing in the required language
3. **Manual attribute override** - The language used can be set using a custom contact attribute. As an example, you can set the \_LM\_language attribute in a contact flow, using the locale code of the required language as the value. e.g. `{"_LM_language":"fr-CA"}`

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731450917786)

### Auditing Smart Translations

For auditing purposes, a complete record of both the the original (non-translated) and translated messages are stored in an S3 bucket within your AWS environment. To access these, you can review the contents within your CTRs as well as ChatTranslations S3 bucket within your Connect directory.

‍

### FAQs

Q: Which languages are supported?

A: The languages supported depend on the model used to power Smart Translations. Neither Anthropic nor Open AI publish a list of supported languages for translations, however they are known to be proficient across a wide range of languages. Local Measure has performed testing in dozens of languages with great success. Specifically, Local Measure has tested English (US, AU, CA, GB), Dutch, French, Mandarin, Spanish, Portuguese, German (DE, AT, SU), Italian, Xhosa, Afrikaans and many more languages.

‍

Q: Will an End Customer know that the conversation is being translated?

A: Not by default. Local Measure recommends adding an automated message that is sent to the End Customer if they are on a queue that may use Smart Translations.

‍

Q: How will I be charged for Smart Translations?

A: There are 2 elements; the AI Service you choose to use, and Local Measure unit consumption. Note that unit consumption applies as soon as the language detection step within Smart Translations is performed. This means that 2 units will be added to the relevant contact even if language detection determines that there is no need for translation.

‍

Q: How does Smart Translations detect the End Customer's language?

A: Smart Translations uses the content from the first 5 messages an End Customer sends to determine their language.

‍

Q: Can I see Smart Translations in historical Contacts / Contact Search?

A: Yes, when viewing historical Contacts you will be able to see both the original and translated messages.
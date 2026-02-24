# Generative replies in advanced AI agents FAQs

Source: https://support.zendesk.com/hc/en-us/articles/8357756420506-Generative-replies-in-advanced-AI-agents-FAQs

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8725042447002), *generative replies* refers to the ability of [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194) and [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) to create and send AI-generated answers in response to customer questions.

This article contains the following topics:

- [General FAQs about generative replies](#h_01HBXCQXCAST30G42GSMZ2XAVW)
- [Privacy and security FAQs about generative replies](#h_01K9FP4BCS5A46HT8Z2168AC3C)

Related articles:

- [Importing a knowledge source to power generative replies in advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749301658)
- [Using the generative replies block in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749315098)

## General FAQs about generative replies

### What are generative replies?

Generative replies leverage large language model (LLM) technologies, including those based on a GPT (generative pre-trained transformer) architecture, the technology behind OpenAI’s ChatGPT.

Generative replies learns from the information in your [imported knowledge sources](https://support.zendesk.com/hc/en-us/articles/8357749301658) to provide answers to customer support queries in a human-like, conversational manner. Generative replies require no training at all and, once connected to your help center, can be live and answering customer queries in minutes.

Overall, generative replies aim to enhance customer experiences by providing a responsive and helpful AI agent that can assist customers 24/7 in 100+ languages.

### Which channels can I use generative replies in?

Generative replies can be used on messaging and email channels. See [Using the generative replies block in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749315098).

### Do I need a minimum number of tickets for generative replies?

No, the number of tickets doesn't influence generative replies. Instead, all you need is a comprehensive knowledge source to power generative replies. See [Best practices: Preparing your help center for generative AI](https://support.zendesk.com/hc/en-us/articles/9067636151834).

### What languages do generative replies support?

Generative replies are fully multilingual and can converse in 100+ languages. Likewise, they are capable of reading knowledge sources written in any language.

### How do generative replies work with dialogues?

Generative replies are activated through either the generative replies [system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882) or the generative replies block in the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810).

### Can generative replies use content from multiple knowledge sources?

Yes, generative replies can be connected to multiple knowledge sources. You can also [create search rules](https://support.zendesk.com/hc/en-us/articles/9185497386394) to control which knowledge sources are searched under specific conditions.

### How long does it take to get started with generative replies?

You can [import a knowledge source](https://support.zendesk.com/hc/en-us/articles/8357749301658) and start using generative replies in minutes.

### What do I need to get started with generative replies?

You need a public knowledge source, written in any language, for the AI agent to generate answers from. The more comprehensive your help center, the better.

## Privacy and security FAQs about generative replies

### What activity is happening?

Generative replies functionality processes customer support transcripts in order to automate conversations. These transcripts can contain personally identifiable information (PII) about end users.

### Who is involved?

To provide the LLM functionality that powers generative replies, OpenAI is used as a sub-processor.

### What is shared?

All conversation content, including prompts, is provided to the OpenAI service following our sanitization process to minimize any end-user PII being transferred. This is shared via OpenAI’s API.

### Where is the data sent?

Both the AI agents - Advanced and OpenAI service infrastructure are located in the European Union (EU).

### What safeguards are in place?

In addition to our own technical and organizational measures, there are a number of other safeguards in place in relation to the transfer:

- **No training data.** Data is not used to train other models. The OpenAI service does not use data submitted via the API to train or improve their models.
- **DPA and SCCs.** We have a Data Processing Agreement (DPA) in place with OpenAI related to transfer of PII, as well as the latest EU Standard Contractual Clauses (SCCs).
- **SOC 2 Type 2 compliance.** In addition to our own SOC 2 compliance, OpenAI has a range of leading security standards and controls in place. More information can be found on their [Security & privacy](https://openai.com/security-and-privacy/) pages.
- **Encryption.** Data is stored in Azure Storage, encrypted at rest by Microsoft-managed keys, within the same region as the resource and logically isolated.
- **Sanitization.** Before anything is sent to the OpenAI service, the conversation is run through our sanitization process, described below.

### How does sanitization work?

Our machine learning and artificial intelligence systems do not require PII to be trained or to do the classification. This means PII can be anonymized in the messages without compromising the service we provide to you.

The anonymization methods for messages detect different categories of PII in the messages and replace these values with an anonymous label corresponding to the detected categories using entities.

For example, email addresses in the messages are replaced with <EMAIL> labels, bank account numbers are replaced with <IBAN> labels, and so forth. <EMAIL> and <IBAN> placeholders are examples of our default and pre-defined entities. For a list of commonly used entities, see [RegEx reference for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756811162).

### Is there anything else to be aware of?

In addition to the safeguards above, you can include language in your AI agent's welcome reply to discourage end users from sending any PII during the conversation.

### Where can I find more security information?

Below are some useful links to relevant information:

- [Zendesk Trust Center](https://www.zendesk.com/trust-center/)
- [Zendesk AI Data Use Information](https://support.zendesk.com/hc/en-us/articles/5729714731290)
- [OpenAI’s Security & privacy page](https://openai.com/security-and-privacy/)
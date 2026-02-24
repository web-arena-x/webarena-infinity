# About data processing in AI agents - Advanced

Source: https://support.zendesk.com/hc/en-us/articles/8357751648666-About-data-processing-in-AI-agents-Advanced

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Our technology processes customer support transcripts in order to automate conversations, provide analytics and improve processes. This customer support data can contain Personal Identifiable Information (PII) data of end users. 

In order to minimize the PII data in chat or email messages stored in our systems, we have implemented a sanitization process when this data is received. 

Our machine learning and artificial intelligence systems do not require PII data to be trained or to do the classification so the PII data can be anonymized in the messages without compromising the service we provide our clients.

The anonymization methods for messages detect different categories of PII data in the messages and replace these values with an anonymous label corresponding to the detected categories using entities. For example, email addresses in the messages are replaced with <EMAIL> labels, bank account numbers are replaced with <IBAN> labels, and so forth. This way, we are able to avoid processing or storing any PII data in our systems. <EMAIL> and <IBAN> placeholders are examples of our default and pre-defined entities. [Here](https://support.zendesk.com/hc/en-us/articles/8357756811162) is a list of commonly used entities.

It is important to note that while we take great care to implement robust sanitization processes, we cannot guarantee that 100% of any PII data that might be received will be removed. As with any automated system and given the nature of free text chat conversations, there is always the possibility of false positives or false negatives in the detection and anonymization of PII data. 

More information about entities can be found below:

- [Entities explained](https://support.zendesk.com/hc/en-us/articles/8357749723546)
- [How to create entities](https://support.zendesk.com/hc/en-us/articles/8357749740698)
- [RegEx collection](https://support.zendesk.com/hc/en-us/articles/8357756811162)
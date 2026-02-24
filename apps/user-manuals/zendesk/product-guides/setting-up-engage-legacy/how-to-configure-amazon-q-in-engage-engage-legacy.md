# How to Configure Amazon Q in Engage (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498851354-How-to-Configure-Amazon-Q-in-Engage-Engage-Legacy

---

Amazon Q is a feature designed to assist agents by recommending relevant content during interactions.

## How to enable Amazon Q in Engage

In order to enable Amazon Q articles, ensure that the follow prerequisites are in place: 
1. Create an Amazon Q in Connect domain in the Amazon Connect console and add the relevant integration. [This](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) section in the Amazon Connect document outlines the steps to follow.

2. Add the Amazon Q in Connect block to the relevant contact flows.

3. Enable Wisdom Knowledge Base in Local Measure Features under General Settings in the Engage admin settings.

![](https://support.zendesk.com/hc/article_attachments/9731498862874)

‍

Note: For S3 integrations, Engage currently supports **.html** and **plain text files** for Amazon Q articles.

‍
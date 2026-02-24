# Configuring Amazon Q in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696127391002-Configuring-Amazon-Q-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Enable Amazon Q in Contact Center to help agents by recommending relevant content during interactions. Set it up by creating an Amazon Q domain in the Connect console, adding it to contact flows, and enabling the Wisdom Knowledge Base in admin settings. Note that for S3 integrations, only .html and plain text files are supported for Amazon Q articles.

Amazon Q assists agents by recommending relevant content during interactions.

**To turn on Amazon Q in Contact Center**

1. Create an Amazon Q in connect domain in the Connect console and add the relevant integration.

   [This](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) section in the Amazon Connect documentation outlines the steps to follow.
2. Add the Amazon Q in connect block to the relevant contact flows.
3. Enable Wisdom Knowledge Base under general settings in the Contact Center admin settings.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_qq_1.png)

Note: For S3 integrations, Contact Center currently supports .html and plain text files for Amazon Q articles.
# Creating and requesting articles while working on tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408835161114-Creating-and-requesting-articles-while-working-on-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Agents can use the [knowledge section of the context panel](https://support.zendesk.com/hc/en-us/articles/5581313653530) to create or request new help center articles while working on tickets. [Depending on your settings](https://support.zendesk.com/hc/en-us/articles/7263163614874), agents can create help center articles from a blank article or any [pre-defined templates](https://support.zendesk.com/hc/en-us/articles/4408828223898) that are available.

Note: Before you create or request an article, make sure that the ticket is created and has a ticket ID.

This article covers the following sections:

- [Creating an article while working on a ticket](#topic_ttt_lms_x5b)
- [Requesting an article while working on a ticket](#topic_zvm_mms_x5b)

## Creating an article while working on a ticket

You can create new help center articles to fill knowledge gaps directly from a ticket you're working on.

**To create an article while working on a ticket**

1. In the ticket that you are working on, click the **Knowledge** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_knowledge.png)) to open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362#topic_ehj_pqz_n4b).
2. In the **Knowledge** section of the context panel, click the **Create or request article** icon (**+**), then select **Create article**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-kiaw-create-article.png)
3. Select a template from the list to create a new article based on an existing template, or click **Blank article** to create a new blank article. Templates within the list are populated based on the ticket requester locale and ticket brand.

   The article editor opens in a new tab. You will not see the option to create a blank article if the setting has been [disabled by an admin](https://support.zendesk.com/hc/en-us/articles/7263163614874), and article templates will not be visible if [an admin hasn't created any](https://support.zendesk.com/hc/en-us/articles/4408828223898).

   ![Knowledge create article](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_knowledge_create_blank_article.png)
4. In the **Title** field, enter a name for your article.
5. Enter the content of your article and use the article toolbar for formatting options.

   Note: Information from the ticket is not automatically populated in the article. However, you can manually copy and paste content from the ticket into your article.
6. After you have created an article, update the article settings as needed. See [Creating and editing articles in the knowledge base](https://support.zendesk.com/hc/en-us/articles/4408839258778-Creating-and-editing-articles-in-the-knowledge-base).

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ew-guide-content-tag-update-article-settings.png)
7. Save or publish your article when you're ready.

## Requesting an article while working on a ticket

You can submit a request for a new help center article to fill a knowledge gaps directly from a ticket you're working on.

**To request an article while working on a ticket**

1. In the ticket that you are working on, click the **Knowledge** icon to open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362#topic_ehj_pqz_n4b).
2. In the **Knowledge** section of the context panel, click the **Create or request article** icon (**+**), then select **Request article**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-kiaw-req-article.png)
3. If you have [help centers for multiple brands set up](../../product-guides/ticket-management/setting-up-multiple-brands.md), select a help center **Brand** for the new article.

   This field defaults to the brand of the ticket you are working in. If you want the article to appear in the help centers of all brands in your account, select **All brands**

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-kiaw-req-article-modal.png)
4. Enter the **Subject** of the request.

   The text you enter appears in the title of the resulting ticket. For example, if you enter a subject of "How article creation works" in your request, the ticket title becomes "Request for article - How article creation works."

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-req-art-subject.png)
5. In **Article request**, enter a description of the content that you want the article to contain. This content appears in the ticket **Description** and can be used to provide context to the agent who will be creating the article.
6. Click **Link this ticket to request** if you want to include an optional link to the original ticket in the new request. When you select this option, the ticket that results from your request displays the link as shown in the following example:

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-req-link.png)
7. Click **Request article**. A new ticket is created with the `knowledge_request_article` tag and the agent who submitted the request listed as the Requester. The ticket is unassigned.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-req-ticket.png)
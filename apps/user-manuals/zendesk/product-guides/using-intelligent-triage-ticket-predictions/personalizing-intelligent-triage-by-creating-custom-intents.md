# Personalizing intelligent triage by creating custom intents

Source: https://support.zendesk.com/hc/en-us/articles/8718789695002-Personalizing-intelligent-triage-by-creating-custom-intents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Create custom intents to tailor intelligent triage to your business needs. By defining specific intents, categories, and subcategories, you enhance ticket classification accuracy and organization. Custom intents are unique to your account and help predict ticket topics without identifying specific details. Admins can easily create and manage these intents to improve customer support operations.

[Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) leverages AI to automatically classify incoming tickets by intent, language and sentiment. The Zendesk Intent Model includes pre-trained intents across several industries, providing relevant intents and use cases tailored to each account's ticket data.

To give you greater flexibility over your available intents, you can create custom intents that address issues specific to your business needs. You can also add new categories and subcategories as you create custom intents so that you can keep your intents organized.

This article contains the following topics:

- [About custom intents](#topic_zyc_c1y_c2c)
- [Creating a custom intent](#topic_qp5_c1y_c2c)

Related articles:

- [Automatically detecting customer intent, language, and sentiment](https://support.zendesk.com/hc/en-us/articles/4550640560538)
- [Accessing and viewing intelligent triage intents](https://support.zendesk.com/hc/en-us/articles/9488234915610)

## About custom intents

An intent is a prediction of what the ticket is about. When you activate intelligent triage, your account includes a prebuilt list of intents specific to your industry.

For example, if a customer submits a ticket saying that the item they ordered arrived damaged, then intelligent triage may automatically tag the ticket with an intent of *damaged on arrival*.

To improve your intent coverage and increase the accuracy of your intent detections, you can create custom intents that are specific to your business needs. Any custom intents you create are specific to your Zendesk account and aren’t available to other Zendesk accounts. See [Examples of custom intents](#topic_lq3_f1y_c2c) in the section below for examples of well-defined, custom intents.

As you create custom intents, you can create custom categories and subcategories to group them in. Custom intent categorization helps you organize your intent structure.

To further fine tune your setup, you can also review and accept intent recommendations made by intelligent triage. See [Reviewing intent recommendations](https://support.zendesk.com/hc/en-us/articles/9484697389210#topic_hq4_zfj_zfc).

When you create a custom intent, it's immediately added to your list of intents and starts detecting the intent of incoming customer requests. Intents aren't intended to identify details of the ticket, such as specific product or service names, branch locations, subscription types, or similar details. Instead, see the [entity detection](https://support.zendesk.com/hc/en-us/articles/6711181959194) feature to identify business-critical information in your incoming requests automatically.

Note that [AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_lrn_rwr_y1c) can't leverage the detection of custom intents.

## Creating a custom intent

Admins can create custom intents in Admin Center. A custom intent should explain the main reason the end user is reaching out and cover a single reason.

You can also create custom intent categories and subcategories when you create an intent.

To create a custom intent, you must have [intents turned on](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_gpp_p4g_htb).

Before creating a custom intent, [check whether a similar intent already exists](https://support.zendesk.com/hc/en-us/articles/9488234915610#topic_l3b_hn3_fzb). Similar or overlapping intents can lead to low-confidence or wrong intent detection. Additionally, creating a high number of custom intents can lead to performance issues.

**To create a custom intent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. Click **Create intent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_hub_intents_screen.png)

   The Create custom intent page opens.
3. Enter a **Name**.

   Use a short, descriptive name for the intent. The intent name is visible to agents, so make sure it’s clear and concise so they can quickly understand it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_intents_create_custom.png)
4. Enter a **Description**.

   This is the explanation of what the ticket is about. Clearly define what the intent should include and exclude. Write the description as if you’re explaining an issue to an agent on their first day. Consider including examples and common words that users might use.
5. Select a **Category**.

   Intents are organized hierarchically in three levels: category, subcategory, and intent. The category is the broad reason for an incoming request, the subcategory provides a more detailed breakdown of the reason, and the intent is a single, very specific reason.

   Alternatively, you can create a custom category:
   - Select**+ Add category and subcategory** from the menu.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_triage_custom_intent_category.png)
   - Enter a **Category name** and **subcategory name**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_triage_custom_inent_create_category.png)
   - Click **Add**.
6. Click **Create custom intent**.

   The new intent is added to the Intent list tab and is labeled *Custom*.

### Examples of custom intents

Below are some examples of well-defined custom intents:

**Product not working as expected**

- **Name**: Product not working as expected
- **Category**: Order
- **Sub-category**: Product issue
- **Description**: The requester wants to report a product that is not functioning correctly, has developed a fault, or is not meeting quality expectations.

**Cancel direct debit**

- **Name**: Cancel direct debit
- **Category**: Billing
- **Sub-category**: Change payment method
- **Description**: The customer wants to stop or cancel an existing direct debit or automatic payment arrangement. They may cite reasons such as financial constraints, changes in circumstances, or dissatisfaction with the service.

**Change booking arrival location**

- **Name**: Change booking arrival location
- **Category**: Travel
- **Sub-category**: Booking update
- **Description**: The end user wants to modify the arrival location of their booking. This could include changing flight destinations, correcting errors in the booked location, or updating hotel addresses.
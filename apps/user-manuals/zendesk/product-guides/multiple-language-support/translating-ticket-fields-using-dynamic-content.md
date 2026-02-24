# Translating ticket fields using dynamic content

Source: https://support.zendesk.com/hc/en-us/articles/4408883892762-Translating-ticket-fields-using-dynamic-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

If you support multiple languages, you can translate, or localize, your ticket fields. That way, when a customer submits a ticket, you can provide them properly translated text in their language.

Standard ticket fields in Zendesk are translated automatically and don't require dynamic content. This article shows you how to get started using dynamic content for translating *custom* ticket fields.

This article includes these sections:

- [Creating and using dynamic content with a ticket field](#h_41e9a85b-2d47-400e-9eca-49492cc7f2ed)
- [Viewing your localized content](#h_075b684f-eb7f-431c-ae57-7c3feff2d654)

## Creating and using dynamic content with a ticket field

Follow these steps to create dynamic content for your [custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408838961562). Note that ticket fields with a value, such as a drop-down, require their own dynamic content.

**To create and use dynamic content with a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Tickets > Fields**.
2. Choose which field you would like to use dynamic content with. 
   In this example, we use a standard field, **Subject** to help illustrate the process. Standard ticket fields are translated automatically and don't require translation, but the process is the same for custom fields.
3. Next, create the dynamic content we need to localize this field. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Workspaces** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)) in the sidebar, then select **Dynamic Content**.
4. Click **Add Item** or **Add one now**.
5. Enter a title for your new piece of dynamic content. Make sure this is a name you'll be able to find later, for example, "Subject Ticket Field - Title." You might be creating many pieces of dynamic content so a good naming convention is important.
6. Select the default language for your dynamic content. This field will show all of the languages that you have enabled for Zendesk Support but that doesn't mean they're enabled on your Help Center. (For more information on enabling multiple languages for your help center, see [Localizing help center content](https://support.zendesk.com/hc/en-us/articles/4408834328090/#topic_esz_slg_p3).) 
   In this example, **English** is selected.
7. Enter the text you want to see for the default language. As this is English, enter "Subject". 
   The final result looks something like this: 
     
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_EnglishSample.png)
8. Remove any trailing spaces or line breaks before saving your text as this might cause issues when used within other Zendesk products.
9. Click **Create.** You're redirected to a screen where you can choose to create a translation.
10. To create a translation, click on **Add variant.** **![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_initialPage.png)**
11. On the next screen, select the language for your variant, choose a status (active or inactive), and then enter the content. This is very similar to creating the default piece of dynamic content. In this example, **Spanish** (*Español*) is selected, the status **Active** is selected, and the Spanish word for subject, "Asunto" is entered. 
      
    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_Espanol.png)
12. Click **Create** to create your variant.
13. Copy the placeholder for your piece of dynamic content. You'll need this for the next step. 
      
    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_placeholder.png)
14. Click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Tickets > Fields**.
15. Click **Edit** for the ticket field you wish to change.
16. Now paste your dynamic content placeholder into the **Title** field for end users. (You can also use dynamic content to change your **Description**, but you'll need to create a separate piece of dynamic content and use a different placeholder). 
      
    ![dc_addPlaceholderAndUpdate.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_addPlaceholderAndUpdate.png) 
    The titles for system fields like Subject cannot be modified for agents, only end users. 

    Note: If you're adding dynamic content for field with a value, such as a drop-down, you must create a dynamic content placeholder for each value. Then, insert the placeholder into the value field.
17. Click **Update field**.

## Viewing your localized content

The result of creating this piece of dynamic content shows on your **Submit a Request** page. You will get two different variations of your title in the Subject Ticket Field, depending on what language you have selected in your Help Center.

In this example, if you use **English** as your language in your Help Center, you'll see the following when you submit a ticket:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_EnglishTranslation.png)

However, if you use **Spanish (**   **Español)** as your language in your Help Center, you see the following:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_SpanishTranslation.png)

You can also do this for other fields, like the Description field. The example below shows two pieces of dynamic content, one for the **Title** of the ticket field, and the other for the **Description** of the ticket field. The example uses the same steps as above, but also adds a placeholder into the ticket field description.

The result in **English**:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/submit_a_request_English.png)

The result in **Spanish (****Español)**:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/submit_a_request_Spanish.png)

To read more about dynamic content, see our guide on [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066).

Note: If you've enabled any language variants in your help center, you must create and use dynamic content placeholders for the variant's parent language in order for translations to fall back to the parent language. For more information on supported languages and language variants, see [Zendesk product support by language](https://support.zendesk.com/hc/en-us/articles/4408830359450).
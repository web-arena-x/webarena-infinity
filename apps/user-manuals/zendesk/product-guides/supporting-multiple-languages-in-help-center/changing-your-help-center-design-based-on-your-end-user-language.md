# Changing your help center design based on your end user language

Source: https://support.zendesk.com/hc/en-us/articles/4408894121754-Changing-your-help-center-design-based-on-your-end-user-language

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Note: Customers who are not on a Suite plan must have Support Professional or
Enterprise with any Guide plan to use this feature.

If you [support multiple languages](configuring-your-help-center-to-support-multiple-languages.md#topic_ys2_kxh_tz), you can
use [dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066) to create your own
translations and reference them in macros, triggers, and other automations using
a *placeholder*. In addition, dynamic content supports HTML code. For
example, you can create a dynamic content item to dynamically change the design
of your help center based on the customer's language.

Let's say that your company targets the French and English speaking markets. You
would therefore like to have a different footer on your help center to provide
different contact information based on your customer's language. Or maybe, for a
better customer experience, you'd like to display the French support number only
to French speaking customers. In this article, you'll learn how to set this
up.

This article covers the following topics:

- [Creating a new dynamic content
  item](#topic_atm_pgc_l4b)
- [Modifying your help center
  theme](#topic_ex1_qgc_l4b)

Note: While HTML is supported in dynamic content in your help center, HTML is not
supported in dynamic content in macros, triggers, automations, agent signatures,
or ticket fields and forms. Dynamic content can only be used in help center
templates and will not render if used in Javascript.

## Creating a new dynamic content item

You need to be a Zendesk Support administrator to create dynamic content. In this
example, you'll create a dynamic content item with a French variant and add the HTML
code of the footer you'd like to be displayed for French speaking customers. Dynamic
content allows you to choose a default language. A good best practice is to English
if your customer selects a language for which you don't have a footer
translation.

1. In [Admin
   Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb),
   click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic
   Content**.
2. Click **Add Item** .
3. Choose a name, such as **footer**  or **HC\_footer**  to more easily find
   your help center related dynamic content later.
4. Select a default language such as English.
5. Paste the HTML code you want to display for English speaking customers in the
   **content**  box.
6. Click **Create** to save your dynamic content item**.**
7. Notice the item's name between curly brackets. You'll use that later on.
8. Now add one or more other translations. To do so, click **Add Variant**  and
   follow steps 3-6 again.

Your dynamic content ready. Now, you can add it to your help center.

## Modifying your help center theme

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click the theme you want to edit to open it.
3. Click the options menu, then select **Edit Code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_menu_option_edit_code.png)
4. This example modifies the footer so open the  **Footer**  template.
5. Use the following syntax to insert the dynamic content item we created above:
   {{dc '  *item\_name*  '}}.
6. Click  **Save**  and you'll be able to see the newly added footer.
7. Click  **Publish changes.**

Now, your custom footer on your help center and the text will be displayed based in
the language your customers select on the homepage.

This article covered only the footer but you can go further than that. You could have
a completely different look and feel based on your customer's language. Or maybe the
product you're selling has a different name in French than in English; in this case
you can use dynamic content to display a different logo based on the customer's
language.
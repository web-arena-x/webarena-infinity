# Translating macros using dynamic content

Source: https://support.zendesk.com/hc/en-us/articles/4776777747866-Translating-macros-using-dynamic-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

If you support multiple languages, you can translate, or localize, your macros. That way,
when an agent needs to use a macro to provide quick and efficient support, they can do
so in the right language.

To learn more about creating macros, see [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034). To learn more about how dynamic
content works, see [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066).

This article contains the following topics:

- [Creating and using dynamic content for
  macros](#topic_shh_ffv_f5b)
- [Creating localized categories for
  macros](#topic_bgc_hfv_f5b)
- [Viewing your localized
  macros](#topic_cnr_3fv_f5b)

## Creating and using dynamic content for macros

To localize your macros, you’ll create dynamic content, which includes a default
language along with additional variants for the other languages you want the macro
to be available in.

To fully localize a macro, you’ll need to create two pieces of dynamic content: one
for the macro name and one for the macro body.

Tip: Before you get started, make sure you’ve
already [created the macro](https://support.zendesk.com/hc/en-us/articles/4408844187034) you want to
localize. Also, make sure you [have the translations](https://support.zendesk.com/hc/en-us/articles/4408886903450) of the macro
content in your supported languages.

**To create dynamic content for a macro name or body**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic Content**.
2. Click **Add item**.
3. Under **Dynamic content item title**, enter a descriptive title for your new
   piece of dynamic content. To make it easier to find and manage your localized
   macros, Zendesk recommends naming the dynamic content the same as the macro name
   in your account's default language (for example, "Macro - <Macro name> -
   Name" or “Macro - <Macro name> - Body”).
4. Select the **Default language** for your dynamic content. This field shows
   all of the [languages that you have enabled](https://support.zendesk.com/hc/en-us/articles/4408888770714) for
   Zendesk Support.
5. In the **Content** field, enter the text you want to see for the default
   language (for either the macro name or the macro body).

   Tip: Remove any trailing spaces or line breaks before
   saving your text, as this might cause issues when used within other Zendesk
   products.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_1.png)
6. Click **Create**. You're redirected to a screen where you can add variants
   for the languages you want your macro to be available in.
7. Click **Add variant** and fill out the following fields:
   1. **Language**: Select a language you want the macro to be available
      in.
   2. **Status**: Select **Active**.
   3. **Default**: Leave this checkbox blank. Select it only if you want to
      change the macro's default language from the one you created earlier to
      this one.
   4. **Content**: Enter the text of the macro in the language you just
      selected. In other words, this is the translation of the text you
      entered in your initial piece of dynamic content.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_2.png)
8. Click **Create**. You’re redirected to the variants page.
9. (Optional) Repeat steps 7-9 for any additional languages you want the macro to
   be available in.
10. Near the top of the variants page, copy the **Placeholder** text for your
    dynamic content. You'll need this for the next step.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_3.png)
11. In the sidebar, click **Workspaces**, then select **Agent tools** >
    **Macros**.
12. Select the macro you want to localize.
13. Paste your dynamic content placeholder into the appropriate field:
    1. If you created dynamic content for the macro name, paste it into the
       **Macro name** field.

       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_4.png)
    2. If you created dynamic content for the macro body, paste it into the
       **Rich content** field (which is available when your macro has an
       **Action** of **Comment/description**).

       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_5.png)

       Note: If you
       no longer have your placeholder copied, don’t worry—just reopen your
       piece of dynamic content (**Workspaces** > **Agent tools** >
       **Dynamic content**) and copy the placeholder again.
14. Click **Save**.

## Creating localized categories for macros

If you’ve [categorized your macros](../../agent-guide/ticket-automation-and-collaboration/organizing-and-managing-your-macros.md#topic_dpr_k1j_mw), you can also
localize the category names.

**To localize macro categories**

1. [Create another piece of dynamic
   content](#topic_shh_ffv_f5b) for the macro category name.
2. Open the macro you want to categorize and localize.
3. Update the macro’s name to include the dynamic content for the category and the
   dynamic content for the macro name, separated by two colons.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_6.png)
4. Click Save.

## Viewing your localized macros

You can view and manage your localized macros on the Macros administration page.

**To view and manage your localized macros**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
  **Workspaces** in the sidebar, then select **Agent tools > Macros**.

When viewed here, localized macros show the placeholder name in the **Name**
column.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_7.png)

For more on managing macros, see [Organizing and managing your macros](https://support.zendesk.com/hc/en-us/articles/4408884166554).

Agents can also view and select localized macros in the Agent Workspace.

**To view and use your localized macros**

- In the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), open a ticket and
  click the **Apply macro** field.

When viewed here, localized macros appear in the agent’s selected language.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_translate_macros_8.png)

For more on using macros, see [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602).
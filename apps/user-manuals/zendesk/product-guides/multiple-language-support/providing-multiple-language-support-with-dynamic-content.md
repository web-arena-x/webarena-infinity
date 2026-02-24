# Providing multiple language support with dynamic content

Source: https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

Create dynamic content to support multiple languages by using placeholders
in automations, macros, and triggers. Define default text and language variants,
ensuring the correct version appears based on user language. Manage translations
directly or via export/import with translation agencies. Use dynamic content
in ticket fields, agent signatures, and system messages to streamline multilingual
support.

Location: 
Admin Center > Workspaces > Agent tools > Dynamic
content

To provide multiple language support, you can create dynamic content that
can
then be referenced via a placeholder in automations, macros, triggers,
custom fields, custom agent statuses, and by many of the system generated
messages such as those sent in email notifications when a user creates an
account.

This article covers the following topics:

- [About dynamic
  content](#topic_ag4_zgp_2fc)
- [Creating dynamic
  content and variants](#topic_qcy_eci_je)
- [Deleting dynamic
  content and variants](#topic_izg_rnv_le)
- [Managing the
  translation of your dynamic content](#topic_hdn_hdi_je)
- [Using your dynamic
  content](#topic_enk_bdi_je)

## About dynamic content

To provide multiple language support, you can create dynamic content
that
can then be referenced via a placeholder in automations, macros,
triggers, custom fields, custom agent statuses, and by many of the
system generated messages such as those sent in email notifications
when a user creates an account.

As an example of how you can use dynamic content, the text of a message
that
you currently add to a macro can be replaced by a dynamic content
placeholder.

This text:

```
If you forget your password, just click the "Help! I don't know what to enter here!" link on the login page. 

Thanks and have a great day!

The MondoCam Support Team
```

Is replaced with this placeholder:

```
{{dc.password_help}}
```

When the macro is applied to a ticket, the content is inserted into the
ticket. If you're already using Zendesk placeholders, you're already
familiar with how this works. The primary difference between the
Zendesk placeholders and dynamic content is that you define the
content that is dynamically inserted into your business rules and
communications with your customers.

Dynamic content is a combination of a default version of the text
(typically in the same language as your default language) and
variants for every other language that you support. In the example
above, the default variant is in English. If your Zendesk also
supports French and German, for example, you create variants for
each of those languages. Then, based on the end user's language, the
appropriate variant is automatically used when the dynamic content
is referenced and displayed to the end user.

If the end user's language is not one of your supported languages, the
default variant is used.

Dynamic content provides you with a way to streamline support for
multiple languages. You reference one placeholder and the
appropriate language is displayed based on the end user's language
preference. How an end user's language is detected is described in
[Setting and detecting a user's
language](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_tmu_gno_ze).

Of course when you support multiple languages, you must translate your
content into the languages you support in your Zendesk. There are a
number of ways to manage the translation of your default content.
You can create and edit all your language variants directly in your
Zendesk or you can export all your dynamic content and send it off
to a translation agency. You then import the dynamic content back
into your Zendesk and all language variants are added.

If you later update the default content, the variants are flagged as
being potentially out of date with the default content. Meaning that
if you update the default content you probably need to also update
the translations in the variants. When an update is required, you
simply repeat the export and import process to update the content.
See
[Managing the
translation of your dynamic content](#topic_hdn_hdi_je).

You can also manually set variants to be inactive so that they are not
used. You might do this if your variant isn't ready to be made
public (for example, if the translation is incomplete or incorrect).

Finally, how you use your dynamic content in automations, macros, and
triggers is tracked so that you have an easy way to monitor their
use.

## Creating dynamic content and variants

When you create a dynamic content item, you select the default language
and enter the text
of the dynamic content. You then create variants for each of your supported
languages.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_select_lang.png)

### Creating dynamic content

You can create dynamic content to provide support in multiple languages.

**To create a dynamic content item**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. Click **Add item**.
3. Enter a title for the dynamic content.
4. Select the default language.

   Note: The list of
   languages you can choose from is
   based on your default language and the
   [additional
   languages you've chosen to support](https://support.zendesk.com/hc/en-us/articles/4408888770714)
   in the
   **Localization** settings
   page. You can add
   language variants for all of the languages that
   Zendesk supports.
5. Enter the text of the dynamic content.
   - You can use Zendesk placeholders in your
     dynamic content. For example, you can add
     placeholders for ticket and user properties. See
     [Zendesk data object
     (placeholders) reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).
     You can also add
     other dynamic content placeholders.
6. Click **Create**.

When you create a dynamic content item, the detail page is
displayed. You [add variants](#topic_trk_vqh_le)
for each of your supported
languages to your dynamic content.

Below the title of the dynamic content, you'll see the
placeholder that you'll use to refer to this dynamic content
in your automations, macros, triggers, and in system
messages. Dynamic content placeholders always begin with the
'dc' prefix. Once you use the placeholder, you'll see where
it's used in the References section.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_new_dc.png)

You can edit the dynamic content title by clicking Edit. The text
of your default content, shown in the Variants section, can
be edited by clicking the Edit button in the table row.

Changing the title after you've created the dynamic content does
not change the placeholder name. It remains the same
regardless of the subsequent changes you may make to the
title.

### Creating variants

Variants are different language versions of the default variant for
your dynamic content.

**To create a variant**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. Click the title of the dynamic content where
   you'd like to add a variant.
3. Click **Add variant**.
4. Select the variant language.

   The list of
   languages you can choose from is based on the
   languages you've chosen to support. See
   [Configuring your
   Help Center to support multiple
   languages](https://support.zendesk.com/hc/en-us/articles/4408827609882).
5. Set the variant to **Active** or
   **Inactive**.

   Active means that the variant
   will be used as the text for all users of that
   language. When you set a variant to Inactive,
   you're disabling its use and users of the inactive
   language will instead see the default content
   variant. In other words, if the default content is
   in English and you make the German variant
   inactive, German users see English content.
   Typically, you set a variant to inactive if the
   variant's content is not ready to be made public
   (i.e., the translation is not complete).
6. You can also optionally set the variant to be
   the default variant, which overrides the current
   default variant.

   Setting a language variant as
   the default variant is useful when you want to
   create dynamic content specifically for a group
   that supports a language other than your default
   language. For example, a Japanese language support
   group can set default variants as Japanese. When
   you change the default from one variant to
   another, the status of the other variants changes
   to **Out of date**.
7. Enter the text of the variant language.

   Depending on how you're managing the
   translation of the content, you can instead first
   create all your dynamic content in your default
   language and then export the content and send it
   to a translation agency. An export file is created
   for each of the languages that your Zendesk
   supports. You then import the files back into your
   Zendesk and all of the language variants are added
   to the dynamic content. For information about
   managing the translation workflow, see
   [Managing
   the translation of your dynamic content](#topic_hdn_hdi_je).
8. Click **Create**.

Here's an example of the password help dynamic content variant in
German.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_new_variant.png)

When you add variants, they are listed as shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_variants_list.png)

In the list of variants, you'll see that the default content is flagged
as the default.
You can edit each variant by clicking **Edit**.
You can also delete all the variants
that are not the default. To delete the default variant you need
to either set a different
variant as the default or delete the entire dynamic content item.
See
[Deleting dynamic content](#topic_zwx_ojv_le).

The status column in the list shows if the variant is active or inactive;
the selections
you made when creating or updating the variant. Status also conveys
the state of variants
relative to the default variant. When the default variant is updated
and the other
variants are not, the other variants are considered to be out of
date with the default
variant. In other words, it is assumed that if the default variant's
text was updated then
the other variants text should also be updated. To give you an indication
that the text in
the variants may be out of sync with the default variant, they are
flagged as being out of
date. Therefore, you may see the following statuses for your variants:

- Active
- Inactive
- Active (Out of date)

As described below, you can quickly view the dynamic content items
that contain variants that are
out of date.

## Deleting dynamic content and variants

You can delete dynamic content or individual variants as needed.

### Deleting dynamic content

You can delete dynamic content only if it is not being referenced
by your automations, macros, or triggers. How your dynamic
content is being used is shown in the References section of
each dynamic content item.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_references.png)

By clicking the link to the reference, you can edit the business
rule and remove the dynamic content placeholder. Once all
the references have been removed, you can delete the dynamic
content item.

Note: References are only tracked
for automations, macros,
and triggers. If you used a dynamic content
placeholder in a system generated message, you'll
need to track their use manually. If you do delete a
dynamic content item without first removing the
placeholder from the system message, the content
continues to be displayed to users.

**To delete a dynamic content item**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. Locate the item you want to delete, then click
   **Delete**.
3. Click **OK** to confirm that you
   want to
   delete the item. If there are no references to the
   dynamic content, the item is deleted. If there are
   references, the item is not deleted. You can then
   remove the references and delete the item.

### Deleting variants

Any of the non-default variants in a dynamic content item can be
deleted at any time. References to the dynamic content
placeholder do not affect the variants. To delete the
default variant, you need to make another variant the
default or delete the entire dynamic content item.

**To delete a dynamic content variant**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Dynamic content**.
2. Locate the item that contains the variant you
   want to delete and open it.
3. Locate the variant and click **Delete**.
4. Click **OK** to confirm that you
   want to
   delete the item.

## Managing the translation of your dynamic content

You can manage the translation of your dynamic content in the following
ways:

- You can add translated content when you create the variants in
  your Zendesk. You can
  then manage updates to the translated content by editing the
  variants.
- You can create all the default language versions of the dynamic
  content and then
  export them as CSV (comma separated values) files and send them
  out for translation.
  When the translations are complete you import the CSV files back
  into your Zendesk and
  all the language variants are added.
- You can do a combination of both these approaches; translating
  and editing some
  variants in-house and using the export/import process to create
  and update the language
  variants via a third-party translation agency.

For information about exporting and importing your dynamic content, see
[Exporting and importing
dynamic content](https://support.zendesk.com/hc/en-us/articles/4408894053530).

## Using your dynamic content

The dynamic part of dynamic content is that the correct version of the
content is automatically
shown to the end user based on their language. The content is also
shown to agents in the same language as the end user. As
with the Zendesk placeholders (see
[Zendesk data object
(placeholders) reference](https://support.zendesk.com/hc/en-us/articles/4408886858138)),
to use your dynamic
content you simply reference the placeholder.

Using the 'Password Help' dynamic content as an example, you can use
the dynamic content by
adding the placeholder into a comment in a business rule, such as a
macro.

Every dynamic content item has a corresponding placeholder.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_placeholder.png)

In this example, it's {{dc.password\_help}}.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_macro_password.png)

When the macro is applied to the ticket, the appropriate language variant
text is inserted into
the comment. If the end user's language is not one of your supported
languages, the default variant is used.

Dynamic content placeholders can be used in your automations, macros,
and triggers. You can also
use your dynamic content for common system messages such as those
used in the sign up process. For example, the text contained in the
user welcome email message can be replaced with a dynamic content
placeholder.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dc_user_welcome.png)

Note: For HTML formatting to
render correctly, you must add Liquid markup to your dynamic
content. See
[Using Liquid markup to support multiple
languages](https://support.zendesk.com/hc/en-us/articles/4408842967578).

You can use dynamic content placeholders in the following:

- Ticket field names, both system and custom (see
  [Using dynamic
  content to translate your ticket
  fields](https://support.zendesk.com/hc/en-us/articles/4408883892762))
- Custom drop-down labels
- Custom ticket statuses
- Ticket form names
- Agent signature (see
  [Adding an agent signature to
  ticket email notifications)](https://support.zendesk.com/hc/en-us/articles/4408822471322)
- Help center (see
  [Adding translated
  text](https://support.zendesk.com/hc/en-us/articles/4408834328090#topic_wnw_fbg_yj))
- Sign-up messages for end users (visible only when Guide
  is enabled), including:
  - User registration message
  - User welcome email
  - Email verification email
- Macros
- Triggers and automations

  Note:
  - When dynamic content is used in the body of a
    **Notify URL target** action,
    the default
    variant is always used.
  - When using dynamic content in the body of an
    **Autoreply** action, it
    must be formatted as HTML to appear
    properly.
- Custom unified agent statuses
- Other dynamic content

  Note: Placeholders of all
  types
  that are used in dynamic content are limited to a
  maximum of five levels of recursion.

How an end user's language is set and detected and then used when displaying
dynamic content is
explained in
[Setting and detecting a user's
language](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_tmu_gno_ze).
You can also find several examples of how
to build a workflow based on language in
[Using a requester's language in your
business rules](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_uqw_ufw_bf).
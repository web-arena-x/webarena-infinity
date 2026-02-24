# Configuring Zendesk Support for your locale and language

Source: https://support.zendesk.com/hc/en-us/articles/4408887059866-Configuring-Zendesk-Support-for-your-locale-and-language

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The default configuration of Zendesk Support is in the English language. However, the agent and administrator user interface can be viewed in a number of [supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826). For example, you can change the language of the system messages that appear in email notifications to your end users.

You can switch Zendesk Support to a different default language by modifying your account settings and updating the default business rules that contain text in English.

If you want to support more than one language, see [Adding multiple languages to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408888770714-Configuring-your-Zendesk-to-support-multiple-languages-Plus-and-Enterprise-). Zendesk fully supports UTF-8 (Unicode). All languages supported by Zendesk can be added to forms, comments, tags, and so on.

This article covers the following tasks:

- [Setting the default language for your account](#topic_rtc_42j_1y)
- [Setting time zone and format for Zendesk Support](#topic_dil_hnc_xe)
- [Translating system-generated new user email notifications](#topic_ijx_svh_xe)
- [Adding translated text to the agent signature](#topic_mck_unc_xe)
- [Adding translated text in default automations, macros, and triggers](#topic_ukk_syh_xe)

## Setting the default language for your account

The default language is the language that agents see in the agent interface by default and that end users see in the Help Center by default.

This setting also affects the UI of the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/8725042447002), but note that the only languages supported for the add-on UI are English, Brazilian Portuguese, French, German, Japanese, and Spanish.

**To set the default language for your account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Appearance > Localization**.
2. Beside **Languages**, select a default language from the drop-down.
3. Click **Save tab**.

## Setting time zone and format for Zendesk Support

You can change your account's time zone and format so that timestamps, such as those on tickets and articles, correspond to your locale.

**To set your account's time and format**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Account** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)) in the sidebar, then select **Appearance > Localization**.
2. Select the appropriate GMT time zone.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/localize_time_zone.png)
3. Select weather time appears in the 12-hour or 24-hour format.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/localize_time_format.png)

   Note: There is currently no support for locale specific date and number formats.

On Support Professional and Enterprise your staff and end users to set their own time zone in the user profile.

## Translating system-generated new user email notifications

When end users sign up, they receive a number of email notifications. By default, these are in English but you can easily translate them into another language.

**To edit the user welcome and verification emails**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Configuration > End users**.

The user welcome email:

```
Please follow the link below to choose a password, and we will log you in right away.
```

The email verification email:

```
We need to verify that you are the owner of this email address. Please follow the link below to verify.
```

If you don't require your end users to register and log in, they will not receive any of these messages. See [Setting up to provide email-only support](https://support.zendesk.com/hc/en-us/articles/4408888722842-Setting-up-to-provide-email-only-support).

If you're using dynamic content (see [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content-Plus-and-Enterprise-), you'd replace this text with placeholders that automatically insert the appropriate language when the email notifications are sent.

## Adding translated text to the agent signature

You can [configure a team member signatures](https://support.zendesk.com/hc/en-us/articles/4408822471322) that appears in outgoing email notifications. You can use placeholders to dynamically insert the signature and phone number that agents add to their own user profiles, like in the example below:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_signature.png)

You can also add additional text in the appropriate language to the account signature. For example:

```
{{agent.signature}} - {{agent.phone}}
Toute l'équipe du Support MondoCam
```

If you use dynamic content, you'd add a dynamic content placeholder here instead. See [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content-Plus-and-Enterprise-).

## Translating the text in default automations, macros, and triggers

When you create a Zendesk account, a number of automations, macros, and triggers are included to help you get started managing your support workflow. Each of these contains text in English that is sent to end users in email notifications. For more information, see the following topics:

- [About the standard Support triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346)
- [About the standard Support automations](https://support.zendesk.com/hc/en-us/articles/4408835051546)
- [Macros to get you started](https://support.zendesk.com/hc/en-us/articles/4408887656602#topic_lty_vgx_tb)

If you support more than one language, you can also use Liquid markup to generate messages in more than one language from a single business rule. For example, you can edit the **Notify requester and CCs of received request** trigger to generate messages based on the user's language setting. For more information, see [Using Liquid markup to support multiple languages in automations, macros, and triggers](https://support.zendesk.com/hc/en-us/articles/4408883291290-Using-Liquid-markup-to-customize-comments-and-email-notifications#topic_snv_nqh_jc).

On Support Professional and Enterprise, you can use dynamic content to manage content for multiple languages. Using dynamic content, you replace the text with a dynamic content placeholders that automatically insert the appropriate language version of the text based on the user's language. See [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content-Plus-and-Enterprise-).

**Related topics**

- [Creating triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466)
- [Managing triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722)
- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602-Using-macros-to-update-tickets-and-chat-sessions)
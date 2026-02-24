# Detecting an end user's language from an email message

Source: https://support.zendesk.com/hc/en-us/articles/4408882016666-Detecting-an-end-user-s-language-from-an-email-message

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

Automatically detect a user's language from email messages, especially useful for email-only support. This feature works for new or unregistered users without a set language. If the language can't be detected, the default language is used. Ensure multiple languages are enabled in your account. Supported languages include English, Spanish, French, and more.

There are several ways to [detect and set a user's language](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_tmu_gno_ze). One of
those ways is automatically detecting an end user's language from an email
message sent to Zendesk Support. Automatic detection works only for requests
from unregistered (new) users and users who do not currently have a language
setting selected.

Email-based language detection is useful if you provide support via email only
since your users don't use help center, never sign in, and aren't able to
set a language preference. The only other way to handle language for
email-only end users is to have them send email support requests to a
language-specific email address such as german@support.myaccount.com.

This article contains the following sections:

- [How it works](#topic_el5_jyv_qy)
- [Supported languages](#topic_lfw_sqk_tf)

## How it works

Email-based language detection is automatically turned on when you have
more than one language in your Zendesk account.

First, the incoming email message is analyzed to detect the language. If the scan detects one
with enough confidence, it is set automatically for the user. The
length of the email message can affect the language analysis.
(Longer messages produce better results.)

If the language-processing analysis couldn't detect a language, and the
email has a valid `Accept-Language` header, then:

- If the language in the `Accept-Language`
  header is included in your [supported
  languages](https://support.zendesk.com/hc/en-us/articles/4408888770714), then the user's language
  preference is set.
- If a language can't be detected by analyzing the email
  text or header, then the user's language is set to
  the Zendesk account's default language.

Note: If the "Ask users to register" setting is enabled, this feature will not set the language for
the end user, because their initial ticket will be suspended. The
language will be set either by the end user when they create their
profile or by the agent when creating the profile to recover the
suspended ticket.

## Supported languages

The email language detection feature currently supports the following languages:

- Arabic
- Chinese
- Danish
- Dutch
- English
- Finnish
- French
- German
- Greek
- Hebrew
- Italian
- Japanese
- Korean
- Norwegian
- Polish
- Portuguese
- Russian
- Spanish
- Swedish
- Thai
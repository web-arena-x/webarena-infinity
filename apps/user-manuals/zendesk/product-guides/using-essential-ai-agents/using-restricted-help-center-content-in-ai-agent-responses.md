# Using restricted help center content in AI agent responses

Source: https://support.zendesk.com/hc/en-us/articles/8087943201306-Using-restricted-help-center-content-in-AI-agent-responses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

To use restricted help center content in your AI agent, it's essential that you
understand what constitutes restricted content, where you can use it in an AI agent, and
the settings across Zendesk you need to consider and configure.

In this article, we’ll explain these concepts and tasks and direct you to
Zendesk resources that can help you incorporate restricted help center content into your
AI agent. You may find that not all of the suggestions in this article apply to your
configuration; just use the information that applies to your use case.

This article includes the following topics:

- [About restricted content](#topic_f4y_3br_vcc)
- [Authenticating end users](#topic_xld_jbr_vcc)
- [Using restricted content in AI agent responses](#topic_nml_jbr_vcc)

## About restricted content

There are two ways you can restrict content in your help center:

- **Using the** **[Require sign-in option](https://support.zendesk.com/hc/en-us/articles/4408825656474-Configuring-Guide-settings#topic_psl_kyf_gjb)**, which
  restricts all content in the help center to authenticated and signed-in end
  users.
  - AI agents support this type of restriction. AI-generated answers will be
    available only for end users who are signed in to your help center.
- **Setting view permissions** (on Suite Growth plans and above) to restrict
  access to specific [articles](https://support.zendesk.com/hc/en-us/articles/4408824005914). Access to [categories and sections](https://support.zendesk.com/hc/en-us/articles/6136330813722) is based on
  article settings.
  - AI agents support this type of restriction. Restricted articles are used
    in AI-generated answers only for end users whose user segment(s) match
    the article’s view permissions.

When you apply restrictions to one of these elements, they apply to all
elements below it in the [help center hierarchy](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ol5_3fd_43):

- When **Require sign-in** is selected in Knowledge admin security settings,
  the entire help center is restricted; all categories, sections, and articles are
  also restricted and require users to sign in for access.
- When an article is restricted, all comments in that article are
  also restricted, and users must sign in for access.
- When all articles in a section are restricted, that section only
  appears to signed-in users.
- When all sections in a category are restricted, that category only
  appears to signed-in users.

## Authenticating end users

End users may be able to view restricted content in a help center using a simple
sign-in procedure. However, to view restricted content through an AI agent, you need
to take additional steps to be authenticated by Zendesk.

To view restricted help center content in an AI agent on a messaging channel:

- The end user must already exist as a user in your Zendesk
  account.
- The end user must be [authenticated via messaging JWT](https://support.zendesk.com/hc/en-us/articles/4411666638746),
  including [mapping them to user records](https://support.zendesk.com/hc/en-us/articles/4411666638746#topic_cqt_xzx_1bc).
- The [external ID](https://support.zendesk.com/hc/en-us/articles/4408893887002) passed via the JWT
  authentication must be associated with the user in Zendesk via the external ID field.

  Note: Optionally, you can [turn on help center
  authentication](https://support.zendesk.com/hc/en-us/articles/9495852479770) to automatically associate user identities
  with end users logged in to the help center.

To view restricted help center content in an AI agent on an email or web form
channel:

- The end user must be part of a [user segment](https://support.zendesk.com/hc/en-us/articles/4408837707290) that has viewing
  permissions for the article.

## Using restricted content in AI agent responses

When you configure the settings described above, authenticated customers can view
restricted content from help center articles in responses from your AI agent.

Additionally, these settings let authenticated customers view restricted content in
the following legacy AI agent functionality:

- [If the AI agent finds relevant
  information](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_o1b_m1n_gbc) standard response
- [Show help center articles step type](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_grj_gwc_k4b) in
  an AI agent answer
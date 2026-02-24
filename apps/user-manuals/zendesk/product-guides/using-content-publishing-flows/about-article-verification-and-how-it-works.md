# About article verification and how it works

Source: https://support.zendesk.com/hc/en-us/articles/5588297664666-About-article-verification-and-how-it-works

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

Location:  Knowledge admin > Settings (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) > Article verification

Verification is an article setting that lets you indicate whether an article is accurate and
current, or whether it needs review and possible revision. Verifying articles is an important
part of keeping your knowledge base healthy and up to date.

This article describes article verification strategies and the resulting experience for
agents and admins, and provides answers to frequently asked questions about article
verification.

This article includes the following sections:

- [How article verification works](#topic_slz_kjc_dxb)
- [About article verification
  emails](#topic_oxr_mjc_dxb)
- [Verifying articles for agents and
  admins](#topic_bxs_mjc_dxb)
- [Article verification FAQs](#topic_zdt_mjc_dxb)

Related articles:

- [Setting reminders to review and verify articles](https://support.zendesk.com/hc/en-us/articles/4408828628634)
- [Verifying articles that need review](https://support.zendesk.com/hc/en-us/articles/4408822044186)
- [Managing article verification rules](https://support.zendesk.com/hc/en-us/articles/4408832243482)

## How article verification works

When you create an article, it is neither verified nor unverified. Articles in this state
appear with a hyphen (-) symbol in the Unverified and Verified at columns of the articles
list. If an article is neither verified nor unverified, there is no way to determine when it
was last reviewed or whether it is current.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-artverif-all-articles2.jpg)

To begin article verification, you can choose one of the following
strategies:

- Manually unverify articles, prompting a review and verification by article
  owners.
- Automatically unverify articles by configuring article verification rules
  based on predefined filter and interval criteria.

Unverified articles appear in the [Needs verification list](https://support.zendesk.com/hc/en-us/articles/4408822078490) and are included in bi-weekly emails to
article owners reminding them to verify their articles. Article owners can click the email
links to open the article editor and manually set the articles to verified, removing them
from the Needs verification list and terminating the email notification for that
article.

Important: Once articles are unverified, they
remain in the Needs verification list and are listed in email notifications to article
owners until they are verified, regardless of whether the rule that put them there is
changed or deleted.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-artverif-needs-verif.jpg)

### Performing a one-time verification using bulk actions

You can use article verification to initiate a one-time review of your
knowledge base content. For example, you might be moving to a new brand name, in which
case you would want to review and revise your articles to reflect the new brand.

To perform a one-time review, you can select the articles you want to unverify from
the articles list, then [use the bulk actions menu](https://support.zendesk.com/hc/en-us/articles/4408836336154) to set those articles to
“unverified.” If there are any articles that you know are already current, you can use
this same process to set those articles to “verified.”

[View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/One-time-verif-bulk-actions.jpg)
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/One-time-verif-bulk-actions.jpg)

### Performing ongoing verification using rules

Knowledge admins can [create article verification rules](setting-reminders-to-review-and-verify-articles.md) to send
reminders when articles need to be reviewed and verified, based on defined criteria and
frequency. This helps ensure that your content doesn’t become inaccurate or out of date.
For example, every three months you might want to review articles that have a specific
label, appear in a certain category, or haven’t been updated in a while. You can create up
to 20 verification rules.

You can use the Article verification page to create article verification rules.
When you add a new rule, you select the

- Frequency at which you want to verify articles (for example 2 weeks, 6
  months, or 1 year).
- Filters that you want to apply when selecting articles for verification (for
  example, only articles within a specific brand or hierarchy).

When you save an article verification rule, the rule runs weekly, setting to
unverified any articles that meet the defined filter criteria and were not verified within
the frequency set by the rule. For example, if the frequency is set to verify articles
every six months, the rule will look for articles that meet the filter criteria and have
not been verified during the prior six-month period.

[View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/PerformingVerifUsingRules.jpg)
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/PerformingVerifUsingRules.jpg)

## About article verification emails

On Mondays and Wednesdays at 00:00 UTC, Zendesk sends article verification
reminder emails to article owners who have unverified articles on the Needs verification
list. If the system cannot find a valid email for an article owner, it will not send the
email, even if there are unverified articles still assigned to that owner. If the owner has
left the company, you should [change the owner](https://support.zendesk.com/hc/en-us/articles/4408832308506) to a valid agent.

This email lists all articles owned by the recipient that require verification
and asks them to verify those articles. If you have a help center with more than one brand,
this email contains all unverified articles that you own across all brands in your account.

Article owners can click an article link to go to the article settings for that article,
where they can [verify the article](https://support.zendesk.com/hc/en-us/articles/4408822044186-Verifying-your-articles). Once the article is verified, it
will no longer be listed in the next article verification email.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-artverif-email.jpg)

Article verification emails are sent until the article owner no longer owns
articles that require verification. Even if the rule that generated the unverified article
status no longer exists, the article remains in the unverified status and consequently
appears on bi-weekly article verification emails until the article owner verifies it.

You cannot change the schedule for the verification emails, nor can you cancel
them. To stop receiving the emails, you must verify the listed articles.

Note: When you downgrade article owners from agents to end users, you must
also reassign their article ownership. Failure to reassign article ownership means the
agents who've been downgraded to end users will still receive article verification emails
for those articles.

## Verifying articles for agents and admins

The process for verifying articles is different for Knowledge admins and
agents. If you are a Knowledge admin, you can verify articles, either individually or in
bulk, from the Needs verification list.

If you are an agent, you must verify
articles that you have permission to publish from within article settings. For more
information, see [Verifying articles that need review](https://support.zendesk.com/hc/en-us/articles/4408822044186).

## Article verification FAQs

Refer to the following frequently asked questions to understand how article
verification works in various use cases.

**What happens if the owner of an unverified article leaves the company?**

If the article owner leaves the company and their email address is no longer
valid, the article remains on the Needs verification list, but the reminder email will no
longer be sent. To resolve this issue, you can [change the owner](https://support.zendesk.com/hc/en-us/articles/4408832308506) of the article to a valid agent.

**What happens to unverified articles when article verification rules are
changed or deleted?**

When article verification rules are changed or deleted, any articles that were
previously unverified will remain so unless they are manually verified. This means that
article owners will continue to receive reminder emails until they verify the article, even
if the rule no longer applies.

**What happens when I update the filters for an article verification
rule?**

Changing the article verification rule filter to include additional or fewer
articles does not affect any articles currently in an unverified state. Unverified articles
remain unverified until they are manually verified by article owners, agents with permission
to publish, or Knowledge admins.

The next time the rule runs (rules run weekly), it will use the new filter to
include or exclude articles for verification. All articles that meet the new criteria will
be assessed against the verification frequency set by the rule, and if they require review,
will be unverified at the appropriate time and added to the Needs verification list.

**Do I have to use an article verification rule?**

You do not need to use article verification rules to implement an article
verification strategy. See [Performing a
one-time verification using bulk actions](#topic_fz3_s4c_dxb) earlier in this article.

**How do I stop receiving article verification emails?**

If you are receiving article verification reminder emails, that means that one or
more articles that you own require review and verification. One way to stop receiving these
emails is to click the article link within the email and verify the article. If you no
longer own these articles, you can also [change the owner](https://support.zendesk.com/hc/en-us/articles/4408832308506)  of the article to redirect the emails to the
current owner.

**If an article is translated, does every translation need to be
verified?**

No, article verifications apply only to the default article language. For
example, if an unverified article with a default language of English is also translated into
German and French translations, you can verify only the English version.

You can establish a process by which you manually track translations for each
article, and then only verify the article once you ensure that all translations are current
as well. However, this is a manual process and is not managed by the article verification
process.

**Who receives verification emails if the article owner is a group?**

If a group is set as the article owner, then article verification emails will go to all
members of that group.

**What's the difference between "updated date" and "last edited date" when using filters
to create verification rules?**

When you create verification rules, the filter is based on "updated" date, while the column
in the result is the "last edited date." The term "edited" indicates that a change was made
to the title or body of an article, whereas the term "updated" can mean multiple things. For
example, an article is marked as "updated" when it's moved to a new section. Articles are
also marked as "updated" when they've been verified. For this reason, articles marked as
"updated" due to verification won't appear in any of the lists for articles updated over six
months ago.
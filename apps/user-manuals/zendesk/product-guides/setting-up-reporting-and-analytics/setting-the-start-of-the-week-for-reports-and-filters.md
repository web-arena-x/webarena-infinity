# Setting the start of the week for reports and filters

Source: https://support.zendesk.com/hc/en-us/articles/4418307079322-Setting-the-start-of-the-week-for-reports-and-filters

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In Explore, you can decide which day of the week should be considered the start of the
week when it comes to the reports you build and the filters you use. The ability to set
a custom start of week gives you more flexibility in weekly reporting.

This article contains the following topics:

- [Understanding the default start of
  week](#topic_zgf_mym_htb)
- [Setting a custom start of
  week](#topic_fcw_nym_htb)
- [Understanding how the start of week
  affects week numbers](#topic_ibw_tym_htb)

Related articles:

- [Setting default chart colors and export
  settings](https://support.zendesk.com/hc/en-us/articles/6456984924442)

## Understanding the default start of week

By default, a user’s profile locale (set in the **Language** field in the user’s
profile in Zendesk Support) determines which day is considered the start of the
week. For example, if the user’s locale is English (United States), then the start
of the week in reports and filters is Sunday. If the user’s locale is English
(United Kingdom), then the start of the week is Monday.

The table below shows a full list of locales and their corresponding start of week
days.

Table 1. Locales and their first day of the week

|  |  |
| --- | --- |
| Arabic | SUNDAY |
| Bulgarian | MONDAY |
| Chinese (Simplified) | SUNDAY |
| Chinese (Traditional) | SUNDAY |
| Czech | MONDAY |
| Danish | MONDAY |
| Dutch | MONDAY |
| English (Canada) | SUNDAY |
| English (United Kingdom) | MONDAY |
| English (United States) | SUNDAY |
| Finnish | MONDAY |
| French | MONDAY |
| French (Canada) | SUNDAY |
| German | MONDAY |
| Greek | MONDAY |
| Hebrew | MONDAY |
| Hindi | MONDAY |
| Hungarian | MONDAY |
| Indonesian | SUNDAY |
| Italian | MONDAY |
| Japanese | SUNDAY |
| Korean | MONDAY |
| Norwegian | MONDAY |
| Polish | MONDAY |
| Português (Portugal) | MONDAY |
| Portuguese (Brazil) | SUNDAY |
| Romanian | MONDAY |
| Russian | MONDAY |
| Spanish | MONDAY |
| Spanish (Latin America) | MONDAY |
| Spanish (Spain) | MONDAY |
| Swedish | SUNDAY |
| Thai | SUNDAY |
| Turkish | MONDAY |
| Ukrainian | MONDAY |
| Vietnamese | SUNDAY |

## Setting a custom start of week

If this default behavior doesn’t suit your needs, Explore administrators can set an
account-wide start of the week. It can be any day of the week, and it will be
applied to all users on your account.

The screenshot below shows a report in an account where the start of the week has
been set to Tuesday.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_custom_start_week_report.png)

**To change the start of the week**

1. In Explore, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) in the left sidebar.
2. Select the **Formatting** tab.
3. Under **Start of the week**, select the day of the week that should be
   considered the first day of the week in reports and filters. Or, select **Based
   on user’s language** to use the [default start of the week based on the user’s
   profile locale](https://support.zendesk.com/hc/en-us/articles/4418307079322#topic_zgf_mym_htb).
4. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_setting_start_of_week.png)

When this setting is updated, it is automatically applied to reports in your account,
but not to dashboard filters. To apply the custom start of the week to dashboard
filters, you’ll need to [re-publish your dashboards](https://support.zendesk.com/hc/en-us/articles/4408827282714-Sharing-dashboards#topic_t2g_pbn_w2b).

Additionally, this setting has no effect on prebuilt dashboards. However, it does
affect copies of the prebuilt dashboards that you've made.

## Understanding how the start of week affects week numbers

Setting a custom start of week affects how Explore calculates the week numbers for
the year. When you set a custom start of week, week 1 always includes the fourth day
of the week. For example:

| Start of week | Week 1 |
| --- | --- |
| Sunday | The week with the first Wednesday of the year |
| Thursday | The week with the first Sunday of the year |
| Saturday | The week with the first Tuesday of the year |

This affects **Week of year** attributes (for example, **Tickets created - Week
of year**).
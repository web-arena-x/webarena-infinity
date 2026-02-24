# Setting up Google Analytics and third-party analytics for your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408828643098-Setting-up-Google-Analytics-and-third-party-analytics-for-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can implement Google Analytics and third-party analytics on your help center
to gain data-driven insights that help you enhance your help center and
content.

Laws in certain jurisdictions (for example, the European Union ePrivacy Directive
or the California Consumer Privacy Act) may require that end users be given
the opportunity to opt-out of Google Analytics or other third-party
tracking, including through the use of a universal opt-out mechanism such as
Global Privacy Control (GPC). For more information on ways to comply with
these requirements, see [Implementing cookie consent in your
help center](https://support.zendesk.com/hc/en-us/articles/4408834944154).

Important: If
you need to use a consent banner to inform users about cookies or
other tracking technologies, you must implement your third-party
analytics in your theme. See [Selecting analytics for cookie
consent](#topic_dkh_kvq_tgc).

This article covers the following topics:

- [Selecting analytics for cookie consent](#topic_dkh_kvq_tgc)
- [Adding Google Analytics or other third-party analytics to your help center](#topic_mt2_dvq_3wb)
- [Using the Google Analytics integration built-in to Zendesk to track help center traffic](#topic_xmc_png_hwb)

## Selecting analytics for cookie consent

When selecting the analytics service that's right for your help center,
consider whether you need to use a consent banner to inform users
about cookies or other tracking technologies. Use only one of the
following options to prevent duplication of analytics:

- **If you require cookie consent**: If you operate in
  jurisdictions where you need to obtain [cookie
  consent](https://support.zendesk.com/hc/en-us/articles/4408834944154) to fully comply with regulations
  such as the European Union ePrivacy Directive or the
  California Consumer Privacy Act, you should
  implement your analytics as described in [Adding Google Analytics or other third-party analytics to your help center](#topic_mt2_dvq_3wb).
- **If you don't require cookie consent**: If you don't
  plan to use a consent banner, you can use the
  Zendesk built-in Google Analytics integration
  described in [Using the Google Analytics integration built-in to Zendesk to track help center traffic](#topic_xmc_png_hwb).

## Adding Google Analytics or other third-party analytics to your help center

If you operate in jurisdictions where you need to obtain [cookie consent](https://support.zendesk.com/hc/en-us/articles/4408834944154) to
fully comply with regulations such as the European Union ePrivacy
Directive or the California Consumer Privacy Act, you can't use the
built-in Google Analytics option. Instead, use this option to add
tracking code for Google Analytics or other third-party analytics
via the theme code. This ensures that cookies only load after
consent is granted.

If the Zendesk built-in Google Analytics integration is enabled, disable
it before adding a third-party consent service to ensure that
cookies only load after consent is granted.

Adding third-party analytics via the theme code is available only if you
are on Suite Growth or higher or have Support with Guide. Once you
add code to your theme, it will be converted to a [custom theme](https://support.zendesk.com/hc/en-us/articles/4408821255834), if its
not already a custom theme.

**To add third-party tracking code to your theme**

- Follow the instructions provided by your analytics
  service for implementing their analytics.

  Most of
  the time, you'll be instructed to paste the tracking
  code snippet into the [document\_head.hbs
  theme template file](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_tvr_f2l_3yb). You can also use
  Google Tag Manager to implement your analytics
  tags see [Using Google Tag
  Manager with your help center](using-google-tag-manager-with-your-help-center.md).

## Using the Google Analytics integration built-in to Zendesk to track help center traffic

If you do not need to obtain cookie consent, you can use the [Google Analytics](http://www.google.com/analytics/) integration
built-in to Zendesk to track your help center traffic. This option
is only for using Google Analytics without a cookie consent tool.
Google Analytics is a third-party, non-Zendesk service. If you need
to obtain cookie consent, see [Adding Google Analytics or other third-party analytics to your help center](#topic_mt2_dvq_3wb).

Before you begin to track traffic using Google Analytics,
establish a Google Analytics account (if you don’t already have
one), then add your help center to that account. For instructions on
each of these tasks, refer to [Google’s support
documentation](https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319).

To use Google Analytics to track your help center traffic, you must set
up your Google Analytics account and then add your Google Analytics
tracking ID to the help center.

**To add your tracking ID to the help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Under **Integrations**, select the option to enable
   Google Analytics and enter your tracking ID.
3. Click **Update** on the upper-right side of the
   page.

Note: For more detailed
information about how to set up GA4 to track your help center
traffic, you can refer to external content such as the article on
[How to set up and use Zendesk
Guide with Google Analytics 4](https://www.swifteq.com/post/zendesk-guide-google-analytics-4) by [Swifteq](https://www.zendesk.com/marketplace/partners/3363/swifteq-ltd/).
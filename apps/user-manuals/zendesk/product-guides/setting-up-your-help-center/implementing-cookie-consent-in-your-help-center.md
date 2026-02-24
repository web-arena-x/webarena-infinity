# Implementing cookie consent in your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408834944154-Implementing-cookie-consent-in-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Laws in certain jurisdictions (for example, the European Union ePrivacy Directive or the California Consumer Privacy Act) may require that you obtain user consent for cookies or allow users to opt-out of cookies on your sites. For example, if you're using a third-party analytics service like Google Analytics cookies in your help center, or if you have [enabled anonymous user tracking](https://support.zendesk.com/hc/en-us/articles/6297027870618), you may be required to allow users to opt-out of those cookies, including through the use of a universal opt-out mechanism.

This article covers the following topics:

- [Setting up a third-party cookie consent service](#topic_ohf_lxw_wwb)
- [Universal opt-outs with Global Privacy Control (GPC)](#topic_qqy_mxw_wwb)

## Setting up a third-party cookie consent service

Important: Before beginning this procedure, verify that you're not using the built-in Google Analytics integration. If the Zendesk built-in Google Analytics integration is enabled, disable it, then add a third-party consent service to ensure that cookies only load after consent is granted. See [Setting up analytics for your help center](https://support.zendesk.com/hc/en-us/articles/4408828643098).

To enable your users to set their own cookie preferences, you must use a third-party cookie consent service (CCS) to apply cookie consent options on your help center. If end users choose to block cookies, they may have a degraded user experience.

If you're using a theme from the Theme Marketplace, it must have a Developer license unless the theme is prepared for cookie consent services. For more information about theming, see [Using help center themes from the Zendesk Marketplace](https://support.zendesk.com/hc/en-us/articles/4408842911898).

Note: Zendesk does not accept any liability for your use of any CCS. Your use of such non-Zendesk services is subject to the terms, conditions and functionality of the CCS provider.

**To set up a third-party cookie consent service**

Note: This procedure assumes you are using the theme editor within your help center. If you are using your own development tools to edit your theme locally, skip steps 2-4 and refer to [Working on a theme locally](https://support.zendesk.com/hc/en-us/articles/4408838187802#topic_bvz_rvc_xlb) for how to access and edit your theme code.

1. Choose a third-party cookie consent management platform, such as [Cookiebot](https://www.cookiebot.com/en/), [TrustArc](https://trustarc.com/cookie-consent-manager/), or [OneTrust](https://www.onetrust.com/products/cookie-compliance/) and follow their instructions.
2. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
3. On the Themes page, click **Customize** on the theme you want to add the cookie consent option to.
4. Click **Edit code**.
5. Follow the instructions of the CCS and implement the Javascript snippets they provided.

   Instructions may vary between services. Generally, you must add the code within the `head` tag. You do that by adding the additional JavaScript snippets provided by a third-party cookie consent management platform to the [document\_head.hbs](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_h5c_k4w_n3) template.
   This template contains anything within the `head` tag.

   If you have one or more analytics snippets in the [document\_head.hbs](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_h5c_k4w_n3) (such as Google Analytics), you should add your cookie consent snippet above the analytics snippets.
6. Using the instructions of the CCS, configure the code to control all Guide cookies, and local storage that is not listed as "Strictly necessary" on the Zendesk cookie list.

## Universal opt-outs with Global Privacy Control (GPC)

Global Privacy Control (GPC) is a browser setting that notifies websites of a user's privacy preferences, including with respect to third-party cookies, by sending a signal to each website a user visits. Unlike cookie consent, a user’s GPC signal applies across different websites. Some laws require website operators to respect GPC signals, even when they might conflict with a user’s cookie consent on a particular website.

Often, CCS providers also offer GPC tools to allow you to respect GPC signals.
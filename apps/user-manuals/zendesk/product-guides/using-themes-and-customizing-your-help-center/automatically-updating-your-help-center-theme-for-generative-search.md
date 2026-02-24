# Automatically updating your help center theme for generative search

Source: https://support.zendesk.com/hc/en-us/articles/9809445946778-Automatically-updating-your-help-center-theme-for-generative-search

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Generative search is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408845834522) released after March 26, 2025. If your help center uses a customized theme and does not have the {{generative\_answers}} helper implemented, you must update your custom theme to add the {{generative\_answers}} helper.

This article contains the following sections:

- [Determining eligibility](#topic_lg1_vcj_xgc)
- [Updating your help center theme with the {{generative\_answers}} helper](#topic_jvt_vcj_xgc)

## Determining eligibility

Eligible accounts can use the theme updater described in this article to automatically update their theme with the generative search helper. Eligibility is determined based on your current theme implementation and other factors.

If you're eligible for this feature, you'll find links to the updater in the following areas:

- From the onboarding message that appears in Knowledge admin > Manage articles > All articles

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/knw-theme-updater-modal.png)
- From the error message that appears in Knowledge admin > Settings >
 Search settings > Quick answers (Manage).

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/KNW-themeupdt-setup2.png)

If you're not eligible for the theme updater, you can [edit your theme to add generative search results](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_tjl_xqc_42c)to your custom theme.

## Updating your help center theme with the {{generative\_answers}} helper

You can use the theme updater to insert the {{generative\_answers}} helper in the code of your live theme.

After the theme update is complete, it will be automatically published to your help center. If you don't want to use generative search, you can [change your search settings](https://support.zendesk.com/hc/en-us/articles/5589418656922) to disable the feature in your help center.

**To update your theme**

1. Open the theme updater from the message that appears to eligible users in one of the following locations:
   - In the message that appears in **Knowledge admin > Manage articles
     > All articles**, Click **Set up quick answers**.
   - In the message that appears in **Knowledge admin > Settings >
     Search settings > Quick answers (Manage)**, click **Theme updater**.

   The theme update begins and displays a status message while the update is ongoing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-theme-update-in-progress.png)

   The theme is automatically published and a preview is displayed in the theme preview page.
2. Review the preview displayed in the theme preview page.

   This view shows you what users will see when they perform help center searches with generative search. You can test quick answers with your own queries to see how quick answers will appear to end users before moving on to the next step.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-theme-gensearch-preview-theme.png)
3. If you:
   - **Want to use generative search** in your help center as shown, no further action is required.
   - **Don't want to show generative search results** in your help center, you can click the Quick answers settings page link in the onboarding message to go to the [search settings page](https://support.zendesk.com/hc/en-us/articles/5589418656922) and turn off generative search.
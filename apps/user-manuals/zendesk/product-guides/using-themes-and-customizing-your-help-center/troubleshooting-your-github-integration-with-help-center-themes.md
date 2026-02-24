# Troubleshooting your Github integration with help center themes

Source: https://support.zendesk.com/hc/en-us/articles/4408829072538-Troubleshooting-your-Github-integration-with-help-center-themes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

This article covers error messages for the [GitHub integration for help center themes](https://support.zendesk.com/hc/en-us/articles/4408832476698) and troubleshooting steps to take when you encounter issues adding or updating a theme.

You must be a Guide admin to manage the GitHub integration.

This article covers the following topics:

- [Failed to import theme](#topic_uld_mxg_nhb)
- [Failed to update theme](#topic_ovg_mxg_nhb)
- [Make sure you have access to the repository](#topic_hgj_mxg_nhb)
- [Make sure the Zendesk Guide app is authorized](#topic_nvj_mxg_nhb)
- [Incorrect theme version number](#topic_et1_mxg_nhb)
- [Theme version number is not allowed](#topic_ygx_kxg_nhb)
- [Cannot authorize using Internet Explorer](#topic_y12_kxg_nhb)

## **Failed to import theme**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/github_failed_import.png)

- Make sure you have written the GitHub repository URL or [username]/[repository] correctly. Preferably copy and paste the repository URL from the address bar when viewing the repository.
- If you are fetching from a specific branch, make sure you have written the branch name correctly.
- [Make sure you have access to the repository](#topic_hgj_mxg_nhb)
- [Make sure the Zendesk Guide app is authorized](#topic_nvj_mxg_nhb)

## **Failed to update theme**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/github_failed_update.png)

- [Make sure you have access to the repository](#topic_hgj_mxg_nhb)
- [Make sure the Zendesk Guide app is authorized](#topic_nvj_mxg_nhb)

## **Make sure you have access to the repository**

Make sure you have access to the repository by going to <https://github.com/settings/repositories>. If you don’t see the repository it is either because your access has been revoked or the repo is deleted. Contact the administrator of the repo to find out

- If your access has been revoked you will need the repo admin to give you access again.
- If the repo has been deleted you cannot update the theme or connect it to another repo, but will have to initiate a new import from a repo that exists.

## **Make sure the Zendesk Guide app is authorized**

Make sure the Zendesk Guide app is authorized for your account in GitHub. Go to <https://github.com/settings/applications> and check that the Zendesk Guide app has access to your account in the “Authorized OAuth Apps” tab.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/github_not_authorized.png)

If the Zendesk Guide app does not appear Authorized OAuth Apps, if might be because:

- The authorization for the Zendesk Guide GitHub app has been revoked and you need to re-authorize it. You can do this by trying to update your theme again or if that does not work try adding the theme as a new theme and then try and update the theme you were trying to update.
- The GitHub organization that owns the repository does not allow authorization of the Zendesk Guide app. In that case you should contact the admin of the GitHub organization to allow authorization of the Zendesk Guide app for the [‘repo’ scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). Since this is the only scope GitHub provides that gives access to the code in a repo, there is no option for allowing a smaller scope.

## **Incorrect theme version number**

The themes version number in the manifest.json file needs to be incremented as it is conflicting with the current version number. Increment the themes version number or ask the theme developer to do so.

## **Theme version number is not allowed**

The themes version number in the manifest.json file does not comply with the [versioning convention](https://support.zendesk.com/hc/en-us/articles/4408846524954-Customizing-the-Settings-panel-Guide-Professional-and-Enterprise-#manifest-object). Have the theme developer correct the themes version number to follow the versioning convention.

## **Cannot authorize using Internet Explorer**

You cannot authenticate using Internet Explorer because GitHub no longer supports it, however, you can authenticate using another GitHub and Zendesk supported browser, such as Google Chrome, Firefox or Safari.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/github_not_ie.png)
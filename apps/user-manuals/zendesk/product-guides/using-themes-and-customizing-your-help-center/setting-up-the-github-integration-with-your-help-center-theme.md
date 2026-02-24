# Setting up the GitHub integration with your help center theme 

Source: https://support.zendesk.com/hc/en-us/articles/4408832476698-Setting-up-the-GitHub-integration-with-your-help-center-theme

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Integrate your help center theme with GitHub to collaborate on theme development and manage it in one place. Prepare your theme in GitHub, ensuring it meets requirements like having a manifest file at the root. Set up the integration in Knowledge admin by importing the theme from GitHub. Manage updates in GitHub and publish them when ready.

Location:  Knowledge admin > Customize design (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) > Add theme > Add from GitHub

The GitHub integration enables you to develop and maintain a theme collaboratively in GitHub,
then preview or publish it in Knowledge admin. To set up the integration, make sure your theme
is stored in GitHub, then set up the integration in Knowledge admin.

Note: The GitHub integration with Help Center does not support GitHub Enterprise Server, but
it does support GitHub Enterprise Cloud. If you use GitHub Enterprise Server you can
alternatively use the [Guide theming API](https://developer.zendesk.com/rest_api/docs/help_center/theming).

You must be a Knowledge admin to set up the GitHub integration.

This article covers the following topics:

- [Preparing your theme in GitHub](#topic_i3v_kyk_chb)
- [Setting up the integration](#topic_vnf_lyk_chb)

## Preparing your theme in GitHub

You need to ensure that your theme is in GitHub before you set up the integration in
Knowledge admin. If you're new to Git and GitHub, check out [this tutorial](https://www.dataquest.io/blog/tutorial-introduction-learn-git-github). If your theme is already in GitHub, and it meets
the following requirements, see [Setting up the
integration](#topic_vnf_lyk_chb).

The integration has the following requirements for your GitHub repo:

- **The manifest file must be at the root of the GitHub repo**

  The file
  manifest.json should be placed at the root of your GitHub repository to be able to add
  your theme. You can still include extra files, such as tooling, which are ignored when
  importing to Knowledge admin.
- **The GitHub repo can have only one theme**

  You should only manage one theme in
  each repository. You can use the branch option during theme import to try out
  variations of your theme.

**To get your theme into a GitHub repo**

- **If you do not currently have a theme**, fork the [Copenhagen theme repo](https://github.com/zendesk/copenhagen_theme) and start building your theme. This enables you to easily
  port improvements from the Copenhagen theme to your theme in the future.
- **If your theme is in Knowledge admin**, [download your theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_udw_zdc_hbb), then create a GitHub repo (if
  you don't already have one), and push your theme to the GitHub repo.
- **If your theme is not in Knowledge admin or GitHub**, create a GitHub repo (if you
  don't already have one), and push your theme to the GitHub repo.

After you've prepared your theme in GitHub, you are ready to [set up the integration](#topic_vnf_lyk_chb).

## Setting up the integration

To set up the GitHub integration you need to make sure your theme is stored in GitHub, then
fetch your theme from GitHub to Knowledge admin. This one-time fetch establishes the
connection between your theme and GitHub.

After you set up the integration, you will work on the theme in GitHub, then update the
theme in Knowledge admin when you're ready. You can then preview or
publish the theme live in Knowledge admin.

**To set up the GitHub integration with your help center theme**

1. In GitHub, ensure that you have [prepared
   your theme](#topic_i3v_kyk_chb).
2. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   The Themes page opens.
3. Click **Add theme** in the upper-right corner.
4. Click **Add from GitHub**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theme_add_new.png)
5. Enter the URL for the repo and, optionally, enter a branch name if you want to fetch
   from a branch other than the default branch, then click **Import**.
6. Log in to GitHub if prompted, then click **Authorize Zendesk**.

The theme thumbnail appears on the Themes page when the import is complete. If you have
problems, see [Troubleshooting the GitHub integration for help center
themes](https://support.zendesk.com/hc/en-us/articles/4408829072538).

After you've established the connection, you will manage your theme in GitHub and [update the theme in Knowledge admin](https://support.zendesk.com/hc/en-us/articles/4408844123162) as needed.
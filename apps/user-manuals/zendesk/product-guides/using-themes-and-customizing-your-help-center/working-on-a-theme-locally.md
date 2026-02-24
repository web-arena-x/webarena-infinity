# Working on a theme locally

Source: https://support.zendesk.com/hc/en-us/articles/4408838187802-Working-on-a-theme-locally

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The most powerful help center theming features are the abilities to import, download, and work
locally with themes. When you’re making major updates to a theme or building your own theme
from scratch, these options enable a streamlined workflow for developers.

The workflow to build a new theme or update an existing theme locally is as follows:

1. [Starting a new theme](#topic_dzr_mvc_xlb) by adding the Copenhagen theme or
   duplicating an existing theme.
2. [Downloading your theme](#topic_z52_rvc_xlb) to work offline.
3. [Editing your theme locally](#topic_bvz_rvc_xlb) locally with your own development
   tools.
4. [Importing your theme](#topic_byb_svc_xlb) back into Knowledge admin.
5. [Publishing your new theme](#topic_qwc_svc_xlb).
6. [Making additional updates](#topic_klt_pzc_xlb).

## Starting a new theme

If you’re building a brand new theme from scratch, consider starting from a new version of
the standard Copenhagen theme. To do so, you add a new theme and a fresh copy of the
Copenhagen theme is added to your Themes page. You can also get a fresh version of the theme
from the open-source [Copenhagen repository](https://github.com/zendesk/copenhagen_theme) on GitHub.

Many people like to start with an existing theme and make major modifications to create
their own theme. If you’re revamping an existing theme and want to keep some of the existing
styles, you can duplicate the theme.

To start a new theme by adding a fresh copy of Copenhagen or by copying an existing theme,
see [Adding a help center theme](https://support.zendesk.com/hc/en-us/articles/4408821790618).

## Downloading your theme

Now you're ready to download your theme from Knowledge admin. A theme is downloaded as a
zip archive of templates, JavaScript, CSS, and assets. This enables you to work on the theme
outside of Knowledge admin, using your own development tools.

To download your theme, see [Downloading a help center theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_udw_zdc_hbb).

## Editing your theme locally

Now you’re ready to start working on your local machine, using your own development tools.

To avoid zipping and importing the files into Knowledge admin every time you want to
preview your changes, you can preview changes locally in a web browser. To set up local
theme previewing, see [Previewing theme changes locally](https://support.zendesk.com/hc/en-us/articles/4408822095642).

Once set up, you can preview changes locally by saving the files you're working on. The
theme reloads automatically in the browser. This lets you work iteratively, making changes
to templates, CSS, JavaScript, and assets, and then previewing the results of your work.

Additionally, when you download a theme to your local machine, it's a good idea to check it
into your favorite version control repository, such as git, mercurial, or SVN.

Your team can also develop and maintain the theme collaboratively using GitHub, then
preview or publish it in Knowledge admin from GitHub. See [Setting up the GitHub integration with your help center theme](https://support.zendesk.com/hc/en-us/articles/4408832476698).

## Importing your theme

After you’ve built out the theme locally, compress the theme directory into a ZIP archive
and import it into Knowledge admin by dragging and dropping the file on the Themes page or
by using the import option.

This will import the theme as a new custom theme. You can preview it further in Knowledge
admin, and other users in your organization will also be able to see the theme.

To import your theme, see [Importing a help center theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_jpd_zdc_hbb).

If you set up an [integration with GitHub](https://support.zendesk.com/hc/en-us/articles/4408832476698), you can update a theme in
Knowledge admin from GitHub. You don't need to create a separate ZIP archive and import it.
See [Updating your GitHub-managed theme in Knowledge admin](https://support.zendesk.com/hc/en-us/articles/4408844123162).

Another option is to build your own integration with the [Themes API](https://developer.zendesk.com/rest_api/docs/help_center/theming) to import and update themes in Knowledge admin. See
[Theme Import Workflow](https://developer.zendesk.com/api-reference/help_center/help-center-api/theming/#theme-import-workflow) and [Theme Update Workflow](https://developer.zendesk.com/api-reference/help_center/help-center-api/theming/#theme-update-workflow) in the Zendesk developer
docs.

## Publishing your new theme

When you're ready to publish your new theme, just click Publish from the theme menu in the
workbench.

## Making additional updates

If you're using version control systems like git or mercurial, continue making changes
locally, not in Knowledge admin. Check in your changes and import the theme into Knowledge
admin again. If you accidently make changes to your theme in Knowledge admin, download the
updated theme and check those changes into your source control system.

Important: If you set up an [integration with GitHub](https://support.zendesk.com/hc/en-us/articles/4408832476698), making any modifications to your theme in
Knowledge admin will break the GitHub integration.
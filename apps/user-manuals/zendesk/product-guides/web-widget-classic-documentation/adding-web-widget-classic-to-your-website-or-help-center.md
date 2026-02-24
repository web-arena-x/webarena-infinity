# Adding Web Widget (Classic) to your website or help center

Source: https://support.zendesk.com/hc/en-us/articles/4408821673242-Adding-Web-Widget-Classic-to-your-website-or-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Channels > Classic > Web Widget

Note: This article applies to accounts using Web Widget (Classic). If you're using the messaging
Web Widget, see [Creating a messaging Web Widget](https://support.zendesk.com/hc/en-us/articles/4409103246874).

Web Widget (Classic) can be added to any page of your website or to your help center,
allowing you to offer support options – help center, contact form, voice, and live chat – to
your customers.

Web Widget (Classic) is fully optimized for the mobile experience and does not affect page
load times. Web Widget (Classic) is presented in the end user’s language, according to the
language setting for end user’s web browser. You can force the widget to always appear in a
specific language (see [Displaying your widget in a different language](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_sty_j2r_gq)).

This article contains the following topics:

- [Adding Web Widget (Classic) to your
  website](#topic_kf2_xcj_vz)
- [Adding Web Widget (Classic) to your help
  center](#topic_a52_wcj_vz)

Related articles:

- [Using Web Widget (Classic) to embed customer service in your
  website](https://support.zendesk.com/hc/en-us/articles/4408836216218)
- [Advanced customization of your Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562)
- [Quickstart - Web Widget JavaScript APIs](https://developer.zendesk.com/documentation/classic-web-widget-sdks/web-widget/quickstart-tutorials/web-widget-javascript-apis)

You cannot use SSO authentication in the Web Widget (Classic) itself. However, you can
restrict access by setting up SSO on your help center, or on the website hosting the widget.
See [Single sign-on options in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226) and [Using restricted help center content with the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843923610).

## Adding Web Widget (Classic) to your website

You can add Web Widget (Classic) to any page of your website. After you add the widget code
to your website, changes are managed in Zendesk Support and with the Advanced Customization
JavaScript APIs, and updates are reflected in the widget wherever it appears.

**To add Web Widget (Classic) to your website**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Installation** tab, if it is not already selected.
3. Under the code box, click the **Copy code** icon.
4. If you want to add the widget to your website, go to the web page where you want to
   add the widget, then paste the code before the closing HTML
   `</body>`
   tag. Add the code to every web page where you want the widget to appear.
5. Make sure your [firewall is configured](https://support.zendesk.com/hc/en-us/articles/4408842860186) to allow the Web Widget (Classic) to
   appear.

If you haven't already, make sure you [configure the components in your widget](https://support.zendesk.com/hc/en-us/articles/4408838063258). For information about
configuring the Web Widget (Classic) using JavaScript APIs, see the [developer docs](https://developer.zendesk.com/embeddables/docs/widget/introduction#content).

If the Web Widget (Classic) does not appear on pages outside your help center, you most
likely have the **Require sign in** option enabled in your Guide security settings (see
[Restricting help center access to signed-in
end-users](https://support.zendesk.com/hc/en-us/articles/4408842656154-Restricting-Help-Center-access-to-signed-in-end-users)).

The Web Widget (Classic) displays help center content that the user is allowed to see. When
**Require sign in** is enabled, and only the **help center** and **Contextual
Help** toggles are on in your Web Widget (Classic) admin settings, the Web Widget
(Classic) will not load for non-authenticated users. If you enabled other options in your
Web Widget (Classic) admin settings, such as **Contact form**, the Web Widget (Classic)
does appear.

## Adding Web Widget (Classic) to your help center

You can add the Web Widget (Classic) to your help center, so that it appears on every page
of your help center.

On some usage plans, you can restrict the pages where the Web Widget (Classic) appears in
your help center by using the Web Widget (Classic) API.

**To add the Web Widget (Classic) to your help center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Installation** tab, if it is not already selected.
3. Select the **Add to help center** checkbox.

   This adds the Web Widget (Classic) to
   every page of your help center. For more information, see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250).

   On some usage plans, you can restrict the pages where
   the Web Widget (Classic) appears in your help center by using the
   `zE.hide()` method of the Web Widget (Classic) API. See [Advanced Customization of your Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562) and [the Web Widget (Classic) API documentation](https://developer.zendesk.com/embeddables/docs/widget/api#ze.hide) for more
   information.
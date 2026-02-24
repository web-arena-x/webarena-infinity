# Using Google Tag Manager with your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408835764122-Using-Google-Tag-Manager-with-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can implement Google Tag Manager for your help center.

This article covers the following topics:

- [About Google Tag Manager](#topic_fgw_fzt_p1b)
- [Implementing Google Tag Manager](#topic_ygv_hzt_p1b)
- [Next steps](#topic_c3s_sc5_p1b)

## About Google Tag Manager

According to Google, "Google Tag Manager is a [tag management system](https://en.wikipedia.org/wiki/Tag_management_system) that allows you to quickly and easily update tags and code snippets on your website or mobile app, such as those intended for traffic analysis and marketing optimization. You can add and update AdWords, Google Analytics, Firebase Analytics, Floodlight, and 3rd party or custom tags from the Tag Manager user interface instead of editing site code."

Google Tag Manager requires you to implement the JavaScript and HTML embed code provided by Google Tag Manager in your help center (see [Sign up for Google Tag Manager](#topic_wkl_3zt_p1b)). From there, it’s able to dynamically embed code snippets into your site. The best part is that you manage the code from the Google Tag Manager interface, rather than implementing custom code in your help center.

## Implementing Google Tag Manager

Follow these steps in the following sections to implement Google Tag Manager for your help center:

- [Sign up for Google Tag Manager](#topic_wkl_3zt_p1b)
- [Add the embed code to your help center](#topic_jkg_5zt_p1b)
- [Create your tag in Google Tag Manager](#topic_ymp_tzt_p1b)
- [View changes in your help center](#topic_hfk_4b5_p1b)

### Sign up for Google Tag Manager

First, you need to sign up for a free Google Tag Manager account.

1. [Sign up](https://www.google.com/analytics/tag-manager/) for Google Tag Manager for free.
2. Set up a new account.

   Be sure to select **Web** as **Where to use** the container.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/GTM1-0822.png)
3. Once your new container is created, copy the two snippets of code to embed in your help center.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/GTM2-0822.png)

### Add the embed code to your help center

Now you'll paste the embed code from Google Tag Manager into two templates in your help center theme.

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.
4. Paste the first snippet in the **Document Head** (document\_head.hbs)
   template.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/GTM3-0822.png)
5. Paste the second snippet in the **Header** (header.hbs) template.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/GTM4-0822.png)
6. Save your changes.

### Create your tag in Google Tag Manager

From here you’ll need to create a tag to test out in your new container. See [Set up and install Tag Manager](https://support.google.com/tagmanager/answer/6103696?hl=en&ref_topic=3441530&sjid=15686348616829092054-NA) in Google Tag Manager Help.

### View changes in your help center

Now you can see the tag you built in your help center. Refresh the preview of your help center to view your new tag.

## Next steps

Now, you’ve configured a container and an example tag from Google Tag Manager and embedded it into your help center.

Google Tag Manager is an incredibly powerful tool for managing analytics and traffic performance tools. Google has put together a lot of resources on use and best practices with Google Tag Manager [here](https://www.google.com/analytics/resources/?topic=tag-management).
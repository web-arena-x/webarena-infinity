# Advanced customization of Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408832257562-Advanced-customization-of-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Channels > Classic > Web Widget

Note: This article applies to accounts using Web Widget (Classic). If you're using the messaging Web Widget, see [Configuring the Web Widget for messaging](https://support.zendesk.com/hc/en-us/articles/4408828655514).

After an administrator [configures the components in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258) and works with their developer to [add Web Widget (Classic) to their website](https://support.zendesk.com/hc/en-us/articles/4408821673242), they can work with their developer to further customize the Web Widget (Classic), if desired.

This article is an overview for administrators about what advanced customizations are possible with the Web Widget (Classic). This article is meant to answer the question, "What else can I do with my Web Widget (Classic)?" It explains the customization process for administrators, and also points to developer documentation that web developers need in order to do the work.

If you’re a web developer (or an administrator who is comfortable doing website development on your own) and are looking for complete documentation about the API settings and commands described in this article, or additional code samples, see [the developer documentation for the Web Widget (Classic) API](https://developer.zendesk.com/api-reference/widget/introduction)
instead.

This article discusses these topics and widget customizations:

- [Planning for Web Widget (Classic)
 customizations](#topic_w1g_yhw_sfb)
- [Displaying the widget in a different language](#topic_sty_j2r_gq)
- [Prefill forms with user contact information](#topic_mnz_pr2_tfb)
- [Disabling ticket attachments](#topic_yms_d5t_gx)
- [Re-positioning the launcher](#topic_nzd_cbq_mx)
- [Offsetting the widget placement](#topic_ozd_cbq_mx)
- [Customizing the color of the widget elements](#topic_pzd_cbq_mx)
- [Changing visible ordering in the widget](#topic_ahz_bbq_mx)
- [Suppressing features on specific pages](#topic_bhz_bbq_mx)
- [Customizing widget text](#topic_chz_bbq_mx)
- [Adding a subject line to the contact form](#topic_gzp_1bq_mx)
- [Hiding the "View Original Article" button](#topic_a3z_1bq_mx)
- [Limiting search results](#topic_usl_bbq_mx)
- [Customizing the help center search placeholder text](#topic_txs_qf1_l1b)
- [Advanced configuration of voice in the Web Widget (Classic)](#topic_ffj_xsy_hdb)
- [Advanced configuration of Chat in the Web Widget (Classic)](#topic_ejs_hcd_tfb)
- [Offering end users multiple contact options](#topic_spt_fb1_l1b)
- [Formatting code for multiple Web Widget (Classic) elements](#topic_y4x_fvz_mx)

For information about adding the Web Widget (Classic) to your site, see [Using Web Widget (Classic) to embed customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218).

For a complete list of Web Widget (Classic) documentation, see [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354).

## Planning for Web Widget (Classic) customizations

Most Support administrators aren’t web developers and work with someone else to implement customizations to the Web Widget (Classic). They don’t customize the Web Widget (Classic)
and websites on their own. They work with a web developer at their company, or an outside developer that they use on a contract basis to implement the changes.

The web developer is the person who does the customization work, and they do it by adding some code (the Web Widget (Classic) API) to the HTML of the website. However, the administrator still has a role to play in the work. They need to understand what customizations are possible for the Web Widget (Classic), and tell the web developer what they want.

Some administrators have experience with HTML and choose to do the customization work themselves, acting as their own developer, and that's fine. Either way, customizing the Web Widget (Classic) is actually a process for the administrator that requires some planning and involves these steps:

1. Review the information in this article to understand what advanced customizations are possible.
2. Meet with key stakeholders at your company to create a list of requirements for your Web Widget (Classic). What colors do want to use? How do you want the Web Widget (Classic) to behave?
3. Prepare a list of the customizations you want. Be as specific as possible and include links to API documentation that your web developer can reference.
4. Give the list to your web developer, who will customize the Web Widget (Classic) by modifying the HTML of your website.

## Displaying the widget in a different language

By default, the Web Widget (Classic) embedded in a website displays text in the end user’s language, based on the language of their browser. For example, if the end user's browser language is set to **de** for German, the widget will appear in German for that user. If the widget is embedded in a help center, it displays text based on the help center language setting.

The Web Widget (Classic) supports a subset of [Zendesk's supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826). If the end user's browser language is not supported by the Web Widget (Classic), the widget defaults to English. If the widget is unable to obtain the language from the end user’s browser, the widget defaults to the language specified in Zendesk Support.

You can customize the widget so that it always appears in a specific language using the [**setLocale**](https://developer.zendesk.com/embeddables/docs/widget/core#setlocale) command. This command sets the language for only the widget and doesn't override your host page’s language.

For more information, see the developer documentation for the [**setLocale**](https://developer.zendesk.com/embeddables/docs/widget/core#setlocale) command.

## Prefill forms with user contact information

You can save visitors to your site a few seconds and some annoyance or frustration by prefilling their name, email address, and phone number into contact forms. This includes ticket forms, pre-chat forms, and chat offline forms. Use the [**identify**](https://developer.zendesk.com/embeddables/docs/widget/core#identify) and [**prefill**](https://developer.zendesk.com/embeddables/docs/widget/core#prefill) settings.

You can also set user information to be read-only using the [**prefill**](https://developer.zendesk.com/embeddables/docs/widget/core#prefill) setting, which is nice because you can avoid having duplicate user accounts in Support for the same person.

For more information, see the developer documentation for the [**identify**](https://developer.zendesk.com/embeddables/docs/widget/core#identify) and [**prefill**](https://developer.zendesk.com/embeddables/docs/widget/core#prefill) settings.

## Disabling ticket attachments

If you have enabled attachments for your tickets, users can attach files to tickets submitted from the Web Widget (Classic), by default. However, you can disable this option, if needed.

For more information, see the developer documentation for the [**attachments**](https://developer.zendesk.com/embeddables/docs/widget/settings#attachments) setting of the [**contactForm**](https://developer.zendesk.com/embeddables/docs/widget/contact_form) object.

## Re-positioning the launcher

The default position for the Web Widget (Classic) is the bottom-right of the browser; when a user clicks on the Web Widget (Classic) launcher, it opens by expanding upward.

You can select a location for the Web Widget (Classic) that varies from page to page (placing it on the left or right side of the page, or moving it to the top of the page where it expands downward when clicked). Use the [**position**](https://developer.zendesk.com/embeddables/docs/widget/settings#position) setting to position the Web Widget (Classic) in the top-left, top-right, bottom-left, or bottom-right of the page.

For more information, see the developer documentation about the [**position**](https://developer.zendesk.com/embeddables/docs/widget/settings#position) setting.

## Offsetting widget placement

You can use the [**offset**](https://developer.zendesk.com/embeddables/docs/widget/settings#offset) setting to reposition the Web Widget (Classic) on your desktop or mobile devices. Use the initial [**position**](https://developer.zendesk.com/embeddables/docs/widget/settings#position) setting as the point of reference, and then use the **[offset](https://developer.zendesk.com/embeddables/docs/widget/settings#offset)** setting to move the Web Widget (Classic) horizontally, vertically, or both from that position (in pixels).

For more information, see the developer documentation for the [**offset**](https://developer.zendesk.com/embeddables/docs/widget/settings#offset) setting.

## Customizing the color of the widget elements

You can specify an overall color scheme for the Web Widget (Classic) (theme color) and a custom color for the text in the launcher, contact button, and header (theme text color)
from the Web Widget (Classic) administration page (see [Configuring components in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258)).

However, if you want to customize specific elements, you need to use the [**color**](https://developer.zendesk.com/embeddables/docs/widget/settings#color) setting. You can choose a unique color for each of these Web Widget (Classic) components:

- Launcher
- Button
- Button text
- Results list
- Header
- Article links

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_elements_1.png)
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_elements_2.png)

For accessibility purposes, the Web Widget (Classic) automatically adjusts colors using an algorithm to guarantee a minimum contrast ratio as specified by the [WCAG guidelines](https://www.w3.org/TR/WCAG20-TECHS/G18.html).

For more information about customizing the color of Web Widget (Classic) elements, see the developer documentation for the [**color**](https://developer.zendesk.com/embeddables/docs/widget/settings#color) setting.

## Changing visible ordering in the widget

You can use the [**zIndex**](https://developer.zendesk.com/embeddables/docs/widget/settings#zindex) setting, one of the core Web Widget (Classic)
settings, to set a new value and change how the Web Widget (Classic) appears in comparison to other elements appearing in the same location on your site.

For more information, see the developer documentation for the [**zIndex**](https://developer.zendesk.com/embeddables/docs/widget/settings#zindex) setting.

## Suppressing widget features on specific pages

You can enable the contact form, chat, voice, and help center in the Web Widget (Classic)
and then use the [**suppress**](https://developer.zendesk.com/embeddables/docs/widget/settings#suppress) setting to change the features offered on particular pages of your site to suit your needs.

For example, you can use [**suppress**](https://developer.zendesk.com/embeddables/docs/widget/settings#suppress) to:

- Have help center deflection on some pages
- Have chat or the contact form without deflection on other pages
- Offer tiered service levels to signed in and identified users

For more information, see the developer documentation for the [**suppress**](https://developer.zendesk.com/embeddables/docs/widget/settings#suppress) setting.

## Customizing widget text

You can change the text of the Web Widget (Classic) components in the table below, and you can also customize the [help center search placeholder text](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_txs_qf1_l1b).

| Component | Details |
| --- | --- |
| | **Object:** [launcher](https://developer.zendesk.com/embeddables/docs/widget/core#launcher-settings) **Setting:** [chatLabel](https://developer.zendesk.com/embeddables/docs/widget/settings#chatlabel) **Description:** Text on the launcher button when chat is enabled and help center is not on **Default text:** **Chat** |
| | **Object:** [launcher](https://developer.zendesk.com/embeddables/docs/widget/core#launcher-settings) **Setting:** [label](https://developer.zendesk.com/embeddables/docs/widget/settings#label) **Description:** Text on the launcher button **Default text:** **Help**, **Support** or **Feedback**, defined on the Web Widget (Classic) Admin page |
| | **Object:** [helpCenter](https://developer.zendesk.com/embeddables/docs/widget/help_center) **Setting:** [title](https://developer.zendesk.com/embeddables/docs/widget/settings#title) **Description:** The title of the help center page **Default text:** **Help** |
| | **Object:** [contactForm](https://developer.zendesk.com/embeddables/docs/widget/contact_form) **Setting:** [title](https://developer.zendesk.com/embeddables/docs/widget/settings#title) **Description:** Title of the contact form **Default text:** **Leave us a message** or **Contact us** defined on the Web Widget (Classic) Admin page |
| | **Object:** [helpCenter](https://developer.zendesk.com/embeddables/docs/widget/help_center) **Setting:** [messageButton](https://developer.zendesk.com/embeddables/docs/widget/settings#messagebutton) **Description:** Text on the button in the help center form that loads the Contact form (~20 character limit) **Default text:** **Leave us a message** or **Contact us** defined on the Web Widget (Classic) Admin page |
| | **Object:** [helpCenter](https://developer.zendesk.com/embeddables/docs/widget/help_center) **Setting:** [chatButton](https://developer.zendesk.com/embeddables/docs/widget/settings#chatbutton) **Description:** Text on the button shown in the help center form that loads the chat (~20 character limit) **Default text:** **Help**, **Support**, or **Feedback** defined on the Web Widget (Classic) Admin page |

You use the **translations** object to change some of the default text displayed in the Web Widget (Classic). Translations are grouped by feature—for example, Launcher, help center, and Contact Form.

Note: If you specify the wildcard character (\*) for the locale name, the string is applied to all locales.

You can explore a list of potential language codes in [Language codes for Zendesk supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826).

The locale translations are triggered by the end user's browser language. You can also force the widget to always appear in a specific language and override the end user's browser language setting. For more information, see [Displaying your widget in a different language](#topic_sty_j2r_gq).

## Adding a subject line to the contact form

With the [**subject**](https://developer.zendesk.com/embeddables/docs/widget/settings#subject) setting on the [**contactForm**](https://developer.zendesk.com/embeddables/docs/widget/contact_form) object, you can set the Web Widget (Classic) to include a subject field in the default contact form.

The default contact form is designed to promote engagement and offer a streamlined user experience when completing the contact form. While the default contact form does not include a subject line, you may want to add one to enhance the support experience for some customers.

For more information, see the developer documentation for the [**subject**](https://developer.zendesk.com/embeddables/docs/widget/settings#subject) setting on the [**contactForm**](https://developer.zendesk.com/embeddables/docs/widget/contact_form) object.

## Hiding the "View Original Article" button

The **View Original Article** button bridges the article in the Web Widget (Classic) and the article in the help center itself. You can hide this button by using the **helpCenter** object, and setting the **originalArticleButton** property to **false**.

For more information, see the developer documentation for the [**originalArticleButton**](https://developer.zendesk.com/embeddables/docs/widget/settings#originalarticlebutton) setting for the [**helpCenter**](https://developer.zendesk.com/embeddables/docs/widget/help_center) object.

## Limiting search results

With the [**filter**](https://developer.zendesk.com/embeddables/docs/widget/settings#filter) setting on the [**helpCenter**](https://developer.zendesk.com/embeddables/docs/widget/help_center) object, you can limit the results of searches performed from the Web Widget (Classic) to articles based on category, section, and labels.
For more information, see the developer documentation for the [**filter**](https://developer.zendesk.com/embeddables/docs/widget/settings#filter) setting.

Scroll down for some additional examples that are not included in the developer docs that illustrate some of the ways you can limit search results.

Note: To specify multiple sections, categories, or labels, use a comma to separate the values (spaces are not required before or after).

To limit search to a specific section:

```
<script type="text/JavaScript">
window.zESettings = {
 webWidget: {
    helpCenter: {
      filter: {
        section: '200154474-Announcements'
      }
    }
 }
};
</script>
```

To limit search to a specific category:

```
<script type="text/JavaScript">
window.zESettings = {
 webWidget: {
    helpCenter: {
      filter: {
        category: '200053794-General'
      }
    }
 }
};
</script>
```

To limit search to content in multiple categories:

```
<script type="text/JavaScript">
window.zESettings = {
 webWidget: {
    helpCenter: {
      filter: {
        category: '115000669485,201742209' 
      }
    }
 }
};
</script>
```

To limit search to content with a specific label:

```
<script type="text/JavaScript">
window.zESettings = {
 webWidget: {
    helpCenter: {
      filter: {
        label_names: 'orders'
      }
    }
 }
};
</script>
```

To limit search to content in a specific category and with specific labels:

```
<script type="text/JavaScript">
window.zESettings = {
 webWidget: {
    helpCenter: {
      filter: {
        category: '200053794-General',
        label_names: 'Label One,Label Two,Label Three'
      }
    }
 }
};
</script>
```

## Customizing the help center search placeholder text

The default placeholder text in the help center search box is **How can we help?** You can customize this text so that it matches the user’s language, or so that specific text appears in certain languages. For more information, see the developer documentation for the [**searchPlaceholder**](https://developer.zendesk.com/embeddables/docs/widget/settings#searchplaceholder) setting.

 
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_search_placeholder.png) 

If [Contextual Help is enabled](https://support.zendesk.com/hc/en-us/articles/4408838063258), you can also configure the Web Widget (Classic) to open to recommended articles, making it easier for your customers to [self-serve](https://support.zendesk.com/hc/en-us/articles/4408836216218). For more information, see the developer documentation for the [**setSuggestions**](https://developer.zendesk.com/embeddables/docs/widget/help_center#helpcenter-setsuggestions) command for the [**helpCenter**](https://developer.zendesk.com/embeddables/docs/widget/help_center) object.

## Advanced configuration of voice in the Web Widget (Classic)

You can create multiple configurations that define how the voice channel behaves in the Web Widget (Classic). With each configuration you can customize call routing and display options in the Web Widget (Classic), based on your needs and preferences.

The key attributes that you can customize in each configuration are:

- The agent group that you want Web Widget (Classic) callback requests to be routed to
- The priority of Web Widget (Classic) callback requests
- Display Request a callback, Call us, or both of these options in the Web Widget (Classic)
- Display an estimated wait time in the Web Widget (Classic)

If you have only created a single configuration for voice in the Web Widget (Classic), this will automatically be the default configuration that displays in the Web Widget (Classic)
whenever voice is available.

If you have created multiple configurations for voice in the Web Widget (Classic), you can use the nickname setting to target the desired configuration.

Note: The nickname in the configuration settings API request must match the nickname of your configuration exactly, including any spaces and capitalization.

For more information, see the developer documentation for the [**talk**](https://developer.zendesk.com/embeddables/docs/widget/talk) object, the [**nickname**](https://developer.zendesk.com/embeddables/docs/widget/settings#nickname) setting, and [Configuring voice options in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426).

## Advanced configuration of chat in the Web Widget (Classic)

If you are using the [live chat in the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408825767962), you can offer chat functions in the Web Widget (Classic) so that visitors to your website can chat with agents, and send and receive files that might help with their problem. Agents can also send proactive messages to visitors, to see if they want or need any help.

For more information, see the developer documentation for the [**chat**](https://developer.zendesk.com/embeddables/docs/widget/chat) object.

With the integrated web and chat widget experience, you can further customize the [**chat**](https://developer.zendesk.com/embeddables/docs/widget/chat) object with these settings:

- [title](https://developer.zendesk.com/embeddables/docs/widget/settings#title)
- [concierge](https://developer.zendesk.com/embeddables/docs/widget/settings#concierge)
- [departments](https://developer.zendesk.com/embeddables/docs/widget/settings#departments)
- [prechatForm](https://developer.zendesk.com/embeddables/docs/widget/settings#prechatForm)
- [offlineForm](https://developer.zendesk.com/embeddables/docs/widget/settings#offlineForm)
- [notifications](https://developer.zendesk.com/embeddables/docs/widget/settings#notifications)
- [tags](https://developer.zendesk.com/embeddables/docs/widget/chat#chataddtags)
- [authenticate](https://developer.zendesk.com/embeddables/docs/widget/settings#authenticate)

## Offering end users multiple contact options

You can allow end users to choose a contact option. You may want to customize your website so that some pages allow end users to make a choice and others don’t. The exact behavior depends on whether chat or voice is configured for the Web Widget (Classic), and whether a chat agent is online. You can customize the default text of contact options, if needed.

Here's a list of the default text:

| Contact option | Default text |
| --- | --- |
| [Contact button](https://developer.zendesk.com/embeddables/docs/widget/settings#contactbutton) | Contact us |
| [Chat label (with agent online)](https://developer.zendesk.com/embeddables/docs/widget/settings#chatlabelonline) | Live chat |
| [Chat label (with agent offline](https://developer.zendesk.com/embeddables/docs/widget/settings#chatlabeloffline) | Chat is unavailable |
| [Contact form label](https://developer.zendesk.com/embeddables/docs/widget/settings#contactformlabel) | Leave us a message |

For more information, see the developer documentation for the [**contactOptions**](https://developer.zendesk.com/embeddables/docs/widget/core#contact-options-settings) setting.

**Offering contact options for chat**

If chat is configured for the Web Widget (Classic), end users are automatically routed to a chat, if a chat agent is available. However, you can allow end users to choose between chatting with an agent or completing a contact form, even if a chat agent is available. If a chat agent is available when the user clicks the launcher, but the agent signs off before the chat begins, the end users may see a message indicating that the agent is not available.

It's a known issue that when end users choose to chat, they cannot use the back button to return to the other contact options. To do so, they need to completely end the chat or refresh the page.

**Offering contact options for voice**

If voice and other contact options are enabled in the Web Widget (Classic), and agents are online, contact options are automatically enabled.

## Formatting code for multiple widget components

Note: This section is provided for instructional purposes only. Zendesk does not support or guarantee the code. Zendesk also can't provide support for third-party technologies such as JavaScript, jQuery, or CSS. Please post any issues you have in the comments section or try searching for a solution online.

Items that are specific to the contact form, help center, and chat are nested under those headings (contactForm, helpCenter and chat) in the HTML of your site, while global items are included separately.

For example, these customizations are defined below:

- The position of the Web Widget (Classic) on the screen has been changed using the offset setting. Offset is a global item, which is why it has its own entry.
- Help center search—doesn’t include the View Original Article button. The title “Search for help” for English-language users, and “Have your say” for all other languages.
- Chat is disabled.
- The contact form title is “Message us” in English and “Contact us” in other languages.
- The launcher button text is “Make a request” in English and “Get help” in other languages.

```
<script type="text/JavaScript">
window.zESettings = {
 webWidget: {
    offset: { horizontal: '400px', vertical: '400px' },
    helpCenter: {
      originalArticleButton: false,
      title: {
        'en-US': 'Search for help',
        '*': 'Have your say'
      }
    },
    chat: {
      suppress: true
    },
    contactForm: {
      title: {
        'en-US': 'SMessage us',
        '*': 'Contact us'
      }
    },
    launcher: {
      label: {
        'en-US': 'Make a request',
        '*': 'Get help'
      }
    }
 }
};
</script>
```
# Providing omnichannel support using Web Widget (Classic) for Zendesk Suite

Source: https://support.zendesk.com/hc/en-us/articles/4408844047898-Providing-omnichannel-support-using-Web-Widget-Classic-for-Zendesk-Suite

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Note: There is an updated version of the Web Widget that provides similar (but not identical)
functionality using Zendesk’s new messaging and automated conversation flows. For
information see [Working with messaging in the Web Widget](https://support.zendesk.com/hc/en-us/articles/4408828655514).

The Zendesk Suite of products provides multiple ways for you to deliver support to
and communicate with your customers.

Through the Web Widget (Classic), Zendesk’s legacy embedded customer service
experience, you can offer your customers any or all of the following Zendesk Suite
products:

- **Help center**: Suggest help center articles for immediate self-service support.
- **Contact form**: Display ticket forms for support requests.
- **Voice**: Let customers request a callback from an agent or initiate a call to an agent.
- **Chat**: Launch a chat with an agent.

Additionally, you can choose which contact options to make available to your end
users based on the web page they’re viewing when they request support via the widget, agent
availability, and more.

This article walks you through the tasks required to use the Web Widget (Classic)
with Zendesk Suite products to provide focused, customized support for your customers, along
with links to relevant documentation so you can get up and running in no time.

The basic workflow is as follows:

1. Decide how you want the widget to perform, taking into consideration your
   Zendesk Suite options, your audience, your staff, and what website or help center pages
   would be enhanced by including the widget.
2. Configure the basic widget settings.
3. Configure the Zendesk Suite products you want to use, to best work with the
   widget.
4. Add the widget to your website or help center code.
5. Customize the widget by modifying the Web Widget API objects.
6. Add the customized objects to your website pages, or to your branded help
   centers.

The steps in this workflow are described in more detail in this article, which
includes the following topics:

- [Why Web Widget (Classic)?](#topic_esm_1dt_vdb)
- [Planning your Web Widget (Classic) strategy
  for Zendesk Suite](#topic_fsm_1dt_vdb)
- [Basic configuration for Web Widget (Classic)](#topic_gsm_1dt_vdb)
- [Configuring Zendesk Suite products for Web
  Widget (Classic)](#topic_hsm_1dt_vdb)
- [Adding Web Widget (Classic) to your support
  portal](#topic_pkk_zct_vdb)
- [Further customization of your widget
  configuration(s) by modifying the API](#topic_fv4_zct_vdb)
- [Adding the modified code to your widget
  instances](#topic_nzs_zct_vdb)
- [Sample workflow](#topic_fzz_zct_vdb)

For links to all of our documentation and support tips on the Web Widget (Classic), see [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354).

## Why Web Widget (Classic)?

Web Widget (Classic) is an extremely flexible tool for embedding customer
service features in your website or help center, allowing your end users to get help without
leaving the page they’re on. It’s also simple to configure and enable, so you can get up and
running quickly. You can add different configurations of the widget to any page of your
website, or create different widgets for multiple help center brands, which makes it the
perfect medium for offering support options.

Your widget organizations options include:

- A single configuration of the widget on every website or help center page
- Different widget configurations on specific web pages
- Different widget configurations for each branded help center

The widget is easily customizable. No matter which Zendesk Suite products you use, you
can configure the widget in a number of ways, including:

- Displaying custom ticket fields and ticket forms, based on the type of
  request being made
- Controlling the appearance of Widget elements to reflect your
  brand(s)
- Restricting access to signed-in users, or making it available to every
  visitor to your site or help center
- Establishing contextual help

You can update these, and other, settings as needed, without redeploying the
code every time you make a change.

Offering multiple contact options gives your end users a better experience as
well. They can self-serve by searching the help center, and they can choose to reach out to
an agent in the way that best fits their situation – via live chat for real-time help, call
or request a callback to be reached by phone, or by filing a ticket if they don’t need
immediate assistance.

## Planning your Web Widget (Classic) strategy for Zendesk Suite

Make a broad, holistic assessment of your business requirements and
restrictions, customer needs, website and help center offerings, and multibrand options -
among other things - to determine how you can best combine the widget with Zendesk Suite
products.

You should decide which pages you want your widget to appear on. If you’re
adding the widget to a website, you can add a customized API to the standard widget code on
each page, displaying different options to your end users. If you have a multi-branded help
center, you can have different configurations of the widget for each brand’s help
center.

The following list includes some things you may want to consider when
determining how to use the widget in conjunction with Zendesk Suite. Use the links to learn
more about each of these elements:

- **Business hours**: When do you offer live support ? How do you want to
  respond to customer service requests outside of business hours?

  Related
  articles:

  - [Setting your schedule with business hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522)
    (Support)
  - [Creating a schedule with operating hours](https://support.zendesk.com/hc/en-us/articles/4408822398106) (chat)
  - [Routing calls based on business hours](https://support.zendesk.com/hc/en-us/articles/4408845919002)

- **Customer service channels**: Which channels do you prefer for
  customer contact? Do you want to encourage self-service, or would you rather take a more
  hands-on approach to helping your customers?

  Related articles:

  - [About Zendesk Support channels](https://support.zendesk.com/hc/en-us/articles/4408824097050)
  - [Suppressing features on specific pages](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_bhz_bbq_mx)

- **Service Level Agreements**: Do your customers require a response or
  resolution within a set time?

  Related articles:

  - [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866)
  - [Viewing and understanding SLA targets](https://support.zendesk.com/hc/en-us/articles/4408832852122)
  - [SLA resources](https://support.zendesk.com/hc/en-us/articles/4408887228442)

- **Staffing and demand**: When do you tend to have the most staff on
  hand to respond to customer requests? When does demand spike, and when does it dip?

  Related articles:

  - [Determining your staffing requirements for voice support](https://support.zendesk.com/hc/en-us/articles/4408823679898)

- **Customer location**: Does it make sense to offer different types of
  service, or route requests to different departments, based on where the customer is on
  your website or help center when they launch the Web Widget?

  Related articles:

  - [Adding custom tags to Web Widget tickets from
    specific pages](https://support.zendesk.com/hc/en-us/articles/4408835672218)

- **Customer info**: Do you break your customers down into different
  support levels, based on their account type or other criteria? Do your VIP customers need
  a different kind of service than your standard customers? Are your customers identified in
  some way that can be leveraged to route them to the right kind of support?

  Related
  articles:

  - [End users and organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842#topic_npu_dkx_ac)
  - [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658)

## Basic configuration for Web Widget (Classic)

A simple, out-of-the-box implementation of Web Widget (Classic) provides a
quick way to embed customer service in your website or help center. From within the Web
Widget (Classic) admin page, you can easily enable a number of features that extend the
capability of your Web Widget (Classic).

This section is intended to be a quick-start guide to help you get a single
instance of Web Widget (Classic) onto every page of your help center or website (mobile or
desktop), with minimal configuration and customization.

Here, we’ll discuss [enabling
the widget and its default configuration](#topic_f4r_s3t_vdb), and how to configure the following
settings:

- [Widget appearance and
  location](#topic_d1f_t3t_vdb)
- [Chat and voice](#topic_p2k_t3t_vdb)
- [Contextual help](#topic_jj4_t3t_vdb)
- [Security settings](#topic_z2t_t3t_vdb)

### Enabling the default widget

To use the Web Widget (Classic), you need to enable it via the Zendesk Support
Web Widget (Classic) admin page.

**To access the Web Widget (Classic) admin page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Customization** tab, to view the default widget settings.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_default.png)

The default settings include:

- **Contact form (enabled)**, a support request form.
- **Ticket form(s) (disabled)**, a set of predefined ticket fields for a specific
  support request. When toggled on, your default ticket form is applied to the contact
  form. See [Managing your ticket forms](https://support.zendesk.com/hc/en-us/articles/4408836460698) for more
  information.
- **Custom ticket fields (disabled)**, custom fields added to your support request
  form(s). You can add any available custom ticket fields to the contact form using the
  drop-down menu. See [Custom ticket fields in Web Widget](https://support.zendesk.com/hc/en-us/articles/4408881857946).
- **Chat (enabled for Chat users; unavailable for customers not using Chat)**, adds a
  chat launcher button to the widget search results screen.
- **Help center (enabled for help center users)**, adds a help center article search
  to the widget.
- **Contextual Help (enabled)**, displays suggested articles upon initial launch of
  the widget, based on the page the end user is viewing. See [Contextual help](#topic_jj4_t3t_vdb), below.
- **Security settings,** applies your current security access permissions to the
  widget. See [Security settings](#topic_z2t_t3t_vdb),
  below.
- **Zendesk logo (enabled)**, displays the Zendesk logo at the bottom of the widget.
  See [Widget appearance and
  location](#topic_d1f_t3t_vdb).
- **Theme color (defaults to green)**, the color applied to most visual elements in
  the widget. See [Widget appearance and
  location](#topic_d1f_t3t_vdb).
- **Position (defaults to right)**, the location of the widget at the bottom of the
  page. See [Widget appearance and
  location](#topic_d1f_t3t_vdb).
- **Web Widget button text (defaults to "Help")**, the text appearing in the widget
  launch button. See [Widget appearance and
  location](#topic_d1f_t3t_vdb).
- **Contact form button text (defaults to "Leave us a message")**, the text appearing
  in the contact form button. See [Widget
  appearance and location](#topic_d1f_t3t_vdb).

**On a website**, by default, and without any further configuration, the
widget will include a simple Help button, which launches a basic contact form, when you
add it to your website:

**Button**:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/help_button-web.png)

**Contact form**:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/simple_contact_form-web.png)

When a customer clicks the Help button, the contact form appears, asking for
some basic support information. When the customer clicks Send, a Support ticket is created
and sent to your ticket queue.

If you’re satisfied with the widget as is, you can add it to your website. See
[Adding the Web Widget (Classic) to your support
portal](https://support.zendesk.com/hc/en-us/articles/4408821673242#topic_kf2_xcj_vz) for more information.

**On a help center**, when enabling the widget the steps, and end result,
are slightly different than described above.

The default configuration for a help center widget includes suggested articles
for your customers, based on keywords included in their query, so you must have a help
center set up, with articles that cover at least the common support questions.

As with the website setup, you’re guided through an initial setup process by a
wizard. To enable the widget for the help center, make sure you toggle on the help center
option.

By default, and without any further configuration, the Widget will include a
simple Help button, which launches a basic search form, when added to your help
center:

Button:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/help_button-hc.png)

Search form:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/simple_search_form-hc.png)

Suggested articles & ticket submit option:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_results.png)

When a customer enters a search query, a list of potentially relevant help
center articles is displayed, along with the option to submit a ticket if they need
further assistance.

If you’re satisfied with the widget as is, you can embed the Web Widget in your help
center. See [Adding the Web Widget to your support portal](https://support.zendesk.com/hc/en-us/articles/4408821673242#topic_kf2_xcj_vz) for
more information.

### Widget appearance and location

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_appearance.png)

You can customize the following appearance-related elements:

- **Zendesk logo** can be displayed or, for some customers, turned off in the
  widget.
- **Theme color** for widget buttons and links, using a color picker.
- **Button position** on the left or right of the page, using a drop-down menu.
- **Widget button text**, using the drop-down menu to select Help (default), Support,
  or Feedback.
- **Contact form button text**, using the drop-down menu to select Leave us a message
  (default) or Contact us.

More information and instructions, as well as links to related articles,
can be found in [Configuring the components in your Web
Widget](https://support.zendesk.com/hc/en-us/articles/4408838063258).

### Chat and voice

If you offer chat or voice support, you can enable those channels in Web Widget
(Classic), and perform a basic configuration to get them up and running.

If you are already using the Web Widget, Chat is available to customers as soon as you
enable it in the Web Widget.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat.png)

You can, however, configure Chat-specific elements if needed. This means you can toggle
on chat on the widget admin page, then visit your Chat admin page to configure the basic
appearance, forms, settings, and security options.

Chat is only presented as a contact option to the end user if chat agents are
online; if no agents are online, the end user is given the option to leave a message.

You can also offer call options in the widget. By default, the widget uses your
default settings to determine the groups widget calls are routed to, the available contact
options, and the like; with minimal configuration effort, you can customize these
settings. More information can be found in the [Configuring voice options in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426).

### Contextual help

If you’re using the basic widget functionality that first asks your end
users to enter a question or keywords, and encourages them to self-service by suggesting
help center articles, you can refine these article suggestions by enabling Contextual
help. Contextual help uses the web page your visitor is currently on, along with your help
center content, to suggest articles that are relevant to their questions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_contextual.png)

For more information, see [About Contextual Help for the Web Widget.](https://support.zendesk.com/hc/en-us/articles/4408824357402)

### Security settings

You can configure your Web Widget to display content from a restricted help
center (one that requires users to sign in for access), or restricted knowledge base
content (a public help center with certain articles or sections restricted to signed-in
users only).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_security.png)

Clicking the **Configure** button, shown above, opens the widget
security settings page, where you can specify whitelisted domains and generate a shared
secret to enable access to restricted content.

When you configure the Web Widget to include restricted content:

- Visitors to your website who are logged in can read the restricted help
  center articles via the Web Widget. Note that the customer site in which the Widget is
  embedded is responsible for authentication of a user's email.
- Visitors who are not logged in, however, see only public articles. If
  there are no public articles, the help center features do not appear in the Web Widget.

For more information, see the following articles:

- [Using restricted help center content with the Web
  Widget](https://support.zendesk.com/hc/en-us/articles/4408843923610)
- [Permitting only added users to submit
  tickets](https://support.zendesk.com/hc/en-us/articles/4408883658906)

- [Configuring widget security settings](https://support.zendesk.com/hc/en-us/articles/4408887520282)
  (Zendesk Chat-specific)

## Configuring Zendesk Suite products for the Web Widget

Each Zendesk Suite product has settings, permissions, and other configuration options that
can impact how they function when paired with the Web Widget. This section describes some of
those options, and how they might affect widget functionality, for:

- [Help center](#topic_b13_yst_vdb)
- [Contact form](#topic_vnw_yst_vdb)
- [Voice](#topic_vpc_zst_vdb)
- [Chat](#topic_afh_zst_vdb)

### Help center

This section discusses some of the help center configuration options that can
affect widget functionality, including:

- [Article labels](#topic_hy1_jtt_vdb)
- [Content restriction](#topic_mzj_jtt_vdb)
- [Autroreplies](#topic_f5t_ktt_vdb)

#### Article labels

By adding labels to your help center articles, you can improve your end
users’ search results. Using labels properly can increase the level of self-service your
end users achieve. If a search through the widget doesn’t result in an answer for your
end user, they’re presented with additional contact options. If they don’t find the
information they needed, do they need to file a ticket, chat with an agent, or request a
callback?

When adding labels to articles, keep in mind that they are indexed for search
with a little less weight than the article title; however, multiple labels with similar
words can outweigh the title and body of the article.

For more information, see [Using labels on your help center articles](https://support.zendesk.com/hc/en-us/articles/4408835056154).

#### Content restriction

You can restrict access to specific articles, or entire sections, in your
help center. Access can be granted based on user authentication, or by creating groups
of end users, called user segments.

Restricting access to articles impacts the search results displayed when an
end user enters a question or search term into Web Widget (Classic). If an end user does
not have permission to view certain articles, their search results may be
less-than-helpful. As with labels, this can affect whether they can solve their own
support issue, or need further assistance from your support team.

For more information, see the following articles:

- [Using restricted help center content with Web Widget
  (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843923610)
- [Applying user segments to restrict access to help
  center knowledge base content](https://support.zendesk.com/hc/en-us/articles/4408824005914)
- [Restricting help center access to signed-in
  users](https://support.zendesk.com/hc/en-us/articles/4408842656154)

#### Article Recommendations

The Zendesk bots Article Recommendations feature uses machine learning to
help answer your customers’ questions with content from your knowledge base. When added
to Web Widget (Classic), Zendesk bots provides a chat-like interaction with your end
users. Article Recommendations suggests suggests articles that may address customer
issues. Article Recommendations is included with all Suite plans.

For information, see the following:

- [Zendesk bot resources](https://support.zendesk.com/hc/en-us/articles/4408834322842)

### Contact form

Your Zendesk Support configuration choices affect the appearance of the
widget, and ticket routing and creation.

This section discusses some of the Support options that impact how the
widget handles Support-related tasks. These options include:

- Custom ticket fields and ticket forms
- Custom user fields
- Ticket tags
- Multiple brands

#### Custom ticket fields and ticket forms

On Zendesk Suite Growth plan and above, you have the option of presenting
your end users with a single default ticket form, or with a selection list of active
forms. You can customize the information displayed in your default contact form using
custom ticket fields, or you can present your end users with multiple custom ticket
forms to choose from.

**Custom ticket fields** allow you to gather more information about
the end user’s support issue, by customizing the information you request from your end
users in your ticket forms. However, every instance of Web Widget (Classic) – even
widgets for different brands - will use the same default ticket form, so you might find
it more useful to create multiple ticket forms that allow your end users to choose the
topic that addresses their issue best.

**Multiple ticket forms** are available on Zendesk Suite Growth plan
and above. They allow you to display all active ticket forms to the end user. When
ticket forms are toggled on, the end user clicks the Leave us a message button, and they
can select the form that matches their needs. You can assign different custom forms to
different brands (and therefore display different forms in the widget associated with
each brand), but the default form is always displayed, no matter the current brand.

Learn more about custom ticket fields, ticket forms, and using them in
Web Widget (Classic) in the following articles:

- [Adding custom fields to your tickets and
  support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794)
- [Using custom ticket fields and ticket forms with Web
  Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408834218522)
- [Creating ticket forms to support multiple
  request types](https://support.zendesk.com/hc/en-us/articles/4408846520858)

#### Custom user fields

Custom user fields are added to user profiles to store additional
customer details. Any custom user fields you create apply to all users. If you require
your users to sign in before interacting with Web Widget (Classic), you can use these
fields in your business rules (triggers, automations, and macros) to route the tickets
generated by the user to the best agent or group to handle

Related articles:

- [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866)

#### Ticket tags

When a ticket is submitted through the Web Widget, it includes, as a tag,
the URL for the page the user was viewing when the ticket is sent. In Zendesk Support,
you can create triggers based on these URLs to add custom tags to the ticket, then use
these tags to route tickets into specific ticket views.

Related articles:

[Adding custom tags to Web Widget tickets from
specific pages](https://support.zendesk.com/hc/en-us/articles/4408835672218)

#### Multiple brands

If you support multiple brands, you can create and customize a separate
widget for each brand. Each brand’s widget can be configured based on that brand’s needs
and style, and then linked to the brand’s help center.

Note: The number of help centers you’re allowed is determined by your current plan. See
[Creating a help center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408828794778)
for information.

Each brand can customize some elements that appear in the widget, such as
security settings, ticket forms, theme color, and the like. Customizable elements are
different for help center and website widgets. Information on these elements is
available in [Basic configuration for Web
Widget (Classic)](#topic_gsm_1dt_vdb) .

Although you can customize each brand’s widget, keep in mind that all
brands and all widgets on your account share some elements. You can use the brands to
tag users when they launch a chat or voice session from the widget, then use those tags
to route them to the right agent or agent group.

For more information, see the following articles:

- [Adding Web Widgets (Classic) for multiple
  brands](https://support.zendesk.com/hc/en-us/articles/4408828483738)
- [Managing multiple brands (Zendesk
  Support)](https://support.zendesk.com/hc/en-us/articles/4408829486362)

### Voice

If you are offering call options, you can create multiple
configurations that define behavior in Web Widget (Classic). With each configuration you
can customize call routing and display options, based on your needs and preferences. These
configurations can use separate numbers, so you can route them to the agents best suited
to address the end users’ issues. Instructions for creating configurations can be found in
[Configuring voice options in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426).

Consider the following scenario:

An end user ordered the wrong size shirt, and wants to exchange it. They are
currently on a website page describing the product return process. When that end user
clicks the launcher button, they choose to request a callback from an agent, for
assistance in exchanging the shirt.

You’ll want a configuration for Web Widget (Classic) that sends the end user to
the agent who can best address their specific issue, so you will want to consider the
following:

- [Group routing](#topic_axk_v5t_vdb)
- [Nicknames](#topic_rbj_v5t_vdb)
- [Priority](#topic_jbg_v5t_vdb)
- [Displaying time
  estimates](#topic_ady_55t_vdb)

#### Group routing

In the scenario above, you’ll want to make sure the agent receiving the
callback request knows how to handle sales-related issues. To do this, you need to
create a specific group, populated by agents familiar with sales support. Any group
you create can be selected in the Group routing setting.

Related articles:

- [Routing incoming calls to groups of agents](https://support.zendesk.com/hc/en-us/articles/4408885952922)

#### Nicknames

If you have created multiple configurations for voice in Web Widget
(Classic), each one has a unique nickname. You can then refer to that nickname in the
Web Widget API, to display a specific configuration on a specific page.

For information on using nicknames to specify widget configurations, see
[Updating voice options for specific
widget instances](#topic_un5_qzt_vdb), below.

#### Priority

Next you can select the priority this call should be given. The
configuration allows you to choose Normal or High priority for calls coming from
this page. This is an important setting if you have other configurations sending
calls to the Sales Support group - High priority calls are pushed to the top of the
queue, ahead of any Normal priority calls, regardless of their wait time.

Related articles:

- [Configuring voice options in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426)

#### Displaying time estimates

If you like, you can display the average waiting time until an agent is
available. This is simply a courtesy to your end user, who can decide whether to wait
for agent assistance, or request a callback when someone is available.

Related articles:

- [Configuring voice optioins in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426)

### Chat

Zendesk Chat can be fully integrated with Web Widget (Classic). You can
customize the appearance of the Chat visual elements, Chat forms, security settings, and
other Chat-specific options. See [Configuring and deploying chat on your website or help center](https://support.zendesk.com/hc/en-us/articles/4408831945626?option=2)
for a walkthrough of your customization options, as well as instructions for enabling Chat
in the Web Widget (Classic). You can also find useful information in the Support Tip [Web Widget (Classic) and chat advanced
customization](https://support.zendesk.com/hc/en-us/articles/4408843561498).

## Adding Web Widget (Classic) to your support portal

When you have configured the widget elements discussed in [Basic configuration for Web Widget (Classic)](#topic_gsm_1dt_vdb) and (if needed) [Configuring Zendesk Suite products for Web Widget
(Classic)](#topic_hsm_1dt_vdb) , you can generate the code and add it to your website or help
center.

For detailed instructions, see [Adding the widget to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242).

You can now work on more complex customization of the widget.

## Further customization of your widget configuration(s) by modifying the API

After you’ve [planned your
widget strategy](#topic_fsm_1dt_vdb), completed the [basic
widget configuration](#topic_gsm_1dt_vdb), and any [product-specific setup](#topic_hsm_1dt_vdb), you’re ready to customize the widget code and update the
configuration - or configurations - you’ve added to your website or help center site.

You can add these custom widget configurations to your website or help center
in each spot where you want that configuration to appear, by adding customizing the widget
API object zESettings, to each page where the widget appears. See [About the Web Widget API](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_f1g_sgq_mx) for more information.

Most configuration-specific customizations are made by modifying the
zESettings object, and can include:

- [Controlling which channels
  are displayed in the widget](#topic_ahh_qzt_vdb)
- [Positioning the widget on
  your page](#topic_m2m_qzt_vdb)
- [Customizing the look and
  language of the widget](#topic_nzp_qzt_vdb)
- [Updating voice options for
  specific widget instances](#topic_un5_qzt_vdb)

### Controlling which channels are displayed in the widget

You can choose to display or suppress support channels in Web Widget (Classic),
based on the website or help center page the widget is launched from. You can suppress any
of the support channels offered through the widget. This allows you to direct your end
users to (or away from) specific contact options.

In the following example, your widget is configured to offer help center search,
contact form, voice, and chat as support options, but when an end user launches the widget
from a payment page, you only want to offer them the option to start a chat with an agent,
with the option to leave a message if no agent is available.

To do this, you need to modify the widget API code included in the payment page’s HTML,
to suppress the channels you do not want your end user to access. On the payment page of
your website, you would add the following to the widget API:

```
<script type="text/JavaScript">
  window.zESettings = {
    webWidget: {
      talk: {
        suppress: true
       },
        helpCenter: {
          suppress: true
       }
      }
    };
</script>
```

This displays only the chat option to your end user (as the voice and help center
channels are suppressed). Remember, the chat option is only available if chat agents are
on duty; otherwise, end users will be instructed to leave a message.

For more information on how to
make similar modifications, see [Suppressing features on specific pages](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_bhz_bbq_mx).

### Positioning the widget on your page

By default,
the widget is placed at the bottom-right of the browser, and it opens by expanding
upward. Widget placement can vary from page to page, by adding different modified
zESettings objects to different pages.

You can change the placement of Web Widget (Classic) in two ways:

- By choosing to place it in another spot - top-left, top-right, or
  bottom-left. See [Re-positioning the widget](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_nzd_cbq_mx)
- By offsetting its placement on the page. See [Offsetting the widget placement](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_ozd_cbq_mx).

### Customizing the look and language of the widget

You can change the color of widget elements, or the text that appears on
them, rather than using the default settings.

Elements you can change include:

- **The color of the widget buttons**, text, and the like, can be
  altered by adding a color theme applied to all elements, or by assigning different
  colors to each element. See [Customizing the color of the widget
  elements](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_pzd_cbq_mx).
- **The widget language**, which by default appears in the end user’s
  selected language. You can force the widget to display in the language of your choice,
  despite the end user’s selection. See [Displaying your widget in a different
  language](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_sty_j2r_gq).
- **The text on most widget elements**, such as the Chat and Support
  launcher buttons, and the title of the widget contact form or help center page. See
  [Customizing widget text](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_chz_bbq_mx).
- **The subject line on the widget contact form**, which by default is
  empty, can say whatever you want. See [Adding a subject line to the contact form](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_gzp_1bq_mx).
- **The search placeholder text**, which is also empty by default. See
  [Customizing the help center search placeholder
  text](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_txs_qf1_l1b).

### Updating voice options for specific widget instances

If you offer [voice support in
the Web Widget](#topic_vpc_zst_vdb), you may want to create multiple configurations that define
channel behavior on different pages. In each configuration, you can customize the
following:

- The agent group that you want Web Widget callback requests to be routed
  to
- The priority of Web Widget callback requests
- Display Request a callback, Call us, or both of these options in the
  Web Widget
- Display an estimated wait time in the Web Widget

When you create multiple configurations for voice in the widget, as
described [above](#topic_vpc_zst_vdb), each configuration
has a unique nickname. You use these nicknames in the modified API code to determine which
configuration appears on each page of your website or help center.

For example, if you’re creating a configuration to handle Sales questions,
you can enter the nickname “Sales Support”. Then, you modify the API to refer to that
configuration.

The following API block would target a configuration with nickname “Sales Support":

```
<script type="text/javascript">
window.zESettings = {
  webWidget: {
    talk: {
      nickname: 'Sales Support'
      }
    }
};
</script>
```

Related articles:

- [Web Widget API - nickname](https://developer.zendesk.com/embeddables/docs/widget/zesettings#nickname)

## Adding the modified code to your widget instances

As discussed above, you can modify the Web Widget API to customize any number
of elements in Web Widget (Classic), and in many cases you can add multiple configurations,
with different customization choices, throughout a single website or help center.

To get the customizations onto your website or help center, you need to add
the modified API objects, along with the basic widget code, to your website or help center,

The basic steps to adding multiple instances of the widget to different
places on your website or help center are as follows:

1. Add the basic widget code to each page of your website where you want it
   to appear, or to your help center, as described in [Adding Web Widget (Classic) to your support portal](#topic_pkk_zct_vdb).
2. On each page where you want to offer a customized version of your widget,
   add the Web Widget API, with the modifications made as described above in [Further customization of your widget
   configuration(s)](#topic_fv4_zct_vdb).
   - For a website, go to each web page where you want to add that version of
     the widget, then paste the code before the Web Widget snippet.
   - For a help center, go to the Knowledge admin for each brand you want to
     customize, and add the modified API to the header code before the Web Widget snippet.

## Sample workflow

In this example, both chat and voice are offered in the widget to end users
only when those channels have agents available.

A potential customer is viewing a marketing page for Product A on your
website during regular business hours. They have a question about the product, and click
Support to launch Web Widget (Classic).

Configuration goal: Enable the Chat integration to provide real-time support
and complement help center and Contact Form.

Customize the configuration to address the following:

- Chat, for immediate response - you’ll want to talk to this person ASAP,
  to capture the sale.
- Product - Sales experts on Product A will be the best fit.
- Availability - If it is after business hours, and no Chat agents are
  available, offer the option to submit a support ticket that is routed to Sales
  agents.

The basic steps to address this scenario are as follows:

1. In Zendesk Chat, [create a schedule with operating hours](https://support.zendesk.com/hc/en-us/articles/4408822398106).
2. [Create chat triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762) for specific pages, and
   [enable skills routing](https://support.zendesk.com/hc/en-us/articles/4408836348058) to send chat requests from those
   pages to the right agent group.
3. In Zendesk Support, [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570#topic_vcr_xfp_ec) for sales-related tickets.
4. [Create a trigger to route Web Widget tickets from
   specific pages into the view](https://support.zendesk.com/hc/en-us/articles/4408835672218) created in step 3. Use the URLs for the
   specific pages (the same URLs as used in step 2).
5. [Configure the components in your Web Widget
   (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258), making sure to enable Chat.
6. [Add the widget to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242).
7. Customize the zESettings object in the API code to:
   - Suppress the help center search option
   - Display different messages based on agent availability
   - Offer the Sales contact form if needed
   - Route the ticket generated by the contact form to the Sales ticket
     view.

     That API customization might look like the
     following:

     ```
     <script type="text/JavaScript">
     window.zESettings = {
       webWidget: {
         helpCenter: {
           suppress: true
         }
     contactOptions: {
        enabled: true,
       chatLabelOnline: { '*': 'Live Chat' },
       chatLabelOffline: { '*': 'Chat is unavailable' },
       contactFormLabel: { '*': 'Leave a message for our Sales agents'}
       }
     };
     </script>
     ```
8. Add this code to the pages [on your website](https://support.zendesk.com/hc/en-us/articles/4408821673242#topic_kf2_xcj_vz), or your [help center](https://support.zendesk.com/hc/en-us/articles/4408821673242#topic_a52_wcj_vz), where needed.
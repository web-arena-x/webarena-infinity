# Launch Guide for Zendesk Suite

Source: https://support.zendesk.com/hc/en-us/articles/4408881507098-Launch-Guide-for-Zendesk-Suite

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As described in [Getting Started in Zendesk Suite](https://support.zendesk.com/hc/en-us/articles/4408881937306), the Zendesk Suite is a collection
of products and capabilities that provide you with the tools you need to create a complete
omnichannel support solution. It’s a ticketing system that seamlessly integrates all of the
communication channels you use to interact with your customers.

This article is for admins who need to roll out Zendesk Suite to their support organization
and customers. Unlike the Getting Started guide, which is an overview, this article contains
the information and tasks you need to set up and launch your Zendesk Suite support solution.
It also includes sections that describe how you can then optimize and enhance your support
solution.

The order of these launch tasks is important, although many steps are optional, because there
are dependencies between them (one should happen before the other). You should follow the
sections in order to get the most from this article.

Note: You can find the task list only, unannotated version of this guide here: [Launch tasks for Zendesk Suite](https://support.zendesk.com/hc/en-us/articles/4408882670106).

This article includes the following topics:

- [Planning your omnichannel support solution](#topic_mjv_v2s_v4b)
- [Defining your organizational structure](#topic_bws_yfs_v4b)
- [Defining your customer support experience](#topic_grq_fgs_v4b)
- [Configuring user access security and authentication](#topic_t45_ngs_v4b)
- [Integrating external apps and services](#topic_qvx_tgs_v4b)
- [Adding your staff members and end users](#topic_rlh_ygs_v4b)
- [Setting up your help center and creating your knowledge base](#topic_u21_dhs_v4b)
- [Automating support with autoreplies](#topic_gmv_flb_z4b)
- [Setting up the web and mobile messaging channels](#topic_khs_hhl_v4b)
- [Setting up the voice channel](#topic_jqd_vks_v4b)
- [Defining ticket routing and workflows](#topic_kpm_nls_v4b)
- [Training your agents](#topic_xwf_hsz_v4b)
- [Testing before going live](#topic_scf_yls_v4b)
- [Going live to customers](#topic_b2v_cms_v4b)
- [Adding social messaging channels](#topic_h5v_gms_v4b)
- [Monitoring performance with reporting and analytics](#topic_m31_lms_v4b)
- [Providing global support](#topic_mxk_zms_v4b)
- [Boosting agent and team productivity](#topic_qny_dns_v4b)
- [Retaining and growing your customer base](#topic_st2_zrl_v4b)

## Planning your omnichannel support solution

The first step toward launching the omnichannel support solution with Zendesk
Suite is to determine the channels of communication that you’ll open up to your customers.
You want to provide support to your customers using the channels that they prefer. With
Zendesk Suite, you have just about every imaginable option: messaging, telephone
conversations, social media messaging, email messages, via mobile devices, and through many
popular Web applications and services.

Determining the channels you need to set up for your customers will help you to
also determine how many agents you need, what skills they need, and the training you need to
provide them with. You’ll also then be able to define your organizational structure and the
workflow you’ll set up for handling incoming support requests. You should also think about
how the type of business or organization you’re providing support for will affect how you
set up your Zendesk Suite.

Here are some things to consider before you start configuring your support
solution.

- To understand what your channel options are, see [About Zendesk channels](../../product-guides/suite-basics/about-zendesk-channels.md). If you could use some
  advice about how to best use channels to manage customer satisfaction and your support
  costs, see [Omnichannel support made easy with Zendesk](https://zen-marketing-content.s3.amazonaws.com/content/resources/OmnichannelSupportMadeEasyWithZendesk_en-GB.pdf) (PDF).
- Consider how you want to set up your Zendesk support solution based on who you are
  providing support to. See the following: [Using Support for your Business-to-Business (B2B) business](https://support.zendesk.com/hc/en-us/articles/4408825510938),
  [Using Support for your Business-to-Consumer (B2C) business](https://support.zendesk.com/hc/en-us/articles/4408832607130), or
  [Using Support for your Business-to Employee (B2E)
  business](https://support.zendesk.com/hc/en-us/articles/4408832551706).
- The Agent Workspace is the ticket interface within Zendesk Support that
  enables agents to work seamlessly across channels. All the support conversations your
  agents have with customers are captured in this single interface. Working in the Agent
  Workspace is the first thing your agents will need to know about handling support
  requests with Zendesk. See [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930).

  You can of course always add more channels and modify your workflows after
  you’ve launched and it's often best to take a phased approach. For example, you might
  start using voice to make outbound phone calls on particularly complex tickets or by
  implementing messaging on your website so that you have better control of
  conversations and the need to have live agents available to respond to them.

## Defining your organizational structure

After you've determined the channels that you’re going to provide to your
customers, the next step is to create an organizational and role structure for your staff
members. You do this in Zendesk Support.

There are two staff member roles: agent and admin. Agents solve tickets and
admins, who can also solve tickets, have additional access to the admin features of the
Suite and are able to set up workflows, for example. What an admin or agent can do in a
Zendesk Suite product varies. Also, there are additional roles for each product and in some
versions of the Zendesk Suite you can also create custom roles.

Groups are used for organizing your staff members. Organizations are meaningful
collections of your end-users, but they can also include staff members. For more information
about how each is used, see [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842).

It’s a good idea to set up your organization structure at the beginning because
it will be needed when you define your workflow in upcoming steps in this guide. You’ll add
staff members (and end users) later in the setup process.

### Launch tasks

| Add groups | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_groups) | [Article](https://support.zendesk.com/hc/en-us/articles/4408894175130) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#groups) | [Video](https://zendesk.wistia.com/medias/t8faswmqcg) |
| Define custom roles \* | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_roles) | [Article](https://support.zendesk.com/hc/en-us/articles/4408882153882) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#roles) |  |
| Customize user fields | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_user_fields) | [Article](https://support.zendesk.com/hc/en-us/articles/4408822051866) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#userorgfields) |  |
| Create organization fields | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_org_fields) | [Article](https://support.zendesk.com/hc/en-us/articles/4408842677786) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#userorgfields) | [Video](https://fast.wistia.net/embed/iframe/vojyfiulfk?popover=true) |
| Create organizations | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_orgs) | [Article](https://support.zendesk.com/hc/en-us/articles/4408882246298) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#organizations) |  |

\* Available in Enterprise and Enterprise Plus plans

## Defining your customer support experience

Your customers’ experience of the support you provide to them is a collection of
contact points that includes your support email addresses, your help center, your social
media presence and other channels you set up, and where you’ve embedded your Zendesk (on any
website and also in mobile apps).

In Zendesk, a collection of customer contact points is referred to as a
*brand*. Depending on your Zendesk Suite plan, you can have from 5 to 300 different
brands. For example, you may provide support for both B2C and B2B customers and want the
experience to be different for each.

Another part of the support experience is how your customers submit their support
requests when they’re not directly communicating with you live (via messaging and voice, for
example). You can customize the type of data that your customers need to provide to you when
submitting a support request.

The following tasks show you how to set up your brand and customize your ticket experience.
These are done in Support.

### Launch tasks

| Create brands | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_brands) | [Article](https://support.zendesk.com/hc/en-us/articles/4408829476378) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408833921306) | [Video](https://fast.wistia.net/embed/iframe/gwswrnsiol?popover=true) |
| Add support addresses | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_address) | [Article](https://support.zendesk.com/hc/en-us/articles/4408842868506) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408887388058) |  |
| Set business schedules | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_sched) | [Article](https://support.zendesk.com/hc/en-us/articles/4408842938522) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#schedules) | [Video](https://zendesk.wistia.com/medias/emkgin709o) |
| Create custom ticket fields | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_ticket_fields) | [Article](https://support.zendesk.com/hc/en-us/articles/4408883152794) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#ticketfields) | [Video](https://fast.wistia.net/embed/iframe/7qc4kqd64i?popover=true) |
| Create multiple ticket forms \* | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_ticket_forms) | [Article](https://support.zendesk.com/hc/en-us/articles/4408846520858) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408886987546#ticketforms) | [Video](https://zendesk.wistia.com/medias/z9zc5amow6) |
| Customize email notifications | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_email_notify) | [Article](https://support.zendesk.com/hc/en-us/articles/4408886168090) |  |  |

\* Available in Zendesk Suite Growth plan and above

There’s a bit more to do to complete your customer support experience, but you’ll want to
set up other parts of your support solution first. In upcoming sections of this article
you’ll find the information you need to complete your customer support experience.

## Configuring user access security and authentication

Before you add any users to your Zendesk account, staff or customers, you should
also define access security and authentication for both.

All staff members must sign in to any part of Zendesk Suite and you can define
your password security level and also what type of authentication will be used. Zendesk user
authentication is enabled by default, but you can also choose third-party authentication
using Microsoft or Google, or single-sign on using a number of different services.

With customers (referred to as end users in Zendesk), if you require them to sign
in, you have the same password and authentication options. In addition, you also have the
option of allowing them to sign in using their X (formerly Twitter) and Facebook accounts.

For an overview of your options for end user access, see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274).

Access security and authentication are defined in the Admin Center.

### Launch tasks

| Configure security settings | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_security) | [Article](https://support.zendesk.com/hc/en-us/articles/4408887485210) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408888782618) |  |
| Configure end-user settings | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_user_settings) | [Article](https://support.zendesk.com/hc/en-us/articles/4408883052442) |  |  |
| Configure single sign-on | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_sso) | [Article](https://support.zendesk.com/hc/en-us/articles/4408883587226) |  |  |

In your embedded support experience, you can also require end users to sign in and be
authenticated.

## Integrating external apps and services

If you also rely on external apps and services to help you manage parts of your
business and your customers, you can integrate those into your Zendesk account.

For example, if you also use Salesforce, JIRA, or Slack, you can manage user data
and ticket flows across those applications. You can also add apps from the Zendesk
Marketplace to integrate with popular services such as SurveyMonkey.

It’s also possible to notify external targets when a ticket is created or
updated. External targets can include cloud-based applications and services as well as HTTP and email.

You use Support to set up apps and external integrations.

### Launch tasks

| Add marketplace apps | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_apps) | [Article](https://support.zendesk.com/hc/en-us/articles/4408824421146) | [Advice](https://support.zendesk.com/hc/en-us/community/posts/360004230608) | [Video](https://zendesk.wistia.com/medias/o0ebrchb0e) |
| Add 3rd-party integrations | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_integ) | [Article](https://support.zendesk.com/hc/en-us/sections/200623816) |  |  |
| Set up notifications to external targets | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_ext_targets) | [Article](https://support.zendesk.com/hc/en-us/articles/4408883282458) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408883017882) |  |

As with channels, you can always add these external apps and integrations after you’ve
launched your Zendesk. If you don’t use external apps and services, you can skip this part
of the Suite launch setup.

## Adding your staff members and end users

With your organizational structure in place, you can now add agents to your Zendesk
account, assign them roles and skills, add them to the groups and organizations you created,
and set their access to specific channels and parts of the Zendesk Suite.

You can also add end users to your account if you already have a database of users that
you’re already providing support to (for example, you were using some other system to manage
users or provide support before you started using Zendesk).

The other method for adding end users to your account is as they come to you for support.
For example, via all the channels you provide, your end users contact you for support and a
new user account is automatically created. If the end user already has an account in your
Zendesk, a new support request will be paired with their existing account. If you haven’t
already done so, read [Understanding how end user accounts are handled across
Zendesk Suite](https://support.zendesk.com/hc/en-us/articles/4408881937306#topic_n35_155_34b) for more information about end user accounts.

The steps you took in [Configuring user access
security and authentication](#topic_t45_ngs_v4b) to define password security and user authentication are
in place and apply to the users you add to your Zendesk account.

You use Support and the Admin Center to add users to your account.

### Launch tasks

| Create skills for routing \* | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_skills) | [Article](https://support.zendesk.com/hc/en-us/articles/4408838892826) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408883700122) | [Video](https://zendesk.wistia.com/medias/oyqkjlazc1) |
| Add agents | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_agents) | [Article](https://support.zendesk.com/hc/en-us/articles/4408886939930) |  |  |
| Set agent roles and access |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408824375450) |  |  |
| Assign agents to skills \* | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_agents_skills) | [Article](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408883700122) | [Video](https://zendesk.wistia.com/medias/oyqkjlazc1) |
| Import end-users | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_end_users) | [Article](https://support.zendesk.com/hc/en-us/articles/4408893496218) |  |  |

\* Skills based routing is available in the Zendesk Suite Professional plan and above.

## Setting up your help center and creating your knowledge base

Earlier in [Defining your customer
support experience](#topic_grq_fgs_v4b) you set up the essential contact points for customers and
defined your support experience brand (or brands). To complete your customer support
experience, you now need to set up your help center and create your knowledge base.

Your help center is one of your customers’ support contact points. It’s where
they can submit support requests, track their support requests, interact with agents via
messaging, and also use the self-service you provide via your knowledge base
articles.

Providing a help center is optional (you could instead embed your Zendesk support
experience into a website or a mobile app, for example). Having a knowledge base is an
essential part of the embedded support experience, of deflecting tickets, and the key to
automating support conversations using AI agents and messaging. Your knowledge base is also
just as valuable to your agents as it is to your customers.

To complete your customer support experience, you now need to set up your help center and
create your knowledge base.

You can leave your help center in setup mode, meaning not available to end users, until
you’re ready to launch the other parts of your Zendesk support solution. When you’re ready
to go live with your help center, see [Going live to customers](#topic_b2v_cms_v4b)
below.

### Launch tasks

**Configuring Knowledge user roles, access, and permissions**

You can define roles for agents that are specific to accessing, creating, and managing
content. For example, you can make agents Knowledge admins so that they can create content and
manage your help center.

| Set Knowledge roles for agents |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408845823386) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408827842458) |  |
| Create user segments |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408837707290) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408827797274) |  |
| Create management permissions |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408827952538) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408827797274) |  |

**Designing your help center**

Each help center comes with a standard theme that you can modify to match your company or
organization’s branding. You can also go deeper into the underlying help center code to
create more complex customizations.

| Brand your help center |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408824139546) | [Advice](https://www.pinterest.com/zendesk/beautiful-help-centers-built-with-zendesk-guide/) |  |
| Customize your help center |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408839332250) | [Advice](https://support.zendesk.com/hc/en-us/community/posts/203191573) |  |

**Creating your content structure and adding articles**

Your knowledge base consists of articles that are organized into categories and sections.
Categories are the top-level organizing containers in your help center. They contain
sections that contain your knowledge base articles. For example My Product > Getting
Started > Getting Started articles.

| Add categories and sections |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408845897370) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408883031706) |  |
| Add knowledge base content |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408839258778) | [Advice](https://support.zendesk.com/hc/en-us/articles/7849915550618) |  |

**Setting up publishing workflows for staff-created content**

In addition to allowing agents to create content, you can also control how and when the
content that they create is published. Available in the Agent Workspace, the Knowledge
section of the Context panel enables agents to easily access and link to articles in your
knowledge base. It also allows them to flag articles for updates and create new articles
for content gaps. You can create workflows to control how that agent content is
published.

| Flagging articles \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408826160922) |  |  |
| Set team publishing workflows \*\* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408832609562) | [Advice](https://www.zendesk.com/resources/leverage-entire-team-create-best-self-service-content/) | [Video](https://zendesk.wistia.com/medias/d5ufuuwanb) |

\* Available in Zendesk Suite Growth, Professional, Enterprise, and Enterprise
Plus plans

\*\* Available in Zendesk Suite Enterprise and Enterprise Plus plans

**Creating and managing a user community**

You can add a community to your help center. This allows your end users to create posts
to ask questions, provide feedback, and to share best practices with other end users in
your community. End users can also add comments to posts and articles. As with
staff-created content, you can also control how this content is published. This moderation
feature, along with the other spam prevention tools provided by Zendesk, allows you to
ensure that only quality content is published to your help center.

| Create a community |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408833845786) | [Advice](https://support.zendesk.com/hc/en-us/community/posts/212963027) |  |
| Configure content moderation |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408894193562) |  |  |

**Final steps before launching your help center**

With your help center design complete and your knowledge base content created and ready
for use, you’re ready to activate it to make it available to your customers. There are
several tasks however that you may also want to do before going live. You may want to
customize the web address (URL domain name) and also set up [Google Analytics](https://support.zendesk.com/hc/en-us/articles/4408828643098) so that you can track typical website usage
and engagement metrics.

| Customize your domain |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408838571930) |  |  |
| Set up Google Analytics |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408828643098) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408828643098) |  |

## Automating support with autoreplies

One of the many advantages of creating a knowledge base is that you can then use it to
provide automated customer support. This is done using autoreplies, powered by Zendesk bots,
which can be set up to automatically respond to incoming support requests via email or
webforms with links to related articles in your knowledge base. that should be able to help
the customer solve their support issue on their own. The bot scans the words used in the
support request and then chooses the appropriate articles to recommend.

Autorepliescan also be used in your web forms, your mobile apps, in web and mobile
messaging (described in the next section), and other places. For more information, see [Understanding everywhere you can use Zendesk bots](https://support.zendesk.com/hc/en-us/articles/4408821281818).

### Launch tasks

| Activate and enable autoreplies |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408820349850) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882682010) |  |
| View and manage autoreply settings |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408821295898) |  |  |

You'll also need to create business rules to define how and when to use autoreplies.
You'll find that launch task in the [Defining ticket routing and workflows](#topic_kpm_nls_v4b)
section below.

## Setting up the web and mobile messaging channels

Because of the importance of self-service and its positive effect on customer
satisfaction, and the convenience and cost savings of automation, you should consider
setting up messaging and adding a bot as your first responder to support requests received
through the Web Widget or mobile channels. Together these two features help customers to
find the answers to their support issues before needing to connect with an agent.

When you set up a messaging channel, you can design a default response that
greets customers when they launch the Web Widget through your website or help center, or
when they request assistance through your mobile app. The response requests information about them and their
support topic, and suggests articles (if available) that may help them self-solve their
issue.

You can choose to add a conversation bot to your web or messaging channel that
prompts customers to tell messaging what they need and provides them with options: simple
responses to answer their questions, links to knowledge base articles that should help them
to resolve their issue, or an option to contact a live agent. You can
customize the bot to your specifications by designing custom answer flows.

Messaging therefore offers two paths for issue resolution: automated messaging
conversations and also live agent conversations. Agents also have the option to contact the
customer using other channels such as email and voice.

First you create a messaging channel, then you can add a bot that presents the
knowledge base articles or custom answers, organize and create support request notification
rules for agents, and give agents access to work on messaging conversations.

### Launch tasks

| Customize and configure the Web Widget for messaging |  | [Article](https://support.zendesk.com/hc/en-us/articles/4409103246874) |  |  |
| Customize and configure messaging for Android and iOS apps |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408834810394) |  |  |
| Add a conversation bot to your messaging channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408824263578) |  |  |
| Customize the bot with answers |  | [Article](https://support.zendesk.com/hc/en-us/articles/4422584657434) |  |  |
| Route messaging tickets and notify agents |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408829019162) |  |  |
| Give your agents access to messaging |  | [Article](https://support.zendesk.com/hc/en-us/articles/6073485578010) |  |  |

The last step is to go live with messaging in your embedded support experience on a
website, your help center, or in mobile apps. Those steps are described in [Going live to customers](#topic_b2v_cms_v4b) below.

## Setting up the voice channel

Agents can initiate a voice channel conversation with customers in the Agent
Workspace, via messaging, and also take incoming calls directly when you provide your
support phone number (or numbers) to your customers (for example, via a link in your help
center or website).

The up front set up of your voice channel in Zendesk involves adding one or more
phone numbers that you’ll provide to your customers, setting up your voice greeting,
configuring voicemail settings, enabling SMS text messaging, and so on.

### Launch tasks

**Enabling the voice channel, adding telephone numbers, assigning agents**

| Prepare your network |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408831417498) |  |  |
| Understand Zendesk number availability |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408846483482) |  |  |
| Enable the voice channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408838035866) |  |  |
| Give your agents access |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408882966170) |  |  |
| Add telephone numbers |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408824192026) |  |  |
| Add address |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408824192026#topic_mqn_mc5_gv) |  |  |

**Configuring global voice settings**

| Configure general settings |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408838035866) |  |  |
| Create greetings |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408821594650) |  |  |
| Configure interactive voice response (IVR) \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408885628698) |  |  |

**Number settings**

| Configure individual number settings |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408823877146) |  |  |
| Set up an overflow number |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408832017690) |  |  |
| Configure voicemail options |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408831899930) |  |  |
| Enable callback |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408884087706) |  |  |
| Set up a failover number |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408881907994#topic_fkr_j2d_yt) |  |  |
| Enable Text for SMS support |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408823877146#topic_gcs_vf3_ccb) |  |  |

\* Available in Zendesk Suite Professional plans and above

The final step is to make your voice channel live to your customers, which is described
in [Going live to customers](#topic_b2v_cms_v4b) below.

## Defining ticket routing and workflows

With enough of the building blocks in place, you can now set up your workflows
and how incoming and updated tickets will be handled in Support. This is where you’ll start
defining your business rules: automating the routing of tickets to specific groups of agents
(for example) and creating views of your tickets based on various criteria (by channels, by
groups, and so on).

If your Zendesk Suite plan includes skills based routing, this is the first thing
you should set up because you’ll use these skills in the business rules you create with
triggers and automations, for example. If your plan does not include skills based routing,
you can easily assign tickets to agents and groups using other methods.

If you’re not already familiar with the routing and workflow tools in Zendesk,
here’s a quick summary:

- **Triggers** are event-based business rules you define that run
  immediately after tickets are created or updated. For example, a trigger can
  automatically assign a high priority to tickets received from VIP customers.
- **Automations** are time-based business rules that perform an action in
  your account based on time elapsed. For example, if a ticket hasn’t been answered in a
  timely manner, an automation can escalate the priority level and notify a manager.
- **Views** dynamically organize tickets based on specific criteria that you
  define. For example, you can create a view for unassigned tickets received over 24 hrs
  ago. You can create views that are shared with all agents and agents can create their
  own personal views of their tickets.
- **Macros** are a predefined set of actions that agents apply to a ticket
  with one click. You create macros for support requests that can be answered with a
  single, standard response.
- **Service Level Agreements** (SLAs) are contracts between you and your
  customers – a promise to respond to and resolve tickets in a certain amount of time.
  SLAs enable agents working with tickets to see the time remaining before each ticket is
  overdue, which makes it easy for them to prioritize.

For an overview of your ticket routing options, see [Routing options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650).

You set up your workflows and how incoming and updated tickets will be handled in
Support.

### Launch tasks

| Create triggers | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_triggers) | [Article](https://support.zendesk.com/hc/en-us/articles/4408886797466) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#triggers) | [Video](https://zendesk.wistia.com/medias/7i9j14lkvl) |
| Set up triggers to route messaging conversations to your live agent group(s) |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408829019162) |  |  |
| Creating and managing triggers for autoreplies |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408825385242) |  |  |
| Create automations | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_auto) | [Article](https://support.zendesk.com/hc/en-us/articles/4408883801626) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#automations) | [Video](https://zendesk.wistia.com/medias/7i9j14lkvl) |
| Create views | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_views) | [Article](https://support.zendesk.com/hc/en-us/articles/4408888828570) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#views) |  |
| Create macros | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_macros) | [Article](https://support.zendesk.com/hc/en-us/articles/4408844187034) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#macros) |  |
| Create SLA policies | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_SLA) | [Article](https://support.zendesk.com/hc/en-us/articles/4408829459866) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#sla) | [Video](https://zendesk.wistia.com/medias/q4d4eckf6c) |

## Training your agents

The Agent Workspace is the ticket interface where your agents manage all
support requests for all of the communication channels you set up (email, voice,
messaging, and so on).

Before you launch your support solution, you should train your agents to use the Agent
Workspace using these helpful agent guide articles.

- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)
- [Managing unified conversations](https://support.zendesk.com/hc/en-us/articles/4408823962906)
- [Receiving and sending messages](https://support.zendesk.com/hc/en-us/articles/4408843683226)
- [Composing messages](https://support.zendesk.com/hc/en-us/articles/4408831849882)
- [Receiving and placing calls](https://support.zendesk.com/hc/en-us/articles/4408844104986)
- [Translating conversations](https://support.zendesk.com/hc/en-us/articles/4408832500506)

The complete agent guide is available in [Agent Guide for Support](https://support.zendesk.com/hc/en-us/categories/5021364328218). There you and your agents will find
all the information needed to manage and solve tickets.

The Zendesk Training team
also provides a series of free agent training courses that you can find [here](https://training.zendesk.com/series/zendesk-agents).

## Testing before going live

Aside from your customer-facing production instance of your Zendesk account, most
Suite accounts also have access to a test environment instance known as the sandbox. The
Enterprise and Enterprise Plus plans includes two sandboxes, and Growth plans and above can
purchase sandbox environments as an add-on.

Use the sandbox instance to test parts of your Zendesk setup before going live to
customers, such as your email templates, your branding, and your channels, for example.
Because sandboxes replicate your configurations and ticket data, you can also test
workflows, experiment with integrations, and provide training for new agents in an
environment that closely mirrors your production environment.

### Launch tasks

| Create a sandbox |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408822049818) |  |  |
| Use the sandbox to test changes |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408824434586) |  |  |

## Going live to customers

Going live means activating your help center, making your embedded
support experience visible to customers, and directing external support contact points to
your Zendesk account (for example, forwarding email messages sent to any existing email
address to your new Zendesk support email address).

You’re now ready to make your support solution available and visible to your customers.

### Launch tasks

| Activate email forwarding | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_email_forward) | [Article](https://support.zendesk.com/hc/en-us/articles/4408886828698) |  |  |
| Configure voice channel call forwarding |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408823796890#topic_imk_g3r_rx) |  |  |
| Activate your help center |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ckn_wc4_qy) | [Advice](https://support.zendesk.com/hc/en-us/community/posts/203459886) |  |
| Embed messaging into your help center or website |  | [Article](https://support.zendesk.com/hc/en-us/articles/4500748175258) |  |  |
| Embed messaging into an iOS or Android app |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408834810394#topic_ig1_2sq_gnb) |  |  |

## Adding social messaging channels

If you also use social media messaging to communicate with your customers, you
can set those up as channels when you’re ready to go live. You can add Facebook, X (formerly Twitter),
WhatsApp, LINE, and WeChat. When customers send messages to these channels, the messages
become tickets and agents can respond to messages from these third-party channels. Facebook
Messenger, WhatsApp, and Instagram DM can be linked to your Web Widget to continue messaging
conversations across platforms, and you can add social media buttons to your emails.

You can also add Viber, Telegram, and Apple Messages for Business using Sunshine
Conversations, which is part of the Sunshine developer platform that is included in Zendesk
Suite.

You can add popular social media channels in the Admin Center.

### Launch tasks

| Add the X (formerly Twitter) DM channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408832388250) |  |  |
| Add the WhatsApp channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408842821786) |  |  |
| Add the Facebook Messenger channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408835753370) |  |  |
| Add the WeChat channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408820034970) |  |  |
| Add the LINE channel |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408844138394) |  |  |
| Add Sunshine Conversations channels |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408836484378) |  |  |
| Link social channels to the Web Widget |  | [Article](https://support.zendesk.com/hc/en-us/articles/4409103296154) |  |  |
| Add social channel buttons to emails |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408826273178) |  |  |

## Monitoring performance with reporting and analytics

When your Zendesk support solution is live, you can begin tracking the many important
customer support metrics that reveal how you’re doing providing support to your customers
and also how your staff are handling the ticket volume.

In-depth reporting and analytics is provided by Zendesk Explore. Explore provides prebuilt
dashboards and reports for the different Zendesk products. On the Professional, Enterprise,
and Enterprise Plus versions of Zendesk Suite, you can also create your own reports and
dashboards.

You first need to activate Explore and then give the agents you choose access to use it.
For a detailed introduction to Explore, see [Getting started with Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618).

Finally, you can use the many Explore recipes that have been created to help you set up
queries and dashboards for many common business scenarios. See [Explore recipes reference](https://support.zendesk.com/hc/en-us/articles/4409149172890).

In addition, there is a live activity dashboard for monitoring activity for the voice
channel. See [Analyzing call activity with the Talk dashboard](https://support.zendesk.com/hc/en-us/articles/4408831823514).

### Launch tasks

| Activate Explore |  | [Article](https://support.zendesk.com/hc/en-us/articles/4799941569690) |  |  |
| Give your agents access to use Explore |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408836002970) |  |  |
| Create Explore queries and dashboards \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4409149172890) |  |  |

## Providing global support

If your customers span the globe, so can the support your provide to them. This means
operating in the time zones and languages of your customers and also providing a fully
translated language experience for both your customers and your agents and admins.

You can configure your Zendesk to operate in specific locales and languages and you can set
your business hours accordingly. You can also set up business rules to ensure that support
is managed in a 24/7, follow-the-sun model.

Both the admin and agents interfaces and the customer facing elements of your support
solution can be viewed in multiple languages. Also, your custom content (words contained in
your business rules, in your help center interface, and in your knowledge base articles) can
also be easily translated to other languages.

### Launch tasks

| Configure your Zendesk to use a follow-the-sun model |  |  | [Advice](https://support.zendesk.com/hc/en-us/articles/4409155876762) |  |
| Configure Support for your locale and language |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408887059866) |  |  |
| Set business schedules | [Intro](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_sched) | [Article](https://support.zendesk.com/hc/en-us/articles/4408842938522) | [Advice](https://support.zendesk.com/hc/en-us/articles/4408882066202#schedules) | [Video](https://zendesk.wistia.com/medias/emkgin709o) |
| Add multiple languages to Support \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408888770714) |  |  |
| Provide multiple language support with dynamic content \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408882999066) |  |  |
| Configure your help center to support multiple languages \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408827609882) |  |  |
| Localize help center content \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408834328090) |  |  |
| Set up automatic translation for messaging conversations |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408842754202) |  |  |

\* Available in Zendesk Suite Growth plan and above

## Boosting agent and team productivity

In addition to the workflow and channel management efficiency of the Agent Workspace, you
can also enable a number of other features and install a number of Support apps to help
improve agent and team productivity. This includes agent collaboration, collaboration with
external resources, agent knowledge sharing, and by providing data and insight into the
context of a customer's previous interactions with your support team and help center
resources.

### Launch tasks

| Set up agent collaboration using CCs, followers, and @mentions |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408822451482) |  |  |
| Enable side conversations \* |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408844206746) |  |  |
| Install the Knowledge Capture app |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408822031898) |  |  |
| Install the Slack app |  | [Article](https://www.zendesk.com/apps/support/slack/) |  |  |
| Install the User Data app |  | [Article](https://www.zendesk.com/apps/support/user-data/) |  |  |
| Install the Time Tracking app |  | [Article](https://www.zendesk.com/apps/support/time-tracking/) |  |  |
| Install the Show Related Tickets app |  | [Article](https://www.zendesk.com/apps/support/show-related-tickets/) |  |  |

\* Available in the Zendesk Suite Professional plan and above

## Retaining and growing your customer base

Ensuring that you have satisfied customers will not only help to retain them, but also to
help expand your customer base. There are several aspects to this.

First, you need to ask your customers how you're doing in providing them with support. You
do this by enabling CSAT surveys, which are sent to customers after their ticket has been
solved. They can also be prompted to provide feedback after concluding messaging and live
chat sessions.

You can also be proactive by popping up a chat window when customers visit your help center
or website and by proactively creating tickets to inform customers of service disruptions or
to notify them of subscription renewals (just two examples of the many ways you might use
this feature).

Finally, Explore provides you with many essential customer support metrics that help to
track and react to customer satisfaction, agent and team performance, and data that may
serve as warning signs for customer churn.

### Launch tasks

| Enable CSAT (customer satisfaction) rating |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408886173338) |  |  |
| Install the Proactive Tickets app |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408828120218) |  |  |
| Use Explore to track metrics that improve customer support |  | [Article](https://support.zendesk.com/hc/en-us/articles/4408832234394) |  |  |

\* Available in Enterprise and Enterprise Plus plans

\*\* Available as a paid add-on to the Zendesk Suite Growth plan and above
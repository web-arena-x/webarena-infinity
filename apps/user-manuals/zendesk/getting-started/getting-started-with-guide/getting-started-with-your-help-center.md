# Getting started with your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408846795674-Getting-started-with-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can create a help center to provide end users with a complete self-service support option and
empower agents to better help customers. A help center includes:

- Branded customer-facing support site
- Knowledge base, for publishing self-service content
- Community, for customer collaboration (available on Suite Professional)
- Customer portal, where customers submit tickets and also manage their
  tickets (ticket management is not available on Suite Team)

Your end users can use the information in the knowledge base or turn to the community (if
available) for answers. If they can't find an answer, they can submit a request to
an agent. Agents can use the knowledge base to help solve tickets faster.

Note: You must be the account owner to enable the help center.

This article covers the following topics:

- [About the knowledge base
  structure](#topic_ol5_3fd_43)
- [Enabling help center in setup
  mode](#topic_ndf_fpf_mk)
- [Preparing your help center for release](#topic_bbn_vc4_qy)
- [Activating your help center](#topic_ckn_wc4_qy)

Tip: Check out the [Self-service learning path](https://training.zendesk.com/page/zendesk-course-catalog#product_guide) to gain the knowledge you need to
successfully set up your help center and start achieving your customer experience
goals.

## About the knowledge base structure

Use the knowledge base for the official content provided by your company or organization.
The help center consists of categories, sections, and articles.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_knowledge_base_structure.png)

On Enterprise plans, you can add subsections to your knowledge base to create more levels,
see [Adding subsections to create more levels in your help center](https://support.zendesk.com/hc/en-us/articles/4408834687130).

**Category**

Categories are the top-level organizing containers of the help center.
Categories contain sections. The help center must have at least one category. If you
have only one category in your help center, then the category itself is hidden to end
users, and they see only the sections in your help center.

Note: A category must have at least one section visible. A section will not be visible until
an article is added.

**Section**

Sections contain related articles. To add a section, you must have at least one
category to act as its parent container, except on Enterprise plans. On Enterprise
plans, sections can also contain subsections, so a section can be a child of a category
or a section, whereas on other plans, each section must be a child of a category.

**Articles**

Articles are content items such as tech notes or help topics.

You can quickly change the look and feel of the help center using simple WYSIWYG tools. You
can easily change the way your content is organized too. You can also use HTML, CSS,
JavaScript (see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250)). Code editing is
not available for Suite Team.

## Enabling help center in setup mode

You can enable your help center to begin building your knowledge base. While your
help center is in setup mode, end users can’t see it. This gives you a chance to
make it look just how you want before you activate it.

**To enable help center in setup mode**

1. Click the **Zendesk Products** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/product_tray_icon.png)) in the top bar, then select
   **Knowledge**.

   Note: You must be the account owner to enable the help
   center.
2. In the page that appears, click **Get started**.

   If you don’t see this
   option, but instead your help center opens, it means your help center has
   already been enabled.

Your help center is created using the default theme. You can customize the theme and add content
while it's in setup mode. For next steps, see [Preparing your help center
for release.](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_bbn_vc4_qy)

## Preparing your help center for release

While your help center is in setup mode, you can prepare it for release. During this time,
end users cannot view your help center.

These are some of the steps you can take to prepare your help center.

Tip: Developers can use a REST API to insert, update, and manage content in help
center. See the [Help center API documentation](https://developer.zendesk.com/api-reference/help_center/help-center-api/introduction/). For help on getting started, see
our [Developer resources for help center](https://support.zendesk.com/hc/en-us/articles/4408836300570).

**To prepare your help center for release**

1. Do some planning for how you will build and launch your help center. See Lisa Painter's
   [Fine tuning: "Blueprinting" your help center](https://support.zendesk.com/hc/en-us/articles/4408834707738).

   Be sure to
   check out the [Pinterest page of beautiful help centers](https://www.pinterest.com/zendesk/zendesk-help-center/) for inspiration.
2. Adjust the look and feel of the help center in setup mode.

   - Brand your help center by adding your product logo and your brand's colors and
     web fonts. See [Branding your help center](https://support.zendesk.com/hc/en-us/articles/4408824139546).
   - Customize your help center (not available on Suite Team). If you're a web
     designer or a web-savvy administrator, you can make more extensive customizations
     by editing the page code (see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250)). Also, check out the [Help center tips from our community](https://support.zendesk.com/hc/en-us/community/posts/203458536).
3. Test your help center.

   Only agents and administrators can access the help center while
   it's in setup mode. To see what your help center looks like to end users, see [Previewing your help center](https://support.zendesk.com/hc/en-us/articles/4408845893274).

   Be sure to test in
   different browsers. See the list of [browsers supported by help center](https://support.zendesk.com/hc/en-us/articles/4408823994778).
4. Set the display name for your help center.

   The display name can be the same as your
   subdomain or different. The name appears in the footer of the standard Copenhagen theme
   ([see Changing the name of your help center](https://support.zendesk.com/hc/en-us/articles/4408839398554)).
5. Ensure that your default language is properly set for your help center.

   It is
   important to set your default language *before* you add any articles to your help
   center, as the source locale for your articles defaults to your default help center
   language. A mismatch between the default language and the language you select for your
   articles could cause your content to not appear.

   Your help center default
   language is initially determined by the default language setting for your account in the
   Support admin (see [Configuring the default language for your help center](https://support.zendesk.com/hc/en-us/articles/4408822162330)).
6. Add your content to the help center.

   - Migrate content from an existing knowledge base or community, if you want (see
     [Migrating existing content to help
     center](https://support.zendesk.com/hc/en-us/articles/4408828053146)).
   - Create knowledge base categories and sections (see [Organizing your help center knowledge base content in categories and
     sections](https://support.zendesk.com/hc/en-us/articles/4408845897370)).

     If you migrated content from another system, you won't need to create categories
     and sections, unless you want to add any.
   - Add articles (see [Working with articles in the knowledge base](https://support.zendesk.com/hc/en-us/articles/4408839258778)).

     If you're starting from scratch, check out [Best
     practices: Finding issues to populate your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408828230554). If you need an
     easy way to back up your knowledge base articles, check out the [kBackups app](https://support.zendesk.com/hc/en-us/community/posts/210927837) in our community.
   - Create user segments to restrict access to content as you'd like (see [Creating user segments to restrict help center access](https://support.zendesk.com/hc/en-us/articles/4408837707290)).
     This feature is not available on Suite Team.
7. Set up your help center to support multiple languages (this requires Suite Growth or
   above *or* Support Professional or Enterprise with Knowledge).

   - Decide what content you want to translate and how (see [Creating and managing translated content for your knowledge
     base](https://support.zendesk.com/hc/en-us/articles/4408886903450)).
   - Enable languages for your help center (see [Configuring your help center to support multiple
     languages](https://support.zendesk.com/hc/en-us/articles/4408827609882)).
   - Create localized versions of your help center content (see [Localizing the help center](https://support.zendesk.com/hc/en-us/articles/4408834328090)).
8. Add any Knowledge admins (see [Understanding Knowledge roles and setting permissions](https://support.zendesk.com/hc/en-us/articles/4408827842458)).

When you are ready to go live, you can activate your help center.

## Activating your help center

When you're ready, you can activate your help center and make it live for end users. You must be
a Zendesk Support administrator to activate the help center. Knowledge admins who are
not Support admins cannot enable the help center.

Tip: Check out [Fine tuning: Best practices for ticket deflection](https://support.zendesk.com/hc/en-us/articles/4848867878682) for tips on how to best promote self-service during your help center launch.

**To activate your help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. In **Help center settings**, click **Activate**.
3. Click **Activate** again to confirm that you want to activate your help center.

Your help center is activated and is now visible to end users. If you need to disable your help
center, see [Deactivating your help
center](https://support.zendesk.com/hc/en-us/articles/4408829088026).

Note: If you are using the community, make sure that is also
activated. See [Getting started with
Community](https://support.zendesk.com/hc/en-us/articles/4408882689306).

Next steps: Be sure to check out our [Help center guide for end users](https://support.zendesk.com/hc/en-us/articles/4408837910426) and also our complete
list of [Knowledge resources](https://support.zendesk.com/hc/en-us/articles/4408823842842).
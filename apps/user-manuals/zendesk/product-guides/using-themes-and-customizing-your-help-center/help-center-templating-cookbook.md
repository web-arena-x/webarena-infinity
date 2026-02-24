# Help center templating cookbook

Source: https://support.zendesk.com/hc/en-us/articles/4408832681626-Help-center-templating-cookbook

---

Each help center theme consists of a collection of editable page templates and custom pages. You can use the help center templating language, Curlybars, to access help center data and manipulate the content in your pages.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Each help center theme consists of a collection of editable page templates and custom pages.
You can use the help center templating language, Curlybars, to access help center data and
manipulate the content in your pages.

This article provides a list of recipes with code snippets you can use. Keep in mind that,
some of the functionality in these recipes might already be in your help center, depending on
whether you are using [a standard theme or a customized theme](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and the date you enabled your
help center.

Trial users are given the Professional plan, which includes code editing options, but they
will no longer be able to access that feature if they purchase Suite Team.

Note: This article is for instructional purposes only. Zendesk Customer Support does not
support or guarantee custom code.

This article covers the following topics:

- [About the Curlybars templating
  language](#topic_tdd_zhw_1x)
- [Customize page templates for specific
  categories, sections, or articles](#topic_osm_kmn_4v)
- [Customize the language names in the
  language selector](#topic_fvh_xxn_4v)
- [Hide one or more languages in the language
  selector](#topic_gml_414_4v)
- [Let users sort article comments by date or
  votes](#topic_yhc_nfg_x5)
- [Add a formatting toolbar to the article
  comment editor](#topic_bb5_2jf_x5)
- [Enable users to vote on article
  comments](#topic_eb2_grf_x5)
- [Add Instant Search (autocomplete) results
  to your help center](#topic_xqw_dd1_cw)
- [Add Federated Search to include external content in help center search](#topic_tn4_sgw_frb)
- [Add generative search results to your custom theme](#topic_tjl_xqc_42c)
- [Add the new request list experience to your custom theme](#topic_h4p_wbj_jhc)
- [Add sorting for subscription types in the
  My Activities Following page](#topic_ljq_jch_jw)
- [Add sorting options “created at” and
  “updated at” for requests in My Activities](#topic_nbr_ytj_dx)
- [Add Follow/Unfollow for users in a shared
  organization](#topic_ccb_5g1_qw)
- [Add ability for users to CC other users on
  support requests](#topic_2hj_jqw_1x)
- [Add a link on follow-up requests to the
  parent request](#topic_why_ysj_dx)
- [Enable CSAT for solved tickets on the
  Customer Portal](#topic_nl4_tnx_ycc)
- [Add voting buttons to articles](#topic_bjk_fdq_4y)
- [Add content tags to articles and
  posts](#topic_bzl_b23_kvb)
- [Add badges to your custom help center
  theme](#topic_tg5_cqx_xmb)
- [Enable users to view user profiles to your help center](#topic_tq5_fn1_sgb)
- [Enable subsections in your help center theme](#topic_k23_2bj_chb)
- [Add sidebar filters and results for multiple help centers to the search results page](#topic_ykx_gms_y3b)
- [Adding the spam filter to help center](#topic_hcb_nws_l4)
- [Adding approvals to your help center](#topic_xrf_2r4_yfc)
- [Adding the service catalog to your help center](#topic_r3w_fr4_yfc)

## About the Curlybars templating language

Your help center is built on a theming framework that includes its own templating language
for advanced customizations. Each help center theme consists of a collection of editable
templates and optional custom pages[.](https://support.zendesk.com/hc/en-us/articles/4408839332250-Customizing-Help-Center#topic_h5c_k4w_n3)

[Editable page templates](https://support.zendesk.com/hc/en-us/articles/4408839332250-Customizing-Help-Center#topic_h5c_k4w_n3) define the layout of each
page. For example, there's a template for knowledge base articles, a template for the list
of requests, and so on. A template is simply a text file to be rendered into an HTML page
when a user wants to see it. Each template consists of a mix of HTML markup and expressions
identifiable by double curly brackets such as `{{post.title}}`.

[Custom pages](https://support.zendesk.com/hc/en-us/articles/4409012911770) are built into the code base of your help center
theme and have a specific URL that you can link from anywhere in your help center. You can
use custom pages to create and code pages from scratch that meet your individual
requirements. For example, you can use custom pages to create special landing pages for your
help center or even create new pages to embed content from sources outside of Zendesk.

The templating language is named Curlybars and implements a large subset of the [Handlebars](http://handlebarsjs.com/) language.
But unlike Handlebars which renders on the client-side, Curlybars renders on the
server-side.

You can use the help center templating language to access help center data and manipulate
the content in your pages. In the following example, help center renders a list of names and
avatars of all the people who left comments on the page:

```
{{#each comments}}
  <li>
    <div class="comment-avatar">
      <img src="{{author.avatar_url}}" alt="Avatar" />
    </div>
    <div class="comment-author">
      {{author.name}}
    </div>
  </li>
{{/each}}
```

Previously you could use components to customize help center, but you could not customize
the components themselves, except for manipulating them with Javascript. With Curlybars you
can get access to the HTML that was previously hidden inside component and edit it.

For more information, see:

- [Help center templating language reference](https://developer.zendesk.com/apps/docs/help-center-templates/introduction)
- [Using the help center templating language](https://support.zendesk.com/hc/en-us/articles/4408824571674)
- [Customizing content with Curlybars](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_qp2_2tr_nt)

## Customize page templates for specific categories, sections, or articles

You can customize the Category, Section, and Article templates for specific categories,
sections, and articles respectively.

**Applicable templates**

- Category
- Section
- Article

**Recipe**

- Specify the category, section, or article id in a `is` block:

  ```
  {{#is id 200646205}}
    ...
  {{/is}}
  ```

**Example**

Inserting the following block in the Section template customizes the template for sections
200646205 and 203133596:

```
{{#is section.id 200646205}}
  <p><strong>This is important security information! Pay attention!</strong></p>
{{/is}}
{{#is section.id 203133596}}
  <p>Videos available at <a href="https://www.somelink.com">Learning to fly</a></p>
{{/is}}
```

**Reference**

- [is helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#is-helper)

## Customize the language names in the language selector

You can customize the language names in the language selector on every page of help center.
This is useful if you want to use one language variant, such as "English (U.S.)", for all
the language's variants, such as "English".

**Applicable template**

- Header

**Applicable expression**

- `{{#if alternative_locales}}...{{/if}}`

**Recipe**

- Replace the `{{current_locale.name}}` expression with the following
  conditional expression:

  ```
  {{#is current_locale.name 'English (US)'}}
    English
  {{else}}
    {{current_locale.name}}
  {{/is}}
  ```

  Also replace the alternative locale `{{name}}` expression with the
  following conditional expression:

  ```
  {{#is name 'English (US)'}}
    English
  {{else}}
    {{name}}
  {{/is}}
  ```

**Example**

```
{{#if alternative_locales}}
  <div class="dropdown language-selector" aria-haspopup="true">
  <a class="dropdown-toggle">
  {{#is current_locale.name 'English (US)'}}
    English
  {{else}}
    {{current_locale.name}}
  {{/is}}
  </a>
  <span class="dropdown-menu dropdown-menu-end" role="menu">
  {{#each alternative_locales}}
    <a href="{{url}}" dir="{{direction}}" rel="nofollow" role="menuitem">
    {{#is name 'English (US)'}}
      English
    {{else}}
      {{name}}
    {{/is}}
    </a>
  {{/each}}
  </span>
  </div>
{{/if}}
```

**Reference**

- [is helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#is-helper)

## Hide one or more languages in the language selector

Hiding a language in the language selector can be useful if the content in that language
isn't ready for release.

**Applicable template**

- Header

**Applicable expression**

- `{{#each alternative_locales}}...{{/each}}`

**Recipe**

- Replace the `<a href="{{url}}" dir="{{direction}}" rel="nofollow"
  role="menuitem"> {{name}} </a>` expression with the following
  conditional expression:

  ```
  {{#is name 'Français'}}
    {{! do nothing }}
  {{else}}
    <a href="{{url}}" dir="{{direction}}" rel="nofollow" role="menuitem">
    {{name}}
    </a>
  {{/is}}
  ```

**Example**

```
{{#each alternative_locales}}
  {{#is name 'Français'}}
    {{! do nothing }}
  {{else}}
    <a href="{{url}}" dir="{{direction}}" rel="nofollow" role="menuitem">
      {{name}}
    </a>
  {{/is}}
{{/each}}
```

**Reference**

- [is helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#is-helper)

## Let users sort article comments by date or votes

By default, article comments are sorted by date from the most recent to the least. You can
add Date and Votes links that users can click to sort the comments by date or by the number
of votes.

Note: The Date and Votes sorting links are available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after the
release of the new Community on November 30th, 2015.

**Applicable template**

- Article

**Applicable HTML element**

- `<section class="article-comments">...</section>`

**Recipe**

- Insert the following div tag after the comment section's heading tag,
  `<h2>{{t 'comments'}}</h2>`, preferably after the
  `{{#if comments}}` expression, if any, to ensure the sorters don't
  appear if nobody left comments yet:

  ```
  <div class="comment-sorter">
    Sort by: 
    {{#each comment_sorters}}
      <a aria-selected="{{selected}}" href="{{url}}">{{name}}</a>
    {{/each}}
  </div>
  ```

**Example**

```
<section class="article-comments">
  <h2>{{t 'comments'}}</h2>
    {{#if comments}}

    <div class="comment-sorter">
      Sort by: 
      {{#each comment_sorters}}
        <a aria-selected="{{selected}}" href="{{url}}">{{name}}</a>
     {{/each}}
    </div> 
     
    <ul class="comment-list">
      {{#each comments}}
      ...
```

**Reference**

- [comment\_sorters property](https://developer.zendesk.com/apps/docs/help-center-templates/article_page#available-properties)

## Add a formatting toolbar to the article comment editor

You can add a formatting toolbar to the editor for article comments. Users can add bold and
italics, unordered or ordered lists, images, and links.

Note: The formatting toolbar is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after the
release of the new Community on November 30th, 2015.

**Applicable template**

- Article

**Applicable object**

- `{{#form 'comment'}}...{{/form}}`

**Recipe**

- Find and replace the `{{textarea 'body'}}` expression in the form
  object with `{{wysiwyg 'body'}}`

**Example**

```
{{#form 'comment' class='comment-form'}}
  <div class="comment-avatar">
    {{user_avatar class='user-avatar'}}
  </div>

  <div class="comment-container">
     {{wysiwyg 'body'}}
     <div class="comment-form-controls">
       {{input type='submit'}}
     </div>
  </div>
{{/form}}
```

**Reference**

- [wysiwyg helper](https://developer.zendesk.com/apps/docs/help-center-templates/advanced_helpers#wysiwyg-helper)

## Enable users to vote on article comments

By default, users can vote on articles. You can also let them vote on article comments.

Note: The voting links are available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after the
release of the new Community on November 30th, 2015.

**Applicable template**

- Article

**Applicable expression**

- `{{#each comments}}...{{/each}}`

**Recipe**

- Insert the following div tag after the `<li id="{{anchor}}">` tag:

  ```
  <div class="comment-vote vote">
    {{vote 'up' class="article-vote-up" selected_class="vote-voted"}}
    {{vote 'sum' class="article-vote-sum"}}
    {{vote 'down' class="article-vote-down" selected_class="vote-voted"}}
  </div>
  ```

  The vote helpers above borrow the CSS classes for articles votes to style the
  comment vote links. You can define your own classes to style the comment
  votes.

**Example**

```
{{#each comments}}
  <li id="{{anchor}}" class="comment">

  <div class="comment-vote vote">
    {{vote 'up' class="article-vote-up" selected_class="vote-voted"}}
    {{vote 'sum' class="article-vote-sum"}}
    {{vote 'down' class="article-vote-down" selected_class="vote-voted"}}
  </div>
  
  <div class="comment-avatar {{#if author.agent}} comment-avatar-agent {{/if}}">
    <img src="{{author.avatar_url}}" alt="Avatar">
  </div>
  ...
```

**Reference**

- [vote helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#vote-helper)

## Add generative search results to your custom theme

Generative search provides AI-generated answers to search queries within your help center.
Generative search provides users who are performing searches in the help center with answers
to their questions, without requiring them to click through multiple search results.

Note: Generative search is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408845834522) released after March 26, 2025. If your help center
was created before March 26, 2025 and uses a customized theme, you must update your custom
theme to add generative search. Generative search is available for all templating API
versions. You can disable generative search, if needed, by deactivating it in your [search settings](https://support.zendesk.com/hc/en-us/articles/5589418656922).

Note: Based on your theme implementation and other factors, you may be
eligible to use the automatic theme updater for generative search. To learn more, see [Automatically updating your help center theme for generative search
(Beta).](https://support.zendesk.com/hc/en-us/articles/9809445946778)

After generative search is activated, it works by evaluating the questions users enter in
the help center search. The top matching articles and posts are evaluated by generative AI,
which then generates an answer. On Enterprise plans with [federated search](https://support.zendesk.com/hc/en-us/articles/4593564000410) configured, the generative AI also evaluates
external content and can be included in the answer. The generated answer is posted by
default at the top of the search results. See [Using generative search to provide AI-powered answers to search
queries](https://support.zendesk.com/hc/en-us/articles/8888178335898).

**Applicable template**

- Search results page (search\_results.hbs)

**Recipe**

- Add the `{{generative_answers}}` helper to the theme's
  search\_results.hbs template where you want the generative answers to appear.

**Example**

```
<section id="main-content" class="search-results-column">
{{generative_answers}}
<h1 class="search-results-subheading">
```

**Reference**

- [search\_results.hbs](https://github.com/zendesk/copenhagen_theme/blob/master/templates/search_results.hbs)
- [generative\_answers helper](https://developer.zendesk.com/api-reference/help_center/help-center-templates/advanced_helpers/#generative_answers-helper)

**To update your custom theme (Knowledge admins)**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   The Themes page opens.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_themes_edit_code_btn.png)
4. Under Templates, click **search\_results.hbs**.
5. Add the **{{generative\_answers}}** helper code to the theme's search\_results.hbs
   template where you want the generative answers to appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-gensearch-helper.png)
6. Click **Save**.
7. After activating, if you find that the Quick answer box UI doesn't match the fonts and
   colors of your custom theme, this could be due to one of the following:
   - You have the required settings in the theme settings interface. However, the
     settings values are not set to match your theme, because your theme's look and feel
     is hardcoded in your CSS file. To update the color and font settings, see [Branding your help center](https://support.zendesk.com/hc/en-us/articles/4408824139546).
   - You do not have some or all of the settings in the theme settings interface. If
     this is the case, you'll need to add the settings and set their values to match the
     rest of your theme. To do this, you can update your manifest.json file with the
     following identifiers from [Github](https://github.com/zendesk/copenhagen_theme/blob/master/manifest.json), replacing the value of each
     identifier with the font or color code that matches your theme:
     - Color settings identifiers:
       - text\_color
       - link\_color
       - hover\_link\_color
       - visited\_link\_color
     - Fonts settings identifiers
       - heading\_font
       - text\_font

## Add the new request list experience to your custom theme

When you enable the new request list experience in your theme, end users can use the new
combinable filtering options to refine the requests they want to manage as well as new
column configuration options to show or hide both system fields and custom fields. See [Submitting and tracking requests in the help center Customer
Portal.](https://support.zendesk.com/hc/en-us/articles/4408846805530)

Note: The new request list experience is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408845834522) released after February 2, 2026. If your help
center was created before February 2, 2026 and uses a customized theme, you must update your
custom theme to add the new request list experience functionality.

**Requests page template**

The request list UI is implemented in the [Copenhagen theme repository](https://github.com/zendesk/copenhagen_theme/tree/11e8049bea05e19b5c1791ca617fc8859d428307/src/modules/request-list) in the [request-list](https://github.com/zendesk/copenhagen_theme/tree/11e8049bea05e19b5c1791ca617fc8859d428307/src/modules/request-list) codebase. To customize the
request list experience, update the components in `request-list` and render
them from your theme’s requests page template.

In `templates/requests_page.hbs`, add a container element and
include a `<script type="module">` block that imports
`renderRequestList` from `request-list`, then render the
request list inside the container. The following example shows the required markup and
initialization code.

**Example**

```
<div id="main-content">
  </div>

<script type="module">
  import { renderRequestList } from "request-list"; 
  
  const container = document.getElementById("main-content"); 
  const settings = {{json settings}}; 

  const props = {   
    locale: {{json help_center.base_locale}},
    customStatusesEnabled: {{json help_center.custom_statuses_enabled}}
  }; 
  
  renderRequestList(settings, props, container);
</script>
```

To see the current implementation used by non-customized themes, review the [requests\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/4c76903fffc7e5918d065989c3728bfee19777a6/templates/requests_page.hbs#L21) template and the
`request-list` components in the Copenhagen theme repository.

**Reference**

- [the request-list codebase](https://github.com/zendesk/copenhagen_theme/tree/11e8049bea05e19b5c1791ca617fc8859d428307/src/modules/request-list)
- [Reference documentation](https://developer.zendesk.com/api-reference/help_center/help-center-api/introduction/)

## Add Instant Search (autocomplete search) results to your custom help center theme

You can display links to suggested articles as the user types in the Search box by adding
Instant Search to your custom theme.

Note: Instant Search is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after the
release Instant Search on July 5th, 2016. You can disable Instant Search, if needed, by
removing it from your theme.

When Instant Search is enabled, a maximum of six suggested articles appear as the user
types their search term in the Search box. Articles are matched for Instant Search based on
the article title only. The user can select matched articles directly from the Search box
without going to the search results page first.

**Applicable templates**

- Whichever template contains your Search expression (most often it's the Header or
  Home page template)

**Applicable expression**

- {{search}}

**Recipe**

- Add `instant=true` to the Search expression.

  ```
  {{search instant=true}}
  ```

**Example**

```
<div class="search-box">
  <h1 class="help-center-name">{{help_center.name}}</h1>
  {{search instant=true}}
</div>
```

## Add Federated Search to include external content in help center search

There are two parts to enabling Federated Search in your help center [Search Results template](https://developer.zendesk.com/apps/docs/help-center-templates/search_results_page):

- [Adding sidebar filters](#topic_rfw_1hw_frb)
- [Looping through the results](#topic_i21_3hw_frb)

### Adding sidebar filters

You need to update the search results template by updating the properties used in the
sidebar filters.

Update the following code in `<div
class="search-results">`.

```
<section class="search-results-sidebar">
{{#if source_filters}}
  <section class="filters-in-section collapsible-sidebar" aria-expanded="false">
    <button type="button" class="collapsible-sidebar-toggle" aria-expanded="false">
    </button>
    <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_source'}}</h3>
    <ul class="multibrand-filter-list multibrand-filter-list--collapsed">
      {{#each source_filters}}
        <li>
        {{#if selected}}
          <a href="{{url}}" class="sidenav-item current" aria-current="page">
        {{else}}
          <a href="{{url}}" class="sidenav-item">
        {{/if}}
            <span class="sidenav-subitem filter-name">{{name}}</span>
            <span class="sidenav-subitem doc-count">({{count}})</span>
          </a>
        </li>
      {{/each}}
      <buttonclass="see-all-filters"aria-hidden="true"aria-label="{{t'show_more_sources'}}">{{t'show_more_sources'}}</button>    </ul>
  </section>
{{/if}}
{{#if type_filters}}
  <section class="filters-in-section collapsible-sidebar" aria-expanded="false">
    <button type="button" class="collapsible-sidebar-toggle" aria-expanded="false">
    </button>
    <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_type'}}</h3>
    <ul class="multibrand-filter-list multibrand-filter-list--collapsed">
      {{#each type_filters}}
        <li>
        {{#if selected}}
          <a href="{{url}}" class="sidenav-item current" aria-current="page">
        {{else}}
          <a href="{{url}}" class="sidenav-item">
        {{/if}}
            <span class="sidenav-subitem filter-name">{{name}}</span>
            <span class="sidenav-subitem doc-count">({{count}})</span>
          </a>
        </li>
      {{/each}}
    </ul>
  </section>
{{/if}}
{{#if subfilters}}
  <section class="filters-in-section collapsible-sidebar" aria-expanded="false">
    <button type="button" class="collapsible-sidebar-toggle" aria-expanded="false">
    </button>
    {{#is current_filter.identifier 'knowledge_base'}}
      <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_by_category'}}</h3>
    {{/is}}
    {{#is current_filter.identifier 'community'}}
      <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_by_topic'}}</h3>
    {{/is}}
    <ul class="multibrand-filter-list multibrand-filter-list--collapsed">
      {{#each subfilters}}
        <li>
          {{#if selected}}
            <a href="{{url}}" class="sidenav-item current" aria-current="page">
          {{else}}
            <a href="{{url}}" class="sidenav-item">
          {{/if}}
            <span class="sidenav-subitem filter-name">{{name}}</span>
            <span class="sidenav-subitem doc-count">({{count}})</span>
          </a>
        </li>
      {{/each}}
      {{#is current_filter.identifier 'knowledge_base'}}
        <button class="see-all-filters" aria-hidden="true" aria-label="{{t 'show_more_categories'}}">{{t 'show_more_categories'}}</button>
      {{/is}}
      {{#is current_filter.identifier 'community'}}
        <button class="see-all-filters" aria-hidden="true" aria-label="{{t 'show_more_topics'}}">{{t 'show_more_topics'}}</button>
      {{/is}}
    </ul>
  </section>
{{/if}}
</section>
```

### Looping through the results

This snippet is an example of how you can use the `{{results}}` helper to
loop through the Federated Search results:

```
{{#if results}}
<ul class="search-results-list">
  {{#each results}}
	<li class="search-result-list-item result-{{type}}">
	  <h2 class="search-result-title">
		<a href="{{url}}" class="results-list-item-link"{{#if is_external}}
               target=”_blank” {{/if}}>
                     {{title}}
                     {{#if is_external}}
                       <svg viewBox="0 0 24 24" width="12px" height="12px" id="zd-svg-icon-12-new-window-fill"><path d="M 19.980469 2.9902344 A 1.0001 1.0001 0 0 0 19.869141 3 L 15 3 A 1.0001 1.0001 0 1 0 15 5 L 17.585938 5 L 8.2929688 14.292969 A 1.0001 1.0001 0 1 0 9.7070312 15.707031 L 19 6.4140625 L 19 9 A 1.0001 1.0001 0 1 0 21 9 L 21 4.1269531 A 1.0001 1.0001 0 0 0 19.980469 2.9902344 z M 5 3 C 3.9069372 3 3 3.9069372 3 5 L 3 19 C 3 20.093063 3.9069372 21 5 21 L 19 21 C 20.093063 21 21 20.093063 21 19 L 21 13 A 1.0001 1.0001 0 1 0 19 13 L 19 19 L 5 19 L 5 5 L 11 5 A 1.0001 1.0001 0 1 0 11 3 L 5 3 z"/></svg>
                     {{/if}}

</a>
	  </h2>
	  <article>
		<div class="search-result-icons">
		  {{#if vote_sum}}
			<span class="search-result-votes">{{vote_sum}}</span>
		  {{/if}}
		  {{#if comment_count}}
			<span class="search-result-meta-count">
			  {{comment_count}}
			</span>
		  {{/if}}
		</div>
		<ul class="meta-group">
		  <li>
			<ol class="breadcrumbs search-result-breadcrumbs">
			  {{#each path_steps}}
				<li title="{{name}}"><a href="{{url}}" target="{{target}}">{{name}}</a></li>
			  {{/each}}
			</ol>
		  </li>
		  <li class="meta-data">{{author.name}}</li>
		  <li class="meta-data">{{date created_at}}</li>
		</ul>
		<div class="search-results-description">{{text}}</div>
	  </article>
	</li>
  {{/each}}
</ul>
{{else}}
<p>
  {{t 'no_results_unified'}}
  {{#link 'help_center'}}
	{{t 'browse_help_center'}}
  {{/link}}
</p>
{{/if}}
```

## Add sorting for subscription types in the My Activities Following page

You can make it easier for users to view their subscriptions by enabling them to sort
subscriptions by type in the My Activities > Following page.

**Applicable templates**

- Following page

**Recipe**

- Under the `<nav>` tag, insert the following code:

  ```
  <div class="my-activities-following-header">
    <span class="dropdown">
      <span class="dropdown-toggle">
        {{current_filter.label}}
      </span>
      <span class="dropdown-menu" role="menu">
        {{#each filters}}
          <a href="{{url}}" aria-selected="{{selected}}" role="menuitem">
            {{name}}
          </a>
        {{/each}}
      </span>
    </span>
  </div>
  ```

## Add sorting options “created at” and “updated at” for requests in My Activities

You can add the sorting options “created at” and “updated at” for end-users on the request
page in My Activities.

Note: The “created at” and “updated at” sorting options are available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after August
2016.

**Applicable template**

- Request list page

**Recipe**

- Replace `{{t 'created'}}`
  with:

  ```
  {{#link 'requests' sort_by='created_at'}}{{t 'created'}}{{/link}}
  ```
- Replace `{{t 'last_activity'}}`
  with:

  ```
  {{#link 'requests' sort_by='updated_at'}}{{t 'last_activity'}}{{/link}}
  ```

**Reference**

- [requests link helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#requests-link)

## Add Follow/Unfollow for users in a shared organization

You can enable users to receive email notifications for requests in their shared
organization. The {{subscribe}} helper inserts a "follow" button that users can click if
they want to receive email notifications when requests are created or updated in their
shared organization. Users also have the option to unfollow if they no longer want to
receive updates.

Note: The Follow button for shared organizations is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after January
23th, 2016.

**Applicable template**

- Request list page

**Applicable object**

- `{{#form 'requests_filter'}}...{{/form}}`

**Recipe**

- Add the `{{subscribe}}` helper to the form object.

**Example**

```
{{#form 'requests_filter' class='request-table-toolbar'}}
  {{input 'query' id='quick-search' type='search' class='requests-search'}}
  <div class="request-table-filters">
    {{label 'organization' for='request-organization-select' class='request-filter'}}
    {{select 'organization' id='request-organization-select' class='request-filter'}}
    {{subscribe}}
    {{label 'status' for='request-status-select' class='request-filter'}}
    {{select 'status' id='request-status-select' class='request-filter'}}
  </div>
{{/form}}
```

**Reference**

- [subscribe helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#subscribe-helper)

## Add ability for signed-in users to CC other users on support requests

You can add the ability for signed-in users to add CCs to new and existing support requests
in your help center. When a CC is added to a support request, the copied user will receive
email notifications for ticket updates.

Note: The CC option is available for support requests by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after December
14th, 2015.

After you add the code to your custom theme, you must enable the feature (see [Setting CC permissions](https://support.zendesk.com/hc/en-us/articles/4408843795482#topic_x3t_4p5_cq)).

**Applicable template**

- Request page

**Applicable object**

- `{{#form 'comment' class='comment-form'}}...{{/form}}`

**Recipe**

- Insert the following snippet inside
  the comment form.

  ```
  {{#if help_center.request_ccs_enabled}}  
    <div class="comment-ccs">
       {{token_field 'ccs'
          class="ccs-input"}}
    </div>
   {{/if}}
  ```

## Add a link on follow-up requests to the parent request

You can display a link in a follow-up request to the parent request, if there is one.

Note: The link to the parent request in the follow-up request is available by default in
[standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after August
2016.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_followup_request_link.png)

**Applicable template**

- Request page

**Recipe**

- Add the following snippet to the Request page template where you want to display the
  link to the parent ticket, if one is present:

  ```
  {{#if request.followup_source_id}}
    <dl class="request-details">
      <dt>{{t 'followup'}}</dt>
      <dd>{{link 'request' id=request.followup_source_id}}
  </dd>
    </dl>
  {{/if}}
  ```

**Reference**

- [new request page](https://developer.zendesk.com/apps/docs/help-center-templates/new_request_page)

## Enable CSAT for solved tickets on the Customer Portal

You can use CSAT to collect feedback from end users via the Customer Portal.

Note: When CSAT is on, the CSAT option in the Customer Portal is available
by default in standard themes and in custom themes based on the Templating API [v3.2.0](https://github.com/zendesk/copenhagen_theme/releases/tag/v3.2.0) (released on February 8, 2024) or higher.

**Applicable template**

- Request page

**Recipe**

- Add a `{{#with satisfaction_response}}...{{/with}}` block to the
  request\_page.hbs template.

**Example**

- See the [Copenhagen theme request page.hbs](https://github.com/zendesk/copenhagen_theme/blob/e7fcde18dcf31608ba4ae16602e3f3e507e52aae/templates/request_page.hbs#L130) on GitHub.
- Add the following template
  code:

  ```
  {{#with satisfaction_response}}
    {{#with rating}}
  	<dl class="request-details">
  	  <dt>{{t 'rating'}}</dt>
  	  <dd>
  		<div>
  		  {{#is scale_type 'numeric'}}
  			{{t 'numerical_rating' value=value max_value=max_value}}
  		  {{else}}
  			{{scale_value}}
  		  {{/is}}
  		</div>

  		{{#link 'survey_response' id=../id}}
  		  {{#if ../editable}}
  			{{t 'edit_feedback'}}
  		  {{else}}
  			{{t 'view_feedback'}}
  		  {{/if}}
  		{{/link}}
  	  </dd>
  	</dl>
    {{else}}
  	{{#if editable}}
  	  <dl class="request-details">
  		<dt>{{t 'rating'}}</dt>
  		<dd>
  		  {{#link 'survey_response' id=id}}
  			{{t 'add_feedback'}}
  		  {{/link}}
  		</dd>
  	  </dl>
  	{{/if}}
    {{/with}}
  {{/with}}
  ```

**Reference**

- [`satisfaction_response`](https://developer.zendesk.com/api-reference/help_center/help-center-templates/request_page/#available-properties)

## Add voting buttons to articles

The vote buttons on articles are part of the standard Copenhagen theme. But if you don't
see the option to vote on your articles, you might have removed the buttons from your
theme.

The code to add voting buttons can vary from theme to theme, but this is the code from the
standard Copenhagen theme, in case you need it.

**Applicable template**

- Article

**Recipe**

- Add the following code to the Article Page template:

  ```
  {{#with article}}
    <div class="article-votes">
      <span class="article-votes-question">{{t 'was_this_article_helpful'}}</span>
      <div class="article-votes-controls" role='radiogroup'>
        {{vote 'up' role='radio' class='button article-vote article-vote-up'}}
        {{vote 'down' role='radio' class='button article-vote article-vote-down'}}
      </div>
      <small class="article-votes-count">
        {{vote 'label' class='article-vote-label'}}
      </small>
    </div>
  {{/with}}
  ```

## Add content tags to articles and posts

The standard Copenhagen theme displays content tags on article, community post, and search pages by default. If you're using a custom or marketplace theme, you may need to update your theme to display content tags on these pages. To get started, you can use the following template files from the Copenhagen theme as a guide:

- [article\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/v2.19.0/templates/article_page.hbs#L95:L108)
- [community\_post\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/v2.19.0/templates/community_post_page.hbs#L127:L141)
- [new\_community\_post\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/v2.19.0/templates/new_community_post_page.hbs#L70:L85)
- [search\_results.hbs](https://github.com/zendesk/copenhagen_theme/blob/v2.19.0/templates/search_results.hbs#L109:L165)

Once you're comfortable, you can add content tags to other pages. For example, the following snippet adds a list of content tags to the community topic page template.

```
{{#each posts}}
  ...

  {{#if (compare content_tags.length ">" 0)}}
    <ul class="content-tag-list">
      {{#each content_tags}}
        <li class="content-tag-item">
          {{#link "search_result" content_tag_id=id}}
            {{name}}
          {{/link}}
        </li>
      {{/each}}
    </ul>
  {{/if}}

  ...

{{/each}}
```

## Add badges to your custom help center theme

Note: Badges are available by default from September 1st, 2020.

You can create a
custom theme if you do not want to use the standard Copenhagen theme. However, badges
require that you use the **Theme Templating API v2**. If you're still using v1, use the
[upgrade instructions](https://developer.zendesk.com/apps/docs/help-center-templates/v1) to do this. You can also find
inspiration for doing this in the Zendesk [example theme on GitHub](https://github.com/zendesk/copenhagen_theme/pull/215).

This topic covers:

- [Adding the new user
  profile actions helper](#topic_tg5_cqx_xmb__section_ik2_dqx_xmb)
- [Showing Title badges
  on the post listings page](#topic_tg5_cqx_xmb__section_kk2_dqx_xmb)
- [Showing Title badges
  on a post and comments page](#topic_tg5_cqx_xmb__section_nk2_dqx_xmb)
- [Showing Title and
  Achivements badges on a user profile page](#topic_tg5_cqx_xmb__section_pk2_dqx_xmb)

### Adding the new user profile actions helper

You must add the Award badge option if you want to award badges for agents. However,
before you can do this, you must add the new actions helper.

**To add the actions helper declaration**

1. Open the theme online code editor, go to an agent's user profile
   page.

   ```
   Page filename: user_profile_page.hbs
   ```
2. Find the **edit** helper declaration.

   ```
   {{edit}}
   ```
3. Replace the edit helper declaration with the new actions helper declaration
   instead.

   ```
   {{actions}}
   ```

Now agents will be able to award badges. The new button will be styled with CSS according
to your preferences. For more inspiration see the Zendesk [example theme](https://github.com/zendesk/copenhagen_theme/pull/215).

### Showing Title badges on the post listings page

You can add Title badges as labels that sit next to the name of the author in the post
listing page. This looks similar to post status labels because, for the sake of
simplicity, the styling class is being reused.

To show Title badges on a post listings page

1. Open the theme online code editor, and go
   to

   ```
   Page filename: community_topic_page.hbs
   ```
2. Find the **author** name declaration. In the Copenhagen theme the line looks like
   this:

   ```
   <li class="meta-data">{{author.name}}</li>
   ```
3. Add this snippet to the line after
   it:

   ```
   {{#each author.badges}}
   <li class="meta-data">
      {{#is category_slug "titles"}}
          <span class="status-label">{{name}}</span>
      {{/is}}
   </li>
   {{/each}}
   ```

For advanced users - do not (re)use the`status-label` CSS class for this
scenario, instead create a new specialized CSS class that you can modify independently of
the status label's style.

Here is an example of a Title badge for a Community Member

![Gather badges title badge example.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_badges_Title_badge_example.png)

### Showing Title badges on a post and comments page

**To show Title badges on a post listings page**

1. Open the theme online code editor, and go
   to

   ```
   Page filename: community_post_page.hbs
   ```
2. Find the **author** name declaration. In the Copenhagen theme the line looks like
   this:

   ```
   <li class="meta-data">{{author.name}}</li>
   ```
3. Add this snippet to the line after
   it:

   ```
   {{#each author.badges}}
   <li class="meta-data">
      {{#is category_slug "titles"}}
          <span class="status-label">{{name}}</span>
      {{/is}}
   </li>
   {{/each}}
   ```

### Showing Title and Achievements badges on a user profile page

On a user profile page you will likely want to add more than just Title badges, for
example, you can also add the user's achievements. The following example assumes that
there is a graphical icon for each Achievement badge. Based on the Copenhagen theme, your
Achievement badges may look like this:

![Gather badges for title and achievement.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_badges_Title_and_achievement_badges.png)

**To show Title and Achievement badges on a user's profile page**

1. Open the theme online code editor, and go
   to

   ```
   Page filename: user_profile_page.hbs
   ```
2. Find the lines in the file where the user's name is rendered. For
   example:

   ```
   <h1 class="name">
     {{#if user.url}}
       <a href="{{user.url}}" target="_zendesk_lotus" title="{{t 'open_user_in_support'}}">{{user.name}}</a>
     {{else}}
       {{user.name}}
     {{/if}}
   </h1>
   ```
3. Replace that snippet with the
   following:

   ```
   <h1 class="name">
     {{#if user.url}}
       <a href="{{user.url}}" target="_zendesk_lotus" title="{{t 'open_user_in_support'}}">{{user.name}}</a>
     {{else}}
       {{user.name}}
     {{/if}}
     {{#each user.badges}}    {{#is category_slug "titles"}}
         <span class="status-label">{{name}}</span>
       {{/is}}  {{/each}}
   </h1>
   <div style="margin-top: 1em;">
     {{#each user.badges}}    {{#is category_slug "achievements"}}
         <div style="float: left; text-align: center; padding: 0.5em; margin: 0.5em; background: white; border-radius: 0.2em;">
           <img src="{{icon_url}}" height="40"><br>
           <span style="font-size: 0.8em;">{{name}}</span>
         </div>
       {{/is}}  {{/each}}
   </div>
   ```

In this example all of the CSS styling is inlined to keep the example simple. For best
practices, use these examples for inspiration, but spend time ensuring that the styling
fits your theme

## Enable users to view user profiles to your help center

This section describes how to update the necessary templates so that users in your
help center can click the author name or avatar and view the user's profile.

Note: User profiles are available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after June
20th, 2016.

The solutions discussed in this section involve using the `link` helper
in the help center templating language. See [link helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#link-helper) in the templating documentation to
update the following templates:

- [Articles](#topic_jzq_cq4_yfc)
- [Community posts](#topic_rkr_gq4_yfc)
- [Search results page](#topic_umf_jq4_yfc)

### Articles

Make the following updates to the Article page template.

**Updating the
article's author name**

Replace the following `if`
block:

```
{{#if article.author.url}}
  <a href="{{article.author.url}}" target="_zendesk_lotus">
    {{article.author.name}}
  </a>
{{else}}
  {{article.author.name}}
{{/if}}
```

with
the following `link`
helper:

```
{{#link "user_profile" id=article.author.id class="user-profile"}}
  {{article.author.name}}
{{/link}}
```

**Updating
comment author names**

Replace the following `if`
block:

```
{{#if author.url}}
  <a href="{{author.url}}" target="_zendesk_lotus">{{author.name}}</a>
{{else}}
  {{author.name}}
{{/if}}
```

with
the following `link`
helper:

```
{{#link "user_profile" id=author.id class="user-profile"}}
  {{author.name}}
{{/link}}
```

**Updating
the avatar of the article and comment authors**

Replace the following image
tag:

```
<img src="{{article.author.avatar_url}}" alt="Avatar"/>
```

with
the following `link`
helper:

```
{{#link "user_profile" id=article.author.id class="user-profile"}}
  <img src="{{article.author.avatar_url}}" alt="Avatar" />
{{/link}}
```

### Community posts

Make the following updates to the Community Post page template.

**Updating the
names of post authors**

Replace the following `if`
block:

```
{{#if post.author.url}}
  <a href="{{post.author.url}}" target="_zendesk_lotus">
    {{post.author.name}}
  </a>
  {{else}}
    {{post.author.name}}
{{/if}}
```

with
the following `link`
helper:

```
{{#link "user_profile" id=post.author.id class="user-profile"}}
  {{post.author.name}}
{{/link}}
```

**Updating
the names of comment authors**

Replace the following `if`
block:

```
{{#if author.url}}
  <a href="{{author.url}}" target="_zendesk_lotus">{{author.name}}</a>
{{else}}
  {{author.name}}
{{/if}}
```

with
the following `link`
helper:

```
{{#link "user_profile" id=author.id class="user-profile"}}
  {{author.name}}
{{/link}}
```

**Updating
the avatars of post authors**

Replace the following image
tag:

```
<img src="{{post.author.avatar_url}}" alt="Avatar"/>
```

with the
following `link`
helper:

```
{{#link "user_profile" id=post.author.id class="user-profile"}}
  <img src="{{post.author.avatar_url}}" alt="Avatar" />
{{/link}}
```

**Updating
the avatars of the comment authors**

Replace the following image
tag:

```
<img src="{{author.avatar_url}}" alt="Avatar"/>
```

with the
following `link`
helper:

```
{{#link "user_profile" id=author.id class="user-profile"}}
  <img src="{{author.avatar_url}}" alt="Avatar" />
{{/link}}
```

### Search results

Make the following updates to the Search results template.

**Updating the author
names of articles in the results**

Replace the following `if` block
in the `{{#each article_results}}`
block:

```
{{#if author.url}}
  <a href="{{author.url}}" target="_zendesk_lotus">{{author.name}}</a>
{{else}}
  {{author.name}}
{{/if}}
```

with
the following `link`
helper:

```
{{#link "user_profile" id=author.id class="user-profile"}}
  {{author.name}}
{{/link}}
```

**Updating
the author names of posts in the results**

Replace the following `if`
block in the `{{#each post_results}}`
block:

```
{{#if author.url}}
  <a href="{{author.url}}" target="_zendesk_lotus">{{author.name}}</a>
{{else}}
  {{author.name}}
{{/if}}
```

with
the following `link`
helper:

```
{{#link "user_profile" id=author.id class="user-profile"}}
  {{author.name}}
{{/link}}
```

**Updating
the search results in older themes**

If you have an older theme, the search results
might use the `{{meta}}` helper instead. In that case you can use the
code described in this section to link author names to profile pages in your help
center.

You may need to update your CSS styling for the search results page to
look uniform.

**Updating the author names of articles in the results**

Replace
the following div
tags:

```
<div class="search-result-meta">{{meta}}</div>
<div class="search-result-description">{{text}}</div>
```

With
the
following:

```
<ol
 class="breadcrumbs">
  {{#each path_steps}}
    <li title="{{name}}"><a href="{{url}}">{{name}}</a></li>
  {{/each}}
</ol>
<div class="search-result-description">
  {{text}}
</div>
<div class="search-result-meta">
  <span dir="auto" class="search-result-meta-name">
    {{#link "user_profile" id=author.id class="user-profile"}}
      {{author.name}}
    {{/link}}
  </span>
  <span class="search-result-meta-time">{{date created_at}}</span>
</div>
```

For
end
result:

```
{{#each article_results}}
  <li class="search-result">
    <a href="{{url}}" class="search-result-link">{{title}}</a>
    {{#if vote_sum}}
      <span class="search-result-votes">{{vote_sum}}</span>
    {{/if}}
    <ol class="breadcrumbs">
      {{#each path_steps}}
        <li title="{{name}}"><a href="{{url}}">{{name}}</a></li>
      {{/each}}
    </ol>
    <div class="search-result-description">
      {{text}}
    </div>
    <div class="search-result-meta">
      <span dir="auto" class="search-result-meta-name">
        {{#link "user_profile" id=author.id class="user-profile"}}
          {{author.name}}
        {{/link}}
      </span>
      <span class="search-result-meta-time">{{date created_at}}</span>
    </div>
  </li>
{{/each}}
```

**Updating
the author names of posts in the
results**

Add:

```
<ol class="breadcrumbs">
  {{#each path_steps}}
    <li title="{{name}}"><a href="{{url}}">{{name}}</a></li>
  {{/each}}
</ol>
```

For
end
result:

```
{{#each post_results}}
  <li class="search-result">
    <a href="{{url}}" class="search-result-link">{{title}}</a>
    <ol class="breadcrumbs">
      {{#each path_steps}}
        <li title="{{name}}"><a href="{{url}}">{{name}}</a></li>
      {{/each}}
    </ol>
    <div class="search-result-description">
      {{text}}
    </div>
    <div class="search-result-meta">
      <span dir="auto" class="search-result-meta-name">
        {{#link "user_profile" id=author.id class="user-profile"}}
          {{author.name}}
        {{/link}}
      </span>
      <span class="search-result-meta-time">{{date created_at}}</span>
      <span class="search-result-meta-count">
        {{t 'comments_count' count=comment_count}}
      </span>
    </div>
  </li>
{{/each}}
```

## Enable subsections in your help center theme

You can [add subsections](https://support.zendesk.com/hc/en-us/articles/4408834687130) to your help center knowledge base
to create more levels in your content hierarchy. If you are using a theme that was
customized before March 29, 2019, you must add code to your help center custom theme to
enable subsections. The following code comes with later versions of the Copenhagen
theme.

Note: Subsections are available for Guide Enterprise by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after March 29,
2019.

**Applicable template**

- Section

**Applicable object**

- `section.sections`

**Recipe**

- Insert the following snippet into the Zendesk section page template,
  **section\_page.hbs**, after the header tag (`<header
  class="page-header">...</header>`) and before the pagination tag
  (`{{pagination}}`)
  :

  ```
  {{#if section.sections}}
    <ul class="section-list section-list--collapsed">
      {{#each section.sections}}
      <li class="section-list-item">
        <a href="{{url}}">
          <span>{{name}}</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" focusable="false" viewBox="0 0 16 16" aria-hidden="true">
            <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M5 14.5l6.1-6.1c.2-.2.2-.5 0-.7L5 1.5"/>
          </svg>
        </a>
      </li>
      {{/each}}
      <a tabindex="0" class="see-all-sections-trigger" aria-hidden="true" id="see-all-sections-trigger" title="{{t 'see_all_sections'}}">{{t 'see_all_sections'}}</a>
    </ul>
  {{/if}}

  {{#if section.articles}}
    <ul class="article-list">
      {{#each section.articles}}
      <li class="article-list-item {{#if promoted}} article-promoted{{/if}}">
  	{{#if promoted}}<span data-title="{{t 'promoted'}}" class="icon-star"></span>{{/if}}
  	<a href="{{url}}" class="article-list-link">{{title}}</a>
      </li>
      {{/each}}
    </ul>
  {{else}}
    <i class="section-empty">
      <a href="{{section.url}}">{{t 'empty'}}</a>
    </i>
  {{/if}}
  ```

## Add sidebar filters and results for multiple help centers to the search results page

The help center search enables users to search across help centers, if you have multiple
help centers, and presents the search results from help centers and from knowledge base and
community, in a single unified feed with filters on the search results page.

If you are using a theme that was customized before March 29, 2019, you must add code to
your help center custom theme to support unified search results and search across multiple
help centers. If you have multiple help centers, you'll need to update your theme for each
help center.

Note: Unified search results and search across multiple help centers is supported by default
in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) and themes that were customized after September
25, 2019.

The fastest way to get the changes needed into your theme is to import the latest version
of the Copenhagen theme that supports unified search results. To do so, see [Adding a help center theme to Guide](https://support.zendesk.com/hc/en-us/articles/4408821790618).

If you prefer to update your existing, custom theme, this section provides an overview of
all of the changes you need to make. The solutions discussed in this section
involve using the `help_center_filters`, `filters`, and
`subfilters` helpers in the Curlybars templating language to update the
following files:

- [Search results](#topic_q1h_5sd_cjb)
- [CSS](#topic_yvw_vsd_cjb)
- [JavaScript](#topic_xzf_ysd_cjb)

### Updating the search results template to add sidebar filters

You need to update the search results template to add sidebar filters and to loop through
the results.

**Adding sidebar filters**

This snippet is an example of how you can implement search facets in the search results
page sidebar using the new filter helpers.

Insert the following code in `<div class="search-results">` in the
search results template:

```
<section class="search-results-sidebar">
     {{#if help_center.community_enabled}}
        <section class="filters-in-section collapsible-sidebar">
          <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_by_type'}}</h3>
          <ul>
            {{#each filters}}
              <li>
                <a href="{{url}}" class="sidenav-item" aria-selected="{{selected}}">{{name}} ({{count}})</a>
              </li>
            {{/each}}
          </ul>
        </section>
      {{/if}}
      {{#if subfilters}}
        <section class="filters-in-section collapsible-sidebar">
          {{#is current_filter.identifier 'knowledge_base'}}
            <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_by_category'}}</h3>
          {{/is}}
          {{#is current_filter.identifier 'community'}}
            <h3 class="collapsible-sidebar-title sidenav-title">{{t 'filter_by_topic'}}</h3>
          {{/is}}
          <ul>
            {{#each subfilters}}
              <li>
                <a href="{{url}}" class="sidenav-item" aria-selected="{{selected}}">{{name}} ({{count}})</a>
              </li>
            {{/each}}
          </ul>
        </section>
      {{/if}}
    </section>
```

**Looping through the results**

This snippet is an example of how you can use
the {{results}} helper to loop through the unified search results.

Replace both
the `{{article_results}}` and `{{post_results}}` helpers
and their associated search-results-subheading H3s

in the search results
template with the
following:

```
{{#if results}}
        <ul class="search-results-list">
          {{#each results}}
            <li class="search-result-list-item result-{{type}}">
              <h2 class="search-result-title">
                <a href="{{url}}" class="results-list-item-link">{{title}}</a>
              </h2>
              <article>
                <div class="search-result-icons">
                  {{#if vote_sum}}
                    <span class="search-result-votes">{{vote_sum}}</span>
                  {{/if}}
                  {{#if comment_count}}
                    <span class="search-result-meta-count">
                      {{comment_count}}
                    </span>
                  {{/if}}
                </div>
                <ul class="meta-group">
                  <li>
                    <ol class="breadcrumbs search-result-breadcrumbs">
                      {{#each path_steps}}
                        <li title="{{name}}"><a href="{{url}}">{{name}}</a></li>
                      {{/each}}
                    </ol>
                  </li>
                  <li class="meta-data">{{author.name}}</li>
                  <li class="meta-data">{{date created_at}}</li>
                </ul>
                <div class="search-results-description">{{text}}</div>
              </article>
            </li>
          {{/each}}
        </ul>
      {{else}}
        <p>
          {{t 'no_results_unified'}}
          {{#link 'help_center'}}
            {{t 'browse_help_center'}}
          {{/link}}
        </p>
      {{/if}}
```

### Updating CSS styling for the sidebar filters in the search results page

You can add CSS styling for the sidebar filters. The following example is based on the
Copenhagen theme.

Make sure the following CSS rules are included in your style.css file:

```
/***** Search results *****/
.search-results {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
}

@media (min-width: 1024px) {
  .search-results {
    flex-direction: row;
  }
}

.search-results-column {
  flex: 1;
}

@media (min-width: 1024px) {
  .search-results-column {
    flex: 0 0 75%;
  }
}

.search-results-sidebar {
  border-top: 1px solid #ddd;
  flex: 1 0 auto;
  margin-bottom: 20px;
  padding: 0;
}

@media (min-width: 1024px) {
  .search-results-sidebar {
    border: 0;
    flex: 0 0 20%;
    height: auto;
  }
}

.search-results-sidebar .sidenav-item[aria-selected="true"] {
  background-color: $brand_color;
  color: $brand_text_color;
  text-decoration: none;
}

.search-results-subheading {
  font-size: 18px;
  font-weight: 600;
}

.search-results-list {
  margin-bottom: 25px;
}

.search-results-list > li {
  padding: 20px 0;
}

.search-results-list > li:first-child {
  border-top: 1px solid #ddd;
}

.search-results-list > li h2 {
  margin-bottom: 0;
}

.search-result-title {
  font-size: 16px;
}

.search-result-description {
  margin-top: 15px;
  word-break: break-word;
}

.search-result-votes, .search-result-meta-count {
  color: lighten($text_color, 20%);
  display: inline-block;
  font-size: 13px;
  font-weight: 300;
  padding: 4px 5px;
  position: relative;
}

.search-result-votes::before, .search-result-meta-count::before {
  color: $brand_color;
}

[dir="ltr"] .search-result-votes, [dir="ltr"] .search-result-meta-count {
  margin-left: 5px;
}

[dir="ltr"] .search-result-votes::before, [dir="ltr"] .search-result-meta-count::before {
  margin-right: 3px;
}

[dir="rtl"] .search-result-votes, [dir="rtl"] .search-result-meta-count {
  margin-right: 5px;
}

[dir="rtl"] .search-result-votes::before, [dir="rtl"] .search-result-meta-count::before {
  margin-left: 3px;
}

.search-result-votes::before {
  content: "\1F44D";
}

.search-result-meta-count::before {
  content: "\1F4AC";
}

.search-result .meta-group {
  align-items: center;
}

.search-result-breadcrumbs {
  margin: 0;
}

.search-result-breadcrumbs li:last-child::after {
  content: "·";
  display: inline-block;
  margin: 0 5px;
}

/* Non-latin search results highlight */
/* Add a yellow background for Chinese */
html[lang|="zh"] .search-result-description em {
  font-style: normal;
  background: yellow;
}

/* Use bold to highlight for the rest of supported non-latin languages */
html[lang|="ar"] .search-result-description em,
html[lang|="bg"] .search-result-description em,
html[lang|="el"] .search-result-description em,
html[lang|="he"] .search-result-description em,
html[lang|="hi"] .search-result-description em,
html[lang|="ko"] .search-result-description em,
html[lang|="ja"] .search-result-description em,
html[lang|="ru"] .search-result-description em,
html[lang|="th"] .search-result-description em {
  font-style: bold;
}
```

### Updating JavaScript for the collapsible sidebar in the search results page

You can add JavaScript for the collapsible sidebar in the search results page. The
following example is based on the Copenhagen theme.

Replace the following block in the script.js file in the custom theme:

```
// Toggles expanded aria to collapsible elements
Array.prototype.forEach.call(document.querySelectorAll('.collapsible-nav, .collapsible-sidebar'), function(el) {
el.addEventListener('click', function(e) {
e.stopPropagation();
var isExpanded = this.getAttribute('aria-expanded') === 'true';
this.setAttribute('aria-expanded', !isExpanded);
});
});
```

with the following code snippet:

```
// Toggles expanded aria to collapsible elements
  var collapsible = document.querySelectorAll('.collapsible-nav, .collapsible-sidebar');

  Array.prototype.forEach.call(collapsible, function(el) {
    var toggle = el.querySelector('.collapsible-nav-toggle, .collapsible-sidebar-toggle');

    el.addEventListener('click', function(e) {
      toggleNavigation(toggle, this);
    });

    el.addEventListener('keyup', function(e) {
      if (e.keyCode === 27) { // Escape key
        closeNavigation(toggle, this);
      }
    });
  });
```

## Adding the spam filter to help center

If you're using a custom help center theme created before April 1, 2014, you need to add
some extra styling to your stylesheet to support the spam filter.

The following new HTML elements have been added:

- Article page
  - `section` element with class
    `"pending-comments-list"`
  - `span` element with class
    `"pending-moderation-comment-badge"`
- Question page
  - `section` element with class
    `"pending-answers-list"`
  - `span` element with class
    `"pending-moderation-answer-badge"`

Add the following to your custom theme
stylesheet:

```
.pending-moderation-comment-badge, .pending-moderation-answer-badge {
border-style: solid;
border-width: 1px;
border-color: #c7aa2b;
color: #c7aa2b;
padding: 3px5px;
margin-top: 10px;
font-size: 12px;
}
```

## Adding approvals to your help center

The standard Copenhagen theme displays approvals by default when the approval request
feature is [turned on](https://support.zendesk.com/hc/en-us/articles/9475816348442). If you're using a custom or marketplace
theme, you must update your theme to display approval requests to end users.

Note:

- Approvals is available by default in standard themes and themes that were customized
  after July 28, 2025. If your help center uses a custom help center theme that was
  customized before July 28, 2025, you need to update your custom theme to support
  approvals.
- The service catalog requires [templating API v4](https://support.zendesk.com/hc/en-us/articles/4408820214554). If you're using v3 or lower, [upgrade to v4](https://support.zendesk.com/hc/en-us/articles/4408820214554-About-Guide-templating-versions#topic_llb_t5g_skb__section_rxc_dbd_tkb) before updating your custom
  theme or [manually customize](#topic_ppb_4cn_bgc) the
  lower templating API version to support approvals.

**Applicable templates**

1. [approval\_request\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/beta/templates/approval_request_page.hbs)
2. [approval\_request\_list\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/beta/templates/approval_request_list_page.hbs)
3. The following [assets](https://github.com/zendesk/copenhagen_theme/tree/beta/assets):
   - approval\_requests\_bundle.js
   - approval\_requests\_translations\_bundle.js

**Recipe**

- Click the **Download raw file** icon on each template and asset file to
  download.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/serv-cat-download-raw-file.png)
- Add the template files (.hbs) to the templates folder in your unzipped live
  theme.
- Copy all assets to the assets folder in your unzipped live theme.
- Add the following code snippet to the **document\_head.hbs** template, then delete
  any other script starting with `<script
  type="importmap">`.

  ```
  <script type="importmap">
  {
    "imports": {
      "new-request-form": "{{asset 'new-request-form-bundle.js'}}",
      "flash-notifications": "{{asset 'flash-notifications-bundle.js'}}",
      "service-catalog": "{{asset 'service-catalog-bundle.js'}}",
      "approval-requests": "{{asset 'approval-requests-bundle.js'}}",
      "approval-requests-translations": "{{asset 'approval-requests-translations-bundle.js'}}",
      "new-request-form-translations": "{{asset 'new-request-form-translations-bundle.js'}}",
      "service-catalog-translations": "{{asset 'service-catalog-translations-bundle.js'}}",
      "shared": "{{asset 'shared-bundle.js'}}",
      "ticket-fields": "{{asset 'ticket-fields-bundle.js'}}",
      "wysiwyg": "{{asset 'wysiwyg-bundle.js'}}"
    }
  }
  </script>
  ```
- If necessary, you can [customize the page templates](https://support.zendesk.com/hc/en-us/articles/4408839332250).
- Zip the theme and upload it to your help center.

## Adding the service catalog to your help center

The standard Copenhagen theme displays service catalog by default when the service catalog
request feature is [turned on](https://support.zendesk.com/hc/en-us/articles/9443951511450). If you're using a custom or marketplace
theme, you must update your theme to display the service catalog to end users.

You can copy the service catalog implementation from the Copenhagen theme following the
steps described below. Alternatively, if you want to completely customize the UI, you can
fork the [Copenhagen theme](https://github.com/zendesk/copenhagen_theme/) and change the implementation in the
`src/modules/service-catalog` folder.

Note:

- Service catalog is available by default in standard themes and themes that were
  customized after July 31, 2025. If your help center uses a custom help center theme
  that was customized before July 31, 2025, you need to update your custom theme to
  support service catalog.
- The service catalog requires [templating API v4](https://support.zendesk.com/hc/en-us/articles/4408820214554). If you're using v3 or lower, [upgrade to v4](https://support.zendesk.com/hc/en-us/articles/4408820214554-About-Guide-templating-versions#topic_llb_t5g_skb__section_rxc_dbd_tkb) before updating your custom
  theme or [manually customize](#topic_ppb_4cn_bgc) the
  lower templating API version to support the service catalog.

**Applicable templates**

- [service\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/service-catalog-eap/templates/service_page.hbs)
- [service\_list\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/service-catalog-eap/templates/service_list_page.hbs)
- [assets](https://github.com/zendesk/copenhagen_theme/tree/service-catalog-eap/assets)

**Recipe**

1. Click the **Download raw file** icon on each template and asset file to
   download.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/serv-cat-download-raw-file.png)
2. Add the template files (.hbs) to the templates folder in your unzipped live
   theme.
3. Copy all assets to the assets folder in your unzipped live theme.
4. Add the following code snippet to the **document\_head.hbs** template, then delete
   any other script starting with `<script
   type="importmap">`.

   ```
   <script type="text/javascript">
     // Load ES module polyfill only for browsers that don't support ES modules
     if (!(HTMLScriptElement.supports && HTMLScriptElement.supports('importmap'))) {
       document.write('<script async src="{{asset 'es-module-shims.js'}}"><\/script>');
     }
   </script>
   <script type="importmap">
   {
     "imports": {
       "new-request-form": "{{asset 'new-request-form-bundle.js'}}",
       "flash-notifications": "{{asset 'flash-notifications-bundle.js'}}",
       "service-catalog": "{{asset 'service-catalog-bundle.js'}}",
       "approval-requests": "{{asset 'approval-requests-bundle.js'}}",
       "approval-requests-translations": "{{asset 'approval-requests-translations-bundle.js'}}",
       "new-request-form-translations": "{{asset 'new-request-form-translations-bundle.js'}}",
       "service-catalog-translations": "{{asset 'service-catalog-translations-bundle.js'}}",
       "shared": "{{asset 'shared-bundle.js'}}",
       "ticket-fields": "{{asset 'ticket-fields-bundle.js'}}",
       "wysiwyg": "{{asset 'wysiwyg-bundle.js'}}"
     }
   }
   </script>
   <script type="module">
     import { renderFlashNotifications } from "flash-notifications";

     const settings = {{json settings}};
     const baseLocale = {{json help_center.base_locale}};

     renderFlashNotifications(settings, baseLocale);
   </script>
   ```
5. Use the link helper to add a link to the service catalog page in the **header.js**
   template.
6. Copy the following styles into your **style.css**
   file:

   ```
   .service-catalog-description {
     display: flow-root;
   }
   .service-catalog-description a {
     color: $link_color;
     text-decoration: underline;
   }
   .service-catalog-description a:visited {
     color: $visited_link_color;
   }
   .service-catalog-description a:hover, .service-catalog-description a:active, .service-catalog-description a:focus {
     color: $hover_link_color;
   }
   .service-catalog-description img {
     height: auto;
     max-width: 100%;
   }
   .service-catalog-description p > img.image-style-align-left {
     float: left;
     margin: 8px 20px 6px 0;
   }
   .service-catalog-description p > img.image-style-align-right {
     float: right;
     margin: 8px 0px 6px 20px;
   }
   .service-catalog-description p > img.image-style-block-align-right {
     margin-left: auto;
     margin-right: 0;
   }
   .service-catalog-description p > img.image-style-block-align-left {
     margin-left: 0;
     margin-right: auto;
   }
   .service-catalog-description figure.image {
     display: table;
     margin: 0 auto;
   }
   .service-catalog-description figure.image > img {
     display: block;
     width: 100%;
   }
   .service-catalog-description figure.image.image-style-align-left {
     float: left;
     margin: 8px 20px 6px 0;
   }
   .service-catalog-description figure.image.image-style-align-right {
     float: right;
     margin: 8px 0px 6px 20px;
   }
   .service-catalog-description figure.image.image-style-block-align-right {
     margin-left: auto;
     margin-right: 0;
   }
   .service-catalog-description figure.image.image-style-block-align-left {
     margin-left: 0;
     margin-right: auto;
   }
   .service-catalog-description figcaption {
     padding: 10px 0;
     font-size: 12px;
     text-align: center;
     background-color: darken($background_color, 5%);
   }
   .service-catalog-description ul,
   .service-catalog-description ol {
     padding-left: 20px;
     list-style-position: outside;
     margin: 20px 0 20px 20px;
   }
   [dir=rtl] .service-catalog-description ul,
   [dir=rtl] .service-catalog-description ol {
     padding-right: 20px;
     padding-left: 0;
     margin-left: 0;
     margin-right: 20px;
   }
   .service-catalog-description ul > ul,
   .service-catalog-description ol > ol,
   .service-catalog-description ol > ul,
   .service-catalog-description ul > ol,
   .service-catalog-description li > ul,
   .service-catalog-description li > ol {
     margin: 0;
   }
   .service-catalog-description ul {
     list-style-type: disc;
   }
   .service-catalog-description :not(pre) > code {
     background: darken($background_color, 3%);
     border: 1px solid #ddd;
     border-radius: 3px;
     padding: 0 5px;
     margin: 0 2px;
   }
   .service-catalog-description pre {
     background: darken($background_color, 3%);
     border: 1px solid #ddd;
     border-radius: 3px;
     padding: 10px 15px;
     overflow: auto;
     white-space: pre;
   }
   .service-catalog-description blockquote {
     border-left: 1px solid #ddd;
     color: lighten($text_color, 20%);
     font-style: italic;
     padding: 0 15px;
   }
   ```
7. If necessary, you can [customize the page templates](https://support.zendesk.com/hc/en-us/articles/4408839332250).
8. Zip the theme and upload it to your help center.

### Adding a service catalog or approvals on Templating API versions lower than 4

The Templating API version 4 includes a [JSON helper](https://developer.zendesk.com/api-reference/help_center/help-center-templates/helpers/#json-helper) that is required for the service
catalog and approvals functionality. However, if you need to continue using a lower
templating version, you can serialize the data differently.

**To use the service catalog or approvals with lower Templating API versions**

1. Remove the JSON helper from boolean and numbers.
2. Serialize strings with the [json\_stringify helper](https://developer.zendesk.com/api-reference/help_center/help-center-templates/helpers/#json_stringify-helper).
3. For complex objects, serialize each property individually.

The following example demonstrates how to adapt the [service\_page.hbs](https://github.com/zendesk/copenhagen_theme/blob/service-catalog-eap/templates/service_page.hbs) template. You'll need to modify
the other required templates in a similar way as well.

Replace the following original
code:

```
<script type="module">
  import { renderServiceCatalogItem } from "service-catalog";

  const settings = {{json settings}};
  const container = document.getElementById("service-catalog-item");

  // Extract the ID from the URL
  const id = window.location.pathname.split("/").pop()

  const props = {
    baseLocale: {{json help_center.base_locale}},
    hasAtMentions: {{json help_center.at_mentions_enabled}},
    userRole: {{json user.role}},
    userId: {{json user.id}},
    brandId: {{json brand.id}},
    organizations: {{json user.organizations}},
    serviceCatalogItemId: id,
    helpCenterPath: {{json (page_path 'help_center')}},
  }

  renderServiceCatalogItem(container, settings, props);
</script>
```

With the
following:

```
<script type="module">
  import { renderServiceCatalogItem } from "service-catalog";

  const settings = {
    background_color: {{json_stringify settings.background_color}},
    text_color: {{json_stringify settings.text_color}},
    brand_color: {{json_stringify settings.brand_color}},
    brand_text_color: {{json_stringify settings.brand_text_color}},
    link_color: {{json_stringify settings.link_color}},
    hover_link_color: {{json_stringify settings.hover_link_color}},
    visited_link_color: {{json_stringify settings.visited_link_color}},
  };
  const container = document.getElementById("service-catalog-item");

  // Extract the ID from the URL
  const id = window.location.pathname.split("/").pop()

  const props = {
    baseLocale: {{json_stringify help_center.base_locale}},
    hasAtMentions: {{help_center.at_mentions_enabled}},
    userRole: {{json_stringify user.role}},
    userId: {{user.id}},
    brandId: {{brand.id}},
    organizations: [
     {{#each user.organizations}}
              {id: {{id}}},
     {{/each}}
    ],
    serviceCatalogItemId: id,
    helpCenterPath: {{json_stringify (page_path 'help_center')}},
  }

  renderServiceCatalogItem(container, settings, props);
</script>
```
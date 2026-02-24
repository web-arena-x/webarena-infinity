# Help center CSS cookbook

Source: https://support.zendesk.com/hc/en-us/articles/4408842914714-Help-center-CSS-cookbook

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can easily customize the look and feel of your help center using Cascading Style Sheets (CSS). This cookbook is designed to help you make your help center look the way you want.

Note: Trial users are given the Professional plan, which includes code editing options, but they can no longer access that feature if they purchase Suite Team.

To access and edit the CSS, see [Customizing the CSS or JavaScript](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_gxl_3qw_n3).

If you're new to CSS or maybe a little rusty, check out the following tutorials to get you up to speed:

- [Getting started with CSS](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started) is the most complete CSS tutorial aimed at complete beginners. It guides you through the basic features of the language with practical examples that you can try for yourself.
- [CSS Beginner Tutorial](http://www.htmldog.com/guides/css/beginner/) gives you just enough to get started.

You can also customize the look of your help center using the Help Center templating language or JavaScript:

- [Help center templates reference](https://developer.zendesk.com/apps/docs/help-center-templates/introduction)
- [Help center templating cookbook](https://support.zendesk.com/hc/en-us/articles/4408832681626)
- [Help center Javascript cookbook](https://support.zendesk.com/hc/en-us/articles/4408836487450)

## Table of contents

The cookbook is organized into sections covering elements of a help center. Each section includes CSS code that you can paste directly into your theme's stylesheet. Use the code as-is or edit it to make it your own.

The cookbook isn't exhaustive. By modifying the HTML templates and CSS stylesheet, the number of things you can do is limited only by your imagination.

### Header and footer

- [Change the background color of the header or footer](#topic_iqb_p4q_xl)
- [Change the height of the header or footer](#topic_x3b_2pq_xl)
- [Change the space above or below the header or footer](#topic_cl5_1qq_xl)
- [Change the appearance of the selected language](#topic_ub4_csq_xl)
- [Change the appearance of the Submit a Request link](#topic_hdj_ztq_xl)
- [Hide the Submit a Request link](#topic_e1x_qq4_4v)
- [Change the appearance of the Sign In link](#topic_xqr_j5q_xl)
- [Change the logo dimensions](#topic_rbd_q5y_1bb)

### Search

- [Change the width or height of the search field](#topic_ovp_rvd_xl)
- [Change the background color of the search field](#topic_wly_gyd_xl)
- [Change the appearance of the search text](#topic_qtq_j5d_xl)
- [Change the appearance of the results page heading](#topic_jy2_45d_xl)
- [Change the appearance of search result keyword highlighting](#topic_ocg_xdp_h5)
- [Change the appearance of the Knowledge base and Community headings](#topic_tjl_sb2_xl)
- [Change the spacing between the results](#topic_zcz_3c2_xl)
- [Change the appearance of the result text](#topic_cdz_3c2_xl)
- [Change the color of the result links](#topic_fdz_3c2_xl)

### Breadcrumbs

- [Change the space above and below the breadcrumbs](#topic_o1s_1qd_xl)
- [Change the appearance of the breadcrumb text](#topic_a3d_w4d_xl)
- [Change the color of the breadcrumb links](#topic_shf_2pd_xl)
- [Change the pointer character (>) in the breadcrumbs](#topic_tnd_qpd_xl)

### Article lists

- [Change the space around the list of articles](#topic_gzv_fmd_xl)
- [Change the spacing between the articles](#topic_izv_fmd_xl)
- [Change the appearance of the article links](#topic_nzv_fmd_xl)
- [Change the color of the article links](#topic_pzv_fmd_xl)

### Knowledge base articles

- [Change the appearance of article titles](#topic_h2g_4cr_xl)
- [Change the appearance of article text](#topic_pbr_qcr_xl)
- [Change the color of article links](#topic_egl_tcr_xl)
- [Change the appearance of the author's name](#topic_qmb_scr_xl)
- [Change the appearance of the last updated string](#topic_nxj_tfr_xl)
- [Change the appearance of "Was this article helpful?"](#topic_jcq_22r_xl)
- [Change the appearance of the vote counter](#topic_svl_m2r_xl)
- [Change the appearance of "Have more questions? Submit a request"](#topic_jdb_j2r_xl)
- [Change the appearance of the Comments title](#topic_g44_cgr_xl)
- [Change the appearance of comment text](#topic_uzv_wcr_xl)

### Community questions and answers

- [Change the appearance of question titles](#topic_gbq_vgr_xl)
- [Change the appearance of question text](#topic_jbq_vgr_xl)
- [Change the color of question links](#topic_lbq_vgr_xl)
- [Change the appearance of the question author's name](#topic_nbq_vgr_xl)
- [Change the appearance of the time since question published](#topic_qbq_vgr_xl)
- [Change the appearance of the share question link](#topic_hth_nhr_xl)
- [Change the appearance of the answers heading](#topic_sbq_vgr_xl)
- [Change the appearance of answer text](#topic_ccq_vgr_xl)
- [Change the appearance of the answer author's name](#topic_d3c_g3r_xl)
- [Change the appearance of the time since answer published](#topic_acj_j3r_xl)
- [Change the appearance of the share answer link](#topic_sfw_l3r_xl)

## Header and footer

The header displays a logo and other components depending on the theme and user roles. You can use the footer to display related links, information about your company, or legal notices.

Back to the [table of contents](#topic_oks_1r2_tl).

### Change the background color of the header or footer

Change or add the **background-color** property in the following selectors.

Header:

```
.header {
 background-color: #666;
}
```

Footer:

```
.footer {
 background-color: #333;
}
```

### Change the height of the header or footer

Change or add the **height** property in the following selectors.

Header:

```
.header {
   height: 70px;
}
```

Footer:

```
.footer {
   height: 20px;
}
```

### Change the space above or below the header or footer

Change or add **margin-bottom** and **margin-top** properties in the following selectors.

Header:

```
.header {
     margin-bottom: 20px;
}
```

Footer:

```
.footer {
     margin-top: 10px;
}
```

### Change the appearance of the selected language

Add the following selector and property:

```
.language-selector .dropdown-toggle {
 color: green;
}
```

### Change the appearance of the Submit a Request link

The header.hbs template has both a desktop and a mobile version of the header in the same template to make it responsive. The desktop version is contained in a div with a class named `nav-wrapper-desktop` and the mobile version is in a div with a class named `nav-wrapper-mobile`. Each div contains a separate Submit a Request link. To change the appearance of the link, you need to create desktop and mobile versions of your CSS rule and increase the specificity of their selectors.

Add the following selectors in the style.css file and modify the text properties:

```
.nav-wrapper-desktop a.submit-a-request {
 font-size: 14px;
 color: green;
}
```

```
.nav-wrapper-mobile a.submit-a-request {
 font-size: 12px;
 color: green;
}
```

### Hide the Submit a Request link

Add the following selectors in the style.css file:

```
.nav-wrapper-desktop a.submit-a-request {
 display:none;
}
```

```
.nav-wrapper-mobile a.submit-a-request {
 display:none;
}
```

### Change the appearance of the Sign In link

Add or modify text properties in the following selector:

```
.login {
 font-size: 14px;
 color: green;
}
```

### Change the logo dimensions

Although the recommended logo image size is 200px by 50px, you can override this default if needed.

Note: To use a logo larger than the recommended size, you need to host the logo image somewhere outside your instance of Zendesk Support.

**To change your logo size**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Edit theme**.
3. Click **CSS** to open the CSS stylesheet, then search for the following rule:

   ```
   .logo img {
     max-height: 37px;
   }
   ```

   To search, click inside the code editor and press Control+F (Windows) or Cmd+F (Mac).
4. Modify the **height** property in the ".logo img" selector to match the height of the image.
5. Click **Save**.

## Search

The search box looks for content in both the knowledge base and community and displays links on a results page. If you want, you can remove the search box. For more information, see the [search helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#search-helper) in the Help Center Templates guide.

Back to the [table of contents](#topic_oks_1r2_tl).

### Change the width or height of the search field

Change the **width** or **height** values in the following selectors.

Large search box:

```
.search input[type=search] {
 height: 50px;
 width: 90%;
}
```

Small search box:

```
.search-small input[type=search] {
 height: 50px;
 width: 320px;
}
```

### Change the background color of the search field

Change the **background** property in the following selectors.

Large search box:

```
.search input[type=search] {
 background: #999;
}
```

Small search box:

```
.search-small input[type=search] {
 background: #999;
}
```

### Change the appearance of the search text

Change or add text properties in the following selectors.

Large search box:

```
.search {
 font-size: 12px;
 font-family: Tahoma, Arial, sans-serif;
}
```

Small search box:

```
.search-small {
 font-size: 12px;
 font-family: Tahoma, Arial, sans-serif;
}
```

### Change the appearance of the results page heading

The heading on the search results page consists of the number of results returned for the search term. Example: **9 results for "serial number"**.

Add the following selector if it's not already in the stylesheet, and change or add text properties:

```
.search-results-heading {
 font-size: 36px;
 font-family: Tahoma, Arial, sans-serif;
}
```

### Change the appearance of search result keyword highlighting

Highlighted terms within search results are wrapped with the inline element <em>
under the .search-result-description container. If you want to have highlights appear as bold with a yellow background, you would do the following:

```
.search-result-description em { 
 font-weight: bold;
 background-color: #FFF3CA;
 padding: 0px 3px 2px;
 border-radius: 3px;
}
```

### Change the appearance of the Knowledge base and Community headings

Add or modify text properties in the following selector:

```
.search-results-subheading {
 font-size: 24px;
 font-family: Tahoma, Arial, sans-serif;
}
```

### Change the spacing between the results

Add a **margin-bottom** property in the following selector:

```
.search-result {
 margin-bottom: 20px;
}
```

### Change the appearance of the result text

Change or add text properties in the following selector:

```
.search-result {
 font-size: 105%;
 font-family: Arial, Helvetica, sans-serif;
}
```

### Change the color of the result links

Add or modify the **color** property in the following selector:

```
.search-result a {
 color: #484;
}
```

## Breadcrumbs

Breadcrumbs help users navigate content in your help center. If you want, you can remove the breadcrumbs. For more information, see the [breadcrumbs helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#breadcrumbs-helper) in the Help Center Templates guide.

Back to the [table of contents](#topic_oks_1r2_tl).

### Change the space above and below the breadcrumbs

Add or change the **padding** properties in the following selector:

```
.breadcrumbs {
 padding-top; 20px;
 padding-bottom: 16px;
}
```

### Change the appearance of the breadcrumb text

Change or add text properties in the following selector:

```
.breadcrumbs li {
 font-size: 12px;
 font-family: Arial, Helvetica, sans-serif;
}
```

### Change the color of the breadcrumb links

Add the following selector and property:

```
.breadcrumbs li a {
 color: #484;
}
```

### Change the pointer character (>) in the breadcrumbs

Change the **color** and **content** properties in the following selector:

```
.breadcrumbs li + li:before {
 color: #158EC2;
 content: ">>";
}
```

## Article lists

Depending on the theme, article lists are used on the home page, category landing pages, and section landing pages.

Back to the [table of contents](#topic_oks_1r2_tl).

### Change the space around the list of articles

Add or modify the following selector and **padding** properties:

```
.article-list {
 padding-left: 16px;
 padding-right; 20px;
}
```

### Change the spacing between the articles

Change the **margin-bottom** property in the following selector:

```
.article-list > li {
 margin-bottom: 10px;
}
```

### Change the appearance of the article links

Change or add text properties in the following selector:

```
.article-list > li {
 font-size: 12px;
 font-family: Arial, Helvetica, sans-serif;
}
```

### Change the color of the article links

Add the following selector and property:

```
.article-list li a {
 color: #FFF;
}
```

## Knowledge base articles

You can change the look and feel of the articles in your knowledge base.

Back to the [table of contents](#topic_oks_1r2_tl).

### Change the appearance of article titles

Add or modify the following selector and properties:

```
.article-header h1 {
 color: #993;
 font-family: Verdana, Geneva, sans-serif;
 font-size: 20px;
}
```

### Change the appearance of article text

Add or modify the following selector and properties:

```
.article-body {
 color: #666;
 font-family: Arial, Helvetica, sans-serif;
 font-size: 13px;
}
```

### Change the color of article links

Add or modify the following selector and property:

```
.article-body a {
 color: #930;
}
```

### Change the appearance of the author's name

Add or modify the following selector and properties:

```
.article-author a {
 color: #669;
 font-family: Georgia, Times New Roman, serif;
 font-size: 16px;
}
```

### Change the appearance of the last updated string

Add or modify the following selector and properties:

```
.article-updated {
 color: #CCC;
 font-family: Tahoma, Geneva, sans-serif;
 font-size: 13px;
}
```

### Change the appearance of "Was this article helpful?"

Add or modify the following selector and properties:

```
.article-vote-question {
 color: #763;
 font-family: Arial, Helvetica, sans-serif;
 font-size: 14px;
}
```

### Change the appearance of the vote counter

Example: "6 out of 8 found this helpful". Add or modify the following selector and properties:

```
.article-vote-count {
 font-family: Georgia, Times New Roman, serif;
 font-size: 10px;
}
```

### Change the appearance of "Have more questions? Submit a request"

Add or modify the following selector and properties:

```
.article-more-questions {
 font-family: Arial, Helvetica, sans-serif;
 font-size: 105%;
}
```

### Change the appearance of the Comments title

Add or modify the following selector and properties:

```
.article-comments h2 {
 color: #666;
 font-family: Georgia, Times New Roman, serif;
 font-size: 130%;
}
```

### Change the appearance of comment text

Add or modify the following selector and properties:

```
.comment-body {
 color: #666;
 font-family: Verdana, Geneva, sans-serif;
 font-size: 12px;
}
```

## Community questions and answers

You can change the look and feel of the content in your community.

Back to the [table of contents](#topic_oks_1r2_tl).

### Change the appearance of question titles

Add or modify the following selector and properties:

```
.question-title {
 color: #484;
 font-family: Verdana, Geneva, sans-serif;
 font-size: 120%;
}
```

### Change the appearance of question text

Add or modify the following selector and properties:

```
.question-text {
 color: #666;
 font-family: Tahoma, Geneva, sans-serif;
 font-size: 14px;
}
```

### Change the color of question links

Add or modify the following selector and property:

```
.question-text a {
 color: #484;
}
```

### Change the appearance of the question author's name

Add or modify the following selector and properties:

```
.question-author {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

To change the link color, add or modify the following selector and property:

```
.question-author a {
 color: #484;
}
```

Because the question author's name, the time since the question was published, and the share link are usually grouped together on a page, it makes good design sense to make all three elements look the same. To do so, use the following combined selector:

```
.question-author, .question-published, .question-share {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

### Change the appearance of the time since question published

Add or modify the following selector and properties:

```
.question-published {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

### Change the appearance of the share question link

Add or modify the following selector and properties:

```
.question-share {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

### Change the appearance of the answers heading

Add or modify the following selector and properties:

```
.answer-list-heading {
 color: #4CC;
 font-family: Verdana, Geneva, sans-serif;
 font-size: 105%;
}
```

### Change the appearance of answer text

Add or modify the following selector and properties:

```
.answer-text {
 color: #333;
 font-family: Tahoma, Geneva, sans-serif;
 font-size: 105%;
}
```

### Change the appearance of the answer author's name

Add or modify the following selector and properties:

```
.answer-author {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

To change the link color, add or modify the following selector and property:

```
.answer-author a {
 color: #484;
}
```

Because the answer author's name, the time since the answer was published, and the share link are usually grouped together on a page, it makes good design sense to make all three elements look the same. To do so, use the following combined selector:

```
.answer-author, .answer-published, .answer-share {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

### Change the appearance of the time since answer published

Add or modify the following selector and properties:

```
.answer-published {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```

### Change the appearance of the share answer link

Add or modify the following selector and properties:

```
.answer-share {
 font-family: Georgia, Times New Roman, serif;
 font-size: 12px;
}
```
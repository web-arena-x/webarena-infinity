# Importing or upgrading jQuery

Source: https://support.zendesk.com/hc/en-us/articles/4408829274906-Importing-or-upgrading-jQuery

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

With Guide Templating V2, you'll need to import a jQuery library if you want to use jQuery statements in a theme in place of vanilla JavaScript.

This guidance is for instructional purposes only, and if you have any jQuery issues, see the official [jQuery site](https://code.jquery.com/).

**To install or upgrade jQuery in your Help Center themes**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. From the theme you want to work with, click **Customize**.
3. Click **Edit code**.
4. Click *document\_head.hbs*.
5. Visit <https://code.jquery.com> and click on the minified version of the jQuery version you want to use.
6. Paste the `script` tag into your HTML file. Example:

   ```
   <script 
     src="https://code.jquery.com/jquery-3.6.0.min.js" 
     integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" 
     crossorigin="anonymous">
   </script>
   ```

   The `integrity` value will vary. The attribute lets browsers know that the resources hosted on the third-party server have not been tampered with.

The jQuery library is loaded, and you can include jQuery statements in your Help Center themes.
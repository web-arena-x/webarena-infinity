# Customizing the logo return URL in your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408839041306-Customizing-the-logo-return-URL-in-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

By default, clicking the logo image in your help center header returns users to the home page. You can edit the HTML in your theme to return users to a different URL.

Before you begin, be sure you've uploaded your logo image to the Assets area (see [Using your own theme assets for help center](https://support.zendesk.com/hc/en-us/articles/4408829155226-)) and made a note of the image's URL.

**To update the logo URL**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize**.
3. Click **Edit code** at the bottom of the page.
4. Choose **header.hbs** from the templates list, and locate the logo div tag in the HTML:

   ```
   <div class="logo"">
   ```
5. Replace this code:

   ```
   {{#link 'help_center'}}
         <img src="{{logo_url}}" alt="{{t 'logo'}}">
       {{/link}}
   ```

   with the following HTML (in bold):

   ```
   <div class="logo">
     <a href="http://new_url">
       <img src={{asset 'uploaded-image-name.png'}} />
     </a>
   </div>
   ```

   The code inserts a linked image in the page.
6. Specify the URL of the page (*new\_url*), the path to your logo image (*path\_to\_image*), and the image name (*image*).
7. Click **Save**.
# Setting up a requests-only (tickets-only) help center

Source: https://support.zendesk.com/hc/en-us/articles/4408884098074-Setting-up-a-requests-only-tickets-only-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

This support tip demonstrates how to set up a request-only help center. That is, a help center that enables end-users to submit requests (tickets), and view existing requests only, and does not contain any self-service content.

There are several ways that you can accomplish this, but in this tip we'll edit the help center home page to provide options for end-users to submit a new request or check their existing requests. The home page will not contain anything else. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_requests_only_example.png)

The benefit of this tip is that it does not use a Javascript redirect to create a request-only help center. [Javascript can, and does, work as well](https://support.zendesk.com/hc/en-us/community/posts/203410646). However it often diminishes the agent experience when using the help center by making it challenging to access due to restrictions on agents viewing the New Request page and My Activities, (the default behavior is to redirect to the Zendesk Support agent interface).

This tip avoids other challenges of JS, for example, accounting for user sign-in, having an open or closed help center, and having multiple locales enabled. Simply, this tip accounts for various desired workflows without the need of additional customizations.

This article contains the following sections:

- [Updating your home page for requests only](#topic_vws_tnk_dx)
- [Hiding unneeded elements of your help center](#topic_s2s_x4k_dx)
- [(Optional) Localizing your home page buttons](#topic_qrr_5nk_dx)
- [(Optional) Changing the default button styling](#topic_lsk_vnk_dx)

## Updating your home page for requests only

First, we'll edit the help center home page to provide two buttons for end-users to submit a new request and check their existing requests. We recommend that you use the Copenhagen theme for your request-only help center, as it is mobile responsive.

**To edit your home page to add the new request and existing requests buttons**

1. In Guide, click the **Customize design** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click your theme to open it, then click **Edit Code**.
3. Open the Home Page template.
4. Comment out the existing code by wrapping it in `{{!-- ... --}}`.

   If you do this correctly, all of the code text will change to gray.
5. Above the commented out code of the homepage add the following code.

   ```
   <div id="divhomecontainer">
   <h1>Welcome to Rebecca's Support Portal</h1> 
     <h2> Select below to Submit a New Request or Check your Existing Requests<h2>

   <form style="display: block; text-align: center; margin: 20px;" class="submitbutton"
   action="{{page_path 'new_request'}}">    
     <input type="submit" value="Submit a Request">
   </form>

   <form  style="display: block; text-align: center; margin: 20px;"class="requestbutton" 
   action="{{page_path 'my_activities'}}"> 
      <input type="submit" value="Check your Existing Requests">
     </form>
   </div>
   ```

   What this code does:
   - Adds a welcome message. Be sure to change the placeholder text with your own welcome message.
   - Creates two buttons: one for the new request form and one to check existing requests. Also, adds a unique class to the buttons to customize the CSS if needed.
   - Adds CSS styles to the buttons inline to enhance the appearance. (Avoids having to have customers also customize the CSS with could likely be confusing i.e. one stop copy-paste solution.)
   - Prompts users who are not signed in to do so when they click the Check your Existing Requests button.
6. Click **Save**.

   You can wait to publish changes until you [hide unneeded elements of your help center](#topic_s2s_x4k_dx) in the next section.

## Hiding unneeded elements of your help center

After you edit your home page to add [the requests-only buttons](#topic_vws_tnk_dx), you'll want to ensure that end users do not accidentally navigate to the content sections. To do so, you'll comment out a few additional lines of code on various templates for:

- Community
- Submit a request button
- Navigation links
- Search

Additionally, you should delete all pre-existing content in categories or set the categories to draft mode, as described below, to prevent end-users from accessing the content inadvertently.

**To hide unneeded elements in your help center**

1. Open the **header** template, then comment out the Community and Submit a Request buttons by wrapping it in `{{!-- ... --}}`.

   If you do this correctly, all of the code text will change to gray.
2. Open the **request\_page** template, then comment out the `<nav>` code at the top.
3. Open the **requests\_page** template, then comment out the `<nav>` code at the top.
4. Open the **new\_request\_page** template, then comment out `{{search}}`.
5. Click **Save**.

**To remove pre-existing help center content**

1. Navigate to the category, then click **Edit category** in the top menu bar.
2. Click the **Mark as draft** checkbox to hide the category and its content, or click **Delete category** at the bottom to permanently remove the category and its contents.
3. If you selected draft, click **Update**, and if you selected delete, click to confirm that you want to delete the category.

## (Optional) Changing the default button styling and color

The help center provides pre-built templates, so the CSS styling already exists for buttons in your help center. If you are having issues overwriting the existing CSS, you will likely need to edit the default styling. You can also change the button color without editing the CSS.

**To find the default CSS button styling**

1. In Guide, click the **Customize design** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click your theme to open it, then click **Edit Code**.
3. Open the **style.css** file.
4. Search (control + F) for "Buttons".
5. Make updates as you'd like, then click **Save**.

**To edit the button colors**

1. In Guide, click the **Customize design** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click your theme to open it.
3. Click **Colors**, then change the colors as needed.

   Here’s how the colors map:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_requests_only_button_colors.png)
4. Click **Save**.

## (Optional) Localizing your home page buttons

Note: Support + Guide customers who are not on a Suite plan must have Support Professional or Enterprise with any Guide plan to use this feature.

You can use dynamic content to localize content in your help center, especially if you want the button text on your home page to be language specific for users accessing the page in different languages.

**To localize your home page buttons**

- Create the dynamic content in the Admin Center, then insert in the DC placeholder in your help center to make the text dynamic for users accessing in different languages.

 See [Adding translated text to your help center](https://support.zendesk.com/hc/en-us/articles/4408894121754) for instructions.

For example:

```
<div id="divhomecontainer">
<h1 style="text-align: center;">{{dc ‘ADD_YOUR_DC'}} </h1>  
 <h2 style="text-align: center;"> {{dc 'ADD_YOUR_DC'}}</h2>

<form style="display: block; text-align: center; margin: 20px;" class="submitbutton"
action="{{page_path 'new_request'}}">    
 <input type="submit" value="Submit a Request">
</form>

<form  style="display: block; text-align: center; margin: 20px;" class="requestbutton" action="{{page_path 'my_activities'}}">  
   <input type="submit" value="Check your Existing Requests">
 </form>
</div>
```
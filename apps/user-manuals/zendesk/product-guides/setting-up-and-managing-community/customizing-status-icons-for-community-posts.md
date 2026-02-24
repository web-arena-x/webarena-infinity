# Customizing status icons for community posts

Source: https://support.zendesk.com/hc/en-us/articles/4408834617114-Customizing-status-icons-for-community-posts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

**Disclaimer**: This article is provided for instructional purposes only. Zendesk does not support or guarantee the code. Please post any issues you have in the comments section or try searching for a solution online.

The community features are wonderful, especially the post actions. However, what happens when the default actions aren't exactly what you are looking for? Currently there is no way to add or modify the actions that are available, but with Curlybars the existing actions can be re-purposed. Please note that this information will only affect the customer facing actions, as the admin options in the drop-down cannot be modified.

This article contains the following sections:

- [Displaying new status icons](#1)
- [Using dynamic content to translate your statuses.](#2)

## Displaying new status icons

For the purpose of this article, let's say we want to change the actions from Planned, Not Planned, Completed, and Answered to: In the Works, Under Construction, Implemented, and Officially Answered. To make these modifications, the replacement text will need to be inserted in all of the affected pages. To learn more about how to use Curlybars to make these changes, see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250).

The image below displays what the original statuses look like:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Modfying1.1.jpg)

The image below displays what the new statuses will look like:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Modfying2.1.png)

There are two steps to change all customer facing instances to the desired replacement name:

1. [Modifying 'Show all'](#1.1)
2. [Changing status icons' names](#1.2)

### **Modifying 'Show all'**

1. In the Help Center, Edit your theme code. For more information on how to edit a Help Center theme, see [Customizing your Help Center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250-Customizing-your-Help-Center-theme-Guide-Professional-and-Enterprise-#topic_h5c_k4w_n3).
2. Select the community\_topic\_page.hbs as the template to edit.
3. Locate the code for the filter labels inside the dropdowns:

   ![](https://support.zendesk.com/hc/article_attachments/7856438637722)
4. Modify the {{#each filters}} with the following 'identifier' information:

   ```
   {{#each filters}}

    <a href="{{url}}" aria-selected="{{selected}}" role="menuitem">

     {{#is identifier 'all'}}{{name}}{{else}}

     {{#is identifier 'not_planned'}}Gathering Feedback{{/is}}

     {{#is identifier 'planned'}}In the Works{{/is}}

     {{#is identifier 'answered'}}Officially Answered{{/is}}

     {{#is identifier 'completed'}}Implemented{{/is}}

     {{/is}}

    </a>

   {{/each}}
   ```
5. Click **Publish**.

### **Changing status icons' names**

The next change you need to make is for the actual status icons on the Community topic page. Your updated status icons will resemble the image below.

![](https://support.zendesk.com/hc/article_attachments/7856444398618)

1. Scroll down to the {{#is status 'none'}} expression lower on the Community topic page.
2. Enter the following code to change your status icons:

   ```
   {{#is status 'none'}} 
    {{else}} 
    <span class="status-label-{{status_dasherized}} status-label striped-list-status"> 
    {{#is status 'not_planned'}}Gathering Feedback{{/is}} 
    {{#is status 'planned'}}In the Works{{/is}} 
    {{#is status 'answered'}}Officially Answered{{/is}} 
    {{#is status 'completed'}}Implemented{{/is}}</span> 
    {{/is}}
   ```
3. Click **Publish**.
4. Next, select the community\_post\_list\_page.hbs template and locate the same {{#is status 'none'}} expression.
5. Enter in the above code there as well.
6. You have successfully modified your list pages and drop-downs. The only thing left to do is make sure the status indicator on the individual posts reflect the correct wording as shown in the screen shot below.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Modifying5.png)
7. Select the community\_post\_page.hbs template to modify individual posts.
8. Enter the following code on the {{#if post.status}} expression:

   ```
   {{#is post.status 'none'}} 
    {{else}} 
    <span class="status-label-{{post.status_dasherized}} status-label"> 
    {{#is post.status 'not_planned'}}Gathering Feedback{{/is}} 
    {{#is post.status 'planned'}}In the Works{{/is}}   
    {{#is post.status 'answered'}}Officially Answered{{/is}} 
    {{#is post.status 'completed'}}Implemented{{/is}} 
    </span> 
    {{/is}}
   ```

   ![](https://support.zendesk.com/hc/article_attachments/7856444396442)
9. Click **Publish**.

## Using dynamic content to translate your statuses

If your Help Center is available in multiple languages you can use dynamic content helpers to translate your new terms. For more information on dynamic content see, [Dynamic content helpers](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#dc-dynamic-content-helper) and [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content-Professional-and-Enterprise-) .

You can create the dynamic content in Zendesk Support and then use the helpers below in place of the previous term.

**![](https://support.zendesk.com/hc/article_attachments/7856438635802)**

This will enable your status icons to translate for your many customers.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/modifying8.png)

Now that all of your bases are covered, all end-user information should display your own words, and not the default options provided with the feature!
# Displaying an alternative author on your articles

Source: https://support.zendesk.com/hc/en-us/articles/4408828708250-Displaying-an-alternative-author-on-your-articles

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You might need to update the author of an article. For a straightforward change of one author to another, you can [change the author for an article in the UI](https://support.zendesk.com/hc/en-us/articles/4408839258778-Contributor-guide-to-the-Help-Center-knowledge-base#topic_xfc_ndh_qw).

But you might have more complex scenarios for changing authors. Maybe you want to set articles in a certain language to show a specific author or you would like to retain the author's name internally, but publicly you want to have a unified or generic author name. Really, the scenarios are endless. I hope to give you the details on how to get started by using our [help center templating language](https://support.zendesk.com/hc/en-us/articles/4408824571674-Using-the-Help-Center-templating-language).

Note:  This article only addresses changes made to the article template. There are some situations, such as the Search Results page or email subscription notifications, that the author name appears. You may be able to use similar techniques to those found in this article on any template pages, or you may be able to remove the author name altogether. The subscription email cannot be altered at this time.

This article covers the following scenarios:

- [Changing all authors to a standard, single agent](#all_authors)
- [Changing all translations in a certain language to a specific author](#author_via_locale)
- [Selectively changing authors on articles by author ID](#by_author_id)
- [Selectively changing authors on articles by article ID](#by_article_id)
- [Combining multiple criteria to specify the new author](#multiple_criteria)

## Changing all authors to a single agent

The default article page in the theme looks a bit like this:

![](https://support.zendesk.com/hc/article_attachments/4408850946074)

The default code on the Article template looks something like this:

```
<div class="article-avatar">  
 <img src="{{article.author.avatar_url}}" alt="Avatar"/>  
</div>  
<div class="article-meta">  
 <strong class="article-author" title="{{article.author.name}}">  
  {{#if article.author.url}}  
   <a href="{{article.author.url}}" target="_zendesk_lotus">{{article.author.name}}</a>  
  {{else}}  
   {{article.author.name}}  
  {{/if}}  
 </strong>
```

That default code can be found here on the default article template page:

![](https://support.zendesk.com/hc/article_attachments/4408852080922)

We will need to change just a couple of items to set our universal author including the avatar and name. To reduce confusion, I'm just going to remove the author URL and just show a picture and a name. I uploaded a new avatar to my assets as described  [here](https://support.zendesk.com/hc/en-us/articles/4408839332250-Using-themes-and-templates-to-customize-your-Help-Center#topic_hkc_jdw_3k), then I use the  [asset helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#asset-helper)  to call in that image.

Here is the code I used:

```
<div class="article-avatar">  
 {{! User image changed here}}  
 <img src="{{asset 'user_image.jpg'}}" alt="Avatar"/>  
</div>  
<div class="article-meta">  
 {{! 'title' text and name changed here}}  
 <strong class="article-author" title="Help Desk Support">  
  Help Desk Support  
 </strong>
```

And here is the result:

![](https://support.zendesk.com/hc/article_attachments/4408850945690)

We have successfully applied an author name and are showing a new image in place of the actual author's avatar. Now we'll build upon this and set a condition which will only show the change on translations of articles in a specific language/locale.

## Changing all translations in a certain language to a specific author

Depending on your support situation, it may make sense to show the name of an agent who is responsible for handling tickets in a particular language rather than the user who was creating the content for your help center. We can use some logic to check the current locale via the  [help\_center object](https://developer.zendesk.com/apps/docs/help-center-templates/objects#help-center-object)  and determine the outcome from there.

Note:  The conditional statements checking the `help_center.url` property will not work in 'Preview', but will only work on a Published theme. This is because we make some special adjustments to URLs so that you can click between pages when previewing and editing themes.

The default code is the same as above. With some additional conditions, we can make the experience work similar to the last solution:

```
<div class="article-avatar">  
 {{! Checking the current locale value to replace the avatar}}  
 <img src="{{#is help_center.url '/hc/en-us'}}  
  {{asset 'user_image.jpg'}}  
 {{else}}  
  {{article.author.avatar_url}}  
 {{/is}}" alt="Avatar"/>  
</div>  
<div class="article-meta">  
 {{! Checking the current locale to set the author name}}  
 {{#is help_center.url '/hc/en-us'}}  
  <strong class="article-author" title="Language Support Team">  
   Language Support Team  
 {{! Fallback if current locale doesn't match above}}  
 {{else}}  
  <strong class="article-author" title="{{article.author.name}}">  
  {{#if article.author.url}}  
   <a href="{{article.author.url}}" target="_zendesk_lotus">  
    {{article.author.name}}  
   </a>  
  {{else}}  
   {{article.author.name}}  
  {{/if}}  
 {{/is}}  
  </strong>
```

You may have to visit your help center in your desired locale to get the text string to replace my `/hc/en-us` above. If you want to set multiple conditions, you can either nest the `#is` conditional statements inside of one another, or set an independent statement for each one of your locales. If you're interested in these types of conditional statements (is, if, each), you can read more  [here](https://developer.zendesk.com/apps/docs/help-center-templates/introduction#conditional-helpers).

## Selectively changing authors on articles by author ID

Note:  You can also change the author for an article in the UI. See [Changing the author for an article](https://support.zendesk.com/hc/en-us/articles/4408839258778-Contributor-guide-to-the-Help-Center-knowledge-base#topic_xfc_ndh_qw).

It's possible you may run into a situation where one of your main contributors leaves the company or moves into a bigger and better role, but you would like to have the face of someone in Support on your articles. By using a conditional statement, we can check the author's identity and then replace their info with one of your remaining agents.

```
<div class="article-avatar">  
 {{! Checking the identity of the author to replace the avatar}}  
 <img src="{{#is article.author.id 319145489}}  
  {{asset 'user_image.jpg'}}  
 {{else}}  
  {{article.author.avatar_url}}  
 {{/is}}" alt="Avatar"/>  
</div>  
<div class="article-meta">  
 {{! Checking the identity of the author to replace the name with 'John Smith'}}  
 {{#is article.author.id 319145489}}  
  <strong class="article-author" title="Jill Smith">  
   Jill Smith  
  </strong>  
 {{! Fallback if author is not user 319145489}}  
 {{else}}  
  <strong class="article-author" title="{{article.author.name}}">  
   {{#if article.author.url}}  
    <a href="{{article.author.url}}" target="_zendesk_lotus">  
     {{article.author.name}}  
    </a>  
   {{else}}  
    {{article.author.name}}  
   {{/if}}  
 {{/is}}  
  </strong>
```

You will want to replace my `319145489` with the ID of your user who you are looking to replace as the author, and with this solution all other articles will still appear with their current authors. Only user `319145489` 's articles will be affected.

## Selectively changing authors on articles by article ID

Note:  You can also change the author for an article in the UI. See  [Changing the author for an article](https://support.zendesk.com/hc/en-us/articles/4408839258778-Contributor-guide-to-the-Help-Center-knowledge-base#topic_xfc_ndh_qw).

Very similar to the last solution, you can change the author by utilizing a specific article's ID. Maybe you want to have an article on a specific topic appear as being authored by a different agent. Here how we would get this done:

```
<div class="article-avatar">  
 {{! Checking the article id to replace the avatar}}  
 <img src="{{#is article.id 208598226}}  
  {{asset 'user_image.jpg'}}  
 {{else}}  
  {{article.author.avatar_url}}  
 {{/is}}" alt="Avatar"/>  
</div>  
<div class="article-meta">  
 {{! Checking the article id to replace the name}}  
 {{#is article.id 208598226}}  
  <strong class="article-author" title="John Smith">  
   John Smith  
  </strong>  
 {{! Fallback if article id is not 208598226}}  
 {{else}}  
  <strong class="article-author" title="{{article.author.name}}">  
  {{#if article.author.url}}  
   <a href="{{article.author.url}}" target="_zendesk_lotus">  
    {{article.author.name}}  
   </a>  
  {{else}}  
   {{article.author.name}}  
  {{/if}}  
 {{/is}}  
  </strong>
```

I recommend using this solution in a limited fashion. The `is` helper cannot check if an article equals multiple values (like an or statement), so you would have to nest multiple conditional statements within one another to check multiple article IDs.

## Combining multiple criteria to specify the new author

Suppose I have an agent who I want to show as the author for all of my content in a specific language, but I only want to replace one author. You can setup multiple conditional statements to check properties like author ID and the locale, and then take action on those conditions like this:

```
<div class="article-avatar">  
 <img src="{{#is help_center.url '/hc/ar'}}  
  {{#is article.author.id 319145489}}  
   {{! Avatar value if author is 319145489 and language is Arabic}}  
   {{asset 'user_image.jpg'}}  
  {{else}}  
   {{! Avatar value if author is not 319145489 and language is Arabic}}  
   {{article.author.avatar_url}}  
  {{/is}}  
 {{else}}  
  {{! Avatar value if language is not Arabic}}  
  {{article.author.avatar_url}}  
 {{/is}}" alt="Avatar"/>  
</div>  
<div class="article-meta">  
 {{#is help_center.url '/hc/ar'}}  
  {{#is article.author.id 319145489}}  
   {{! Author name if author id is 319145489 and language is Arabic}}  
   <strong class="article-author" title="John Smith">  
    John Smith  
  {{else}}  
   {{! Start Author Name if Arabic and not author 319145489}}  
   <strong class="article-author" title="{{article.author.name}}">  
   {{#if article.author.url}}  
    <a href="{{article.author.url}}" target="_zendesk_lotus">  
     {{article.author.name}}  
    </a>  
   {{else}}  
    {{article.author.name}}  
   {{/if}}  
  {{/is}}  
 {{else}}  
  {{! Start author name if not Arabic}}  
  <strong class="article-author" title="{{article.author.name}}">  
  {{#if article.author.url}}  
   <a href="{{article.author.url}}" target="_zendesk_lotus">  
    {{article.author.name}}  
   </a>  
  {{else}}  
   {{article.author.name}}  
  {{/if}}  
 {{/is}}  
  </strong>
```

Due to the way conditional statements work, we had to repeat some code here to satisfy all of the scenarios, but now we have successfully replaced a specific author when they appear on articles only in Arabic.
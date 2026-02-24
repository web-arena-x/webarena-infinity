# Using the help center templating language

Source: https://support.zendesk.com/hc/en-us/articles/4408824571674-Using-the-help-center-templating-language

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

This article covers the following topics:

- [Introduction](#toc_1)
- [Templating basics](#toc_2)
- [Comments](#toc_3)
- [Block Comments](#toc_4)
- [Literals](#toc_5)
- [Properties](#toc_6)
- [Conditionals](#toc_7)
- [How conditions are evaluated](#toc_8)
- [Trimming white space](#toc_9)
- [Helpers](#toc_10)
- [Changing scope](#toc_11)
- [Passing the root context to a helper](#toc_12)
- [Accessing items in an array](#toc_13)
- [Length](#toc_14)
- [Subexpressions](#toc_15)

### Introduction

Each help center theme consists of a collection of [editable page templates](https://support.zendesk.com/hc/en-us/articles/4408839332250-Customizing-Help-Center#topic_h5c_k4w_n3) that define the layout of different types of pages in help center. For example, there's a template for knowledge base articles, a template for the list of requests, and so on.

Each template consists of a mix of HTML markup and Handlebars-like expressions, identifiable in the template by double curly brackets. [Handlebars](http://handlebarsjs.com) is a simple templating engine that lets you insert or manipulate content on a page at render-time rather than at design-time.

The templating language in help center is called *Curlybars* and implements a large subset of the Handlebars language. This guide shows you how use the language to customize your pages in help center.

help center provides you with helpers and named properties to customize your content. Some are shared and available on all help center pages. The rest are page-specific.

**Example**

```
{{#each comments}}
  <li class="comment" id="{{comment_id}}">
    <div class="comment-avatar {{#if author.agent}} comment-avatar-agent {{/if}}">
      <img src="{{author.avatar_url}}" alt="Avatar" />
    </div>

    <div class="comment-container">
      <header class="comment-header">
        <strong class="comment-author">
          {{author.name}}
        </strong>
      </header>
    </div>
  </li>
{{/each}}
```

The example generates a list of users who left comments on the page. The `each` helper iterates through each value in the page's `comments` property. For each comment, the values of the `author.avatar_url` and `author.name` properties are inserted in the HTML.

Note: Before making custom changes to your help center, take a few minutes to check out the support tip [Preventing poor help center load times by following templating best practices](https://support.zendesk.com/hc/en-us/articles/227065927) by Jake Bantz.

### Templating basics

This section introduces the building blocks you need to write any template. For more information, see [Help Center Templates](https://developer.zendesk.com/apps/docs/help-center-templates/introduction) on developer.zendesk.com.

A Curlybars template is made up of two things: verbatim text to be rendered as is, and Curlybars expressions. This implies that an empty template is also a valid template, and a template that contains only text is also a valid one. For instance, the following is a valid template:

```
<h1>Article</h1>

<p>Some details on the article</p>
```

Of course, if help center templates only supported verbatim text, you couldn't really customize them at render-time. To add templating logic, you need Curlybars expressions, which are enclosed double curly brackets(`{{` and `}}`).

To add templating logic to the previous example, you might modify the template as follows:

```
<h1>Article</h1>

<p>Some details on the article</p>

{{article.author.name}}
```

The following sections explain how to write valid expressions to make meaningful changes to the template.

Note that nesting a pair of curlies within other pair of curlies is not valid syntax. For example, the following isn't allowed:

```
<h1>Article</h1>

<p>Some details on the article</p>

{{ {{ ... }} }}
```

### Comments

There are situations where having some notes in the template that do not leak into the rendered page might come in handy. For this purpose, Curlybars allows to make comments putting an exclamation mark right after the opening curlies, without any space: `{{! ... }}`. You can use this syntax to add a code comment in the example:

```
{{!
  This template aims to
  show details of an article
}}

<h1>Article</h1>

<p>Some details on the article</p>
```

Here's what's sent to the browser after the page is rendered:

```
<h1>Article</h1>

<p>Some details on the article</p>
```

This effect of discarding anything within the comments can actually come in handy while developing a template. You might want to comment out some code to do some checks, debug, and more.

#### Block Comments

Unfortunately, the comment syntax described so far isn't suitable for commenting out Curlybars code. To comment out Curlybars code, use the following syntax: `{{!-- ... ---}}`. This kind of comment can span several lines and effectively comment out code. Example:

```
{{!
  This template aims to
  show details of an article
}}

<h1>Article</h1>

<p>Some details on the article</p>

{{!--
  I want to commend out the following code:

  {{ ... some Curlybars expressions }}

--}}
```

The template above is rendered as follows:

```
<h1>Article</h1>

<p>Some details on the article</p>
```

### Literals

To include values that you want Curlybars to interpret exactly as they're written, Curlybars supports the concept of *literals*. A literal can represent 3 types of values: a **string**, a **boolean**, or a **number**.

To express a string, you can use both single and double quotes, but you can't mix them. For example, `'this is a valid string'`, `"this is valid as well"`, but `"this is not valid'`.

A number can be any positive or negative integer. `123` is a valid positive number, `+123` represents the same value, `00123` is still valid, and `-123` is valid as well.

A boolean is represented by `true` and `false`. No other variation is allowed. For example, `TRUE` and `FALSE` aren't intepreted as booleans in Curlybars.

You can render literals. Example:

```
A string: {{ 'hello world' }}
A boolean: {{ true }}
A number: {{ 42 }}
```

The page is rendered as follows:

```
A string: 'hello world'
A boolean: true
A number: 42
```

### Properties

Every template in the help center has access to a *context* that represents data about your help center. For instance, the Article Page template has an object named `article` that exposes the structure of the article requested by the users. For all the properties you can use in your templates, see [Help Center Templates](https://developer.zendesk.com/apps/docs/help-center-templates/introduction) on developer.zendesk.com.

Use dot notation to pluck a specific information from these objects. A simple example is `article.title`.

The fully qualified name of a property is sometimes called a *path*. For example, `name` is a property in the `author` object, but `article.author.name` is its path.

You can display the value of a property by enclosing it within double curly brackets. Getting back to the example, you might want to print out the name of the author in a separate paragraph:

```
<h1>Article</h1>

<p>Author: {{article.author.name}}</p>
```

Let's say a user wants to see an article written by an agent named John Venturini. The template will be rendered as follows:

```
<h1>Article</h1>

<p>Author: John Venturini</p>
```

You might also want to render the article itself. The `article` object has a `body` property that contains the content of the article. You'd modify the template as follows to render the body of the article:

```
<h1>Article</h1>

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>
```

### Conditionals

In addition to rendering property values, the templating language lets you add conditional rendering logic to your templates.

For instance, you might want to render a snippet of HTML in case the requested article is internal. The Article Page context has an `article.internal` property that returns `true` if the article is internal and `false` otherwise.

You can create an `if` block with this information. The `if` expression must specify a condition that's true or false. The result determines whether the content in the block is rendered or not. Here's the basic syntax:

```
{{#if condition}}
  This is rendered if the condition is true.
{{/if}}
```

You can modify the example template as follows:

```
<h1>Article</h1>

{{#if article.internal}}
  <p>This article is internal.</p>
{{/if}}

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>
```

You might want to render a block when the condition is false. In that case, use an `unless` block. The syntax is similar to the `if` block:

```
{{#unless condition}}
  This is rendered if the condition is false.
{{/unless}}
```

Back to the example, suppose you also want to render a message when an article is not internal. You can modify the template as follows:

```
<h1>Article</h1>

{{#if article.internal}}
  <p>This article is internal.</p>
{{/if}}

{{#unless article.internal}}
  <p>This is a publicly visible article!</p>
{{/unless}}

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>
```

This kind of conditional logic -- "if true do this or else do this" -- is usually handled by an `if-else` block. The syntax is as follows:

```
{{#if condition}}
  This is rendered if the condition is true.
{{else}}
  This is rendered if the condition is false.
{{/if}}
```

You can modify the example as follows:

```
<h1>Article</h1>

{{#if article.internal}}
  <p>This article is internal.</p>
{{else}}
  <p>This is a publicly visible article!</p>
{{/if}}

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>
```

The `unless` block also has an `unless-else` variant. You could use it to achieve the same result as an `if-else` block:

```
<h1>Article</h1>

{{#unless article.internal}}
  <p>This is a publicly visible article!</p>
{{else}}
  <p>This article is internal.</p>
{{/unless}}

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>
```

#### How conditions are evaluated

A condition is usually a help center property such as `article.internal`, which has a boolean value of **true** or **false**. Some properties don't have boolean values. These properties are evaluated as follows:

- If the value is a number, then 0 is false and any other number is true
- If the value is a string, an empty string is false and any other string is true
- If the value is a collection of objects, an empty collection is false and any other collection is true
- If the value is null, the expression is false

Suppose you want to set up some conditional logic that checks numbers. The Article Page has an `article.comment_count` property that contains the total number of comments in an article. You can use the `if` condition to test if the count is not `0` and display some cheerful message. Example:

```
<h1>Article</h1>

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>

{{#if article.comment_count}}
  <p>Yahoo! This article has got some comments!</p>
{{/if}}
```

### Trimming white space

When Curlybars processes a template, it displays any verbatim text as is. That's good and works well most of the time. However, sometimes you need to have more control on the blank characters next to an expression. Take the following code for example:

```
<a href="..." class="{{#if highlighted}} highlight {{/if}}">Click me!</a>
```

It renders the following HTML when `highlighted` is true:

```
<a href="..." class=" highlight ">Click me!</a>
```

There's a leading and a trailing space around the word *highlight*. This of course works fine, but suppose you want to keep the spaces in the template without rendering them. You can use the tilde character (~).

Adding a tilde character in your opening or closing curly brackets trims white space from the enclosed text. Example:

```
<a href="..." class="{{#if highlighted~}} highlight {{~/if}}">Click me!</a>
```

The tilde characters trim the leading and a trailing spaces around the word *highlight*:

```
<a href="..." class="highlight">Click me!</a>
```

The tilde character trims any blank character that doesn't have a graphical representation but affects spacing or split lines, such as newlines, tabs, carriage returns, line feeds, simple spaces, or tabs. This means you can take the example to an extreme and express the previous `if` block on more lines to make it more readable. Example:

```
<a href="..." class="
  {{~#if highlighted~}}
    highlight
  {{~/if~}}
">Click me!</a>
```

This still renders as follows:

```
<a href="..." class="highlight">Click me!</a>
```

These examples don't make much sense in real life, but the effectiveness of using the tilde character can vary from case to case.

### Helpers

Accessing data, displaying it, and adding some conditional logic can be all you need in some templates. Still, you might like some added functionality. For example, you might want to display a localized string that changes according to the locale of the page requester. Or you might want to truncate a long passage of text.

You can get this kind of functionality in templates with *helpers*. For all the helpers you can use in your templates, see [Help Center Templates](https://developer.zendesk.com/apps/docs/help-center-templates/introduction) on developer.zendesk.com.

For example, you can use a helper named `excerpt` in the Article page template to truncate strings. In the article example, suppose you need to show a truncated version of the article title. You can do this by modifying the template as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

<p>Author: {{article.author.name}}</p>

<article>{{article.body}}</article>
```

The example above shows that curly brackets are used to invoke a helper. The `excerpt` helper accepts a parameter that consists of an expression that resolves to a string. The helper has a `characters` option to specify the number of characters to keep. The `characters` option isn't mandatory. If you don't specify it, a default value is used. See [excerpt](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#excerpt-helper) in Help Center Templates for further details.

The syntax to invoke a helper is `{{<helper> [<param> ...] [<key=value> ...]}}`. The only mandatory element is the name of the helper. Parameters and options vary depending on the helper.

Now, suppose you want to update the template to display a cheerful message when the author's name is John Venturini. Unfortunately, you can't use an `if` condition to check if `article.author.name` is equal to `"John Venturini"` because `if` only works on one expression. Comparison operators like `==` are not available.

How to add such a logic then? Fortunately, you can use the `is` helper. It takes two parameters and tests them for equality. Example:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#is article.author.name 'John Venturini'}}
  <p>Cool! John Venturini is the author of this article!</p>
{{/is}}

<article>{{article.body}}</article>
```

The snippet above renders the cheerful message if the author is John Venturini. But what if you want to render a different message if it's not him? The good news is that `is` can also include an `else` block just like the `if-else` statement. To restore the old message if the author is not John Venturini, you can add an `else` block as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#is article.author.name 'John Venturini'}}
  <p>Cool! John Venturini is the author of this article!</p>
{{else}}
  <p>Author: {{article.author.name}}</p>
{{/is}}

<article>{{article.body}}</article>
```

### Changing scope

Accessing data is pretty straightforward using dot notation, especially when the path to the information we need is not too long. Example: `article.title`. In some circumstances, though, you might want to access a property with a longer path. Example: `article.author.name`. You can use longer paths in templates if you want. For example, you can add the author's name and avator in the example as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

<img src="{{article.author.avatar_url}}" alt="Author's avatar" height="42" width="42">
{{#is article.author.name 'John Venturini'}}
  <p>Cool! John Venturini is the author of this article!</p>
{{else}}
  <p>Author: {{article.author.name}}</p>
{{/is}}

<article>{{article.body}}</article>
```

The snippet above works just fine, but the long property paths make the code look a little cluttered. One way around the problem is to use the special `with` construct. `with` accepts one parameter that represents the base context to use in the code block associated with it. The syntax is as follows:

```
{{#with <context>}}
   ...
{{/with}}
```

You can improve the example as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#with article.author}}
  <img src="{{avatar_url}}" alt="Author's avatar" height="42" width="42">
  {{#is name 'John Venturini'}}
    <p>Cool! John Venturini is the author of this article!</p>
  {{else}}
    <p>Author: {{name}}</p>
  {{/is}}
{{/with}}

<article>{{article.body}}</article>
```

The `article.author` parameter eliminates the need to include `article.author` in any paths in the block. So `{{name}}` inside the block is equivalent to `article.author.name` outside the block.

You can't use `article.author.name` in the block because it would be evaluated as `article.author.article.author.name`. Similarly, you can't access the title of the article in the block with `article.title` because the article object is accessible only in the root context, which is outside the block.

To escape from the context set by `with` and access the outer context, use the `../` notation in the path. You can render the title of the article inside the `with` block as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#with article.author}}
  {{../article.title}}

  <img src="{{avatar_url}}" alt="Author's avatar" height="42" width="42">
  {{#is name 'John Venturini'}}
    <p>Cool! John Venturini is the author of this article!</p>
  {{else}}
    <p>Author: {{name}}</p>
  {{/is}}
{{/with}}

<article>{{article.body}}</article>
```

You can use the `../` notation repeatedly in the same path. It'll jump back the same number of contexts. For instance, the following example will still work as expected:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#with article}}
  {{#with author}}
    {{../../article.title}}

    ...

{{/with}}

<article>{{article.body}}</article>
```

You might want to be defensive and render a specific message whenever the author is not specified. You might decide to use an `if` block to do this, as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#if article.author}}
  {{#with article.author}}
    ...
  {{/with}}
{{else}}
  No author is present for this article!
{{/if}}

<article>{{article.body}}</article>
```

Note that in Help Center, `article.author` is actually never null. We assumed so here only for the sake of the example.

The snippet above works just fine, but you can achieve the same result with an `else` block in the `with` construct. The else block is executed if the parameter is falsy. You can modify the example as follow:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#with article.author}}
  ...
{{else}}
  No author is present for this article!
{{/with}}

<article>{{article.body}}</article>
```

Using an `else` block also makes the code more readable.

#### Passing the root context to a helper

Use the `this` keyword to pass the current root context to a helper. Suppose you have a `render_author` helper that accepts an `article` object as a parameter in order to display details about its author. You can use the `this` keyword as follows:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#with article}}
  {{render_author this}}
{{/with}}

<article>{{article.body}}</article>
```

`this` will be resolved as `article`.

### Accessing items in an array

Some help center properties consist of arrays of objects. For example, the `attachments` property consists of an array of attachments.

To access the items in an array, you need to iterate over each one. The `each` helper does exactly that. Example:

```
<h1>{{excerpt article.title characters=50}}</h1>

{{#with article.author}}
  ...
{{/with}}

<article>{{article.body}}</article>

{{#each attachments}}
  <a href="{{url}}" target="_blank">{{name}}</a>
  <span>({{size}})</span>
{{/each}}
```

The snippet above lists all the attachments. Each list item displays data specific to one attachment, such as its `url`, `name`, and `size`.

Like `with`, `each` changes the context in its block. This means that if you want to access the outer context, you can use the `../` notation.

You might want to render a message when an array is empty. You can easily achieve this by using an `if` block, as follows:

```
...

{{#if attachments}}
  {{#each attachments}}
    <a href="{{url}}" target="_blank">{{name}}</a>
    <span>({{size}})</span>
  {{/each}}
{{else}}
  Sorry, no attachments available!
{{/if}}
```

This works just fine, but you could also use an `else` block to make the code easier to read:

```
...

{{#each attachments}}
  <a href="{{url}}" target="_blank">{{name}}</a>
  <span>({{size}})</span>
{{else}}
  Sorry, no attachments available!
{{/each}}
```

### Length

Every array has an implicit `length` property that gives the number of elements in the array. For example, if you want to display the number of attachments, use the `length` property as follows:

```
...

There are {{attachments.length}}.

{{#each attachments}}
  <a href="{{url}}" target="_blank">{{name}}</a>
  <span>({{size}})</span>
{{/each}}
```

### Subexpressions

Subexpressions allow you to invoke multiple helpers within a single expression, and pass the results of inner helper invocations as arguments to outer helpers. Subexpressions are delimited by parentheses.

The following example shows a subexpression in an expression:

```
{{search placeholder=(dc "search_text")}}
```

Subexpressions can be nested:

```
{{search placeholder=(excerpt (dc "search_text"))}}
```

Subexpressions can be used in conditional helpers:

```
{{#if (compare collection.length "==" 0)}}  
  <div>Empty collection.</div>  
{{else}}  
  <div>Your collection has {{collection.length}} items</div>  
{{/if}}
```

Subexpressions can be used in array iterator helpers:

```
{{#each (slice (filter user.badges on="category_slug" equals="achievements")   
0 4)}}  
  
   <section>  
      <h3>{{name}}</h3>  
      <div>{{description}}</div>  
   </section>  
{{/each}}
```
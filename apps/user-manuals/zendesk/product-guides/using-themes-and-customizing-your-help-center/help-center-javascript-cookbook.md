# Help center JavaScript cookbook

Source: https://support.zendesk.com/hc/en-us/articles/4408836487450-Help-center-JavaScript-cookbook

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

This JavaScript cookbook helps you customize your help center's look and feel using JavaScript and jQuery. You can modify elements like link text, form fields, and language selectors. The guide provides code snippets for tasks such as hiding fields, renaming labels, and adding headers. Note that these customizations apply to older templating versions.

Note: These recipes apply only if you have help center templating version 3 or earlier. Newer versions of the help center templating language uses React instead of jQuery. See [About templating versions for help center themes](https://support.zendesk.com/hc/en-us/articles/4408820214554) and [Checking your templating version](https://support.zendesk.com/hc/en-us/articles/4408820214554#topic_llb_t5g_skb__section_psp_hwg_skb).

In templating version 3 or earlier, you can easily customize the look and feel of a help center using JavaScript and jQuery. This cookbook is designed to help you make your help center look the way you want.

jQuery is not provided by default. Make sure that you import a jQuery library if you want to use jQuery statements in a theme in place of vanilla JavaScript. See [Importing or upgrading jQuery](importing-or-upgrading-jquery.md) for more information.

Note: Trial users are given the Professional plan, which includes code editing options, but they can no longer access that feature if they purchase a Team plan.

To access and edit the JavaScript in your help center, see [Customizing the CSS or JavaScript](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_gxl_3qw_n3).

You can also customize your help center using the Help Center templating language or CSS:

- [Help center templates reference](https://developer.zendesk.com/apps/docs/help-center-templates/introduction)
- [Help center templating cookbook](https://support.zendesk.com/hc/en-us/articles/4408832681626)
- [Help center CSS cookbook](https://support.zendesk.com/hc/en-us/articles/4408842914714)

## Recipe list

We'll be adding more recipes over time but we can never hope to be exhaustive. The number of things you can do with JavaScript is limited only by your imagination. Please post your recipes in the comments section and we'll add them to this cookbook.

- [Change the My Activities link text](#topic_uwl_mq4_4v)
- [Hide custom fields in the ticket sidebar in My Activities](#topic_rpj_fg5_ncc)
- [Rename the "Subject" and "Description" labels on the Request form](#topic_ikg_yr4_4v)
- [Prepopulate the fields of custom ticket forms](#topic_jbp_fs4_4v)
- [Change the order of custom fields on the Request form](#topic_qbk_h54_4v)
- [Add headers to the Request form](#topic_rkn_s54_4v)
- [Hide a language in the language dropdown](#topic_jn1_dv4_4v)
- [Replace text strings in the language selector with flag icons](#topic_jm5_jv4_4v)
- [Hide the Community based on the selected language](#topic_ujz_vv4_4v)

Note: When you edit the page templates, CSS, or JavaScript for a standard theme, or when you develop your own theme, it is saved as a *custom theme*. Recipes that require custom themes are *not* supported by Zendesk and are *not* automatically updated when new features or themes are released (see [About standard themes and custom themes in help center](https://support.zendesk.com/hc/en-us/articles/4408821255834)).

## Change the My Activities link text

Add the my activities class to the header.hbs template:

```
{{link "my_activities" role="menuitem" class='my-activities'}}
```

Add the following jQuery statement to the `$(document).ready(function()` function in the JavaScript template:

```
$(' .my-activities').html(' See my requests');
```

## Hide custom fields in the ticket sidebar in My Activities

You can use JavaScript to hide custom fields in the ticket sidebar on the My Activities page. You select the custom fields based on their labels. For example, if the label of a custom field is "Member rewards", you can hide the field if its label contains "Member" or "rewards" or "Member rewards".

Add the following jQuery function in the script.js file:

```
$(document).ready(function() {
  if (window.location.href.indexOf('/requests') > -1) {
    setTimeout(function() {
      $('dt:contains("Member rewards")').hide().next('dd').hide(); 
      // add more selectors as necessary
    }, 1000); // adjust the timeout duration as needed
}});
```

## Rename the "Subject" and "Description" labels on the Request form

Add the following jQuery statements to the `$(document).ready(function()` function in the JavaScript template:

```
$('label[for=request_subject]').html("Custom Subject");
$('label[for=request_description]').html("Custom Description");
```

## Prepopulate the fields of custom ticket forms

Note: Only certain plans support multiple ticket forms. For a list, and for general information about how ticket forms work, see [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858).

Suppose you use a custom ticket form in your help center to let users register products. You can detect the form and prepopulate its fields when a user opens it in the help center.

You'll need the ticket form ID, which you can find in the form's URL in your help center. See [this example](http://screencast.com/t/bxNkmJmq).

The following jQuery example prepopulates the Subject field with "Product registration" and the Description field with "This is a new product registration". Add the statements to the `$(document).ready(function()` function in the JavaScript template:

```
var ticketForm = location.search.split('ticket_form_id=')[1];
if(ticketForm == 18570) {
  $('section.main-column h1').html('Product Registration');
  $('#request_subject').val('Product Registration');
  $('#request_description').val('There is a new product registration.');
  $('#request_subject').parent('.request_subject').hide(); // Hide subject
  $('#request_description').parent('.request_description').hide(); 
  $("<p>Please upload your product receipt here.<p>").insertAfter('label:contains("Attachments")'); // Adds text below "Attachments"
}
```

## Change the order of custom fields on the Request form

You'll need the ids of the custom fields, which you can find in the Zendesk Support interface. See [this example](http://screencast.com/t/Wq4MRelm6).

```
var firstName = $('input#request_custom_fields_22231170').parent();
var lastName = $('input#request_custom_fields_22231180').parent();
firstName.insertBefore($('input#request_subject').parent());
lastName.insertBefore($('input#request_subject').parent());
```

## Add headers to the Request form

Add the following jQuery statements to the `$(document).ready(function()` function in the JavaScript template:

```
 $('.form-field.request_anonymous_requester_email').prepend('<h2>Your personal information</h2>')
 $('.form-field.request_subject').prepend('<h2>Your issue</h2>');
 $('.form-field.request_custom_fields_21875914').prepend('<h2>Your device information</h2>');
 $('.form-field.request_custom_fields_22033620').prepend('<h2>Your purchase information</h2>');
 $('.form-field > label:contains("Attachments")').prepend('<h2>Support attachments</h2>');
```

## Hide a language in the language dropdown

Hiding a language in the language selector can be useful if the content in that language isn't ready for release. Add the following jQuery statement to the `$(document).ready(function()` function in the JavaScript template:

```
$("ul.dropdown-panel li a:contains('Français')").hide();
```

## Replace text strings in the language selector with flag icons

For example, if your help center provides content in U.S. English and German, you could display the national flags instead of "U.S. English" and "Deutsch" in the language selector. Add the following jQuery statement to the `$(document).ready(function()` function in the JavaScript template:

```
$(function(){
$('a.dropdown-toggle:contains("English (US)")').html('<img src="http://icons.iconarchive.com/icons/gosquared/flag/48/United-States-flat-icon.png" width="48" height="48">');
$('a.dropdown-toggle:contains("Deutsch")').html('<img src="http://icons.iconarchive.com/icons/gosquared/flag/48/Germany-flat-icon.png" width="48" height="48">');
$('a:contains("English (US)")').html('<img src="http://icons.iconarchive.com/icons/gosquared/flag/48/United-States-flat-icon.png" width="48" height="48">');
$('a:contains("Deutsch")').html('<img src="http://icons.iconarchive.com/icons/gosquared/flag/48/Germany-flat-icon.png" width="48" height="48">');
});
```

## Hide the Community based on the selected language

Add the following jQuery statement to the `$(document).ready(function()` function in the JavaScript template:

```
if (document.location.pathname.match( (/hc\/de/) || (/hc\/es/) )) {
  $('.community').hide();
}
```
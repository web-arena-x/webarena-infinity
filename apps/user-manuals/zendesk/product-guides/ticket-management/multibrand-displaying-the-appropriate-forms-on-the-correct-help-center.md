# Multibrand: Displaying the appropriate forms on the correct Help Center

Source: https://support.zendesk.com/hc/en-us/articles/4408829681050-Multibrand-Displaying-the-appropriate-forms-on-the-correct-Help-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

This workaround is only necessary in select scenarios like if you want to use a form for Web Widget, but not in Help Center. Please reference [Creating and applying branded ticket forms](https://support.zendesk.com/hc/en-us/articles/4408822414490) to find out how to selectively display different forms for different brands.

I've created multiple Help Centers for all of my brands, and now I'm ready to roll out ticket forms for each of the brands. But wait! I don't want my forms for my primary brand to show up on my Help Center for my secondary brand. Well this little trick is hopefully just the thing to fix that.

This article covers two scenarios:

- [Selecting ticket forms for brands with multiple forms](#multiple_forms)
  - [The code: Option 1](#Option_1)
  - [The code: Option 2](#Option_2)
- [Displaying only one ticket form per brand](#only_one_form)
  - [The code](#Code_2)
  - [Remove form selection dropdown from ticket form](#Remove)

**Note:**  Before you can begin to select forms, you must find the IDs of the forms you want to hide. Follow the steps below for information on how to find your form IDs.

### Finding the form IDs

Whether you want to hide a form or single it out, for you to be able to target the individual forms, you have to first find the form IDs. This article will not cover creating  forms. For more information on creating forms see,  [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858-Creating-ticket-forms-to-support-multiple-request-types-Enterprise-)  .

Here is how you can find the IDs quickly in the agent interface:

1. In[Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then click **Tickets > Forms**.
2. Click the name of the form you want to hide or use as your standalone form.
3. Take note of the form ID in the address bar as shown below:  
     
   ![](https://support.zendesk.com/hc/article_attachments/7856440054554)
4. Repeat for each form you would like to hide or isolate.

### Displaying multiple forms per brand

Often times each Help Center will manage multiple types of requests. This section will show you how to selectively hide any ticket forms you do not want to appear in a particular brand's Help Center, while still enabling the end-user to select the remaining forms.

![](https://support.zendesk.com/hc/article_attachments/7856445840922)

### The code

Now that we have recorded the ticket forms that we want to hide as  [described above](#find_form_ID)  , we can now target them with the code below.

You will want to place one of these versions of code in the  **`$(document).ready(function(){`**  in the `script.js` template when customizing your Help Center.

**Note:**  When you copy and paste the code, make sure to enter in your own form IDs, not the ones given in this example.

#### Option 1

In this first option, you simply repeat the lines where the form IDs are located. My form IDs are `12775` and `31495` .

![](https://support.zendesk.com/hc/article_attachments/7856445840410)

```
//remove the options from the dropdown selector
$('#request_issue_type_select option[value="12775"]').remove();
$('#request_issue_type_select option[value="31495"]').remove();
//remove the options from the nesty-input after it's been created. 

$('.nesty-panel').on('DOMNodeInserted', function(e){
    $(this).children('ul').children().remove('#12775');
    $(this).children('ul').children().remove('#31495');
});
```

#### Option 2

Now in this 2nd option, I've instead decided to use an array, so we can simply input the list of forms we want to hide inside of the square brackets  **`[ 12775,31495 ]`**  . You must  separate each ID with a comma. This will loop through the function until all IDs have been removed.

![](https://support.zendesk.com/hc/article_attachments/7856445839898)

```
$.each([ 12775,31495 ], function( index , formValue ) {
  $('#request_issue_type_select option[value="' + formValue + '"]').remove();
  
 $('.nesty-panel').on('DOMNodeInserted', function(e){
    $(this).children('ul').children().remove('#' + formValue);
 });
});
```

### Displaying one form per brand

Now you might be saying, "I only need one form for each brand." That's a perfectly acceptable workflow too! Instead of having to hide all of the extra brands, you could change your 'Submit a request' link to send users to one of your forms directly, and then hide the 'Please choose your issue below' dropdown list on the form.

### The code

To send your users to one form, you will need your own form ID found in the  [steps above](#find_form_ID)  .

We can easily replace the 'Submit a request' link by using the Help Center templating language Curlybars. You can find some more Curlybars and templating documentation  [here](https://developer.zendesk.com/apps/docs/help-center-templates/introduction)  .

You will want to place this code in the Header template where you want the 'Submit a Request' link to appear (be sure to replace the `ticket_form_id` with your own). This does take localization into consideration, so the link will be offered in the appropriate language if you have multiple languages offered in your Help Center:

```
<a href="{{page_path 'new_request' ticket_form_id='17369'}}">{{t 'submit_a_request'}}</a>
```

![](https://support.zendesk.com/hc/article_attachments/7856440052122)

### Remove form selection dropdown from ticket form

Next, we want to remove the form selection dropdown from the ticket form, so users don't select an alternate form for the current brand. You will want to place this code in the `style.css` template of your Help Center:

```
.request_ticket_form_id{
     display:none;
}
```

![](https://support.zendesk.com/hc/article_attachments/7856440051738)  
Enter the CSS in the `style.css` template.

### How it Works

When the new request page is generated, all end-user facing ticket forms are made available in the dropdown list. The first example removes the form options which you do not want to appear for each specified brand and the second example simply directs users to one specific form for your brand.
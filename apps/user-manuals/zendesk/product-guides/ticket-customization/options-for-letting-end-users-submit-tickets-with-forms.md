# Options for letting end users submit tickets with forms

Source: https://support.zendesk.com/hc/en-us/articles/4408846913050-Options-for-letting-end-users-submit-tickets-with-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The Zendesk help center provides end users with a default [HTML form](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_hgd_mqd_yy) for submitting
tickets:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_submit_request_form.png)

It's a good starting point but it might not meet all your needs. Here are other
options, including:

- [Customizing the help center ticket form](#topic_ixm_hbv_z1b)
- [Embedding a ticket form in your website](#topic_rdc_r2v_z1b)
- [Building a ticket form](#topic_qt5_w2v_z1b)

## Customizing the help center ticket form

You can add custom fields to the help center form or change its look and
feel.

Note: If you have the Professional add-on or are on
Enterprise, you can define multiple custom forms for
different types of requests.

Resources:

- [Adding custom fields
  to your tickets and support request
  forms](https://support.zendesk.com/hc/en-us/articles/4408883152794)
- [Customizing your help
  center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250)
- [Creating and applying
  branded ticket forms](https://support.zendesk.com/hc/en-us/articles/4408822414490)
- [Creating ticket forms
  to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858)
- [Presenting ticket
  forms to end users](https://support.zendesk.com/hc/en-us/articles/4408842873498)

## Embedding a ticket form in your website

The embeddable Web Widget (Classic) includes a customizable HTML form
that lets end users submit tickets. You can embed Web Widget
(Classic) in any page of your website. Clicking the widget gives the
user the option of using a ticket form:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_enduser_leavemsgattatchment_selected.png)

Resources:

- [Using Web Widget
  (Classic) to embed customer service in your
  website](https://support.zendesk.com/hc/en-us/articles/4408836216218)
- [Adding Web Widget
  (Classic) to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242)
- [Advanced
  customization of your Web Widget
  (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562)
- [Contact form
  settings](https://developer.zendesk.com/embeddables/docs/widget/contact_form#settings) (Web Widget JavaScript API)

## Building a ticket form

For maximum flexibility, you can build your own HTML ticket form, host it
on your own server, and use the Zendesk API to submit the form data
to your Zendesk Support account.

Important: If your team prefers to create
a custom ticket form, it is not recommended to route requests from
the form through a support email address. This workflow is
unsupported and can result in emails becoming [suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408889141146). To
avoid this issue, [use the API](https://developer.zendesk.com/documentation/ticketing/managing-tickets/building-a-custom-ticket-form-with-the-zendesk-api/) to build
your ticket form or utilize the Web Widget. See [Tickets created from my
custom ticket form are suspended](https://support.zendesk.com/hc/en-us/articles/4408881830298).

Resources:

- [Building a custom
  ticket form with the Zendesk API](https://developer.zendesk.com/documentation/ticketing/managing-tickets/building-a-custom-ticket-form-with-the-zendesk-api)
- [Requests API
  reference](https://developer.zendesk.com/rest_api/docs/support/requests)
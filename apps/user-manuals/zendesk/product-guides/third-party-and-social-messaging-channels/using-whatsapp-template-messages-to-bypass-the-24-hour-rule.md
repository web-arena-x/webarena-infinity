# Using WhatsApp template messages to bypass the 24-hour rule

Source: https://support.zendesk.com/hc/en-us/articles/5869718332954-Using-WhatsApp-template-messages-to-bypass-the-24-hour-rule

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Social Messaging add-on |

Customers without Zendesk Suite must have Support and Chat with the Social Messaging add-on to use this feature.

If you want to bypass the 24-hour rule by WhatsApp, you can send WhatsApp template
messages to your end users, as long as they have already reached out to your business by
opening a ticket via WhatsApp.

Before you can set this up, you must have at least one phone number connected to the
WhatsApp Business API. If you haven't already done so, complete the process to [add WhatsApp channels to the Zendesk Agent workspace](https://support.zendesk.com/hc/en-us/articles/4408842821786).

This article covers the following topics:

- [About the 24-hour rule](#topic_gjr_mvw_wxb)
- [Creating and submitting WhatsApp
  template messages via the WhatsApp Business account UI](#topic_jfy_tvw_wxb)
- [Using shorthand syntax to send
  WhatsApp template messages](#topic_zkl_qyw_wxb)
- [Using Sunshine Conversations API
  to send WhatsApp template messages](#topic_dtq_w1x_wxb)
- [Troubleshooting WhatsApp
  templates](#topic_wmv_y1x_wxb)

## About the 24-hour rule

The starting point for the 24-hour window is when the end user sent the message from
WhatsApp. It’s not when the message was received by Support and the ticket was
created, for example. If you fail to reply within the 24-hour window, you can’t
reply to the end user until the end user sends another message, reopening the
24-hour window. The 24-hour period restarts every time the end user sends a message.

If you reply after 24 hours, the reply is still added to the ticket and appears in
the ticket interface, but the end user doesn’t actually receive the reply (meaning a
reply in WhatsApp or an email ticket notification). Error messages about the failure
appear in the upper-right portion of the agent interface and in the Events log.

Messages sent automatically through the auto-responder meet the criteria for
WhatsApp's 24-hour response times.

## Creating and submitting WhatsApp template messages via the WhatsApp business account UI

After you've connected your phone number to the WhatsApp Business API, you
can create and submit WhatsApp template messages within the WhatsApp Business
account UI. For more information about the process, see [Create message templates for your WhatsApp
Business account](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) in the Meta documentation.

If you submit a WhatsApp template message with a variable, parameter,
and/or media, you must submit the actual content as a sample, otherwise WhatsApp
will reject it.

The sample of a variable must be clear, general, and understood by all, for
example:

```
“Hi {{1}},
Welcome to the {{2}}, we wish you a great stay. If you need anything, feel free to reach out to {{3}} and they’ll be happy to assist you.
Have a great day,”
```

In this example, the variables are:

`{{1}}` The end user name

`{{2}}` The hotel name

`{{3}}` The team name

WhatsApp can take anywhere from one minute - five business days to provide
an update.

Important: Only Meta can approve or reject WhatsApp template
messages, Zendesk does not control this approval process.

## Using shorthand syntax to send WhatsApp template messages

Use shorthand syntax to bypass the 24-hour rule by WhatsApp when a WhatsApp end user
has reached out to your WhatsApp Business number and a ticket has been
created.

Note: You cannot use shorthand syntax to send proactive WhatsApp
templates to end users who have never reached out to your business. You need to
use the Sunshine Conversations [Notification API](https://docs.smooch.io/guide/outbound-messaging/#notification-api) for
this.

### Bypassing the WhatsApp 24 hour rule

If you can't reply to a message sent via WhatsApp within 24 hours, consider bypassing
the WhatsApp 24 hour rule so you can still reply later.

**To bypass the WhatsApp 24 hour rule**

1. An end user has messaged your business and opened a ticket.
2. Use Sunshine Conversations shorthand syntax (see [Sunshine conversations
   WhatsApp](https://docs.smooch.io/guide/whatsapp/#shorthand-syntax)).
3. After the WhatsApp template message is approved, create a [macro](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_zh2_4nw_4y) to send the
   WhatsApp template message to end users who have already opened a
   ticket.

   Here are two examples of how to create the content of the
   macro:

   ```
   &((namespace=[[namespace]] template=[[template]] fallback=[[text_fallback]] language=[[language]] body_text=[[param_1]]))&
   ```

   or

   ```
   &((
    namespace=[[namespace]]
    template=[[template]]
    fallback=[[fallback]]
    language=[[language]]
    body_text=[[param_1]]
   ))&
   ```

   - `namespace` - the unique ID for your WhatsApp
     Business account. You can find your namespace on the toolbar
     of your WhatsApp Business account by clicking
     **Namespace**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/WhatsApp_namespace.png)
   - `template` - enter a name for your
     template.
   - `language` - for the language code, see [Supported
     languages](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/supported-languages) in the Meta for developers
     documentation.
4. Thoroughly test the functionality of each WhatsApp template message
   macro, before deploying to production.

   Note: WhatsApp template message content is not reconstructed within
   the ticket after you have sent it (it appears only as shorthand
   syntax to the agent). However, your end users will see the
   content of the WhatsApp template message.

### Testing your macro functionality

**To test text without variables**

1. Create a [macro](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_zh2_4nw_4y).
2. Under **Actions**, paste the following example in the **Rich content
   field** and insert the relevant information for your namespace,
   template, fallback text, and
   language.

   ```
   &((namespace=[[namespace]] template=[[template]] fallback=[[text_fallback]] language=[[language]]))&
   ```

**To test text with variables**

1. Create a [macro](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_zh2_4nw_4y).
2. Under **Actions**, paste the following example in the **Rich content
   field** and insert the relevant information for your namespace,
   template, fallback text, language, and for example the ticket requester’s
   first
   name.

   ```
   &((namespace=[[namespace]] template=[[template]] fallback=[[text_fallback]] language=[[language]] body_text=[[ticket.requester.first_name]]))&
   ```

**To test text with variables and a media image**

1. Create a [macro](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_zh2_4nw_4y).
2. Under **Actions**, paste the following example in the **Rich content
   field** and insert the relevant information for your namespace,
   template, fallback text, language, and for example the URL location of the
   header
   image.

   ```
   &((namespace=[[namespace]] template=[[template]] fallback=[[text_fallback]] language=[[language]] header_image=[[image_location]] 
   body_text=[[param_1]] body_text=[[param_2]]))&
   ```

**To test text with variables, media, and buttons**

1. Create a [macro](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_zh2_4nw_4y).
2. Under **Actions**, paste the following example in the **Rich content
   field** and insert the relevant information for your namespace,
   template, fallback text, language, and for example the URL location of the
   header image, two different types of body text, the button index, and the
   URL location of the
   button.

   ```
   &((namespace=[[namespace]] template=[[two_variable_media_buttons]] fallback=[[text_fallback]] language=[[language]] 
   header_document=[[document_location]] body_text=[[param_1]] body_text=[[param_2]] button_index=[[1]] button_url=[[url]]))&
   ```

## Using Sunshine conversations API to send WhatsApp template messages

If the end user has not yet messaged your business, you can still send an outbound
message to them by using the Notifications API feature, see the [How to start conversations](https://docs.smooch.io/guide/whatsapp/#how-to-start-conversations) section of
Sunshine Conversations: WhatsApp. You or your Engineering team can do this by using
the Sunshine Conversations API.

## Troubleshooting WhatsApp templates

**WhatsApp rejected my WhatsApp template**

To find out why your template was rejected, click the template. Depending
on the reason for rejection, you can either edit the body, the variable, and the
media of your WhatsApp template message, or [appeal the decision](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=DK&destination=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fmessage-templates%2Fguidelines%2F%23appeals&event_type=click&last_nav_impression_id=0tDVHEoBbZkpJ8129&max_percent_page_viewed=93&max_viewport_height_px=842&max_viewport_width_px=1621&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fmessage-templates%2Fguidelines%2F&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dwhatsapp%26path2%3Dmessage-templates%26path3%3Dguidelines&region=emea&scrolled=true&session_id=1yMi3aXekKv0MHXPT&site=developers). However, if your
template keeps being rejected, you must create a new one with a new name and
content. For more information, see [Message template guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) in the Meta
for developers documentation.
# Setting up and using Google Analytics for the Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408825534234-Setting-up-and-using-Google-Analytics-for-the-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Google
Analytics](http://www.google.com/analytics/) is an analytics tool that helps you understand and analyze your web
traffic. The Web Widget (Classic) supports reporting of widget events and channel events
in Google Analytics. This provides insights into how your users are interacting with the
widget.

This article describes the events tracked in the widget, setting up event
reporting, and viewing event reports in Google Analytics.

This article includes the following topics:

- [Enabling Web Widget (Classic) event reporting for Google Analytics](#topic_fcm_jwk_nlb)
- [Viewing Web Widget (Classic) event data on Google Analytics](#topic_ikf_rwk_nlb)
- [Disabling Web Widget (Classic) event reporting for Google Analytics](#topic_hw5_qxk_nlb)
- [Reported widget events](#id_gbf_s1r_nlb)

Related information:

- [Analytics API setting](https://developer.zendesk.com/embeddables/docs/widget/settings#analytics)
- [Customizing Web Widget (Classic) events
  tracking to third-party analytics services](https://developer.zendesk.com/documentation/classic-web-widget-sdks/web-widget/getting-started/customizing-web-widget-events-tracking-to-third-party-analytics-services)
- [Adding the Web Widget (Classic) to your
  website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242)
- [Quickstart – Web Widget (Classic) JavaScript
  APIs](https://developer.zendesk.com/documentation/classic-web-widget-sdks/web-widget/quickstart-tutorials/web-widget-javascript-apis)

## Enabling Web Widget (Classic) event reporting for Google Analytics

By default, the Web Widget (Classic) detects if Google Analytics is present on your
web page. When the Google Analytics tag is on your web page, the widget
automatically starts reporting events to Google Analytics.

**To set up Google Analytics on your web page**

1. [Set up a web property](https://support.google.com/analytics/answer/1042508) in your
   Google Analytics account.
2. Paste the [analytics tag](https://support.google.com/analytics/answer/1008080) to each web page
   with the embedded widget.

## Viewing Web Widget (Classic) event data on Google Analytics

You can view and filter widget event data in your Google Analytics account.

**To access the event data on Google Analytics**

1. Sign in to your Google Analytics account.
2. On the left sidebar, select **Behavior** > **Events** >
   **Top Events**.
3. Under **Event Category**, select **Zendesk Web
   Widget**.

## Disabling Web Widget (Classic) event reporting for Google Analytics

The [analytics setting API](https://developer.zendesk.com/embeddables/docs/widget/settings#analytics) is used to disable
the automatic Web Widget (Classic) event tracking for Google Analytics.

**To disable widget event reporting for Google Analytics**

- To each webpage with the widget, add the analytics setting script set to
  “false”. Make sure it is before the [widget code snippet](https://support.zendesk.com/hc/en-us/articles/4408821673242) in the body
  element.

  ```
  <script type="text/javascript">
      window.zESettings = {
          analytics: false
      };
  </script>

  <!-- Start of your_subdomain Zendesk Widget script -->
  <script id="ze-snippet" src="https://static.zdassets.com/ekr/{YOUR_SNIPPET_KEY}">
  </script>
  <!-- End of Zendesk Widget script -->
  ```

## Reported widget events

An event is a description of an activity that has occurred. The following table
lists and describes the events reported in the Web Widget (Classic).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Widget channel** | **Category** | **Action** | **Event label** | **Description** |
| **General** | Zendesk Web Widget (Classic) | Web Widget (Classic) Opened |  | When the end user opens the widget |
|  | Zendesk Web Widget (Classic) | Web Widget (Classic) Minimised |  | When the end user minimises the widget |
| **Chat** | Zendesk Web Widget (Classic) | Chat Opened |  | When Chat is initiated |
|  | Zendesk Web Widget (Classic) | Chat Shown - same as Chat Opened |  | When Chat is initiated |
|  |  | Chat Served by Operator | Agent display name | When an operator joins an initiated chat |
|  | Zendesk Web Widget (Classic) | Chat Rating Bad |  | When the end user submits a bad rating post-chat |
|  | Zendesk Web Widget (Classic) | Chat Rating Good |  | When the end user submits a good rating post-chat |
|  | Zendesk Web Widget (Classic) | Chat Comment Submitted |  | When the end user submits a comment along with their rating |
|  | Zendesk Web Widget (Classic) | Chat Request Form Submitted | Department name | When the end user submits a chat request form |
|  | Zendesk Web Widget (Classic) | Chat Offline Message Sent |  | When the end user submits a chat message when the agent is offline |
| **Contact and ticket forms** | Zendesk Web Widget (Classic) | Contact Form Shown | If ticket forms are also enabled, the label includes  the ticket form ID and ticket form name | When the contact form is shown to the end user |
|  | Zendesk Web Widget (Classic) | Contact Form Submitted | Ticket form ID, ticket form name | When the end user submits the contact form |
| **Help center** | Zendesk Web Widget (Classic) | Help Center Shown |  | When the end user is presented with the help center |
|  | Zendesk Web Widget (Classic) | Help Center Search | Search term | When the end user searches the Help Center in the widget |
|  | Zendesk Web Widget (Classic) | Help Center Article Viewed | Article ID, article name | When the end user views a help center article link |
|  | Zendesk Web Widget (Classic) | Help Center View Original Article Clicked | Article ID, article name | When the end user views the help center article |
| **Voice** | Zendesk Web Widget (Classic) | Talk Shown | Talk contact option | When the end user is presented with call options |
|  | Zendesk Web Widget (Classic) | Talk Callback Request Submitted |  | When the end user submits a callback request |
| **Help Center** | Zendesk Web Widget (Classic) | Answer Bot Article Viewed | Article ID, article name | When the end user views an article from the list of suggested articles |
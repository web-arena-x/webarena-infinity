# Adding the Zendesk Chat widget to your website

Source: https://support.zendesk.com/hc/en-us/articles/4408881932698-Adding-the-Zendesk-Chat-widget-to-your-website

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Note: If you have both Zendesk Chat and Zendesk Support, this article doesn't apply to you.
Instead, you need to use the Web Widget to add Chat to your
website.
Follow the instructions in [Setting up Zendesk Chat in the Web
Widget
(Classic)](https://support.zendesk.com/hc/en-us/articles/4408825767962)
and [Configuring components in the Web
Widget
(Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258).

Before your visitors can start chatting with you, you’ll need to add the Chat
widget to your site by embedding the Chat widget script in the HTML source code of one or more
pages.

**To add the Chat widget to a web page**

1. From the dashboard, select **Settings** > **Widget**, then click the **Getting
   Started** tab.
2. Copy the embed script, as shown in the example
   below:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/embed_web_widget_script-chat.png)
3. In the source code of the web page, paste the embed script between the page's head
   tags.

   You can paste it either right after the opening <head> tag or right before
   the closing </head>.

   If you are concerned about page load performance, we recommend placing the snippet at the
   end of the <body> rather than the <head>. Even though the snippet script is
   very lightweight, it’s best to avoid inserting scripts that will block the browser from
   continuing to render a web page until that script has loaded. Just keep in mind that any
   scripts that use the Web Widget zE JavaScript API must be placed after the snippet
   script.
4. Save and publish the page.

The widget should be visible after reloading the page in a browser.
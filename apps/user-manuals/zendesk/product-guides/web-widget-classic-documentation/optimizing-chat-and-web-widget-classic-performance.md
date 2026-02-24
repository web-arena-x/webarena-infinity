# Optimizing Chat and Web Widget (Classic) performance

Source: https://support.zendesk.com/hc/en-us/articles/4408820305562-Optimizing-Chat-and-Web-Widget-Classic-performance

---

Note: This article is provided for instructional purposes only. Zendesk does not support or guarantee the code. Please post any issues you have in the comments section or try searching for a solution online.

You can use the [`connectOnPageLoad JavaScript API`](https://developer.zendesk.com/embeddables/docs/widget/settings#connectonpageload) to defer the Chat connection until your visitor interacts with the Web Widget.

Using this setting, you can fine-tune your website for performance, while still leveraging all features on specific pages.

This article includes the following topics:

- [Understanding the Web Widget-Chat connection](#topic_lhq_2xt_vjb)
- [Understanding the connectOnPageLoad setting's impact](#topic_iwk_2xt_vjb)
- [Adding connectOnPageLoad to your web pages](#topic_p3d_2xt_vjb)

Related articles:

- [ConnectOnPageLoad: Configuration best practices for common Chat use cases](https://support.zendesk.com/hc/en-us/articles/4408893434778)
- [Developer documentation: ConnectOnPageLoad setting](https://developer.zendesk.com/embeddables/docs/widget/settings#connectonpageload)

## Understanding the Chat-Web Widget (Classic) connection

By default, Web Widget (Classic) connects to live chat services on page load, for any page where the widget snippet is embedded AND Chat is enabled.

The timing of this connection makes features like proactive chat and conversion tracking possible. However, it can negatively affect performance in a number of ways:

- If you have high visitor traffic volume, these connections can reduce the performance of your chat product, and make it more difficult to identify customers when [monitoring your website visitors](https://support.zendesk.com/hc/en-us/articles/4408821265178#topic_ttb_b4d_4fb).
- It impacts Web Widget (Classic) performance. Connecting to live chat on page load means that more assets need to be delivered, before the Web Widget (Classic) is interactive on a web page. This can impact your overall web page load speed.

## Understanding the connectOnPageLoad setting's impact

When you enable the `connectOnPageLoad` setting, there should be no noticeable impact on the end user experience. There may be a slight delay of one to two seconds (at the most) when a customer opens the widget.

However, using `connectOnPageLoad` to defer the connection comes with some important trade-offs to consider, before implementation.

**When `connectOnPageLoad = true`:**

- There is no impact on live chat functionality. The live chat experience is the same as if there is no `connectOnPageLoad` setting in the page code.

**When `connectOnPageLoad = false`:**

- You will only be able to [monitor visitors](https://support.zendesk.com/hc/en-us/articles/4408821265178#topic_ttb_b4d_4fb) who have initiated chat or have clicked on the Web Widget (Classic).
- Some of the live chat features may be impacted, such as conversion tracking, proactive triggers, and Web Widget (Classic) JS APIs which rely on visitors' connections with Chat services.

To learn more about the impact of using `connectOnPageLoad` in different configuration scenarios, see [ConnectOnPageLoad: Configuration best practices for common Chat use cases](https://support.zendesk.com/hc/en-us/articles/4408893434778).

## Adding connectOnPageLoad to your web pages

You can add `connectOnPageLoad` to any page with the embedded Web Widget (Classic). The setting is added to the source code on each web page, as in the following example:

```
<script type="text/javascript">
 window.zESettings = {
     webWidget: {
        chat: {
            connectOnPageLoad: false        
        }
    }
 };
</script>
```

The setting must be assigned a value, either true or false, which determines how visitors are handled on each page:

- `connectOnPageLoad: true`: Connects to the Chat service when the page loads, allowing you to engage with every visitor on that web page.
- `connectOnPageLoad: false:` Connects to the Chat service when a user interacts with the widget, allowing you to focus on visitors currently chatting with agents, or who have initiated a chat.

To learn more about the impact of using `connectOnPageLoad`, see [ConnectOnPageLoad: Configuration best practices for common Chat use cases](https://support.zendesk.com/hc/en-us/articles/4408893434778).

**To include the `connectOnPageLoad` setting on your website**

1. In the source code of the web page, locate the Chat widget code snippet.
2. Add the [`connectOnPageLoad` setting](https://developer.zendesk.com/embeddables/docs/widget/settings#connectonpageload) to your source code, above the Web Widget (Classic) code snippet:

   ```
   <script type="text/javascript">
    window.zESettings = {
       webWidget: {
           chat: {
               connectOnPageLoad: false
           }
       }
    };
   </script>
   ```
3. Set the value of `connectOnPageLoad` as `true` or `false` depending on your use case.
4. Save and publish the page.
5. Repeat these steps on every page of your website with the widget embedded.
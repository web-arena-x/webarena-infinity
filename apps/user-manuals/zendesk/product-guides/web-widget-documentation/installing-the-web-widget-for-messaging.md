# Installing the Web Widget for messaging

Source: https://support.zendesk.com/hc/en-us/articles/4500748175258-Installing-the-Web-Widget-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Note: This article applies to accounts using the Web Widget for messaging. If you're using Web Widget (Classic), see [Configuring the components in your Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258).

When you've finished configuring your Web Widget, you can install it on your website or help center and make it available to your customers. Alternatively, you can embed the Web Widget if you want control over exactly where and how it appears.

This article includes the following topics:

- [Installing the Web Widget on a website](#topic_fqh_qtc_3rb)
- [Installing the Web Widget on a help center](#topic_oqh_zbd_btb)
- [Embedding the Web Widget](#topic_bd3_gfn_phc)

## Installing the Web Widget on a website

Installing the Web Widget on a website requires some basic familiarity with your website's code, as you need to paste the code snippet before the closing HTML
</body> tag.

The following video gives you an overview of how to add messaging to your website:

Adding messaging to your website [1:40]

Tip: You can further control where the Web Widget appears by creating an allowlist. See [Using an allowlist to control where the Web Widget appears](https://support.zendesk.com/hc/en-us/articles/10212540848538).

**To add the Web Widget to your website**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the widget you want to install.
3. Scroll down, then click **Installation** to expand it.
4. Click the **Copy** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/code_snippet_copy_icon_SDK.png)) at the bottom of the code snippet frame.
5. In the source code of the web page where you want to add the widget, paste the code snippet before the closing HTML </body> tag. Add the code to every web page where you want the widget to appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/install_ww_website.png)
6. If you want to send the code to someone else (a developer, for example), click **Email code to a team member**.
7. Make sure your firewall is configured to allow the Web Widget to appear.

## Installing the Web Widget on a help center

Installing the widget on a help center is a simple, one-click process – no tech support needed. You must have [created and activated your help center](https://support.zendesk.com/hc/en-us/articles/5702269234330) to install Web Widget.

**To add the Web Widget to your help center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the widget you want to install.
3. Scroll down, then click **Installation** to expand it.
4. Click the checkbox to **Automatically embed Web Widget in your Help Center**.

   You will not see this option if you have not [created and activated your help center](https://support.zendesk.com/hc/en-us/articles/5702269234330).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/install_ww_hc.png)
5. Click **Save**.

   The Web Widget is added to every page of your help center.

## Embedding the Web Widget

Embedded mode places the Web Widget inside a specific HTML container on your page, rather than displaying it as a floating overlay with a fixed position. The widget automatically fills the dimensions of your chosen container, giving you control over exactly where and how it appears. For example, this is useful for advanced layouts like split views with conversation lists and messages side-by-side.

Embedded mode requires you to use a [JavaScript embed API call](https://developer.zendesk.com/api-reference/widget-messaging/web/core/#embedded-mode) to specify both the mode and the target container for the widget.

To use embedded mode, start by disabling the widget's default auto-render behavior:

```
window.zEMessenger = {
 autorender: false
}
```

Then, tell the widget where to appear by specifying a container's ID or class:

```
zE('messenger', 'render', {
 mode: 'embedded',
 widget: {
    targetElement: '#messaging-container'
 }
});
```

The Web Widget now displays inside the `#messaging-container` element and takes on the size and position defined by your CSS.

For more information, see [Web Widget embedded mode](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/web/embedded-mode/) in our developer documentation. To view more examples, see [Embedded mode for the Zendesk Widget](https://internalnote.com/embeddable-zendesk-widget/#embedded-the-widget-in-some-actual-websites).
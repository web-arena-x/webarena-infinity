# Customizing the Zendesk Chat widget with advanced AI agents (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357750787098-Customizing-the-Zendesk-Chat-widget-with-advanced-AI-agents-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended. Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

Zendesk Chat widget can be customized to meet different requirements, such as [hiding your department dropdown menu](https://support.zendesk.com/hc/en-us/articles/8357750793370). In this article, we share our experiences of other use cases that might be helpful for you as well.

The use cases covered in this article are:

- [Use case 1: Hide widget when agents are offline](#h_01F67AZE0D665XH49RNB7DKYJ3)
- [Use case 2: Routing users based on URL](#h_01F67AZE0D665XH49RNB7DKYJ3)

The widget customizing script snippets should always be added to right below the Zendesk Chat widget snippet on your website or in help center.

If you're not sure where the widget is on your website, please contact your website developer. For help center, read about [locating Zendesk Chat widget in help center (Zendesk Guide).](https://support.zendesk.com/hc/en-us/articles/8357750793370#h_01F673DD1EBWCK8CYZP32TBP8S)

## Use case 1: Hide widget when agents are offline

### Widget behavior

- When widget is on --> Route chats to AI agent department first
- When agents are offline --> Hide widget

```
<script>

     window.zESettings = {
      webWidget: {
       chat: {
         departments: {
             select:'BOT_DEPARTMENT',
             enabled: ['']
          }
       }
    }
};

zE('webWidget:on', 'chat:connected', function() {
var ChatDepartment = zE('webWidget:get', 'chat:department', 'SUPPORTDEPARTMENT');
if (ChatDepartment.status == "online") {
zE('webWidget', 'show');
} else {
zE('webWidget', 'hide');
}
});

</script>
```

## 

## Use case 2: Routing users based on URL

This script snippet is suitable if you want to route users to different AI agents or departments based on their locale. For example, German users routed to DE AI agent and French users to FR AI agent.

You'll need to set up two things in Zendesk for this to work:

1. Turn pre-chat form off
2. Set a trigger like the example below in Zendesk Chat > Settings > Triggers.

![routing_zd_trigger_setup.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_routing_zd_trigger_setup.png)

### Widget behavior

- Doesn't show pre-chat form after user clicks on the widget
- Re-authenticates to make sure the URL reflects user locale

```
<script type="text/javascript">
zE('webWidget', 'chat:reauthenticate');
</script>
```

If you are interesting in knowing and doing more, Zendesk has two great articles:

- [Configuring components in the Web Widget](https://support.zendesk.com/hc/en-us/articles/115009692388-Configuring-components-in-the-Web-Widget)
- [Advanced customization of the Web Widget](https://support.zendesk.com/hc/en-us/articles/229167008)
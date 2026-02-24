# Hiding the department dropdown for advanced AI agents with Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357750793370-Hiding-the-department-dropdown-for-advanced-AI-agents-with-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

In Web Widget (Classic), you can hide the department dropdown menu. This
article walks you through the steps to do so and provides the necessary script
snippet.

This article contains the following topics:

- [About hiding departments](#h_01F66ZWY4QRCYWP2DKAK2M24A0)
- [Hiding the department dropdown menu](#h_01F66ZX58C9PR733B6DXJ2ZZYP)

Related articles:

- [Configuring components in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/115009692388-Configuring-components-in-the-Web-Widget)
- [Advanced customization of Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/229167008)

## About hiding departments

Hiding the departments means end users don't see the dropdown menu in the
pre-chat form. This prevents them from selecting between an AI agent or human
department.

The screenshots below show what it looks like with and without the department
dropdown.

|  |  |
| --- | --- |
| **With department dropdown:** | **Without department dropdown:** |
| Chat widget | Chat widget 2 |

## Hiding the department dropdown menu

You can hide the department dropdown menu by performing the following tasks:

1. [Editing the snippet](#h_01F66ZPA90JW09RQTT4N15QAVE)
2. [Adding the snippet to your website or help center](#h_01F66ZQ8FYKGT734GC2AT0410Y)

### Editing the snippet

Edit the Web Widget (Classic) snippet below by replacing BOT\_DEPARTMENT and HUMAN\_DEPARTMENT with the names of your departments or groups in Zendesk Chat or Support.

When the AI agent is online, the AI agent department will be selected. When the AI agent is offline, the human department will be selected.

```
<script>  
zE('webWidget:on', 'chat:departmentStatus', function(dept) {  
 if (dept.name === 'BOT_DEPARTMENT' && dept.status === 'online') {  
  zE('webWidget', 'updateSettings', {  
   webWidget: {  
    chat: {  
     departments: {  
      enabled: [''],  
       select: 'BOT_DEPARTMENT'  
                  },  
                }  
              }  
            });  
} else if (dept.name === 'BOT_DEPARTMENT' && dept.status !== 'online') {  
 zE('webWidget', 'updateSettings', {  
  webWidget: {  
   chat: {  
    departments: {  
     enabled: [''],  
      select: 'HUMAN_DEPARTMENT'  
                 },  
                }  
              }  
           });  
}  
});  
</script>
```

### Adding the snippet to your website or help center

Note: This section assumes you've already
[added Web Widget (Classic) to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242).

Insert the snippet immediately below the Web Widget (Classic) snippet in your website or help center:

- **Website**: If you're not sure where the Web Widget (Classic) snippet is, contact your website developer.
- **Help center**: The Web Widget (Classic) snippet is located in the **Document head** (document\_head.hbs) template. For help, see [Customizing page templates and custom pages with HTML and Curlybars](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_h5c_k4w_n3).
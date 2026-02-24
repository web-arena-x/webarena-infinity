# About message restrictions in advanced AI agents with Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357757844122-About-message-restrictions-in-advanced-AI-agents-with-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

Due to the limitation of the Zendesk Chat widget, there are three things to pay attention to when building dialogues if your AI agent will be using Zendesk Chat.

1. **Message**
   - Any message in a block must be less than 1000 characters
2. **Link Block**
   - Max 3 "Link clicked" on the same level 
     ![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_i7iOe.png)
3. **Buttons**
   - Button text must be less than 20 characters
   - Max 10 buttons on the same level
   - Buttons are NOT supported on Zendesk Chat mobile SDK. Further information is available [here](https://support.zendesk.com/hc/en-us/articles/360022184394-Using-structured-messages-in-Zendesk-Chat).
   - Buttons and Link Blocks cannot be on the same level

![mceclip1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip1_gv66d.png)
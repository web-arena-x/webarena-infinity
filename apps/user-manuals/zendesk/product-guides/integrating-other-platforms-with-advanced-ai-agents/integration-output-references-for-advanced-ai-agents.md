# Integration output references for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749798682-Integration-output-references-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The following areas should be considered when designing an integration to drive an intent workflow. Here you will find output references for:

- [Chat](#h_01HCJ2VZNFHQWD2D8J9M0V34NZ)
- [Ticket & Email](#h_01HCJ2VZNF4W4CKK86B8CB8MS2)
- [Cards & Carousels](#h_01HCJ2VZNFN3K6BMMT6ZN8X6X8)

## CHAT TEXT

All CRMs can send one or more messages in a row which you can populate with dynamic data. You can output information directly using shorthand {{paramName}} to render the value in an AI agent message, or use the parameter name to customize AI agent messages based on the individual possible param values using [Conditional Blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234-Conditional-Blocks-Explained).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_fzZ2CMU99zQdfdzs9B7OlKL556sYY_OZoyoA13gBkbRa3okRefvh4X7SftALth5wxNXwSSYhT_FkOE9ZSs9uI4b_OB2Bly4stNP67hQl0sp8mdY9jlCeofbnNpJQ-fusTRKWwFQTYiaognd0cMV5q94.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_71Dmouk9aYmBPfuL0g-otoJaaz04ZyyQDsd5CI3FPg3T7SgcDRRpw7aNdaPzkmHW6m_xxXWngyxYy2_DBVwtbS78F2XiDn71W_xEWzR9uViFSKPum93ICis6zM558_6Kx9GoFJhjlsSweMrwIVSW488.png)

## TICKET & EMAIL TEXT

Ticket and email AI agents can send one singular message in reply to a recognized intent. Therefore it’s usually better to send too much (relevant) information rather than too little.

Structuring messages for multiple results can be tricky if you’re only able to send one message though - try to use Conditional Blocks to segment out different response bodies as much as possible.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_5rF5P5fTgswXPNawARladHntUjf22FU6Fnexglzr6TA8KGFMpC2n8mGNSHd2BRwqlINB1HIitxNnOP6fGRvcw3N7W5rPTig77S3yMxgos_modOJTIxBVKzMNEYZhqeOHpJyR2cK9vaj_iFOtWF9BmB8.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_meC_oCsiojQXilwEpobSFx_VQvJBTI86pq1OYyxegSEEnToe4NjMg8F6qnko8hyw7fC0h5JocFNZaFVBAZV8V4xh1_vr7_k67Vgd5xKCgxVkVYyg63RLagYoNXucfvw11UmnyYMMjzV9BDlcx4xIzDs.png)

## CARDS & CAROUSELS

Dynamic Cards & Carousels can be populated with incoming API data. They’re a great option if you want to display multiple options at once, e.g. if a customer has multiple shipments in a single order. Once the end-user clicks on a card of their choice, information that only pertains to that specific item will be released to the dialogue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_ml5zBEYOxVSaCS9qpgu-x6A8Yrr08V7-yw2R8w7_jz4UApssv04saQXwPBWFAtT3kfppdCJs_sZL3VhzqxSKrbHIlK-0cjxXy8STroSnmRTDHK_FFbMaUaOwIFHKCMOwROsVHCoE1NMlFnaUz_EczMM.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_c-1jz3B-Mz-9UMSdKlwKnqSdHkrNqyv6JLuKZxIhQCTH1iRoEdt73D8YhNR_13TtfEQYEK9Sr-w_MG5Tb-Qhm1740WLv4VOBvqanaTrTVMxdEVoNIw30dBX_YrBcqVJkJpiicoHzQFuePW_ZozlpZR8.png)

Specifically for Cards & Carousels, consider carefully how you want to populate the following fields. All of them can be dynamic API content, static text / URLs or a combination of both.  
  
Card data: Image URL, Card Title, and Description.

Card button: Button Text.

Dialogue: Any additional parameters you want to release to the rest of the dialogue to customize the resulting flow, e.g. tracking link, shipping country, days since last update etc.

Please keep in mind that your CRM restricts what can and should be displayed - keep an eye on the limitations [here](https://support.zendesk.com/hc/en-us/articles/8357749513370-Carousels).

Generally, none of the fields should come back with API data of null, undefined or empty. Consider adding a fallback value if you think that might be the case for certain edge cases.
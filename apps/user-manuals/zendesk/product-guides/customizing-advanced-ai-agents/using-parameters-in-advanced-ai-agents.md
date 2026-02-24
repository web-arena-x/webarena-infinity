# Using parameters in advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9522180655386-Using-parameters-in-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In AI agents - Advanced, parameters are pieces of information you can collect and use to tailor your AI agent workflows. Specifically, you can leverage parameters in [conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234), [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530), and [API integrations](https://support.zendesk.com/hc/en-us/articles/8920235767834).

This article contains the following topics:

- [Available parameters](#topic_cth_4xp_xfc)
- [Available operators](#topic_jbc_qxp_xfc)

## Available parameters

Parameters can come from three sources:

- [CRM platform parameters](#topic_ofp_hzp_xfc)
- [Session data parameters](#topic_lf5_pzp_xfc)
- [Backend integration parameters](#topic_yc5_ybq_xfc)

### CRM platform parameters

CRM platforms typically store customer information such as name and email address. This information can be fetched from your CRM platform and saved to use in conditional blocks.

To fetch information from your CRM platform, [add an action](https://support.zendesk.com/hc/en-us/articles/8357756651290) associated with the “Conversation started” [event](https://support.zendesk.com/hc/en-us/articles/8357749555610) to collect the data from your CRM when a conversation begins. The information will be collected for every new conversation and applied to all dialogues within your AI agent.

### Session data parameters

Session data refers to information customers provide during a messaging session with the AI agent. [Add a block-level action](https://support.zendesk.com/hc/en-us/articles/8357756651290) to a dialogue flow to fetch session data and save it as a parameter value.

These session parameters are collected by default:

| Parameter | Use case example |
| --- | --- |
| {{lastDetectedLanguage}} | Provide the unsupported language system reply in the user’s language. |
| {{active\_language}} | Create language-specific replies.   You must use the language’s ID, not its name, as the parameter value. You can find the ID by going to **Settings** > **AI agent settings** > **Languages** and selecting a language. |
| {{chatTranscript}} | Attach the conversation transcript to a ticket for escalation via email. |
| {{lastVisitorMessage}} | Repeat the customer’s words, often in a default reply, such as: “I’m afraid I don’t know anything about {{lastVisitorMessage}} yet.” |
| {{integrationId}} | Route incoming messages to relevant AI agents with routing rules based on the source (`integrationId`) of the incoming message.   [View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conditional_blocks_integrationId.png) |
| {{confidence\_score}} | Base the reply on the intent recognition confidence threshold. `Confidence_score` is rounded up or down to whole numbers (integers).   [View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conditional_blocks_confidence_score.png) |
| {{lastResolution}} | Set a different dialogue flow based on the last custom resolution state: `Undefined`, `Informed`, `Resolved`, `Not Resolved`, `Escalated To Agent`, or `Escalated via Email`, and send to your CRM as a tag upon escalation. |

When creating your own session parameters with an action, don’t use the same name as one of these system parameters. It will cause an error and the data won't be retrieved.

[Entities](https://support.zendesk.com/hc/en-us/articles/8357749740698) are also considered session data parameters. The name of the entity is the name of the parameter. Any information captured via entities is stored as session data until two hours after conversation inactivity.

### Backend integration parameters

The AI agent can also fetch information from a [custom API integration](https://support.zendesk.com/hc/en-us/articles/8357756844442) to create personalized dialogue flows.

## Available operators

The table below lists the available operators, which each fall into one of the following types:

- **String**: Word
- **Boolean**: True or false
- **Array/list**: Comma-separated list
- **Integer**: Whole number
- **Float**: Decimal number

| Operator | Use for | Example | Expected parameter type | Condition value type |
| --- | --- | --- | --- | --- |
| `is / Is not` | Single values | `country` `is` `Germany` | string | string |
| `Is (boolean)` | True or false statements | `loggedIn` `Is` `True` | boolean | boolean |
| `Is (number)` | Single values | `timeout is 30` | integer | integer |
| `Is in / Is not in` | An OR condition with multiple values separated by a comma | `country` `In` `Germany, Japan, Finland` | string | array |
| `Array includes item / Array does not include item` | Checking for a particular value within a list of values stored as an array in the session | `tags_Array` `Array` `Includes item` `VIP` | array | string |
| `Text includes / Text does not include` | Checking for a substring, like a country code in a URL, based on text-based data in the session | `URL text` `Includes` `fr` | string | string |
| `Is present / Is not present` | Checking if a parameter is present in the session, without a specific value | `email` `Exists` `country: ''` , `null`, or completely undefined | any | N/A |
| `Starts with / Does not start with` | Single string values | `country` `Starts with` `united` | string | string |
| `Greater than` `Greater than or equal` `Less than` `Less than or equal` | All number types (integers and floats), with content recognition and actions, including whether the value - Exceeds a set value - Exceeds or is equal to a set value - Is less than a set value - Is less than or equal to a set value | `Number` `Greater than or equal` `9` | integer or float | integer or float |
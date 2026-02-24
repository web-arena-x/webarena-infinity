# Creating custom action flow triggers

Source: https://support.zendesk.com/hc/en-us/articles/9712284817818-Creating-custom-action-flow-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

An [action flow](https://support.zendesk.com/hc/en-us/articles/8855513857306) is a user-defined automated workflow. Each action flow consists of an action flow trigger, which initiates the flow, and one or more actions.

You can use [pre-defined action flow triggers](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_zg5_sx3_t2c), or admins can define custom action flow triggers. This article describes how to create a custom action flow trigger to listen for an HTTP request from a specific external system.

After creating an action flow trigger, you can use it in any action flow. See [Creating action flows](https://support.zendesk.com/hc/en-us/articles/8855601898266).

Note: Custom action flow triggers support up to 100 incoming API requests per minute.

## Creating a custom action flow trigger

Action flow triggers are created and managed within the action builder.

**Creating a custom action flow trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Click **+ Add trigger**.
4. In the step sidebar, under **Custom triggers**, click **Create trigger**.
5. Enter a unique and identifiable **Name** for the action flow trigger.

   Maximum length is 255 characters.
6. (Optional) Enter a **Sample payload** of the HTTP request you expect the trigger to receive.

   This should be a POST request with a valid JSON body.
   The payload can't exceed 200KB.

   The sample payload must include all of the properties, with the appropriate data type, you want to use later in an action flow that begins with this trigger.
7. Click **Next**.
8. If you provide a sample payload, map the data by clicking **Add** next each key-value pair you intend to capture as outputs in your action flow, and then clicking **Next**.

   If necessary, you can use the options menu to edit the name and type of a key-value pair or remove it from the trigger. The output names must be unique within the trigger and can't exceed 255 characters.

   The following data types are supported as outputs from custom triggers:
   - Text
   - Number
   - Decimal
   - True/false
   - Date (`YYYY-MM-DD`)
   - Date and time (`YYYY-MM-DDTHH:MM:SS[.sss]Z` or `YYYY-MM-DDTHH:MM:SS[.sss]+/-hh:mm`)
   - Arrays and objects are converted to strings.
9. Use the custom **Webhook URL** that is generated for the trigger to configure a webhook in an external system that will send requests to the custom trigger to initiate an action flow.

   Additionally, if you have the option, configure the external system's retry strategy to use exponential backoff with jitter for three retries at 20 seconds, 120 seconds, and 300 seconds after a rate-limited request.

   Note:
   - Treat the custom action flow trigger's webhook URL as a secret and do not share it.
   - Your account's [IP restrictions](https://support.zendesk.com/hc/en-us/articles/4408894156186) are enforced for the webhook URL.
10. Add the custom action flow trigger to an action flow. See [Creating action flows](https://support.zendesk.com/hc/en-us/articles/8855601898266).

## Using outputs from custom action flow triggers

All data you want to output from the action flow trigger must be assigned the proper data type. This is set automatically based on your sample payload, but you can modify it as needed. If the data received differs from the expected payload, the action flow will attempt to convert the data using the following rules:

- **Text outputs**:
 - Any number, decimal, true/false, date, or datetime value is converted to text.
 - If the key is missing from the request body, it is represented as null.
- **Number outputs**:
 - Decimal values are rounded to the nearest whole number, with .5 values rounding up.
 - For true/false values, true is converted to *1* and false to *0*.
 - A string representing a number is converted to a number.
 - A string representing a decimal is rounded to the nearest whole number, with .5 values rounding up.
 - All other strings are converted to nil.
 - If the key is missing from the request body, it is represented as nil.
- **Decimal outputs**:
 - Number values are passed through without modification.
 - For true/false values, true is converted to *1* and false to *0*.
 - A string representing a number is converted to a decimal.
 - A string representing a decimal is converted to a decimal.
 - All other strings are converted to nil.
 - If the key is missing from the request body, it is represented as nil.
- **True/false outputs**:
 - Null values are converted to *false*.
 - Number and decimal values of zero (0, -0, 0.0, -0.0) are converted to *false*.
 - Empty strings ("", "''", and "``") are converted to *false*.
 - All other number, decimal, string, date, and datetime values are converted to *true*.
 - If the key is missing from the request body, it is represented as nil.
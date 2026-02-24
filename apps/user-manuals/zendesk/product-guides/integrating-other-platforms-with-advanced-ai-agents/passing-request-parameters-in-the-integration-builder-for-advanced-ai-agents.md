# Passing request parameters in the integration builder for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8920235767834-Passing-request-parameters-in-the-integration-builder-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

When using the integration builder, you can pass request parameters of types such as string, number, boolean, and array in the API request body. This functionality enables greater flexibility in API integrations and supports a wider range of use cases. In this article, we’ll guide you through the process of configuring these parameters.

This article contains the following topics:

- [Setting the parameter type in request parameters](#h_01JMFSFD7HTNAJSAQQBZ32J530)
- [Add reformatting for array parameters](#h_01JMFSNQFER294SX67CRCYDVV2)
- [Using parameters in the API call request body](#h_01JMFSFD7HYFD25W9231DYC5BP)
- [Testing your configuration](#h_01JMFSFD7H1M3HP51E4Q3M5KR1)

Related articles:

- [Integration builder resources](https://support.zendesk.com/hc/en-us/articles/8498753675290)

## Setting the parameter type in request parameters

**To set the parameter type in request parameters**

1. Navigate to the **Request Parameters** section in the integration builder.
2. Define your parameter and set its type as one of the following:  
   - **String**: For textual data enclosed in quotes (for example, "example text").
   - **Number**: For numerical values (for example, 123).
   - **Boolean**: For true/false values.
   - **Array**: For a collection of values (for example, ["item1", "item2"]).  
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_pass_params_1.png)

## Add reformatting for array parameters

For testing purposes in the integration builder with parameters of type array, you must add a reformatting function to ensure proper handling of the data type. To do so, use the following function:

$eval($)

This function parses the string value into an array object.

If the parameter is already an array object, the function will not alter its behavior.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_pass_params_2.png)

For more information, see [Reformatting values in request parameters for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8560203369242).

## Using parameters in the API call request body

In the API call request body, these parameters can be used in the same format as string parameters, using the syntax: {{<REQUEST\_PARAMETER>}}

While the parameter may visually appear as a string in the body—as you can see in the screenshot below—during execution it will transform into the corresponding data type specified in the Request Parameters section.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_pass_params_3.png)

## Testing your configuration

Use the Test Production button in the integration builder to execute your API call.

Verify that the parameters are being passed with the correct types (string, number, boolean, array) in the request.

Review the response to ensure proper handling by the API.

Note: Successful transformations depend on correctly setting up parameter types and reformatting functions. Misconfiguration may lead to errors in API calls.
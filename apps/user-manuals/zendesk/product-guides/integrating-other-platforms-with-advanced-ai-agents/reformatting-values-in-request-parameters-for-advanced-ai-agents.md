# Reformatting values in request parameters for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8560203369242-Reformatting-values-in-request-parameters-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In the [integration builder](https://support.zendesk.com/hc/en-us/articles/8357756844442), request parameters allow you to pull data (conversation parameters) from AI agent conversations and pass it to external endpoints. In some cases, you may need to transform or reformat this data before sending it in an API request as either a URL query or in the request body. To do this, you can use JSONata, a powerful query and transformation language.

This article contains the following topics:

- [Reformatting the value of a request parameter](#h_01JFB2S65WMQX70ZV1EZYNPQN1)
- [Common use case examples for reformatting values](#h_01JFB2SHX43ED9QVH5MVFD6441)

Related articles:

- [Integration builder resources](https://support.zendesk.com/hc/en-us/articles/8498753675290)

## Reformatting the value of a request parameter

You can reformat a request parameter’s value using JSONata.

**To reformat the value of a request parameter**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select your AI agent.
2. In the main menu on the left, click **API integrations**.
3. Select or create an integration.
4. On the **Request parameters** page, select or create the request parameter you want to reformat the value for.
5. In the **Test value** field, select the **Reformat value** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformat_value_icon.png)). 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformatting_values_1.png)
6. In the **Reformat value** dialog, in the **Reformatting JSONata** field, use JSONata to transform or reformat the value associated with the selected request parameter key. 
   In your JSONata query, use **'$'** to represent the key whose value you’re reformatting. 
   The **Test value preview** field gives you a way to check the results of your query in real time. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformatting_values_2.png)
7. Click **Done**.
8. (Optional) If you’re adding the request parameter to the body of an API request:
   1. Under the **Environment header** on the left, select the appropriate environment.
   2. Select the **Body** tab.
   3. Add your JSON object, using the request parameter as a value in double curly brackets. 
      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformatting_values_3.png)

## Common use cases for reformatting values

Within the integration builder, you can define request parameters by assigning them to specific keys. While these values may work as is, there are scenarios where they need to be transformed or reformatted to match the requirements of the external system.

For example, you might want to:

- **Reformat dates**: Change the format of a date from MM/DD/YYYY to YYYY-MM-DD or ISO 8601 to match API requirements.
- **Perform string operations**: Manipulate strings, such as adding or removing characters, combining multiple fields, or transforming strings to contain HTML.
- **Apply conditional logic**: Apply conditions, such as checking whether a field is empty or assigning a default value if needed.

This section contains the following examples:

- [Scenario: Reformatting dates](#h_01JFB4304S6T2GAD4NXXRJHNP4)
- [Scenario: Reformatting URLs to make links clickable](#h_01JFB45K9TSRJC0G8S6MD157AD)
- [Scenario: Reformatting a chat transcript to make it more readable](#h_01JFB43M0FJW3RQG80KDDSVRSN)

### Scenario: Reformatting dates

In this scenario, your endpoint needs to check a date formatted as YYYY-MM-DD or in an ISO 8601 format. However, for your conversation, you want dates displayed in a more user-friendly format of DD/MM/YYYY.

Here’s the JSONata query you would use in this scenario:

```
$substring($, 6, 10) & "-" & $substring($, 3, 2) & "-" & $substring($, 0, 2)
```

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformatting_values_4.png)

### Scenario: Reformatting URLs to make links clickable

In this scenario, you want to convert URLs into clickable links by searching for text (a substring) that starts with http:// or https:// followed by a number of non-whitespace characters. You then want to replace that substring using the JSONata $replace function, with a string that wraps the matched URL in an HTML <a> tag, creating a clickable link.

Here’s the JSONata query you would use in this scenario:

```
( 
$text := "Chat transcript unavailable. Here is a link:https://www.zendesk.com. Here is another link: https://www.w3schools.com."; 
 
$replace($text, /(https?:\/\/[^\s]+)/, '<a href="$1">$1</a>' 
)
```

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformatting_values_5.png)

### Scenario: Reformatting a chat transcript to make it more readable

In this scenario, you want to add a chat transcript to a ticket. However, in its default form, the chat transcript is not very readable:

- Chat Transcript - 2024-10-12 (13:04:10) AI agent: Welcome to the customer engineering AI agent! (13:04:10) AI agent: Choose which integration to test: (13:04:10) Visitor: test c.id: d501304d-da09-4485-a4c7-1c708ec0005d All times in UTC

You want to transform it into a more user-friendly format by breaking each message onto a new line. Because each new message starts with an open parenthesis ( ( ) , you can use JSONata to replace each occurrence of ( with a line break followed by the (.

The reformatted conversation would then look like this:

- Chat Transcript - 2024-10-12 (13:04:10) AI agent: Welcome to the Integration Builder AI agent!
 (13:04:10) AI agent: Choose which integration to test: 
 (13:04:10) Visitor: test c.id: d501304d-da09-4485-a4c7-1c708ec0005d All times in UTC

Here’s the JSONata query you would use in this scenario:

```
$replace($, “(“, “\n(“)
```

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_reformatting_values_6.png)

Additionally, you’d need to add this parameter to the the body section in your environment so that it’s sent with the request:

```
{ 
"chatTranscript": "{{chatTranscript}}" 
}
```
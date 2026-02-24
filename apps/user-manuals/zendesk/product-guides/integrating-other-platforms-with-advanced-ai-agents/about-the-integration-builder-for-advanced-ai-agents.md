# About the integration builder for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756844442-About-the-integration-builder-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The integration builder is a powerful no-code tool that enables you to connect your AI agent to any API or data source without extended technical or programming skills. Personalize your chat experiences and drive higher automated resolutions with dynamic content.

Imagine an AI agent that can seamlessly access customer information from your back office system, retrieve data from any other external data source, or interact with third-party applications, all without requiring you to write a single line of code.

With dynamic content capabilities, the integration builder allows for real-time data retrieval, analysis, and transformation, enabling your AI agent to provide tailored responses, recommendations, and solutions based on individual user needs.

With its user-friendly interface, intuitive features, and no-code functionalities, the integration builder offers full flexibility and customization without the need for extensive technical knowledge.

In this article, we will explore the key features and benefits of the integration builder, along with a step-by-step guide on how to harness its capabilities to connect your AI agent to any API or data source.

- [Getting started](#h_01HAY9KGH0YC6ZH7800G5VZCNG)
- [Request parameters](#h_01HAY9KGH06WFPD1BMJAPA3D0Q)
- [Environments](#h_01HAY9KGH0CWG0E9T0BEAJ7772)
- [Test functionality](#h_01HAY9KGH0W4XZ3BSZ8XPT9R51)
- [Scenarios](#h_01HAY9KGH1TPKF9B3C9KN6P7E2)

## Getting started

To access the integration builder, simply click on "API integrations" in the side navigation menu. This will take you to an overview list where all your future integrations will be conveniently listed and accessible. Initially, you will start with either no API integrations or an example API integration, depending on your onboarding journey.

To create a new integration, click on "Add Integration" located in the top right corner. 
Provide a name for the integration, Add a short description with additional context.

Note: For APIs to be used by an [AI agent with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) at the right time and in the right context, it’s extremely important to add a clear description. Make sure your description covers what the API is, how to use it, and the meaning of different parameters.

Once done, click "Save" to proceed to the integration configuration page.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867222715410.png)

If you can’t see API integrations in the side navigation, this most probably means that you are not a Client Admin. We currently restrict access to the integration builder to Client Admins only. In this case, please contact your CSM to discuss your access rights.

In case you prefer learning with video and audio input, we have an introduction video below by a member of our custom engineering team, Chloe.

## Request parameters

To begin, you need to configure the necessary request parameters to ensure a successful response from the API. These request parameters contain information derived from the conversation and serve to define the specifics of the API request. For instance, if you intend to retrieve particular user information to display during the conversation, it becomes crucial to include the userID as part of the request. This ensures that the API response contains data relevant to the current user or visitor engaged in the chat.

Below is an example of a configured request parameter.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867222717202.png)

In addition to specifying the key and request parameter type, you have the option to set a test value. It is highly recommended to do so, as this test value will be used during configuration when utilizing the test functionality in the top right corner. During an actual live conversation, the value will be passed to the API integration before making the request. However, since we lack the context of the current live conversation, setting a test value is necessary to successfully perform an API call.

The "required" checkbox allows you to determine whether the request parameter is optional or needs to be gathered before calling the API integrations in the conversation if it hasn't already been saved in the session.

The inclusion of request parameters depends on the specific requirements of the API being called. For some APIs, the request parameters are appended to the URL, while for others, they are included in the headers or body of the request. Please consult your API documentation to determine where the request parameter should be included. Once identified, you can add the request parameter to the URL, header, or body by simply referencing the key surrounded by double curly brackets - {{userID}}.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867222720018.png)

## Environments

Once the request parameter is added, the primary setup for the API call can be performed within the environment section. Adjacent to the environment name that appears during integration testing or when referring to it in the dialogue builder, you need to choose the method, URL, and Authorization type based on the underlying API documentation.

### Authorization types

We offer the following Authorization types:

| | | |
| --- | --- | --- |
| Authorization type | Description | Example |
| API Key | A simple API Key that should be provided by the API owner. | |
| Bearer Token | Another token that should be provided by the API owner. | |
| Basic Auth | A username and password are used to authenticate with the API. | |
| OAuth 2.0 | Several Authentication information is needed based on the grant type | Screenshot |
| Custom | Authorization via expiration token | See [Using custom authorization with the integration builder](https://support.zendesk.com/hc/en-us/articles/8357749813658). |

Please remember to include the auth token in the request by adding it as {{apiToken}} to the headers for all authorization types (except for no authorization). Take a look at the header section for an example.

### Headers

Headers contain additional information about the request or the client and server communicating with each other. They are key-value pairs included in the request's header section. Some commonly used headers include:

- Content-Type: Indicates the format of the data in the request body (e.g., JSON, XML, form data).
- Authorization: Provides credentials or tokens to authenticate the client making the request.
- User-Agent: Specifies the user agent initiating the request, typically the web browser or client application.
- Accept: Informs the server about the response formats accepted by the client.
- Cache-Control: Defines caching directives for the server or intermediary caches.
- X-Requested-With: Identifies the type of request (e.g., XMLHttpRequest, Fetch API) made by the client.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867222725778.png)

### Body

The body of an API request contains the data sent to the API. It is typically used in requests that require input data for processing or data manipulation on the API side. The body can contain various formats, such as JSON, XML, plain text, or form data, depending on the API and the specific endpoint being called. In our case, we only support JSON so far.

![Screenshot 2023-09-22 at 13.13.47.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_13906741866770.png)

### Managing environments

In order to address the challenges of handling sandbox and production environments for APIs, we have incorporated the concept of environments into the integration builder. Alongside the default main environment that is automatically created when setting up an integration, you have the flexibility to include additional environments.

These additional environments allow you to customize the URL, authentication details, headers, and body of requests, enabling you to target specific sandbox or production environments within your API.

To create a new environment, simply click on the "+" button located beside the Environment section. If you wish to replicate an existing environment, hover over it and choose the "duplicate" option from the three-dot menu. Keep in mind that only one environment can be set as the default, which will be positioned at the top of the list and automatically selected first in the dialogue builder (unless intentionally modified).

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867236211474.png)

If an environment is not being utilized by any AI agents and it is either the sole environment or the default environment, it can be deleted. To modify the default settings, you can easily select the appropriate option from the three-dot menu.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867222730770.png)

## Test functionality

Once you have completed the setup of the API request, it is helpful to verify if all configurations were done correctly. To facilitate this process, the integration builder offers a convenient testing functionality located at the top right corner.

The test button is easily identifiable by the label "Test" followed by the name of the default environment. By clicking on it, the integration builder initiates a request to the API using the provided information from the request parameters and environment sections. The response received from the API is then displayed in the Test Integration section on the right-hand side of the interface. If you wish to test the API using the request details from a different environment, simply select the desired environment from the dropdown menu within the test functionality and click the test button again.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867222732178.png)

### Response Content

Within the Test Integration section, the integration builder presents the response obtained from the API. The content of the response is organized into the following objects:

| | | |
| --- | --- | --- |
| Objects | Content | Example |
| statusCode | HTTP response status codes indicate whether a specific HTTP request has been successfully completed. [Learn more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). | "statusCode": 200 |
| data | The data object showcases the relevant data of the API in the event of a successful request. However, if the request is unsuccessful, it provides additional information based on the corresponding status codes. | "data": { "name": "Germany", "capital": "Berlin", "region": "Europe", "population": 83240525, "area": 357114 } |
| requestParameters | Within the requestParameters object, the integration builder exhibits the request parameters along with the associated test values employed to invoke the API. | "requestParameters": { "country": "de"} |

#### Before utilizing the test functionality again to examine the integration with any modified configurations, please ensure to save the integration.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867236219282.png)

## Scenarios

Each newly created integration includes three pre-configured scenarios. While two of these scenarios can be customized or deleted according to your needs, the third scenario, named "Fallback," cannot be edited. This "Fallback" scenario functions as the primary fallback option in case none of the previous scenarios get triggered.

| | | |
| --- | --- | --- |
| Scenario | Default query | Description |
| Success | statusCode >= 200 and statusCode < 300 | The scenario that should capture the preferred/happy path if the statusCode is between 200 and 300. |
| Failure | statusCode < 200 or statusCode >= 300 | The scenario that should capture the unsuccessful path if the statusCode is outside of 2XX. |
| Fallback | - | Fallback scenario to always trigger at least one scenario. |

Scenarios are equivalent with the different branches the conversation follows on the dialogue when the API integration is triggered.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867236220178.png)

### Scenario queries

Only one scenario can be triggered for each API integration. The logic for determining which scenario gets triggered during a conversation is based on the Scenario Queries and the order in which the scenarios are defined.

The Scenario Queries represent the conditions that must be met in order to trigger a specific scenario. To determine if a condition is true, the integration builder examines the Scenario Query as well as the data contained in the API response. Commonly used data fields include statusCodes, API-specific data within the data object of the API response, and possibly even values from the request parameters.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11867236223762.png)

The Success scenario's default scenario query requires the API response's statusCode to be within the range of 200 to 300. If this condition is met, the Success scenario will be triggered.

Since the default scenario queries can be modified and new scenarios can be added, it is possible for multiple scenario queries from different scenarios to be true based on the API response. In such cases, the order of the scenarios determines which scenario will be triggered.

To provide visual feedback, we have implemented a feature that indicates which scenario would be triggered based on the current API response. It also identifies scenarios that would theoretically be triggered but are not actually triggered due to a higher-order scenario being triggered. Additionally, it highlights scenarios that would not be triggered because their conditions are not fulfilled.

| | | |
| --- | --- | --- |
| Criteria match | Visualisation | Description |
| Criteria matches first in order | Screenshot | The scenario highlighted by a blue solit dot represents the scenario that will be triggered. |
| Criteria doesn’t match | Screenshot | The scenario(s) highlighted by an empty dot will not be triggered. |
| Criteria matches but not first in order | Screenshot | The scenario(s) represented by a grey solid dot would only be theoretically triggered. |

To modify the order of scenarios, simply click on a scenario and rearrange the order by dragging it. Except for the Fallback scenario, which always remains in the last position, you can adjust the order according to your preference.

### Session parameters

When configuring each scenario, you have the ability to enhance the conversation with various data points from your backend systems. You can specify the desired data to be accessible for each scenario by transforming and storing relevant information from the API response into session parameters. These session parameters can then be utilized in the dialogue-building process to present information to visitors or to map out the underlying workflow.

A session parameter is defined by a key-value pair. The key serves as a reference within the dialogue builder, while the query is employed to transform and extract specific data from the API response to save the value. The integration builder provides real-time feedback on how the saved value, based on the current response, will appear in the response value field.

![Screenshot](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11879016516242.png)

In the image above, the session parameter key is defined as "capital" and can be referenced within the dialogue builder using curly brackets - {{capital}}. The query determines which data should be transformed and saved as the value for the session parameter. In this case, it extracts the content from the "capital" field within the data object of the API response.

### Query language - JSONata

JSONata serves as the query language for both scenario-level and session parameter-level queries. It is designed with the principle that simple queries should be easy to write, making it accessible to both tech-savvy and non-tech-savvy professionals. JSONata features a shallow learning curve, allowing it to be quickly mastered. With JSONata, you can execute basic functions, transform dates, and even merge different data points together.

![Screenshot 2024-02-21 at 09.21.32.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_17178077806994.png)

JSONata is a publicly documented query and transformation language and the documentation can be found [here.](https://docs.jsonata.org/overview.html)
# Messaging recipe: Getting external data for your AI agent for messaging (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5414486254618-Messaging-recipe-Getting-external-data-for-your-AI-agent-for-messaging-Legacy

---

This article describes
functionality available only to customers who had a drafted or published AI
agent as of February 2, 2025. For information about equivalent functionality
in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see
[Building dialogues for AI agents -
Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

The [Make API call](https://support.zendesk.com/hc/en-us/articles/4572971586586) step lets an AI agent for messaging
use a REST API request to fetch data from an external system, such as Shopify or
Salesforce.

In this recipe, you’ll create an AI agent answer that retrieves weather data for a location
provided by an end user. The answer gets the data from the [OpenWeather
API](https://openweathermap.org/api). You can use the answer flow created in this recipe as a starting
point for building your own API-powered answers.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/make-api-call-step-testing-bot.gif)

The recipe involves the following tasks:

- [Task 1: Checking your setup](#topic_ufl_lgl_nwb)
- [Task 2: Creating an API connection](#topic_gbv_wgl_nwb)
- [Task 3: Creating a custom ticket field](#topic_eqy_fhl_nwb)
- [Task 4: Building an AI agent answer](#topic_ffc_shl_nwb)
- [Task 5: Testing your changes](#topic_evp_lml_nwb)

Note:
Zendesk provides this article for instructional purposes only. Zendesk
doesn't support the examples in this article. Zendesk also doesn’t support
third-party technologies, such as the OpenWeather API.

## Task 1: Checking your setup

To complete this recipe, you’ll need the following:

- A Zendesk account with a published AI agent for messaing. You can use a [sandbox testing environment](https://support.zendesk.com/hc/en-us/articles/4408828617370) to test the
  AI agent before using it in production.

  To set up an AI agent on a
  web and mobile messaging channel, see [Creating an AI agent for your web and
  mobile channels](https://support.zendesk.com/hc/en-us/articles/4408824263578). For information about using
  messaging in a sandbox environment, see [Using messaging in your
  sandbox](https://support.zendesk.com/hc/en-us/articles/4408844075930).
- An API key for an [OpenWeather](https://openweathermap.org/)account. The API used in this recipe is
  available on OpenWeather’s free plan.

  To sign up for a free
  OpenWeather account, see the Create New Account page on [openweathermap.org](https://home.openweathermap.org/users/sign_up). After signing
  in, you can get an API key on your [OpenWeather account page](https://home.openweathermap.org/api_keys).

  To
  activate OpenWeather API keys, you must verify your account email
  address. After verification, API keys can take up to two hours to
  activate. For more information, see the FAQ on [openweathermap.org](https://openweathermap.org/faq).

## Task 2: Creating an API connection

To start, create an API connection to store your OpenWeather API key. Your AI agent can use this
connection to authenticate calls to the OpenWeather API.

**To create the connection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Connections >
   Connections**.
2. Click
   **Create connection**.
3. Select the
   **API key**
   authentication type.
4. Enter
   **openweather\_api\_key** as the
   **Connection name**.
5. Enter
   **x-api-key** as the
   **Header name**.
6. Enter your OpenWeather API key as the
   **Value**.
7. Enter
   **api.openweathermap.org** as the
   **Allowed domain**.
8. Click
   **Save**
   to create the connection.

## Task 3: Creating a custom ticket field

Next, create a custom ticket field to capture the location provided by the end
user.

**To create the custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Click
   **Add field**.
3. Select the
   **Text**
   field type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_downvote_feedback_text_custom_field.png)
4. Enter
   **Location**
   as the
   **Display name**.
5. Under
   **Permissions**, select
   **Customers can edit**.
6. Under
   **Customers**, enter
   **Location**
   as the
   **Title shown to
   customers**.
7. Click
   **Save**.

If your account uses a single ticket form, the new field automatically appears in
your ticket form. To remove the field, see
[Editing ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858#topic_c5x_l3b_lk).

## Task 4: Building an AI agent answer

This section walks you through creating the answer, setting its intent, and adding
steps for the answer in the bot builder. This involves the following steps:

- [Step 1: Creating the answer](#topic_sry_thl_nwb)
- [Step 2: Setting the answer’s intent](#topic_kv1_f3l_nwb)
- [Step 3: Adding an initial message step](#topic_ifq_33l_nwb)
- [Step 4: Asking the end user for a location](#topic_mpx_n3l_nwb)
- [Step 5: Retrieving weather data for the location](#topic_hd2_rjl_nwb)
- [Step 6: Sending a weather message to the end user](#topic_rgg_qkl_nwb)
- [Step 7: Adding a failure message](#topic_zxc_vll_nwb)
- [Step 8: Publishing your updated AI agent](#topic_u1q_3ml_nwb)

### Step 1: Creating the answer

Use bot builder to create an answer for your AI agent.

**To create the answer**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to work with.
3. On the Answers tab, click
   **Create answer**.

### Step 2: Setting the answer’s intent

Set the answer’s intent and training phrases. These include phrases and words
used to trigger the answer in a conversation.

**To set the answer’s intent**

1. On the Answers tab of the AI agent’s edit page, click **Create answer**.
2. Click **Build your own answer**, then click **Next**.
3. Enter
   **Get weather**
   as the answer’s
   **Intent**.
4. Under
   **Training phrases**, enter
   **Get weather forecast**
   and
   **Get current temperature.**
5. Click
   **Next**.

   The answer opens in the bot builder where you can
   build out the response.

### Step 3: Adding an initial message step

Add a
**Send message**
step to ask the user for a location. This is the first
step in the answer’s flow.

**To add an initial message step**

1. In the bot builder, click
   **Add step**.
2. Under
   **Choose step**, select
   **Send message**.
3. In **AI agent message**, enter the following text:

   ```
           What location would you like to get the weather for?

   Include the country code. For example: "Melbourne, AU" or  "San Francisco, US"
   ```

### Step 4: Asking the end user for a location

After the initial message, add an
**Ask for details**
step to present a basic
form to the end user. The form includes a text box for the
**Location**
ticket field’s value.

**To add an Ask for details step**

1. In the bot builder, click the
   **Add step** icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-step-icon.png)).
2. Under
   **Choose step**, select
   **Ask for details**.
3. Enter
   **Get location**
   as the
   **Name**.
4. In
   **Fields**, type and select the
   **Location**
   ticket field.

### Step 5: Retrieving weather data for the location

Add a
**Make API call**
step to get weather data for the location from the
OpenWeather API’s
[Current weather data](https://openweathermap.org/current)
endpoint.

**To add a Make API call step**

1. In the bot builder, click
   **Add step**.
2. Under
   **Choose step**, select
   **Make API Call**.
3. Enter
   **Get weather**
   as the
   **Name**.
4. Under
   **API details,**
   enter
   `https://api.openweathermap.org/data/2.5/weather?units=metric&q=`as the
   **Endpoint URL.**
5. Use the **Add a variable** icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-variable-icon.png)) to append the
   **Location** field variable to the **Endpoint
   URL** value.

   The finished **Endpoint URL**
   value should look like this:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/make-api-call-step-openweather-url.png)
6. In
   **Authentication**, select the
   **openweather\_api** connection.
7. To test the API request, click
   **Make API call**.
8. Under
   **Test Data**, enter
   **Melbourne, AU**
   as the
   **Location**.
9. Click
   **Make API call**.
10. Save the following variables using their default names:
    - **main**
      >
      **temp**
    - **weather**
      >
      **item 1**
      >
      **description**

### Step 6: Sending a weather message to the end user

After retrieving the weather data, use a
**Send message**
step to respond with
a message containing the weather data.

**To add an API success message**

1. In the bot builder, click
   **Add step** under the
   **Get weather**
   step’s
   **API call successful**
   branch.
2. Under
   **Choose step**, select
   **Send message**.
3. In **AI agent message**, enter the following text:

   ```
           It's {{temp}}° C with {{description}} in
   ```
4. Use the **Add a variable** icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-variable-icon.png)) to append the
   **Location** field variable to the **AI agent
   message** value. Then add a period (.).

   The
   finished **AI agent message** value should look
   like this:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/make-api-call-step-recipe-success-msg.png)

### Step 7: Adding a failure message

The request made during the
**Make API call**
step may fail. For example, the
request may include a location that doesn’t exist. Add a
**Send message**
step to the
**API call failed**
branch. This step returns a message if the
OpenWeather API call fails.

**To add an API failure message**

1. In the bot builder, click
   **Add step** under the
   **Get weather**
   step’s
   **API call failed**
   branch.
2. Under
   **Choose**
   step, select
   **Send message**.
3. In **AI agent** message, enter the following text:

   ```
           I'm sorry. I wasn't able to get weather data for
   ```
4. Use the **Add a variable** icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-variable-icon.png)) to append the
   **Location** field variable to the **AI agent
   message** value. Then add a period (.).

   The
   finished **AI agent message** value should look
   like this:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/make-api-call-step-recipe-fail-msg.png)

### Step 8: Publishing your updated AI agent

To push the answer live, publish the updated AI agent.

**To publish the AI agent**

1. Click **Done** in the upper right corner of the bot
   builder.
2. On the AI agent page, click **Publish AI agent**.
3. Click **Publish**.

## Task 5: Testing your changes

After you publish your changes, you can test the new answer by asking “How’s the weather?” in a
conversation with the updated AI agent. For more information about testing
AI agents for messaging, see [Testing the end user's messaging
experience](https://support.zendesk.com/hc/en-us/articles/4408835784602).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/make-api-call-step-testing-bot.gif)
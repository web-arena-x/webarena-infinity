# Creating custom actions for auto assist and action flows

Source: https://support.zendesk.com/hc/en-us/articles/8013439366810-Creating-custom-actions-for-auto-assist-and-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

Custom actions are automated tasks that you configure. They can be carried out by [auto assist](https://support.zendesk.com/hc/en-us/articles/7051314237466), which is part of [agent copilot](https://support.zendesk.com/hc/en-us/articles/7908817636378), and by [action flows](https://support.zendesk.com/hc/en-us/articles/8855513857306), which perform a pre-defined series of
automated actions.

This article contains the following topics:

- [Best practices for creating custom actions](#topic_gyz_55n_xcc)
- [Creating a custom action](#topic_lp5_s5n_xcc)
- [Testing an action](#topic_bxm_t5n_xcc)
- [Next steps](#topic_ynl_w5r_1fc)

Related articles:

- [About actions for auto assist and action
  flows](https://support.zendesk.com/hc/en-us/articles/9174548349978)
- [Managing actions for auto assist and action
  flows](https://support.zendesk.com/hc/en-us/articles/9156980948250)

## Best practices for creating custom actions

When creating custom actions, follow these best practices:

- **Use connections for authentication.** Don’t include authentication
  credentials in your custom action configuration. [Use a connection](https://support.zendesk.com/hc/en-us/articles/5040378297626) instead, which are
  purpose-built to keep your sensitive details safe.
- **Be mindful of access privileges.** Keep in mind that a connection might
  have higher access privileges than your agents or end users. Configure your
  custom actions, [procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738), and agent training to
  avoid sharing sensitive data to the wrong audience.
- **Keep your data as private as possible.** When capturing parts of a custom
  action’s response as outputs, be mindful of only capturing the specific data
  points you need. Capturing data that isn’t directly relevant to the task at hand
  isn’t good privacy practice, and furthermore could confuse auto assist.
- **Write good names and descriptions for custom actions, inputs, and
  outputs.** Names and descriptions help auto assist determine when custom
  actions (including their inputs and outputs) are relevant to a customer request.
  Additionally, if you make changes to an existing custom action, make sure that
  the name and description are still accurate.

  Names and descriptions must
  clearly describe the meaning and outcome of a custom action. For example:

  - Custom action name: Add book to cart
  - Custom action description: Adds a book to the customer's shopping
    cart.

  When referencing custom actions in auto assist procedures, remember to
  use similar language to invoke a particular action.

  - For example: “After the customer has confirmed the book they want to
    purchase, add that book to their cart.”
- **Plan for missing inputs.** If an input will be available only sometimes,
  make sure your description explains how that situation should be handled. For
  example, not every requester will have an email address. So your description for
  an input named *requester\_email\_address* might say, "The email address of
  the end user who initiated the ticket. If this isn't available, use 'not
  available.'"
- **Clearly differentiate your names and descriptions for custom action and
  action flows.** If you're using both custom actions and action flows,
  it's important that the names you use for each are clearly differentiated. While
  custom actions and action flows are managed in separate parts of Admin Center,
  auto assist still sees both and considers them to be equivalent.

  For example,
  if you have a custom action named "order refund" and an action flow named
  "refund order", the descriptions need to be detailed enough to differentiate
  them. If they both have vague descriptions, auto assist might suggest the
  wrong one or pick both.

### Limits for custom actions

The following limits apply to custom actions:

- You can have a maximum of 100 custom actions per account.
- Each custom action has a maximum of 100 inputs and 100 outputs.
- Custom actions have a timeout of 10 seconds. If the external system takes
  longer than 10 seconds to respond, or that response fails to be received by
  your Zendesk account, the action isn't performed.
- Custom actions have a maximum response size of 2MB.
- Custom actions created before March 13, 2025 aren't available as steps in
  action flows until they've been updated and saved.

## Creating a custom action

Admins can create custom actions in Admin Center. Custom actions connect to external
systems and require the following information:

- **Input**: The information that an action uses in order to run. Each
  input you define creates an input placeholder, which can be inserted into
  the URL, body, query parameters, or headers of your action.

  Auto assist
  replaces these placeholders with data when it executes the action. In
  action flows, the placeholders can be used in various properties of
  action flow steps.
- **API call**: How, exactly, the information should be structured when
  it’s sent to the API.
- **Output**: Determines how Zendesk should interpret the data returned by
  the API. The outputs you define tell the action which parts of the API
  response to send back to auto assist when the action is executed.

**To create a custom action**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Custom
   actions**.
2. Click **Create custom action**.
3. In the **Name** field, enter a descriptive name for your custom action.

   This name appears to agents and in the event log.
4. In the **Description** field, enter a description of the action.

   This
   description is used by the system to determine when the custom action
   should be used with [auto assist](https://support.zendesk.com/hc/en-us/articles/7051314237466). For help writing
   good descriptions, see [Best practices for creating custom actions](#topic_gyz_55n_xcc).
5. In the **Inputs** section, click **Add input**.
   1. In the **Add input** window, provide the following information:
      - **Name**: Enter a descriptive name for the input.
      - **Description**: Enter a description of the input.
      - **Type**: Select from the following options:
        **String**, **Integer**, **Decimal**,
        **Boolean**, **Date**, **Datetime**, or an
        **Array** of the supported data types.

        Input types are
        strictly enforced. For example, 3.0 isn't accepted as an
        integer, the string “true” isn't accepted as a boolean,
        and the boolean value false isn't accepted as a
        string.
   2. Click **Add input**.
6. In the **API configuration** panel, provide the following information:
   1. **Request method**: Select **GET**, **POST**, **PATCH**,
      **PUT**, or **DELETE**, depending on what you want your
      action to do.
   2. **Endpoint URL**: Enter the URL of your external service.

      Only
      `https://` URLS are allowed.
   3. **Authentication**: Select an existing [API connection](https://support.zendesk.com/hc/en-us/articles/5040378297626).
   4. **Body**: Enter the information that you’re requesting in this
      API call.

      To insert placeholders for any of the inputs you
      created, click **{+}** and select the appropriate
      input.
   5. **Query parameters**: Click **Add parameter** and add a
      **Key** and **Value** for any parameters that apply to
      this API call.
   6. **Headers**: Click **Add header** and add a **Name** and
      **Value** for any headers that apply to this API call.

      You
      don’t need to add a content-type header. Only the
      application/json value is supported, and this header is
      automatically added when the API call is made.

      If you
      specify an accept header, use the format
      `application/{{subtype}}+json`, where
      `{{subtype}}` is replaced with the system you
      want to connect to. For example, to connect with Recurly, you'd
      specify
      `application/vnd.recurly.v2021-02-25+json`.
      If you don't specify an accept header, this header is
      automatically added with the `application/json`
      value.
7. In the **Outputs** section, click **Add output**.
   1. In the **Add outputs** window, enter test data for each of the
      inputs you configured.
   2. Click **Make API call**.

      This information is sent to your
      external service, which returns a representative response.

      Note: When an external action runs,
      the response must be JSON and must have the appropriate JSON
      header (content-type: application/json). Other JSON-compatible
      content types aren’t currently supported (for example,
      vnd.oracle.resource+json or vnd.api+json).
   3. On the **Output** tab, find the appropriate output from the
      response and click **Add**.

      You can click the **Response
      body** tab to see how the actual response is
      formatted.
   4. Enter a **Name** and **Description** for the output, then
      click **Add output**.
   5. Repeat as required to capture all the outputs you want to return to
      auto assist.
   6. Click **Done**.

      If a mapped output isn’t included in the
      response when an action is executed, the action still succeeds,
      but the output’s key is omitted from the response sent back to
      auto assist.
8. Click **Save**.

## Testing an action

When you create a custom action, you should test it to make sure it behaves as you
expect. If necessary, run multiple tests with different input values that yield
different responses to test all possible outputs.

**To test an action**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Custom
   actions**.
2. For the custom action you want to edit, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Test**.
3. In the **Inputs** section of the **Test** tab, enter test data for
   each of the inputs you configured.
4. Click **Make API** call.

   This sends information to the external
   service your custom action is connected to and returns a representative
   response.
5. In the **Outputs** section, verify that the response includes the
   information you expect.

If you encounter issues during testing, here are some troubleshooting
recommendations:

- Because custom actions are connected to external systems, the external system's
  documentation is the best source for detailed troubleshooting.
- For an overview of HTTP error codes that you might encounter during testing, see
  [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).
- Ensure that all inputs and outputs are the correct data type (integer, decimal,
  string, or boolean) for your use case.
- You can see more details about the custom action execution in the [integration log](https://support.zendesk.com/hc/en-us/articles/4408819871130).

## Next steps

After creating and testing an action, you can do the following:

- [Insert the action when creating auto
  assist procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738#topic_vs3_j44_xcc)
- [Add the action as a step when creating
  action flows](https://support.zendesk.com/hc/en-us/articles/8855601898266)
- [Manage your custom actions](https://support.zendesk.com/hc/en-us/articles/9156980948250)
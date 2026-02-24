# Using Workday actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/10050789681050-Using-Workday-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Workday, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Workday to action builder](#topic_qpb_pjf_phc)
- [Using Workday actions in action flows](#topic_ilp_rjf_phc)
- [Recipe: Notifying managers when a request for hardware is approved](#topic_i5h_sjf_phc)

## Connecting Workday to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it's a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect Workday to the action builder**

1. [Create an OAuth client in Workday](#topic_c5j_ktm_phc).
2. [Use the OAuth client to connect Workday to the action builder](#topic_vp5_qtm_phc).

   After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Workday.
3. (Optional) Configure Workday to allow contact information to be updated through REST API requests.

### Creating an OAuth client in Workday

Workday uses OAuth 2.0 for authorization. A Workday administrator must set up an OAuth 2.0 client in Workday to provide Zendesk secure access to your data in Workday.

**To set up an OAuth 2.0 client in Workday**

1. Sign into your Workday account as an administrator.
2. In the Workday search bar, type **Edit Tenant Setup - Security**, then select the matching option from the search results list.
3. Scroll down to the OAuth 2.0 Settings section and turn on the **OAuth 2.0** configuration.
4. Configure the API client:
   - **Search**: Select **Register API Client**.
   - **Client Name**: Enter a meaningful name for your client, such as *Zendesk connection*.
   - **Client Grant Type**: Choose **Authorization Code**. See [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) for more information about grant types.
   - **Client Redirect URL**: Enter

     ```
     https://zis.zendesk.com/api/services/zis/connections/oauth/callback
     ```
5. Use the **API scopes** field to specify the following permissions for the app to access Workday data:
   - ```
     System
     ```
   - ```
     Staffing
     ```
   - ```
     Time off and leave
     ```
   - ```
     Home Contact Information
     ```
   - ```
     Work Contact Information
     ```
6. Click **Save**.
7. After saving, securely save the following generated values that appear in Workday. These are required for connection, authentication, and token generation.
   - Client ID
   - Client Secret

     Note: The Client Secret displays only once. Copy and save it in a secure
     location, such as a password manager.
   - Token Endpoint URL
   - Authorization Endpoint URL
   - Workday REST API URL

Note: If an Admin changes the password in Workday, the OAuth2 client stops functioning. When this happens, you must remove the existing connection and set it up again.

### Connecting Workday to the action builder

After creating the Workday OAuth 2.0 client, you have the information necessary
to connect Workday to action builder.

**To connect action builder to Workday**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Workday**.
5. Click **Connect**.
6. Enter the following values from the [Workday OAuth client](#topic_c5j_ktm_phc) in the corresponding
   fields:
   - **Client ID**
   - **Client Secret**
   - **Token Endpoint URL**
   - **Authorization Endpoint URL**
   - **Workday REST API URL**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/action_flow_workday_connector.png)
7. Follow Workday's prompts to authenticate and complete the
   connection.

   Note: All external actions performed by an action flow
   are attributed to the user who connected the external system.
   Therefore, it's a best practice to use a dedicated service account
   rather than personal credentials when connecting to each external
   system.

### Configuring Workday to allow REST API updates to contact information

Before you can use the *Contact information* action, you must configure
Workday to allow users' contact information to be updated by the API. To do
this, grant permission to a security group to update employee contact
information using the Workday REST API.

The following requirements must be met to configure this:

- Admin-level access to Workday security and business process
 policies
- A security group exists or is created for the service account
- All changes are tested in a sandbox environment first

**To configure Workday to allow API updates to user contact information**

1. In Workday, run the **Maintain Permissions for Security Group**
   task.
2. Select the security group you want to allow to use the API to update
   contact information.
3. For the **Person Data: Home Contact Information** and **Person Data:
   Work Contact Information** domains, add the following
   permissions:
   - **View and Modify**
   - **Get and Put**
4. Run **Activate Pending Security Policy Changes** to publish the
   domain-level permission updates.
5. Open your **Business Process Security Policy for Work Contact
   Change** to edit it.
6. Under **Initiating Action > Change Work Contact Information (REST
   Service)**, add the security group you just granted permission to
   use the API to update contact information.
7. Click **Save**.
8. Open your **Business Process Security Policy for Home Contact
   Change** to edit it.
9. Under **Initiating Action > Change Home Contact Information (REST
   Service)**, add the security group you just granted permission to
   use the API to update contact information.
10. Click **Save**.
11. Run **Activate Pending Security Policy Changes** to publish the
    updates.

## Using Workday actions in action flows

Workday action steps can be used to look up employee details and submit time off
requests.

The following Workday actions are available:

- [Look up worker](#topic_gqx_j1g_phc)
- [Request time off](#topic_wns_k1g_phc)
- [Manage primary home
 email](#topic_tq1_fmf_d3c)
- [Manage primary home
 phone](#topic_dgg_bqf_d3c)
- [Manage primary work
 email](#topic_njm_fqf_d3c)
- [Manage primary work
 phone](#topic_mjn_hqf_d3c)

### Looking up an employee

Use the *Look up worker* action to retrieve the personal and employment data
for an individual employee.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `Worker ID` or `Work email address` |
| Output | The employee's personnel data |

### Requesting time off

Use the *Request time off* action to submit time off requests in Workday on
behalf of employees.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `Worker ID`, `Request date`, `Time off type`, `Daily quantity` Note: Dates must be formatted as YYYY-MM-DD or YYYY-MM-DDhh:mm and in the Workday account's timezone. (Optional) `Start date`, `End date`, `Comment` |
| Output | `Request ID` |

### Managing a user's primary home email address

Use the *Manage primary home email* action to update a user's primary home
email address.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `Worker ID`, `Home email` (Optional) `Comment`, `Public visibility` |
| Output | `Request status`, `Updated primary home email` |

### Managing a user's primary home phone number

Use the *Manage primary home phone* action to update a user's primary home
phone number.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `Worker ID`, `Home phone number`, `Country`, `Device type` (Optional) `Public visibility` |
| Output | `Request status`, `Updated primary home phone number` |

### Managing a user's primary work email address

Use the *Manage primary work email* action to update a user's primary work
email address.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `Worker ID`, `Work email` (Optional) `Comment`, `Public visibility` |
| Output | `Request status`, `Updated primary work email` |

### Managing a user's primary work phone number

Use the *Manage primary work phone* action to update a user's primary work
phone number.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `Worker ID`, `Work phone number`, `Country`, `Device type` (Optional) `Public visibility` |
| Output | `Request status`, `Updated primary work phone number` |

## Recipe: Notifying managers when a request for hardware is approved

The following example action flow automatically sends an email notification to an
employee's manager when a Zendesk ticket requesting new hardware, such as a laptop,
is approved.

**To create an action flow that automatically notifies managers when their
employee's request for hardware is approved**

1. [Add an action flow trigger](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_zg5_sx3_t2c) with
   the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click
      **Tickets**.
   3. Click **Properties** and select **Ticket tags changed**.
   4. Click **Add condition**.
   5. Under **Variable**, click **Ticket tags changed** and select
      **Tags (added)**.
   6. Set the **Operator** to **Contains at least 1 of**.
   7. Under **Value**, enter **approved**.
2. Add a step to [look up user details in
   Zendesk](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_fpp_cnk_t2c):
   1. In the action builder, beneath the action flow trigger, click the
      **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      user**.
   3. Under **Ticket ID**, click into the field and then click
      **Select a variable instead**.
   4. Within the variable menu, select **Ticket tags changed** as the
      step that outputs the variable you want to use, and then select
      **Requester ID**.
3. Add a step to look up details about the ticket requester in Workday:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      worker**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Ticket tags changed** as the
      step that outputs the variable you want to use, and then select
      **Requester ID**.
4. Add a step to retrieve the employee's data in Workday:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **Workday** and then select **Look up worker**.
   3. Under **Employee email**, click **Add variable** .
   4. Within the variable menu, select **Look up user** as the step
      that outputs the variable you want to use, and then select **Work
      email**.
5. Add a step to [send an email](https://support.zendesk.com/hc/en-us/articles/9840940606106) notification to the
   employee's manager:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **Microsoft Outlook** and then select **Send email**.
   3. Under **Recipient email**, click **Add variable**.
   4. Within the variable menu, select **Look up worker** as the step
      that outputs the variable, and then select **Supervisor's
      email**.
   5. Under **Subject**, enter the subject of the email. For example:
      "Update: Laptop request for *Employee Name*" where *Employee
      Name* is a variable from the Look up user step.
   6. Under **Body**, enter the message you want to send to the
      employee's supervisor. Include relevant information as variables
      from the Look up user and Look up worker steps, respectively, to
      streamline their ability to solve the ticket. In the following
      example, all variables are
      italicized:

      ```
      Hi Look up worker > Supervisor Name, Your team member, Look up user > Name (employee ID: Look up worker > ID), will be issued a (Ticket tags changed > Laptop make) laptop in the next five days.
      ```

      Note: To
      make the laptop information available for use as variables in
      the action flow, that information must be configured as a ticket
      field.
6. Add a step that [updates the ticket](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_fpp_cnk_t2c) with a copy of
   the email sent to the supervisor:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, select **Update
      ticket**.
   3. Under **Ticket ID**, click **Add variable**.
   4. Within the variable menu, select **Ticket tags changed** as the
      step that outputs the variable, and then select **Ticket
      ID**.
   5. Under **Additional fields**, select **Comment** and **Comment
      is public**.
   6. Under **Comment**, copy and paste the **Body** value from the
      send email step.
7. Under **Comment is public**, select **False**.

   The comment is added
   to the ticket as an internal note.
8. Click **Save**.
9. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
10. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the
    action flow to automatically send an email to employees' supervisors when a
    request for hardware is approved.
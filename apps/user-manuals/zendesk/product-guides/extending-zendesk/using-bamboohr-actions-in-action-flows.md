# Using BambooHR actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/10042011737370-Using-BambooHR-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as BambooHR, admins
can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting BambooHR to action builder](#topic_wkn_2bk_4hc)
- [Using BambooHR actions in action flows](#topic_ffm_hbk_4hc)
- [Recipe: Automatically creating a time off request in BambooHR after it's approved in a Zendesk ticket](#topic_ih2_gjr_4hc)

## Connecting BambooHR to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the
  external system. Therefore, it's a best practice to use a dedicated service
  account rather than personal credentials when connecting to each external
  system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to BambooHR**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **BambooHR**.
5. Click **Connect**.
6. Follow BambooHR's prompts to authenticate and complete the connection.

   The
   following scopes are required: `Claims - read`,
   `Employee - read/write`, `Time Off -
   read/write`, `Reports - read`,
   `Company - read`, `Miscellaneous - read meta
   data`.

   Note: All external actions performed by an
   action flow are attributed to the user who connected the external
   system. Therefore, it's a best practice to use a dedicated service
   account rather than personal credentials when connecting to each
   external system.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
BambooHR.

## Using BambooHR actions in action flows

BambooHR action steps can be used to add and manage employee details and time off
requests in BambooHR.

The following BambooHR actions are available:

- [Get employee
  details](#topic_p2s_jbk_4hc)
- [Add employee](#topic_vyx_jbk_4hc)
- [Update employee](#topic_jgy_y3r_4hc)
- [Request time off](#topic_pt4_z3r_4hc)

### Getting details about an employee from BambooHR

Use the *Get employee details* action to retrieve the personal and
employment data for an individual employee.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `Employee ID` or `Work email address` |
| Output | The employee's personnel data |

### Adding an employee to BambooHR

Use the *Add employee* action to add a new employee to BambooHR.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `First name`, `Last name`, `Work email address` Optional: `Middle name`, `Preferred name`, `Employee number`, `Job title`, `Department`, `Division`, `Location`, `Hire date`, `Gender`, `Home email address`, `Work phone number`, `Mobile phone number`, `Status` |
| Output | `Employee ID` and any variables specified in the input |

### Updating an employee in BambooHR

Use the *Update employee* action to update details for an existing employee
in BambooHR.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `Employee ID` Optional: `First name`, `Middle name`, `Last name`, `Preferred name`, `Employee number`, `Job title`, `Department`, `Division`, `Location`, `Hire date`, `Gender`, `Home email address`, `Work phone number`, `Mobile phone number`, `Status` |
| Output | The employee's updated personnel data |

### Requesting time off in BambooHR

Use the *Request time off* action to submit a time off request for an
employee in BambooHR.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `Employee ID`, `Start date`, `End date`, `Type` Note: Dates must be formatted as YYYY-MM-DD and in the BambooHR account's timezone. |
| Output | Confirmation of submitted request |

## Recipe: Automatically creating a time off request in BambooHR after it's approved in a Zendesk ticket

The following example action flow automatically submits a time off request in
BambooHR when a Zendesk ticket related to the request is approved.

Such an action flow would consist of the following steps:

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
2. Add a step to [look up ticket details](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_fpp_cnk_t2c):
   1. In the action builder, beneath the action flow trigger, click the
      **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      ticket**.
   3. Under **Ticket ID**, click into the field and then click
      **Select a variable instead**.
   4. Within the variable menu, select **Ticket tags changed** as the
      step that outputs the variable you want to use, and then select
      **Ticket ID**.
3. Add a step to [look up user details](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_fpp_cnk_t2c) about the
   ticket assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Ticket tags changed** as the
      step that outputs the variable you want to use, and then select
      **Requester ID**.
4. Add a step to retrieve the employee's data in BambooHR:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **BambooHR** and then select **Get employee
      details**.
   3. Under **Employee email**, click **Add variable** .
   4. Within the variable menu, select **Look up user** as the step
      that outputs the variable you want to use, and then select **Work
      email**.
5. Add a step to submit the time off request in BambooHR:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **BambooHR** and then select **Request time off**.
   3. Under **Employee ID**, click **Add variable**.
   4. Within the variable menu, select **Look up user** as the step
      that outputs the variable you want to use, and then select **Work
      ID**.
   5. Under **Start date**, click **Add variable**.
   6. Within the variable menu, select **Look up ticket** as the step
      that outputs the variable you want to use, and then select the
      **Start date**.
   7. Under **End date**, click **Add variable**.
   8. Within the variable menu, select **Look up ticket** as the step
      that outputs the variable you want to use, and then select the
      **End date**.

   Note: To make the start date and end date information available for use
   as variables in the action flow, these must be configured as ticket
   fields.
6. Add a step that [sends a direct message in Slack](https://support.zendesk.com/hc/en-us/articles/9849650344730) to
   the ticket requester's supervisor that contains the information you
   collected for the time off request:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **Slack** and then select **Post direct message**.
   3. Under **Email**, click **Add variable**.
   4. Within the variable menu, select **Get employee details** as the
      step that outputs the variable, and then select **Supervisor's
      email**.
   5. Under **Message**, enter the message you want to send to the
      employee's supervisor. Include relevant information as variables
      from the Look up ticket and Look up user steps, respectively, to
      streamline their ability to solve the ticket. In the following
      example, all variables are
      italicized:

      ```
      Hi Employee details > Supervisor Name,

      A time off request has been submitted in BambooHR for Requester > Name and requires your attention. Please respond as soon as possible.

      Time off request summary:
      - Start date: Ticket > Start date
      - End date: Ticket > End date
      - Notes: Requester > Notes
      ```
7. Click **Save**.
8. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
9. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the
   action flow to automatically submit a time off request in BambooHR when a
   Zendesk ticket related to the request is approved.
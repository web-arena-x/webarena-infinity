# Editing and managing action flows

Source: https://support.zendesk.com/hc/en-us/articles/9052312956570-Editing-and-managing-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Action flows](https://support.zendesk.com/hc/en-us/articles/8855513857306)
are user-defined integrated workflows that perform actions in Zendesk and external systems, but are managed entirely from within Zendesk. After you [create](https://support.zendesk.com/hc/en-us/articles/8855601898266)
an action flow, you can update it, deactivate it, or delete it.

This article contains the following topics:

- [Managing action flows](#topic_hn2_stk_t2c)
- [Managing an action flow's steps](#topic_ant_ttk_t2c)
- [Testing an action flow](#topic_uyj_qsw_3fc)
- [Troubleshooting action flows](#topic_sdx_vtk_t2c)

Related articles:

- [Creating action flows to automate processs across Zendesk and external systems](https://support.zendesk.com/hc/en-us/articles/8855601898266)
- [Monitoring the usage of action credits and action flow activity](https://support.zendesk.com/hc/en-us/articles/10149993578522)

## Managing action flows

From the Action flows page in Admin Center, you can view and manage your list of action flows in the following ways:

- [Editing an action flow's name and description](#topic_j1x_tlv_bfc)
- [Activating action flows](#topic_kvg_lkv_bfc)
- [Deactivating action flows](#topic_uqv_4lv_bfc)
- [Deleting action flows](#topic_chp_plv_bfc)

### Editing an action flow's name and description

Editing an action flow's name and description is separate from editing the flow's steps in the action builder.

**To edit an action flow's name or description**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Next to the action flow you want to update, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   and select **Edit name or description**.
3. Enter the updated name or description.
4. Click **Save**.

### Activating action flows

New action flows are inactive by default. An admin must activate the flow for it to be used.

**To activate an action flow**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Next to the action flow you want to activate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   and select **Activate**.

### Deactivating action flows

To prevent an action flow from being used, you can deactivate it or [delete](#topic_chp_plv_bfc) it.
Deactivated flows don't occur when their trigger event occurs and aren't presented as options for agent copilot auto assist.

**To deactivate an action flow**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Next to the action flow you want to deactivate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   and select **Deactivate**.

### Deleting action flows

To prevent an action flow from being used, you can deactivate it. However, you can have a maximum of 10 action flows at a time. If you are permanently finished with an action flow, you can delete it.

**To delete an action flow**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Next to the action flow you want to delete, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   and select **Delete**.
3. In the confirmation dialog, click **Confirm**.

## Managing an action flow's steps

Using the action builder, you can edit and delete steps in an action flow.

**To open and manage an action flow in the action builder**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Next to the flow you want to manage steps for, click **Edit workflow**.
3. Make any of the following changes:
   - [Editing a step in an action flow](#topic_dp2_4gw_bfc)
   - [Rearranging the steps in an action flow](#topic_bqp_pgw_bfc)
   - [Delete a step in an action flow](#topic_dfs_qgw_bfc)
4. Click **Save**.

### Editing a step in an action flow

In the action builder, you can click on any step of an action flow to review and modify its configuration as needed.

**To edit a step**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Click the name of the action flow you want to edit.
3. Click on the step you want to edit.
4. Use the step sidebar to update the step's configuration.
5. Click **Save**.

### Rearranging the steps in an action flow

Steps can't be re-ordered. Instead, if you need to change the order of the steps, [delete](#topic_dfs_qgw_bfc) and [re-create steps](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_evq_mrw_bfc)
in the appropriate locations within the flow. In addition to the options to add steps at the end of an action flow's branches, you can also insert them between existing steps.

**To insert a step between existing steps**

- In the action builder, hover between steps and click the add step icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png))
 that appears.

### Delete a step in an action flow

In the action builder, you can click on any step of an action flow to review and modify its configuration as needed.

Note: Any subsequent steps in the action flow that refer to a deleted step's output enter an error state and must be fixed after you delete a step. Even if you recreate an identical step, you still must remove and re-add references to it in subsequent steps.

**To delete a step**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Click the name of the action flow you want to edit.
3. Within the step in the action builder, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   and select **Delete**.
4. In the confirmation dialog, click **Delete step**.

## Testing an action flow

After an action flow has been saved, admins can test it with sample inputs. Test executions are logged in the [integrations log](https://support.zendesk.com/hc/en-us/articles/4408819871130).

Note:

- When testing an action flow, real API requests are submitted for each step. Use test data, such as test tickets, Jira issues, and so on to avoid accidentally altering your service data.
- Any conditions configured for the action flow's trigger are disregarded during testing.

**To test an action flow**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Click the name of the action flow you want to test.
3. Click **Test**.
4. If prompted, use the Test action flow sidebar to enter sample inputs.

   Outputs from the action flow trigger are simulated, so only variable inputs used in the action flow need to be provided during tests.
5. Click **Run test**.
6. Review the results for each step.

   Each step has a status of *Done* or *Failed* and can be expanded to display its output.

   A test ends when a step fails or all steps have been completed successfully.
7. Click **Done** or click **Test again** to try the action flow with other sample inputs.

## Troubleshooting action flows

Do the following if you're having trouble with your action flows:

- [Check the activation status of your action flow](#topic_ivw_2pg_3fc)
- [Fix broken steps](#topic_itl_1rg_3fc)
- [Check the letter casing of values in conditional steps](#topic_pmm_grg_3fc)
- [Check date and datetime formatting](#topic_cdz_ks2_5gc)
- [Align action flow names and descriptions with auto assist procedures](#topic_rrc_qrg_3fc)
- [Re-adding updated action steps](#topic_agk_z1t_mfc)
- [Differentiate the names of action flows from auto assist actions](#topic_q3f_jrm_3fc)
- [Troubleshoot custom code steps](#topic_obr_cfb_chc)

### Checking action flow activation status

If an action flow isn't working as expected, you can start by checking that it's been [activated](#topic_kvg_lkv_bfc).
The activation status of your action flows is visible in the list on the Action flows page in Admin Center.

### Fixing broken steps

Assuming the flow has been activated, the next thing to check is whether all of the steps are properly configured. Steps that aren't working properly, such as an invalid input or a broken connection to an external service, are highlighted in red in the action builder.

**To fix a broken step**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. Click the name of the action flow you are troubleshooting.
3. Click on a step highlighted in red.
4. Use the step sidebar to resolve any configuration issues with the step.
5. Click **Save**.

### Checking letter case in conditional steps

Values for conditional steps are case-sensitive. That means checking for the type *Problem* isn't the same as checking for *problem*.

Standard Zendesk fields typically use lowercase values.

### Check date and datetime formatting

Action flows expect specific [formats for date and datetime values](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_gwb_fxr_hgc).
Ensure date and datetimes include the expected punctuation and have the values in the expected order.

In datetimes, milliseconds are optional, but a timezone is required.

### Aligning action flow names and descriptions with auto assist procedures

When an action flow is initiated by an agent approving an auto assist suggestion, it is important that the language used in the action flow's name and description is closely aligned with one or more of your [auto assist procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738).
When the language isn't similar enough, the action flow won't get suggested to agents.

### Re-adding updated action steps

If you have changed an auto assist action since adding it to your flow, you must delete it and re-add the action. If you use outputs from the action in subsequent steps, you will also need to update these references so they reflect the new version of the action.

### Differentiating names of action flows from auto assist actions

Because auto assist can suggest both actions and action flows, it's important to be precise enough in the names and descriptions for both that auto assist can tell them apart. If the names are too similar, auto assist might suggest the wrong one or both, which could result in unexpected behavior.
For example, if you have an action named *Create Jira issue* and an action flow named *Create Jira ticket*, it's likely auto assist could confuse or conflate the action and action flow.

### Troubleshooting custom code steps

If you're using custom code steps in your action flow, you might also need to do the following:

- [Using code-hinting tips](#topic_dw1_jfb_chc)
- [Checking your input and output names](#topic_tvt_sfb_chc)
- [Checking your data types](#topic_btz_xfb_chc)
- [Validating your outputs](#topic_dtj_ggb_chc)

#### Using code-hinting tips

Within the step, errors in your code are indicated by squiggly red underlining. Hover your mouse over the underlined section to view an explanation of the issue and suggestions for fixing it.

#### Checking your input and output names

The names of inputs and outputs within your code must match the names you enter in the step inputs and outputs. Capitalization and punctuation must match exactly.

#### Checking your data types

Verify that your data is of the correct type. If necessary, you can modify the code to convert the inputs into the correct format. For example:

- If you need to perform calculations on a string input, convert it to a number using `Number(my_input_string)`.
- If you’re working with dates, use `new Date(my_input_date_string)` to convert a string to a JavaScript Date object.

#### Validating your outputs

It's important that your code always returns outputs in the correct type as defined in your step. For example, if you specify a number as the output type, but your code returns a text or null value, the step will fail.

To prevent this sort of error, make sure your code checks that the values exist and are in the expected format. When needed, you can use fallback values, such as the following, for outputs to maintain reliability:

- For text, return an empty string `""`.
- For numbers and decimals, return `-1`.
- For true/false, return `false`.
- For arrays, return an empty array `[]`.
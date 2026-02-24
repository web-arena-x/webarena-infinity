# Turning on and configuring data masking (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/9368104312602-Turning-on-and-configuring-data-masking-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

Enable data masking to protect personally identifiable information (PII)
by hiding end-user names, phone numbers, and email addresses from agents in custom and light agent roles. Consider role-specific needs before activation, and test changes in a sandbox environment. Update messaging ticket subject lines to exclude PII. You can disable data masking to restore access to previously hidden data.

As described in [About data masking](https://support.zendesk.com/hc/en-us/articles/7713908123674), customers with the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906)
can hide personally identifiable information (PII) from agents in custom and light agent roles.
The data masking feature allows you to mask end-user names, phone numbers, and email addresses.

This article includes the following topics:

- [Considerations before turning on data masking](#topic_y1w_dxj_1fc)
- [Turning on data masking](#topic_d4l_vdk_1fc)
- [Removing end-user names from the subject line of messaging tickets](#topic_c1g_qnt_rfc)
- [Turning off data masking](#topic_jy1_kpk_1fc)

## Considerations before turning on data masking

- Define which roles require data masking. Configure masking permissions based on the principle of least privilege, ensuring only those who truly need access to PII can see it. You may want to create dedicated roles specifically designed to restrict access to PII.
- Data masking can significantly affect an agent’s ability to access and interact with end-user information. Before turning on data masking for a custom or light agent role, carefully evaluate the tasks and responsibilities of the agents assigned to that role, and ensure agents are assigned to the correct roles when toggling data masking on or off.
- Carefully select which fields and data types (names, email addresses, or phone numbers) should be masked. Regularly review and update the list to reflect any changes in data collection or business processes.
- Before rolling out changes, test in a [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058)
 to verify that masking rules are working as intended across all relevant areas.
- Provide clear guidance or documentation so admins and agents understand what is masked and why.

## Turning on data masking

Zendesk admins can turn on data masking for agents in custom roles.

**To turn on data masking**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. On the role you want to turn data masking on for, click the options icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png))
   and select **Edit**.
3. In the **Data masking** section, select the **Mask** checkbox for each end-user field you want to mask for agents in this role.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/data_masking_fields.png)
4. Click **Save**.

   An acknowledgment page displays, listing the permission changes that will take effect after clicking **Save**. These changes are required to prevent agents in this role from accessing the selected end-user fields.

   Additional considerations are also provided:
   - To prevent agents from accessing sensitive data in reports, [Explore permissions](https://support.zendesk.com/hc/en-us/articles/4408836002970#topic_ygz_hkr_sjb)
     will be set to **No access** for roles with data masking turned on.
   - The subject line in the messaging ticket template may include end-user names. To secure the PII there, set the messaging template subject line to **Conversation with {end user ID}**.
     See [Removing end-user names from the subject line of messaging tickets](#topic_c1g_qnt_rfc).

     
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/data_masking_turn_on_2.png)
5. Select the statements on the acknowledgment page, then click **Save**.
6. Repeat these steps for any other roles you wish to turn on data masking for.

## Removing end-user names from the subject line of messaging tickets

By default, new messaging tickets include the end user's name in the subject line (for example, "Conversation with Jane Smith"). If you turned on data masking to hide end-user names, you may want to update the subject line to display the end-user ID instead (for example, "Conversation with 5083543234201"). This option is available when data masking is turned on for at least one role and applies to new tickets only.

You can change the subject line back to show the user name instead of the ID.
However, doing so only applies to new messaging tickets. The subject line on existing tickets won't change.

When you update the messaging subject line, it applies to all agents.
The subject line can't be updated for specific roles.

**To remove end-user names from the subject line of messaging tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Manage settings**.
3. In the Tickets section, expand the **Ticket subject line when data is masked** option.
4. Select **Conversation with {end user ID}**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/data_masking_messaging_subject.png)
5. Click **Save settings**.

## Turning off data masking

After you turn off data masking for a custom or light agent role, team members assigned to that role can view previously masked PII. In addition, permissions that were previously locked to protect PII become editable again.

**To turn off data masking**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. On the role you want to turn data masking off for, click the options icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png))
   and select **Edit**.
3. In the **Data masking** section, deselect the **Mask** checkbox for all user fields.
4. Click **Save**.

   An acknowledgment page displays, listing all the changes that will occur after turning off data masking for this role.

     
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/data_masking_turn_off_2.png)
5. Select the statements on the acknowledgment page, then click **Save**.
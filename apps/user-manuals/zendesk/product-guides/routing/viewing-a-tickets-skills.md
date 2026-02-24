# Viewing a ticket's skills

Source: https://support.zendesk.com/hc/en-us/articles/5834247413786-Viewing-a-ticket-s-skills

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Workspaces > Agent tools > Views

As soon as you [add a skill to a skill type](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ug2_j4y_hdb), the Skills field
becomes visible to admins on all tickets. Admins can change settings so that the field
is also visible or editable by agents, too.

This article contains the following topics:

- [Viewing skills on a ticket](#topic_kqk_vlw_vxb)
- [Configuring who can see the skills ticket field](#topic_qxr_glw_vxb)

For information about assigning skills to tickets, see [Adding and managing skills on tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930).

## Viewing skills on a ticket

**To view the skills assigned to a ticket**

- In Support, [open the ticket](https://support.zendesk.com/hc/en-us/articles/4408882039450-Working-with-tickets-#topic_xlz_zsm_pf:~:text=syntax%20(if%20applicable).-,To%20open%20a%20ticket,-Locate%20the%20ticket) and find the
  **Skills** field.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/skills_field_ticket.png)

## Configuring who can see the skills ticket field

Unless you modify the settings to grant agents additional permissions, only
admins can see and update the skills field. The settings chosen here are applied to
all admins and agents, and to all skills. You can update these settings at any
time.

Light agents can't edit skills, regardless of the selected settings.

**To configure the skills field visibility options**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Click the configuration icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/mobile_settings_icon.png)) next to the New skill type button.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/skill_configuration_icon_fullscreen.png)
3. In the **Manage skills on tickets** dialog, use the dropdown to
   select the visibility configuration you want to apply to the skills field:
   - **Administrators only (view and update)**: (Default) Administrators
     can view and update skills in tickets. Agents cannot view or update
     skills.
   - **Administrators (view and update) and agents (view only)**:
     Administrators can view and update skills in tickets. Agents can view
     skills in tickets, but can't update them.
   - **Administrators (view and update) and agents (view and update)**:
     Administrators and agents can view and update skills in tickets.
   - **No one (disabled)**: The Skills field isn't visible to any users.
4. Click **Save**.
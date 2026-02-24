# Giving agents access to voice

Source: https://support.zendesk.com/hc/en-us/articles/4408882966170-Giving-agents-access-to-voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

After you've [turned on and configured the voice channel](https://support.zendesk.com/hc/en-us/articles/4408838035866), you need to give your agents access. On Enterprise plans, you use custom roles to configure access for multiple users simultaneously. If you're not using an Enterprise plan, or if you want to configure settings for individual users, you configure access from the Team members page in Admin Center.

You can manage access to the voice channel for one user at a time.

This article contains the following sections:

- [Giving access to voice (non-Enterprise plans)](#topic_anr_nj3_vyb)
- [Giving access to voice (Enterprise plans)](#topic_ycb_4j3_vyb)

## Giving access to voice (non-Enterprise plans)

If you're not using an Enterprise plan, you configure access to voice from the Team members page in Admin Center.

**To manage access to voice (non-enterprise plans)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. On the **Team members** page, click the user you want to grant access. The user you choose must have the **User type** of **Staff member**.
3. In the **Voice** section of the page, enable the **Access** checkbox. If you don't enable this checkbox, the user cannot access voice.
4. From the **Role** dropdown, choose one of the following voice roles for this agent:
   - **Admin:** An admin can manage all voice settings found in Admin Center under **Channels** > **Talk**, but cannot make or receive calls.
   - **Team lead:** A team lead is a voice admin who can also make or receive calls.
   - **Agent:** The agent will be the role you'll typically give. Agents can make or receive calls only.

   The voice admin role does not consume a seat when used in conjunction with a free Support seat such as Contributor or Light agent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_role_update.png)
5. When you are finished, click **Save**.

The agent now has access to voice with the permissions you configured.

## Giving access to voice (Enterprise plans)

If you're on an Enterprise plan, you can use [custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) to more efficiently configure access to voice settings and the [Talk dashboard](https://support.zendesk.com/hc/en-us/articles/4408831823514) by role, insead of by individual user.
Support admins can manage voice settings and view the dashboard, regardless of their voice role.

**To manage access to voice (Enterprise plans)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Hover over the role for which you want to configure access, click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)), and select **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/roles_view_edit3.png)

   A detailed view of the custom role's settings is displayed. A list of users assigned to the role is also visible in a panel on the right.
3. Configure the following settings as required:
   - **Manage channels and extensions:** Turn on this setting to let users assigned to this role [manage Talk settings](https://support.zendesk.com/hc/en-us/articles/4408838035866). When this setting is turned on and omnichannel routing is turned off, agents can change the status of other agents from the Talk dashboard."
   - **View Talk dashboard:** Turn on this setting to let users assigned to this role view the [Talk dashboard](https://support.zendesk.com/hc/en-us/articles/4408831823514).
4. When you're finished, click **Save**.
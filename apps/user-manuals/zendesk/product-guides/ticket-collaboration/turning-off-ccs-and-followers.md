# Turning off CCs and followers

Source: https://support.zendesk.com/hc/en-us/articles/4408834737434-Turning-off-CCs-and-followers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets >
Settings

In some rare cases, you may decide to turn off CCs and followers in your account.

This article covers the following topics:

- [Turning off CCs and followers](#topic_isl_bfp_gfb)
- [Rolling back CCs and followers](#topic_lnx_s2p_gfb) (for accounts created *before* May 2019 that migrated to the updated CCs and followers experience)

## Turning off CCs and followers

When you turn off CCs or followers, the settings and permissions associated with each feature are also turned off but saved in case you turn them back on. For example, if you modified the follower email template or created a blocklist, the values in those fields will be available if you turn these features back on.

**To turn off CCs and followers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs and followers on tickets** to expand it.
3. Uncheck the **Allow followers** or **Allow CCs** checkboxes.
4. Click **Save**.
5. Refresh your browser and open a few tickets to verify that the **Follower** field in the sidebar and the **CC** link in the comment header have been removed.

## Rolling back CCs and followers

If your account was created *before* May 2019 and migrated to the updated CCs and followers experience, you can roll back to the previous CCs experience if you don't want to use the updated CCs and followers experience.

If you don't see the rollback options described in this section, it means you aren't allowed to roll back the updated CCs and followers experience. However, you can [turn off CCs and followers](#topic_isl_bfp_gfb).

### Rolling back your account

See [About migrating to CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408839371418#topic_gsd_sns_y2b) to learn more about the previous experience you'll be rolling back to.

Note: If you migrate to the new CCs and followers experience and then roll back to the old CCs experience, any actions that used to be **Email user + (requester)** remain as **Email user + (requester and CCs)**. *However, the trigger’s old behavior is restored, meaning that only the requester is emailed.* Don’t forget to manually [roll back your business rules](https://support.zendesk.com/hc/en-us/articles/4408834737434#topic_isl_bfp_gfb), which includes changing the **Email user + (requester and CCs)** action back to **Email user + (requester)**.

**To roll back CCs and followers**:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs and followers on tickets** to expand it.
3. In **Opting out of the CCs and followers experience**, click **Opt out**.

   A confirmation message appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_followers_opt_out2A.png)
4. Click **Yes, opt out** to confirm.
5. After a few minutes, refresh your browser and open a few of your tickets to verify that the **Follower** field in the sidebar has been replaced by a **CCs** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_before.png)

### Rolling back business rules

After you roll back your account, you’ll need to manually roll back your triggers, macros, and automations to remove settings for CCs and followers. There’s no migration wizard for this.

**To manually roll back triggers, macros, and automations**

1. As a guide to rolling back business rules, refer to the affected rules list for your account.

   This is the list you downloaded when you [migrated to CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408839371418--Draft-Migrating-to-CCs-and-followers).
2. Roll back your business rules.
   - To roll back triggers:

     In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
     **Objects and rules** in the sidebar, then select **Business rules >
     Triggers**.

     Trigger [revision history](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_syw_z14_lbb) may be useful.
   - To roll back macros:

     In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
     **Workspaces** in the sidebar, then select **Agent tools > Macros**.
   - To roll back automations:

     In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
     **Objects and rules** in the sidebar, then select **Business rules >
     Automations**.
3. Change the rules back to their original settings. For example, change **Email user: (requester and CC)** back to **Email user: (requester)**.
4. When you’ve finished making updates, save your changes.
5. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
6. Click **CCs** to expand it.
7. Restore your **CC** email template. When you roll back, the **CC** email template replaces the **Follower** email template.
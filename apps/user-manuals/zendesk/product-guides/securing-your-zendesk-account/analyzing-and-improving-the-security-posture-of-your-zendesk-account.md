# Analyzing and improving the security posture of your Zendesk account

Source: https://support.zendesk.com/hc/en-us/articles/9774890665370-Analyzing-and-improving-the-security-posture-of-your-Zendesk-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Access the Security overview page to manage your account's security settings and assess your security health. Review critical and recommended security ratings to identify potential vulnerabilities. Expand sections to view detailed recommendations and take action to enhance your security posture. Remember, these recommendations are general best practices, and you should tailor controls to fit your organization's needs.

Location:  Admin Center > Account > Security > Overview

The Security overview page in Admin Center serves as a centralized location for
managing your account's security-related settings and provides insight into which
features are enabled in your account.

This article includes these sections:

- [Opening the Security overview page](#topic_ypj_y3f_p2c)
- [Viewing the overall security health of your account](#topic_uh4_dhk_vgc)
- [Reviewing Zendesk recommendations and updating your configuration](#topic_krm_gvl_vgc)

Related articles:

- [General security best practices](https://support.zendesk.com/hc/en-us/articles/4408888782618)

## Opening the Security overview page

You must be an admin to access the Security overview page.

**To open the Security overview page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
  **Account** in the sidebar, then select **Security > Security overview**.

The Security overview page opens. This page includes separate sections to help you
view and manage the security features available in your account. Only the security
settings related to your account plan are displayed.

## Viewing the overall security health of your account

The panels at the top of the Security overview page provide a high-level dashboard of
your account's security health.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_dashboard_overview.png)

Use the table below to understand the different security ratings in the
dashboard.

| Security rating | Description |
| --- | --- |
| Critical () | Security settings rated as critical require your immediate review. Your current configuration for these settings could compromise the overall security of your account. |
| Recommended () | We recommend you review these settings and determine if they are appropriately set for your use of Zendesk. These settings may be introducing additional exposure to attacks, and adjusting them may reduce this exposure. |
| Healthy | Healthy settings adhere to Zendesk's general recommendations. No action or changes are required. |
| Unavailable | Zendesk couldn't retrieve data for the setting. This can occur for several reasons, such as the API endpoint being inaccessible or the current user not having the necessary privileges to access it. Try refreshing your browser. |

## Reviewing Zendesk recommendations and updating your configuration

On the Security overview page, security settings are organized into expandable
sections by type.

If any settings within the group have a Critical or Recommended status, an icon
displays in the section header.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_dashboard_collapsed.png)

Expand the header to review the details and recommendations.

Important: The recommendations on the Security
overview page reflect general best practices and do not guarantee security. You
are responsible for determining and implementing controls appropriate to your
organization.

**To review ratings and recommendations for security settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Security overview**.
2. Expand a section that displays a Critical (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_critical_icon.png)) or
   Recommended (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_recommended_icon.png))
   rating.
3. Click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png) next to a
   setting, then click **View details**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_dashboard_menu_2.png)
4. In the side panel that appears, review the setting description and Zendesk
   recommendations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_dashboard_side_panel.png)
5. After reviewing the information, take action as needed:
   - To learn more about the setting, click the link to view a Zendesk help
     center article.
   - Click **Go to setting** to review or update the setting in your
     Zendesk account.
   - Click **Close** to close the side panel.
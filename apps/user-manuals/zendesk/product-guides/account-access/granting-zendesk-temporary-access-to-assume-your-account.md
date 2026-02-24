# Granting Zendesk temporary access to assume your account

Source: https://support.zendesk.com/hc/en-us/articles/4408824477082-Granting-Zendesk-temporary-access-to-assume-your-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Account > Security >
Advanced

To help troubleshoot problems, you can allow Zendesk to assume the role of an agent for a
specific amount of time. Allowing Zendesk to access your account as an agent does not affect
your license, or your available agent seats.

Note: Zendesk reserves the right to assume the role of an agent in your account without prior
notice in certain situations. These include emergency situations to prevent serious harm to
you or others, or situations where we suspect that your use or access to the Services is
violating the terms of the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

This article discusses the following topics:

- [Determining when to grant access to your
  account](#topic_p1l_m3y_4cb)
- [Granting access to your
  account](#topic_g22_m3y_4cb)
- [Access to trial accounts](#topic_tjz_wlc_sjb)

Related articles:

- [General security best practices](https://support.zendesk.com/hc/en-us/articles/4408888782618-Security-best-practices)

## Determining when to grant access to your account

You may want to grant access to Zendesk Support agents when you’re facing an issue that is
too complex to be understood when the agent has read-only access to your account.

Some common examples include:

- Highly-technical issues that need to be escalated through multiple levels
  of support.
- Replication of your issue cannot be reproduced anywhere else.
- Visual analysis of console information is needed, and is not obtainable
  via any other method.
- Your IP configuration is incorrect.
- You need test tickets created so you can test or troubleshoot issues.

## Granting access to your account

The account assumption setting is part of your security properties in [Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554). This setting is turned off by default and
can be turned on by Support and Chat admins. For example, if you are an agent in Support but
an administrator in Analytics, you cannot turn on this option. You can grant access to your
account for a set period of time, or indefinitely, and can turn it off at any time.

**To grant Zendesk access to your account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. On the **Account assumption** tab, select **Enable account assumption**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_security_account_assumption2.png)
3. Use the **Duration** drop-down menu to choose how long Zendesk can access your
   account (One day, One week, One month, One year, or Indefinitely).

   Access from
   Zendesk is disabled automatically after this period of time; however, you can update
   the duration to extend (or reduce) access time as needed. If you select
   **Indefinitely**, access is granted until you manually disable this setting, or
   select a new access duration.
4. Click **Save**.

## Access to trial accounts

The **Account assumption** tab in Admin Center does not show for trial accounts.
Zendesk trial accounts always have account assumption enabled. Only when the trial account
is converted into a paid account will you have the option to choose when Zendesk can assume
into your account.
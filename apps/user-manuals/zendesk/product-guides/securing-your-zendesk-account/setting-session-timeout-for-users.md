# Setting session timeout for users

Source: https://support.zendesk.com/hc/en-us/articles/4408832533274-Setting-session-timeout-for-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Customize session time-out settings to enhance security by automatically signing out inactive users. This helps prevent unauthorized access while ensuring active users remain signed in.

Location: 
Admin Center > Account > Security >
Advanced

Like most applications, Zendesk implements a session expiration to enhance
security.
Signing users out after a period of inactivity reduces the risk of unauthorized
access.
Admins can customize the session expiration time.

Zendesk recommends setting the shortest duration possible for your organization.
Ideally,
use the default settings, 60 minutes for agents and eight hours for end
users, or set
shorter sessions, if possible. Shorter session expiration windows reduce
the amount of
time for a potential session takeover, but does require users to reauthenticate
more
often.

This article includes the following topics:

- [Understanding Zendesk session time](#topic_oky_wry_kbc)
- [Customizing the inactivity session time-out period](#topic_i25_yry_kbc)

## Understanding Zendesk session time

When users sign in to Zendesk, their session remains valid as long
as user activity
occurs, unless the user explicitly signs out of Zendesk. By default,
a session
expires after 60 minutes of inactivity for agents and after eight
hours of
inactivity for end users.

- **User activity** is when you click
  something explicitly in the Zendesk user
  interface or when the application pulls information automatically
  in the
  background. Information pulls often happen to keep the Zendesk
  interface up to
  date, but pulls don't occur uniformly across all Zendesk pages.
- **Session expiration countdown** starts
  when you close your browser or quit
  the browser tab where the Zendesk session is running. The countdown
  can also be
  triggered when you put your computer to sleep or turn it off.
  When the session
  expiration limit is reached, Zendesk terminates your sign-in
  session, and you
  have to sign in again to use Zendesk.

There are other technical differences and edge cases, but the main
idea is that if a
user is active, they will never be signed out. If they are inactive,
the session
will last eight hours by default.

## Customizing the inactivity session time-out period

Admins can customize the session expiration period. If your security
requirements
differ for team members and end users, you can set separate expiration
periods for
each.

By default, agents are signed out after 60 minutes, and end users
are signed out
after eight hours. Zendesk recommends setting the shortest duration
possible for
your organization.

**To set an inactivity session time-out period**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. Click the **Authentication** tab.
3. Select a
   **Team member session expiration period**
   and an
   **End user session
   expiration period**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_sessionexpiration.png)
4. Click **Save**.
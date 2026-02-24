# Tracking agent time spent outside of Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/6676772528026-Tracking-agent-time-spent-outside-of-Zendesk

---

Zendesk WFM admins can track how agents spend time outside of Zendesk by using the Zendesk time tracker Google Chrome extension. Configure extension tracking by mappinggeneral tasksto URLs that agents visit. By mapping general tasks to URLs, you can understand how agents are working and choose how the activity is recorded when agents visit one of your mapped URLs.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Track agent time spent outside the platform using the time tracker Chrome extension. Configure it by mapping general tasks to URLs, allowing you to monitor agent activities. Agents can install the extension to see tracked activities on visited URLs. Admins can manage settings to auto-track or handle unmapped URLs, enhancing visibility into agent time management.

Zendesk WFM admins can track how agents spend time outside of Zendesk by using the
Zendesk time tracker Google Chrome extension. Configure extension tracking by mapping
[general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) to URLs that agents visit. By
mapping general tasks to URLs, you can understand how agents are working and choose how
the activity is recorded when agents visit one of your mapped URLs.

After you set up extension tracking and agents install and sign in to the extension, they
can see which activity is being tracked on the URLs they visit. This helps them better
understand how their time is tracked.

Agents can install the [Zendesk time tracker extension](https://chromewebstore.google.com/detail/zendesk-time-tracker/bccgcacpbhfoocnlbdkhccbiklgckpon?pli=1) from the Google
Chrome web store. They must sign in to the extension after installation, and we
recommend selecting *Keep me signed in* to ensure that they stay logged in even
after closing their browser.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_chrome_time_tracker_agent_sign_in.png)

After you set up extension tracking and agents install the extension, they can
see which activities are being tracked on the URLs they visit. This helps them better
understand how their time is tracked.

This article contains the following topics:

- [Configuring extension tracking](#topic_mpd_kqy_vfc)
- [Configuring extension tracking settings](#topic_jtj_p3z_vfc)

## Configuring extension tracking

To configure extension tracking, you must first define [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) to track agent activities or tasks that
occur outside of Zendesk, or [map unified agent statuses in WFM](https://support.zendesk.com/hc/en-us/articles/10117789027610).

You must be a Zendesk WFM admin to configure extension tracking.

**To configure extension tracking**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Extension tracking**.

   The Extension tracking page is displayed showing any URLs that have
   been configured for general tasks or agent statuses.

   Tip: If you've configured a large number of URLs, use the search
   box to show only the URLs you want. You can also click the filter to
   show only the URLs assigned to a specific general task or agent
   status.
2. Click **Map URLs**, then select one general task or agent status for all
   URLs. Each general task or status can have up to 25 URLs mapped to it.

   For
   example, you might want to add *https://www.youtube.com/* to your
   "Lunch" general task. Every time an agent visits YouTube, their time will be
   tracked as lunch.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_ext_2.png)
3. (Optional) If you entered multiple URLs, click **Next** to confirm that each
   URL is mapped to the correct general task or status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_map_urls_confirm.png)
4. When you've finished entering URLs, click **Map URLs**.

Now, when agents visit a website with a mapped URL, they can click the WFM icon to
see the general task or agent status associated with the time they spend on that
page. This will automatically continue until the agent signs out of Zendesk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_ext_4.png)

If agents sign out or their [session expires](https://support.zendesk.com/hc/en-us/articles/4408832533274), tracking pauses until they sign back
in.

Tip: Closing tabs doesn’t sign agents out. If an agent closes their tabs and
browser without logging out of Zendesk, the extension continues to track them if
they navigate to a mapped URL. [Create an automation](https://support.zendesk.com/hc/en-us/articles/6443374423066) to notify you when an agent remains
clocked into a task or status longer than expected, allowing you to review and
correct the entry.

## Configuring extension tracking settings

You can configure various settings that control how extension manager works. These
settings only affect team members with the Zendesk time tracker extension installed
in their browser.

**To configure extension tracking settings**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Extension tracking**.
2. Click **Manage settings**.
3. Configure the following options as required:
   - **Auto tracking:** Select this option to automatically track your
     team member's browser activity while the user is signed in to
     Zendesk.
   - **Unmapped URLs**: Configure how extension tracking will work for
     URLs that are not assigned to a task. Choose from:
     - **Don't track with extension:** (Default) Don't track any
       time spent browsing unmapped URLs.
     - **Track as specific general task or agent status:** From the
       dropdown list, select the general task or agent status that any
       unmapped URLs will be assigned to.
     - **Track as untracked:** Track any time spent browsing
       unmapped URLs and label this time as untracked.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_ext_3.png)
4. Click **Save**.